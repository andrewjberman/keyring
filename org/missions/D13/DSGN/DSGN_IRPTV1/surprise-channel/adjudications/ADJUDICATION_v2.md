# DSGN_IRPTV1 -- round 3 adjudication (judgment grades)

Author: 3.0.0_SA_CVO. Round: 3 (document v2). Fabric: laptop. Recorded: 2026-09-25T17:42:21Z.

Input snapshot: workspace @98c72cdfb0 (drain-end), portal DEV 8242412d (= origin DEV per 2.0.0_SA_COO~D msg 100983).
Round 3 = IV-e-9..IV-e-20, twelve orders, every one `<risk>LOCAL`.

**Scope, stated.** Spine L8 (`org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md:464-466` at HEAD): "In a round of `LOCAL`
cells only, the CVO is not engaged. The COO's drain-end message then carries the real-run record and the round's
`BLOCKING` and `ARMED` rows to the CTO, and stands in for the slug." The twelve issued orders nonetheless name
`3.0.0_SA_CVO` as the grader of each AC4, "never self-graded". This document grades those twelve criteria and nothing
more:
- no L8 compile of the channel;
- no disposition of the ARMED rows, which the spine sends to 1.0.0_SA_CTO in a LOCAL round;
- no remediation document.

**ARMED investigation rows with no adjudication row** (census over INVESTIGATION_v1.md at this vintage, 41 rows; 8
dispositioned in ADJUDICATION_v1): S3, S5, S6, S7, S9, W10-S1, W7-S1, W7-S2, W9-S1, W9-S4, W11-S1, W11-S2, W11-S3,
W11-S4 (14). Later rows record disarms for some of them: S14 records W11-S3 and W11-S4 disarmed at the drain, and
the COO's message records W11-S1 and W11-S2 disarmed by the CTO's R6. They are listed here and not adjudicated.

**FAST interval** (spine Closer, FAST: "the CVO's next slug carries one section on the FAST interval"). The grades are
in `org/tier1_exec/3.0.0_SA_CVO/deliverables/DSGN_IRPTV1_FAST_PIN_GRADES_20260924.md@ddb0339061`: 16 pins, 14 PASS,
1 FAIL (`68f46e18`, row S10), 1 not graded. On this close run:
- N1 is fixed: Generate reads "Client: the client selected above".
- N2 is fixed on the probe: `unavailableWord:false`.
- N3 is fixed: "Observed: September 23rd, 2026, 8:00p ET".
- N4 is fixed: "Opal supervised" / "Advised".
- N5 is not evidenced: no Allocation bars at rest.

Tally: 12 of 12 AC4 criteria graded. 2 PASS, 5 FAIL, 5 NOT_EVALUATED.

```json
[
  {
    "id": "DSGN_IRPTV1-C-S15",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-25T17:42:21Z",
    "one_line": "Round-3 L9 judgment grades on the COO's close run: 2 PASS (IVE15, IVE17), 5 FAIL (IVE10, IVE14, IVE16, IVE18, IVE19), 5 NOT_EVALUATED (IVE9, IVE11, IVE12, IVE13, IVE20: the object is not on the close run).",
    "class": "OBSERVATION",
    "spec_asserts": "The twelve round-3 orders IV-e-9..IV-e-20 each name 3.0.0_SA_CVO as the L9 grader of their AC4 judgment criterion, 'from the real run on localhost:5174 the COO takes at the drain', never self-graded.",
    "world_is": "The COO's close run covers five screens at rest (two sample views; Performance, Holdings, Analysis with a client) on a fixture with no model level. It never opens 'More holdings views', never drills, never opens the picker, never generates a report, and never visits Positioning or Model Portfolios.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/round3-close.run.txt@98c72cdfb0 (read in full)",
        "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/round3-close.01..05-*.png@98c72cdfb0 (each viewed)",
        "portal DEV 8242412d: src/pages/InvestorReporting/index.tsx:190-195 (read); gen-wire.ts re-run in a sparse scratch worktree",
        "the twelve AC4 clauses, read at each task order's criterion line"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Grade record only: this row opens and adjudicates no investigation item.",
    "grades": [
      {
        "criterion": "IVE9-AC4",
        "instance": "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~7/DSGN_IRPTV1.TO-IV-e-9.shared-search-and-paginator.proof_of_spec.json@a9e8bd1983",
        "verdict": "NOT_EVALUATED",
        "reason": "Bar (IVE9-AC4, FWD-3 ACCEPT): the picker reads as the portal dropdown, legible, no clipped name, on 1440 and on each other importer before/after. Reachable in the COO's close run (deliverables/2.0.0_SA_COO~D/round3-close.run.txt and the .01-.05 PNGs @98c72cdfb0, portal DEV 8242412d, fixture round3-close.fixture.json): the CLOSED picker only (legible ink, 'Cottonwood Trust', no clipping, all five PNGs). Unreachable: the open suggestion list, the paged list, and any other importer's before/after -- none is in the run. Row S14 separately names no combobox/listbox roles and no keyboard navigation."
      },
      {
        "criterion": "IVE10-AC4",
        "instance": "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~7/DSGN_IRPTV1.TO-IV-e-10.accounts-in-the-view.proof_of_spec.json@3183f567f2",
        "verdict": "FAIL",
        "reason": "Bar (IVE10-AC4, FWD-2 ACCEPT): narrow to one account from inside Holdings AND Performance. Holdings passes: 04-holdings.png shows 'Account: All accounts' beside the view (probe accountFilter:1). Performance does not: the probe reads accountFilter:0 on the client Performance DOM and 03-performance.png shows no account control; the accounts table sits in the collapsed 'Monthly returns and accounts'."
      },
      {
        "criterion": "IVE11-AC4",
        "instance": "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~8/DSGN_IRPTV1.TO-IV-e-11.model-colour-by-code.proof_of_spec.json@7b1bf213e3",
        "verdict": "NOT_EVALUATED",
        "reason": "Bar (IVE11-AC4, FWD-12 ACCEPT): Ultra Long-Term red as on Model Portfolios; no model changes colour between charts, tabs or pages, on before/after screenshots. The close fixture carries no model node: 04-holdings.png shows securities (IEFA, SPHY) as the top categories and 'Model coverage 0 of 2 accounts'. No Opal model is on screen, and no Model Portfolios before/after is in the run."
      },
      {
        "criterion": "IVE12-AC4",
        "instance": "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~8/DSGN_IRPTV1.TO-IV-e-12.cash-green-and-unclassified.proof_of_spec.json@a971f70a93",
        "verdict": "NOT_EVALUATED",
        "reason": "Bar (IVE12-AC4, FWD-13 ACCEPT): equities blue, fixed income and cash green, alternatives orange, structured pink, commodities gold, the same on Positioning. The Securities map sits in the collapsed 'More holdings views' in 04-holdings.png and Positioning is not in the run. The only security colours on screen are the drill pie's IEFA purple and SPHY cyan, which row S14 attributes to a name-hash palette, not the served class."
      },
      {
        "criterion": "IVE13-AC4",
        "instance": "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~8/DSGN_IRPTV1.TO-IV-e-13.drill-on-the-map.proof_of_spec.json@99d2abb0ef",
        "verdict": "NOT_EVALUATED",
        "reason": "Bar (IVE13-AC4, FWD-14 ACCEPT): drill total assets -> models -> one model's securities on the map; no chart breaks. The run never opens 'More holdings views' (the map) and never drills; the fixture has no model level, so the pie's stop at models cannot show."
      },
      {
        "criterion": "IVE14-AC4",
        "instance": "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~9/DSGN_IRPTV1.TO-IV-e-14.analysis-cards-and-prospect.proof_of_spec.json@d439b73b1d",
        "verdict": "FAIL",
        "reason": "Bar (IVE14-AC4, FWD-7/FWD-8; the issuing cell IV-e-14 (a): 'with a client chosen, the cards come first'). 05-analysis.png, client chosen: the three variant cards render in the Philosophy style and the upload has a visible drop zone and state, but the Prospect portfolio upload panel sits ABOVE the cards. No report is completed in the run (Generate disabled; 'No job submitted from this browser yet'), so 'completes one report' is unshown. The Report title placeholder prints the code 'C-CW-01 -- Overview'."
      },
      {
        "criterion": "IVE15-AC4",
        "instance": "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~10/DSGN_IRPTV1.TO-IV-e-15.sample-view.proof_of_spec.json@899e6814d4",
        "verdict": "PASS",
        "reason": "Bar (IVE15-AC4, FWD-17 ACCEPT): with no client, each tab shows what it will show; nothing could be mistaken for real numbers. 01-sample-performance.png and 02-sample-holdings.png: every panel carries a SAMPLE badge and 'Illustrative sample -- not a client's data'; one prompt, 'Choose a client, relationship or account above'. Probe sampleBadges:3, choosePrompts:1 on both. Note for the outcome read, not this criterion: FWD-17's 'eye-catching' limb reads weakly, because the sample visuals are grey placeholder bars."
      },
      {
        "criterion": "IVE16-AC4",
        "instance": "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~10/DSGN_IRPTV1.TO-IV-e-16.export-and-tab-order.proof_of_spec.json@4047bdbea7",
        "verdict": "FAIL",
        "reason": "Bar (IVE16-AC4, FWD-9/FWD-10 ACCEPT): export the tab being looked at from one place; tabs read Performance, Holdings, Analysis. Tab order passes, and there is one header Export with no per-tab buttons (probe headerExport:1, perTabExport:0). Exporting the looked-at tab fails on Holdings: 04-holdings.png shows the Export in its disabled style with a client chosen. portal/src/pages/InvestorReporting/index.tsx:190-195 at DEV confirms 'Holdings has no export kind (see EXPORT_KIND_BY_TAB)'. The remedy is an export kind for Holdings, which is the export producer's territory (PRD FWD-9)."
      },
      {
        "criterion": "IVE17-AC4",
        "instance": "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~9/DSGN_IRPTV1.TO-IV-e-17.wire-regen.proof_of_spec.json@75aab6f6a7",
        "verdict": "PASS",
        "reason": "Bar (IVE17-AC4): no stray hand edit in the regenerated diff. I re-ran gen-wire.ts at portal 8242412d in a sparse scratch worktree against the workspace contracts: WIRE TYPES GENERATED 23 of 23, RESPONSE ENVELOPES 17 of 17, rc=0, 26 files rewritten. Content diff: 4 lines in 2 files (HoldingsSnapshot asset_class gains 'other'; submit-export data becomes optional). Both follow producer schema commits 3d5a590ad0 and f6fd60f4fd, landed after the generation; the committed files cite the prior schema hashes, @a73241ef66 and @7915bc9b2c. Every other line is byte-equal to generator output."
      },
      {
        "criterion": "IVE18-AC4",
        "instance": "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~11/DSGN_IRPTV1.TO-IV-e-18.client-language-sweep.proof_of_spec.json@d2573bc4b6",
        "verdict": "FAIL",
        "reason": "Bar (IVE18-AC4, FWD-15 ACCEPT: no code string, key or reason code on any body). Fixed on the run: no UNAVAILABLE, raw ISO, acc_ id or status-band code (probe), 'Opal supervised' / 'Advised' in words, the status band in 'Report details'. Still on the bodies: the 'F-CW' firm chip on Performance and Holdings (03, 04; IV-e-18 named FirmAttribution for the move), 'F-CW -- Account' in the identity card, the Analysis Report title 'C-CW-01 -- Overview', and the 'Opal model or ETF key' placeholder (05)."
      },
      {
        "criterion": "IVE19-AC4",
        "instance": "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~11/DSGN_IRPTV1.TO-IV-e-19.progressive-disclosure.proof_of_spec.json@68cc8f94bd",
        "verdict": "FAIL",
        "reason": "Bar (IVE19-AC4, FWD-16 ACCEPT: at rest a headline and one main picture; the rest behind a toggle, tile, pop-up or help tip). Performance passes: the headline, the cumulative chart, and 'Report details' and 'Monthly returns and accounts' collapsed (03). Holdings is close: the summary and Asset Category Views, with 'More holdings views' collapsed (04). Analysis fails: with a client chosen, the full Prospect upload form and the full Generate form are both open at rest (05, about 1,900 px tall)."
      },
      {
        "criterion": "IVE20-AC4",
        "instance": "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~11/DSGN_IRPTV1.TO-IV-e-20.light-look.proof_of_spec.json@6c8a16b536",
        "verdict": "NOT_EVALUATED",
        "reason": "Bar (IVE20-AC4, FWD-18 ACCEPT): Andrew gives the page a once-over on a real client and finds nothing off the light look. The reader the bar names is Andrew, on a real client; the close run is fixture-driven (row S14) and no once-over by Andrew is recorded. The CVO does not stand in for Andrew's eye. Seen, for his pass: every panel header is a navy bar, and the sample visuals are grey."
      }
    ]
  }
]
```
