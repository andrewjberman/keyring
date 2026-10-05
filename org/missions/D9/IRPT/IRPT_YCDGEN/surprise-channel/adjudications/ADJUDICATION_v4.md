# IRPT_YCDGEN -- round 4 L8/L9 adjudication (the fourth compile of the project's channel)

<sweep_watermark>2026-10-05T06:43:17Z</sweep_watermark>

Author: 3.0.0_SA_CVO, 2026-10-05 ~09:15Z. L8 inputs: `surprise-channel/investigations/INVESTIGATION_v1.md` at CLOUD HEAD
742b4665df (27 rows; the 7 surfaced after REMEDIATION_v3's watermark 2026-10-05T02:25:00Z are this compile's: W3-S5, W3-S6,
W2-S6, W4-S5, W4-S6, S7, S8); the issuer's round-4 drain-end packet
`deliverables/2.0.0_SA_COO~Y/round4/DRAIN_END_PACKET.md` @742b4665df (2.0.0_SA_COO~Y: 4 of 4 orders terminal and merged --
r-4 0a439396d1, o-4 c6a2cbb058, l-4 57b511a031, m-4 c3b266a60a; 7 mechanical checks PASS on the merged tree; m-4.AC3 the
judgment criterion for this seat); the close records `close/YCD-R4-20261005T0552Z_host_run.txt`,
`close/YCD-R4-20261005T0620Z_host_run.txt` and `close/YCD-R4-20261005T0700Z_host_run.txt`; and this seat's own reads
for this compile (code and git at CLOUD HEAD 742b4665df, the project's paths unchanged through c9effa7684; read-only AWS
as user/Andrew_Berman: the run.json of the seven round-4 close runs A to G read without any figure value, round 2's and
run A's kept scatter answers read in memory for keys, types and shape labels only, the two retained Comparison and Multi
PDFs located by their job checkpoints and read in memory; no YCharts call). 7 items compiled, all surfaced at or before
the watermark, and none ahead of the clock: the latest (S7 and S8, 06:43:17Z) precedes this compile's read. The 4
round-4 task orders are complete at HEAD. 5 are dismissed by the rows below (W3-S5, W2-S6, W4-S5, W4-S6, S8); 2 graduate
in `remediations/REMEDIATION_v4.md`, both OPEN (W3-S6, S7), round label v5. ARMED: 0 before, 0 after.

IN-PLACE CLOCK ADVANCES on `remediations/REMEDIATION_v3.md` (remediation.state and closed only; every other field
byte-equal; `clock_advances.json` beside this draft holds the full old and new rows; each passes the gate's
_monotone_advance and _mutation_violations):
- IRPT_YCDGEN-S4, remediation.state OPEN -> REMEDIATED, closed false -> true. Evidence: keeper.shape_of at CLOUD HEAD
  742b4665df, imported read-only and applied in memory to round 2's kept scatter answer (request=YCD-R2-20261004T2315Z-A
  step 01, VersionId pLB076hgb6mkZSlPElvwxcJerj_Qf2Tl), returns DATA (it returned IDENTIFIERS at a1b316c5b0); the same
  call kept live by run YCD-R4-20261005T0552Z-A (step 03) was labelled DATA at keep; negative control, the same body with
  every number turned to a string, returns IDENTIFIERS; tests/test_keeper.py 11 passed, including
  test_point_object_scatter_skeleton_labels_data (the type-skeleton fixture; r-4.AC2 PASS (2)).
- IRPT_YCDGEN-W4-S4: NOT advanced. m-4.AC3 is graded FAIL on eight items (the seven placeholder labels "row": Comparison
  p5.e17, p9.e04; Multi p5.e12-e14, p9.e03, p9.e04; and Multi p9's third-security "No data available" row, unlisted); the
  50 rows its remedy named are listed. It closes when those labels name their securities and the p9 row is listed.

Re-checked and left OPEN: (1) W2-S4 -- l-4 built the six statistics (contract 4.3 records the decision; seven
test_six_statistic_* tests pass on synthetic elements), but the Overview map's six elements p7.e02, p7.e03, p7.e05,
p7.e06, p7.e07 and p7.e08 still carry source.statistic null, so compute_element reads each STATISTIC_UNKNOWN:None at
HEAD (this seat's in-memory run with the l-4 fixtures), and p7.e08's column ids value_at_risk_monthly_5_<w> do not
parse as 4.3's var_monthly_<w>. The close condition (a layout test that pins the decided behaviour for each of the six
elements) is not met. (2) S6 -- the budget half holds: r-4.AC1 PASS (16; a 7th request is never sent in a window) and
five live windows of 6, 6, 6, 1 + 1 and 2 + 2 requests drew no challenge; the route half does not: the feed's 6
requests answered 400 (S8), so no run keeps a 200 DATA answer per holding.

Outside this compile: (1) FWD-2's true arm -- the packet reads it realized by runs F and G; this seat reads F and G as a
changed request under one call name, not a changed answer (S7 graduates; L9 grade, FWD-2). (2) The keeper labels a 400
JSON error body DATA (run C steps 1-4); the packet carries it as a label fix (section 4 item 4) and no row carries it.
(3) The packet's "26-call Overview" is not derived in the packet: the Overview map at HEAD plans 129 requests for Y-5's
99 holdings (14 portfolio calls, 21 expand calls at chunk 20, 1 at chunk 10).

```json
[
  {
    "id": "IRPT_YCDGEN-C-S12",
    "project": "IRPT_YCDGEN",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-05T09:15:00Z",
    "one_line": "W3-S5: YCD-l-4 changed one base test's unknown-statistic id from beta_1y to kurtosis_1y because contract 4.3 made beta_1y a statistic; the issuer accepted it at the drain, and the assertion still pins the unknown case.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_YCDGEN-W3-S5"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "The base test asserted STATISTIC_UNKNOWN:beta_1y, and contract 4.3 makes beta_<w> a statistic id for 1y to 15y, so the order's 'keep every existing test passing' and its own contract could not both hold for that one line. tests/test_layout_overview.py:205 at CLOUD HEAD 742b4665df asserts STATISTIC_UNKNOWN:kurtosis_1y, and layout_overview.py's statistic pattern (:169) admits no kurtosis id, so the line still pins an unnamed id. The issuer's drain note on YCD-l-4 accepts W3-S5; l-4.AC1 PASS (7) and the research suite reads 104 passed on the merged tree.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row(s) IRPT_YCDGEN-W3-S5",
        "org/missions/D9/IRPT/IRPT_YCDGEN/task-orders/IRPT_YCDGEN.TO-YCD-l-4.layout-six-statistics.md record face, DRAIN (2.0.0_SA_COO~Y): W3-S5 ACCEPTED",
        "infra/aws/lambda/investor-reporting/ycharts/research/tests/test_layout_overview.py:205 at CLOUD HEAD 742b4665df: STATISTIC_UNKNOWN:kurtosis_1y (this compile's read, 2026-10-05 ~07:3xZ to ~09:1xZ)",
        "infra/aws/lambda/investor-reporting/ycharts/research/layout_overview.py:160-169 at CLOUD HEAD 742b4665df: _STATS and _STAT_ID name no kurtosis (this compile's read, 2026-10-05 ~07:3xZ to ~09:1xZ)",
        "org/missions/D9/IRPT/IRPT_YCDGEN/decompositions/IRPT_YCDGEN_DECOMP_R4.md contract 4.3: statistic ids alpha_<w>, beta_<w>, sharpe_<w>, sortino_<w>, var_monthly_<w>, max_drawdown_15y"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Answered: the issuer accepted the changed assertion with no remedy owed, and the assertion keeps its intent with an id no contract names."
  },
  {
    "id": "IRPT_YCDGEN-C-S13",
    "project": "IRPT_YCDGEN",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-05T09:15:00Z",
    "one_line": "W2-S6: o-4 found no Opal table holding the 158 held-data figures per holding, so all 158 feed YCHARTS_SECURITY through a 6-request probe map with inferred metric ids; the issuer accepted it, and the live probe (S8) then measured that request form refused.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_YCDGEN-W2-S6"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "o-4.AC1 PASS (158 of 158 fed, all YCHARTS_SECURITY) and o-4.AC2 PASS (6 requests for 99 holdings) on the merged tree, and the issuer's drain note on YCD-o-4 accepts W2-S6 and keeps the census. The row's inferred parts were measured by the issuer's run YCD-R4-20261005T0620Z-C, whose run.json this seat read: schema irpt-ycdgen-run-v2, status COMPLETE, 6 calls, every one HTTP 400 (row S8). REMEDIATION_v3 row S6 (OPEN, v4) already owes a security-level route that answers 200 DATA per holding.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row(s) IRPT_YCDGEN-W2-S6",
        "org/missions/D9/IRPT/IRPT_YCDGEN/task-orders/IRPT_YCDGEN.TO-YCD-o-4.held-data-feed-census-and-probe-map.md record face, DRAIN (2.0.0_SA_COO~Y): W2-S6 ACCEPTED; the census stands",
        "s3://opal-data-cottonwood/irpt/cottonwood/state/ycharts_runs/request=YCD-R4-20261005T0620Z-C/run.json: schema irpt-ycdgen-run-v2, status COMPLETE, holdings block present, steps 1-6 status 400 (this compile's read, 2026-10-05 ~07:3xZ to ~09:1xZ, statuses and labels only, no figure value)",
        "investigation row IRPT_YCDGEN-S8 (the live probe's 400 answers)",
        "org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/remediations/REMEDIATION_v3.md row IRPT_YCDGEN-S6 (OPEN, v4)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Answered: the census finding was accepted with no remedy of its own, and its inferred request form was measured refused by S8; the route it was meant to open is S6's graduated remedy, still OPEN, so this row owes no separate remedy."
  },
  {
    "id": "IRPT_YCDGEN-C-S14",
    "project": "IRPT_YCDGEN",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-05T09:15:00Z",
    "one_line": "W4-S5: the seven Multi third-security Risk Info statistic names and Comparison p8.e33 stay map-side, outside map_pdf's rule; the issuer accepted it, and each of those labels reads right on its PDF page.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_YCDGEN-W4-S5"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "multi_map.json p10.e21 to p10.e27 read 'Risk Info: <statistic> iShares Russell 2000 ETF', each sourced to comparison_risk_stats at key_index 2; map_pdf at CLOUD HEAD 742b4665df, run in memory on the retained Multi PDF, labels the same seven rows 'Risk Info: iShares Russell 2000 ETF', because the PDF prints the statistic name only on the portfolio's line. On Comparison page 8 the portfolio's Bond Maturity column (x 148 to 358 pt) holds grey baselines and no bar and the key's column (x 375 to 530 pt) holds the bars; p8.e33 (chart 1 of 2) is sourced to portfolio_bond_exposure and p8.e03 (chart 2 of 2) to comparison_bond_exposure at key_index 1, as the geometry reads. The skeleton lists 573 Comparison elements and the map 574; the one difference is p8.e33. Contract 4.4 says no map-side repair; beside these eight, 22 Comparison and 24 Multi labels carried from round 3 differ from the skeleton, and every one reads right on its page by this seat's word check. The issuer's drain note on YCD-m-4 accepts W4-S5.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row(s) IRPT_YCDGEN-W4-S5",
        "org/missions/D9/IRPT/IRPT_YCDGEN/task-orders/IRPT_YCDGEN.TO-YCD-m-4.map-label-rule-and-rows.md record face, DRAIN (2.0.0_SA_COO~Y): W4-S5 ACCEPTED (the seven stat names and p8.e33 remain map-side, named)",
        "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/maps/multi_map.json p10.e21 to p10.e27 and comparison_map.json p8.e03, p8.e33 at CLOUD HEAD 742b4665df (this compile's read, 2026-10-05 ~07:3xZ to ~09:1xZ)",
        "the two retained PDFs (Comparison REQ-7ea49c2d9b27957d0ea8888f VersionId ZG118xXXEh2pCZozNhAnF9Dw9C3UOujR, Multi REQ-329a56182b2668d44a28c8d7 VersionId r317DqU2TxVMuwvtLV6WAI1fFQEo2lNv), sha256 equal to each job's checkpoint, read in memory: map_pdf.map_pdf skeleton aligned with each map page by page; Comparison page 8 drawing geometry (this compile's read, 2026-10-05 ~07:3xZ to ~09:1xZ, labels and coordinates only)",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_YCDGEN_ROUND4_L9_GRADE_20261005.md (this seat's m-4.AC3 grade, FAIL on eight items)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Answered: the issuer accepted the map-side labels and the listed chart with no remedy owed; each label reads right on its page and the chart's source matches the page geometry. A regeneration through map_pdf would drop them, so a regeneration needs the rule first, the condition W4-S1's dismissal (C-S8) already set."
  },
  {
    "id": "IRPT_YCDGEN-C-S15",
    "project": "IRPT_YCDGEN",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-05T09:15:00Z",
    "one_line": "W4-S6: with the third security's page-21 row listed, p21.e06 is re-sourced BUILDER_ONLY and the key-2 row is p21.e21, and 129 masked data-row labels took the rule's ordinal with ids and sources kept; the issuer accepted it.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_YCDGEN-W4-S6"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Page 21 of the retained Multi PDF prints, in order, the portfolio's row, Opal Ultra Long-Term, iShares Russell 2000 ETF, then the holdings. multi_map.json at CLOUD HEAD 742b4665df lists them as p21.e04, p21.e05 (key 1), p21.e21 (comparison_standardized_returns at key_index 2) and p21.e06 onward (BUILDER_ONLY), so round 3's key-2 source on p21.e06 belonged to a holdings row and is now corrected. Between a1b316c5b0 and HEAD: 0 element ids removed, 0 kind or page changes, 2 source changes (p8.e03, p21.e06); the label changes are 83 Comparison and 42 Multi data-row ordinals, the four Multi Waivers labels now masked, and p8.e03's chart ordinal. Every masked 'data row N' group (10 Comparison and 9 Multi, by page and heading) runs 1 to k in file order. layout_overview.py, runner.py and keeper.py hold no 'data row' string.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row(s) IRPT_YCDGEN-W4-S6",
        "org/missions/D9/IRPT/IRPT_YCDGEN/task-orders/IRPT_YCDGEN.TO-YCD-m-4.map-label-rule-and-rows.md record face, DRAIN (2.0.0_SA_COO~Y): W4-S6 ACCEPTED (129 ordinal labels renumbered with ids and sources kept)",
        "git show a1b316c5b0 and 742b4665df of org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/maps/comparison_map.json and multi_map.json, compared by element id (this compile's read, 2026-10-05 ~07:3xZ to ~09:1xZ)",
        "page 21 of REQ-329a56182b2668d44a28c8d7, read in memory: row order of the Annualized Returns table (this compile's read, 2026-10-05 ~07:3xZ to ~09:1xZ, labels only)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Answered: the issuer accepted the re-source and the renumbering with no remedy owed; the corrected source matches the printed order, ids and sources were kept, and no reader keys on a data-row label."
  },
  {
    "id": "IRPT_YCDGEN-C-S16",
    "project": "IRPT_YCDGEN",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-05T09:15:00Z",
    "one_line": "S8: the held-data probe's 6 requests answered HTTP 400 (security items and metric ids refused); it is a measurement under S6's open remedy, which keeps its owner and close condition.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_YCDGEN-S8"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Run YCD-R4-20261005T0620Z-C, read by this seat: 6 calls (held_metrics_exposure_fundamentals__c01 and __c02, held_metrics_region_maturity__c01 and __c02, held_level_series__c01 and __c02), every one HTTP 400. feed_probe_map.json at CLOUD HEAD 742b4665df sends each holding as the item 'id:{ticker},include:true,,' joined by ',', so a separator follows an item that already ends ',,'; the same map's metrics parameter joins its items with no extra separator. Run YCD-R4-20261005T0552Z-A's securities_info probe answered 200 IDENTIFIERS. REMEDIATION_v3 row S6 (OPEN, v4, owner 2.0.0_SA_COO~Y) owes a security-level route that answers 200 DATA per holding and closes on a run that keeps one behind a HELD_DATA element group. Separately, the keeper labels steps 1-4's 400 JSON bodies DATA and steps 5-6's 400 text bodies IDENTIFIERS (packet section 4 item 4).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row(s) IRPT_YCDGEN-S8",
        "s3://opal-data-cottonwood/irpt/cottonwood/state/ycharts_runs/request=YCD-R4-20261005T0620Z-C/run.json: steps 1-6 status 400, shapes DATA x4 and IDENTIFIERS x2 (this compile's read, 2026-10-05 ~07:3xZ to ~09:1xZ)",
        "s3://opal-data-cottonwood/irpt/cottonwood/state/ycharts_runs/request=YCD-R4-20261005T0552Z-A/run.json: step 5 security_info_probe status 200 IDENTIFIERS (this compile's read, 2026-10-05 ~07:3xZ to ~09:1xZ)",
        "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/maps/feed_probe_map.json at CLOUD HEAD 742b4665df: 3 calls, expand item 'id:{ticker},include:true,,', join ','",
        "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/close/YCD-R4-20261005T0620Z_host_run.txt: run C COMPLETE calls=6",
        "org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/remediations/REMEDIATION_v3.md row IRPT_YCDGEN-S6 (OPEN, v4)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Carried: S6's graduated remedy (OPEN) is the route this probe tried and its close condition is unchanged, so S8 owes no separate remedy; the steps it names (resolve each holding through securities_info, drop the extra separator, validate the metric ids on one public security inside the budget) are the next acts under S6."
  }
]
```
