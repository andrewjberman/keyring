# NFRA_IAMROLES202609.TO-IAM-x-5 -- NARROW opal-portal-lambda-role's opal-portal-s3-read: six non-existent buckets leave a WRITE+DELETE statement (row Z-S39, E5)

<!-- ===================== WORKER FACE -- this is the WHOLE of the assignee's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_IAMROLES202609/decompositions/NFRA_IAMROLES202609_DECOMP_R7.md</decomp_doc>
<owned_cells>IAM-x-5</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~IR</issued_to>
<placeholders>NONE</placeholders>

## THE CELL, INLINED IN FULL (round-6 analysis Addendum 3, item E5 -- MOST URGENT of round 7)

```
IAM-x-5. ACT: under ROUND_ANALYSIS.round6.md Addendum 3 (1.0.0_SA_CTO~Z @85cbea7549), remove from opal-portal-lambda-role's
inline policy `opal-portal-s3-read`, Sid `S3ReadWrite` (s3:GetObject, PutObject, DeleteObject, ListBucket), the 12 ARNs
(bucket + /*) of the six buckets read 404 by the CTO: opal-data-smartx, opal-data-smartx-v2, opal-portal-data,
opal-data-portal-s3, opal-market-data-v2, opal-data-aaii-sentiment. KEEP opal-data-portal-v2 and opal-data-news-v2 and all
four actions. WHY: the role runs 12 Lambda functions; whoever creates one of those global bucket names receives WRITE and
DELETE from a production role, and a Lambda still addressing it would write Opal data into their bucket.

THE POLICY IS DECLARED IN TERRAFORM: infra/aws/terraform/shared-infra/opal-portal-lambda-role.tf (the
aws_iam_role_policy with name = "opal-portal-s3-read", ~line 388; NFRA_TERRAFORM-P2's adoption, PHASE 2). The narrowing is
an edit of that declaration's Resource list, applied with -target on that one address. shared-infra also carries
ADVI_COTBKF's never-applied restricted_breakglass pair: an untargeted apply would CREATE them, so -target is load-bearing.

PHASE A -- read-only, no AWS write:
  1. REFERENCE CENSUS, per name: count references in the 12 functions' environment variables (get-function-configuration)
     and in their DEPLOYED code, read from the package manifest or source map, never by filename. A positive control,
     opal-data-portal-v2, must be found. Write
     org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.7.0_AE_CloudOps~IR/round7/portal_s3/PORTAL_S3_SURVEY.md
     with one line per dead name, exactly:
       REFS: <bucket>: env=<n> code=<n>
     and exactly:
       CONTROL: opal-data-portal-v2: env=<n> code=<n>
     A reference found is NOT a reason to keep the grant: it is a broken feature the grant hides. Narrow anyway, and file
     the reference as its own row naming the function.
  2. Re-read each of the six names live (s3api get-bucket-location -> NoSuchBucket; the error CODE, not an HTTP status),
     and save the as-live policy document from get-role-policy to .../portal_s3/ROLLBACK_opal-portal-s3-read.json.
  3. In YOUR OWN worktree, edit the declaration (drop exactly the 12 ARNs). Plan with
     -target=<that aws_iam_role_policy address>, and record:
       PLAN: shared-infra: <the targeted plan summary, verbatim>
     plus the per-attribute grade (one policy attribute changes, losing exactly the 12 ARNs) and the untargeted plan beside
     it (its restricted_breakglass adds unchanged). Grade the naming on the .tf with `git diff --cached --no-renames`.
     Commit the survey and the rollback file only, never the edit.
  4. STOP. Report to 2.0.0_SA_COO~ZI. The pair ledger/NEVER_WIDEN_ROUND7_X-5_{COO,CTO}_HALF.md is written against your survey.

PHASE B -- only on the issuer's GO, after both halves are SIGNED:
  5. Read .open_deploys/ for shared-infra; open a NEVER-2 entry `iamroles-r7-narrow-portal-s3`.
  6. Commit the edit on your worktree branch, then `safe-apply` with -target on that one address only, then drain the same
     session. After the drain, record the untargeted shared-tree plan: 0 to destroy, the breakglass adds unchanged.
  7. Record in .../portal_s3/POST_APPLY_portal_s3.md, exactly:
       POST-APPLY-PLAN: shared-infra: 0 to add, 0 to change, 0 to destroy
     Verify LIVE: the policy document differs from the rollback by exactly the 12 removed ARNs. Then read ONE real
     invocation of a portal function on this role AFTER the change and confirm it succeeded (the CTO's condition).
     Then close the entry.
```

## DEPENDENCIES

None. A separate workstream of round 7 (DECOMP_R7 section 9), MOST URGENT: take it before IAM-x-3 and IAM-x-4. In
shared-infra it serializes with IAM-x-1 row 6 on `.open_deploys/`.

## BOUNDS

```
ONLY the 12 dead ARNs leave; the two live buckets, all four actions, every other statement and every other policy of the
role stay byte-identical. Nothing is added; no trust, no tag, no role change.
-target ONLY in shared-infra (restricted_breakglass). safe-apply only (NEVER-9); the NEVER-2 entry opens first and closes last.
G-21: no alert, monitor or schedule.  G-25: no Access Analyzer.
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
infra/aws/terraform/shared-infra/opal-portal-lambda-role.tf
org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.7.0_AE_CloudOps~IR/round7/portal_s3/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D12/NFRA/NFRA_IAMROLES202609/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D12/NFRA/NFRA_IAMROLES202609/task-orders/NFRA_IAMROLES202609.TO-IAM-x-5.narrow-portal-s3-read.md
</paths>

Surprise rows: id `NFRA_IAMROLES202609-Z-S<k>` (next free k), `"fabric": "site-z"`. Commit through `.tools/safe-commit.sh` under
your own author line. At the end, flip this order's LAST `<status>` to `complete` with a proof instance in your deliverables
directory (`to_id` NFRA_IAMROLES202609.TO-IAM-x-5).

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="IAM-x-5"><invocation>bash -c "f=org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.7.0_AE_CloudOps~IR/round7/portal_s3/PORTAL_S3_SURVEY.md; test -f \$f || { echo MISSING:\$f; exit 2; }; echo refs=\$(grep -c -E '^REFS: [a-z0-9-]+: env=[0-9]+ code=[0-9]+\$' \$f) control=\$(grep -c -E '^CONTROL: opal-data-portal-v2: env=[0-9]+ code=[0-9]+\$' \$f)"</invocation><expect>`refs=6 control=1` -- a reference count for each of the six names, beside the positive control</expect></criterion>
  <criterion id="AC2" cell_refs="IAM-x-5"><invocation>bash -c ".tools/aws iam get-role-policy --role-name opal-portal-lambda-role --policy-name opal-portal-s3-read --output json > /c/tmp/x5_live.json; echo dead=\$(grep -c -E 'opal-data-smartx|opal-portal-data|opal-data-portal-s3|opal-market-data-v2|opal-data-aaii-sentiment' /c/tmp/x5_live.json) live=\$(grep -c -E 'opal-data-portal-v2|opal-data-news-v2' /c/tmp/x5_live.json)"</invocation><expect>`dead=0` and `live=` 2 or more -- the six names are gone from the live policy and the two live buckets remain (a read that failed would show live=0)</expect></criterion>
  <criterion id="AC3" cell_refs="IAM-x-5"><invocation>bash -c "echo open=\$(ls -a org/critical_paths/.open_deploys/ | grep -c 'iamroles-r7-narrow-portal-s3') closed=\$(grep -l '^\*\*Status:\*\* CLOSED' org/critical_paths/change_management/*iamroles-r7-narrow-portal-s3* 2>&1 | grep -c '\.md\$')"</invocation><expect>`open=0` and `closed=1` -- the NEVER-2 entry's own Status line reads CLOSED</expect></criterion>
  <criterion id="AC4" cell_refs="IAM-x-5" judgment="true"/>
</proof_of_spec>

- **AC4** (JUDGMENT, never self-graded; UNVERIFIABLE-BY-INSTRUMENT, status_reason naming 3.0.0_SA_CVO~Z): did exactly the 12
  dead ARNs leave, with every reference found filed as a row, and did a real portal invocation succeed after the change?

Every invocation runs under `timeout 120`.

<!-- ===================== RECORD FACE -- does NOT travel to the assignee ===================== -->

<status>pending</status>
<round>7</round>
<workstream>PORTAL_S3</workstream>
<slot>0.7.0_AE_CloudOps~IR</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<issued_by>2.0.0_SA_COO~ZI</issued_by>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<to_id>NFRA_IAMROLES202609.TO-IAM-x-5</to_id>

**Issuer:** `2.0.0_SA_COO~ZI` (L5+L6, round 7, Addendum 3) - **Project:** NFRA_IAMROLES202609 - **PRD:** v0.2 @3cadaf52ca (L4-R GRANDFATHERED per `prd-signoff.py status`)
**Authority chain:** row Z-S39 (0.7.0_AE_CloudOps~IR) -> `ROUND_ANALYSIS.round6.md` Addendum 3 @85cbea7549 (E5; msg 33246) -> DECOMP_R7 section 9 -> this issuance.
**Risk WORLD:** a permission narrowing on a production role behind 12 Lambda functions, two phases, PHASE B under its own never-widen pair.
<preflight>
comp-schedule: RUN -- `python .tools/comp-schedule --budget 120` at the round-7 cut: BUDGET REACHED, 1 of 6 carriers, C2 PARTIAL, rc=3; PARTIAL_OR_BLIND; the assignee reads .open_deploys/ for shared-infra before its entry opens.
comp-iam: RUN -- `bash .tools/comp-iam stats`: 219 IAM roles parsed; Grep of infra/aws/terraform/*.tf: opal-portal-s3-read declared at shared-infra/opal-portal-lambda-role.tf:388; the issuer's 07:1xZ shared-infra plan showed no change on it (declaration == live), only the restricted_breakglass adds.
comp-adversary: RUN -- recut taken as GIVEN; denominator of re-derived premises 3 of 3 (the six names 404 per the CTO's live read; the declaration matches live; -target load-bearing in shared-infra).
</preflight>

**Preflight disposition:** checks dry-run at the base: AC1 base FAIL as expected (`MISSING:` the survey); AC2 base FAIL as expected (dead > 0 while the grant stands); AC3 base FAIL as expected (`open=0 closed=0`).
