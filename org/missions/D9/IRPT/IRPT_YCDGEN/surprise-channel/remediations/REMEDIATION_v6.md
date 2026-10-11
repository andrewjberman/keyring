# IRPT_YCDGEN: remediations, round 7

<sweep_watermark>2026-10-11T06:46Z</sweep_watermark>

Round 7 slug by `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T06:46:30Z. L8 input: `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/r7/ROUND7_DRAIN_END_READ_20261011.md @6505291224 (msg 4282)`. L9: `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_YCDGEN_ROUND_7_L9_GRADE_20261011.md`.
**FWD-1 is NOT MET by the run of record.** The served read path on irpt-status revision 6 is established.
Graduated, round label v8: 11 rows, OPEN. ARMED: 6 (D2-S38, S16, W6-S1, W6-S2, D2-W6-S3, D2-W7-S1; the issuer names the last four as not yet re-measured). 45 INERT rows of rounds 6 and 7 are not compiled in this pass.

```json
[
 {
  "id": "IRPT_YCDGEN-D2-S39",
  "project": "IRPT_YCDGEN",
  "fabric": "dell2",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "FWD-1's journey has not been run: the run of record is a service account reading an existing 49financial request. No submission, no sitting by Andrew, no page opened; 251 of 257 sections read NOT_AVAILABLE.",
  "evidence": [
   "investigation row IRPT_YCDGEN-D2-S39",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_YCDGEN_ROUND_7_L9_GRADE_20261011.md",
   "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/r7/R4_R5_OWNER_READ_REV6_20261011.json @46e01935cf"
  ],
  "remedy": "One live sitting as the PRD words it: Andrew signs in, submits a Cottonwood portfolio and opens the Overview. Rows D2-S38 and S16 are cleared first. The CTO rules whether 6 of 257 valued sections is an acceptable first Overview.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v8",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v8"
  },
  "closed": false
 },
 {
  "id": "IRPT_YCDGEN-D2-S38",
  "project": "IRPT_YCDGEN",
  "fabric": "dell2",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "mechanism": "The portal's own status-job call (with the date opt-in header) is refused INVALID_INPUT for a READY Opal report: 251 of 257 sections sit undated. The page would not show a finished Opal report as finished.",
  "evidence": [
   "investigation row IRPT_YCDGEN-D2-S38",
   "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/r7/R6_STATUS_JOB_OPT_IN_REV6_20261011.json @220bbcfa95"
  ],
  "remedy": "As the CTO ruled it (msg 4188); the close is the portal's own call answering for a READY Opal report, read by this seat on the live function.",
  "owner": "2.0.0_SA_COO~G2",
  "round": "v8",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~G2",
   "round": "v8"
  },
  "closed": false,
  "disarm": {
   "state": "ARMED",
   "owner": "2.0.0_SA_COO~G2",
   "at": null
  }
 },
 {
  "id": "IRPT_YCDGEN-S16",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "Andrew's own F1 run of 2026-10-07 stopped at generation with 'This action is unavailable (ENVELOPE_STATUS)'. It has not been re-run since the fixes of rounds 6 and 7.",
  "evidence": [
   "investigation row IRPT_YCDGEN-S16",
   "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/r7/ROUND7_DRAIN_END_READ_20261011.md @6505291224 (msg 4282)"
  ],
  "remedy": "The issuer re-measures the generation step on the live build before Andrew's next sitting, and states what changed since 2026-10-07.",
  "owner": "2.0.0_SA_COO~G2",
  "round": "v8",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~G2",
   "round": "v8"
  },
  "closed": false,
  "disarm": {
   "state": "ARMED",
   "owner": "2.0.0_SA_COO~G2",
   "at": null
  }
 },
 {
  "id": "IRPT_YCDGEN-W6-S1",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "mechanism": "With the OPAL_ENGINE branch in the schema, the generator's output differs from the committed generated type, so the criterion that compares them is unreachable.",
  "evidence": [
   "investigation row IRPT_YCDGEN-W6-S1",
   "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/r7/ROUND7_DRAIN_END_READ_20261011.md @6505291224 (msg 4282)"
  ],
  "remedy": "The issuer re-measures against the tree as it stands (later cells changed this code, by its own packet) and closes or re-cuts.",
  "owner": "2.0.0_SA_COO~G2",
  "round": "v8",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~G2",
   "round": "v8"
  },
  "closed": false,
  "disarm": {
   "state": "ARMED",
   "owner": "2.0.0_SA_COO~G2",
   "at": null
  }
 },
 {
  "id": "IRPT_YCDGEN-W6-S2",
  "project": "IRPT_YCDGEN",
  "fabric": "laptop",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "mechanism": "With the branch in, 5 python tests and 2 portal content pins went red against the base schema, with one stale hash pin.",
  "evidence": [
   "investigation row IRPT_YCDGEN-W6-S2",
   "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/r7/ROUND7_DRAIN_END_READ_20261011.md @6505291224 (msg 4282)"
  ],
  "remedy": "Same re-measure; DSGN_IRPTV1's suite sample of today names the portal pins still red (its row D2-W43-S2).",
  "owner": "2.0.0_SA_COO~G2",
  "round": "v8",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~G2",
   "round": "v8"
  },
  "closed": false,
  "disarm": {
   "state": "ARMED",
   "owner": "2.0.0_SA_COO~G2",
   "at": null
  }
 },
 {
  "id": "IRPT_YCDGEN-D2-W6-S3",
  "project": "IRPT_YCDGEN",
  "fabric": "dell2",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "mechanism": "The generator emits an interface declared as a union, which is not valid TypeScript, for the v2 report type.",
  "evidence": [
   "investigation row IRPT_YCDGEN-D2-W6-S3",
   "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/r7/ROUND7_DRAIN_END_READ_20261011.md @6505291224 (msg 4282)"
  ],
  "remedy": "Same re-measure: the generated file compiles, or the generator is fixed.",
  "owner": "2.0.0_SA_COO~G2",
  "round": "v8",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~G2",
   "round": "v8"
  },
  "closed": false,
  "disarm": {
   "state": "ARMED",
   "owner": "2.0.0_SA_COO~G2",
   "at": null
  }
 },
 {
  "id": "IRPT_YCDGEN-D2-W7-S1",
  "project": "IRPT_YCDGEN",
  "fabric": "dell2",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "mechanism": "The resident builder's research filter omits .svg, so a research build does not package the Opal logo and the resident host would refuse the Opal layout.",
  "evidence": [
   "investigation row IRPT_YCDGEN-D2-W7-S1",
   "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/r7/ROUND7_DRAIN_END_READ_20261011.md @6505291224 (msg 4282)"
  ],
  "remedy": "Same re-measure: one research build lists the logo among its members.",
  "owner": "2.0.0_SA_COO~G2",
  "round": "v8",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~G2",
   "round": "v8"
  },
  "closed": false,
  "disarm": {
   "state": "ARMED",
   "owner": "2.0.0_SA_COO~G2",
   "at": null
  }
 },
 {
  "id": "IRPT_YCDGEN-D2-S3",
  "project": "IRPT_YCDGEN",
  "fabric": "dell2",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "On 2026-10-08 the resident host held no Opal brand spec or logo, so the Opal layout refused every Opal-path Overview. A later run produced and retained an Opal-engine report, which this seat read served on revision 6; the host's brand files themselves were not read.",
  "evidence": [
   "investigation row IRPT_YCDGEN-D2-S3",
   "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/r7/ROUND7_DRAIN_END_READ_20261011.md @6505291224 (msg 4282)"
  ],
  "remedy": "The issuer states the host's brand spec and logo as present (one listing), and this row closes on it.",
  "owner": "2.0.0_SA_COO~G2",
  "round": "v8",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~G2",
   "round": "v8"
  },
  "closed": false
 },
 {
  "id": "IRPT_YCDGEN-D2-W6-S1",
  "project": "IRPT_YCDGEN",
  "fabric": "dell2",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "With the generator reading the v2 schema, its output is not identical to the committed generated report type.",
  "evidence": [
   "investigation row IRPT_YCDGEN-D2-W6-S1",
   "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/r7/ROUND7_DRAIN_END_READ_20261011.md @6505291224 (msg 4282)"
  ],
  "remedy": "Re-measure at the tree as it stands: the generated file equals the committed one, or the difference is ruled.",
  "owner": "2.0.0_SA_COO~G2",
  "round": "v8",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~G2",
   "round": "v8"
  },
  "closed": false
 },
 {
  "id": "IRPT_YCDGEN-D2-W6-S2",
  "project": "IRPT_YCDGEN",
  "fabric": "dell2",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "Three python tests among the readers of the report schemas failed in the worker's tree for reasons outside either schema.",
  "evidence": [
   "investigation row IRPT_YCDGEN-D2-W6-S2",
   "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/r7/ROUND7_DRAIN_END_READ_20261011.md @6505291224 (msg 4282)"
  ],
  "remedy": "Re-measure at the tree as it stands: the three pass, or each has an owner.",
  "owner": "2.0.0_SA_COO~G2",
  "round": "v8",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~G2",
   "round": "v8"
  },
  "closed": false
 },
 {
  "id": "IRPT_YCDGEN-D2-W8-S1",
  "project": "IRPT_YCDGEN",
  "fabric": "dell2",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "The accepted analysis request record carries no server-recorded actor (only the upload row does), so the owner-read cell's code arm stopped.",
  "evidence": [
   "investigation row IRPT_YCDGEN-D2-W8-S1",
   "org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/r7/ROUND7_DRAIN_END_READ_20261011.md @6505291224 (msg 4282)"
  ],
  "remedy": "The request record carries its actor, or the CTO rules the upload row as the source of the owner.",
  "owner": "2.0.0_SA_COO~G2",
  "round": "v8",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~G2",
   "round": "v8"
  },
  "closed": false
 }
]
```
