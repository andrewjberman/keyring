# IRPT_YCDGEN -- round 5 L8/L9 adjudication (the fifth compile of the project's channel)

<sweep_watermark>2026-10-05T12:58:00Z</sweep_watermark>

Author: 3.0.0_SA_CVO, 2026-10-05 ~19:5xZ. L8 inputs: `surprise-channel/investigations/INVESTIGATION_v1.md` at CLOUD HEAD
7acefc344b (33 rows; the 6 surfaced after REMEDIATION_v4's watermark 2026-10-05T06:43:17Z are this compile's: W1-S2,
W2-S7, W2-S8, W2-S9, W3-S7, W2-S10); the issuer's round-5 drain-end packet
`deliverables/2.0.0_SA_COO~Y/round5/DRAIN_END_PACKET.md` @043a6cc2d1 (2.0.0_SA_COO~Y, msg 105346: 5 orders merged --
r-5 84a7af1854, p-5 306a315dc9, h-5 a979784ea4, m-5 bb0c22bd1e, w-5 ff51386f38; 12 mechanical checks PASS on the merged
tree; m-5.AC3 the judgment criterion for this seat); the close record `close/YCD-R5-E4-leg1_host_run.txt`; and this
seat's own reads for this compile (code and git at CLOUD HEAD 7acefc344b, the project's paths unchanged since
043a6cc2d1; read-only AWS as user/Andrew_Berman: the two retained Comparison and Multi PDFs located by their job
checkpoints and read in memory, labels and coordinates only; no YCharts call). 6 items compiled, all surfaced at or
before the watermark, and none ahead of the clock. 4 are dismissed by the rows below (W1-S2, W2-S7, W2-S8, W3-S7); 2
graduate in `remediations/REMEDIATION_v5.md`, both OPEN (W2-S9, W2-S10), round label v6. ARMED: 0 before, 0 after.

ORDER STATE AT HEAD: 3 of 5 round-5 orders read `complete` at CLOUD HEAD 7acefc344b (p-5, h-5, w-5). YCD-m-5 and
YCD-r-5 read `issued` at HEAD; their DRAIN notes and `complete` flips sit uncommitted in the shared tree (git diff,
this compile's read). The packet's "5 of 5 orders are terminal" holds in the working tree only. The flips are the
issuer's to commit.

NOT COMPILED: row IRPT_YCDGEN-S9 (4.0.0_SA_CRO, the held risk-free object stopped updating on 2026-08-05) sits
uncommitted in the shared tree and is not at HEAD; it belongs to the next compile. Its surfaced_at reads 19:55:00Z and
this seat first read it at 19:44Z by `date -u`.

IN-PLACE CLOCK ADVANCES on `remediations/REMEDIATION_v3.md` (remediation.state and closed only; every other field
byte-equal):
- IRPT_YCDGEN-W4-S4, remediation.state OPEN -> REMEDIATED, closed false -> true. Evidence: m-5.AC3 graded PASS by this
  seat (`org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_YCDGEN_ROUND5_L9_GRADE_20261005.md`). The seven placeholder
  labels carry the name each page prints on the line above the values, and map_pdf's rule at HEAD gives the same seven
  labels on the two PDFs; Multi p9.e08 lists the third security's row on comparison_bond_exposure at key_index 2;
  between 742b4665df and HEAD 0 ids are removed, 0 kinds, pages or sources changed, and the 8 changed or added labels
  hold no figure value.
- IRPT_YCDGEN-W2-S4, remediation.state OPEN -> REMEDIATED, closed false -> true. Evidence: contract 4.3 records the
  decision; the Overview map's p7.e02, e03, e05, e06, e07 and e08 carry alpha_1y, beta_1y, sharpe_1y, sortino_1y,
  max_drawdown_1y and var_monthly_1y at HEAD (they carried null at 742b4665df); p-5.AC3 re-run here reads PASS, 6 of 6;
  `test_layout_overview.py -k "wired or six_statistic"` reads 10 passed, including
  test_wired_statistics_compute_from_the_kept_benchmark_and_the_held_yield. The windows beyond 1y are row W2-S9's.

Re-checked and left OPEN: (1) W3-S6 -- the test half is met (test_wired_both_render_paths_pass_the_two_series passes);
the live half is not: E6 has not run (attempt 1 refused before the lease, the re-run held by the evicted session), so no
run.json traces the four statistics to a value. (2) S7 -- the request hash is built (the E4 leg 1 lookup prints
request_sha256 f464fb7e.. beside sha256 539579bb..) and r-5.AC2 pins the test half; the unchanged-request true arm is E4
leg 2, pending. (3) S6, W2-S3, S3, W3-S2, W3-S3 -- each closes on a live run that has not been made.

Outside this compile: the packet's ruling line "W2-S7: the benchmark ^SPXTR, confirmed at E6" reads ahead of the world.
The order's drain note says "confirmed or corrected by the issuer's live Overview run (E6)", and E6 has not run.

```json
[
  {
    "id": "IRPT_YCDGEN-C-S17",
    "project": "IRPT_YCDGEN",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-05T19:55:00Z",
    "one_line": "W1-S2: lookup.py takes --region with default us-east-1 because contract 5.4 names no region source; the issuer accepted it, and the first live lookup ran on the default and printed the kept record.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_YCDGEN-W1-S2"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "The issuer's drain note on YCD-r-5 accepts W1-S2. The close record of E4 leg 1 shows the lookup run on the resident host after run YCD-R5-E4-20261005T1215Z: LOOKUP firm=cottonwood call=portfolio_level_series_zoom step=2, status 200, shape DATA, a sha256 and a request_sha256 printed, lookup rc=0. The record passes no --region, so the default served.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row(s) IRPT_YCDGEN-W1-S2",
        "org/missions/D9/IRPT/IRPT_YCDGEN/task-orders/IRPT_YCDGEN.TO-YCD-r-5.runner-plan-budget-request-hash-lookup.md record face, DRAIN (2.0.0_SA_COO~Y): Row W1-S2 ACCEPTED (working tree; the note is uncommitted at CLOUD HEAD 7acefc344b)",
        "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/close/YCD-R5-E4-leg1_host_run.txt: LOOKUP firm=cottonwood request=YCD-R5-E4-20261005T1215Z, status 200, shape DATA, runner rc=0 lookup rc=0 (this compile's read, 2026-10-05 ~19:4xZ to ~19:5xZ)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Answered: the issuer accepted the flag and its default, and the first live lookup returned the kept record on that default."
  },
  {
    "id": "IRPT_YCDGEN-C-S18",
    "project": "IRPT_YCDGEN",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-05T19:55:00Z",
    "one_line": "W2-S7: the benchmark call's id ^SPXTR comes from a prior record, not from portfolio_info's answer; no run has sent it yet, and W3-S6's open remedy closes on the live run that would confirm or correct it.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_YCDGEN-W2-S7"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "The issuer's drain note on YCD-p-5 accepts W2-S7 with the id to be confirmed or corrected by the live Overview run (E6). E6 has not run: attempt 1 refused before the lease on a runner defect (fixed @05fc7afa6f) and the re-run is held by the evicted YCharts session (packet section 2). E4 leg 1 sent 2 requests, portfolio_info and the portfolio's level series, and no benchmark call. So ^SPXTR is unmeasured as a fund_data security id. If YCharts refuses it, benchmark_from_kept returns None and alpha and beta read INPUT_MISSING:benchmark; nothing is approximated. REMEDIATION_v4 row W3-S6 (OPEN, v5, owner 2.0.0_SA_COO~Y) closes on one live run whose run.json traces alpha and beta to a value or to a reason other than INPUT_MISSING:benchmark.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row(s) IRPT_YCDGEN-W2-S7",
        "org/missions/D9/IRPT/IRPT_YCDGEN/task-orders/IRPT_YCDGEN.TO-YCD-p-5.budgeted-overview-map-and-statistics-wired.md record face, DRAIN (2.0.0_SA_COO~Y): W2-S7 ACCEPTED -- confirmed or corrected by the issuer's live Overview run (E6)",
        "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round5/DRAIN_END_PACKET.md @043a6cc2d1 section 2: E6 attempt 1 refused before the lease, re-run held",
        "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/close/YCD-R5-E4-leg1_host_run.txt: PLAN requests=2; KEPT step=01_portfolio_info and step=02_portfolio_level_series_zoom only",
        "org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/remediations/REMEDIATION_v4.md row IRPT_YCDGEN-W3-S6 (OPEN, v5)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Carried: the id fails safe to a named reason, and W3-S6's graduated remedy (OPEN) closes on the live run that confirms or corrects it, so this row owes no separate remedy. The packet's 'confirmed at E6' is not yet true: E6 has not run."
  },
  {
    "id": "IRPT_YCDGEN-C-S19",
    "project": "IRPT_YCDGEN",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-05T19:55:00Z",
    "one_line": "W2-S8: Overview element p7.e15 (the benchmark level chart) is not printed on the source PDF; it exists so the benchmark call is read by an element, and the issuer kept it for this round, named as Opal's addition.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_YCDGEN-W2-S8"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "overview_map.json at CLOUD HEAD 7acefc344b holds 254 elements and 8 calls; p7.e15 reads 'Benchmark level series (input to Alpha and Beta)', kind chart, and its label says what it is. Contract C-MAP's 'labels are printed label text only' is not met by this one element, by the issuer's ruling. p-5.AC1 PASS (8 requests for 99 holdings, 0 unread calls) rests on it. The issuer's drain note on YCD-p-5 accepts W2-S8 for this round.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row(s) IRPT_YCDGEN-W2-S8",
        "org/missions/D9/IRPT/IRPT_YCDGEN/task-orders/IRPT_YCDGEN.TO-YCD-p-5.budgeted-overview-map-and-statistics-wired.md record face, DRAIN (2.0.0_SA_COO~Y): W2-S8 ACCEPTED -- p7.e15 stays for this round, named as Opal's addition",
        "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/maps/overview_map.json at CLOUD HEAD 7acefc344b: 254 elements, 8 calls, p7.e15 label and kind (this compile's read, 2026-10-05 ~19:4xZ to ~19:5xZ)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Answered: the issuer accepted the added element for this round with no remedy owed; its label names it as an input chart and not as a printed element. Whether an Opal-added chart stays on the report is a layout decision for the next endpoint revision."
  },
  {
    "id": "IRPT_YCDGEN-C-S20",
    "project": "IRPT_YCDGEN",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-05T19:55:00Z",
    "one_line": "W3-S7: Opal holds the held-data figures for at most 37 of Y-5's 99 holdings; the issuer accepted the census and the worker's mappings, and the question of printing a value on that coverage graduates as W2-S10.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_YCDGEN-W3-S7"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "h-5.AC1 PASS on the merged tree: 158 of 158 rows, 86 OPAL_HELD and 72 NOT_HELD. The issuer's drain note on YCD-h-5 accepts W3-S7 and confirms the worker's sector and region mappings, the group id and the renormalization over the held holdings. The packet carries the wider feed forward (section 4: the handoff to 4.0.0_SA_CRO holds the Opal data inventory and the gaps; section 5 item 3: coverage censuses for Comparison and Multi). This seat did not re-count the 37 of 99; the count is the worker's, measured read-only.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row(s) IRPT_YCDGEN-W3-S7",
        "org/missions/D9/IRPT/IRPT_YCDGEN/task-orders/IRPT_YCDGEN.TO-YCD-h-5.opal-held-census-and-module.md record face, DRAIN (2.0.0_SA_COO~Y): W3-S7 ACCEPTED; the worker's choices CONFIRMED",
        "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round5/DRAIN_END_PACKET.md @043a6cc2d1 sections 1, 4 and 5",
        "org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/remediations/REMEDIATION_v5.md row IRPT_YCDGEN-W2-S10 (OPEN, v6)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Carried: the census and mappings were accepted with no remedy of their own; the consequence that needs a decision (a held value printed on partial coverage) is W2-S10's graduated remedy, and the wider feed is in the handoff to the brief's author."
  }
]
```
