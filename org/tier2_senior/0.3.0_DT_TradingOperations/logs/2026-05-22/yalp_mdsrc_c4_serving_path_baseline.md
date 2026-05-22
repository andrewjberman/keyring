# Session Log — YALP_MDSRC.C4 Phase-2C Serving-Path Drift Baseline

| Field | Value |
|---|---|
| Agent | 0.3.0_DT_TradingOperations |
| Date | 2026-05-22 |
| TO | YALP_MDSRC.C4 — dt-phase2c-serving-path-drift-baseline |
| Issued by | 2.0.0_SA_COO (GO on pickup) |
| Status | Complete |

## Current State

- Startup protocol run: registered (PID 3364), inbox processed. The
  `.unread-deliveries` sentinel held 5 watcher-delivered messages — 3
  SSCN_DIVDEF.006 closure ACKs (project already closed, informational, no
  action) and the C4 GO + NUDGE. Sentinel cleared.
- YALP_MDSRC.C4 executed end to end. Deliverable committed + pushed.
- Baseline doc: `docs/briefs/mdsrc-c4-phase2c-serving-path-drift-baseline-20260522.md`.

## Work Done

Read-only baseline of the CloudFront routing the Phase-2C YCharts-pull
migration (TO-C2) will touch — the `/api/general/*` and `/json-tiered/*` path
families on distribution `EVTSA9VEHNZVH` (opalinvest.dev).

- Captured all 22 ordered CloudFront behaviors via `comp-routes behaviors`.
- The three in-scope behaviors documented in full (origin, methods, cache
  policy, origin-request policy, Lambda@Edge associations):
  - #6 `/api/general/json-tiered/*` — json_tiered_5min (5-min TTL), 3 edge Lambdas.
  - #7 `/json-tiered/*` — json_tiered_5min, NO edge Lambdas (direct passthrough).
  - #8 `/api/general/*` — Managed-CachingOptimized (1-day default TTL), 3 edge Lambdas.
- Cross-checked against `infra/aws/terraform/portal-auth/cloudfront-distribution.tf`
  — comp-routes model and Terraform agree exactly, no drift.
- Cross-referenced PRD §5.2 (32-surface matrix) — mapped the C2-migrated
  market-data / macro surfaces to serving behavior #8 (S3-served artifacts)
  and #6/#7 (Market Overview tiered variants). WS1-DDB-01 (DynamoDB price
  series) is not on either in-scope path family.
- 8 baseline findings flagged (BF-1..BF-8). No live routing defect found —
  all findings are drift / design observations for C2/D1 to plan around.
  Highest-impact: BF-1 — `/api/general/*` long-TTL cache vs json-tiered 5-min,
  so a daily YCharts pull on `/api/general/*` needs an explicit freshness
  mechanism.

## Compiler Tools

| Tool | Result | Notes |
|---|---|---|
| `comp-routes behaviors` | 22 ordered behaviors + default captured | Mandate Phase 1 — primary baseline evidence. Behaviors #6/#7/#8 in scope. |
| `comp-routes rewrites` | `public-data-router` rewrite map captured | `/api/general/json[-tiered]/` -> `json[-tiered]/` S3 prefix strip. |
| portal-auth `cloudfront-distribution.tf` cross-check | Terraform == comp-routes model | No drift between routing model and Terraform. |
| `aws s3 ls opal-data-portal-v2/json[-tiered]/` | Content prefixes listed | Grounded the surface-to-prefix mapping; surfaced BF-6 (valuation/valuations split). |

Phase 2 (before-commit) and Phase 3 (after-commit) compiler gates do not apply —
C4 is a read-only baseline, no code change.

## Next Steps

1. **[2.0.0_SA_COO / 1.0.0_SA_CTO]** RAVC2 sent — C4 deliverable for review.
2. **[C2 / D1 owners]** Baseline handed off; BF-1 (freshness mechanism for the
   long-TTL `/api/general/*` path) is the action item with the largest blast
   radius for the migration.
3. **[0.3.0_DT — separate handoff]** 0.3.0_DE handoff received: SSCN_UNVREV
   portal revert (DEV 47330865) PROD-ready pending Andrew DEV smoke; portal
   submodule left on PROD branch needs return to DEV — but another pod's
   uncommitted MDPF_ASSETS.033 WIP is in that tree, so the branch return is
   being coordinated, not done unilaterally.
