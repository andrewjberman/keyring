# TO-AR-g-95 -- the upload door derives the price date and never honours one: a sent price_date is ignored and journalled as a closed token

<to_id>IRPT_ANLREQ.TO-AR-g-95</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~196</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>20</round>
<workstream>~G</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (ENGINE) | **Decomp cell:** `AR-g-95` (`decompositions/IRPT_ANLREQ_DECOMP_R20_G.md`) |
**outcome_ref:** FWD-7 (C-PRICES, PRD v0.16) | **depends_on:** `AR-g-68` (merged `4c82e94402`, the last cell to edit the door). Order: CTO msg 8647 (PRD v0.16 @a4af0e5bba, Andrew-direct: no price-date selection; every price is the T-1 close; "T-1 is the correct terminology").

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~196`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-196` (branch `wk-IRPT_ANLREQ-196`), provisioned by the issuer with the whole of `infra/`, `docs/`, `data/` and `org/missions/D9/IRPT` on disk (it has no portal sub-worktree; your cell does not touch the portal). Work only there.
- Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~196 <0.9.0_WK_IRPT_ANLREQ~196@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool. Do not pre-`git add`. The workspace worktree may show ` M portal` and a modified `.parquet` fixture: never commit either.
- A row id has the form `IRPT_ANLREQ-D2-W196-S<k>` (take the next free `<k>`; check the channel file for `W196` first); `surfaced_at` of any row = `date -u +%FT%TZ` at filing. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` (Python 3.9 syntax). No non-ASCII in what you add.
- No live call, NO PUSH, no deploy, no AWS call, no network, no install. Scratch outside the product tree.
- Run each test file ON ITS OWN (`python -m pytest -q <one file>`).

### Read first (under `C:/dev/wk-irpt-anlreq-196/infra/aws/lambda/investor-reporting/`)

- `intake/uploads.py`: `validate_upload` (line 209) and the two places `UploadService` calls `default_price_date(options["price_date"])` (near lines 444 and 612); `intake/portfolio.py` `default_price_date` (line 59: with no date it returns the close of the NYSE trading day before today, from `lib/trading_calendar.py`).
- `intake/tests/test_price_date_default.py` (its harness class `PriceDateDefaultTests`, `payload`, `PRIOR`, `WEDNESDAY`) and `intake/tests/test_uploads.py`.

### THE CELL (`AR-g-95`, inlined)

PRD v0.16: the form has no price-date field; every price is the T-1 frontier close, stated as the report's as-of; the server derives the date and never requires it; a `price_date` a client still sends is ignored and logged, never honoured. Today the door accepts a sent `price_date`, stores it in the options (and so the revision hash) and `default_price_date` returns it as sent. This cell makes the door drop it.

**`intake/uploads.py`, `validate_upload`, exactly this:**
1. The key `price_date` stays in the `optional` set, so a client that still sends it is not refused with `UPLOAD_FIELDS`.
2. Right after `options = {key: payload.get(key) for key in optional - {"supersedes_input_id"}}`: `if options["price_date"] is not None:` print the closed token line `IRPT_UPLOAD price_date_ignored=1` (`print(..., flush=True)`; the value is never in the line), then in every case set `options["price_date"] = None`. A comment cites PRD v0.16 (C-PRICES) in two lines.
3. The valuation-option shape guard that loops over `("price_date", "reference_notional")` now loops over `("reference_notional",)` only: any value of a sent `price_date` (malformed, a number, a list, a long string) is ignored, not refused. The `reference_notional` guard is unchanged.
4. Nothing else in the file changes: `UploadService` still calls `default_price_date(options["price_date"])`, which now always receives `None` and so always derives the date. `portfolio.py`, `ops/prospect_dates.py`, the schemas and the portal are not touched.

**Four existing tests send a date and change as follows (nothing else in those files changes):**
- `intake/tests/test_price_date_default.py`: `test_a_date_that_is_sent_is_used_exactly_as_sent` becomes `test_a_date_that_is_sent_is_ignored_and_the_derived_date_is_used` (patch `portfolio._new_york_today` to `WEDNESDAY`, send `price_date="2026-09-21"`, assert the state NORMALIZED, `resolve_prices` asked at `PRIOR[WEDNESDAY]` and each priced row's `as_of` equal to it); `test_a_malformed_date_that_is_sent_still_refuses_as_it_always_did` becomes `test_a_malformed_date_that_is_sent_is_ignored_too` (`"2026-13-45"`: NORMALIZED, derived date). In the module docstring the sentence "A date that IS sent behaves exactly as before." becomes "A date that IS sent is ignored (PRD v0.16): the server derives the date."
- `intake/tests/test_uploads.py`: in `test_same_token_and_options_reuse_success_before_reresolving_security_or_price` and `test_explicit_refresh_can_reprice_and_preserves_original_value` drop `price_date="2026-09-21"` from the payload and make the price fakes answer with the date they are asked for (`args[-1]`) instead of the fixed `"2026-09-21"`.

**Tests.** A NEW file `intake/tests/test_price_date_ignored.py`, offline, with these exact test function names (the checker looks for each by name); import the harness of `test_price_date_default.py` as a module and capture stdout with `contextlib.redirect_stdout`:
`test_a_sent_price_date_is_dropped_from_the_options_and_logged_as_a_closed_token` (exactly `IRPT_UPLOAD price_date_ignored=1`, once; no line when the date is absent or `None`), `test_a_malformed_or_odd_price_date_is_ignored_too` (`"2026-13-45"`, `"yesterday"`, `5`, a list, a 500-character string), `test_the_same_upload_with_and_without_a_price_date_is_the_same_revision` (equal responses), `test_a_shares_file_is_priced_at_the_derived_t_minus_1_whatever_date_is_sent` (three sent dates, `portfolio._new_york_today` patched to `MONDAY`, `resolve_prices` asked at `PRIOR[MONDAY]`), `test_a_dollars_file_ignores_a_sent_date_and_resolves_no_price`.

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR95-g-AC1" cell_refs="AR-g-95"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g95_checks.py g95</invocation><expect>^AR-G95-OK</expect></criterion>

<criterion id="AR95-g-AC2" cell_refs="AR-g-95"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g95_checks.py regress</invocation><expect>^AR-G95-REGRESS-OK</expect></criterion>

<expected_criteria>AR95-g-AC1,AR95-g-AC2</expected_criteria>

- AC1 asks the validator and the upload service ten things on fakes (the date dropped and one token journalled, no token when none is sent, odd values ignored and never printed, equal options with and without a date, the valuation guard standing, a SHARES file priced at the derived T-1 whatever is sent, the door asking `default_price_date` for the derived date only, a malformed date no longer refusing, one revision with and without a date, a dollars file untouched), then checks your five named tests exist and pass. At base it FAILs.
- AC2 runs nine existing test files one at a time (156 tests: the upload service and its refusal class and on-behalf tests, the owner lookup, the unresolved-keep, the template reader, the proxy corrections, the prospect dates) and needs all of them to pass: the guard that your four test edits are exactly those. At base it PASSes. Run it under `timeout 590`.

## BOUNDS

- **Grant.** The `<paths>` block only. No deploy, no AWS call, no HTTP, no installs.
- **Refusal clause.** If a criterion cannot be met as written, or a commit is refused as another lane: stop, file a row with the refusal text, report what is committed and what is not, and do not weaken a check or force a commit.
- **Rows.** APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below; gate: `python .tools/surprise-row-gate.py --check <path>`.

<paths>
infra/aws/lambda/investor-reporting/intake/uploads.py
infra/aws/lambda/investor-reporting/intake/tests/test_price_date_ignored.py
infra/aws/lambda/investor-reporting/intake/tests/test_price_date_default.py
infra/aws/lambda/investor-reporting/intake/tests/test_uploads.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~196/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-95.door-derives-the-price-date.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R20_G.md</decomp_doc> round 20, workstream ~G, cell `AR-g-95`.
<owned_cells>AR-g-95</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR95-g-AC1, AR95-g-AC2. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~196/IRPT_ANLREQ.TO-AR-g-95.door-derives-the-price-date.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-95`.
- Each acceptance entry's `invocation` is the criterion's text EXACTLY (put the `timeout` bound in the evidence line, not in the invocation).
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder (use `kind` `test` for a test file): commit the product files first, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the check's OK line.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR95-g-AC1,AR95-g-AC2` BEFORE the flip to complete.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~67/IRPT_ANLREQ.TO-AR-g-32.packager-own-store-precheck-no-ticket-read.proof_of_spec.json`.
</proof_of_spec>

**REPORT (final message):**
- each criterion's output lines;
- the lines you changed with line numbers;
- commits and row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- `validate_upload` is called by `UploadService.create` and by `reports/generate_installed.py` (the submission pre-check, which now prints the token on a sent date); `options` flows into the retained revision hash, so an upload that is RE-POSTED with the same token after the release, and whose first post sent a price_date, will compute different options and meet CHANGED_UPLOAD_SAME_TOKEN (the form never sends a date after its own change, and in-flight tokens are short-lived; stated, not mitigated). `default_price_date`, the prospect-dates reader and the schemas are untouched. Nothing is deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no permission change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-adversary: RUN -- read against PRD v0.16 and the four tests that send a date. Traps: the date dropped from the payload but still reaching the options (so the revision hash differs by it); a refusal of an old client that still sends the key (UPLOAD_FIELDS) instead of an ignore; the sent value in the journal line (a malformed or long value would leak into a log); a token on every call, including calls that sent no date; the valuation guard on `reference_notional` lost with the loop edit; a dollars file asking the price service. The checker feeds a green arm (a reference build passes the ten cases, the five named tests and the 156 regress tests) and five mutant arms (the value kept: five or more cases fail; no token: 2; the value in the line: 2; a token when the key is merely present: 1; the reference_notional guard lost: 1).
</preflight>

- Cut on CTO msg 8647 and the issuer's reference build (four existing tests fail on it and are edited as listed). Risk WORLD: the floor of an infrastructure path; source and tests only, nothing deployed. Base: `AR95-g-AC1` FAILs and `AR95-g-AC2` PASSes (156), as expected.
- The portal's form change (removing the price-date field) is `~Y2`'s cell. The door change ships in the ONE resident release r32 if it merges before the release pin.
