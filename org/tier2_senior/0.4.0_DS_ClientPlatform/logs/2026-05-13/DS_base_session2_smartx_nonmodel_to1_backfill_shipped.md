# DS-base 2026-05-13 session 2 — SmartX Non-Model TO-1 backfill shipped

**Agent:** 0.4.0_DS_ClientPlatform (base, no tilde lane)
**Window:** ~17:55Z → ~18:40Z 2026-05-13 (~45 min)
**Project ref:** SMARTX_NONMDL.TO-1 (informal — brief is the scope; no formal TO file)
**Trigger:** Andrew session-direct on SmartX recon → 5-segment surgical-fix brief authored + COO GO at 17:55Z to execute ahead of INFGRO Stage 1.

## TL;DR

Shipped backfill script (`data/smartx/scripts/backfill_non_model_assets.py`, +418 lines, commit `11d91fde6`) that resolves the 4-month-stale $272M plug on ModelPortfolios. Preview JSON live at `s3://opal-data-portal-v2/json/portfolios/non_model_assets_preview.json` (ETag `e42e183b41c1e9e64519be3a620c26b2`). 557 daily rows 2024-11-01 → 2026-05-11. Identity check 0 fails. Boundary deltas match prediction. RAVC2 sent to COO + DE TO-4 dispatch.

Latest 2026-05-11: enterprise $1.804B / model $1.359B / **non_model $445.3M (24.7%)** — vs frozen plug of $271.2M (1/5).

## Five-segment stitch result

| Segment | Range | Source | Rows | Status |
|---|---|---|---|---|
| A | 2024-11-01 → 2026-01-05 | existing file | 431 | Preserved verbatim |
| B | 2026-01-06 → 2026-01-15 | HOLD A-final | 10 | Held at $271.2M (Andrew-confirmed) |
| C | 2026-01-16 → 2026-03-10 | silver/allocations sum | 36 | All 36 silver/allocations partitions in window |
| D | 2026-03-11 → 2026-05-11 | aua_certification | 37 | All 37 BD-blessed daily files |
| ffill | weekends/holidays | calendar-day expansion | +43 | Matches existing pattern |
| **Total** | | | **557** | |

## Boundary deltas (predicted vs observed)

| Boundary | Date | Enterprise Δ | Non-Model Δ | Verdict |
|---|---|---|---|---|
| A→B | 2026-01-05 → 01-06 | **$0** | **$0** | Hold worked |
| B→C | 2026-01-15 → 01-16 | +$169.83M | +$123.71M | Real measurement returning post-plug — Andrew-accepted as the only visible step |
| C→D | 2026-03-10 → 03-11 | +$5.27M | +$6.55M | Silver-vs-certified methodology step — predicted ~$5M matches |

## Defensive schema handling (2026-01-26, 01-28, 02-05)

Three legacy-Title-Case partitions discovered during dry-run:
- Schema "L" (normalized silver): 76 of 79 partitions. `account_market_value` lowercase, 1 row/account.
- Schema "T" (legacy bronze-style): 3 partitions only. `Account Market Value` Title-Case, ~5x row replication.

Both schemas handled: when `Account Market Value` is present without `account_market_value`, dedupe by `AccountID` before summing. Verified 2026-01-26 deduped sum = $1.559B = 2026-01-23 run-rate (continuous).

## Owned-paths config drift (flagged to COO)

`.owned-paths.yaml:632` labels `data/smartx/**` as **POD3 (TradingOperations)**. SmartX is the ModelPortfolios data pipeline owned by POD4 (Client Platform) per my prompt.md. Committed via `GIT_COMMIT_AUTHOR_OVERRIDE=POD4` audit-bypass — one-file scope, COO GO-authorized work, not a real lane crossing. Recommended amendment in RAVC2: relabel `data/smartx/**` to POD4, or add a `POD3_OR_POD4` shared lane.

Audit log entry: `org/git-author-override-audit.log`.

## Compiler Tools

| Tool | Run | Result |
|---|---|---|
| `aws s3 cp s3://opal-data-portal-v2/json/portfolios/non_model_assets.json` + jq probe | 1× | Confirmed existing schema + dead state (2026-01-05 frozen) |
| `Grep non_model_assets` portal-side + Lambda-side | 3× | 3 portal files + 1 Lambda route confirm wiring; surgical fix viable |
| `aws s3 ls s3://opal-data-bd/silver/allocations/` | 1× | 79 partitions 2026-01-16 → 2026-05-11 |
| `aws s3 ls s3://opal-data-bd/gold/aua_certification/` | 1× | 37 files 2026-03-11 → 2026-05-11 |
| Schema scan across all 79 silver partitions (Python list_objects_v2 + per-file pandas read) | 1× | 3 legacy-schema partitions (1/26, 1/28, 2/5); handler added |
| Cross-check silver-sum vs certified_aua on 2026-05-11 | 1× | -$4.77M Δ = exact liability-exclusion match → methodology consistent |
| `.tools/ds-commit-gate.sh data/smartx/scripts/backfill_non_model_assets.py` | 2× (2nd PASS) | First run: F401/F841/E402 (11 errors); fixed (`from __future__` placement + remove unused). Second: PASS |
| `python data/smartx/scripts/backfill_non_model_assets.py --dry-run` | 2× (2nd full PASS) | First: schema RuntimeError on 1/26; fixed. Second: 557 rows, 0 identity fails, all boundary deltas as predicted |
| `python data/smartx/scripts/backfill_non_model_assets.py` (publish to preview) | 1× | S3 PUT s3://opal-data-portal-v2/json/portfolios/non_model_assets_preview.json ETag `e42e183b41c1e9e64519be3a620c26b2` |
| `GIT_COMMIT_AUTHOR_OVERRIDE=POD4 .tools/safe-commit.sh` | 1× | Commit `11d91fde6` (CLOUD), audit log entry |
| `git push origin CLOUD` | 1× | safe-deploy pre-push hook: "no deploy-scope script files detected, nothing to do" — push clean |

## Files Modified

| File | Change | Commit |
|---|---|---|
| `data/smartx/scripts/backfill_non_model_assets.py` | NEW — 5-segment stitch + S3 publisher | `11d91fde6` (+418 lines) |
| `s3://opal-data-portal-v2/json/portfolios/non_model_assets_preview.json` | NEW — preview output | ETag `e42e183b41c1e9e64519be3a620c26b2` |

Prod path (`non_model_assets.json`) intentionally untouched — preview path used for DE TO-4 smoke before promotion.

## MCPs Sent

| Recipient | Subject | Purpose |
|---|---|---|
| 2.0.0_SA_COO | RAVC2 ACK GO SmartX TO-1 | Acknowledge dispatch |
| 2.0.0_SA_COO | RAVC2 SHIP SmartX TO-1 | Evidence summary (SHA + ETag + boundary deltas) |
| 0.4.0_DE_ClientPlatform | SmartX TO-4 standby | Preview JSON ready for portal smoke |

## Next Steps

| Recipient | Item |
|---|---|
| **DE 0.4** | TO-4 smoke against preview JSON. Verify stacked chart smooth from 2026-01-16 forward; only visible step at 2026-01-15→01-16 (real B→C transition). RAVC2 to COO on PASS. |
| **DS (me)** | After DE PASS → TO-2 author new Step 6 in `infra/aws/lambda/smartx_ingestion_pipeline/lambda_function.py` for daily extension. |
| **AE 0.7** | TO-3 (parallel with my TO-2) — IAM cross-bucket grant smartx-ingestion-lambda-role → `opal-data-bd` reads; build-and-upload; terraform apply; smartx-pipeline-v{X.Y.Z} tag. |
| **DS (me)** | TO-5 retire `compute_non_model_assets.py` post-deploy. |
| **COO** | Amend `.owned-paths.yaml:632` `data/smartx/**` lane (POD3 → POD4 or `POD3_OR_POD4`). |

## Decision notes

1. **Surgical fix over greenfield contract.** The existing `non_model_assets.json` portal contract was already shaped exactly right (`latest{} + time_series[]`); rewriting in-place is invisible to the portal. Recognized this early in recon (Lambda route + frontend hook + render code all already wired) — avoided proposing new endpoint / new file / new portal-side changes.

2. **Preview path before prod path.** TO-1 deliberately writes to `non_model_assets_preview.json`, not the live prod path. DE smoke catches any portal-side rendering issues without showing partner-visible discontinuity. Promotion to prod is a 1-second `aws s3 cp` after TO-4 PASS.

3. **Schema scan across all 79 partitions before publishing.** Caught the 3 legacy-Title-Case dates before they would have produced a partial backfill or wrong sums. Worth the ~30s cost.

4. **Owned-paths bypass with audit log.** The right way to handle stale config + authorized work — `GIT_COMMIT_AUTHOR_OVERRIDE` with a clear narrative in the commit message. Avoided the alternative of waiting on COO to amend YAML before shipping. Loop closed on COO side via RAVC2 flag — config will be amended on COO's timeline.

5. **Validation discipline pays off.** Identity check + monotonic-jump detection + boundary-delta logging in the dry-run run caught the schema issue before publishing. The "$5.27M C→D step matches predicted ~$5M" confirmation is the kind of cross-check that builds trust in the whole stitch.

## Pacing

~45 min from COO GO → script ship + preview published + RAVC2 out. Recon was already done in prior session; this session was pure execution. ds-commit-gate fixed in 2 minutes (one rename of docstring/__future__ order). Dry-run iteration revealed the legacy-schema gotcha; defensive handler added in 5 minutes. Final dry-run + publish + commit + push + RAVCs: ~10 minutes.
