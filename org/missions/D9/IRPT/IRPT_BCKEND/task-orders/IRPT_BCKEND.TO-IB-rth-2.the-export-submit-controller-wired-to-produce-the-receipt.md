# TO IRPT_BCKEND.TO-IB-rth-2 -- THE EXPORT SUBMIT CONTROLLER WIRED TO PRODUCE THE RECEIPT: round 7 (rtg-1, R72-AC1 PASS 8/8) proved the export receipt CONTRACT -- key alignment (S105) and taxonomy-by-CODE (S106) -- on the served path, with the receipt WRITE standing in for the deployed submit path. Row W1-S43 disclosed the gap: the deployed `submit_export` raises `NOT_READY` unconditionally, so no production submit produces a receipt. This cell wires it.

<to_id>IRPT_BCKEND.TO-IB-rth-2</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~2</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-21</issued_date>
<status>pending -- HANDED by 2.0.0_SA_COO~B 2026-09-21 (round 8, recut on the CTO's round-7 analysis @0d400d5c07). Served-path handler change -> packet + both never-widen halves at HEAD BEFORE any apply (arm (c) STOP is the expected first pass, the rtg-1 shape).</status>

**Directive:** D9 | **Fabric:** laptop | **Round:** 8 | **PRD:** `../prd/IRPT_BCKEND_PRD.md` (no round-8 addendum) | **Round-7 analysis:** `../deliverables/1.0.0_SA_CTO/IRPT_BCKEND_ROUND7_ANALYSIS.md` @0d400d5c07 | **Decomp cell:** `IB-rth-2` (`../decompositions/IRPT_BCKEND_DECOMP.md` v0.8, s.R8.1) | **outcome_ref:** FWD-2 (serving half) | **row:** W1-S43 | **supersedes:** the submit half IB-rtg-1 disclosed

---

## IDENTITY AND WORKTREE
- **Serial:** `0.9.0_WK_IRPT_BCKEND~2`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_IRPT_BCKEND~2;`.
- **Worktree:** the issuer creates `/c/tmp/wk-irpt-8-2` on `wk-irpt_bckend-8-2` from CLOUD HEAD, `.tools/terraform.exe` provisioned; absolute path at spawn. First act: `cd`, `git rev-parse --abbrev-ref HEAD`, `test -d org && test -d .tools && echo TREE-OK`; write the `.serial` file before any apply. Repo root = the worktree.
- **Commit:** `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~2 <0.9.0_WK_IRPT_BCKEND~2@opal.agent>" -F <msgfile> -- <paths>`, `<msgfile>` by the Write tool. Branch only. Capture output to a file; never `| tail`; never `$( )`. Verify by `git log`.
- Python `py -3.12`; AWS via `.tools/aws`; APPLY via `.tools/safe-apply.sh` (never bare terraform apply, never `aws lambda update-function-code`); recursive grep/find rail-DENIED.

## THE CELL
- **(a) MEASURE FIRST, printed with denominators:** read `export/entry.py`/`export/handler.py` at HEAD; confirm the deployed `submit_export` path raises `NOT_READY` (the W1-S43 evidence) and WHY (the controller not wired to the entry, or a feature flag); identify the MINIMAL wiring that makes a real submit produce a receipt at the aligned address rtg-1 proved (`firms/{firm}/generations/.../exports/{rev}/receipt.json`). Re-derive any grant/ownership count LIVE, never inherit.
- **(b) THE SOURCE EDIT:** wire `submit_export` to the real controller so an authorized submit produces the receipt via the same `handler.persist_receipt()`/`receipt.build()` rtg-1 proved -- do NOT change the S105 key template or the S106 taxonomy (rtg-1's contract stands; a diff there is a STOP). Then `infra/aws/lambda/ci/build-and-upload.sh investor-reporting irpt-export-render` (confirm the served function name).
- **(c) THE PACKET** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/NEVER_WIDEN_SIGNOFF_PACKET_IB-rth-2.md`, committed, `blob <hash>` printed: K-CODE x 1 (irpt-export-render rebuilt from HEAD under a build ledger; the prior live `CodeSha256` READ LIVE via `get-function-configuration` -- never this face -- kept with its build-store object version as the rollback source; built sha VERIFIED AT REST == bytes == built; served-byte delta EXACTLY the edited members; import closure); WRITERS of the served property counted; BLAST RADIUS both branches; ROLLBACK = re-publish the prior live `CodeSha256` from its build-store version via Terraform, never `update-function-code`; the identity line. THEN read for BOTH halves at HEAD naming this blob. ABSENT -> STOP HERE (arm (d) FAILS truthfully in a VALID instance, the order stays open, report). PRESENT -> continue.
- **(d) APPLY under a change-management ledger OPENED BEFORE the apply:** pre-apply re-verify (halves 2 of 2, this blob, the built artifact latest at its sha); the arm-(d) SUBTRACTION gate (fresh plan per root; compare `resource_changes` per root minus {a `data.aws_s3_object` `version_id`/`last_modified`}; print the two-part denominator; FAIL CLOSED on anything else) -- export root EXACTLY the one function update (before/after `source_code_hash`), every other root EMPTY after subtraction; `.tools/safe-apply.sh` the export root, `0 to destroy`, rc 0, post-apply 0-diff; `CodeSha256 == built`; CLOSE the ledger. Rollback if half-landed: re-publish the prior sha via Terraform; verify; escalate loud.
- **(e) PROVEN LIVE, UNDER THE DEPLOYED ROLE + BYTES:** reuse `../deliverables/0.7.0_AE_CloudOps~V/battery_ib_rtf_10.py` (bounded principal, fresh epoch, full lifecycle). ACCEPTANCE R77-AC1: an exercised submit-export -> receipt round trip on the REAL path PRODUCES + SERVES the receipt (no `NOT_READY`, no `NOT_FOUND`), the read key EQUALS a key the wired writer produces; AND rtg-1's S105 alignment + S106 taxonomy-by-CODE (real 403/404) STILL hold (no regression). Route/function/role printed; 0 `NOT_READY` for a valid submit on the exercised firm.

## DELIVERABLE
the `export/` source edit; `NEVER_WIDEN_SIGNOFF_PACKET_IB-rth-2.md`; the build ledger; `battery_ib_rth_2.py`, its output, the result.md; the apply + live-principal ledgers; the proof instance.

## BOUNDS
- The ONLY code that deploys: `irpt-export-render` rebuilt with the submit-wiring edit; the served-byte delta EXACTLY that edit or STOP; NO change to the S105 key template or S106 taxonomy (rtg-1's contract); no other function's bytes; no IAM change unless the wired write needs a grant it lacks (then a MEASURED key in this packet, never assumed); NO APPLY before both halves at HEAD name the blob; the ledger OPENED before the apply.
- The forward-looking-criterion bar; R-40; S56 vintage pins; the identity bar.
- **Surprises:** one row per failed premise / wrong path / absent capability at `../surprise-channel/investigations/INVESTIGATION_v1.md`, id `IRPT_BCKEND-W2-S<k>` continuing above the highest at your HEAD (append INSIDE the first fence's array, PREVAILING EOL, UTF-8 explicit, full ISO `surfaced_at`, `disarm_owner` a SEAT SERIAL when ARMED); then keep working. Never edit this face except the `<status>` flip; never widen; never fix a neighbour.

<expected_criteria>R77-AC1, R77-AC2</expected_criteria>
<criterion id="R77-AC1" cell_refs="IB-rth-2"><invocation>timeout 1800 py -3.12 org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/battery_ib_rth_2.py</invocation><expect>IBR77-EXPORT-SUBMIT-PRODUCES-AND-SERVES-THE-RECEIPT</expect></criterion>

<placeholders>NONE</placeholders>

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rth-2.the-export-submit-controller-wired-to-produce-the-receipt.md
infra/aws/lambda/investor-reporting/export/
infra/aws/lambda/ci/lambda-source-map.json
infra/aws/terraform/investor-reporting/export/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> v0.8, cell `IB-rth-2` (s.R8.1).
<owned_cells>IB-rth-2</owned_cells>
</decomp_ref>

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- nothing scheduled or fired.
comp-iam: DECLARED-NOT-APPLICABLE -- a source edit under the function's existing role; IF the wired write needs a grant the role lacks, that grant is a MEASURED key in this order's never-widen packet (arm c), never assumed at the cut.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; the assignee's instrument at report time.
lane: the `<paths>` block above IS the grant plus the two tree-convention grants. A path you need that is not listed is a BLOCKING row, never an override.
</preflight>

<proof_of_spec>
Criterion ids minted at cut: R77-AC1 (a real submit produces + serves the receipt, no NOT_READY, rtg-1's contract unregressed), R77-AC2 (judgment, the CVO's at L9). Instance at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/IRPT_BCKEND.TO-IB-rth-2.the-export-submit-controller-wired-to-produce-the-receipt.proof_of_spec.json` per `org/standards/PROOF_OF_SPEC.schema.json`: one acceptance row per id, `criterion_verbatim`, `invocation`, `output_evidence`, `denominator` beside every count, `expect` from this face, R-40 content hash per produced/served artifact pinned to its commit; the judgment row under `UNVERIFIABLE-BY-INSTRUMENT` naming `3.0.0_SA_CVO`. Validate `py -3.12 .tools/proof-of-spec-check.py <instance> --governing-order <this face path>`; rc 0 AND R77-AC1 PASS-by-output, then flip `<status>` complete. A FAIL row leaves it open.
</proof_of_spec>
