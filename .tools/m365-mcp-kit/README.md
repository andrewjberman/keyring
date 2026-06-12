# M365 MCP Kit

A drop-in kit that connects **Claude Code** to your Microsoft 365 account (Outlook,
OneDrive, SharePoint) through the [Lokka](https://github.com/merill/lokka) Microsoft
Graph MCP server, with ready-made `/outlook`, `/onedrive`, and `/sharepoint` skills.

## What you get

- Ask Claude about **your own** email, files, and SharePoint sites in natural language.
- Everything is **individual-scoped**: you sign in as yourself, and Claude can only see
  what *you* can already see in Outlook/OneDrive/SharePoint. There is no shared service
  account and no access to anyone else's mailbox.
- `/outlook`, `/onedrive`, `/sharepoint` slash-skills that bake in the right Microsoft
  Graph calls so the common asks "just work."

## How to install (the easy way)

1. Copy this whole folder to your machine.
2. Open it in Claude Code (PowerShell):  `cd m365-mcp-kit ; claude`
3. Tell Claude:  **"Read BOOTSTRAP.md and set this up for me."**
4. Follow the one browser sign-in prompt with your **work** account.

That's it. The agent verifies prerequisites, registers the MCP server, installs the
skills, and runs a test query.

## Prerequisites

- **Claude Code** (you're using it).
- **Node.js LTS** (provides `npx`, which runs Lokka). The bootstrap checks for this and
  tells you how to install it if missing.
- A **Claude for Work / Enterprise** account on your company tenant. *(This matters:
  email and file content is sent to the model to answer your question. Your org's Claude
  commercial terms — no training on your data, controlled retention — are what make that
  acceptable. Andrew handles this org-wide; you don't configure it per-person.)*

## What the agent that owns this app registration looks like

One single-tenant Microsoft Entra app, configured as a public/native client, with
**delegated** Graph permissions and admin consent. The `TENANT_ID` and `CLIENT_ID` in
`.mcp.json` are the same for everyone in the company and are **not secrets** — there is
no client secret in this flow.

## Files

| File | Purpose |
|---|---|
| `BOOTSTRAP.md` | Setup runbook your Claude Code agent executes. |
| `.mcp.json` | The Lokka MCP server config (project-scoped). |
| `.claude/skills/outlook/SKILL.md` | Email skill. |
| `.claude/skills/onedrive/SKILL.md` | OneDrive skill. |
| `.claude/skills/sharepoint/SKILL.md` | SharePoint skill. |

## Safety note

The send-email and write-file skills **draft first and require your confirmation** before
anything leaves your account. Don't remove that guard.
