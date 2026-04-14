# Brief — Weekly Business Briefing

You are generating a weekly briefing for the vault owner. Your job is to read the entire vault, synthesize what's happened, and surface connections and insights the owner might not see on their own.

## What to read (in this order)

1. `README.md` — current priorities
2. `CLAUDE.md` — vault rules
3. `mistakes-made.md` — past errors
4. The pillar file in `pillars/`
5. All pages in `wiki/`
6. All files in `decisions/`
7. The 3 most recent briefings (if any exist)
8. Everything in `raw/` that hasn't been processed yet
9. Everything in `inbox/`

## Briefing structure

Write the briefing to `wiki/briefings/YYYY-MM-DD.md` with this structure:

```markdown
---
title: Weekly Briefing — YYYY-MM-DD
type: briefing
created: YYYY-MM-DD
generated_by: /brief
---

## What's Changed Since Last Time
(New notes, updated pages, decisions made. If first briefing, summarize what's in the vault.)

## What You've Been Thinking About
(3-5 topics with the most activity or movement. Use the owner's own words from Owner's Take sections.)

## Connections Worth Noting
(This is the most important section. Cross-cutting patterns, links between ideas that aren't obvious. "Your frustration with [X] might be related to the approach you described in [Y]." Be specific. Cite the notes.)

## Things to Push Back On
(One or two positions where you think the owner might be wrong or incomplete. Be respectful but honest. Cite evidence.)

## Open Questions
(Pulled from Open Questions sections across notes. Group them if related.)

## Unprocessed Items
(Files sitting in raw/ or inbox/ that haven't been turned into wiki pages yet.)

## Vault Health
(Quick structural audit. Check for:)
- Orphan pages (no inbound links from other notes)
- Non-.md files or unexpected folders at vault root
- Unprocessed raw files (missing `processed: true` in frontmatter)
- Stale projects (status: active but no updates in 14+ days)
- File count sanity (a small vault shouldn't have thousands of files)
- Contradictions between pages
- Claims without source attribution (a wiki page making claims with no `## Sources` section)
- Missing cross-references (wiki pages that mention a concept but don't link to the relevant page)
(If everything is clean, say so in one line. Only detail problems.)

## One Thing to Do This Week
(A single, concrete suggestion. Not a to-do list. One thing.)
```

## Rules

- **Never overwrite a previous briefing.** Each one is a new file with today's date.
- **Cite every claim** with links: `[[wiki/page-name]]`
- **Use the owner's actual words** from Owner's Take sections when possible.
- **Keep it to a 5-minute read.** Be concise.
- **Never invent data.** If the vault doesn't say it, you don't know it.
- **Be a friend who pushes back**, not a yes-man. If something doesn't add up, say so.

## Special case: almost-empty vault

If the vault has fewer than 5 wiki pages, write a short briefing that:
1. Summarizes what's there
2. Suggests what to capture next (based on gaps you see)
3. Encourages them: "Tell me a few thoughts about your business this week, and next week's briefing will have much more to work with."

## After writing

Append to `log.md`: `## [YYYY-MM-DD] lint | Weekly briefing`

Tell the owner:
- Where you saved the briefing
- The top 2-3 things you think they should pay attention to
- Ask: "Anything in here that surprised you?"
