# IRPT_YCDGEN round 4 -- L9 grade (3.0.0_SA_CVO, 2026-10-05 ~09:1xZ)

Input: drain-end packet `deliverables/2.0.0_SA_COO~Y/round4/DRAIN_END_PACKET.md` @742b4665df (msg 105205). The channel
compile is ADJUDICATION_v4 + REMEDIATION_v4 (drafts beside this file): 5 rows dismissed (W3-S5, W2-S6, W4-S5, W4-S6,
S8), 2 graduated OPEN (W3-S6, S7), round label v5, 0 ARMED, watermark 2026-10-05T06:43:17Z; in-place clock advances on
REMEDIATION_v3: S4 REMEDIATED, W4-S4 stays OPEN (m-4.AC3 FAIL on R1 and R2); W2-S4 and S6 stay OPEN.
Reads at CLOUD HEAD 742b4665df (the project's paths unchanged through c9effa7684); read-only AWS as user/Andrew_Berman;
no YCharts call. No figure value, client name or account number appears below.

## YCD-m-4.AC3 -- FAIL (Comparison and Multi), narrowly

Adopted verdict: every printed value row is listed (178 of 178, 221 of 221), every chart is listed, and the maps hold 0
figure values; the criterion's "labels read right" is not met by the seven placeholder labels "row" (R2), and Multi p9's
third-security "No data available" row has no element (R1). Eight items; W4-S4 stays OPEN for them.

"m-3.AC2 re-graded by 3.0.0_SA_CVO against the PDFs: every row listed, labels read right, no figure value." Sources:
the same retained certified PDFs as round 3, each located through its job's checkpoint_pdf and the artifact row's
VersionId, sha256 equal to the checkpoint, read in memory only: Comparison REQ-7ea49c2d9b27957d0ea8888f (VersionId
ZG118xXXEh2pCZozNhAnF9Dw9C3UOujR, 32 pages) and Multi REQ-329a56182b2668d44a28c8d7 (VersionId
r317DqU2TxVMuwvtLV6WAI1fFQEo2lNv, 34 pages). Maps at HEAD: `comparison_map.json` 574 elements (306 number, 181 table,
25 chart, 62 text) and `multi_map.json` 423 (8 number, 223 table, 24 chart, 168 text).

| check | Comparison | Multi |
|---|---|---|
| table rows (3+ values after a label): PDF / listed | 178 / 178 (round 3: 157) | 221 / 221 (round 3: 192) |
| rows added this round | 21, all holdings rows, BUILDER_ONLY data rows | 29: 14 third-security rows at key_index 2 on the comparison_* calls, 15 holdings rows BUILDER_ONLY |
| charts | 25 (24 + p8's baselines-only portfolio column, p8.e33) | 24 / 24 |
| removed or re-kinded since round 3 | 0 ids removed, 0 kind or page changes | 0 ids removed, 0 kind or page changes |
| labels: every word printed on its page | 509 of 512 (1 printed truncation; 2 placeholder 'row') | 249 of 255 (1 printed truncation; 5 placeholder 'row') |
| holdings names in the map | 0 of 112 | 0 of 73 (round-3 map: 2, the Waivers names) |
| figure values (C-FIRM) | 0 of 3,525 PDF-matching tokens | 0 of 3,204 PDF-matching tokens |

- **The 50 rows are listed and read right.** The Multi's third-security rows sit on the comparison calls at key_index
  2, each sourced like its key-1 sibling: p3.e13 and p3.e14; p10.e21 to p10.e27, which carry the seven statistic names;
  p11.e12, p11.e13 and p14.e10; p21.e21; and p22.e23. The printed order was checked on pages 21 and 22. The holdings rows
  are masked "data row N", and every (page, heading) group runs 1..k in file order.
- **p8 bar column (Comparison).** The portfolio's column (x 148-358 pt) is grey baselines with no bar; all 15 of its
  printed values are zero. It is listed as p8.e33, "chart 1 of 2", sourced to portfolio_bond_exposure. The key's bars
  (x 375-530 pt) are p8.e03, "chart 2 of 2", now sourced to comparison_bond_exposure at key_index 1. This matches the
  geometry.
- **p22.e16 to p22.e19 (Multi).** These now read "Waivers: data row 1" (two elements) and "data row 2" (two). That is
  two Waivers rows of two values each, as printed. No holding name remains.
- **Nothing removed.** Two sources changed, and both are named: p8.e03 above, and p21.e06 (the Global X row, now
  BUILDER_ONLY). There are 125 data-row ordinals, plus the four Waivers masks and p8.e03's chart ordinal (W4-S6: 129).
- **Rule vs map-side.** On the two PDFs, map_pdf at HEAD gives 573 and 423 elements. Still rejected by the rule: 5
  rows, all the portfolio's own, and each is listed through the {portfolio_name} branch. The labels the rule does not
  give are map-side: the seven statistic names and p8.e33 (W4-S5, accepted), plus 22 Comparison and 24 Multi labels
  carried from round 3. Each reads right on its page. Contract 4.4's "no map-side repair" is not met for them; the
  issuer's ruling accepts that.
- **Controls.**
  - One table element dropped in memory: FLAGGED. No drop: clean.
  - The round-3 maps under the same instrument reproduce the FAIL (157 and 192).
  - Planted decimal, percent and thousands values are flagged as FIGURE_CANDIDATE: 3 of 3 and 2 of 2. A nonsense token
    matches neither PDF.
- **Residuals, not graded as failures.** Neither is a figure value, and both pre-date round 4.
  - (R1) Multi page 9: the third security's Bond Credit Quality row prints "No data available" and eight '--' under its
    stacked name. No element lists it. It is outside m-3.AC2's census (a label plus 3 or more values, every number,
    table and chart). A strict "every printed row" reading would count it.
  - (R2) Seven placeholder labels "row": Comparison p5.e17 and p9.e04; Multi p5.e12 to p5.e14, p9.e03 and p9.e04. The
    PDF prints each name on the line above the values. Each element is sourced in print order, and its note says so.
  - Both are carried for the CTO's round-4 analysis.
- Evidence file: scratch `ycdgen_r4/m-4_AC3_evidence.txt`.
  - Round-3 instruments, unedited: `locate.py`, `figures.py`, `ac2_confirm.py`, `c3_firm.py`.
  - Round-4 instruments: `figures_at.py`, `mapdiff.py`, `skel_labels.py`, `labels_read.py`, `names_in_map.py`,
    `dropped_r4.py`, `dashrows.py`.

## Packet claims checked

- **"--end is not a driver" (S7): holds.**
  - Run A and run B both read 539579bbaee2.. (B reads false).
  - Run D and run E both read ef306d6162e1.. (E reads false).
- **"G reads changed_since_previous true ... and false on portfolio_info": holds.**
  - F's level series reads 04f9de536ee8.. (no_previous); G's reads 539579bbaee2.. (true).
  - portfolio_info reads df70928da81c.. in both.
  - G's answer equals run A's answer of 05:56Z. Judged under FWD-2 below.
- **"The budget holds at 6 requests a window with 660 s between windows": holds as measured.**
  - The host records show runs of 6, 6, 6, 1 + 1 and 2 + 2 requests, with no challenge.
  - Each wait of 660 s or more ran from the previous run's end.
  - No window sent a 7th request; round 3's 3 of 3 challenges at the 7th still stand.
- **S4 answered by r-4: borne out.**
  - keeper.shape_of at HEAD returns DATA on round 2's kept scatter answer. It returned IDENTIFIERS at a1b316c5b0.
  - Run A's live scatter answer was labelled DATA when kept.
  - Negative control: the same body with every number turned to a string reads IDENTIFIERS.
  - test_keeper: 11 passed. S4 advances to REMEDIATED.
- **W2-S4 answered by l-4: not borne out at the element level.**
  - The six statistics are built, and seven tests pass on synthetic elements.
  - The Overview map's p7.e02, e03, e05, e06, e07 and e08 still carry statistic null, so each reads
    STATISTIC_UNKNOWN:None at HEAD (in-memory run with the l-4 fixtures).
  - p7.e08's ids value_at_risk_monthly_5_<w> do not parse as 4.3's var_monthly_<w>.
  - Both render paths call compute_all without a benchmark or risk-free series; W3-S6 graduates for this.
  - W2-S4 stays OPEN.
- **"6 of 6 requests answered HTTP 400" (S8): holds.** Run C's run.json shows steps 1-6 at 400. Steps 1-4 are labelled
  DATA, which is the packet's item 4.
- **"a 26-call Overview needs 5 windows": the count is not derived in the packet.** At HEAD the Overview map plans 129
  requests for Y-5's 99 holdings: 14 portfolio calls, 21 expand calls at chunk 20 and 1 at chunk 10.
- **"104 passed": the packet's number.** This read ran test_keeper only (11 passed). The suite's render tests launch a
  browser.

## Outcomes (evidence for the slug)

| FWD | evidence at this read |
|---|---|
| 1 | Still Andrew's act. On 2026-10-04 he said he would open it when ~Y sends the link (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261004_220xZ_ALL_RECS_APPROVED_REPORT_OPEN_BD_PULL_RSI_49F_BUILD.md` item 1). His opening of run 3's Opal-branded Overview is not on record (packet section 2). E6 was not rendered because the feed answered 400. NOT REALIZED until he opens it |
| 2 | **True arm NOT REALIZED on an unchanged request. Runs F and G answer a different question.** DONE WHEN: "EXERCISED -- an analyst has looked one up". ACCEPT: "for a finished run, an analyst picks any one call and sees what it gave back, whether that was identifiers, data or a document, and whether it changed since the previous run". C-KEEP computes the flag "from the same call's previous kept sha256 for the same portfolio". "It" is what the call gave back. F asked for 5 years of the level series and G for all of it, so G's answer had to differ: G's true reports a changed request. With the request held fixed (zoom=max in run A at 05:56Z and run G at 07:08Z), the answer is byte-identical. The runner keys the previous answer by call name alone (runner.py:155-158), so the flag cannot tell a changed request from a changed answer. F and G exercise the comparison's true branch live. They do not exercise the outcome. **Unambiguous realization:** repeat the byte-identical zoom=max level-series request after a new trading day's close has reached YCharts. Monday 10-05 closes at 20:00Z, plus the vendor's lag. Compare it against an indexed run whose series ends 10-02 (A, B or G). Read true, with the kept series' last date advanced. Then have an analyst look that call up from the store. The false and no_previous arms are live. Separately, the keeper labels a 400 JSON error body DATA (run C), which misstates "whether that was identifiers, data or a document" for an error answer. Remedy: REMEDIATION_v4 row S7 |
| 3 | The Overview map is complete (round 2). The Comparison and Multi maps now list every value row (178 of 178, 221 of 221) and every chart. Each row is either tied to a named call or listed as BUILDER_ONLY, with 0 figure values: m-4.AC3 FAIL on residuals R1 and R2 only. DONE WHEN, "an analyst has traced one element of each type": not on record in this packet. Maps READY; NOT EXERCISED for Comparison and Multi |
| 6 | NOT EXERCISED (Andrew's sitting). The measured budget is 6 requests a window, with 660 s or more between windows and no challenge in 5 windows; the window length below 660 s is unmeasured. A plan of N requests needs ceil(N/6) windows and at least (ceil(N/6) - 1) x 11 min of waiting. The packet's 26-call Overview needs 5 windows, about 44 min of waiting. 20 requests (14 portfolio calls plus the feed's 6, if the feed replaces the 22 expand calls) need 4 windows, about 33 min. The Overview map as it stands at HEAD (129 requests) needs 22 windows, about 3 h 51 min. Andrew's bar (PRD FWD-6 SOURCE: "It has no need to take 15-20 minutes") fits at most 2 windows (12 requests) at 660 s. A shorter window, or a 12-request plan, is what would let FWD-6 pass |
| Elements (E1, E4) | The 158 HELD_DATA elements are not fed (S8; S6 OPEN). The six 4.3 statistics are built but not wired to the Overview's elements (W2-S4 OPEN; W3-S6 graduates) |

-- 3.0.0_SA_CVO (reads by a read-only delegate of this seat)
