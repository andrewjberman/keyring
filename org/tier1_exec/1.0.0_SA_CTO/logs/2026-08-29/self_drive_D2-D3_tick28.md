# /self-drive D2 & D3 — tick 28 (2026-08-29 01:21Z) — state: ARMED

Covers tick 28 (tick 27 logged @c24e28e19a). Cron bde882a4 (:07/:37; ran on idle). Paired:
`/drive D2 & D3 @ 2.0.0_SA_COO` (:22/:52). Written on DELTA: the detached driver APPLIED and
tested live on a halt; a reap hazard against it caught, disarmed on a predicate this seat amended
against its own first form, and remediated by a zero-kill census; a doctrine line placed; BD's
nightly ending in its own SIGTERM with a two-pid discriminator read.

## Scope (register-read, §0)

`D2 & D3` -> 2 of 12 live directives -> 10 projects (D2 9: 1 complete; D3 1: 0). Open TOs 30
(D2 23, D3 7). Flags none. Device LAPTOP. Claims scan 342 of 342 JSONs: D2 7 / D3 1, all members,
0 claimed-not-member.

## Calls (§1-2)

**Zero adjudicable.** No pitch. RESERVED unchanged. Ledger unchanged: 15 rows / 0 unconsumed.

## The detached driver — APPLIED on three seats, first live test passed (§3)

- **~L 80064, APPLIED 00:56Z @e6f667b9a6:** pid 3367134, ppid 1 by design; `nohup + & + disown`
  borrowed from `.tools/commit-worker-launch.sh` (the fabric's convention, as MSTR was asked for;
  `setsid` excluded per Rule 16); pidfile + kill path (`kill $(cat .../ADVI_49F.P14-VEHICLE_
  DRIVER.pid)`) in the commit; the swap taken mid-date on purpose — TaskStop, the child REAPED
  explicitly (TaskStop does not reap it), `ps`=0, launch behind a singleton pidfile guard. Two
  fixes beyond the kill: `python -u` (every prior task's log was BLOCK-BUFFERED and lagged its own
  ledger — never usable as an instrument; why a 00:37Z log read showed 06-06 while the ledger was at
  06-24) and the singleton guard. COO 80078 confirmed on its own instruments (pidfile alive, `-u`,
  5 rows since the swap); CVO 80089 certified on a third (exactly ONE driver process; 4 rows by its
  own oracle at ~109 s). **EXERCISED not claimed** — the bar is a full ~1h53m boot without a kill.
- **HALT #4 handled UNATTENDED (CVO 80109; ~L 80104 item 5):** 2025-07-10 ARTIFACT-INCOMPLETE
  written by the detached driver's own oracle 01:12:57Z (StateReason read BEFORE start, fourth
  occurrence, Client.InstanceInitiatedShutdown); `ensure_host_running` re-started the box 01:13:02Z;
  relaunch via the committed launcher, pid 3442203 — the stale-pidfile path fired ("pid 3367134 not
  alive — replacing"): the singleton guard working, not asserted. **256 of 534 at 01:21Z** (newest
  2025-07-14; pidfile reads 3442203 in the tree).
- **MSTR 80046 on the kill cause: UNDETERMINED across three planes** — reaper excluded (trigger,
  pattern, audit); harness: both task files end in a literal `[killed]` (the harness's own word), no
  TaskStop readable, ~L's transcript NOT LOCATABLE (runtime 487bc753 has no jsonl under any of 10
  project dirs — an instrument limit stated); device: an IT-agent restart 68 s before kill 1
  (periodic; the driver survived an earlier one), a Windows servicing event at the SAME SECOND as
  kill 2 (correlation, no mechanism), commit charge 91-92% (32 GB; 15 claude.exe + 70 bash.exe).
  ~L's limb-(b) negative: no TaskStop for either killed task (the one TaskStop all session was the
  announced 00:54Z swap) — the harness path narrows to a terminal gesture or a session event,
  neither inferable from inside. The ruling stands as the right shape regardless.

## The reap hazard — ARMED, disarmed on a predicate, remediated by outcome (§3.3)

- **CVO 80053 (BLOCKING x ARMED -> MSTR):** MSTR's memory-pressure reap predicate "bash.exe with no
  live parent" MATCHED THE LIVE DRIVER — its wrapper (pid 3319308) read PPID=1 (the MSYS `ps -p 1`
  trap); the detached driver reads that way PERMANENTLY. **CTO 80056 concurred same-turn** with the
  predicate ruled (exclude by cmdline first; ppid==1 UNKNOWN never ORPHAN; reap only a resolved-dead
  ppid; positive control on 3319308; census with denominator BEFORE any kill); COO 80061 made it the
  drive's line. **~L 80086 corrected the ORDER, and 80091 amended this seat's own item 2:** MSYS `ps`
  mangles the TAIL of long cmdlines where the serial tag sits, so a token test alone could MISS the
  process it exists to spare — the PIDFILE is authoritative (the pid + its child tree), cmdline
  second on the HEAD of the line. CVO @4fbb35a6cb: its own `ps` read had cut the driver's line at
  `--run -` — the instrument fact measured.
- **MSTR 80096 CENSUS DONE, 0 REAPED -> REMEDIATED by outcome:** 79 bash.exe = 8 excluded by cmdline
  + 45 inbox-watchers (15 serials x 3 rows) + 26 transient hook shells; the driver never a candidate
  (python, not bash; cmdline-excluded; pidfile read = 3442203's predecessor; 0 driver rows); alive
  before and after on three seats' reads. **The first pass's "15 orphans aged 3.7-23 h" was an MSYS
  ARTEFACT: `exec` spawns a new Win32 process and retires the old, so a HEALTHY watcher's Win32
  parent reads DEAD** (positive control: ~L's only watcher, that exact form, hearing its mail); every
  one of the 45 rows was born in the same minute as its serial's session. Memory: bash is not it
  (45 x ~10 MB); WindowsTerminal.exe 3.1 GB / 38 tabs, 15 claude.exe 6.7 GB; MSTR next censuses
  DEAD-seat terminal tabs (print-before-act; Andrew's tabs untouched).
- **Doctrine line PLACED @4d37e97de2 (own-lane; broadcast 80099-80101):** `.claude/skills/watcher/
  SKILL.md` gains, beside the `ps -p 1` trap: "Win32 parent = dead" is "ppid = 1" one instrument
  over; the discriminator is CREATION TIME vs the serial's live session, never parent liveness on
  either instrument.

## BD's nightly — NOT a clean finish (~L 80104; CTO read 80126-80129)

From boot -1's persistent journal: `run-gold-layer.sh[4520]` armed `shutdown -h +2` at 01:04:11Z;
`run-gold-layer.sh[122711]` logged a fresh spine header and Step 3/4 starting at 01:05:44Z; systemd
01:06:12Z "Main process exited code=killed status=15/TERM; Failed with result 'signal'; Consumed
4h 11min CPU". ~L does NOT file CVO 79538 REMEDIATED (a signal with its evidence, not a verdict on
BD's data) — right. **This seat's read, both readings held open:** 4520 (the unit's main script)
armed the shutdown as its LAST act after a full-length chain; 122711 was a SECOND invocation starting
from Step 1 ninety-three seconds later — so (A) "the chain halts its own late stage" (~L's) vs (B) "an
unrequested SECOND chain per boot, killed by the first's shutdown" (under which the first run's
served output is complete and what died was a redundant pass). Discriminator = `journalctl -b -1
_PID=122711` (parent, argv) + the same two-pid shape across the nine-boot table — the gold-layer
owner's at the sitting; row 7 (n) gains the question verbatim; item 12 (the `/tmp` "-new" script) is
the first place a re-invocation would live. CVO classifies. **No claim that BD's data is wrong.**

## Standing obligations (carried)

- **05:07Z tick = BACKUP prompter for the 04:35Z INSURE fire reads** (COO 79393 / CTO 79396): list
  `org/mcp/inbox/0.7.0_AE_CloudOps~K/` (+ `read/`) for a 2.0.0_SA_COO file stamped >= 04:52Z
  carrying WAKE; ABSENT -> send [WAKE] to ~K + CVO; PRESENT -> nothing.
- Bridge residual (bounded turn read) + the harness-kill cause (MSTR's read) at the sitting.
- Spec re-open items unchanged.

## Completion test (§4)

NOT DONE — 1 of 10 projects complete. REACHABLE 10 / UNREACHABLE 0.

## RESERVED at Andrew

None open in scope.

state: ARMED · push state of this log: LOCAL (origin/CLOUD @bc277e9710 == HEAD before this commit,
ls-remote read 01:21Z — ticks 26-27, the bridge fix and the /watcher line are ON origin)

## Compiler Tools

- `python .tools/directives-check.py --json` · claims scan 342 JSONs · verdict ledger `wc -l` (15) ·
  campaign ledger tree read + pidfile read · `git ls-remote` + MERGE_HEAD · `/watcher` skill edit
  by python with exact-match assertion · `ack_messages` (80035-80109 as received) · `send_message`
  to_agents (80056-80059, 80091-80094, 80099-80101, 80126-80129; 15 of 15 DELIVERED).
