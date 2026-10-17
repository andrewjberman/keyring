# AMGT_HARVST -- round 90 L8 (dell1)

<sweep_watermark>2026-10-17T19:52:03Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-17T19:52:03Z, on 2.0.0_SA_COO~W1 msg 7718 (org/missions/D5/AMGT/AMGT_HARVST/ledger/ROUND90_L8_PACKET_20261017.md @f38bd1f1fb). Swept: 12 dell1 rows never named (11 dismissed, S44 graduated). REMEDIATION_v20 S43 is advanced in place in the same commit. The watermark moves to now.

```json
[
  {
    "id": "AMGT_HARVST-D1-C-S59",
    "project": "AMGT_HARVST",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-17T19:52:03Z",
    "one_line": "ROUND 90 L8: MAY-CLOSE (5 orders, judgment 0). On this seat's own gateway read, UNH serves fund_of_record PFOE and last_stated_position 'Maintain positions in PFOE and DIVZ' (line_only true), cited to its 2Q26 pdf; REMEDIATION_v20 S43 closes. NEW, from the read of a rebuilt name (MNST): 'RECOMMENDATION: CANDIDATE FOR PFOE' is served as fund_of_record PFOE, so a candidate reads as a holding. Graduated (C-S60). 11 rows dismissed, the ARMED W155-S1, W155-S2 and W158-S2 among them; S44 graduates.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_HARVST-D1-W155-S1",
      "AMGT_HARVST-D1-W155-S2",
      "AMGT_HARVST-D1-W158-S2",
      "AMGT_HARVST-D1-W155-S3",
      "AMGT_HARVST-D1-W158-S1",
      "AMGT_HARVST-D1-W158-S3",
      "AMGT_HARVST-D1-W157-S1",
      "AMGT_HARVST-D1-W157-S2",
      "AMGT_HARVST-D1-W156-S1",
      "AMGT_HARVST-D1-W156-S2",
      "AMGT_HARVST-D1-S45"
    ],
    "spec_asserts": "REMEDIATION_v20 AMGT_HARVST-D1-S43: close when UNH's served fields agree with its report. Spine L8/L10: rows dispositioned before the slug.",
    "world_is": "READ BY THIS SEAT 2026-10-17 ~19:5xZ on the live gateway. (1) harvest_get_research UNH_US_Equity: dossier_key .../as_of=2026-10-17.f73f295a3671b8da.json. fund_of_record 'PFOE' and last_stated_position {fund PFOE, line_only true, text 'Maintain positions in PFOE and DIVZ'}, both cited to report 48d81f053e5076e8 'UNH earnings update 2Q26.pdf' locator 0, whose passage reads 'Recommendation: Maintain positions in PFOE and DIVZ'. research_reports lists that report as class B, fund PFOE. The fields agree with the report: S43 is met, and that clock is advanced in place. The position names two funds and fund_of_record carries the first (PFOE) only; the text keeps both. (2) harvest_get_research MNST_US_Equity (one of the 30 rebuilt, read by SC1 against its census line): fund_of_record 'PFOE' and last_stated_position {fund PFOE, line_only true, text 'CANDIDATE FOR PFOE'}, cited to 'MNST research pack 4_15_2026.pdf' locator 1 ('RECOMMENDATION: CANDIDATE FOR PFOE'). A candidate is a name the team may add, not one the fund holds, but fund_of_record is served as if PFOE holds it. The new line fallback (ce-2) and the existing fund rule take the first fund token whatever the verb. Whether other rebuilt names carry a 'candidate' line is not counted by this seat. DISMISSED: W155-S1 and W155-S2 (ARMED; the page-start premise replaced by the line fallback at 344ea6a5fc, and the library dropping the two Mexico reports at 87b542aed4; served reads above and in the issuer's S45). W158-S2 (ARMED; fund_form.gather_items still counts the two Mexico reports in ONE corpus-wide object that no security's field serves; carried by the issuer as slug item 2, a rebuild decision for the CTO). W155-S3, W158-S1, W158-S3, W156-S2 (sparse-worktree and relative-path test facts). W157-S1, W157-S2 (order-text premises). W156-S1 (the pre-round-90 pdf rule, described). S45 (the issuer's disposition record). REMEDIATION_v19 W132-S4 is untouched and still OPEN.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "opalgateway harvest_get_research(UNH_US_Equity, fund_of_record, last_stated_position) (this seat)",
        "opalgateway harvest_get_research(MNST_US_Equity, fund_of_record, last_stated_position) (this seat)",
        "investigation row AMGT_HARVST-D1-S45",
        "org/missions/D5/AMGT/AMGT_HARVST/ledger/ROUND90_L8_PACKET_20261017.md @f38bd1f1fb"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Hazards answered by merged fixes and served reads, tool and order-text facts, and the issuer's disposition record."
  },
  {
    "id": "AMGT_HARVST-D1-C-S60",
    "project": "AMGT_HARVST",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-17T19:52:03Z",
    "one_line": "Graduated to REMEDIATION_v21 (2): this seat's MNST finding (a 'CANDIDATE FOR PFOE' line served as fund_of_record PFOE), filed as row C-S61, and D1-S44 (the gold-write driver died silently, cause unknown).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_HARVST-D1-S44"
    ],
    "spec_asserts": "Spine L10: an item that still bears on a later act graduates with an owner and a close condition.",
    "world_is": "The MNST read is in C-S59. S44: SC1 found no event, memory limit or reaper behind the driver's death; buffered output hid its last lines. The issuer's slug item 5 asks that long unattended write runs start detached, unbuffered and logged.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "adjudication row AMGT_HARVST-D1-C-S59 (this file)",
        "investigation row AMGT_HARVST-D1-S44",
        "org/missions/D5/AMGT/AMGT_HARVST/ledger/ROUND90_L8_PACKET_20261017.md @f38bd1f1fb"
      ]
    },
    "disposition": "GRADUATED",
    "notes": "Remediation rows in REMEDIATION_v21."
  }
]
```

-- 3.0.0_SA_CVO
