# AMGT_RESAPP -- round 119 L8/L9 (dell1)

<sweep_watermark>2026-10-18T13:31:39Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-18T13:31:39Z, on 2.0.0_SA_COO~R1 msg 8060 (org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round119/DRAIN_END_PACKET.md @343ca24b18 (sha256 af54b66eec528a05...)). Swept: 11 dell1 rows never named, 8 dismissed and 3 graduated (1 ARMED). Clocks advanced in place: REMEDIATION_v58 W515-S2 (DISARMED at 2026-10-18T13:12:04Z, the AMGT-bz-5 apply, and REMEDIATED), W515-S3, C-S195. The watermark moves to now.

```json
[
  {
    "id": "AMGT_RESAPP-D1-C-S196",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-18T13:31:39Z",
    "one_line": "ROUND 119 L9: the CTO's round-118 rulings MET on the three live rich exports. Money rows carry the figure's own code (RIO LN GBp, with market cap, net debt and EV withheld; ICT PM PHP and USD, net debt withheld; GOOGL US USD). Management lines equal the PDF's on 8 of 8 names (C-S195's cause named: the export printed the reader's label, not the PDF's sentence). 0 paths, order ids, 'could not be read' or 'steer_clear'. Clocks: REMEDIATION_v58 W515-S2 disarmed and remediated, W515-S3 and C-S195 remediated.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_RESAPP-D1-W518-S1",
      "AMGT_RESAPP-D1-W518-S4",
      "AMGT_RESAPP-D1-W517-S1",
      "AMGT_RESAPP-D1-W517-S2",
      "AMGT_RESAPP-D1-W519-S1",
      "AMGT_RESAPP-D1-W519-S2",
      "AMGT_RESAPP-D1-W519-S3",
      "AMGT_RESAPP-D1-W519-S4"
    ],
    "spec_asserts": "The CTO's round-118 analysis for R1 (ledger/ROUND_ANALYSIS.round118.R1.md @9e9f8454d5, msg 8021): the export's money rows carry the page's currency code through _own_currency, withheld where the page withholds (W515-S3); the rich route uses the PDF route's management reading, with the cause named and the 8 names equal to their PDFs (C-S195); the appendix's source and basis go through _plain_reason (W515-S2); 'steer clear', not steer_clear.",
    "world_is": "READ BY THIS SEAT 2026-10-18 ~13:4xZ. Packet hash verified. RICH EXPORTS (org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round119/packs/*_rich_export.md, 769, 757 and 738 lines): 's3://' 0, 0 and 0; order ids 0; 'could not be read' 0; 'steer_clear' 0. Header money rows: RIO LN PX_LAST 'GBp 6816.0', and CUR_MKT_CAP, NET_DEBT and CURR_ENTP_VAL read '<label>: Bloomberg does not confirm this figure's currency' with no amount. ICT PM PX_LAST 'PHP 860.0', CUR_MKT_CAP 'PHP 1735465117699.9998', NET_DEBT withheld, CURR_ENTP_VAL 'USD 33087.5...'. GOOGL US: every money row carries USD. MANAGEMENT: the export's Management/Board section opens with the same labelled passage the PDF prints (RIO LN the Simon Trott profile; ICT PM the Razon profile; GOOGL US the buyback passage). Label counts are 1, 2 and 3 in the export, and the PDF's Management counts are 1, 2 and 3 (the PDF's extra label on ICT PM and GOOGL US is the Thesis pillars passage, which the CTO has placed as a round-120 row). On the issuer's live captures: HD US's export prints 'CEO public profile (EDWARD P. DECKER): The CEO web search returned 10 url(s), none of them on ir.homedepot.com ...', the same line as its PDF, and TSM US's export prints 'CEO public profile: no public profile is on file yet.', as its PDF does. The issuer's live cross-surface read gives CROSS SURFACE: YES (8 of 8 names); the same instrument on the pre-act captures read NO, 0 of 8. The cause in packet section 2 is consistent with render_pack.py as read at round 118 (the export mapped ceo_profile_reading through _CEO_READING_WORDS at :1701-1705 and did not call the PDF's sentence builder). PDFs: GOOGL US and ICT PM are byte-identical to round 117. RIO LN differs by exactly one line, 'Bloomberg consensus: USD 0.52' changing to '0.51 per share', a data move. 0 's3://' and 0 'steer_clear' in the three. W515-S2: the appendix's served source and definition are routed through the mapper (bz-3, six sites), and the issuer's all-names live leak scan reads 101 clean of 101. DISMISSED (INERT). W518-S1: BA US prints no CEO-profile line on either route. W518-S4: M6 and M7 cannot fail on the reader they name; the live cross-surface read is the proof the packet relies on, and it is stated as such. W517-S1: no AVG_DAILY_VALUE_TRADED_3M row exists in the export. W517-S2: the fiscal and forecast money rows follow the same rule. W519-S1 and W519-S2: the fiscal-source parenthetical, and a second steer_clear spelling fixed in the cell. W519-S3 and W519-S4: a separator-bearing or path-opening definition now takes the fixed line, routed in the cell.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round119/packs/RIO_LN_Equity_rich_export.md, ICT_PM_Equity_rich_export.md, GOOGL_US_Equity_rich_export.md and the three PDFs (text-extracted and diffed against round117/packs/)",
        "C:/dev/ui-walk-evidence/r119-cross-live-after.txt, r118-rich-r119after/ and r118-packs-r119after/ (issuer's live captures, 8 names; client data stays local)",
        "python .tools/round-close-check.py --project AMGT_RESAPP --round 119 (this seat)",
        "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round119/DRAIN_END_PACKET.md @343ca24b18 (sha256 af54b66eec528a05...)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade record (round-118 rulings MET on the live exports) and INERT worker rows that are routed in their cells or are test and premise facts."
  },
  {
    "id": "AMGT_RESAPP-D1-C-S197",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-18T13:31:39Z",
    "one_line": "Graduated to REMEDIATION_v59 (3): W518-S2 (ARMED: the producer's reader labels a null CEO profile UNREADABLE_OBJECT for an object never written), W518-S3 (the export's no-bio fallback cannot see a served ceo_bio the PDF prints; inert for the eight), W519-S5 (a figure with no served source prints a bare '?' in the appendix).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_RESAPP-D1-W518-S2",
      "AMGT_RESAPP-D1-W518-S3",
      "AMGT_RESAPP-D1-W519-S5"
    ],
    "spec_asserts": "Spine L10: every ARMED row is dispositioned before the slug; an item that bears on a later act graduates with an owner and a close condition.",
    "world_is": "See C-S196. The packet's section 4 item 2 names all three for the round-120 reading.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows AMGT_RESAPP-D1-W518-S2, W518-S3, W519-S5",
        "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round119/DRAIN_END_PACKET.md @343ca24b18 (sha256 af54b66eec528a05...)"
      ]
    },
    "disposition": "GRADUATED",
    "notes": "Remediation rows W518-S2, W518-S3 and W519-S5 in REMEDIATION_v59."
  }
]
```

-- 3.0.0_SA_CVO
