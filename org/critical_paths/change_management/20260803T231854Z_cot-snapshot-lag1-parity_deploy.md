# Deploy ledger: cot snapshot LAG=1 parity (ADHOC.cot-snapshot-lag1-parity-and-shell-trace)

- **Opened/closed:** 2026-08-03 23:18:54Z (single-leg deploy, completed in-session)
- **Operator:** 0.4.0_DS_ClientPlatform (DS lane per Rule 13; CTO dispatch-now 225311Z item 2)
- **Change:** `data/cot/scripts/bronze/cot_bronze_ingest.py` BD_SNAPSHOT_ASOF_LAG_BDAYS
  default "0" -> "1" (comment block updated with grounding + history). Commit @bf4c0aabbe.
- **Pattern source:** infra/aws/terraform/bd-pipeline/bd-49f-interim.tf:310
  (`BD_SNAPSHOT_ASOF_LAG_BDAYS = "1"`, the proven 49f configuration).
- **Deploy:** `aws s3 cp` -> s3://opal-data-cot/code/bronze/cot_bronze_ingest.py
  (--sse AES256). VERIFIED MATCH: S3 ETag 94744092f0ffb9e61d9d286b215bd563 == local md5,
  73,220 B, LastModified 2026-08-03T23:18:54Z. Pre-deploy baseline: ETag
  ed5097de2e5d4d073d12e8f11818d5ac, 72,808 B, 2026-07-24 (head-object read BEFORE firing).
- **Scope decision (deliberate):** cot plane ONLY. The bd plane copy
  (opal-data-bd/code/bronze/cot_bronze_ingest.py) is 56,885 B @2026-07-09 -- SIX WEEKS
  DIVERGED from the cot plane's deployed copy. Deploying there would carry the whole
  07-09->08-03 repo delta into the 49f runner, far beyond this one-hunk fix, and the 49f
  runner sets the env EXPLICITLY (the default is moot there). The bd-plane staleness is
  REPORTED as a Model-B one-source drift finding, not silently "fixed".
- **Effect:** next nightly cot run's snapshot primaries (holdings/allocations/unrealized)
  request as-of = run_date - 1 business day; layered with the same-morning retry-net
  generalization @545bde4e9a (holdings-only -> ALL SNAPSHOT_TABLES).
- **Push:** commit rides the integrator cycle (LANES COMMIT, INTEGRATORS PUSH, standing).
