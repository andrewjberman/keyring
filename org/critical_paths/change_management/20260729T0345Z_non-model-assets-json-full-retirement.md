# DEPLOY LEDGER: non_model_assets.json FULL RETIREMENT (teardown-wave member #1)

**Opened:** 2026-07-29T03:45Z by 0.7.0_AE_CloudOps~A
**Status:** OPEN -- steps 1-3 executing in-session; step 4 (no-regen proof) closes on the 15:00Z fire.

## Authorization
**ANDREW-DIRECT ~0336Z (relayed by 1.0.0_SA_CTO 033738Z, VERBATIM):** *"Ok have 0.7.0_AE_CloudOps~A
get rid of that non_model_assets.json and make sure that there is no producer who is going to
generate that shit again."* CTO co-sign for the NEVER#3 S3-deletion leg is in the same message;
COO cc'd. Sovereign-ordered freeze exception (same class as tonight's ETFS apply).

## Step 1 -- WRITER CENSUS (writers-to-the-KEY, not grep-for-names)
Key: `s3://opal-data-portal-v2/json/portfolios/non_model_assets.json`
| Writer candidate | Verdict | Evidence |
|---|---|---|
| mdpf chain Stage 3.5 -> `build_legacy_compat_emit.py --upload` (deployed dispatch `:363-385`, EC2 pulls `s3://opal-data-mdpf/code/scripts/`) | **THE live scheduled writer** | put_object @ script `:899` (pre-edit); object LastModified 2026-07-27T15:10:07Z == Stage 3.5 emit time to the second |
| smartx 11:30Z rule `smartx-account-distribution-daily` -> opal-smartx-ingestion-pipeline `{"job":"account_distribution"}` | **READER only** (CTO's unverified item RESOLVED) | lambda source: only get_object on the key (`load_enterprise_totals` :121-131); zero put_object refs |
| `build_aggregate_aua_timeseries.py` (ROLLUP, dispatch `:391`) | NOT a writer of this key | grep "non_model_assets" = 0 (series-name refs only) |
| `data/smartx/scripts/backfill_non_model_assets.py --prod` | manual-only writer-CAPABLE, unscheduled | prod key @ `:38`; no schedule anywhere |
| `data/smartx/scripts/compute_non_model_assets.py` | DEAD (raises on invoke, retired 2026-05-13 TO-5) | `:32` hard deprecation |
| `dim_mdpf_non_model_assets.py` (dispatch 6c) | different key -- writes `gold/mdpf_revamp/global/non_model_assets.json` (revamp staging; NOT the legacy served artifact; out of scope, untouched) | script `:89` |

## Step 2 -- WRITE-LEVEL RETIREMENT (C1: unit of retirement is the WRITE)
- `build_legacy_compat_emit.py`: NM put_object REMOVED from the upload block; NM read made
  absence-tolerant (NoSuchKey -> {}) so the aum-timeseries.json leg keeps emitting unchanged;
  docstring re-written to the retirement truth. Producer keeps running (aum leg intact).
- `backfill_non_model_assets.py`: ALL S3 writes refused (rc=3 with retirement message);
  --dry-run analysis preserved. Closes the last writer-capable path (both prod + preview keys).
- commit-gate PASS on both files. NOT a {gold,silver,bronze} path (Rule-13 enumeration) --
  AE lane; DS base notified (CTO cc'd them in the order).

## Step 3 -- OBJECT DELETION (NEVER#3 leg: Andrew explicit word + CTO co-sign, above)
Family census on S3 (`aws s3 ls json/portfolios/ | grep non_model`): exactly 2 objects --
- `json/portfolios/non_model_assets.json` (114,553 B, LastModified 2026-07-27T15:10:07Z) -- THE target
- `json/portfolios/non_model_assets_preview.json` (84,760 B, 2026-05-13) -- same-family QA residue,
  written only by the now-retired manual backfill; not served (portal route serves only the main key,
  portal_data_proxy `:2204`). Deleted under the same order, disclosed here.
Bucket is versioned: deletes create delete markers (restorable; deliberate -- reversibility preserved).
- (deletion timestamps appended on execution)

## Step 4 -- NO-REGEN PROOF (closes this ledger)
The 15:00Z unattended fire is the natural test: after chain completion (~15:15Z), the key must NOT
exist. Anything recreating it = a writer the census missed -> STOP + report per CTO spec. D2 note:
the retirement touches no trigger/schedule -- the fire's schedule evidence is unaffected.

## Known consequence (surfaced by CTO to Andrew; not mine to fix)
Until DE's queued chart fix promotes, Global trend/band surfaces reading this file render
reduced/absent non-model -- honest absence over the wrong 232.31 composition.
