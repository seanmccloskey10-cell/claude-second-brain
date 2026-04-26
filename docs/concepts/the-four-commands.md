# The Four Commands

> **TL;DR:** Four slash commands run the whole vault: `/setup` (once, at the start), `/hello` (at session start), `/goodbye` (at session end), `/brief` (weekly, often automatic). Two more — `/ingest` and `/check` — handle articles and sanity-checks. You don't need to memorize any of them. Talk to Claude in plain English; it'll suggest the right command if it helps.

## The four you'll actually use

### `/setup` — once, at the very start

The first-run wizard. Interviews you about your business, customizes your README, creates your first pillar file, and offers to set up the global instruction file (so Claude knows about your vault from any folder, not just the vault folder).

Takes 5–10 minutes. You only run it once.

### `/hello` — at the start of each session

Reads your README, your CLAUDE.md, your most recent session notes, and the current state of your vault. Briefs you in 6–8 lines: what you've been working on, what's open, what's worth focusing on today.

This is the "Claude already knows me" moment. After a few weeks, the briefings get sharp.

### `/goodbye` — at the end of meaningful sessions

Reviews what changed during the session. Writes a session note appended to `SESSION-NOTES.md`. Names what's incomplete or worth carrying forward. Gives the next `/hello` something concrete to load.

You don't need to run this for short sessions where nothing changed. Run it when real work happened.

### `/brief` — weekly, often automatic

A full vault review. Reads your pillars, wiki, decisions, recent raw items, and inbox. Surfaces:

- What's changed since last time
- Topics with the most movement
- Connections between ideas you might not see yourself
- One or two pushbacks (where Claude thinks you might be wrong)
- Open questions, unprocessed items
- Vault health (orphan pages, stale projects, anything weird)
- One thing to focus on this week
- An optional voice memo script (turned into MP3 audio if you've set up the [ElevenLabs key](voice-briefings.md))

CLAUDE.md instructs Claude to fire `/brief` automatically if 7+ days have passed since the last one. You can also trigger it yourself anytime.

## The two extras

### `/ingest` — when you share an article, post, or PDF

Reads the source fully. Compares it against your existing wiki to check for novelty. Saves the original to `raw/` (with frontmatter). Synthesizes it into wiki pages. Updates `wiki/index.md`. Flags contradictions with anything you've previously captured. Marks the raw file as `processed: true`.

This is the [Karpathy raw → wiki pipeline](folder-grammar.md). It's how reading-time becomes vault-time.

### `/check` — when something feels wrong

A read-only sanity scan. Verifies your README has been customized (no template placeholders left), your pillar file exists, the global instruction file is in place if you set it up, all commands are present, and the web-clipper templates haven't drifted. Returns a green/yellow/red report.

Run it when something doesn't feel right, or after a big change.

## You don't need to memorize these

The vault's CLAUDE.md tells Claude when each command applies. So if you say *"I want to wrap up for tonight"*, Claude will offer to run `/goodbye` for you. If you say *"I read this article — process it"*, Claude will run `/ingest`.

The commands are scaffolding. Plain English to Claude is the actual interface.

## Cross-references

- [Three layers of memory](three-layers-of-memory.md) — why these commands exist
- [Folder grammar](folder-grammar.md) — where each command writes
- [Voice briefings](voice-briefings.md) — the optional audio version of `/brief`
- [Capacity and compaction](capacity-and-compaction.md) — why `/hello` and `/goodbye` matter even within a single project
