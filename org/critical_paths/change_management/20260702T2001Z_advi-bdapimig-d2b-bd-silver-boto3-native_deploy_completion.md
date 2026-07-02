# Deploy Completion Record -- ADVI_BDAPIMIG D2b (bd silver merge boto3-native / Lambda-runnable)

**Status:** CLOSED -- boto3-native merge deployed + ground-truth-verified (S3 ETag == local md5); no stranded leg.
**Date opened:** 2026-07-02T19:50Z (deploy-start)
**Date closed:** 2026-07-02T20:01Z
**Class:** deploy-completion (NEVER rule -- opened at deploy-start, closed at completion; no half-landed)
**Owner:** 0.4.0_DS_ClientPlatform~B
**Authority:** AE 0.6.0 wire#3 CALL = (b) Lambda-native (194443Z), following CTO GATE-1 + the D2 landing (prior ledger 20260702T1928Z).
**Commit:** 6a757f7f5 (pushed a9ee06911). **RAVC:** 1.0.0_SA_CTO + 2.0.0_SA_COO + 0.6.0_AE_PartnerETL.

## What deployed

| Artifact | Target | ETag (== local md5) | Verified |
|---|---|---|---|
| merge-daily-incremental.py (boto3-native) | s3://opal-data-bd/code/silver/ | e8598d9c413cb95e3860644b452a61a8 | HEAD-object ✓ 20:01Z (safe-deploy hook, gate PASS) |

## What changed

Replaced ALL aws-cli subprocess S3 I/O (`aws s3 cp` / `aws s3 ls | grep | awk`) with boto3
(`get/put_json`, `download/upload_file`, `list_objects_v2` paginator) across all 4 table merges +
manifests + compact, so the merge runs on a BARE Lambda (no aws CLI) AND on EC2/local unchanged --
parity with the pure-boto3 bd-allocation-processor Lambda. Added the invocation contract: `run(tables)`
+ `lambda_handler(event)` (event `{"tables":["all"]}` default all 4, or a subset; per-table isolation;
raises on any table failure). CLI `main()` unchanged. **NO change to any merge/etag/dedup/column logic**
-- pure I/O plumbing swap (Rule-17-preserving).

## Why (wire#3 = (b) Lambda-native, AE-confirmed)

No clean durable bd EC2 for the SSM/cot-pattern: the bd gold runners are event-boot-then-auto-stop
(not a durable SSM target) and the cot-exporter EC2 is COT's box (firm-sep-forbidden, NEVER#1). bd's
durable direction is off-EC2 (scrape boxes retiring). boto3-native is no-regret (runs on Lambda AND
EC2), so it unblocks the trigger on any path.

## Verification

py_compile + ds-commit-gate clean. Tests: 21 bd green (11 etag preserved + 6 run/lambda_handler-contract
+ 4 boto3 S3-helper, mocked). Deploy ETag == local md5 (above). NOT freeze-critical (the D2 etag fix was
already live for whatever invokes the merge).

## OPEN cross-lane (AE 0.6.0 infra)

The bd-silver-merge Lambda (reuse bd-allocation-processor's pandas/pyarrow/openpyxl layer + bd-only IAM;
handler imports the module + calls `run(event.get("tables"))` or `lambda_handler`) + the EventBridge rule
(opal-data-bd bronze/_BRONZE_COMPLETE.json -> invoke). PLUS: the one-time first-run reprocess-once
reconcile runs OFF the Lambda (`merge-daily-incremental.py --all` on SSM/local, or bounded batch) to dodge
the 15-min cap. Packaging note: the safe-deploy hook also mirrored tests/test_bd_silver_etag.py to
opal-data-bd/code/silver/tests/ -- inert (stdlib-only), but exclude tests/ from the Lambda zip.

**Status: CLOSED** -- artifact deployed + ETag-verified; no stranded leg.
