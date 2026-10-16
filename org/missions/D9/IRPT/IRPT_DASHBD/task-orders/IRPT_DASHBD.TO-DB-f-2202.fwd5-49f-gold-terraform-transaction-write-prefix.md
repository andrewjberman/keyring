# TO IRPT_DASHBD.TO-DB-f-2202 -- the FWD-5 49 FINANCIAL GOLD TERRAFORM WRITE PREFIX, ONE CELL (W2): the reporting-gold root declares the transaction table and its prefix and adds the prefix, last, to the write list the one PutObject statement takes; no read or list grant, no other file; the CTO's round-135 analysis, item 1 (msg 9837, W2)

<to_id>IRPT_DASHBD.TO-DB-f-2202</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~2202</issued_to>
<issued_by>2.0.0_SA_COO~F2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>136</round>
<workstream>~F2</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** F-SHIP (`~F2`) | **Ordered by:** 1.0.0_SA_CTO~DELL2, the round-135 analysis @8d48df1751 (msg 9837): W2 Terraform (plan offline); ruling 3: the sid `WriteTheFiveGoldPrefixesOnly` stays as it is and the packet states that the plan changes the statement's prefix list only | **Rows:** IRPT_DASHBD-D2-W2202-S<k> | **Decomp cell:** `DB-f-2202` (`org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_R136_F.md`) | **outcome_ref:** FWD-5 | **depends_on:** none

**Risk class WORLD** is the floor of the path below (`infra/` path): Terraform text in a branch; no Terraform command, no AWS call, no push. The plan, the apply and the first write are the applier's under a later signed pair.

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-2202` (branch `wk-IRPT_DASHBD-2202`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~2202/`. The worktree is a full checkout. Never push; never commit the workspace `portal` gitlink. **You have NO AWS in this order and run NO Terraform command: make no AWS call of any kind.** Client data is not involved. Write files with the Write or Edit tool, not shell heredocs. Do not grep or find recursively over the repo; read named files.

**Why.** In `infra/aws/terraform/investor-reporting/reporting-gold/`, the execution role's single PutObject statement (`iam.tf`, sid `WriteTheFiveGoldPrefixesOnly`, which keeps its name: a renamed sid reads as a NEW statement to the issuer's checker) takes its resources from `local.irpt_rg_gold_write_arns` (`locals.tf`). That list names the returns, class, three activity and lot, and filled-report prefixes. The handler is about to write one more table, `account_transaction` (sibling order DB-f-2201), so its prefix joins the list. The handler writes the table but does not list or read it, so the read prefixes, the read arns and the list pattern do NOT change.

**The cell (`DB-f-2202`).**
1. **Read first, whole:** the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r136/p136_tf.py` (your two criteria; `ac1` and `semantic_problems` are the exact spec; it has a `--selftest`); `locals.tf` (read whole) and `iam.tf` (read only).
2. **The edit: ONE file, `infra/aws/terraform/investor-reporting/reporting-gold/locals.tf`, by PURE INSERTION (every base line survives, in order; added lines ASCII, LF endings).**
   - Beside the other table constants, add `irpt_rg_gold_table_transaction = "account_transaction"`.
   - Beside `irpt_rg_gold_filled_prefix`, add `irpt_rg_gold_transaction_prefix = "irpt/${local.irpt_rg_firm}/gold/${local.irpt_rg_gold_table_transaction}/"` (built from the firm and the table constant, never typed).
   - In `irpt_rg_gold_write_arns`, add ONE element as the LAST element: `"arn:aws:s3:::${local.irpt_rg_gold_bucket}/${local.irpt_rg_gold_transaction_prefix}*",`.
   - You may add comment lines (`#`) naming this order and the round. Every other line, and `iam.tf`, `lambda.tf`, `main.tf` and `schedule.tf`, stay byte for byte.
3. **Run the checks yourself before the record:** `python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r136/p136_tf.py" . DBF136-2-AC1`, then `DBF136-2-AC2`.
4. **Record** `RD_TRANSACTION_WRITE_PREFIX_FACTS_R136.json` in your folder with EXACTLY these fields: `file` ("infra/aws/terraform/investor-reporting/reporting-gold/locals.tf"); `lines_added` (an integer); `write_arns_before` and `write_arns_after` (integers); `read_list_changed` (false); `list_pattern_changed` (false); `words` (one paragraph, 80 to 1800 characters: what changed and why, and what is NOT proven: no plan was run and nothing was applied; the plan gate and the first write are the applier's under a later pair).

<criterion id="DBF136-2-AC1" cell_refs="DB-f-2202" judgment="false"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r136/p136_tf.py" . DBF136-2-AC1</invocation><expect>DBF136-2-AC1 PASS</expect></criterion>
`DBF136-2-AC1` -- `iam.tf`, `lambda.tf`, `main.tf` and `schedule.tf` are byte-identical to the base (sha256), and `locals.tf` differs from the pinned base copy by insertion only (no base line removed or changed, added lines ASCII). Base: FAIL.
<criterion id="DBF136-2-AC2" cell_refs="DB-f-2202" judgment="false"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r136/p136_tf.py" . DBF136-2-AC2</invocation><expect>DBF136-2-AC2 PASS</expect></criterion>
`DBF136-2-AC2` -- the meaning: the table constant and the prefix are declared as above, the write list is the base's elements and then exactly the transaction arn as the LAST element, and the read prefixes, read arns and list pattern lines are unchanged and do not name the transaction prefix (no read or list grant). Base: FAIL.

<expected_criteria>DBF136-2-AC1,DBF136-2-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **AWS: none; no Terraform command; no push.**
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If a checker clause is wrong rather than your edit, file a BLOCKING row naming the clause and stop on it.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W2202-S<k>` (D2 is the device coordinate, never F2), with the real UTC time (`date -u +%FT%TZ`); append as BYTES (the file is shared and append-only). Commit with `.tools/safe-commit.sh`; run its gates in the background and wait. ASCII only. If a commit is refused because the order is `complete`, stop and report.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~2202/
infra/aws/terraform/investor-reporting/reporting-gold/locals.tf
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-f-2202.fwd5-49f-gold-terraform-transaction-write-prefix.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_R136_F.md</decomp_doc> round 136, workstream ~F2 (F-SHIP), cell `DB-f-2202`.
<owned_cells>DB-f-2202</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBF136-2-AC1, DBF136-2-AC2 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~2202/IRPT_DASHBD.TO-DB-f-2202.fwd5-49f-gold-terraform-transaction-write-prefix.proof_of_spec.json`
(copy the shape of the instance at `deliverables/0.9.0_WK_IRPT_DASHBD~2101/`). Validate it with `python .tools/proof-of-spec-check.py <instance> DBF136-2-AC1,DBF136-2-AC2 --governing-order <this order>` (from the repo root, the order path repo-relative) BEFORE you finish; pin each artifact row to the commit that carried it. Do not flip the order's status; the issuer does.
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the facts record's numbers; the commit hash(es); anything off-task (as row ids). No client figure.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: Terraform text in a branch; no plan, no apply, nothing deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: the write list gains one prefix in the branch only; the IAM change takes effect at the applier's signed apply, whose plan gate the packet states (0 add / 2 change / 0 destroy: the statement's prefix list and the function's code attributes); the worker has no AWS access.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; DBF136-2-AC1 and AC2 FAIL at base, the checker's helpers are exercised by its self-test (7 arms) and the intended edit applied to a scratch copy passed both clauses.
lane: the <paths> block IS the grant.
</preflight>
