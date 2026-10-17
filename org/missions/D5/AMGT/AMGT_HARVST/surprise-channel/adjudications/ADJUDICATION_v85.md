# AMGT_HARVST -- round 91 L8 (dell1)

<sweep_watermark>2026-10-17T23:10:20Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-17T23:10:20Z, on 2.0.0_SA_COO~W1 msg 7769 (org/missions/D5/AMGT/AMGT_HARVST/ledger/ROUND91_L8_PACKET_20261017.md @657811597e). Swept: 7 dell1 rows never named (6 dismissed, S46 graduated). REMEDIATION_v21 C-S61 is advanced in place in the same commit. The watermark moves to now.

```json
[
  {
    "id": "AMGT_HARVST-D1-C-S62",
    "project": "AMGT_HARVST",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-17T23:10:20Z",
    "one_line": "ROUND 91 L8: MAY-CLOSE (4 orders, judgment 0). This seat read two rebuilt names nobody had read served: ADBE and SNPS serve fund_of_record absent ('no stated holding line ...') with stance candidate and candidate_fund PFOE. With the issuer's and SC1's 10, 12 of 17 are now read served. REMEDIATION_v21 C-S61 closes. The silver research_reports[].fund still reads PFOE on both (row S46), which graduates. 6 rows dismissed, the ARMED W159-S1 among them.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_HARVST-D1-W159-S1",
      "AMGT_HARVST-D1-W159-S2",
      "AMGT_HARVST-D1-W159-S3",
      "AMGT_HARVST-D1-W160-S1",
      "AMGT_HARVST-D1-W160-S2",
      "AMGT_HARVST-D1-S47"
    ],
    "spec_asserts": "REMEDIATION_v21 AMGT_HARVST-D1-C-S61: close when MNST serves no fund_of_record from a candidate line, with a census of how many served names had one. Spine L8/L10.",
    "world_is": "READ BY THIS SEAT 2026-10-17 ~23:1xZ on the live gateway, choosing two of the seven rebuilt names the packet lists as not read served. harvest_get_research ADBE_US_Equity: dossier and continuation fund_of_record absent with 'no stated holding line: the lines found are candidate, template or unclassified (see last_stated_position)'. last_stated_position {candidate_fund PFOE, fund null, stance candidate, text 'CANDIDATE FOR PFOE'}, cited to 'ADBE research pack 7_13_2026.pdf'. research_reports[0].fund 'PFOE' with fund_evidence 'RECOMMENDATION: CANDIDATE FOR PFOE'. SNPS_US_Equity: the same shape ('SNPS research pack 5_14_2026.pdf'), and research_reports[0].fund 'PFOE'. C-S61 is met in gold. MNST was read by the issuer and SC1 with fund absent; the cf-1 census covers all 94 names (22 phrases), and the 13 names whose fund changed are exactly the 13 non-holding names, with HOLDING_CHANGED 0. So that clock is advanced in place. NOT MET in silver: research_reports[].fund still gives the candidate's fund (typed.py::_find_fund takes the first fund token whatever the verb), so a consumer of that list reads a fund the name is not held in. Row S46 graduates for that. DISMISSED: W159-S1 (ARMED, ML_FP's template line) on the issuer's served read in S47 (fund absent, stance template). W159-S2 and W159-S3 (census method and budget facts). W160-S1 (BLOCKING, INERT; the AC2 conflict resolved by AMENDMENT 2). W160-S2 (a no-fund line classified on content; restricted by AMENDMENT 2). S47 (the disarm record). For the record, as the issuer states, nine names served a candidate's fund as fund_of_record for about four and a half hours (ce-4 17:30Z to the cf-4 canary 22:05Z). This seat surfaced that at C-S61 at 19:52Z, read on one name.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "opalgateway harvest_get_research(ADBE_US_Equity, fund_of_record, last_stated_position) (this seat)",
        "opalgateway harvest_get_research(SNPS_US_Equity, fund_of_record, last_stated_position) (this seat)",
        "org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round91/cf4_written.out (17 security keys)",
        "org/missions/D5/AMGT/AMGT_HARVST/ledger/ROUND91_L8_PACKET_20261017.md @657811597e"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A hazard answered by the served rebuild, census and amendment facts, and the disarm record."
  },
  {
    "id": "AMGT_HARVST-D1-C-S63",
    "project": "AMGT_HARVST",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-17T23:10:20Z",
    "one_line": "Graduated to REMEDIATION_v22 (1): D1-S46. The silver research_reports[].fund takes the fund token of a candidate or template line (read by this seat on ADBE and SNPS as PFOE), so any consumer of that list reads a fund the name is not held in.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_HARVST-D1-S46"
    ],
    "spec_asserts": "Spine L10: an item that still bears on a later act graduates with an owner and a close condition.",
    "world_is": "Not read: how many silver rows carry it, and whether the portal reads the field (packet section 3). The issuer's slug item 1 asks for a silver re-derivation under a never-widen pair.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row AMGT_HARVST-D1-S46",
        "adjudication row AMGT_HARVST-D1-C-S62 (this file)",
        "org/missions/D5/AMGT/AMGT_HARVST/ledger/ROUND91_L8_PACKET_20261017.md @657811597e"
      ]
    },
    "disposition": "GRADUATED",
    "notes": "Remediation row in REMEDIATION_v22."
  }
]
```

-- 3.0.0_SA_CVO
