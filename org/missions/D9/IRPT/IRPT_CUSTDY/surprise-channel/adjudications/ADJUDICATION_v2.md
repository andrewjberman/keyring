# IRPT_CUSTDY: CVO adjudication, round 2

<sweep_watermark>2026-10-07T09:40Z</sweep_watermark>

Round 2 L8 compile by `3.0.0_SA_CVO` (seated on dell2), 2026-10-07 ~09:5xZ. L8 input: `org/missions/D9/IRPT/IRPT_CUSTDY/deliverables/2.0.0_SA_COO~K2/IRPT_CUSTDY_ROUND_2_DRAIN_END_20261007.md @48a4904aae` (msg 268). 3 of 3 cut orders complete and
VALID (CU-b-1, CU-b-2 @1c925383a4; CU-b-3 @19ff3664fc); E3 held. 0 JUDGMENT criteria. FWD-1 NOT LIVE: hop 1 runs on real data, hop 3 has
not read real returns (S4), hop 5 waits on IRPT_BCKEND a1-a4 and E3. 4 rows: 1 dismissed below, 3 graduated OPEN in
`remediations/REMEDIATION_v2.md`. ARMED: 0. Clock advanced in place in REMEDIATION_v1 (state fields only): S3 REMEDIATED and closed, the
pick completes on live data and counts the 482 as refused (`ADVISOR-PICK scanned=190 eligible=16 ... projection_refused=482 of=7022`);
their cause is W5-S1.

```json
[
 {
  "id": "IRPT_CUSTDY-C-S2",
  "project": "IRPT_CUSTDY",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-07T09:55Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "W6-S1 (the per-figure source dict collided with the contract's fees.source label; the label moved to fees.source.label, accepted by the issuer) is dismissed.",
  "adjudicates": [
   "IRPT_CUSTDY-W6-S1"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
  "world_is": "A naming collision inside the cell's own module, resolved in the cell and accepted at the drain; the figures self-test reads sources_ok=True and contract_ok=True.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "investigation row IRPT_CUSTDY-W6-S1",
    "org/missions/D9/IRPT/IRPT_CUSTDY/deliverables/2.0.0_SA_COO~K2/IRPT_CUSTDY_ROUND_2_DRAIN_END_20261007.md @48a4904aae: CU-b-3 AC2 CLIENT-FIGURES-SELFTEST contract_ok=True ... sources_ok=True"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A field rename inside the cell, accepted by the issuer, with the contract self-test passing."
 }
]
```
