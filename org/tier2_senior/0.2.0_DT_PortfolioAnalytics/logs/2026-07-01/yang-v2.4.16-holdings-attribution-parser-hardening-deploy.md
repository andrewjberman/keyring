# yang-v2.4.16 holdings-attribution parser hardening -- forensic + deploy + served-data confirm
**archetype:** MIXED
**secondary_archetypes:** DIAGNOSE, DEPLOY, VALIDATE

**Agent:** 0.2.0_DT_PortfolioAnalytics
**Date:** 2026-07-01
**Window:** since my prior log (1d711172f MDPF-P1 + QTD/YTD) -> now. Andrew-direct: compare attribution files Mar-Jun to test "May red herring" hypothesis, then ship the parser hardening, then confirm served-data repopulation.

## Summary

Forensic-compared 6 monthly attribution Excel files (Jan-Jun 2026) -> REFUTED Andrew's
"May was the format mistake, June reverted to old format" hypothesis: Jan-May are ALL identical
(portfolio "vs Benchmark" headers at cols 5/16/27); JUNE is the lone anomaly (shifted left 3 ->
2/13/24). Shipped yang-v2.4.16: widened the holdings-attribution parser's format-DETECTION to
scan all columns (was fixed [5,16,27]). Full DT deploy cycle + deploy-ledger CLOSED. Re-triggered
the pipeline (via manifest.json, not the inert xlsx-drop) -> SFN SUCCEEDED -> served
allocation_summary CONFIRMED repopulated (5 portfolios). Attribution un-blanked live.

## Part 1 -- Forensic (DIAGNOSE): which month is the anomaly?

Pulled month-end files from data-refresh/archive/exec-*/ + uploads/, ran each _QTD sheet through
the parser's own detection logic (openpyxl):

| File | _QTD hdr row | portfolio-block cols | parser [5,16,27] |
|---|---|---|---|
| Jan 20260131 | 4 | 5/16/27 | detects |
| Feb 20260228 | 6 | 5/16/27 | detects |
| Mar 20260331 | 6 | 5/16/27 | detects |
| Apr 20260430 | 6 | 5/16/27 | detects |
| May 20260531 | 6 | 5/16/27 | detects |
| **Jun 20260630** | 6 | **2/13/24** (-3 shift) | **MISS -> 0 models** |

Conclusion: May is NOT a red herring -- it matches Jan-Apr exactly. June is the sole deviation
(every portfolio block shifted left by 3 cols; NOT a revert -- no prior month was ever at 2/13/24).
Parser detection cols [5,16,27] set by f7d892052 (2026-03-02), stable + consistent with Jan-May.

## Part 2 -- Parser hardening (DEPLOY): yang-v2.4.16

Fix (parse_period_sheet detection, lines ~216): `for col_idx in [5,16,27]` -> `for col_idx in
range(df.shape[1])` (scan ALL columns). The extractor (parse_period_sheet_horizontal) already
full-column-scans + maps headers to model codes, so widening detection is sufficient; stray hits
filtered there. Output shape unchanged (comp-blast: no breaking edges).

Local validation (imported the edited module, real archived files): JUN 20260630 now extracts
5 models [INT,LTA,LTC,ST,UST] across _QTD/_YTD/_1Y/_SI (was 0); Jan/Feb/Mar/Apr/May still 5 (no
regression).

### Deployment Sequence + Verification (actual output)

```
1  edit          detection scans range(df.shape[1]) (was [5,16,27])
2  local test    JUN 0->5 models; Jan-May 5->5 (no regression)
3  build+upload   yang-generate-holdings-attribution.zip SHA256 m00Ju4xm9dbNC0NEXk5/MtLUCh0sSoA207DngNHGZ3A=
4  commit source  866583a87 (source + lambda-source-map.json; audited GIT_COMMIT_AUTHOR_OVERRIDE=CLOUD_OPS_OR_ETL)
5  safe-apply     Apply complete! Resources: 0 added, 1 changed, 0 destroyed.
6  0-diff plan    "No changes. Your infrastructure matches the configuration."
7  F5 live        get-function CodeSha256 = m00Ju4xm9dbNC0NEXk5/MtLUCh0sSoA207DngNHGZ3A=  LastModified 2026-07-01T19:49:34Z
8  core doc       deployment_map current_tag 2.4.15 -> 2.4.16 (d1d3f8c4a)
9  record+tag     record-terraform-deploy (CHANGELOG) + annotated tag yang-v2.4.16 -> origin/CLOUD --follow-tags
10 ledger         deploy_ledger CLOSED yang-holdings-attr-parser-hardening 2/2 legs (98e9afc18)
```

## Part 3 -- Re-trigger + served-data confirm (VALIDATE)

- First re-trigger (aws s3 cp June xlsx -> uploads/) was INERT: no SFN execution. Root: the
  yang-pipeline-trigger S3 notification filters prefix `uploads/` + SUFFIX `manifest.json`
  (get-bucket-notification-configuration) -- it fires on a manifest.json, NOT the raw .xlsx.
- Correct re-trigger: uploaded uploads/manifest.json (version 20260701_v2, referencing the
  staged June xlsx; format replicated from archive exec-10bebf4065f6/manifest.json).
- Result: SFN 20260701_v2-f31a558f SUCCEEDED. Served allocation_summary.json = 963 bytes
  (was 93), generated_at 2026-07-01T20:47:44Z, portfolios [UST,ST,INT,LTC,LTA] with populated
  asset_classes (UST FI-only; ST FI+Equity). data_as_of 2026-06-30. CONFIRMED repopulated.

## Compiler Tools

| Tool | Target | Result | Note |
|---|---|---|---|
| comp-blast | yang-generate-holdings-attribution | PASS | blast radius holdings_attribution -> allocation_summary -> portal_data_proxy -> portal; input-side change, no breaking edges (Rule 20 pre-infra) |
| comp-freshness (earlier window) | mdpf/positioning served | n/a | (this window did not re-run; blast covered the graph check) |

What worked: comp-blast confirmed the additive/input-side nature (output shape unchanged) before the infra change. Local module-import test against real archived files was the decisive validation (0->5 models on June, no regression) before deploy. What failed: none. Gap: the parser brittleness itself (fixed-column detection) is now removed. Non-comp verification (openpyxl forensic, aws s3api notification config, SFN status) has no comp-tool -- operational.

## Blockers

None.

## Current State

- yang-generate-holdings-attribution LIVE with hardened detection (scan all cols). CodeSha256
  m00Ju4xm9dbNC0NEXk5/MtLUCh0sSoA207DngNHGZ3A=, tag yang-v2.4.16 on origin/CLOUD. deployment_map
  current_tag 2.4.16. Source infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-holdings-attribution/lambda_function.py.
- Served json/positioning/allocation_summary.json REPOPULATED (5 portfolios, data_as_of 2026-06-30,
  generated 20:47:44Z) via SFN 20260701_v2-f31a558f. Attribution tab renders again.
- FE (prior window): portal DEV 62cdb473 useEffectivePeriod + Attribution wiring guards future
  period-boundary blanks (independent of this data fix).
- A stray uploads/manifest.json (20260701_v2) remains in uploads/ -- the pipeline's cleanup lambda
  normally removes it; harmless if it lingers (idempotent trigger already consumed).

## Next Steps

- [0.2.0_DT_PortfolioAnalytics] (optional, my pipeline) apply the same as-of-anchor Layer-1 fix in
  yang-generate-allocation-summary / -holdings-attribution if we ever want QTD/YTD relative to
  data_as_of at source (deferred; current fix resolves the reported break).
- [Andrew/Yang] going forward, June-layout (2/13/24) now parses -- no re-export needed; but standard
  5/16/27 layout also still works. No action required.
- [0.4.0_DE_ClientPlatform] AdvisorsTab dedup migration to shared useEffectivePeriod (their lane, ACK'd).
