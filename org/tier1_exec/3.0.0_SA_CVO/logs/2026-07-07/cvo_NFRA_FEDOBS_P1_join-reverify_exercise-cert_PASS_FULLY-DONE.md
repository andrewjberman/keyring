# CVO Exercise-Cert — NFRA_FEDOBS P1 CORE join re-verify (obs_findings live binding): PASS

**Date:** 2026-07-07 (post-reboot restart session)
**Agent:** 3.0.0_SA_CVO
**Target:** the held join re-verify limb from `cvo_NFRA_FEDOBS_P1_AC2_boundary_exercise-cert_PASS.md` (§ "HELD"), unblocked by 0.5.0's GO msg `20260707T123424Z` (obs_findings parquet landed, Glue partitions bound, Trino read-runnable).
**Grounding:** exercised (Rule 22a) — I ran both queries myself against the live globgrph Trino via `.tools/_trino_fed.py` (in-VPC Fargate task), independent of 0.5.0's report. Not a self-report read.

## 1. cross_observer_hotspots (fedobs_views.sql) — independently run

Result: 4 node-grain rows resolving to 3 distinct AWS resources, matching 0.5.0's stated expectation exactly:
- `opal-data-mdpf` (S3_BUCKET) — observers `[GRAPHS-D8, PIPESCRIPT]` — `DECLARED`
- `opal-portal-market-data` (DYNAMODB_TABLE) — observers `[GRAPHS-D8, PIPESCRIPT]` — `LIVE-no-DECLARED`
- `opal-data-portal-v2` — observers `[GRAPHS-D8, PIPESCRIPT]` — `LIVE-no-DECLARED`, appearing as **two node-grain entries** (`S3_BUCKET` + `S3_BUCKET_POLICY` — same bucket, two node_ids in the graph). This is an expected graph-modeling artifact (a bucket has both a resource node and a policy node), not a discrepancy — the underlying finding (portal-v2 flagged by both observers, LIVE-no-DECLARED) is single and matches.

The two-observer x C1 correlation (D8 x PIPESCRIPT meeting at a C1 node) is REAL and reproduces independently — this is the headline FEDOBS-P1 correlation the whole design exists to prove.

## 2. obs_findings_enriched — evidence_ref decompress spot-check (2 independent checks, not 1)

- **GRAPHS-D8 row** (`model_portfolios.headline:served_buckets`) → decompressed against `org/modules/graph/critical-surfaces.yaml:30`: `served_buckets: ["opal-data-mdpf", "opal-data-portal-v2"]`. Matches the evidence_ref exactly — real source, not a synthetic pointer.
- **PIPESCRIPT row** (`opal-data-mdpf`) → I independently re-ran `pipescript --resource opal-data-mdpf` (not 0.5.0's cached output): returned `1 thread(s): mdpf / mdpf-global-view` — byte-identical to the evidence_ref content stored in `obs_findings`. Confirms the observer finding is a live, reproducible pipescript call, not a stale/frozen string.

Both decompress cleanly to real, independently-verifiable source. No hollow evidence_ref found.

## Verdict

**PASS.** The two-observer x C1 join is live, correct, and independently reproducible; both sampled evidence_refs decompress to real source on independent re-run (not trusting 0.5.0's report). This closes 0.5.0's held limb from the AC2 boundary cert.

**FEDOBS-P1 is now FULLY done** (AC1 two-observer overlap — CTO-accepted; AC2 read-only-on-truth boundary — CVO PASS 2026-07-07T11:57Z; the live join — CVO PASS here). All three legs independently certed.
