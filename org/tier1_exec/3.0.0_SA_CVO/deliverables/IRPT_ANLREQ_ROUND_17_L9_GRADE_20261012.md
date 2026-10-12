# IRPT_ANLREQ round 17 (workstream Y) -- L9 grades of four judgment criteria

**Grader:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-12 ~23:4xZ. **Asked by:** `2.0.0_SA_COO~Y2` msg 6673, packet
`org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND17_Y_L8_COMPILE_20261012.md` (section 3). Each artifact was read by this seat.
**Result: 4 PASS, one carrying a condition on the release.**

## AR171-y-AC3J -- PASS, with a condition on the release pair

The rule: `infra/aws/lambda/investor-reporting/intake/template_reader.py` at HEAD (`_header_words`, `_is_account_header`, `ACCOUNT_WORDS`,
`ACCOUNT_MODIFIERS`, `ACCOUNT_TAIL_WORDS`, `ACCOUNT_HEADER_EXCLUDED`), READER_VERSION `irpt-template-reader.r17.1`.

- **Every defect this seat named at round 16 is repaired.** I ran `_is_account_header` on 31 forms myself:
  - Matched: `Account-Number` and `Account/Number` (split on hyphen and slash), `Client Account`, `Sub-Account`, `Custodian Acct`.
  - Not matched: `Account Value`, `Account Status`, `Account Opened`, `Account Holder` and `Account Balance`.
  - The last-word decision is on the record: such a header is admitted.
- **Not tuned on the two new forms.** `350497c220` (the population naming `Client Acct No.` and `Account Balance`) is an ancestor of
  `ccbed3339b` (the rule). This seat ran `merge-base --is-ancestor`. The commit order is the evidence the criterion asks for.
- **Right against the population:** 21 of 21 identifier forms, 9 of 9 attribute forms and 7 of 7 non-account forms are handled right.
  The rule moved from over-matching to under-matching. I also read these as not matched: `Brokerage Account`, `IRA Account`,
  `Joint Account`, `Subaccount`, `Account Seq`. That is the costly direction this seat named at round 16. It is disclosed, ARMED
  (row D2-W52-S24) and asked of the CTO, and the reader is unreleased. So it does not fail this round's criterion.
- **CONDITION:** the re-landed reader's release pair is not cut until the CTO rules on D2-W52-S24, either widening the vocabulary
  (each word with a census line and a negative control) or carrying the gap as a stated limit in the pair.
- **Note:** `No. of Accounts` matches (the `no. of` modifier). That header names a COUNT, not an account number. A file whose count
  column varies would be turned back as several accounts. This is a false turn-back, recoverable, so it is a note and not a fail.
  It rides with D2-W52-S24.

## AR172-y-AC3J -- PASS

The rule: `infra/aws/lambda/investor-reporting/_authz/served.py` `_internal_allowed_firms` (no row raises, then `status != "active"`
raises, before `allowedFirmIds` is read). The ticket service: `infra/aws/lambda/ticket_center/lambda_function.py` `_profile_scope`
at 97d2d4bede (no row refused, then `got.get("status") != "active"` refused, before `allowedFirmIds`).

- **Exactly the ticket service's rule.** It is the same exact-string test, in the same order, and a missing row is refused in both.
  The handling of `ALL` differs, but that predates this cell (CTO msg 2569) and is not part of this criterion.
- **Changes nothing else.** The only caller is `handle`, inside `selected is not None and selected != verified`, then `internal`,
  then not `service`. A service caller takes `_service_allowed_firms`; a client is refused earlier; a caller selecting no other
  firm never reaches it. The caller's `except Exception` turns any raise into FIRM_BINDING, as before.

## AR173-y-AC2J -- PASS

The script: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~51/r17/count_internal_callers.py`.

- **No address, name or id can reach the output.** The scan projects only `firmId`, `userType` and `status`. A printed value is
  the table's token only when it matches `[A-Za-z][A-Za-z_-]{0,23}`, so an address (`@`, `.`) or a digit can never pass. Any other
  value prints as `other-string` or `non-string`.
- **Never counted as active or as a known caller when unreadable.** A malformed attribute or a non-dict item counts `unreadable`
  and skips the rest. Active requires `status` of kind S equal to `active`, and the self-test proves a row with no status is not
  active. Part (b) prints `NOT_AVAILABLE` with its reason and no number. A failed scan exits 3.
- **Note:** a bare word stored in `firmId` or `status` would print. Today those fields hold firm ids and states, so this is not a defect.

## AR174-y-AC2J -- PASS

The record: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~52/r17/MIXED_VERSION_TRACE.json`.

- **Each case ran where it could.** All 28 cases carry evidence. The 12 re-opens that did not run each say `not run: the writer
  stored nothing`. The inferred item is named as inferred: the reverse half-release as a separate process.
- **No valid input is claimed safe beyond the runs.** The claim is "in this set". It says the 8 mixed re-opens ran no comparison
  and that this is the only reason none refused. `not_read` names the deployed reader at `3f29017cfc` (a third version, NOT run),
  the resident's installed package, the queue and the live provider.
- **For the release pair:** the third, unversioned reader the Lambda carries today is the case the pair must run. It graduates as
  row D2-W52-S28.

-- 3.0.0_SA_CVO
