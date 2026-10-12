# TO NFRA_CTLPLN.TO-CT-u-6 -- workstream REMOTE CT-u-6: the data proxy and the content api read the caller's tier and answer 403 unless it is internal

<to_id>NFRA_CTLPLN.TO-CT-u-6</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~62</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-12</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>REMOTE</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-u-6` (`decompositions/NFRA_CTLPLN_DECOMP.remote1.md`) | **outcome_ref:** FWD-28 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

FWD-28: a function behind the portal authorizer that serves Opal-internal data reads the caller's tier before it answers. Two such
functions examine no caller today, so a verified partner-firm login can read what they serve. You change their CODE and prove it with unit
tests on fake events. You deploy nothing and call no AWS service (a separate cell applies it).

### BUILD

**The rule (CTO ruling, exact):** read `tier` from the authorizer context; answer **403** unless `tier == 'internal'` after
`str(x or '').strip()`; fail closed on a missing, empty or `'null'` value. Do NOT also admit by `firmId`, and do NOT test whether the event
"came through API Gateway" (forgeable, not a control).

**The reference helper** (read it, copy its context-reading shape, NOT its second admit clause):
`infra/aws/lambda/trade-pipeline/trade-dashboard-api/src/dashboard_api.py` lines 38-60 (`_require_internal`), tests in
`infra/aws/lambda/trade-pipeline/trade-dashboard-api/tests/test_internal_only.py`. Its context read is:
`authorizer_ctx = (event.get('requestContext', {}) or {}).get('authorizer', {}) or {}` then
`claims = authorizer_ctx.get('lambda', authorizer_ctx) or {}` then `tier = str(claims.get('tier') or '').strip()`.

1. **`opal-portal-data-proxy`** -- file `infra/aws/lambda/portal_data_proxy/lambda_function.py`. Add one helper `_require_internal(event, tracker)`
   returning `None` for an internal caller, else the 403 the file already builds with `tracker.wrap_response(403, {...})` (use the same
   response helper the file uses for its other errors, so CORS headers match). In `lambda_handler` (line ~2088), call it AFTER the OPTIONS
   preflight return and AFTER the `?warm=1` keep-warm return (both stay unchanged, open to every caller: they serve no data) and BEFORE every
   route, so all routes (health, `/market/*`, AUM, positioning and model holdings, valuation, macro, news, sentiment) are covered by the one call.
   Do not add a per-route check. Do not touch `session_tracker.py`. Do not change any route's behaviour for an internal caller.
2. **`opal-portal-content-api`** -- file `infra/aws/lambda/portal_content/lambda_function.py`. The router (`lambda_handler`, line ~158) sends `GET`
   with no tail to `get_all_overrides()`. Make that GET answer 403 (`_resp(403, {"error": "forbidden: Opal-internal readers only"})`) unless the
   tier is internal, using the same helper shape (the file already has `_actor` at line 66 reading the same context). `PUT` and `DELETE` are
   UNCHANGED: they keep their existing `_is_internal(actor)` firm fence (`firmId == INTERNAL_FIRM_ID`).
3. **Tests** (new files; they are not packaged, since each function's zip takes only the files named in `infra/aws/lambda/ci/lambda-source-map.json`):
   `infra/aws/lambda/portal_data_proxy/tests/test_internal_only.py` and `infra/aws/lambda/portal_content/tests/test_internal_only.py`.
   Stub `boto3` and any module that connects on import (set `sys.modules['boto3']` to a fake before importing the function); read the
   reference test for the pattern. Each file covers, with the real `lambda_handler`:
   - tier `internal` (flat context AND `{'lambda': {...}}` nested): the route answers as before (200 or the route's own normal response);
   - tier `advisor`, `client`, `service`, `''`, the string `'null'`, and a missing authorizer context: 403;
   - the OPTIONS preflight and (data proxy) `?warm=1` still answer 200 for a caller with NO context;
   - (content api only) `PUT` and `DELETE` by a non-internal firm still answer 403 and by the internal firm are unchanged; GET by a partner is 403.
   Data-proxy: also assert that EVERY route string the handler matches is behind the gate by driving ten representative paths from the file's route
   list (read the `if http_method == 'GET' and path ...` lines) with a partner context and requiring 403 on each.

### RULES FOR THIS CELL

You change exactly two source files and add exactly two test files. You run no `terraform`, no `aws` call and no deploy, and you push nothing. You
do not edit `lambda-source-map.json`, any `.tf`, the portal frontend, or the authorizer. You add no alarm, logging service or timeout. No
non-ASCII in any file you write. Python 3.11 compatible; ruff clean. The law files `CLAUDE.md` and `org/XXX.md` are LOCKED.
FOUND SOMETHING ODD OFF-TASK? Append ONE row (`spec_asserts` + `world_is`) to
`org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W62-S<k>`) and keep working. In
particular, if a portal page you can find in the repo (a `portal/` source file calling the content-api GET or a data-proxy route) is one a
PARTNER-firm login can open, name the page and the route in a row: the fence will break it and the issuer must tell the CTO.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTu6-AC1" cell_refs="CT-u-6"><invocation>python -m pytest -q infra/aws/lambda/portal_data_proxy/tests/test_internal_only.py</invocation><expect>passed</expect></criterion>
`CTu6-AC1` -- the data-proxy tests pass, including the ten-route partner-403 arm.

<criterion id="CTu6-AC2" cell_refs="CT-u-6"><invocation>python -m pytest -q infra/aws/lambda/portal_content/tests/test_internal_only.py</invocation><expect>passed</expect></criterion>
`CTu6-AC2` -- the content-api tests pass, including GET 403 for a partner, and PUT/DELETE unchanged.
</proof_of_spec>

<expected_criteria>CTu6-AC1,CTu6-AC2</expected_criteria>

Each invocation runs from the worktree root under `timeout 120`. Write the proof instance to
`org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~62/NFRA_CTLPLN.TO-CT-u-6.portal-functions-caller-tier-fence.proof_of_spec.json`, validate it with
`python .tools/proof-of-spec-check.py <instance> CTu6-AC1,CTu6-AC2`, and flip `<status>` to `complete` only when every mechanical criterion
passes and the instance is VALID.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.remote1.md</decomp_doc>
<owned_cells>CT-u-6</owned_cells>
</decomp_ref>

<paths>
infra/aws/lambda/portal_data_proxy/lambda_function.py
infra/aws/lambda/portal_data_proxy/tests/
infra/aws/lambda/portal_content/lambda_function.py
infra/aws/lambda/portal_content/tests/
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call and no policy change.
comp-adversary: RUN -- the second admit clause (firmId) copied from the reference helper and widening the fence (the face forbids it; the tests use tier advisor with the internal firm id and require 403); a route added later that bypasses the one gate call (the ten-route arm); preflight and keep-warm accidentally fenced (their own arm); a non-internal caller reaching PUT/DELETE (unchanged arm); BLIND: a deployed authorizer that does not put `tier` in the context for some token type, which would 403 an internal user (the apply cell exercises it live).
risk: WORLD is declared because the L6 gate derives a WORLD floor from the infrastructure paths this cell edits (infra/aws/lambda/...), not because it applies anything: this cell deploys nothing and calls no AWS service.
lane: the <paths> block IS the grant (worker RULING 1). The Terraform apply is `CT-u-7`, a WORLD order under a signed pair.
</preflight>

Source: PRD `prd/NFRA_CTLPLN_PRD.md` v0.23 FWD-28; CTO rulings `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULINGS_POST_OFFLINE_FIVE_CROSSBOX_CALLS_AND_TWO_SECURITY_CARRIES_20261012.md`
section 3 (XB-20261011T194408Z-e588; record `0.9.0_WK_NFRA_OPSWKF~7/FOUR_FUNCTIONS_WHAT_A_NON_INTERNAL_CALLER_CAN_DO.md` @723a94955a).
