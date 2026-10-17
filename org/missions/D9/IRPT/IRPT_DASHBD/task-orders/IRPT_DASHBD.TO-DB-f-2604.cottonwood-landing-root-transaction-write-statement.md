# TO IRPT_DASHBD.TO-DB-f-2604 -- the COTTONWOOD LANDING ROOT'S TRANSACTION WRITE STATEMENT, ONE cell: `infra/aws/terraform/investor-reporting/account-return-daily/` gains, by pure insertion, the table constant `irpt_arc_gold_table_transaction` (`locals.tf`) and the NEW statement `WriteTheAccountTransactionGoldPrefixOnly` (`iam.tf`: `s3:PutObject` on the one Cottonwood `account_transaction` gold prefix); the CTO's XA-20261016T224156Z-3c21 (msg 10002)

<to_id>IRPT_DASHBD.TO-DB-f-2604</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~2604</issued_to>
<issued_by>2.0.0_SA_COO~F2</issued_by>
<issued_date>2026-10-17</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>138</round>
<workstream>F2COTTF</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** F2COTTF (`~F2`) | **Ordered by:** 1.0.0_SA_CTO~DELL2, XA-20261016T224156Z-3c21 (`org/critical_paths/cross_adjudication/20261016T2302Z_XA-20261016T224156Z-3c21.md`, RULED 23:02:55Z; msg 10002): host the landing function `account-return-daily`, conditional on the sizing read (done: `deliverables/2.0.0_SA_COO~F2/R137_COTTONWOOD_SIZING_READ.md`: the role already lists and reads `fact_transactions` silver, so NO read grant is added; the one new grant is a WRITE); the CTO's acceptance of the round 138 list (msg 10145, item 1) | **Decomp cell:** `DB-f-2604` (`org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_R138_F.md`, "Cells 4 and 5") | **outcome_ref:** FWD-5 | **depends_on:** none.

**Risk class WORLD** is the floor of the path below (`infra/` path): Terraform text in a branch; no Terraform command, no AWS call, no push. The bundle, the plan, the pair's signatures, the apply, the dry run, the first write and the range are later acts (a NEVER-WIDEN pair and the single IRPT CloudOps lane).

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-2604` (branch `wk-IRPT_DASHBD-2604`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~2604/`. The worktree is a full checkout. Never push; never commit the workspace `portal` gitlink. **You have NO AWS and run NO Terraform command: make no AWS call of any kind.** No client data. Write files with the Write or Edit tool, not shell heredocs. Do not grep or find recursively over the repo; read named files.

**Why.** The Cottonwood transaction stage will run as the last stage of the landing function. Its role `irpt-cot-account-return-daily-execution-role` (one inline policy, five statements) already lists and reads the Black Diamond `fact_transactions` silver and writes only the `account_return_daily` gold prefix; the stage needs ONE new write grant on `.../gold/account_transaction/*`. The existing write statement is named for exactly one prefix, so a second resource would make its name false: the new grant is a NEW statement.

**The cell (`DB-f-2604`).**
1. **Read first, whole:** the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r138/p138_cot_tf.py` (your two criteria; its docstring, `RESOURCE`, `SID`, `TABLE_RE` and the helper functions are the exact spec; it has a `--selftest`), the pinned bases `checks/r138/cot_iam_base.tf.txt` and `checks/r138/cot_locals_base.tf.txt` (the trunk's two files), and the root's `iam.tf`, `locals.tf` (whole).
2. **The edit: TWO files, `infra/aws/terraform/investor-reporting/account-return-daily/locals.tf` and `iam.tf`, each by PURE INSERTION** (every base line survives in order; added lines ASCII; LF endings):
   - `locals.tf`: the table constant `irpt_arc_gold_table_transaction = "account_transaction"` beside the existing gold table constant, in the same style.
   - `iam.tf`: ONE new statement in the existing policy document, Sid `WriteTheAccountTransactionGoldPrefixOnly`, Effect Allow, Action `["s3:PutObject"]` only, ONE Resource built exactly as the checker's `RESOURCE` string (the gold-bucket local, the firm local and the new table constant), no Condition. Place it so that no existing line changes (insert it as a whole object after a comma-terminated one, or before the last one; the checker's `insertion_problems` is the test).
   - No other action, no read or list grant, no change to any existing statement, `lambda.tf`, `main.tf` or `schedule.tf`. You may NOT run `terraform fmt`; align as the files do.
3. **Run the checks yourself before the record:** `python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r138/p138_cot_tf.py" . DBF138-4-AC1`, then `AC2`. Write `RD_COT_TF_FACTS_R138.json` in your folder: `claim` ("measured"), `lines_added` (per file), `statement_sids` (the six sids of the policy after), `files_touched` (2), `other_files_touched` (0).
4. Commit with `.tools/safe-commit.sh --author "0.9.0_WK_IRPT_DASHBD~2604 <0.9.0_WK_IRPT_DASHBD~2604@opal.agent>" -F <msgfile> -- <paths>` (message file written with the Write tool): the two Terraform files and the facts record in one commit, the proof in a second.

<criterion id="DBF138-4-AC1" cell_refs="DB-f-2604" judgment="false"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r138/p138_cot_tf.py" . DBF138-4-AC1</invocation><expect>DBF138-4-AC1 PASS</expect></criterion>
`DBF138-4-AC1` -- `locals.tf` and `iam.tf` are pure ASCII insertions against the pinned bases and `lambda.tf`, `main.tf` and `schedule.tf` are byte-identical. Base: FAIL (both unchanged).
<criterion id="DBF138-4-AC2" cell_refs="DB-f-2604" judgment="false"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r138/p138_cot_tf.py" . DBF138-4-AC2</invocation><expect>DBF138-4-AC2 PASS</expect></criterion>
`DBF138-4-AC2` -- the table constant is declared and the new statement is Allow, `s3:PutObject` only, on the one resource built from the gold-bucket, firm and table locals, with no condition, no wildcard and no typed bucket. Base: FAIL (constant and statement absent).

<expected_criteria>DBF138-4-AC1, DBF138-4-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited: every other Terraform file, the registry, the standards, the handler, the checker.
- **AWS: none; no Terraform command; no push.** No file under `infra/logic/registry/` or `org/standards/` is touched.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If either Terraform file at your worktree's HEAD differs from its pinned base, STOP and report; do not merge by hand.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W2604-S<k>` (D2 is the device coordinate, never F2), with the real UTC time (`date -u +%FT%TZ`); append as BYTES. **Report once, under 150 words.**

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~2604/
infra/aws/terraform/investor-reporting/account-return-daily/locals.tf
infra/aws/terraform/investor-reporting/account-return-daily/iam.tf
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-f-2604.cottonwood-landing-root-transaction-write-statement.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_R138_F.md</decomp_doc> round 138, workstream F2COTTF (F-SHIP), cell `DB-f-2604`.
<owned_cells>DB-f-2604</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBF138-4-AC1, DBF138-4-AC2 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~2604/IRPT_DASHBD.TO-DB-f-2604.cottonwood-landing-root-transaction-write-statement.proof_of_spec.json`
(copy the shape of `deliverables/0.9.0_WK_IRPT_DASHBD~2603/IRPT_DASHBD.TO-DB-f-2603.inf-pipeline-runner-policy-gains-s4-list-on-gold-prefix.proof_of_spec.json`). Validate with `python .tools/proof-of-spec-check.py <instance> DBF138-4-AC1,DBF138-4-AC2 --governing-order <this order>` (from the repo root, the order path repo-relative); pin each artifact row to the commit that carried it. Do not flip the order's status; the issuer does.
</proof_of_spec>

**REPORT:** each criterion's last line; the facts record; the commits. No client figure.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; Terraform text in a branch, nothing planned or applied; the later apply's blast radius is one added statement on one inline policy of one role, named in the Cottonwood pair's packet, and the sizing read (R137_COTTONWOOD_SIZING_READ.md) read the live role and policy.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; the policy statements are the checker's subject (actions, resources and conditions are graded from the text) and the live policy was read in the sizing read.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is changed (schedule.tf is byte-identical by criterion).
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; DBF138-4-AC1 and AC2 FAIL at base, the checker's selftest (9 arms) carries a reference insertion that passes both clauses, and its pinned bases were re-pinned to the trunk by the issuer at the cut.
lane: the <paths> block IS the grant.
</preflight>
