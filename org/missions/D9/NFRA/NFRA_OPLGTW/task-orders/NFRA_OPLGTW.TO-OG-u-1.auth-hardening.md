# NFRA_OPLGTW task order -- `OG-u-1` -- ROUND 2 (E9, part 1): `/ms/site_children` authenticates before it validates; the browser OIDC routes join AUTH_PATHS (rows W3-S11, W3-S18), BUILD only

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-u-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~12</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a code change; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change.
comp-adversary: DECLARED-NOT-APPLICABLE -- both remedies are named in their rows and ruled into E9 by the round-1 analysis.
EGRESS CLASS, declared: NONE. No AWS call, no deploy, no data write.
</preflight>

## 1. THE CELL -- `OG-u-1` (decomposition addendum R2-E, item E9, part 1)

`GW` = `infra/aws/ec2/opal-gateway`. There are two defects, each a few lines. Print the cited bytes at your HEAD first
(`OG-t-1`, earlier in your queue, does not touch these files).

1. **W3-S11: parameters validated before the credential.** `GW/app/server.py:794-799`:
   ```
   async def ms_site_children(request: Request):
       sid = request.query_params.get("site_id", "")
       path = request.query_params.get("path") or None
       if not sid:
           return JSONResponse({"error": "site_id required"}, status_code=400)
       return _ms_run(request, lambda: ms_ingest.ms_site_children(sid, path))
   ```
   An unauthenticated caller with no `site_id` reads 400 `site_id required` before `_ms_guard` (`:761-773`) runs, so it
   learns the route's parameter contract.
   **Fix:** run `_ms_guard(request)` FIRST and return its response when it is not None. Validate `site_id` only after
   that. Behaviour for an authenticated caller is unchanged (400 without `site_id`, else `_ms_run`). Do not double-audit:
   `_ms_guard` logs the credential once, so the authenticated path must not call it twice (restructure, or add a
   `_ms_run` variant that takes an already-passed guard).
2. **W3-S18: the browser OIDC endpoints are rate-limited as ordinary traffic.** `GW/app/ratelimit.py:41-42`:
   ```
   # The unauthenticated OAuth endpoints -- per-IP FAIL-CLOSED here (the limiter is their only brute-force guard).
   AUTH_PATHS = frozenset({"/authorize", "/token", "/register", "/callback"})
   ```
   The browser login and callback are `browser_oidc.LOGIN_PATH` = `/schwab/download/login` and `CALLBACK_PATH` =
   `/schwab/download/callback` (`GW/app/browser_oidc.py:59-61`). Each callback costs an upstream code redemption.
   **Fix:** add both paths to `AUTH_PATHS`. `GW/app/server.py:248` (`is_auth = path in ratelimit.AUTH_PATHS`) then puts
   them in the FAIL-CLOSED auth bucket. Write the two literals in `ratelimit.py`; do not import `browser_oidc` there,
   because `ratelimit` is loaded early. The test asserts the literals equal `browser_oidc.LOGIN_PATH` /
   `browser_oidc.CALLBACK_PATH`.
3. **Tests.** New `GW/tests/test_auth_hardening.py` (moto is not needed). Use a Starlette TestClient on `server.app` with
   the ALB check stubbed, as `GW/tests/test_owner_gate.py:36-93` does. Exactly these 5 tests:
   - `test_site_children_no_credential_no_params_is_401`: 401 with `WWW-Authenticate: Bearer`, not 400;
   - `test_site_children_valid_credential_no_params_is_400`: with `ms_ingest.authorize` and `configured` stubbed to accept;
   - `test_browser_login_path_in_auth_paths`
   - `test_browser_callback_path_in_auth_paths`
   - `test_browser_callback_uses_auth_bucket`: the limiter's auth bucket, not the global one, denies the (N+1)th request
     within the window at the configured `RL_IP_AUTH_*` limit.

## 2. BOUNDS

1. Code and tests only. No AWS call, no deploy. In `GW/app/server.py` touch ONLY `ms_site_children` and, if you need
   one, a new helper beside `_ms_run`.
2. Every test run sets `AUDIT_PATH` to a temp file. If the tracked `GW/audit.jsonl` is dirtied (row W3-S2), restore it
   to HEAD bytes and never commit it.
3. You work in the worktree named in your identity line (the same one as `OG-t-1`). Standing: no push, no vendor call,
   never `git stash`. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/server.py
infra/aws/ec2/opal-gateway/app/ratelimit.py
infra/aws/ec2/opal-gateway/tests/test_auth_hardening.py
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~12/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md`, id
`NFRA_OPLGTW-Z-W12-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-u-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/round2/checks/hd.AC1.sh; echo "exit=$?"</invocation><expect>named tests passed 5 of 5; failed/error lines 0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-u-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/round2/checks/hd.AC2.sh; echo "exit=$?"</invocation><expect>RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

- `AC1` -- W3-S11 and W3-S18: the 5 named tests pass.
- `AC2` -- regression control: the rate limiter's and the tier/attachment suites still pass, 14 or more, none failed.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~12/NFRA_OPLGTW.TO-OG-u-1.auth-hardening.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance>`. Report once: the diff stat, the 5 test names, the literal
AC1-AC2 output, that `GW/audit.jsonl` is clean, the commits and the rows.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Slot ~12, queue position 2 (after `OG-t-1`). Rides `OG-t-2`'s narrow release with `OG-t-1` and `OG-u-2`.
- `server.py` is not in `OG-t-1`'s `<paths>`, so the two write sets are disjoint; one worker queue because both ride one
  release. `hd.AC2` runs `test_ratelimit.py` alone with the tier suites (no asyncio-clock pairing, so W3-S6 does not bite).
- `<risk>` WORLD is GATE (xii)'s floor (an `infra/` path); the cell deploys nothing.

<status>staged</status>
<round>3</round>
<slot>~12</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
