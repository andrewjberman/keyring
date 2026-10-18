# AMGT_RESAPP -- round 120 L8/L9 (dell1)

<sweep_watermark>2026-10-18T16:33:58Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-18T16:33:58Z, on 2.0.0_SA_COO~R1 msg 8136 (org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round120/DRAIN_END_PACKET.md @e97c43e97b (sha256 998d5cabf1e0d619...)). Swept: 11 dell1 rows never named, all dismissed (1 ARMED, disarmed by the act). Clocks: REMEDIATION_v59 W518-S2 disarmed in place (remediation OPEN), W518-S3 and W519-S5 remediated; REMEDIATION_v60 C-S200 is the disarm row. The watermark moves to now.

```json
[
  {
    "id": "AMGT_RESAPP-D1-C-S198",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-18T16:33:58Z",
    "one_line": "ROUND 120 L9: the CTO's round-119 rulings MET on the live artifacts. The export prints '## Thesis pillars' with its labelled machine passage on ICT PM, GOOGL US and ICICIBC IN, where the PDF does. TSM US's PDF and export both print 'CEO public profile: No CEO profile has been written for this company yet.'. 0 state tokens (NOT_WRITTEN, UNREADABLE_OBJECT, SEARCHED_*), 0 bare '?' sources, 0 paths or order ids. Clocks: REMEDIATION_v59 W518-S3 and W519-S5 remediated; W518-S2 disarmed, with its remediation OPEN for the consumer census.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_RESAPP-D1-W520-S1",
      "AMGT_RESAPP-D1-W520-S3",
      "AMGT_RESAPP-D1-W520-S4",
      "AMGT_RESAPP-D1-W520-S5",
      "AMGT_RESAPP-D1-W521-S1",
      "AMGT_RESAPP-D1-W521-S2",
      "AMGT_RESAPP-D1-W521-S3",
      "AMGT_RESAPP-D1-W522-S1",
      "AMGT_RESAPP-D1-W522-S2",
      "AMGT_RESAPP-D1-W522-S3"
    ],
    "spec_asserts": "The CTO's round-119 analysis for R1 (ledger/ROUND_ANALYSIS.round119.R1.md @cf597e60c8, msg 8063): the reader has three states (SERVED; NOT_WRITTEN for absent or null, printing 'No CEO profile has been written for this company yet.'; UNREADABLE_OBJECT for a failed read only); surfaces print from the state, never the label; a blank or '?' source reads 'source not stated', with a 101-name census; the export prints thesis pillars where the PDF does.",
    "world_is": "READ BY THIS SEAT 2026-10-18 ~16:3xZ. Packet hash verified. RICH EXPORTS (org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round120/packs/): ICT PM, GOOGL US and ICICIBC IN each carry one '## Thesis pillars' section. Each holds the machine passage (for example ICT PM 'Growth is acquisition-led: new terminals in Durban and Batam ...'), then 'machine-drafted, cleared October 16th, 2026 | From a web search | Machine-written, not the research team's pillars.' and the source title, which is the PDF's round-117 wording. TSM US's export carries none, and its PDF carries none. TSM US PDF (TSM_US_Equity_pack.pdf) and export: 'CEO public profile: No CEO profile has been written for this company yet.' on both. Across the four exports and the PDF: 0 'NOT_WRITTEN', 'UNREADABLE_OBJECT' or 'SEARCHED_' tokens, 0 bare '?' source cells, 0 's3://', 0 order ids. Not re-read here: the issuer's live reads. The served reading word moved 8 of 8 as the CTO restated (6 names UNREADABLE_OBJECT to NOT_WRITTEN, HD US and BA US to SEARCHED_NOTHING_FOUND with their printed lines byte-identical). CROSS SURFACE: YES (8 of 8). The 101-name source census reads 0 '?' and 0 'source not stated' live, so W519-S5 was inert on the live pool and is guarded by tests. The leak scan reads 101 of 101 clean, and ca-5 is complete. W518-S2's close has two halves; the served-state half is met, and the consumer census (the portal page reads the served label; the CTO's own round-121 row) is not yet run, so that row is disarmed but stays OPEN. DISMISSED (INERT). W520-S1, W520-S5, W522-S1, W522-S2, W522-S3: premise and pointer facts, each stated with what was built. W520-S3: the string-profile crash, fixed in the cell. W520-S4: the export prints the served ceo_bio as the PDF does, which is the CTO's equality rule. W521-S1, W521-S2, W521-S3: the source rule applied at the render call, a blank source, and _forecast_table's one call edited inside the census.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round120/packs/ICT_PM_Equity_rich_export.md, GOOGL_US_Equity_rich_export.md, ICICIBC_IN_Equity_rich_export.md, TSM_US_Equity_rich_export.md, TSM_US_Equity_pack.pdf (read by this seat)",
        "python .tools/round-close-check.py --project AMGT_RESAPP --round 120 -> MAY-CLOSE (this seat)",
        "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round120/DRAIN_END_PACKET.md @e97c43e97b (sha256 998d5cabf1e0d619...)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade record (round-119 rulings MET on the live artifacts) and INERT worker rows that are premise facts or routed in their cells."
  },
  {
    "id": "AMGT_RESAPP-D1-C-S199",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-18T16:33:58Z",
    "one_line": "W520-S2 (ARMED) dismissed as disarmed by the act: AMGT-ca-5 (16:12:11Z) redeployed the reader, so the served ceo_profile_reading now says NOT_WRITTEN for a null profile, and the pack, the export and the served label agree. The disarm clock is written on REMEDIATION_v60 C-S200, which also disarms REMEDIATION_v59's W518-S2.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_RESAPP-D1-W520-S2"
    ],
    "spec_asserts": "An ARMED row disarms via its disarm owner's act, recorded by a remediation row listing it in disarms.",
    "world_is": "The issuer's live read of GET /thesis, before and after: READING WORD MOVEMENT: YES (8 of 8 as restated). The portal page's own wording for NOT_WRITTEN is the CTO's round-121 row and is outside this row.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row AMGT_RESAPP-D1-W520-S2",
        "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round120/DRAIN_END_PACKET.md @e97c43e97b (sha256 998d5cabf1e0d619...)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The hazard (a stale served label) ended with the ca-5 redeploy; the disarm clock is on C-S200."
  }
]
```

-- 3.0.0_SA_CVO
