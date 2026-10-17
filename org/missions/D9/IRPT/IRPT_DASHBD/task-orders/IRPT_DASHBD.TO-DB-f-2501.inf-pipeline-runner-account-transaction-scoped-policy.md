# TO IRPT_DASHBD.TO-DB-f-2501 -- the INFLECTION RUNNER'S NEW SCOPED POLICY, ONE cell: `infra/aws/terraform/inf-pipeline/iam.tf` gains, by pure insertion, ONE new inline policy on the Orion gold runner's role with three statements (Get and List on the Orion Inflection `fact_transactions` silver prefix; Put on the one Inflection `account_transaction` gold prefix), every bucket and prefix derived from the registry; the cross-adjudication XA-20261017T005839Z-a222, RULED yes (msg 10119)

<to_id>IRPT_DASHBD.TO-DB-f-2501</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~2501</issued_to>
<issued_by>2.0.0_SA_COO~F2</issued_by>
<issued_date>2026-10-17</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>137</round>
<workstream>F2INFIAM</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** F2INFIAM (`~F2`) | **Ordered by:** 1.0.0_SA_CTO~DELL2, the cross-adjudication `org/critical_paths/cross_adjudication/20261017T0102Z_XA-20261017T005839Z-a222.md` (RULED yes at 01:02:59Z; msg 10119; the REC in msg 10106 and the submission `deliverables/1.0.0_SA_CTO~DELL2/XADJ_D95F_INFLECTION_RUNNER_IAM_SUBMISSION_20261017.md` @cac7bf1012): "(a) the runner role, through ONE new scoped inline policy: Get and List on the Inflection fact_transactions silver prefix, Put on the one Inflection gold prefix, addresses by address(), nothing cross-firm"; condition (2): "ListBucket conditioned on s3:prefix equal to that one prefix and its children, and the GetObject resource ending at it" | **Rows:** IRPT_DASHBD-D2-W2501-S<k> | **Decomp cell:** `DB-f-2501` (`org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_R137_F.md`) | **outcome_ref:** FWD-5 | **depends_on:** none

**Risk class WORLD** is the floor of the path below (`infra/` path): Terraform text in a branch; no Terraform command, no AWS call, no push. The plan, the pair's signatures, the apply, the policy simulation and the first run are later acts of the pair (CTO condition 1: a NEVER-WIDEN pair, since it is a new read on client data) and of the single IRPT CloudOps lane, AFTER Monday's 49 Financial first-fire read and never at the same time as another IB2 apply.

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-2501` (branch `wk-IRPT_DASHBD-2501`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~2501/`. The worktree is a full checkout. Never push; never commit the workspace `portal` gitlink. **You have NO AWS in this order and run NO Terraform command: make no AWS call of any kind.** No client data is read or recorded. Write files with the Write or Edit tool, not shell heredocs. Do not grep or find recursively over the repo; read named files.

**Why.** The Orion gold runner's role `inf-gold-layer-ec2-role` (`aws_iam_role.inf_gold_layer`, `inf-pipeline/iam.tf`) can read and write `opal-data-inf` and, in the assets bucket, only the scope-account-feed prefixes. The Inflection transaction step (the launcher `INF_G_01.account_transaction_gold.py`, round 135) reads ONE Orion silver snapshot from `fact_transactions` (a different prefix of the assets bucket, which the role cannot read) and writes the Inflection gold `account_transaction` days (a different bucket, on which the role holds nothing). The role also carries an explicit deny on two other firms' buckets. The measured read is `deliverables/2.0.0_SA_COO~F2/R137_INFLECTION_RELEASE_PLAN.md`.

**The model (read it whole).** The block `1a. Scope account feed` in `inf-pipeline/iam.tf` (lines about 120 to 195): an `opal_name` module for the policy name, a `locals` block that derives the sources, scopes, tier homes and keys from `infra/logic/registry/*.json` by `lookup`, and an `aws_iam_role_policy` of two statements. Your block follows it exactly in spirit: nothing typed that the registry holds.

**The cell (`DB-f-2501`).**
1. **Read first, whole:** the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r136/p137_inf_tf.py` (your two criteria; `insertion_problems` and `semantic_problems` are the exact spec; it has a `--selftest`), the pinned base copy `checks/r136/inf_iam_base.tf.txt` and the manifest `checks/r136/inf_pipeline_base_manifest.json`; `iam.tf` (whole); `lib/opal_naming.py` `address()` and `name()`; the launcher's two addresses (`data/inf/scripts/gold/INF_G_01.account_transaction_gold.py`: `ORION_BUCKET`, `ORION_PREFIX`, and the gold address its producer builds with `opal_naming.address("irpt", "inflection", "gold", "account_transaction", ...)`).
2. **The edit: ONE file, `infra/aws/terraform/inf-pipeline/iam.tf`, by PURE INSERTION** (every base line survives in order; added lines ASCII; LF endings), placed just BEFORE the line `resource "aws_iam_role_policy" "inf_gold_layer_runner_shared" {` with a comment header in the style of the scope-feed block naming this order and the ruling. It adds:
   - `module "account_transaction_policy_name"` from `../modules/opal_name` with `system = "orion"`, `scope = "inflection"`, `function = "account-transaction"`, `kind = "policy"` (the builder was run by the issuer: it returns `orion-inf-account-transaction-policy` and needs NO registry row; **if you find otherwise, STOP**: file a BLOCKING row and do NOT edit any file under `infra/logic/registry/` or `org/standards/`, because the Inflection bundle's pin holds those files);
   - a `locals` block that derives, from the existing registry locals (`scope_feed_tiers`, `scope_feed_scopes`, `scope_feed_source`, `scope_feed_scope` already in the file) and the two table names (`fact_transactions` and `account_transaction`, the only typed values): the silver bucket (the FIRM tier home for silver, as the scope feed does), the silver key `${source}/${scope}/silver/fact_transactions`, the gold bucket (the Inflection scope row's `bucket` in `scopes.json`) and the gold key `irpt/${scope}/gold/account_transaction`. Name every new local with the prefix `txn_`;
   - `resource "aws_iam_role_policy" "inf_gold_layer_account_transaction"` with `name = module.account_transaction_policy_name.name`, `role = aws_iam_role.inf_gold_layer.id` and a `jsonencode` policy of EXACTLY three statements, each Effect Allow:
     - `S1ReadOrionInflectionTransactionsSilverOnly`: Action `["s3:GetObject"]`; Resource the silver bucket's `arn:aws:s3:::<bucket>/<silver key>/*` (the resource ends at that prefix's children); no condition;
     - `S2ListOrionInflectionTransactionsSilverOnly`: Action `["s3:ListBucket"]`; Resource the silver bucket's arn; Condition `StringLike` on `s3:prefix` with values `[<silver key>, "<silver key>/*"]` (the prefix and its children);
     - `S3PutInflectionAccountTransactionGoldOnly`: Action `["s3:PutObject"]`; Resource `arn:aws:s3:::<gold bucket>/<gold key>/*`; no condition.
   - No other action, no wildcard action or resource, no typed bucket name (`opal-data-...`), no change to any existing policy, statement, the role or any other file. `terraform fmt` style: align as the file does; you may NOT run it.
3. **Run the checks yourself before the record:** `python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r136/p137_inf_tf.py" . DBF137-5-AC1`, then `DBF137-5-AC2`.
4. **Record** `RD_RUNNER_POLICY_FACTS_R137.json` in your folder with EXACTLY these fields: `file` ("infra/aws/terraform/inf-pipeline/iam.tf"); `lines_added` (an integer); `policy_resource` ("aws_iam_role_policy.inf_gold_layer_account_transaction"); `policy_name_builder_output` ("orion-inf-account-transaction-policy", as `lib/opal_naming.py name()` returns it); `statements` (the three sids with their actions); `derived_addresses` ({`silver_prefix_template`, `gold_prefix_template`}: the HCL template strings you wrote, which must equal what `address()` yields for the same segments, said in words); `registry_files_touched` (0); `other_files_touched` (0); `words` (one paragraph, 80 to 1800 characters: what changed and why, and what is NOT proven: no plan was run and nothing was applied; the role's other consumers, the trust policy and the post-apply policy simulation are the applier's steps under the signed pair).

<criterion id="DBF137-5-AC1" cell_refs="DB-f-2501" judgment="false"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r136/p137_inf_tf.py" . DBF137-5-AC1</invocation><expect>DBF137-5-AC1 PASS</expect></criterion>
`DBF137-5-AC1` -- every other file of the `inf-pipeline` root is byte-identical to the base (the manifest of 46 files, sha256), and `iam.tf` differs from the pinned base copy by insertion only (no base line removed or changed, added lines ASCII, LF). Base: FAIL.
<criterion id="DBF137-5-AC2" cell_refs="DB-f-2501" judgment="false"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r136/p137_inf_tf.py" . DBF137-5-AC2</invocation><expect>DBF137-5-AC2 PASS</expect></criterion>
`DBF137-5-AC2` -- the meaning: the resource `inf_gold_layer_account_transaction` attaches to `aws_iam_role.inf_gold_layer`, takes its name from an `opal_name` module of kind policy, and holds exactly the three statements with exactly the actions `s3:GetObject`, `s3:ListBucket` (conditioned by `StringLike` on `s3:prefix`) and `s3:PutObject`; no wildcard, no typed bucket name; the inserted text names `fact_transactions`, `account_transaction`, `silver` and `gold`. Base: FAIL.

<expected_criteria>DBF137-5-AC1,DBF137-5-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited: every other Terraform file, the registry, the standards, the launcher, the producers.
- **AWS: none; no Terraform command; no push.**
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If a checker clause is wrong rather than your edit, file a BLOCKING row naming the clause and stop on it.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W2501-S<k>` (D2 is the device coordinate, never F2), with the real UTC time (`date -u +%FT%TZ`); append as BYTES (the file is shared and append-only). Commit with `.tools/safe-commit.sh`; run its gates in the background and wait. ASCII only. If a commit is refused because the order is `complete`, stop and report.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~2501/
infra/aws/terraform/inf-pipeline/iam.tf
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-f-2501.inf-pipeline-runner-account-transaction-scoped-policy.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_R137_F.md</decomp_doc> round 137, workstream F2INFIAM (F-SHIP), cell `DB-f-2501`.
<owned_cells>DB-f-2501</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBF137-5-AC1, DBF137-5-AC2 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~2501/IRPT_DASHBD.TO-DB-f-2501.inf-pipeline-runner-account-transaction-scoped-policy.proof_of_spec.json`
(copy the shape of the instance at `deliverables/0.9.0_WK_IRPT_DASHBD~2202/`). Validate it with `python .tools/proof-of-spec-check.py <instance> DBF137-5-AC1,DBF137-5-AC2 --governing-order <this order>` (from the repo root, the order path repo-relative) BEFORE you finish; pin each artifact row to the commit that carried it. Do not flip the order's status; the issuer does.
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the facts record's numbers; the commit hash(es); anything off-task (as row ids). No client figure.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: Terraform text in a branch; no plan, no apply; the blast radius (a scoped read of one silver prefix and a scoped write of one gold prefix on the runner's role) is the signed pair's to state.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: the role's live policies were read by the issuer (R137_INFLECTION_RELEASE_PLAN.md); this cell changes text only, and the pair's applier prints the role's attached and inline policies and its trust before the apply and simulates the policy after it (CTO conditions 3 and 4).
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; DBF137-5-AC1 and AC2 FAIL at base, the checker's helpers are exercised by its self-test (10 arms) and a reference insertion shaped like the scope-feed block passes both clauses.
lane: the <paths> block IS the grant.
</preflight>
