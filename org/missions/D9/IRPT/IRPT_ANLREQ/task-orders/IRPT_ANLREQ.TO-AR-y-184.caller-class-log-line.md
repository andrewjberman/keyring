# TO IRPT_ANLREQ.TO-AR-y-184.caller-class-log-line -- one log line naming the internal caller CLASS, so the status rule's population is measurable

<to_id>IRPT_ANLREQ.TO-AR-y-184</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~55</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-12</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>18</round>
<workstream>Y</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD
**Decomp cell:** `AR-y-184` (`decompositions/IRPT_ANLREQ_DECOMP_R18_Y.md`) | **outcome_ref:** FWD-1 (hop 2) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~55`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-55` (branch `wk-IRPT_ANLREQ-55`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~55 <0.9.0_WK_IRPT_ANLREQ~55@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W55-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`;
  every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES (a mutant that leaves your criterion passing makes the instance INVALID).
  No live call, no push, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add. If a scratch copy is needed, put it OUTSIDE the product tree and leave it (you may not delete recursively; say where it is).

### THE CELL (`AR-y-184`, inlined) -- BUILD. Nothing is released by this order.

*ONE log line in `served.py` names the CLASS of an internal caller that selects a firm other than its own, so the population the status rule would refuse becomes measurable.* A log line is not a monitor and raises nothing.

**Read first:** the CTO's ruling `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_ANLREQ_Y_ROUND_18_20261012.md` section 1 (the status rule's pair row), the round-17 compile `org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND17_Y_L8_COMPILE_20261012.md` section 2 (`AR-y-173`: no log line carries the caller), the census record
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~51/r17/CENSUS_SCRIPT_RECORD.json` (`what_it_cannot_read`), and the code: `infra/aws/lambda/investor-reporting/_authz/served.py` (`Entry._internal_allowed_firms` and its use in `Entry.handle`, lines about 1138-1240; how this file logs, around lines 81-108).

1. **The line.** In `Entry.handle`, in the branch for an INTERNAL, non-service caller that selects a firm other than its verified firm, write ONE line, in the file's existing logging idiom (read how `served.py` logs at lines 81-108 and copy it), of the form
   `INTERNAL-CALLER-CLASS class=<row_present|row_absent|row_non_active> outcome=<admitted|refused>`. `row_present` = a users row whose status is exactly `active`; `row_absent` = no row; `row_non_active` = a row whose status is anything else.
   It carries NO email, user type, firm id, selected firm, name or id, and nothing but those two tokens. It is written once per such call, before the answer is returned, and it changes NO served answer, status code or envelope (the refusal reasons stay exactly as they are).
2. **Tests** in `infra/aws/lambda/investor-reporting/_authz/tests/test_caller_class_log.py` (new), functions named EXACTLY:
   `test_a_caller_with_an_active_row_logs_the_class_row_present`, `test_a_caller_with_no_row_logs_the_class_row_absent`, `test_a_caller_with_a_non_active_row_logs_the_class_row_non_active`, `test_the_caller_class_line_carries_no_identity`
   (the last captures the log output for a caller with a distinctive email and firm and asserts neither appears in ANY captured line). Use the folder's own fakes (the `active_internal_row` pattern in `test_interactive_entry.py`; copy it, do not edit that file).
   Every earlier test in `_authz/tests` keeps passing (337 at the base).
3. **In your report:** the line and where it sits (file:line), the logging idiom you copied, confirmation that no served answer changed (cite the earlier tests that prove it), and how a later census would read the line from the function's logs.

### ACCEPTANCE

<criterion id="AR184-y-AC1" cell_refs="AR-y-184"><invocation>python C:/dev/wk-irpt-anlreq-55/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r18/ar18_checks.py y184-log --root C:/dev/wk-irpt-anlreq-55</invocation><expect>Y184-LOG-OK</expect></criterion>
`AR184-y-AC1`: the four named log tests exist and pass.

<criterion id="AR184-y-AC2" cell_refs="AR-y-184"><invocation>python C:/dev/wk-irpt-anlreq-55/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r18/ar18_checks.py y184-keep --root C:/dev/wk-irpt-anlreq-55</invocation><expect>Y184-KEEP-OK</expect></criterion>
`AR184-y-AC2`: the difference control -- the whole `_authz` test folder passes (337 at the base).

<criterion id="AR184-y-AC3J" cell_refs="AR-y-184" judgment="true"/>
`AR184-y-AC3J` (judgment, graded at L9, never by you): the line names the class and the outcome only, carries no identity under any input, and changes no served answer.

<expected_criteria>AR184-y-AC1 AR184-y-AC2 AR184-y-AC3J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~55/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else.

<paths>
infra/aws/lambda/investor-reporting/_authz/served.py
infra/aws/lambda/investor-reporting/_authz/tests/test_caller_class_log.py
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R18_Y.md</decomp_doc>
<owned_cells>AR-y-184</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~55/IRPT_ANLREQ.TO-AR-y-184.caller-class-log-line.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-184`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> <the criterion ids>`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: RUN -- by reading the AR-y-163 read and the round-17 compile: `served.py` is packaged by 8 functions; the line is BUILT, NOT RELEASED, and adds a log line to the INTERNAL, non-service, other-firm branch only.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading the CTO's ruling (a log line naming the caller CLASS only, no identity; not a monitor) against the cell; the lens: a log line that leaks an identity or changes a served answer. A test captures all log output for a caller with a distinctive email and firm and requires neither to appear. NOT seen: the deployed functions' real log output (0 live log lines read) and the 7 other packagers of served.py.
lane: the files named in <paths> and the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on the CTO's round-18 analysis item 4 ("the same cell adds ONE log line in `served.py` naming the caller CLASS only"). Base: `AR184-y-AC1` FAIL as expected (no file); `AR184-y-AC2` base PASS (337).
- BUILT, NOT RELEASED. Together with the status rule it ships to all eight packagers or the pair names each that stays.
