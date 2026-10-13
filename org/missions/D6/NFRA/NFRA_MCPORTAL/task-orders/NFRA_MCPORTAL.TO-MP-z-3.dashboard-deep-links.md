# NFRA_MCPORTAL task order -- `MP-z-3` -- WORKSTREAM GW ROUND 1: deep links to the dashboard's pages (row Z-S41)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPORTAL/decompositions/NFRA_MCPORTAL_DECOMP.md</decomp_doc>
<owned_cells>MP-z-3</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPORTAL.TO-MP-z-3</to_id>
<issued_to>0.9.0_WK_NFRA_MCPORTAL~15</issued_to>
<issued_by>2.0.0_SA_COO~MP</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a request handler; no cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; a file read beside the bundle the gateway already serves.
comp-adversary: DECLARED-NOT-APPLICABLE -- the named tests are the adversary arms (non-owner, unknown path, missing list, existing routes unchanged).
EGRESS CLASS, declared: none.
</preflight>

## 1. THE CELL -- `MP-z-3` (workstream GW round 1, decomposition sections GW.1 and GW.4)

Your worktree is `C:/tmp/mp-gw-15` (branch `wk-NFRA_MCPORTAL-gw-15`). Work and commit only there.

**The defect** (row NFRA_MCPORTAL-Z-S41; ruling `1.0.0_SA_CTO~Z` msg 33519). Andrew opened
`https://mcp.opalinvest.dev/control-plane` and `/open-calls` directly and got 404. `app/server.py` serves the dashboard
bundle only at `/` (`dashboard_root`, about `:317-330`) and `/assets/{path}` (`dashboard_asset`), mounted near the end of
the route list (about `:1147-1156`). The bundle is a single-page app whose router uses PATH routes, so a direct load or a
refresh of any page but `/` never reaches `index.html`. The issuer measured it on the live host today: `/control-plane`,
`/open-calls` and `/gateway` each answer 404.

**The fix, as ruled:** one owner-gated route serving `index.html` for each path in the bundle's route list; an unknown
path still 404s; a test of each.

**The route list** is a file the bundle ships (a parallel cell adds it): `<DASHBOARD_BUNDLE_DIR>/routes.json`, shaped
`{"version": 1, "paths": ["/", "/control-plane", ...]}`. `DASHBOARD_BUNDLE_DIR` is `_cfg.DASHBOARD_BUNDLE_DIR`
(`app/config.py`, about `:348`).

Build, in the gateway app at `infra/aws/ec2/opal-gateway/`:
1. **In `app/server.py`:** a handler `dashboard_deep_link` and its route.
   - Read `routes.json` at REQUEST time (a deploy replaces the bundle). Use the request path exactly, with no
     normalisation beyond what Starlette gives.
   - The path is in `paths` (and is not `/`, which `dashboard_root` keeps serving): run `owner_gate.require_owner`
     exactly as `dashboard_root` does (a non-owner gets that function's 401/403 response, no body hint), then return
     `index.html` exactly as `dashboard_root` does, including its 503 when the file is missing. Reuse `dashboard_root`'s
     body by factoring a small shared helper if you need one; do not change its behaviour.
   - The path is not in `paths`, or `routes.json` is missing, unreadable, not JSON, or not that shape: answer 404 the way
     an unmatched route answers today (Starlette's plain 404). So a missing list serves `/` only (fail closed).
   - **Placement:** the route must not shadow ANY existing route. Put it LAST in the route list, after `Mount("/mcp", ...)`,
     as `Route("/{path:path}", dashboard_deep_link, methods=["GET"])`, so only a path nothing else matches reaches it.
     Add a comment above it citing NFRA_MCPORTAL MP-z-3 and row Z-S41.
2. **`tests/test_dashboard_deep_links.py` (new).** Use the real `app.server.app` with `TestClient`, a temporary bundle
   directory (patch `DASHBOARD_BUNDLE_DIR` the way `tests/test_owner_gate.py` or the existing dashboard tests do), and the
   owner stubbing those tests use. These five tests, by these exact names:
   - `test_each_listed_route_serves_index_to_owner` -- a planted `routes.json` with `/`, `/control-plane`, `/open-calls`,
     `/gateway` and `/mcp-server/recent-changes`: each answers 200 with the planted `index.html` body for the owner.
   - `test_listed_route_refuses_non_owner` -- `/control-plane` with no identity and with a non-owner identity answers
     the owner gate's refusal status, and the body does not contain the `index.html` text.
   - `test_unknown_path_still_404` -- `/no-such-page` (not in the list) answers 404 for the owner.
   - `test_missing_routes_file_serves_root_only` -- with no `routes.json`, and again with a non-JSON one: `/` answers 200
     for the owner and `/control-plane` answers 404.
   - `test_existing_routes_keep_their_endpoint` -- for each of `/health`, `/assets/x.js`, `/api/admin/whoami`, `/mcp`,
     `/sprint` and `/`, the endpoint the app's router resolves (walk `app.routes` and `route.matches(scope)` until the
     first FULL match) is the same object as before your change: record the expected endpoint/app by name in the test
     and assert none of these resolves to `dashboard_deep_link`.

**AMENDMENT 1 (issuer, 2026-10-13 ~10:5xZ, at the drain read of `24608f8f8a`): the catch-all must not change the answer to
ANY method on a path it does not serve.** Measured by the issuer on your branch's route table: `POST /mcp`, `DELETE /mcp`
and `POST /no-such` now resolve PARTIAL to `dashboard_deep_link` (Starlette answers 405), where the live code answered
`POST /mcp` with Starlette's 307 to `/mcp/` and `POST /no-such` with 404. Every MCP client is registered at
`https://mcp.opalinvest.dev/mcp` (no trailing slash) and POSTs there, so shipping this would break the gateway for every
client. Change, in `app/server.py` only:
- The route accepts EVERY method: `Route("/{path:path}", dashboard_deep_link)` with no `methods=` (or the full method
  list), still LAST.
- In the handler, serve `index.html` (through `dashboard_root`) ONLY for `GET`/`HEAD` on a listed path other than `/`.
  Every other request -- any other method, or an unlisted path -- takes the slash-replay you wrote, matched the way
  Starlette's own `redirect_slashes` matches (a route counts if its match is NOT `Match.NONE`, i.e. FULL or PARTIAL),
  answering 307 to the other slash form; otherwise the plain 404.
- Two more tests in `tests/test_dashboard_deep_links.py`, by these exact names:
  - `test_bare_mcp_post_still_redirects` -- resolve `POST /mcp` through the app's router (walk `app.routes` as in
    `test_existing_routes_keep_their_endpoint`, then call the resolved endpoint, or call `dashboard_deep_link` with a
    `POST /mcp` request): the answer is 307 with `location` ending `/mcp/`, never 405. Also `DELETE /mcp`: 307, never 405.
  - `test_unknown_path_any_method_404` -- `POST /no-such-page` and `PUT /no-such-page` answer 404, never 405.
- AC1 now names 7 tests (the check file is amended at the same commit).

**AMENDMENT 2 (issuer, 2026-10-13 ~11:5xZ, at the drain hygiene run on trunk `ed6ccbcfc5`): the test file must not pollute a
suite that runs after it.** Each gateway test file passes alone, but `python -m pytest tests/test_dashboard_deep_links.py
tests/test_owner_gate.py tests/test_admin_grants.py tests/test_admin_refusals.py` reads 7 failed, 16 passed (for example
`test_owner_gate.py::test_owner_page_served` and `test_admin_grants.py::test_get_grant_reads_store`). With the deep-link file
LAST, everything passes. The cause read by the issuer: the module fixture `app_mods` pops every `app`/`app.*` module it
imported from `sys.modules` at teardown (`tests/test_dashboard_deep_links.py:47-49`). Test files collected earlier still
hold the old module objects, so a later import builds fresh ones and their patches land on the wrong objects. The release
cell runs these files together in that order, so this blocks the release. Change, in `tests/test_dashboard_deep_links.py`
only (no product code): leave the process's module table as the other gateway test files expect it, e.g. by not popping
modules and relying on the `MonkeyPatch.undo()` you already run, or by following the pattern the other admin test files use.
AC1's check now also runs that co-run, deep-link file FIRST, and requires 0 failed. The 7 named tests are unchanged.

## 2. BOUNDS

1. Write surface: exactly the paths in section 3. Change nothing in `server.py` but the new handler, its route line, its
   comment, and (only if needed) a helper shared with `dashboard_root` that keeps `dashboard_root`'s behaviour byte for
   byte. Do not edit `owner_gate.py`, `admin_api.py`, `config.py`, any other module, Terraform, the manifest or `mcportal/`.
   No deploy and no AWS call.
2. Standing rules: no push and no vendor call. Commit via `.tools/safe-commit.sh` with your serial as author (CLAUDE.md
   14a). If you cannot meet a criterion as written, REFUSE it with its measurement. Never repair a criterion.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/server.py
infra/aws/ec2/opal-gateway/tests/test_dashboard_deep_links.py
org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~15/**
org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/**
</paths>

Read, never write: `infra/aws/ec2/opal-gateway/app/owner_gate.py`, `app/config.py`, `tests/test_owner_gate.py`, the
gateway's existing dashboard tests, `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/fwd20/checks/`.

Rows go to `org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, with id
`NFRA_MCPORTAL-Z-W15-S<k>` (the next free k for W15). `surfaced_at` = `date -u +%FT%TZ` at filing. `disarm_owner` on an
ARMED row is `2.0.0_SA_COO~MP`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MP-z-3"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/fwd20/checks/z3.AC1.sh; echo "exit=$?"</invocation><expect>co-run (deep links first): 0 failed; deep-link tests: 0 failed; named tests PASSED 7 of 7 -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~15/NFRA_MCPORTAL.TO-MP-z-3.dashboard-deep-links.proof_of_spec.json`.
Report once, with:
- the check output;
- the commit hash;
- the diff of `server.py` (it is small; paste it);
- any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** cut at the GW issuance (decomposition v7) on `1.0.0_SA_CTO~Z` msg 33519 ("the FWD-20 issuance carries
one cell, an owner-gated route serving index.html for each path in the bundle's route list (an unknown path still
404s), with a test of each"), row Z-S41 @4160a7a9db. Live 404s re-measured by the issuer's z5.AC2 dry run (SSM
f25b53c5): /control-plane, /open-calls, /gateway = 404. Check dry-run at base 8abe56f2cd: AC1 FAIL (test file absent).
Under 100 product lines: worker-light. No gate. Lives through MP-z-5.

<status>pending</status>
<round>1</round>
<workstream>GW</workstream>
<slot>~15</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<status>complete</status>
<!-- REOPENED by the issuer 2026-10-13 ~10:5xZ: AMENDMENT 1 (the catch-all turned POST /mcp from 307 into 405); the same worker continues. -->
<status>in_progress</status>
<!-- REOPENED by the issuer 2026-10-13 ~11:5xZ: AMENDMENT 2 (the test file's teardown pollutes later suites; 7 failed in co-run). Slot ~15 re-seated. -->
