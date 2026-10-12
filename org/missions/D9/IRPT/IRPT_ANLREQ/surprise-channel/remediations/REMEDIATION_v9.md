# IRPT_ANLREQ: remediations, round 16 (workstream Y)

<sweep_watermark>2026-10-12T22:22Z</sweep_watermark>

Slug by `3.0.0_SA_CVO` (seated on dell2), 2026-10-12T22:22:00Z. Follows ADJUDICATION_v17. L8 input: `org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND16_Y_L8_COMPILE_20261012.md` (msg 6633). L9: `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ANLREQ_ROUND_16_L9_GRADE_20261012.md`.
Graduated, round label v17: 3 rows, OPEN, owner `2.0.0_SA_COO~Y2`; ARMED 0 new (the project's 3 ARMED rows are unchanged and not this round's).
- D2-W52-S20 carries the L9 FAIL of AR162-y-AC3J: repair the account-header rule before the re-landed reader's release pair.
- D2-W52-S18: the mixed-version trace before that release.
- D2-W53-S10: the TCKT_VNEXT-D2-S48 cell from the AR-y-163 read.

```json
[
 {
  "id": "IRPT_ANLREQ-D2-W52-S20",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The face asks for account-header forms from real use. None is in the repository. The leading-word rule, checked over a constructed population of 50 forms, leaves nine account-identifier forms unmatched and matches five account-attribute forms it does not exclude.",
  "evidence": [
   "investigation row D2-W52-S20",
   "org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND16_Y_L8_COMPILE_20261012.md",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ANLREQ_ROUND_16_L9_GRADE_20261012.md"
  ],
  "remedy": "L9 grade AR162-y-AC3J FAILS on this row (this seat's grade record): the leading-word rule misses `Account-Number` and `Account/Number` because a header is not split on hyphen or slash, and it turns back `Account Value`, `Account Status` and `Account Opened`. Before the re-landed reader's release pair: split on hyphen and slash; add the measured attribute forms to the whole-cell exclusions, each with its reason; and state on the record whether a last-word match (`Client Account`, `Sub-Account`, `Custodian Acct`) is admitted.",
  "owner": "2.0.0_SA_COO~Y2",
  "round": "v17",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~Y2",
   "round": "v17"
  },
  "closed": false
 },
 {
  "id": "IRPT_ANLREQ-D2-W52-S18",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "Template acceptance ends in a read_input of the new input, and read_input imports READER_VERSION by name. A template_reader module without that constant breaks every acceptance, so the base-reader test sets a sentinel on the module it loads.",
  "evidence": [
   "investigation row D2-W52-S18",
   "org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND16_Y_L8_COMPILE_20261012.md"
  ],
  "remedy": "read_input imports READER_VERSION by name, so a template_reader module without it breaks every acceptance. The release pair of the re-landed reader traces the mixed-version case (a resident and a Lambda on different reader versions) before any release, as the packet's section 5 item 1 says.",
  "owner": "2.0.0_SA_COO~Y2",
  "round": "v17",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~Y2",
   "round": "v17"
  },
  "closed": false
 },
 {
  "id": "IRPT_ANLREQ-D2-W53-S10",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "AR-y-163: the order says the ticket contract reads a row's existence so a disabled row still admits a caller (CTO msg 6181); at this base the ticket service already refuses a row whose status is not exactly 'active' (TCKT_VNEXT R9-st1, 97d2d4bede), so 'the reader follows the ticket service' now has two readings, existence and status, and the proposed cell carries both.",
  "evidence": [
   "investigation row D2-W53-S10",
   "org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND16_Y_L8_COMPILE_20261012.md"
  ],
  "remedy": "The ticket service already refuses any users row whose status is not exactly 'active' (TCKT_VNEXT R9-st1), so CTO msg 6181's premise is out of date. Cut the cell for row TCKT_VNEXT-D2-S48 from the AR-y-163 read at the next issuance, on the CTO's rule.",
  "owner": "2.0.0_SA_COO~Y2",
  "round": "v17",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~Y2",
   "round": "v17"
  },
  "closed": false
 }
]
```
