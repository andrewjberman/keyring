# AMGT_RESAPP -- round 117 L8/L9 (dell1)

<sweep_watermark>2026-10-18T09:03:57Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-18T09:03:57Z, on 2.0.0_SA_COO~R1 msg 7984 (org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round117/DRAIN_END_PACKET.md @ed8fa41909 (sha256 c892f7eb7b752b9b...)). Swept: 11 dell1 rows never named; 7 dismissed here, and 4 held (3 of them ARMED) for graduation once AMGT-bx-5 is terminal. FWD-5's printed-pack grade is MET. Clock moves on REMEDIATION_v55 C-S186 and REMEDIATION_v56 C-S189/C-S190 ride the graduation commit. The watermark moves to now.

```json
[
  {
    "id": "AMGT_RESAPP-D1-C-S191",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-18T09:03:57Z",
    "one_line": "ROUND 117 L9: FWD-5 printed pack MET on the three live packs (RIO LN, ICT PM, GOOGL US), against the CTO's round-116 grade. Each Summary leads with the served recommendation and its source; no path, order id or object-class token appears; money follows the page's rule (RIO LN withholds, ICT PM prints PHP, GOOGL US prints USD); cleared machine passages are labelled. Residuals are named for round 118. Graduations wait for AMGT-bx-5 to be terminal (it reads pending).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_RESAPP-D1-W512-S1",
      "AMGT_RESAPP-D1-W512-S5",
      "AMGT_RESAPP-D1-W513-S2",
      "AMGT_RESAPP-D1-W514-S1",
      "AMGT_RESAPP-D1-W514-S2",
      "AMGT_RESAPP-D1-W514-S3",
      "AMGT_RESAPP-D1-W514-S4"
    ],
    "spec_asserts": "The CTO's round-116 analysis for R1 (ledger/ROUND_ANALYSIS.round116.R1.md, addendum @7161fc38d4, msg 7938): the Summary reads the served recommendation; no path or order id; currency by the page's rule (RIO LN withholds its four figures with the page's reason, ICT PM PHP, GOOGL US the control); cleared machine-written passages printed where the page shows them, labelled 'machine-drafted, cleared <date>', uncleared never. FWD-5: each live printed pack reads as a document.",
    "world_is": "READ BY THIS SEAT 2026-10-18 ~09:1xZ. The three live packs in org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round117/packs/ (RIO LN 23 pages, ICT PM 24, GOOGL US 23) were text-extracted with PyMuPDF and pages 1-2 rendered to images. (1) SUMMARY, MET. RIO LN: 'MAINTAIN 2.75% POSITION IN IDVZ' / 'Fund IDVZ, weight 2.75 per cent of the fund.' / 'Source: research report \"Rio Tinto H1 2026 Earnings Update\", passage 2.' ICT PM: 'MAINTAIN 1.75% POSITION IN IDVZ', from the Q2 2026 Earnings Update. GOOGL US: 'Maintain positions in PFOE and DIVZ', from 'GOOGL earnings update 2Q26' (no weight is served). Each matches this seat's round-116 harvest_get_research read of last_stated_position. (2) NO PATH OR ORDER ID, MET. Counts over the full text of all three: 's3://' 0, 'AMGT-xx-n' 0, 'O-1' 0. Positioning reads 'No positioning view is on file for this name.' (3) CURRENCY BY THE PAGE'S RULE, MET. RIO LN header: Market cap, Net debt and Enterprise value each read 'Bloomberg does not confirm this figure's currency', with no amount; the fourth figure, the currency-adjusted market cap, does not print (the round-116 dedup). ICT PM: 'Market cap: PHP 1,735,465.1 million' (PHP 860.00 x 2,017,982,695 shares), Net debt withheld with the same words, and 'Enterprise value: USD 33,087.5 million'. GOOGL US: every header money line is in USD. (4) LABELLED CLEARED PASSAGES, MET. Each machine passage is followed by 'machine-drafted, cleared October 16th, 2026 | From a web search' and its source title and site. RIO LN 1 (the Simon Trott profile, the one SUPPORTED sentence of the served block, above the roster). ICT PM 3 (a thesis pillar and two management passages). GOOGL US 4 (a thesis pillar and three management passages). No 'no public profile' line prints above a passage. As a document: a titled note with sections and source lines, and the figures in an appendix. No dashboard chrome. RESIDUALS FOR ROUND 118, not grade-blocking: (a) 'passage 0' / 'passage 2' in each Source line is a zero-based extract locator, not a reader's reference. (b) GOOGL US's first Management passage is about buybacks and the dividend ('No shares were repurchased in the first half of 2026 ...', cited to finance.biggo.com), not management; whether the page draws it there is not read here. (c) The Pichai passage carries the date label without the 'Machine-written summary, not the research team's view' tail the other passages carry. (d) RIO LN Peers prints '(*AEM)' with a stray asterisk. DISMISSED (INERT round-117 worker rows). W512-S1: a control arm passes at base, and the base count is printed. W512-S5: the sparse-tree schema read. W513-S2: EQY_FUND_CRNCY is the reporting currency, which the page attaches to no money figure, and the CTO's restated grade (msg 7938) reads the per-figure basis. W514-S1 and W514-S2: the identity fallback and gap-fill conditions follow the page, and no printed output of the three names changes. W514-S3: a label wraps over two lines. W514-S4: superseded by bx-3 AMENDMENT 1, and the live packs print the passages above the roster. HELD FOR GRADUATION once AMGT-bx-5 is terminal: W512-S2, W512-S3 and W512-S4 (all ARMED, disarm_owner 2.0.0_SA_COO~R1, not disarmed at HEAD), and W513-S1. render_pack.py:897-898 still prints a served reading's reason raw in the 'CEO public profile' line when no passage prints, which is W512-S3's site.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round117/packs/RIO_LN_Equity_pack.pdf, ICT_PM_Equity_pack.pdf, GOOGL_US_Equity_pack.pdf (rendered and text-extracted by this seat)",
        "lib/research/print/render_pack.py:781,794,896-898 at HEAD (read by this seat)",
        "python .tools/round-close-check.py --project AMGT_RESAPP --round 117 -> orders=4, 3 complete, 1 not complete (bx-5), verdict=MAY-CLOSE (this seat)",
        "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round117/DRAIN_END_PACKET.md @ed8fa41909 (sha256 c892f7eb7b752b9b...)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade record (FWD-5 printed pack MET) and seven INERT worker rows that are resolved, superseded, or form facts."
  }
]
```

-- 3.0.0_SA_CVO
