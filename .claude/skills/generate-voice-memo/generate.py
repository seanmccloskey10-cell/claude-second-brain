#!/usr/bin/env python3
"""Generate an ElevenLabs MP3 of a weekly briefing's "Voice memo script" section.

Optional skill — only runs if Eleven_Labs is set in .env at the vault root.
The vault works perfectly without it.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

DEFAULT_VOICE_ID = "xQoJctkjLbN6MAa5Ibhk"  # British female narrator, stable on long-form
MODEL_ID = "eleven_multilingual_v2"
API_BASE = "https://api.elevenlabs.io/v1/text-to-speech"
ENV_KEY = "Eleven_Labs"

# 7-min cap at ~150 wpm ≈ 1050 words ≈ ~5500 chars.
SANITY_CAP = 5500

# Pronunciation overrides — applied AFTER markdown stripping, BEFORE the API call.
# ElevenLabs tries to pronounce short all-caps initialisms as words; spell them out.
INITIALISM_REPLACEMENTS = {
    "TL;DR": "T L D R",
    "LLM": "L L M",
    "LLMs": "L L Ms",
    "API": "A P I",
    "APIs": "A P Is",
    "CLI": "C L I",
    "MCP": "M C P",
    "MVP": "M V P",
    "PRD": "P R D",
    "ADR": "A D R",
    "RAG": "R A G",
    "RLHF": "R L H F",
    "SFT": "S F T",
    "CLAUDE.md": "Claude dot M D",
    "README.md": "Read me dot M D",
}


def find_vault_root(memo_path: Path) -> Path:
    """Walk up from memo_path looking for a vault marker (CLAUDE.md + README.md)."""
    current = memo_path.resolve().parent
    while current != current.parent:
        if (current / "CLAUDE.md").exists() and (current / "README.md").exists():
            return current
        current = current.parent
    sys.exit(f"ERROR: could not locate vault root from {memo_path}")


def load_api_key(env_path: Path) -> str:
    if not env_path.exists():
        sys.exit(
            f"ERROR: .env not found at {env_path}\n"
            f"Copy .env.example to .env, then fill in your ElevenLabs key.\n"
            f"Get a free key at https://elevenlabs.io (no credit card needed).\n"
            f"The .env file is gitignored — it never leaves your machine."
        )
    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line.startswith(f"{ENV_KEY}="):
            value = line.split("=", 1)[1].strip().strip('"').strip("'")
            if not value or value == "your-elevenlabs-key-here":
                sys.exit(
                    f"ERROR: {ENV_KEY}= is empty or still the placeholder in {env_path}.\n"
                    f"Replace the placeholder with your actual ElevenLabs key."
                )
            return value
    sys.exit(
        f"ERROR: {ENV_KEY}= not found in {env_path}\n"
        f"Add a line: {ENV_KEY}=your-actual-key"
    )


def extract_text(memo_path: Path) -> str:
    raw = memo_path.read_text(encoding="utf-8")
    body = re.sub(r"\A---\n.*?\n---\n", "", raw, count=1, flags=re.DOTALL)

    match = re.search(
        r"^## Voice memo script[^\n]*\n(.*?)(?=^## (?!#)|\Z)",
        body, re.DOTALL | re.MULTILINE,
    )
    if not match:
        sys.exit(
            "ERROR: '## Voice memo script' section not found in briefing.\n"
            "This section should be the last part of the briefing, written for\n"
            "the narrator to read aloud. Check .claude/commands/brief.md — /brief\n"
            "should produce this section automatically."
        )
    text = match.group(1)

    # Strip markdown
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = re.sub(r"\*(.+?)\*", r"\1", text)
    text = re.sub(r"\[\[.+?\]\]", "", text)
    text = re.sub(r"\[(.+?)\]\(.+?\)", r"\1", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"^#+\s*", "", text, flags=re.MULTILINE)
    text = re.sub(r"\n{3,}", "\n\n", text)

    # Pronunciation pass — longest-match first
    for term, spoken in INITIALISM_REPLACEMENTS.items():
        text = text.replace(term, spoken)
    # Generic fallback for any remaining @-handles
    text = re.sub(r"@(\w+)", r"the \1 account", text)

    text = text.strip()
    if not text:
        sys.exit(
            "ERROR: extracted Voice memo script is empty after markdown stripping.\n"
            "The section exists but has no readable content."
        )
    return text


def synthesize(text: str, api_key: str, voice_id: str, output_path: Path) -> None:
    url = f"{API_BASE}/{voice_id}"
    payload = json.dumps({
        "text": text,
        "model_id": MODEL_ID,
        "voice_settings": {
            "stability": 0.75,
            "similarity_boost": 0.75,
            "style": 0.0,
            "use_speaker_boost": True,
        },
    }).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=payload,
        headers={
            "xi-api-key": api_key,
            "Content-Type": "application/json",
            "Accept": "audio/mpeg",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=90) as resp:
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_bytes(resp.read())
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        sys.exit(f"ERROR: ElevenLabs API returned {e.code}\n{body}")
    except urllib.error.URLError as e:
        sys.exit(f"ERROR: network failure calling ElevenLabs: {e.reason}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("briefing_path", help="Path to briefing .md file")
    parser.add_argument("--voice-id", default=DEFAULT_VOICE_ID,
                        help="ElevenLabs voice ID (default: stable British female narrator)")
    parser.add_argument("--out",
                        help="Output MP3 path (default: <vault>/wiki/briefings/audio/<basename>.mp3)")
    args = parser.parse_args()

    memo_path = Path(args.briefing_path).resolve()
    if not memo_path.exists():
        sys.exit(f"ERROR: briefing not found at {memo_path}")

    vault_root = find_vault_root(memo_path)
    env_path = vault_root / ".env"
    api_key = load_api_key(env_path)

    if args.out:
        output_path = Path(args.out).resolve()
    else:
        output_path = vault_root / "wiki" / "briefings" / "audio" / f"{memo_path.stem}.mp3"

    text = extract_text(memo_path)
    char_count = len(text)

    if char_count > SANITY_CAP:
        print(f"[generate-voice-memo] WARN: char count {char_count} exceeds 7-min cap ({SANITY_CAP} chars).")
        print(f"[generate-voice-memo] WARN: voice memo script is too long. Trim the section.")
        print(f"[generate-voice-memo] WARN: aborting to protect your ElevenLabs free-tier budget.")
        sys.exit(2)

    print(f"[generate-voice-memo] briefing: {memo_path.name}")
    print(f"[generate-voice-memo] voice:    {args.voice_id}")
    print(f"[generate-voice-memo] chars:    {char_count} (free tier: 10,000/mo, 7-min cap: {SANITY_CAP})")
    print(f"[generate-voice-memo] output:   {output_path}")
    print(f"[generate-voice-memo] calling ElevenLabs...")

    synthesize(text, api_key, args.voice_id, output_path)

    size_kb = output_path.stat().st_size // 1024
    print(f"[generate-voice-memo] OK: wrote {size_kb} KB")


if __name__ == "__main__":
    main()
