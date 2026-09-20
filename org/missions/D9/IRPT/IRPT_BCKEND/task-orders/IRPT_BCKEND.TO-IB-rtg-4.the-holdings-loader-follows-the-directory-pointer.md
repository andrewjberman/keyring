# TO IRPT_BCKEND.TO-IB-rtg-4 -- THE HOLDINGS LOADER FOLLOWS THE DIRECTORY POINTER: round 6 confirmed S100 on the PERMITTED path (FWD-5) -- holdings refused FIRM_BINDING for an account the principal's own resolve had just granted. Cause: `holdings/entry.py:88-89` `_load_directory` calls `directory/handler.py`'s single-key `load_directory` (one `get_object` on the literal `latest.json`, returned verbatim), so holdings reads the POINTER document (`{"key": "..."}`) as if it were the directory artifact and finds no `firm_id_opaque` -> `FirmBinding` raises. The correct two-step pattern already exists in `_authz/loaders.py:71-78` (fetch `latest.json` pointer, then fetch `pointer["key"]`). This order makes holdings follow the pointer.

<to_id>IRPT_BCKEND.TO-IB-rtg-4</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~4</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-20</issued_date>
<status>pending -- HANDED by 2.0.0_SA_COO~B at 2026-09-20 (round 7, the recut on the round-6 analysis @fa2ff4f0dd). The holdings entitlement defect S100 is one of round 7's four backend cells (S100's disarm_owner is already this seat); scope confirmed by investigation a7edd66ed0. Served-path handler deploy -> both never-widen halves at HEAD BEFORE any apply.</status>

**Directive:** D9 | **Fabric:** laptop | **Round:** 7 (the CTO's round-6 analysis @fa2ff4f0dd) | **PRD:** `../prd/IRPT_BCKEND_PRD.md` v0.15 | **Round-6 analysis:** `../deliverables/1.0.0_SA_CTO/IRPT_BCKEND_ROUND6_ANALYSIS.md` @fa2ff4f0dd | **Decomp cell:** `IB-rtg-4` (`../decompositions/IRPT_BCKEND_DECOMP.md` v0.7 @a1c21f1424, s.R7.1) | **outcome_ref:** FWD-5

---

## IDENTITY AND WORKTREE

- **Serial:** `0.9.0_WK_IRPT_BCKEND~4`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_IRPT_BCKEND~4;`.
- **Worktree:** `/c/tmp/wk-irpt-7-4` on branch `wk-irpt_bckend-7-4`, cut from CLOUD HEAD at hand-off; `.tools/terraform.exe` provisioned. First act: `git rev-parse --abbrev-ref HEAD` and `test -d org && test -d .tools && echo TREE-OK`; then the session-serial line BEFORE any apply.
- **Repo root:** the worktree; prefix `/c/tmp/wk-irpt-7-4/`.
- **Commit:** `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~4 <0.9.0_WK_IRPT_BCKEND~4@opal.agent>" -F <msgfile> -- <paths>`, `<msgfile>` via Write tool. Branch only; never push/merge/rebase/`checkout --`/`clean`. Output to a file, never `| tail`, never with `$( )`.
- **Python:** `py -3.12`. AWS `.tools/aws`. `.tools/terraform.exe` by path. Recursive `grep`/`find` rail-DENIED; Read/Grep tools. `build-and-upload.sh` from `/c/`.

---

## THE CELL

- (a) MEASURE FIRST, printed: read `holdings/entry.py:70-112`, `directory/handler.py:78-89`, and the correct pattern `_authz/loaders.py:71-78` at HEAD; confirm S100 (holdings' `_load_directory` at `:88-89` calls the single-key `load_directory` and reads the pointer doc as the artifact, so `opaque_firm_for` at `:109-112` finds no `firm_id_opaque` and `FirmBinding` raises for an account resolve granted). Re-derive the ownership/grant count LIVE against the live map and PRINT it (the 44/19 re-derive constraint -- read `platinum/{firm}/ownership_map.json` live, never inherit 33/18). The mutant: the pre-fix single-key read still raising `FirmBinding` for the granted account.
- (b) THE SOURCE EDIT: make `holdings/entry.py`'s `_load_directory` FOLLOW the `latest.json` pointer the way `_authz/loaders.py:71-78` does (fetch `latest.json`, then fetch `pointer["key"]`) -- either call the shared `_authz` loader or replicate its two-step fetch; do NOT keep `directory/handler.py`'s single-key `load_directory` on this path. Confined to `holdings/entry.py` (+ a shared-loader import if reused). Then `infra/aws/lambda/ci/build-and-upload.sh investor-reporting irpt-holdings` (confirm the served name at `_ids/ids.py`).
- (c) THE PACKET, `../deliverables/0.9.0_WK_IRPT_BCKEND~4/NEVER_WIDEN_SIGNOFF_PACKET_IB-rtg-4.md`, committed, `blob <hash>` printed: K-CODE x 1 (holdings rebuilt under a build ledger; prior live `CodeSha256` READ LIVE as rollback with its build-store version; built sha VERIFIED AT REST; served-byte delta exactly the edit; import closure); WRITERS counted; BLAST RADIUS both branches (with the fix: a granted account reads a scope-resolved answer or a real policy refusal WITH firm_id; without: FIRM_BINDING with firm_id absent); ROLLBACK = re-publish the prior live `CodeSha256` via Terraform, never `update-function-code`; the identity line per arm. THEN read BOTH halves at HEAD (`..._{COO,CTO}_HALF_..._IB-rtg-4_*.md`) naming this blob. ABSENT -> STOP HERE (arm (d) FAILS truthfully, order stays open, report). PRESENT -> continue.
- (d) APPLY under a change-management ledger OPENED BEFORE the apply (the W1-S41 exposure; sentinel committed before, closed before the grading reads): pre-apply re-verification (halves 2 of 2, this blob, built artifact latest at its sha), THEN the arm-(d) SUBTRACTION gate (the W1-S37 lesson, verbatim -- `resource_changes` PER ROOT and nothing else, minus {plan `.timestamp`; a `data.aws_s3_object` read entry's `version_id`/`last_modified` within `resource_changes`}, print the two-part denominator, FAIL CLOSED); PASS iff the holdings root shows EXACTLY the one function `update`, other roots EMPTY. `.tools/safe-apply.sh`, `0 to destroy`, rc 0, post-apply 0-diff; `CodeSha256 == built`.
- (e) PROVEN LIVE, UNDER THE DEPLOYED ROLE AND BYTES (the identity bar): reuse `../deliverables/0.7.0_AE_CloudOps~V/battery_ib_rtf_10.py` at HEAD -- the bounded principal under this order's ledger (rtf-9 packet blob a1f36b95b2, both halves at HEAD, a new epoch, full lifecycle). ACCEPTANCE: an exercised holdings request for an account the principal's own `resolve` just GRANTED reads a scope-resolved answer (served, or a real policy refusal WITH `firm_id` present), NEVER `FIRM_BINDING` with `firm_id` absent; route/function/role printed; the negative control (a foreign firm's account) still refused with `firm_id` present. NOTE (round-6 carry S110): a holdings NEGATIVE control asserting a refusal is VACUOUS while S100 is armed -- once this cell moves S100 the refusal-side evidence is no longer vacuous; state the discriminator (a terminated/forbidden account refused with a DIFFERENT code than the granted account gets, not the same FIRM_BINDING).

---

## DELIVERABLE
the `holdings/entry.py` source edit; `NEVER_WIDEN_SIGNOFF_PACKET_IB-rtg-4.md`; the build ledger; `battery_ib_rtg_4.py`, `IB-rtg-4_R<n>-AC1_battery_output.txt`, `the-holdings-loader-follows-the-pointer.result.md`; the apply and live-principal ledgers; the proof instance.

---

## BOUNDS
- The ONLY code that deploys: `irpt-holdings` rebuilt with the pointer-follow edit; the served-byte delta exactly that or STOP; no other function's bytes; NO APPLY before both halves at HEAD naming the packet blob; the ledger OPENED before the apply.
- **THE 44/19 RE-DERIVE CONSTRAINT:** read the ownership map LIVE and print the count; never inherit round-6's 33/18. The producer (`data/assets/scripts/gold/runners_49f/d08_firm_ownership_map.py`) is DS and NOT touched here -- backend only reads its output.
- **THE FORWARD-LOOKING-CRITERION BAR:** every claim about a run/served artifact bound to its CONTENT HASH READ AT THE EVENT.
- **R-40:** content hash beside every run/artifact id, graded against the hash.
- **S56:** every line citation `path:line @ <commit-ish>`; a bare `:NNN` is a defect.
- **Surprises:** ONE row per failed premise/wrong path/absent capability -- at `../surprise-channel/investigations/INVESTIGATION_v1.md`, id `IRPT_BCKEND-W4-S<k>` continuing above the highest at your HEAD (append INSIDE the first fence's array, PREVAILING line endings, UTF-8 explicit, full ISO `surfaced_at`, `disarm_owner` a SEAT SERIAL when ARMED); then keep working. Never edit this face, widen the order, or fix a neighbouring defect.
- **BLOB PINS `blob <hash>`;** `@<hash>` is commit-ish. No `memory/` path. Every rule inline.

---

<expected_criteria>R75-AC1, R75-AC2</expected_criteria>
<criterion id="R75-AC1" cell_refs="IB-rtg-4"><invocation>timeout 1800 py -3.12 org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~4/battery_ib_rtg_4.py</invocation><expect>IBR75-HOLDINGS-FOLLOWS-POINTER-AND-SERVES</expect></criterion>

<placeholders>NONE</placeholders>

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rtg-4.the-holdings-loader-follows-the-directory-pointer.md
infra/aws/lambda/investor-reporting/holdings/
infra/aws/lambda/ci/lambda-source-map.json
infra/aws/terraform/investor-reporting/holdings/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> v0.7, cell `IB-rtg-4` (s.R7.1 -- the round-7 recut on the round-6 analysis @fa2ff4f0dd).
<owned_cells>IB-rtg-4</owned_cells>
</decomp_ref>

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- nothing scheduled or fired.
comp-iam: DECLARED-NOT-APPLICABLE -- a source edit under the function's existing role; IF following the `latest.json` pointer reads an S3 prefix the holdings role lacks GetObject on, that grant is a MEASURED key in this order's never-widen packet (arm (c)), never assumed at the cut.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; the assignee's instrument at report time.
lane: the `<paths>` block above IS the grant plus the two tree-convention grants (`deliverables/<serial>/`, this order's own face). A path you need that is not listed is a BLOCKING row, never an override.
</preflight>

<proof_of_spec>
Criterion ids minted at cut: R75-AC1 (an exercised holdings request for an account the principal's own resolve granted reads a scope-resolved answer, never FIRM_BINDING with firm_id absent), R75-AC2 (judgment, the CVO's at L9). Instance at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~4/IRPT_BCKEND.TO-IB-rtg-4.the-holdings-loader-follows-the-directory-pointer.proof_of_spec.json` (the TASK ORDER'S OWN BASENAME stem), per `org/standards/PROOF_OF_SPEC.schema.json`: one acceptance row per id, `criterion_verbatim`, `invocation`, `output_evidence`, `denominator` beside every count, `expect` carried from this face, R-40 the content hash of every produced/served artifact EACH PINNED TO THE COMMIT THAT CARRIED IT; the judgment row under `UNVERIFIABLE-BY-INSTRUMENT` naming the CVO. Validate with `py -3.12 .tools/proof-of-spec-check.py <instance> --governing-order <this face path>` BEFORE the complete flip; rc 0 AND R75-AC1 PASS-by-output, then flip `<status>` to `complete` and commit instance and flip together. A FAIL row leaves the order open.
</proof_of_spec>
