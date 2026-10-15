# TO IRPT_DASHBD.TO-DB-b-261 -- the Cottonwood landing root's SCHEDULER POLICY gets its own BUILDER NAME (round 129, workstream B-49F): one `opal_name` module (kind policy, qualifier scheduler) and the policy's `name` pointing at it, because the naming-plan gate refused the apply

<to_id>IRPT_DASHBD.TO-DB-b-261</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~213</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>129</round>
<workstream>B-49F</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** B-49F, round 129 | **Ordered by:** the issuer, repairing its own round-123 order `DB-b-252` under the AE applier's STOP on TO-DB-b-260 (msg 8351) and the CTO ROUND-126 ANALYSIS (B-49F) @2cf3e13682 ruling 1 | **Decomp cell:** `DB-b-261` (decomposition section 127).

**Risk class WORLD** is the floor of the path below (an `infra/` path): this order edits one Terraform file and runs no Terraform command, no AWS write and no upload.

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-213` (branch `wk-IRPT_DASHBD-213`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~213/`. Never push; never commit the workspace `portal` gitlink. Client data lives ONLY under `C:/dev/_irpt_private_evidence_20261009/`: counts, dates, hashes and words only in the repo, a row, a commit message or your report; never a household or account id or a client value (a public security identifier with a count of accounts is not a client value). Your private output folder is `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~213/` (create it if absent). **A commit message, a row, a record or a report that quotes a client figure is a defect even if it is later removed: your branch is merged whole, history included. Before every commit, scan what you stage for a client figure and for long identifier runs.** The commit gate's client-data list is absent on this box, so that scan is yours. **Commit order: the artifacts first, then the proof instance, then the status flip to complete as the LAST commit; once the order is complete your grant ends, so do every edit before the flip.**

**Why.** The AE applier's `safe-apply` of the signed Cottonwood landing pair was REFUSED by the naming-plan gate (rc 7, nothing written): `aws_iam_role_policy.irpt_account_return_daily_scheduler` in `infra/aws/terraform/investor-reporting/account-return-daily/iam.tf` (line 152) takes its `name` from the scheduler ROLE's name module, so the policy is named `irpt-cot-account-return-daily-scheduler-role`, a role name on a policy. The builder's policy name for that role is `irpt-cot-account-return-daily-scheduler-policy` (`lib/opal_naming.py name()`, kind `policy`, qualifier `scheduler`); the execution policy already uses its own policy-name module and is CONFORMANT. This order gives the scheduler policy its own builder name and changes nothing else.

**The cell (`DB-b-261`).**
1. **Read first, whole:** the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r129/p129_iam.py` (your three criteria; every clause and the record's exact form are in it); `infra/aws/terraform/investor-reporting/account-return-daily/iam.tf` (the file you edit; see the execution policy's name module for the form).
2. **The edit, `iam.tf` only.** Add ONE module block `module "irpt_account_return_daily_scheduler_policy_name"` in the form of its siblings: `source = "../../modules/opal_name"`, `system = "irpt"`, `scope = local.irpt_arc_firm` (the same local the scheduler role's module uses; never a typed firm), `function = "account-return-daily"`, `kind = "policy"`, `qualifier = "scheduler"` (aligned as `terraform fmt` aligns). Change ONLY the `name` attribute of `resource "aws_iam_role_policy" "irpt_account_return_daily_scheduler"` to `module.irpt_account_return_daily_scheduler_policy_name.name`. The scheduler ROLE keeps `module.irpt_account_return_daily_scheduler_role_name.name`. A short comment above the new module may say why. NOTHING else in code changes; every other root file stays byte for byte.
3. **Record** `RD_COT_NAMES_FACTS_R129.json` in your folder with EXACTLY these fields: `names` (the six builder names, in this order: the function, the execution role, the execution policy, the scheduler policy, the scheduler role, the schedule); `scheduler_policy` ("irpt-cot-account-return-daily-scheduler-policy"); `gate_verdict` (the naming gate's own LAST output line as the checker reads it: run `python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r129/p129_iam.py" . DB129-1-AC2` and copy the final line that its OK message quotes in parentheses, or run `python .tools/naming-apply-gate.py --plan-json <a plan document holding the six names> --root infra/aws/terraform/investor-reporting/account-return-daily` and copy its last line); `words` (one paragraph, 80 to 1500 characters: what was wrong, what you changed, what is NOT proven: no plan, no apply).

<criterion id="DB129-1-AC1" cell_refs="DB-b-261"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r129/p129_iam.py" . DB129-1-AC1</invocation><expect>DB129-1-AC1 PASS</expect></criterion>
`DB129-1-AC1` -- against the order's first commit, `iam.tf` gains exactly the module of step 2 (opal_name, irpt, account-return-daily, policy, scheduler, scope from the same local as the role's module) and the scheduler policy's `name` points at it; the role keeps its own module; no other code line moves (comments excluded, spacing normalised); every other root file is byte-equal to the base.
<criterion id="DB129-1-AC2" cell_refs="DB-b-261"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r129/p129_iam.py" . DB129-1-AC2</invocation><expect>DB129-1-AC2 PASS</expect></criterion>
`DB129-1-AC2` -- the checker builds the six names from the root's own module arguments with `lib/opal_naming.py`, writes a synthetic plan document holding the six resources with those names, and runs the REAL `.tools/naming-apply-gate.py` in plan mode on it: six CONFORMANT lines, no REFUSE.
<criterion id="DB129-1-AC3" cell_refs="DB-b-261"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r129/p129_iam.py" . DB129-1-AC3</invocation><expect>DB129-1-AC3 PASS</expect></criterion>
`DB129-1-AC3` -- the record has exactly the form of step 3, its six names equal the checker's recount, and its `gate_verdict` equals the gate's last line as the checker reads it.

<expected_criteria>DB129-1-AC1,DB129-1-AC2,DB129-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited: the other root files, the handler, the adapter, the source map, the registry, the naming gate, the issuer's check files and the portal.
- **Reads and writes.** Reads: repo files and `lib/opal_naming.py`. Writes: the repo files of the grant and your private folder. No Terraform command, no AWS call, no upload, no push.
- **Client data.** None is involved.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If the gate still refuses a name after your edit, record the refusal line verbatim, file a BLOCKING row and stop.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W213-S<k>` (start at S1), with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write; every `.py` passes ruff (target py39, no semicolon-joined statements).

<paths>
infra/aws/terraform/investor-reporting/account-return-daily/iam.tf
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~213/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-261.cottonwood-landing-root-scheduler-policy-builder-name.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 127 (round 129, workstream B-49F), cell `DB-b-261`.
<owned_cells>DB-b-261</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB129-1-AC1, DB129-1-AC2, DB129-1-AC3 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~213/IRPT_DASHBD.TO-DB-b-261.cottonwood-landing-root-scheduler-policy-builder-name.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB129-1-AC1,DB129-1-AC2,DB129-1-AC3` BEFORE the flip (the ids as ONE comma-joined argument); pin each artifact row to the commit that carried it (a PENDING-THIS-COMMIT pin that predates the instance commit makes it INVALID).
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the lines you changed; the gate's verdict line; what is NOT proven. Counts, paths and words only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: one Terraform file edited in a branch; nothing is planned, applied, uploaded, scheduled or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no grant is changed in AWS; no AWS write and no grant changes: only the policy's name attribute moves, its document is untouched.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criteria FAIL at base and the checker's clauses are exercised by its self-test (green and red arms); its HCL, gate-output and facts clauses were exercised by its self-test (green and red arms), its gate clause reproduced the applier's refusal on the role-named policy and passes on the builder-named one, and all three FAIL at the base.
lane: the <paths> block IS the grant.
</preflight>
