# TO IRPT_ANLREQ.TO-AR-y-194.account-header-value-backstop -- the vocabulary widened once more and closed on values (rows S31, S32)

<to_id>IRPT_ANLREQ.TO-AR-y-194</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~59</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-12</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>19</round>
<workstream>Y</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD
**Decomp cell:** `AR-y-194` (`decompositions/IRPT_ANLREQ_DECOMP_R19_Y.md`) | **outcome_ref:** FWD-1 (hop 2) | **depends_on:** the reader's release pair is cut
**SPAWN AMENDMENT 1 (issuer `2.0.0_SA_COO~Y2`, 2026-10-13).** The reader's release pair is cut, signed and applied (resident 0485393f3a-r19 at 06:09:33Z, Lambda CodeSha256 bNPCG2Oe... at 06:27Z; CTO half @6facbbb2d3). Slot `~59` was used by `AR-y-201` after this order was written, so this order is re-slotted to `~59` (worktree `C:/dev/wk-irpt-anlreq-59`, branch `wk-IRPT_ANLREQ-59`): every `~59` below is now `~59`. Base for the work: the trunk head's `template_reader.py` (READER_VERSION r18.1, the bytes now released). Nothing in this order is released by it; the next reader release repeats the two-leg method. No gate limb graded this amendment (a pending order's text).

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~59`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-59` (branch `wk-IRPT_ANLREQ-59`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~59 <0.9.0_WK_IRPT_ANLREQ~59@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W59-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`;
  every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES (a mutant that leaves your criterion passing makes the instance INVALID).
  No live call, no push, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add. If a scratch copy is needed, put it OUTSIDE the product tree and leave it (you may not delete recursively; say where it is).

### THE CELL (`AR-y-194`, inlined) -- BUILD. Nothing is released by this order.

*The account-header rule is widened once more AND closed on VALUES by one backstop.* The CTO (round-19 analysis, rows S31 and S32): stop chasing spellings; close the class on values.

**Read first:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_ANLREQ_Y_ROUND_19_20261013.md` section 1 rows D2-W52-S31 and D2-W52-S32, the round-18 build `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~52/r18/` (`ACCOUNT_HEADER_POPULATION.json`, `CLOSED_LISTS_RULE24.json`), and the rule in `intake/template_reader.py` (`_header_words`, `_is_account_header`, `_several_accounts`, the word sets, the findings and their `WORDS`).

1. **Name the negative controls FIRST** in `r19/ACCOUNT_HEADER_POPULATION.json` (`word_negative_controls`, AT LEAST SIX headers: one each for `roth ira`/`trust` as modifiers, plural tails, `nos`/`seqno`/`serial`, `accnt`, one header with an account ROOT whose values are NOT identifiers, and one count-like header), each a header carrying the new word as something that is NOT an account column. Commit that file alone BEFORE the rule changes; say the hashes.
2. **Widen:** modifiers `roth ira`, `trust`; plural tails (`numbers`, `nos`, `seqno`, `serial`), `acct`/`accnt` as account words, `subaccounts`; each with its census line.
3. **The VALUE BACKSTOP:** a column whose header carries an account ROOT (`acc`, `acct`, `accnt`, `subacc`) and holds TWO OR MORE DISTINCT IDENTIFIER-LIKE values is read as an account column for the multi-account check, even if the header-word rule did not match it. Define "identifier-like" in the code (for example: a short token of letters and digits with at least one digit, or a run of digits; NOT a name, a date, a money value or a status word) and write the definition on the record. `No. of Accounts` is excluded ONLY when its values are COUNTS (one small integer per row); if it holds identifiers the backstop reads it as an account column. One negative control each way.
4. **The words:** the finding the backstop raises says WHAT IS SEEN and ASKS; it never tells a person to split the file (reuse the repeated-header words' pattern).
5. **Move the version legitimately:** bump `READER_VERSION` and move the pin in the same commit as the rule.
6. **Write `r19/ACCOUNT_HEADER_POPULATION.json`** (completed): `identifier_forms` CONTAINING every form the check names (`Account`, `Account Number`, `Acct`, `Brokerage Account`, `IRA Account`, `Joint Account`, `Subaccount`, `Account Seq`, `Account Sequence`, `No. of Account`, `Sub-Account`, `Custodian Acct`, `Client Account`, `Account Numbers`, `Subaccounts`, `Accnt`, `Account Nos`, `Account Seqno`, `Account Serial`, `Roth IRA Account`, `Trust Account`), `attribute_forms` (`Account Holder`, `Account Manager`, `Account Value`, `Account Status`, `Account Opened`, `Account Type`, `Account Name`, `Account Balance`), `not_account_forms` (`Custodian`, `Accounting`, `Portfolio`, `Sleeve`, `Model`), `word_negative_controls`. Write `r19/CLOSED_LISTS_RULE24.json`.
7. **Tests:** `intake/tests/test_account_value_backstop.py` (new), functions named EXACTLY: `test_an_account_root_header_with_two_identifier_values_is_read_as_an_account_column`, `test_an_account_root_header_with_one_value_is_not_several_accounts`, `test_no_of_accounts_holding_counts_is_excluded`, `test_no_of_accounts_holding_identifiers_is_read_as_an_account_column`, `test_the_backstop_words_say_what_is_seen_and_ask`; plus one test per widened form in `test_template_account_totals.py`. Every earlier test keeps passing (331 at the base).
8. **In your report:** the rule and the backstop in two sentences, the definition of identifier-like, the negative-control hashes, the new `READER_VERSION` and digest, every existing test whose expectation changed.

### ACCEPTANCE

<criterion id="AR194-y-AC1" cell_refs="AR-y-194"><invocation>python C:/dev/wk-irpt-anlreq-59/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r19/ar19_checks.py y194-rule --root C:/dev/wk-irpt-anlreq-59</invocation><expect>Y194-RULE-OK</expect></criterion>
`AR194-y-AC1`: over the stored population every listed identifier form is matched, every attribute, non-account and negative-control form is not.

<criterion id="AR194-y-AC2" cell_refs="AR-y-194"><invocation>python C:/dev/wk-irpt-anlreq-59/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r19/ar19_checks.py y194-backstop --root C:/dev/wk-irpt-anlreq-59</invocation><expect>Y194-BACKSTOP-OK</expect></criterion>
`AR194-y-AC2`: the five named backstop tests exist and pass.

<criterion id="AR194-y-AC3" cell_refs="AR-y-194"><invocation>python C:/dev/wk-irpt-anlreq-59/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r19/ar19_checks.py y194-keep --root C:/dev/wk-irpt-anlreq-59</invocation><expect>Y194-KEEP-OK</expect></criterion>
`AR194-y-AC3`: the difference control -- the whole intake test folder passes (331 at the base) and `READER_VERSION` differs from r18.1.

<criterion id="AR194-y-AC4J" cell_refs="AR-y-194" judgment="true"/>
`AR194-y-AC4J` (judgment, graded at L9, never by you): the backstop cannot turn back a one-account file, the identifier-like definition is stated and right, and each negative control was named before the rule changed.

<expected_criteria>AR194-y-AC1 AR194-y-AC2 AR194-y-AC3 AR194-y-AC4J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~59/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else.

<paths>
infra/aws/lambda/investor-reporting/intake/template_reader.py
infra/aws/lambda/investor-reporting/intake/tests/test_account_value_backstop.py
infra/aws/lambda/investor-reporting/intake/tests/test_template_account_totals.py
infra/aws/lambda/investor-reporting/intake/tests/test_template_reader.py
infra/aws/lambda/investor-reporting/intake/tests/test_stored_input_contract.py
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R19_Y.md</decomp_doc>
<owned_cells>AR-y-194</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~59/IRPT_ANLREQ.TO-AR-y-194.account-header-value-backstop.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-194`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> <the criterion ids>`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: RUN -- by reading the round-18 build (drained @a665d34dd3): the rule is used by `_several_accounts` only; the reader is BUILT, NOT RELEASED, so nothing live changes.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading the CTO's ruling (round-19 analysis rows S31 and S32: close the class on VALUES) against the cell; the lens: a backstop that turns back a one-account file whose header carries an account root. The order requires a negative control each way and an identifier-like definition on the record. NOT seen: real client headers (0 read; the population is constructed).
lane: the files named in <paths> and the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on the CTO's round-19 analysis item 2. NOT SPAWNED until the reader's release pair is cut (the CTO: nothing else in this round is cut ahead of it); it rides the NEXT reader release unless it merges before the pair is cut. Base: `AR194-y-AC1` FAIL as expected (the new forms unmatched).
