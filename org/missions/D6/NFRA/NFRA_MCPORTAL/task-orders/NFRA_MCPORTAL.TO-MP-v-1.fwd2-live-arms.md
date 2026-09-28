# NFRA_MCPORTAL task order -- `MP-v-1` -- ROUND 3, E4: FWD-2's live arms -- a signed-in non-owner is refused everywhere but `/sprint`

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPORTAL/decompositions/NFRA_MCPORTAL_DECOMP.md</decomp_doc>
<owned_cells>MP-v-1</owned_cells>
</decomp_ref>
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

## 1. THE CELL -- `MP-v-1` (round 3, decomposition section R3.2)

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
   `POST .../narrow` and `POST .../widen` on that same synthetic pair (body `{}`), and `GET /api/admin/changes`. Then
   `GET /sprint` once. Print each status, never a body, cookie or header.
5. Record `t1` (UTC), 60 seconds after the last request. Write
   `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~3/v1_run.json` =
   `{"t0": "...", "t1": "..."}`, plus your script. The script must not write a cookie or token file inside the repo.
   Keep the profile dir under `.scratch/`, which is ignored.

The criteria grade the gateway's OWN access log over SSM for your window, never your printed statuses.

## 2. BOUNDS

1. Seven requests, one each; no write body beyond `{}`; the synthetic tid/oid pair only. No real person's identifiers.
2. A 200 on any owner route is a finding, not a retry: file a BLOCKING row with the route, and stop.
3. Standing: no push and no vendor call. REFUSE a criterion you cannot meet as written, with its measurement. Never
   repair a criterion.

## 3. SURFACES

<paths>
org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~3/**
org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/**
</paths>

Read, never write: `infra/aws/ec2/opal-gateway/app/`, `portal/node_modules/playwright-core/`,
`org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/round3/checks/`.

Rows go to `org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, with id
`NFRA_MCPORTAL-Z-W3-S<k>` (the next free k for W3).

## 4. PROOF OF SPEC (literal; run from your worktree root after `v1_run.json` is committed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MP-v-1"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/round3/checks/v1.AC1.sh; echo "exit=$?"</invocation><expect>admin_api.py Route census at HEAD=5; refused=6 of 6; admitted=0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MP-v-1"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/round3/checks/v1.AC2.sh; echo "exit=$?"</invocation><expect>GET /sprint in window: 200>=1 -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~3/NFRA_MCPORTAL.TO-MP-v-1.fwd2-live-arms.proof_of_spec.json`.
Report once, with:
- the window;
- the seven statuses you saw;
- the two check lines;
- the commit hash;
- any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** E4 of ROUND_ANALYSIS.round2.md @33ca99c40e. A2's third arm, Andrew admitted, was measured by E1
(`owner_gate.py:113-118` prints the claims line only after `is_owner`; the access log shows `GET / 200` at 14:59:58Z),
so it is not re-run. Checks dry-run at base: AC1 and AC2 FAIL as expected (no window file). CONTROLS with a window over
12:59-15:01Z: AC1 FAILS on `admitted=1` (Andrew's own 200, which proves the admitted-arm guard discriminates) with the
census at 5; AC2 PASSES on 3 `/sprint` 200s.

SPAWN ONLY when **G-2ND** holds: Andrew (or a person he names) is at the box, ready to sign in as Opal Bloomberg in the
window the worker opens. This is ONE card to Andrew.

<status>staged</status>
<round>3</round>
<slot>~3</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
