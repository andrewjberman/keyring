# ADVI_COTBKF: CVO adjudication, round 6

<sweep_watermark>2026-10-07T10:30Z</sweep_watermark>

Round 6 L8 compile and L9 by `3.0.0_SA_CVO` (seated on dell2), 2026-10-07 ~10:5xZ. L8 input: `deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_6_DRAIN_END_20261007.md @f6d26131f1` (msg 340): CB-f-1 VALID @fa9d12daa1,
and the issuer's three applies (E5 crosswalk, E3 documents, E2 links), each under a never-widen pair with its ledger CLOSED. 6 rows (S13-S18):
5 dismissed by C-S12 below, 1 graduated in `remediations/REMEDIATION_v4.md` (S14, REMEDIATED and closed). Clocks advanced in place: S9 and
S12 (REMEDIATION_v3) DISARMED by 2.0.0_SA_COO~C2 (rows S16, S18), REMEDIATED and closed; W12-S1 (REMEDIATION_v2) DISARMED (row S17),
REMEDIATED and closed. ARMED after: 0. L9: CB4d5-AC3 MET; CB4d1-AC3 re-graded NOT MET (W12-S2 stays OPEN); grade file `org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_6_L9_GRADE_20261007.md`.
Still OPEN from earlier rounds: W6-S5, W12-S2, W12-S4, S7, W19-S1.

```json
[
 {
  "id": "ADVI_COTBKF-C-S12",
  "project": "ADVI_COTBKF",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-07T10:50Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "S13 (S12's premise corrected: the applies write opal-data-assets), S15 (the laptop's listing of the two never-listed buckets), and the disarm records S16 (S9), S17 (W12-S1) and S18 (S12) are dismissed; L9: CB4d5-AC3 MET, CB4d1-AC3 re-graded NOT MET.",
  "adjudicates": [
   "ADVI_COTBKF-S13",
   "ADVI_COTBKF-S15",
   "ADVI_COTBKF-S16",
   "ADVI_COTBKF-S17",
   "ADVI_COTBKF-S18"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
  "world_is": "S13: opal_naming.address() resolves the crosswalk, documents and links to opal-data-assets, so S12's fence was measured on a bucket neither apply touches; this seat's REMEDIATION_v3 S12 mechanism carried that wrong premise, and S18 closes it on the applies actually run (three ledgers CLOSED). S16: the links applied from dell2 on the 2010-2027 calendar equal the laptop deliverable on every column, 1,450 of 1,450. S17: the census on the covering calendar needs 9,388,961 security-days, equal to round 2. S15 is the input to this seat's CB4d1-AC3 re-grade, which stays NOT MET (W12-S2 stays OPEN). Clocks advanced in place: S9, S12 (REMEDIATION_v3), W12-S1 (REMEDIATION_v2).",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "investigation rows ADVI_COTBKF-S13, S15, S16, S17, S18",
    "deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_6_DRAIN_END_20261007.md @f6d26131f1",
    "org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_6_L9_GRADE_20261007.md"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A premise correction, a listing, and three disarm records; their effects are carried on the rows and grades they name."
 }
]
```
