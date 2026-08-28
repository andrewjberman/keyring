---
name: log
description: "Write and pathspec-commit the current Codex seat's canonical session log. Use when the user invokes $log or /log, asks Codex to write its session log, requests a one-shot log, or explicitly requests a recurring log cadence. Mirrors the repository Claude /log workflow while preserving Codex exact-seat identity and launcher-owned runtime boundaries."
---

# Log the current Codex seat

Write the current seat's canonical session log for work since its previous log. The format
authority is `org/ref/SESSION_LOG_STANDARD.md`; read it completely on every invocation and let it
win over this entrypoint if they diverge. The archetype requirement is in `org/XXX.md` under
`Archetype tag`.

## Invocation modes

| Form | Behavior |
|---|---|
| `$log`, `/log`, `$log once`, `/log once` | Write and commit one log now. Do not schedule another tick. |
| `$log 90m`, `/log 30m`, `$log [2h]` | Run one tick now, then arm that cadence only through a supported Codex scheduled-task capability. |
| `$log off`, `/log off` | Cancel only the recurring log task for this exact seat. Write no log. |

Cadence mode is operator-initiated only. Never arm it at seat startup. If this runtime exposes no
supported scheduled-task capability that can preserve the same repository and exact seat serial,
run the requested tick once and report `cadence unavailable - not armed`. Never emulate cadence
with Windows Task Scheduler, a shell sleep loop, a second Codex process, a second inbox helper, or
another background process. Never claim a cadence was armed or cancelled without observing it.

## 1. Anchor and derive the exact seat

Start at the workspace root:

```powershell
$workspace = (git rev-parse --show-toplevel).Trim()
Set-Location -LiteralPath $workspace
```

Use `$env:OPAL_AGENT_SERIAL` as the identity. Stop if it is absent. Never infer a serial from the
working directory, `.comp-graph/.agent_context`, a base role, an inbox path, or prior log authors.
Derive the repository paths mechanically:

```powershell
python org/mcp/codex-seat-load.py --serial $env:OPAL_AGENT_SERIAL --format json
```

Stop if it exits nonzero or returns a different serial. Use the returned `seat_home` for the log
directory. A lane suffix remains part of the title, author, handoffs, and report even when its
repository home is the base role directory.

## 2. Establish the log window

- Log directory: `<seat_home>/logs/<YYYY-MM-DD>/` in UTC.
- Find the newest prior log across the latest two dated log directories. Cover the substantive
  delta after that log; if none exists, cover the current session.
- One-shot filename: choose a concise `{scope}_{action}.md`; for a session close use
  `session_close_{HHMM}-{HHMM}Z.md`.
- Cadence tick filename: `work_{HHMM}Z.md`.
- Preserve existing user and peer changes. The new log is the only path this workflow owns unless
  the user explicitly adds another path.

Use hot conversation context as evidence when it is complete. For compacted or uncertain windows,
verify only the missing facts with read-only checks:

```powershell
git log --oneline --author="$env:OPAL_AGENT_SERIAL" --since="<window start>"
```

Use the generated context's exact `read_inbox` only when message recall is genuinely uncertain.
Do not reread every message to manufacture a traffic table. Count significant traffic and name
only GOs, rulings, findings, merge windows, and validation opens/closes.

## 3. Write the canonical record

Follow `org/ref/SESSION_LOG_STANDARD.md` exactly, including role-specific additions. These points
are non-negotiable:

1. Put `**archetype:** TAG` immediately after the title. Use an allowed archetype or `MIXED`.
2. Include `## Compiler Tools` with the table, What worked, What failed, and Gap found. If no
   compiler tool ran, write one sentence explaining why. Never rerun a tool just to populate the
   log, and never append to `org/compiler-tools-log.md`.
3. Write Current State for a reader with no prior context. Name exact files, functions, commits,
   artifact paths, external resources, and live holds where material.
4. Use the Blocker Verification Protocol before writing `BLOCKED`. Name `AMBIGUOUS` when evidence
   does not establish a live blocker.
5. Cross-seat Next Steps name the receiving full serial in brackets.
6. Use plain ASCII. No emoji or decorative Unicode.
7. Record what happened; do not turn logging into new project work. Routine composition should
   remain under 90 seconds when the active context already carries the facts.

For interval mode, write nothing when there is no substantive delta: no commits, significant
messages handled, deploys, rulings, validations, or material state change. Report a no-delta skip
without creating a heartbeat-only file.

## 4. Commit only the log

Before committing, honor any active Master merge-window hold. If a hold is live, write the log but
do not stage or commit it; report the exact local path and `commit held by merge window`. Resume
only after the explicit CLOSE frame and a clean staged-index check.

Otherwise invoke the repository wrapper from the workspace root. Do not pre-stage anything:

```powershell
$author = "$env:OPAL_AGENT_SERIAL <$env:OPAL_AGENT_SERIAL@opal.agent>"
bash .tools/safe-commit.sh --author $author `
  -m "log($env:OPAL_AGENT_SERIAL): <one-line window summary>" `
  -- <repo-relative-log-path>
```

Require exit zero, then measure that the resulting commit contains the log path and has the exact
author. Never broaden the pathspec, use `git add -A`, use `git commit -a`, or absorb another seat's
staged paths. The launcher owns Codex registration and heartbeat; do not start, replace, or signal
a heartbeat helper as part of logging.

## 5. Cadence handling

When a supported scheduler is available:

- List existing recurring tasks first. Keep at most one log cadence for the exact serial.
- Replace an existing log cadence when the user supplies a new interval.
- The task must re-invoke `$log` for the same workspace and exact serial and repeat this workflow
  for the delta since the previous tick.
- `$log off` cancels only that exact task and reports the observed task identifier.

When no supported scheduler is available, do not create persistent state and do not alter other
automations. The one-shot tick remains valid; cadence state is `not armed`.

## Report

End every invocation with:

```text
$log <exact serial>
  MODE:    ad-hoc | loop tick (<task id>, every <interval>) | armed <interval> (<task id>) | off (cancelled <task id>) | no-delta skip | cadence unavailable - not armed
  LOG:     <repo-relative path> @ <commit hash> | <path> (local only - merge hold) | none (no delta)
  WINDOW:  <since> -> <now>; <N> commits, <M> significant messages, <K> deploys/rulings/validations covered
```

Write only this seat's log. This skill standardizes ad-hoc and recurring logging; it does not
replace event-driven logs at task completion, rulings, handoffs, or session close.
