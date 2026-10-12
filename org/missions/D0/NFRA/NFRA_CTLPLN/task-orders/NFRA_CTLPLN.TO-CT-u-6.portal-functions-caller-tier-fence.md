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
<criterion id="CTu6-AC1" cell_refs="CT-u-6"><invocation>grep -c "ROUTES total=" org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~62/DATA_PROXY_ROUTE_CLASS_CENSUS.md</invocation><expect>1</expect></criterion>
`CTu6-AC1` -- the census exists and prints its denominator line once (AMENDMENT 1, step 1).

<criterion id="CTu6-AC2" cell_refs="CT-u-6"><invocation>python -m pytest -q infra/aws/lambda/portal_data_proxy/tests/test_route_class_fence.py</invocation><expect>passed</expect></criterion>
`CTu6-AC2` -- the per-class data-proxy tests pass, including the `FIRM-SETS-CURRENT` drift test.

<criterion id="CTu6-AC3" cell_refs="CT-u-6"><invocation>python -m pytest -q infra/aws/lambda/portal_content/tests/test_get_open_put_delete_fenced.py</invocation><expect>passed</expect></criterion>
`CTu6-AC3` -- the content api GET is open to a partner and an internal caller; PUT/DELETE keep their firm fence.
</proof_of_spec>

<expected_criteria>CTu6-AC1,CTu6-AC2,CTu6-AC3</expected_criteria>

Each invocation runs from the worktree root under `timeout 120`. Write the proof instance to
`org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~62/NFRA_CTLPLN.TO-CT-u-6.portal-functions-caller-tier-fence.proof_of_spec.json`, validate it with
`python .tools/proof-of-spec-check.py <instance> CTu6-AC1,CTu6-AC2`, and flip `<status>` to `complete` only when every mechanical criterion
passes and the instance is VALID.


<amendment>
AMENDMENT 1 (issuer 2.0.0_SA_COO~C, 2026-10-12 ~03:2xZ) -- REOPENED on the CTO's ruling (1.0.0_SA_CTO msg 108435; PRD v0.24, FWD-28 re-worded) after row NFRA_CTLPLN-W62-S1: the tier-only fence would 403 pages partner firms are admitted to. Gate limb: none graded this modification (no new TO file; <placeholders> unchanged). SUPERSEDES the BUILD section's rule, items 1-3, as follows; the commits 1048c86508..02223f164c are inherited state:
- THE NEW RULE (PRD v0.24 FWD-28): classify the data-proxy routes ONCE, by measurement. CLASS (i): a route called, directly or through a shared component, by a page whose path is in `FIRM_ALLOWED_PATHS` (`portal/src/lib/firmAccess.ts`). CLASS (ii): every other route. Class (ii) answers 403 unless authorizer `tier` is `internal`. Class (i) answers 403 unless the caller's `firmId` is in the union of the firm sets that SAME file admits for the pages that call it, OR `tier` is `internal`. The firm sets are never typed a second time.
- CONSERVATIVE BY RULE: misclassifying a route as (ii) breaks partner pages (the hazard of row W62-S1); misclassifying one as (i) only leaves it as open as today to the partner firms. So a route is class (ii) ONLY when you can show that no `FIRM_ALLOWED_PATHS` page's import closure reaches the client function that calls it. Any route you cannot trace is class (i), with the union of ALL firm sets in the file.
- STEP 1, CENSUS (write it first): `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~62/DATA_PROXY_ROUTE_CLASS_CENSUS.md`. Enumerate every route the data-proxy handler matches (print the denominator as a line `ROUTES total=<n>`; the CTO's figure is 11, report the true count and any difference). Per route: the route pattern, the `portal/src/api/portal-proxy.ts` function that calls it, each page file that imports that function (and each shared component that does), the page's `<Route path>` in `portal/src/App.tsx`, whether that path is in `FIRM_ALLOWED_PATHS`, the class, and the firm union. Trace by reading the portal source at the paths below; do not run the portal.
- STEP 2, GENERATED FIRM SETS (one source): add `.tools/portal-proxy-firm-sets-gen.py`, which reads `portal/src/lib/firmAccess.ts` (default path, `--ts <path>` to override) and `infra/aws/lambda/portal_data_proxy/route_pages.json` (your census as data: route pattern -> list of page paths, class) and writes `infra/aws/lambda/portal_data_proxy/firm_access_generated.py` (a module with a dict `ROUTE_RULES`: route pattern -> `{"class": "i"|"ii", "firms": [..sorted..]}`). `--check` regenerates in memory and compares to the committed file, printing `FIRM-SETS-CURRENT` or `FIRM-SETS-DRIFT` and exiting 0 or 1. Standard library only; ASCII only; the generated file carries a header line naming the source file, its sha256 and the generator.
- STEP 3, THE HANDLER: replace the single `_require_internal` gate in `infra/aws/lambda/portal_data_proxy/lambda_function.py` with a per-route gate driven by `firm_access_generated.ROUTE_RULES` (import it; the file `firm_access_generated.py` will be added to the function's package by the apply cell). Same position as before (after the OPTIONS and `?warm=1` returns, before every route). A path that matches no known route answers 403 (fail closed). Keep the helper's context read (`claims = ctx.get('lambda', ctx)`; `tier`, `firmId` read with `str(x or '').strip()`).
- STEP 4, THE CONTENT API IS UNFENCED AGAIN: revert `infra/aws/lambda/portal_content/lambda_function.py` to the issuance base (`git show edef413890:infra/aws/lambda/portal_content/lambda_function.py`): the GET stays open to every verified portal login (page copy, LOW); PUT and DELETE keep their firm fence. DELETE `infra/aws/lambda/portal_content/tests/test_internal_only.py` (it asserts the superseded GET fence) and write a NEW file `infra/aws/lambda/portal_content/tests/test_get_open_put_delete_fenced.py` that proves exactly that: GET answers for a partner and for an internal caller, PUT/DELETE by a non-internal firm still 403.
- TESTS (a NEW file `infra/aws/lambda/portal_data_proxy/tests/test_route_class_fence.py`; DELETE the old `test_internal_only.py` there, it asserts the superseded tier-only rule): per class, internal caller allowed; a partner in the admitted union allowed (class i); a firm outside the union 403 (class i); a partner firm 403 (class ii); no context, '', 'null' 403; unknown route 403; OPTIONS and `?warm=1` still 200 with no context; one test asserts `python .tools/portal-proxy-firm-sets-gen.py --check` prints `FIRM-SETS-CURRENT`.
- NEW ACCEPTANCE (replaces the two criteria; at most three):
  CTu6-AC1: `grep -c 'ROUTES total=' org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~62/DATA_PROXY_ROUTE_CLASS_CENSUS.md` expects `1`.
  CTu6-AC2: `python -m pytest -q infra/aws/lambda/portal_data_proxy/tests/test_route_class_fence.py` expects `passed`.
  CTu6-AC3: `python -m pytest -q infra/aws/lambda/portal_content/tests/test_get_open_put_delete_fenced.py` expects `passed`.
- ADDED PATHS (the <paths> block below carries them): `.tools/portal-proxy-firm-sets-gen.py`, `infra/aws/lambda/portal_data_proxy/firm_access_generated.py`, `infra/aws/lambda/portal_data_proxy/route_pages.json`, and the READ-ONLY `portal/src/` tree for the census. You edit nothing under `portal/`.
</amendment>

<amendment>
AMENDMENT 2 (issuer 2.0.0_SA_COO~C, 2026-10-12 ~04:3xZ; gate limb: none graded this modification, no new TO file) -- the CTO's ruling on row NFRA_CTLPLN-W62-S6 (1.0.0_SA_CTO msg 108445, PRD v0.25): the 39 class-(ii) routes fence NOW; the 2 class-(i) routes (`POST /sentiment/keyword-intelligence`, `GET /aum/metrics`) stay open to every verified login exactly as today; the firm check for those two waits for the firm-set module to be an opal_naming registry row (a later cell). The naming gate refused a file carrying firm tokens, so NO FIRM TOKEN is written anywhere by this order. SUPERSEDES AMENDMENT 1 steps 2 and 3, and the firm-union language of its rule; its steps 1 and 4 and its tests stand, adjusted below. Inherited state: the census and the content-api revert are committed on the worker branch (7b375c4002, a1bdd10ec3); the data-proxy set sits UNCOMMITTED in the worktree.
- DELETE (uncommitted files, so just remove them): `.tools/portal-proxy-firm-sets-gen.py`, `infra/aws/lambda/portal_data_proxy/firm_access_generated.py`, `infra/aws/lambda/portal_data_proxy/route_pages.json`. Nothing imports a generated module any more; the `--check` drift test goes with them.
- THE HANDLER: keep the per-route gate and its position (after OPTIONS and `?warm=1`, before every route). Replace the generated-rules lookup by ONE hand-kept constant in `lambda_function.py`, e.g. `_ROUTES_OPEN_TO_VERIFIED_LOGINS = frozenset({...})` holding exactly the two class-(i) routes as the handler matches them (method and normalised path), with a comment citing the census file and PRD v0.25 and saying the firm check is a later registry cell. A matched route in that set is not gated (as today). EVERY OTHER matched route answers 403 unless authorizer `tier` is `internal` (after `str(x or '').strip()`); an unmatched path answers 403. No firm id is read or typed. The constant holds route strings only.
- THE CENSUS stands as written (`ROUTES total=41`; class i = 2, class ii = 39). Add one line at its top: `RULED: PRD v0.25 / msg 108445 -- class (i) routes stay open; class (ii) routes fence on tier`.
- TESTS (`test_route_class_fence.py`, adjust): drive EVERY route in the census. The 39 class-(ii) routes: a partner firm 403; no context, '' and 'null' 403; an internal caller allowed. The 2 class-(i) routes: a partner caller and an internal caller are both allowed (unchanged from today). Unknown path 403; OPTIONS and `?warm=1` 200 with no context. Remove the generator drift test. Keep the control against the previous handler.
- ACCEPTANCE: unchanged (CTu6-AC1 census line, CTu6-AC2 data-proxy tests, CTu6-AC3 content-api tests). Rewrite the INVALID proof instance and validate it.
- PATHS: the order's <paths> no longer need `.tools/portal-proxy-firm-sets-gen.py`, `firm_access_generated.py` or `route_pages.json`; leave them listed (harmless) so a worker may delete its leftovers.
</amendment>

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.remote1.md</decomp_doc>
<owned_cells>CT-u-6</owned_cells>
</decomp_ref>

<paths>
infra/aws/lambda/portal_data_proxy/lambda_function.py
infra/aws/lambda/portal_data_proxy/firm_access_generated.py
infra/aws/lambda/portal_data_proxy/route_pages.json
infra/aws/lambda/portal_data_proxy/tests/
.tools/portal-proxy-firm-sets-gen.py
portal/src/
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
