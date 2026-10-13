# TO IRPT_ANLREQ.TO-AR-y-216.suite-expectations-to-status-rule -- three function suites' expectations moved to the status rule

<to_id>IRPT_ANLREQ.TO-AR-y-216</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~65</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-12</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>10</round>
<workstream>YR</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD
**Decomp cell:** `AR-y-216` (`decompositions/IRPT_ANLREQ_DECOMP_R20T_Y.md`) | **outcome_ref:** FWD-1 (hop 2) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~65`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-65` (branch `wk-IRPT_ANLREQ-65`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~65 <0.9.0_WK_IRPT_ANLREQ~65@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W65-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`;
  every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES (a mutant that leaves your criterion passing makes the instance INVALID).
  No live call, no push, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add. If a scratch copy is needed, put it OUTSIDE the product tree and leave it (you may not delete recursively; say where it is).

### THE CELL (`AR-y-216`, inlined) -- MOVE THREE SUITES' EXPECTATIONS TO THE STATUS RULE. TEST FILES ONLY. Nothing is released.

*The CTO's ruling (msg 6882, per rounds 17 and 18): an internal caller with no users row, or a row whose status is not exactly `active`, is REFUSED (selecting another firm: `FIRM_BINDING`); an active row binds as before; service subjects are unchanged.* Three suites expect the old behaviour: `narrative/tests` (13 of 69 fail with the rule), `directory/tests` (6 fail and 28 error), `export/tests` (7 fail). The rule is in the trunk's `infra/aws/lambda/investor-reporting/_authz/served.py` (blob 30c0eb88..., commit 564e60483858a3cc5c51ffea6aed0f76ff291abe) and in your worktree.

**Read first:** the two rebase records (`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~61/r20/STATUS_RULE_REBASE_GROUP_A.json`, `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~64/r20/STATUS_RULE_REBASE_GROUP_B.json`: per function `tests` with `failed_names`, `control_failed_names`, `staging`), the rule's own tests `infra/aws/lambda/investor-reporting/_authz/tests/test_internal_status_active.py` and `test_caller_class_log.py` (they show what the rule does), and `_authz/served.py` (`_internal_allowed_firms`).

1. **Reproduce first.** For each suite, run it at your worktree's HEAD (the trunk's served.py, with the rule) with `python -m pytest <folder> -q -p no:cacheprovider` under `timeout 580` from the folder `infra/aws/lambda/investor-reporting/<function folder>` as the suite expects; record `before` (`passed`, `failed`, `errors`, `failed_names`) and `collected_before`. Then the CONTROL: the same run with the ORIGINAL served.py staged in place (for narrative the pin `361c44fa9d`, for the other two the live package's, blob at pin `74a62fb46c`, via `git show <pin>:infra/aws/lambda/investor-reporting/_authz/served.py` into a scratch copy of the tree OUTSIDE your worktree): the failures that remain are PRE-EXISTING; `control_failed_names` lists them; you leave them alone. Never edit `_authz/served.py` or any file outside the three test folders.
2. **Move the expectations.** For each test that fails or errors ONLY with the rule: decide whether it tests the binding itself or only uses an internal caller to reach something else. (a) Tests the binding (a caller with no row, an empty list, or a row without `status`, expected bound or admitted): change the EXPECTATION to the refusal the rule gives (`FIRM_BINDING` or the suite's own refusal assertion), naming in a comment `AR-y-216: status rule (CTO msg 6882)`. (b) Only reaches something else (content hash, receipt, directory cache, and so on): change the FIXTURE so the internal caller has an ACTIVE users row (`status` exactly `active`), so the test measures what it meant. Do not weaken an assertion, delete a test, skip or xfail one, or change a service subject. Record per edit `name`, `how` (`expectation` or `fixture`), `why` (one line).
3. **Prove it.** Re-run the three suites at HEAD (the rule): `after` (`passed`, `failed`, `errors`, `failed_names`) must have `errors` 0 and every failing name also in `control_failed_names`; `collected_after` at least `collected_before`. Run the two `_authz` status tests (unchanged): `authz_tests` {`passed`, `failed`}.
4. **Write `r20/RULE_EXPECTATIONS.json`:** `suites` (one object each for `narrative`, `directory-search`, `export-render`: `suite`, `folder`, `files_changed` (repo paths), `tests_edited`, `before`, `after`, `control_failed_names`, `collected_before`, `collected_after`), `authz_tests`, `claim`, `not_read`. Commit after each suite so a stop leaves something readable.
5. **In your report:** per suite: tests edited by kind, before and after counts, what still fails and why it is pre-existing.

### ACCEPTANCE

<criterion id="AR216-y-AC1" cell_refs="AR-y-216"><invocation>python C:/dev/wk-irpt-anlreq-65/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r20/ar20_checks.py y216-expect --root C:/dev/wk-irpt-anlreq-65</invocation><expect>Y216-EXPECT-OK</expect></criterion>
`AR216-y-AC1`: for each of the three suites the record names the test files changed (inside the suite's folder), every edited test with how and why, no collection or setup error after the edit, every remaining failure also failing with the original bytes, no test removed, and the two `_authz` status tests passing unchanged.

<criterion id="AR216-y-AC2J" cell_refs="AR-y-216" judgment="true"/>
`AR216-y-AC2J` (judgment, graded at L9, never by you): each edit keeps the test's intent (an expectation moved to the rule's refusal, or a fixture given an active row), none weakens an assertion, hides a test or touches a service subject, and the pre-existing failures were left as they were.

<expected_criteria>AR216-y-AC1 AR216-y-AC2J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~65/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else.

<paths>
infra/aws/lambda/investor-reporting/narrative/tests/
infra/aws/lambda/investor-reporting/directory/tests/
infra/aws/lambda/investor-reporting/export/tests/
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R20T_Y.md</decomp_doc>
<owned_cells>AR-y-216</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~65/IRPT_ANLREQ.TO-AR-y-216.suite-expectations-to-status-rule.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-216`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> <the criterion ids>`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: RUN -- by reading the three test folders' scope: test files only; no product file is changed; nothing is released or called.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading the CTO's ruling (msg 6882) against the cell; the lens: a test made to pass by weakening it, a refusal expected where the test meant something else, or a pre-existing failure hidden. The order requires a control run with the original bytes, a count of collected tests that may not fall, and a record of how each edit was made. NOT seen: the suites' behaviour under real callers.
lane: the files named in <paths> and the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on the CTO's msg 6882 as workstream `YR` round 10. Base: `AR216-y-AC1` FAIL as expected (no record).
- The status-rule PAIR and its APPLY are not this order.
