# IRPT_YCDGEN -- round 3 L8/L9 adjudication (the third compile of the project's channel)

<sweep_watermark>2026-10-05T02:25:00Z</sweep_watermark>

Author: 3.0.0_SA_CVO, 2026-10-05 ~04:43Z. L8 inputs: `surprise-channel/investigations/INVESTIGATION_v1.md` at
CLOUD HEAD a1b316c5b0 (20 rows; the 11 surfaced after REMEDIATION_v2's watermark 2026-10-05T00:30:00Z are this compile's:
S4, W1-S1, W3-S4, W2-S4, W2-S5, W4-S1, W4-S2, W4-S3, W4-S4, S5, S6); the issuer's round-3 drain-end packet
`deliverables/2.0.0_SA_COO~Y/round3/DRAIN_END_PACKET.md` @22f9a0b8c0 (2.0.0_SA_COO~Y: all 4 orders terminal and
merged -- r-3 dd418f6555, l-3 614554f60f, w-3 37e2a053c6, m-3 04c20019c8; 7 mechanical checks PASS on the merged tree;
m-3.AC2 the judgment criterion for this seat); the close records `close/YCD-R3-20261005T0207Z_host_run.txt` and
`close/YCD-R3-20261005T0219Z_host_run.txt`; and this seat's own reads for this compile (code and git at CLOUD HEAD
a1b316c5b0; read-only AWS as user/Andrew_Berman: the round-3 close's run.json and stop_row.json read without any figure
value, round 2's kept scatter and snapshot answers read in memory for keys and types only, the two retained Comparison
and Multi PDFs located by their job checkpoints and read in memory; no YCharts call). 11 items compiled, all surfaced at
or before the watermark, and none ahead of the clock: each surfaced_at precedes the commit that added its row, and the
latest (S6, 02:25:00Z) precedes this compile's read. The 4 round-3 task orders are complete at HEAD. 7 are dismissed by
the rows below (W1-S1, W3-S4, W2-S5, W4-S1, W4-S2, W4-S3, S5); 4 graduate in `remediations/REMEDIATION_v3.md`, all OPEN
(S4, W2-S4, W4-S4, S6). ARMED: 0 before, 0 after.

Outside this compile: (1) the packet reads S4 as answered by r-3's series rule; this seat's in-memory read finds
keeper.shape_of at HEAD still returns IDENTIFIERS for the live round-2 scatter answer, so S4 graduates (REMEDIATION_v3).
(2) REMEDIATION_v2 rows, not re-compiled: S3 has met its first close condition (S5 is a live stop row, filed from the
runner's own stop_row.json), and its second (the table_data indices=P: calls retired from the canonical map) is a
round-4 cell (packet section 4 item 3); W3-S2's coverage gap is now the OWN_SERIES class (9 of its 10 elements; p12.e04
stays BUY_AND_HOLD by the issuer's ruling), and its live close condition waits on a run that feeds them; W3-S3's remedy
route (table_data with real tickers) is measured dead by S6, and its close condition stands. W2-S3 (OPEN, v2) is
unchanged. (3) W4-S3's question -- a READY certified Comparison (REQ-e4b7f5ab) whose pages never print its comparison
key -- concerns the served IRPT path, not this project; it is carried for the CTO's round-3 analysis to place with that
path's owner. (4) m-3.AC2 is graded FAIL at L9 (both maps leave table rows unlisted; neither carries a figure value); the
remedy rides W4-S4's graduation.

```json
[
  {
    "id": "IRPT_YCDGEN-C-S5",
    "project": "IRPT_YCDGEN",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-05T04:43:00Z",
    "one_line": "W1-S1: run.json is v2 with a holdings block only for a run given holdings, v1 unchanged otherwise; the issuer accepted it as built, the layout reads a run with no holdings as not available, and the round-3 close wrote v2 with its holdings.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_YCDGEN-W1-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "W1-S1 (0.9.0_WK_IRPT_YCDGEN~1, 01:08Z) reports that contract 3.2's unconditional v2 would break the kept runner tests that pin v1's exact key set, so the runner writes v2 plus holdings only when it is given holdings. The issuer's drain ruling on YCD-r-3 accepts this as built: v1's key pin stays valid and the layout reads v1 as no holdings. layout_overview.py _holdings raises INPUT_MISSING:holdings when run.json carries no holdings rows, so a v1 run prints not available rather than a wrong figure. The round-3 close run YCD-R3-20261005T0219Z wrote schema irpt-ycdgen-run-v2 with its holdings block.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row(s) IRPT_YCDGEN-W1-S1",
        "org/missions/D9/IRPT/IRPT_YCDGEN/task-orders/IRPT_YCDGEN.TO-YCD-r-3.runner-holdings-expand-and-series-shape.md record face, DRAIN (2.0.0_SA_COO~Y): issuer ruling on row W1-S1, accepted as built",
        "infra/aws/lambda/investor-reporting/ycharts/research/layout_overview.py:204-219 at CLOUD HEAD a1b316c5b0: _holdings raises INPUT_MISSING:holdings when the run record has no holdings rows (this compile's read, 2026-10-05 ~02:5xZ to ~04:5xZ)",
        "s3://opal-data-cottonwood/irpt/cottonwood/state/ycharts_runs/request=YCD-R3-20261005T0219Z/run.json: schema irpt-ycdgen-run-v2, holdings block present, status STOPPED (this compile's read, 2026-10-05 ~02:5xZ to ~04:5xZ, no figure value)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Answered: the issuer's ruling accepts the conditional v2 with no remedy owed, the one consumer reads v1 as no holdings, and the live close wrote v2 with its holdings."
  },
  {
    "id": "IRPT_YCDGEN-C-S6",
    "project": "IRPT_YCDGEN",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-05T04:43:00Z",
    "one_line": "W3-S4: the five computation conventions YCD-l-3 fixed where contracts 3.4 and 3.5 were silent are confirmed by the issuer at the drain, and each is pinned by a test.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_YCDGEN-W3-S4"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "The issuer's drain note on YCD-l-3 confirms all five conventions: renormalize over the answered holdings; percent units; buy-and-hold t0 at the latest first observation among answered holdings, with SERIES_TOO_SHORT beyond it; each field read from its security's node; the sleeve share read by calc name. l-3.AC1 PASS (6) and l-3.AC2 PASS (2) on the merged tree 614554f60f, and the research suite reads 73 passed. No computed element has been fed live yet, so none has been compared with YCharts' printed values.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row(s) IRPT_YCDGEN-W3-S4",
        "org/missions/D9/IRPT/IRPT_YCDGEN/task-orders/IRPT_YCDGEN.TO-YCD-l-3.layout-computed-elements-and-trace.md record face, DRAIN (2.0.0_SA_COO~Y): issuer ruling on row W3-S4, all five conventions CONFIRMED",
        "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round3/DRAIN_END_PACKET.md section 1 (l-3 merged 614554f60f, l-3.AC1 PASS (6), l-3.AC2 PASS (2), 73 passed) and section 2 ('Built but not yet fed live')"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Answered: the row asked the issuer to confirm or amend each convention before the computed sources are graded, and the issuer confirmed all five; no remedy is owed. Comparing computed values with YCharts' printed ones is evidence for the next live run, not a remedy of this row."
  },
  {
    "id": "IRPT_YCDGEN-C-S7",
    "project": "IRPT_YCDGEN",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-05T04:43:00Z",
    "one_line": "W2-S5: the 16-column element and the inferred field paths. The probe paths resolve on round 2's kept answers, and the table_data field paths and the 8-column split belong to a route the round-3 close measured dead (S6), whose graduated remedy re-derives them.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_YCDGEN-W2-S5"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "The issuer accepted the row pending the close run's measurement. The close never reached holdings_bond_exposure_01 or _02: it stopped at step 7, and steps 3-6 (/indices/table_data over the holdings' own tickers) answered 404. This seat read the two probe answers kept by round-2 run YCD-R2-20261004T2315Z-A in memory: the scatter answer carries data.series as a list of 1 item and the snapshot answer carries chart_data as a list of 1 item, so the inferred paths $.data.series[*] and $.chart_data[*] resolve. The 8-column bound came from reading the step-7 challenge as request-shaped; S6 measures it as the 7th request of any run.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row(s) IRPT_YCDGEN-W2-S5",
        "org/missions/D9/IRPT/IRPT_YCDGEN/task-orders/IRPT_YCDGEN.TO-YCD-w-3.map-held-data-own-series-other-endpoint-wiring.md record face, DRAIN: W2-S5 accepted, measured by the close run",
        "s3://opal-data-cottonwood/irpt/cottonwood/state/ycharts_runs/request=YCD-R3-20261005T0219Z/run.json: steps 3-6 holdings_key_stats__c01..c04 status 404; stop at step 7; no holdings_bond_exposure call sent (this compile's read, 2026-10-05 ~02:5xZ to ~04:5xZ, no figure value)",
        "s3://opal-data-cottonwood/irpt/cottonwood/state/ycharts_responses/request=YCD-R2-20261004T2315Z-A/step=01_portfolio_scatter_documented_ids.json and s3://opal-data-cottonwood/irpt/cottonwood/state/ycharts_responses/request=YCD-R2-20261004T2315Z-A/ (the portfolio_snapshot_metrics kept answer): read in memory, data.series a list (1 item), chart_data a list (1 item); keys and types only (this compile's read, 2026-10-05 ~02:5xZ to ~04:5xZ)",
        "investigation row IRPT_YCDGEN-S6: the challenge falls on the 7th request of a run; table_data answers 404 for the holdings' tickers"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Answered or superseded: the probe paths resolve on the kept answers, measured here; the table_data field dialect and the 8-column split belong to a route that answers 404 for these holdings. S6 graduates with the remedy to choose a route and re-derive the field paths and any column split against it, so this row owes no separate remedy."
  },
  {
    "id": "IRPT_YCDGEN-C-S8",
    "project": "IRPT_YCDGEN",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-05T04:43:00Z",
    "one_line": "W4-S1: map_pdf's footer rule is portrait-only; the Multi map carries the landscape footer items as BUILDER_ONLY text, the issuer accepted the repair, and no consumer reads them.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_YCDGEN-W4-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "multi_map.json at CLOUD HEAD keeps each of the 34 landscape pages' footer logo, caption and date as kind text ('page footer logo', 'page footer text', 'page footer date'), BUILDER_ONLY, and renumbers the real charts. This seat's census of the Multi PDF finds 24 charts (19 embedded images that are not page chrome and 5 vector-drawn), all 24 listed in the map and none of them a footer. The issuer accepted W4-S1 to W4-S4 at the drain.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row(s) IRPT_YCDGEN-W4-S1",
        "org/missions/D9/IRPT/IRPT_YCDGEN/task-orders/IRPT_YCDGEN.TO-YCD-m-3.comparison-and-multi-maps.md record face, DRAIN: rows W4-S1..S4 noted, landscape page footers kept as BUILDER_ONLY text",
        "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/maps/multi_map.json at CLOUD HEAD a1b316c5b0: footer text elements on every page; 24 chart elements (this compile's read, 2026-10-05 ~02:5xZ to ~04:5xZ)",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_YCDGEN_ROUND3_L9_GRADE_20261005.md (this seat's m-3.AC2 grade): chart census of the Multi PDF, 19 embedded + 5 vector-drawn, all listed"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Answered: the map-side repair is in place and accepted, so no element is wrong today. A page-size-aware footer rule is owed only if map_pdf regenerates a landscape map, and W4-S4's graduated remedy makes it a condition of that regeneration."
  },
  {
    "id": "IRPT_YCDGEN-C-S9",
    "project": "IRPT_YCDGEN",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-05T04:43:00Z",
    "one_line": "W4-S2: the C-MAP extension for a second and third security (column_sources, key_index, comparison_* calls, {comparison_security_id}) is accepted by the issuer for round 4's layouts; the ETF key's entity parameter is the security-level route question that S6 carries.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_YCDGEN-W4-S2"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "The issuer's YCD-m-3 drain note accepts the extension for round 4's layouts. comparison_map.json and multi_map.json at CLOUD HEAD each carry 12 comparison_* calls beside the 12 portfolio_* calls, and 14 and 86 elements with column_sources. The round-3 close read no comparison key's answer. It measured that /indices/table_data answers 404 for the holdings' own tickers (S6), so the ETF reading of the comparison_* table_data calls (the Multi's iShares Russell 2000 ETF key) is the same unmeasured route as S6's.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row(s) IRPT_YCDGEN-W4-S2",
        "org/missions/D9/IRPT/IRPT_YCDGEN/task-orders/IRPT_YCDGEN.TO-YCD-m-3.comparison-and-multi-maps.md record face, DRAIN: the C-MAP extension for second/third securities accepted for round 4's layouts",
        "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/maps/comparison_map.json and multi_map.json at CLOUD HEAD a1b316c5b0: 24 calls each (12 comparison_*), 14 and 86 elements with column_sources (this compile's read, 2026-10-05 ~02:5xZ to ~04:5xZ)",
        "investigation row IRPT_YCDGEN-S6 (table_data 404 for the holdings' tickers)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Answered: the contract gap is closed by the issuer's acceptance of the extension, and the open measurement (an ETF key's entity parameter on table_data) is part of S6's graduated remedy; this row owes no separate remedy."
  },
  {
    "id": "IRPT_YCDGEN-C-S10",
    "project": "IRPT_YCDGEN",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-05T04:43:00Z",
    "one_line": "W4-S3: Cottonwood's READY Comparison PDF for REQ-e4b7f5ab never prints its comparison key's name; the issuer ruled it is not Comparison evidence, and the map is read from REQ-7ea49c2d, whose retained PDF this seat re-read by its checkpoint.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_YCDGEN-W4-S3"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "The issuer's drain note rules that REQ-e4b7f5ab is not Comparison evidence (no key printed). comparison_map.json's source_pdf names REQ-7ea49c2d9b27957d0ea8888f, artifact prefix ART-2ef3ef7d42a1, 32 pages. This seat located that PDF through irpt-jobs checkpoint_pdf, the irpt-requests ARTIFACT row and its VersionId, read it in memory, and its sha256 equals the checkpoint's; it has 32 pages. Whether a Comparison whose key goes unprinted is a vendor-build defect or a case defect is a question about the served IRPT path, not about this project's cells.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row(s) IRPT_YCDGEN-W4-S3",
        "org/missions/D9/IRPT/IRPT_YCDGEN/task-orders/IRPT_YCDGEN.TO-YCD-m-3.comparison-and-multi-maps.md record face, DRAIN: REQ-e4b7f5ab is not Comparison evidence (no key printed)",
        "boto3 get_item irpt-jobs (tenant cottonwood, job REQ-7ea49c2d9b27957d0ea8888f) checkpoint_pdf.pdf_ref -> irpt-requests ARTIFACT row -> s3://opal-data-irpt/irpt/cottonwood/state/vendor_documents/ART-2ef3ef7d42a1.../ VersionId ZG118xXXEh2pCZozNhAnF9Dw9C3UOujR, sha256 equal to the checkpoint's, 32 pages (this compile's read, 2026-10-05 ~02:5xZ to ~04:5xZ, read in memory)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Answered for this project: the issuer's ruling excludes the PDF as evidence and the map rests on the verified one, so no IRPT_YCDGEN remedy is owed. The served-path question is carried in this compile's header for the CTO's round-3 analysis to place with that path's owner."
  },
  {
    "id": "IRPT_YCDGEN-C-S11",
    "project": "IRPT_YCDGEN",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-05T04:43:00Z",
    "one_line": "S5: the round-3 close's stop row, written by the runner and filed by the issuer, is C-SESSION working as specified (a stop at step 7, the lease released, no retry); its cause is S6's measured bound, which graduates.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_YCDGEN-S5"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Run YCD-R3-20261005T0219Z: run.json reads status STOPPED, stop_reason WAF_REFRESH_REQUIRED at step 7 (holdings_key_stats__c05) status=202, 6 calls recorded. stop_row.json (905 bytes, written 02:20:18Z) sits beside it, surprise-row-shaped, surfaced_at 2026-10-05T02:20:17Z, and its world_is names the step, the status and the decision; the channel row S5 carries the same text. The close record shows runner rc=1, run end 02:20:17Z and the work dir removed, and the packet records the lease released. This is also the first live exercise of the stop-row path that REMEDIATION_v2 row S3 asked for.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row(s) IRPT_YCDGEN-S5",
        "s3://opal-data-cottonwood/irpt/cottonwood/state/ycharts_runs/request=YCD-R3-20261005T0219Z/ listed: run.json and stop_row.json; run.json status, stop_reason and per-call status read; stop_row.json keys and world_is read (this compile's read, 2026-10-05 ~02:5xZ to ~04:5xZ, no figure value)",
        "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/close/YCD-R3-20261005T0219Z_host_run.txt:7, :9 and :17 (RUN status=STOPPED calls=6; STOP row key; runner rc=1)",
        "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round3/DRAIN_END_PACKET.md section 2, attempt 2: STOPPED; the lease was released; the runner wrote stop_row.json, filed as S5"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Answered: the row records the specified behaviour working (C-SESSION: stop, release, file, no retry storm) and asserts no defect of its own; the cause of the stop is S6, graduated in REMEDIATION_v3 with the remedy."
  }
]
```
