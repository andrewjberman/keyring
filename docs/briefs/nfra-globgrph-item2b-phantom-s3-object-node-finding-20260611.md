# NFRA_GLOBGRPH ITEM-2B finding — phantom S3 object-key nodes (20x graph bloat)

**Author:** 0.7.0_AE_CloudOps~B · **Date:** 2026-06-11 · **Status:** FIXED + DEPLOYED (globgrph-v0.1.9)
**Surfaced:** during an Andrew-directed live demo of the Kuzu query path (`kuzu_nessie_load.py` -> `comp-kuzu`).
**Fix commit:** `b723f3ea1` · **Deploy:** terraform safe-apply (HALTGT), 0 add/1 change/0 destroy, hash `yM0hkuAIEABC1jz2hTUEKFAhvsGmkgwgCMYtwC4Vvis=`, 0-diff verified.

## What was found

A live `comp-kuzu` load of the Nessie-versioned graph read **24,831 nodes** where the real
AWS account is **~1,167** (824 DECLARED + 321 LIVE-no-DECLARED + 21 AWS_MANAGED + 1 MULTI_STATE
from the nightly full-derive baseline — matches the ~1,116 architecture figure).

The 20x inflation = **23,664 phantom `LIVE-INCREMENTAL` S3_BUCKET nodes**, of which **23,656
have a `/` in the name** — i.e. they are **S3 object keys mis-typed as buckets**:
`opal-data-bd/gold/views/firm_summary.json`, `opal-data-inf/code/silver/...py`, etc.
Real bucket count: **26**.

## Root cause

`infra/aws/lambda/globgrph/incremental_updater/lambda_function.py` (Item-2b updater):
- `extract_arns_from_event` pulls object-level ARNs (`arn:aws:s3:::bucket/key`) from CloudTrail
  S3 PutObject events (the `resources[].ARN` array).
- `bounded_derive_node` s3 branch did `name = arn.split(":::")[-1]` -> `bucket/key`, minting a
  **distinct S3_BUCKET node per object**. Every gold-pipeline artifact write (thousands nightly)
  became a phantom "bucket."

## Why the cert bar did not catch it

**AC4 (`untyped == 0`) PASSES** — the phantoms are validly *typed* `S3_BUCKET`. The 0-untyped bar
detects *missing* type, not *semantically wrong* type/grain. This is a cert-methodology gap worth
a CVO/CTO note: a **grain/identity-sanity check** (e.g. an S3_BUCKET node_id must not contain `/`;
node count within a sane band of the nightly baseline) would catch this class. Recommend adding a
graph-metrics sentinel: `incremental_node_count / baseline_node_count` ratio + per-class
identity-format assertions.

## Impact

1. **Data quality** — 95% of the graph was phantom; any S3-scoped Cypher needs a
   `source='full-derive'` filter to be usable. Pollutes P2-STITCH AC5 (the cross-layer traversal
   walks `... -> S3_DATA_KEY -> ... -> S3_BUCKET -> IAM_ROLE`).
2. **Cost/churn** — every S3 object write triggered a bounded derive + Nessie commit (same class
   as the 06-09/10 409 storm, milder post concurrency-cap, but a continuous driver). Daily
   sawtooth: nightly 02:00 `overwrite()` resets to ~1,167, re-bloats to 20k+ by evening.
3. **Cert blindspot** — above.

## Fix (shipped v0.1.9)

- s3 branch collapses `arn:aws:s3:::bucket/key` -> **bucket grain** (`.split("/")[0]`), rebuilds the
  canonical bucket ARN.
- handler dedups derived nodes by canonical arn -> a batch of N object writes maps to **one** bucket
  node, not N duplicate rows.
- Unit-verified: 3 object/bucket ARNs -> 1 bucket node. Backlog self-clears at the next 02:00
  nightly full overwrite; post-fix intraday no longer re-bloats.

## Recommended follow-ups (route as normal)

- **CVO/CTO:** add the graph-metrics identity/grain sentinel (above) so this class fails the run,
  not just the eyeball. Candidate AC addition.
- **AE (me):** audit the other `bounded_derive_node` classes for analogous sub-resource grain
  (dynamodb stream/index ARNs, etc.) — lower risk than S3 but worth a sweep. Folds into the
  P2-STITCH substrate-cleanliness pass since AC5 traverses these nodes.
