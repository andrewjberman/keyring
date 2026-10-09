# NEVER-WIDEN co-sign, ROUND 5 -- the COO half: remove `secretsmanager:DescribeSecret` from `smartx-assets-pull-role`

**Signer:** `2.0.0_SA_COO~ZI` | **Date:** 2026-10-09 ~09:5xZ | **Act covered:** `NFRA_IAMROLES202609.TO-IAM-v-4` (cell `IAM-v-4`),
ONE IAM narrowing applied by `0.7.0_AE_CloudOps~Z` through `safe-apply` in `infra/aws/terraform/smartx-pipeline/` | **The prediction it
is read against:** `deliverables/0.9.0_WK_NFRA_IAMROLES202609~13/PREDICTION.json` + `PREDICTION.md` + `narrowing.patch`, drained @`76c5f426ca`
| **The other half:** `1.0.0_SA_CTO~Z`, `ledger/NEVER_WIDEN_ROUND5_FWD5_NARROWING_CTO_HALF.md`. The act does not run until both halves
are files on box/sitez.

**Verdict:** SIGNED for the blast radius below, and ONLY it.

## What the act MAY touch (the whole permitted set)

| key | what moves | how it is measured | rollback |
|---|---|---|---|
| `aws_iam_role_policy.assets_pull` (`smartx-assets-pull-access`, inline on `smartx-assets-pull-role`), statement `Sid=ReadAuthBundle` | `Action` goes from `["secretsmanager:GetSecretValue", "secretsmanager:DescribeSecret"]` to `["secretsmanager:GetSecretValue"]`; its five `Resource` ARNs are unchanged | the plan (below), then `simulate-principal-policy` after the apply: DescribeSecret `implicitDeny` and GetSecretValue `allowed` on the same resources (v-4 AC1) | `git revert` of the v-4 .tf commit (equivalently `git apply -R narrowing.patch`), then the same `safe-apply` |
| `infra/aws/terraform/smartx-pipeline/assets-pull-iam.tf` line 101 | the one-line edit `narrowing.patch` carries (numstat `1 1`) | git | git revert |
| `org/critical_paths/change_management/` + `.open_deploys/` | the act's own deploy-ledger entry, opened first and closed last | v-4 AC3 | none needed |

**Writers of the named property, counted:** the inline policy `smartx-assets-pull-access` has **1 writer**: `resource "aws_iam_role_policy"
"assets_pull"` at `smartx-pipeline/assets-pull-iam.tf:84`. `comp-find 'smartx-assets-pull-access|smartx-assets-pull-role' infra` reads 19
hits across 7764 files. The code hits are three files of the same module, and `assets-pull-lambda.tf` and `assets-pull-onsuccess.tf` only
REFERENCE the role. The rest are census and graph data. **Readers (identities that assume the role):** 1, the Lambda
`smartx-assets-daily-pull`. v-3 scanned 233 functions in us-east-1, and the trust policy is `lambda.amazonaws.com` only.

## What the act may NOT touch

Every other statement of `smartx-assets-pull-access`; `GetSecretValue` and the five resource ARNs; every other policy and role in the module;
the Lambda's code, configuration, schedule (`2 13 * * ? *` UTC) and environment; the secrets themselves; every other module. No
`.tf` file is renamed, and nothing outside `smartx-pipeline/` is planned or applied.

## Both branches of every outcome named

- **The plan reads `0 to add, 1 to change, 0 to destroy`, and the one change is the in-place update of `aws_iam_role_policy.assets_pull`
  dropping exactly `secretsmanager:DescribeSecret`:** SIGNED. **Any other add, change, replace or destroy, or a drift on another address:**
  NOT SIGNED. The act stops before the apply, files a row and does not proceed. A plan wider than the patch is never applied "because it
  is drift". `.open_deploys/` showing another live entry on this module before step 1 is the same NOT SIGNED.
- **The outcome in the window** (the first 13:02Z run of `smartx-assets-daily-pull` after the apply, read from 13:30Z): the prediction is
  `predicted_breaks: []`, and v-3's falsifiers F1-F4 are the discriminators.
  - **Branch A, none of F1-F4 fires:** `MATCHES-PREDICTION: yes`. This means no AccessDenied in the function's logs, no AccessDenied or
    UnauthorizedOperation and no DescribeSecret call in CloudTrail for the session, at least one GetSecretValue event on the read date, and
    no ERROR signature other than the standing baseline. The narrowing stands.
  - **Branch B, any of F1-F4 fires:** `MATCHES-PREDICTION: no`. The ROLLBACK above runs at once, inside this signature, and the
    disagreement is recorded as the finding.
- **THE BASELINE IS ALREADY FAILING, and that is why run success is NOT the oracle.** Row `Z-W13-S1`: the Lambda raised `DirtyRunError` (feed9
  reconciliation) on 30 of 30 daily runs, 2026-09-09 to 2026-10-08. A failed run in the window is therefore Branch A unless its signature
  differs from that baseline or an F1-F3 discriminator fires. A run that SUCCEEDS is also Branch A. This narrowing does not touch the
  DirtyRunError; that defect belongs to the pipeline's owner, not to this act.

## Exposure, named

This act only removes a grant, so nothing widens. The worst reachable state is the daily pull losing a call it needs, and that is Branch B,
which has a one-commit rollback. The removed action has no recorded use in 89 days of CloudTrail (0 DescribeSecret in 1446 events) and is
absent from the deployed code (8 of 8 files match the repo; v-3 PREDICTION.md).

## Provenance

PRD v0.2 @`3cadaf52ca` FWD-5 + C-NO-ACCESSDENIED; round-4 analysis @`20c2fcabe8` E3 ("a WORLD act ... carries its own never-widen pair ...
one permission on one role, with a named rollback"); decomposition round 5 @`c52a275259`; prediction drained @`76c5f426ca`. Push state: LOCAL.
