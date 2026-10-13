# IRPT_ANLREQ: remediations, round 18 (workstream Y)

<sweep_watermark>2026-10-13T01:24Z</sweep_watermark>

Slug by `3.0.0_SA_CVO` (seated on dell2), 2026-10-13T01:24:00Z. Follows ADJUDICATION_v19. L8 input: `org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND18_Y_L8_COMPILE_20261013.md` (msg 6720). L9: `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ANLREQ_ROUND_18_L9_GRADE_20261013.md`.
Graduated, round label v19: 6 rows, OPEN; ARMED 5.
**LIVE today:** D2-W52-S33. The deployed irpt-ycharts-generate reader (3f29017cfc) holds a two-account or total-row template upload as one
portfolio; only the reader's release pair disarms it. For the CTO: D2-W54-S5 (the status pair's eight packagers), D2-W52-S32 (the COUNT
exclusion), and the ruling on D2-W52-S31.

```json
[
 {
  "id": "IRPT_ANLREQ-D2-W54-S5",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "The narrative test file reports 13 passed after the reader change, but it runs the PINNED served.py (staged_from pin 361c44fa9d), not the worktree file, so its green run says nothing about AR-y-172 on narrative",
  "evidence": [
   "investigation row D2-W54-S5",
   "org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND18_Y_L8_COMPILE_20261013.md",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ANLREQ_ROUND_18_L9_GRADE_20261013.md"
  ],
  "remedy": "The status rule's release pair moves ONE served.py that carries the rule into all eight packagers, the two pin groups (361c44fa9d: performance-adapter, narrative, status; 74a62fb46c: the other five) together, and narrative's test staging to the new pin, so narrative's suite tests the rule it ships (AR-y-185's record). Disarmed when that pair's live reads show the rule on all eight.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v19",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v19"
  },
  "closed": false,
  "disarm": {
   "state": "ARMED",
   "owner": "1.0.0_SA_CTO~DELL2",
   "at": null
  }
 },
 {
  "id": "IRPT_ANLREQ-D2-W55-S1",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "A call whose profile lookup raises, or whose selected firm is outside the bucket registry, has no users-row class, so the AR-y-184 line is not printed for it. The cell's once-per-call reading is not met for those calls, and a census must read them from the answer, not from the line.",
  "evidence": [
   "investigation row D2-W55-S1",
   "org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND18_Y_L8_COMPILE_20261013.md",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ANLREQ_ROUND_18_L9_GRADE_20261013.md"
  ],
  "remedy": "The status rule's pair states the caller-class line's two limits: a lookup exception or an unregistered firm prints no line (those callers are counted from FIRM_BINDING answers), and outcome= is the selection gate's verdict, not the final answer (row W55-S3 folds in).",
  "owner": "2.0.0_SA_COO~Y2",
  "round": "v19",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~Y2",
   "round": "v19"
  },
  "closed": false
 },
 {
  "id": "IRPT_ANLREQ-D2-W52-S31",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "After the AR-y-181 widening, the rule still does not match identifier-like headers whose spelling sits outside the ruled vocabulary: Account Numbers (plural tail), Subaccounts (plural account word), Accnt, Account Nos, Account Seqno and Account Serial. A multi-account file under one of them passes as one account, the same costly direction as S24.",
  "evidence": [
   "investigation row D2-W52-S31",
   "org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND18_Y_L8_COMPILE_20261013.md",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ANLREQ_ROUND_18_L9_GRADE_20261013.md"
  ],
  "remedy": "The CTO rules: widen again (Account Numbers, Subaccounts, Accnt, Account Nos, Seqno, Roth IRA Account, Trust Account, each with a census line and a negative control) or carry the spellings into the reader's pair as a stated limit. Unreleased.",
  "owner": "2.0.0_SA_COO~Y2",
  "round": "v19",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~Y2",
   "round": "v19"
  },
  "closed": false,
  "disarm": {
   "state": "ARMED",
   "owner": "2.0.0_SA_COO~Y2",
   "at": null
  }
 },
 {
  "id": "IRPT_ANLREQ-D2-W52-S32",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "The whole-cell exclusion for No. of Accounts (plural) reads only the header words, not the values. A file whose column is headed No. of Accounts but holds account identifiers, not one count, is not turned back, so a multi-account file under that header passes as one account.",
  "evidence": [
   "investigation row D2-W52-S32",
   "org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND18_Y_L8_COMPILE_20261013.md",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ANLREQ_ROUND_18_L9_GRADE_20261013.md"
  ],
  "remedy": "The COUNT exclusion matches header words only. This seat's L9 judgment: a column headed exactly 'No. of Accounts' that holds account numbers is not a plausible export. If the CTO wants it closed, the cheap test is on values (a count column holds one small integer). Otherwise carry it as a stated limit.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v19",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v19"
  },
  "closed": false,
  "disarm": {
   "state": "ARMED",
   "owner": "1.0.0_SA_CTO~DELL2",
   "at": null
  }
 },
 {
  "id": "IRPT_ANLREQ-D2-W52-S33",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "The Lambda's pinned reader (template_reader.py at 3f29017cfc) has no account check and no total-row check. Reader-level, in process: it returns no finding on the two-account sheets or on the total-row sheet, so the file's rows are held with the account column ignored, and the total row is held as a holding named TOTAL.",
  "evidence": [
   "investigation row D2-W52-S33",
   "org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND18_Y_L8_COMPILE_20261013.md",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ANLREQ_ROUND_18_L9_GRADE_20261013.md"
  ],
  "remedy": "LIVE today: irpt-ycharts-generate carries template_reader.py at 3f29017cfc, which has no account check and no total-row check, so a two-account or total-row template upload through the Lambda's door is held as one portfolio. Disarmed by the reader's release pair: uploads.py and template_reader.py move in ONE deploy to HEAD and r18.1 together with the resident (single-file moves fail as measured, row W52-S34 folds in), after the pinned pair is RUN in a scratch tree (this seat's AR186 condition).",
  "owner": "2.0.0_SA_COO~Y2",
  "round": "v19",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~Y2",
   "round": "v19"
  },
  "closed": false,
  "disarm": {
   "state": "ARMED",
   "owner": "2.0.0_SA_COO~Y2",
   "at": null
  }
 },
 {
  "id": "IRPT_ANLREQ-D2-W52-S35",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "Under the r18.1 read_input gate a template stored by the pinned reader is accepted unchanged on re-open, because a template with no reader_version member is not compared. A multi-account file the pinned reader stored as one account's rows therefore stays accepted on re-open after the widening, with no re-read.",
  "evidence": [
   "investigation row D2-W52-S35",
   "org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND18_Y_L8_COMPILE_20261013.md",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ANLREQ_ROUND_18_L9_GRADE_20261013.md"
  ],
  "remedy": "Under r18.1 a template stored by the pinned reader is accepted unchanged on re-open (computed, not run). TO-READS-Y9 measured 0 of 56 stored inputs turned back by the widened reader, so no stored input is affected today. The release pair re-counts the stored templates written between this count and the deploy, and runs the re-open of a pinned-stored template in the scratch tree of the pinned pair.",
  "owner": "2.0.0_SA_COO~Y2",
  "round": "v19",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~Y2",
   "round": "v19"
  },
  "closed": false,
  "disarm": {
   "state": "ARMED",
   "owner": "2.0.0_SA_COO~Y2",
   "at": null
  }
 }
]
```
