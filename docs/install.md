# Setup Guide — Starting from Scratch

This guide takes about 15 minutes. By the end, you'll have a working second brain.

## What You Need

| Tool | What it does | Cost |
|------|-------------|------|
| [VS Code](https://code.visualstudio.com/) | Where you work with Claude | Free |
| [Claude Code](https://docs.anthropic.com/en/docs/claude-code) | Claude running in VS Code | Part of your Claude plan |
| [Obsidian](https://obsidian.md/) | Where you browse your vault | Free |
| A Claude plan (Pro, Max, or Team) | Powers everything | Your existing plan |

**You do NOT need an API key.** This runs entirely on your existing Claude subscription.

## Step 1 — Get the template

**Option A (easiest):** Go to the GitHub page, click **Code → Download ZIP**. Extract it somewhere on your computer. Rename the folder to something meaningful (like `my-brain` or `my-business-vault`).

**Option B (advanced — only if you already use git):**
```
git clone https://github.com/seanmccloskey10-cell/claude-second-brain my-brain
```

## Step 2 — Open it in VS Code

Open VS Code. Go to **File → Open Folder** and select the folder you just created.

## Step 3 — Start Claude Code

Open the command panel at the bottom of VS Code (View → Terminal, or press `` Ctrl+` ``). This is where you type commands to talk to Claude.

First, connect VS Code to your Claude account — the same one you use on claude.ai:

```
claude login
```

This links to your existing plan. No API key needed, no extra bill.

Then start Claude:
```
claude
```

Claude reads the `CLAUDE.md` file automatically. It now knows how to work with your vault.

## Step 4 — Tell Claude about your business

Just start talking:

"I want to tell you about my business. Can you interview me and capture everything in my vault?"

Claude will ask about you and your business. Talk to it — voice-transcribe if you can. It'll capture everything into your vault, showing you what it's going to write before making any changes. This is the most important step: getting your business context into the vault.

## Step 5 — Open in Obsidian

Open Obsidian. Choose **"Open folder as vault"** and select the same folder you opened in VS Code.

Now you have two windows into the same brain:
- **VS Code** — where you work with Claude (capture, interview, brief)
- **Obsidian** — where you browse your notes, follow links, see the big picture

## Step 6 — Make the brain follow you everywhere (recommended)

Right now, your vault only works when the vault folder is open. There's a way to make Claude always read your vault, even when you're working on something else.

See [global-instruction-file.md](global-instruction-file.md) for the 2-minute setup.

## Step 7 — Try your first briefing

Back in VS Code, in your vault folder:
```
/brief
```

If you've only just started, the briefing will be short — that's normal. It gets richer every week as you add more.

## What to Do This Week

1. **One thought per day** — just tell Claude what's on your mind (30 seconds, voice-transcribe)
2. **Find one article** relevant to your business. Save it in `raw/`. Tell Claude to process it.
3. **Run `/brief` on Friday.** See what Claude learned.

That's the whole habit. A few minutes per day.

---

## Common Issues

**"claude: command not found"**
Claude Code isn't installed yet. Follow the [install guide](https://docs.anthropic.com/en/docs/claude-code).

**"I see files in VS Code but not in Obsidian"**
Make sure you opened the same folder in both apps. In Obsidian: Open Vault → select the vault folder.

**"Claude isn't reading my vault context"**
Make sure you're in the vault folder when you start Claude Code. Check that `CLAUDE.md` exists in the root of your vault folder.

**"I want to back up my vault"**
Your vault is just files on your computer. You can:
- Copy the folder to an external drive
- Create a private backup on GitHub (ask Claude to help you set this up)
- Use any backup tool you already have

Your data stays on your machine unless you choose to put it somewhere else.
