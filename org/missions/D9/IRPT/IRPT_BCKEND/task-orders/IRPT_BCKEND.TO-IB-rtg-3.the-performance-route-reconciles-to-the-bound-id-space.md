# TO IRPT_BCKEND.TO-IB-rtg-3 -- THE PERFORMANCE ROUTE RECONCILES TO THE BOUND ID SPACE: round 6's performance tab returned DEPENDENCY_UNAVAILABLE (FWD-2, row W2-S27). Cause: `performance/tenants.py:81,91,101` keys `ROUTES` on a THIRD firm-id spelling (`F-49F`/`F-COT`/`F-INF`) while `performance/handler.py:79-80` passes the OPAQUE verified id (`fir_...`) straight to `route_for`, and `performance/entry.py:113-118` maps the resulting `UnknownTenant` to `DEPENDENCY_UNAVAILABLE`. This order reconciles `route_for`'s lookup to the id space the boundary binds on, using the estate's EXISTING `_ids` normalizer -- NEVER a fourth firm-token mapping.

<to_id>IRPT_BCKEND.TO-IB-rtg-3</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~3</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-20</issued_date>
<status>pending -- HANDED by 2.0.0_SA_COO~B at 2026-09-20 (round 7, the recut on the round-6 analysis @fa2ff4f0dd). The performance data path is one of round 7's four backend cells; scope confirmed by investigation a7edd66ed0. Served-path handler deploy -> both never-widen halves at HEAD BEFORE any apply. BOUND: if the reconciliation cannot be done without minting a new lookup, STOP and ROW it for the issuer to route to the CTO (FirmBinding axis W2-S9) -- do NOT cut an ad hoc mapping.</status>

**Directive:** D9 | **Fabric:** laptop | **Round:** 7 (the CTO's round-6 analysis @fa2ff4f0dd) | **PRD:** `../prd/IRPT_BCKEND_PRD.md` v0.15 | **Round-6 analysis:** `../deliverables/1.0.0_SA_CTO/IRPT_BCKEND_ROUND6_ANALYSIS.md` @fa2ff4f0dd | **Decomp cell:** `IB-rtg-3` (`../decompositions/IRPT_BCKEND_DECOMP.md` v0.7 @a1c21f1424, s.R7.1) | **outcome_ref:** FWD-2

---

## IDENTITY AND WORKTREE

- **Serial:** `0.9.0_WK_IRPT_BCKEND~3`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_IRPT_BCKEND~3;`.
- **Worktree:** `/c/tmp/wk-irpt-7-3` on branch `wk-irpt_bckend-7-3`, cut from CLOUD HEAD at hand-off; `.tools/terraform.exe` provisioned. First act: `git rev-parse --abbrev-ref HEAD` and `test -d org && test -d .tools && echo TREE-OK`; then the session-serial line BEFORE any apply.
- **Repo root:** the worktree; prefix `/c/tmp/wk-irpt-7-3/`.
- **Commit:** `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~3 <0.9.0_WK_IRPT_BCKEND~3@opal.agent>" -F <msgfile> -- <paths>`, `<msgfile>` via Write tool. Branch only; never push/merge/rebase/`checkout --`/`clean`. Output to a file, never `| tail`, never with `$( )`.
- **Python:** `py -3.12`. AWS `.tools/aws`. `.tools/terraform.exe` by path. Recursive `grep`/`find` rail-DENIED; Read/Grep tools. `build-and-upload.sh` from `/c/`.

---

## THE CELL

- (a) MEASURE FIRST, printed: read `performance/tenants.py:81-101`, `performance/handler.py:79-80`, `performance/entry.py:113-118`, and the estate's ONE id-space normalizer `_ids/` at HEAD; confirm W2-S27 (`route_for` keys on `F-49F`/`F-COT`/`F-INF` while the boundary binds the opaque `fir_...` id) and identify the SINGLE id space the boundary binds on. Re-derive any grant/firm count LIVE and PRINT it, never inherit a round-6 number. The mutant: the pre-fix `route_for` still raising `UnknownTenant` on the opaque id.
- (b) THE SOURCE EDIT: reconcile `performance/tenants.py`'s `route_for` lookup to the SAME id space the boundary binds, USING the estate's existing `_ids` normalizer (a source change confined to `performance/tenants.py`, + `_ids/` only if it already exposes the mapping) -- NEVER inventing a fourth firm-token table. ⛔ IF the reconciliation CANNOT be done without minting a NEW lookup table: STOP, do NOT edit, and ROW it (that is FirmBinding's axis W2-S9, the issuer routes it to the CTO). Then, only if the edit is a clean reconciliation, `infra/aws/lambda/ci/build-and-upload.sh investor-reporting irpt-performance-adapter` (confirm the served name at `_ids/ids.py`).
- (c) THE PACKET, `../deliverables/0.9.0_WK_IRPT_BCKEND~3/NEVER_WIDEN_SIGNOFF_PACKET_IB-rtg-3.md`, committed, `blob <hash>` printed: K-CODE x 1 (the performance function rebuilt under a build ledger; prior live `CodeSha256` READ LIVE as rollback with its build-store version; built sha VERIFIED AT REST; served-byte delta exactly the edit; import closure); WRITERS counted; BLAST RADIUS both branches (with the fix: each registry firm resolves a TenantRoute; without: DEPENDENCY_UNAVAILABLE); ROLLBACK = re-publish the prior live `CodeSha256` via Terraform, never `update-function-code`; the identity line per arm. THEN read BOTH halves at HEAD (`..._{COO,CTO}_HALF_..._IB-rtg-3_*.md`) naming this blob. ABSENT -> STOP HERE (arm (d) FAILS truthfully, order stays open, report). PRESENT -> continue.
- (d) APPLY under a change-management ledger OPENED BEFORE the apply (the W1-S41 exposure; sentinel committed before, closed before the grading reads): pre-apply re-verification (halves 2 of 2, this blob, built artifact latest at its sha), THEN the arm-(d) SUBTRACTION gate (the W1-S37 lesson, verbatim -- `resource_changes` PER ROOT and nothing else, minus {plan `.timestamp`; a `data.aws_s3_object` read entry's `version_id`/`last_modified` within `resource_changes`}, print the two-part denominator, FAIL CLOSED); PASS iff the performance root shows EXACTLY the one function `update`, other roots EMPTY. `.tools/safe-apply.sh`, `0 to destroy`, rc 0, post-apply 0-diff; `CodeSha256 == built`.
- (e) PROVEN LIVE, UNDER THE DEPLOYED ROLE AND BYTES (the identity bar): reuse `../deliverables/0.7.0_AE_CloudOps~V/battery_ib_rtf_10.py` at HEAD -- the bounded principal under this order's ledger (rtf-9 packet blob a1f36b95b2, both halves at HEAD, a new epoch, full lifecycle). ACCEPTANCE: an authorized, scope-resolved performance request for EACH of the 3 registry firms resolves a `TenantRoute` (no `DEPENDENCY_UNAVAILABLE`), 0 fourth-id-space literals introduced (grep the deployed bytes); route/function/role printed.

---

## DELIVERABLE
the `performance/tenants.py` (+ `_ids/` if applicable) source edit; `NEVER_WIDEN_SIGNOFF_PACKET_IB-rtg-3.md`; the build ledger; `battery_ib_rtg_3.py`, `IB-rtg-3_R<n>-AC1_battery_output.txt`, `the-performance-route-reconciles.result.md`; the apply and live-principal ledgers; the proof instance. IF the STOP-and-ROW branch fires: the row + the result stating the FirmBinding-axis finding, no deploy.

---

## BOUNDS
- The ONLY code that deploys: `irpt-performance-adapter` rebuilt with the reconciliation; the served-byte delta exactly that or STOP; ⛔ NEVER a fourth firm-token mapping (STOP + ROW for the CTO if the fix needs one); no other function's bytes; NO APPLY before both halves at HEAD naming the packet blob; the ledger OPENED before the apply.
- **THE FORWARD-LOOKING-CRITERION BAR:** every claim about a run/served artifact bound to its CONTENT HASH READ AT THE EVENT.
- **R-40:** content hash beside every run/artifact id, graded against the hash.
- **S56:** every line citation `path:line @ <commit-ish>`; a bare `:NNN` is a defect.
- **THE READER-CENSUS BAR:** census the N readers of any shared flag/field this flips before calling it safe.
- **Surprises:** ONE row per failed premise/wrong path/absent capability -- at `../surprise-channel/investigations/INVESTIGATION_v1.md`, id `IRPT_BCKEND-W3-S<k>` continuing above the highest at your HEAD (append INSIDE the first fence's array, PREVAILING line endings, UTF-8 explicit, full ISO `surfaced_at`, `disarm_owner` a SEAT SERIAL when ARMED); then keep working. The new-mapping STOP is itself a Surprise row. Never edit this face, widen the order, or fix a neighbouring defect.
- **BLOB PINS `blob <hash>`;** `@<hash>` is commit-ish. No `memory/` path. Every rule inline.

---

<expected_criteria>R74-AC1, R74-AC2</expected_criteria>
<criterion id="R74-AC1" cell_refs="IB-rtg-3"><invocation>timeout 1800 py -3.12 org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~3/battery_ib_rtg_3.py</invocation><expect>IBR74-PERFORMANCE-ROUTE-RESOLVES-EACH-FIRM</expect></criterion>

<placeholders>NONE</placeholders>

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rtg-3.the-performance-route-reconciles-to-the-bound-id-space.md
infra/aws/lambda/investor-reporting/performance/
infra/aws/lambda/investor-reporting/_ids/
infra/aws/lambda/ci/lambda-source-map.json
infra/aws/terraform/investor-reporting/performance/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> v0.7, cell `IB-rtg-3` (s.R7.1 -- the round-7 recut on the round-6 analysis @fa2ff4f0dd).
<owned_cells>IB-rtg-3</owned_cells>
</decomp_ref>

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- nothing scheduled or fired.
comp-iam: DECLARED-NOT-APPLICABLE -- a source reconciliation under the function's existing role; no grant change (if the fix needs a new firm-token mapping the order STOPs and ROWs for the CTO, and no deploy runs).
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; the assignee's instrument at report time.
lane: the `<paths>` block above IS the grant plus the two tree-convention grants (`deliverables/<serial>/`, this order's own face). A path you need that is not listed is a BLOCKING row, never an override. `_ids/` is granted READ + a reconciliation edit ONLY if `_ids` already exposes the mapping; a NEW mapping is the STOP-and-ROW branch, not an `_ids` edit.
</preflight>

<proof_of_spec>
Criterion ids minted at cut: R74-AC1 (an authorized, scope-resolved performance request for each of the 3 registry firms resolves a TenantRoute, no DEPENDENCY_UNAVAILABLE, 0 fourth-id-space literals), R74-AC2 (judgment, the CVO's at L9). Instance at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~3/IRPT_BCKEND.TO-IB-rtg-3.the-performance-route-reconciles-to-the-bound-id-space.proof_of_spec.json` (the TASK ORDER'S OWN BASENAME stem), per `org/standards/PROOF_OF_SPEC.schema.json`: one acceptance row per id, `criterion_verbatim`, `invocation`, `output_evidence`, `denominator` beside every count, `expect` carried from this face, R-40 the content hash of every produced/served artifact EACH PINNED TO THE COMMIT THAT CARRIED IT; the judgment row under `UNVERIFIABLE-BY-INSTRUMENT` naming the CVO. IF the STOP-and-ROW (new-mapping) branch fires, R74-AC1 is FAIL by the row and the order stays open. Validate with `py -3.12 .tools/proof-of-spec-check.py <instance> --governing-order <this face path>` BEFORE any flip; rc 0 AND R74-AC1 PASS-by-output, then flip `<status>` to `complete`. A FAIL row leaves the order open.
</proof_of_spec>
