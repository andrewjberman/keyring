# TO IRPT_BCKEND.TO-IB-pr-603 -- BUILD the Scope feed's IAM resource in `infra/aws/terraform/inf-pipeline/iam.tf` so that the commit-time naming gate ACCEPTS it: the policy name from the `opal_name` module, every scope, bucket and prefix read from the registry (no apply, no plan against AWS)

<to_id>IRPT_BCKEND.TO-IB-pr-603</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~439</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>8</round>
<workstream>~PO</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** IB2's STOP on IB-pr-600 (msg 8563: the commit-time naming gate, LGIC_ENFORCE, rule 30, refuses the signed packet's HCL: the policy name `scope-account-feed-assets-put` has a token in no vocabulary, and four hand-typed `inflection`/bucket/prefix strings must come through the registry) | **Decomp cell:** `IB-pr-603` (decomposition section 228) | **outcome_ref:** FWD-3

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-IRPT_BCKEND-439`, cut from the current branch by the issuer. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~439 <0.9.0_WK_IRPT_BCKEND~439@opal.agent>" -F <msgfile> -- <explicit paths>` (message file by the Write tool, ending with `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>`; no backtick or dollar-parenthesis in the command line). `portal` shows modified in a fresh worktree: NEVER commit it. Never push. Do not run a recursive grep over the repository (use Grep, Glob, Read on named files and folders). Commit gates take minutes: wait for them. **The worktree is a sparse checkout:** your first act is `git sparse-checkout add infra/aws/terraform/inf-pipeline infra/aws/terraform/modules infra/logic lib org/standards` and, if the commit gate asks for it, the further directory it names (locally, never committed). **Client data rule:** no account, household or client identifier in any tracked file. **Channel rows:** append each row you file as its OWN block at the END of `INVESTIGATION_v1.md`: a line `## <row id> -- <one line>`, a blank line, a ```json fence holding ONE row object, a closing fence.

**Cell `IB-pr-603` (inlined).** The inf gold runner role `inf-gold-layer-ec2-role` cannot put the Scope account feed's keys: the feed lives in the shared assets bucket (`lib/opal_naming.address()` for source `orion`, scope `inflection`, tiers bronze and silver, table `scope_account_returns`; tiers.json FIRM bronze and silver point at it, doctrine R4) and the role reaches the inf bucket only. The signed IAM pair (packet `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/NEVER_WIDEN_SIGNOFF_PACKET_SCOPE_FEED_IAM_PAIR.md`, blob `cea5395ee7`; read its sections "Root, address and plan shape" (the HCL) and "Why") grants ONE new inline policy of two statements: S1 `s3:PutObject` and `s3:GetObject` on the two feed prefixes; S2 `s3:ListBucket` on the bucket under an `s3:prefix` condition naming the same two prefixes. **Its HCL was written with the policy name and the scope, bucket and prefix strings typed by hand, and the commit-time naming gate REFUSES that.** This cell writes the SAME resource so the gate ACCEPTS it. It changes the SPELLING, never the grant: the two statements, the actions, the conditions and the resource address stay exactly the packet's. **BUILD ONLY: no `terraform plan` or `apply` against AWS, no AWS call, no write to any registry file.**

**READ FIRST (named files only):** the packet section above; `infra/aws/terraform/inf-pipeline/iam.tf` (the neighbouring `inf_gold_layer_s3` resource, lines 97 to 121, shows the role reference `aws_iam_role.inf_gold_layer.id`); `infra/aws/terraform/inf-pipeline/inf-portal-publisher-floor.tf` (a file in the same root that already uses the `opal_name` module: copy its idiom for the policy NAME); the module `infra/aws/terraform/modules/opal_name/` (its variables and outputs); `.tools/naming-gate.py` lines 600 to 710 (the function `tf_literals` states the permitted forms: a literal inside a `module` block whose source is the opal_name module; the key of `lookup(local.X, "<key>")` or `local.X["<key>"]` where local X is fed in the same file from `jsondecode(file(".../logic/registry/<name>.json"))`); `lib/opal_naming.py` (`address()`, `name()`, `lookup()`, `grade()`); and the registry files `infra/logic/registry/tiers.json` and `infra/logic/registry/scopes.json` (read only).

**Do:**
1. Add to `iam.tf` (beside `inf_gold_layer_s3`; change nothing else in the file) the resource `aws_iam_role_policy.inf_gold_layer_scope_feed` with the packet's two statements (same `Sid` values, `Effect`, `Action` lists and the `s3:prefix` `StringLike` condition), `role = aws_iam_role.inf_gold_layer.id`, a policy NAME from the `opal_name` module (choose the system, scope-less shared function and kind tokens the module's variables take so that the module output is a name `lib/opal_naming.grade()` accepts; try candidates with `grade()` or `name()` BEFORE you edit, and record the chosen module arguments), and the bucket, the two object-ARN prefixes and the two list prefixes built in a `locals` block from `jsondecode(file("${path.module}/<relative path>/logic/registry/<tiers or scopes>.json"))` and `lookup(local.X, "<key>")` / `local.X["<key>"]`, composed the way `address()` composes them for source `orion`, scope `inflection`, tiers bronze and silver, table `scope_account_returns`. No quoted string inside the resource block may contain `inflection`, `orion`, `opal-data-assets` or `scope_account_returns`; they come only through the registry reads. The result evaluates to exactly the `address()` output for the two layers, as ARN prefixes ending `/*` for objects and key prefixes ending `/*` for the list condition.
   **AMENDMENT 1 (issuer, after worker 438's stop, rows W438-S1 to S3 merged @ed884f9095):** the TABLE name `scope_account_returns` has no registry row and the issuer does not ask for one: write it ONCE as a plain string in a `locals` block, OUTSIDE the resource block (the naming gate grades such a bare literal 0 literals, row W438-S2); the resource block itself holds no quoted string containing it. Say in a note that the table name is the one value not read from the registry. The policy name route you found works (`name()` of source `orion`, scope `inflection`, function `scope-account-feed`, kind `policy` grades CONFORMANT as IAM_POLICY, row W438-S1's probe): take the NAME from the `opal_name` module with those arguments if the module takes them, else from the closest accepted form, and record the arguments. Everything else in this cell is unchanged. Slot ~439 is yours; worker 438's commits are inherited state (rows only, `iam.tf` unchanged).
2. **Commit** `iam.tf` (and nothing else of the product) with `safe-commit.sh`; the commit-time naming gate runs on it. **It must ACCEPT.** If it refuses, read what it prints (it names the literal and the canonical form) and fix the spelling; repeat. If no spelling is accepted because a REGISTRY ROW is missing (for example a name token in no vocabulary), STOP, file a row naming the row to add, and change nothing in `infra/logic/registry/` (the CTO adds registry rows).
3. **Evaluate** the prefixes your locals build WITHOUT AWS: if `terraform` is installed, `terraform console` over the root is not available offline, so instead write a small python script (committed in your deliverables folder) that performs the same registry lookups your locals make and prints the resulting ARN prefixes, and compare them with the `address()` output for the two layers; record `evaluated_by` `registry reading`. The lists must be equal character for character.

**Record** `deliverables/0.9.0_WK_IRPT_BCKEND~439/IB234-1_scope_feed_iam_hcl.json`: `{"base_commit":"<40hex: git rev-parse HEAD at your first act>","changed_paths":["infra/aws/terraform/inf-pipeline/iam.tf"],"naming_gate":{"commit_accepted":true,"refused":0,"literals_graded":<n: the count the gate printed, 1 or more>,"policy_name_source":"name()" or "registered"},"evaluated_prefixes":[<the two object ARN prefixes>],"evaluated_by":"registry reading","module_arguments":{"<what you passed the opal_name module>"},"notes":[at least two lines of 30+ characters: what each fact rests on, what was not run],"functions_invoked":0,"sign_ins_made":0,"aws_writes_made":0,"rows_written":0,"figures_written":0,"vendor_requests_sent":0}`. `changed_paths` lists the files your commits changed other than your deliverables folder and the channel file. Commit the python script and the record under your deliverables folder, record each criterion output and exit code verbatim in `IB234-1_criteria_output.txt`, write the proof instance named under proof_of_spec (**it MUST carry a `decomp_ref` object `{"doc":"org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md","vintage_commit":"<the 40-hex commit of your base>","to_ref":"<this order file's repo path>"}`**) and validate it with `python .tools/proof-of-spec-check.py <instance>`; commit the instance alone in a second commit with explicit paths. Do not flip the order's status. Report once, in your final message: the commit ids, the three outputs, the rows filed.

**Criteria (run each under `timeout 120` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB234-1-AC1" cell_refs="IB-pr-603"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r234/p234_cells.py" . IB234-1-AC1</invocation><expect>IB234-1-AC1 PASS</expect></criterion>
<criterion id="IB234-1-AC2" cell_refs="IB-pr-603"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r234/p234_cells.py" . IB234-1-AC2</invocation><expect>IB234-1-AC2 PASS</expect></criterion>
<criterion id="IB234-1-AC3" cell_refs="IB-pr-603"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r234/p234_cells.py" . IB234-1-AC3</invocation><expect>IB234-1-AC3 PASS</expect></criterion>

<expected_criteria>IB234-1-AC1, IB234-1-AC2, IB234-1-AC3</expected_criteria>

What the checks grade: AC1 the resource in `iam.tf` holds exactly two statements with the packet's actions, no Delete and no KMS action, the `s3:prefix` condition, the role reference, and no hand-typed `inflection`, `orion`, bucket or table literal; AC2 the diff bounded to `iam.tf`, the commit accepted by the naming gate, the evaluated prefixes equal to `address()` output; AC3 notes and the six counters 0. Do not edit the checks.

## BOUNDS

- **Grant:** the `paths` block, the worktree and a scratch directory outside the repository. READ ONLY on AWS (none needed). **Nothing is planned against AWS, applied, deployed, written to AWS or to a registry file; the grant of the packet is NOT widened by one action or one prefix.**
- **Refusal clause:** STOP, file a row, change nothing more, on any of: a need to widen an action, a prefix or a condition; a need to edit a registry file or any file outside the paths block (the issuer amends); no spelling the naming gate accepts; a step that stalls 25 minutes. Never weaken a check or the gate.
- **Row ids** are `IRPT_BCKEND-D2-W439-S<k>` (start at 1); file a row for anything odd (`grounding` and `surfaced_at` = `date -u +%FT%TZ`) and keep working.

<paths>
infra/aws/terraform/inf-pipeline/iam.tf
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-603.scope-feed-iam-hcl.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~439/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 228 (round 8, workstream ~PO), cell `IB-pr-603`.
<owned_cells>IB-pr-603</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB234-1-AC1, IB234-1-AC2, IB234-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~439/IRPT_BCKEND.TO-IB-pr-603.scope-feed-iam-hcl.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE you report.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- a repository edit of one Terraform file in the inf-pipeline root; no plan, apply or AWS call; the apply stays IB-pr-600 (IB2) after the CTO re-signs the rebuilt text; the grant is the signed packet's, spelling only.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission is changed by this order (the resource is only written to a file; the grant is applied under IB-pr-600 and its signed pair).
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched or created.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched.
comp-adversary: RUN -- p234_cells.py IB234-1 dry-run at base on dell2 2026-10-15 ~19:3xZ: AC1, AC2, AC3 FAIL (no resource, no record). Positive control in temp git roots the run created itself (the real naming library and registry, a stub iam.tf, a worker commit, a synthetic record; removed): all three PASS; fourteen negatives (Delete action, KMS action, a typed scope, no prefix condition, one statement, no registry local, wrong role, gate not accepted, gate refused, prefixes differ, changed paths wrong, evaluated_by missing, a nonzero counter, short notes) and the no-input cases each fail their own arm.
lane: the paths block IS the grant (floor WORLD by the `infra/` path); worker `0.9.0_WK_IRPT_BCKEND~439` (worktree `C:/dev/wk-IRPT_BCKEND-439`). Class WORLD by path; nothing is deployed.
</preflight>
