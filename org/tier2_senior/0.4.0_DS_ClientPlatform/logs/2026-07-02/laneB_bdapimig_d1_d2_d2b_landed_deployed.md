# ADVI_BDAPIMIG D1 + D2 + D2b landed, deployed, verified (DS lane ~B)

**archetype:** IMPLEMENT
**secondary_archetypes:** DEPLOY, COORDINATE
**serial:** 0.4.0_DS_ClientPlatform~B | **date:** 2026-07-02 | **window:** ~1844Z (spawn) -> ~2010Z

## Summary

Spawned (MSTR-DIRECT 184413Z, Andrew-pre-auth) to own ADVI_BDAPIMIG D1+D2 in parallel, freeing DS~A
for the inf as_of label-fix. Delivered all DS-side legs before the bd feed run: **D1** (parameterized
firm-safe txn chunking in the shared cot_bronze_ingest), **D2** (HALF-2 etag content-keyed skip across
all 4 bd silver merges), and **D2b** (made the bd silver merge boto3-native / Lambda-runnable after AE
surfaced the aws-cli-shell-out blocker on wire#3). CTO ARCH-SIGNED D1+D2 (firm-separation independently
verified) and D2b (I/O-only). Three deploy ledgers CLOSED; the e2e un-freeze now gates purely on 0.6.0's
activation quartet.

## What I did (source-grounded)

1. **D1 -- firm-safe txn chunk** (`data/cot/scripts/bronze/cot_bronze_ingest.py`). New
   `BD_TXN_CHUNK_DAYS` env (default 0 = OFF = single 14d pull = ZERO cot regression; cot SSM never sets
   it). >0 splits the transactions restatement window into <=Nd sub-pulls via a dispatch at the
   `ingest_table` boundary (`_chunk_windows` tiles 5x3d newest-first; `_ingest_transactions_chunked`;
   original body renamed `_ingest_one`). Newest chunk (run_date) fails LOUD (propagates -> runner
   retry/backoff+CW); older restatement chunks best-effort self-heal. Runner needs NO code change (env
   only). Firm-safety ground-truthed on the actual invocation sites: cot-pipeline/ssm.tf:189-190 exports
   only BD_S3_BUCKET/BD_FIRM_ID (no chunk var); bd-49f-runner sets env explicit.
2. **D2 -- HALF-2 etag content-skip** (`data/black_diamond/scripts/silver/merge-daily-incremental.py`).
   Ported the proven cot_silver_merge Cond-2 (`_bronze_etag`/`_load_processed_etags`/`_should_skip` +
   `_select_target_files`) into all 4 merges (txn/alloc/realized/unrealized): skip on the bronze S3 ETag
   not the filename -> a same-name re-land of fresher data REPROCESSES (fixes the 06-26->06-29 49F freeze
   root). Legacy processed_files migrates -> reprocess-once (self-heals latent frozen partitions +
   reconciles the TXN_DAILY_*->TRANSACTIONS_DAILY_* rename). Extensive per-file + per-run logging (Andrew
   directive). Rule-17-preserving (skip predicate only).
3. **D2b -- boto3-native** (same file). Replaced ALL aws-cli subprocess S3 I/O with boto3 (get/put_json,
   download/upload_file, list_objects_v2 paginator) so it runs on a bare Lambda AND EC2/local. Added the
   `run(tables)` + `lambda_handler(event)` invocation contract. No merge/etag/dedup/column change.
4. Surfaced + closed a firm-parity gap: the bd copy of the shared cot_bronze_ingest was 2 versions STALE
   (@06-25, missing the 06-29 retry-net) because PIPELINE_MAP maps data/cot->opal-data-cot only; the bd
   shared-copy is a manual DS `aws s3 cp` (done).

## Files Modified

See commit messages: 8029aa080 (D1+D2 + tests), 6a757f7f5 (D2b + tests), fb8a58d41 / 8b40a3d92 /
7c63345f0 (ledgers). New test: `data/black_diamond/scripts/silver/tests/test_bd_silver_etag.py` (21
cases); extended `data/cot/scripts/bronze/tests/test_retry_net.py` (+9 D1).

## Deployment Sequence + Verification (DS owns, Rule 13)

| Artifact | Target | ETag == local md5 | Verify |
|---|---|---|---|
| cot_bronze_ingest.py (D1) | opal-data-cot/code/bronze/ | 9a66e582... | HEAD-object OK 19:23Z (hook) |
| cot_bronze_ingest.py (D1) | opal-data-bd/code/bronze/ | 9a66e582... | HEAD-object OK 19:27Z (manual cp -- PIPELINE_MAP no dual-deploy) |
| merge-daily-incremental.py (D2 initial) | opal-data-bd/code/silver/ | ad21d413... | HEAD-object OK 19:23Z (hook) |
| merge-daily-incremental.py (D2b boto3) | opal-data-bd/code/silver/ | e8598d9c413cb95e3860644b452a61a8 | HEAD-object OK 20:01Z (safe-deploy gate PASS) |

Tests: 22 cot (test_retry_net.py) + 21 bd (test_bd_silver_etag.py) GREEN. py_compile + ds-commit-gate
clean on every commit. deploy_ledger.py check --red = clean (3 ledgers CLOSED + indexed).

## Compiler Tools

| run | result | note |
|---|---|---|
| comp-blast cot_bronze_ingest | NOT-FOUND | expected -- bronze not in the gold/portal trace graph; CTO endorsed grounding firm-safety on invocation sites instead |
| comp-pipescript deployed merge-daily-incremental / cot_bronze_ingest | MATCH / no-bd-match | confirmed silver deploy path opal-data-bd/code/silver; cot_bronze not tracked in bd bucket sweep |
| comp-pipescript io merge-daily-incremental | tool quirk (script-not-found) | silver script not in the io (gold-column) scope; change is schema-neutral so no column-gap risk |
| (rail-checked) Grep infra for cot_bronze_ingest invocation env | PASS | ground-truthed firm-safety: cot SSM env vs bd-49f-runner env -- the correct lens for a shared bronze script (no comp-tool reads TF-invocation env-vars) |

What worked: invocation-site Grep gave decisive firm-safety grounding where comp-blast couldn't (bronze
off-graph). What failed: comp-pipescript io doesn't resolve a hyphen-named silver script. Gap: no comp-tool
maps "which firms invoke this shared script with which env" (an invocation-env lens); recurring for
shared bronze/silver.

## Blockers

NONE. All DS legs landed+deployed+verified. The e2e un-freeze is GATED on 0.6.0_AE's activation quartet
(runner env BD_TXN_CHUNK_DAYS=3 + emit_bronze_sentinel call + bronze-complete EventBridge rule +
bd-silver-merge Lambda w/ pandas layer + fail-loud freshness alarm) -- a real cross-lane external gate,
handed off with precise contracts + ETag-verified artifacts. Not a DS block.

## Current State (handoff)

- **D1** live in cot_bronze_ingest.py (both buckets). DORMANT until 0.6.0 sets BD_TXN_CHUNK_DAYS=3 in the
  bd-49f-runner Lambda env (firm-safe default off). Chunk dispatch at ingest_table:485-487.
- **D2/D2b** live at opal-data-bd/code/silver/merge-daily-incremental.py (ETag e8598d9c...). The etag
  content-skip is ACTIVE for the next bd silver run whatever invokes it (freeze-prevention already in
  force). Invocation contract: `run(tables)` / `lambda_handler({"tables":["all"]})`.
- **AE (0.6.0) owns:** the bd-silver-merge Lambda (reuse bd-allocation-processor pandas layer + bd-only
  IAM) + EventBridge rule (opal-data-bd bronze/_BRONZE_COMPLETE.json -> invoke) + wires 1+2 (env,
  emit_bronze_sentinel) + the one-time first-run reconcile OFF-Lambda (`--all` on SSM/local, 15-min cap).
- Ledgers: 20260702T1928Z (D1+D2), 20260702T2001Z (D2b) -- both CLOSED. RAVC CTO (SIGNED both) + COO + 0.6.0.

## Next Steps

- **[0.6.0_AE_PartnerETL]** land the activation quartet + point the Lambda at run()/lambda_handler; run the
  first-run reconcile off-Lambda; RAVC CTO the runner-env + sentinel + EventBridge + fail-loud-alarm commit.
- **[0.4.0_DS_ClientPlatform~B]** (me) standing by: on the first triggered merge run, scope + freshness-
  re-verify the TO-6b historical reprocess-once sweep vs raw forwardfill; available for a runner/Lambda-
  handler DS review.
- **[2.0.0_SA_COO]** consider a durable guard for the shared-script dual-deploy (bd copy stranding).
