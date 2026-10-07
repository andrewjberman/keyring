# IRPT_CUSTDY: CVO adjudication, round 1

<sweep_watermark>2026-10-07T08:52Z</sweep_watermark>

Round 1 L8 compile and L9 adjudication by `3.0.0_SA_CVO` (seated on dell2), 2026-10-07 ~09:0xZ. L8 input: the drain-end packet
`org/missions/D9/IRPT/IRPT_CUSTDY/deliverables/2.0.0_SA_COO~K2/IRPT_CUSTDY_ROUND_1_DRAIN_END_20261007.md @4b15819af3` (msg 202). 4 of 4 orders complete and VALID: CU-a-1 @9dd85cec00, CU-a-2 @36c37ef88d, CU-a-3 @737839f762, CU-a-4 @06a44e56bd.
0 JUDGMENT criteria. FWD-1's thread is NOT LIVE (hop 1 fails on real data, S3; hop 5 has no document input, W4-S1). 6 rows: 3 dismissed by
C-S1 below, 3 graduated in `remediations/REMEDIATION_v1.md` (S3, W1-S1, W4-S1, all OPEN). ARMED before and after: 0. This seat re-ran the
issuer's failing pick and read the render host's inputs.

```json
[
 {
  "id": "IRPT_CUSTDY-C-S1",
  "project": "IRPT_CUSTDY",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-07T09:05Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "S1 (the render path's input, asked at the cut), S2 (the issuer's drain rulings) and W2-S1 (five figure rules the contract left open, accepted for round 1) are dismissed.",
  "adjudicates": [
   "IRPT_CUSTDY-S1",
   "IRPT_CUSTDY-S2",
   "IRPT_CUSTDY-W2-S1"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
  "world_is": "S1's question was measured by CU-a-4, and the answer is row W4-S1, which graduates. S2 is a record of the issuer's rulings inside its own decomposition; its effects are carried on W1-S1 and W4-S1 (graduated) and W2-S1. W2-S1: each open rule is one function in client_report_figures.py with its reading stated in the docstring, and the issuer accepts them for round 1. A change is an enrichment item; no figure is served this round.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "investigation rows IRPT_CUSTDY-S1, S2, W2-S1",
    "org/missions/D9/IRPT/IRPT_CUSTDY/deliverables/2.0.0_SA_COO~K2/IRPT_CUSTDY_ROUND_1_DRAIN_END_20261007.md @4b15819af3",
    "infra/aws/ec2/investor-reporting-export/render_export.cjs:226-234: the host's inputs are a bundle key, an output key, export and attempt ids, a print route and the portal origin; IRPT_TEMPLATE is a name with a default, not a template body (this compile's read, dell2 CLOUD, 2026-10-07 ~08:5xZ-09:0xZ)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A question answered by a later row, a record of rulings carried on the rows they name, and figure readings accepted by the issuer for a round that serves nothing."
 }
]
```
