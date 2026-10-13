# TO IRPT_ANLREQ.TO-AR-y-211.account-header-backstop-repair -- the r19.1 backstop repaired against the CVO's cases

<to_id>IRPT_ANLREQ.TO-AR-y-211</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~60</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-12</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>20</round>
<workstream>Y</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD
**Decomp cell:** `AR-y-211` (`decompositions/IRPT_ANLREQ_DECOMP_R20_Y.md`) | **outcome_ref:** FWD-1 (hop 2) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~60`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-60` (branch `wk-IRPT_ANLREQ-60`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~60 <0.9.0_WK_IRPT_ANLREQ~60@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W60-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`;
  every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES (a mutant that leaves your criterion passing makes the instance INVALID).
  No live call, no push, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add. If a scratch copy is needed, put it OUTSIDE the product tree and leave it (you may not delete recursively; say where it is).

### THE CELL (`AR-y-211`, inlined) -- REPAIR THE r19.1 BACKSTOP. BUILD. Nothing is released by this order.

*The backstop turns back a one-account file whose header is an ABBREVIATED account root plus an attribute word.* The CVO ran it (`org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ANLREQ_ROUND_19_L9_GRADE_20261013.md`, AR194-y-AC4J clause 1): `Acct Market Value` holding `25000000` and `31000000` is turned back as two accounts; so are `Acct CUSIP` (`912828ZT6`, `38141G104`) and `Acct Lot`. The CTO ruled (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_ANLREQ_Y_ROUND_20_20261013.md` section 2, row D2-W59-S1): repair before r19.1 is released; the attribute exclusions apply to the abbreviated root too, and the identifier-like test is checked against the same negative controls.

**Read first:** `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ANLREQ_ROUND_19_L9_GRADE_20261013.md` (the AR194 section), `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_ANLREQ_Y_ROUND_20_20261013.md` section 2, the rule and the backstop in `infra/aws/lambda/investor-reporting/intake/template_reader.py` (`ACCOUNT_HEADER_EXCLUDED`, `_has_account_root`, `_identifier_like`, `_several_accounts`; `READER_VERSION` is `irpt-template-reader.r19.1` at the trunk head), and the r19 population record `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~59/r19/ACCOUNT_HEADER_POPULATION.json`.

1. **Name the negative controls FIRST** in `r20/ACCOUNT_HEADER_REPAIR.json` (`negative_controls`: header and values for every case below, and `positive_controls`), and commit that file ALONE before the rule changes; say the commit hash. Negative controls (a one-account file; `_several_accounts` must return nothing): `Acct Market Value` [25000000, 31000000]; `Acct CUSIP` [912828ZT6, 38141G104]; `Acct Lot` [LOT1234, LOT5678]; `Accnt Value` [12000000, 15000000]; `Acct Status` [AX1234, BX5678]; `Acct Type` [IRA1234, ROTH5678]; `Acct Name` [ACME-401K, ACME-403B]; `Acct Holder` [SMITH2024, JONES2023]; `Acct Balance` [10000000, 12000000]; `Acct Opened` [20200101, 20210202]. Positive controls (a two-account file; must be turned back): `Acct` [A1B2C3D4, E5F6G7H8]; `Account Number` [12345678, 87654321]; `Accnt` [AC123456, AC654321].
2. **Repair (a):** a header that carries an account ROOT (`acc`, `acct`, `accnt`, `subacc`) AND any attribute word never enters the backstop. Define the attribute-word set in one constant next to the existing exclusions, containing at least: `value`, `cusip`, `lot`, `status`, `opened`, `type`, `name`, `holder`, `manager`, `balance`, `market`, `price`, `quantity`, `qty`, `shares`, `amount`, `date`. Each word has a one-line reason in a comment, as `ACCOUNT_HEADER_EXCLUDED` does.
3. **Repair (b):** a run of digits only is identifier-like (8 or more digits) ONLY when no other value in the same column carries a decimal point, a comma or another separator; a column that mixes plain digit runs with decimals is a money column. Write the changed definition next to the constants.
4. **Move the version legitimately:** `READER_VERSION` becomes `irpt-template-reader.r19.2` and the pin (the digest the stored-input tests carry) moves in the same commit as the rule.
5. **Tests:** in `intake/tests/test_account_value_backstop.py` keep the five named tests (their names are fixed) and add one test per negative control above (`test_attribute_header_<slug>_is_not_several_accounts`) and one per positive control. Every earlier test keeps passing (347 at the base).
6. **Complete `r20/ACCOUNT_HEADER_REPAIR.json`:** the two repairs in words, the attribute-word set, the new `READER_VERSION` and digest, the commit hashes (controls alone; rule), `claim`, `not_read`, and the residual you can still see (a root-with-tail header holding per-row letter-and-digit values that are not account numbers).
7. **In your report:** the repair in two sentences, the negative-control commit hash, the new `READER_VERSION` and digest, every existing test whose expectation changed.

### ACCEPTANCE

<criterion id="AR211-y-AC1" cell_refs="AR-y-211"><invocation>python C:/dev/wk-irpt-anlreq-60/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r20/ar20_checks.py y211-repair --root C:/dev/wk-irpt-anlreq-60</invocation><expect>Y211-REPAIR-OK</expect></criterion>
`AR211-y-AC1`: none of the ten one-account negative controls is turned back, the three positive controls are, and the five named backstop tests pass.

<criterion id="AR211-y-AC2" cell_refs="AR-y-211"><invocation>python C:/dev/wk-irpt-anlreq-60/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r20/ar20_checks.py y211-keep --root C:/dev/wk-irpt-anlreq-60</invocation><expect>Y211-KEEP-OK</expect></criterion>
`AR211-y-AC2`: the difference control -- the whole intake test folder passes (347 at the base) and `READER_VERSION` differs from r19.1.

<criterion id="AR211-y-AC3J" cell_refs="AR-y-211" judgment="true"/>
`AR211-y-AC3J` (judgment, graded at L9, never by you): the repair cannot turn back a one-account file the CVO's cases or their obvious neighbours describe, the changed identifier-like definition is stated and right, and the controls were named before the rule changed.

<expected_criteria>AR211-y-AC1 AR211-y-AC2 AR211-y-AC3J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~60/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
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
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R20_Y.md</decomp_doc>
<owned_cells>AR-y-211</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~60/IRPT_ANLREQ.TO-AR-y-211.account-header-backstop-repair.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-211`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> <the criterion ids>`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: RUN -- by reading the r19 build (drained @86471e5472): the rule is used by `_several_accounts` only; the reader is BUILT, NOT RELEASED (live is r18.1), so nothing live changes.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading the CVO's grade against the cell; the lens: a repair that turns back one-account files the cases name by neighbour (other attribute words) or that stops turning back a real two-account column. The order names ten negative and three positive controls, committed alone before the rule. NOT seen: real client headers (0 read; the population is constructed).
lane: the files named in <paths> and the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on the CTO's round-20 analysis row D2-W59-S1 and the CVO's AC4J grade as round 20 workstream `Y`. Base: `AR211-y-AC1` FAIL as expected (9 negatives turned back).
- The release of r19.2 is its own pair, by the release-19 method.
