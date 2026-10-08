---
name: govern
description: MSTR-only ALWAYS-PROCEED loop (LD-0090): sweep open subjects and Andrew-pending decisions; where Andrew has been silent one turn, proceed with discretion on the dispositioned recommendation; explicit Andrew-asks are reserved for S3/S4 sovereign-class decisions.
---

# /govern — MSTR ALWAYS-PROCEED loop

The operational materialization of LD-0090 sovereign ratification. /govern is the recurring sweep where MSTR proceeds-with-discretion on every open subject where Andrew has been silent ≥1 turn. Three-clause constitutional binding per LD-0090:

1. **ALWAYS proceed** on dispositioned recs (no confirm-loops)
2. **NEVER delay or wait** when discretion exists
3. **1-turn-no-response = proceed** with discretion on any open subject

MSTR-only (a fabric manager: `0.0.0_AB_MSTR` or its lane `0.0.0_AB_MSTR~<lane>`; each box's manager is a lane). Other agents invoking halt at Step 0.

**A manager's record carries no project ruling** (C-SEATS clause 3, Andrew-direct 2026-10-07: "MSTR whole purpose is not
business logic/project reasoning, they are infrastructure managers"). Its acts are merges, pulls, pushes, integration, spawn,
kill, unstick and the bid. A question of substance it receives is PASSED to its CTO by a file, never answered here;
`python .tools/mstr-record-check.py --serial <manager serial> --since <UTC>` lists anything in a manager's day that looks like
a ruling, for a reviewer to judge.

**Historical note:** /govern was RETIRED per LD-0069 (`04f705733`) as a periodic supervision loop because it duplicated Tier-1 supervision work. RESTORED per LD-0090 (`7b613e2db`) with categorically different operational scope — not supervision, but ALWAYS-PROCEED discipline. The two functions are distinct; the prior retire stands as historically correct; this restore is a new skill body under the same name.

## Invocation forms

| Form | Behavior |
|---|---|
| `/govern` | Run sweep, then loop — re-fire **every 1 hour** (default). |
| `/govern 20m` / `30m` / `90m` | Run sweep, then loop at the given interval. |
| `/govern once` | Run sweep once — no loop. |
| `/govern off` (or `stop`) | End the loop. |

## When to invoke

- **Andrew discretion only.** `/govern` is NOT auto-armed at session start (Andrew
  direct 2026-06-03, superseding the LD-0124 startup-arm clause). MSTR does not load
  a `/govern` loop at load; whether to run it — and at what cadence — is Andrew's call.
- When Andrew invokes `/govern`, it initiates the loop at the 1-hour default (or the
  interval Andrew gives).
- Never invoked by any agent other than a fabric manager (`0.0.0_AB_MSTR`, with or without a `~<lane>`).

## Step 0 — Identity gate

Confirm the caller is a fabric manager: `0.0.0_AB_MSTR` or `0.0.0_AB_MSTR~<lane>` (`$env:OPAL_AGENT_SERIAL` or session
registration; `lib/seat_roles.py kind <serial>` reads MSTR for the base serial, and a lane is the same kind). Each box's manager
is a lane, so a bare-serial-only test would halt the manager on every box but one. Non-MSTR invocation halts here with an error.

## Step 1 — Sweep open subjects

Build the list of currently-open subjects awaiting Andrew direction. Sources:

- **Inbox MCPs from agents** asking for MSTR/Andrew direction (subjects matching `[BLOCKED-ASK]`, `[STUCK]`, `[CONSULT-REQUEST]`, `[RATIFY-REQUEST]`, `[ANDREW-DIRECT-NEEDED]`, `[HARD-EXIT]`, `[SOVEREIGN]`)
- **COO sovereign-decision-requests (run `/fabric-check`; LD-0155).** Andrew-direct: part of the /govern sweep is checking whether COO has declared any sovereign-decision-requests. Run `python .tools/fabric-check.py --blocks` (or check your inbox for COO `[SOVEREIGN]`-tagged messages) — any agent in the SOVEREIGN-DECISION-REQUEST bucket, or any COO message declaring a block needs sovereign discretion, is an open subject. These are blocks COO surfaced because their resolution needs an Andrew/MSTR ruling; under LD-0090 / Art. XVI, if Andrew is silent ≥1 turn MSTR issues the ruling (bounded by Directives + Stakes Matrix — a genuinely S3/S4-sovereign item still holds for Andrew).
- **Open LD-0089 (PAVC) ACs** with pending owner decisions OR awaiting Andrew sovereign sign-off
- **MSTR's own surfaced recs** to Andrew in the last 1-2 turns that haven't been responded to (re-read your own outbound text-to-user)
- **Cross-fabric forks** routed via LD-0022 1-tick auto-route discipline
- **Mid-execution decisions** awaiting MSTR ruling that defaulted to "asking Andrew first"

For each open subject, capture:
- Origin (MCP / chat / commit)
- The rec / lean / disposition (what action is being proposed)
- Andrew's response state (RESPONDED / SILENT ≥1 turn / SILENT >1 turn / PRE-1-TURN)
- The stakes class (S0-S2 = MSTR discretion / S3-S4 = sovereign-class reserved for Andrew)
- The dependencies (what unblocks if MSTR acts)

## Step 2 — Classify each open subject

| Classification | Andrew-state | Stakes-class | Action |
|---|---|---|---|
| **PROCEED** | SILENT ≥1 turn | S0/S1/S2 | Execute the rec under MSTR discretion |
| **RESERVED** | SILENT ≥1 turn | S3/S4 | Hold for Andrew; surface again next cycle |
| **RESPONDED** | RESPONDED | any | Already handled; close from open-subject list |
| **PRE-1-TURN** | not yet 1 turn old | any | Hold for current turn; re-evaluate next cycle |

## Step 3 — Execute PROCEED actions

For each PROCEED-classed open subject:

1. Re-state the rec + reasoning briefly in cycle log
2. Execute the action via the appropriate channel (MCP dispatch / commit / scribe / spawn / kill / etc.)
3. Cite LD-0090 + the originating MCP/subject as authorization-chain
4. Log per-action outcome

If execution fails or hits a structural block (e.g., HARD-BLOCK class-5), surface to Andrew as a fresh open subject + classify as RESERVED for next cycle.

## Step 3a — SEAT LIVENESS (this box's own seats; every box's manager runs it)

Andrew-direct 2026-10-07 ~16:3xZ, VERBATIM: "They also can manage /unstick /mstr-spawn /mstr-kill to keep their fabric running
cleanly." Every cycle, before Step 3b:

1. **MEASURE.** Run `python .tools/seat-liveness.py` (read-only). It lists each seat on THIS box as MOVING, QUIET, HUNG, DEAD,
   ELSEWHERE(<box>) or UNKNOWN, and ends `SEAT-LIVENESS device=<d> seats=<n> ... dead=<e> elsewhere=<f> unknown=<g> ok=<True|False>`.
   `ok=False` (a source could not be read): record it and act on nothing from that run.
2. **HUNG** (alive by process, an open task order, nothing in 45 minutes): run `/unstick <serial>`. The unstick skill's own
   diagnosis stands: peek first, key only a seat that is at a prompt.
3. **DEAD** is a seat with an open order whose project is PLACED ON THIS BOX and no process here. Read the order first (the line
   prints its count, its placed-here and elsewhere counts, and newest issued date). Respawn by `/mstr-spawn <serial>` when the
   order is current; `/mstr-spawn`'s own pre-flight (1pt process truth, 1a, 1b, 1d) stands and a refusal is the answer. An old
   order to a seat that never ran is a finding for the COO that issued it, not a respawn. **ELSEWHERE(<box>)** is never respawned
   here: the serial string is the same on every box and this box cannot see another box's sessions, so the seat is working on
   that box. It is that box's manager's to look at; ask that box's manager over the bus (Step 3b's frame), naming the serial.
   **UNKNOWN** (including "placement unread for <n> order(s)") is never respawned: an unread placement licenses no respawn.
4. **QUIET, MOVING, ELSEWHERE, UNKNOWN**: no act here. List the ELSEWHERE and UNKNOWN seats in the report.
5. **RECORD** each act (the serial, the class, the skill run, its result) in the cycle report's SEATS line and the heartbeat.
6. **GARBAGE COLLECTION** (Andrew-direct 2026-10-08 ~16:3xZ, `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_153xZ_TWO_PRIORITIES_GITOPS_AND_PROCESS_GC.md`).
   Every cycle, this box's processes: run `powershell -NoProfile -File .tools/kill-maint.ps1 -Mode scripts` (dry), and run the
   `/watcher` step-2 census for every serial with a row, since the reaper does not yet see a REPLACED copy. Zero targets and one
   watcher row per serial: record `GC: 0`. Otherwise read each target, then stop it: `kill-maint.ps1 -Mode scripts -Execute`,
   and for a serial with more than one watcher row, `taskkill /T /F /PID` on every row but the newest. Never a target: a live
   seat's newest watcher row, a process under a live claude.exe, a process working in a `drain-*` worktree. Record count,
   classes and MB freed on the GC line.

This step acts on this box only. Another box's seat is that box's manager's; the register `org/devices/DEVICES.json` is the list
of boxes and Step 3b is how the managers keep in touch.

## Step 3b — CROSS-FABRIC COMPONENT (Andrew-direct 2026-08-19 ~21:16Z at the MSTR terminal, VERBATIM)

> "I also want you to update your govern loop so that it has a component of staying in touch with
> the sitez MSTR~Z. I have tried to keep the fabrics relatively quarantined by assigning them
> directives that do not overlap, but you should stay in touch and make sure that you are on track
> with your fabric and they are on track with theirs and the two of you /integrate merge in quiet
> periods."

Every cycle, after Step 3a. The other boxes are READ FROM THE REGISTER, never named here: `bash .tools/agentbus-sqs.sh devices`
prints the declared set (one line per box with its queue) and a `this device:` line with this box's own name. Every box in that
set but this one is an other box.

1. **STATUS EXCHANGE** — one bus frame to EACH other box, addressed to that box's manager
   (`bash .tools/agentbus-sqs.sh send <that-box> <your-full-serial> <body>`; the first line of the body says it is for that
   box's fabric manager): this box's on-track read (per directive placed here: on-schedule /
   slipped-with-redate / blocked-named) + ask theirs for the set placed on that box. Terse; measured beats complete. Each answer
   folds into the next cycle report. A box whose frame is unanswered for two cycles is a finding, not a retry loop.
2. **ON-TRACK CHECK, every side** — a slip with a written re-date is HEALTHY; a slip WITHOUT one is
   the finding (route to the owning COO). Directive overlap appearing between the fabrics is itself
   a finding for Andrew (his quarantine premise — same law as /integrate Step 2's overlap band).
3. **QUIET-PERIOD MERGE** — if EVERY fabric reads quiet (no seat mid-commit on another box per that box's
   manager's word; no unswept lane commits here) and divergence is nonzero, run **`/integrate merge`** (the
   full protocol, every leg coordinated over the bus). Not quiet = assess-only and carry to the
   next cycle. The 08-19 evening precedent: overlap ~0 is the healthy shape; a large overlap stops
   the merge and surfaces to Andrew.

## Step 4 — Cycle report

Print fixed format (CROSS-FABRIC line added per the 2026-08-19 amendment):

```
/govern cycle {N}
  OPEN SUBJECTS: {count}
  PROCEED:       {N} executed
                 - {subject 1}: {action taken} | {result}
                 - ...
  RESERVED:      {N} held for Andrew (S3/S4 class)
                 - {subject 1}: {reason held}
                 - ...
  PRE-1-TURN:    {N} too fresh
  RESPONDED:     {N} closed
  SEATS:         {n} seats | moving {a} quiet {b} hung {c} dead {e} unknown {u} | acts: {serial: skill -> result | none}
  GC:            {n} stopped ({classes}) | {MB} MB freed | watcher rows {r} over {s} serials | 0
  CROSS-FABRIC:  status exchanged | on-track every box / finding: ... | merge: ran (heads) / assess-only / not-quiet
  LOOP:          cron-driven (next cycle in {interval})
```

When all open subjects clear OR all remaining are PRE-1-TURN/RESERVED, the cycle is a quiet no-op — report concisely without padding.

## Step 5 — Heartbeat

```
heartbeat(serial="0.0.0_AB_MSTR", summary="/govern cycle {N} — {N} PROCEED executed; {N} RESERVED for Andrew")
```

## Step 6 — Loop continuation

Per LD-0082 pattern (CronCreate-driven), the loop is already armed at the cron schedule. No ScheduleWakeup needed.

If invoking standalone (not on cron), arm via `CronCreate("7 * * * *", "/govern")` (hourly default) OR re-evaluate per the interval Andrew gave.

---

## Discipline / risk notes

- **MSTR-only.** Other agents invoking /govern violate scope; halt at Step 0. A manager rules on no project (see the top).
- **S3/S4 reservation is non-negotiable.** Sovereign-class decisions (constitutional amendments, principal redirects, S3+ risk-class actions per Stakes Matrix) NEVER auto-fire under /govern. They surface to Andrew + remain RESERVED until Andrew responds. Per LD-0090 §Sovereign-class reservation.
- **Authorization chain mandatory.** Every PROCEED action cites LD-0090 + the originating open-subject MCP. Audit trail enables Andrew countermand + post-hoc review.
- **Andrew countermand respected.** If Andrew explicitly counter-directs after MSTR proceeds, MSTR reverts the action (per LD-0090 §Rollback) + updates classification rule for that subject-class.
- **Companion to /mstr-review.** /mstr-review (12h cadence) is the long-form governance review — git-rooted commit walk, directive progress, S0-S4 decision distribution. /govern (1h default cadence, Andrew-discretion) is the action-pacing operating loop — discretion-execution on open subjects. /mstr-review surfaces strategic state; /govern executes tactical proceed-on-rec discipline.
- **Not auto-armed.** Unlike /mstr-review (the standing MSTR cron), /govern is loaded at Andrew's discretion only — never at session start (Andrew direct 2026-06-03).
- **Cousin to /drive.** Both implement "no standing-by terminal state" pattern at different tiers — COO drives lane fulfillment, MSTR drives sovereign-discretion fulfillment.
- **Quiet loop is healthy.** Most cycles will be PRE-1-TURN/RESPONDED quiet. The cycle earns its keep when an item crosses the 1-turn-silent threshold — that's when MSTR proceeds.

## Cross-references

- **LD-0090** (`7b613e2db`) — Constitutional ALWAYS-PROCEED rule; principal authority for this skill
- **LD-0069** — MSTR thin architecture (retired /govern as supervision loop); /govern RESTORED with different operational scope (ALWAYS-PROCEED, not supervision)
- **LD-0082** — CronCreate-driven primary loop pattern; /govern follows same shape
- **LD-0022** — 1-tick auto-route on architectural forks; LD-0090 generalizes; /govern is the operational sweep that fires the generalized rule
- **LD-0089** — Current PAVC GOAL; /govern monitors AC progress for Andrew-pending decisions
- **Memory `feedback_andrew_standing_proceed_on_recs.md`** — constitutional anchor in memory form

## Rollback

If /govern produces false-positive auto-actions OR Andrew explicitly amends the LD-0090 rule:

- `/govern off` ends the loop immediately
- Mark LD-0090 status `closed` + supersede with new LD ratifying revised operating principle
- Per-action revert via standard channel (git revert for commits, /mstr-kill for spawns, etc.)

The skill is reversible at every layer.
