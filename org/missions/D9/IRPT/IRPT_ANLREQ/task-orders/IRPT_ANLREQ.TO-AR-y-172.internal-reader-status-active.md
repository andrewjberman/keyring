# TO IRPT_ANLREQ.TO-AR-y-172.internal-reader-status-active -- the internal firm reader admits a caller only on a users row with status exactly active (row W53-S10 / TCKT_VNEXT-D2-S48)

<to_id>IRPT_ANLREQ.TO-AR-y-172</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~54</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-12</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>17</round>
<workstream>Y</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD
**Decomp cell:** `AR-y-172` (`decompositions/IRPT_ANLREQ_DECOMP_R17_Y.md`) | **outcome_ref:** FWD-1 (hop 2) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~54`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-54` (branch `wk-IRPT_ANLREQ-54`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~54 <0.9.0_WK_IRPT_ANLREQ~54@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W54-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`;
  every non-PASS row carries a `status_reason`. No live call, no push, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add.

### THE CELL (`AR-y-172`, inlined) -- BUILD. Nothing is released by this order.

*The investor-reporting internal reader follows the ticket service: an internal caller that selects a firm other than its own is admitted only on a users row whose `status` is exactly the string `active`.*

**Read first:** the AR-y-163 read `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~53/r16/INTERNAL_READER_NO_ROW_READ.json` (the `reader`, `cases`, `proposed_cell` and `the_ticket_service_shape` members), the CTO's
ruling `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_ANLREQ_Y_ROUND_17_20261012.md` section 1 row W53-S10, and the code:
`infra/aws/lambda/investor-reporting/_authz/served.py` (`Entry._internal_allowed_firms`, and its use in `Entry.handle` for the INTERNAL, non-service branch).

1. **The rule.** In `_internal_allowed_firms`: a caller whose users row is ABSENT raises (the existing handler turns it into FIRM_BINDING); a row whose `status` is not exactly
   the string `active` (absent status, `disabled`, any other value, wrong case) raises, BEFORE `allowedFirmIds` is read. The rest (absent attribute, empty list, a list,
   a non-list, `ALL`) stays exactly as it is. SERVICE callers and CLIENT callers are unchanged. Narrowing happens only where it happens today: when the caller selects a firm
   other than its verified firm; a caller that selects nothing, or its own firm, is served as today. Say this in the report, with the line numbers.
2. **Tests** in `infra/aws/lambda/investor-reporting/_authz/tests/test_internal_status_active.py` (new), functions named EXACTLY:
   `test_internal_caller_with_an_active_row_is_admitted`, `test_internal_caller_with_a_disabled_row_is_refused`, `test_internal_caller_with_a_row_and_no_status_is_refused`,
   `test_internal_caller_with_no_row_is_refused`, `test_service_and_client_callers_are_unchanged`. Use the folder's own fakes (read how `test_allowed_firm_ids.py` builds them).
   Every earlier test in `_authz/tests` keeps passing (320 at the base); if one changes expectation (a test that ASSUMED a no-row caller is admitted), change it, and name it with its reason.
3. **In your report:** the changed lines; the tests whose expectation changed; which of the 24 routes this narrows (from the AR-y-163 read) and which it does not; and what
   a refused caller sees (the public reason code; no change to the envelope).

### AMENDMENT 1 (issuer `2.0.0_SA_COO~Y2`, 2026-10-12, after the first worker's BLOCKING row `IRPT_ANLREQ-D2-W54-S4`)

The first run built the rule, the five status tests (17 pass) and moved fixtures in `test_allowed_firm_ids.py`, and found FIVE tests outside the grant that now fail because their fixture
gives an internal caller NO active users row, which the new rule refuses: `tests/test_interactive_entry.py` (4 tests: `test_other_creator_record_reaches_compute_with_real_viewer`
[both params], `test_opal_prospect_create_is_prospect_not_custody_or_partner`, `test_foreign_creator_input_keeps_both_identities_for_submitter_contract`) and `tests/test_svc_custody_statement.py`
(`test_svc_custody_statement_does_not_change_opal_or_dev_admission`, whose `_ALL_ROW` has no status). I reproduced the five (332 pass, 5 fail). The rule is the CTO's, so the tests are what
changes. **The grant now includes those two test files.** Do exactly this:
1. FIXTURES ONLY: where such a test's internal caller reads a default profile with no row or no status, give that row `status: "active"` (nothing else); each test's ASSERTIONS stay
   exactly as they are, because each test is about what happens AFTER the fence, not about the fence. In `test_svc_custody_statement.py` set `status: "active"` on the row the test means to be admitted
   and leave any row that is MEANT to be refused without one. If a test's assertion would have to change, STOP on that test, leave it failing, and file a row naming it.
2. Say, per test, which fixture line you changed and why that caller is meant to be admitted (one sentence each).
3. Re-run `y172-status` and `y172-keep` (332 + 5 = 337 collected, all passing is the aim), re-validate the proof, flip `<status>` to `complete` only when VALID, and commit as a NEW commit.
4. Your first run's rows S4 and S5 stay. S4 is answered by this amendment (say so in your report); S5 (the narrative test runs a PINNED `served.py`, so its green run is no evidence) is
   the CTO's and stays ARMED: say in the report what narrative's pin means for the release pair.

### ACCEPTANCE

<criterion id="AR172-y-AC1" cell_refs="AR-y-172"><invocation>python C:/dev/wk-irpt-anlreq-54/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r17/ar17_checks.py y172-status --root C:/dev/wk-irpt-anlreq-54</invocation><expect>Y172-STATUS-OK</expect></criterion>
`AR172-y-AC1`: the five named status tests are present and pass.

<criterion id="AR172-y-AC2" cell_refs="AR-y-172"><invocation>python C:/dev/wk-irpt-anlreq-54/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r17/ar17_checks.py y172-keep --root C:/dev/wk-irpt-anlreq-54</invocation><expect>Y172-KEEP-OK</expect></criterion>
`AR172-y-AC2`: the difference control -- the whole `_authz` test folder passes (320 at the base).

<criterion id="AR172-y-AC3J" cell_refs="AR-y-172" judgment="true"/>
`AR172-y-AC3J` (judgment, graded at L9, never by you): the rule is exactly the ticket service's (status exactly `active`, no row refused) and changes nothing for service or client callers or for a caller that selects no other firm.

<expected_criteria>AR172-y-AC1 AR172-y-AC2 AR172-y-AC3J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~54/` and this order's file (status flip only).
- READ only: everything else.

<paths>
infra/aws/lambda/investor-reporting/_authz/served.py
infra/aws/lambda/investor-reporting/_authz/tests/test_internal_status_active.py
infra/aws/lambda/investor-reporting/_authz/tests/test_allowed_firm_ids.py
infra/aws/lambda/investor-reporting/_authz/tests/test_interactive_entry.py
infra/aws/lambda/investor-reporting/_authz/tests/test_svc_custody_statement.py
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R17_Y.md</decomp_doc>
<owned_cells>AR-y-172</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~54/IRPT_ANLREQ.TO-AR-y-172.internal-reader-status-active.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-172`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> <the criterion ids>`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: RUN -- by reading the AR-y-163 read (`deliverables/0.9.0_WK_IRPT_ANLREQ~53/r16/INTERNAL_READER_NO_ROW_READ.json`): 23 of 24 routes are served by the one `Entry.handle`, so the change narrows a served answer on 23 routes; BUILT, NOT RELEASED, and its release is its own never-widen pair carrying a census.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading the CTO's ruling (round-17 analysis section 1, row W53-S10: status exactly `active`; a caller with no row refused) against the AR-y-163 read; the lens: narrowing a served answer for a caller who is served today. The cell is source only; the census (cell AR-y-173) counts them before any release.
lane: the files named in <paths> and the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on the CTO's round-17 analysis item 2 (row W53-S10). Base: `AR172-y-AC1` FAIL as expected (no test file); `AR172-y-AC2` base PASS (320).
- BUILT, NOT RELEASED. It narrows a served answer, so its release is a never-widen pair carrying a census of internal callers with no row or a non-active row (cell `AR-y-173`); the dell agents' grants are not touched (portal callers only).
