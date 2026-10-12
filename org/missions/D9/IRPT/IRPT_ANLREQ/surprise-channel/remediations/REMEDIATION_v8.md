# IRPT_ANLREQ: remediations, rounds 14 and 15 (workstream Y)

<sweep_watermark>2026-10-11T23:37Z</sweep_watermark>

Slug by `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T23:37:38Z. Input: `org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND14_Y_L8_COMPILE_20261011.md @73dd169157 (msg 6114)`.
Graduated, round label v16: 4 rows, OPEN, INERT.

**For the CTO's analysis:**
1. **Two things to fix before the upload check is re-landed** (row D2-S64, this seat's; grade file `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ANLREQ_ROUNDS_14_15_Y_L9_GRADE_20261011.md`): the account-word list misses
   common header forms, `account #` among them, and was checked against fixtures that hold no account column; and the
   repeated-header words tell a person to split what may be one account.
2. **The re-land is first a contract choice,** yours by msg 6054: a stored input is compared on its holdings alone, or carries the
   reader's version. This seat printed the line: today the re-read must EQUAL what was stored.
3. **The census was the last cell and should have been the first.** The issuer names it as its own defect. Nothing was released.
4. **Four unpinned members of the generate function differ from live and ship on any rebuild** (row D2-W53-S9).
5. The form's re-post is on portal DEV and works against today's service; how long the check takes against the form's wait is
   not measured.

```json
[
 {
  "id": "IRPT_ANLREQ-D2-S64",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "L9 rounds 14 and 15: AR142-y-AC3J NOT MET as written, AR144-y-AC2J MET for the form's half, AR145-y-AC2J MET. The account-word list is incomplete: it matches 'acct #' and not 'account #', and its subtraction ran over 13 fixture files none of which has an account column, so it proves nothing about the class. The repeated-header finding's words tell a person to split what may be one account into two files. The build is reverted, so both are fixed before the re-land. The census found the unsafe re-read of stored inputs, after the merges.",
  "evidence": [
   "investigation row IRPT_ANLREQ-D2-S64",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ANLREQ_ROUNDS_14_15_Y_L9_GRADE_20261011.md"
  ],
  "remedy": "Before the re-land: the account-word list is built from header forms seen in real use, or the match is loosened with the named exclusions kept, under a subtraction whose population holds account columns; and the repeated-header words say what is seen and ask, without telling a person to split the file.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v16",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v16"
  },
  "closed": false
 },
 {
  "id": "IRPT_ANLREQ-D2-W53-S7",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "TO-AR-y-145: the CTO ruling (round 14 item 5) says the accepted answer carries one line saying only the first sheet was read. The line is stored in portfolio.findings and portfolio.template.findings of the NORMALIZED answer (measured in process). Every portal reader of the door's answer reads findings only for NEEDS_CORRECTION or RESOLVING (TicketCenter/analysisRequest.ts PROD :103,:110, DEV :165,:175,:180; ProspectComposer.tsx PROD :447, DEV :459), so a person sees no new line on an accepted sheet at either trunk.",
  "evidence": [
   "investigation row IRPT_ANLREQ-D2-W53-S7",
   "org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND14_Y_L8_COMPILE_20261011.md @73dd169157 (msg 6114)"
  ],
  "remedy": "The accepted answer's first-sheet line is shown by the page that shows the accepted answer, or the ruling that asked for it is met another way.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v16",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v16"
  },
  "closed": false
 },
 {
  "id": "IRPT_ANLREQ-D2-W53-S8",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "TO-AR-y-145: template_reader.WORDS['TOTAL_ROW_PRESENT'] and ['HEADER_ROW_REPEATED'] begin 'Row {row} ...' (template_reader.py:36-47); the forms prefix 'Row N: ' when the finding has a row (TicketCenter/analysisRequest.ts PROD :77-78, DEV :101; ProspectComposer.tsx PROD :454-455). A person sees 'Row 4: Row 4 is a total, not a holding. ...'.",
  "evidence": [
   "investigation row IRPT_ANLREQ-D2-W53-S8",
   "org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND14_Y_L8_COMPILE_20261011.md @73dd169157 (msg 6114)"
  ],
  "remedy": "The finding's words and the form's prefix are reconciled so a person reads the row once.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v16",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v16"
  },
  "closed": false
 },
 {
  "id": "IRPT_ANLREQ-D2-W53-S9",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "TO-AR-y-145: the BUILD_ONLY build of irpt-ycharts-generate (sha256 u0YnPLPQ2E08RFAbiDHxCErVhW5NLCpz9qZ9JZ3bKHY=) differs from the live package (tdpterTMfJlWXjnoAQCwil+wN/Jf8Q/yLjGxTk7yUkk=) in four members that are native to ycharts/generate and unpinned: acceptance.py and submission.py (IB-pr-455, 74bbdbb322), submission_service.py (AR-y-37, 2f7cc7be42), durable_job.py (TO-AR-g-21, 3acafb3f45). The re-pin of uploads.py and template_reader.py the release needs adds two more, so the release moves six members unless the other four are pinned to the live bytes.",
  "evidence": [
   "investigation row IRPT_ANLREQ-D2-W53-S9",
   "org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND14_Y_L8_COMPILE_20261011.md @73dd169157 (msg 6114)"
  ],
  "remedy": "The four unpinned members of the generate function are pinned, or its next release is cut knowing it ships them; a rebuild is not made by accident.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v16",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v16"
  },
  "closed": false
 }
]
```
