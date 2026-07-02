# Deploy-completion ledger -- ADVI_BDAPIMIG D1+D2 (txn-chunk + bd-silver etag content-skip)

**Owner:** 0.4.0_DS_ClientPlatform~B | **Opened+Closed:** 2026-07-02 (~19:15Z -> 19:28Z, same session)
**Authority:** MSTR-DIRECT (184413Z) + CTO GATE-1 BLESSED (183251Z) + Andrew-GO HALF-2 (2026-07-02).
**Commit:** 8029aa080 (on origin/CLOUD). **RAVC:** 1.0.0_SA_CTO + 2.0.0_SA_COO + 0.6.0_AE_PartnerETL.

## What deployed (DS-owned, Rule 13)

| Artifact | Target | ETag (== local md5) | Verified |
|---|---|---|---|
| cot_bronze_ingest.py (D1) | s3://opal-data-cot/code/bronze/ | 9a66e582b07f59f46875a5f5ab5d2c9e | HEAD-object ✓ 19:23Z (safe-deploy hook) |
| cot_bronze_ingest.py (D1) | s3://opal-data-bd/code/bronze/ | 9a66e582b07f59f46875a5f5ab5d2c9e | HEAD-object ✓ 19:27Z (explicit `aws s3 cp` -- PIPELINE_MAP does NOT dual-deploy the shared script) |
| merge-daily-incremental.py (D2) | s3://opal-data-bd/code/silver/ | ad21d41359b016170819f57b52a3d58b | HEAD-object ✓ 19:23Z (safe-deploy hook) |

**Firm-parity note (surfaced):** the bd copy of the shared cot_bronze_ingest.py was STALE at the
2026-06-25 vintage (27,119 B) -- two versions behind the cot copy (06-29, 37,602 B) -- i.e. the
06-29 DATEMODE-B holdings retry-net had NEVER been propagated to the bd bronze copy. This deploy
brings BOTH buckets current at 43,186 B (06-29 base + D1). Latent gap closed; flag to AE/COO that
the shared-script dual-deploy is a manual DS step (PIPELINE_MAP maps data/cot -> opal-data-cot only).

## What it does

- **D1** (firm-safe txn chunking): `BD_TXN_CHUNK_DAYS` env (default 0 = OFF = single 14d pull = ZERO
  cot regression). >0 splits the transactions restatement window into <=Nd sub-pulls at the
  ingest_table dispatch boundary. Firm-separation held (txn-scoped, env-gated, never crosses cot data).
- **D2** (etag content-skip, HALF-2): all 4 bd silver merges skip on the bronze S3 ETag not the
  filename -> a same-name re-land of fresher data REPROCESSES (fixes the 06-26->06-29 49F freeze
  root). Legacy manifest migrates -> reprocess-once (auto-heals latent frozen partitions + reconciles
  the TXN_DAILY_*->TRANSACTIONS_DAILY_* rename). Extensive per-file + per-run logging (Andrew directive).

## Verification (this session)

- py_compile clean (both scripts). ds-commit-gate clean (4 files). safe-commit surface-check OK.
- Tests: 22 cot (test_retry_net.py, +9 D1) + 11 bd (new test_bd_silver_etag.py) -- ALL GREEN.
- Deploy ground-truthed via S3 HEAD-object ETag == local md5 for all 3 targets (above).

## OPEN cross-lane dependencies (NOT DS scope -- AE 0.6.0 infra; e2e un-freeze gates on these)

1. **BD_TXN_CHUNK_DAYS=3** in the bd-49f-runner Lambda env (TF) -- else D1 stays OFF and the 14d txn
   query still ERRORs on the runner-enable.
2. **Runner emits the bronze sentinel:** bd-49f-runner must call `mod.emit_bronze_sentinel(run_date,
   landed)` after landing (function is DS-owned + firm-bound to opal-data-bd) -- else no
   _BRONZE_COMPLETE.json for the bronze-complete->silver EventBridge rule to fire on.
3. **EventBridge rule** (AE): opal-data-bd bronze/{date}/_BRONZE_COMPLETE.json -> invoke the bd silver
   merge `--all` (the etag-fixed merge). Firm-separated (bd sentinel -> bd merge only).

## Follow-on (DS, TO-6b `<data_reprocess_scope>`)

Historical same-name-skipped partitions: the D2 reprocess-once migration AUTO-HEALS these on the first
post-deploy merge run (every current forwardfill file reprocesses once -> REPLACE). Residual scoping +
freshness re-verify vs raw forwardfill to be RAVC'd after the first triggered run confirms the sweep.

**Status: CLOSED** -- all 3 DS artifacts deployed + ground-truth-verified; no stranded leg. Cross-lane
items (1-3) tracked to 0.6.0_AE for the runner-enable wave.
