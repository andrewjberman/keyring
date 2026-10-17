# TO IRPT_DASHBD.TO-DB-f-2603 -- the INFLECTION RUNNER POLICY GAINS S4, ONE cell: `infra/aws/terraform/inf-pipeline/iam.tf` gains, by pure insertion into the block of DB-f-2501, a statement `s3:ListBucket` on the Inflection gold bucket conditioned on `s3:prefix` equal to the one gold prefix and its children (no GetObject on gold), and the two locals it needs; the CTO's ruling, msg 10239

<to_id>IRPT_DASHBD.TO-DB-f-2603</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~2603</issued_to>
<issued_by>2.0.0_SA_COO~F2</issued_by>
<issued_date>2026-10-17</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>138</round>
<workstream>F2INFIAM</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** F2INFIAM (`~F2`) | **Ordered by:** 1.0.0_SA_CTO~DELL2, msg 10239 (the answer to the issuer's ask): "s3:ListBucket on opal-data-inflection, conditioned on s3:prefix equal to irpt/inflection/gold/account_transaction/ and its children (address() output); no GetObject on gold; XA-a222 condition 2's form applies, and its simulate control gains S4: ALLOW for the list on that prefix, DENY for a list of another prefix. Name it in the pair." | **Decomp cell:** `DB-f-2603` (`org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_R138_F.md`, "Cell 3") | **outcome_ref:** FWD-5 | **depends_on:** `DB-f-2501` (merged @3e5d4896e2).

**Risk class WORLD** is the floor of the path below (`infra/` path): Terraform text in a branch; no Terraform command, no AWS call, no push. The plan, the pair's signatures, the apply and the simulation are later acts of the Inflection pair (a NEVER-WIDEN pair) and of the single IRPT CloudOps lane, after Monday's 49 Financial first-fire read.

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-2603` (branch `wk-IRPT_DASHBD-2603`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~2603/`. The worktree is a full checkout. Never push; never commit the workspace `portal` gitlink. **You have NO AWS and run NO Terraform command: make no AWS call of any kind.** No client data. Write files with the Write or Edit tool, not shell heredocs. Do not grep or find recursively over the repo; read named files.

**Why.** The launcher's bounded default (cell DB-f-2602) reads the newest written day by listing the gold prefix; the runner policy of DB-f-2501 lists only the silver bucket, so the list would be AccessDenied. The CTO ruled the fix.

**The cell (`DB-f-2603`).**
1. **Read first, whole:** the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r138/p138_inf_s4.py` (your two criteria; `semantic_problems` and the function `_reference` are the exact spec, `_reference(base)` returns an insertion that passes both criteria; it has a `--selftest`), the pinned base `checks/r138/inf_iam_r138_base.tf.txt` (the trunk's `iam.tf`), and `infra/aws/terraform/inf-pipeline/iam.tf` lines 190 to 260 (the block of DB-f-2501: module, locals, resource with S1 to S3).
2. **The edit: ONE file, `infra/aws/terraform/inf-pipeline/iam.tf`, by PURE INSERTION** (every base line survives in order; added lines ASCII; LF endings):
   - in the existing gold locals (right after `txn_gold_object_arns`), two new locals in the silver locals' shape: `txn_gold_bucket_arn = "arn:aws:s3:::${local.txn_gold_bucket}"` and `txn_gold_list_prefixes = [local.txn_gold_key, "${local.txn_gold_key}/*"]`;
   - in the policy `inf_gold_layer_account_transaction`, a statement placed BETWEEN S2 and S3 (so no existing line changes): `Sid = "S4ListInflectionAccountTransactionGoldOnly"`, `Effect = "Allow"`, `Action = ["s3:ListBucket"]`, `Resource = [local.txn_gold_bucket_arn]`, `Condition = { StringLike = { "s3:prefix" = local.txn_gold_list_prefixes } }`, closed with a comma like S2.
   - No other action, no GetObject or PutObject in S4, no typed bucket name, no wildcard, no change to S1 to S3, to any other policy, the role or any other file. You may NOT run `terraform fmt`; align as the file does (the issuer's `_reference` shows the shape).
3. **Run the checks yourself before the record:** `python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r138/p138_inf_s4.py" . DBF138-3-AC1`, then `AC2`. Also run `python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r136/p137_inf_tf.py" . DBF137-5-AC1` and `AC2`: both must still read PASS. Write `RD_RUNNER_POLICY_S4_FACTS_R138.json` in your folder: `claim` ("measured"), `lines_added`, `statements` (the four sids), `registry_files_touched` (0), `other_files_touched` (0).
4. Commit with `.tools/safe-commit.sh --author "0.9.0_WK_IRPT_DASHBD~2603 <0.9.0_WK_IRPT_DASHBD~2603@opal.agent>" -F <msgfile> -- <paths>` (message file written with the Write tool): `iam.tf` and the facts record in one commit, the proof in a second.

<criterion id="DBF138-3-AC1" cell_refs="DB-f-2603" judgment="false"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r138/p138_inf_s4.py" . DBF138-3-AC1</invocation><expect>DBF138-3-AC1 PASS</expect></criterion>
`DBF138-3-AC1` -- the root's 46 other files are byte-identical to the base and `iam.tf` is a pure insertion of ASCII lines against the pinned base (LF endings kept). Base: FAIL (iam.tf unchanged).
<criterion id="DBF138-3-AC2" cell_refs="DB-f-2603" judgment="false"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r138/p138_inf_s4.py" . DBF138-3-AC2</invocation><expect>DBF138-3-AC2 PASS</expect></criterion>
`DBF138-3-AC2` -- the policy carries S1 to S4, S1 to S3 unchanged, S4 Allow `s3:ListBucket` on the gold bucket conditioned by StringLike on `s3:prefix` over the gold key and its children, no gold GetObject, nothing typed, no wildcard. Base: FAIL (S4 absent).

<expected_criteria>DBF138-3-AC1, DBF138-3-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited: every other Terraform file, the registry, the standards, the launcher, the checker.
- **AWS: none; no Terraform command; no push.** No file under `infra/logic/registry/` or `org/standards/` is touched (the Inflection bundle's pin holds them).
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If `iam.tf` at your worktree's HEAD differs from the pinned base (someone edited it), STOP and report; do not merge by hand.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W2603-S<k>` (D2 is the device coordinate, never F2), with the real UTC time (`date -u +%FT%TZ`); append as BYTES. **Report once, under 150 words.**

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~2603/
infra/aws/terraform/inf-pipeline/iam.tf
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-f-2603.inf-pipeline-runner-policy-gains-s4-list-on-gold-prefix.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_R138_F.md</decomp_doc> round 138, workstream F2INFIAM (F-SHIP), cell `DB-f-2603`.
<owned_cells>DB-f-2603</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBF138-3-AC1, DBF138-3-AC2 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~2603/IRPT_DASHBD.TO-DB-f-2603.inf-pipeline-runner-policy-gains-s4-list-on-gold-prefix.proof_of_spec.json`
(copy the shape of `deliverables/0.9.0_WK_IRPT_DASHBD~2501/IRPT_DASHBD.TO-DB-f-2501.inf-pipeline-runner-account-transaction-scoped-policy.proof_of_spec.json`). Validate with `python .tools/proof-of-spec-check.py <instance> DBF138-3-AC1,DBF138-3-AC2 --governing-order <this order>` (from the repo root, the order path repo-relative); pin each artifact row to the commit that carried it. Do not flip the order's status; the issuer does.
</proof_of_spec>

**REPORT:** each criterion's last line (and the two round-137 lines); the facts record; the commits. No client figure.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; Terraform text in a branch, nothing planned or applied; the blast radius of the later apply is one added statement on one inline policy of one role, named in the Inflection pair's packet.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; the policy is the checker's subject (statements, actions, resources and conditions are graded from the text), and the CTO's condition 4 simulation runs at the apply.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is changed.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; DBF138-3-AC1 and AC2 FAIL at base, the reference insertion made both PASS and was reverted, and the checker's pure helpers are exercised by its selftest (10 arms).
lane: the <paths> block IS the grant.
</preflight>
