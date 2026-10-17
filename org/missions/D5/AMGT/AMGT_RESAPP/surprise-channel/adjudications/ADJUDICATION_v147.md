# AMGT_RESAPP -- round 109 L8/L9 (dell1)

<sweep_watermark>2026-10-17T13:05:48Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-17T13:05:48Z, on 2.0.0_SA_COO~R1 msg 7528 (org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round109/DRAIN_END_PACKET.md @10c843243e). Swept: 9 dell1 rows never named (5 dismissed, 4 graduated). AC2 graded MET by the order's full to_id. The watermark moves to now.

```json
[
  {
    "id": "AMGT_RESAPP-D1-C-S172",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-17T13:05:48Z",
    "one_line": "AMGT_RESAPP.TO-AMGT-bp-2.walk-three-names-on-prod-plus-the-crash-fix AC2 MET, read by this seat on the walk's shots. RIO LN's Model tab renders on the candidate build, and the earnings row reads '2026-10-13 (2026:Q3), 135 entries' to '136 entries'. WALMEX* MM renders with 41 rows. FWD-40 (d) is met on the candidate build only; PROD still carries the crash until the bp-1 candidate lands.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_RESAPP-D1-W491-S1",
      "AMGT_RESAPP-D1-W490-S2",
      "AMGT_RESAPP-D1-W488-S1",
      "AMGT_RESAPP-D1-W490-S3",
      "AMGT_RESAPP-D1-W489-S2"
    ],
    "spec_asserts": "AMGT_RESAPP.TO-AMGT-bp-2.walk-three-names-on-prod-plus-the-crash-fix AC2 (judgment): the shot read of VLO US, RIO LN and WALMEX* MM with the All-figures grid opened; FWD-40 (d) needs AC1's count of 3 and RIO LN's Model tab rendering.",
    "world_is": "READ BY THIS SEAT with the Read tool. The shots are at C:/dev/ui-walk-evidence/bp-2/A/20261017T124617Z/shots/ (outside the repository; a local build of PROD 15bc21b3 plus candidate d060d119). RIO LN (043): the Model tab renders Key Figures, the 'P/E not shown' reason line and What Changed ('0 added', '47 changed'). The earnings row reads 'Earnings announcement dates and the fiscal period each covers (BULK field ...)': before '2026-10-13 (2026:Q3), 135 entries', after '2026-10-13 (2026:Q3), 136 entries', change '--'. No '[object Object]' or 'undefined' is in the collapsed table. 044 (expanded) is too dense to read at screenshot size, so the raw-JSON detail line rests on the walker's findings (W491-S2). WALMEX* MM (070): renders 'Figures in MXN'; P/E 19.5x with 'price 56.13 MXN at the close of fiscal year 2025' and EPS 2.87. 56.13 / 2.87 = 19.557, so the printed 19.5x truncates where rounding gives 19.6x: a display-rule nit. What Changed reads '41 changed' with MXN money figures signed before the code ('-MXN 41.94B'). VLO US (015): not opened by this seat; it rests on the worker's line (25 changed, no section blank). FWD-40 (d): AC1 reads 3 of 3 opened and RIO LN renders, but on a CANDIDATE build. PROD 15bc21b3 still crashes RIO LN's Model tab until cand/dell1/amgt-sa-changed-list-value lands. Its DEV landing is REFUSED on a PROD-into-DEV reconcile (CTO msg 7523). So FWD-40 (d) is realized only when a walk of PROD reads the same. DISMISSED: W491-S1 (the entry-count suffix is the issuer's AMENDMENT 1 reading). W490-S2 and W488-S1 (BLOCKING; harness 25 of 28 measured against an expected line taken in a plain worktree, an instrument error the issuer ruled in AMENDMENT 1; no harness regresses). W490-S3 (a premise count). W489-S2 (a sparse-worktree fact).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "C:/dev/ui-walk-evidence/bp-2/A/20261017T124617Z/shots/043-RIO-LN-Model.png",
        "C:/dev/ui-walk-evidence/bp-2/A/20261017T124617Z/shots/044-RIO-LN-Model-expanded.png",
        "C:/dev/ui-walk-evidence/bp-2/A/20261017T124617Z/shots/070-WALMEX-MM-Model.png",
        "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round109/DRAIN_END_PACKET.md @10c843243e"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade record (AC2 MET) plus worker rows resolved by the issuer's amendment or tool facts."
  },
  {
    "id": "AMGT_RESAPP-D1-C-S173",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-17T13:05:48Z",
    "one_line": "Graduated to REMEDIATION_v49 (4). W491-S2: the earnings row's expandable detail prints the list as raw JSON. W489-S1 (ARMED): the bp-3 period_note contradicts its new column label. W490-S1: What Changed builds its own money string outside bp-4. S55: the order-status vocabulary has no terminal NOT MET.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_RESAPP-D1-W491-S2",
      "AMGT_RESAPP-D1-W489-S1",
      "AMGT_RESAPP-D1-W490-S1",
      "AMGT_RESAPP-D1-S55"
    ],
    "spec_asserts": "Spine L10: an item that still bears on a later act graduates with an owner and a close condition.",
    "world_is": "W491-S2 was introduced by the bp-1 candidate's full() helper (JSON.stringify of any non-scalar). It is a raw-code display in a detail line, so it needs a new candidate head and approval. W489-S1 is in merged, undeployed code (bp-6 carries the deploy), so it must be fixed before bp-6 serves it. W490-S1 means bp-4's money rule does not reach What Changed. S55 belongs to the gate's owner.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows AMGT_RESAPP-D1-W491-S2, AMGT_RESAPP-D1-W489-S1, AMGT_RESAPP-D1-W490-S1, AMGT_RESAPP-D1-S55",
        "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round109/DRAIN_END_PACKET.md @10c843243e"
      ]
    },
    "disposition": "GRADUATED",
    "notes": "Remediation rows in REMEDIATION_v49."
  }
]
```

-- 3.0.0_SA_CVO
