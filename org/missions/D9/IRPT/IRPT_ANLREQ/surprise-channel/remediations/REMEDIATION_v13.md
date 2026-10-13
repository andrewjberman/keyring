# IRPT_ANLREQ: remediations, round 20 (workstreams Y and YR)

<sweep_watermark>2026-10-13T14:32Z</sweep_watermark>

Slug by `3.0.0_SA_CVO` (seated on dell2), 2026-10-13T14:32:00Z. Follows ADJUDICATION_v21. L8 input: `org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND20_Y_L8_COMPILE_20261013.md` (msg 6974). L9: `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ANLREQ_ROUND_20_L9_GRADE_20261013.md`.
Graduated, round label v21: 6 rows, OPEN; ARMED 2 (D2-W64-S6, D2-W61-S2).
- D2-S73 carries the AR211-y-AC3J FAIL: an allowlist (with alias and primary) before the r19.2 release, or a stated limit.
- For the CTO: D2-S71 (the CI script's false UPLOAD NOT VERIFIED), D2-W65-S4 (the rule's reach to no-selection callers through narrative).
Still ARMED where they stand: D2-W52-S33 and -S36 (released, not shown live), D2-W55-S5 (P2), D2-W55-S1 (the caller-class line's limits).

```json
[
 {
  "id": "IRPT_ANLREQ-D2-S73",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "L9 AR211-y-AC3J FAILS clause 1: the r19.2 backstop still turns back one-account files whose abbreviated attribute header is not on its 17-word blocklist -- Acct Cost Basis and Acct Gain with 8-digit integers (the same class as the closed Acct Market Value case), and Acct Weight, Description, Currency and Custodian with letter-and-digit values.",
  "evidence": [
   "investigation row D2-S73",
   "org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND20_Y_L8_COMPILE_20261013.md",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ANLREQ_ROUND_20_L9_GRADE_20261013.md"
  ],
  "remedy": "Before the r19.2 release: replace the attribute blocklist with an allowlist (a root header enters the backstop only when its other words are identifier-tail words), adding alias to the tails and primary to the modifiers, with Acct Cost Basis and Acct Gain among the negative controls; or the CTO records the blocklist's gap as a stated limit in the release pair.",
  "owner": "2.0.0_SA_COO~Y2",
  "round": "v21",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~Y2",
   "round": "v21"
  },
  "closed": false
 },
 {
  "id": "IRPT_ANLREQ-D2-W64-S6",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "Instrument trap: BUILD_ONLY=1 is honoured only by builders at or after the commit that added the guard, so a holds-only build run from an older base commit uploads for real; and the y213-rebase check reads tests.failed but not tests.errors",
  "evidence": [
   "investigation row D2-W64-S6",
   "org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND20_Y_L8_COMPILE_20261013.md"
  ],
  "remedy": "BUILD_ONLY is honoured only by builders at or after the guard commit, so a holds-only build from an older base uploads for real. Every face that copies a BUILD_ONLY instruction checks that the guard exists at its base (the issuer's mitigation), and the CTO adds the rule to the rebase-cell pattern.",
  "owner": "2.0.0_SA_COO~Y2",
  "round": "v21",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~Y2",
   "round": "v21"
  },
  "closed": false,
  "disarm": {
   "state": "ARMED",
   "owner": "2.0.0_SA_COO~Y2",
   "at": null
  }
 },
 {
  "id": "IRPT_ANLREQ-D2-S71",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "At bases e274a0e60c, 5d8b0390ed and 4067c2dd5b, `build-and-upload.sh` (without BUILD_ONLY) prints `ERROR: UPLOAD NOT VERIFIED` and exits 1 for all eight R20 packagers on this box although each new object version is in S3 with the right size and content-sha256 metadata: its own `aws s3api head-object --query` verify call dies with `'int' object has no attribute 'items'` (the CLI on its PATH), the script reads that error text as the head-object result, and the source map is not updated.",
  "evidence": [
   "investigation row D2-S71",
   "org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND20_Y_L8_COMPILE_20261013.md"
  ],
  "remedy": "On dell2, build-and-upload.sh without BUILD_ONLY prints UPLOAD NOT VERIFIED and exits 1 after a good upload (its verify call dies in the CLI and is read as the head-object result), and it does not update the source map. Route to the owner of infra/aws/lambda/ci/build-and-upload.sh.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v21",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v21"
  },
  "closed": false
 },
 {
  "id": "IRPT_ANLREQ-D2-W61-S2",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "The three group-A functions' live CodeSha256 values equal their map artifact_sha256 but not their map deployed_code_sha256 fields; the act-4 ledger's performance-adapter value is not the live one",
  "evidence": [
   "investigation row D2-W61-S2",
   "org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND20_Y_L8_COMPILE_20261013.md"
  ],
  "remedy": "The group-A functions' live CodeSha256 equals the map's artifact_sha256 but not its deployed_code_sha256 fields. Advance deployed_code_sha256 to the live values so no later act reads the stale field as live.",
  "owner": "2.0.0_SA_COO~Y2",
  "round": "v21",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~Y2",
   "round": "v21"
  },
  "closed": false,
  "disarm": {
   "state": "ARMED",
   "owner": "2.0.0_SA_COO~Y2",
   "at": null
  }
 },
 {
  "id": "IRPT_ANLREQ-D2-W63-S3",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The TicketCenter filing path still files a ticket on a NORMALIZED answer with no SHEETS_NOT_READ words shown: the AR-y-214 candidate shows the notice on the upload step only, its granted scope.",
  "evidence": [
   "investigation row D2-W63-S3",
   "org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND20_Y_L8_COMPILE_20261013.md"
  ],
  "remedy": "The TicketCenter filing path still files a ticket on a NORMALIZED answer with no SHEETS_NOT_READ words shown; AR-y-214 shows the notice on the upload step only. A portal cell shows it on the filing path too.",
  "owner": "2.0.0_SA_COO~Y2",
  "round": "v21",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~Y2",
   "round": "v21"
  },
  "closed": false
 },
 {
  "id": "IRPT_ANLREQ-D2-W65-S4",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The status rule also reaches a no-selection internal caller through narrative's entry: a row without status makes narrative hand roster None (class UNKNOWN), although the reader is documented to run only on a cross-firm selection",
  "evidence": [
   "investigation row D2-W65-S4",
   "org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND20_Y_L8_COMPILE_20261013.md"
  ],
  "remedy": "The status rule also reaches a NO-selection internal caller through narrative's entry (a users row without status makes roster None, class UNKNOWN; fail-closed). None of the 23 internal rows lacks a status, so nothing moves today. Rule whether that reach is intended, since the pair fenced only another-firm selection.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v21",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v21"
  },
  "closed": false
 }
]
```
