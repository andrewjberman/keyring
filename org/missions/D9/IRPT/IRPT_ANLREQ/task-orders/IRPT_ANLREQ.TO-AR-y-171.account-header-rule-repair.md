# TO IRPT_ANLREQ.TO-AR-y-171.account-header-rule-repair -- the account-header rule repaired (row W52-S20), with a negative control

<to_id>IRPT_ANLREQ.TO-AR-y-171</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~52</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-12</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>17</round>
<workstream>Y</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD
**Decomp cell:** `AR-y-171` (`decompositions/IRPT_ANLREQ_DECOMP_R17_Y.md`) | **outcome_ref:** FWD-1 (hop 2) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~52`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-52` (branch `wk-IRPT_ANLREQ-52`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~52 <0.9.0_WK_IRPT_ANLREQ~52@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W52-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`;
  every non-PASS row carries a `status_reason`. No live call, no push, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add.

### THE CELL (`AR-y-171`, inlined) -- BUILD. Nothing is released by this order.

*The account-header rule is repaired so that no account-identifier header is missed and no account-attribute header is turned back.*

**Read first:** `org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND16_Y_L8_COMPILE_20261012.md` section 2 (`AR-y-162`), the CVO's FAIL
`org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ANLREQ_ROUND_16_L9_GRADE_20261012.md` clause 1 (the defects and the three remedies named), the CTO's ruling
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_ANLREQ_Y_ROUND_17_20261012.md` section 1 row W52-S20, and the current rule in
`infra/aws/lambda/investor-reporting/intake/template_reader.py` (`_norm`, `_is_account_header`, `ACCOUNT_LEAD_WORDS`, `ACCOUNT_HEADER_EXCLUDED`) with its Rule 24 record
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~52/r16/CLOSED_LISTS_RULE24.json`.

1. **Name the two new test forms FIRST.** Before you change the rule, write into `r17/ACCOUNT_HEADER_POPULATION.json` the members `new_identifier_form` (an
   account-identifier header NOT among the forms of this order or the round-16 population) and `new_attribute_form` (an account-attribute header NOT among them), and commit
   that file alone. They are the negative control: the rule must not have been tuned on them. Commit order is the evidence; say the two commit hashes in your report.
2. **Repair the rule** in `template_reader.py`:
   - split a header cell on hyphen and slash (as well as whitespace) BEFORE taking its words, so `Account-Number` and `Account/Number` read as `account number`;
   - the nine identifier forms the round-16 census left unmatched (`Accounts`, `Acc #`, `Acc No`, `Custodian Acct`, `Sub-Account`, `Account-Number`, `Client Account`,
     `Account/Number`, `No. of Accounts`) are all matched, by a rule you can state in one sentence (a plural, an `acc` or `acct` abbreviation, a custodian, client or sub word
     before `account`, `no. of` before it); say which of your choices is a LAST-WORD match (`Client Account`, `Sub-Account`, `Custodian Acct`) and write ONE sentence on the
     record saying whether a last-word match is admitted and what a multi-account file with such a header does;
   - the five attribute forms (`Account Holder`, `Account Manager`, `Account Value`, `Account Status`, `Account Opened`) are NOT turned back; add each to the whole-cell
     exclusions with its reason and its census line (the other two exclusions, `account type` and `account name`, stay); `Accounting`, `Custodian`, `Portfolio`,
     `Sleeve`, `Model` stay unmatched.
3. **Move the version legitimately.** The reader's output changes, so bump `READER_VERSION` and move the digest stored beside it in `READER_PINS`, in the SAME commit
   (the pin test says how). A stored input written under the round-16 version is not compared under the new one (CONTRACT C-STOREDINPUT); say so in the report.
4. **Write `r17/ACCOUNT_HEADER_POPULATION.json`** (the file of point 1, completed): `identifier_forms` (every identifier form you tested, CONTAINING these seeds:
   `Accounts`, `Acc #`, `Acc No`, `Custodian Acct`, `Sub-Account`, `Account-Number`, `Client Account`, `Account/Number`, `No. of Accounts`, `Account`, `Account Number`,
   `Account #`, `Acct`, `Account No`), `attribute_forms` (CONTAINING `Account Holder`, `Account Manager`, `Account Value`, `Account Status`, `Account Opened`,
   `Account Type`, `Account Name`), `not_account_forms` (CONTAINING `Custodian`, `Accounting`, `Portfolio`, `Sleeve`, `Model`), `new_identifier_form`, `new_attribute_form`,
   and `last_word_match_sentence`. Write `r17/CLOSED_LISTS_RULE24.json` (members or rule, domain, denominator, the uncovered member hunted by subtraction over the
   population, the exclusions each with a reason).
5. **Tests.** Extend `infra/aws/lambda/investor-reporting/intake/tests/test_template_account_totals.py` with one test per repaired class (hyphen and slash forms;
   each attribute form accepted as a one-account sheet; the new forms), and keep the reader pin test passing at the new version. Every earlier test keeps passing.
6. **In your report:** the rule in one sentence; the two new-form commit hashes; the last-word sentence; the new `READER_VERSION` and digest; every existing test whose
   expectation changed; anything you could not decide from the code (a row, not a guess).

### ACCEPTANCE

<criterion id="AR171-y-AC1" cell_refs="AR-y-171"><invocation>python C:/dev/wk-irpt-anlreq-52/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r17/ar17_checks.py y171-rule --root C:/dev/wk-irpt-anlreq-52</invocation><expect>Y171-RULE-OK</expect></criterion>
`AR171-y-AC1`: over the stored population, 0 identifier forms unmatched, 0 attribute or non-account forms turned back, and one new form of each class that is not in the seeds is handled right.

<criterion id="AR171-y-AC2" cell_refs="AR-y-171"><invocation>python C:/dev/wk-irpt-anlreq-52/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r17/ar17_checks.py y171-keep --root C:/dev/wk-irpt-anlreq-52</invocation><expect>Y171-KEEP-OK</expect></criterion>
`AR171-y-AC2`: the difference control -- the whole intake test folder passes (311 at the base) and `READER_VERSION` differs from the round-16 value.

<criterion id="AR171-y-AC3J" cell_refs="AR-y-171" judgment="true"/>
`AR171-y-AC3J` (judgment, graded at L9, never by you): the rule and its exclusions are right against a population that holds account columns, the two new forms were not tuned on, and the last-word sentence says what a multi-account file with that header does.

<expected_criteria>AR171-y-AC1 AR171-y-AC2 AR171-y-AC3J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~52/` and this order's file (status flip only).
- READ only: everything else.

<paths>
infra/aws/lambda/investor-reporting/intake/template_reader.py
infra/aws/lambda/investor-reporting/intake/tests/test_template_account_totals.py
infra/aws/lambda/investor-reporting/intake/tests/test_template_reader.py
infra/aws/lambda/investor-reporting/intake/tests/test_stored_input_contract.py
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R17_Y.md</decomp_doc>
<owned_cells>AR-y-171</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~52/IRPT_ANLREQ.TO-AR-y-171.account-header-rule-repair.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-171`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> <the criterion ids>`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: RUN -- by reading the round-16 build (drained @aaf156e8eb) and its Rule 24 record: the rule is used by `_several_accounts` only; the reader is BUILT, NOT RELEASED, so nothing live changes.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading the CVO's FAIL (`IRPT_ANLREQ_ROUND_16_L9_GRADE_20261012.md`, clause 1) against the cell; the lens: a rule tuned to the forms it was checked on. The order requires one NEW form of each class that the rule was not tuned on, named and committed before the change, and a sentence on the last-word match.
lane: the files named in <paths> and the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on the CTO's round-17 analysis item 1 (row `IRPT_ANLREQ-D2-W52-S20`, the CVO's FAIL of `AR162-y-AC3J`). Base: `AR171-y-AC1` FAIL as expected (identifier forms unmatched, attribute forms turned back); `AR171-y-AC2` base: the count passes (311) but the version equals the round-16 one.
- BUILT, NOT RELEASED. The release pair is a later act, cut only after this merges.
