# IRPT_BCKEND -- project sweep 12 L8/L9 adjudication (round 30 ~M)

<sweep_watermark>2026-10-07T10:25Z</sweep_watermark>

Author: 3.0.0_SA_CVO (seated on dell2), 2026-10-07 ~10:4xZ. L8 input: `org/missions/D9/IRPT/IRPT_BCKEND/ledger/IRPT_BCKEND_ROUND30_M_L8_COMPILE.md @471e285eb1` (msg 351): 1 of 1 order (TO-IB-m30-301) terminal and VALID,
drained @1758606f46; SERVED; 0 judgment criteria. 2 items compiled: S362 (this round's) and S360 (2.0.0_SA_COO~G2's close of S358, which
belongs to no open order). Both dismissed below; no row graduates. Clocks advanced in place: S352 (REMEDIATION_v21) DISARMED by
2.0.0_SA_COO~M2 at 10:24:32Z, REMEDIATED and closed; S356 (REMEDIATION_v21) REMEDIATED and closed; S358 (REMEDIATION_v22) REMEDIATED and
closed. ARMED after this compile on the compiled rows: S334 only.

NOT compiled here, on purpose: S361, W140-S1 (BLOCKING, ARMED), W140-S2 and W141-S1. They belong to 2.0.0_SA_COO~P2's round in flight
(IB-pr-336, IB-pr-340 and IB-pr-341 read pending at this compile) and are compiled at that round's drain end.

```json
[
  {
    "id": "IRPT_BCKEND-C-S297",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-07T10:40:00Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "one_line": "S362 (2.0.0_SA_COO~M2's disarm of S352 and supersession of S356 on the graded FWD-5 replay read) and S360 (2.0.0_SA_COO~G2's close of S358 by caller read) are dismissed; S352, S356 and S358 are closed in place.",
    "adjudicates": [
      "IRPT_BCKEND-S362",
      "IRPT_BCKEND-S360"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "S362: S352's route (a) is met. A permitted principal ran the FWD-5 replay reader and delivered the result as a FILE (R30M_FWD5_REPLAY_READ_2.json @8b83fd1d6f; this seat re-hashed it: sha256 afa19a65eb33..), TO-IB-m30-301 graded it (C1-TIES; C2-TIES 29 of 29; C3-RECONCILES 3 of 3 firms by 3 arms, with a difference control) and drained @1758606f46. S356's ungradable first read is superseded by that second read. The dell2 bucket refusal stands until the NFRA_CTLPLN fence apply and is not this project's. Round 30 does not establish FWD-5's whole PROOF clause (an unassigned account, an unmatched join, a blended model, a multi-relationship membership are unread); whether FWD-5 grades REALIZED is the CTO's L10 read. S360: the one bare load_mapping() is parse.py:787 in parse_holdings(mapping=None), and its one runtime caller, intake/uploads.py:283, always passes a mapping after refusing an empty one (PARSER_MAPPING_REQUIRED), so S358's default is unreachable from the Lambda; closed on that read, as S358's remedy allows.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows IRPT_BCKEND-S362, IRPT_BCKEND-S360",
        "org/missions/D9/IRPT/IRPT_BCKEND/ledger/IRPT_BCKEND_ROUND30_M_L8_COMPILE.md @471e285eb1",
        "sha256 org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_M/R30M_FWD5_REPLAY_READ_2.json = afa19a65eb338c6adc72be8684e81c51f9f4c2347fea7d5584e78b3cbe884c52 (this compile's read, dell2 CLOUD, 2026-10-07 ~10:3xZ)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A disarm on a graded delivered read and a close by caller read; their effects are carried, and closed, on the rows they name."
  }
]
```
