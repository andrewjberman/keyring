# TO IRPT_BCKEND.TO-IB-pr-307 -- the API Gateway authorizer (V2) admits a render token on the 49F reporting SERIES route, as the edge (V3) already does

<to_id>IRPT_BCKEND.TO-IB-pr-307</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~110</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-10-03</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>42</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** CTO RULINGS batch 226 (msg 104702): "S307 RULED FIX FORWARD. Cut the
authorizer cell now: RENDER_ROUTE_CLAIMS gains the reporting-series route for render-delegate only, pinned like IB-pr-304's edge."
GATE (x) puts this in ROUND 42 (row S267). | **Decomp cell:** `IB-pr-307` (decomposition section 34) | **outcome_ref:** P-6 (the
export) | **depends_on:** none. It is BUILT now; it is SERVED under its own never-widen half (the CTO signs it on receipt).

---

## WORKER FACE

**What is broken.** On PROD, a 49 Financial export refuses `DEPENDENCY_UNAVAILABLE`, and row IRPT_BCKEND-S307 holds the trace.
- The export's submit reads the account's series through the reporting route as the submitter's RENDER DELEGATE (a render
  token, `aud irpt-render`).
- The edge (V3, `infra/aws/lambda-edge/auth-validator-edge/render_auth.mjs`) admits that token on
  `/api/scoped/investor-reporting/reporting/{id}/series`.
- The API Gateway authorizer (V2, `C:/Users/AndrewBerman/Desktop/<your worktree>/infra/aws/users/lambda/portal-authorizer/index.mjs`)
  then refuses it. Its `RENDER_ROUTE_CLAIMS` (lines 56-60) holds only three routes, so it logs
  "Render token presented on a non-render route: GET /api/scoped/investor-reporting/reporting/{account_id}/{which}".

**What you build, in `index.mjs`'s render branch only** (from `const RENDER_ROUTE_CLAIMS` through the end of
`authorizeRenderToken`; nothing outside it changes, which criterion IB42-1-AC2 checks):
1. **Add the route.** `'GET /api/scoped/investor-reporting/reporting/{account_id}/{which}'` joins `RENDER_ROUTE_CLAIMS`, and the
   three existing routes keep their exact behavior.
2. **Map the path parameter to the claim.** Today `authorizeRenderToken` compares `event.pathParameters[claimName]` with
   `decoded[claimName]`, which assumes the path parameter and the claim share a name. For this route the path parameter is
   `account_id` and the claim is `accountSetId`: the export pins `accountSetId` to the account at
   `infra/aws/lambda/investor-reporting/export/retained_export.py:308`.
   - Give the route a path-parameter-to-claim mapping. Any shape works, for example an entry
     `{param: 'account_id', claim: 'accountSetId'}`, while the three existing string entries keep meaning param = claim.
   - The id must still match exactly, or the request is denied.
3. **Series only.** For this route, `event.pathParameters.which` must equal `'series'`, or the request is denied. This mirrors
   V3's rule: "the series path only, never the manifest or the client summary". The summary route
   (`GET .../reporting/client/{client_id}/summary`) stays out of `RENDER_ROUTE_CLAIMS`, so it is denied as a non-render route.
4. **Context.** On success the authorizer context is the same as the other render routes (`renderDelegate: 'true'`, and so on).
   Change nothing else.

**Tests.** Create `infra/aws/users/lambda/portal-authorizer/tests/test_render_reporting_series.mjs` using `node:test`. It must hold
at least 6 tests and name `series`, `manifest`, `accountSetId` and `summary`:
- the series route with a matching `accountSetId` -> authorized, `renderDelegate` `'true'`;
- the same route with `which` = `manifest` -> denied;
- a render token whose `accountSetId` is a DIFFERENT account (a foreign account) -> denied;
- the summary route key -> denied (non-render route);
- a forbidden claim (for example `tier internal`) on the series route -> denied;
- the existing performance route with a matching `accountSetId` -> still authorized (regression).

Use throwaway RSA keypairs generated in-process, and inject the public key through `IRPT_RENDER_JWT_PUBLIC_KEY_PEM`, the
existing seam at `index.mjs:62-68`.

**Two environment facts, measured by the issuer:**
1. `node_modules` is gitignored, so your worktree has none. COPY
   `C:/Users/AndrewBerman/Desktop/ajb_workspace/infra/aws/users/lambda/portal-authorizer/node_modules` to the same path in your
   worktree. It is a local copy: never run npm, bun install or any network install, and never commit it.
2. `index.mjs` cannot be imported bare by a test. It imports `../../../lambda/lib/authkeys/jwtPublicKeys.mjs`, which imports
   `@aws-sdk/client-secrets-manager`, and that package resolves from a directory with no `node_modules` (the Lambda runtime
   supplies it).
   - Make the test import a bundle instead, the deploy script's own way. `bun build index.mjs --format=esm --target=node`, with
     `--external` for each `@aws-sdk/*` package, into a temporary file under `portal-authorizer/tests/` that is removed after
     the run and never committed. That bundle resolves `@aws-sdk` from `portal-authorizer/node_modules`.
   - Or use another way that needs no install. bun is at `/c/Users/AndrewBerman/.bun/bin/bun`.
   - If a render-path test needs `SecretsManagerClient`, patch it, the way
     `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~15/test_edge_render_delegate_v2_authorizer.mjs:47-70` does.

<criterion id="IB42-1-AC1" cell_refs="IB-pr-307"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r42/p42_authorizer_reporting_series.py" . IB42-1-AC1</invocation><expect>IB42-1-AC1 PASS</expect></criterion>
`IB42-1-AC1` -- `RENDER_ROUTE_CLAIMS` (read from the source) holds the reporting route beside the three existing routes, and the new
test file names the four words and passes at least 6 tests with 0 failed. Base: FAIL (three routes, no test file).

<criterion id="IB42-1-AC2" cell_refs="IB-pr-307"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r42/p42_authorizer_reporting_series.py" . IB42-1-AC2</invocation><expect>IB42-1-AC2 PASS</expect></criterion>
`IB42-1-AC2` -- a GUARD: `index.mjs` outside the render branch is byte-unchanged against 3376d7b446, so the human token path does
not move. Base: PASS.

<expected_criteria>IB42-1-AC1,IB42-1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below.
- **AWS:** none. No build, upload, deploy, invoke or Secrets Manager read. The deploy is the issuer's, under its own never-widen
  half.
- **Refusal clause.** Any change outside the render branch, a new dependency, a network install, or a render route beyond the
  series route (the manifest or the summary) is a defect: stop and file a row.

<paths>
infra/aws/users/lambda/portal-authorizer/index.mjs
infra/aws/users/lambda/portal-authorizer/tests/test_render_reporting_series.mjs
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~110/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read without a grant (never written): `infra/aws/lambda-edge/auth-validator-edge/`, `infra/aws/lambda/investor-reporting/`,
`infra/aws/lambda/lib/authkeys/`.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 34 (round 42, workstream ~P), cell `IB-pr-307`.
<owned_cells>IB-pr-307</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB42-1-AC1, IB42-1-AC2. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~110/IRPT_BCKEND.TO-IB-pr-307.authorizer-reporting-series-render-route.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IB42-1-AC1,IB42-1-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message must give:
- the commit hashes, and each criterion's last line;
- the mapping shape you chose;
- every test, with its expectation;
- the bundling or import method you used;
- any surprise row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- opal-portal-authorizer is the API Gateway authorizer of every portal API route; the change is confined to its render-token branch (aud irpt-render, a separate key) and the human path is byte-unchanged (AC2); 0 served bytes move in the cell; its deploy is a separate never-widen half the CTO signs on receipt (batch 226), with two PROD arms (a 49F export outside the six reaches its receipt; a foreign-account render token refuses).
comp-iam: DECLARED-NOT-APPLICABLE -- no role changes.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is added or removed; the authorizer's decision on one existing route changes for render tokens only.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- IB42-1-AC1 base FAIL (keys are the three existing routes), IB42-1-AC2 base PASS (guard), dry-run at the base 2026-10-03 ~19:2xZ.
lane: the <paths> block IS the grant.
</preflight>
