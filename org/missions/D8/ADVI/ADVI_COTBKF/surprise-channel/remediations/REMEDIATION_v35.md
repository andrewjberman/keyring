# ADVI_COTBKF: remediations, rounds 54 to 57

<sweep_watermark>2026-10-11T05:08Z</sweep_watermark>

Rounds 54-57 slug by `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T05:08:20Z. L8 input: `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_57_DRAIN_END_20261011.md @6edfe081c7 (msg 4128)`. **L9: CB57be1-AC2 MET** (`org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_57_L9_GRADE_20261011.md`).
Graduated, round label v58: 4 rows, OPEN, INERT. 
D2-S80 (the manifest is restored) and D2-S77 (the device default is removed) are REMEDIATED on this seat's reads, but their rows in
REMEDIATION_v34 still read OPEN: the row gate refuses the in-place close, because this seat wrote that file's ARMED rows with a
`disarm_owner` string and no `disarm` block. Correcting them is a gate question for `1.0.0_SA_CTO`.
Still ARMED from REMEDIATION_v34: D2-S60 and D2-W66-S1, both gating the CB-al-2 mint.

**For the CB-al-2 pair (the CTO's ruling):** method row 3's income basis is true for every row being minted, because no measured
account-day holds a bond; it would be false for a bond day priced from this store. The pair states that limit, or row 3's text is
edited first.

```json
[
 {
  "id": "ADVI_COTBKF-D2-S84",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "With the device default removed, no non-test importer of commonwealth_sweeps has a source for COTBKF_SWEEPS_CONFIG other than the shell of whoever runs it. 11 scripts import the module directly and none sets or documents the variable; each fails closed at import.",
  "evidence": [
   "investigation rows ADVI_COTBKF-D2-S84 and ADVI_COTBKF-D2-S83",
   "this seat's read of data/assets/scripts/silver/commonwealth_sweeps.py at HEAD: no device path and no SWEEPS_CONFIG_DEFAULT; the path is the argument or COTBKF_SWEEPS_CONFIG"
  ],
  "remedy": "State where the private config lives for a run (one documented variable per box, or a resolver beside the scripts) and which runs need it. The silver suite's collection states the same requirement.",
  "owner": "2.0.0_SA_COO~C2",
  "round": "v58",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~C2",
   "round": "v58"
  },
  "closed": false
 },
 {
  "id": "ADVI_COTBKF-D2-W83-S2",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "CB56bd1-AC1 and CB56bd1-AC2 cannot read 'passed' as written: a round-55 test asserts the variable is set, and the criteria run with it unset. The issuer closed round 56 on its own runs.",
  "evidence": [
   "investigation row ADVI_COTBKF-D2-W83-S2",
   "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_57_DRAIN_END_20261011.md @6edfe081c7 (msg 4128)"
  ],
  "remedy": "The two criteria and that test are reconciled (one states the variable set, the other unset), so the next issuance does not inherit a check that fails on a correct tree.",
  "owner": "2.0.0_SA_COO~C2",
  "round": "v58",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~C2",
   "round": "v58"
  },
  "closed": false
 },
 {
  "id": "ADVI_COTBKF-D2-W66-S2",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "Blank days carry day_quality NOT_MEASURABLE with no reason column in the table's schema; the reasons are in a sidecar only.",
  "evidence": [
   "investigation row ADVI_COTBKF-D2-W66-S2"
  ],
  "remedy": "IRPT_DASHBD's contract call: a reason column, or the sidecar named in the contract as the reason's carrier.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v58",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v58"
  },
  "closed": false
 },
 {
  "id": "ADVI_COTBKF-D2-W66-S3",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The holdings neighbour and the FWD-3 rows share no account id string on any of 75 neighbour days, so NO_HOLDINGS_ROW means 'no row under this id', not 'no holdings'.",
  "evidence": [
   "investigation row ADVI_COTBKF-D2-W66-S3"
  ],
  "remedy": "An account crosswalk between the two id forms, or the guard states it cannot grade these rows.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v58",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v58"
  },
  "closed": false
 }
]
```
