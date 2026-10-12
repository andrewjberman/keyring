# TO NFRA_CTLPLN.TO-CT-aa-3 -- workstream DEVFENCE round 1 (cell CT-aa-3): the data proxy's route fence admits a Dev-type staff login beside the internal tier (CTO msg 108579, row D1-S9)

<to_id>NFRA_CTLPLN.TO-CT-aa-3</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~75</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-12</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>DEVFENCE</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-aa-3` (`decompositions/NFRA_CTLPLN_DECOMP.round11.md`, Amendment 1) | **outcome_ref:** FWD-28 |
**depends_on:** none (it edits `lambda_function.py` and adds a test file; `CT-aa-1` touches only the thread-trace tool)

---

## WORKER FACE

### THE CELL

The data proxy `opal-portal-data-proxy` fences its routes in `_require_route_access(event, tracker, http_method, path)` (about line 2094 of `infra/aws/lambda/portal_data_proxy/lambda_function.py`). It reads the authorizer context (`event['requestContext']['authorizer']`, or its nested `lambda` object), takes `tier = str(claims.get('tier') or '').strip()`, and admits when `tier == 'internal'`; otherwise a class-(i) route admits a caller whose `firmId` claim is in `ROUTE_FIRMS[f'{http_method} {path}']`; everything else answers 403 `{'error': 'forbidden: Opal-internal readers only'}`.

MEASURED (dell1 row D1-S9, 14:1xZ today, table `opal-users-v2`): six staff PROFILE rows carry `userType` `Dev`; three of them carry a tier of advisor or none, firm `opal-capital`, role admin. The authorizer grants a Dev user ALL whatever the tier, and puts the value in the authorizer context as `userType` (the string `'null'` when the user has none). The fence's `tier == 'internal'` test therefore refuses those three staff logins on the 39 class-(ii) routes. RULED by the CTO (cluster-wide, msg 108579): the helper admits `tier == 'internal'` OR `userType == 'Dev'`; no user record is edited for a fence.

### BUILD

1. In `_require_route_access`, read `user_type = str(claims.get('userType') or '').strip()` from the SAME `claims` object as `tier`, and admit (return None) when `tier == 'internal' or user_type == 'Dev'`. The match is EXACT and case-sensitive after the strip: `'dev'`, `'DEV'`, `'Developer'`, `''`, `'null'` and a missing key are NOT admitted by this clause. Nothing else in the helper changes: the class-(i) `firmId` test, the 403 body and the fail-closed rule stay byte-for-byte. Update the docstring (state that a Dev-type login reads every route, as the authorizer grants it, and that Dev outranks the firm test: a Dev login whose firmId is a partner firm is admitted).
2. Do NOT touch `firm_page_access.py`, the registry, `lib/opal_naming.py`, `lambda-source-map.json`, `session_tracker.py` or the portal. The generated module and the source map need no change (no file is added to or removed from the package).
3. A NEW test file `infra/aws/lambda/portal_data_proxy/tests/test_route_dev_fence.py`, in the style of the existing `tests/test_route_firm_fence.py` (read it whole first: it stubs boto3, loads the handler, drives the real `lambda_handler` on fake API Gateway events over EVERY census route from `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~62/DATA_PROXY_ROUTE_CLASS_CENSUS.md` with each route function replaced by a sentinel that answers 200; copy its scaffolding, do not import the other test file). Over all 41 routes: (a) a caller with tier `advisor`, `userType` `Dev` and a made-up firm answers 200 (reached the route), through BOTH the flat and the nested `lambda` authorizer context; (b) the same caller with tier absent answers 200; (c) a partner-advisor caller (tier `advisor`, a made-up partner firm id, `userType` `Advisor`, and again with `userType` absent and with `'null'`) answers 403 on every class-(ii) route and, on the two class-(i) routes, exactly as before (200 only when its firm is in `ROUTE_FIRMS`); (d) the non-matching spellings `'dev'`, `'DEV'`, `'Developer'`, `''` answer 403 on every class-(ii) route; a value `' Dev '` (padded) is admitted (the helper strips); (e) a Dev login whose firmId is a made-up partner firm is admitted on a class-(ii) route. Control arm: `PORTAL_PROXY_UNDER_TEST=<a pre-edit copy of lambda_function.py>` (as in the existing file) must make cases (a), (b), (e) FAIL; state the count in your report. Every firm id and email in a test is made up; type no real firm name (the naming gate refuses firm tokens; if it REFUSES a commit, STOP and file a BLOCKING row, never encode around it).

### RULES FOR THIS CELL

Your write surface is exactly the `<paths>`. No terraform, no aws, no deploy, no push; nothing is deployed by this cell (a separate order applies it under a signed pair). `.tools/safe-commit.sh` for every commit. Do NOT commit the `portal` gitlink. No non-ASCII added; Python 3.11 compatible; ruff clean. CLAUDE.md and org/XXX.md are LOCKED. FOUND SOMETHING ODD OFF-TASK? Append ONE row (`spec_asserts` + `world_is`) to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W75-S<k>`, `surfaced_at` = `date -u +%FT%TZ`) and keep working.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTaa3-AC1" cell_refs="CT-aa-3"><invocation>python -m pytest -q infra/aws/lambda/portal_data_proxy/tests/test_route_dev_fence.py</invocation><expect>passed</expect></criterion>
`CTaa3-AC1` -- the Dev-type tests pass over all 41 routes (report the whole last line: it must read `N passed` with no `failed` and no `error`).

<criterion id="CTaa3-AC2" cell_refs="CT-aa-3"><invocation>python -m pytest -q infra/aws/lambda/portal_data_proxy/tests/test_route_firm_fence.py</invocation><expect>965 passed</expect></criterion>
`CTaa3-AC2` -- the firm fence still holds exactly as built (965 tests, unchanged; a control that PASSES at the base).

<criterion id="CTaa3-AC3" cell_refs="CT-aa-3"><invocation>python -m pytest -q infra/aws/lambda/portal_data_proxy/tests/test_no_credentials_in_logs.py</invocation><expect>1012 passed</expect></criterion>
`CTaa3-AC3` -- the log-capture tests still pass (1012; a control that PASSES at the base).
</proof_of_spec>

<expected_criteria>CTaa3-AC1,CTaa3-AC2,CTaa3-AC3</expected_criteria>

Each invocation runs from the worktree root under `timeout 120`; record the criterion text as the invocation (no `timeout` prefix). Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~75/NFRA_CTLPLN.TO-CT-aa-3.data-proxy-fence-admits-dev.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTaa3-AC1,CTaa3-AC2,CTaa3-AC3`, and flip `<status>` to `complete` only when all three pass and the instance is VALID (if the flip is refused as outside your grant, leave it `pending` and say so; the issuer flips). Report the control-arm count and the diff of `lambda_function.py` (it should be a few lines).

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round11.md</decomp_doc>
<owned_cells>CT-aa-3</owned_cells>
</decomp_ref>

<paths>
infra/aws/lambda/portal_data_proxy/lambda_function.py
infra/aws/lambda/portal_data_proxy/tests/
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call and no policy.
comp-adversary: RUN -- a Dev clause that admits a partner (case c holds partner-advisor 403 over all 39 class-(ii) routes, and the spellings that are not exactly Dev, case d); a Dev value trusted from a field a caller controls (it is read from the authorizer context, set by the authorizer from the user record, never from a header or body); a fence change that alters the class-(i) answer (CTaa3-AC2 holds the 965 tests); BLIND: whether the authorizer sets `userType` for every Dev login in the live context (the live reads of the separate apply order measure it).
risk: WORLD is declared because the L6 gate derives a floor from the infra paths; this cell deploys nothing.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: CTO msg 108579 (information from dell1 D1-S9); CT-u-6 / CT-w-2 for the helper it edits.
