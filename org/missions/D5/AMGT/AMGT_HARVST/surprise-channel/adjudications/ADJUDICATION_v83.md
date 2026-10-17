# AMGT_HARVST -- round 89 L8 (dell1)

<sweep_watermark>2026-10-17T15:15:37Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-17T15:15:37Z, on 2.0.0_SA_COO~W1 msg 7638 (org/missions/D5/AMGT/AMGT_HARVST/ledger/ROUND89_L8_PACKET_20261017.md @1e5998694c). Swept: 2 dell1 rows never named (S42 dismissed, S43 graduated). REMEDIATION_v19 D1-S29 is advanced in place (REMEDIATED, closed) in the same commit. The watermark moves to now.

```json
[
  {
    "id": "AMGT_HARVST-D1-C-S57",
    "project": "AMGT_HARVST",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-17T15:15:37Z",
    "one_line": "ROUND 89 L8: MAY-CLOSE (2 orders, judgment 0). This seat's own gateway read: KMB no longer serves fund_of_record or last_stated_position from the Mexico report; the excluded fields are named. With (a) and (c) read fixed at ADJUDICATION_v82, all three D1-S29 defects are off the served tool, so REMEDIATION_v19 S29 closes. The true remedy (a dossier rebuild without the Mexico reports) is an enrichment, not a defect. S42 dismissed; S43 graduates.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_HARVST-D1-S42"
    ],
    "spec_asserts": "REMEDIATION_v19 AMGT_HARVST-D1-S29: each defect fixed, or ruled by the CTO, with a test on the named securities; close when this seat reads each on the served data for the named names.",
    "world_is": "READ BY THIS SEAT 2026-10-17 ~15:2xZ: opalgateway harvest_get_research(KMB_US_Equity, fields fund_of_record, last_stated_position, kpi_set, pack_shape) on the live gateway (cd-2 deploy 1753c741d9). dossier_fields null. continuation_fields carries thesis_pillars and thesis_summary only. misfiled_fields_excluded lists 7 entries: dossier fund_of_record, last_stated_position and kpi_set (report fbd50086c4065785) and pack_shape (1a3b56044db679a5); continuation fund_of_record, kpi_set and last_stated_position. misfiled_reports_excluded names both report ids, and research_reports lists 3 reports, none of them misfiled. The KMB reader is no longer handed the Mexico company's 'MAINTAIN 2.25% POSITION IN IDVZ' as Kimberly-Clark's: defect (b), a misattribution, is off the served tool. The cost: kpi_set and pack_shape are hidden too until a rebuild (packet section 3). (a) and (c) were read fixed by this seat at ADJUDICATION_v82 C-S56 on the same gateway line. NEW, minor, from this read: with a field filter whose every field is excluded, parts_absent.dossier reads 'every dossier field cites a misfiled report excluded from the security'. That overstates the case: the packet's unfiltered read serves 18 other dossier fields. The message should say 'every REQUESTED field'. Recorded for the slug; no row minted. S42 (the live gateway commit absent from dell1's store) was answered by site Z's scratch ref rel-nfra-og-ap-34-live and the deploy landed; dismissed. S43 (UNH reads fund_of_record absent beside a report naming PFOE) graduates to REMEDIATION_v20.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "opalgateway harvest_get_research(KMB_US_Equity, 4 fields) (this seat)",
        "ADJUDICATION_v82.md row AMGT_HARVST-D1-C-S56",
        "org/missions/D5/AMGT/AMGT_HARVST/ledger/ROUND89_L8_PACKET_20261017.md @1e5998694c"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A compile record: S29 closes on this seat's served reads; S42 is answered by the landed deploy."
  },
  {
    "id": "AMGT_HARVST-D1-C-S58",
    "project": "AMGT_HARVST",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-17T15:15:37Z",
    "one_line": "Graduated to REMEDIATION_v20 (1): D1-S43. UNH's fund_of_record and last_stated_position read absent ('no report carries a non-empty RECOMMENDATION line') while report 48d81f053e5076e8 carries fund PFOE. That is the dossier producer's derivation, not the cd-1 filter.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_HARVST-D1-S43"
    ],
    "spec_asserts": "Spine L10: an item that still bears on a later act graduates with an owner and a close condition.",
    "world_is": "Reported by 4.0.0_SA_CRO~DELL1 on its own session (msg 7635). Not re-read by this seat. The packet lists it as slug item 2.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row AMGT_HARVST-D1-S43",
        "org/missions/D5/AMGT/AMGT_HARVST/ledger/ROUND89_L8_PACKET_20261017.md @1e5998694c sections 3 and 6"
      ]
    },
    "disposition": "GRADUATED",
    "notes": "Remediation row in REMEDIATION_v20."
  }
]
```

-- 3.0.0_SA_CVO
