# TO-AR-g-172 -- the resident role may read the model return series and the positioning object (Terraform, plan only)

<to_id>IRPT_ANLREQ.TO-AR-g-172</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~331</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-20</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>60</round>
<workstream>~G</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (ENGINE) | **Decomp cell:** `AR-g-172` (`decompositions/IRPT_ANLREQ_DECOMP_R60_G.md`) |
**outcome_ref:** FWD-10 (PRD v0.25 @b83ce81b5b, C-MODEL-SOURCE; CTO msg 11442, ruling R1) | **depends_on:** none (chain B, independent of chain A). Nothing is deployed by this cell.

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~331`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-331` (branch `wk-IRPT_ANLREQ-331`), provisioned by the issuer. Work only there. First confirm `org/` and `.tools/` exist in it.
- Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~331 <0.9.0_WK_IRPT_ANLREQ~331@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool. Do not pre-`git add`. The worktree may show ` M portal` and a modified `.parquet` fixture: never commit either.
- A row id has the form `IRPT_ANLREQ-D2-W331-S<k>` (check the channel file for `W331` first); `surfaced_at` of any row = `date -u +%FT%TZ` at filing.
- Python 3.9 syntax, ruff clean, ASCII only. Run tests with plain `python -m pytest --color=no -q -p no:cacheprovider` (the producer's tests need `pypdf`, which `python -I` cannot see). Do not touch anything outside the `<paths>` block. Do NOT run `git sparse-checkout`.
- **The checker** is `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_grant_check.py` (read it; you cannot edit it). It builds its own deterministic fixtures and computes every expected number itself, independent of your code: if your number and the checker's differ, re-read the cell text before you doubt the checker, and if you still believe the checker is wrong file a BLOCKING row quoting both numbers, and stop on that criterion.

### THE CELL (`AR-g-172`, inlined)

Directory `TF` = `infra/aws/terraform/investor-reporting/ycharts/`. Edit ONE file: `TF/resident.tf`. Terraform is not installed on this box: nothing is planned, applied or run; the commit is the PIN for the later CloudOps apply.

**Why.** FWD-10 reads two objects of the firm-neutral bucket `opal-data-portal-v2` (PRD C-MODEL-SOURCE; CTO ruling R1, key corrected @b9de1e559d). The resident runs on the YCharts runner host under `aws_iam_role.runner`; its policy is `aws_iam_role_policy.runner_resident` in `TF/resident.tf`. That policy has no grant on either key (issuer trace Q5), so the producer's read would be AccessDenied. The precedent is commit `430cd08b2aa` (TO-AR-y-445): ONE read-only statement added to the same policy, additions only; read its diff first and follow its style.

**The change.** Add ONE statement to `aws_iam_role_policy.runner_resident`: `Effect = "Allow"`, `Action = ["s3:GetObject"]` (exactly that one action; no `GetObjectVersion`, no put, list or delete), `Resource` = exactly two object ARNs: `arn:aws:s3:::opal-data-portal-v2/json/benchmarks/model_portfolio_timeseries.json` and `arn:aws:s3:::opal-data-portal-v2/json/positioning/positioning_data.json`. No wildcard anywhere in the statement. Give it a `Sid` of your choice that names the model series and positioning read, and a comment citing the PRD row and the CTO ruling. If the repository already carries the bucket name `opal-data-portal-v2` in a Terraform local, variable or remote-state output for this root, build the ARNs from that and the two literal keys; otherwise type the bucket once in a `locals` entry with the same comment. Place the statement directly after the last existing S3 read statement of the policy. Do not change any other statement, local, resource or file.

1. Make the edit. 2. Run the three criteria. 3. Commit (code), then the proof and the status flip as separate commits. 4. Report. Include in the report the exact text of the added statement.

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR172-g-AC1" cell_refs="AR-g-172"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_grant_check.py build</invocation><expect>^AR-GRANT-OK</expect></criterion>

<criterion id="AR172-g-AC2" cell_refs="AR-g-172"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_grant_check.py guard</invocation><expect>^AR-GRANT-OK</expect></criterion>

<criterion id="AR172-g-AC3" cell_refs="AR-g-172"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_grant_check.py regress</invocation><expect>^AR-GRANT-REGRESS-OK</expect></criterion>

<expected_criteria>AR172-g-AC1,AR172-g-AC2,AR172-g-AC3</expected_criteria>

- AC1: the diff adds ONE statement allowing exactly `s3:GetObject` on exactly the two keys, with no wildcard and no other action. At base it FAILs (no diff).
- AC2: the diff deletes no line and touches no file but `resident.tf`. At base it PASSes.
- AC3: `resident.tf` is still balanced and every existing statement id is still there. At base it PASSes.

## BOUNDS

- **Grant.** The `<paths>` block only. Every other file is read only.
- **Refusal clause.** If a step cannot be done as written, or a commit is refused as another lane: stop, file a row with the refusal text, report what is committed and what is not, and do not weaken a check or force a commit.
- **Rows.** APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below; gate: `python .tools/surprise-row-gate.py --check <path>`.

<paths>
infra/aws/terraform/investor-reporting/ycharts/resident.tf
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~331/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-172.terraform-read-grant-model-series-and-positioning.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R60_G.md</decomp_doc> round 60, workstream ~G, cell `AR-g-172`.
<owned_cells>AR-g-172</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR172-g-AC1,AR172-g-AC2,AR172-g-AC3. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~331/IRPT_ANLREQ.TO-AR-g-172.terraform-read-grant-model-series-and-positioning.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-172`, and its `decomp_ref` to the order's `<decomp_ref>` block (the proof gate requires it).
- Each acceptance entry's `invocation` is the criterion's text EXACTLY (put any `timeout` bound in the evidence line, not in the invocation).
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder: the code and tests first, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the check's RESULT line.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR172-g-AC1,AR172-g-AC2,AR172-g-AC3` BEFORE the flip to complete. Flip the order's `<status>` to complete ONLY if all three criteria PASS.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~308/IRPT_ANLREQ.TO-AR-g-170.producer-guard-held-price-layout-and-stale-tests.proof_of_spec.json` (read it from the main tree `C:/dev/ajb_workspace` if absent in your sparse worktree).
</proof_of_spec>

**REPORT (final message):** the commit hashes, the three criterion outputs (the RESULT lines), and any row filed.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- one read-only statement on the resident role's policy for two firm-neutral objects; it takes effect only at the CloudOps apply, which waits on the COO+CTO never-widen pair; nothing is planned or applied by this cell.
comp-iam: RUN (by reading) -- the statement is `s3:GetObject` on two exact object ARNs of `opal-data-portal-v2`, additions only. Precedent: commit 430cd08b2aa. Blast radius: the resident role gains read on those two keys and nothing else; rollback: remove the statement.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is added or changed.
comp-cache: DECLARED-NOT-APPLICABLE -- no cache key or TTL is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-adversary: RUN -- the criteria were dry-run at the base from the invocations above: build FAIL (no diff), guard PASS, regress PASS (`ar_grant_check.py`). Traps: `GetObjectVersion` or a list action sneaking in; a wildcard key; deleting a line of the policy; a typed key that differs from the CTO-corrected one (json/benchmarks/..., NOT yang/global/platinum/...). NOT seen (blind): `terraform validate` and `plan` (Terraform is not installed on the boxes; CloudOps plans at the apply).
</preflight>

- Cut by the issuer inside its own decomposition (R60) on the CTO's order to decompose and issue FWD-10 as one round (msg 11442). Base: AC1 FAILs, AC2 PASSes, AC3 PASSes.
