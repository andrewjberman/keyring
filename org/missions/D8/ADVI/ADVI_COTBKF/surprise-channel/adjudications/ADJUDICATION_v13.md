# ADVI_COTBKF: CVO adjudication, round 16

<sweep_watermark>2026-10-07T20:5xZ</sweep_watermark>

Round 16 L8 compile by `3.0.0_SA_CVO` (seated on dell2), 2026-10-07 ~21:0xZ. L8 input: `deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_16_DRAIN_END_20261007.md` (msg 1086). 3 of 3 orders complete and VALID:
CB-p-1 @b07434a3f5, CB-p-2 @319769d04e, CB-p-3 @9884c4bd5d. FWD-3's chain runs end to end on Opal's stores; prices are the binding gap (7.8%
of account-days fully priced). 8 rows: 5 dismissed below, 3 graduated OPEN in `remediations/REMEDIATION_v9.md`. Clock advanced in place:
W6-S5 (REMEDIATION_v1) REMEDIATED and closed. ARMED: 0. Still OPEN from earlier rounds: W12-S4, S7, W19-S1, D2-W26-S1.

```json
[
 {
  "id": "ADVI_COTBKF-C-S20",
  "project": "ADVI_COTBKF",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-07T21:05Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "D2-S22 (the FWD-1 thread re-traced after the applies reproduces), D2-S23 (closes W6-S5), D2-W33-S1 (Amount's sign; answered by the round's census), D2-W33-S2 and D2-W32-S1 (loader notes) are dismissed; W6-S5 closed in place.",
  "adjudicates": [
   "ADVI_COTBKF-D2-S22",
   "ADVI_COTBKF-D2-S23",
   "ADVI_COTBKF-D2-W33-S1",
   "ADVI_COTBKF-D2-W33-S2",
   "ADVI_COTBKF-D2-W32-S1"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
  "world_is": "D2-S22: both 2026-10-06 traces reproduce on dell2 after rounds 4-11's applies (0 rows missing or changed; acct#0e4ff3a3's 5 extra rows are C-SILVER-restored repeats), every trace resolving to its delivered line. D2-S23: commonwealth_price_census.py reads every legacy store through lib/opal_naming.legacy_address() (7 references) and no longer reads a --stores record file (this seat read it), so W6-S5 (REMEDIATION_v1) is REMEDIATED and closed. D2-W33-S1: the round's Amount census settles the sign (unsigned on in/out types, negative on ftax/stax), so direction x |Amount| is right. D2-W33-S2 and D2-W32-S1 are notes on loaders that each script now works around in memory.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "investigation rows ADVI_COTBKF-D2-S22, ADVI_COTBKF-D2-S23, ADVI_COTBKF-D2-W33-S1, ADVI_COTBKF-D2-W33-S2, ADVI_COTBKF-D2-W32-S1",
    "deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_16_DRAIN_END_20261007.md",
    "pytest -q data/assets/scripts/silver/tests: 465 passed, 11 skipped (this compile's read, dell2 CLOUD, 2026-10-07 ~21:0xZ)",
    "data/assets/scripts/analysis/commonwealth_price_census.py: legacy_address 7 occurrences, '--stores' absent (this compile's read, dell2 CLOUD, 2026-10-07 ~21:0xZ)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A reproduced trace, a closure record, a settled convention and two loader notes."
 }
]
```
