# COMM_ASSIST -- surprise channel, ADJUDICATION v11 (laptop) -- CA-e-1 L9, the INTERNAL flag

<sweep_watermark>2026-10-16T03:55Z</sweep_watermark>

**Author:** `3.0.0_SA_CVO~L` (laptop), 2026-10-16 ~03:5xZ, on `2.0.0_SA_COO~CA` msg 109578 (record
`org/tier1_exec/2.0.0_SA_COO~CA/ANDREW_DIRECT_20261016_024xZ_COMM_ASSIST_E1_TEST_MAIL_FROM_OPALBLOOMBERG.md` @b5e752b6f3).
The project stays parked at round 20; this grades one JUDGMENT clause of cell `CA-e-1` (decomp round 13: "the CVO grades
the INTERNAL flag on the text he receives") under PRD FWD-4 ACCEPT ("an Opal sender as internal").

**Result: CA-e-1 INTERNAL flag MET, claim INFERRED (not MEASURED).** The text Andrew got carried `Opal` on its flag line,
read from the deployed bytes and the live object's state; the SMS body itself is not retained anywhere this seat can read,
so the received text was not read directly. One OBSERVATION row (C-S21) records the grade; nothing graduates.

```json
[
 {
  "id": "COMM_ASSIST-C-S21",
  "project": "COMM_ASSIST",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO~L",
  "surfaced_at": "2026-10-16T03:55Z",
  "one_line": "CA-e-1 INTERNAL flag graded MET, claim INFERRED: the #M611 text sent 02:57:14Z for Andrew's opalbloomberg mail resolved firm=opal, and the deployed bytes render firm opal as 'Opal' on the flag line (negative control: alongside renders 'CLIENT alongside'). The SMS body is not retained, so the received text itself was not read.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "PRD FWD-4 ACCEPT: an Opal sender is flagged as internal; decomp round 13 cell CA-e-1: the CVO grades the INTERNAL flag on the text he receives.",
  "world_is": "Handler log 02:56:30Z-02:58:30Z: sms_sent parts=1 tag=M611, mail_considered ok=1. The M611 object's state row: mail_log[0] firm=opal domain=opalinvest.com; pending null. Deployed CodeSha256 gSq68yr2uV/DwTwAuhWRGzRJoSTo3fzU4mmeitNCpok= (LastModified 2026-10-15T09:18:48Z); its mail_requests.py is byte-identical to the working tree; its mail_parties.json marks opal role=internal; run from the extracted zip, internal_parties() = ['opal'] and _mail_text line 2 = 'Opal'. Not read: the text on Andrew's phone.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    ".tools/aws logs filter-log-events /aws/lambda/teams-global-chat-assist-handler-lambda, 2026-10-16 02:56:30Z-02:58:30Z",
    ".tools/aws dynamodb get-item teams-global-chat-assist-table #index#sms-tag/M611 and the object's state row, 2026-10-16T03:5xZ",
    ".tools/aws lambda get-function teams-global-chat-assist-handler-lambda (code zip extracted and exercised), 2026-10-16T03:5xZ",
    "org/tier1_exec/2.0.0_SA_COO~CA/ANDREW_DIRECT_20261016_024xZ_COMM_ASSIST_E1_TEST_MAIL_FROM_OPALBLOOMBERG.md @b5e752b6f3"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A record of a JUDGMENT grade against the served state; no defect."
 }
]
```

## Evidence (each read 2026-10-16 03:4xZ-03:5xZ)

1. **The send.** Handler log group `/aws/lambda/teams-global-chat-assist-handler-lambda`, 02:56:30Z-02:58:30Z, 10 events:
   `sms_sent parts=1 tag=M611`; `mail_considered ok=1 sender_domain=0 body_no_andrew=0`; `tenant mail.messages result=texted`.
2. **The firm resolved for that text.** `teams-global-chat-assist-table`, `#index#sms-tag` / `M611` -> the mail object;
   its `state` row's `mail_log[0]` reads `tag=M611 firm=opal domain=opalinvest.com considered_at=2026-10-16T02:57:14Z`.
   `pending` is null and `pending_list` empty (the item has been acted on), so the stored text is gone.
3. **The flag rule, on the deployed bytes.** `get-function` CodeSha256 `gSq68yr2uV/DwTwAuhWRGzRJoSTo3fzU4mmeitNCpok=`,
   LastModified 2026-10-15T09:18:48Z (before the send). In the zip, `data/transcripts/scripts/teams_chat/mail_requests.py` is
   byte-identical to the working-tree source; `flag = "Opal" if item.get("internal") else "CLIENT <firm>"` and
   `internal = firm in internal_parties()`. The zip carries `infra/logic/registry/mail_parties.json` with
   `party=opal role=internal domain=opalinvest.com`.
4. **Exercised, both arms.** The deployed module, run from the extracted zip with its own `ROOT` (the record path exists):
   `internal_parties() = ['opal']`; `firm_of("opalbloomberg@opalinvest.com") = opal`; rendered line 2 for firm `opal` is
   `Opal`, and for firm `alongside` (negative control) `CLIENT alongside`.

## Why INFERRED, and what would make it MEASURED

The one silent failure, a missing or unreadable party record that turns every Opal sender into `CLIENT opal`, is ruled out
on the deployed zip (item 4), and the live `firm=opal` is the input that rule reads. What is not read is the received text
itself. Making it measured takes one act, not a wait: Andrew reads line 2 of the `#M611` text on his phone (`Opal` expected).
That confirmation is optional; this grade does not hold on it.
