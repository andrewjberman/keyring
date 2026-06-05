# Yield-Curve 1Y-Ago FE Smoke — Andrew-escalated DRIVE

**archetype:** VALIDATE

## Task
Andrew-escalated: Macro yield-curve "1Y-ago" line was broken (1Y node missing). Data-layer
fix deployed + CVO-PASS by 0.7.0_AE; CloudFront force-invalidated. My job: FE visual smoke the
user-facing result, RAVC2 to COO 2.0.0 + CTO 1.0.0.

## Result: PASS (rendered-correctly, no defect). Escalation closed user-facing.

## What I verified

### 1. Served origin (data layer, independent re-check)
- `aws s3 cp s3://opal-data-portal-v2/json/macro/yield_curve_fred.json` -> all 10 tenors present
  incl **US Treasury 1Y = 498 obs** (last 2026-06-03 = 3.84). `data_as_of` 2026-06-05,
  `generated_at` 2026-06-05T15:50Z (fresh).
- Simulated the FE `getOneYearAgoValue()` logic (today-365d, within-7d window) for every tenor:
  closest 1Y-ago date 2025-06-05, 0 days off -> non-null for **all 10** tenors incl 1Y. So no
  node would gap.

### 2. FE render (visual smoke)
- localhost:5175 DEV portal (portal tree on DEV per Rule 19), Playwright MCP under Node+Edge
  (headless-smoke resolution), authenticated via the sanctioned smoke account real-JWT login
  (devBypass token is rejected by the new auth-validator-edge universal JWT gate on /api/general/*).
- Console: `[yield-curve] Loaded FRED yield curve data` (success).
- "1Y Ago" toggle is enabled (`hasOneYearData=true`; label "1Y Ago" not "(N/A)", cursor=pointer).
- DOM geometry of the red 1Y-ago line (#ef4444, dash 5/5): **subpaths:1 (continuous, NO break),
  9 segments, nodeCount:10** = a node at every tenor incl the restored 1Y. `connectNulls=false`
  would split the path into multiple subpaths if 1Y were null — it did not.
- X-axis ticks: 1M, 3M, 1Y, 2Y, 3Y, 5Y, 7Y, 10Y, 20Y, 30Y (all 10).
- Tooltip @30Y: Current 4.97 / 1M 4.97 / **1Y Ago 4.88** (== S3 origin) / 1Y Change +9 bps.
- No stale-cache artifact; Current + 1M + 1Y all fresh and continuous.
- The 2 console "errors" = pre-login `/auth/refresh` 401s (no token yet — benign, expected before
  login). recharts `width(-1)` warnings = transient ResponsiveContainer measure on tab mount.
  Neither is data-related.
- Screenshots: `ajb_workspace/yield-curve-1y-ago-fullchart-20260605.png` (full chart + x-axis +
  tooltip) and `-smoke-` viewport variant.

## Coordination
- Served-path coordinated with 0.7.0_AE (LIVE; owns CloudFront/data-proxy; yield-curve fix CVO-PASS).
- Auth note for fabric: `/api/general/*` now sits behind the auth-validator-edge universal JWT gate.
  Anon CDN fetch -> 401; the dev `devBypass` fake token is also rejected. FE smokes of general data
  must use a real-JWT login (smoke-account form-login) OR verify served origin via S3.

## RAVC2
- Primary CLOSE -> 2.0.0_SA_COO (`20260605T161836Z`).
- CC -> 1.0.0_SA_CTO (`20260605T161844Z`).

## Compiler Tools
None run this session. Pure FE visual-smoke / served-artifact validation — no gold-script edit,
no portal-component schema change, no fetch/endpoint change, no IAM/infra touch. The validation
axes used were the served S3 artifact + live DOM render geometry, which the comp-* catalog does
not cover (comp-transform schema-check etc. are for component-prop wiring changes, not a read-only
render smoke of unchanged code).
