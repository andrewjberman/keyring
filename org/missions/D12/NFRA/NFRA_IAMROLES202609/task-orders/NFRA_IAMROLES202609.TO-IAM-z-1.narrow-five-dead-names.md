# NFRA_IAMROLES202609.TO-IAM-z-1 -- NARROW five dead global bucket names off six roles, resource grain, write-bearing first (round-8 analysis E1)

<!-- ===================== WORKER FACE -- this is the WHOLE of the assignee's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_IAMROLES202609/decompositions/NFRA_IAMROLES202609_DECOMP_R9.md</decomp_doc>
<owned_cells>IAM-z-1</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~IR</issued_to>
<placeholders>NONE</placeholders>

## THE CELL, INLINED IN FULL (ROUND_ANALYSIS.round8.md @d14162158d, E1; your own sweep DEAD_BUCKET_SWEEP.md section 7)

```
IAM-z-1. ACT: remove, from every ALLOW statement that names them, the ARNs (bucket and bucket/*) of five S3 names that read
404 and carry no tombstone. Live grants at the cut (issuer's read, 18:4xZ):
  ajb-workflow          -> workspace-sync-lambda-role                                   (write)
  opal-data-portal-s3   -> workspace-sync-lambda-role                                   (write)
  opal-data-smartx-v2   -> infrastructure-ops-lambda-role, smartx-exporter-role-20251218220948293500000001,
                           smartx-ingestion-lambda-role                                 (write)
  opal-market-update    -> FredIngestionLambdaRole                                      (write)
  opal-data-smartx      -> smartx-exporter-role-20251218220948293500000001              (read only)
KEEP every other ARN, every action and every other statement. Where a statement's Resource list would become EMPTY, the
statement goes, and that is named in the survey. The x-2 / x-5 shape: per role a reference census, then only dead ARNs leave.

WHERE EACH IS DECLARED (Grep at the cut; confirm each):
  infrastructure-ops-lambda-role     infra/aws/terraform/shared-infra/iam_legacy.tf:43, S3InfraWrite at :74. shared-infra
                                     carries the never-applied restricted_breakglass adds, so -target is load-bearing.
  smartx-ingestion-lambda-role,      infra/aws/terraform/smartx-pipeline/iam.tf:21 and :116 (smartx-v2 at :52-53 and
  smartx-exporter-role-2025...       :152-153; smartx at :164-165).
  FredIngestionLambdaRole            infra/aws/terraform/fred-pipeline/iam.tf:10, console-created, a data reference at :63.
                                     The opal-market-update grant may be a console inline policy: then it is an IAM-API act.
  workspace-sync-lambda-role         no declaration found: an IAM-API act (put-role-policy with the narrowed document).

PHASE A -- read-only, no AWS write:
  1. REFERENCE CENSUS, per (role, name): references in the environment variables of every function or instance on the role
     and in its DEPLOYED code (package manifest or source map, never by filename). A positive control per role: one live
     bucket the role really uses must be found. Write
     org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.7.0_AE_CloudOps~IR/round9/narrow_dead/NARROW_DEAD_SURVEY.md
     with one line per (role, name), exactly:
       REFS: <role> <bucket>: env=<n> code=<n>
     A reference found is NOT a reason to keep the grant: it is a broken feature the grant hides. Narrow anyway, and file the
     reference as its own surprise row naming the function.
  2. Re-read each name live (s3api get-bucket-location -> NoSuchBucket, the error CODE). Save each as-live policy document
     to .../narrow_dead/ROLLBACK_<role>_<policy>.json.
  3. Per ACT (one per module, one per IAM-API role): in YOUR OWN worktree, edit the declaration; plan with -target on the
     changed policy addresses; record `PLAN: <module>: <targeted plan summary, verbatim>`, the per-attribute grade (only the
     dead ARNs leave) and the untargeted plan beside it. For an IAM-API act, record the before/after document diff instead.
     Grade the naming with `git diff --cached --no-renames`. Note in the survey that
     infra/aws/terraform/smartx-v2-bucket-lifecycle/main.tf:34 declares a lifecycle on the 404 opal-data-smartx-v2 (a row;
     not this cell's act). Commit the survey and rollback files only, never an edit.
  4. STOP. Report to 2.0.0_SA_COO~ZI. One pair per act: ledger/NEVER_WIDEN_ROUND9_Z-1_<ACT>_{COO,CTO}_HALF.md.

PHASE B -- per act, only on the issuer's GO after that act's two halves are SIGNED. Write-bearing names first,
opal-data-smartx last:
  5. Read .open_deploys/ for the module; open a NEVER-2 entry `iamroles-r9-narrow-dead-<act>`.
  6. Commit the edit on your worktree branch, `safe-apply` with -target on the signed addresses only, drain the same session;
     then the untargeted shared-tree plan reads 0 to destroy. An IAM-API act: put-role-policy with the signed document.
  7. Verify LIVE: each document differs from its rollback by exactly the signed ARNs. Read ONE real invocation or run of a
     function on each changed role after the change and confirm it succeeded. Record in .../narrow_dead/POST_APPLY.md, one
     line per act, exactly:
       POST-APPLY: <act>: verified
     Then close the entry.
```

## DEPENDENCIES

None. Its PHASE A runs together with IAM-z-2's and IAM-z-3's; PHASE B serializes with them on `.open_deploys/`.

## BOUNDS

```
ONLY the dead ARNs of the five names leave. Nothing is added; no trust, tag or role change; no bucket created.
-target in shared-infra (restricted_breakglass). safe-apply only (NEVER-9); each NEVER-2 entry opens first and closes last.
STANDING (Z-S40): your survey names its read time; each act re-reads its baseline before it applies.
G-21: no alert, monitor or schedule.  G-25: no Access Analyzer.
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
infra/aws/terraform/shared-infra/iam_legacy.tf
infra/aws/terraform/smartx-pipeline/iam.tf
infra/aws/terraform/fred-pipeline/iam.tf
org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.7.0_AE_CloudOps~IR/round9/narrow_dead/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D12/NFRA/NFRA_IAMROLES202609/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D12/NFRA/NFRA_IAMROLES202609/task-orders/NFRA_IAMROLES202609.TO-IAM-z-1.narrow-five-dead-names.md
</paths>

Surprise rows: id `NFRA_IAMROLES202609-Z-S<k>` (next free k), `"fabric": "site-z"`. Commit through `.tools/safe-commit.sh` under
your own author line. At the end, flip this order's LAST `<status>` to `complete` with a proof instance in your deliverables
directory (`to_id` NFRA_IAMROLES202609.TO-IAM-z-1).

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="IAM-z-1"><invocation>bash -c "f=org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.7.0_AE_CloudOps~IR/round9/narrow_dead/NARROW_DEAD_SURVEY.md; test -f \$f || { echo MISSING:\$f; exit 2; }; echo refs=\$(grep -c -E '^REFS: [A-Za-z0-9_.-]+ [a-z0-9.-]+: env=[0-9]+ code=[0-9]+\$' \$f)"</invocation><expect>`refs=7` -- one reference count per (role, name) pair: 2 + 3 + 1 + 1</expect></criterion>
  <criterion id="AC2" cell_refs="IAM-z-1"><invocation>bash -c ".tools/aws iam get-account-authorization-details --output json > /c/tmp/z1_auth.json && python 'org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/2.0.0_SA_COO~ZI/checks/round9/allow_names.py' /c/tmp/z1_auth.json ajb-workflow opal-data-portal-s3 opal-data-smartx-v2 opal-market-update opal-data-smartx opal-data-portal-v2"</invocation><expect>each of the five dead names `=0`, and `opal-data-portal-v2=` 30 or more beside a `DENOMINATOR:` line (a failed read exits 2 and prints ERROR, never a zero)</expect></criterion>
  <criterion id="AC3" cell_refs="IAM-z-1"><invocation>bash -c "echo open=\$(ls -a org/critical_paths/.open_deploys/ | grep -c 'iamroles-r9-narrow-dead') closed=\$(grep -l '^\*\*Status:\*\* CLOSED' org/critical_paths/change_management/*iamroles-r9-narrow-dead* 2>&1 | grep -c '\.md\$')"</invocation><expect>`open=0` and `closed=` the number of acts in the survey -- every NEVER-2 entry's own Status line reads CLOSED</expect></criterion>
  <criterion id="AC4" cell_refs="IAM-z-1" judgment="true"/>
</proof_of_spec>

- **AC4** (JUDGMENT, never self-graded; UNVERIFIABLE-BY-INSTRUMENT, status_reason naming 3.0.0_SA_CVO~Z): did only the dead
  ARNs leave, with every reference found filed as a row, and did a real run on each changed role succeed afterwards?

Every invocation runs under `timeout 120`, except AC2, whose account-wide read takes up to 300 seconds.

<!-- ===================== RECORD FACE -- does NOT travel to the assignee ===================== -->

<status>pending</status>
<round>9</round>
<slot>0.7.0_AE_CloudOps~IR</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<issued_by>2.0.0_SA_COO~ZI</issued_by>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<to_id>NFRA_IAMROLES202609.TO-IAM-z-1</to_id>

**Issuer:** `2.0.0_SA_COO~ZI` (L5+L6, round 9) - **Project:** NFRA_IAMROLES202609 - **PRD:** v0.2 @3cadaf52ca (L4-R GRANDFATHERED per `prd-signoff.py status`)
**Authority chain:** round-8 slug (msg 33357, REMEDIATION_v8.Z.md @28b6af06ae) -> `ROUND_ANALYSIS.round8.md` @d14162158d E1 (msg 33361) -> L5 round-9 decomp -> this issuance.
**Risk WORLD:** permission narrowings on six production roles, two phases, each act under its own never-widen pair.
<preflight>
comp-schedule: RUN -- PARTIAL_OR_BLIND at the round-7 read (`python .tools/comp-schedule --budget 120`, rc=3); the assignee reads .open_deploys/ per module before each entry opens.
comp-iam: RUN -- live get-account-authorization-details at the cut through checks/round9/allow_names.py: principals=357 documents=652; the five names hold 7 (role, name) grants on the six roles above; control opal-data-portal-v2=38.
comp-adversary: RUN -- recut taken as GIVEN; denominator of re-derived premises 3 of 3 (each name 404 per the sweep; each grant live at the cut; -target load-bearing in shared-infra).
</preflight>

**Preflight disposition:** checks dry-run at the base: AC1 base FAIL as expected (`MISSING:` the survey); AC2 base FAIL as expected (ajb-workflow=1, opal-data-portal-s3=1, opal-data-smartx-v2=3, opal-market-update=1, opal-data-smartx=1; control 38); AC3 base FAIL as expected (`open=0 closed=0`).
