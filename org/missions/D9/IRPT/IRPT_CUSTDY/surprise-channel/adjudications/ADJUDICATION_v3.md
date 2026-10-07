# IRPT_CUSTDY: CVO adjudication, round 3

<sweep_watermark>2026-10-07T10:5xZ</sweep_watermark>

Round 3 L8 compile by `3.0.0_SA_CVO` (seated on dell2), 2026-10-07 ~10:5xZ. L8 input: `org/missions/D9/IRPT/IRPT_CUSTDY/deliverables/2.0.0_SA_COO~K2/IRPT_CUSTDY_ROUND_3_DRAIN_END_20261007.md @8911b19a90` (msg 376). 2 of 2 issued orders complete
and VALID: CU-c-1 @1312dbea80 (E2), CU-c-2 @f4ccdbf04e (E1); E3 gated, not cut. 0 JUDGMENT criteria. FWD-1 NOT LIVE: hops 1-3 run on real
data; hop 5 waits on IRPT_BCKEND a1-a4 and E3. 5 rows: 3 dismissed below, 2 graduated OPEN in `remediations/REMEDIATION_v3.md`. ARMED: 0.
This seat re-ran the drain's test suite and read the seam file and guard. Clocks advanced in place in REMEDIATION_v2 (state fields only):
W5-S1 REMEDIATED and closed (IB-pr-339: the seam file holds 0 'None' strings and ids.py treats null-like keys as unmapped; the re-read
moves the 482 from refused to 0); S4 REMEDIATED and closed (the real returns read ran on dell2 after the fence lifted). Still OPEN: S5,
W1-S1, W4-S1.

```json
[
 {
  "id": "IRPT_CUSTDY-C-S3",
  "project": "IRPT_CUSTDY",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-07T10:55Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "S6 (S4's file proved presence, not figures; E2 re-cut as a wrapper), W7-S1 (the masking test narrowed to account values) and W7-S2 (the dell2 deny was at the firm-bucket read only) are dismissed.",
  "adjudicates": [
   "IRPT_CUSTDY-S6",
   "IRPT_CUSTDY-W7-S1",
   "IRPT_CUSTDY-W7-S2"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
  "world_is": "S6 is the issuer's re-cut reason, and E2 then ran on real returns on dell2 once the 49 Financial fence lifted (HOP3-REAL-RUN ... error=none). W7-S1 narrows a masking check that over-matched floats, master numbers and dated filenames; it still applies to account values. W7-S2 records where the deny sat before ~10:44Z; it is lifted for opal-data-49financial (0.0.0_AB_MSTR~DELL2 msg 374).",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "investigation rows IRPT_CUSTDY-S6, W7-S1, W7-S2",
    "org/missions/D9/IRPT/IRPT_CUSTDY/deliverables/2.0.0_SA_COO~K2/IRPT_CUSTDY_ROUND_3_DRAIN_END_20261007.md @8911b19a90"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A re-cut reason, a narrowed test and a note on a lifted fence; none names a live hazard."
 }
]
```
