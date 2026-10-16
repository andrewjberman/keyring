# TO ADVI_COTBKF.TO-CB-dc-1.silver-account-attributes-apply -- round 106 CB-dc-1: apply the one-line ssm.tf change so the Cottonwood silver run merges account_attributes, under the signed never-widen pair, and prove the live document changed by exactly that line

<to_id>ADVI_COTBKF.TO-CB-dc-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.7.0_AE_CloudOps~FB1</issued_to>
<issued_by>2.0.0_SA_COO~C1</issued_by>
<issued_date>2026-10-16</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<proof_genre>DEPLOY</proof_genre>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>106</round>
<workstream>~C1</workstream>

**Directive:** D8 | **Fabric:** dell1 (placement DELL1) | **Decomp cell:** `CB-dc-1` (`decompositions/ADVI_COTBKF_DECOMP.round106.md`) |
**outcome_ref:** S59 (CTO msgs 6923, 6946, 6968) | **depends_on:** the signed pair (both halves)

---

## WORKER FACE

### THE CELL

Cottonwood's daily silver run is the SSM document `opal-cot-silver-run` (live version 4, hash `83b3fc89a34b4f2e4f286f6992e43242449cc3144b8e3174d4fe59b25675423e`), managed as `aws_ssm_document.cot_silver_run` in `infra/aws/terraform/cot-pipeline/ssm.tf`. It never runs `--table account_attributes`, so silver `account_attributes` has been stale since 2026-08-19. You apply ONE added line, from the patch file, through `safe-apply`, under a signed never-widen pair. The first scheduled fire (about 2026-10-17 midday) then writes the new silver partitions and, in the next gold run, moves four columns of the gold accounts dimension; **you do not dispatch the document, run the merge script, write to S3, or read the result of the fire. That fire is read later by the COO and the CVO.**

**Read first (the pair; both exist and are signed):**
1. COO half: `org/missions/D8/ADVI/ADVI_COTBKF/ledger/NEVER_WIDEN_R106_ACCOUNT_ATTRIBUTES_COO_HALF.md` @7a14b821b4. Confirm its sha256 begins `257283f50cac3197` with `git show 7a14b821b4:<path> | sha256sum`.
2. CTO half: `org/missions/D8/ADVI/ADVI_COTBKF/ledger/NEVER_WIDEN_R106_ACCOUNT_ATTRIBUTES_CTO_HALF.md` SIGNED (CTO msg 6968), with condition C-1 and "no early dispatch". Its conditions bind you as the COO half's section 5 does.

**The patch to apply (READ-ONLY input):** `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~195/SSM_ACCOUNT_ATTRIBUTES.patch` at the trunk (one added line, no removal; it applies to `ssm.tf` at HEAD). Record its sha256 in the ledger. You apply THIS patch, not a rewrite.

**Your items, in this order. Stop at the first that fails and change nothing you have not yet written.**
1. **Before any write.** Verify the pair (items 1 and 2 above). Open the change-management ledger entry with `deploy_ledger.py open` (it commits its own files); record the blast radius: one resource, `aws_ssm_document.cot_silver_run`, in place; the rollback is to set the document's default version back to 4 (`ssm update-document-default-version --name opal-cot-silver-run --document-version 4`) and then revert the line and reconcile Terraform, or revert the line and `safe-apply`.
2. **Re-read the world immediately before the apply and STOP if any differs from the COO half's section 1:** `ssm describe-document` reads `DocumentVersion` 4, `DefaultVersion` 4, `LatestVersion` 4 and hash `83b3fc89a34b4f2e4f286f6992e43242449cc3144b8e3174d4fe59b25675423e`; `head-object` of `silver/cot_incremental_manifest_account_attributes.json` in `opal-data-cot` reads VersionId `EJDw_ZHST0x7oLC_k34IoqWcC80hn6.w`; the keys under `silver/account_attributes/` number 1. Record each read in the ledger.
3. **Make the edit and plan it.** In the tree you apply from, apply the patch to `infra/aws/terraform/cot-pipeline/ssm.tf` (`git apply`), then run `.tools/terraform.exe -chdir=infra/aws/terraform/cot-pipeline plan -out=<planfile> -input=false`. The plan MUST read exactly one change, `aws_ssm_document.cot_silver_run` updated in place, `Plan: 0 to add, 1 to change, 0 to destroy`. Otherwise STOP, revert the edit, report, write nothing. (The issuer's plan on a copy read the same.)
4. **Apply the saved plan.** `.tools/safe-apply.sh -chdir=infra/aws/terraform/cot-pipeline apply <planfile>` (never a bare `terraform apply`). Commit the `ssm.tf` change with `.tools/safe-commit.sh` in your lane.
5. **Prove and close.** Run acceptance AC1 and AC2. Close the ledger with the read-back (document default version, hash, and the state check). If AC1 fails after the apply, roll back as in item 1, write the reason in the ledger and file a surprise row.

### ACCEPTANCE

<criterion id="CB106dc1-AC1" cell_refs="CB-dc-1"><invocation>python -I org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C1/dc1_apply_check.py doc</invocation><expect>^SILVER-DOC default_version=([5-9]|[1-9][0-9]) prior_version=4 added=1 removed=0 added_is_account_attributes=True nongating=True after_holdings=True$</expect></criterion>
`CB106dc1-AC1` -- the live default version of `opal-cot-silver-run` differs from version 4 by exactly one added line: the non-gating `account_attributes` step, immediately after the holdings step, with nothing removed. (The issuer's script reads the document only; read it, do not edit it.)

<criterion id="CB106dc1-AC2" cell_refs="CB-dc-1"><invocation>python -I org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C1/dc1_apply_check.py state</invocation><expect>^SILVER-STATE manifest_unchanged=True partitions=1 existing_partition_unchanged=True$</expect></criterion>
`CB106dc1-AC2` -- the apply wrote nothing to S3: the account_attributes manifest and the 2026-08-19 partition are the versions the COO half records, and the prefix still holds one key. (This holds only before the first scheduled fire, about 2026-10-17 midday; if you finish after it, say so, and the COO reads the fire instead.)

<expected_criteria>CB106dc1-AC1,CB106dc1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The one Terraform change above, applied through `.tools/safe-apply.sh` from a saved plan; read-only `describe-document`, `get-document`, `list-document-versions`, `head-object`, `list-objects-v2`; the SSM `update-document-default-version` ONLY as the rollback of item 1. Repo: `infra/aws/terraform/cot-pipeline/ssm.tf` (the patch only), the change-management ledger files for this deploy, the surprise channel row, and this order's file.
- **Pair first.** No write before items 1 to 3 pass.
- **No account number, advisor, client, portfolio-group name or dollar value** in a ledger entry, a record, a row or a message: counts, hashes, VersionIds and versions only.
- **NEVER** a bare `terraform apply`, `aws ssm send-command` or `start-automation`, a dispatch of the silver document, a run of `cot_silver_merge.py`, a write to `opal-data-cot`, a delete of any object or version, a change to any other resource or module, a push without the gate, or `--force`.
- **Refusal clause.** If a criterion cannot be met as written, stop. Roll back as in item 1 if you wrote, write the reason in the ledger, and file a NEW surprise row (id `ADVI_COTBKF-D1-WFB1-S<k>`, `"fabric": "dell1"`), APPENDED to the channel with `open(path, 'ab')` writing LF bytes only. Do not weaken the test.

<paths>
infra/aws/terraform/cot-pipeline/ssm.tf
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D8/ADVI/ADVI_COTBKF/task-orders/ADVI_COTBKF.TO-CB-dc-1.silver-account-attributes-apply.md
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.7.0_AE_CloudOps~FB1/
</paths>

The block is your repo WRITE grant. The AWS grant is the one resource above.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round106.md</decomp_doc> (round 106), cell `CB-dc-1`.
<owned_cells>CB-dc-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB106dc1-AC1, CB106dc1-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.7.0_AE_CloudOps~FB1/ADVI_COTBKF.TO-CB-dc-1.silver-account-attributes-apply.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB106dc1-AC1,CB106dc1-AC2` BEFORE the flip. Both are mechanical. The `output_evidence` of each criterion must equal its `expect` pattern exactly. **YOU flip your own order `<status>` to `complete` in the commit that carries the proof instance, and only when both PASS.**
</proof_of_spec>

**REPORT:** the pair files and the COO half's hash read; the patch hash; the pre-apply reads (document version, hash, manifest VersionId, partition count); the ledger entry; the plan's summary line; the apply line; the new document version and hash; the two criterion lines; commits and their push state (measured); every refusal and denial verbatim. No account number or value.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE the order changes the content of an existing SSM document; no schedule or trigger is created or changed. The organic fire (cot-bronze-complete to cot-silver-run) is the existing one.
comp-iam: RUN at apply time -- the applier identity's ssm:UpdateDocument and ssm:UpdateDocumentDefaultVersion on the one document (the cot-pipeline root already manages it); BLIND: none beyond the one resource.
comp-adversary: RUN -- pair before write; the world re-read and recorded; the plan must read exactly one in-place change; the saved plan is what is applied; AC1 compares the live default version with version 4 (the issuer's script was run on its own synthetic good, gating, misplaced and removal edits of version 4: only the good edit reads added=1 removed=0 added_is_account_attributes=True nongating=True after_holdings=True); AC2 checks the apply wrote nothing to S3. BLIND: the document's behaviour on the data (whether the new step runs clean on 45 workbooks, and what gold then builds) is read at the first fire by the COO and the CVO, not here; a rollback of the default version leaves Terraform state ahead of the live document until reconciled.
lane: SERVED write by the macro CloudOps lane; the issuer signed the COO half; the CTO signed his with C-1.
</preflight>

**ISSUER NOTES:** Source: CTO msg 6968 (CTO half signed; "ask MSTR~DELL1 to seat the ADVI lane"). Mechanical checks dry-run at the base: AC1 reads `default_version=4 ... added=0` (FAIL as expected, nothing applied); AC2 reads `manifest_unchanged=True partitions=1 existing_partition_unchanged=True` (PASS today, by design: it guards that the apply wrote nothing; it stays a pass only until the first scheduled fire).
