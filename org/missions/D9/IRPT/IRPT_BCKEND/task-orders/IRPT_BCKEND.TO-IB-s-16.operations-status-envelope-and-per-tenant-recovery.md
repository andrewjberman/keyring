# TO IRPT_BCKEND.TO-IB-s-16 -- OPERATIONS: the StatusEnvelope, manifests, clocks, leases and traces -- and the seven failure arms driven on the deployed jobs, each shown to touch no second firm

<to_id>IRPT_BCKEND.TO-IB-s-16</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~1</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-10</issued_date>
<status>staged -- assigned to slot ~1; becomes pending when the COO hands it over after IB-s-6, IB-s-9, IB-s-12 and IB-s-14 are all terminal and merged.</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_BCKEND_PRD.md` v0.4 @62301f71e0 | **Decomp cell:** `IB-s-16` (`../decompositions/IRPT_BCKEND_DECOMP.md` v0.1.1, s.1 + s.2) | **outcome_ref:** FWD-10 (own, the proof arms), FWD-7, FWD-6 (contrib) | **PRD candidate:** B16

---

## IDENTITY AND WORKTREE

- **Serial:** `0.9.0_WK_IRPT_BCKEND~1`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_IRPT_BCKEND~1;`.
- **Worktree:** `/c/tmp/wk-irpt-1-1` on branch `wk-irpt_bckend-1-1`, cut by the issuer from `HEAD` of `CLOUD` at hand-off. First act: `git rev-parse --abbrev-ref HEAD` and `test -d org && test -d .tools && echo TREE-OK`; a worktree that does not carry the paths this face names is a BLOCKING row and a stop.
- **Repo root for every path below:** the worktree. Every path in this face is relative to that root; make it absolute by prefixing `/c/tmp/wk-irpt-1-1/`.
- **Commit:** `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~1 <0.9.0_WK_IRPT_BCKEND~1@opal.agent>" -F <msgfile> -- <paths>`, `<msgfile>` written with the Write tool. On your branch only; never push, merge, rebase, `checkout --` or `clean`.
- **Deliverables:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/` (granted by the tree convention; no `<paths>` entry needed).
- **Queue:** fourth in slot ~1, after IB-s-5; cross-slot waits on IB-s-6 (~3), IB-s-9 (~3), IB-s-12 (~2), IB-s-14 (~4).

---

## THE CELL

**The PRD row, verbatim at @62301f71e0 (the one carrier; the acceptance clause draft is the bar you build to):**

- **cell:** B16 operations: `StatusEnvelope`, manifests, clocks, leases, retries, traces, per-tenant recovery
- **serves:** FWD-10 (own, the proof arms), FWD-6 (contrib), FWD-7
- **brief sections consumed:** O7 operations paragraph; IV.2 BRONZE-SILVER-GOLD-PLATINUM paragraph; IV.7 path-manifest requirement
- **contracts (P=produces, C=consumes):** P `StatusEnvelope`
- **paths: reuse:** --
- **paths: new home:** `infra/aws/lambda/investor-reporting/`; `infra/aws/terraform/investor-reporting/` (queues, leases, DynamoDB keys, outbox)
- **fixtures / evidence:** --
- **acceptance clause draft:** failed source partition, stale model map, duplicated event, expired lease, queue replay, worker restart, revocation mid-job -- each recovers one provider or tenant with unaffected functions available and NO second-firm effect; failed work cannot publish a false-complete snapshot, overwrite newer output or resurrect a permission; every published snapshot reconciles to its input lineage; a path manifest names each dependency and owner

**What L5 adds (decomposition v0.1.1 s.2, s.6, s.9):**

- `infra/aws/lambda/investor-reporting/ops/` (Lambda `irpt-status`): the `StatusEnvelope` producer (operation + revision; the nine states queued / running / ready / partial / stale / unavailable / needs-correction / uncertain / failed; source dates; safe retry/recovery actions; a PUBLIC reason code and an INTERNAL correlation id; no credential or infrastructure payload), source-completion manifests with explicit business/data clocks, and the recovery runbook `RUNBOOK.md` (how an operator recovers ONE provider or tenant while unaffected functions stay available).
- The seven recovery arms, driven on the DEPLOYED jobs of IB-s-6 (intake), IB-s-9 (generation), IB-s-12 (holdings) and IB-s-14 (export) under QA prefixes: a failed source partition, a stale model map, a duplicated event, an expired lease, a queue replay, a worker restart, a revocation during a job -- each shown to recover the one tenant AND to leave a second firm's objects byte-identical (hash before == after, denominator printed). Three difference controls: failed work cannot publish a false-complete snapshot; cannot overwrite a newer result with an older one; cannot resurrect a revoked permission.
- Every published snapshot reconciles to its input lineage (manifest ids); `PATH_MANIFEST.json` (IB-s-18) is COMPLETE at this point -- every concrete read/write path the deployed cells use has an owner (`N of N`, the manifest's denominator against a census of the deployed roles' policies).

**ISSUER AMENDMENT (2.0.0_SA_COO~B, 2026-09-11 ~01:4xZ, at the IB-s-3 drain, before this order was handed -- the disarm of rows `IRPT_BCKEND-W2-S9` and `IRPT_BCKEND-W2-S10`, whose disarm_owner is the issuer; recorded as channel row `IRPT_BCKEND-S9`):**
- **EVERY HANDLER THIS CELL SHIPS IS WRAPPED BY `_authz.guard()`** (`infra/aws/lambda/investor-reporting/_authz/enforce.py`, merged at 3cca035c66): resolve, reauthorize before serving, keys through `_keys`, one refusal envelope. A handler reachable through a route without `guard()` is a defect this cell's own battery prints: `_authz.unguarded_routes()` over the routes this cell registers reads `0 of N`, N printed. Where this cell ships no handler, the same census runs over `routes.json` at the replay.
- **THE FIRM ID HAS TWO SPELLINGS AND ONLY `_authz.FirmBinding` RECONCILES THEM (row W2-S9).** `X-Firm-Id` and `_keys.cache_key` carry the REGISTRY id (`49financial`); `DirectoryEntry.ids.firm_id` and the `_scope` cross-firm filter carry the OPAQUE id (`fir_...`, `directory_runner.opaque_id`). A handler that passes the header value into the directory join returns an EMPTY population that reads exactly like a revocation, and no per-module test can see it. Every firm-scoped read this cell makes binds through `FirmBinding`, proven against the directory artifact's own `firm_id_opaque`; a binding that does not reconcile is a REFUSAL (`FIRM_BINDING`), never an empty set. No hash is recomputed and `opaque_id` is not duplicated into a Lambda.
- **A `_keys` REFUSAL NAMES THE REFUSED VALUE (row W2-S10).** `KeyComponentRefused` carries the component with `%r` at twelve message sites; `str(exc)` in a response, a log line, an audit row, a battery print or a surprise row DISCLOSES exactly the value that was refused for being a client name or an e-mail address. Nothing this cell writes surfaces a `_keys` exception's text: the wrapper's refusal reason (parameter NAMES, found through the public `cache_key`) is the only refusal that leaves a handler, and at least one test asserts over the WHOLE envelope (body + reason + audit trail), never the census alone. `_keys` itself is not edited by this cell (not in its `<paths>`; the sanitised exception is the issuer's round-2 item on IB-s-17's surface).
- **THE DIRECTORY AND PERFORMANCE HANDLERS ALREADY MERGED (IB-s-1, IB-s-11) PREDATE THE WRAPPER** -- a decomposition sequencing defect of the issuer, carried to L10; this cell does not edit them, and IB-sb-3's replay is where their unguarded state is measured.

---

## DELIVERABLE

`infra/aws/lambda/investor-reporting/ops/` (`status.py`, `manifests.py`, `RUNBOOK.md`) + `tests/`; `infra/aws/terraform/investor-reporting/ops/` (`lambda.tf`, `iam.tf`, `main.tf` completed); the seven-arm harness `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/ib_s_16_recovery_arms.py`; the ledger entry + sentinel; the battery `battery_ib_s_16.py` and `.result.md`.

---

## BOUNDS

- **The arms run under QA prefixes** (`investor-reporting/qa/` and `firms/<id>/qa/`); no served object is touched.
- **No notification is built** (G-20); the envelope is a product status, not an alarm.
- **A second firm's objects are hashed BEFORE and AFTER every arm**; an arm without that pair is not an arm.

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

<criterion id="S16-AC1" cell_refs="IB-s-16"><invocation>timeout 600 python org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/battery_ib_s_16.py</invocation><expect>IBS16-RECOVERY-ISOLATED</expect></criterion>
**`S16-AC1` -- PASSES BY OUTPUT -- seven arms, three difference controls, the manifest complete.**
**(a) SEVEN OF SEVEN, SECOND FIRM UNTOUCHED.** Each arm driven on the deployed job it targets; the affected tenant recovers (state printed); the second firm's object set hashes identical before and after (`N of N` objects). Printed per arm.
**(b) THREE DIFFERENCE CONTROLS.** A failed run cannot publish a false-complete snapshot (it publishes `partial`/`failed`, never `ready`); an older result cannot overwrite a newer one (revision check printed); a revoked permission is not resurrected by a retry (refused, printed). A build with any guard disabled FAILS the arm.
**(c) NINE STATES, ONE ENVELOPE.** Each state produced by a fixture; the envelope validates; no credential or infrastructure field in the public view (census).
**(d) LINEAGE.** Every snapshot published in the arms reconciles to its input manifest ids (`N of N`).
**(e) THE MANIFEST IS COMPLETE.** Census the deployed roles' policies for every S3 prefix, table and queue they touch (denominator printed) and show each has a `PATH_MANIFEST.json` entry with an owner.
**(f) LEDGER CLOSED.** `get-function-configuration irpt-status` `CodeSha256` equals the built zip's; sentinel committed (hash).

**(amend) GUARDED, BOUND, AND SILENT ON THE REFUSED VALUE (issuer amendment at the IB-s-3 drain, rows W2-S9 / W2-S10).** `unguarded_routes()` over this cell's routes reads `0 of N` (N printed); every firm-scoped read binds through `FirmBinding` and a fixture with a non-reconciling binding is REFUSED with `FIRM_BINDING` rather than served empty; a fixture that keys by a client display name is refused and the whole envelope (body + reason + audit trail) contains 0 occurrences of the refused value (census printed). Where this cell ships no handler, the arm reads over `routes.json` at the replay. CLARIFIED at the IB-s-7 drain (row W3-S5, disarm by the issuer): `routes.json` is IB-s-15's deliverable at `infra/aws/terraform/investor-reporting/api/routes.json` and does not exist before that cell lands; a cell that ships no handler and runs before it does NOT report a `0 of 0` census as a pass -- it prints the census AS VACUOUS and runs the two CONTROLS IB-s-7's battery ran (a handler registered unguarded censused `1 of 1`; the same handler wrapped censused `0 of 1`), so the arm proves the censor, not an empty set. IB-s-15 and IB-sb-3 read the real file.

<criterion id="S16-AC2" cell_refs="IB-s-16"><invocation>timeout 120 .tools/terraform.exe -chdir=infra/aws/terraform/investor-reporting/ops plan -no-color -input=false -lock=false</invocation><expect>No changes\. Your infrastructure matches the configuration\.</expect></criterion>
**`S16-AC2` -- THE ROOT IS CONVERGED after this cell's apply.**
Run after the apply and after the ledger closes.

<criterion id="S16-AC3" cell_refs="IB-s-16" judgment="true"/>
**`S16-AC3` -- JUDGMENT, RECORDED AND NOT SELF-GRADED.** State for `3.0.0_SA_CVO`: which failure modes the seven arms do NOT cover (a KMS key disabled, a bucket policy edited by hand, a Graph delta that never expires); whether 'no path by which a second firm could be touched' is shown by the arms or only by the IAM conditions (name which); and what the runbook assumes about the operator's own permissions. No verdict: the instance row carries the output under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming `3.0.0_SA_CVO` at L9.


<expected_criteria>S16-AC1, S16-AC2, S16-AC3</expected_criteria>


<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-s-16.operations-status-envelope-and-per-tenant-recovery.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
infra/aws/lambda/investor-reporting/ops/
infra/aws/terraform/investor-reporting/ops/
infra/aws/lambda/investor-reporting/PATH_MANIFEST.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/irpt-bckend-s16.json
infra/aws/lambda/ci/lambda-source-map.json
</paths>


<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> v0.1.1, cell `IB-s-16` (s.1 the rectangle; s.2 the L5 note; s.6 the root; s.8 the bounds).
<owned_cells>IB-s-16</owned_cells>
</decomp_ref>


<preflight>
comp-schedule: RUN at the cut (20:2xZ, --budget 150) -- WITHIN BUDGET, denominator 5 of 5 carriers (C1=92 C2=6 C3=12 C4=20 C5=335), 25 gates ARMED, 0 name IRPT or any surface of this cell; the moratoria that bind here are G-20 (no monitor), G-23 (cross-firm), G-24 (vendor egress). BLIND SPOT: a ledger of gates, not prose obligations; 137 prose blocking fields unread.
comp-iam: RUN at the cut -- `comp-iam stats` + `roles`: denominator 191 roles parsed, 188 services, 307 gaps estate-wide; ZERO investor-reporting roles exist on the DESIRED plane, so this cell's role is graded at Phase 1 by `comp-iam service irpt-status` once its `.tf` exists and at Phase 2 by `comp-iam gaps` -- both recorded in the instance. BLIND SPOT: DESIRED plane only (the repo's Terraform); a GRANTED-BROAD wildcard cannot be falsified by a resource check.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; the assignee's instrument at report time on its own deliverable (a fresh cut has no prior artifact for it to read).
lane: the `<paths>` block above IS the grant (RULING 1 @9ef9a40aae) plus the two tree-convention grants (`deliverables/<serial>/`, this order's own face). Every `infra/aws/**` and `data/assets/scripts/gold/**` path resolves to lane CLOUD_OPS_OR_ETL at HEAD and is admitted to you ONLY through this order while it is non-terminal; a path you need that is not listed is a BLOCKING row, never an override.
</preflight>


<proof_of_spec>
Criterion ids minted at cut: S16-AC1, S16-AC2, S16-AC3. Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/IRPT_BCKEND.TO-IB-s-16.operations-status-envelope-and-per-tenant-recovery.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem, which `.tools/to-pipeline-gate.py` `check_complete_flip` globs for under `deliverables/*/`), per `org/standards/PROOF_OF_SPEC.schema.json`: one acceptance row per id, `criterion_verbatim` the spec's words, `invocation` the exact command, `output_evidence` the verbatim deciding excerpt, `denominator` beside every count, `expect` carried from this face; a judgment row under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming the CVO. Validate with `python .tools/proof-of-spec-check.py org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/IRPT_BCKEND.TO-IB-s-16.operations-status-envelope-and-per-tenant-recovery.proof_of_spec.json S16-AC1,S16-AC2,S16-AC3` BEFORE the complete flip; rc 0 AND every mechanical criterion PASS-by-output, then flip this order's `<status>` to `complete` and commit instance, deliverables and flip together. A FAIL row leaves the order open and is your final report on it.

The grant is read from HEAD of your branch and only while this order is NON-TERMINAL: the issuance commit is in your ancestry at hand-off, so the flip is a modification, not an add.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages -- anything you would ask is a surprise row.
