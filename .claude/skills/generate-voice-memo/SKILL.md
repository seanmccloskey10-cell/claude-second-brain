---
name: generate-voice-memo
description: Optional. Generate an ElevenLabs MP3 of a weekly briefing's "Voice memo script" section, so the owner can listen on a walk instead of reading. Off by default — only runs if Eleven_Labs key is set in .env. Default voice is a British female narrator; configurable.
---

# generate-voice-memo

Optional skill that turns the weekly briefing into an audio MP3, for owners who'd rather listen than read.

**This skill is OPT-IN.** The vault works perfectly without it. To enable: add `Eleven_Labs=<your-key>` to `.env`. If the key is missing, `/brief` skips the audio step silently.

## When it runs

- **Automatically** at the end of `/brief`, IF an `Eleven_Labs` key is set in `.env`. If the key is missing or empty, `/brief` skips the audio step and tells the owner about the option once (then drops it).
- **On demand** when the owner asks for audio for a specific existing briefing.

## How to invoke manually

From the vault root:

```bash
python .claude/skills/generate-voice-memo/generate.py wiki/briefings/YYYY-MM-DD.md
```

With a different voice:

```bash
python .claude/skills/generate-voice-memo/generate.py wiki/briefings/YYYY-MM-DD.md --voice-id <elevenlabs-voice-id>
```

## What it does

1. Reads the briefing markdown file.
2. Extracts the `## Voice memo script` section (a tighter, audio-friendly version of the full briefing — written by `/brief` specifically for listening).
3. Strips markdown and applies pronunciation overrides for common technical initialisms (LLM, API, CLI, etc.).
4. Calls the ElevenLabs REST API.
5. Writes the MP3 to `wiki/briefings/audio/<basename>.mp3`.

## The "Voice memo script" section

`/brief` writes a dedicated `## Voice memo script` section at the END of each briefing. This section is:

- **5–7 minutes when read aloud** at normal speaking pace (≤ 5500 chars hard cap)
- **Conversational, first-person register** — like a letter from a thoughtful assistant, not a dry executive summary
- **The audio's actual content** — the narrator reads this, not the full briefing

This separation lets the full briefing stay comprehensive (multiple sections, all the detail the owner might want to reference) while the audio stays tight (skimmable for the ear). Think: full doc for the eye, executive summary for the ear.

## Output

- Default path: `wiki/briefings/audio/<briefing-basename>.mp3`
- Override with `--out <path>`

## Voice

Default: **a British female narrator** with stable long-form delivery. Voice ID hardcoded in the script (`xQoJctkjLbN6MAa5Ibhk`).

Voice settings tuned for narration stability:
- `stability: 0.75` — consistent volume and tone across 5+ minute reads
- `use_speaker_boost: true` — reduces drift across long text
- `style: 0.0` — neutral narrator register
- `similarity_boost: 0.75` — standard

To use a different voice, browse the [ElevenLabs voice library](https://elevenlabs.io/voices), copy the voice ID, and pass `--voice-id <id>`.

## API key

Reads `Eleven_Labs=<key>` from `.env` at the vault root. The `.env` is gitignored — it never leaves your machine.

To get a key:
1. Sign up at [elevenlabs.io](https://elevenlabs.io) (free tier, no credit card required).
2. Go to your profile → API Keys → create a new key.
3. Copy `Eleven_Labs=<paste-key-here>` into your vault's `.env` file.

If `.env` doesn't exist yet, copy `.env.example` to `.env` and fill it in.

## Free-tier budget

ElevenLabs free tier = **10,000 characters/month**.

- A weekly briefing's voice memo script is ~3,000–5,500 chars
- That's **2–3 audio briefings per month** on the free tier
- If you want more, Starter is $5/mo (30K chars), Creator is $22/mo (100K chars)

The script prints the character count before each call so you can budget.

## Failure modes

- Missing `.env` or `Eleven_Labs=` line → exits with clear error + create instructions
- Briefing missing `## Voice memo script` section → exits with clear error pointing to `/brief`
- Voice memo script exceeds 7-min cap (5500 chars) → aborts with trim suggestion
- ElevenLabs HTTP error → prints status code + response body, exits non-zero
- Network failure → prints reason, exits non-zero

The script never silently retries. If something fails, you see why.

## Dependencies

Python 3.9+ standard library only. No `pip install` required. Uses `urllib.request`, `json`, `re`, `argparse`, `pathlib` — all built in.

If `python` isn't on your machine: macOS ships with `python3` (run `python3 --version` to check). Windows: `winget install -e --id Python.Python.3.11`.

## What this skill does NOT do

- Does not replace reading the full briefing — the audio is a tighter version, not a complete substitute
- Does not work without an ElevenLabs API key (graceful skip in `/brief`, hard error if invoked manually)
- Does not store the API key anywhere except `.env` (gitignored). The key never leaves your machine.
