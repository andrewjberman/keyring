# /canonical-drive -- the COO's loop over the ten limbs

⚠ **RENAMED FROM `/drive` 2026-09-11 per Andrew-direct ~22:2xZ** (relayed by `1.0.0_SA_CTO~Z`, msg 21695,
Step 1b-F @`3c2439d7fe`), VERBATIM: *"That is actually what /drive needs to be rebranded as, it is explicitly
about moving the canonical-flow forward for the respective COOs active project"*. He gave the MEANING, not a
string. **`/drive` REMAINS A LIVE ALIAS** -- `.claude/skills/drive/SKILL.md` points here and is kept working
deliberately, because live crons, `DRIVE.md`, the drive-pair protocol and every log cite the old name. **FLOW
MEASURES where the project stands; DRIVE MOVES IT.** Where the two files differ, THIS ONE governs.

**One tick = measure each in-scope project's LIMB from its tree artifacts, fire the acts that limb owes, adjudicate
what surfaced, log the limb table, heartbeat.** No reporting without acting. Authority: LD-0056 -> LD-0530
(Andrew-direct 2026-09-03: "COOs should be very aggressive in driving L5 L6 activity"; "80 line or less ... a built in
adjudication feature"). Process: `org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md` -- this skill adds no limb. Doctrine,
incidents and instrument traps: `org/tier1_exec/2.0.0_SA_COO/DRIVE.md`; pre-rewrite text: git history @`096aec5b7a`.

## 0. Who, when, over what

- **`2.0.0_SA_COO`** (base + `~lane`) runs COO MODE (obligations 1-7). **`3.0.0_SA_CVO`** (base + lanes) runs CVO MODE
  (obligation 6 only). Any other serial halts and MCPs the COO. Tick start: `get_live_agents()`; re-register if absent.
- `/canonical-drive` = one tick + a cron (`CronList` first); `... 30m|1h`; `... once`; `... off`; `... <scope>` =
  the actuate half of a drive pair (`org/ref/DRIVE_PAIR_PROTOCOL.md`). **`/drive` is the live alias for every form.**
- **Cadence 10m, STANDING and DIRECTED, for a COO on its own active project** (Andrew-direct 2026-09-11 ~22:2xZ,
  *"Both COOs need to be on 10m /drive loops for their projects"* -- the verb is "need to be", so an arm on this
  basis records as DIRECTED, never CHOSEN); **20m for any other in-scope project reading `DECOMP` / `EXECUTING` /
  `ROUND_CLOSE`; 60m when none does.** A seat ARMS ITS OWN LOOPS -- the Step 1b-F table records the authorization
  and no other seat arms, re-arms or re-times it for you.
  ON for the base COO from LD-0530 (supersedes LD-0288's OFF). A lane COO ticks its own team's project.
- **Scope:** projects with a tree home under `org/missions/D*/<MACRO>/<CODE>/` in those stages. Flat projects wait for
  `/canonical-flow`. Never touch `ADVI_BDAPIMIG` `ADVI_TAGATTR` `DATA_SSOTMG` `MDPF_BASISSWITCH` (Andrew 2026-07-10).

## 1. Measure the limb (artifacts only, never a status word or a seat's summary)

Per project: `dep_stage` + round (`project.json`, L10 stamps in `surprise-channel/remediations/`); task orders
terminal/total + assignee (`task-orders/*.md` faces); cells covered / cells serving an ungraded FWD (latest
`decompositions/*.md` x the faces' `cell_refs` x the PRD's FWD ids); open/graduated/armed rows (`comp-surprise
--project <CODE> --json`); the L8 packet and the CVO's READ ack on it (`get_delivery_state`); assignee liveness
(`get_live_agents()` + commits since the last tick). Row: `project | limb | round | TOs t/T | cells c/F | act fired`.

⛔ **THEN NAME THE `/canonical-flow` STAGE AND EXACTLY ONE OF ANDREW'S THREE OUTCOMES IN THE TICK ROW** (his
~22:2xZ word: *"checking explicitly for project stage in /canonical-flow to either drive forward, parallelize
more labor, or assess a dropped ball and nudge the responsible agent"*): **(1) DRIVE FORWARD** -- an unblocked
act at the measured limb; fire it. **(2) PARALLELIZE MORE LABOR** -- an uncovered cell with no unmet
dependency; cut and spawn it (obligation 2). **(3) ASSESS A DROPPED BALL AND NUDGE.** None applies -> NO-OP,
and say which. ⛔ **(3) DOES NOT RUN NAKED: a nudge is authorized ONLY after `/canonical-flow`'s LIVE-PRODUCTION
PROBE reports nothing moving.** Four planes -- COMMITS, DELIVERABLES, the seat's WORKTREE, the CODEX RUNTIME
DIR -- each reading `MOVING | COLD | INCONCLUSIVE`. ⛔ **RUN IT FROM `.claude/skills/canonical-flow/SKILL.md`
AT HEAD AND DO NOT RESTATE IT HERE.** Every control it needs lives there: the per-arm anchor for an author
zero (`AMGT_RESAPP-Z-S84`/`Z-S85`), the author scoping for the SHARED tier-1 home (`Z-S82`), the artifacts-only
filter, and why a codex seat's worktree plane is structurally blind. ⚠ **THIS BLOCK USED TO CARRY THAT TEXT AND
DRIFTED AHEAD OF IT** -- a restatement stronger than its authority is unfalsifiable at a glance, because the
pointer looks authoritative (`1.0.0_SA_CTO~Z`, `Z-S85`). ⚠ **AND NOTHING MOVING IS NOT PROOF OF STALLED**: it
lowers confidence in IN-PROGRESS and never licenses a ladder ending in a kill. **A FIFTH PLANE ANSWERS WHAT ALL
FOUR CANNOT -- LOOK AT THE SCREEN** (`/unstick <serial> --peek`): a seat idle at an empty composer is alive,
bound, unblocked and doing nothing until prompted, and reads GREEN on every process-plane instrument.
⛔ **AND A PEEK IS NOT DONE WHEN IT FINDS A COMPOSER -- ASK WHICH SURFACE HAS THE KEYBOARD.** Measured: the
composer rendered EMPTY was SCROLLBACK and the tab's input went to a PowerShell prompt, so a 1360-char
direction landed in the SHELL, unexecuted behind an unterminated quote. **A rendered composer is not a
reachable one**, and prompting one that is not is how a correct text fails silently. COST: one pointer read
plus asking where the keys go. NON-APPLICATION: a seat that has answered this tick.

## 2. The obligations, in this order, every tick

1. **Round-N analysis in hand -> ONE issuance SAME TICK** (spine v3.0 L10): the choice between a
   re-decomposition and a re-issue is the COO's own, recorded in the issuance commit; the route tokens are
   retired. Never scheduled for later.
2. **WIDTH at L6.** Every uncovered cell serving an ungraded FWD with no unmet dependency is cut THIS tick, one order per
   cell, one cell per lane, through `.tools/to-pipeline-gate.py`; under spine v3.0 the workers are
   subagents the COO spawns in worktrees, fan-out `N of M chains, cap K` stated in the issuance commit
   (default cap 8); a v2 lane is seated the same tick (`/mstr-spawn`; Codex via `ajb2 <FULL_SERIAL>`) only
   for a round already open on v2. **The cap is stated, never silent.** No cell is cut for coverage alone.
3. **Terminal orders -> L8 compile NOW**, by you, handed to the CVO. The compile is an act, never a wait.
4. **L8 packet at the CVO:** no READ ack at one tick -> nudge with path + hash; two ticks -> `[STUCK]` to `0.0.0_AB_MSTR`.
5. **Idle lane + uncovered FWD-serving cell = a DEFECT** in this tick's row; the remedy is 2, same tick.
6. **CVO MODE:** packet received -> L9 adjudication + L10 stamp in the tick that reads it; a packet older than one
   tick unstamped is your own defect row; `[STUCK]` to MSTR at two ticks when blocked outside your power.
7. **ADJUDICATE what surfaced (ported from `/self-drive`).** Every open call or escalation that reached you this tick
   (a `BLOCKED` order, a worker's question, a spec or scope question, a `[STUCK]` from a lane) is classified on ONE
   test: **RESERVED only if a NEVER-class law line or a verbatim standing Andrew hold names its class, quoted on the
   card; everything else is ADJUDICABLE, the default.** ADJUDICABLE within your own L5/L6 authority -> RULE it now and
   dispatch. Otherwise PITCH it with your REC in the same tick: spec/scope -> `1.0.0_SA_CTO` (L2/L4), everything else
   -> this fabric's `3.0.0_SA_CVO`; subject `[DRIVE <CODE> tick N] k call(s) for adjudication + r reserved`. RESERVED
   cards go to `0.0.0_AB_MSTR` for Andrew, never to a worker. Verdicts received since the last tick are executed as
   rulings (row in the tick log citing the message id), a verdict you believe wrong is executed AND surfaced to MSTR in
   one line, never re-litigated. Adjudicator dark on the broker -> spawn ask to MSTR the same tick, no pitch into a dead
   inbox. **A worker never receives a question back; it receives an order or a ruling.**

Then seat triage: an assignee with no commit and no work row since the last tick -> nudge with the order id and the
ground truth; a second silent tick -> reseat on a live same-lane exec's lane or `[STUCK]` to MSTR; a dead assignee
with an open order is respawned or reseated this tick. **A dispatch into an unverified lane is a hope, not a drive.**

## 3. Dispatch, gate, log

- Rule 27: an order comes from a cell, names one worker serial (`0.9.0_WK_<CODE>~<n>`; a Tier-2 seat only on a
  round already open on v2), passes the L6 gate on its own. Subject `[DRIVE]` /
  `[STUCK]`; body = project, limb, order id, reason, RAVC window. A gate someone else legitimately holds is a gate;
  verify it is real; a self-inflicted wait is coasting.
- **Hard gate:** a tick that read a graduated round, an uncompiled terminal order, an unacked packet past one tick, an
  idle lane beside an uncovered FWD-serving cell, or an unadjudicated call, and fired nothing on it, FAILS. "All
  standing by" is never a terminal state; the same self-resolvable gate re-attested twice is the coast failure.
- **Log** on substantive ticks only: `org/tier1_exec/{RUNNING_SERIAL}/drive_log_{YYYYMMDDTHHMMZ}.md` (limb table, acts,
  verdicts, findings); commit via `safe-commit.sh` with a non-shell-written message file; verify by your own hash. The
  movement window derives from your last substantive log, never a shared marker. Every tick ends with `heartbeat`.
- Instruments: `jq` is absent, read JSON with python; never `2>/dev/null` a verdict-bearing read; two signals agreeing
  convict, one absence convicts nothing; `u`/`w`/`read/`/`channel push` are not delivery oracles (`DRIVE.md §4, §4a`).
  `/govern` verifies this loop's health, it does not run it. **Changing this file: imperative + mechanism + pointer, under
  80 lines; the why goes to `DRIVE.md`.**
