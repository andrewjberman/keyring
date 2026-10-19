# NFRA_OPLGTW task order -- `OG-en-32` -- NAME THE CAUSE of five route tests that answer 404 where they expect 405, then repair the TESTS only (round 44; row `Z-S391`; round-43 analysis item 3)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-en-32</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-en-32</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~158</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- tests only; no deploy, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; no AWS call is needed.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's round-43 analysis, item 3 (name the cause read-only, then a one-line repair or a test update).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-en-32` (decomposition addendum R3-T.121, round 44, workstream ENRICH-R44-A)

WHY. Five test cases in the gateway's route tests fail at the base on trunk: each expects HTTP 405 and receives 404. The refusal still refuses (404 is also a refusal); only the status differs. Row `Z-S391` did not establish whether the cause is the installed `starlette` (this tree reads 1.3.1; `infra/aws/ec2/opal-gateway/requirements.txt` says only `starlette>=0.37.0`), a route-table change, or a real defect in how an unsupported method is refused. The five cases, fixed (a case dropped, renamed or skipped is a failure of the check):
1. `tests/test_transcript_route.py::test_bearer_constant_time_own_prefix_only`
2. `tests/test_teams_route.py::test_methods_and_unknown_routes`
3. `tests/test_teams_route.py::test_new_routes_are_get_only_and_allowlist_still_refuses_neighbours`
4. `tests/test_mail_route.py::test_transcript_and_ms_bearers_refused_on_mail_prefix`
5. `tests/test_mail_route.py::test_graph_get_only_fails_closed`
(paths under `infra/aws/ec2/opal-gateway/`; run them from that folder: `python -m pytest -q -p no:cacheprovider <ids>`).

DO, IN THIS ORDER:
1. NAME THE CAUSE, READ-ONLY, BEFORE ANY EDIT. Run the five and read each failure. Find in the application (`app/server.py` and the route modules the tests import) how a request with a method the route does not allow is answered, and what the installed `starlette` does for a path that matches a `Route` whose `methods` exclude the request's method (read the installed package's `routing.py`: does a method mismatch on a single route return a 405 `PartialMatch` response, or fall through to the 404 "not found" handler, and does a `Mount` change that?). Then decide `cause_class`: `routing_library_version` (the installed starlette answers 404 where the older one the tests were written against answered 405: show it by the installed version, the library's own code, and if you can by `pip download starlette==0.37.0 --no-deps` into a scratch folder OUTSIDE the repository and a one-request comparison there), `test_premise` (the tests assert a status the application never promised; the property the tests name is fail-closed, and 404 is closed), or `real_routing_defect` (the application itself answers a wrong status for a method it should refuse with 405, or lets a method through). Write the record `W/ROUTE_404_CAUSE.json` (exact shape in the header of `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r44/checks/en32.AC2.sh`; read it first): `installed.starlette` and `pinned.requirements_line` are checked against what this tree reads.
2. THE REPAIR, TESTS ONLY. If `cause_class` is `routing_library_version` or `test_premise`: change ONLY the three test files so that each of the five cases asserts the property it names (a method the route does not allow is REFUSED, closed) without depending on which of 404 or 405 the installed library returns: accept either status (`in (404, 405)`) where the case checks the status of a refusal, and keep every other assertion of the case unchanged (the body is not served, the handler did not run, the allowlist still refuses the neighbours). Do NOT delete or skip a case, do NOT weaken any other assertion. Record `change` = `{"kind": "test_update", "files": [<the test files you changed>], "why": "<one line>"}`. If the cause is a `real_routing_defect`, change NOTHING, record `change.kind` `none`, file a BLOCKING row naming the file and line of the defect, and STOP: the application is not yours to change in this order.
3. Run the five again: all five pass together (`5 passed`).

## 2. BOUNDS

- Write only the three test files named above (and only in step 2), `W/ROUTE_404_CAUSE.json`, your scratch folder (outside the repository) and, if a row is needed, the channel. NO application file (`app/`), no other test, no release, no deploy.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; print a secret, an email address or a client value.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/tests/test_transcript_route.py
infra/aws/ec2/opal-gateway/tests/test_teams_route.py
infra/aws/ec2/opal-gateway/tests/test_mail_route.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~158/` (the tree convention grants it). Rows: id `NFRA_OPLGTW-Z-W158-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`; a row's `disposition` is one of `UNDER_INVESTIGATION`, `GRADUATED`, `DISMISSED_WITH_REASON` (the last needs a `dismissal_reason`), `DECOMP_INVALIDATING`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-en-32"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r44/checks/en32.AC1.sh; echo "exit=$?"</invocation><expect>(?s)the five named route-test cases: passed 5 of 5; failed 0; pytest rc=0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-en-32"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r44/checks/en32.AC2.sh; echo "exit=$?"</invocation><expect>(?s)cause class (routing_library_version|test_premise|real_routing_defect) \(ok\); installed starlette \S+ equals what this tree reads \(\S+\): yes; requirements line equals the file's: yes; evidence strings \d+ \(want >= 3\).*five cases listed with expected 405 and got_at_base 404: yes; change kind (none|test_update|one_line_repair) over \d+ file\(s\), only the three route-test files: yes; a real defect changes nothing here: yes; email-shaped strings 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-en-32"><invocation>git log --author='0.9.0_WK_NFRA_OPLGTW~158 <' --name-only --format= | grep -v -E '^(org/missions/D9/NFRA/NFRA_OPLGTW/|infra/aws/ec2/opal-gateway/tests/test_(transcript|teams|mail)_route\.py$)' | grep -c . ; echo "exit=$?"</invocation><expect>(?s)^0\s*exit=[01]\s*$</expect></criterion>
</proof_of_spec>

- `AC1`: the five fixed cases pass together. `AC2`: the cause is classed with evidence and the versions are the ones this tree reads, the five cases are listed as 405-expected and 404-at-base, and the change touches only the three route-test files. `AC3`: your commits touch no file outside the project tree except those three test files.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-en-32.round-44-the-five-route-tests-that-fail-at-the-base.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if all three PASS, and report once (commit hash, the AC lines, the cause class and installed starlette version in one sentence, what you changed in the tests in one sentence).

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 44, workstream ENRICH-R44-A. Source: the CTO's round-43 analysis (`ledger/ROUND_ANALYSIS.round43.md` @d35c913755, msg 35841), list item 3: "name the cause read-only: routing-library version, or a real routing defect; then make a one-line repair or a test update; criteria: the cause is printed with its evidence, and the five cases pass at the base."
- READING DISCLOSED TO THE CTO: the repair is bounded to the three test files (a `real_routing_defect` stops the order with a BLOCKING row and comes back to me for a ruling), because an application change would need its own release under a never-widen. Three mechanical criteria (the built behaviour, the cause record, the write-set control).
- The issuer ran the five at the base in the main tree: 5 failed (starlette 1.3.1 here). `AC1` base FAIL as expected; `AC2` base FAIL as expected (record absent); a synthetic green record passes it and a record that names `app/server.py` as changed fails it.
- Risk `WORLD` is the gateway-path floor, as for `OG-en-31`.

<status>pending</status>
<round>44</round>
<workstream>ENRICH-R44-A</workstream>
<slot>~158</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
