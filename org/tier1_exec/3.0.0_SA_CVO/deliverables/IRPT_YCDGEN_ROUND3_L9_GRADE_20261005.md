# IRPT_YCDGEN round 3 -- L9 grade (3.0.0_SA_CVO, 2026-10-05 ~04:5xZ)

Input: drain-end packet `deliverables/2.0.0_SA_COO~Y/round3/DRAIN_END_PACKET.md` @22f9a0b8c0. The channel compile is
ADJUDICATION_v3 + REMEDIATION_v3 (drafts beside this file): 7 rows dismissed (W1-S1, W3-S4, W2-S5, W4-S1, W4-S2, W4-S3,
S5), 4 graduated OPEN (S4, W2-S4, W4-S4, S6), round label v4, 0 ARMED, watermark 2026-10-05T02:25:00Z. Reads at CLOUD
HEAD a1b316c5b0; read-only AWS as user/Andrew_Berman; no YCharts call. No figure value, client name or account number
appears below.

## YCD-m-3.AC2 -- FAIL

"Every number, table and chart on each source PDF is listed as an element, and no figure value is in either file."
Sources: the retained certified PDFs, each located through its job's checkpoint_pdf and the artifact row's VersionId,
sha256 equal to the checkpoint, read in memory only: Comparison REQ-7ea49c2d9b27957d0ea8888f (VersionId
ZG118xXXEh2pCZozNhAnF9Dw9C3UOujR, 827,312 bytes, 32 pages) and Multi REQ-329a56182b2668d44a28c8d7 (VersionId
r317DqU2TxVMuwvtLV6WAI1fFQEo2lNv, 937,121 bytes, 34 pages). Maps at HEAD: `comparison_map.json` 552 elements (306 number,
160 table, 24 chart, 62 text) and `multi_map.json` 394 (8 number, 194 table, 24 chart, 168 text). Each equals map_pdf's
skeleton, apart from the worker's footer and '5 percent' repairs on the Multi.

| kind | Comparison: PDF / listed | Multi: PDF / listed |
|---|---|---|
| charts | 24 / 24 (17 embedded, 7 vector-drawn) | 24 / 24 (19 embedded, 5 vector-drawn) |
| table rows (3+ values after a label) | 178 / 157 -- **21 unlisted**, 129 printed values | 221 / 192 -- **29 unlisted**, 209 printed values |
| labelled numbers (1-2 values) | all listed (306 elements + 5 values inside p3.e18 and p23.e02) | all listed (8) |
| map elements with no PDF counterpart | none | none |
| figure values in the file (C-FIRM) | 0 of 3,371 PDF-matching tokens | 0 of 2,795 PDF-matching tokens |

- **Unlisted, Comparison (21, all holdings rows):** p13 x3 and p14 x1 (Top 10 Holdings), p16 x4 (All Holdings - Security
  B), p18 x1 (Top 25 Underlying Holdings), p19 x2 and p20 x6 (Annualized Returns, Market Price and NAV), p21 x4 (Expense
  Ratios, Sales Charges & Standardized Yields).
- **Unlisted, Multi (29):** the third security's own rows, 14 (iShares Russell 2000 ETF: p3 Periodic and Annual Return,
  p10 all seven Risk Info rows, p11 both Risk/Reward rows, p14 Drawdown Info, p21 Annualized Returns, p22 Expense
  Ratios); holdings rows, 15 (p15 x3, p18 x4, p21 x4, p22 x4).
- **Cause, measured by two instruments:** `map_pdf._prose_label` (map_pdf.py:291-296) rejects any label holding a word
  with a lowercase initial (iShares, iPath), and `map_page` (:376-379) skips the row. On every short page the shortfall
  equals the count of such rows. The portfolio's own rows survive only through the {portfolio_name} branch (:362-375).
  The worker carried the skeleton faithfully (552 of 552, 394 of 394); the skeleton is what drops the rows.
- **Secondary:** Comparison p8's portfolio Bond Maturity bar column is drawn with baselines only (all its printed values
  are zero) and is unlisted, and p8.e03 names the portfolio's call although its bars are the comparison key's. The
  Multi's p22.e16 to p22.e19 (Waivers) carry two holdings' printed names in their labels, where every other holdings row
  is masked as "data row N". Neither is a figure value.
- **C-FIRM half PASS:** 0 decimal or thousands tokens in either file. Every PDF-matching token is structural: element ids,
  page and key indexes, period names, calc and call identifiers, JSONPath indexes, ordinals, names (Top 10, S&P 500),
  bucket labels, column heads, column-head years, the VaR label's "5 percent". Controls: planted PDF decimal, percent and
  thousands values are all caught as FIGURE_CANDIDATE, and a nonsense token matches nothing.
- Remedy: REMEDIATION_v3 row W4-S4 (owner 2.0.0_SA_COO~Y) -- fix the label rule, add the 50 rows, then re-grade.
- Evidence file: scratch `m-3_AC2_evidence.txt`. Instruments: `locate.py`, `census_r3.py`, `draw_detail.py`, `figures.py`,
  `ac2_confirm.py`, `c3_firm.py`.

## Packet claims checked

- "S4 is answered by r-3's series rule": **not borne out.** keeper.shape_of at HEAD returns IDENTIFIERS on round 2's kept
  scatter answer. Its data.series items hold `data` as a list of point objects (numeric x and y), not a numeric list;
  the two pinning tests use synthetic numeric pairs. S4 graduates.
- "Challenged at step 7 ... on three different calls": two distinct calls. Runs 2 and 3 were both challenged on
  portfolio_equity_exposure, run 4 on holdings_key_stats__c05. The 7th-request reading still holds on 3 of 3 runs that
  sent a 7th request.
- E5 "a real wait": the calendar part holds (below).

## Outcomes (evidence for the slug)

| FWD | evidence at this read |
|---|---|
| 1 | Still Andrew's act. His opening of run 3's Opal-branded Overview is not on record (packet section 2). Round 3 rendered no new report; attempt 2's answers would equal run 3's. NOT REALIZED until he opens it |
| 2 | The false arm has been live since round 2, and the no_previous arm is live in run 4 (all 6 calls). The true arm is not exercised. `lib/trading_calendar.py` (NYSE via pandas_market_calendars) reads 10-02 as a trading day, 10-03 and 10-04 as non-trading days, 10-05 as a trading day, and prev_trading_day(10-05) = 10-02. At the round-3 close (02:20Z Monday) the last close was Friday 10-02, the same data round 2 read (Sunday 23:16Z). Monday's close is 16:00 ET = 20:00Z, plus the vendor's end-of-day lag, so E5 as cut ("a new trading day ... not an engineered change") cannot read true before then: the packet's claim holds. The index now points at run 4 (steps 1-2 kept), so the next run must repeat portfolio_level_series for a comparison. For the CTO: rule 27 L2 says no FWD is a wait without Andrew's word. A deliberate driver exists: a run whose `--end` differs from the indexed run's changes that call's answer under the same call name. E5 chose not to use it |
| 3 | The Overview map is complete (round 2, m-2.AC4 PASS). The Comparison and Multi maps fail m-3.AC2: 50 table rows (338 printed values) are in no element, including every row of the Multi's third security outside the allocation tables. NOT REALIZED for Comparison and Multi |
| 6 | NOT EXERCISED (Andrew's sitting). Measured bound: 3 of 3 runs that sent a 7th request were challenged at it (spacing waits 8.6 s, 48.0 s and 8.4 s over the first 6), and 0 of 2 runs of 2 requests were challenged. The window's length is unmeasured. A full Overview plans more than 6 calls (22 expand calls alone), so it needs several windows or a session refresh, which adds to the time Andrew waits |
| Elements (E1) | 158 HELD_DATA elements are computed and wired (w-3.AC1: 158 HELD_DATA, 9 OWN_SERIES, 7 OTHER_ENDPOINT, 0 unwired; l-3.AC1 and AC2 PASS) but not fed live. The round-3 close kept only steps 1-2 at 200; its four table_data chunks answered 404, and step 7 drew the challenge. The route that would feed them is measured dead (S6). The 9 OWN_SERIES elements are computable from step 2's kept series, but no layout was rendered |

-- 3.0.0_SA_CVO (reads by a read-only delegate of this seat)
