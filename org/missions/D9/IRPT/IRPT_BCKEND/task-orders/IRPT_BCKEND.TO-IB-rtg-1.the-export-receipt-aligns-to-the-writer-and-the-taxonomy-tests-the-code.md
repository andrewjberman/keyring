# TO IRPT_BCKEND.TO-IB-rtg-1 -- THE EXPORT RECEIPT ALIGNS TO THE WRITER AND THE TAXONOMY TESTS THE CODE: round 6 left the export route as the last data-plane split (FWD-2). Row S105 -- the reader's receipt key `export/entry.py:63-64` `RECEIPT_KEY_TEMPLATE = investor-reporting/export/{firm}/{export_id}/receipt.json` matches 0 of the role's GetObject ARNs and NO writer produces it. Row S106 -- `export/entry.py:104-105` maps refusal by exception CLASS NAME against `("NoSuchKey","ClientError")`, so botocore's modeled `AccessDenied` (403) is neither and a real IAM denial reads UNEXPECTED. This order aligns the reader key to the family a writer actually produces AND writes the receipt beside the bundle AND rewrites the taxonomy to decide off the error CODE -- ONE cell per the CTO ruling (splitting yields a vacuous acceptance), S106 landing first-or-with S105, never after.

<to_id>IRPT_BCKEND.TO-IB-rtg-1</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~1</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-20</issued_date>
<status>pending -- HANDED by 2.0.0_SA_COO~B at 2026-09-20 (round 7, the recut on the round-6 analysis @fa2ff4f0dd). The export data path is one of round 7's four backend cells; scope confirmed by investigation a7edd66ed0. Served-path handler deploy -> both never-widen halves at HEAD BEFORE any apply (arm (c) STOP is the expected first pass).</status>

**Directive:** D9 | **Fabric:** laptop | **Round:** 7 (the CTO's round-6 analysis @fa2ff4f0dd) | **PRD:** `../prd/IRPT_BCKEND_PRD.md` v0.15 | **Round-6 analysis:** `../deliverables/1.0.0_SA_CTO/IRPT_BCKEND_ROUND6_ANALYSIS.md` @fa2ff4f0dd | **CTO S105/S106 ruling:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_IRPT_BCKEND_S105_S106_EXPORT_RECEIPT_CONTRACT_20260919.md` @0110b9de01 | **Decomp cell:** `IB-rtg-1` (`../decompositions/IRPT_BCKEND_DECOMP.md` v0.7 @a1c21f1424, s.R7.1) | **outcome_ref:** FWD-2

---

## IDENTITY AND WORKTREE

- **Serial:** `0.9.0_WK_IRPT_BCKEND~1`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_IRPT_BCKEND~1;`.
- **Worktree:** `/c/tmp/wk-irpt-7-1` on branch `wk-irpt_bckend-7-1`, cut by the issuer from CLOUD HEAD at hand-off; `.tools/terraform.exe` provisioned there. First act: `git rev-parse --abbrev-ref HEAD` and `test -d org && test -d .tools && echo TREE-OK`; then write the gitignored `org/mcp/sessions/<CLAUDE_CODE_SESSION_ID>.serial` BEFORE any apply.
- **Repo root for every path below:** the worktree; make a path absolute by prefixing `/c/tmp/wk-irpt-7-1/`.
- **Commit:** `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~1 <0.9.0_WK_IRPT_BCKEND~1@opal.agent>" -F <msgfile> -- <paths>`, `<msgfile>` written with the Write tool. On your branch only; never push, merge, rebase, `checkout --` or `clean`. Capture safe-commit output to a file, never `| tail`, never with `$( )`.
- **Python:** `py -3.12`. AWS through `.tools/aws` / `.tools/aws.cmd`. `.tools/terraform.exe` by that path, never a PATH substitute. A recursive `grep`/`find` in Bash is DENIED by a rail hook; use the Read/Grep tools, keep a gated read in its own call. `build-and-upload.sh` runs from a `/c/` cwd.

---

## THE CELL

- (a) MEASURE FIRST, printed with denominators: read `export/entry.py:63-104` and `export/handler.py` at HEAD; confirm S105 (the reader's `RECEIPT_KEY_TEMPLATE` at `:63-64`, formatted at `:100`) resolves to a key NO writer under `export/handler.py` produces (the submit path writes `bundle.json` under `firms/{firm}/generations/.../exports/{rev}/` at `:126-130`, no `receipt.json` sibling) and S106 (the `except` at `:104-105` matching CLASS NAMES `("NoSuchKey","ClientError")`, so `botocore.errorfactory.AccessDenied` is neither). Where any count is grant/ownership derived, RE-DERIVE it LIVE and PRINT it -- never inherit a round-6 number (the 44/19 re-derive constraint, s.R7.3). No mutant is named by the face for this criterion; the battery's own before/after on the wire is the discriminator.
- (b) THE SOURCE EDIT (S106 first-or-with S105, per the CTO ruling; do NOT split): (i) S106 -- rewrite `export/entry.py:104-105`'s `except` to decide refusal off `exc.response["Error"]["Code"]` (or `isinstance(exc, botocore.exceptions.ClientError)`) PLUS the HTTP status, letting genuinely unexpected classes propagate; (ii) S105 -- align `RECEIPT_KEY_TEMPLATE` (`export/entry.py:63-64`) to the `firms/{firm}/generations/.../exports/{rev}/` family the writer produces, AND add a receipt write BESIDE the bundle write in `export/handler.py:126-130`'s submit path. NO Terraform `IRPT_EXPORT_RECEIPT_KEY` override (the ruling REFUSES it -- a config that masks a wrong source default). Then `infra/aws/lambda/ci/build-and-upload.sh investor-reporting irpt-export-render` (confirm the served function name at `_ids/ids.py`'s staged_from map).
- (c) THE PACKET, `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/NEVER_WIDEN_SIGNOFF_PACKET_IB-rtg-1.md`, committed, `blob <hash>` printed: K-CODE x 1 (the export function rebuilt from HEAD under a build ledger; the prior live `CodeSha256` READ LIVE via `get-function-configuration` -- never from this face -- kept with its build-store object version as the rollback source; built sha printed and VERIFIED AT REST -- metadata == bytes == built; the served-byte delta EXACTLY the edited members; import closure); WRITERS of the served property counted; BLAST RADIUS both branches (with the fix: a 403/AccessDenied serves a policy code and a real receipt read returns the just-written receipt; without it: the current UNEXPECTED / NOT_FOUND); ROLLBACK = re-publish the prior live `CodeSha256` from its build-store version via Terraform, never `update-function-code`; the identity line per arm (arm (e) runs the DEPLOYED BYTES as the function's own role). THEN read for BOTH halves at HEAD (`NEVER_WIDEN_SIGNOFF_{COO,CTO}_HALF_IRPT_BCKEND_IB-rtg-1_*.md`) naming this blob. ABSENT -> STOP HERE: arm (d) FAILS truthfully in a VALID instance, the order stays open, report. PRESENT -> continue.
- (d) APPLY under a change-management ledger OPENED BEFORE the apply (the round-6 W1-S41 exposure -- no apply cycle without a pre-opened ledger; sentinel committed before, closed and committed before the grading reads): the pre-apply re-verification (halves 2 of 2, this blob, the built artifact the latest at its sha), THEN the arm-(d) SUBTRACTION gate (the W1-S37 lesson, verbatim): generate a fresh plan per root, and for each compare the `resource_changes` array of `terraform show -json` PER ROOT AND NOTHING ELSE (never the whole document -- `timestamp`/`prior_state`/`relevant_attributes` are siblings), WITHIN `resource_changes` subtract only {a `data.aws_s3_object` read entry's `version_id`/`last_modified`}, PRINT the two-part denominator (entries compared; paths subtracted, an observed count), FAIL CLOSED on any field outside the subtraction set; PASS iff the export root shows EXACTLY the one function `update` (before/after `source_code_hash`) and every other root EMPTY after subtraction. `.tools/safe-apply.sh` the export root, `0 to destroy`, rc 0, post-apply 0-diff; then `CodeSha256 == built`, `get-function-configuration` read back.
- (e) PROVEN LIVE on the export route, UNDER THE DEPLOYED ROLE AND BYTES (the identity bar): reuse `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~V/battery_ib_rtf_10.py` at HEAD -- the bounded principal under this order's ledger (rtf-9 packet blob a1f36b95b2, both halves at HEAD, a new epoch, the full lifecycle incl. the delete verified). ACCEPTANCE: an exercised submit-export -> export-receipt round trip on the REAL path returns the just-written receipt (no `NOT_FOUND`) and the read key EQUALS a key a writer produced; AND the taxonomy is exercised on a REAL WIRE ERROR (an unsigned GetObject 403/`AccessDenied` -> a policy code, NOT UNEXPECTED; the operator's 404/`NoSuchKey` -> `NOT_FOUND`) -- NEVER a constructed `ClientError` stub (the ruling §3 names this trap: a stub tests the author's model of botocore, not botocore). Route/function/role printed; 0 UNEXPECTED for this cause on the exercised firm.

---

## DELIVERABLE
the `export/entry.py` + `export/handler.py` source edits; `NEVER_WIDEN_SIGNOFF_PACKET_IB-rtg-1.md`; the build ledger; `battery_ib_rtg_1.py`, `IB-rtg-1_R<n>-AC1_battery_output.txt`, `the-export-receipt-aligns-to-the-writer.result.md`; the apply and live-principal ledgers; the proof instance.

---

## BOUNDS
- The ONLY code that deploys: `irpt-export-render` rebuilt with the two source edits; the served-byte delta is exactly those edits or STOP; NO Terraform `IRPT_EXPORT_RECEIPT_KEY` override (ruling §2, REFUSED); no other function's bytes; no IAM change unless the aligned receipt address needs a GetObject grant -- if so, that grant is its OWN never-widen key in this packet, measured, not assumed; NO APPLY before both halves at HEAD naming the packet blob; the ledger OPENED before the apply.
- **S106 lands FIRST OR WITH S105, NEVER AFTER** (CTO ruling §1): taking the address first converts a loudly-wrong answer into a correctly-shaped NOT_FOUND on one branch while leaving the denial branch lying.
- **THE FORWARD-LOOKING-CRITERION BAR:** no criterion certifies what a future event WILL find; every claim about a run/served artifact is bound to its CONTENT HASH READ AT THE EVENT.
- **R-40:** every criterion whose subject is a RUN or PRODUCED ARTIFACT records that artifact's content hash beside its run id and is graded against the hash.
- **S56:** every line citation carries a vintage `path:line @ <commit-ish>`; a bare `:NNN` is a defect the issuer greps for at the drain.
- **Surprises:** ONE row per premise that fails, path that is wrong, result the invocation does not produce, or capability you lack -- at `../surprise-channel/investigations/INVESTIGATION_v1.md`, id `IRPT_BCKEND-W1-S<k>` continuing above the file's highest at your HEAD (append INSIDE the first fence's array, the file's PREVAILING line endings, UTF-8 explicit, full ISO `surfaced_at`, `disarm_owner` a SEAT SERIAL when ARMED, omit it when INERT); then keep working. Never edit this face, never widen the order, never fix a neighbouring defect.
- **BLOB PINS are written `blob <hash>`;** `@<hash>` is commit-ish. No `memory/` path cited. Every rule relied on is inline.

---

<expected_criteria>R72-AC1, R72-AC2</expected_criteria>
<criterion id="R72-AC1" cell_refs="IB-rtg-1"><invocation>timeout 1800 py -3.12 org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/battery_ib_rtg_1.py</invocation><expect>IBR72-EXPORT-RECEIPT-ALIGNED-AND-TAXONOMY-BY-CODE</expect></criterion>

<placeholders>NONE</placeholders>

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rtg-1.the-export-receipt-aligns-to-the-writer-and-the-taxonomy-tests-the-code.md
infra/aws/lambda/investor-reporting/export/
infra/aws/lambda/ci/lambda-source-map.json
infra/aws/terraform/investor-reporting/export/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> v0.7, cell `IB-rtg-1` (s.R7.1 -- the round-7 recut on the round-6 analysis @fa2ff4f0dd).
<owned_cells>IB-rtg-1</owned_cells>
</decomp_ref>

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- nothing scheduled or fired.
comp-iam: DECLARED-NOT-APPLICABLE -- the fix is a source edit under the function's existing role; IF the aligned receipt address needs a GetObject grant the role lacks, that grant is a MEASURED key in this order's never-widen packet (arm (c)), never assumed at the cut.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; the assignee's instrument at report time.
lane: the `<paths>` block above IS the grant plus the two tree-convention grants (`deliverables/<serial>/`, this order's own face). A path you need that is not listed is a BLOCKING row, never an override.
</preflight>

<proof_of_spec>
Criterion ids minted at cut: R72-AC1 (the export route serves the receipt round-trip AND the taxonomy decides off the CODE on a real wire error), R72-AC2 (judgment, the CVO's at L9). Instance at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/IRPT_BCKEND.TO-IB-rtg-1.the-export-receipt-aligns-to-the-writer-and-the-taxonomy-tests-the-code.proof_of_spec.json` (the TASK ORDER'S OWN BASENAME stem), per `org/standards/PROOF_OF_SPEC.schema.json`: one acceptance row per id, `criterion_verbatim` the spec's words, `invocation` the exact command, `output_evidence` the verbatim deciding excerpt, `denominator` beside every count, `expect` carried from this face, and R-40 the content hash of every produced/served artifact EACH PINNED TO THE COMMIT THAT CARRIED IT (`PENDING-THIS-COMMIT` a one-shot sentinel); a blob pin is written `blob <hash>`; the judgment row under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming the CVO. Validate with `py -3.12 .tools/proof-of-spec-check.py <instance> --governing-order <this face path>` BEFORE the complete flip; rc 0 AND R72-AC1 PASS-by-output, then flip this order's `<status>` to `complete` and commit instance and flip together. A FAIL row leaves the order open and is your final report on it.
</proof_of_spec>
