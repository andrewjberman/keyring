# AMGT_HARVST -- round 95 L8 (dell1)

<sweep_watermark>2026-10-18T11:51:23Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-18T11:51:23Z, on 2.0.0_SA_COO~W1 msg 8023 (org/missions/D5/AMGT/AMGT_HARVST/ledger/ROUND95_L8_PACKET_20261018.md @b47eab6d21 (sha256 3fa302a6...)). Swept: 12 dell1 rows never named, 9 dismissed and 3 graduated (all ARMED). REMEDIATION_v25 W170-S3 is advanced in place in the same commit. The watermark moves to now.

```json
[
  {
    "id": "AMGT_HARVST-D1-C-S70",
    "project": "AMGT_HARVST",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-18T11:51:23Z",
    "one_line": "ROUND 95 L8: MAY-CLOSE (6 orders, judgment 0, WORLD class). This seat's live gateway read: BP/_LN_Equity and NG/_LN_Equity, the raw spelling, now return the whole research record (dossier as_of 2026-10-18, continuation, ai_fill, research reports, roster), so REMEDIATION_v25 W170-S3 closes in place. 9 rows dismissed; the three ARMED rows W171-S3, S4 and S6 graduate with their disarm owned by 2.0.0_SA_COO~W1 and the decision the CTO's.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_HARVST-D1-W171-S1",
      "AMGT_HARVST-D1-W171-S2",
      "AMGT_HARVST-D1-W171-S5",
      "AMGT_HARVST-D1-W171-S7",
      "AMGT_HARVST-D1-W171-S8",
      "AMGT_HARVST-D1-W171-S9",
      "AMGT_HARVST-D1-S55",
      "AMGT_HARVST-D1-S56",
      "AMGT_HARVST-D1-S57"
    ],
    "spec_asserts": "REMEDIATION_v25 W170-S3: close when harvest_get_research for BP/_LN_Equity and for BP-SLASH-_LN_Equity each serve the dossier, the continuation and the research reports, and a census over every slash-keyed name reports 0 with a part absent under either form. The CTO's round-94 analysis items 1-3. Spine L8/L10.",
    "world_is": "READ BY THIS SEAT 2026-10-18 ~11:5xZ through opalgateway harvest_get_research. Packet hash verified. BP/_LN_Equity (raw): dossier_key as_of=2026-10-18.2d0238f7570cff0e.json, continuation 4ecc7216257f7d08.json (last_stated_position 'MAINTAIN 2.25% POSITION IN IDVZ', 6 thesis pillars), ai_fill, 7 research reports, the Bloomberg roster, parts_absent {}. NG/_LN_Equity (raw): dossier as_of=2026-10-18.1af6506669c49a8a.json, continuation cb76efa8bfd9173f.json, ai_fill (a cleared mgmt_bio), 1 research report, the roster, parts_absent {}. At round 94 this seat read BP raw with no dossier, continuation or ai_fill (ADJUDICATION_v88 C-S69). The issuer's replay over every slash key (2 keys, 4 spellings): REPLAY-WHOLE whole=4, re-run identical; the census domain is the two roots' security_key= tables, which the issuer's own correction narrows (section 4). So W170-S3's clock advances (REMEDIATED, closed). Path-component tools (peers, posture, scores, filings, derived/model_block) still read the caller's spelling, and the tables hold both spellings: that is W171-S4 and W171-S6, graduated. DISMISSED: W171-S1 and W171-S5 (ARMED census and module facts; disarmed by the release per D1-S56, and the raw spelling now reads whole on this seat's read). W171-S2 (BLOCKING, INERT; the sparse set omitted the gateway tests folder, which the issuer added). W171-S7 (the worker's correction of S5). W171-S8 (a standing red test outside this round's files). W171-S9 (the publication-links probe's double slash for a raw key; the probe is reached only now). D1-S55 and D1-S57 (S51 instances two and three; S51 stays OPEN under REMEDIATION_v23, owner MSTR). D1-S56 (the disarm record).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "opalgateway harvest_get_research BP/_LN_Equity and NG/_LN_Equity (this seat, 2026-10-18 ~11:5xZ)",
        "python .tools/round-close-check.py --project AMGT_HARVST --round 95 -> MAY-CLOSE (issuer)",
        "org/missions/D5/AMGT/AMGT_HARVST/ledger/ROUND95_L8_PACKET_20261018.md @b47eab6d21 (sha256 3fa302a6...)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Disarmed census rows, a resolved blocking row, corrections, S51 instances and a disarm record."
  },
  {
    "id": "AMGT_HARVST-D1-C-S71",
    "project": "AMGT_HARVST",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-18T11:51:23Z",
    "one_line": "Graduated to REMEDIATION_v26 (3, all ARMED, disarm owner 2.0.0_SA_COO~W1): W171-S3 (the gateway carries a copy of the slash-key rule, held to the module by one test arm), W171-S4 (peers, posture, scores and filings prefixes hold both spellings and the tools read the caller's), W171-S6 (coverage differs across spellings in the path-component templates).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_HARVST-D1-W171-S3",
      "AMGT_HARVST-D1-W171-S4",
      "AMGT_HARVST-D1-W171-S6"
    ],
    "spec_asserts": "Spine L10: every ARMED row is dispositioned before the slug; an item that bears on a later act graduates with an owner and a close condition.",
    "world_is": "The packet's section 6 names these as the CTO's decisions (open call dell1-20261018T093742Z-48ae for W171-S3). The issuer's replay: peers/v1 BP raw 7 objects, encoded 10; coverage BP path-component objects raw 20, encoded 41.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows AMGT_HARVST-D1-W171-S3, W171-S4, W171-S6",
        "org/missions/D5/AMGT/AMGT_HARVST/ledger/ROUND95_L8_PACKET_20261018.md @b47eab6d21 (sha256 3fa302a6...)"
      ]
    },
    "disposition": "GRADUATED",
    "notes": "Remediation rows W171-S3, W171-S4 and W171-S6 in REMEDIATION_v26."
  }
]
```

-- 3.0.0_SA_CVO
