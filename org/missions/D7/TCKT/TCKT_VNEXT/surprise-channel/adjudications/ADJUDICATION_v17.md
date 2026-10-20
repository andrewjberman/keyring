# TCKT_VNEXT: CVO adjudication, round 20 close -- the ten undispositioned investigation rows

<sweep_watermark>2026-10-20T06:05Z</sweep_watermark>

Author: 3.0.0_SA_CVO~DELL2, 2026-10-20.

L9 disposition by `3.0.0_SA_CVO~DELL2` (dell2), 2026-10-20T06:05Z. The row gate (spine L10 precondition) reads 10 of 120 BLOCKING,
ARMED or ungraded investigation items of TCKT_VNEXT whose latest carrier is UNDER_INVESTIGATION. This file disposes of all ten.

## The six worker stops on sparse worktrees: DISMISSED_WITH_REASON (overtaken; each cell later built and graded)

Each is a worker that stopped correctly because its worktree's sparse-checkout cone omitted a path it needed. In order: `infra/aws` for
W45-S1, W46-S1, W47-S1 and W48-S1; the D9 fixture `I7_SAMPLE.json` for W47-S2 and W53-S1. Each cell was later built in a full tree and
graded by this seat on the source and the suite at the built commit:

| row | cell | graded |
|---|---|---|
| D2-W45-S1 | TO-R19-L1 | v8: R19L1-AC3J MET |
| D2-W46-S1 | TO-R19-L2 | v8: R19L2-AC3J MET |
| D2-W47-S1 | TO-R19-L3 | v8: R19L3-AC3J MET |
| D2-W47-S2 | the R19-L3 drain check | v8: suite 466 passed at de2fdb4a4f |
| D2-W48-S1 | TO-R19-TR | v8: R19TR-AC3J MET |
| D2-W53-S1 | TO-R20-LM7 | v14: R20LM7-AC3J MET; the suite passes 476 and 471 in full trees |

**The class stays visible, as a note for the issuer, not a defect of any cell.** A worker worktree cut with a sparse cone that omits
`infra/aws` or a fixture the harness reads at import stops the cell. W47-S2 and W53-S1 are the same fixture, eleven days apart. The cut
should include the harness's import-time fixtures.

## D2-S55: DISMISSED_WITH_REASON (remediated)

`r19_mig_check.py` counted the one string-valued service row as locked out, so it could never pass while the pair held. The issuer fixed
the check (357bbd02af7, "the check now counts only the rows the pair selects"). The migration's 19 markers stand, and R19 released REL-OK
(v8).

## D2-S56: DISMISSED_WITH_REASON (overtaken)

Step 3 could not click Trade Request on DEV while the hide stood. Andrew lifted the Trade hold (CTO msg 10728), and the PROD Trade journey
`TO-R20-PROD3` was then run and cancelled by the CTO's ruling msg 11040 (its own rows D2-S62 to S64). Nothing is left for this row.

## D2-S46 and D2-S53: GRADUATED to remediation, still ARMED, owner `1.0.0_SA_CTO~DELL2`

Both are live standing hazards with a named owner, not defects of a round's cell:
- **S46:** a direct `lambda:InvokeFunction` goes around the portal authorizer, and the handler trusts the event's caller context. The CTO's
  IAM read of who holds that grant is in progress.
- **S53:** an active users row on an outside domain carries the internal firm id. ADJUDICATION_v16 found that the data-refresh gate also
  trusts that firm id. Whether the row should be internal is Andrew's.

They graduate so the round can close with them tracked on the remediation plane (REMEDIATION_v2), OPEN and ARMED, rather than as open
items.

```json
[
  {
    "id": "TCKT_VNEXT-D2-C-S12",
    "project": "TCKT_VNEXT",
    "fabric": "dell2",
    "surfaced_by": "3.0.0_SA_CVO~DELL2",
    "surfaced_at": "2026-10-20T06:05Z",
    "one_line": "Eight undispositioned TCKT_VNEXT items closed: six sparse-worktree worker stops (each cell later built and graded), D2-S55 (check fixed 357bbd02af7) and D2-S56 (Trade hold lifted; PROD3 cancelled).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "TCKT_VNEXT-D2-W45-S1",
      "TCKT_VNEXT-D2-W46-S1",
      "TCKT_VNEXT-D2-W47-S1",
      "TCKT_VNEXT-D2-W47-S2",
      "TCKT_VNEXT-D2-W48-S1",
      "TCKT_VNEXT-D2-W53-S1",
      "TCKT_VNEXT-D2-S55",
      "TCKT_VNEXT-D2-S56"
    ],
    "spec_asserts": "Spine L10 precondition: the slug waits until every BLOCKING, ARMED or ungraded investigation item is CVO-dispositioned.",
    "world_is": "R19-L1/L2/L3/TR graded MET in ADJUDICATION_v8 (suite 466 passed at de2fdb4a4f); R20-LM7 graded MET in v14; r19_mig_check.py fixed at 357bbd02af7 and R19 released REL-OK; the Trade hold lifted (CTO msg 10728) and TO-R20-PROD3 cancelled (CTO msg 11040).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ADJUDICATION_v8.md, ADJUDICATION_v14.md",
        "commit 357bbd02af7 (r19_mig_check.py fix)",
        "CTO msgs 10728, 11040"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Six worker stops overtaken: each cell was built in a full tree and graded MET (v8, v14); note for the issuer that the worktree cone must carry import-time fixtures (W47-S2 and W53-S1 are one class). S55 remediated by the check fix 357bbd02af7. S56 overtaken by the lifted Trade hold and the CTO's cancellation of TO-R20-PROD3."
  },
  {
    "id": "TCKT_VNEXT-D2-C-S13",
    "project": "TCKT_VNEXT",
    "fabric": "dell2",
    "surfaced_by": "3.0.0_SA_CVO~DELL2",
    "surfaced_at": "2026-10-20T06:05Z",
    "one_line": "D2-S46 (direct invoke bypasses the portal authorizer) and D2-S53 (an outside-domain row carries the internal firm id) graduate to remediation, OPEN and ARMED, owner 1.0.0_SA_CTO~DELL2.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO~DELL2",
    "adjudicates": [
      "TCKT_VNEXT-D2-S46",
      "TCKT_VNEXT-D2-S53"
    ],
    "spec_asserts": "A standing hazard with a named owner is tracked on the remediation plane until its owner disarms it; it does not hold a round open as an undispositioned item.",
    "world_is": "S46: the ticket handler trusts the event's caller context on a direct invoke (the CTO's IAM read in progress). S53: an active outside-domain users row carries the internal firm id; the data-refresh gate also trusts it (ADJUDICATION_v16). Neither is moved by any round-20 release.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows TCKT_VNEXT-D2-S46, TCKT_VNEXT-D2-S53",
        "ADJUDICATION_v16.md (is_opal_internal trusts firmId)",
        "org/missions/D7/TCKT/TCKT_VNEXT/surprise-channel/remediations/REMEDIATION_v2.md"
      ]
    },
    "disposition": "GRADUATED"
  }
]
```

-- `3.0.0_SA_CVO~DELL2`
