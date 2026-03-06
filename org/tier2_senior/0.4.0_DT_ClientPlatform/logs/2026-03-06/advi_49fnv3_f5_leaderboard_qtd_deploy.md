# ADVI_49FNV3-F5: Leaderboard QTD Window Deploy -- 0.4.0_DT_ClientPlatform

**Date:** 2026-03-06
**Project:** ADVI_49FNV3
**Fix:** F5 -- QTD/YTD values differ in Q1 2026
**Pipeline:** bd-pipeline
**Lambdas:** bd-portal-publisher, bd-portal-advisor-publisher
**Tag:** bd-v2.17.1

---

## DS Fix (received, committed 7059d1ff)

- bd-portal-publisher: `_leaderboard_entries()` refactored to accept `window_start`
  directly. `build_architect_leaderboard()` adds `qtd` window via `_quarter_start(today, 0)`.
  `available_windows` now includes `'qtd'`.
- bd-portal-advisor-publisher: `_qtd_start(today)` helper added.
  `build_implementor_leaderboard()` loop extended with `('qtd', _qtd_start(today))` pair.
  `available_windows` now includes `'qtd'`.
- Root cause: leaderboard only had rolling windows (3M/6M/1Y/2Y/3Y). Frontend mapped
  qtd -> '3M' (90 days trailing), not calendar Q1. In March 2026: Q1 = ~65 days,
  trailing 3M = 90 days -- different NNA.

## Actions Taken

1. Gate check: both source dirs clean.

2. Build bd-portal-publisher:
   - SHA256: `CPs+K+vGlRH4YV6tlNBFcJhP7wkC5oi3nsRKMq8mjF4=` (changed from `2WIG...`)
   - New S3 version uploaded.

3. Build bd-portal-advisor-publisher:
   - SHA256: `a8nItfw+Ief0szleBe4ZtjwOuNdGlA/0b8mH932xcYg=`
   - New S3 version uploaded.

4. Source map committed: `e2c39ac4` [skip ci].

5. Terraform plan: 2 changes -- both Lambdas updating `source_code_hash` + `s3_object_version`.
   No other drift.

6. Terraform apply: `Apply complete! Resources: 0 added, 2 changed, 0 destroyed.`

7. 0-diff verified: `No changes. Your infrastructure matches the configuration.`

8. record-terraform-deploy.sh: source map + CHANGELOG.json updated, commit `1c06b7d5`.

9. Tag: `bd-v2.17.1` (bd-v2.17.0 already existed for OOM fix; bd-v2.16.x through .4
   consumed by prior deploys).

10. Pushed CLOUD with --follow-tags.

11. Lambda triggers: both invoked async (202) to regenerate leaderboard JSONs.

## Verification Required

After Lambda execution (~1-2 min):
- `architect_leaderboard.json` on S3: `available_windows` should include `'qtd'`,
  `windows['qtd']` should exist with non-zero entries.
- `implementor_leaderboard.json` on S3: same check.
- In March 2026: `windows['qtd'].summary.total_nna` should differ from
  `windows['3M'].summary.total_nna` (Q1 ~65 days vs trailing 90 days).

## Handoff to DE

F5-DE: `periodToChartWindow('qtd')` should now map to `'qtd'` instead of `'3M'`.
The key exists in the leaderboard JSON. DE to wire the frontend mapping per their
task order.

## Deploy History This Session

| Tag | Fix | Lambdas |
|-----|-----|---------|
| bd-v2.16.4 | F1: growth_decomposition (stale S3 version) | bd-portal-publisher |
| bd-v2.17.1 | F5: qtd calendar window in leaderboards | bd-portal-publisher, bd-portal-advisor-publisher |
