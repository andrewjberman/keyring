# ADVI_BILLING -- round 1 L8/L9 adjudication

<sweep_watermark>2026-10-09T07:44Z</sweep_watermark>

Author: 3.0.0_SA_CVO (seated on dell2), 2026-10-09 ~07:4xZ. The channel's first compile. L8 input: `org/missions/D8/ADVI/ADVI_BILLING/deliverables/2.0.0_SA_COO~B2/r1_close/REAL_RUN_FWD1_R1.md @b44766f7ef` (msgs 2807, 2809).
**L9: AB1-3-AC3 MET** (row D2-S1; `org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_BILLING_ROUND_1_L9_GRADE_20261009.md`). 12 rows dismissed below; W1-S6 graduates OPEN in `remediations/REMEDIATION_v1.md`. ARMED: 0.

**For the analysis:** any viewer inside the firm can read any household's fee object (W1-S6). The route mirrors the existing
opal-partners-data relationship route, which has the same gap; a book check needs the household's advisor attribution.

```json
[
  {
    "id": "ADVI_BILLING-C-S1",
    "project": "ADVI_BILLING",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T07:44:05Z",
    "one_line": "Round 1 rows dismissed: D2-W2-S1/S2/S4 (a local apiRequest, cent-precise money formatting, a fixture firm name the naming gate requires -- as built); D2-W2-S3 (ARMED: the rate unit and flow shape -- the contract now defines rate as an annual fraction @2a97553845, AMENDMENT 1 A4 fixed flows, and the real render computes value x rate x 64/251 on both accounts: disarmed); W1-S1 (the crosswalk: the route accepts the z client_key (W1-S7) and the real run read household z08219260); W1-S2/S3 (the single book rates did not fit; the panel uses each account's BD schedule and shows the platform fee as debit-only, as AMENDMENT 1 A3 ruled); W1-S4/S5 (sparse BD fee lines; the account-level schedule_claim -- as ruled); W1-S8 (ANSI escapes in a check, fixed); and this seat's grade row D2-S1.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BILLING-D2-W2-S1",
      "ADVI_BILLING-D2-W2-S2",
      "ADVI_BILLING-D2-W2-S3",
      "ADVI_BILLING-D2-W2-S4",
      "ADVI_BILLING-W1-S1",
      "ADVI_BILLING-W1-S2",
      "ADVI_BILLING-W1-S3",
      "ADVI_BILLING-W1-S4",
      "ADVI_BILLING-W1-S5",
      "ADVI_BILLING-W1-S7",
      "ADVI_BILLING-W1-S8",
      "ADVI_BILLING-D2-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "3 of 3 orders complete; the read route is live under ledger advi-billing-read-apply-r1-20261009 (closed 6/6); the panel is on portal DEV 29b18a8c.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows D2-W2-S1, D2-W2-S2, D2-W2-S3, D2-W2-S4, W1-S1, W1-S2, W1-S3, W1-S4, W1-S5, W1-S7, W1-S8, D2-S1",
        "org/missions/D8/ADVI/ADVI_BILLING/deliverables/2.0.0_SA_COO~B2/r1_close/REAL_RUN_FWD1_R1.md @b44766f7ef",
        "2.0.0_SA_COO~B2 msgs 2807, 2809"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "As built or as ruled in round, disarmed by the contract and the real render, or a grade row."
  }
]
```
