# ADVI_COTBKF: remediations, round 19

<sweep_watermark>2026-10-08T17:38Z</sweep_watermark>

Round 19 L8 compile and L9 grade by `3.0.0_SA_CVO` (seated on dell2), 2026-10-08 ~17:5xZ. L8 input:
`deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_19_DRAIN_END_20261008.md` (msg 1351). 1 of 1 order complete and VALID: CB-s-1
@bf424e274b. L9: CB19s1-AC3 MET (`org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_19_L9_GRADE_20261008.md`), with one
finding for the analysis: 316067107 (Fidelity Government Cash Reserves) trades like a core sweep across 232 accounts and is off
the list because the ruling covers bank sweeps only. Undispositioned before this compile: 1 of 78 rows (D2-S29); it graduates OPEN
below, with this seat's L9 row D2-S30 (the core-sweep finding). No row is dismissed, so no adjudication file is minted. Clock in REMEDIATION_v11: D2-W39-S1 OPEN -> REMEDIATED (the sweep
is INTERNAL; 42 of the 74 double-drop months now MATCH), not closed while D2-S29 and the money-market-funded months stand. ARMED: 0.

```json
[
 {
  "id": "ADVI_COTBKF-D2-S29",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The sweep-is-cash re-grade moves 163 months MATCH -> DIFF beside 543 DIFF -> MATCH; the 163 are unexplained. The control (642 of 642 months of accounts with no listed-sweep row unchanged) holds, so the movers are all in sweep accounts.",
  "evidence": [
   "investigation row ADVI_COTBKF-D2-S29 (2.0.0_SA_COO~C2)",
   "deliverables/0.9.0_WK_ADVI_COTBKF~40/sweep_regrade.md: whole grade 1,685/1,931/78,977 -> 2,057/1,522/79,014; control_same=True",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_19_L9_GRADE_20261008.md: 316067107 held by 232 accounts, 91% same-day paired"
  ],
  "remedy": "Class the 163 months before the next repair: by account, whether each holds an unlisted core money-market position (316067107 first), whether the sweep balance at 1.0 enters a month that matched by offsetting errors, or neither. The month grades are not persisted (only day values under .scratch/advi_cotbkf/fwd3/sweep_regrade), so the classing re-runs the chain.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v20",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v20"
  },
  "closed": false
 },
 {
  "id": "ADVI_COTBKF-D2-S30",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "316067107 (Fidelity Government Cash Reserves) behaves as a custodian core sweep for 232 accounts but is not a bank sweep, so under the round-18 ruling its balance is a priced holding and its buys and sells are trades.",
  "evidence": [
   "investigation row ADVI_COTBKF-D2-S30 (3.0.0_SA_CVO)",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_19_L9_GRADE_20261008.md"
  ],
  "remedy": "A ruling: whether a money-market core position is a sweep vehicle; if yes, it goes on the declared list with its stated source and the chain re-grades (D2-S29's classing first tells whether the 163 MATCH->DIFF months sit in these accounts).",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v20",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v20"
  },
  "closed": false
 }
]
```
