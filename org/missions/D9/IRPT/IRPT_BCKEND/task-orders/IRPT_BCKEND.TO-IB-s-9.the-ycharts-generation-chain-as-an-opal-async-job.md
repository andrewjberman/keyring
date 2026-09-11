# TO IRPT_BCKEND.TO-IB-s-9 -- THE YCHARTS GENERATION CHAIN: the seven captured steps as an Opal async job -- SUBMITTING persisted before the side effect, uncertain creates reconciled by owned identity, settings read back, no vendor job id invented

<to_id>IRPT_BCKEND.TO-IB-s-9</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~3</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-10</issued_date>
<status>staged -- assigned to slot ~3; becomes pending when the COO hands it over after IB-s-7 is terminal and merged (IB-s-8 and IB-s-17 already terminal by then).</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_BCKEND_PRD.md` v0.4 @62301f71e0 | **Decomp cell:** `IB-s-9` (`../decompositions/IRPT_BCKEND_DECOMP.md` v0.1.1, s.1 + s.2) | **outcome_ref:** FWD-4 (contrib) | **PRD candidate:** B9

---

## IDENTITY AND WORKTREE

- **Serial:** `0.9.0_WK_IRPT_BCKEND~3`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_IRPT_BCKEND~3;`.
- **Worktree:** `/c/tmp/wk-irpt-1-3` on branch `wk-irpt_bckend-1-3`, cut by the issuer from `HEAD` of `CLOUD` at hand-off. First act: `git rev-parse --abbrev-ref HEAD` and `test -d org && test -d .tools && echo TREE-OK`; a worktree that does not carry the paths this face names is a BLOCKING row and a stop.
- **Repo root for every path below:** the worktree. Every path in this face is relative to that root; make it absolute by prefixing `/c/tmp/wk-irpt-1-3/`.
- **Commit:** `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~3 <0.9.0_WK_IRPT_BCKEND~3@opal.agent>" -F <msgfile> -- <paths>`, `<msgfile>` written with the Write tool. On your branch only; never push, merge, rebase, `checkout --` or `clean`.
- **Deliverables:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~3/` (granted by the tree convention; no `<paths>` entry needed).
- **Queue:** fourth in slot ~3, after IB-s-7.

---

## THE CELL

**The PRD row, verbatim at @62301f71e0 (the one carrier; the acceptance clause draft is the bar you build to):**

- **cell:** B9 YCharts generation chain
- **serves:** FWD-4 (contrib)
- **brief sections consumed:** O4; IV.4 captured retrieval recipe steps 1-7
- **contracts (P=produces, C=consumes):** P `AnalysisReport` (attempt, vendor artifact hash)
- **paths: reuse:** endpoints per recipe: `/search/suggest/report_securities`, `/securities/securities_info`, `/model_portfolios/fixed/holdings_upload/client`, `/model_portfolios/fixed/`, `/model_portfolios/{id}/status`, `/custom_pdf_reports/generate/collection`, `/generate/{template_id}`, `/validate_report_securities/{template_id}`, `/custom_pdf_reports/{template_id}`; templates 14141822 / 14141824 / 14141847 (captured configuration, not constants)
- **paths: new home:** `infra/aws/lambda/investor-reporting/` (generation job)
- **fixtures / evidence:** HAR evidence; comparison field census; 34-key vs 33-key body shapes
- **acceptance clause draft:** upload uses the observed browser upload (multipart field names NOT captured -- do not invent; the captured response carries status, errors, rows, weight, upload_record_id, isExtractedHoldings); creation is `POST /model_portfolios/fixed/` with the captured portfolio/items JSON multipart form, the REAL upload_record_id and correct units, returning model_portfolio_id on 201; opaque deterministic portfolio name, checkpoint intent before submit, reconcile uncertain creates by owned identity, never adopt the newest row; SUBMITTING persisted before the side effect; short-lived URL downloaded immediately over TLS, signed params never logged; PDF content and hash verified; owned encrypted artifact retained; effective settings READ BACK and verified after creation against the recorded configuration (quarterly rebalance, dividends false, oldest start, prior close, non-qualified, `^SPXTR`, fee `0.003`); a default tax setting is not client tax status and a No Benchmark template does not remove the calculation benchmark; typed P:/M:/S:/cash identities preserved; Overview primary/portrait, Comparison primary plus one/portrait, Multi primary plus two to five/landscape (the captured Multi evidence holds two comparisons only); single `secondarySecurity` vs Multi array, asymmetric null/empty fields and consistent duplicate cover fields per S8 body authority; no PUT of global preferences; the vendor 201 is slow and SYNCHRONOUS with `report_url`/`zip_url`, wrapped in Opal's own async job, and no vendor background-job id is ever invented

**What L5 adds (decomposition v0.1.1 s.2, s.6, s.9):**

- `infra/aws/lambda/investor-reporting/ycharts/generate/` (Lambda `irpt-ycharts-generate` dispatching to the runner host over SSM when live; a job runner that consumes `irpt-generation`): the seven-step recipe per PRD row B9 and S8 s.5 -- resolve securities preserving P:/M:/S:/cash identities; upload through the OBSERVED browser upload (multipart names NOT captured, NOT invented; the response's `status, errors, rows, weight, upload_record_id, isExtractedHoldings` parsed); create with the captured portfolio/items JSON multipart form, the REAL `upload_record_id` and correct units, 201 -> `model_portfolio_id`; an opaque deterministic portfolio name; checkpoint intent BEFORE submission; reconcile an uncertain create by owned identity/fingerprint/name and NEVER adopt the newest row; read back effective settings and verify against `settings.json` (IB-s-7); template catalogue / detail / validate; templates 14141822 / 14141824 / 14141847 as CAPTURED CONFIGURATION in `templates.json`, not constants in code; the slow synchronous 201 with `report_url`/`zip_url` wrapped in Opal's own job -- `SUBMITTING` persisted before the side effect; the short-lived URL downloaded immediately over TLS from the allowed host, signed params never logged; PDF content and hash verified; the owned encrypted artifact retained under `firms/<id>/generations/<id>/attempts/<a>/vendor/report.pdf`; `AnalysisReport` attempt row schema-valid.
- Body shapes per S8: single `secondarySecurity` vs the Multi array, the 34-key August vs 33-key July body, asymmetric null/empty fields, consistent duplicate cover fields; no PUT of global preferences (censused).
- Proof is OFFLINE against a HAR-replay transport built from the HAR evidence JSON; the live calls are the qualified arm.

**ISSUER AMENDMENT (2.0.0_SA_COO~B, 2026-09-11 ~01:4xZ, at the IB-s-3 drain, before this order was handed -- the disarm of rows `IRPT_BCKEND-W2-S9` and `IRPT_BCKEND-W2-S10`, whose disarm_owner is the issuer; recorded as channel row `IRPT_BCKEND-S9`):**
- **EVERY HANDLER THIS CELL SHIPS IS WRAPPED BY `_authz.guard()`** (`infra/aws/lambda/investor-reporting/_authz/enforce.py`, merged at 3cca035c66): resolve, reauthorize before serving, keys through `_keys`, one refusal envelope. A handler reachable through a route without `guard()` is a defect this cell's own battery prints: `_authz.unguarded_routes()` over the routes this cell registers reads `0 of N`, N printed. Where this cell ships no handler, the same census runs over `routes.json` at the replay.
- **THE FIRM ID HAS TWO SPELLINGS AND ONLY `_authz.FirmBinding` RECONCILES THEM (row W2-S9).** `X-Firm-Id` and `_keys.cache_key` carry the REGISTRY id (`49financial`); `DirectoryEntry.ids.firm_id` and the `_scope` cross-firm filter carry the OPAQUE id (`fir_...`, `directory_runner.opaque_id`). A handler that passes the header value into the directory join returns an EMPTY population that reads exactly like a revocation, and no per-module test can see it. Every firm-scoped read this cell makes binds through `FirmBinding`, proven against the directory artifact's own `firm_id_opaque`; a binding that does not reconcile is a REFUSAL (`FIRM_BINDING`), never an empty set. No hash is recomputed and `opaque_id` is not duplicated into a Lambda.
- **A `_keys` REFUSAL NAMES THE REFUSED VALUE (row W2-S10).** `KeyComponentRefused` carries the component with `%r` at twelve message sites; `str(exc)` in a response, a log line, an audit row, a battery print or a surprise row DISCLOSES exactly the value that was refused for being a client name or an e-mail address. Nothing this cell writes surfaces a `_keys` exception's text: the wrapper's refusal reason (parameter NAMES, found through the public `cache_key`) is the only refusal that leaves a handler, and at least one test asserts over the WHOLE envelope (body + reason + audit trail), never the census alone. `_keys` itself is not edited by this cell (not in its `<paths>`; the sanitised exception is the issuer's round-2 item on IB-s-17's surface).
- **THE DIRECTORY AND PERFORMANCE HANDLERS ALREADY MERGED (IB-s-1, IB-s-11) PREDATE THE WRAPPER** -- a decomposition sequencing defect of the issuer, carried to L10; this cell does not edit them, and IB-sb-3's replay is where their unguarded state is measured.

**ISSUER AMENDMENT (2.0.0_SA_COO~B, 2026-09-11 ~03:2xZ, at the IB-s-12 drain, before this order was handed -- the PRD moved to v0.8 @d67e9813b5 mid-round and the CTO left the amend-at-drain versus re-cut decision to this lane (1.0.0_SA_CTO 95751); recorded as channel row `IRPT_BCKEND-S11`. Round 1 stays FROZEN on v0.4 @62301f71e0 for the cell's RECTANGLE; this block carries the v0.5 and v0.8 additions to the B9 row as the MEASURED SHAPES the replay transport records, so the cell is not built to contracts the estate has already measured to be wrong):**
- **THE UPLOAD FIELD IS MEASURED, NOT INVENTED.** The v0.4 row said the multipart field names were NOT captured and must not be invented. PRD v0.8 (SUPP VI.5, measured live 2026-09-11 on Andrew's live-test word) records them: the holdings upload multipart field is `holdings`; the portfolio save is multipart JSON fields `portfolio` / `items` returning 201 with the new portfolio id. Use those names, cited to the PRD row at d67e9813b5 -- the bound against invention stands for every OTHER field.
- **THE 201 CONTRACT, MEASURED.** The report POST returns 201 only with the FULL HAR-shaped `generationModalsState` plus the current `selectedReport` and its disclosure together (individual field necessity NOT isolated); a minimal payload returns 404 and is a CONTRACT failure, never session expiry; a zero annual management fee returns 422 `invalid_management_fee` and the captured 0.003 annual recipe succeeds; the saved Overview template legitimately returns an EMPTY `sections` array; the Overview 201 took a 26.76 s invocation, so the JOB BUDGET is sized from that measurement (a durable worker is selected if the measured duration exceeds the Lambda budget; a timeout never licenses regeneration); the PDF is downloaded by a SEPARATE unauthenticated storage client (the YCharts session cookie is NEVER forwarded to the signed URL) and validated by parse before READY. Comparison and Multi-Comparison have NO live proof yet and stay on the HAR shapes.
- **THE REST DECISION TABLE BINDS (v0.5, SUPP IV.7 / IV.8 / III.2), as classified branches the replay exercises:** an expected authenticated response and schema continues from the current checkpoint; an explicit 401 or a VERIFIED concurrent-login eviction coordinates ONE refresh attempt through B8 and resumes the safely retryable stage; a 200 HTML body or a wrong JSON shape is NEVER healthy (an unknown schema is a protocol failure, not permission to loop logins); a WAF action/header/interstitial is challenge handling, never bad holdings or authorization denial; an unrelated 403 or invalid input preserves the failure with no login retry; 429 or a transient read failure respects Retry-After with bounded backoff and no auth-refresh storm; a timeout, disconnect or ambiguous 5xx during upload, creation or generation marks the outcome UNCERTAIN and RECONCILES the owned vendor object before any replay (HTTP class alone never proves a mutation did not execute); repeat eviction after the allowed refresh preserves the request and surfaces a retryable/attention state; the legacy client's raw error-body logging is replaced by a sanitized adapter.
- **REUSE, do not reinvent the transport:** `docs/research/investor_reporting_ycharts_cloud_20260911/{cloud_transport.py,test_cloud_transport.py,README.md}` (v0.8) and `docs/research/investor_reporting_ycharts_auth_20260910/{recovery_contract.py,test_recovery.py}` (v0.5) are read-only reuse sources named by the PRD; the session-acquisition changes to B8 (the broker, the isolated secret, the fence) are NOT this cell's -- the replay transport STUBS the session and the live arm remains the CTO's qualified read at L10 on Andrew's per-use word. IB-s-8 (merged at 95a34541f8) was built to v0.4 and its v0.5/v0.8 delta is round-2 material.
- **v0.9 @86bde3ea26 (Andrew-direct 2026-09-11 ~03:1xZ via 1.0.0_SA_CTO 95756): THE MECHANISM IS FIXED, NOT A BUILD CHOICE.** FWD-4 CONSTRAINT++: EC2 capture by the K3 controller -> fenced publication of a versioned session -> browserless Lambda REST replay (identity by the structured page contract, Set-Cookie persisted) -> upload, portfolio, generation, PDF. For THIS cell that means the transport IS `docs/research/investor_reporting_ycharts_cloud_20260911/cloud_transport.py` extended into the generation package (B9 BUILDS ON it) -- never a parallel transport, never the stopped-host SSM dispatch as the primary path (that was v0.4's B8 and is round-2 material). The v0.4 L5 note's `irpt-ycharts-generate` dispatching over SSM is read as the LAMBDA REPLAY path instead: the Lambda holds the fenced session by NAME and replays REST; the EC2 capture is B8's, stubbed here. v0.9's arm (5) -- Comparison 14141824 and Multi-Comparison 14141847 replayed LIVE with parsed PDFs -- is a LIVE VENDOR CALL and stays the CTO's qualified read at L10 on Andrew's per-use word (bound 1); this cell proves both variants against the HAR shapes on the replay and says so.

---

## DELIVERABLE

`infra/aws/lambda/investor-reporting/ycharts/generate/` (`job.py`, `recipe.py`, `transport.py`, `templates.json`) + `tests/` + `fixtures/har/`; `infra/aws/terraform/investor-reporting/ycharts/generate.tf`; the ledger entry + sentinel; the battery `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~3/battery_ib_s_9.py` and `.result.md`.

---

## BOUNDS

- **NO LIVE YCHARTS CALL.** The transport is the replay; an outbound request to a `ycharts.com` host fails arm (h).
- **Do not invent the upload's multipart field names.** The pure-HTTP upload stays a named gap; the observed browser upload is the mechanism.
- **Never adopt the newest portfolio row.** Reconciliation is by owned identity only.
- **No PUT of global preferences.**

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

<criterion id="S9-AC1" cell_refs="IB-s-9"><invocation>timeout 600 python org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~3/battery_ib_s_9.py</invocation><expect>IBS9-GENERATION-CHAIN</expect></criterion>
**`S9-AC1` -- PASSES BY OUTPUT -- the seven steps against the replay, the job's durability, the read-back.**
**(a) SEVEN OF SEVEN.** Each recipe step runs against the replay with the captured request shape and the captured response parsed; printed per step.
**(b) SUBMITTING BEFORE THE SIDE EFFECT -- THE DIFFERENCE CONTROL.** A kill injected after the create POST and before the response is recorded: on restart the job reads SUBMITTING, reconciles by owned identity (the replay returns the portfolio it created) and does NOT submit again; a deliberately broken build that resubmits FAILS the arm. Both printed.
**(c) NEVER THE NEWEST ROW.** The replay's collection carries a newer foreign portfolio; reconciliation picks the owned one. Printed.
**(d) SETTINGS READ BACK.** Effective settings after creation equal `settings.json` (seven of seven), and a replay that returns a drifted setting is detected. Printed.
**(e) BODIES PER S8.** Single vs Multi `secondarySecurity`, the 34-key vs 33-key body, the asymmetric null/empty fields, duplicate cover fields consistent; templates read from `templates.json`; `0` PUTs of global preferences (census).
**(f) THE 201 IS WRAPPED.** The job's own id is Opal's; no field named like a vendor background-job id exists (census); `report_url` downloaded immediately; signed params absent from every log line (log scan, denominator printed); PDF hash verified and the artifact key under the bound firm's generations prefix.
**(g) SCHEMA-VALID.** The `AnalysisReport` attempt row validates.
**(v0.8) THE MEASURED CONTRACTS AND THE DECISION TABLE, ON THE REPLAY (issuer amendment at the IB-s-12 drain, PRD v0.8 @d67e9813b5).** The replay's fixtures carry the measured shapes: upload field `holdings`; save fields `portfolio` / `items` -> 201; the full `generationModalsState` + `selectedReport` + disclosure payload -> 201 and a minimal payload -> 404 classified CONTRACT-FAILURE (never session expiry); fee 0 -> 422 `invalid_management_fee` and 0.003 -> 201; an empty `sections` array accepted as legitimate; the PDF fetched by the separate unauthenticated client with 0 session-cookie headers on that request (census). Each classified branch of the decision table (healthy / 401-or-eviction -> ONE refresh / 200-HTML-never-healthy / WAF-challenge / unrelated-403-no-retry / 429-Retry-After / UNCERTAIN-then-reconcile / repeat-eviction-attention) is exercised once against the replay and its branch label printed, `N of N`; the job budget is printed beside the measured 26.76 s.
**(h) NOTHING LEFT THE MACHINE; THE LEDGER CLOSED.** 0 external connections; `get-function-configuration irpt-ycharts-generate` `CodeSha256` equals the built zip's; sentinel committed (hash).

**(amend) GUARDED, BOUND, AND SILENT ON THE REFUSED VALUE (issuer amendment at the IB-s-3 drain, rows W2-S9 / W2-S10).** `unguarded_routes()` over this cell's routes reads `0 of N` (N printed); every firm-scoped read binds through `FirmBinding` and a fixture with a non-reconciling binding is REFUSED with `FIRM_BINDING` rather than served empty; a fixture that keys by a client display name is refused and the whole envelope (body + reason + audit trail) contains 0 occurrences of the refused value (census printed). Where this cell ships no handler, the arm reads over `routes.json` at the replay. CLARIFIED at the IB-s-7 drain (row W3-S5, disarm by the issuer): `routes.json` is IB-s-15's deliverable at `infra/aws/terraform/investor-reporting/api/routes.json` and does not exist before that cell lands; a cell that ships no handler and runs before it does NOT report a `0 of 0` census as a pass -- it prints the census AS VACUOUS and runs the two CONTROLS IB-s-7's battery ran (a handler registered unguarded censused `1 of 1`; the same handler wrapped censused `0 of 1`), so the arm proves the censor, not an empty set. IB-s-15 and IB-sb-3 read the real file.

<criterion id="S9-AC2" cell_refs="IB-s-9"><invocation>timeout 120 .tools/terraform.exe -chdir=infra/aws/terraform/investor-reporting/ycharts plan -no-color -input=false -lock=false</invocation><expect>No changes\. Your infrastructure matches the configuration\.</expect></criterion>
**`S9-AC2` -- THE ROOT IS CONVERGED after this cell's apply.**
Run after the apply and after the ledger closes.

<criterion id="S9-AC3" cell_refs="IB-s-9" judgment="true"/>
**`S9-AC3` -- JUDGMENT, RECORDED AND NOT SELF-GRADED.** State for `3.0.0_SA_CVO`: which captured responses you had to extend (the upload body, the two-comparison-only Multi example) and how the first live run could differ; what 'uncertain create' cases the replay cannot produce; and what an operator sees when a step fails mid-chain. No verdict: the instance row carries the output under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming `3.0.0_SA_CVO` at L9.


<expected_criteria>S9-AC1, S9-AC2, S9-AC3</expected_criteria>


<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-s-9.the-ycharts-generation-chain-as-an-opal-async-job.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
infra/aws/lambda/investor-reporting/ycharts/
infra/aws/terraform/investor-reporting/ycharts/
infra/aws/lambda/investor-reporting/PATH_MANIFEST.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/irpt-bckend-s9.json
infra/aws/lambda/ci/lambda-source-map.json
</paths>


<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> v0.1.1, cell `IB-s-9` (s.1 the rectangle; s.2 the L5 note; s.6 the root; s.8 the bounds).
<owned_cells>IB-s-9</owned_cells>
</decomp_ref>


<preflight>
comp-schedule: RUN at the cut (20:2xZ, --budget 150) -- WITHIN BUDGET, denominator 5 of 5 carriers (C1=92 C2=6 C3=12 C4=20 C5=335), 25 gates ARMED, 0 name IRPT or any surface of this cell; the moratoria that bind here are G-20 (no monitor), G-23 (cross-firm), G-24 (vendor egress). BLIND SPOT: a ledger of gates, not prose obligations; 137 prose blocking fields unread.
comp-iam: RUN at the cut -- `comp-iam stats` + `roles`: denominator 191 roles parsed, 188 services, 307 gaps estate-wide; ZERO investor-reporting roles exist on the DESIRED plane, so this cell's role is graded at Phase 1 by `comp-iam service irpt-ycharts-generate` once its `.tf` exists and at Phase 2 by `comp-iam gaps` -- both recorded in the instance. BLIND SPOT: DESIRED plane only (the repo's Terraform); a GRANTED-BROAD wildcard cannot be falsified by a resource check.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; the assignee's instrument at report time on its own deliverable (a fresh cut has no prior artifact for it to read).
lane: the `<paths>` block above IS the grant (RULING 1 @9ef9a40aae) plus the two tree-convention grants (`deliverables/<serial>/`, this order's own face). Every `infra/aws/**` and `data/assets/scripts/gold/**` path resolves to lane CLOUD_OPS_OR_ETL at HEAD and is admitted to you ONLY through this order while it is non-terminal; a path you need that is not listed is a BLOCKING row, never an override.
</preflight>


<proof_of_spec>
Criterion ids minted at cut: S9-AC1, S9-AC2, S9-AC3. Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~3/IRPT_BCKEND.TO-IB-s-9.the-ycharts-generation-chain-as-an-opal-async-job.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem, which `.tools/to-pipeline-gate.py` `check_complete_flip` globs for under `deliverables/*/`), per `org/standards/PROOF_OF_SPEC.schema.json`: one acceptance row per id, `criterion_verbatim` the spec's words, `invocation` the exact command, `output_evidence` the verbatim deciding excerpt, `denominator` beside every count, `expect` carried from this face; a judgment row under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming the CVO. Validate with `python .tools/proof-of-spec-check.py org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~3/IRPT_BCKEND.TO-IB-s-9.the-ycharts-generation-chain-as-an-opal-async-job.proof_of_spec.json S9-AC1,S9-AC2,S9-AC3` BEFORE the complete flip; rc 0 AND every mechanical criterion PASS-by-output, then flip this order's `<status>` to `complete` and commit instance, deliverables and flip together. A FAIL row leaves the order open and is your final report on it.

The grant is read from HEAD of your branch and only while this order is NON-TERMINAL: the issuance commit is in your ancestry at hand-off, so the flip is a modification, not an add.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages -- anything you would ask is a surprise row.
