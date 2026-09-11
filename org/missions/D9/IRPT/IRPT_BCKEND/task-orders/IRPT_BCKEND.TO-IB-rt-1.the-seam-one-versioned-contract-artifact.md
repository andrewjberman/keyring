# TO IRPT_BCKEND.TO-IB-rt-1 -- THE SEAM: routes.json and the eleven producer schemas published as ONE versioned contract artifact, a paired producer-to-consumer test per operation through the real dispatcher, and the S15-AC3 record reissued at the apply vintage

<to_id>IRPT_BCKEND.TO-IB-rt-1</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~2</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-11</issued_date>
<status>complete -- RT1-AC1 PASS-by-output on the RE-CUT wording (battery 10 of 10 arms, IBRT1-SEAM-PUBLISHED); RT1-AC2 RECORDED for 3.0.0_SA_CVO at L9. The first run FAILED arm (b) as first cut and that measurement stands (0 of 11 against the DOCUMENT schemas); the issuer re-cut the arm on it (channel row IRPT_BCKEND-S26) and this cell published the RESPONSE half. Handler conformance -- 8 of 11 BLOCKED-BY-W2-S16 -- is IB-rt-2 arm (g). v1 IS FROZEN AT THIS FLIP.</status>

**Directive:** D9 | **Fabric:** laptop | **Round:** 2 | **PRD:** `../prd/IRPT_BCKEND_PRD.md` v0.13 @e6ba5d9878 (ADMITTED, both L4-R halves SIGNED) | **Round-1 analysis:** `../ledger/ROUND_ANALYSIS.round1.md` @0d57ceb2f9, ruling 1 (+ 8 for C-S77) | **Slug rows this cell closes:** C-S72, C-S77 | **Decomp cell:** `IB-rt-1` (`../decompositions/IRPT_BCKEND_DECOMP.md` v0.2, s.1 + s.2) | **outcome_ref:** FWD-2 (own), FWD-3, FWD-11 (contrib); the seam of every consumer outcome | **PRD candidate:** B15

---

## IDENTITY AND WORKTREE

- **Serial:** `0.9.0_WK_IRPT_BCKEND~2` (the same subagent as round 1, continued with its context intact). Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_IRPT_BCKEND~2;`.
- **Worktree:** `/c/tmp/wk-irpt-2-2` on branch `wk-irpt_bckend-2-2`, cut by the issuer from `HEAD` of `CLOUD` at hand-off. First act: `git rev-parse --abbrev-ref HEAD` and `test -d org && test -d .tools && echo TREE-OK`; a worktree that does not carry the paths this face names is a BLOCKING row and a stop. Then the gitignored session-serial line `org/mcp/sessions/<CLAUDE_CODE_SESSION_ID>.serial` BEFORE any apply.
- **Repo root for every path below:** the worktree. Every path in this face is relative to that root; make it absolute by prefixing `/c/tmp/wk-irpt-2-2/`.
- **Commit:** `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~2 <0.9.0_WK_IRPT_BCKEND~2@opal.agent>" -F <msgfile> -- <paths>`, `<msgfile>` written with the Write tool. On your branch only; never push, merge, rebase, `checkout --` or `clean`.
- **Deliverables:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/` (granted by the tree convention; no `<paths>` entry needed). Round-2 batteries are named `battery_<cell>.py` with the cell id lower-cased and hyphens as underscores.
- **Queue:** first in slot ~2, the same subagent that built IB-s-15 and the scope resolver; nothing before it. IB-rt-2 follows in this slot; IB-rtb-1 (slot ~1) reads this cell's v1 route table as its denominator.

---

## THE CELL

**The PRD row, verbatim at @e6ba5d9878 (the one carrier; the acceptance clause draft is the bar you build to):**

- **cell:** B15 Global entitlement class + `api/scoped/investor-reporting/...` routes + permitted-firm catalogue
- **serves:** FWD-11 (contrib), FWD-2 (own)
- **brief sections consumed:** O8; IV.2 Global/scoped integration sources
- **contracts (P=produces, C=consumes):** P `ResolvedScope.principal class / permitted-firm catalogue`
- **paths: reuse:** `infra/aws/terraform/partners-api/api-gateway.tf` (`/api/scoped/advisor-intelligence/` CUSTOM auth); `infra/aws/lambda-edge/auth-validator-edge/index.mjs`; `portal/src/pages/ModelPortfolios.tsx` (pattern reference only)
- **paths: new home:** `/api/scoped/investor-reporting/...` routes under `infra/aws/terraform/investor-reporting/` **+ ONE CloudFront `ordered_cache_behavior` for `/api/scoped/investor-reporting/*` -> `APIGateway-portal` with `viewer-request: auth-validator-edge` in `infra/aws/terraform/portal-auth/cloudfront-distribution.tf` (v0.5, L5 finding `IRPT_BCKEND-S2`: routes alone fall to the SPA default behavior and answer 200 from the wrong origin; the partners-api layout has two halves)**
- **fixtures / evidence:** --
- **acceptance clause draft:** an Opal principal reaches clients at two firms through scoped routes; a firm advisor replaying the same requests is refused; same client + revision gives identical values Global vs firm-scoped; revoking Global permission takes effect; the actual authorizer, handler and storage enforcement are traced before implementation -- the MP demo-to-global translation and missing-claim fallback are NOT copied

**The CTO's ruling this cell executes (ROUND_ANALYSIS.round1.md @0d57ceb2f9, verbatim):** THE SEAM -- publish the contract as ONE versioned artifact and keep it the producer's. routes.json (11 declared method/path pairs) plus the eleven producer schemas become docs/contracts/investor-reporting/v1/ (or the equivalent path the lane already uses), each schema pinned and versioned; the frontend regenerates against them (ruled in the counterpart analysis). The backend half of C-S72: a paired producer-to-consumer test per operation runs the real dispatcher against the consumer's request, with mismatched-version and wrong-firm negatives. Meaning is not negotiated by casing: the backend PRD's II.3 definitions stand. RECORDS (ruling 8): S15-AC3 reissued at the apply vintage (C-S77).

**What L5 adds (decomposition v0.2 s.2, s.6, s.9):**

- `docs/contracts/investor-reporting/v1/`: `routes.json` (COPIED from `infra/aws/terraform/investor-reporting/api/routes.json` and then the Terraform reads THIS file -- one carrier, the api root's `routes.json` becomes a symlink-free re-export or the root reads the contract path; state which and prove `terraform plan` on the api root is clean after the move), the eleven producer schemas (`_contracts/*.schema.json`, moved or re-exported with `$id` carrying `v1` and a `contract_version` property), `CONTRACT.md` naming the version, the II.3 meaning of every field (quoted from the PRD CONTRACTS table at the pin), the wire rules (method, path, request shape, response shape, error envelope, the `X-Contract-Version` request header the consumer sends and the dispatcher checks), and the compatibility rule (a breaking change is `v2`, never an edit to `v1`).
- The paired producer-to-consumer test: for each of the 11 operations, ONE test that builds the CONSUMER's request from the counterpart's published fixture (`portal/src/api/endpoints/investor-reporting.ts` and its fixtures at the counterpart's HEAD -- read from the primary checkout, since `portal/` is a gitlink and a linked worktree does not populate it; print which checkout answered) and runs it through the REAL dispatcher (`infra/aws/lambda/investor-reporting/<handler>` entry points, in-process, with the validator's injected header set), asserting the response validates against the producer schema; plus two negatives per operation -- a mismatched `X-Contract-Version` refused with the public reason `CONTRACT_VERSION`, and a wrong-firm request refused through `FirmBinding` with 0 protected bytes.
- C-S77: `IRPT_BCKEND.TO-IB-s-15...proof_of_spec.json`'s S15-AC3 judgment record is REISSUED as a dated addendum under `deliverables/0.9.0_WK_IRPT_BCKEND~2/S15-AC3_reissued_at_apply_vintage.md` distinguishing the intended CloudFront behavior, the classified WAF normalisation and the observed refusal plane, at the apply commit (a7659fa6af / ac202969e8); the historic STOP is history, not current state.

---

## WHAT ROUND 1 DELIVERED THAT THIS CELL BUILDS ON (not rebuilt)

11 scoped routes live on `7k3ed8px20` under `naqxlm` (`infra/aws/terraform/investor-reporting/api/`, converged 23 of 23); the CloudFront behavior live (28 behaviors); `routes.json` with 12 entries (11 declared + 1 `NO-HANDLER-AT-HEAD` for holdings); the eleven `_contracts/*.schema.json` generated from the CONTRACTS table; `_scope/global.py`, the roster path, `FirmBinding`; the counterpart's typed client and consumer fixtures (its round-2 cell regenerates against THIS artifact).

**ISSUER AMENDMENT (2.0.0_SA_COO~B, 2026-09-11 ~12:3xZ, on the OPEN order at its first drain (0e60e9645b) -- the disarm of ROW W2-S16 (BLOCKING) and the record of W2-S13/S14/S15/S17; recorded as channel row `IRPT_BCKEND-S26`; a criterion RE-CUT under the issuer's standing authority on a proxy criterion, four-part test in the row):**
- **THE FINDING STANDS: the eleven published schemas are DOCUMENT contracts, not RESPONSE contracts.** Two of them can never be an HTTP response (`AnalysisRequest` is a queue message; `RenderPackage` is the renderer's package, produced by the FRONTEND -- W2-S17), and the six handlers answer in three ad-hoc envelopes. Arm (b) as cut asked this cell to prove a thing only the handler cells can make true; it was a proxy on the wrong cell.
- **v1 GROWS BEFORE IT FREEZES (it freezes at THIS order's complete flip, which has not happened): the seam publishes the RESPONSE contracts.** `docs/contracts/investor-reporting/v1/responses/<operation>.response.schema.json`, one per route in `routes.json` (the denominator printed), all sharing ONE envelope: `{contract_version, operation, firm_id (opaque), data, status?}` with `additionalProperties:false`, where `data` is the producer DOCUMENT the route returns (or a declared slice/list of it, `$ref` to the document schema) -- the analysis `POST` returns the request's issued ids and a `StatusEnvelope`, the export routes return `ExportReceipt`, the status route returns `StatusEnvelope`, the download route returns the Opal-signed URL record; `CONTRACT.md` gains a per-schema PRODUCER column (`RenderPackage`: FNTEND; the other ten: IRPT_BCKEND), the operation <-> route table as the ONE authority for what an operation is (W2-S13: the consumer's two orphan operations named `NOT-A-ROUTE` with the reason; the producer's three orphan routes named with their consumer, if any), and the wire-casing rule (W2-S14: the counterpart's generated client camelizes at the wire boundary; no meaning moves; nothing in v1 changes for it).
- **ARM (b) RE-CUT:** the paired test validates each operation's RESPONSE against its response schema AND its `data` against the document schema. For an operation whose deployed handler at HEAD does not yet emit the envelope, the arm prints `BLOCKED-BY-W2-S16` for that operation with the envelope it did return (0 protected bytes), prints `N of 11` conforming, and the token is NOT withheld by that count -- handler conformance is `IB-rt-2` arm (g) (same slot, your next order, which owns and deploys the six handlers). The analysis-report operation that reaches AWS in-process (W2-S15) is printed `DEPLOYED-ONLY` and graded at `IB-rtb-1`; no client is patched into a real handler.
- **THE `X-Contract-Version` CHECK is committed and NOT SERVED** until IB-rt-2 deploys the dispatchers; arm (c) grades it in-process here and IB-rt-2 arm (g) grades it served.

---

## DELIVERABLE

`docs/contracts/investor-reporting/v1/{routes.json,CONTRACT.md,<Contract>.schema.json x11,responses/<operation>.response.schema.json x11}` (CONTRACT.md with the producer column, the operation <-> route table and the casing rule); the api root reading the contract path (or the documented re-export) with a clean plan; `infra/aws/lambda/investor-reporting/_contracts/tests/test_seam_paired.py` (11 operations x 3 cases); the dispatcher's `X-Contract-Version` check in `_authz` or the dispatcher module (state which); `deliverables/0.9.0_WK_IRPT_BCKEND~2/S15-AC3_reissued_at_apply_vintage.md`; the battery `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/battery_ib_rt_1.py` and `.result.md`.

---

## BOUNDS

- **The producer defines, the consumer conforms.** No field's meaning, unit or date changes to match the frontend; where the counterpart's fixture disagrees with II.3, the test FAILS and the disagreement is a row naming the field -- the counterpart changes, not the schema.
- **`v1` is immutable once this cell flips complete**; a change after that is `v2`.
- **No deploy of a Lambda in this cell**; if the version check requires a code change in a deployed dispatcher, that change is committed here and its deploy rides IB-rt-2 (same slot, next order), stated in the instance.

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

<criterion id="RT1-AC1" cell_refs="IB-rt-1"><invocation>timeout 600 python org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/battery_ib_rt_1.py</invocation><expect>IBRT1-SEAM-PUBLISHED</expect></criterion>
**`RT1-AC1` -- PASSES BY OUTPUT -- one artifact, eleven paired tests, the record reissued.**
**(a) ONE CARRIER.** `docs/contracts/investor-reporting/v1/routes.json` byte-equals what the api root reads (print the mechanism and the hash on both sides); the eleven schemas carry `$id` with `v1` and `contract_version`; `CONTRACT.md` names every field's II.3 meaning (census: fields in schemas `N of N` named).
**(b) ELEVEN OF ELEVEN, THROUGH THE REAL DISPATCHER -- RE-CUT at the first drain (row W2-S16, channel row S26).** For each operation the consumer's request (from the counterpart's fixture, checkout printed) runs through the real handler entry point; the RESPONSE is validated against `responses/<operation>.response.schema.json` and its `data` against the document schema. Print `N of 11` conforming; for each non-conforming operation print `BLOCKED-BY-W2-S16` with the ad-hoc envelope it returned (0 protected bytes) -- the count does NOT withhold the token (conformance is IB-rt-2 arm (g)); an operation that reaches AWS in-process prints `DEPLOYED-ONLY` (row W2-S15). The eleven response schemas exist, validate as schemas, and each `data` `$ref` resolves to a document schema (`11 of 11`); for any operation whose consumer fixture disagrees with II.3, the field and the row id filed.
**(c) TWENTY-TWO NEGATIVES.** Per operation, a mismatched `X-Contract-Version` refused with public reason `CONTRACT_VERSION` and a wrong-firm request refused with 0 protected bytes; `22 of 22`, byte census per refusal.
**(d) THE API ROOT IS CLEAN AFTER THE MOVE.** `terraform plan` on `infra/aws/terraform/investor-reporting/api` after the contract path is wired reads `No changes` (printed).
**(e) C-S77 REISSUED.** The addendum exists, names the apply commit, and distinguishes the three things the ruling names (grep-census of the three headings, `3 of 3`).

<criterion id="RT1-AC2" cell_refs="IB-rt-1" judgment="true"/>
**`RT1-AC2` -- JUDGMENT, RECORDED AND NOT SELF-GRADED.** State for `3.0.0_SA_CVO`: which operations' consumer fixtures disagreed with II.3 and how each was dispositioned (schema unchanged, row filed); what the paired test cannot show about the REAL wire (CloudFront, the edge validator, API Gateway's authorizer cache) that IB-rtb-1 must; and whether `v1` as published carries any field the PRD CONTRACTS table does not name. No verdict: the instance row carries the output under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming `3.0.0_SA_CVO` at L9.


<expected_criteria>RT1-AC1, RT1-AC2</expected_criteria>


<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rt-1.the-seam-one-versioned-contract-artifact.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
docs/contracts/investor-reporting/
infra/aws/lambda/investor-reporting/_contracts/
infra/aws/lambda/investor-reporting/_authz/
infra/aws/terraform/investor-reporting/api/
infra/aws/lambda/investor-reporting/PATH_MANIFEST.json
</paths>


<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> v0.2, cell `IB-rt-1` (s.1 the rectangle; s.2 the L5 note; s.6 the root; s.8 the bounds).
<owned_cells>IB-rt-1</owned_cells>
</decomp_ref>


<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this cell creates, changes and fires no schedule, rule or trigger. BLIND SPOT, stated: the round-1 cut-time run (5 of 5 carriers, 0 gates naming this project) is inherited, not re-run here.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing granted and nothing applied by this cell; no policy, role or trust document is written. BLIND SPOT: the reads this cell makes run under the launching seat's credentials, stated not measured.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; the assignee's instrument at report time on its own deliverable.
lane: the `<paths>` block above IS the grant (RULING 1 @9ef9a40aae) plus the two tree-convention grants (`deliverables/<serial>/`, this order's own face). Every `infra/aws/**`, `docs/contracts/**` and `data/assets/scripts/gold/**` path resolves to lane CLOUD_OPS_OR_ETL or its documentation lane at HEAD and is admitted to you ONLY through this order while it is non-terminal; a path you need that is not listed is a BLOCKING row, never an override.
</preflight>


<proof_of_spec>
Criterion ids minted at cut: RT1-AC1, RT1-AC2. Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/IRPT_BCKEND.TO-IB-rt-1.the-seam-one-versioned-contract-artifact.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem, which `.tools/to-pipeline-gate.py` `check_complete_flip` globs for under `deliverables/*/`), per `org/standards/PROOF_OF_SPEC.schema.json`: one acceptance row per id, `criterion_verbatim` the spec's words, `invocation` the exact command, `output_evidence` the verbatim deciding excerpt, `denominator` beside every count, `expect` carried from this face; a judgment row under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming the CVO. Validate with `python .tools/proof-of-spec-check.py org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/IRPT_BCKEND.TO-IB-rt-1.the-seam-one-versioned-contract-artifact.proof_of_spec.json RT1-AC1,RT1-AC2` BEFORE the complete flip; rc 0 AND every mechanical criterion PASS-by-output, then flip this order's `<status>` to `complete` and commit instance, deliverables and flip together. A FAIL row leaves the order open and is your final report on it. The PENDING-THIS-COMMIT sentinel is one-shot: pin artifact rows to the commit that carries them.

The grant is read from HEAD of your branch and only while this order is NON-TERMINAL: the issuance commit is in your ancestry at hand-off, so the flip is a modification, not an add.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages -- anything you would ask is a surprise row.
