# ADVI_COTBKF: remediations, rounds 58 to 63

<sweep_watermark>2026-10-11T09:31Z</sweep_watermark>

Slug by `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T09:31:33Z. L8 inputs: `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_62_63_DRAIN_END_20261011.md @53af818717 (msg 4568)`, the round 61 packet and the mint packet.
**L9, all MET on this seat's own reads:** CB61bi1-AC2, CB61bi2-AC2, CB38al1-AC2 (the served mint), CB62bj1-AC3 (the break-glass role).
Graduated, round label v64: 6 rows, OPEN. ARMED: 1 (D2-S92), disarm owner `1.0.0_SA_CTO~DELL2`.

**For the CTO's analysis:**
1. The Cottonwood returns table is served, truthful and 94% blank (row D2-S100). IRPT_DASHBD's publisher would refuse it as it
   stands, because income is null on every row (IRPT_DASHBD row D2-W96-S2).
2. The break-glass role's trust carries no condition. That is what the pair signed.
3. Still open as a gate question: REMEDIATION_v34's rows D2-S80, D2-S77, D2-S60 and D2-W66-S1 are remediated or disarmed and cannot be
   closed in place (this seat wrote that file's ARMED rows without a `disarm` block).

```json
[
 {
  "id": "ADVI_COTBKF-D2-S92",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "A refreshing plan of shared-infra on dell2's credentials is denied two reads on the portal bucket, and the provider renders that as the bucket deleted: the plan wants to create the bucket and replace its encryption configuration. An untargeted apply from dell2 would act on them.",
  "evidence": [
   "investigation row ADVI_COTBKF-D2-S92",
   "this seat's read of the applier's saved plans under C:/dev/_cotbkf_private_evidence_20261009/r63/: step2_plan.json holds 2 resource changes, both creates, the role and its policy; shared_infra_plan_after.json holds 242 with 2 changing, neither of them the two (the portal bucket artifacts of row D2-S92)"
  ],
  "remedy": "No seat applies shared-infra from dell2 (the CTO's ruling) until the two reads are granted or the root is planned from a box that has them. The after-plan of round 63 still lists both.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v64",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v64"
  },
  "closed": false,
  "disarm": {
   "state": "ARMED",
   "owner": "1.0.0_SA_CTO~DELL2",
   "at": null
  }
 },
 {
  "id": "ADVI_COTBKF-D2-S100",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "75.8% of Cottonwood position rows carry no value because no close exists for the security. The minted returns table is 94% blank for that reason.",
  "evidence": [
   "investigation row ADVI_COTBKF-D2-S100",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_MINT_CB38AL1_AC2_L9_GRADE_20261011.md"
  ],
  "remedy": "FWD-8's coverage work, sized by the CTO's analysis: the price source's coverage of Cottonwood's holdings, weighted by value.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v64",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v64"
  },
  "closed": false
 },
 {
  "id": "ADVI_COTBKF-D2-S101",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "1,757 minted account-days are MEASURED with no holdings row: each has a day-end value of exactly 0 and nearly all carry an external flow. They are the day an account is emptied.",
  "evidence": [
   "investigation row ADVI_COTBKF-D2-S101"
  ],
  "remedy": "The first reader states how it shows such a day (the CTO's condition on the reader, msg 4472, asks this row answered first).",
  "owner": "2.0.0_SA_COO~C2",
  "round": "v64",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~C2",
   "round": "v64"
  },
  "closed": false
 },
 {
  "id": "ADVI_COTBKF-D2-W86-S2",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The mint's apply now refuses an unstamped manifest; the older apply tests pass only because a conftest turns that refusal off for their module.",
  "evidence": [
   "investigation row ADVI_COTBKF-D2-W86-S2"
  ],
  "remedy": "The older tests supply a stamped manifest, and the conftest switch is removed.",
  "owner": "2.0.0_SA_COO~C2",
  "round": "v64",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~C2",
   "round": "v64"
  },
  "closed": false
 },
 {
  "id": "ADVI_COTBKF-D2-W87-S1",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The wider served read-back changed the verify line; two older exact-line tests outside that order's grant fail on it.",
  "evidence": [
   "investigation row ADVI_COTBKF-D2-W87-S1"
  ],
  "remedy": "The two tests are updated to the new line, or each has an owner.",
  "owner": "2.0.0_SA_COO~C2",
  "round": "v64",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~C2",
   "round": "v64"
  },
  "closed": false
 },
 {
  "id": "ADVI_COTBKF-D2-S99",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The deploy ledger tool has no state for an apply refused by a gate with nothing created: both of its hold forms refuse the case.",
  "evidence": [
   "investigation row ADVI_COTBKF-D2-S99"
  ],
  "remedy": "The ledger gains that state. The tool is not this project's; the CTO places it with its owner.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v64",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v64"
  },
  "closed": false
 }
]
```
