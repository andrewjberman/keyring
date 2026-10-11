# IRPT_ANLREQ: remediations, round 3 (workstream Y)

<sweep_watermark>2026-10-11T09:50Z</sweep_watermark>

Slug by `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T09:50:52Z. Inputs: msgs 4564, 4571, 4612. Read: `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ANLREQ_ROUND_3_Y_L9_READ_20261011.md`.
Graduated, round label v4: 7 rows, OPEN, INERT. No judgment criterion this round.

**For the CTO's analysis:**
1. **Nothing built this round is live.** Release 5 waits on your half of the pair. The re-pin changes 14 of 49 members against live;
   two of the eleven censused inert were judged by reading only.
2. **The history page can be refused by one bad row** once release 5 serves it (row D2-W52-S4).
3. **The packager cannot read the ticket** (row D2-W66-S1, BLOCKING): release 4's attach is not idempotent as built.

```json
[
 {
  "id": "IRPT_ANLREQ-D2-W66-S1",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "The ticket service refuses the packager's service principal the ticket read (403), so the packager's idempotence read cannot succeed live and the attach cannot be idempotent as built.",
  "evidence": [
   "investigation row IRPT_ANLREQ-D2-W66-S1",
   "org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND3_Y_L8_COMPILE_ADDENDUM_1_20261011.md @81b38e28a5 (msg 4612)"
  ],
  "remedy": "The ticket service admits that read for the packager, or the packager proves idempotence another way. It crosses into TCKT_VNEXT; the CTO places it.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v4",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v4"
  },
  "closed": false
 },
 {
  "id": "IRPT_ANLREQ-D2-W52-S4",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "With the client stated on every history row, the history page reads the selection from every row's retained composition; one composition naming no selection refuses the whole page.",
  "evidence": [
   "investigation row IRPT_ANLREQ-D2-W52-S4",
   "org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND3_Y_L8_COMPILE_ADDENDUM_1_20261011.md @81b38e28a5 (msg 4612)"
  ],
  "remedy": "A test with one bad row among good ones, and a decision: skip-and-mark the row, or refuse the page. Before release 5 serves it.",
  "owner": "2.0.0_SA_COO~Y2",
  "round": "v4",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~Y2",
   "round": "v4"
  },
  "closed": false
 },
 {
  "id": "IRPT_ANLREQ-D2-W52-S3",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The schema edits of cell AR-y-32 have three consequences the release must carry, one in a contract file outside the cell's paths.",
  "evidence": [
   "investigation row IRPT_ANLREQ-D2-W52-S3",
   "org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND3_Y_L8_COMPILE_ADDENDUM_1_20261011.md @81b38e28a5 (msg 4612)"
  ],
  "remedy": "The release 5 pair names all three.",
  "owner": "2.0.0_SA_COO~Y2",
  "round": "v4",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~Y2",
   "round": "v4"
  },
  "closed": false
 },
 {
  "id": "IRPT_ANLREQ-D2-S33",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The source map's irpt-status entry still carries deploy fields describing 2026-10-05 (deployed_code_sha256, last_deployed_commit, last_deployed_at); read again by this seat after the re-pin.",
  "evidence": [
   "investigation row IRPT_ANLREQ-D2-S33",
   "org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND3_Y_L8_COMPILE_ADDENDUM_1_20261011.md @81b38e28a5 (msg 4612)"
  ],
  "remedy": "The release 5 apply records them, or they are corrected to the live revision by their recorder.",
  "owner": "2.0.0_SA_COO~Y2",
  "round": "v4",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~Y2",
   "round": "v4"
  },
  "closed": false
 },
 {
  "id": "IRPT_ANLREQ-D2-S34",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "Two of the 17 investor-reporting functions do not build from the source map with no skip flag.",
  "evidence": [
   "investigation row IRPT_ANLREQ-D2-S34",
   "org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND3_Y_L8_COMPILE_ADDENDUM_1_20261011.md @81b38e28a5 (msg 4612)"
  ],
  "remedy": "Each is made to build, or carries a stated reason and an owner.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v4",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v4"
  },
  "closed": false
 },
 {
  "id": "IRPT_ANLREQ-D2-S35",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "Queued by CTO ruling: two empty members of persist_inputs.report_index in the owned request schema get a type.",
  "evidence": [
   "investigation row IRPT_ANLREQ-D2-S35",
   "org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND3_Y_L8_COMPILE_ADDENDUM_1_20261011.md @81b38e28a5 (msg 4612)"
  ],
  "remedy": "The next cell of this workstream.",
  "owner": "2.0.0_SA_COO~Y2",
  "round": "v4",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~Y2",
   "round": "v4"
  },
  "closed": false
 },
 {
  "id": "IRPT_ANLREQ-D2-S38",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The ticket's opened report prints a decimal fraction beside the unit 'percent' on a fixture render (0.0712 percent). Whether a served section has that shape is not read.",
  "evidence": [
   "investigation row IRPT_ANLREQ-D2-S38",
   "org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND3_Y_L8_COMPILE_ADDENDUM_1_20261011.md @81b38e28a5 (msg 4612)"
  ],
  "remedy": "Read one served report's section: its unit and whether the value is a fraction. Then the page formats it, or the fixture is corrected.",
  "owner": "2.0.0_SA_COO~Y2",
  "round": "v4",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~Y2",
   "round": "v4"
  },
  "closed": false
 }
]
```
