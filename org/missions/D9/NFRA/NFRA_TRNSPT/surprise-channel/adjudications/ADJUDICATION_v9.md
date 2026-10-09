# NFRA_TRNSPT -- rounds 12-14 L8/L9 adjudication (FWD-10 commentary thread; securities exception review)

<sweep_watermark>2026-10-09T02:26Z</sweep_watermark>

Author: 3.0.0_SA_CVO (seated on dell2; tree on box/dell2), 2026-10-09 ~02:3xZ. L8 inputs: R12/R13/R14_CLOSE.md (msg 2189). All orders
complete, 0 judgment criteria, each round MAY-CLOSE. 3 rows dismissed below; D2-S7 and D2-W2-S3 (both BLOCKING) graduate OPEN in
`remediations/REMEDIATION_v6.md`, committed when TO-TR-j15 (round 15, same lane) is terminal: the gate holds new remediation rows until then. Securities exception v1 (Apple): APPROVED (`org/tier1_exec/3.0.0_SA_CVO/deliverables/NFRA_TRNSPT_SECURITIES_EXCEPTION_REVIEW_APPLE_20261009.md`). ARMED: 0.

**For the analysis:**
1. **The vendor authority is cited wrongly in the packet, and the real one has a limit.** Round 13's real Kimi call stands on
   Andrew's 10-07 'Dell Boxes have vendor egress as needed'. A Lambda calling Kimi from AWS is outside that word, so CALL 1 stays his.
2. **Real reports would dead-letter at H6.** D2-S7: household is required by the ticket contract and absent from the composition.
   This is the next blocker on the thread.

```json
[
  {
    "id": "NFRA_TRNSPT-C-S14",
    "project": "NFRA_TRNSPT",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T02:26:24Z",
    "one_line": "Rounds 12-14 rows dismissed: D2-W1-S5 (the composition's missing fields, answered by ~P2: account_type, themes and household absent; carried by D2-S7 and D2-W2-S3), D2-S6 (the H4 -> H6 seam: generated_at, fixed at bf2332f487; round 13's trace reaches H6 done), D2-W3-S3 (two stale allowlist assertions, fixed under amendment 1 @2a2915b702).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "NFRA_TRNSPT-D2-W1-S5",
      "NFRA_TRNSPT-D2-S6",
      "NFRA_TRNSPT-D2-W3-S3"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "All rounds 12-14 merges (98ca40fd4c, 6c4581b47c, 34ec06266d, bf2332f487, d153aeaba0, 1587d53a4c, 113047fc82, 2a2915b702) are ancestors of box/dell2 HEAD; round-close 12/13/14 MAY-CLOSE (this seat's reads). Round 13's ONE real Kimi K3 call (synthetic input, no prompt or draft text stored) is authorized by Andrew's 2026-10-07 item 4 ('The Dell Boxes have vendor egress as needed', org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261007_183xZ_TWELVE_ITEMS_ANSWERED_INSTALLER_PUSH_VENDOR_EGRESS_STORE_OUTLOOK_LAW_LINE_D2_HOLD_LIFTED.md), not by the 2026-09-30 word the packet cites (that word is a design direction). The commentary Lambda runs in AWS, not on a Dell box, so its live calls still need Andrew's standing word (the packet's CALL 1).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows NFRA_TRNSPT-D2-W1-S5, D2-S6, D2-W3-S3",
        "org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/2.0.0_SA_COO~T2/R12_CLOSE.md",
        "org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/2.0.0_SA_COO~T2/R13_CLOSE.md",
        "org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/2.0.0_SA_COO~T2/R14_CLOSE.md",
        "org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261007_183xZ_TWELVE_ITEMS_ANSWERED_INSTALLER_PUSH_VENDOR_EGRESS_STORE_OUTLOOK_LAW_LINE_D2_HOLD_LIFTED.md"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Answered, fixed at source, or fixed under amendment inside the rounds."
  }
]
```
