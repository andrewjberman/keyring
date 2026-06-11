# ADVI_COTETL.CHAIN-FIX — cot S3-sentinel emission contract (DS half)

**archetype:** CONTRACT (design pre-stage) · **Author:** 0.4.0_DS_ClientPlatform · **Date:** 2026-06-11
**For:** 0.7.0_AE_CloudOps (EventBridge rewrite) + 2.0.0_SA_COO · **Status:** PROPOSAL — adopt at CHAIN-FIX (post-P1/TO-2). Pre-staged per COO 145140Z to make the AE+DS handoff a single agreed contract, not a round-trip.

---

## Why (the break this fixes)

The 3 cot chain-advance EventBridge rules (`infra/aws/terraform/cot-pipeline/eventbridge.tf`:
`cot_session_complete`, `cot_bronze_complete`, `cot_silver_complete`) fire on
**`aws.ssm` "EC2 Run Command Result" `status=Success`** for `opal-cot-{bronze,silver}-run`.
SSM reports Success on the SSM command's **exit 0** — which a script can return even when it
swallowed an error and produced **no/partial output** (the documented "swallowed-error →
handler success while the served artifact stays stale" class, cf.
`memory/reference_lambda_local_staging_write_crashes_readonly_fs_use_tmp`). So the chain can
advance on a stage that didn't actually land its data.

inf's proven house pattern triggers on **`aws.s3` "Object Created"** for a **sentinel object**
the producer writes as its LAST act — so the next stage fires only when the prior stage
*actually wrote its completion marker*, i.e. the data is provably on S3. AE rewrites the cot
rules to that pattern; the cot bronze/silver scripts (DS-owned) must emit the sentinel objects.
This is the DS-side contract.

## inf reference (the convention being mirrored)

- Bronze: `s3://opal-data-inf/bronze/orion-api/{date}/_BRONZE_COMPLETE.json`
  (`data/inf/scripts/bronze/orchestrator.py:write_sentinel`, emitted after all dims).
- Silver: `s3://opal-data-inf/silver/eclipse/{date}/_meta/silver_complete.json`
  (`data/inf/scripts/silver/convert_eclipse_portfolios_to_silver.py`, last step).
- Shape: small JSON `put_object` (date, completed_at, overall, summary). Date-partitioned key
  → a fresh object each day → S3-Object-Created fires once per day.

## cot sentinel contract (DS emits; AE fires rules on these keys)

All keys in **`opal-data-cot`** (the cot firm bucket; never cross-firm). `{run_date}` = the
pipeline run date (ISO `YYYY-MM-DD`), already threaded through both scripts.

| Stage | Producer (DS-owned) | Sentinel key | Emission point |
|---|---|---|---|
| bronze | `data/cot/scripts/bronze/cot_bronze_ingest.py` | `bronze/{run_date}/_BRONZE_COMPLETE.json` | LAST step of `main`, AFTER all per-table `forwardfill_v2/{table}/{TABLE}_DAILY_{run_date}.xlsx` are written **and re-confirmed present in S3** |
| silver | `data/cot/scripts/silver/cot_silver_merge.py` | `silver/{run_date}/_meta/silver_complete.json` | LAST step, AFTER all `silver/{table}/{run_date}.parquet` partitions + compaction + manifests are written **and re-confirmed present** |

### Emission semantics (the robustness rule — the whole point)

1. **Emit ONLY on verified success.** Write the sentinel only after the stage's expected data
   objects are confirmed present in S3 (re-`head_object`/`list` the keys the run should have
   produced). A failed or partial stage emits **no sentinel** → the next stage's S3-Object-
   Created rule never fires → the chain halts **visibly** (no false advance). This is the exact
   fix for the SSM-exit-0-without-output break. (Stricter than inf, which writes always with an
   `overall` field; recommended for cot because the current bug IS a false-success advance.)
2. **Write direct to S3** (`s3.put_object`), never via a local staging file (read-only-fs /
   swallowed-write class). The sentinel write is itself the success signal — if it throws, the
   stage is not complete and the chain correctly does not advance.
3. **Idempotent / overwrite-safe:** re-running a `run_date` overwrites that day's sentinel
   (same key) → a fresh S3-Object-Created event → re-triggers downstream. Acceptable + desired.

### Sentinel body (JSON, small — for observability + optional downstream gating)

```json
{ "stage": "bronze",                      // or "silver"
  "run_date": "2026-06-11",
  "completed_at": "2026-06-11T02:14:53Z", // UTC ISO
  "overall": "success",
  "artifacts": { "tables": ["transactions","allocations", "..."], "count": N },
  "producer": "cot_bronze_ingest.py" }
```

The S3-Object-Created rule fires on the KEY regardless of body; the body is for CloudWatch/log
observability and lets a downstream Lambda optionally re-check `overall` (defense-in-depth).

## AE side (for reference — the rule rewrite this contract enables)

Replace each `aws.ssm` "EC2 Run Command Result" pattern with an S3 pattern, e.g.:

```hcl
event_pattern = jsonencode({
  source        = ["aws.s3"]
  "detail-type" = ["Object Created"]
  detail = {
    bucket = { name = ["opal-data-cot"] }
    object = { key = [{ suffix = "_BRONZE_COMPLETE.json" }] }   # silver: "silver_complete.json"
  }
})
```

(Requires S3 EventBridge notifications enabled on `opal-data-cot` — AE infra. The `key.suffix`
filter keys off the sentinel filename so a fresh `bronze/{date}/_BRONZE_COMPLETE.json` fires
bronze→silver, and `silver/{date}/_meta/silver_complete.json` fires silver→gold.)

## Open items for AE to confirm (the round-trip this pre-stage collapses)

1. **session→bronze stage:** `cot_bd_session_fetch.py` writes `.bd.identity` to **Secrets
   Manager**, not S3 — it has no natural S3 data object. Options: (a) KEEP `cot_session_complete`
   on the SSM-success trigger (session is a credential refresh, not a data producer — the
   SSM-success risk is lower there), or (b) DS emits a tiny `bronze/_session/{run_date}/
   session_complete.json` after the `.bd.identity` write for full S3-sentinel consistency. **AE's
   call** — I'll implement (b) if you want uniformity, else leave session on SSM.
2. **Key prefixes:** I proposed `bronze/{run_date}/...` and `silver/{run_date}/_meta/...`. Confirm
   these don't collide with any existing cot rule/lifecycle and that S3 EventBridge notifications
   are (or will be) enabled on `opal-data-cot`.
3. **gold-run trigger:** `cot_silver_complete` currently triggers the gold chain. The silver
   sentinel covers it. Confirm gold consumes the silver sentinel (no separate gold sentinel
   needed unless a gold→downstream stage exists).

## DS commitment

On AE's contract confirmation (and CHAIN-FIX activation, post-P1): I implement the two
sentinel emissions in `cot_bronze_ingest.py` + `cot_silver_merge.py` (Rule 14 gate, Rule 13
deploy to `opal-data-cot/code/{bronze,silver}/`), the verify-before-emit checks, and (b) above
if AE elects it. Held until AE confirms the key contract so the emission matches the rule
filters exactly — no round-trip.
