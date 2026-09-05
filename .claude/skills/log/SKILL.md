---
name: log
description: Write your session log per org/ref/SESSION_LOG_STANDARD.md for the work since your last log and commit it under your own author line via safe-commit.sh. Bare `/log` = now; `/log 90m` / `30m` / `2h` = arm a recurring cron (operator-initiated only, never at launch), each tick logging the delta and skipping silently when there is none; `/log off`. The Compiler Tools section is mandatory. Every agent, every tier.
---

# /log — canonical session log (ad-hoc or looped)

Write YOUR session log, the canonical way, right now — or on a cadence for long-running work.
**Authority for format:** `org/ref/SESSION_LOG_STANDARD.md` (the full template + role-specific
additions + blocker-verification protocol). This skill is the executable entry point; the
standard wins on any divergence. Archetype-tag requirement: `org/XXX.md` § "Archetype tag".

## Invocation forms

| Form | Behavior |
|---|---|
| `/log` | AD-HOC one-shot: write the session log NOW covering work since your last log. No cron. |
| `/log once` | Same as bare `/log`. |
| `/log 90m` / `/log [90m]` / `30m` / `2h` / `45m` | Arm a recurring **CronCreate** loop at that cadence (for long-running processes), then run one tick now. Operator/Andrew-initiated only — NEVER auto-arm at launch (LD-0175). |
| `/log off` | `CronList` → `CronDelete` any `/log` cron. No log written. |

## Step 0 — ANCHOR to the workspace root, identify yourself, scope the window

- **ANCHOR FIRST (mechanical, every invocation):**
  ```bash
  cd /c/Users/AndrewBerman/Desktop/ajb_workspace && git rev-parse --show-toplevel
  ```
  **Doctrine (Andrew-direct 2026-06-12): the workspace root IS every agent's base — your files,
  logs, task orders, and identity all live under `org/` in ajb_workspace. No agent is ever BASED
  in `portal/`.** Portal is a WORK-SITE you visit for portal tasks — address it explicitly
  (`git -C portal log ...`, scoped `cd portal && ... && cd -`) and return to base; a CWD that
  LINGERS in `portal/` after the portal task is itself the defect, not a normal state. Why it
  bites here: portal is its own git repo, so a lingering portal CWD errors `safe-commit.sh` at
  best and at worst silently feeds you the WRONG repo's history (a bare `git log` inside
  `portal/` returns portal commits only — evidence under-reports with no error). The anchor
  above is simply RETURNING TO BASE; it is not a /log-specific quirk.
- **Serial:** your full registered serial INCLUDING any `~B`/`~C` lane suffix.
- **Log dir:** `org/{tier_folder}/{your_serial}/logs/{YYYY-MM-DD}/` (tier folders: `tier0/`,
  `tier1_exec/`, `tier2_senior/`, `tier3_junior/`). Lane agents: use the folder matching your
  registered serial if it exists; else the base-serial folder with the lane named in the title.
- **Window:** everything since your LAST log entry (find it: newest file across your last two
  `logs/{date}/` dirs). First log of a session with no prior = the whole session.
- **Filename:** `{scope}_{action}.md` per convention (e.g. `gldinc_battery_results.md`,
  `session_close_HHMM-HHMMZ.md`); loop ticks use `work_{HHMM}Z.md`.

## Step 1 — Gather the material (verify if uncertain, SKIP if certain)

The log cites evidence, not recollection — but **hot context IS evidence**. If the window's
work is in your working context (the normal session-close case), write from it directly and
skip these pulls. They are the SAFETY NET for compacted sessions, long windows, or anything
you're not certain of:

```bash
git log --oneline --author="{your_serial}" --since="<window start>"   # your commits
cat .comp-graph/.agent_context                                         # current TO context
ls -t org/mcp/inbox/{base}/[~{lane}/]read/ | head   # only if MCP recall is fuzzy; lane = NESTED,
                                                   # never inbox/{base}~{lane}/ (flat, unread by all)
```
Plus (cite from context, verify only the uncertain ones): deploys/tags, artifacts verified,
RAVC loops opened/closed, rulings/findings issued or received.

## Step 2 — Write the log (the canonical format)

Follow `org/ref/SESSION_LOG_STANDARD.md` **base template** exactly, with these non-negotiables:

1. **Archetype tag** — single line immediately after the title: `**archetype:** TAG`
   (one of EXPLORE / TRACE / DIAGNOSE / VALIDATE / DEPLOY / IMPLEMENT / COORDINATE / SCRIBE,
   or MIXED; optional `**secondary_archetypes:**` line). Required on every substantive entry.
2. **Compiler Tools section** — the table + What worked / What failed / Gap found. If you ran
   none, ONE SENTENCE explaining why (e.g. "doc-only amendment, no code/infra change — Rule-20
   checks ride the implementing TOs"). Blank / "N/A" is NOT acceptable. Role minimums are in
   the standard §"Compiler Tools — Role Minimums".
3. **Role-specific additions** — DE/RD header commit lines; DS Briefs-Written table; DT/AE
   Deployment Sequence + Verification (paste ACTUAL output) — per the standard.
4. **Blockers** — only per the Blocker Verification Protocol (evidence-cited BLOCKED, or
   AMBIGUOUS routed to DE/COO; never assumption-BLOCKED).
5. **Current State** — written for a reader with ZERO prior context: files, functions, AWS
   resources, commit hashes, S3 paths. This is the primary handoff surface.
6. **Next Steps** — cross-agent handoffs name the receiving agent's FULL serial in brackets.
7. **Plain ASCII** — no emojis (CLAUDE.md Code Quality rule applies to logs).

**Speed contract (0.4.0_DE telemetry 2026-06-12 — keep routine logs ≤90s; density may scale
COMPOSITION, never PROCESS):**
- **MCP traffic:** total count + the SIGNIFICANT dispatches only (GOs, rulings, findings,
  RAVC opens/closes). Do NOT enumerate every message; do NOT count broker re-surfaces of
  already-handled messages; do NOT re-read message files to build a table.
- **Compiler Tools rows:** cite runs from working context — NEVER re-run a tool for the table,
  and don't agonize over result classification (a fast PASS/PARTIAL/FAIL/WARN call with a
  one-line note beats a deliberated one; the standard's definitions are the tiebreak).
- **Files Modified:** when your commit messages already carry per-file summaries, the table may
  be `see commit messages: <hash>, <hash>` plus only the rows needing extra context.
- The log is a RECORD of work done, not new work. If a section is costing minutes, you are
  re-deriving — stop and cite.

## Step 3 — Compiler-tools log line + commit

1. (RETIRED 2026-07-29, Andrew-direct.) Do **not** append to or commit `org/compiler-tools-log.md`.
   The Compiler Tools section stays in your session log; the shared-file append is gone.
2. Commit BOTH files via the wrapper, under YOUR author line, pathspec-scoped — do NOT
   pre-`git add` (the wrapper stages your pathspec itself, CLAUDE.md Rule 14a). **Run from the
   workspace root** — a CWD left in `portal/` (or any subdir) errors the wrapper:

```bash
.tools/safe-commit.sh --author "{serial} <{serial}@opal.agent>" \
  -m "log({serial}): <one-line summary of the window>" \
  -- org/{tier_folder}/{serial}/logs/{date}/{file}.md
```

3. `heartbeat("{serial}", summary="<current state one-liner>")`.

## Step 4 — Loop handling

- **Bare `/log` / `once`:** done after Step 3. No cron, no ScheduleWakeup.
- **Interval form:** after the Step-3 commit, `CronCreate` a job that re-invokes `/log` at the
  given cadence (one `/log` cron max — `CronList` first; if one exists, replace it). Each tick
  repeats Steps 0-3 for the delta since the previous tick.
- **No-delta tick (loop mode only):** if the window contains NO substantive work (no commits,
  no MCP traffic handled, no deploys/rulings/verifications), write NOTHING — heartbeat with
  `log-tick: no delta` and end the tick. Heartbeat-only noise files dilute the log signal
  (org/XXX.md: heartbeat-only entries don't even take archetype tags).
- **`/log off`:** `CronList` → `CronDelete` the `/log` job; confirm in one line.

## Report (end of every invocation)

```
/log {serial}
  MODE:    ad-hoc | loop tick (cron <id>, every <interval>) | armed <interval> (cron <id>) | off (cancelled <id>) | no-delta skip
  LOG:     <path committed> @ <commit hash> | none (no delta)
  WINDOW:  <since> -> <now>; <N> commits, <M> MCP messages, <K> deploys/rulings covered
```

## Notes

- **Self-scoped.** You write YOUR log only — never another agent's (their folder is their lane;
  the owned-paths hook enforces it).
- **This skill does not replace event-driven logging.** Logging at natural boundaries (TO
  completion, session close, ruling issued) remains the norm; `/log` standardizes the ad-hoc
  ask and gives long-running processes a cadence.
- **Session-close logs:** a bare `/log` at session end IS the session-close log — name it
  `session_close_{HHMM}-{HHMM}Z.md` and make Current State the handoff.
- **CL fabric:** propagates ws → CL via `.tools/sync-skills-to-worktree.sh` per LD-0089 A.4-EXT.
