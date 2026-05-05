# Session Log — ADVI_INFINGE.1a-1 Chain Dispatch + Ops Findings
**Agent:** 0.7.0_AE_CloudOps
**Date:** 2026-05-05
**Session window:** ~19:00Z – ~21:30Z (ongoing)
**Branch:** CLOUD

---

## Context

Pinch-hit GO from CTO (20260505T183037Z): DS 0.6.1 dark; AE 0.7 fires PATH A
(5-day positions pull + silver convert) then chain-full `--from INF_B_00` on
PROD runner `i-0ed5afded2ebd4ed4`. Andrew sprint directive (~19:50Z):
"aint no tomorrow" — all Phase 1a TOs ship tonight.

---

## 7 Ops Findings (Structural, Carry-Forward to TO 1a-2 + 1a-3)

### Finding 1 — gold-runner has no checked-out repo

`inf-gold-layer-runner` does not have a git repo. All scripts are S3-synced to
`/tmp/orion_gold_scripts/` at dispatch time. Cannot use `git pull` or relative
imports for live changes — must upload to S3 first then redispatch.

**TO capture:** TO 1a-2 (deployment pattern doc)

### Finding 2 — watchdog regex is WORKDIR-relative

`watchdog-shutdown.sh` grep regex: `GOLD_REGEX="orion_gold_scripts/|orion-gold-dispatch"`.
This matches processes whose cmdline contains `/tmp/orion_gold_scripts/`. When the
dispatch script exits after launching a `--bg` chain, the dispatch script PID disappears
from the process table. If the chain step running in background also exits during a
5-minute gap, no matching process remains → watchdog fires shutdown.

**TO capture:** TO 1a-3 (watchdog regex extension/doc)

### Finding 3 — cross-prefix lib dependency (`_orion_api_silver_lib.py` at `code/gold/`)

`_orion_api_silver_lib.py` lives locally at `data/orion/scripts/silver/` but is deployed
to `s3://opal-data-inf/code/gold/` because all gold-runner scripts import it directly.
CI was not checking this cross-prefix deployment. The S3 lib drift CI check
(`inf-pipeline-lib-parity.yml`) was authored to close this gap.

**TO capture:** ADVI_INFINGE.1a-1 (closed by CI workflow + PARITY.md)

### Finding 4 — flat-vs-Hive path bug traced to lib drift (Scenario X)

D1d dispatch ran using stale `_orion_api_silver_lib.py` from `s3://opal-data-inf/code/gold/`.
The stale version's `silver_api_dim_s3_key()` returned flat `silver/{dim}/{date}.parquet`
instead of Hive `silver/api_dims/{dim}/snapshot_date={date}/data.parquet`.
Result: D1d wrote 5 flat-path artifacts at `silver/positions_mv/` → INF_B_00
could not find the artifact at the Hive key → chain failure. S3 versioning confirmed
enabled; stale version history preserved for forensic reference.

**Fix:** Uploaded local canonical lib to `s3://opal-data-inf/code/gold/_orion_api_silver_lib.py`
at 19:30Z. D1e confirmed Hive paths. 5 flat-path artifacts at `silver/positions_mv/` are
cleanup-only (Hive canonical at `silver/api_dims/positions_mv/`).

### Finding 5 — S3 lib version drift confirmed via bucket versioning

`opal-data-inf` bucket has versioning enabled. Pre-fix stale version of `_orion_api_silver_lib.py`
at `code/gold/` is preserved as version history. Useful for forensics (can compare
stale-vs-canonical diffs for post-incident review). S3 versioning provides de-facto
rollback for all runtime artifacts.

### Finding 6 — watchdog inter-step gap pattern + heartbeat fix

Watchdog fires shutdown when NO matching process is running for `GRACE_SECONDS=300`
(5 min). After a dispatch script exits (having launched `--bg` chain), the heartbeat
is NOT automatically running. Fix: created `/tmp/orion_gold_scripts/.ae07_heartbeat.sh`
(infinite `while true; do sleep 30; done` loop). Running as
`bash /tmp/orion_gold_scripts/.ae07_heartbeat.sh` matches watchdog regex and keeps
the instance alive indefinitely through inter-step gaps.

**Current state:** Heartbeat running as PID 3046, keeping runner alive through
chain D2c (started INF_C_00 at 20:04Z).

**TO capture:** TO 1a-2 (deployment pattern doc — canonical heartbeat pattern)

### Finding 7 — chain end-of-run shutdown fires independent of heartbeat

The heartbeat only guards against the WATCHDOG shutdown trigger. It does NOT protect
against the dispatch script's own end-of-run `sudo shutdown` call at CHAIN COMPLETE.
Runner stopped after D2d completion (20:23Z) despite heartbeat PID 3046 being alive.

**Workaround (tonight):** issue `sudo shutdown -c` via SSM immediately after `--bg` launch
before the 2-minute end-of-run countdown elapses.

**Three structural fix candidates** (TO 1a-3 scope):
- (a) Heartbeat issues `shutdown -c` continuously (defensive cancel loop)
- (b) Patch dispatch script to skip auto-shutdown when guard file (`.no_auto_shutdown`) exists
- (c) `--no-shutdown` flag on dispatch script for chained `--from X` invocations

**TO capture:** TO 1a-2 (deployment pattern doc) + TO 1a-3 (watchdog/shutdown guard pattern)

---

## Dispatch Timeline

| Dispatch | Start | Steps | Outcome |
|---|---|---|---|
| D1a (PATH A — positions pull) | ~19:05Z | `pull_inflection_assets_v2.py` (positions) | OK — 24,205 rows, 5-day range |
| D1b (silver convert) | ~19:15Z | `convert_orion_api_to_silver.py --dim positions_mv` | OK — Hive path (stale lib not yet identified) |
| D1c (INF_B_00 only) | ~19:30Z | INF_B_00 standalone | FAIL — positions Hive key not found (Finding 4 triggered) |
| D1d (re-run after suspected issue) | ~15:00Z (backfill) | `convert_orion_api_to_silver.py --dim positions_mv` 5 dates | WRONG PATH — stale lib wrote flat `silver/positions_mv/` |
| D1e (post-lib-fix) | ~19:35Z | Same as D1d, new lib | OK — wrote correct Hive paths at `silver/api_dims/positions_mv/` |
| D2a (chain-full `--from INF_B_00`) | ~19:42Z | Full chain | FAIL — watchdog shutdown during C-chain gap |
| D2b (re-fire `--from INF_B_00`) | ~19:50Z | Full chain | FAIL — watchdog shutdown again |
| D2c (heartbeat-guarded `--from INF_C_00`) | 20:04Z | C_00..INF_09 | IN PROGRESS — C_03 running at 20:16Z |
| D2d (pending) | ~20:40Z | `--from INF_D_00c` (post DS~D AUDIT-003a rep_id=6 fix) | PLANNED |

---

## ADVI_INFINGE.1a-1 TO Status

### Phase 1 — Enumerate scope (COMPLETE)

| Item | Status |
|---|---|
| Shared libs in scope: 1 (`_orion_api_silver_lib.py`) | DONE |
| S3 deployment paths: 1 (`code/gold/`) | DONE |
| Flat-path artifact sets: 3 sets classified cleanup-only | DONE |
| Flat-path counts | `silver/positions_mv/`: 5, `silver/assets_v2/`: 2168, `silver/transactions/`: 1502 |

### Phase 2 — CI check implementation (IN PROGRESS)

| Step | Status | Notes |
|---|---|---|
| Step 1: Author CI yaml | DONE | `.github/workflows/inf-pipeline-lib-parity.yml` |
| Step 2: CTO commit CI yaml | PENDING | MCP sent to 1.0.0_SA_CTO 20260505T201640Z |
| Step 3: Consumer classification | DONE | All flat-path artifacts cleanup-only |
| Step 4: Cleanup `silver/positions_mv/` (5 files) | PENDING | Awaiting explicit GO (S3 delete requires confirmation per CLAUDE.md) |
| Step 4b: Classify `silver/assets_v2/` + `silver/transactions/` | DEFERRED | `assets_v2` flat path IS intended output of `convert_assets_v2_to_silver.py` (AUDIT-008 wrote there); need COO clarification before deleting 2168+1502 files |
| Step 5: Author INF_PIPELINE_LIB_PARITY.md | DONE | `infra/aws/lambda/ci/INF_PIPELINE_LIB_PARITY.md`, commit `3fb5504e1` |

### Phase 3 — Commit + push

Pending CTO commit of CI yaml + DT push + silver/positions_mv/ cleanup GO.

---

## RAVC Trail

| RAVC | Status | Notes |
|---|---|---|
| RAVC5 (D2c empirical) | PENDING | Awaiting INF_09 completion; dashboard.json/leaderboard.json update |
| RAVC5' (D2d post rep_id=6 fix) | PENDING | Awaiting D2d completion (COO Path A) |

---

## Open Items (carry-forward)

| Item | Notes |
|---|---|
| D2c chain complete + D2d fire | Chain at C_03 as of 20:16Z; D2d incantation: `--from INF_D_00c` post D2c |
| RAVC5 + RAVC5' | Triggers DS~A v10, DS~B RPBKTPI.002, DS~C RPBKTPI.001 AC4 |
| TO 1a-1 Phase 2 cleanup | `silver/positions_mv/` 5 files pending GO; `assets_v2`/`transactions` pending classification |
| TO 1a-2 (deployment-pattern doc) | Author post 1a-1 close |
| TO 1a-3 (watchdog regex doc) | Time-permitting tonight |
| BD nightly watch | `TXN_DAILY_2026-05-05.xlsx` expected at 21:53Z in `s3://opal-data-bd/forwardfill_v2/transactions/` |
| Silver catch-up (stale Hive dims) | household/performance/activity/accounts_v2 for 2026-04-29, 04-30, 05-01; needs silver convert dispatch |
