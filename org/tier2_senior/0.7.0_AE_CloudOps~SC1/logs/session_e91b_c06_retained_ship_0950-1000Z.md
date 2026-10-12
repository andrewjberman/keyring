# Session log -- 0.7.0_AE_CloudOps~SC1, 2026-10-12 ~09:49Z to ~10:00Z

**archetype:** DEPLOY

Written for a reader with zero prior context. GO msg 4326 arrived at 09:49:41Z on a quiet watcher tick (after
a long idle since the e87b ship) and was acted on the same turn.

## TO-SC-e91b -- BD C_06 shipped ALONE. Legs V, P, D CLOSED; leg G is the issuer's.

Evidence lives in the ledger `secclass-e91-c06-retained-unclassified-sc1-20261012` and the proof instance
`MDPF_SECCLASS.TO-SC-e91b...proof_of_spec.json` (VALID, rc=0). Not restated. What this log keeps:

### 1. The base was NOT the one the request cites, and step 0 is why that was safe

The request's older text names the SC-e-87 object (`1aa6e3b5`). The served C_06 read `8e1b350f` at VersionId
`5xAeM...` (the ADVI FB-f-9 mode move, 2026-10-12T06:18:21Z), which is what the ORDER and both halves say.
The order's step 0 and COO condition 1 gate on that value, so it was read first and again in the ship's own
shell; it matched, so no STOP. Had the request's value been trusted, the act would have been aborted on a
true base.

### 2. The window, again in the ship's own shell

Runner last launched 04:00:46Z and read `stopped`; `gold/trigger-pending.json` a 404. Re-read at 09:54:18Z
inside the same shell as `safe-deploy.sh`, with the C_06 ETag and VersionId and the repo md5 re-checked
before upload. The guard read open and was not exercised against a closed window in this act.

### 3. Leg P is larger than the order says

The order says "about 11k data keys". The enumeration is 29,547 keys: 18,230 under `gold/entities/clients/`
(449 pages) and 11,314 under `gold/client_timeseries/` (206 pages), with 3 singles. The order's named shapes
(`{rid}.json`, `{rid}_views.json`, legacy `{rid}.json`) are a subset; the composition siblings and nested
keys are included on purpose so any key the retained pass rewrites has a restore target. 0 keys without a
VersionId.

### 4. The seat-gates limb read CLEAR this time

`CROSSBOX-DEPLOY open_call=clear overlap=clear upset=clear open_deploy=clear verdict=CLEAR`. The e87b ship drew
one OPEN-DEPLOY hit (row S28 class d); this one drew none. No row filed.

## What a successor does

Nothing for e91b except the report the order asks for AFTER the first BD fire that follows the ship: C_06's
wall time and the chain's launch-to-stop from the runner telemetry (STOP rule: more than about 30 minutes over
the 04:00:46Z fire's 2h19m, then restore C_06 by VersionId `5xAeM.OWYUSxd7gHYSF6SKmR.ZTmo.PP`, the data keys
by `E91_PREFIRE_VERSIONS_20261012.json`, reporting to `2.0.0_SA_COO~M1` with `1.0.0_SA_CTO~DELL1` copied).
Leg G is the issuer's; the entry is HELD on it. The order is left `in_progress`.

The next scheduled fires: 23:00Z fallback Mon-Sat tonight (2026-10-12 is a Monday), else 04:00Z.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `safe-deploy.sh` | one named gold script path | gate PASS, 1 of 1 deployed and verified; 3 `[not shipped]` lines; seat gates CLEAR. |
| `deploy_ledger.py` | `open` 4 legs, `close-leg V\|P\|D`, `hold` | all accepted; hold accepted after D closed. |
| boto3 `list_object_versions` paginator | leg P over two prefixes, IsLatest only | 29,547 keys / 449 + 206 pages / 0 without a VersionId. |
| boto3 `list_objects_v2` | watch set over `code/gold/` pre and post | 190 / 190, MOVED=1 ADDED=0 GONE=0. |
| `e91_shipped_check.py` | AC1, run before and after | ok=False at the cut, ok=True after, control=MATCH both. |
| `proof-of-spec-check.py` | `<instance> AC1` | VALID (rc=0) first time. |
| `comp-adversary` | not run | the order's preflight declares it RUN by the issuer; declared as an exclusion in the proof instance. |

## Push state

Committed LOCAL on `box/dell1`; this lane does not push a shared branch. Origin state is stated in the report
from an `ls-remote` read at send time.
