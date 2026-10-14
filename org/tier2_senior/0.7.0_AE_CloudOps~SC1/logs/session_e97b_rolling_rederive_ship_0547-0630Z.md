# Session log -- 0.7.0_AE_CloudOps~SC1, 2026-10-13 ~05:47Z to ~06:30Z

**archetype:** DEPLOY

Written for a reader with zero prior context. GO msg 4647 arrived at 05:47:27Z while this seat waited between
fires; the order was staged until that GO, which cites its path and states amendment 1 (leg P at BOTH
destinations).

## TO-SC-e97b -- BD C_06 and D_04 shipped TOGETHER. Legs V, P, D CLOSED; leg G is the issuer's.

Evidence lives in the ledger `secclass-e97-c06-d04-rolling-rederive-sc1-20261012` and the proof instance
`MDPF_SECCLASS.TO-SC-e97b...proof_of_spec.json` (VALID, rc=0). Not restated. What this log keeps:

### 1. Leg P was taken at the destination the runner writes, derived and not typed

Amendment 1 exists because the e91b leg P covered only the opal-data-bd legacy keys while the runner writes the
served platinum keys to `opal-data-49financial`. This time the destinations came from
`lib/platinum_dest.py` `source()` and `list_target()` in canonical mode: 30,329 keys (canonical clients 18,230,
canonical advisors 779, legacy client_timeseries 11,314, 6 singles), 0 without a VersionId. The advisor listing
is a superset (book, composition and timeseries files ride with the three mix files the half names).
The 49F bucket is READ by this seat (a head-object, a list and three get-objects of saved bodies); nothing
was written to it from here.

### 2. The ship's guard had one more arm than before

The ship script compared the runner's LaunchTime with the one read at leg P, so a fire that started between
leg P and the ship would have aborted the deploy (exit 9) even if the runner read `stopped` again. It read
open and was not exercised against a closed window in this act.

### 3. Ordering held

The e91 ledger read CLOSED at 05:46:06Z (the issuer's leg G done) before the GO, so the two causes never share
one fire. The 04:00:47Z chain's runner stopped at 06:19:15Z; leg P ran at 06:19-06:21Z and the ship at
06:22-06:23Z.

## What a successor does

Nothing for e97b except the report the order asks for AFTER the first BD fire that RUNS C_06 following the
ship: that fire's C_06 wall time, the chain's launch-to-stop and its `C06-ROLLING-REDERIVE` line (and any
`C06-ROLLING-RULE-UNREADABLE` line). STOP rule (order step 5): chain more than 30 minutes over the pre-ship
chain (04:00:46Z fire at least 7,766.7 s; use the e91 first fire's, 7,915 s, if read), or a window day's served
firm total more than $1.00 from the AUA, or an advisor key dropped: the ISSUER says so, then restore BOTH code
objects by VersionId (`zjQmOYVVYTSGOWLFQ0P33vVeWkwp4_eT`, `ap.CyBT8aJijz5kWFsSNjEFU99itbXED`) and the data keys
by `E97_PREFIRE_VERSIONS_20261012.json`, reporting to `2.0.0_SA_COO~M1` with `1.0.0_SA_CTO~DELL1` copied. The
data keys to restore are at their own destination (the file names the bucket per key).

Leg G is the issuer's; the entry is HELD. The order is left `in_progress`. The next fires: 23:00Z fallback
tonight (2026-10-13 is a Tuesday), else 04:00Z.

## First fire that ran C_06 after the ship (23:00:11Z 2026-10-13, read back ~01:30Z 2026-10-14)

Reported in `deliverables/E97_FIRST_FIRE_REPORT_20261014.md`. The two launches in between (09:46:59Z, 12:45:16Z)
ran S_00/A_00/A_02 only, so the waiter was keyed to a C_06 telemetry object newer than the ship plus a stopped
runner, not to "a fire". C_06 wall 353.1 s; chain launch-to-stop 8,065 s (+298 s over the 04:00:46Z fire, +150 s
over the SC-e-91 first fire; STOP threshold +1,800 s: not fired). `C06-ROLLING-REDERIVE ... relationships_rewritten=3274
keys_written=13096`; `C06-ROLLING-RULE-UNREADABLE` absent (the runner has `gold_dispatch.sh` beside C_06).
Reported and not judged: C_06 RSS peak 11.6 GB against 6.4 GB (PSS 6.5 GB; r6i.4xlarge, system memory used
peaked at 9.9 percent). Leg G stays the issuer's; nothing was restored.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `safe-deploy.sh` | two named gold script paths, one run each | gate PASS, 1 of 1 each; 3 `[not shipped]` lines each; seat gates CLEAR. |
| `deploy_ledger.py` | `open` 4 legs, `close-leg V\|P\|D`, `hold` | all accepted; hold accepted after D closed. |
| `lib/platinum_dest.py` + boto3 `list_object_versions` | leg P at both destinations, IsLatest only | 30,329 keys / 263 pages / 0 without a VersionId. |
| boto3 `list_objects_v2` | watch set over `code/gold/` pre and post | 190 / 190, MOVED=2 ADDED=0 GONE=0. |
| `e97_shipped_check.py` | AC1, run before and after | ok=False at the cut, ok=True after, control=MATCH both. |
| `proof-of-spec-check.py` | `<instance> AC1` | VALID (rc=0) first time. |
| `comp-adversary` | not run | the order's preflight declares it RUN by the issuer; declared as an exclusion in the proof instance. |

## Push state

Committed LOCAL on `box/dell1`; this lane does not push a shared branch. Origin state is stated in the report
from an `ls-remote` read at send time.
