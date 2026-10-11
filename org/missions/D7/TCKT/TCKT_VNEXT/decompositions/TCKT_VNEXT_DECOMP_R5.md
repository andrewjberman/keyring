# TCKT_VNEXT decomposition -- ROUND 5, 2026-10-11, issuer 2.0.0_SA_COO~V2, dell2

**Authority:** the CTO's round-5 analysis `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_TCKT_VNEXT_ROUND_5_20261011.md`
@d94b65958b (msg 5654), section 3, answering the round-4 slug `ledger/L10_SLUG_R4.md` @ffca1edbaa. No PRD addendum. FWD-1 is NOT
REALIZED and its stop is outside every dell2 project; **this round is not a thread round: it opens on the cells carried since
round 1**, by the CTO's ruling. No request goes down the vendor path in any cell here.

| cell | builds | list item | outcome | status | placement | risk | worker_class | depends on |
|---|---|---|---|---|---|---|---|---|
| `R5-ac-1` | a READ: where an account is named in an uploaded holdings file, whether the upload door can count accounts today, and where a one-account check can live (the door, the ticket type, or the form). A findings file, no code | 1 | FWD-3 | cut | dell2 worker, slot 20 | LOCAL | worker-light | none |
| `R5-ac-2` | the one-account check itself, where `R5-ac-1` finds it can live | 1 | FWD-3 | NOT-EVALUATED, NOT CUT | by the read's answer; a served change comes under its own pair | -- | -- | `R5-ac-1` |
| `R5-c6-1` | FWD-6's two clauses on the ticket service: the commentary draft lands on the SAME ticket (the request now stores its `ticket_id`), and the ticket records who sent the final commentary and when | 2 | FWD-6 | NOT-EVALUATED, NOT CUT this issuance | dell2 worker | WORLD by path floor | worker | `R5-ml-1` (same file, the handler); and a ruling on who may write each field, asked of the CTO with this issuance |
| `R5-fn-1` | tests that another firm's caller is refused on a ticket, on the list and on the creator's report record, and that a refusal returns no field of the ticket. Tests only; the handler is not edited | 3 | FWD-2 | cut | dell2 worker, slot 19 | WORLD by path floor (a file under `infra/` is added); nothing is applied | worker | none |
| `R5-fn-2` | FWD-2's live proof: "a real other-firm sign-in refused, in front of Andrew" (PRD section 3 item 1) | 3 | FWD-2 | NOT-EVALUATED, NOT CUT | Andrew's act, or a run under a pair | WORLD | -- | his sitting, or the CTO's word on a synthetic other-firm identity |
| `R5-qa-1` | FWD-5, an issuer RECORD: what the queue list shows for type and age today, read at portal `origin/DEV` and in the service's list answer; and the gap | 4 | FWD-5 | done at this issuance (below) | ISSUER | LOCAL | -- | none |
| `R5-gr-1` | a RECORD of who may read the `svc-commentary` secret (rows D2-S8, D2-S9): read from the policy; no grant added or changed | 5 | (governance) | NOT-EVALUATED | ISSUER, by a cross-box read ask through `0.0.0_AB_MSTR~DELL2` (this box's identity cannot read another principal's policy) | LOCAL | -- | the laptop's return |
| `R5-ml-1` | the client mail log lines carry a digest of the recipient address and never the address; the send-failed line stops printing the raw error text, which can carry the address. Code and tests; no send is made | 6 | (instrument for FWD-2 and FWD-8) | cut | dell2 worker, slot 18 | WORLD by path floor; nothing is applied | worker | none |
| `R5-ml-2` | the apply of `R5-ml-1` (and of `R5-c6-1` if built by then: one deploy), under its own pair | 6 | -- | NOT-EVALUATED | ISSUER + applier seat | WORLD | -- | `R5-ml-1` |
| `R5-dr-1` | row D2-W6-S2, ONE read: the deployed `opal-data-refresh-api` package diffed member by member against its build input at the recorded commit; and whether the deployed `validate_user_type` admits only a `Dev` caller or an Opal-internal one | 7 | (closes an ARMED row) | cut | applier seat, read-only | LOCAL by act (a download and a diff; nothing is written to AWS) | -- | none |
| `R5-sit-1` | STAGED for Andrew's sitting, run only if he files: the ticket's `report_ref` read after his request, and the laptop's rendered walk of the Open report page asked through `0.0.0_AB_MSTR~DELL2` | 8 | FWD-1 (the Opal producer) | STAGED, NOT RUN | ISSUER | LOCAL (reads) | -- | his filing |

**Chains (M = 7):** {`R5-ac-1` -> `R5-ac-2`}; {`R5-ml-1` -> `R5-c6-1` -> `R5-ml-2`}; {`R5-fn-1`}; {`R5-fn-2`}; {`R5-gr-1`};
{`R5-dr-1`}; {`R5-sit-1`}. `R5-qa-1` is done. **Fan-out now: 3 workers of 7 chains, cap 8, plus one applier order.**

**Write sets (disjoint):** `R5-ml-1`: `infra/aws/lambda/ticket_center/lambda_function.py` and ONE new test file
`tests/test_client_mail_digest.py`. `R5-fn-1`: ONE new test file `tests/test_fence_other_firm.py`, no other file under `infra/`.
`R5-ac-1`: its own deliverables folder. `R5-dr-1`: the applier's deliverables folder. `R5-c6-1` would edit the handler too, which
is why it is not cut beside `R5-ml-1`.

## Rule 24 record

- **MECE over the analysis's section 3.** Domain: its eight numbered items. By subtraction: 1 -> `R5-ac-1` (+ `R5-ac-2`); 2 ->
  `R5-c6-1`; 3 -> `R5-fn-1` (+ `R5-fn-2`); 4 -> `R5-qa-1`; 5 -> `R5-gr-1`; 6 -> `R5-ml-1` (+ `R5-ml-2`); 7 -> `R5-dr-1`; 8 ->
  `R5-sit-1`. Nothing of section 3 is uncovered. Cells cut now: 4 of 11; the rest carry a named dependency.
- **Why item 1 starts with a read.** The PRD says the type adds a one-account check "the door lacks". This seat read that the
  door's prospect path sets `account_ids` to an empty list (`infra/aws/lambda/investor-reporting/intake/uploads.py:209`) and did
  not find where an uploaded file's accounts are counted. A build cut on that would be a guess; a wrong home for the check (the
  ticket service cannot see the file) would be a second cell.
- **Why item 3 is tests and not a handler change.** Read by this seat: `tests/test_profile_firm_scope.py` already holds 13 tests
  of the profile-row scope (list filtered, get, claim, complete and report refused outside scope). What it does not hold: a
  CLIENT caller of another firm, the creator's record (built this morning), and an assertion that a refusal's body carries no
  field of the ticket. If one of the new tests cannot pass against the handler as it is, that is a finding, filed as a BLOCKING
  row, not a handler edit under this cell.
- **Same grain:** one read, one build or one act per cell. **State:** nothing here moves the vendor path.

## Issuer record `R5-qa-1` (FWD-5), read 2026-10-11 ~19:4xZ

- The service: `list_tickets` (`infra/aws/lambda/ticket_center/lambda_function.py:1167-1198`) returns each item whole, so
  `ticket_type` and `created_at` are in the answer; it filters by `status`, `assignee`, `ticket_type` and the caller's firm
  scope, and sorts newest first. There is no `age` field: age is derivable from `created_at`.
- The page: portal `origin/DEV` `c3a03c246a` (read 16:45Z, not re-fetched for this record),
  `src/pages/TicketCenter/TicketCenter.tsx:576` renders the type by its label and `:579` renders the created time
  (`fmtWhen(t.created_at)`).
- **So FWD-5's "tell them apart without opening them" holds for TYPE; for AGE the queue shows when a ticket was created, not how
  old it is.** Whether a created time meets "age" is a judgment for the CVO; if it does not, the remedy is one column on a page
  `2.0.0_SA_COO~Y2` is cutting now, so that cell is theirs or waits for their file to be quiet. Put to the CTO.

## Battery

comp-schedule, comp-iam: DECLARED-NOT-APPLICABLE for every cut cell (no schedule; no IAM; `R5-dr-1` reads one function's package
and writes nothing). comp-adversary: `R5-fn-1` IS the adversarial cell; `R5-ml-1`'s arm is the test that an SES error text
carrying the address does not reach the log line.

Dry-run at the base (box/dell2, 2026-10-11 ~19:4xZ, 175 ticket tests): ml-digest FAIL absent, ml-regress FAIL (175 below 178),
fn-fence FAIL absent, fn-regress FAIL (175 below 179), ac-read FAIL absent, all as expected.
