# AMGT_RESAPP -- round 111 L8 (dell1)

<sweep_watermark>2026-10-17T18:55:45Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-17T18:55:45Z, on 2.0.0_SA_COO~R1 msg 7709 (org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round111/DRAIN_END_PACKET.md @c83b436940). Swept: 9 dell1 rows never named (6 dismissed, 3 graduated). REMEDIATION_v50 W492-S3 is advanced in place in the same commit. No judgment criterion. The watermark moves to now.

```json
[
  {
    "id": "AMGT_RESAPP-D1-C-S176",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-17T18:55:45Z",
    "one_line": "ROUND 111 L8: MAY-CLOSE (5 orders, judgment 0). This seat read the close walk's findings.json: 12 findings on PROD 932cea99, none raw-code and none format:money, so round 110's IS_EPS footer and Peers USD-beside-$ findings no longer fire. Portal PROD 932cea99 and DEV 0f6dc96b are read. W492-S3 closes; W491-S2 stays OPEN (the earnings row was not walked). 6 rows dismissed, 3 graduate.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_RESAPP-D1-W493-S1",
      "AMGT_RESAPP-D1-W493-S2",
      "AMGT_RESAPP-D1-W493-S3",
      "AMGT_RESAPP-D1-W494-S2",
      "AMGT_RESAPP-D1-W494-S3",
      "AMGT_RESAPP-D1-W494-S4"
    ],
    "spec_asserts": "Spine L8/L10: rows dispositioned before the slug. REMEDIATION_v50 W492-S3 closes when the check passes and a walk reads no raw-code finding on What Changed.",
    "world_is": "READ BY THIS SEAT 2026-10-17 ~18:5xZ. git -C portal ls-remote origin: PROD 932cea99e8, DEV 0f6dc96b0f. Both equal the packet's br-5 reads. C:/dev/ui-walk-evidence/r111-close/findings.json (outside the repository) holds 12 findings by check: timeline:no-event-element 3, unconnected-field 2, layout:clipped 2, walker:control-missing 1, layout:truncated 1, timeline:no-day-bar 1, occluded-popover 1, format:dates 1. There are 0 raw-code and 0 format:money, against round 110's 2 raw-code (the IS_EPS footer on RIO LN and ICT PM) and 1 format:money (ICT PM Peers). W492-S3's close condition is met on its own terms: br-1's harness graded the rendered <td> (6 of 6, re-run by the issuer, O1 to O3 red at the base), and the PROD walk reads no raw-code finding. Limit, as the issuer states: no live object-valued What Changed cell was in the walked states, so the harness fixture carries the visible-cell grade. That clock is advanced in place. W491-S2 stays OPEN: its close needs RIO LN's earnings row detail read on a walk, and the earnings row was in no walked pair (br-2 and the close walk). DISMISSED: W493-S1 to S3 and W494-S4 (worktree, sparse-cone and pre-commit tool facts). W494-S2 and W494-S3 (order-text examples the worker read correctly). NOT READ: the live site tied to 932cea99 by bytes (round 110's method not re-run; the CI run is the deploy evidence), and the footer's rendered sentence in a crop.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git -C portal ls-remote origin PROD DEV (this seat)",
        "C:/dev/ui-walk-evidence/r111-close/findings.json counted by check (this seat)",
        "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round111/PROD_CLOSE_WALK.md @55139659f4",
        "python .tools/round-close-check.py --project AMGT_RESAPP --round 111 -> MAY-CLOSE",
        "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round111/DRAIN_END_PACKET.md @c83b436940"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Tool and order-text facts; the compile reading is recorded."
  },
  {
    "id": "AMGT_RESAPP-D1-C-S177",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-17T18:55:45Z",
    "one_line": "Graduated to REMEDIATION_v51 (3), each carried to round 112. W494-S1: the producer of the stored model-block reasons that can reach the P/E footer was not read at source. W495-S1: a USD-priced peer's Price cell reads '148.07 currency not stated'. W495-S2: the header and the Peers table name the price currency by different rules when PX_LAST carries none.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_RESAPP-D1-W494-S1",
      "AMGT_RESAPP-D1-W495-S1",
      "AMGT_RESAPP-D1-W495-S2"
    ],
    "spec_asserts": "Spine L10: an item that still bears on a later act graduates with an owner and a close condition.",
    "world_is": "All three are named in the packet's sections 3 and 4 as the CTO's round-112 items (the br-3 census gap; br-4's currency rule).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows AMGT_RESAPP-D1-W494-S1, AMGT_RESAPP-D1-W495-S1, AMGT_RESAPP-D1-W495-S2",
        "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round111/DRAIN_END_PACKET.md @c83b436940"
      ]
    },
    "disposition": "GRADUATED",
    "notes": "Remediation rows in REMEDIATION_v51."
  }
]
```

-- 3.0.0_SA_CVO
