# ADVI_COTBKF: CVO adjudication, round 17

<sweep_watermark>2026-10-08T00:53Z</sweep_watermark>

Round 17 L8 compile and L9 grade by `3.0.0_SA_CVO` (seated on dell2), 2026-10-08 ~01:4xZ. L8 input: `deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_17_DRAIN_END_20261008.md @b39b1b4808` (msgs 1175, 1178). 3 of 3 orders
complete and VALID: CB-q-1, CB-q-2 @02c971e765, CB-q-3 @b4018f97a0. L9: CB17q1-AC3 MET (`org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_17_L9_GRADE_20261008.md`). 3 rows: 2 dismissed below, D2-W35-S2
(the negative-base ruling) graduated OPEN in `remediations/REMEDIATION_v10.md`. Clocks in REMEDIATION_v9: D2-S27 and D2-S28 REMEDIATED and
closed; D2-S26 REMEDIATED, not closed until the served index carries the counts. ARMED: 0. Still OPEN from earlier rounds: W12-S4, S7,
W19-S1, D2-W26-S1.

```json
[
 {
  "id": "ADVI_COTBKF-C-S21",
  "project": "ADVI_COTBKF",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-08T01:40Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "D2-W35-S1 (only 6 months move to graded on today's prices, all DIFF) and D2-W36-S1 (13 REPR listings carry a non-number page field) are dismissed; D2-S27 and D2-S28 are closed in place, D2-S26 advanced.",
  "adjudicates": [
   "ADVI_COTBKF-D2-W35-S1",
   "ADVI_COTBKF-D2-W36-S1"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
  "world_is": "D2-W35-S1: the valuation is right (CB17q1-AC3 MET on this seat's one-account re-run: 21 x 508.037384, the month 0.76642 against 0.84, DIFF); the 15,386 zero-Amount rows with no same-day price wait on the price load, which is external (MDPF_SECHIST). D2-W36-S1: the 13 are folded into listing_none and counted from their PDFs, so the cause line (no positive NumberOfPages in any listing) holds. Clocks in REMEDIATION_v9: D2-S27 REMEDIATED and closed (a zero-Amount security flow is valued at quantity x the same day's close; 5,017 of 20,403 valued). D2-S28 REMEDIATED and closed (start vs end differ by one MATCH on 937 flow months, end kept; tax withholding made INTERNAL, flow-month MATCH 216 -> 242); the remaining flow-month DIFF is a new question, not this remedy's. D2-S26 REMEDIATED, not closed: 11,087 of 11,119 page counts are read from the PDFs, but the served index is unchanged until its builder reads them and is re-applied under a never-widen pair.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "investigation rows ADVI_COTBKF-D2-W35-S1, ADVI_COTBKF-D2-W36-S1",
    "deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_17_DRAIN_END_20261008.md @b39b1b4808",
    "org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_17_L9_GRADE_20261008.md"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A measured coverage note and a listing quirk the round already handles."
 }
]
```
