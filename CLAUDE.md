# Vault Instruction File

This file tells Claude how to work with your vault. Claude reads it automatically at the start of every session.

## What This Vault Is

A personal second brain for one person and their business. It stores context, decisions, knowledge, and lessons so that Claude has memory across sessions. The vault is the source of truth.

## Session Start — What to Read First

Every session, before responding, read these files in order:

1. `README.md` — current priorities and what's active
2. This file (`CLAUDE.md`) — how to work with the vault
3. `mistakes-made.md` — past errors, so you don't repeat them
4. The pillar file in `pillars/` — the owner's business context

Do not announce that you've read them. Just use the context naturally.

## Folder Map

| Folder | What goes here |
|--------|---------------|
| `pillars/` | The owner's business — one file per major life area (start with one) |
| `raw/` | Original sources — PDFs, articles, posts. Never edit these. |
| `wiki/` | Synthesized knowledge — Claude turns raw sources into useful pages here |
| `inbox/` | Quick capture — thoughts, ideas, anything not yet sorted |
| `decisions/` | Business decisions with context, so future-you knows why |
| `docs/` | Setup guides and reference (for the owner, not for Claude) |

## File Conventions

### The info block at the top of each file
Every file starts with a block like this:
```yaml
---
title: Short descriptive name
type: pillar | wiki | decision | inbox
status: active | dormant | archived
created: 2026-04-14
updated: 2026-04-14
tags: [relevant, tags]
---
```

### Naming
- Lowercase with dashes: `client-retention.md`, not `ClientRetention.md`
- Dates in ISO format: `2026-04-14`
- One concept per file — if a file covers two topics, split it

### Links between notes
- Use `[[double brackets]]` to link notes: `[[pillars/my-business]]`
- Every note should link to at least one other note
- A note without links is a bug — always connect it to something

## How to Behave

### Do
- Read relevant vault files before answering questions
- Cite which vault file informed your answer
- Append to existing notes rather than replacing content
- Preserve the owner's exact words in "Owner's Take" sections
- Flag contradictions: old claim vs. new information
- Push back when the owner is making a mistake
- Be concise — bullets over paragraphs

### Don't
- Overwrite the owner's words or paraphrase their voice
- Invent facts or data not in the vault
- Delete files without explicit permission
- Store passwords, API keys, tokens, or credentials — write "stored in [location]" instead
- Store sensitive personal information about clients or customers
- Add content without showing the owner first

## Staleness Check

Look at the `Focus updated:` date in README.md. If it's more than 7 days old, ask the owner to update their current priorities before doing anything else. Stale context means wrong advice.

## Slash Commands

This vault has four commands in `.claude/commands/`:

| Command | What it does |
|---------|-------------|
| `/interview` | Structured conversation to capture business knowledge |
| `/brief` | Weekly briefing — synthesizes what's changed and what to focus on |
| `/add-note` | Quick capture of a single thought |
| `/ingest` | Turn a raw source (article, post) into a wiki page |

## Session End

When a meaningful session ends:
1. Summarize what was done
2. Update the `Focus updated:` date in README.md
3. Ask if any decisions should be logged in `decisions/`
4. Ask if Claude made any mistakes worth adding to `mistakes-made.md`
