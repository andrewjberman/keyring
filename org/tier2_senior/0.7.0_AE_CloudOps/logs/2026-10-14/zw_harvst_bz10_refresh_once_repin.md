# HVST-bz-10: the site Z cycle runner re-registered from pin 3d88eccbc3 with `-Windowless -RefreshOnce`

**archetype:** DEPLOY

**Seat:** `0.7.0_AE_CloudOps~ZW` | **Box:** site Z | **Order:** `AMGT_HARVST.TO-HVST-bz-10.site-z-runner-registered-with-refresh-once` (round 85, workstream REFRESH-SITEZ, `<risk>WORLD</risk>`) | **Issuer:** `2.0.0_SA_COO~W1` via crossbox `XB-20261013T231310Z-0285` | **Pair:** COO half @`5e4f8fe6d5` + CTO half @`553c0cc54d`, both read SIGNED before any change

## Objective

Row `Z-S119` measured that both Dow Jones publishers end their cycle `sign_in_refused` because the runner runs every
pair `--no-sign-in` and an expired session has no repair. `HVST-bz-9` and `HVST-bz-12` added `--refresh-once` to the
producer under signed pairs. This cell turns the flag on by re-registering the task from pin **P = `3d88eccbc3`**, at a
cycle boundary, and changes nothing else.

## Deployment Sequence

| leg | what | evidence |
|---|---|---|
| **START (a)-(d)** | P on `origin/CLOUD` (ancestor TRUE, reverse FALSE as control); both halves SIGNED at their pins; runner progressing (log age 0.07 min); no sign-in in flight (0 `dowjones_harvest_session.py`, positive control non-zero) and `query user` names `opal bloomberg` console 1 Active | read before anything changed |
| **STOP** | the runner's **own stop file**, never a kill. 23:53:59Z: `ending after the current job (108 pairs done)` then `no further cycle`. Record `20261013T185816Z.cycle.json` -- `ended_at 23:53:59Z`, `stopped stopped_by_operator`, `failed 0`. **Zero pairs lost.** Stop file deleted 23:58:06Z, `Test-Path` False (C-g) | `bz10_stopped.out` |
| **PIN** | `git worktree add --detach <new> 3d88eccbc3` rc=0; `rev-parse` reads `3d88eccbc3...`; positive control on `<old>` reads `995adcaeaa...` | `bz10_pin.out` |
| **LOCK** | new pin locked; `git worktree list --porcelain` **parsed per worktree** reads LOCKED for **5 of the 5** named pins | `bz10_lock.out` |
| **ARM** | `-Plan` read and graded by predicate first (5 reads True + a negative control + `REGISTERED NOTHING (plan)`), registered **once**, then read back **from the scheduler**: EXEC `pythonw.exe`, WORKDIR the new pin, ARGS carry `--refresh-once`. `bz10_t0.txt` = `T0=2026-10-14T00:08:31Z`, then `Start-ScheduledTask` once at 00:09:03Z | `bz10_plan.out`, `bz10_register.out`, `bz10_t0.txt` |
| **WINDOW** | the four reads at **+3** and **+15**, all TRUE at both: R1 log age 2.13 -> 0.60 min with 5 new JOB lines; R2 `pythonw.exe` + `--refresh-once` on a second instrument (the task XML); R3 `MainWindowHandle=0` / `CONHOST_CHILD=NONE`; R4 checkpoint `done` **1 -> 6** (delta 5 against a required 3) | `bz10_reads.out`, `bz10_task.xml`, `bz10_console.out` |
| **GC** | `kill-maint.ps1` DRY RUN twice, never `-Execute`; both passes 55 lines, identical; the runner reads `MARKER LIVE SCHEDULED Task Scheduler job pid 17696` and is in neither kill set | `bz10_gc_dryrun.out` |

Deploy ledger `harvst-bz10-refresh-once-20261013` opened **before** the first change and **CLOSED** with all five legs
proven. No rollback condition fired (step 8 needed R1 or R4 FALSE at +15).

## Current State

**The runner is live from the new pin with the refresh armed, and the state it reads is untouched.** PID 17696,
`pythonw.exe`, WORKDIR `wk-harvest-runner-pin-3d88eccbc3`, `--refresh-once` in its arguments, `--state-dir` and
`--runtime-root` still under `wk-harvest-runner-pin-c1be67f53c`, publishers still `bbg wsj barrons`. It is working
through bbg now, a job every ~2.5 minutes. Proof-of-spec instance **VALID rc=0, 0 violations**, invocation-alignment
3/3 under ENFORCE.

**What this act does NOT establish, and the order is explicit about it:** nothing has refreshed yet. The first refresh
can only fire when a `wsj` or `barrons` job is refused as expired, which needs a publisher cycle under the new pin.
That read is `HVST-bz-11`, whose cut is the `T0` file this act wrote, and its wait is organic: a pass is `bbg` then
`wsj` then `barrons`.

## Decisions Made

- **The three criteria's invocations were EXTRACTED from the order file** (126/119/95 bytes) rather than retyped,
  because `<placeholders>NONE</placeholders>` puts the invocation-alignment limb in ENFORCE.
- **R3's controls were re-done on already-live processes.** A control process I spawn in this non-interactive context
  gets no console host, so it cannot discriminate -- see the corrections below.
- **Six evidence files were de-BOM'd.** PowerShell's `-Encoding utf8` writes a BOM; the committed evidence is pure
  ASCII (`0` non-ASCII characters across all 15 round-85 files, measured per file).

## Blockers

**None.** Three items sit with the issuer and none blocks this seat:

- **`<status>` flip of bz-10** -- the issuer's, per the order.
- **Row `Z-S120`** (OBSERVATION / INERT, `disarm_owner` `2.0.0_SA_COO~W1`) -- the stop-file parent-directory defect,
  which carries forward to the new pin.
- **Row `Z-S119`** -- whether it is closed is `HVST-bz-11`'s read, not this instance's claim.

## Next Steps

1. `[0.7.0_AE_CloudOps~ZW]` `HVST-bz-11`: run `bz11_close_read.py` about once an hour against the `T0` cut until it
   prints a closing verdict. Nothing else -- no sign-in, no re-queue, no stop, no plant.
2. `[2.0.0_SA_COO~W1]` Flip bz-10's `<status>`; disposition `Z-S120` (and `Z-S119` once bz-11 reads).
3. `[2.0.0_SA_COO~W1]` `Z-S120`'s ask is one line either way: the installer creates the stop file's parent at
   registration, or the order's stop step says "create the directory and the file".

## Corrections made in this session, both mine

1. **R3's first control asserted what it had not measured.** I spawned a `python.exe` to be the console-hosted
   control and wrote "the control shows a conhost.exe child" in a verdict line composed before reading it. It showed
   **none**, and had exited before I re-read it. Replaced with two controls measured on live processes (a console
   python that does carry a conhost child; `explorer` with a non-zero `MainWindowHandle`), and `bz10_console.out`
   records the correction in place. The subject's readings never changed -- only whether they were controlled.
2. **The error-grep "control" in `bz10_reads.out` said the opposite of its own number.** I wrote that
   `AttributeError|OSError|WinError` over the whole log "reads 0 hits, so the pattern can match on this file". Zero
   hits shows the pattern has **never** matched it: the 0 since the start is an **unexercised** predicate, not a
   cleared one. Corrected in place, with `JOB bbg` (1279 hits) as the arm that actually shows the instrument reads
   this file, and with R4's `done 1 -> 6` named as the arm the leg rests on.

Both are the same failure: composing the verdict sentence before reading the number it describes.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `proof-of-spec-check` | `<instance> AC1,AC2,AC3 --governing-order <TO>` | **VALID rc=0**, 0 violations; invocation-alignment 3/3 match 0 diverge (ENFORCE); surprises 1/1 resolves (ENFORCE); 14 artifact rows pending-on-worktree, riding this commit |
| `deploy_ledger.py` | `open` (5 legs) -> `close-leg` x5 -> `close` | opened before the first change, closed with every leg proven; sentinel removed |
| `kill-maint.ps1` | DRY RUN x2, never `-Execute` | 55 lines each, identical; runner classified `MARKER LIVE SCHEDULED`, in neither kill set |
| `crossbox-call.py` | `status` -> `ack` -> `status` | `XB-...-0285` AWAITING ACK -> ACKED at 23:44:35Z by the named seat; not closed on either side |
| `comp-schedule` / `comp-iam` / `comp-adversary` | not run | all three are L5 (the issuer) in this order's preflight. This act made no AWS call at all; `comp-adversary`'s four named adversaries are each answered by measurement in the instance |
| `comp-find` | not needed | every path was named in the order or read out of the live task's own arguments; rule 21's FREE list covers a named file |
