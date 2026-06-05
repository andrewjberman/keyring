# work-cycle 0012 — MDLP_DISTFIX I1+I2 smartx-side deploy COMPLETE + verified

**archetype:** DEPLOY
**secondary_archetypes:** DIAGNOSE, VALIDATE, COORDINATE
**Date:** 2026-06-05 ~1740-1818Z
**Trigger:** DS run-contract confirm (180236Z) + both producers GO'd; AE = smartx-side committer/deployer (data/smartx/** SHARED_OPAL_ETL lane)

## What shipped
Restored the SmartX account-distribution surface (holdings-count bell-curve) lost in the global->firm-id migration. Both re-pointed producers now read the MDPF `model_aua_positions` feed directly (dead `opal-data-smartx-v2` source retired) and run as a daily Lambda-scheduled job.

**Code (commits):**
- `d24e98545` — event-gated handler + bundled producers + TF (IAM + EventBridge)
- `67f15d8fa` — source-map files[] register (Rule 4; BAU parity gate)
- `77e97eec4` — Global producer /tmp fallback fix (read-only-fs crash, found by smoke-invoke)

**Handler event-gate:** `{"job":"account_distribution"}` runs ONLY the Global (`compute_account_distribution`) + per-firm (`compute_per_firm_account_distribution`) producers with `--upload`, SKIPS the dead-source consolidate pipeline. Each isolated try/except; 500 on any producer fail.

**IAM:** READ-ONLY `opal-data-mdpf` grant (GetObject+ListBucket), separate statement (producers only consume the feed; write to opal-data-portal-v2).

**Schedule:** `aws_cloudwatch_event_rule.account_distribution_daily` cron(30 11) = 11:30Z daily, ENABLED, input `{"job":"account_distribution"}`, target = ingestion pipeline + lambda_permission. Fires after the MDPF feed lands (~11:0xZ).

**Deploy mechanism:** build-and-upload.sh -> S3 artifact -> targeted safe-apply (HALTGT, Rule 18). Targeted on the 5 MDLP resources to keep blast radius tight — `build-and-upload` re-zipped the whole pipeline giving jwt_refresher/rest_pull/ec2_autostart new s3_object_versions with UNCHANGED source_code_hash (byte-identical content, build side-effect); left those out of scope for a later full reconcile.

## The catch (smoke-invoke surfaced a silent failure)
First invoke returned both producers `success` BUT the Global `json/portfolios/account-distribution.json` stayed stale (6/01). CloudWatch logs: Global computed the union correctly then crashed on `save_results()` local-staging write — `OSError Errno 30 read-only file system: /var/task/../staging` (Lambda fs is RO except /tmp). The error was swallowed internally so it falsely reported OK. Per-firm was unaffected (writes straight to S3). Fix = makedirs in try/except -> `tempfile.gettempdir()` (/tmp) on OSError; additive, EC2/Windows paths unchanged.

## Verification (all fresh 2026-06-05 18:17:39Z, reconcile to the cent)
- Global: account_count **7,301**, total_aum **$1,491,982,925.05**, period 2026-06-05, 7 by_model buckets incl inflection 50/50 blends.
- Per-firm 49financial: 6,852 funded / $1,376,858,220 ; inflection: 449 / $115,124,705.
- Reconcile: 6,852 + 449 = 7,301 ; $1,376,858,220 + $115,124,705 = $1,491,982,925 == Global total. PASS.
- Lambda code sha live = GcAjQr2neA8HJ9Wi+NO3eZt1H5K0Gqb43ZjbEjeFjNw=.

## Coordination
- ~A confirmed ZERO file-overlap (MDPF_COUNTS = aggregate-aua-timeseries.json count-series vs my account-distribution.json histogram; disjoint scripts/artifacts; shared read-only MDPF input). ACK'd.
- RAVC2 -> COO; CC CTO + DS.

## Compiler tools
ds-commit-gate (3x clean), comp-iam service, build-and-upload BAU-parity, terraform plan/safe-apply (targeted), live-AWS (lambda invoke/get-function-configuration, events describe-rule/list-targets, iam get-role-policy, s3api head-object). comp-iam service reported "no AWS ops detected" (handler delegates to imported producer modules — boto3 calls live in the producers, not lambda_function.py); IAM verified live instead.
