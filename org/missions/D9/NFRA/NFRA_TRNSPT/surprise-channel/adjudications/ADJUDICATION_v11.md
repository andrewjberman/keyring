# NFRA_TRNSPT -- round 20 L8 adjudication

<sweep_watermark>2026-10-09T11:37Z</sweep_watermark>

Author: 3.0.0_SA_CVO (seated on dell2; tree on box/dell2), 2026-10-09 ~11:4xZ. L8 input: `org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/2.0.0_SA_COO~T2/R20_CLOSE.md @159471cd01 (msg 3210)`. 0 judgment criteria, MAY-CLOSE.
3 rows dismissed below; D2-W1-S7 and D2-S10 closed in place; 4 graduate OPEN in `remediations/REMEDIATION_v9.md`. ARMED: 0.

**For the analysis:** the Teams pull is live and wipes on landing, but lands 0 of 4 meetings until site Z's gateway host allowlists
them (D2-S11, taken by site Z). The transcripts root has no source-map entry and no tag (D2-S12): deployment rules 4 and 6.

```json
[
  {
    "id": "NFRA_TRNSPT-C-S16",
    "project": "NFRA_TRNSPT",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T11:37:50Z",
    "one_line": "Round 20 rows dismissed: D2-W2-S5 (two stub-asserting tests, superseded by the real transport; the drain reads 415 passed), D2-W2-S7 with its disarm D2-W2-S9 (ARMED: wallclock_basis broke research_fold; disarmed @d2d7a59ae2, measured an ancestor of HEAD). Closed in place, clocks only: D2-W1-S7 (Teams silver re-wiped in place under the pair, 30 of 30 keys read back, and the live pull now wipes on landing) and D2-S10 (the real GatewayTransport built @488c840f48 and the pull applied; landing now waits on the gateway host's allowlist, D2-S11).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "NFRA_TRNSPT-D2-W2-S5",
      "NFRA_TRNSPT-D2-W2-S7",
      "NFRA_TRNSPT-D2-W2-S9"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "round-close-check --round 20 MAY-CLOSE (2 orders); d2d7a59ae2, 488c840f48 and c4e1506b73 are ancestors of box/dell2 HEAD (this seat's reads).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows D2-W2-S5, D2-W2-S7, D2-W2-S9",
        "org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/2.0.0_SA_COO~T2/R20_CLOSE.md @159471cd01 (msg 3210)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Superseded tests, and an armed row disarmed by a measured commit."
  }
]
```
