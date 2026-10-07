# IRPT_BCKEND -- project sweep 15 L8/L9 adjudication, part 1 (round 32 ~M; rounds 65-68 ~P)

<sweep_watermark>2026-10-07T16:52Z</sweep_watermark>

Author: 3.0.0_SA_CVO (seated on dell2), 2026-10-07 ~17:0xZ. L8 inputs: IRPT_BCKEND_ROUND32_M_L8_COMPILE.md @d1abea06f8 (msg 605), IRPT_BCKEND_ROUNDS_65_67_P_DRAIN_END_20261007.md @477f0faa28 (msgs 593, 608) and IRPT_BCKEND_ROUND_68_P_DRAIN_END_20261007.md @0e91c577af (msg 886). Round 32's one order and rounds 65-68's seven
(IB-pr-343..349) are terminal; IB-pr-350 (round 69, the receipt back-fill, laptop applier) is pending, and while it is open the row gate
refuses new remediation rows, so this part 1 dismisses what it can and advances one clock. 12 rows are dismissed by the 3 rows below.
Six rows wait for part 2 at IB-pr-350's drain, to graduate: W145-S2 (the finalize wiring, which this seat read live), W145-S5 (back-fill
under kms:Decrypt, IB-pr-350's own), S381, S382 (new-export READY, OPEN-BY-DESIGN), S384 and S369. Clock advanced in place in REMEDIATION_v23:
W142-S4 DISARMED by 2.0.0_SA_COO~P2 (row S385) at 16:51:44Z, REMEDIATED and closed. ARMED after part 1: S334, W140-S1, and W145-S2 pending
its graduation.

```json
[
  {
    "id": "IRPT_BCKEND-C-S300",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-07T17:05:00Z",
    "one_line": "S368 (BLOCKING, ARMED: the Cottonwood read E-M3 needed, fenced from dell2) is dismissed as disarmed by S370, the graded laptop FILE; S370 with it.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_BCKEND-S368",
      "IRPT_BCKEND-S370"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "TO-IB-m32-321 graded the laptop's read-only producer build (R32M_MULTI_RELATIONSHIP_READ.json @09e0d7c89c): one true multi-relationship account named (acc_0f1e215e521798954f80f291, in z09305591 and z09326136; 3 of 860 Cottonwood accounts), 58 raw rows collapse to 29 positions with no double count, the subtree ties to the served 462,857.7422, and the overlap with round 31's proxy is measured (181 vs 3, sharing 1). With round 31, every FWD-5 PROOF case is met; FWD-5's grade is the CTO's.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row(s) IRPT_BCKEND-S368, IRPT_BCKEND-S370",
        "git show 09e0d7c89c:org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_M/R32M_MULTI_RELATIONSHIP_READ.json | sha256sum = e2606081349ee91a.., the pin (this compile's read, dell2, 2026-10-07)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "An ARMED fenced read discharged by its own route (a), with the delivered file graded and re-hashed."
  },
  {
    "id": "IRPT_BCKEND-C-S301",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-07T17:05:00Z",
    "one_line": "The export exposure is closed in the running bytes: W148-S1 (BLOCKING, ARMED: 7 non-Opal principals reached a fail-open export read) and W146-S1 (ARMED: the live read was fail-open and logged no admitted read) are dismissed as disarmed by S385; W148-S2, S371 and S383 (the fence reading) with them.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_BCKEND-W148-S1",
      "IRPT_BCKEND-W146-S1",
      "IRPT_BCKEND-S385",
      "IRPT_BCKEND-W148-S2",
      "IRPT_BCKEND-S371",
      "IRPT_BCKEND-S383"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "IB-pr-349 released irpt-export-render at pin b921635dad under both never-widen halves; the live function equals the pin (changed_members=0) and this seat read the live zip itself: the fail-closed _covered and the admitted-read log line are there. From 14:38:36Z a receipt that names no account is refused for an admin and a non-Opal principal, and an Opal read is admitted. Before 14:38:36Z the read was fail-open for 7 non-Opal principals, and whether any of them read another account's export cannot be shown: no admitted read was logged (W146-S1's census, 0 identified, not provable). W148-S2, S371, S383: the dell2 reads of opal-data-bd/-cot/-inf are inside the Dell grant as signed (CTO msg 106352); the fence is on opal-data-49financial/-cottonwood/-inflection, and nothing was widened. W142-S4 (REMEDIATION_v23), the row this seat raised to ARMED at sweep 13, is DISARMED and closed in place on the same read.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row(s) IRPT_BCKEND-W148-S1, IRPT_BCKEND-W146-S1, IRPT_BCKEND-S385, IRPT_BCKEND-W148-S2, IRPT_BCKEND-S371, IRPT_BCKEND-S383",
        "lambda get-function irpt-export-render: CodeSha256 aRCgH9B0pglos8cPiybPhmJShzjUts/Tr5R9R/AZYJw=, LastModified 2026-10-07T14:38:36Z; the live zip's entry.py _covered carries the FAIL CLOSED branch (a receipt naming no account is refused) and the irpt_export_read_admitted log line; covered_account_ids is wired through handler.py, finalize_on_read.py, receipt.py and bundle.py (read at ~15:1xZ and ~17:0xZ) (this compile's read, dell2, 2026-10-07)",
        "ledger org/critical_paths/change_management/20261007T1356Z_irpt-export-render-ib-pr-349-failclosed-20261007_deploy_completion.md CLOSED"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A security exposure closed in the running bytes and read there; its residual (an unprovable past) is stated, not hidden."
  },
  {
    "id": "IRPT_BCKEND-C-S302",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-07T17:05:00Z",
    "one_line": "Notes and records from rounds 65-67: W145-S1 (tests that minted account-less receipts, resolved by IB-pr-343's amendments), W145-S3 (legacy keys kept, writer never emits them), W145-S4 (pending.json already carried the accounts) and S372 (portal DEV landing of the two reader branches).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_BCKEND-W145-S1",
      "IRPT_BCKEND-W145-S3",
      "IRPT_BCKEND-W145-S4",
      "IRPT_BCKEND-S372"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Each is resolved inside its order or a record of a landing; IB-pr-343 drained VALID under amendment 2 and is the code the live release carries.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row(s) IRPT_BCKEND-W145-S1, IRPT_BCKEND-W145-S3, IRPT_BCKEND-W145-S4, IRPT_BCKEND-S372",
        "IRPT_BCKEND_ROUND32_M_L8_COMPILE.md @d1abea06f8 (msg 605), IRPT_BCKEND_ROUNDS_65_67_P_DRAIN_END_20261007.md @477f0faa28 (msgs 593, 608) and IRPT_BCKEND_ROUND_68_P_DRAIN_END_20261007.md @0e91c577af (msg 886)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Resolved order-scope notes and a landing record; no live hazard."
  }
]
```
