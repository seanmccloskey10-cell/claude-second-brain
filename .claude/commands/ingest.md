# Ingest — Turn a Source into Knowledge

You are processing a raw source (article, post, PDF, transcript) and turning it into useful knowledge in the vault's wiki.

## Before you start

1. Read `README.md` and `CLAUDE.md` for vault context
2. Read the pillar file in `pillars/` — you need to know what the owner's business is to judge relevance
3. Check `wiki/` for existing pages that might need updating

## The flow

### Step 1 — Find what to process
Ask: **"What should I process?"**

Or, if they don't specify, scan `raw/` for files that don't have `processed: true` in their info block. List them and ask which one to start with.

### Step 2 — Read the source fully
Read the entire source. Don't skim.

### Step 3 — Extract what matters
Pull out insights that are relevant to the owner's business. Ignore everything else. For each insight, note:
- The key idea
- Why it matters for the owner's specific situation
- Any action it suggests

### Step 4 — Show your work
Before writing, show the owner:
- Which wiki pages you'd create or update
- What you'd add to each one
- Which existing notes this connects to

Say: **"Here's what I'd pull from this. Want to go through it?"**

### Step 5 — Write and link
Once approved:
- Create new wiki pages or update existing ones
- Add `[[links]]` to connect the new knowledge to existing notes
- Add a source citation at the bottom of each wiki page you update:
  ```
  ## Sources
  - [[raw/YYYY-MM-DD-article-name]] — processed YYYY-MM-DD
  ```

### Step 6 — Mark as processed
Add or update the info block in the raw file:
```yaml
processed: true
processed_date: YYYY-MM-DD
```

Tell the owner what you created and what it connects to.

## What NOT to do

- Don't copy the article word-for-word into wiki — synthesize it
- Don't create wiki pages for content that isn't relevant to the owner's business
- Don't create a page for every minor point — group related ideas into one page
- Don't lose the source — always link back to the original in `raw/`

## Good wiki pages look like

```markdown
---
title: Client Retention Strategies
type: wiki
status: active
created: 2026-04-14
updated: 2026-04-14
tags: [clients, retention, business]
---

## What This Is
Strategies for keeping existing clients coming back.

## Key Ideas
- [Insight from the article, in plain language]
- [Another insight, connected to the owner's situation]

## How This Applies to My Business
(Write this from the owner's perspective, based on what you know from the pillar file.)

## Owner's Take
(Empty until the owner adds their thoughts via /add-note or /interview.)

## Open Questions
- [Questions this raises for the owner's specific situation]

## Sources
- [[raw/2026-04-14-retention-article]] — processed 2026-04-14

## Related
- [[wiki/pricing-strategy]]
- [[pillars/my-business]]
```
