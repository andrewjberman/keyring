# TO IRPT_ANLREQ.TO-AR-y-445.resident-role-reads-the-analysis-commentary-draft-terraform-statement -- TERRAFORM SOURCE ONLY: add ONE read-only statement to the resident role's policy (s3:GetObject and s3:GetObjectVersion on the ANALYSIS_COMMENTARY prefixes of the same client firms), so the packager can read the commentary draft; nothing is planned, applied or run

<to_id>IRPT_ANLREQ.TO-AR-y-445.resident-role-reads-the-analysis-commentary-draft-terraform-statement</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~320</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-20</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>43</round>
<workstream>ZZ104</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD by the path floor | **Decomp cell:** `AR-y-445` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-1 (the four attachments: the packager must read the commentary to attach it), O5 | **depends_on:** IB2 reads A_PACKAGER_CLIENTERROR.txt (R3) and the issuer's simulation on run 6's real keys; CTO msgs 11262 and 11264 ("add s3:GetObject ONLY ... shaped like the existing ycharts_opal_reports grant ... from builder output, no typed ARN"; "approved ... expects exactly 0/1/0")

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~320`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-320` (branch `wk-IRPT_ANLREQ-320`), provisioned by the issuer from the current branch. First confirm `org/` and `.tools/` exist. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~320 <0.9.0_WK_IRPT_ANLREQ~320@opal.agent>" -F <msgfile> -- <paths>`; write every message file with the Write tool; do not pre-`git add`. A commit may take longer than 120 s: give it up to 400 s and check `git log` before retrying. The worktree may show a modified `.parquet` fixture and ` M portal`: never commit either. A row id has the form `IRPT_ANLREQ-D2-W320-S<k>`; `surfaced_at` = `date -u +%FT%TZ`; APPEND only to `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md` (0 deletions), class OBSERVATION or BLOCKING. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` (ruff clean; no single-letter names `l`, `O`, `I`; no non-ASCII).
- **No AWS call, no network, no push, no deploy.** The proof instance copies the shape of `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~306/IRPT_ANLREQ.TO-AR-y-406.resident-release-r34l-build-only-two-movers.proof_of_spec.json` (read it first; `git show HEAD:<path>` if absent), with `to_id` exactly the order's id, a `controls.mutant` that FIRES (named in the cell) and a `controls.determinism` really run; run `python .tools/proof-of-spec-check.py <instance> "<ids>"` with THIS worktree's own `.tools/` and flip `<status>` to `complete` (commit alone) only on VALID.

### THE CELL (`AR-y-445`, inlined)

*Context and the measured gap.* The packager (`ycharts/research/opal_packager.py`, `handle_commentary_ready`) reads the commentary draft with an S3 get through the reporting repository before it renders the commentary PDF. The resident runs as the role `irpt-ycharts-runner-role`, whose inline policy `irpt-ycharts-runner-resident-policy` is the Terraform resource `aws_iam_role_policy.runner_resident` in `infra/aws/terraform/investor-reporting/ycharts/resident.tf`. The issuer ran `iam simulate-principal-policy` for that role on the REAL object keys of run 6 (`s3:GetObject`, `s3:PutObject`): `extraction_evidence`, `normalized_portfolios`, `ycharts_opal_reports` allowed both; `original_holdings` and `request_compositions` allowed get only; `analysis_commentaries` **implicitDeny** for both, so the packager's read raised `ClientError` (AccessDenied) at 08:04:18Z. The family is `ANALYSIS_COMMENTARY` in the reporting policy revision `irpt-anlreq-x10-v1` (`infra/logic/registry/reporting_policies.json`: `{"tier": "state", "table": "analysis_commentaries", "extension": "json"}`, source `irpt`, three client firms). The object keys have the form `irpt/<firm-long>/state/analysis_commentaries/ART-<hex>/<sha256>.json`.

*The change (CTO msgs 11262, 11264).* In `infra/aws/terraform/investor-reporting/ycharts/resident.tf`: (1) add, in the existing `locals` block, a policy local that selects `irpt-anlreq-x10-v1` the way `resident_reporting_policy` selects `irpt-x10-v1`, and a list `resident_commentary_read_prefixes` built exactly like `resident_read_prefixes` (the same `setproduct`-free shape is fine: one entry per key of `local.resident_scopes`) as `arn:aws:s3:::${local.resident_bucket}/${<policy>.source}/${local.resident_scopes[<firm>].long}/${<policy>.families["ANALYSIS_COMMENTARY"].tier}/${<policy>.families["ANALYSIS_COMMENTARY"].table}/*`; NO typed ARN, bucket, firm, tier or table literal. (2) add ONE statement to `aws_iam_role_policy.runner_resident`, placed right after `ReadFrozenCompositionAndNormalizedInput`: `Sid = "ReadTheAnalysisCommentaryDraft"`, `Effect = "Allow"`, `Action = ["s3:GetObject", "s3:GetObjectVersion"]`, `Resource = local.resident_commentary_read_prefixes`, with a comment in the file's style citing the packager read (`ycharts/research/opal_packager.py` `live_read_artifact` -> the repository's S3 get) and these CTO messages. NO put, NO list, NO delete, NO other statement changed, NO other file changed. The KMS decrypt the bucket key needs is already allowed for this role (the simulation says so). Terraform is not installed on this box: do not try to run it.

*What to do.* (1) Read `infra/aws/terraform/investor-reporting/ycharts/resident.tf` (the locals block lines 23-60 and the statements around `ReadFrozenCompositionAndNormalizedInput`) and the registry files it reads (`infra/logic/registry/scopes.json`, `reporting_policies.json`). (2) Make the edit above, only additions (`git diff --numstat` for the file must show `<n> 0`). (3) Write `check_commentary_grant.py` in `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~320/` (stdlib only, ruff clean, offline). It (a) reads `infra/aws/terraform/investor-reporting/ycharts/resident.tf` text and asserts, by regex over the HCL, that the statement `ReadTheAnalysisCommentaryDraft` exists with Effect Allow, Action exactly the two actions above and Resource `local.resident_commentary_read_prefixes`, that the list local is built from `resident_scopes`, `resident_bucket` and the registry policy (and holds no `arn:aws:s3:::opal` literal); (b) evaluates the prefix formula in Python from the registry (`scopes.json`: scopes with class FIRM, tenant kind client and tenant enabled true, the same filter as `local.resident_scopes`; `reporting_policies.json`: the policy `irpt-anlreq-x10-v1`) and compares, firm by firm, with the key the repository's own naming builder gives: load `lib/opal_naming.py` BY PATH (it has no package) and call its `key()` (read its signature first; it returns `{source}/{scope}/{tier}/{table}/{partition}`) with the firm's scope and the family's tier and table; each Terraform prefix must equal `arn:aws:s3:::<bucket>/` + the builder key without its partition part + `/*` (state the comparison you used); the bucket is read from the core stack's reporting bucket name literal only if the file types it, else compared without it; (c) checks that run 6's real commentary key `irpt/49financial/state/analysis_commentaries/` (a literal prefix of the form above) lies under one of the evaluated prefixes. It prints `COMMENTARY-GRANT-OK firms=<n> prefixes=<n> builder_equal=yes` only when all hold, else `COMMENTARY-GRANT-BAD <why>` and a non-zero exit. `--selftest` re-evaluates with the table name changed in memory to `analysis_commentary` and prints `CONTROL-FIRES` only when that variant is BAD. (4) Write `check_commentary_bound.py` in the same folder: it prints `COMMENTARY-BOUND-OK numstat=<n>/0 files=1` only when `git diff --numstat <your cut commit>..HEAD -- infra/` lists exactly one path, `infra/aws/terraform/investor-reporting/ycharts/resident.tf`, with 0 deletions (anchor the cut with `git log --format=%H --grep='TO-AR-y-445' -1 --diff-filter=A -- org/missions/D9/IRPT/IRPT_ANLREQ/task-orders`), else `COMMENTARY-BOUND-BAD <paths>` and a non-zero exit. (5) Commit the Terraform edit ALONE first (subject begins `tf(IRPT_ANLREQ TO-AR-y-445,`; this commit is the PIN the apply order will use), then the workspace files, then the proof instance, and flip on VALID with all three PASS. Report the pin commit sha and the full diff of the file.

---

## ACCEPTANCE

<criterion id="AR445-y-AC1" cell_refs="AR-y-445"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~320/check_commentary_grant.py</invocation><expect>^COMMENTARY-GRANT-OK firms=[0-9]+ prefixes=[0-9]+ builder_equal=yes$</expect></criterion>
<criterion id="AR445-y-AC2" cell_refs="AR-y-445"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~320/check_commentary_grant.py --selftest</invocation><expect>^CONTROL-FIRES$</expect></criterion>
<criterion id="AR445-y-AC3" cell_refs="AR-y-445"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~320/check_commentary_bound.py</invocation><expect>^COMMENTARY-BOUND-OK numstat=[0-9]+/0 files=1$</expect></criterion>



<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~320/IRPT_ANLREQ.TO-AR-y-445.resident-role-reads-the-analysis-commentary-draft-terraform-statement.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-445.resident-role-reads-the-analysis-commentary-draft-terraform-statement`. Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR445-y-AC1,AR445-y-AC2,AR445-y-AC3"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-445</owned_cells>
</decomp_ref>

- **Grant.** The `<paths>` block, this order's file (status line only) and the surprise investigation file are the only repository places you write.

<paths>
infra/aws/terraform/investor-reporting/ycharts/resident.tf
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~320/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-y-445.resident-role-reads-the-analysis-commentary-draft-terraform-statement.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- one Terraform file edited by additions only, plus checks in the worker deliverables; nothing is planned, applied or run; the apply is a later IB2 order under a signed pair.
comp-routes: DECLARED-NOT-APPLICABLE. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call by the worker.
comp-adversary: RUN -- by reading the resident policy statements and the simulation against this cell; the lens: a typed ARN or table name (forbidden: the formula must come from the registry and be proved equal to the naming builder), a Put or List or Delete action (read only), another statement changed, a grant for a family or firm the existing grants do not cover, the control that cannot fire (the selftest changes the table name and must read BAD). NOT seen (blind): the live plan (the apply order expects exactly 0 to add, 1 to change, 0 to destroy on aws_iam_role_policy.runner_resident); denominator: three criteria.
</preflight>
