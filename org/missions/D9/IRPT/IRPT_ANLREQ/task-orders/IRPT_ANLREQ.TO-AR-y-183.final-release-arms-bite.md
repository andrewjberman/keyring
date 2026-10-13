# TO IRPT_ANLREQ.TO-AR-y-183.final-release-arms-bite -- each final-release arm bites on the check it names (row W54-S7)

<to_id>IRPT_ANLREQ.TO-AR-y-183</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~54</issued_to>
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
**Decomp cell:** `AR-y-183` (`decompositions/IRPT_ANLREQ_DECOMP_R18_Y.md`) | **outcome_ref:** FWD-1 (hop 2) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~54`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-54` (branch `wk-IRPT_ANLREQ-54`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~54 <0.9.0_WK_IRPT_ANLREQ~54@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W54-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`;
  every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES (a mutant that leaves your criterion passing makes the instance INVALID).
  No live call, no push, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add. If a scratch copy is needed, put it OUTSIDE the product tree and leave it (you may not delete recursively; say where it is).

### THE CELL (`AR-y-183`, inlined) -- TESTS ONLY. No product file changes.

*Each of the six arms of `test_final_release_refuses_changed_actor_owner_or_service_identity` is shown to BITE: it fails when its named check, and that check alone, is removed.*

**Read first:** row `IRPT_ANLREQ-D2-W54-S7` and `-S6` in `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md`, the CTO's ruling `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_ANLREQ_Y_ROUND_18_20261012.md` section 1 row D2-W54-S7, `_authz/tests/test_interactive_entry.py` (the test at line 86 and the `active_internal_row` fixture), and the checks the arms name:
`_scope/owner_reads.py` lines 36-41 (the principal is resolved again and compared at 38-39; the retained record's owner is compared at 41) and `prospect.py` lines 91-95 (the same three for the prospect lane), plus the SECOND comparison that also refuses some arms (`interactive_access.py` around line 110).
The round-17 worker found: with the principal re-resolution removed alone, the actor and renderer arms still pass, because `interactive_access.py:110` also refuses them.

Write `infra/aws/lambda/investor-reporting/_authz/tests/test_final_release_bites.py` (new), functions named EXACTLY:
`test_read_actor_arm_bites_when_its_named_check_alone_is_removed`, `test_read_owner_arm_bites_when_its_named_check_alone_is_removed`, `test_read_renderer_arm_bites_when_its_named_check_alone_is_removed`,
`test_prospect_actor_arm_bites_when_its_named_check_alone_is_removed`, `test_prospect_owner_arm_bites_when_its_named_check_alone_is_removed`, `test_prospect_renderer_arm_bites_when_its_named_check_alone_is_removed`.
Each test, using the folder's own fakes and the existing `active_internal_row` pattern (copy the fixture into the new file; do not edit the older file):
1. runs the arm's scenario and asserts it is REFUSED with the check present (say which line refuses it);
2. runs the SAME scenario with the arm's named check alone made a no-op (a `monkeypatch` of that one comparison, with the SECOND comparison that also refuses it neutralised in the same test and the reason stated in a comment), and asserts the arm now FAILS to refuse (the private payload, or the changed identity, gets through);
3. restores everything (monkeypatch only; no source file is edited).
If an arm cannot be made to bite on its named check alone (the check is not isolatable from its second comparison), STOP on that arm: file a BLOCKING row naming the arm and the two lines, and leave the test file without that test; do not weaken the test. Everything outside the new file stays unchanged.
**In your report:** per arm, the named check (file:line), the second comparison and how you neutralised it, and the result with and without the check.

### ACCEPTANCE

<criterion id="AR183-y-AC1" cell_refs="AR-y-183"><invocation>python C:/dev/wk-irpt-anlreq-54/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r18/ar18_checks.py y183-bite --root C:/dev/wk-irpt-anlreq-54</invocation><expect>Y183-BITE-OK</expect></criterion>
`AR183-y-AC1`: the six named bite tests exist and pass.

<criterion id="AR183-y-AC2" cell_refs="AR-y-183"><invocation>python C:/dev/wk-irpt-anlreq-54/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r18/ar18_checks.py y183-keep --root C:/dev/wk-irpt-anlreq-54</invocation><expect>Y183-KEEP-OK</expect></criterion>
`AR183-y-AC2`: the difference control -- the whole `_authz` test folder passes (337 at the base).

<criterion id="AR183-y-AC3J" cell_refs="AR-y-183" judgment="true"/>
`AR183-y-AC3J` (judgment, graded at L9, never by you): each test removes ONLY the check its arm names, neutralises the second comparison for a stated reason, and would fail if the named check were absent.

<expected_criteria>AR183-y-AC1 AR183-y-AC2 AR183-y-AC3J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~54/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else.

<paths>
infra/aws/lambda/investor-reporting/_authz/tests/test_final_release_bites.py
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R18_Y.md</decomp_doc>
<owned_cells>AR-y-183</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~54/IRPT_ANLREQ.TO-AR-y-183.final-release-arms-bite.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-183`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> <the criterion ids>`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- one new test file; no product file changes and nothing is called.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading the round-17 worker's mutant results (row W54-S7: the principal mutant left the actor and renderer arms passing) against the cell; the lens: a test that passes for a reason other than the one it names. Each test removes the named check alone and requires the arm to fail.
lane: the files named in <paths> and the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on the CTO's round-18 analysis item 3 (row `IRPT_ANLREQ-D2-W54-S7`). Base: `AR183-y-AC1` FAIL as expected (no file); `AR183-y-AC2` base PASS (337).
