# ADVI_BILLING -- round 3 L8 adjudication and FWD-3 grade

<sweep_watermark>2026-10-09T10:15Z</sweep_watermark>

Author: 3.0.0_SA_CVO (seated on dell2), 2026-10-09 ~10:1xZ. L8 input: `org/missions/D8/ADVI/ADVI_BILLING/deliverables/2.0.0_SA_COO~B2/r3_close/DRAIN_END_R3.md @a62249088d` (msg 3103). **FWD-3: REALIZED** (row D2-S5; `org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_BILLING_ROUND_3_L9_GRADE_20261009.md`).
4 rows dismissed below; D2-S3 and D2-S4 closed in place; D2-W7-S1 graduates OPEN in `remediations/REMEDIATION_v3.md`. ARMED: 0.

**For the analysis:** FWD-3 is realized on real data, and the cross-firm refusal is exercised, not absent. The panel's PROD push is
Andrew's word (the page is client-facing). The E2 release (the SMArtX statement tool) is site Z's, carried by D2-W7-S1.

```json
[
  {
    "id": "ADVI_BILLING-C-S3",
    "project": "ADVI_BILLING",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T10:15:45Z",
    "one_line": "Round 3 rows dismissed: D2-W7-S2 (the gateway env line lives in deploy-to-ec2.sh; packed into site Z's release), D2-W7-S3 (a whole-root plan cannot run from dell2; the targeted plan reads 1/0/0), D2-W7-S4 (the HCL takes the bucket from the registry's tier-home rule, as opal_name reads exemptions.json), and this seat's FWD-3 grade row D2-S5 (REALIZED). Closed in place, clocks only: D2-S4 (FWD-3's flows and exclusions now stated on real data) and D2-S3 (the cross-firm arm EXERCISED: an Inflection admin token with complete claims is refused 401 'Access denied to this firm' by advi-49f-billing-read-lambda). D2-W7-S1 (BLOCKING for the release) graduates to site Z.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BILLING-D2-W7-S2",
      "ADVI_BILLING-D2-W7-S3",
      "ADVI_BILLING-D2-W7-S4",
      "ADVI_BILLING-D2-S5"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "3 of 3 orders complete, round-close-check --round 3 MAY-CLOSE (this seat's read). The CTO's PROD precondition for the panel (msg 2995 item 3) reads complete; the PROD push is Andrew's word.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows D2-W7-S2, D2-W7-S3, D2-W7-S4, D2-S5",
        "org/missions/D8/ADVI/ADVI_BILLING/deliverables/2.0.0_SA_COO~B2/r3_close/DRAIN_END_R3.md @a62249088d"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Release-packing notes, a grade row, and two rows closed on measured evidence."
  }
]
```
