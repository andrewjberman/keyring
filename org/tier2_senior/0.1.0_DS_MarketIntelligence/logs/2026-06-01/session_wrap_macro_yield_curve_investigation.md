# Session Wrap — Macro-Page Yield-Curve Investigation (2026-06-01)

**archetype:** DIAGNOSE
**secondary_archetypes:** IMPLEMENT, COORDINATE

Andrew-direct macro-investigation lane (spawned by MSTR, TO'd by ws CTO). Joined 0.5.0_AE_OpalETL (lead) on the portal Macroeconomics-page anomaly. Net: the assigned sub-problem (yield-curve 1Y-ago missing tenors) is root-caused, fixed, pre-validated, and handed to AE for an Andrew-gated deploy.

## Arc of the session

1. **Startup** — /watcher self-heal (registered LIVE PID 16996; killed an auto-respawn watcher; tracked watcher relaunched), org/XXX.md protocol, identity (Tier-2 DS, Market Intelligence pod). Andrew flagged that I'd over-invested in startup ceremony while three CTO TOs sat unread; pivoted to the work.
2. **Task refinement** — three CTO messages: the original macro May-blank/June-filled TO was superseded. The May-blank half is genuine release-lag (AE answered separately + shipped a fix). My active scope became the **yield-curve 1Y-ago missing-tenors** regression, with Andrew's amplified hypothesis = a TF-module / artifact-path swap.
3. **Diagnosis** — traced producer -> artifact -> FE; pulled the live + 4 historical S3 versions; replicated the FE 1Y-ago selection logic.
4. **Fix** — authored retry+backoff + merge-preserve in the ingest; ds-commit-gate PASS; pre-validated 10/10 offline against real artifacts.
5. **Handoff** — owned-paths blocked DS from infra/aws (AE lane); handed code to AE (ACK'd with deploy plan). Deploy is COO-surfaced + Andrew-gated safe-hold during wind-down.

## Root cause (verdict)

The 1Y-ago yield curve dropped tenors because `ingest_yield_curve_fred.py` uploads a **partial combined artifact** whenever a daily FRED fetch fails for a DGS series (no retry), clobbering the prior good `json/macro/yield_curve_fred.json`. The empty-tenor set **varies day to day** (S3 versions: Jan15 frozen=10/10; May27=3Y; May30=20Y+30Y; May31=1M+3Y+10Y). `DGS10` empty is impossible as a real FRED gap -> proves fetch-failure, not data-absence. FE `getOneYearAgoValue()` returns null for an empty array -> tenor drops from the red 1Y-ago line.

- **NOT a TF/path swap** (Andrew's hypothesis, refuted by `comp-lambdamap check` — only seeking-alpha drifts; fred-data-ingestion clean).
- **Onset = May21** (`fae806585`) when the dormant runner was revived — a correct staleness fix that exposed a latent partial-overwrite bug.
- **Resolves the CTO<->Andrew missing-set mismatch** ({1M,3Y,10Y} vs {1M,3Y,20Y,30Y}): the set genuinely changes daily; Andrew viewed ~May30, CTO+I read May31.
- **Architecture note**: the panel is two-source — Current/1M from Yang PKL, 1Y-ago only from FRED — so "current full / 1Y-ago partial" is by-design, not an artifact repoint.

## Fix (CTO-approved, authored, pre-validated)

`infra/aws/lambda/fred-data-ingestion/ingest_yield_curve_fred.py`:
1. `fetch_series` — 3x retry + exponential backoff (transient FRED 5xx/timeout).
2. `run()` — no-regression merge-preserve: carry forward the prior artifact's series for any tenor still empty after retries (1Y-ago is HISTORICAL/immutable -> zero fabrication; data-honesty bar satisfied) + NO-REGRESSION GUARD log of residual empties.
3. `upload_to_s3` — `preserved_tenors` metadata + per-tenor `PRESERVE` WARN (CTO-required observability so chronic FRED failures stay visible).

**Pre-deploy validation (offline vs real artifacts):** May31 partial (empty {1M,3Y,10Y}) + May30 or Jan15 prior -> complete 10/10, preserved_tenors=[1M,3Y,10Y]; carried 1Y-ago points are real immutable FRED obs (1M@2025-06-02=4.33, 3Y=3.91, 10Y=4.46).

## Briefs Written

| Brief | Path | Audience |
|-------|------|----------|
| DevOps deploy + exact diff + validation | `docs/briefs/devops-brief-yield-curve-fred-partial-overwrite-fix.md` | 0.5.0_AE_OpalETL (deploy), CTO/COO |
| Root-cause investigation log | `org/tier2_senior/0.1.0_DS_MarketIntelligence/logs/2026-06-01/yield_curve_1y_ago_missing_tenors_root_cause.md` | Reference |

## Files Modified

| File | Change |
|------|--------|
| `infra/aws/lambda/fred-data-ingestion/ingest_yield_curve_fred.py` | retry+backoff in fetch_series + merge-preserve guard in run() + preserved_tenors metadata in upload_to_s3. AUTHORED + ds-gate PASS; staged in working tree (AE owned-paths lane — AE commits+deploys). |
| `docs/briefs/devops-brief-yield-curve-fred-partial-overwrite-fix.md` | New brief (committed 742a71509 + validation update 921a80ac3). |
| `org/tier2_senior/0.1.0_DS_MarketIntelligence/logs/2026-06-01/yield_curve_1y_ago_missing_tenors_root_cause.md` | New root-cause log (committed 742a71509). |

Commits (my author line): `742a71509` (log + brief), `921a80ac3` (brief validation update). Code fix NOT yet committed — AE owns the infra/aws commit + deploy.

## Compiler Tools

| Tool | Result | Note |
|------|--------|------|
| `comp-lambdamap check` | seeking-alpha drift only; fred-data-ingestion CLEAN | Refuted the TF/source_dir path-swap hypothesis for the yield-curve lambda. |
| `comp-trace yield_curve --direction both` | no node matching `yield_curve` | Artifact key not graphed; traced manually instead. |
| `comp-pipescript io <ingest>` | lambda_pipeline_script; I/O not detected (self.s3_client attr-pattern) | No column-gap signal; the only follow-on is the IAM note (new get_object needs s3:GetObject) — flagged to AE. |
| `.tools/ds-commit-gate.sh <ingest>` | All checks passed (exit 0) | py_compile + ds-precommit-check + ruff. |

## Current State

- Yield-curve fix COMPLETE on the DS side: authored, gate-passed, pre-validated 10/10, briefed.
- Deploy = COO-surfaced + Andrew-gated safe-hold (drive cycle28 `55b9934b8`); fabric in wind-down. Not a blocker.
- AE ACK'd with a concrete deploy plan (commit --only + Lambda deploy + verify 10/10 + RAVC back).

## Next Steps

1. [AE OpalETL] Commit `ingest_yield_curve_fred.py` (--only, DS authorship credited) + deploy via fred-pipeline TF/Lambda path; confirm `s3:GetObject` in role (comp-iam service) for the merge-preserve read; verify deployed lambda re-pulls 10/10. Exact steps in the devops brief.
2. [DS self] RAVC-close the moment the deployed `yield_curve_fred.json` reads 10/10 + `preserved_tenors` populated as expected.
3. [Andrew] push-vs-ride decision on firing the deadline-free yield-curve deploy now vs next cycle (wind-down).
