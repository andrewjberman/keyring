# IRPT_ANLREQ: remediations, round 17 (workstream Y)

<sweep_watermark>2026-10-12T23:44Z</sweep_watermark>

Slug by `3.0.0_SA_CVO` (seated on dell2), 2026-10-12T23:44:00Z. Follows ADJUDICATION_v18. L8 input: `org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND17_Y_L8_COMPILE_20261012.md` (msg 6673). L9: `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ANLREQ_ROUND_17_L9_GRADE_20261012.md`.
Graduated, round label v18: 5 rows, OPEN; ARMED 2 (D2-W52-S24, D2-W52-S29; neither reachable live, the reader is unreleased).
For the CTO: the D2-W52-S24 ruling gates the reader's release pair (this seat's L9 condition); D2-W52-S25 (dell2's client-data gate is
blind) is routed through you to the box owner. Also from the packet, owed and not rows: the status rule's never-widen pair must say
the no-row population is UNKNOWN until `served.py` logs the caller, and narrative's pinned `served.py` (row D2-W54-S5) is yours.

```json
[
 {
  "id": "IRPT_ANLREQ-D2-W52-S24",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "The repaired rule admits a modifier only from custodian, client, sub, or no. of, and an identifier tail only from a closed word list. Brokerage Account, Subaccount, Account Seq and Account Sequence name accounts and are not matched, so a multi-account file under one of them passes as one account. The leading-word rule before the repair missed them too, so this is not a regression.",
  "evidence": [
   "investigation row D2-W52-S24",
   "org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND17_Y_L8_COMPILE_20261012.md",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ANLREQ_ROUND_17_L9_GRADE_20261012.md"
  ],
  "remedy": "The CTO rules before the re-landed reader's release pair is cut (this seat's L9 condition on AR171-y-AC3J): widen the closed vocabulary (brokerage, ira, joint as modifiers; subaccount as an account word; seq and sequence as identifier words), each with a census line and a negative control, or carry the gap into the pair as a stated limit. Also decide `No. of Accounts`, which matches today although it names a count.",
  "owner": "2.0.0_SA_COO~Y2",
  "round": "v18",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~Y2",
   "round": "v18"
  },
  "closed": false,
  "disarm": {
   "state": "ARMED",
   "owner": "2.0.0_SA_COO~Y2",
   "at": null
  }
 },
 {
  "id": "IRPT_ANLREQ-D2-W52-S29",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "Under the repaired reader, a two-account Account-Number sheet that the round-16 door stored answers NORMALIZED on a same-token re-POST, while a fresh-token POST of the same bytes is turned back with ACCOUNT_COLUMN_SEVERAL_VALUES. A stored normalization row is answered without judging the file again.",
  "evidence": [
   "investigation row D2-W52-S29",
   "org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND17_Y_L8_COMPILE_20261012.md"
  ],
  "remedy": "Before the release: count the round-16 inputs stored as NORMALIZED that the repaired reader would turn back (a two-account Account-Number sheet), and disposition each, because a same-token re-POST returns the stored NORMALIZED.",
  "owner": "2.0.0_SA_COO~Y2",
  "round": "v18",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~Y2",
   "round": "v18"
  },
  "closed": false,
  "disarm": {
   "state": "ARMED",
   "owner": "2.0.0_SA_COO~Y2",
   "at": null
  }
 },
 {
  "id": "IRPT_ANLREQ-D2-W52-S28",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The source map pins irpt-ycharts-generate's template_reader.py at 3f29017cfc and its uploads.py at f09b802cdc, both before the AR-y-142 and AR-y-162 changes. The 3f29017cfc reader writes no reader_version member. So the Lambda's reader is neither the round-16 reader (aaf156e8eb) that the trace calls old, nor the repaired one; the four traced pairs do not cover the Lambda as it is pinned today.",
  "evidence": [
   "investigation row D2-W52-S28",
   "org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND17_Y_L8_COMPILE_20261012.md",
   "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ANLREQ_ROUND_17_L9_GRADE_20261012.md"
  ],
  "remedy": "The Lambda carries a third, unversioned reader (template_reader.py at 3f29017cfc, no reader_version member). The release pair runs that case beside the four pairs of AR-y-174, and the resident and the Lambda move together to one pinned reader.",
  "owner": "2.0.0_SA_COO~Y2",
  "round": "v18",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~Y2",
   "round": "v18"
  },
  "closed": false
 },
 {
  "id": "IRPT_ANLREQ-D2-W54-S7",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "AMENDMENT 2 bite check: with the principal identity comparison disabled, the actor and renderer arms of test_final_release_refuses_changed_actor_owner_or_service_identity still PASS, because a second identity comparison refuses them after compute; only the owner arms fail under their named comparison",
  "evidence": [
   "investigation row D2-W54-S7",
   "org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND17_Y_L8_COMPILE_20261012.md"
  ],
  "remedy": "With the principal re-resolution disabled, the actor and renderer arms of test_final_release_refuses_changed_actor_owner_or_service_identity still pass on a second comparison, so they do not bite on the check they name. A test cell makes each arm fail when its named check alone is removed.",
  "owner": "2.0.0_SA_COO~Y2",
  "round": "v18",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~Y2",
   "round": "v18"
  },
  "closed": false
 },
 {
  "id": "IRPT_ANLREQ-D2-W52-S25",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "Every safe-commit of this order printed 'client-data-check: hashed account-id list ABSENT ... this commit was NOT checked for client account ids'. The commits carry synthetic labels only (ACCT-ONE, ACCT-TWO, Client Acct No.). The gate's client-account read is therefore not evidence for these commits.",
  "evidence": [
   "investigation row D2-W52-S25",
   "org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND17_Y_L8_COMPILE_20261012.md"
  ],
  "remedy": "On dell2 every safe-commit prints 'client-data-check: hashed account-id list ABSENT ... this commit was NOT checked for client account ids' (this seat's commits print it too). The box's client-data gate is blind until the list is placed or OPAL_ACCOUNT_ID_HASHES is set. Routed to the box owner through the CTO.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v18",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v18"
  },
  "closed": false
 }
]
```
