# TO IRPT_BCKEND.TO-IB-sb-3 -- THE REPLAY BATTERY: swapped identifiers across EVERY deployed route including the PDF download, a revoked grant against a warm cache, an Opal principal against a firm advisor -- the exercised proof of FWD-2

<to_id>IRPT_BCKEND.TO-IB-sb-3</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~1</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-10</issued_date>
<status>staged -- assigned to slot ~1; becomes pending when the COO hands it over after IB-s-16 is terminal and merged AND IB-s-15 (slot ~2) is terminal and merged.</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_BCKEND_PRD.md` v0.4 @62301f71e0 | **Decomp cell:** `IB-sb-3` (`../decompositions/IRPT_BCKEND_DECOMP.md` v0.1.1, s.1 + s.2) | **outcome_ref:** FWD-2 (own) | **PRD candidate:** B3

---

## IDENTITY AND WORKTREE

- **Serial:** `0.9.0_WK_IRPT_BCKEND~1`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_IRPT_BCKEND~1;`.
- **Worktree:** `/c/tmp/wk-irpt-1-1` on branch `wk-irpt_bckend-1-1`, cut by the issuer from `HEAD` of `CLOUD` at hand-off. First act: `git rev-parse --abbrev-ref HEAD` and `test -d org && test -d .tools && echo TREE-OK`; a worktree that does not carry the paths this face names is a BLOCKING row and a stop.
- **Repo root for every path below:** the worktree. Every path in this face is relative to that root; make it absolute by prefixing `/c/tmp/wk-irpt-1-1/`.
- **Commit:** `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~1 <0.9.0_WK_IRPT_BCKEND~1@opal.agent>" -F <msgfile> -- <paths>`, `<msgfile>` written with the Write tool. On your branch only; never push, merge, rebase, `checkout --` or `clean`.
- **Deliverables:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/` (granted by the tree convention; no `<paths>` entry needed).
- **Queue:** fifth and last in slot ~1, after IB-s-16; cross-slot wait on IB-s-15's merge. The last cell of the round.

---

## THE CELL

**The PRD row, verbatim at @62301f71e0 (the one carrier; the acceptance clause draft is the bar you build to):**

- **cell:** B3 authorization enforcement on every route, warm-cache revocation
- **serves:** FWD-2 (own)
- **brief sections consumed:** O1 enforcement paragraph; II.3 cache/idempotency-key paragraph
- **contracts (P=produces, C=consumes):** C `ResolvedScope`; keys per II.3
- **paths: reuse:** `infra/aws/terraform/partners-api/api-gateway.tf` (CUSTOM authorizer pattern)
- **paths: new home:** `infra/aws/terraform/investor-reporting/`
- **fixtures / evidence:** negative integration fixtures (swapped firm/advisor/account/relationship/report/PDF ids; revoked grant vs warm cache)
- **acceptance clause draft:** every negative request reveals no protected data; a cached result or artifact is reauthorized before serving; client names are never cache keys

**What L5 adds (decomposition v0.1.1 s.2, s.6, s.9):**

- The battery half of PRD candidate B3 (decomposition s.1): the end-to-end replay the endpoint's FWD-2 PROOF names, run against the DEPLOYED routes through the real path (CloudFront -> edge validator -> API Gateway authorizer -> handler), not against in-memory handlers.
- Identity: the battery needs authenticated principals. It uses whatever the estate's own test-principal mechanism is (read `infra/aws/lambda/portal-auth/` and the authorizer `opal-portal-authorizer` for how a test JWT is minted -- if NO such mechanism exists that a worker may use without a human, that is a BLOCKING row on arm (a) and the battery falls back to the post-authorizer plane: direct Lambda invocations with the validator's injected header set, stating the boundary it could not cross).
- Denominator from a file: every route key in `infra/aws/terraform/investor-reporting/api/routes.json` (IB-s-15) is replayed; the PDF download route included.

**ISSUER AMENDMENT (2.0.0_SA_COO~B, 2026-09-11 ~01:4xZ, at the IB-s-3 drain, before this order was handed -- the disarm of rows `IRPT_BCKEND-W2-S9` and `IRPT_BCKEND-W2-S10`, whose disarm_owner is the issuer; recorded as channel row `IRPT_BCKEND-S9`):**
- **EVERY HANDLER THIS CELL SHIPS IS WRAPPED BY `_authz.guard()`** (`infra/aws/lambda/investor-reporting/_authz/enforce.py`, merged at 3cca035c66): resolve, reauthorize before serving, keys through `_keys`, one refusal envelope. A handler reachable through a route without `guard()` is a defect this cell's own battery prints: `_authz.unguarded_routes()` over the routes this cell registers reads `0 of N`, N printed. Where this cell ships no handler, the same census runs over `routes.json` at the replay.
- **THE FIRM ID HAS TWO SPELLINGS AND ONLY `_authz.FirmBinding` RECONCILES THEM (row W2-S9).** `X-Firm-Id` and `_keys.cache_key` carry the REGISTRY id (`49financial`); `DirectoryEntry.ids.firm_id` and the `_scope` cross-firm filter carry the OPAQUE id (`fir_...`, `directory_runner.opaque_id`). A handler that passes the header value into the directory join returns an EMPTY population that reads exactly like a revocation, and no per-module test can see it. Every firm-scoped read this cell makes binds through `FirmBinding`, proven against the directory artifact's own `firm_id_opaque`; a binding that does not reconcile is a REFUSAL (`FIRM_BINDING`), never an empty set. No hash is recomputed and `opaque_id` is not duplicated into a Lambda.
- **A `_keys` REFUSAL NAMES THE REFUSED VALUE (row W2-S10).** `KeyComponentRefused` carries the component with `%r` at twelve message sites; `str(exc)` in a response, a log line, an audit row, a battery print or a surprise row DISCLOSES exactly the value that was refused for being a client name or an e-mail address. Nothing this cell writes surfaces a `_keys` exception's text: the wrapper's refusal reason (parameter NAMES, found through the public `cache_key`) is the only refusal that leaves a handler, and at least one test asserts over the WHOLE envelope (body + reason + audit trail), never the census alone. `_keys` itself is not edited by this cell (not in its `<paths>`; the sanitised exception is the issuer's round-2 item on IB-s-17's surface).
- **A THIRD ID SPELLING (row W2-S11, ARMED, disarmed here by the issuer at the IB-s-4 drain):** `HoldingsSnapshot.scope.account_ids` carries a NAMESPACE PREFIX (`<firm>:acct:acc_...`) while `DirectoryEntry` carries the bare opaque tail (`acc_...`); joined AS WRITTEN they read `0 of N` for ALL THREE firms, which is a prefix difference and cosmetic, on top of the REAL raw-key difference of W1-S7 that affects INF and COT only. CORRECTED at the IB-s-16 drain (row W1-S9: NO shared normaliser exists on disk -- IB-s-4 normalised inside its own battery only; the issuer's S15 sentence was a false premise). The prefix is minted at `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py:370/486/638` as `<firm>:acct:<opaque>` with firm tokens `49f|inf|cot`. Any read this cell makes that joins holdings to the directory strips EXACTLY that grammar (`^(49f|inf|cot):acct:`) in ONE named function of its own, cites those three lines, and prints BOTH counts per firm -- resolved as written and resolved after normalisation -- so the two causes stay distinguishable (expected shape at HEAD: 49F 5,856 of 5,873 after, INF 0 of 790, COT 0 of 946). No join is changed; which spelling is canonical is the CTO's L10 read.
- **THE DEPLOYED EXPORT WORKER REPORTS RENDERER ABSENCE (row W4-S9, ARMED, disarmed here by carry):** `irpt-export-render` is live with `IRPT_EXPORT_RENDERER=unavailable` set explicitly and no `s3:PutObject` / `kms:Decrypt` grant, because a python3.12 Lambda has no headless browser and fetching one is egress the estate refused (rows W3-S1/S2). The render mechanism is proved in the worktree on the estate's existing local Edge path. This cell grades the export ROUTE on the function's own ABSENCE REPORT (reason code present, no credential/infra payload), never on a render; the headless runtime (container image, browser layer or out-of-Lambda worker) is a round-2 build decision at L10. Its layer carries 2 of 5 IRPT contracts (row W4-S10): the export contracts resolve from the repo path in tests and are ABSENT on the runtime -- print which resolution branch answered.
- **A CLIENT NAME CAN REACH A DURABLE S3 KEY THROUGH `_keys.s3_evidence_key` (row W3-S12, ARMED, routed by the issuer):** that function checks non-empty / no slash / not lock-shaped / not a foreign firm token and NEVER calls the shape checks `cache_key` does, so `"Whitfield Family"` or an e-mail address lands in `firms/<firm>/generations/<...>/` -- in access logs, CloudTrail, Inventory and every ListObjects, un-loggable. `_keys` is IB-s-17's surface (round 2). Every S3 key this cell builds or replays passes through a shape check BEFORE `s3_evidence_key` (IB-s-10's wrapper is the pattern), and the replay censuses every key it observes for name-shaped or e-mail-shaped components (`0 of N`, N printed); a hit is a FAIL, never a note.
- **THE DIRECTORY AND PERFORMANCE HANDLERS ALREADY MERGED (IB-s-1, IB-s-11) PREDATE THE WRAPPER** -- a decomposition sequencing defect of the issuer, carried to L10; this cell does not edit them, and IB-sb-3's replay is where their unguarded state is measured.

---

## DELIVERABLE

The battery `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/battery_ib_sb_3.py`, its fixtures and `.result.md`; no code home is written.

---

## BOUNDS

- **Read-only against the deployed plane** except the QA requests it creates under QA prefixes.
- **Never print a protected value**; the byte census reports counts, not content.
- **Deploys nothing.**

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

<criterion id="SB3-AC1" cell_refs="IB-sb-3"><invocation>timeout 600 python org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/battery_ib_sb_3.py</invocation><expect>IBSB3-REPLAY-CLEAN</expect></criterion>
**`SB3-AC1` -- PASSES BY OUTPUT -- every route, every swap, no protected byte.**
**(a) THE PLANE.** Print which plane the replay ran on (the real path with a test principal, or the post-authorizer plane with the boundary named) and why.
**(b) EVERY ROUTE, SIX SWAPS.** For each route in `routes.json` (`N of N`), authorized request served; then swapped firm / advisor / account / relationship / report / PDF identifiers each REFUSED with 0 protected bytes in the body (census per swap).
**(c) REVOKED AGAINST A WARM CACHE.** Served, revoked, replayed: refused; printed.
**(d) OPAL VS FIRM.** An Opal principal reaches two firms' clients; a firm advisor replaying the same requests is refused; printed.
**(e) THE DOWNLOAD.** The PDF download route with a swapped PDF id: refused; with the right id after revocation: refused; printed.

**(amend) GUARDED, BOUND, AND SILENT ON THE REFUSED VALUE (issuer amendment at the IB-s-3 drain, rows W2-S9 / W2-S10).** `unguarded_routes()` over this cell's routes reads `0 of N` (N printed); every firm-scoped read binds through `FirmBinding` and a fixture with a non-reconciling binding is REFUSED with `FIRM_BINDING` rather than served empty; a fixture that keys by a client display name is refused and the whole envelope (body + reason + audit trail) contains 0 occurrences of the refused value (census printed). Where this cell ships no handler, the arm reads over `routes.json` at the replay. CLARIFIED at the IB-s-7 drain (row W3-S5, disarm by the issuer): `routes.json` is IB-s-15's deliverable at `infra/aws/terraform/investor-reporting/api/routes.json` and does not exist before that cell lands; a cell that ships no handler and runs before it does NOT report a `0 of 0` census as a pass -- it prints the census AS VACUOUS and runs the two CONTROLS IB-s-7's battery ran (a handler registered unguarded censused `1 of 1`; the same handler wrapped censused `0 of 1`), so the arm proves the censor, not an empty set. IB-s-15 and IB-sb-3 read the real file.

<criterion id="SB3-AC2" cell_refs="IB-sb-3" judgment="true"/>
**`SB3-AC2` -- JUDGMENT, RECORDED AND NOT SELF-GRADED.** State for `3.0.0_SA_CVO`: which boundary the replay could not cross (if any) and what FWD-2's EXERCISED bar therefore still lacks; which route's refusal came from the edge, which from the authorizer, which from the handler -- and whether that layering is what the design intended. No verdict: the instance row carries the output under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming `3.0.0_SA_CVO` at L9.


<expected_criteria>SB3-AC1, SB3-AC2</expected_criteria>


<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-sb-3.the-replay-battery-across-every-deployed-route.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>


<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> v0.1.1, cell `IB-sb-3` (s.1 the rectangle; s.2 the L5 note; s.6 the root; s.8 the bounds).
<owned_cells>IB-sb-3</owned_cells>
</decomp_ref>


<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this cell creates, changes and fires no schedule, rule or trigger; it builds a library and runs a local battery. BLIND SPOT, stated: the cut-time run (5 of 5 carriers, 0 gates naming this project) is inherited from the issuance, not re-run here.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing granted and nothing applied by this cell; no policy, role or trust document is written. BLIND SPOT: the reads this cell makes run under the launching seat's credentials, which is stated, not measured.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; the assignee's instrument at report time on its own deliverable (a fresh cut has no prior artifact for it to read).
lane: the `<paths>` block above IS the grant (RULING 1 @9ef9a40aae) plus the two tree-convention grants (`deliverables/<serial>/`, this order's own face). Every `infra/aws/**` and `data/assets/scripts/gold/**` path resolves to lane CLOUD_OPS_OR_ETL at HEAD and is admitted to you ONLY through this order while it is non-terminal; a path you need that is not listed is a BLOCKING row, never an override.
</preflight>


<proof_of_spec>
Criterion ids minted at cut: SB3-AC1, SB3-AC2. Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/IRPT_BCKEND.TO-IB-sb-3.the-replay-battery-across-every-deployed-route.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem, which `.tools/to-pipeline-gate.py` `check_complete_flip` globs for under `deliverables/*/`), per `org/standards/PROOF_OF_SPEC.schema.json`: one acceptance row per id, `criterion_verbatim` the spec's words, `invocation` the exact command, `output_evidence` the verbatim deciding excerpt, `denominator` beside every count, `expect` carried from this face; a judgment row under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming the CVO. Validate with `python .tools/proof-of-spec-check.py org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/IRPT_BCKEND.TO-IB-sb-3.the-replay-battery-across-every-deployed-route.proof_of_spec.json SB3-AC1,SB3-AC2` BEFORE the complete flip; rc 0 AND every mechanical criterion PASS-by-output, then flip this order's `<status>` to `complete` and commit instance, deliverables and flip together. A FAIL row leaves the order open and is your final report on it.

The grant is read from HEAD of your branch and only while this order is NON-TERMINAL: the issuance commit is in your ancestry at hand-off, so the flip is a modification, not an add.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages -- anything you would ask is a surprise row.
