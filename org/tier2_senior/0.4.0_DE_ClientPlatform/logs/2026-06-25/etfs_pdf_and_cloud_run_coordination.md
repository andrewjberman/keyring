# ETFS month-end -- PDF output + cloud-run (monthly, last-day) coordination with 0.5.0

**archetype:** MIXED
**secondary_archetypes:** IMPLEMENT, COORDINATE
**Serial:** 0.4.0_DE_ClientPlatform | **Date:** 2026-06-25 | **Window:** 20:40Z -> 21:35Z (since 2d146dbfd)

## Summary
Andrew approved the month-end shape -> asked for PDFs, then to productionize the generation in the cloud (last day of every
month, SVGs/PDFs to a bucket, "work with 0.5.0"). Delivered: PDF output (print CSS + headless-Chromium), made the renderer
cloud-portable, designed the cloud-run, and coordinated the full build with 0.5.0 (compute-pattern decided, entrypoint handed
off). Plus confirmed + hardened the daily-row stores for Andrew.

## Current State (handoff)
- **PDFs:** `ETFS_month_end_2026-05.pdf` + `_2026-06.pdf` on Andrew's Desktop -- clean 5-page landscape decks (marquis / summary /
  charts / per-client-ETF / daily register), SVG+Lato+brand+logo preserved. Generated via `render_month_end.py --pdf` (headless
  Chrome print-to-pdf) + the `@media print` stylesheet (landscape 13.33x7.5in, one slide per full-bleed page, charts trimmed --
  killed the orphan footnote page). Playwright-QA'd page-by-page.
- **Renderer cloud-portable** `data/etfs/scripts/presentation/render_month_end.py` (@ 76efed220): `_find_chromium()` locates
  Linux distro-chromium + playwright-bundled binary (+ `--no-sandbox`/`--disable-dev-shm-usage`) alongside Windows; the cloud
  monthly entrypoint -- `--month YYYY-MM|current|last` (current = the cron(L) last-day month), `--out` optional (temp default),
  `--s3-out s3://bucket/prefix` uploads HTML(+PDF) -> `{prefix}/{YYYY-MM}/etf_ownership.{html,pdf}` (ContentType set). Cloud path
  is boto3+json+stdlib only (pandas/pyarrow are lazy-imported inside the preview-only `load_inf_canonical`).
- **Cloud-run design** `data/etfs/ETFS_monthly_report_cloud_run_design.md` (@ a784b4bd4). 0.5.0 DECIDED (212608Z): **Pattern A =
  transient EC2 + chromium** (reuse the proven `infra/aws/ec2/astn-wsjft/` playwright+headless-chromium pattern; EventBridge
  start->SSM run->self-stop). EventBridge `cron(0 23 L * ? *)` (last day). Output `opal-data-etfs/platinum/reports/{YYYY-MM}/`,
  etfs-reader IAM (read etfs/Dynamo, write reports/ only, zero firm-bucket), CVO internal-only cert. The exact SSM invocation
  handed to 0.5.0: `render_month_end.py --month current --pdf --s3-out s3://opal-data-etfs/platinum/reports/` (NO
  --inf-canonical-preview in cloud).
- **Daily-row stores CONFIRMED live** (for Andrew): DynamoDB `opal-etfs-ownership-daily` = 396 rows (PK client#etf / SK date +
  GSI-etf + GSI-client; describe-table ItemCount lags ~6h, real scan=396). Source = S3 `opal-data-etfs/daily/{partner}/{date}.json`
  (producers write daily -> fan-in -> Dynamo). inf daily now 52 files (05-01 program-start backfill landed -> $7.49M May).
- **HYGIENE FINDING routed to 0.5.0:** the stray `daily/inflection/holdings_2026-06-24.json` (non-date key) is still in S3 AND
  leaked into Dynamo as 4 malformed-SK rows (`inflection#{ETF}/holdings_2026-06-24`) -- the fan-in lacks the date-key guard the
  dashboard reader has. Would break the monthly producer's date-range query. Asked 0.5.0 to guard the fan-in + scrub the 4 rows +
  the stray S3 file.

## Compiler Tools
| Tool | Target | Result | Note |
|---|---|---|---|
| `comp-grep` / `comp-glob` | chromium/pdf precedent + ETFS infra | PASS | found the ASTN-WSJFT transient-EC2+playwright-chromium pattern = the cloud-run blueprint |
| `ds-commit-gate` | every render_month_end.py edit | PASS | py_compile + ruff py39 clean each commit |
| playwright (screenshot) | June PDF/HTML page QA | PASS | visual QA of brand+logo+charts+pagination (full-page + charts-slide clip) |
| aws dynamodb/s3 (operational) | Dynamo count + S3 daily slices + stray | PASS | confirmed 396 Dynamo rows + caught the stray-row pollution -- operational data-plane reads |

**What worked:** the ASTN-WSJFT precedent gave 0.5.0 a proven cloud-chromium pattern (no chromium-in-Lambda gamble); headless-Chrome print-to-pdf preserved the SVG/Lato/brand exactly. **What failed:** matplotlib still absent (inline-SVG path stands); a `--scan-index-forward false` CLI quoting slip (used `--no-scan-index-forward`). **Gap:** the fan-in date-key guard (routed to 0.5.0) -- a producer-input-shape validation the dashboard reader had but the Dynamo writer didn't.

## Blockers
None. Event-gated: 0.5.0 provisions the transient-EC2 + EventBridge + IAM + the fan-in guard/cleanup + the inf-05-01 re-fan-in; DS re-runs AVGCAP May full-window; CVO internal-only cert; Andrew reviews the Desktop PDFs.

## Next Steps
- **[0.5.0_AE_OpalETL]** provision Pattern-A (transient EC2 + chromium) + EventBridge cron(L) + SSM doc (the handed invocation) + etfs-reader-write-reports IAM + deploy ledger; add the fan-in date-key guard + scrub the 4 stray Dynamo rows + the stray S3 file; re-fan-in inf 05-01..14.
- **[0.4.0_DE]** on 0.5.0's box-ready: confirm `--pdf`/`--s3-out` run green on the EC2 (chromium-found, reports/ write) + diff the first cloud PDF vs the Desktop PDFs; any entrypoint tweak to the EC2 shape.
- **[3.0.0_SA_CVO]** internal-only firm-sep cert on the reports/ artifact + the COT-staleness mechanism grounding (prior).
- **[Andrew]** review the Desktop May/June PDFs; the cloud job lands the monthly PDFs in opal-data-etfs/platinum/reports/ once 0.5.0 deploys.
