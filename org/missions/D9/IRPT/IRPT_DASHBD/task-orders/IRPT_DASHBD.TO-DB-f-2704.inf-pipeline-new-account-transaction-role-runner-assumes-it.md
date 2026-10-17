# TO IRPT_DASHBD.TO-DB-f-2704 -- the INFLECTION TRANSACTION POLICY MOVES TO A NEW NARROW ROLE, ONE cell: `infra/aws/terraform/inf-pipeline/iam.tf` gains the builder-named role (trust: the runner role only, a fixed session name), the existing four-statement policy re-pointed at it byte for byte, and ONE `sts:AssumeRole` statement on the runner role; the CTO's route-B ruling, msg 10542

<to_id>IRPT_DASHBD.TO-DB-f-2704</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~2704</issued_to>
<issued_by>2.0.0_SA_COO~F2</issued_by>
<issued_date>2026-10-17</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>139</round>
<workstream>F2INFROLE</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** F2INFROLE (`~F2`) | **Ordered by:** 1.0.0_SA_CTO~DELL2, msg 10542 (route B): the four-statement policy lives on a NEW role whose builder-made name matches `role/*-inf-*` so the Inflection bucket's cross-firm fence admits it; the runner role may assume it; the fence, the registry and the bucket policy are not touched. | **Decomp cell:** `DB-f-2704` (`org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_R139_F.md`, amendment 3) | **outcome_ref:** FWD-5 | **depends_on:** `DB-f-2501`, `DB-f-2603` (merged).

**Risk class WORLD** is the floor of the path below (`infra/` path): Terraform text in a branch; no Terraform command, no AWS call, no push. The plan, the pair's signatures, the apply and the simulation are later acts of the Inflection pair (a NEVER-WIDEN pair) and of the single IRPT CloudOps lane, after Monday's 49 Financial first-fire read.

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-2704` (branch `wk-IRPT_DASHBD-2704`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~2704/`. The worktree is a full checkout. Never push; never commit the workspace `portal` gitlink. **You have NO AWS and run NO Terraform command: make no AWS call of any kind.** No client data. Write files with the Write or Edit tool, not shell heredocs. Do not grep or find recursively over the repo; read named files.

**Why.** The Inflection gold bucket denies every principal whose ARN does not match `role/*-inf-*` (or a listed exemption); the runner role `inf-gold-layer-ec2-role` matches neither, so the policy of DB-f-2501 and DB-f-2603 on it can never write. The policy moves to a new role the builder names `orion-inf-account-transaction-role` (it matches), and the runner role assumes it.

**The cell (`DB-f-2704`).**
1. **Read first, whole:** the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r139/p139_inf_role.py` (your three criteria; the header, `semantic_problems`, `removed_outside_region` and the function `reference` are the exact spec, and `reference(base)` returns an edit that passes all three; it has a `--selftest <repo_root>`), the pinned base `checks/r139/inf_iam_r139_base.tf.txt` (the trunk's `iam.tf`), and `infra/aws/terraform/inf-pipeline/iam.tf` from the line `# 1b. Inflection account_transaction gold step` to the resource `inf_gold_layer_runner_shared` (modules, locals, the policy with S1 to S4). For the shape of a role plus an assume policy, read the precedent statement `IrptHmacListStageAssumeRole` in `infra/aws/terraform/mdpf-pipeline/iam.tf` and `infra/aws/terraform/investor-reporting/directory/hmac_list_stage.tf`.
2. **The edit: ONE file, `infra/aws/terraform/inf-pipeline/iam.tf`** (added lines ASCII; LF endings; the removed lines only inside the 1b region):
   - two modules from `../modules/opal_name` in the file's existing module shape: the role name (system `orion`, scope `inflection`, function `account-transaction`, kind `role`) and the assume policy's name (function `account-transaction-assume`, kind `policy`);
   - locals: `txn_session_name = "inf-g-01-account-transaction"` and `txn_role_arn = "arn:aws:iam::${local.account_id}:role/${module.account_transaction_role_name.name}"`;
   - `aws_iam_role.inf_account_transaction`: name from the role module; `assume_role_policy` one statement, `sts:AssumeRole`, Principal AWS = `aws_iam_role.inf_gold_layer.arn` ONLY, Condition `StringEquals` `sts:RoleSessionName` = `local.txn_session_name`;
   - the existing `aws_iam_role_policy.inf_gold_layer_account_transaction` keeps its name and its four statements BYTE FOR BYTE; only its `role` line changes, to `aws_iam_role.inf_account_transaction.id`;
   - `aws_iam_role_policy.inf_gold_layer_assume_account_transaction` on `aws_iam_role.inf_gold_layer` with ONE statement, Sid `AssumeTheAccountTransactionRoleOnly`, `sts:AssumeRole`, Resource `[local.txn_role_arn]`, nothing else.
   - No typed role or bucket name, no wildcard, no data action in the assume policy, no change to any other policy, role or file. You may NOT run `terraform fmt`; align as the file does.
3. **Run the checks yourself before the record:** `python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r139/p139_inf_role.py" . DBF139-4-AC1`, then `AC2`, then `AC3`. Write `RD_INF_ACCOUNT_TRANSACTION_ROLE_FACTS_R139.json` in your folder: `claim` ("measured"), `lines_added`, `lines_removed`, `statements` (the four sids), `resources_added` (3), `registry_files_touched` (0), `other_files_touched` (0).
4. Commit with `.tools/safe-commit.sh --author "0.9.0_WK_IRPT_DASHBD~2704 <0.9.0_WK_IRPT_DASHBD~2704@opal.agent>" -F <msgfile> -- <paths>` (message file written with the Write tool): `iam.tf` and the facts record in one commit, the proof in a second.

<criterion id="DBF139-4-AC1" cell_refs="DB-f-2704" judgment="false"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r139/p139_inf_role.py" . DBF139-4-AC1</invocation><expect>DBF139-4-AC1 PASS</expect></criterion>
`DBF139-4-AC1` -- the root's 46 other files are byte-identical to the base; `iam.tf` differs from the pinned base only by additions plus changes inside the 1b region; added lines ASCII, LF endings kept. Base: FAIL (iam.tf unchanged).
<criterion id="DBF139-4-AC2" cell_refs="DB-f-2704" judgment="false"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r139/p139_inf_role.py" . DBF139-4-AC2</invocation><expect>DBF139-4-AC2 PASS</expect></criterion>
`DBF139-4-AC2` -- the new role: builder-made names (kind role and kind policy), trust the runner role only with the fixed session name, the existing policy now on the new role with S1 to S4 unchanged. Base: FAIL (no role).
<criterion id="DBF139-4-AC3" cell_refs="DB-f-2704" judgment="false"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r139/p139_inf_role.py" . DBF139-4-AC3</invocation><expect>DBF139-4-AC3 PASS</expect></criterion>
`DBF139-4-AC3` -- the runner role's assume policy: exactly one statement, `sts:AssumeRole`, on the new role's ARN only; no data action, no wildcard, no typed name. Base: FAIL (no assume policy).

<expected_criteria>DBF139-4-AC1, DBF139-4-AC2, DBF139-4-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited: every other Terraform file, the registry, the standards, the bucket policy, the launcher, the checker.
- **AWS: none; no Terraform command; no push.** No file under `infra/logic/registry/` or `org/standards/` is touched.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If `iam.tf` at your worktree's HEAD differs from the pinned base (someone edited it), STOP and report; do not merge by hand.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W2704-S<k>` (D2 is the device coordinate, never F2), with the real UTC time (`date -u +%FT%TZ`); append as BYTES. **Report once, under 150 words.**

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~2704/
infra/aws/terraform/inf-pipeline/iam.tf
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-f-2704.inf-pipeline-new-account-transaction-role-runner-assumes-it.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_R139_F.md</decomp_doc> round 139, workstream F2INFROLE (F-SHIP), cell `DB-f-2704`.
<owned_cells>DB-f-2704</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBF139-4-AC1, DBF139-4-AC2, DBF139-4-AC3 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~2704/IRPT_DASHBD.TO-DB-f-2704.inf-pipeline-new-account-transaction-role-runner-assumes-it.proof_of_spec.json`
(copy the shape of `deliverables/0.9.0_WK_IRPT_DASHBD~2603/IRPT_DASHBD.TO-DB-f-2603.inf-pipeline-runner-policy-gains-s4-list-on-gold-prefix.proof_of_spec.json`). Validate with `python .tools/proof-of-spec-check.py <instance> DBF139-4-AC1,DBF139-4-AC2,DBF139-4-AC3 --governing-order <this order>` (from the repo root, the order path repo-relative); pin each artifact row to the commit that carried it. Do not flip the order's status; the issuer does.
</proof_of_spec>

**REPORT:** each criterion's last line; the facts record; the commits. No client figure.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; Terraform text in a branch, nothing planned or applied; the blast radius of the later apply is one new role, its inline policy and one inline policy on the runner role, named in the Inflection pair's packet REVISION 2.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; the role, trust and policies are the checker's subject (graded from the text); the simulation WITH the bucket policy as the resource policy runs at the apply (the finding R139_INFLECTION_BUCKET_FENCE_FINDING).
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is changed.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; DBF139-4-AC1 to AC3 FAIL at base, the checker's reference edit made all three PASS and was restored, and the pure helpers are exercised by its selftest (11 arms).
lane: the <paths> block IS the grant.
</preflight>
