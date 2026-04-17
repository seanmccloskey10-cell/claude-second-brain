# /setup — First-Run Wizard for Your Second Brain

You are walking the owner through their first-run setup. They just cloned this repo and this is their first time opening it. Be warm, patient, beginner-safe. Use plain language. No jargon.

## Step 1 — Confirm the right folder

Read CLAUDE.md and README.md to confirm you're in a fresh second-brain vault. If either file is missing, stop and tell the owner:

> "It looks like this folder isn't a vault. Make sure you've opened the cloned 'claude-second-brain' folder (the one with CLAUDE.md and README.md inside it), then try /setup again."

If both files are there, proceed.

## Step 1.5 — Has /setup been run before?

Before greeting, check if the vault has already been customized. Signals that it HAS been run:
- README.md "Your Vault Right Now" section does NOT contain `_(run /setup)_` or `YYYY-MM-DD` placeholders
- `pillars/` contains a non-template file (anything other than `_TEMPLATE.md`)

If the vault is already customized, do NOT proceed silently. Ask the owner:

> "Looks like /setup has already run on this vault. Want to:
> 1. **Redo it from scratch** — I'll re-interview you and overwrite the customizations (your raw/, wiki/, decisions/, inbox/ content stays untouched)
> 2. **Update specific things** — tell me what you want to change (e.g., 'update my pillar', 'rerun the global file step')
> 3. **Skip** — exit /setup and continue with what you have"

Wait for their answer. If (1), proceed to Step 2 with a clear "I'll overwrite the README and create a new pillar" warning. If (2), ask what they want to update and skip to that step. If (3), exit cleanly.

If the vault is fresh (placeholders still in README, only `_TEMPLATE.md` in pillars/), skip this step and proceed to Step 2.

## Step 2 — Greet and explain

Greet the owner warmly:

> "Welcome! Let's get your second brain set up. This will take about 5-10 minutes. I'll ask you a few questions about you and your business, then I'll customize this vault for you. I'll show you every change before I make it — nothing happens without your okay."

## Step 3 — Interview

Ask these questions ONE AT A TIME. Wait for each answer before asking the next.

1. "What's your name?"
2. "In one sentence, what does your business do?"
3. "Who's your customer?"
4. "What's the single biggest thing you want to use this second brain for? For example: remembering customer conversations, organizing your thinking, processing articles you read, planning marketing."
5. "If everything went well, where do you want this business to be in 12 months?"

After each answer, briefly reflect what you heard so they know you got it right. Don't lecture — just confirm.

## Step 4 — Customize the README

Update the "Your Vault Right Now" section in README.md with their actual data:
- Replace `**Focus updated:** _(run /setup)_` with today's date
- Replace `**Current priorities:**` placeholder with 1-3 priorities you can pull from their answers (especially answer 4)
- Replace `**Your pillar:**` placeholder with a wikilink to the pillar file you'll create in Step 5

Show the owner the new section before writing. Get explicit approval ("yes" or similar) before writing.

## Step 5 — Create their first pillar file

Decide on a pillar slug from their business name. Use lowercase-with-dashes (e.g., `yan-tutoring`, `speechway`, `joe-coaching`). Show the slug to the owner first and ask: "I'm going to create your pillar file at `pillars/[slug].md`. Does that look right, or want to call it something else?"

Once confirmed, create `pillars/[slug].md` based on `pillars/_TEMPLATE.md`. Fill in:
- `title:` — their business name
- `created:` and `updated:` — today's date
- "What This Is" section — based on answers 2 and 3
- "North Star" section — based on answer 5
- "Current State" section — one line: "Just getting started — vault initialized [today's date]"

Leave the other sections (What's Working, What's Not Working, Active Work, Open Questions, Key Decisions, Owner's Take) as empty placeholders for them to fill in over time.

Show the file before writing. Get approval.

After writing, update the README's `**Your pillar:**` line to point at the actual file you just created.

## Step 6 — Offer to set up the global instruction file

Tell the owner:

> "There's one more thing worth doing. Right now this vault only works when this folder is open in VS Code. There's a way to make Claude read your vault from ANY folder on your computer — so when you're working on something else, Claude still knows about your business. It takes 30 seconds and I can do it for you. Want to set it up?"

If yes:
1. Detect the operating system. On Windows the path is `C:\Users\[username]\.claude\CLAUDE.md`. On Mac/Linux it's `~/.claude/CLAUDE.md`. The username can be derived from the home directory.
2. Read `docs/global-instruction-file.md` for the template.
3. Fill the template with:
   - Their vault path (the folder you're currently in — use the absolute path)
   - Their name and one-line business description from the interview
4. Show the file before writing. Get approval.
5. After creating the file, tell them: "Quit VS Code completely and reopen it for the global file to take effect. Then test it: open any other folder, start Claude Code, and ask 'what do you know about my business?' If I describe your business, the brain is following you everywhere."

If they say no, tell them: "No problem. Whenever you're ready, just ask me to set up the global instruction file, or follow `docs/global-instruction-file.md`."

## Step 7 — Web Clipper offer (optional)

Ask: "There's a free Chrome extension that lets you save articles, X posts, and YouTube videos into your vault with one click. Want me to walk you through setting it up now, or save it for later?"

If now: read `docs/web-clipper/setup.md` and walk them through it one step at a time.
If later: tell them they can open `docs/web-clipper/setup.md` whenever they're ready (or just ask you to walk them through it).

## Step 8 — Close

Briefly explain the daily commands:

> "You're all set up. Here are the four commands worth knowing:
>
> - **/hello** — run at the start of every session. I'll read your vault and brief you on where you are.
> - **/goodbye** — run at the end of every session. I'll write session notes for next time.
> - **/brief** — runs once a week (I'll do this automatically — you don't have to remember). It's a deep review of your vault with one thing for you to focus on that week.
>
> For everything else, just talk to me naturally. Tell me a thought, share an article, ask a question. I'll figure out where things go.
>
> Try saying `/hello` right now to see how it works."

## Rules

- Show every change before writing. Always. Get explicit approval before each write.
- One question at a time. Never batch questions.
- Plain language. No jargon. Avoid "frontmatter", "wikilinks", "schema", "YAML", "markdown".
- If the owner stalls or seems confused, slow down. Re-explain in different words.
- Never lecture. Be a friend, not a tutorial.
- If they want to skip a step, let them. Note that they can come back to it later.
- If something fails, tell them what failed and what to try, then stop. Don't push forward through errors.
