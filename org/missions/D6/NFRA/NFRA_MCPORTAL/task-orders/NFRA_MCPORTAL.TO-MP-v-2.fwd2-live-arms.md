# NFRA_MCPORTAL task order -- `MP-v-2` -- ROUND 5, R-15 (MP-v-1 re-cut): FWD-2's live arms -- a signed-in non-owner is refused everywhere but `/sprint`

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPORTAL/decompositions/NFRA_MCPORTAL_DECOMP.md</decomp_doc>
<owned_cells>MP-v-2</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPORTAL.TO-MP-v-2</to_id>
<issued_to>0.9.0_WK_NFRA_MCPORTAL~3</issued_to>
<issued_by>2.0.0_SA_COO~MP</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one live walk; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM surface; the reads are HTTP to the served gateway plus SSM journal reads.
comp-adversary: DECLARED-NOT-APPLICABLE -- the walk IS the adversary arm (a non-owner identity).
EGRESS CLASS, declared: none beyond Opal's own served gateway `https://mcp.opalinvest.dev` and Microsoft's sign-in page
the ALB redirects to.
</preflight>

## 1. THE CELL -- `MP-v-2` (round 5, decomposition section R5.1; the re-cut of round 3's MP-v-1)

**AMENDMENT 1 (issuer, 2026-10-16 ~07:4xZ).** Your workspace worktree is `C:/tmp/mp-v2-3` (branch `wk-NFRA_MCPORTAL-3`); every shell call of yours resets to the primary checkout, so begin each with `cd C:/tmp/mp-v2-3 &&`. The walk below has THIRTEEN requests, not eight: `admin_api.py` has twelve routes now (the fabric, gateway-breakdown and People routes landed after this order was cut), and the check counts every one.

PRD acceptance A2 (FWD-2): *a second signed-in Opal account refused on every page and every write handler (one request
per handler, denominator printed); `/sprint` served to it.* The dashboard's owner gate (`infra/aws/ec2/opal-gateway/app/owner_gate.py:109-119`)
answers 401 when no verified identity exists and **403 for a verified identity that is not the owner**. The ALB signs
everyone in, so a signed-in colleague reaches the gate and must get 403.

**The account:** `Opal Bloomberg`, the terminal box's own Entra account, which is not the dashboard owner. Its sign-in
takes Entra MFA, a human act. A person will be at the box to type it into the window you open.

**The walk, in order:**
1. Record `t0` (UTC, `date -u +%Y-%m-%dT%H:%M:%SZ`) BEFORE the first request.
2. Launch a HEADED Edge from the portal's own Playwright: a node script that `require`s
   `<worktree>/portal/node_modules/playwright-core` (if your worktree has no `portal/node_modules`, use the main tree's
   `C:/Users/Opal Bloomberg/Desktop/ajb_workspace/portal/node_modules/playwright-core`), then
   `chromium.launchPersistentContext(<a profile dir under your deliverables' .scratch/>, { channel: 'msedge', headless:
   false })`. `chromium.launch()` without `channel` fails on this box, because the pinned Chromium build is not
   installed. Open `https://mcp.opalinvest.dev/sprint`. The shared Playwright MCP is headless and cannot carry MFA, so
   do not use it.
3. Poll (up to 10 minutes) until the page is back on `mcp.opalinvest.dev` and serves `/sprint`. If the sign-in does not
   complete in that time: STOP with a BLOCKING row naming "G-2ND: nobody signed in as Opal Bloomberg". Do not retry
   with another account.
4. From the signed-in page context (`page.request` or `fetch` with credentials), send exactly one request each:
   `GET /`, `GET /api/admin/whoami`, `GET /api/admin/grants/00000000-0000-4000-8000-0000000000e5/00000000-0000-4000-8000-0000000000f6`,
   `POST .../narrow` and `POST .../widen` on that same synthetic pair (body `{}`), `GET /api/admin/changes`,
   `GET /api/admin/fabric/boxes`, `GET /api/admin/fabric/overlap`, `GET /api/admin/fabric/gitstate`,
   `GET /api/admin/fabric/calls`, `POST /api/admin/fabric/calls/close` (body `{}`), `GET /api/admin/gateway/breakdown`
   and `GET /api/admin/people` (thirteen requests in all, one each, AMENDMENT 1). Then
   `GET /sprint` once. Print each status, never a body, cookie or header.
5. Record `t1` (UTC), 60 seconds after the last request. Write
   `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~3/v2_run.json` =
   `{"t0": "...", "t1": "..."}`, plus your script. The script must not write a cookie or token file inside the repo.
   Keep the profile dir under `.scratch/`, which is ignored.

The criteria grade the gateway's OWN access log over SSM for your window, never your printed statuses.

## 2. BOUNDS

1. Thirteen requests, one each, then `/sprint`; no write body beyond `{}`; the synthetic tid/oid pair only (and no call id for `calls/close`). No real person's identifiers.
2. A 200 on any owner route is a finding, not a retry: file a BLOCKING row with the route, and stop.
3. Standing: no push and no vendor call. REFUSE a criterion you cannot meet as written, with its measurement. Never
   repair a criterion.

## 3. SURFACES

<paths>
org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~3/**
org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/**
</paths>

Read, never write: `infra/aws/ec2/opal-gateway/app/`, `portal/node_modules/playwright-core/`,
`org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/round5/checks/`.

Rows go to `org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, with id
`NFRA_MCPORTAL-Z-W3-S<k>` (the next free k for W3).

## 4. PROOF OF SPEC (literal; run from your worktree root after `v2_run.json` is committed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MP-v-2"><invocation>cd C:/tmp/mp-v2-3 && bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/round5/checks/v2.AC1.sh; echo "exit=$?"</invocation><expect>admin_api.py Route census at HEAD=12; refused=13 of 13; admitted=0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MP-v-2"><invocation>cd C:/tmp/mp-v2-3 && bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/round5/checks/v2.AC2.sh; echo "exit=$?"</invocation><expect>GET /sprint in window: 200>=1 -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~3/NFRA_MCPORTAL.TO-MP-v-2.fwd2-live-arms.proof_of_spec.json`.
Report once, with:
- the window;
- the eight statuses you saw;
- the two check lines;
- the commit hash;
- any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** R-15 of ROUND_ANALYSIS.round4.md @460bc0af2f: round 3's MP-v-1 re-cut, after MP-v-1 was superseded
@39ea2d5e3e to clear the project-grain L10. The one change is the eighth request, `GET /api/admin/fabric/boxes`, for
MP-x-1's route. The checks move to `round5/checks/v2.AC*`, where the census is 6 and 7 of 7 must be refused. Window file
`v2_run.json`, same slot `~3`. Checks dry-run at base: AC1 and AC2 FAIL (no window file).

**AMENDMENT 1 NOTE (issuer, ~07:4xZ):** found while readying the window for Andrew's site-Z session (CTO msg 34814). The AC1 census asserted 6 admin routes; `admin_api.py` carries 12 at HEAD and on the live host (d577e0e7297b), so a perfect walk would have failed on a stale denominator. The check now counts 12 routes and 13 requests (the page plus every route) and `_root.sh` anchors to its own file. Dry-run at the base: AC1 FAIL as expected with no window; run against a planted empty window it prints census 12 and `refused=0 of 13`. Not covered (stated, not widened): the SPA deep links (`/gateway`, `/people`, `/control-plane`, `/open-calls`); the PRD's "every page" is read as `GET /` plus every Route, as the order was cut. Gate limb: this modifies an existing order, graded only on `<placeholders>`, which reads NONE.

SPAWN ONLY when ALL hold:
- **MP-x-4 has drained**, so the new route is live and its refusal can be read;
- **G-2ND:** Andrew (or a person he names) is at the box, ready to sign in as Opal Bloomberg in the window the worker
  opens. This is ONE card to Andrew.

<status>cancelled -- Andrew-direct 2026-10-19 ~16:3xZ, the human half is no longer owed (org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261019_163xZ_SIX_HANGING_OPEN_CALLS_RESOLVED.md); the ACs read files the human half would have written and cannot run as written. CTO ruling 1.0.0_SA_CTO~Z msg 36018 (YES, cancel citing the record). FWD grading is the CVO's on the evidence the project holds; no replacement human act is cut.</status>
<round>5</round>
<slot>~3</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
