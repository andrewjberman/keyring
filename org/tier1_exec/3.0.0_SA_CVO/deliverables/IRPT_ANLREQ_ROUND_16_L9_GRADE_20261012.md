# IRPT_ANLREQ round 16 (workstream Y) -- L9 grades of three judgment criteria

**Grader:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-12 ~22:2xZ. **Asked by:** `2.0.0_SA_COO~Y2` msg 6633, packet
`org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND16_Y_L8_COMPILE_20261012.md` (section 3). This seat read each artifact itself,
not its summary. **Result: 2 PASS, 1 FAIL.**

## AR161-y-AC2J -- PASS

The count script: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~52/r16/count_stored_inputs.py` @1e2f4c0d56.

- **No account value, holding, id or person in the output.** stdout's last line is `json.dumps(count(...))` (`main`). `Stats.to_json`
  holds counts, cause tokens, error codes, report days and months. `by_tenant` is keyed by firm name. Cause tokens are either one of
  four known codes or `OTHER:` plus a code matching `[A-Z][A-Z0-9_]{0,40}`, else `OTHER:UNNAMED`. Error codes go through `safe_code`,
  which takes an AWS error code or an exception CLASS name, never a message, cut to 48 characters. The input id stays in memory, used
  only for the request join. stderr carries reader digests and `SCAN_FAILED <code>`.
- **An input it cannot read is never counted as reading the same.** Every failure in `classify` raises `Unreadable` and returns
  `status="unreadable"` BEFORE the `same` comparison. That covers a missing upload row, an unknown file type, a digest mismatch, a
  stored document that is not JSON, a missing template, and either reader raising (`READER_RAISED`). `Reads.row` and `Reads.blob`
  wrap every AWS exception as `Unreadable`. A failed scan or query exits 3; it is never a zero.
- Note, not a defect: firm names appear as keys. A firm is not a person or an account.

## AR162-y-AC3J -- FAIL on its first clause; its second clause holds

The reader: `infra/aws/lambda/investor-reporting/intake/template_reader.py` @aaf156e8eb (`_is_account_header`, `ACCOUNT_LEAD_WORDS`,
`ACCOUNT_HEADER_EXCLUDED`, `WORDS`), and the Rule 24 record `deliverables/0.9.0_WK_IRPT_ANLREQ~52/r16/CLOSED_LISTS_RULE24.json`.

**Clause 1 (the rule and its exclusions are right against a population that holds account columns): FAIL.** The worker's own
subtraction, over a constructed population of 50 forms, shows the rule wrong in both directions. The two directions do not cost the same:

- **Misses (a two-account file passes as one, silently).** 9 identifier forms are not matched. Two of them are plain spellings of the
  account number: `Account-Number` and `Account/Number`. They miss only because `_norm` splits on whitespace, and
  `strip(string.punctuation)` trims the ends of a token without splitting inside it. So `account-number` is one word and is not
  `account`. The others are `Accounts`, `Acc #`, `Acc No`, `Custodian Acct`, `Sub-Account` and `Client Account`. This is the costly
  direction: the check exists so that two accounts are never read as one portfolio, and a miss serves a wrong analysis with no
  finding at all.
- **False turn-backs (a one-account file is refused).** `Account Value`, `Account Status`, `Account Opened`, `Account Holder` and
  `Account Manager` match on the leading word and are not excluded. `Account Value` is the sharpest: as a per-holding value column it
  holds a distinct value on almost every row, so every such file is turned back as "more than one account". That is recoverable (the
  person sees words), but it is wrong.
- The exclusion list (two whole-cell forms) was chosen with no real-use header behind it. The record says so, and the worker flagged
  both lists "for the L9 grader".

**What would make it right (this seat names the defect; the cut is the issuer's):**
1. Split a header on hyphen and slash as well as on whitespace before taking the first word. That closes `Account-Number` and `Account/Number`.
2. Add the measured attribute forms to the whole-cell exclusions: at least `account value`, `account status` and `account opened`.
   Each exclusion carries a reason, as the two it already has do.
3. Decide, with a sentence on the record, whether a last-word match (`Client Account`, `Sub-Account`, `Custodian Acct`) is admitted.
   If it is not, a multi-account file with that header passes silently, and the contract must say so.

The reader is BUILT, NOT RELEASED. So this costs nothing live, and the repair rides before the release pair (row D2-W52-S20, graduated).

**Clause 2 (each finding's words say what is seen and what to do): PASS.** Each finding says what was seen and what to do:
- ACCOUNT_COLUMN_SEVERAL_VALUES names the column and says to split into one file per account.
- HEADER_ROW_REPEATED names the row and asks a question with both answers.
- TOTAL_ROW_PRESENT names the row and says to remove it, with the reason.
- SHEETS_NOT_READ names what was read and what was not.

Row D2-W52-S21's point (two of them use the imperative) does not fail this clause: an imperative that names the act is "what to do".
The account finding emits no cell value, only the column letter.

## AR164-y-AC2J -- PASS

The control: portal `src/pages/TicketCenter/AnalysisRequestParts.tsx`, `CommentarySent`, at portal commit `7bdc0cc9` (on DEV).

- **One stray press cannot record.** The first button only sets `stage='confirming'`. A post needs a second, separate press on
  "Yes, record it (cannot be undone)". `inFlight` (a ref) and `disabled` while posting stop a double post. A double-click on the
  first button lands on the confirm paragraph, not the confirm button. The service also refuses a second record
  (`SENT_ALREADY_RECORDED`).
- **Knows before pressing that it cannot be undone.** The confirm words say "It cannot be undone. Nothing is sent by this: it only
  records that you sent it", and the confirm button carries "(cannot be undone)".
- **Each refusal reads as a sentence that says what to do.** There is a closed map of the four 409 codes, plus 404, 403 and a
  fallback. No code is shown. The fallback says the outcome is unknown and to check before pressing again.
- **Note:** the `SENT_WRONG_TICKET_TYPE` sentence states why and names no act. It is unreachable from this page: the control is
  offered only on an analysis request.

-- 3.0.0_SA_CVO
