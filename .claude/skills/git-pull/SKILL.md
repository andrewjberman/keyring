---
name: git-pull
description: Keep this checkout current with the remote on a cadence: bare `/git-pull` arms a 15-minute in-session Monitor that fetches and fast-forwards (never rebases, never auto-merges), notifying only on an advance or a blocker. `/git-pull 5m|30m|1h|90s`; `/git-pull once`; `/git-pull status`; `/git-pull off`. In-session only (re-arm after a restart). At MSTR launch `/integrate` absorbs this step.
---

# /git-pull — recurring fast-forward pull of the shared checkout

Keeps this workspace's git checkout current with the remote by **re-pulling on a
cadence**. The default is a **15-minute in-session loop**. It is a pure mechanical
puller — it runs as a background **Monitor** (so it costs no agent turns per tick)
and it only ever **fast-forwards**, so an unattended pull can never rebase shared
history or produce a conflict-y auto-merge.

## Why fast-forward-only (read once)

This is a shared, multi-agent branch (`CLOUD` etc.), and this machine is a
**contributor** (agents commit + push from here). The loop uses
`git fetch` + `git merge --ff-only origin/<branch>`, NOT `git pull`:

- **Never rebase.** Rebasing a shared branch rewrites multi-agent history — banned
  by CLAUDE.md NEVER#7 and enforced by `.tools/hooks/never-rules-gate.sh`. `--ff-only`
  cannot rebase.
- **Never a messy merge.** If local has committed work that has diverged from origin,
  `--ff-only` **cleanly refuses** (no data touched) and the loop emits a `BLOCKED`
  event so a human/agent reconciles deliberately (`git pull` merge, then re-push).
  It never silently auto-merges.
- **No-op = silence.** When origin hasn't moved, the loop emits nothing. You are
  notified only on a real fast-forward, a `BLOCKED` divergence, or a `FETCH FAILED`.

## Prerequisites (already set up on this machine — verify if a pull fails)

Non-interactive credentials must be wired, or every fetch hangs on Git Credential
Manager's browser prompt. This repo is configured with:

- a file-store token (`credential.helper=store` repo-local, token in `~/.git-credentials`),
- `core.longpaths=true` (the repo has `org/threads/…` paths over Windows' 260-char limit),
- `core.autocrlf=false`, `pull.rebase=false`.

If a `FETCH FAILED` event mentions auth (the stored token expired), complete **one**
GCM popup manually (e.g. `git -C <ws> fetch origin`), re-pin it, then re-arm.

## Invocation forms

| Form | Behavior |
|---|---|
| `/git-pull` | Arm the **default 15-minute** ff-only loop (`sleep 900`). |
| `/git-pull 5m` · `30m` · `1h` · `90s` | Arm the loop at that cadence. Parse to seconds: `5m`=300, `15m`=900, `30m`=1800, `1h`=3600, `90s`=90. |
| `/git-pull once` | A **single** fetch + ff-only pull now. No loop. Report the result. |
| `/git-pull status` | Report: is a loop running (Monitor task id), current branch, `HEAD` vs `origin/<branch>` (ahead/behind), last-known state. No changes. |
| `/git-pull off` / `stop` | `TaskStop` the running pull Monitor. Confirm stopped. |

**One loop at a time.** Before arming, if a pull Monitor is already running this
session, either leave it (report it via `status`) or `TaskStop` the old one first —
do not stack two loops on the same checkout.

## Step 1 — Resolve workspace root + branch (DEVICE-INDEPENDENT — never hardcode a path)

- **Workspace root:** resolve it **dynamically** with `git rev-parse --show-toplevel`,
  never a hardcoded absolute path. This repo is worked interchangeably on multiple
  machines (e.g. `C:\Users\AndrewBerman\…` vs `C:\Users\Opal Bloomberg\…`); a literal
  path baked into a committed skill breaks on every other device. The agent arms the
  Monitor from the workspace root (the Bash tool's cwd), so `git rev-parse` resolves
  correctly at arm time on whatever machine.
- **Branch:** the loop targets **the currently checked-out branch**, resolved at run
  time (`git rev-parse --abbrev-ref HEAD`) — normally `CLOUD`. It does not hardcode a
  branch, so it stays correct if the checkout is on a different branch.

## Step 2 — Arm the loop (Monitor tool, persistent)

Use the **Monitor tool** with `persistent: true`, `timeout_ms: 3600000`. Substitute
`<SECONDS>` for the requested cadence (default `900`). The command emits an event only
on a fast-forward, a blocked divergence, or a fetch failure — silent otherwise:

```
Monitor(
  persistent=true, timeout_ms=3600000,
  description="CLOUD auto-pull every <N> (ff-only)",
  command="cd \"$(git rev-parse --show-toplevel)\" || exit 1; BR=$(git rev-parse --abbrev-ref HEAD); while true; do if git fetch -q origin \"$BR\" 2>/dev/null; then before=$(git rev-parse --short HEAD); out=$(git merge --ff-only \"origin/$BR\" 2>&1); after=$(git rev-parse --short HEAD); if [ \"$before\" != \"$after\" ]; then echo \"[git-pull] $BR $before -> $after fast-forwarded\"; elif printf '%s' \"$out\" | grep -qiE 'not possible|diverg|overwritten|conflict|^error|^fatal'; then echo \"[git-pull] $BR BLOCKED (needs reconcile): $(printf '%s' \"$out\" | head -1)\"; fi; else echo \"[git-pull] $BR FETCH FAILED $(date -u +%Y-%m-%dT%H:%MZ) — if auth, complete one GCM popup then re-arm\"; fi; sleep <SECONDS>; done")
```

Note the returned **task id** — that is what `/git-pull status` (`TaskOutput(id, block=false)`)
and `/git-pull off` (`TaskStop(id)`) act on. It is **not** visible in `TaskList`.

**BANNED:** launching this under Bash `run_in_background` — the Bash tool only notifies
on *exit*, and this loop never exits, so you would go silent. It MUST run under the
Monitor tool. Also never swap `merge --ff-only` for `git pull`/`git rebase`/`git reset`
in the loop body — the ff-only guard is the whole safety model.

## Step 3 — Confirm + report

After arming, print a compact confirmation:

```
/git-pull  <branch>
  LOOP:   armed every <N> — Monitor task <id> (ff-only; silent on no-op)
  HEAD:   <short> (origin/<branch>: <short>, <ahead>/<behind>)
  CREDS:  non-interactive (no popups)
```

For `/git-pull once`, run one `git fetch -q origin <branch>` + `git merge --ff-only
origin/<branch>` inline and report `<before> -> <after>` (or `up to date`, or the
`BLOCKED`/`FETCH FAILED` reason).

## Handling a BLOCKED event

A `BLOCKED (needs reconcile)` event means local has **committed** work that diverged
from origin, so a fast-forward is impossible. Do **not** force it. Reconcile
deliberately: `git pull` (a merge — never `--rebase`) to integrate, resolve any
conflicts, then push. The loop resumes fast-forwarding once local and origin share a
lineage again.

## Notes

- **In-session scope.** The Monitor dies when the session ends or the machine reboots.
  Re-run `/git-pull` at the start of the next session. If durable-across-reboots pulling
  is wanted, that is a separate Windows Scheduled Task — not this skill.
- **Self-contained + read-mostly.** The loop only fetches and fast-forwards the current
  branch; it never commits, pushes, rebases, resets, or touches untracked / gitignored
  local data (inbox, sessions, `data/`, `node_modules`, `.comp-graph`).
- **Not a monitor/alarm.** This is the *pull action itself* on a cadence (Andrew asked
  for it) — it does not build any freshness-checker / alerter, consistent with the
  standing alarm-moratorium.
