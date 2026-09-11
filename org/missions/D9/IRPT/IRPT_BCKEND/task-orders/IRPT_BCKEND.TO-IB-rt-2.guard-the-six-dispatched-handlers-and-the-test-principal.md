# TO IRPT_BCKEND.TO-IB-rt-2 -- GUARD THE SIX: the verified FirmBinding wrapper on every handler the real route file dispatches, real request handlers where a route pointed at a queue-only or capabilities-only function, the self-wrapping harness retired, and a test principal from the existing authorizer's own path or a HUMAN-GATED arm naming the operator's exact act

<to_id>IRPT_BCKEND.TO-IB-rt-2</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~2</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-11</issued_date>
<status>pending -- handed by 2.0.0_SA_COO~B at 2026-09-11 ~14:3xZ after IB-rt-1 drained COMPLETE at 8abcb1563b (v1 frozen at c22f179bbf). Second order of slot ~2.</status>

**Directive:** D9 | **Fabric:** laptop | **Round:** 2 | **PRD:** `../prd/IRPT_BCKEND_PRD.md` v0.13 @e6ba5d9878 (ADMITTED, both L4-R halves SIGNED) | **Round-1 analysis:** `../ledger/ROUND_ANALYSIS.round1.md` @0d57ceb2f9, ruling 2 | **Slug rows this cell closes:** W1-S10, W2-S7 (served-path half), W2-S9 (handler half) | **Decomp cell:** `IB-rt-2` (`../decompositions/IRPT_BCKEND_DECOMP.md` v0.2, s.1 + s.2) | **outcome_ref:** FWD-2 (own), FWD-11 | **PRD candidate:** B3

---

## IDENTITY AND WORKTREE

- **Serial:** `0.9.0_WK_IRPT_BCKEND~2` (the same subagent as round 1, continued with its context intact). Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_IRPT_BCKEND~2;`.
- **Worktree:** `/c/tmp/wk-irpt-2-2` on branch `wk-irpt_bckend-2-2`, cut by the issuer from `HEAD` of `CLOUD` at hand-off. First act: `git rev-parse --abbrev-ref HEAD` and `test -d org && test -d .tools && echo TREE-OK`; a worktree that does not carry the paths this face names is a BLOCKING row and a stop. Then the gitignored session-serial line `org/mcp/sessions/<CLAUDE_CODE_SESSION_ID>.serial` BEFORE any apply.
- **Repo root for every path below:** the worktree. Every path in this face is relative to that root; make it absolute by prefixing `/c/tmp/wk-irpt-2-2/`.
- **Commit:** `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~2 <0.9.0_WK_IRPT_BCKEND~2@opal.agent>" -F <msgfile> -- <paths>`, `<msgfile>` written with the Write tool. On your branch only; never push, merge, rebase, `checkout --` or `clean`.
- **Deliverables:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/` (granted by the tree convention; no `<paths>` entry needed). Round-2 batteries are named `battery_<cell>.py` with the cell id lower-cased and hyphens as underscores.
- **Queue:** second in slot ~2, after IB-rt-1. IB-rtb-1 (slot ~1, last) replays what this cell guards and uses the principal this cell establishes.

---

## THE CELL

**The PRD row, verbatim at @e6ba5d9878 (the one carrier; the acceptance clause draft is the bar you build to):**

- **cell:** B3 authorization enforcement on every route, warm-cache revocation
- **serves:** FWD-2 (own)
- **brief sections consumed:** O1 enforcement paragraph; II.3 cache/idempotency-key paragraph
- **contracts (P=produces, C=consumes):** C `ResolvedScope`; keys per II.3
- **paths: reuse:** `infra/aws/terraform/partners-api/api-gateway.tf` (CUSTOM authorizer pattern)
- **paths: new home:** `infra/aws/terraform/investor-reporting/`
- **fixtures / evidence:** negative integration fixtures (swapped firm/advisor/account/relationship/report/PDF ids; revoked grant vs warm cache)
- **acceptance clause draft:** every negative request reveals no protected data; a cached result or artifact is reauthorized before serving; client names are never cache keys

**The CTO's ruling this cell executes (ROUND_ANALYSIS.round1.md @0d57ceb2f9, verbatim):** GUARD THE SIX, THEN PROVE THE AUTHENTICATED PATH. The six actually-dispatched handlers (W1-S10) take the verified FirmBinding wrapper on the real route file; the harness that wrapped them itself is retired as evidence. The authenticated real-path swap arms need a principal: the CTO rules a test principal issued by the existing authorizer's own path under the existing entitlement class (no new permission, no vendor call); if the lane finds no such path exists, the arm is written HUMAN-GATED with the exact act an operator takes, never silently skipped.

**What L5 adds (decomposition v0.2 s.2, s.6, s.9):**

- The population is the REAL route file (`docs/contracts/investor-reporting/v1/routes.json` after IB-rt-1): every route's integration target is read from the api root's Terraform, and every targeted function's entry point is wrapped by `_authz.guard()` with `FirmBinding` proven against the directory artifact -- including the three round 1 left unguarded because they were written before the route table existed: `POST /analysis` (a REAL request handler in `ycharts/generate/` that accepts the browser request half of `AnalysisRequest` (v0.10), builds the `resolved` half server-side through `_scope`'s Generate resolver -- the browser never submits it -- and enqueues the job; the queue-only entry stays for the worker), `GET /narrative/{reportId}` (`narrative/handler.py` gains the wrapper and a scope check on the report's firm), `GET /export/{exportId}` (a real export-status operation in `export/`, reading the receipt under the bound firm's prefix). `unguarded_routes()` over the real file reads `0 of N` and the census is a control on the census: one handler deliberately unregistered from the wrapper in a throwaway copy reads `1 of N`.
- Every guarded handler's refusal is the ONE envelope (`_authz`): public reason, correlation id, 0 protected bytes; `FirmBinding` takes the firm from the VERIFIED principal (the injected `X-Firm-Id` reconciled against the artifact's `firm_id_opaque`), never from a request-controlled field (W2-S9's handler half); the ownership-map projection is wired on the served path so a grant without projection is `UNPROJECTED-ID` (W2-S7's served-path half).
- The test principal: Phase 1 reads `infra/aws/lambda/portal-auth/` and the authorizer `opal-portal-authorizer` for the estate's own way to mint a JWT the validator accepts under an EXISTING entitlement class (a test user in the existing pool, a signing path the authorizer already trusts). If one exists and a worker may use it without a human, the battery mints a principal for one test firm and proves ONE authenticated request through the real path (CloudFront -> edge -> authorizer -> handler) and ONE swapped-firm refusal. If none exists, the arm is written `HUMAN-GATED` naming the exact operator act (which console, which user, which claim) and its expected reading -- never skipped silently. NO new permission, NO vendor call.
- The deploy: every function whose code changes here is rebuilt, its zip uploaded, its root applied under a ledger entry (roots: ycharts, narrative, export -- each state key its own; `-target` never), `CodeSha256` verified; every plan shows ONLY the function code/hash changes.

---

## WHAT ROUND 1 DELIVERED THAT THIS CELL BUILDS ON (not rebuilt)

`_authz` with `guard()`, `FirmBinding`, `unguarded_routes()` and the refusal envelope (IB-s-3, 3cca035c66); the eleven live routes and the CloudFront path; `_scope` with the resolver, `id_projection`, `global.py` and the roster path; the round-1 replay's measurement 6 of 11 unguarded (three known: IB-s-1 directory x2, IB-s-11 performance; three new: analysis, narrative, export status).

**ISSUER AMENDMENT (2.0.0_SA_COO~B, 2026-09-11 ~12:3xZ, at IB-rt-1's first drain -- the second half of ROW W2-S16's disarm; channel row `IRPT_BCKEND-S26`):**
- **EVERY DISPATCHED HANDLER RETURNS THE v1 RESPONSE ENVELOPE.** IB-rt-1 publishes `docs/contracts/investor-reporting/v1/responses/<operation>.response.schema.json` -- ONE envelope `{contract_version, operation, firm_id, data, status?}` with `data` the producer document -- and measured that the six handlers answer in three ad-hoc envelopes (0 of 11 validate). This cell, which owns and deploys the six, makes each handler's response validate against its response schema and its `data` against the document schema; the `X-Contract-Version` check is SERVED (a mismatched version refused `CONTRACT_VERSION` on the deployed function). The refusal envelope of `_authz` and the response envelope are two shapes of one family: `status` carries the `StatusEnvelope` on both.

---

**ISSUER AMENDMENT (2.0.0_SA_COO~B, 2026-09-11 ~17:3xZ, at the drain of this order's first report -- rows W2-S19..S27 read at aef37711d3; the order stays OPEN):**
- **W2-S19 GRANTED.** `<paths>` now carries `infra/aws/lambda/investor-reporting/ops/` and `infra/aws/terraform/investor-reporting/ops/`: `irpt-status` and its three routes are inside the six, and arm (a) reads `0 of N` over all eleven handler-bearing routes.
- **W2-S24 GRANTED, under the shared-surface rule (row W4-S15).** `<paths>` now carries `infra/aws/lambda/layers/irpt-common/` and `infra/aws/lambda/ci/lambda-layer-map.json`. `_authz` reaches the zips through the layer: rebuild the layer FROM THE TREE AT YOUR CUT (the union of every declared member list; the `carried_forward_members` block is removed by IB-rt-7 or by you, whichever touches the file first -- assert no duplicate member path), publish, repoint `3 of 3`, print the version you READ and the version you PUBLISHED. IB-rt-7 (slot ~1, cut at df84a8a952) is rebuilding the same layer now from a tree that predates your guard; whichever of you publishes second publishes the superset, because both build from the merged tree. The capabilities read prints `5 of 5` contracts and the `_authz` members present.
- **W2-S22 RESOLVED BY SEQUENCE.** IB-rt-4 is COMPLETE and merged (56525018f8 -> 3ed2c79443); its export apply landed and closed. From your re-cut onward `irpt-export-render` is this order's alone; the new entry module per function stands, and `export/handler.py` may now be touched where the guard needs it.
- **W2-S21 SPLIT BY OWNER.** `irpt-status` (5 of 7 declared build inputs absent) and `irpt-directory-search` (builder parity on a shared source dir) are THIS order's: register the truth in `lambda-source-map.json` -- a build input that does not exist in the tree is REMOVED from the list, never invented; two functions sharing one source dir carry two entries whose packaged lists are each derivable from the tree and whose parity check passes; every registered `artifact_sha256` equals the S3 object's `content-sha256` equals the live `CodeSha256` (`N of N` printed). `irpt-ycharts-generate` (7 of 25 absent) is IB-rt-9's and is carried to it by amendment. The CLOSED ledger entry that claims a byte-identical rebuild at a commit that lacks the inputs is a RECORD defect carried to L10 by name -- do not edit a closed entry.
- **W2-S23 IN LANE.** `_authz/errors.py` PUBLIC_REASONS gains `CONTRACT_VERSION` (it is the one envelope; the reason set is closed by design and grows by amendment, which this is). Arm (g)'s mismatched-header refusal is served with that code.
- **W2-S25 RULED.** A refusal is NEVER an instance of a response contract: it is v1's `StatusEnvelope`. Arm (g) grades SUCCESS responses against `responses/<operation>.response.schema.json` and REFUSALS against `StatusEnvelope`, both printed per operation; the v1 freeze at c22f179bbf stands and nothing in `docs/contracts/` is edited by this order.
- **W2-S27 IN LANE.** `performance/tenants.py` routes on the firm the boundary binds (the registry spelling resolved from the issued opaque id), and the `F-49F`/`F-COT`/`F-INF` spelling is retired from the adapter; the swap census covers performance after the change.
- **W3-S22 / W4-S24 ROUTED HERE.** `_authz/dispatch.py` was authored in this slot (173349a652) and collides with `export/dispatch.py` on the flat `sys.path` every export module shares (IB-rt-8's own tests cannot see its module). Rename `_authz/dispatch.py` to `_authz/authz_dispatch.py`, update every importer, and print a census of module basenames in `_authz/` against every function directory: `0` collisions. `export/dispatch.py` is not renamed.
- Arm (a)'s inherited `6 of 11` is retired by your census (`11 of 11` unguarded at the cut, row W2-S20); the battery prints the census it derives from `routes.json` + the source map + each root's `handler =`, never an inherited number.

## DELIVERABLE

The guarded entry points in `directory/`, `performance/`, `ycharts/generate/` (the request handler), `narrative/`, `export/` (the status operation); `_authz/tests/test_unguarded_census.py` with the control; the test-principal module `_authz/testprincipal.py` OR the `HUMAN-GATED` arm record `deliverables/0.9.0_WK_IRPT_BCKEND~2/RT2_test_principal_human_gated.md`; the ledger entries + sentinels for each root applied; the battery `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/battery_ib_rt_2.py` and `.result.md`.

---

## BOUNDS

- **The subject is the real route file and the real entry points** (s.8 bound 12); a battery that wraps a copy proves nothing here.
- **No new IAM permission, no new user pool, no vendor call** for the principal; the existing authorizer's own path or a HUMAN-GATED arm.
- **The generate handler enqueues; it never runs the vendor chain inline**, and the queue-only worker entry keeps its consent gate.

### Bounds every order carries (decomposition v0.2 s.8, verbatim)

1. **NO LIVE VENDOR CALL.** Endpoint, verbatim: *"NO LIVE VENDOR CALL is authorized by this document -- availability is not authorization; a live YCharts, Black Diamond or Orion call needs Andrew's explicit per-use word."* The same bound covers the mailbox read and a YCharts login or session capture. A cell that carries a live arm proves its MECHANISM against recorded fixtures through a transport stub with a difference control; the live arm is an express qualification read by the CTO at L10 on Andrew's per-use word, never something this order does.
2. **NO MONITOR, ALARM, SNS OR SES SEND.** Nothing in this project notifies anyone. A scheduler this project creates is the product's own trigger and is applied `DISABLED` where its first fire would be a vendor call.
3. **CROSS-FIRM, both shapes.** Per-firm prefixes + IAM conditions in the shared bucket; the FIRM's own bucket for directory and holdings data; the `FirmDestinationPolicy`; the firm fixed from the sender's domain at ingestion and immutable after; Global GRANTED to an Opal principal, never to a firm one; no new all-firm financial aggregate.
4. **Deploys (NEVER-2, NEVER-9).** `.tools/safe-apply.sh` only, from a root whose state key is this cell's; a change-management entry opened at the start (`python .tools/deploy_ledger.py open ...`) and its OPEN sentinel `org/critical_paths/.open_deploys/<slug>.json` COMMITTED IMMEDIATELY (row W3-S4's rule) before the act; the entry closed at completion and COMMITTED BEFORE the reads that grade the act; served bytes verified as `CodeSha256` against the built zip, never by filename; `aws lambda update-function-code` never; `.tools/terraform.exe` is provisioned in your worktree by the issuer -- use it by that path, never a PATH substitute (a substitute re-pins remote state); every provider cache was purged estate-wide, so `init` each root you plan with the vendored binary.
5. **Andrew's four fixed constraints are not build choices:** the BDAPI-with-Kimi runner STYLE with NO OTP branch; the firm from the sender's domain at ingestion gated to enumerated destinations; the multitenant `api/scoped/` layout; terminated clients STAY VISIBLE under entitlement. And the endpoint's: units are part of a number's meaning; unsupported positions are never silently removed; no PUT of global YCharts preferences; no vendor call in render or preview; missing history is an answer, not an empty state; the narrative states contemporaneity and never causes; model targets never masquerade as observed holdings; THE YCHARTS MECHANISM IS FIXED (v0.9: K3 capture on the dedicated host -> fenced publication -> browserless Lambda REST replay).
6. **No credential in any artifact, log, fixture or commit.** Secrets are read by NAME at runtime; a recorded fixture is scrubbed before it is committed; signed URL parameters are never logged; a `describe-secret` prints version state, never a value.
7. **No served output is touched.** The 28 existing CloudFront behaviors, the 14 pre-existing scoped routes, this project's 11 live routes and every existing bucket, table and Lambda are read, never edited, except where THIS order's cell says it CHANGES or ADDS a resource.
8. **The spec is FROZEN mid-round.** A premise that does not hold, a path that is not where this face says, a result the invocation does not produce, a capability you lack: ONE row at `org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md`, id `IRPT_BCKEND-W<your slot>-S<k>` (a DS lane mints `IRPT_BCKEND-D-S<k>`), per `org/surprise_channel/schemas/investigation_item.schema.json`, inside the fenced json array, appended never edited, k continuing your slot's round-1 numbering; then keep working. Never edit this face, never widen the order, never fix a neighbouring defect.
9. **Every invocation terminates.** You run each named invocation under `timeout`; rc 124 IS the recorded output, retried once at most.
10. **Every `.py` edit passes `.tools/commit-gate.sh`.** Python 3.12 (`Python312` first on PATH; bare `python` may resolve to 3.14 without PyYAML). ASCII only in production code, logs and AWS names (`OK:`/`WARN:`/`ERROR:`/`SKIP:`/`BLOCKED:`).
11. **Scratch** is `<your worktree>/.scratch/` only.
12. **NO SELF-WRAPPING HARNESS AS EVIDENCE (round-1 lesson, rows W1-S10, S24).** An arm's subject is the REAL artifact -- the real route file, the real dispatcher, the deployed function, the served object -- never a copy the battery wraps, patches or re-registers itself. A census reads the real population and prints its denominator; a `0 of 0` is printed as VACUOUS, never as a pass. Every manifest of hashes a cell writes is re-derived by its battery every run (row W3-S9).
13. **TYPED, ISSUED IDENTIFIERS AT EVERY BOUNDARY (round-1 lesson, rows W2-S9/S11, W1-S7, W3-S12).** Firm, client, relationship, account, report, export and job ids cross a function boundary as ISSUED opaque ids of a declared type; a display name, an e-mail address, a raw upstream key or a request-controlled firm token is refused at the boundary, and a refusal never echoes the refused value.

---

## ACCEPTANCE

<criterion id="RT2-AC1" cell_refs="IB-rt-2"><invocation>timeout 900 python org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/battery_ib_rt_2.py</invocation><expect>IBRT2-SIX-GUARDED</expect></criterion>
**`RT2-AC1` -- PASSES BY OUTPUT -- the census reads zero on the real file, the control reads one, every refusal is the envelope, the principal is real or the gate is named.**
**(a) ZERO OF N, AND THE CONTROL.** `unguarded_routes()` over `docs/contracts/investor-reporting/v1/routes.json` at HEAD reads `0 of N` (N = handler-bearing routes, printed); the throwaway copy with one handler unregistered reads `1 of N`.
**(b) SIX SWAPS ON EACH OF THE SIX, IN-PROCESS.** For each of the six handlers: swapped firm / advisor / account / relationship / report / PDF identifiers refused with 0 protected bytes (byte census per swap); a valid principal served; `36 of 36` refusals.
**(c) THE FIRM COMES FROM THE PRINCIPAL.** A request whose body or path carries a different firm than the verified principal is refused `FIRM_BINDING`; a reconciling pair is served; printed.
**(d) THE PROJECTION IS ON THE SERVED PATH.** Through the real directory dispatcher: a grant present with no projection -> `UNPROJECTED-ID` refusal; a grant with the projection -> the narrowed intersection (`N of M` accounts, printed).
**(e) DEPLOYED AND VERIFIED.** For each function changed: `get-function-configuration` `CodeSha256` equals the built zip's; each root's plan after the apply reads `No changes` (printed per root); ledgers CLOSED with sentinels committed (hashes).
**(g) ENVELOPE CONFORMANCE, SERVED (amendment, row W2-S16).** IB-rt-1's paired producer-to-consumer test re-run against the DEPLOYED functions (invoke by name with the validator's injected header set): `11 of 11` responses validate against their response schema and `data` against the document schema; a mismatched `X-Contract-Version` refused `CONTRACT_VERSION` on `11 of 11`; printed per operation.

**ISSUER AMENDMENT (2.0.0_SA_COO~B, at the hand-off, from IB-rt-1's census, row W2-S18):** arm (g)'s denominator is the ROUTES THAT HAVE A DEPLOYED HANDLER AT THIS CELL'S HEAD, printed as `N of N`, with the one published route that has NO handler at HEAD (`holdings-snapshot`, IB-rt-7's) named and EXCLUDED on its own line, never counted as a pass or a fail. IB-rt-1 handed the census `CONFORMS 0 / BLOCKED-BY-W2-S16 8 / DEPLOYED-ONLY 1 / NOT-A-ROUTE 2`: of the eight blocked, seven are handlers answering in an ad-hoc envelope and one is the no-handler route -- the seven are this cell's, the eighth is IB-rt-7's. The `X-Contract-Version` check is committed and NOT served (IB-rt-1 deployed nothing); this cell serves it. The seam's response contracts live at `docs/contracts/investor-reporting/v1/responses/<operation>.response.schema.json` (one envelope `{contract_version, operation, firm_id, data, status?}`, `additionalProperties: false`; `data` the producer document or a declared slice whose properties `$ref` the document's own subschemas).
**(f) THE PRINCIPAL.** Either: one authenticated request through the real path served and one swapped-firm request refused, the principal minted through the named existing path (secret names only, no values); or: the `HUMAN-GATED` record printed verbatim naming the operator's exact act -- and the arm reads `HUMAN-GATED`, which is admitted by this criterion as a PASS of the arm's own rule, never as a skip.

<criterion id="RT2-AC2" cell_refs="IB-rt-2" judgment="true"/>
**`RT2-AC2` -- JUDGMENT, RECORDED AND NOT SELF-GRADED.** State for `3.0.0_SA_CVO`: which of the six were unguarded for a reason that ALSO protected them (the consent gate, the identity-less request shape, the absent operation) and whether guarding changed that protection; whether the test principal, if minted, differs from a real advisor's in any claim the validator reads; and what the in-process swaps cannot show that IB-rtb-1's real-path run must. No verdict: the instance row carries the output under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming `3.0.0_SA_CVO` at L9.


<expected_criteria>RT2-AC1, RT2-AC2</expected_criteria>


<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rt-2.guard-the-six-dispatched-handlers-and-the-test-principal.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
infra/aws/lambda/investor-reporting/_authz/
infra/aws/lambda/investor-reporting/_scope/
infra/aws/lambda/investor-reporting/directory/
infra/aws/lambda/investor-reporting/performance/
infra/aws/lambda/investor-reporting/ycharts/generate/
infra/aws/lambda/investor-reporting/narrative/
infra/aws/lambda/investor-reporting/export/
infra/aws/terraform/investor-reporting/directory/
infra/aws/terraform/investor-reporting/performance/
infra/aws/terraform/investor-reporting/ycharts/
infra/aws/terraform/investor-reporting/narrative/
infra/aws/terraform/investor-reporting/export/
infra/aws/lambda/investor-reporting/PATH_MANIFEST.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/irpt-bckend-rt2.json
infra/aws/lambda/ci/lambda-source-map.json
infra/aws/lambda/investor-reporting/ops/
infra/aws/terraform/investor-reporting/ops/
infra/aws/lambda/layers/irpt-common/
infra/aws/lambda/ci/lambda-layer-map.json
</paths>


<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> v0.2, cell `IB-rt-2` (s.1 the rectangle; s.2 the L5 note; s.6 the root; s.8 the bounds).
<owned_cells>IB-rt-2</owned_cells>
</decomp_ref>


<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this cell creates, changes and fires no schedule, rule or trigger. BLIND SPOT, stated: the round-1 cut-time run (5 of 5 carriers, 0 gates naming this project) is inherited, not re-run here.
comp-iam: RUN at the round-1 cut (191 roles parsed, 307 gaps estate-wide) and the round-1 roles now exist on the DESIRED and APPLIED planes; this cell's change to `irpt-ycharts-generate, irpt-narrative, irpt-export-render, irpt-directory-search, irpt-performance-adapter` is re-graded by the assignee at Phase 1 by `comp-iam service irpt-ycharts-generate, irpt-narrative, irpt-export-render, irpt-directory-search, irpt-performance-adapter` and at Phase 2 by `comp-iam gaps` -- both recorded in the instance. BLIND SPOT: DESIRED plane only; a GRANTED-BROAD wildcard cannot be falsified by a resource check.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; the assignee's instrument at report time on its own deliverable.
lane: the `<paths>` block above IS the grant (RULING 1 @9ef9a40aae) plus the two tree-convention grants (`deliverables/<serial>/`, this order's own face). Every `infra/aws/**`, `docs/contracts/**` and `data/assets/scripts/gold/**` path resolves to lane CLOUD_OPS_OR_ETL or its documentation lane at HEAD and is admitted to you ONLY through this order while it is non-terminal; a path you need that is not listed is a BLOCKING row, never an override.
</preflight>


<proof_of_spec>
Criterion ids minted at cut: RT2-AC1, RT2-AC2. Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/IRPT_BCKEND.TO-IB-rt-2.guard-the-six-dispatched-handlers-and-the-test-principal.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem, which `.tools/to-pipeline-gate.py` `check_complete_flip` globs for under `deliverables/*/`), per `org/standards/PROOF_OF_SPEC.schema.json`: one acceptance row per id, `criterion_verbatim` the spec's words, `invocation` the exact command, `output_evidence` the verbatim deciding excerpt, `denominator` beside every count, `expect` carried from this face; a judgment row under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming the CVO. Validate with `python .tools/proof-of-spec-check.py org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/IRPT_BCKEND.TO-IB-rt-2.guard-the-six-dispatched-handlers-and-the-test-principal.proof_of_spec.json RT2-AC1,RT2-AC2` BEFORE the complete flip; rc 0 AND every mechanical criterion PASS-by-output, then flip this order's `<status>` to `complete` and commit instance, deliverables and flip together. A FAIL row leaves the order open and is your final report on it. The PENDING-THIS-COMMIT sentinel is one-shot: pin artifact rows to the commit that carries them.

The grant is read from HEAD of your branch and only while this order is NON-TERMINAL: the issuance commit is in your ancestry at hand-off, so the flip is a modification, not an add.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages -- anything you would ask is a surprise row.
