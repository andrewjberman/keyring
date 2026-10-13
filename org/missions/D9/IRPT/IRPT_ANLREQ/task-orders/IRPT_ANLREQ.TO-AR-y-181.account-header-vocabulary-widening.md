# TO IRPT_ANLREQ.TO-AR-y-181.account-header-vocabulary-widening -- the account-header vocabulary widened and the COUNT form excluded (row W52-S24), with negative controls

<to_id>IRPT_ANLREQ.TO-AR-y-181</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~52</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-12</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>18</round>
<workstream>Y</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD
**Decomp cell:** `AR-y-181` (`decompositions/IRPT_ANLREQ_DECOMP_R18_Y.md`) | **outcome_ref:** FWD-1 (hop 2) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~52`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-52` (branch `wk-IRPT_ANLREQ-52`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~52 <0.9.0_WK_IRPT_ANLREQ~52@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W52-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`;
  every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES (a mutant that leaves your criterion passing makes the instance INVALID).
  No live call, no push, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add. If a scratch copy is needed, put it OUTSIDE the product tree and leave it (you may not delete recursively; say where it is).

### THE CELL (`AR-y-181`, inlined) -- BUILD. Nothing is released by this order.

*The account-header rule's identifier vocabulary is widened so a multi-account file under `Brokerage Account`, `IRA Account`, `Joint Account`, `Subaccount`, `Account Seq` or `Account Sequence` is turned back, and `No. of Accounts` (a COUNT) is not read as an account column.*

**Read first:** the CTO's ruling `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_ANLREQ_Y_ROUND_18_20261012.md` section 1 row D2-W52-S24, the row itself in `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md`, the round-17 build
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~52/r17/` (`ACCOUNT_HEADER_POPULATION.json`, `CLOSED_LISTS_RULE24.json`) and the rule in `intake/template_reader.py`
(`_header_words`, `_is_account_header`, `ACCOUNT_WORDS`, `ACCOUNT_MODIFIERS`, `ACCOUNT_TAIL_WORDS`, `ACCOUNT_HEADER_EXCLUDED`).

1. **Name the negative controls FIRST.** Before you change the rule, write into `r18/ACCOUNT_HEADER_POPULATION.json` the member `word_negative_controls`: AT LEAST FIVE headers, each carrying one
   of the new words as a word that is NOT an account column (one each for `brokerage`, `ira`, `joint`, `seq` or `sequence`, and `subaccount` or `sub` if you can; for example a fee, a contribution,
   a holder name, a date). Commit that file alone. The rule must not have been tuned on them. Say the commit hashes in your report.
2. **Widen the rule** in `template_reader.py`, each addition with its census line (the form it admits, why it names an account):
   - modifiers: `brokerage`, `ira`, `joint` (before the account word);
   - account word: `subaccount` (and `subaccounts` only if you can justify it);
   - identifier tail words: `seq`, `sequence`;
   - **`No. of Accounts` is a COUNT, not an identifier:** when the header begins `no. of` and the account word after it is PLURAL (`accounts`, `accts`), it is a whole-cell exclusion (not an account header); `No. of Account`
     (singular) STILL matches. Give the exclusion its reason.
   Nothing already matched stops matching, except `No. of Accounts`; nothing already unmatched (the attribute forms, `Account Balance`, `Custodian`, `Accounting`, `Portfolio`, `Sleeve`, `Model`) starts matching.
3. **Move the version legitimately.** Bump `READER_VERSION` and move the digest in `READER_PINS`, in the SAME commit as the rule (the pin test says how). A stored input under r17.1 is not compared under the new version (CONTRACT C-STOREDINPUT); say so.
4. **Write `r18/ACCOUNT_HEADER_POPULATION.json`** (completed): `identifier_forms` CONTAINING `Accounts`, `Acc #`, `Acc No`, `Custodian Acct`, `Sub-Account`, `Account-Number`, `Client Account`, `Account/Number`, `Account`, `Account Number`,
   `Account #`, `Acct`, `Account No`, `No. of Account`, `Brokerage Account`, `IRA Account`, `Joint Account`, `Subaccount`, `Account Seq`, `Account Sequence`; `count_forms` CONTAINING `No. of Accounts`; `attribute_forms` CONTAINING `Account Holder`,
   `Account Manager`, `Account Value`, `Account Status`, `Account Opened`, `Account Type`, `Account Name`, `Account Balance`; `not_account_forms` CONTAINING `Custodian`, `Accounting`, `Portfolio`, `Sleeve`, `Model`; and `word_negative_controls`.
   Write `r18/CLOSED_LISTS_RULE24.json` (members or rule, domain, denominator, the uncovered member hunted by subtraction over the population, the exclusions each with a reason).
5. **Tests.** Extend `intake/tests/test_template_account_totals.py` with one test per addition (each new modifier, the account word, the tail words, the COUNT exclusion and its singular control, a negative control per new word); keep the pin test passing at the new version. Every earlier test keeps passing.
6. **In your report:** the rule in one sentence; the negative-control commit hashes; the new `READER_VERSION` and digest; every existing test whose expectation changed; anything you could not decide from the code (a row, not a guess).

### ACCEPTANCE

<criterion id="AR181-y-AC1" cell_refs="AR-y-181"><invocation>python C:/dev/wk-irpt-anlreq-52/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r18/ar18_checks.py y181-rule --root C:/dev/wk-irpt-anlreq-52</invocation><expect>Y181-RULE-OK</expect></criterion>
`AR181-y-AC1`: over the stored population, every identifier form is matched, `No. of Accounts` is not (and `No. of Account` is), every attribute and non-account form is unmatched, and each of at least five negative controls is unmatched.

<criterion id="AR181-y-AC2" cell_refs="AR-y-181"><invocation>python C:/dev/wk-irpt-anlreq-52/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r18/ar18_checks.py y181-keep --root C:/dev/wk-irpt-anlreq-52</invocation><expect>Y181-KEEP-OK</expect></criterion>
`AR181-y-AC2`: the difference control -- the whole intake test folder passes (317 at the base) and `READER_VERSION` differs from the round-17 value.

<criterion id="AR181-y-AC3J" cell_refs="AR-y-181" judgment="true"/>
`AR181-y-AC3J` (judgment, graded at L9, never by you): each addition names an account and not an attribute, each negative control is a header whose new word is NOT an account column and was named before the rule changed, and the COUNT exclusion cannot hide a real account column.

<expected_criteria>AR181-y-AC1 AR181-y-AC2 AR181-y-AC3J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~52/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else.

<paths>
infra/aws/lambda/investor-reporting/intake/template_reader.py
infra/aws/lambda/investor-reporting/intake/tests/test_template_account_totals.py
infra/aws/lambda/investor-reporting/intake/tests/test_template_reader.py
infra/aws/lambda/investor-reporting/intake/tests/test_stored_input_contract.py
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R18_Y.md</decomp_doc>
<owned_cells>AR-y-181</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~52/IRPT_ANLREQ.TO-AR-y-181.account-header-vocabulary-widening.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-181`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> <the criterion ids>`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: RUN -- by reading the round-17 build (drained @b09e84971f) and its record: the rule is used by `_several_accounts` only; the reader is BUILT, NOT RELEASED, so nothing live changes.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading the CTO's ruling (round-18 analysis section 1, row S24: WIDEN, a stated limit does not stop a wrong holding reaching a report) against the cell; the lens: a widened rule that turns back a one-account file. The order requires at least five negative controls, one per new word, committed before the rule changes.
lane: the files named in <paths> and the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on the CTO's round-18 analysis item 1 (row `IRPT_ANLREQ-D2-W52-S24`, ARMED). Base: `AR181-y-AC1` FAIL as expected (six identifier forms unmatched, `No. of Accounts` matched); `AR181-y-AC2` base PASS count but the version equals round 17's.
- BUILT, NOT RELEASED. The reader's release pair is cut only after this and the count (`AR-y-182`) merge.
