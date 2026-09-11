# TO IRPT_BCKEND.TO-IB-s-15 -- THE SCOPED ROUTES, THE OPAL PRINCIPAL CLASS AND THE CLOUDFRONT BEHAVIOR: /api/scoped/investor-reporting/ on the portal API under the existing authorizer, the permitted-firm catalogue, and the one behavior that makes the prefix reachable

<to_id>IRPT_BCKEND.TO-IB-s-15</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~2</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-10</issued_date>
<status>staged -- assigned to slot ~2; becomes pending when the COO hands it over after IB-s-12 is terminal and merged AND IB-s-10, IB-s-11, IB-s-14 and IB-s-16 are terminal and merged.</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_BCKEND_PRD.md` v0.4 @62301f71e0 | **Decomp cell:** `IB-s-15` (`../decompositions/IRPT_BCKEND_DECOMP.md` v0.1.1, s.1 + s.2) | **outcome_ref:** FWD-11 (contrib), FWD-2 (own) | **PRD candidate:** B15

---

## IDENTITY AND WORKTREE

- **Serial:** `0.9.0_WK_IRPT_BCKEND~2`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_IRPT_BCKEND~2;`.
- **Worktree:** `/c/tmp/wk-irpt-1-2` on branch `wk-irpt_bckend-1-2`, cut by the issuer from `HEAD` of `CLOUD` at hand-off. First act: `git rev-parse --abbrev-ref HEAD` and `test -d org && test -d .tools && echo TREE-OK`; a worktree that does not carry the paths this face names is a BLOCKING row and a stop.
- **Repo root for every path below:** the worktree. Every path in this face is relative to that root; make it absolute by prefixing `/c/tmp/wk-irpt-1-2/`.
- **Commit:** `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~2 <0.9.0_WK_IRPT_BCKEND~2@opal.agent>" -F <msgfile> -- <paths>`, `<msgfile>` written with the Write tool. On your branch only; never push, merge, rebase, `checkout --` or `clean`.
- **Deliverables:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/` (granted by the tree convention; no `<paths>` entry needed).
- **Queue:** sixth and last in slot ~2, after IB-s-12; cross-slot waits on IB-s-10 (~3), IB-s-11 and IB-s-14 (~4), IB-s-16 (~1). IB-sb-3 (slot ~1) waits on this cell.

---

## THE CELL

**The PRD row, verbatim at @62301f71e0 (the one carrier; the acceptance clause draft is the bar you build to):**

- **cell:** B15 Global entitlement class + `api/scoped/investor-reporting/...` routes + permitted-firm catalogue
- **serves:** FWD-11 (contrib), FWD-2 (own)
- **brief sections consumed:** O8; IV.2 Global/scoped integration sources
- **contracts (P=produces, C=consumes):** P `ResolvedScope.principal class / permitted-firm catalogue`
- **paths: reuse:** `infra/aws/terraform/partners-api/api-gateway.tf` (`/api/scoped/advisor-intelligence/` CUSTOM auth); `infra/aws/lambda-edge/auth-validator-edge/index.mjs`; `portal/src/pages/ModelPortfolios.tsx` (pattern reference only)
- **paths: new home:** `/api/scoped/investor-reporting/...` routes under `infra/aws/terraform/investor-reporting/`
- **fixtures / evidence:** --
- **acceptance clause draft:** an Opal principal reaches clients at two firms through scoped routes; a firm advisor replaying the same requests is refused; same client + revision gives identical values Global vs firm-scoped; revoking Global permission takes effect; the actual authorizer, handler and storage enforcement are traced before implementation -- the MP demo-to-global translation and missing-claim fallback are NOT copied

**What L5 adds (decomposition v0.1.1 s.2, s.6, s.9):**

- **Routes:** `infra/aws/terraform/investor-reporting/api/` declares `aws_apigatewayv2_route` resources on API `7k3ed8px20` with `authorization_type = "CUSTOM"` and `authorizer_id = "naqxlm"` (the pattern at `infra/aws/terraform/partners-api/api-gateway.tf:15-31`), integrations (`aws_apigatewayv2_integration`, AWS_PROXY) to THIS project's handler Lambdas read by data source (`data.aws_lambda_function`): directory search/resolve (IB-s-1), performance (IB-s-11), analysis request/status/sections (IB-s-9/IB-s-10 through the status handler), holdings (IB-s-12), export/receipt/download (IB-s-14), status (IB-s-16). Route keys under `/api/scoped/investor-reporting/...`, enumerated in `routes.json` so the replay battery (IB-sb-3) reads its denominator from a file, not from memory.
- **The CloudFront behavior (row `IRPT_BCKEND-S2`):** ONE `ordered_cache_behavior` for `/api/scoped/investor-reporting/*` -> the `APIGateway-portal` origin with `viewer-request: auth-validator-edge`, added to `infra/aws/terraform/portal-auth/cloudfront-distribution.tf` in the EXACT shape of the neighbouring `/api/scoped/partners/*` behavior (read it; copy its cache policy, origin request policy and Lambda association; change only the path pattern and the comment). Applied from the `portal-auth` root under ITS OWN ledger entry (slug `irpt-bckend-s15-cloudfront`), a served-surface act: `terraform plan` MUST show exactly ONE change (the added behavior) before the apply, printed verbatim in the instance; any other change in that plan is a STOP and a BLOCKING row.
- **The Opal principal class and the permitted-firm catalogue** in `_scope/` (IB-s-2's module): an authenticated Opal entitlement class (from the claim IB-s-2 traced -- if IB-s-2 found it NOT distinguishable, this cell's Phase 1 traces `infra/aws/lambda-edge/auth-validator-edge/index.mjs` and the authorizer `opal-portal-authorizer` for the claim and records the finding; it does NOT copy `ModelPortfolios.tsx`'s demo-to-global translation or its missing-claim fallback as a grant), a permitted-firm catalogue read from `data/firm_registry.json`, selected-firm resolution to ONE verified firm and its exact permitted account set for request, report, job and export; a firm advisor can never acquire cross-firm permission by selecting Global or swapping identifiers; the same client + revision returns identical values Global vs firm-scoped.
- Proof: `get-routes` on the API lists every route in `routes.json` with the authorizer id (`N of N`); `get-distribution-config` carries the new behavior; an UNAUTHENTICATED `curl` to `https://<portal host>/api/scoped/investor-reporting/status` returns 401/403 (the difference control against the pre-behavior state, where the SPA answered 200 -- record the pre-apply status too); the Global logic on in-memory handlers with two firms' fixtures.

**ISSUER AMENDMENT (2.0.0_SA_COO~B, 2026-09-11 ~01:1xZ, at the IB-s-2 drain, before this order was handed -- the disarm of row `IRPT_BCKEND-W2-S7`, whose disarm_owner is the issuer):**
- **THE PERMITTED SET IS AN INTERSECTION THROUGH AN INJECTED SEAM, AND THIS CELL WIRES THE SEAM.** IB-s-2 (merged at 22a125e098) found that `resolve(headers, directory)` cannot produce a permitted account set from its two named inputs: no header carries an account claim and `DirectoryEntry.ids` carries no advisor. The resolver therefore takes an OPTIONAL third input -- the ownership map the edge validator itself reads (`s3://opal-data-{alias}/platinum/{firmId}/ownership_map.json`, `advisors[advisorId].{accounts,relationships}`) -- and the permitted set is the INTERSECTION of that grant with the verified firm's directory population. The map is keyed in the custodian id space and the directory in the opaque `sha256(namespace|firm|kind|raw)[:24]` space, so the join needs a projection, injected as `id_projection` (`infra/aws/lambda/investor-reporting/_scope/resolve.py`, `advisor_grant` / `unmatched_reasons`). **The hazard is that an ABSENT projection fails safe and silent: the advisor sees nothing, which reads exactly like a correct revocation.** This cell's handlers and `_scope/global.py` therefore (i) pass a REAL `id_projection` -- ONE definition of the opaque id shared with `directory_runner.opaque_id`, imported from one module (the shared layer `irpt-common` of IB-s-13 is the intended home; if that layer has not merged when you build, a module under `_scope/` that the runner is NOT edited to import is a BLOCKING row, not a second definition); (ii) treat a request whose scope was resolved with NO projection while a grant was present as a REFUSAL with reason `UNPROJECTED-ID`, never as an empty permitted set served as 200; and (iii) surface `unmatched_reasons` in the scope object the handlers log, never in the response body.
- **OPAL_GLOBAL IS NEVER MINTED FROM HEADERS.** IB-s-2's Phase-1 finding: the discriminating claim `firmRole` is read at `index.mjs:205` and injected 0 times; `index.mjs:184-185` and `:202-204` contradict each other on `role==='admin'`; `tier`/`userType` are free-text with no registry. So the Opal principal class comes from an explicit SERVER-SIDE ROSTER the resolver already accepts (empty by default), and a `role=admin` caller with a verified firm resolves `FIRM_OPERATIONS`. This cell builds the roster path (`_scope/global.py`, roster read by NAME from a parameter or secret, never a literal in code); the one-line edge fix beside `index.mjs:390` is a served-output act on a distribution fronting 28 behaviors and is OUTSIDE this order's `<paths>` -- if the roster path cannot satisfy arm (d), that is a BLOCKING row naming `CLOUD_OPS_OR_ETL`, never an edit to the edge function.
- **THE PRINCIPAL-CLASS VOCABULARY IS THE CONTRACT'S** (row `IRPT_BCKEND-W2-S8`): `OPAL_GLOBAL | FIRM_ADVISOR | FIRM_OPERATIONS | CLIENT | UNKNOWN` from `_contracts/ResolvedScope.schema.json`; the face's `firm-advisor | firm-admin | opal` are prose names for the first three. Build a third spelling nowhere.

**ISSUER AMENDMENT (2.0.0_SA_COO~B, 2026-09-11 ~01:4xZ, at the IB-s-3 drain, before this order was handed -- the disarm of rows `IRPT_BCKEND-W2-S9` and `IRPT_BCKEND-W2-S10`, whose disarm_owner is the issuer; recorded as channel row `IRPT_BCKEND-S9`):**
- **EVERY HANDLER THIS CELL SHIPS IS WRAPPED BY `_authz.guard()`** (`infra/aws/lambda/investor-reporting/_authz/enforce.py`, merged at 3cca035c66): resolve, reauthorize before serving, keys through `_keys`, one refusal envelope. A handler reachable through a route without `guard()` is a defect this cell's own battery prints: `_authz.unguarded_routes()` over the routes this cell registers reads `0 of N`, N printed. Where this cell ships no handler, the same census runs over `routes.json` at the replay.
- **THE FIRM ID HAS TWO SPELLINGS AND ONLY `_authz.FirmBinding` RECONCILES THEM (row W2-S9).** `X-Firm-Id` and `_keys.cache_key` carry the REGISTRY id (`49financial`); `DirectoryEntry.ids.firm_id` and the `_scope` cross-firm filter carry the OPAQUE id (`fir_...`, `directory_runner.opaque_id`). A handler that passes the header value into the directory join returns an EMPTY population that reads exactly like a revocation, and no per-module test can see it. Every firm-scoped read this cell makes binds through `FirmBinding`, proven against the directory artifact's own `firm_id_opaque`; a binding that does not reconcile is a REFUSAL (`FIRM_BINDING`), never an empty set. No hash is recomputed and `opaque_id` is not duplicated into a Lambda.
- **A `_keys` REFUSAL NAMES THE REFUSED VALUE (row W2-S10).** `KeyComponentRefused` carries the component with `%r` at twelve message sites; `str(exc)` in a response, a log line, an audit row, a battery print or a surprise row DISCLOSES exactly the value that was refused for being a client name or an e-mail address. Nothing this cell writes surfaces a `_keys` exception's text: the wrapper's refusal reason (parameter NAMES, found through the public `cache_key`) is the only refusal that leaves a handler, and at least one test asserts over the WHOLE envelope (body + reason + audit trail), never the census alone. `_keys` itself is not edited by this cell (not in its `<paths>`; the sanitised exception is the issuer's round-2 item on IB-s-17's surface).
- **A THIRD ID SPELLING (row W2-S11, ARMED, disarmed here by the issuer at the IB-s-4 drain):** `HoldingsSnapshot.scope.account_ids` carries a NAMESPACE PREFIX (`<firm>:acct:acc_...`) while `DirectoryEntry` carries the bare opaque tail (`acc_...`); joined AS WRITTEN they read `0 of N` for ALL THREE firms, which is a prefix difference and cosmetic, on top of the REAL raw-key difference of W1-S7 that affects INF and COT only. Any read this cell makes that joins holdings to the directory normalises through the ONE normaliser IB-s-4 shipped under `infra/aws/lambda/investor-reporting/directory/` (import it; never a second strip), and prints BOTH counts per firm -- resolved as written and resolved after normalisation -- so the two causes stay distinguishable (expected shape at HEAD: 49F 5,856 of 5,873 after, INF 0 of 790, COT 0 of 946). No join is changed; which spelling is canonical is the CTO's L10 read.
- **THE DEPLOYED EXPORT WORKER REPORTS RENDERER ABSENCE (row W4-S9, ARMED, disarmed here by carry):** `irpt-export-render` is live with `IRPT_EXPORT_RENDERER=unavailable` set explicitly and no `s3:PutObject` / `kms:Decrypt` grant, because a python3.12 Lambda has no headless browser and fetching one is egress the estate refused (rows W3-S1/S2). The render mechanism is proved in the worktree on the estate's existing local Edge path. This cell grades the export ROUTE on the function's own ABSENCE REPORT (reason code present, no credential/infra payload), never on a render; the headless runtime (container image, browser layer or out-of-Lambda worker) is a round-2 build decision at L10. Its layer carries 2 of 5 IRPT contracts (row W4-S10): the export contracts resolve from the repo path in tests and are ABSENT on the runtime -- print which resolution branch answered.
- **A CLIENT NAME CAN REACH A DURABLE S3 KEY THROUGH `_keys.s3_evidence_key` (row W3-S12, ARMED, routed by the issuer):** that function checks non-empty / no slash / not lock-shaped / not a foreign firm token and NEVER calls the shape checks `cache_key` does, so `"Whitfield Family"` or an e-mail address lands in `firms/<firm>/generations/<...>/` -- in access logs, CloudTrail, Inventory and every ListObjects, un-loggable. `_keys` is IB-s-17's surface (round 2). Every S3 key this cell builds or replays passes through a shape check BEFORE `s3_evidence_key` (IB-s-10's wrapper is the pattern), and the replay censuses every key it observes for name-shaped or e-mail-shaped components (`0 of N`, N printed); a hit is a FAIL, never a note.
- **THE DIRECTORY AND PERFORMANCE HANDLERS ALREADY MERGED (IB-s-1, IB-s-11) PREDATE THE WRAPPER** -- a decomposition sequencing defect of the issuer, carried to L10; this cell does not edit them, and IB-sb-3's replay is where their unguarded state is measured.

---

## DELIVERABLE

`infra/aws/terraform/investor-reporting/api/` (`routes.tf`, `integrations.tf`, `routes.json`, `main.tf` completed); the ONE behavior in `infra/aws/terraform/portal-auth/cloudfront-distribution.tf`; `infra/aws/lambda/investor-reporting/_scope/global.py` + `tests/`; TWO ledger entries + sentinels (api; cloudfront); the battery `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/battery_ib_s_15.py` and `.result.md`.

---

## BOUNDS

- **The CloudFront plan shows exactly ONE change or you STOP.** The distribution serves the whole portal; a plan that touches any other behavior, origin or setting is a BLOCKING row, never an apply.
- **No existing route, behavior or origin is edited.**
- **No new all-firm financial aggregate.** Global is a selector over firms; every result is one firm's, attributed.
- **Do not copy the Model Portfolios demo-to-global translation or its missing-claim fallback.**

### Bounds every order carries (decomposition v0.1.1 s.8, verbatim)

1. **NO LIVE VENDOR CALL.** Endpoint, verbatim: *"NO LIVE VENDOR CALL is authorized by this document -- availability is not authorization; a live YCharts, Black Diamond or Orion call needs Andrew's explicit per-use word."* The same bound covers the mailbox read. A cell that carries a live arm proves its MECHANISM against recorded fixtures through a transport stub with a difference control; the live arm is an express qualification read by the CTO at L10 on Andrew's per-use word, never something this order does.
2. **NO MONITOR, ALARM, SNS OR SES SEND.** Nothing in this project notifies anyone. A scheduler this project creates is the product's own trigger and is applied `DISABLED` where its first fire would be a vendor call.
3. **CROSS-FIRM, both shapes.** Per-firm prefixes + IAM conditions in the shared bucket; the FIRM's own bucket for directory and holdings data; the `FirmDestinationPolicy`; the firm fixed from the sender's domain at ingestion and immutable after; Global GRANTED to an Opal principal, never to a firm one; no new all-firm financial aggregate.
4. **Deploys (NEVER-2, NEVER-9).** `.tools/safe-apply.sh` only, from a root whose state key is this cell's; a change-management entry opened at the start (`python .tools/deploy_ledger.py open ...`) and closed at completion, the sentinel `org/critical_paths/.open_deploys/<slug>.json` COMMITTED; ORDER on any act that changes the world: open the entry, ACT, close the entry and COMMIT it BEFORE taking the reads that grade the act; served bytes verified as `CodeSha256` against the built zip, never by filename; `aws lambda update-function-code` never; `.tools/terraform.exe` is provisioned in your worktree by the issuer -- use it by that path, never a PATH substitute (a substitute re-pins remote state).
5. **Andrew's four fixed constraints are not build choices:** the BDAPI-with-Kimi runner STYLE with NO OTP branch; the firm from the sender's domain at ingestion gated to enumerated destinations; the multitenant `api/scoped/` layout; terminated clients STAY VISIBLE under entitlement. And the endpoint's: units are part of a number's meaning; unsupported positions are never silently removed; no PUT of global YCharts preferences; no vendor call in render or preview; missing history is an answer, not an empty state; the narrative states contemporaneity and never causes; model targets never masquerade as observed holdings.
6. **No credential in any artifact, log, fixture or commit.** Secrets are read by NAME at runtime; a recorded fixture is scrubbed before it is committed; signed URL parameters are never logged; a `describe-secret` prints version state, never a value.
7. **No served output is touched.** The 28 existing CloudFront behaviors, the 14 existing scoped routes and every existing bucket, table and Lambda are read, never edited, except where THIS order's cell says it ADDS a resource.
8. **The spec is FROZEN mid-round.** A premise that does not hold, a path that is not where this face says, a result the invocation does not produce, a capability you lack: ONE row at `org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md`, id `IRPT_BCKEND-W<your slot>-S<k>`, per `org/surprise_channel/schemas/investigation_item.schema.json`, inside the fenced json array, appended never edited; then keep working. Never edit this face, never widen the order, never fix a neighbouring defect.
9. **Every invocation terminates.** You run each named invocation under `timeout`; rc 124 IS the recorded output, retried once at most.
10. **Every `.py` edit passes `.tools/commit-gate.sh`.** Python 3.12 (`Python312` first on PATH; bare `python` may resolve to 3.14 without PyYAML). ASCII only in production code, logs and AWS names (`OK:`/`WARN:`/`ERROR:`/`SKIP:`/`BLOCKED:`).
11. **Scratch** is `<your worktree>/.scratch/` only.

---

## ACCEPTANCE

<criterion id="S15-AC1" cell_refs="IB-s-15"><invocation>timeout 600 python org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/battery_ib_s_15.py</invocation><expect>IBS15-ROUTES-LIVE</expect></criterion>
**`S15-AC1` -- PASSES BY OUTPUT -- the routes and the behavior live, the prefix refuses unauthenticated, Global proven on fixtures.**
**(a) EVERY ROUTE, THE AUTHORIZER.** `aws apigatewayv2 get-routes --api-id 7k3ed8px20` filtered to the prefix: every key in `routes.json` present with `AuthorizerId naqxlm` (`N of N`); each integration targets one of this project's Lambda ARNs (census).
**(b) THE BEHAVIOR IS LIVE -- THE DIFFERENCE CONTROL.** Pre-apply: an unauthenticated request to the prefix returned the SPA (status and first bytes recorded); post-apply: `get-distribution-config` lists the behavior with the edge association, and the same request returns 401 or 403. Both printed.
**(c) EXACTLY ONE CHANGE.** The saved `terraform plan` output for `portal-auth` before the apply shows `1 to add, 0 to change, 0 to destroy` or an in-place update touching only the new behavior block; printed verbatim.
**(d) GLOBAL, ON FIXTURES.** An Opal principal selects clients at two firms and each result carries its firm; a firm advisor replaying the same requests is REFUSED; the same client + revision gives identical values Global vs firm-scoped (hash equal); revoking the Global entitlement in the fixture takes effect. `4 of 4`.
**(e) THE CATALOGUE IS THE REGISTRY.** Permitted firms == enabled client firms in `data/firm_registry.json` (`3 of 3`).
**(f) TWO LEDGERS CLOSED.** Both sentinels committed (hashes).
**(g) THE SEAM IS WIRED, AND ITS ABSENCE IS LOUD (amendment, row W2-S7).** With a fixture ownership map granting N custodian ids: projection PRESENT -> the permitted set is the intersection, `N of N` matched or each unmatched id carrying one of `CROSS-FIRM | NOT-IN-DIRECTORY | UNPROJECTED-ID`; projection ABSENT with a grant present -> the request is REFUSED with `UNPROJECTED-ID`, never served as an empty 200; and the projection's opaque id equals `directory_runner.opaque_id` on 3 of 3 sample raw ids (one definition, printed with the module path it was imported from). Three outcomes printed.

**(amend) GUARDED, BOUND, AND SILENT ON THE REFUSED VALUE (issuer amendment at the IB-s-3 drain, rows W2-S9 / W2-S10).** `unguarded_routes()` over this cell's routes reads `0 of N` (N printed); every firm-scoped read binds through `FirmBinding` and a fixture with a non-reconciling binding is REFUSED with `FIRM_BINDING` rather than served empty; a fixture that keys by a client display name is refused and the whole envelope (body + reason + audit trail) contains 0 occurrences of the refused value (census printed). Where this cell ships no handler, the arm reads over `routes.json` at the replay. CLARIFIED at the IB-s-7 drain (row W3-S5, disarm by the issuer): `routes.json` is IB-s-15's deliverable at `infra/aws/terraform/investor-reporting/api/routes.json` and does not exist before that cell lands; a cell that ships no handler and runs before it does NOT report a `0 of 0` census as a pass -- it prints the census AS VACUOUS and runs the two CONTROLS IB-s-7's battery ran (a handler registered unguarded censused `1 of 1`; the same handler wrapped censused `0 of 1`), so the arm proves the censor, not an empty set. IB-s-15 and IB-sb-3 read the real file.

<criterion id="S15-AC2" cell_refs="IB-s-15"><invocation>timeout 120 .tools/terraform.exe -chdir=infra/aws/terraform/investor-reporting/api plan -no-color -input=false -lock=false</invocation><expect>No changes\. Your infrastructure matches the configuration\.</expect></criterion>
**`S15-AC2` -- THE API ROOT IS CONVERGED after this cell's apply.**
Run after the apply and after the ledgers close. (The `portal-auth` root's convergence is read the same way and printed in arm (c)'s record; it is not a second criterion because that root is not this project's.)

<criterion id="S15-AC3" cell_refs="IB-s-15" judgment="true"/>
**`S15-AC3` -- JUDGMENT, RECORDED AND NOT SELF-GRADED.** State for `3.0.0_SA_CVO`: how the Opal principal is distinguished (the claim, the file, the line) and whether it required a change outside this project (name the seat that owns it); what the unauthenticated 401/403 proves and does not prove about an AUTHENTICATED cross-firm request (IB-sb-3's territory); and whether the `portal-auth` apply changed anything you did not intend (the plan is the evidence). No verdict: the instance row carries the output under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming `3.0.0_SA_CVO` at L9.


<expected_criteria>S15-AC1, S15-AC2, S15-AC3</expected_criteria>


<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-s-15.scoped-routes-opal-principal-and-the-cloudfront-behavior.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
infra/aws/terraform/investor-reporting/api/
infra/aws/terraform/portal-auth/cloudfront-distribution.tf
infra/aws/lambda/investor-reporting/_scope/
infra/aws/lambda/investor-reporting/PATH_MANIFEST.json
org/critical_paths/.open_deploys/irpt-bckend-s15-cloudfront.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/irpt-bckend-s15.json
infra/aws/lambda/ci/lambda-source-map.json
</paths>


<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> v0.1.1, cell `IB-s-15` (s.1 the rectangle; s.2 the L5 note; s.6 the root; s.8 the bounds).
<owned_cells>IB-s-15</owned_cells>
</decomp_ref>


<preflight>
comp-schedule: RUN at the cut (20:2xZ, --budget 150) -- WITHIN BUDGET, denominator 5 of 5 carriers (C1=92 C2=6 C3=12 C4=20 C5=335), 25 gates ARMED, 0 name IRPT or any surface of this cell; the moratoria that bind here are G-20 (no monitor), G-23 (cross-firm), G-24 (vendor egress). BLIND SPOT: a ledger of gates, not prose obligations; 137 prose blocking fields unread.
comp-iam: RUN at the cut -- `comp-iam stats` + `roles`: denominator 191 roles parsed, 188 services, 307 gaps estate-wide; ZERO investor-reporting roles exist on the DESIRED plane, so this cell's role is graded at Phase 1 by `comp-iam service irpt-directory-search` once its `.tf` exists and at Phase 2 by `comp-iam gaps` -- both recorded in the instance. BLIND SPOT: DESIRED plane only (the repo's Terraform); a GRANTED-BROAD wildcard cannot be falsified by a resource check. The routes grant `lambda:InvokeFunction` to API Gateway on this project's functions only (resource-based permissions in `integrations.tf`).
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; the assignee's instrument at report time on its own deliverable (a fresh cut has no prior artifact for it to read).
lane: the `<paths>` block above IS the grant (RULING 1 @9ef9a40aae) plus the two tree-convention grants (`deliverables/<serial>/`, this order's own face). Every `infra/aws/**` and `data/assets/scripts/gold/**` path resolves to lane CLOUD_OPS_OR_ETL at HEAD and is admitted to you ONLY through this order while it is non-terminal; a path you need that is not listed is a BLOCKING row, never an override.
</preflight>


<proof_of_spec>
Criterion ids minted at cut: S15-AC1, S15-AC2, S15-AC3. Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/IRPT_BCKEND.TO-IB-s-15.scoped-routes-opal-principal-and-the-cloudfront-behavior.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem, which `.tools/to-pipeline-gate.py` `check_complete_flip` globs for under `deliverables/*/`), per `org/standards/PROOF_OF_SPEC.schema.json`: one acceptance row per id, `criterion_verbatim` the spec's words, `invocation` the exact command, `output_evidence` the verbatim deciding excerpt, `denominator` beside every count, `expect` carried from this face; a judgment row under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming the CVO. Validate with `python .tools/proof-of-spec-check.py org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/IRPT_BCKEND.TO-IB-s-15.scoped-routes-opal-principal-and-the-cloudfront-behavior.proof_of_spec.json S15-AC1,S15-AC2,S15-AC3` BEFORE the complete flip; rc 0 AND every mechanical criterion PASS-by-output, then flip this order's `<status>` to `complete` and commit instance, deliverables and flip together. A FAIL row leaves the order open and is your final report on it.

The grant is read from HEAD of your branch and only while this order is NON-TERMINAL: the issuance commit is in your ancestry at hand-off, so the flip is a modification, not an add.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages -- anything you would ask is a surprise row.
