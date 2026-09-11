# TO IRPT_BCKEND.TO-IB-rt-4 -- TYPED IDS AT EVERY KEY-BUILDER BOUNDARY AND THE EXCEPTION PATH: every key constructor rejects a name or an e-mail without echoing it, and every reachable error path returns a public reason with a correlation id, never str(exc)

<to_id>IRPT_BCKEND.TO-IB-rt-4</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~3</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-11</issued_date>
<status>pending -- GO paired at the round-2 issuance (the hand-off is the GO). First order of slot ~3.</status>

**Directive:** D9 | **Fabric:** laptop | **Round:** 2 | **PRD:** `../prd/IRPT_BCKEND_PRD.md` v0.13 @e6ba5d9878 (ADMITTED, both L4-R halves SIGNED) | **Round-1 analysis:** `../ledger/ROUND_ANALYSIS.round1.md` @0d57ceb2f9, ruling 4 (keys and the exception path) | **Slug rows this cell closes:** W3-S12, W2-S10 | **Decomp cell:** `IB-rt-4` (`../decompositions/IRPT_BCKEND_DECOMP.md` v0.2, s.1 + s.2) | **outcome_ref:** FWD-10 (own), FWD-2 | **PRD candidate:** B17

---

## IDENTITY AND WORKTREE

- **Serial:** `0.9.0_WK_IRPT_BCKEND~3` (the same subagent as round 1, continued with its context intact). Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_IRPT_BCKEND~3;`.
- **Worktree:** `/c/tmp/wk-irpt-2-3` on branch `wk-irpt_bckend-2-3`, cut by the issuer from `HEAD` of `CLOUD` at hand-off. First act: `git rev-parse --abbrev-ref HEAD` and `test -d org && test -d .tools && echo TREE-OK`; a worktree that does not carry the paths this face names is a BLOCKING row and a stop. Then the gitignored session-serial line `org/mcp/sessions/<CLAUDE_CODE_SESSION_ID>.serial` BEFORE any apply.
- **Repo root for every path below:** the worktree. Every path in this face is relative to that root; make it absolute by prefixing `/c/tmp/wk-irpt-2-3/`.
- **Commit:** `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~3 <0.9.0_WK_IRPT_BCKEND~3@opal.agent>" -F <msgfile> -- <paths>`, `<msgfile>` written with the Write tool. On your branch only; never push, merge, rebase, `checkout --` or `clean`.
- **Deliverables:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~3/` (granted by the tree convention; no `<paths>` entry needed). Round-2 batteries are named `battery_<cell>.py` with the cell id lower-cased and hyphens as underscores.
- **Queue:** first in slot ~3, the same subagent that built intake, generation and extraction; nothing before it. IB-rt-9 follows in this slot.

---

## THE CELL

**The PRD row, verbatim at @e6ba5d9878 (the one carrier; the acceptance clause draft is the bar you build to):**

- **cell:** B17 tenant-scoped storage and keys: DynamoDB tenant/request keys, immutable revisions, S3 evidence layout, cache/idempotency keys; the REQUEST LEDGER and the ACCOUNT COORDINATOR (v0.5)
- **serves:** FWD-10 (own), FWD-2 (own), FWD-9, FWD-4 (contrib, v0.5)
- **brief sections consumed:** IV.4 records + DynamoDB paragraphs; II.3 keys paragraph; **SUPP** O4, III.4, IV.5 lease paragraph, IV.6 publication paragraph, IV.8 retention paragraph
- **contracts (P=produces, C=consumes):** P `request ledger`, `account coordinator` (server-only)
- **paths: reuse:** --
- **paths: new home:** proposed `opal-data-ycharts` SSE-KMS bucket (absent at inspection) with `firms/{firm_id}/intake|requests|generations/...` under enumerated prefixes; raw generation artifacts and normalized/report manifests under `firms/{firm_id}/{request}/{revision}/{attempt}/` prefixes; the account-coordinator table (one row per shared vendor login: lease owner, attemptId, fence, expiry, host id, command id, accepted session VersionId/generation)
- **fixtures / evidence:** --
- **acceptance clause draft:** queues carry ids not attachments; S3 holds immutable evidence, never locks; keys include tenant, account-set fingerprint, source/schema/config revisions and operation parameters; once bound the firm is immutable; **(v0.5)** firm/advisor claims are RE-CHECKED against the server's request ledger before any vendor mutation and before artifact delivery; native vendor portfolio ids are accepted only through a firm-scoped ownership mapping; a shared login or a global template catalog never confers access to another firm's request, portfolio or PDF; COOKIE BUNDLES NEVER LAND IN `opal-data-ycharts` (they live in the protected session resource, B8); the coordinator's accepted session version is authoritative and a conditional write is the only publish path

**The CTO's ruling this cell executes (ROUND_ANALYSIS.round1.md @0d57ceb2f9, verbatim):** Typed, issued identifiers at every key-builder boundary and the name/email controls rejected (W3-S12); the exception path returns a public reason and a correlation id with injected client-name / email / key-bearing negatives (W2-S10).

**What L5 adds (decomposition v0.2 s.2, s.6, s.9):**

- `_keys/keys.py`: EVERY constructor (`cache_key`, `s3_evidence_key`, `queue_message`, and any other public builder -- census them, print the denominator) takes ISSUED opaque ids of a declared type (`_ids` types from IB-rt-3 where merged, else the round-1 `_scope` id shapes) and REFUSES a display name, an e-mail address, a raw upstream key and a request-controlled firm token with a structured exception carrying the component NAME and a reason CLASS -- the refused VALUE lives in a developer-only attribute never rendered by `str()`; twelve `%r` message sites become zero.
- The exception path (W2-S10): every reachable error path in `directory/`, `_authz/`, `intake/`, `ycharts/`, `export/`, `ops/` handlers returns the ONE envelope (public reason code from a closed enum, correlation id, no `str(exc)`, no stack, no path, no key); the correlation id is logged with the internal detail server-side; injected negatives -- an exception whose message carries a client name, an e-mail, an S3 key -- produce a response and a public log line with 0 occurrences of the injected value (byte census over body + headers + the public log).
- The deploy: functions whose code changes are rebuilt and applied under ledger entries per root; `CodeSha256` verified; plans show only the code changes.

---

## WHAT ROUND 1 DELIVERED THAT THIS CELL BUILDS ON (not rebuilt)

`_keys` (IB-s-17) with `cache_key` refusing names and `s3_evidence_key` admitting them (W3-S12); `_authz`'s refusal reason built from parameter names (IB-s-3, W2-S10's fix inside the wrapper); the closed `StatusEnvelope` reason vocabulary (IB-s-16).

---

## DELIVERABLE

`infra/aws/lambda/investor-reporting/_keys/{keys.py,tests/}`; the error-envelope helper in `_authz/` used by every handler; the handler edits; the ledger entries + sentinels; the battery `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~3/battery_ib_rt_4.py` and `.result.md`.

---

## BOUNDS

- **Verify all constructors, not one** (the CVO's remedy): the census of public builders IS the denominator of arm (a).
- **Public reasons are a closed enum**; a new reason is a schema change on `StatusEnvelope` and a row, never a free string.
- **No key already written to S3 is renamed by this cell** (an S3 key move is a served-surface act, carried); the constructor's refusal is forward-only, and the round-1 evidence keys are censused and listed, not moved.

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

<criterion id="RT4-AC1" cell_refs="IB-rt-4"><invocation>timeout 600 python org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~3/battery_ib_rt_4.py</invocation><expect>IBRT4-KEYS-TYPED</expect></criterion>
**`RT4-AC1` -- PASSES BY OUTPUT -- every constructor refuses without echoing, every error path is the envelope, injected negatives leave zero trace.**
**(a) N OF N CONSTRUCTORS.** Census the public key builders in `_keys` (denominator printed); for each, four negatives (display name, e-mail, raw upstream key, request-controlled firm) REFUSED with 0 occurrences of the value in `str(exc)`, the log line and the envelope; `4N of 4N`.
**(b) THE POSITIVE STILL BUILDS.** For each constructor the round-1 valid inputs still produce the same key as at round-1 HEAD (hash equality, `N of N`) -- the refusal did not change the grammar.
**(c) THE ENVELOPE EVERYWHERE.** Census the handler error paths (denominator printed); each returns a public reason from the closed enum and a correlation id; `str(exc)` appears in 0 of them (AST census).
**(d) INJECTED NEGATIVES.** Three injected exceptions (client name, e-mail, S3 key) per handler family: 0 occurrences in body, headers and the public log; the correlation id resolves to the internal record (printed once, values redacted).
**(e) DEPLOYED.** `CodeSha256` equality per changed function; each root's post-apply plan `No changes`; ledgers CLOSED, sentinels committed.

**ISSUER AMENDMENT (2.0.0_SA_COO~B, 2026-09-11 ~14:3xZ, at the drain of this order's first report -- rows W3-S13..S18 read; the order stays OPEN and arm (e) completes at the merged tip):**
- **W3-S17 IS ROUTED, AND ITS PREMISE WAS WRONG IN A WAY THAT CHANGES NOTHING ABOUT THE WITHHELD APPLY BEING CORRECT.** The three resources the export root planned to destroy (`aws_iam_role_policy.export_render_dispatch`, `aws_iam_role_policy.export_render_evidence`, `aws_ssm_document.export_render_run`) were never removed by IB-s-14: `git show 1beda4bf49 -- infra/aws/terraform/investor-reporting/export/` removes nothing. They are IB-rt-8's, declared on `wk-irpt_bckend-2-4` at 1365a96fad, applied by that cell into the shared export state at 67aa231c29, and merged onto CLOUD at 790d948e98. This order's worktree was cut before that branch existed, so its plan read another cell's live, declared resources as orphans. NOT destroyed, NOT re-declared, NOT state-rm'd: the route is the merge, which has now happened. The "second writer" on the root was the same cell (IB-rt-8's controller deploy at 12:57:39Z), sequenced by the drain, not concurrent any more.
- **THE DRAIN TOOK IB-rt-8's SIDE OF `export/handler.py`, `export/render.py` AND THE EXPORT ENTRY OF `lambda-source-map.json`** (rt-8 restructured the function into a controller -- `submit_export`, `persist_bundle`, `finalize_export`, `dispatch`, `exclusion`, `identity`, `package` -- and its bytes are what the function SERVES). This order's edits to those two files (the `_fail` envelope, `_internal_sink`/`_public_log`, `build_enforcer`, the parser-message hygiene in `render.py`, `errors.py` in the packaged list) are NOT in the tree at 790d948e98 and are re-applied by this order ON THE CONTROLLER STRUCTURE at the merged tip; arm (c)'s census re-runs over the merged module set and prints its denominator again. Every other file of this order merged clean and is in the tree.
- **ARM (e) AT THE MERGED TIP, in this order:** (1) `terraform plan` on the export root reads ONLY this order's code change (`0 to destroy`; print the plan summary line) -- if it reads anything else, STOP and file a row; (2) the export function's build input gains `enforce.py` (with its own imports) and `errors.py` (row W3-S14: `download.py` imports `enforce` at module level and the zip never carried it -- the import-closure check in a clean subprocess prints `6 of 6` functions importable in the `/var/task` layout, and that check is an arm of the battery); (3) `irpt-common` is REBUILT FROM THE MERGED TREE (row W4-S15: the layer is a shared write surface; two cells published it last-writer-wins; the union of every cell's CONTRACTS/MODULES/DATA lists at the tip), published as a new version, and `3 of 3` functions repointed BEFORE any apply of the performance root; the runtime capabilities read prints `5 of 5` contracts; (4) ledger OPEN sentinel committed, apply through `.tools/safe-apply.sh`, post-apply plan `No changes`, ledger CLOSED; (5) registration: `artifact_sha256` in `lambda-source-map.json` equals the S3 object's `content-sha256` metadata equals the live `CodeSha256`, printed `6 of 6` (row W3-S18 -- the export registration at the tip is IB-rt-8's and is re-registered here because this order deploys the function).
- Arm (c)'s denominator (row W3-S15) is NOT widened by this amendment: the one ordinary-return instance is fixed; the dataflow census is carried to L10 by name.

<criterion id="RT4-AC2" cell_refs="IB-rt-4" judgment="true"/>
**`RT4-AC2` -- JUDGMENT, RECORDED AND NOT SELF-GRADED.** State for `3.0.0_SA_CVO`: which round-1 S3 keys already carry a name-shaped component (the census and the list) and what removing them would require; whether the closed reason enum lost any diagnostic an operator needs; and which error path you could not reach with an injected exception. No verdict: the instance row carries the output under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming `3.0.0_SA_CVO` at L9.


<expected_criteria>RT4-AC1, RT4-AC2</expected_criteria>


<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rt-4.typed-ids-at-every-key-boundary-and-the-exception-path.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
infra/aws/lambda/investor-reporting/_keys/
infra/aws/lambda/investor-reporting/_authz/
infra/aws/lambda/investor-reporting/directory/
infra/aws/lambda/investor-reporting/intake/
infra/aws/lambda/investor-reporting/ycharts/
infra/aws/lambda/investor-reporting/export/
infra/aws/lambda/investor-reporting/ops/
infra/aws/terraform/investor-reporting/directory/
infra/aws/terraform/investor-reporting/intake/
infra/aws/terraform/investor-reporting/ycharts/
infra/aws/terraform/investor-reporting/export/
infra/aws/terraform/investor-reporting/ops/
infra/aws/lambda/investor-reporting/PATH_MANIFEST.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/irpt-bckend-rt4.json
infra/aws/lambda/ci/lambda-source-map.json
</paths>


<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> v0.2, cell `IB-rt-4` (s.1 the rectangle; s.2 the L5 note; s.6 the root; s.8 the bounds).
<owned_cells>IB-rt-4</owned_cells>
</decomp_ref>


<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this cell creates, changes and fires no schedule, rule or trigger. BLIND SPOT, stated: the round-1 cut-time run (5 of 5 carriers, 0 gates naming this project) is inherited, not re-run here.
comp-iam: RUN at the round-1 cut (191 roles parsed, 307 gaps estate-wide) and the round-1 roles now exist on the DESIRED and APPLIED planes; this cell's change to `every function whose code changes` is re-graded by the assignee at Phase 1 by `comp-iam service every function whose code changes` and at Phase 2 by `comp-iam gaps` -- both recorded in the instance. BLIND SPOT: DESIRED plane only; a GRANTED-BROAD wildcard cannot be falsified by a resource check.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; the assignee's instrument at report time on its own deliverable.
lane: the `<paths>` block above IS the grant (RULING 1 @9ef9a40aae) plus the two tree-convention grants (`deliverables/<serial>/`, this order's own face). Every `infra/aws/**`, `docs/contracts/**` and `data/assets/scripts/gold/**` path resolves to lane CLOUD_OPS_OR_ETL or its documentation lane at HEAD and is admitted to you ONLY through this order while it is non-terminal; a path you need that is not listed is a BLOCKING row, never an override.
</preflight>


<proof_of_spec>
Criterion ids minted at cut: RT4-AC1, RT4-AC2. Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~3/IRPT_BCKEND.TO-IB-rt-4.typed-ids-at-every-key-boundary-and-the-exception-path.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem, which `.tools/to-pipeline-gate.py` `check_complete_flip` globs for under `deliverables/*/`), per `org/standards/PROOF_OF_SPEC.schema.json`: one acceptance row per id, `criterion_verbatim` the spec's words, `invocation` the exact command, `output_evidence` the verbatim deciding excerpt, `denominator` beside every count, `expect` carried from this face; a judgment row under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming the CVO. Validate with `python .tools/proof-of-spec-check.py org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~3/IRPT_BCKEND.TO-IB-rt-4.typed-ids-at-every-key-boundary-and-the-exception-path.proof_of_spec.json RT4-AC1,RT4-AC2` BEFORE the complete flip; rc 0 AND every mechanical criterion PASS-by-output, then flip this order's `<status>` to `complete` and commit instance, deliverables and flip together. A FAIL row leaves the order open and is your final report on it. The PENDING-THIS-COMMIT sentinel is one-shot: pin artifact rows to the commit that carries them.

The grant is read from HEAD of your branch and only while this order is NON-TERMINAL: the issuance commit is in your ancestry at hand-off, so the flip is a modification, not an add.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages -- anything you would ask is a surprise row.
