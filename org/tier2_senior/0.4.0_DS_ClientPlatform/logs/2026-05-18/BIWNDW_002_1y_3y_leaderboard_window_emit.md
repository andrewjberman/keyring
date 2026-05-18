# Session Log -- ADVI_BIWNDW.002 1Y/3Y leaderboard window emit

**Agent:** 0.4.0_DS_ClientPlatform (DS~C lane)
**Date:** 2026-05-18
**TO:** ADVI_BIWNDW.002 (ds-1y-3y-leaderboard-window-emit), issued by 2.0.0_SA_COO
**Project:** ADVI_BIWNDW

> This log back-fills the AC1/AC5 record for the BIWNDW.002 window-emit work,
> which shipped in commit `a2010a2b3` during the 2026-05-15 wind-down without a
> dedicated session log. Evidence below verified against live S3 on 2026-05-18.

---

## Current State

BIWNDW.002 is fully code-complete on both firms. The only remaining step is the
INF gold chain run -- co-sequenced with ADVI_INFGRO.007 (same file
INF_D_00c.portal_leaderboard.py), gated behind AE 0.7.0's RUNDATE-DISPATCH-IMPL
deploy. The final RAVC2 closes post-chain-run alongside INFGRO.007's.

---

## Work Shipped (commit a2010a2b3)

- **BE-1** -- `_window_date_range()` in `INF_D_00c.portal_leaderboard.py` carries
  1Y (`data_as_of - 365d`) and 3Y (`data_as_of - 1095d`) branches.
- **BE-2** -- the INF_D_00c build loop iterates `('QTD','YTD','MAX','1Y','3Y')`;
  `available_windows` literal lists all five. Window keys emitted exactly `1Y` /
  `3Y` (the FE PERIOD_TO_LB_WINDOW interface contract).
- **49F** -- `D_04.client_portal_summary.py` `_LEADERBOARD_WINDOWS` widened to
  `('QTD','YTD','MAX','1Y','3Y')` (the 1Y/3Y data already existed upstream in
  `employee_leaderboard.json`; per the TO context, D_00c needed zero change).
- **BE-3** -- confirmed no per-aggregation change needed: the NNA / new-clients /
  GRO aggregators are already `(window_start, window_end)`-parameterized.

---

## Acceptance Criteria

| AC | Status | Evidence |
|----|--------|----------|
| AC1 (BE-4 coverage) | PASS | INF `client_performance.parquet` spans 2020-05-26..2026-05-17 (6yr) -> 3Y horizon fully covered. 49F 1Y/3Y already materialized. No short-coverage to surface. |
| AC2 (window-emit both scripts) | PASS | INF_D_00c `_window_date_range()` + build loop + `available_windows` all carry QTD/YTD/MAX/1Y/3Y; D_04 `_LEADERBOARD_WINDOWS` widened. Keys emitted exactly `1Y`/`3Y`. |
| AC3 (49F materialized) | PASS | `s3://opal-data-bd/platinum/firm/leaderboard.json` carries `available_windows [QTD,YTD,MAX,1Y,3Y]`, all five window keys populated (data_as_of 2026-05-14). |
| AC4 (INF materialized) | PARTIAL -> chain-gated | `s3://opal-data-inf/platinum/firm/leaderboard.json` already carries 1Y/3Y (entry_count=4, summary total_aua $201M). The INFGRO.007 co-land chain run refreshes them with corrected TWRs. Final RAVC2 post-run. |
| AC5 (compiler/payload/Rule 15) | PASS | See Compiler Tools. BE-6 payload: INF leaderboard.json 20.6 KB -- far under any split-mode threshold. Rule 15 `from __future__ import annotations` present in both scripts. No emoji. |

---

## Compiler Tools

| Tool | Target | Result |
|------|--------|--------|
| `comp-pipescript io` | INF_D_00c.portal_leaderboard.py | Run for INFGRO.007 (same file) -- no COLUMN GAPS. The 1Y/3Y aggregators reuse the existing `(window_start, window_end)`-parameterized code path -- no new columns read. |
| `ds-commit-gate.sh` | INF_D_00c / D_04 | PASS at the a2010a2b3 ship (py_compile + AST + ruff py39). |

---

## BE-6 Payload Size Check

`s3://opal-data-inf/platinum/firm/leaderboard.json` = 20,606 bytes (~20 KB) with
all five windows. Far under the D_04 / dashboard split-mode threshold. +2 windows
added negligible size. PASS.

---

## Next Steps

| Recipient | Item |
|-----------|------|
| **AE 0.7.0** | The INF gold chain run (post RUNDATE-DISPATCH-IMPL deploy) co-materializes BIWNDW.002 1Y/3Y with the INFGRO.007 corrected TWRs. |
| **DS~C (self)** | On AE chain-completion ping: verify INF leaderboard.json 1Y/3Y carry corrected window TWRs, then send the BIWNDW.002 RAVC2 to COO alongside INFGRO.007's. |
| **COO 2.0.0** | RAVC2 (final) post-chain-run -- AC1/AC2/AC3/AC5 PASS; AC4 closes on the materialized artifact. |
