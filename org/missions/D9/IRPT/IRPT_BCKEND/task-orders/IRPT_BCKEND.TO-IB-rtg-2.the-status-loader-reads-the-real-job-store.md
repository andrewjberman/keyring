# TO IRPT_BCKEND.TO-IB-rtg-2 -- THE STATUS LOADER READS THE REAL JOB STORE: round 6's status tab returned UNSUPPORTED_OPERATION on a served request (FWD-2). The cause is a WIRING GAP, not a data absence: `ops/entry.py:56-104` passes `ops/status.py:338-345`'s `_default_status_loader` as the fallback, and that default ALWAYS raises `NoSuchOperation("no status_loader was configured ... lambda_handler must call register_routes(enforcer, real_loader)")`. The read-side building blocks already exist -- `ops/manifests.py:57-90` `build_source_completion_manifest` reuses `intake/checkpoint.py`'s `irpt-jobs` DynamoDB store -- but no function ever composes them into a real loader and wires it in. This order writes the real `status_loader` against the backend's OWN job store and wires it in place of the always-raising default.

<to_id>IRPT_BCKEND.TO-IB-rtg-2</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~2</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-20</issued_date>
<status>pending -- HANDED by 2.0.0_SA_COO~B at 2026-09-20 (round 7, the recut on the round-6 analysis @fa2ff4f0dd). The status data path is one of round 7's four backend cells; scope confirmed by investigation a7edd66ed0 (backend wiring against the backend's own irpt-jobs store, not a DS feed). Served-path handler deploy -> both never-widen halves at HEAD BEFORE any apply.</status>

**Directive:** D9 | **Fabric:** laptop | **Round:** 7 (the CTO's round-6 analysis @fa2ff4f0dd) | **PRD:** `../prd/IRPT_BCKEND_PRD.md` v0.15 | **Round-6 analysis:** `../deliverables/1.0.0_SA_CTO/IRPT_BCKEND_ROUND6_ANALYSIS.md` @fa2ff4f0dd | **Decomp cell:** `IB-rtg-2` (`../decompositions/IRPT_BCKEND_DECOMP.md` v0.7 @a1c21f1424, s.R7.1) | **outcome_ref:** FWD-2

---

## IDENTITY AND WORKTREE

- **Serial:** `0.9.0_WK_IRPT_BCKEND~2`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_IRPT_BCKEND~2;`.
- **Worktree:** `/c/tmp/wk-irpt-7-2` on branch `wk-irpt_bckend-7-2`, cut by the issuer from CLOUD HEAD at hand-off; `.tools/terraform.exe` provisioned there. First act: `git rev-parse --abbrev-ref HEAD` and `test -d org && test -d .tools && echo TREE-OK`; then write the gitignored session-serial line BEFORE any apply.
- **Repo root for every path below:** the worktree; prefix `/c/tmp/wk-irpt-7-2/`.
- **Commit:** `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~2 <0.9.0_WK_IRPT_BCKEND~2@opal.agent>" -F <msgfile> -- <paths>`, `<msgfile>` via the Write tool. On your branch only; never push/merge/rebase/`checkout --`/`clean`. Capture safe-commit output to a file, never `| tail`, never with `$( )`.
- **Python:** `py -3.12`. AWS through `.tools/aws`. `.tools/terraform.exe` by that path. Recursive `grep`/`find` in Bash is rail-DENIED; use Read/Grep tools. `build-and-upload.sh` from a `/c/` cwd.

---

## THE CELL

- (a) MEASURE FIRST, printed: read `ops/entry.py:56-104`, `ops/status.py:338-345`, `ops/manifests.py:57-90` and `intake/checkpoint.py` at HEAD; confirm the wiring gap (`_default_status_loader` is the only loader supplied and it always raises `NoSuchOperation`) and the reachable job-state building blocks (TenantLease/checkpoint reads + `build_source_completion_manifest`) against the `irpt-jobs` DynamoDB table the backend's OWN `intake/` + `ycharts/generate/job.py` populate. Re-derive any grant/count LIVE and PRINT it, never inherit a round-6 number. The mutant for the wiring: the pre-fix `_default_status_loader` path still raising `NoSuchOperation` on the exercised job.
- (b) THE SOURCE EDIT: write the real `status_loader(request, scope)` in `ops/` (compose `TenantLease`/checkpoint state + `ops/manifests.py` helpers against `irpt-jobs`; return a validated `StatusEnvelope`), and WIRE it into `ops/entry.py` at the `register_routes`/`_status_envelope` `loader` argument in place of `_default_status_loader`. No new DynamoDB table, no external feed -- read the store the backend already owns. Then `infra/aws/lambda/ci/build-and-upload.sh investor-reporting irpt-status` (confirm the served function name at `_ids/ids.py`'s staged_from map).
- (c) THE PACKET, `../deliverables/0.9.0_WK_IRPT_BCKEND~2/NEVER_WIDEN_SIGNOFF_PACKET_IB-rtg-2.md`, committed, `blob <hash>` printed: K-CODE x 1 (the status function rebuilt under a build ledger; prior live `CodeSha256` READ LIVE as the rollback source with its build-store version; built sha VERIFIED AT REST; served-byte delta exactly the edited/added members; import closure); WRITERS counted; BLAST RADIUS both branches (with the fix: a real status-summary returns a StatusEnvelope; without: UNSUPPORTED_OPERATION); ROLLBACK = re-publish the prior live `CodeSha256` via Terraform, never `update-function-code`; the identity line per arm. THEN read for BOTH halves at HEAD (`..._{COO,CTO}_HALF_..._IB-rtg-2_*.md`) naming this blob. ABSENT -> STOP HERE (arm (d) FAILS truthfully, order stays open, report). PRESENT -> continue.
- (d) APPLY under a change-management ledger OPENED BEFORE the apply (the W1-S41 exposure; sentinel committed before, closed before the grading reads): pre-apply re-verification (halves 2 of 2, this blob, built artifact latest at its sha), THEN the arm-(d) SUBTRACTION gate (the W1-S37 lesson, verbatim -- compare `resource_changes` PER ROOT and nothing else, minus the closed printed volatile set {plan `.timestamp`; a `data.aws_s3_object` read entry's `version_id`/`last_modified` within `resource_changes`}, print the two-part denominator, FAIL CLOSED); PASS iff the status/ops root shows EXACTLY the one function `update` and every other root EMPTY after subtraction. `.tools/safe-apply.sh`, `0 to destroy`, rc 0, post-apply 0-diff; `CodeSha256 == built`.
- (e) PROVEN LIVE, UNDER THE DEPLOYED ROLE AND BYTES (the identity bar): reuse `../deliverables/0.7.0_AE_CloudOps~V/battery_ib_rtf_10.py` at HEAD -- the bounded principal under this order's ledger (rtf-9 packet blob a1f36b95b2, both halves at HEAD, a new epoch, the full lifecycle). ACCEPTANCE: an exercised status-summary request for a job the intake/export/render path ACTUALLY RAN returns a validated `StatusEnvelope` (not `UNSUPPORTED_OPERATION`); route/function/role printed; the negative control (a status request for a non-existent job) refused with its declared code, not UNEXPECTED.

---

## DELIVERABLE
the `ops/` status_loader source + the `ops/entry.py` wiring; `NEVER_WIDEN_SIGNOFF_PACKET_IB-rtg-2.md`; the build ledger; `battery_ib_rtg_2.py`, `IB-rtg-2_R<n>-AC1_battery_output.txt`, `the-status-loader-reads-the-real-job-store.result.md`; the apply and live-principal ledgers; the proof instance.

---

## BOUNDS
- The ONLY code that deploys: `irpt-status` rebuilt with the loader + wiring edit; the served-byte delta exactly those edits or STOP; NO new DynamoDB table or external feed (read the backend's own `irpt-jobs`); no other function's bytes; NO APPLY before both halves at HEAD naming the packet blob; the ledger OPENED before the apply.
- **THE FORWARD-LOOKING-CRITERION BAR:** every claim about a run/served artifact is bound to its CONTENT HASH READ AT THE EVENT.
- **R-40:** content hash beside every run/artifact id, graded against the hash.
- **S56:** every line citation carries `path:line @ <commit-ish>`; a bare `:NNN` is a defect.
- **THE READER-CENSUS BAR:** if this edit flips a shared flag/field, census its N readers (N rules read, N printed) before calling the flip safe.
- **Surprises:** ONE row per failed premise/wrong path/absent capability -- at `../surprise-channel/investigations/INVESTIGATION_v1.md`, id `IRPT_BCKEND-W2-S<k>` continuing above the highest at your HEAD (append INSIDE the first fence's array, PREVAILING line endings, UTF-8 explicit, full ISO `surfaced_at`, `disarm_owner` a SEAT SERIAL when ARMED); then keep working. Never edit this face, widen the order, or fix a neighbouring defect.
- **BLOB PINS `blob <hash>`;** `@<hash>` is commit-ish. No `memory/` path. Every rule inline.

---

<expected_criteria>R73-AC1, R73-AC2</expected_criteria>
<criterion id="R73-AC1" cell_refs="IB-rtg-2"><invocation>timeout 1800 py -3.12 org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/battery_ib_rtg_2.py</invocation><expect>IBR73-STATUS-LOADER-SERVES-ENVELOPE</expect></criterion>

<placeholders>NONE</placeholders>

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rtg-2.the-status-loader-reads-the-real-job-store.md
infra/aws/lambda/investor-reporting/ops/
infra/aws/lambda/ci/lambda-source-map.json
infra/aws/terraform/investor-reporting/ops/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> v0.7, cell `IB-rtg-2` (s.R7.1 -- the round-7 recut on the round-6 analysis @fa2ff4f0dd).
<owned_cells>IB-rtg-2</owned_cells>
</decomp_ref>

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- nothing scheduled or fired.
comp-iam: DECLARED-NOT-APPLICABLE -- the fix is a source edit under the function's existing role; IF the status role lacks the `irpt-jobs` DynamoDB read the loader needs, that grant is a MEASURED key in this order's never-widen packet (arm (c)), never assumed at the cut.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; the assignee's instrument at report time.
lane: the `<paths>` block above IS the grant plus the two tree-convention grants (`deliverables/<serial>/`, this order's own face). A path you need that is not listed is a BLOCKING row, never an override.
</preflight>

<proof_of_spec>
Criterion ids minted at cut: R73-AC1 (an exercised status-summary for a real job returns a validated StatusEnvelope, not UNSUPPORTED_OPERATION), R73-AC2 (judgment, the CVO's at L9). Instance at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/IRPT_BCKEND.TO-IB-rtg-2.the-status-loader-reads-the-real-job-store.proof_of_spec.json` (the TASK ORDER'S OWN BASENAME stem), per `org/standards/PROOF_OF_SPEC.schema.json`: one acceptance row per id, `criterion_verbatim` the spec's words, `invocation` the exact command, `output_evidence` the verbatim deciding excerpt, `denominator` beside every count, `expect` carried from this face, R-40 the content hash of every produced/served artifact EACH PINNED TO THE COMMIT THAT CARRIED IT; the judgment row under `UNVERIFIABLE-BY-INSTRUMENT` naming the CVO. Validate with `py -3.12 .tools/proof-of-spec-check.py <instance> --governing-order <this face path>` BEFORE the complete flip; rc 0 AND R73-AC1 PASS-by-output, then flip `<status>` to `complete` and commit instance and flip together. A FAIL row leaves the order open.
</proof_of_spec>
