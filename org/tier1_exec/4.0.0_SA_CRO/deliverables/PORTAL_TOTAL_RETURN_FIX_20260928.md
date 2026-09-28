# Portal total-return correction: deployed and verified

Seat: 4.0.0_SA_CRO~I. Authority: Andrew-direct, 2026-09-28.
Production deployment: 2026-09-28T23:25:55Z. Data as of: 2026-09-25.

The two affected Lambda handlers are deployed, their three output objects have
been regenerated, and the Portal cache invalidation is complete. All 1,715
checked published return cells match independent compounding of the pinned
daily total-return inputs. The full, untargeted Yang Terraform plan exits zero
with `No changes. Your infrastructure matches the configuration.`

## What changed

| Lambda | Correction | Portal surface |
|---|---|---|
| yang-generate-positioning | Include the opening day of WTD/MTD/QTD/YTD; use 91 calendar days for 1Q; exclude observations after the requested as-of date | Positioning holdings and Opal aggregate |
| yang-generate-etf-returns | Replace 21/63/252-row trailing periods with 30/91/365-calendar-day windows; sort legacy wide input by date | Model Portfolios Performance ETF comparison |
| yang-model-portfolio-benchmarks | Already correct; production code and JSON unchanged | Model Portfolios Benchmark |
| opal-market-overview-tiered-generator | Already correct; production code unchanged; exercised with the same boundary fixtures | Market Overview |

Daily total returns dated on the first day of a to-date period are included.
Rolling 1M/1Q/1Y exclude their opening cutoff and include their end date. The
existing Benchmark implementation cites Andrew's June 1, 2026 ruling to retain
30/91-calendar-day rolling 1M/1Q. No change to model construction or input source
was needed. Existing since-inception annualization and insufficient-history
policies retain their separate, pre-existing definitions.

## Proof and provenance

| Check | Result | Evidence |
|---|---|---|
| Regression contract | Four tests pass across all four production function implementations, including both ETF input representations | inflection-performance-fix-20260928/test_period_contract.py |
| Negative control | Captured old deployed handlers fail 49 subtest comparisons, with zero execution errors | ROLLBACK.md; ignored snapshot negative_control.txt |
| Positioning | 1,280/1,280 cells match: 640 current_holdings plus 640 mirrored portfolios holdings | published_verification.json |
| Opal aggregate | 240/240 cells match | published_verification.json |
| ETF Performance | 45/45 cells match | published_verification.json |
| Benchmark | 150/150 current cells match; JSON bytes/version unchanged | published_verification.json |
| Deployed code | Both ZIPs' complete member sets equal local source bytes; ZIP SHA256 equals Lambda CodeSha256 | deployed_provenance.json |
| Infrastructure | Saved plan: zero add, two code updates, zero destroy; full post-apply plan: zero differences | terraform_plan.json; deployment_checks.json |
| Cache | EVTSA9VEHNZVH invalidation IA4G138SBPNP00E74PL6N1R5UI Completed; six request/rewrite paths, including query variants | cache_invalidation.json |

Evidence filenames in this table are under `inflection-performance-fix-20260928/`.
The input chain is documented in `RCN-0019_INFLECTION_PORTAL_PERFORMANCE_20260928.md`
and `inflection-performance-audit-20260928/source_provenance.json`: Bloomberg
`DAY_TO_DAY_TOT_RETURN_GROSS_DVDS`, matching local/S3 PKLs, deployed consumers,
published JSON and Portal field bindings. The correction compounds those same
income-inclusive returns; it does not derive returns from PX_LAST.

Source objects: `s3://opal-data-portal-v2/benchmarks/model_20260925_v1.pkl`
(version `7g8i_WYpykY7zpDWFpa8sH6ndmWwqkUe`) and `data_20260925_v1.pkl`
(version `H7ZfeDOVxcNmnSzIWI_QqN55gQIDzfa7`). SHA256s are recorded in
published_verification.json. Input keys and all new output versions are in
deployed_provenance.json; pre-deploy recovery versions are in predeploy_versions.json.

Examples at the unchanged September 25 as-of date: VGSH WTD is now -0.02%
(previously -0.07%), VGSH MTD -0.52% (previously -0.43%), and VCSH MTD -1.06%
(previously -0.87%). The ETF comparison's VGSH 1Y is now 1.74%, from 1.66%,
because the window is now 365 calendar days. YTD values and Benchmark data did
not require a numerical correction in this snapshot.

## AUM input change checked separately

Regeneration picked up the existing live AUM source's September 25 version,
replacing September 24 weights used by the prior run. This changed five model
AUM fields and aggregate weights/membership totals. A read-only replay of the
old deployed handler, using the exact new AUM version and intercepting all S3
writes locally, reproduces EVERY non-return field in the new published outputs.
There are zero unexplained non-return differences. See controlled_replay.py and
controlled_replay.json. The pinned AUM object is
`platinum/mdpf/global/aum-metrics.json`, version `N_KOsRfVbwJr7danRAxFjAmYOfhCViGu`.

## Deployment record and limits

Source commit `978e4b0eec`; artifact/contract commit `58162c16ed`; scoped deploy
record `652cf48876`; local tag `yang-v2.4.20`. The recorder updated exactly 2 of
28 Yang entries and preserved the other 26. The deploy ledger
`org/critical_paths/change_management/20260928T2314Z_portal-total-return-20260928-croi_deploy_completion.md`
is CLOSED with all six legs proven. Rollback instructions and old versions are
preserved; no rollback was needed. Commits/tag remain LOCAL; no Git push was made.

This is implementation plus self-verification against deployed code and live
output objects, not an independent CVO review. An authenticated browser was not
available; no visual render is claimed. The deployed router and source bindings
were traced, the S3 origin objects were verified, and their cache invalidation
completed. The prior audit's upstream 2.36-basis-point model-versus-weighted-ETF
YTD difference and the downloader's unflagged missing-total-return fallback
remain separate provenance limitations; neither is the corrected date-boundary
defect or evidence that the Portal omits income in the verified snapshots.
