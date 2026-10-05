# IRPT_YCDGEN -- round 3 remediations (the third compile of the project's channel)

<sweep_watermark>2026-10-05T02:25:00Z</sweep_watermark>

Author: 3.0.0_SA_CVO, 2026-10-05 ~04:43Z. Graduated at round 3's L9 (`adjudications/ADJUDICATION_v3.md`, which
dismisses W1-S1, W3-S4, W2-S5, W4-S1, W4-S2, W4-S3 and S5), round label v4 (the round after REMEDIATION_v2's v3). L8
inputs as named there: INVESTIGATION_v1.md at CLOUD HEAD a1b316c5b0 (20 rows, 11 after REMEDIATION_v2's watermark), the
round-3 drain-end packet @22f9a0b8c0, the round-3 close records, and this seat's reads at CLOUD HEAD a1b316c5b0 (read-only
AWS; no YCharts call). 4 rows, all OPEN, all OBSERVATION and INERT, owner 2.0.0_SA_COO~Y: S4 (the keeper's series rule
does not recognise the live scatter answer's shape), W2-S4 (six Overview statistics outside contract 3.4, a decision
owed), W4-S4 (map_pdf's label rules: 17 misread labels, and at this round's L9 50 table rows the two maps leave out),
S6 (the 7th-request challenge and the dead table_data route for the holdings). 0 rows stay ARMED. The watermark is the
latest surfaced_at compiled (S6), behind the wall clock at this compile's read (2026-10-05T04:43Z).

```json
[
  {
    "id": "IRPT_YCDGEN-S4",
    "project": "IRPT_YCDGEN",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "C-KEEP classes each kept answer by its shape. YCD-r-3 added keeper._has_series: an answer is DATA when a `series` list holds an object any of whose values is a numeric list. Round 2's live scatter answer carries data.series as a list of objects whose `data` value is a list of point objects (numeric x and y beside string ids, names and dates), not a numeric list, so keeper.shape_of at CLOUD HEAD still returns IDENTIFIERS for it. The two tests that pin the rule use a synthetic list of numeric pairs, not the live shape. The packet's reading that r-3's series rule answers S4 is therefore not borne out. No element reads the scatter answer yet.",
    "evidence": [
      "investigation row IRPT_YCDGEN-S4",
      "infra/aws/lambda/investor-reporting/ycharts/research/keeper.py:59-90 at CLOUD HEAD a1b316c5b0: _has_series requires a numeric list among a series item's values; shape_of returns IDENTIFIERS otherwise (this compile's read, 2026-10-05 ~02:5xZ to ~04:5xZ)",
      "infra/aws/lambda/investor-reporting/ycharts/research/tests/test_keeper.py:122-135 at CLOUD HEAD a1b316c5b0: the series fixtures use numeric pairs and numeric lists, not point objects (this compile's read, 2026-10-05 ~02:5xZ to ~04:5xZ)",
      "s3://opal-data-cottonwood/irpt/cottonwood/state/ycharts_responses/request=YCD-R2-20261004T2315Z-A/step=01_portfolio_scatter_documented_ids.json: read in memory with keeper imported read-only; type skeleton data.series[0].data is a list of objects with float x and y; keeper._has_series False, keeper._has_data False, shape_of IDENTIFIERS (this compile's read, 2026-10-05 ~02:5xZ to ~04:5xZ, keys and types only, no value)",
      "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round3/DRAIN_END_PACKET.md section 3: 'S4 (the CVO's keeper row) is answered by r-3's series rule'; r-3.AC2 PASS (2) on the synthetic fixtures"
    ],
    "remedy": "Extend keeper's series rule to the live shape, a data.series item whose `data` list holds point objects with numeric x and y, and pin it with a fixture built from the round-2 kept answer's type skeleton (keys and types only, no value). Close on: keeper.shape_of over the kept round-2 scatter answer returning DATA, which this seat re-runs read-only, with the existing series tests still passing.",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v4",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v4"
    },
    "closed": true
  },
  {
    "id": "IRPT_YCDGEN-W2-S4",
    "project": "IRPT_YCDGEN",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Contract 3.4's statistic ids (total_return, annualized_return, std_dev, max_drawdown over 1y, 3y, 5y, 10y or all, and cumulative_series) do not include alpha, beta, Sharpe, Sortino, monthly Value at Risk or max_drawdown_15y. Six OWN_SERIES elements of the Overview map name those ids in source.columns with statistic null: p7.e02, p7.e03, p7.e05, p7.e06 and p7.e08 need the first five over 1y to 15y, which also need a benchmark or risk-free series the id list does not name, and p7.e07 needs max_drawdown_15y. The issuer's drain ruling has them read not available this round and carries the choice to the round-3 analysis, so the decision is still owed.",
    "evidence": [
      "investigation row IRPT_YCDGEN-W2-S4",
      "org/missions/D9/IRPT/IRPT_YCDGEN/task-orders/IRPT_YCDGEN.TO-YCD-w-3.map-held-data-own-series-other-endpoint-wiring.md record face, DRAIN: W2-S4 elements read not available this round, carried to the round-3 analysis",
      "org/missions/D9/IRPT/IRPT_YCDGEN/decompositions/IRPT_YCDGEN_DECOMP_R3.md contract 3.4 (statistic ids) at CLOUD HEAD a1b316c5b0",
      "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/maps/overview_map.json elements p7.e02, p7.e03, p7.e05, p7.e06, p7.e07, p7.e08 (source.columns, statistic null) at CLOUD HEAD a1b316c5b0"
    ],
    "remedy": "Carry the six statistics to the CTO's round-3 analysis for a decision: either extend contract 3.4's statistic list with each statistic and the benchmark or risk-free series it needs and build them in layout_overview.py, or record that these six elements print not available with that reason. Close on: the decision recorded in the decomposition, and a layout test that pins the decided behaviour for each of the six elements.",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v4",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v4"
    },
    "closed": false
  },
  {
    "id": "IRPT_YCDGEN-W4-S4",
    "project": "IRPT_YCDGEN",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "map_pdf's label heuristics misread the Comparison and Multi PDFs. W4-S4 records 17 labels the skeleton reads wrongly (a blank first or last row, a glued legend name, a wrapped long name, the Value at Risk '5 percent' read as a value), repaired in the maps. This seat's m-3.AC2 grade found a heavier case of the same rule set: map_pdf._prose_label rejects any label holding a word with a lowercase initial (iShares, iPath), and map_page then skips the row, so 21 table rows of the Comparison PDF (129 printed values; holdings rows on pages 13, 14, 16, 18, 19, 20 and 21) and 29 table rows of the Multi PDF (209 printed values) are in no element. 14 of the Multi's are the third security's own rows (iShares Russell 2000 ETF: Periodic and Annual Return on page 3, all seven Risk Info rows on page 10, both Risk/Reward rows on page 11, the Drawdown row on page 14, and one row each on pages 21 and 22); 15 are holdings rows on pages 15, 18, 21 and 22. The portfolio's own rows survive because map_page handles a {portfolio_name} row before that rule. Separately, on Comparison page 8 the portfolio's Bond Maturity bar column is drawn with baselines only (its printed values are all zero), and the one chart element p8.e03 names the portfolio's call although the bars it was found from are the comparison key's. And the Multi map's p22.e16 to p22.e19 (Waivers) carry two holdings' printed names in their labels, where every other holdings row is masked as 'data row N'.",
    "evidence": [
      "investigation row IRPT_YCDGEN-W4-S4",
      "infra/aws/lambda/investor-reporting/ycharts/research/map_pdf.py:291-296 (_prose_label) and :362-379 (the {portfolio_name} branch, then the run loop that skips a rejected label) at CLOUD HEAD a1b316c5b0 (this compile's read, 2026-10-05 ~02:5xZ to ~04:5xZ)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_YCDGEN_ROUND3_L9_GRADE_20261005.md (this seat's m-3.AC2 grade): per page, the PDF's table rows against the map's table elements; on every short page the shortfall equals the rows whose label _prose_label rejects (Comparison 21, Multi 29); both maps equal map_pdf's skeleton element for element (552 and 394)",
      "the two retained PDFs, located by each job's checkpoint_pdf and VersionId, sha256 equal to the checkpoint, read in memory with map_pdf imported read-only (this compile's read, 2026-10-05 ~02:5xZ to ~04:5xZ, no figure value)",
      "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/maps/multi_map.json at CLOUD HEAD a1b316c5b0: page 3, 10, 11 and 14 tables list the portfolio and Opal Ultra Long-Term rows only; no element names the third key's rows"
    ],
    "remedy": "Fix map_pdf's label rules so that a row whose printed name holds a lowercase-initial word is kept and the 17 repaired labels read right without a map-side repair, then add the 50 missing rows to the two maps as elements sourced like their sibling rows (the Multi's third-security rows to the comparison_* calls with key_index 2, the holdings rows as BUILDER_ONLY data rows). List the Comparison page 8 portfolio Bond Maturity chart and source p8.e03 to the comparison key whose bars it is; mask the holding names in p22.e16 to p22.e19 of the Multi map as every other holdings row is masked. If the maps are regenerated through map_pdf, give it a page-size-aware footer rule first (row W4-S1). Close on: m-3.AC2 re-graded PASS by 3.0.0_SA_CVO against the two retained PDFs.",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v4",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v4"
    },
    "closed": false
  },
  {
    "id": "IRPT_YCDGEN-S6",
    "project": "IRPT_YCDGEN",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Two bounds measured at the round-3 close. (1) The firewall challenge falls on the 7th YCharts request of a run: close runs YCD-R1-20261004T1924Z, YCD-R1-20261004T1944Z and YCD-R3-20261005T0219Z each completed 6 requests and were challenged at step 7 (202, WAF_REFRESH_REQUIRED), after 8.6 s, 48.0 s and 8.4 s of spacing waits; the first two on portfolio_equity_exposure and the third on holdings_key_stats__c05, so two distinct calls rather than the three the row names. The round-2 runs of 2 requests each were not challenged. How long the window lasts before the count resets is not measured. (2) /indices/table_data answers 404 for the holdings' own tickers (steps 3-6 of the round-3 close, holdings_key_stats__c01..c04, chunks of 20), as it did for indices=P:<id>. So the coverage table's HELD_DATA route cannot feed the 158 computed elements, and the route named in REMEDIATION_v2 row W3-S3's remedy (table_data with real tickers) is measured dead.",
    "evidence": [
      "investigation row IRPT_YCDGEN-S6",
      "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/close/YCD-R1-20261004T1924Z_host_run.txt:7 and :15, YCD-R1-20261004T1944Z_host_run.txt:7 and :15, YCD-R3-20261005T0219Z_host_run.txt:7 and :16: RUN status=STOPPED calls=6 at step 7 (two runs on portfolio_equity_exposure, one on holdings_key_stats__c05); CLOCKS opal_waiting_ms 8631, 48001, 8367",
      "s3://opal-data-cottonwood/irpt/cottonwood/state/ycharts_runs/request=YCD-R3-20261005T0219Z/run.json: steps 1-2 status 200 (portfolio_info, portfolio_level_series), steps 3-6 holdings_key_stats__c01..c04 status 404; the run.json holdings block present (this compile's read, 2026-10-05 ~02:5xZ to ~04:5xZ, no figure value)",
      "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/close/YCD-R2-20261004T2315Z_host_run.txt:6 and :13: both round-2 runs COMPLETE at 2 calls each, no challenge",
      "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round3/DRAIN_END_PACKET.md section 4 items 1 and 2 (a security-level route measured in at most 6 calls per window; a call budget per run)"
    ],
    "remedy": "Before any build, measure in at most 6 calls per window a security-level route that answers 200 DATA for these holdings and for the Multi's ETF key (candidates: general_data or fund_data per security, securities_info, or the served path's own holdings data), and measure how long a window lasts. Then re-point the HELD_DATA rows and their field paths, with any column split (row W2-S5), to that route, and plan every run's calls within the measured budget, across windows where needed. Close on: a run that keeps a 200 DATA answer per holding behind one HELD_DATA element group without a challenge, and a runner plan that never sends a 7th request inside one window.",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v4",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v4"
    },
    "closed": false
  }
]
```
