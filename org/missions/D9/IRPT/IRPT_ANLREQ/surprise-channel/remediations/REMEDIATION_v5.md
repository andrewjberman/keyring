# IRPT_ANLREQ: remediations, rounds 5 to 9 (workstream Y)

<sweep_watermark>2026-10-11T17:07Z</sweep_watermark>

Slug by `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T17:07:52Z. Inputs: msgs 5106 and 5416. Read: `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ANLREQ_ROUNDS_8_9_Y_L9_READ_20261011.md`.
Graduated, round label v10: 3 rows, OPEN. ARMED: 1 (D2-S51), disarm owner `1.0.0_SA_CTO~DELL2`.

**For the CTO's analysis:**
1. **The ordering hazard is still armed** (row D2-S51): the portal change that sends the ticket's id must not reach DEV before the
   service carries its half. It is not on DEV (read by this seat). Only a message holds it.
2. **Release 6 is live and reached by no product path.** Two of its three changed members are called inert on one request; that is
   an inference, as the census says.
3. **Nothing from rounds 3 to 7 is on irpt-status.** Release 5's return, now with the ticket binding, waits on two portal changes
   reaching PROD, which is Andrew's word.
4. **A laptop agent session can read the packager's secret** (row S1, filed by the laptop applier).
5. Of 51 accepted requests, 45 store no ticket id (the laptop's count). That is the baseline the ticket binding meets.

```json
[
 {
  "id": "IRPT_ANLREQ-D2-S51",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "mechanism": "The round-7 portal candidate makes a ticket's Open report read send ticket_id. Live irpt-status (revision 6) refuses any query member but selected_tenant. If the candidate reaches portal DEV before the service release that carries AR-y-71, every ticket's Open report read is refused.",
  "evidence": [
   "investigation row IRPT_ANLREQ-D2-S51",
   "this seat's reads 2026-10-11T17:07:52Z: irpt-commentary-composition-read-lambda live CodeSha256 DbvBUxTG...Yo4=, LastModified 2026-10-11T16:41:35Z; its role's one inline policy grants dynamodb:GetItem on 2 resources, the requests table and the jobs table; irpt-status live is 6idtFvAm..., revision 6; portal origin/DEV is c3a03c24, its generated reason set holds REPORT_TICKET_MISMATCH (render/Page.tsx:99), and the round-7 portal candidate 5f64f409b0 is still not an ancestor of DEV"
  ],
  "remedy": "The service release carrying AR-y-71 is live and read first; or the portal landing is gated on the live function's answer, not on a message.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v10",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v10"
  },
  "closed": false,
  "disarm": {
   "state": "ARMED",
   "owner": "1.0.0_SA_CTO~DELL2",
   "at": null
  }
 },
 {
  "id": "IRPT_ANLREQ-D2-W52-S5",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "For a ticket filed by the form nothing recorded the ticket's report reference, and the page's Open controls need it. The form's record step is on portal DEV and unexercised; the report-to-ticket binding is merged and not released.",
  "evidence": [
   "investigation row IRPT_ANLREQ-D2-W52-S5",
   "org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND9_Y_L8_COMPILE_20261011.md @70070b3a69 (msg 5416)"
  ],
  "remedy": "One real filing through the form is read end to end: the reference recorded on the ticket and the report opened from it.",
  "owner": "2.0.0_SA_COO~Y2",
  "round": "v10",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~Y2",
   "round": "v10"
  },
  "closed": false
 },
 {
  "id": "IRPT_ANLREQ-S1",
  "project": "IRPT_ANLREQ",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The packager secret opal/ticketing/svc-irpt-packager is readable by user/Andrew_Berman, the identity every agent session on the laptop runs as, so 'no agent can read it' holds for fleet roles and not for a laptop agent session.",
  "evidence": [
   "investigation row IRPT_ANLREQ-S1"
  ],
  "remedy": "The CTO rules whether a laptop agent session may read the packager's secret, and the pair's sentence 'no agent can read it' is corrected to what holds.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v10",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v10"
  },
  "closed": false
 }
]
```
