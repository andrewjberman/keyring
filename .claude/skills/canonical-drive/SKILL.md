# /canonical-drive -- the COO's loop over the ten limbs

**One tick = read each in-scope project's mode lease, measure its LIMB from tree artifacts, fire the acts that limb
owes, rule what surfaced, log, heartbeat.** No reporting without acting. Process: `org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md`
(this skill adds no limb). `/drive` is a live alias for every form. History and quotations:
`docs/references/CANONICAL_DRIVE_SKILL_PRE_CUT_20260924.md`; doctrine and instrument traps: `org/tier1_exec/2.0.0_SA_COO/DRIVE.md`.

## 0. Who, when, over what

- **`2.0.0_SA_COO`** (base + `~lane`) runs COO MODE (obligations 1-8); **`3.0.0_SA_CVO`** runs CVO MODE (obligation 6
  only); any other serial halts and messages the COO. Tick start: `get_live_agents()`; re-register if absent.
- Forms: `/canonical-drive` = one tick + a cron (`CronList` first); `... 30m|1h`; `... once`; `... off`; `... <scope>`.
- **Cadence: 60m, every case** (Andrew-direct 2026-10-10 ~23:3xZ, "slower pacing ... canonical drive and self drive loops
  can be on 60m interval", to avoid the usage limit; record
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261010_23xxZ_SLOWER_PACING_LOOPS_60M_KEEP_DRIVING_OFF.md`;
  supersedes the former 10m/20m tiers). A seat arms its own loops; org/XXX.md Step 1b-F records the authority.
- **Scope:** projects with a tree home `org/missions/D*/<MACRO>/<CODE>/` in those stages. Never drive `ADVI_BDAPIMIG`
  `ADVI_TAGATTR` `DATA_SSOTMG` `MDPF_BASISSWITCH`, a row reading `status: closed`, or a row carrying `closer_contract`
  (the closer owns it until hand-back; its state is the contract's STATUS files).
- **READ THE LEASE FIRST, per project:** `python .tools/drive-mode.py read <CODE>`. **FAST -> run `/closer-drive` for
  that project instead of this body. HOLD -> skip it this tick.** FULL (the fail-closed default) -> continue below.

## 1. Measure the limb (artifacts only, never a status word or a seat's summary)

Per project: `dep_stage` + round (`project.json`, L10 stamps); task orders terminal/total + assignee (faces); cells
covered / cells serving an ungraded FWD (latest decomposition x `cell_refs` x the PRD's FWD ids); open/graduated/armed
rows (`comp-surprise --project <CODE> --json`); the L8 packet and the CVO's READ ack (`get_delivery_state`); assignee
liveness; **thread live** (a `FWD-1` trace exercised this round: `y` / `n` / `none`). Row: `project | limb | round |
TOs t/T | cells c/F | thread | act fired`.

**Name the `/canonical-flow` stage and exactly ONE outcome in the tick row:** (1) DRIVE FORWARD -- an unblocked act at
the measured limb; fire it. (2) PARALLELIZE -- an uncovered cell with no unmet dependency; cut and spawn it. (3) NUDGE --
only after `/canonical-flow`'s LIVE-PRODUCTION PROBE (run from its file at HEAD) reports nothing moving, and after a
look at the screen (`/unstick <serial> --peek`) that names which surface has the keyboard. Nothing moving is not proof of
stalled and never licenses a kill. **None applies -> EMPTY TICK: if `python .tools/open-calls.py mode get --part empty_tick` reads `state=on` (the
`/keep-driving` switch), run `/next-calls <CODE> --drive` and execute its SEQUENCE
(NOW + WHILE WAITING), queueing each call with `open-calls.py add`, until it returns no FREE option; then `python .tools/unblock.py
tick --serial <you> --project <CODE> --result nothing|work`. `THIRD-EMPTY-TICK` (two empty ticks, nothing opened on the third)
-> write your position to the CRO with `/unblock`; `WAITING` -> keep running `/next-calls`; `RESUME` -> drive on the signed fold**
(Andrew-direct 2026-10-09 ~00:0xZ and ~02:3xZ; records `ANDREW_DIRECT_20261009_000xZ_*`, `..._023xZ_*`).

## 2. The obligations, in this order, every tick

1. **Round-N analysis in hand -> ONE issuance SAME TICK.** The recut reads the analysis's ENRICHMENT LIST as the round's
   rectangle: one cell per item plus the remediations, thread-breaking first, repairs batched into ONE cell. Round 1 of
   a threaded project is the THREAD. Cut under `/dispatch` Step 2 (every check dry-run at the base first). A cell under
   the size floor with `<risk>LOCAL</risk>` takes the DIRECT-ACT path (`/dispatch` Step 2).
2. **WIDTH at L6.** Every uncovered cell of this round's rectangle serving an ungraded FWD with no unmet dependency is
   cut THIS tick, one order per cell, through `.tools/to-pipeline-gate.py`; fan-out `N of M chains, cap K` stated in
   the issuance commit (default cap 8). No cell is cut for coverage alone.
3. **Terminal orders -> merge per chain end (`/dispatch` Step 5), then the ONE REAL RUN of each outcome at close** --
   the running page looked at, or the real entry point -- and the L8 compile, by you. The compile is an act, never a wait.
   Before the round is counted finished (`dep_stage` to `ROUND_CLOSE`), run `python .tools/round-close-check.py --project <CODE> --round <n>`; `verdict=REFUSED` means it is not finished.
4. **L8 packet at the CVO** (`SERVED` / `WORLD` rounds): no READ ack at one tick -> nudge with path + hash; two ticks ->
   `[STUCK]` to `0.0.0_AB_MSTR`.
5. **Idle lane + uncovered FWD-serving cell = a DEFECT** in this tick's row; the remedy is 2, same tick. On round 1 of a
   threaded project only FWD-1 is in scope.
6. **CVO MODE:** packet received -> L9 on judgment criteria of `SERVED` / `WORLD` cells, graded on the real run's
   artifact, + the L10 stamp in the tick that reads it; a packet older than one tick unstamped is your own defect row.
7. **RULE what surfaced.** RESERVED only if a NEVER-class law line or a verbatim standing Andrew hold names its class,
   quoted on the card; everything else is yours: **the issuer rules everything inside its own decomposition** (amend,
   re-point, grant paths), recorded in the amendment commit with the gate limb that graded it. Only an ENDPOINT change
   or `SERVED` / `WORLD` work goes to `1.0.0_SA_CTO`; RESERVED cards go to `0.0.0_AB_MSTR` for Andrew. A worker never
   receives a question back; it receives an order or a ruling.
8. **CLOSER CANDIDATE -> PITCH.** Two or more rounds and `thread n` -> one pitch to `1.0.0_SA_CTO`, subject
   `[DRIVE <CODE> tick N] closer candidate`; keep driving meanwhile.

Seat triage: an assignee with no commit since the last tick -> nudge with the order id; a second silent tick -> reseat
or `[STUCK]` to MSTR; a dead assignee with an open order is respawned or reseated this tick.

## 3. Gate and log

- **Hard gate:** a tick that read a graduated round, an uncompiled terminal order, an unacked packet past one tick, an
  idle lane beside an uncovered cell, an unruled call, an unpitched closer candidate or an empty tick with no `/next-calls --drive`, and fired nothing on it, FAILS.
  The empty-tick limb is MECHANICAL: the `Stop` hook `.tools/hooks/coo-drive-tick-gate.py` reads the turn (not the label) and
  refuses to end a COO drive turn that fired no act and ran no `/next-calls --drive` + `unblock.py tick` while keep-driving is ON.
- **Log:** append each tick to `org/mcp/drive_ticks/<RUNNING_SERIAL>.md` (gitignored runtime file). Commit one log,
  `org/tier1_exec/<RUNNING_SERIAL>/drive_log_<YYYYMMDDTHH>Z_<host>.md` (`<host>` = `hostname | tr A-Z a-z`, derived,
  never typed: one serial on two devices otherwise collides at the merge) holding that hour's substantive ticks, once per
  closed decision or once per hour, whichever comes first; never one commit per tick. Every tick ends with `heartbeat`.
- Instruments: read JSON with python; never `2>/dev/null` a verdict-bearing read; `u`/`w`/`read/`/channel push are
  not delivery oracles.
- **Changing this file:** imperative + mechanism + pointer, under 80 lines; the why goes to `DRIVE.md`.
