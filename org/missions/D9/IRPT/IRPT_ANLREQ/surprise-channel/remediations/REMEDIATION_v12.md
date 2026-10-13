# IRPT_ANLREQ: remediations, round 19 (workstreams Y and YR)

<sweep_watermark>2026-10-13T07:14Z</sweep_watermark>

Slug by `3.0.0_SA_CVO` (seated on dell2), 2026-10-13T07:14:00Z. Follows ADJUDICATION_v20. L8 input: `org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND19_Y_L8_COMPILE_20261013.md` (msg 6836). L9: `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ANLREQ_ROUND_19_L9_GRADE_20261013.md`.
Graduated, round label v20: 6 rows, OPEN; ARMED 3 (D2-W52-S36, D2-W55-S5, D2-W55-S25).
- D2-W59-S1 carries the AR194-y-AC4J FAIL: repair the backstop before the r19.1 release.
- D2-W58-S4 (CTO): the PROD ticket page shows a raw reason code; client-facing, so Andrew's word for a PROD push.
- D2-W52-S36: RELEASED, NOT SHOWN LIVE until Andrew's staff act uploads the two synthetic files.

```json
[
 {
  "id": "IRPT_ANLREQ-D2-W59-S1",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "AR-y-194 says No. of Accounts is excluded ONLY when its values are counts; the existing r18 test holds name values under that header and expects no finding, so the built rule reads it as: excluded unless its values are identifier-like.",
  "evidence": [
   "investigation row D2-W59-S1",
   "org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND19_Y_L8_COMPILE_20261013.md",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ANLREQ_ROUND_19_L9_GRADE_20261013.md"
  ],
  "remedy": "Carries this seat's L9 FAIL of AR194-y-AC4J: the r19.1 backstop turns back a one-account file whose abbreviated attribute header (Acct Market Value, Acct CUSIP, Acct Lot) holds two distinct 8+-digit integers or letter-and-digit tokens. Before the r19.1 release: a root header enters the backstop only when its other words are identifier tail words, and a digits-only run is admitted only where no value in the column carries a decimal point or separator. Built, not released.",
  "owner": "2.0.0_SA_COO~Y2",
  "round": "v20",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~Y2",
   "round": "v20"
  },
  "closed": false
 },
 {
  "id": "IRPT_ANLREQ-D2-W52-S36",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "Run in a scratch tree on the Lambda's pinned pair (uploads f09b802cdc, reader 3f29017cfc), the door answers NORMALIZED with no finding and total_dollars 600 on total_row_sheet: the file's TOTAL row is held as a holding and counted into the total (AAA 100, BBB 200, TOTAL 300).",
  "evidence": [
   "investigation row D2-W52-S36",
   "org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND19_Y_L8_COMPILE_20261013.md",
   "this seat's live read 2026-10-13T07:06Z: irpt-ycharts-generate CodeSha256 bNPCG2Oe1oQM/ztjggmrdDbdl83CAmUEcPnBFxlj2Rk= (06:27:22Z, Successful); since 06:27Z Traceback 0, ImportError 0, TypeError 0, 1 invocation"
  ],
  "remedy": "RELEASED, NOT SHOWN LIVE: the moved pair is live (this seat's digest read). Disarms on a live D1/D2, the two synthetic files Andrew's staff act dell2-20261012T222152Z-2e30 uploads on portal DEV in 49financial, with the door answering NEEDS_CORRECTION for both.",
  "owner": "2.0.0_SA_COO~Y2",
  "round": "v20",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~Y2",
   "round": "v20"
  },
  "closed": false,
  "disarm": {
   "state": "ARMED",
   "owner": "2.0.0_SA_COO~Y2",
   "at": null
  }
 },
 {
  "id": "IRPT_ANLREQ-D2-W55-S5",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "mechanism": "The W328-S1 repair (IB-pr-477, a stored-bundle probe whose reply is a WAF challenge ends the run without a second sign-in) is in infra/aws/ec2/investor-reporting-ycharts/ycharts_session.js at 069b8f797e. That file is not a member of either builder tarball, so a release built with the same arguments does not carry the repair, and the LIBRARY_SHA256 argument still names the old library a1c288.",
  "evidence": [
   "investigation row D2-W55-S5",
   "org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND19_Y_L8_COMPILE_20261013.md"
  ],
  "remedy": "This release did not move the host capture library (host library = bindings library = a1c28801...), so the W328-S1 stored-bundle repair is not on the host. It rides IRPT_BCKEND's next resident release, owned by ~P2.",
  "owner": "2.0.0_SA_COO~P2",
  "round": "v20",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~P2",
   "round": "v20"
  },
  "closed": false,
  "disarm": {
   "state": "ARMED",
   "owner": "2.0.0_SA_COO~P2",
   "at": null
  }
 },
 {
  "id": "IRPT_ANLREQ-D2-W55-S25",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "mechanism": "A named reader test fails on the built package: the release uploads.py declares 24 correction words that the st32 ops/status.py does not, and the CTO's held-member ruling leaves ops/status.py at st32 bytes. AC1 is not met.",
  "evidence": [
   "investigation row D2-W55-S25",
   "org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND19_Y_L8_COMPILE_20261013.md"
  ],
  "remedy": "The deployed irpt-status status.py (sha256 cb3b2ea620...) carries 4 correction words and none of the 24 the release uploads.py declares, so for those codes its envelope adds no CORRECT action. Accepted as a named limit (msg 6778). Carried to irpt-status by the all-eight status pair.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v20",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v20"
  },
  "closed": false,
  "disarm": {
   "state": "ARMED",
   "owner": "1.0.0_SA_CTO~DELL2",
   "at": null
  }
 },
 {
  "id": "IRPT_ANLREQ-D2-W58-S4",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "For the BEFORE body of header_repeated_csv (AMOUNT_NOT_A_NUMBER with no description), the ticket path shows 'AMOUNT_NOT_A_NUMBER, row 3' at PROD 37aa1247 and 'One finding has no description; see details' at DEV 64980b4d.",
  "evidence": [
   "investigation row D2-W58-S4",
   "org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND19_Y_L8_COMPILE_20261013.md"
  ],
  "remedy": "PROD's ticket message shows the raw reason code TEMPLATE_FINDINGS where DEV shows words. The page is client-facing, so any PROD push waits on Andrew's word; the CTO places it.",
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
  "id": "IRPT_ANLREQ-D2-W57-S5",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "SHEETS_NOT_READ (NOTICE) is carried at portfolio.findings in the moved two_sheet_workbook answer; no non-test portal file reads portfolio.findings or notices at PROD or DEV, so no person is shown it.",
  "evidence": [
   "investigation row D2-W57-S5",
   "org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND19_Y_L8_COMPILE_20261013.md"
  ],
  "remedy": "SHEETS_NOT_READ (NOTICE) rides portfolio.findings in the stored answer, and no portal reader shows it, so a person whose workbook has another sheet is never told it was not read. A portal cell shows it.",
  "owner": "2.0.0_SA_COO~Y2",
  "round": "v20",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~Y2",
   "round": "v20"
  },
  "closed": false
 }
]
```
