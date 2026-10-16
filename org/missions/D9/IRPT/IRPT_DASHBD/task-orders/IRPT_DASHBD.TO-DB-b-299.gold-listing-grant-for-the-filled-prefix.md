# TO IRPT_DASHBD.TO-DB-b-299 -- the LISTING GRANT the 49 Financial gold function's filled-report stage lacks (round 149, row IRPT_BCKEND-D2-S219): the role policy's list pattern also takes the filled report-values prefix; one expression in one Terraform file; no read grant, no write change

<to_id>IRPT_DASHBD.TO-DB-b-299</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~241</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>149</round>
<workstream>GOLDLIST</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** GOLDLIST, round 149 | **Ordered by:** the issuer's own decomposition (section 160), on the first scheduled fire of hop 1 (`irpt-dashbd-hop1-filled-report-values-20261015`, leg L6): `2.0.0_SA_COO~S2`'s msg 9333 and its row `IRPT_BCKEND-D2-S219` (the fire at 11:41Z logged `FILLED_CATCHUP_LIST_FAILED`, AccessDenied on `s3:ListBucket` of `opal-data-49financial`, and wrote 0 objects) | **Decomp cell:** `DB-b-299` (decomposition section 160).

**Risk class WORLD** is the floor of the path below (`infra/` path): one Terraform expression in a branch; no Terraform command, no AWS write, no push. The plan, the apply and the first write are the applier's under a later signed pair.

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-241` (branch `wk-IRPT_DASHBD-241`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~241/`. Never push; never commit the workspace `portal` gitlink. Client data lives ONLY under `C:/dev/_irpt_private_evidence_20261009/`: counts, dates, hashes and words only in the repo, a row, a commit message or your report. **Before every commit, scan what you stage for a client figure and for long identifier runs; the commit gate's client-data list is absent on this box, so that scan is yours.** **Commit order: the artifact first, then the proof instance, then the status flip to complete as the LAST commit; once the order is complete your grant ends.**

**Why.** In `infra/aws/terraform/investor-reporting/reporting-gold/`, the execution role's policy statement `ListExactlyTheSixGoldPrefixes` (`iam.tf`) takes its `s3:prefix` patterns from `local.irpt_rg_gold_list_pattern` (`locals.tf`), and that local is built from the READ prefixes only. The filled report-values prefix, `local.irpt_rg_gold_filled_prefix`, is in the WRITE list (`irpt_rg_gold_write_arns`) but in no list pattern, so the stage's catch-up listing of its own newest landed partition is denied and the stage writes nothing. The fix is to list that one prefix. It adds no read grant (the stage lists the prefix, it does not read an existing filled partition) and changes no write grant.

**The cell (`DB-b-299`).**
1. **Read first, whole:** the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p167_gold_list_grant.py` (your three criteria; `check_diff` and `check_semantics` are the exact spec); `infra/aws/terraform/investor-reporting/reporting-gold/locals.tf` (the declarations around `irpt_rg_gold_read_prefixes`, `irpt_rg_gold_list_pattern`, `irpt_rg_gold_filled_prefix`, `irpt_rg_gold_write_arns`) and `iam.tf` (the statement; read only).
2. **The edit (ONE file, `infra/aws/terraform/investor-reporting/reporting-gold/locals.tf`, ONE expression).** The line `irpt_rg_gold_list_pattern    = [for p in local.irpt_rg_gold_read_prefixes : "${p}*"]` becomes `irpt_rg_gold_list_pattern    = [for p in concat(local.irpt_rg_gold_read_prefixes, [local.irpt_rg_gold_filled_prefix]) : "${p}*"]` (keep the existing spacing before the `=`). You may add comment lines (starting with `#`) above it naming this order and the row. Every other line of the file, and every other file of the root (`iam.tf`, `lambda.tf`, `main.tf`, `schedule.tf`), stays byte for byte. The statement's sid `ListExactlyTheSixGoldPrefixes` keeps its name (a renamed sid reads as a new statement). Write the file as bytes with LF line endings.
3. **Run the checks yourself before the record:** `python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p167_gold_list_grant.py" . DB167-1-AC1`, then AC2, then AC3.
4. **Record** `RD_GOLD_LIST_GRANT_FACTS_R149.json` in your folder with EXACTLY these fields: `file` ("infra/aws/terraform/investor-reporting/reporting-gold/locals.tf"); `expression_old` (the old right-hand side, character for character); `expression_new` (the new right-hand side, character for character); `read_list_changed` (false); `write_list_changed` (false); `words` (one paragraph, 80 to 1800 characters: what changed and why, and what is NOT proven: no plan was run, nothing was applied, and whether the stage then writes is read at the first scheduled fire after the apply).

<criterion id="DB167-1-AC1" cell_refs="DB-b-299"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p167_gold_list_grant.py" . DB167-1-AC1</invocation><expect>DB167-1-AC1 PASS</expect></criterion>
`DB167-1-AC1` -- `locals.tf` differs from the base in exactly the one list-pattern expression (plus added comment lines); `iam.tf`, `lambda.tf`, `main.tf` and `schedule.tf` are byte-identical. Base: FAIL.
<criterion id="DB167-1-AC2" cell_refs="DB-b-299"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p167_gold_list_grant.py" . DB167-1-AC2</invocation><expect>DB167-1-AC2 PASS</expect></criterion>
`DB167-1-AC2` -- the new list pattern is the earlier patterns in the same order and then the filled prefix; the read prefixes, the read arns and the write arns declarations are untouched (no read grant is added). Base: FAIL.
<criterion id="DB167-1-AC3" cell_refs="DB-b-299"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p167_gold_list_grant.py" . DB167-1-AC3</invocation><expect>DB167-1-AC3 PASS</expect></criterion>
`DB167-1-AC3` -- the facts record states the two expressions and that the read and write lists are unchanged, and the worker's commits change only `locals.tf`, the folder, the investigation file and task-order files. Base: FAIL.

<expected_criteria>DB167-1-AC1,DB167-1-AC2,DB167-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **Reads and writes.** Reads: repo files. No network, no AWS call, no Terraform command, no push. Writes: the one Terraform file of the grant and your private folder.
- **Client data.** None is involved.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If a checker clause is wrong rather than your edit, file a BLOCKING row naming the clause and stop on it.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W241-S<k>` (start at S1), with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write.

<paths>
infra/aws/terraform/investor-reporting/reporting-gold/locals.tf
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~241/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-299.gold-listing-grant-for-the-filled-prefix.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 160 (round 149, workstream GOLDLIST), cell `DB-b-299`.
<owned_cells>DB-b-299</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB167-1-AC1, DB167-1-AC2, DB167-1-AC3 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~241/IRPT_DASHBD.TO-DB-b-299.gold-listing-grant-for-the-filled-prefix.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB167-1-AC1,DB167-1-AC2,DB167-1-AC3` BEFORE the flip (the ids as ONE comma-joined argument); pin each artifact row to the commit that carried it (a PENDING-THIS-COMMIT pin that predates the instance commit makes it INVALID).
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the old and new expression in one line; what is NOT proven. Counts, paths and words only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: one Terraform expression in a branch; no plan, no apply, nothing deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: nothing is applied in this cell; the later pair's plan gate grades the one policy change (a list pattern on the function's own filled prefix, no read, no write); the checker proves the read and write lists are untouched.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criteria FAIL at base and the diff and semantics clauses are exercised by the checker's self-test (7 red arms) and were run by the issuer on the real locals.tf with the reference edit (green).
lane: the <paths> block IS the grant.
</preflight>
