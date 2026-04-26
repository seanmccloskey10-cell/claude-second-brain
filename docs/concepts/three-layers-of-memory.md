# Three Layers of Memory — Boat, Island, Continent

> **TL;DR:** Claude's memory comes in three layers: a single chat (boat — sinks every time), a single project (island — survives across its sessions), and a whole life (continent — survives across all your projects). This template is the continent. Knowing which layer you're on tells you what's possible and what's not.

## The metaphor

Every conversation with Claude is taking place on one of three surfaces:

| Layer | What it is | What persists | What dies |
|---|---|---|---|
| **🚤 Boat** | A single chat — ChatGPT.com, Claude.ai, a fresh Claude Code session with no project | Nothing | Everything, the moment you close the tab |
| **🏝️ Island** | A single project folder with `CLAUDE.md` + a `/hello` `/goodbye` pattern | Your project's history, decisions, state | Anything outside that one project |
| **🌍 Continent** | A vault that spans your whole life or business | Your pillars, decisions, raw sources, synthesized wiki, weekly briefings — across every session, every project | Nothing within scope. The vault is the memory. |

## Why this matters

Most people start on the boat. They open ChatGPT, get a brilliant response, close the tab, and lose it forever. They re-explain their business every time. They make decisions that contradict what they decided last week because last week didn't survive.

The island is a huge upgrade. One project, persistent memory across all its sessions. If you're working on one specific thing — a tutoring business, an equity research habit, a single product — an island is enough. See the [hello-goodbye pattern](https://github.com/seanmccloskey10-cell/claude-second-brain-template/blob/main/docs/concepts/the-four-commands.md) for the simplest island setup.

The continent is when your work spans multiple things, you have cross-cutting knowledge, and you want Claude to *connect* what's happening in pillar A to what you said about pillar B last month. **This template is the continent.**

## Which layer are you on?

- If you only have one thing you care about → **island** is enough. You may not need this template yet.
- If you have multiple pillars, want cross-pillar synthesis, or want a weekly briefing that draws from everywhere → **continent**, you're in the right place.
- If you're not sure → start with one pillar in this template. Add more as your work grows. The continent gracefully starts as a small island.

## What each layer can't do

- **Boat can't:** remember anything. Stop expecting it to.
- **Island can't:** see across projects. If you discover a pricing principle in your tutoring island, it won't show up when you're working in your speech-therapy island. Both are isolated by design.
- **Continent can't:** save you from yourself. The vault only knows what you put in it. Claude won't synthesize what you haven't captured.

## Cross-references

- [The four commands](the-four-commands.md) — how `/setup`, `/hello`, `/goodbye`, `/brief` make the continent work
- [Folder grammar](folder-grammar.md) — what each folder in the vault is for
- [Capacity and compaction](capacity-and-compaction.md) — why even the continent has session-level limits
