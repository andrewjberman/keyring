# AMGT_HARVST ROUND 7 -- L8 COMPILE + L9 ADJUDICATION

**Seat:** `3.0.0_SA_CVO~O`, routed by `1.0.0_SA_CTO~Z` (file 20260927T231533Z) because `3.0.0_SA_CVO~Z` is wound down
on Andrew's word. **Written:** 2026-09-27 ~23:25Z. **Terminality:** 2 of 2 (`HVST-v-1`, `HVST-v-2` complete; issuer
`2.0.0_SA_COO~Y`).

Input: `investigations/INVESTIGATION_v1.md`, 65 rows, 16 of them undispositioned on `_latest_dispositions` before this
compile. This file dispositions the 4 INERT ones and grades AC4. The 12 ARMED ones are carried on
`remediations/REMEDIATION_v1.md`: 6 REMEDIATED and DISARMED, 6 OPEN into round 8. This seat re-ran HVST-v-2's instance:
VALID rc=0.

```json
[
  {
    "id": "AMGT_HARVST-Z-C-S21",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-09-27T23:25:00Z",
    "one_line": "Round 7 L8: four INERT rows are dispositioned DISMISSED_WITH_REASON; each is a fact recorded as filed, with no hazard to disarm and no remedy owed.",
    "class": "OBSERVATION",
    "spec_asserts": "The L8 compile dispositions every undispositioned row of the round.",
    "world_is": "Z-W21-S3: wsj_p2's captured bytes carry an empty searchResults, a vendor-data fact. Z-W22-S1: AC2's 25-name ceiling is unreachable in one invocation by construction; recorded and accepted in the order's AMENDMENT 1. Z-W22-S4: the order file and the worker face named different script paths; AMENDMENT 2 aligned them (limb 3/3, re-run by this seat). Z-S30: 3.0.0_SA_CVO~Z's own row that round 7 was not yet terminal; it is terminal now (2 of 2).",
    "adjudicates": [
      "AMGT_HARVST-Z-W21-S3",
      "AMGT_HARVST-Z-W22-S1",
      "AMGT_HARVST-Z-W22-S4",
      "AMGT_HARVST-Z-S30"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "task-orders/AMGT_HARVST.TO-HVST-v-2.drain-what-is-held-then-capture.md sections 7-9",
        "INVESTIGATION_v1.md#AMGT_HARVST-Z-W21-S3, -Z-W22-S1, -Z-W22-S4, -Z-S30"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "INERT as filed: each records a fact or a resolved misalignment, and none carries a hazard or an owed remedy."
  },
  {
    "id": "AMGT_HARVST-Z-C-S22",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-09-27T23:25:00Z",
    "one_line": "L9 grade, HVST-v-2 AC4 (judgment): PASS with stated limits. 0 of 40 sa listing rows are filed under a wrong name; 36 of 40 link the queried symbol in their own content, and the other 4 are named in the title or are a sector piece.",
    "class": "OBSERVATION",
    "spec_asserts": "AC4: are the listing rows that reached silver actually about the security they are filed under? The worker presents the evidence and does not grade it.",
    "world_is": "The sample is every sa listing_hit row in silver, n = 40: ASML 20 and LNVGY 20. ASML: all 20 filed under security-81a74ed057551e58 (ASML); 17 carry ASML in their content links; r14 carries 'asml' (a case miss by the corroboration check); r17 and r18 name ASML in the title. LNVGY: 19 of 20 carry LNVGY in their content links; r14 is a PC-market sector piece with no link. In the presented evidence LNVGY rows file under no key (the alias-join defect Z-W22-S3); fixed at 4cc54df506, where sa rows match on sa_symbol, so they file under 992_HK (Lenovo).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "deliverables/0.9.0_WK_AMGT_HARVST~22/ac4_output.txt@4dde9408ae",
        "deliverables/0.9.0_WK_AMGT_HARVST~22/AMGT_HARVST.TO-HVST-v-2.drain-what-is-held-then-capture.proof_of_spec.json@508d060383 (VALID rc=0 on this seat's run)",
        "commit 4cc54df506 (the sa_symbol join, reader and builder, with a test)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Grade record only: this row opens and adjudicates no investigation item.",
    "grades": [
      {
        "criterion": "HVSTv2-AC4",
        "instance": "deliverables/0.9.0_WK_AMGT_HARVST~22/AMGT_HARVST.TO-HVST-v-2.drain-what-is-held-then-capture.proof_of_spec.json@508d060383",
        "verdict": "PASS",
        "reason": "No row is counted against the wrong name: every row is about, or names, the security whose symbol was queried. Limits: (1) relevance is not subject -- about half the LNVGY rows are sector or multi-name pieces where Lenovo is one ticker of several, so a per-security count includes coverage that mentions the name rather than coverage of it; (2) the file-under column for LNVGY was presented before the join fix 4cc54df506, so this grade judges the fixed rule (sa_symbol) against these rows, not a post-fix rerun of the evidence; (3) the corroboration check is case-sensitive (ASML r14)."
      }
    ]
  }
]
```

-- 3.0.0_SA_CVO~O
