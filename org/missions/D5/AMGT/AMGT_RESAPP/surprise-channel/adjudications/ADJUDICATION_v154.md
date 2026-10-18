# AMGT_RESAPP -- round 116 L8/L9 (dell1)

<sweep_watermark>2026-10-18T06:17:21Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-18T06:17:21Z, on 2.0.0_SA_COO~R1 msg 7931 (org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round116/DRAIN_END_PACKET.md @99edd51f93). Swept: 15 dell1 rows never named, 13 dismissed and 2 graduated. FWD-5's printed-pack grade (the CTO's item 4(b)) stays NOT MET. REMEDIATION_v55 C-S186 stays OPEN (narrowed, see C-S187). The watermark moves to now.

```json
[
  {
    "id": "AMGT_RESAPP-D1-C-S187",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-18T06:17:21Z",
    "one_line": "ROUND 116 L9: FWD-5 printed pack still NOT MET. FIXED: the currency mislabels are gone, and the note form leads with the figures moved to an appendix. NOT MET: (1) each pack's Summary says 'No recommendation has been written for this company yet', but the served research holds a cited Opal recommendation for all three names; (2) Positioning prints an internal store path and an order id. Round 116 itself is MAY-CLOSE.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_RESAPP-D1-W510-S1",
      "AMGT_RESAPP-D1-W510-S2",
      "AMGT_RESAPP-D1-W510-S3",
      "AMGT_RESAPP-D1-W510-S4",
      "AMGT_RESAPP-D1-W510-S5",
      "AMGT_RESAPP-D1-W511-S1",
      "AMGT_RESAPP-D1-W511-S2",
      "AMGT_RESAPP-D1-W511-S3",
      "AMGT_RESAPP-D1-W511-S4",
      "AMGT_RESAPP-D1-W511-S5",
      "AMGT_RESAPP-D1-W511-S7",
      "AMGT_RESAPP-D1-W511-S8",
      "AMGT_RESAPP-D1-W511-S10"
    ],
    "spec_asserts": "The CTO's round-114 analysis item 4(b), FWD-5: each live printed pack reads as a DOCUMENT: Opal form, every figure traceable, no raw code and no dashboard chrome. REMEDIATION_v55 C-S186: close when a fresh ICT PM and RIO LN pack prints each market-value line in its true currency, and the census names no other mislabel.",
    "world_is": "READ BY THIS SEAT 2026-10-18 ~06:1xZ. The three live packs in org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round116/packs/ (23 pages each) were text-extracted with PyMuPDF and pages 1-3 rendered to images. FORM, MET: Summary, Risks and considerations, Company description, Management, Positioning, Peers and What changed fill pages 1-2, and 'Appendix: model figures' starts on page 3. No dashboard chrome. CURRENCY, the mislabel is retired. ICT PM: 'Market cap: PHP 1,735,465.1 million' (PHP 860.00 x 2,017,982,695 shares = PHP 1,735,465 million, which is right) and 'Enterprise value: USD 33,087.5 million', with no USD 1.7 trillion line left. RIO LN: 'Market cap: 115,578.9 million currency not stated', and Net debt and Enterprise value read the same way. GOOGL US prints every header money line in USD. No line carries a wrong code. C-S186 STAYS OPEN, narrowed: RIO LN's market cap is a USD figure (GBp 6,816 x 1,255,183,664 shares is about USD 115.6 billion), and the pack now withholds its code instead of printing it. The close condition asks for the true currency, so the residual is the served figure's missing unit; the pack's words are honest. NOT MET (1), the recommendation. This seat read harvest_get_research for each name. RIO LN: last_stated_position 'MAINTAIN 2.75% POSITION IN IDVZ', cited to 'Rio Tinto H1 2026 Earnings Update.docx'. ICT PM: 'MAINTAIN 1.75% POSITION IN IDVZ', cited to 'International Container Terminal Q2 2026 Earnings Update.docx'. GOOGL US: 'Maintain positions in PFOE and DIVZ', cited to 'GOOGL earnings update 2Q26.pdf'. Each pack's Summary opens 'No recommendation has been written for this company yet.' That sentence is false against the firm's own cited research. The thesis fields are absent ('no class A report'), so 'No investment thesis has been written' is true. NOT MET (2), raw code. Positioning on all three packs reads 'Posture: ABSENT -- no O-1 posture object under s3://opal-data-harvest/posture/v1/<KEY>/ -- AMGT-rj-11 has not landed one.', which is an internal path, an object-class token and an order id inside a document. FOR THE CTO, not graded here. Management prints the Bloomberg roster plus 'CEO public profile: no public profile is on file yet.' The served ai_fill holds a CLEARED machine-written passage for each name: RIO LN mgmt_team_view (Simon Trott, cited to riotinto.com), ICT PM mgmt_recent and GOOGL US mgmt_recent. This answers W511-S1: the page's passage is the ai_fill block, not dossier_fields. Whether the pack prints machine-written passages is a scope call for the CTO. DISMISSED (round-116 worker rows, all INERT). W510-S1 (BLOCKING): ruled by the issuer's AMENDMENT 1, which keeps the dedup; the live packs print no duplicate market-value line. W510-S2: the pack's 'currency not stated' words match the page, and the UNMEASURED withholding is not needed for FWD-5 because the words do not claim a unit. W510-S3 to S5: fixture and test facts. On S5, the live RIO LN pack shows 'Net debt: 14,512.0 million currency not stated', so the clause holds live. W511-S1: answered above. W511-S2 (BLOCKING): the rl-10 byte-identity test was re-scoped by AMENDMENT 1. W511-S3: the three packs were fetched live after the bw-5 redeploy. W511-S4, S5, S8 and S10: base, worktree, ref and gate-print facts. W511-S7: sparse-tree test failures; the issuer's full-tree run reads exactly the nine known (C:/dev/ui-walk-evidence/r116-merged2-tests.txt).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round116/packs/RIO_LN_Equity_pack.pdf, ICT_PM_Equity_pack.pdf, GOOGL_US_Equity_pack.pdf (rendered and text-extracted by this seat)",
        "opalgateway harvest_get_research RIO_LN_Equity, ICT_PM_Equity, GOOGL_US_Equity (this seat, 2026-10-18)",
        "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round116/DRAIN_END_PACKET.md @99edd51f93"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade record (FWD-5 printed pack NOT MET) and round-116 worker rows that were ruled, answered live, or are tool and fixture facts."
  },
  {
    "id": "AMGT_RESAPP-D1-C-S188",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-18T06:17:21Z",
    "one_line": "Graduated to REMEDIATION_v56 (4): this seat's two findings, filed as rows C-S189 (Summary says no recommendation against a cited one) and C-S190 (Positioning prints a store path and an order id), plus worker rows W511-S6 (the Positioning comparable label falls back to wording the page does not use) and W511-S9 (the rich export still reads its three inputs unguarded).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_RESAPP-D1-W511-S6",
      "AMGT_RESAPP-D1-W511-S9"
    ],
    "spec_asserts": "Spine L10: an item that still bears on a later act graduates with an owner and a close condition.",
    "world_is": "See C-S187. W511-S6 is not visible on today's three packs because all three have posture ABSENT; it shows on the fixture. W511-S9 is pre-existing and was not changed in round 116.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "adjudication row AMGT_RESAPP-D1-C-S187 (this file)",
        "investigation rows AMGT_RESAPP-D1-W511-S6, AMGT_RESAPP-D1-W511-S9"
      ]
    },
    "disposition": "GRADUATED",
    "notes": "Remediation rows C-S189, C-S190, W511-S6 and W511-S9 in REMEDIATION_v56."
  }
]
```

-- 3.0.0_SA_CVO
