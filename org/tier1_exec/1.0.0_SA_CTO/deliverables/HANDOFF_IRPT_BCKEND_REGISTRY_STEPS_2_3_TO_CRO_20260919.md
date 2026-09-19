# HANDOFF -- `IRPT_BCKEND` steps 2-3: the registry edit `1.0.0_SA_CTO` MAY NOT COMMIT

**Seat:** `1.0.0_SA_CTO`. **Date:** 2026-09-19 ~01:5xZ. **For:** `4.0.0_SA_CRO` (the lane's only permitted writer).

## WHY THIS IS A HANDOFF AND NOT A COMMIT

`safe-commit` REFUSED: `infra/logic/registry/scopes.json -- lane=PLATFORM_LOGIC_DOCS ... agent=1.0.0_SA_CTO not in permitted_agents`.
The lane names this seat by EXCLUSION, with its reason: *"NOT `1.0.0_SA_CTO` -- it gave the arch input and
explicitly did not ask for write access, and a grant nobody requested is a widening."* The refusal is CORRECT.

⛔ **AND NO OVERRIDE IS TAKEN.** That same lane's doctrine forbids it: *"a repeat override for a STANDING
role-authorized action = a coverage gap to close"* and *"Andrew ruled ENUMERATE over bless-the-override"*.
Taking `GIT_COMMIT_AUTHOR_OVERRIDE` here would convert a singular audited escape into a de-facto lane, which is
the exact failure that lane text was written to prevent.

## ⛔ THE EDIT IS ATOMIC BY REQUIREMENT -- BOTH FILES IN ONE COMMIT

`infra/aws/terraform/shared-infra/s3-lgic-firm-buckets.tf:97-100` at HEAD selects
`lookup(s,"bucket_managed_by","") == "s3-lgic-firm-buckets.tf"` **OR** `(field absent AND bucket_provisioned == false)`,
and its own comment at `:88-89` states the constraint. **Flip without the field -> both rows fall out of BOTH
branches -> the measured 10-resource DESTROY. Exemption rows without the flip -> the naming gate refuses them.**

## PART 1 -- `infra/logic/registry/scopes.json` (4 insertions / 2 deletions)

```diff
diff --git a/infra/logic/registry/scopes.json b/infra/logic/registry/scopes.json
index 2267a8cd39..daa145d6a7 100644
--- a/infra/logic/registry/scopes.json
+++ b/infra/logic/registry/scopes.json
@@ -123,7 +123,8 @@
       "short": "inf",
       "tenancy": "FIRM",
       "bucket": "opal-data-inflection",
-      "bucket_provisioned": false,
+      "bucket_provisioned": true,
+      "bucket_managed_by": "s3-lgic-firm-buckets.tf",
       "monolith_scopes": {"orion": ["inflection"], "eclipse": ["inflection"]},
       "tenant": {
         "display_name": "Inflection Wealth Management",
@@ -161,7 +162,8 @@
       "short": "cot",
       "tenancy": "FIRM",
       "bucket": "opal-data-cottonwood",
-      "bucket_provisioned": false,
+      "bucket_provisioned": true,
+      "bucket_managed_by": "s3-lgic-firm-buckets.tf",
       "monolith_scopes": {"blackdiamond": ["cottonwood"]},
       "pipeline_trees": [
         {
```

## PART 2 -- `infra/logic/registry/exemptions.json`: two new keys, three rows each (40 insertions / 0 deletions)

Insert after the `"opal-data-cot": [],` line. ⛔ **NOT a mirror of `opal-data-49financial`'s 16-principal admit
set** -- 13 of those are service roles derived from a census of THAT bucket's existing principals, and copying an
enumeration across a firm boundary is how a cross-firm fence widens silently. Operator identities only.

```json
{
    "opal-data-inflection": [
        {
            "principal": "Andrew_Berman",
            "arn": "arn:aws:iam::313476888478:user/Andrew_Berman",
            "reason": "Operator identity of opal-data-inflection, the bucket this root creates. NOT a census row: opal-data-inflection is NEW and EMPTY with NO existing principals, so the 'Existing principal (FENCE_WRITER_CENSUS.md, granted)' ground the opal-data-49financial rows carry DOES NOT APPLY and is deliberately not reproduced. Scope token: none (IAM_USER: NOT GRADED), so the scope-derived DenyForeignFirmPrincipals matches and denies it. MEASURED CONSEQUENCE OF ITS ABSENCE: the fence applied with an empty exemption list denied EVERY identity this estate holds, including the applying identity -- head-bucket, get-bucket-policy, get-bucket-versioning and delete-bucket-policy all AccessDenied post-apply (IRPT_BCKEND row W3-S43). This row admits the operator and nothing else.",
            "signoff_ref": "org/critical_paths/change_management/20260918T1949Z_irpt-bckend-ib-rte-3-lgic-firm-buckets_deploy_completion.md -- the ledger entry IB-rte-3 opened before the apply and left OPEN/RED; unsigned at this write"
        },
        {
            "principal": "Andrew_Berman_Console",
            "arn": "arn:aws:iam::313476888478:user/Andrew_Berman_Console",
            "reason": "Operator identity of opal-data-inflection, the bucket this root creates. NOT a census row: opal-data-inflection is NEW and EMPTY with NO existing principals, so the 'Existing principal (FENCE_WRITER_CENSUS.md, granted)' ground the opal-data-49financial rows carry DOES NOT APPLY and is deliberately not reproduced. Scope token: none (IAM_USER: NOT GRADED), so the scope-derived DenyForeignFirmPrincipals matches and denies it. MEASURED CONSEQUENCE OF ITS ABSENCE: the fence applied with an empty exemption list denied EVERY identity this estate holds, including the applying identity -- head-bucket, get-bucket-policy, get-bucket-versioning and delete-bucket-policy all AccessDenied post-apply (IRPT_BCKEND row W3-S43). This row admits the operator and nothing else.",
            "signoff_ref": "org/critical_paths/change_management/20260918T1949Z_irpt-bckend-ib-rte-3-lgic-firm-buckets_deploy_completion.md -- the ledger entry IB-rte-3 opened before the apply and left OPEN/RED; unsigned at this write"
        },
        {
            "principal": "Opal_Terminal",
            "arn": "arn:aws:iam::313476888478:user/Opal_Terminal",
            "reason": "Operator identity of opal-data-inflection, the bucket this root creates. NOT a census row: opal-data-inflection is NEW and EMPTY with NO existing principals, so the 'Existing principal (FENCE_WRITER_CENSUS.md, granted)' ground the opal-data-49financial rows carry DOES NOT APPLY and is deliberately not reproduced. Scope token: none (IAM_USER: NOT GRADED), so the scope-derived DenyForeignFirmPrincipals matches and denies it. MEASURED CONSEQUENCE OF ITS ABSENCE: the fence applied with an empty exemption list denied EVERY identity this estate holds, including the applying identity -- head-bucket, get-bucket-policy, get-bucket-versioning and delete-bucket-policy all AccessDenied post-apply (IRPT_BCKEND row W3-S43). This row admits the operator and nothing else.",
            "signoff_ref": "org/critical_paths/change_management/20260918T1949Z_irpt-bckend-ib-rte-3-lgic-firm-buckets_deploy_completion.md -- the ledger entry IB-rte-3 opened before the apply and left OPEN/RED; unsigned at this write"
        }
    ],
    "opal-data-cottonwood": [
        {
            "principal": "Andrew_Berman",
            "arn": "arn:aws:iam::313476888478:user/Andrew_Berman",
            "reason": "Operator identity of opal-data-cottonwood, the bucket this root creates. NOT a census row: opal-data-cottonwood is NEW and EMPTY with NO existing principals, so the 'Existing principal (FENCE_WRITER_CENSUS.md, granted)' ground the opal-data-49financial rows carry DOES NOT APPLY and is deliberately not reproduced. Scope token: none (IAM_USER: NOT GRADED), so the scope-derived DenyForeignFirmPrincipals matches and denies it. MEASURED CONSEQUENCE OF ITS ABSENCE: the fence applied with an empty exemption list denied EVERY identity this estate holds, including the applying identity -- head-bucket, get-bucket-policy, get-bucket-versioning and delete-bucket-policy all AccessDenied post-apply (IRPT_BCKEND row W3-S43). This row admits the operator and nothing else.",
            "signoff_ref": "org/critical_paths/change_management/20260918T1949Z_irpt-bckend-ib-rte-3-lgic-firm-buckets_deploy_completion.md -- the ledger entry IB-rte-3 opened before the apply and left OPEN/RED; unsigned at this write"
        },
        {
            "principal": "Andrew_Berman_Console",
            "arn": "arn:aws:iam::313476888478:user/Andrew_Berman_Console",
            "reason": "Operator identity of opal-data-cottonwood, the bucket this root creates. NOT a census row: opal-data-cottonwood is NEW and EMPTY with NO existing principals, so the 'Existing principal (FENCE_WRITER_CENSUS.md, granted)' ground the opal-data-49financial rows carry DOES NOT APPLY and is deliberately not reproduced. Scope token: none (IAM_USER: NOT GRADED), so the scope-derived DenyForeignFirmPrincipals matches and denies it. MEASURED CONSEQUENCE OF ITS ABSENCE: the fence applied with an empty exemption list denied EVERY identity this estate holds, including the applying identity -- head-bucket, get-bucket-policy, get-bucket-versioning and delete-bucket-policy all AccessDenied post-apply (IRPT_BCKEND row W3-S43). This row admits the operator and nothing else.",
            "signoff_ref": "org/critical_paths/change_management/20260918T1949Z_irpt-bckend-ib-rte-3-lgic-firm-buckets_deploy_completion.md -- the ledger entry IB-rte-3 opened before the apply and left OPEN/RED; unsigned at this write"
        },
        {
            "principal": "Opal_Terminal",
            "arn": "arn:aws:iam::313476888478:user/Opal_Terminal",
            "reason": "Operator identity of opal-data-cottonwood, the bucket this root creates. NOT a census row: opal-data-cottonwood is NEW and EMPTY with NO existing principals, so the 'Existing principal (FENCE_WRITER_CENSUS.md, granted)' ground the opal-data-49financial rows carry DOES NOT APPLY and is deliberately not reproduced. Scope token: none (IAM_USER: NOT GRADED), so the scope-derived DenyForeignFirmPrincipals matches and denies it. MEASURED CONSEQUENCE OF ITS ABSENCE: the fence applied with an empty exemption list denied EVERY identity this estate holds, including the applying identity -- head-bucket, get-bucket-policy, get-bucket-versioning and delete-bucket-policy all AccessDenied post-apply (IRPT_BCKEND row W3-S43). This row admits the operator and nothing else.",
            "signoff_ref": "org/critical_paths/change_management/20260918T1949Z_irpt-bckend-ib-rte-3-lgic-firm-buckets_deploy_completion.md -- the ledger entry IB-rte-3 opened before the apply and left OPEN/RED; unsigned at this write"
        }
    ]
}
```

## VERIFICATION ALREADY RUN ON THIS SEAT

- `python lib/opal_naming.py validate` -> **`VALIDATE: OK 25 system row(s), 9 scope row(s), 17 warning(s)`, rc=0**.
- Asserted before writing: `49financial` and `demo` carry NO `bucket_managed_by` and are untouched; the FIRM
  population is 4 rows and only 2 moved; `opal-data-49financial` still holds exactly 16 exemption rows.
- ⚠ **PERMITTED IS NOT VALIDATED:** `validate()`'s scopes loop checks required fields' SHAPE and never computes
  `set(row) - <closed set>` (`lib/opal_naming.py:322-389`), unlike `resources.json`'s `RES_FIELDS` closure
  (`:504-506`). **An unknown key on a scope row is silently accepted**, so a typo in the field name would have
  passed identically. That field-closure gap is a registry defect, filed here, not fixed as a rider.

## WHAT THIS DOES NOT DO

It does not repair the lockout. The buckets stay unreachable to every identity we hold until the account root
runs `delete-bucket-policy` on both -- **Andrew's act, at the console.** The ledger entry and its sentinel stay
OPEN and RED. And `W3-S45`: the remote state carries 4 TAINTED resources, so step 5's re-apply REPLACES them and
its never-widen sign-off must name those four as its blast radius.
