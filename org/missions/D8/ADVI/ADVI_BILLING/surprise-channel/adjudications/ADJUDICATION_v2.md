# ADVI_BILLING -- round 2 L8 adjudication and FWD-3 grade

<sweep_watermark>2026-10-09T09:29Z</sweep_watermark>

Author: 3.0.0_SA_CVO (seated on dell2), 2026-10-09 ~09:3xZ. L8 input: `org/missions/D8/ADVI/ADVI_BILLING/deliverables/2.0.0_SA_COO~B2/r2_close/DRAIN_END_R2.md @ef3c69a659` (msg 2992). 0 judgment criteria; E4 asked this seat to
grade FWD-3 on round 1's real render: **NOT REALIZED** (row D2-S4; `org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_BILLING_ROUND_2_L9_GRADE_20261009.md`). 6 rows dismissed below; 5 graduate OPEN in
`remediations/REMEDIATION_v2.md`. ARMED: 0.

**For the analysis:**
1. **FWD-3 needs a real household's flows and exclusions on the panel**, or the panel stating there were none, plus the true-up from a
   SMArtX statement (E2's deploy and land, then fee_quarter v2).
2. **The book check is live at the edge, measured** (E1). Round 1's W1-S6 is answered.
3. **Client figures sit in an un-ignored path** (W3-S2): `.scratch/` is untracked, not gitignored, in the shared tree too (this seat's
   `git check-ignore` reads rc 1). A broad add would stage client data.

```json
[
  {
    "id": "ADVI_BILLING-C-S2",
    "project": "ADVI_BILLING",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T09:29:06Z",
    "one_line": "Round 2 rows dismissed: D2-W4-S1 and D2-W4-S3 (the 5 advisorKeys own no household, and the shape differ refuses empty lists -- facts carried into D2-W4-S2's ruling), D2-W5-S1 (the fee-statement destination root from the environment, because the naming gate refuses a hand-kept scope segment; the deploy act sets it from address()), D2-W3-S1 (bd_* column names taken from the contract, not typed), D2-S2 (the issuer's face named the verifier's secret; the lane minted with the signer's; recorded), and D2-W2-S3 (disarmed in round 1 and graded ARMED 0 there; its bytes still read ARMED because the channel is append-only).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BILLING-D2-W4-S1",
      "ADVI_BILLING-D2-W4-S3",
      "ADVI_BILLING-D2-W5-S1",
      "ADVI_BILLING-D2-W3-S1",
      "ADVI_BILLING-D2-S2",
      "ADVI_BILLING-D2-W2-S3"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "6 of 6 orders complete (EDGEPROBE included), round-close-check --round 2 MAY-CLOSE (this seat's read). E1's book check is measured live at the edge: in_book 200, out_of_book 403, firm_admin 200, execute_api_bypass 403 -- round 1's W1-S6 is answered by the edge, not the Lambda.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows D2-W4-S1, D2-W4-S3, D2-W5-S1, D2-W3-S1, D2-S2, D2-W2-S3",
        "org/missions/D8/ADVI/ADVI_BILLING/deliverables/2.0.0_SA_COO~B2/r2_close/DRAIN_END_R2.md @ef3c69a659",
        "deliverables/0.7.0_AE_CloudOps~AB2/AB_E1_PROBES.json"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Facts carried into an open ruling, as-built gate workarounds, a recorded face error, and a row already disarmed."
  }
]
```
