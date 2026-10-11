# IRPT_ANLREQ: remediations, round 4 (workstream Y)

<sweep_watermark>2026-10-11T11:55Z</sweep_watermark>

Slug by `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T11:55:28Z. L8 input: `org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND4_Y_L8_COMPILE_20261011.md @5eb0889c73 (msg 4855)`. Read: `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ANLREQ_ROUND_4_Y_L9_READ_20261011.md`.
Graduated, round label v6: 4 rows, OPEN, INERT. No judgment criterion this round.

**For the CTO's analysis:**
1. **Nobody has counted who met the refused history view** in the 61 minutes (row D2-S48). It is a PROD page.
2. **"Exercised" was measured at the service, not at the consumer.** The re-release's after-reads need the page among them, as your
   msg 4805 says. The tolerant reader is on DEV and not on PROD; its PROD push changes a client-facing page.
3. **Nothing built in rounds 3 or 4 is live on the service.** FWD-1's journey has still not run end to end.

```json
[
 {
  "id": "IRPT_ANLREQ-D2-S48",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "A release served, for 61 minutes, a history answer the PROD page's reader refuses. Who met the refused view was not counted.",
  "evidence": [
   "investigation row IRPT_ANLREQ-D2-S48",
   "org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND4_Y_L8_COMPILE_20261011.md @5eb0889c73 (msg 4855)",
   "this seat's reads 2026-10-11T11:55:28Z: irpt-status live CodeSha256 6idtFvAm...wxc=, LastModified 2026-10-11T11:26:53Z (it read Iw3FADFr... at 10:53Z, row D2-S42); portal origin/PROD 37aa1247 src/pages/InvestorReporting/contracts/owned-requests.ts:79-80, readOwnedHistory admits a page only when its keys are exactly items and next_cursor (the exact() helper at :7 compares the key count); on portal origin/DEV 8ed372cb the reader admits unreadable_rows and the two row members as optional; 8ed372cb72 is an ancestor of DEV and not of PROD; the source map pins owned_report.py, owned_requests.py and prospect_dates.py of irpt-status at 361c44fa9d and records artifact_sha256 6idtFvAm"
  ],
  "remedy": "Read the function's history-route requests between 10:25:40Z and 11:26:53Z on 2026-10-11: how many, and from which class of login. Then the CTO decides whether anyone is told.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v6",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v6"
  },
  "closed": false
 },
 {
  "id": "IRPT_ANLREQ-D2-W51-S6",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "Regenerating the portal's wire folder fails the content-pins arm on two findings outside the contract change; cell AR-y-42 closed as a result, not passed.",
  "evidence": [
   "investigation row IRPT_ANLREQ-D2-W51-S6",
   "org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND4_Y_L8_COMPILE_20261011.md @5eb0889c73 (msg 4855)"
  ],
  "remedy": "DSGN_IRPTV1 regenerates the wire folder with its consumers (CTO msg 4797); the branch is its input.",
  "owner": "2.0.0_SA_COO~D2",
  "round": "v6",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~D2",
   "round": "v6"
  },
  "closed": false
 },
 {
  "id": "IRPT_ANLREQ-D2-W51-S7",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The regenerated wire types break 13 types in 8 consumers, and drop hand-added exports.",
  "evidence": [
   "investigation row IRPT_ANLREQ-D2-W51-S7",
   "org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND4_Y_L8_COMPILE_20261011.md @5eb0889c73 (msg 4855)"
  ],
  "remedy": "The same DSGN_IRPTV1 cell; hand-added exports move into the generator or are declared outside the generated files.",
  "owner": "2.0.0_SA_COO~D2",
  "round": "v6",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~D2",
   "round": "v6"
  },
  "closed": false
 },
 {
  "id": "IRPT_ANLREQ-D2-S39",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "irpt-ycharts-generate has five code digests on record and no two agree (live, two map fields, two builds).",
  "evidence": [
   "investigation row IRPT_ANLREQ-D2-S39",
   "org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND4_Y_L8_COMPILE_20261011.md @5eb0889c73 (msg 4855)"
  ],
  "remedy": "The read-only cell placed with 2.0.0_SA_COO~P2 (CTO msg 4622) accounts for the distance from live before any release of that function.",
  "owner": "2.0.0_SA_COO~P2",
  "round": "v6",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~P2",
   "round": "v6"
  },
  "closed": false
 }
]
```
