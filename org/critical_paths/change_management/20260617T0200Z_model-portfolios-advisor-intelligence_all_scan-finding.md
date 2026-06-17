# Scheduled-scan finding — KNOWN FALSE-POSITIVE (baseline provenance mismatch)

- **Class:** scan-finding
- **Surfaces:** model_portfolios (.headline SEV1, .benchmark SEV1, .aum SEV2, .peers SEV2), advisor_intelligence (SEV1)
- **Firms:** all
- **Scan event:** 2026-06-17 02:00Z nightly `opal-globgrph-derive-runner-nightly` in-derive SURFACE_SCAN (Layer-1)
- **Logged by:** 0.7.0_AE_CloudOps, 2026-06-17 ~14:25Z
- **TO:** NFRA_GRAPHS.D8-FP (faded9893) — active fix in this agent's lane
- **Verdict:** KNOWN FALSE-POSITIVE. Do NOT react to this SEV1/SEV2 as a real MP/ADVI removal.

## What fired
The 02:00Z in-derive SURFACE_SCAN published `[SEV1][PAGE] critical-surface graph change 20260617`
(model_portfolios.benchmark, model_portfolios.headline, advisor_intelligence) +
`[SEV2][digest] ...` (model_portfolios.aum, model_portfolios.peers) to `opal-critical-surface-alerts`,
reporting the watched portal nodes (e.g. `component:portal/src/pages/ModelPortfolios.tsx`,
`endpoint:formatAUM`, the AdvisorIntelligence/PartnerAnalytics components) as REMOVED.

## Root cause (confirmed, CTO-adjudicated 141614Z + 142330Z)
Baseline/scan-scope mismatch — NOT a real removal:
- The signed baseline `s3://opal-313476888478-globgrph/critical-surface-baseline.json`
  (== `.comp-graph/baseline.json`, `built_at`≈2026-06-12T18:32Z, 2139 nodes / 2691 edges) is a
  **comp-graph MERGED build** keyed `node_type:name` (gold:1294, lambda:303, s3:287, endpoint:166,
  eventbridge:62, component:27 — includes portal-AST + a gold/data layer).
- The in-derive Layer-1 scan diffs the **AWS-only derive graph** keyed by **ARN** (1256 nodes).
- The two key-spaces never intersect → `+1239/-2139/~0` (zero matches); only the portal `endpoint:`/
  `component:` removed-nodes (portal/src file_paths) matched watched surfaces → the fire.
  (`SURFACE_SCAN_STALENESS_SKIP prev_marker_ts=None` = first-run/unreadable baseline.)
- AWS estate verified HEALTHY on the 06-17 derive census (nodes=1256, s3=31, lambda=161, ec2=25, ...) —
  no real ~900-node AWS drop. CTO AC1 = high-confidence FP, no escalation.

## Status
- Fix in progress under NFRA_GRAPHS.D8-FP: domain-match the in-derive scan to the derive scope +
  de-noise WITHOUT blinding (AC3) + confirm MP/ADVI healthy on served state (AC4).
- INTERIM (binding until the fix lands): treat any further 02:00Z MP/ADVI critical-surface SNS on this
  same baseline-mismatch signature as the same KNOWN-FP. Do not re-trip; do not re-escalate.
