# P live-scope repair and bounded runtime plan

Authority: current completion CONTRACT.md section 1; CTO operative GO 20260923T051817Z. Andrew directly instructed this P session: **"Proceed"**, then **"go on"** (Codex user channel, 2026-09-23; recorded 2026-09-23T05:30:48.940870+00:00). These instructions continue the live scope/shared wire/runtime repair. They do not authorize unrelated renderer or vendor work.

## Baseline and ownership

Backend isolated baseline cd8d11825424e45fe82f1e78df0396904c0b9ae0; Portal a538217980cdb5d15dc67cdcc98794baeb5e2517, tree equal to published DEV3a298311 / PRODe83ebbfe release portal-v2.1.184. M owns directory, principal scope, header, search and firm UI. P owns shared API client, wire/schema, route and runtime composition. Andrew owns visual smoke.

## Measured defect and runtime

The actual source directory entry returns a selected-set result for resolve-scope; the frontend expects published ResolvedScope and dereferences viewer_policy. Fixing the producer is M-owned. P adds a typed parser refusal and actual Entry-to-client proof once the producer replacement is available. No fabricated scope or permissive fallback.

P independently read AWS account313476888478/us-east-1: directory Lambda Active/Successful, entry.lambda_handler, Python3.12, code cmh6XwybmdXSiWQkQZMeer7wtw0QW/1lXnAIJlPjJKg=, last modified2026-09-21T15:02:21Z. Its IRPT_REQUESTS_TABLE environment member is absent. Current invoke policy already limits access to API7k3ed8px20 scoped IRPT prefix. No API/role mutation performed. API state serial2 contains seven integrations and twelve routes; directory state serial24 contains existing search/refresh resources; core state serial4 contains requests table and KMS key. Protected raw snapshots: isolated backend .runtime/live-scope/. Actual failing authenticated user HTTP response is not yet measured; source mismatch and stale package are concrete defects, not a claimed complete live cause.

## Shared browse seam

Agreed P/M GET /api/scoped/investor-reporting/directory/browse, operation directory-browse; q (empty initial browse), cursor (opaque), limit default25/max100. Response data: entries, next_cursor, directory_revision, scope_fingerprint. Existing v1 outer envelope, including unprojected_grant, preserved. Client rejects malformed or cross-context/stale pages. Server reauthorizes every page and owns cursor binding. No fixture catalogue fallback.

Runtime plan in preparation: target only directory function/dependencies, exact new browse/selection routes and selection storage IAM. Preserve other live routes, integrations, scheduled refresh and held render. No blanket root apply. Awaiting M producer/headers and concrete executable packaging proof; all source-only tests remain distinct from live acceptance.

## Executed targeted Terraform plans (read-only, 2026-09-23 05:31Z)

Worktree canonical Terraform1.9.8 initialized existing API/directory backends; provider5.100.0. Targeting is bounded incident repair, not full-root convergence. API refreshes seven integration data dependencies but CHANGES ONLY two routes; render has no mutation.

- api plan SHA256 `156c4b2a46569336bfbab6a5188d090b57824a662bf21c379ea68ef250217652`: aws_apigatewayv2_route.irpt["GET /api/scoped/investor-reporting/directory/browse"] create; aws_apigatewayv2_route.irpt["POST /api/scoped/investor-reporting/selections"] create
- directory plan SHA256 `c058a53307141c93ffbbe1bbd4601ae905bff8693c9f75a14e78e076d1f27e67`: aws_iam_role_policy.directory_selection create; module.irpt_directory_search.aws_lambda_function.this update

API: GET directory/browse and POST selections, both CUSTOM naqxlm to existing g9302sp; no authorizer, existing route or invoke-policy widening. Directory: add IRPT_REQUESTS_TABLE=irpt-requests to existing function and create directory_selection inline policy. DynamoDB GetItem/PutItem limited to exact irpt-requests ARN and registry client LeadingKeys; KMS exact core key, ViaService=dynamodb.us-east-1.amazonaws.com, encryption-context tableName=irpt-requests. No Scan/Query/Delete/Update permission, destruction or scheduling changes.

These initial plans read the OLD S3 package and do not deploy the code repair. After immutable M/P candidate and ZIP review: canonical single-function build/upload, refresh these targets, verify only exact code hash/version plus environment/policy/routes, obtain scoped CTO adjudication, apply through safe-apply, verify live hash and guarded HTTP journey. No apply yet.


## Live scope repair handoff - 2026-09-23 05:46Z

- Shared backend: LOCAL8827b8730e, includes124c0694b7 on cd8d11825424e45fe82f1e78df0396904c0b9ae0. Browse response/route plus optional directory revision.
- Shared Portal: LOCALcdc60da2, includes321331c1/504b775e on a538217980cdb5d15dc67cdcc98794baeb5e2517. API/parser, firm/fingerprint/revision binding, wire-level nonempty-row validation. No M header files edited.
- Validation: 62 tests /259 assertions PASS across12files; latest new boundary suite7tests24assertions; full TypeScript, targeted ESLint, production Vite build PASS (9.83s). Logs in isolated Portal .runtime/live-scope-client-tests.log and live-scope-build.log. No live PASS asserted.
- Initial read-only Terraform plan receipt475b471784; CTO30069a5254 accepted resource scope and authorized exact single-function artifact staging only AFTER composed regression/package proof. OLD-artifact plans must not be applied. No staging/apply performed yet.
- CVO008107ab97 assertion files extracted byte-for-byte into isolated backend .runtime/bootstrap-replay. candidate_replay.py changes only driver pins/root/output destinations; assertion source is unchanged. Set IRPT_REPLAY_BACKEND_PIN and IRPT_REPLAY_PORTAL_PIN to exact composed pins before executing. Offline .runtime/prove_directory_package.py stages canonical manifest members and verifies pinned blob hashes, import closure and flat cold import; run after M pin/manifest integration.
- Remaining external dependency: M owns actual bootstrap/browse producer and header/search/firm changes. Exact committed candidate requested; last received M message051709 was proposal/read-only evidence, not a repair pin. Shared pins sent053507/053904/054346; CTO dependency coordination requested054557. No inferred M liveness failure and no competing edits.
- Next: merge exact M backend/Portal commits into isolated P branches using safe-merge; run unchanged CVO bootstrap and cursor/auth negative controls; repin exact directory manifest and cold-package proof; canonical single-function upload per30069a5254; refresh exact API/directory plans and return final plan hashes for CTO apply decision; canonical deployment and real guarded HTTP acceptance; Andrew visual smoke.
- Live diagnostics04:50-05:44Z: two CloudWatch pages,19events, no continuation; six START/END/REPORT sets and no error marker. This does NOT establish success or the authenticated user response. Protected raw window in isolated backend .runtime/live-scope/directory-log-window-protected.json.

## Andrew local preview instruction - 2026-09-23 05:47Z

Codex user channel, verbatim: "bun run dev build the localhost on 5173 and let me check it out". Started latest P Portal cdc60da2 via bun run dev --host127.0.0.1 --port5173 --strictPort, hidden process bunPID26600/VitePID15164. HTTP root200; Vite ready623ms. URL http://localhost:5173/. Main workspace and other listeners unchanged. This preview does not include the awaited M bootstrap/header candidate. Build already PASS; CTO054659 confirms retain candidate and await exact M handoff.
