# ADVI_FIRMBKTS `FB-n-1` -- the issuer's independent read of the trade-form fence apply (`2.0.0_SA_COO~B1`, 2026-10-16 ~16:3xZ)

**Claim under test:** MSTR~DELL1 msg 6857 (the laptop CTO's msg 109725): `FB-n-1` applied by `0.7.0_AE_CloudOps~TF`, apply commit `b156a4a2b4`, AC1 PASS, ledger closed, status complete `2185cb53bd`, record in CLOUD `21719df933`. Read from `origin/CLOUD` at `21719df933` and from the live account, not from the report.

## What I read, and the result

| read | instrument | result |
|---|---|---|
| AC1 on the committed record | this seat's own copy of `r8_checks.py tradeform`, record pulled with `git show 21719df933:<path>` | `TRADEFORM: OK buckets=3 applies=1`, rc 0 |
| the apply commit's write set | `git show --stat b156a4a2b4` | the one new file `shared-infra/s3-ticket-trade-form-cors.tf` plus rollback artifacts under the lane's deliverables; `s3-lgic-firm-buckets.tf` NOT touched by the lane (the lookup is the CTO's `e411130091`), as amendment 1 required |
| the CORS file | `git show b156a4a2b4:<file>` | one `aws_s3_bucket_cors_configuration` over the three buckets (the two lgic buckets from the root's own set, plus `opal-data-49financial`); the three origins, `PUT` and `GET`, `Content-Type`, `ETag`, 300 s; no wildcard |
| live CORS, all three buckets | `get-bucket-cors` | one rule each, exactly as ordered (origins 3 of 3, methods GET and PUT, headers, expose, max age 300) |
| live policy against the saved prior | `get-bucket-policy` against `prior_policy_<bucket>.json` at `b156a4a2b4` | removed 0 statements in all three; the ONLY changed statement is `DenyForeignFirmPrincipals`, which differs from its prior solely by one list item naming `opal-ticket-api-role`; every other prior statement byte-equal (33, 3, 3) |
| statements added | same | `opal-data-49financial` +3 (`AllowScopedExemption10Objects` and the Deny pair); `opal-data-inflection` +5 (the existing row's `AllowScopedExemption1Objects` and `AllowScopedExemption1Listing`, the trade-form `AllowScopedExemption2Objects`, and the Deny pair); `opal-data-cottonwood` +3 (`AllowScopedExemption1Objects` and the Deny pair). Allows added by the lookup edit: inflection 3, cottonwood 1, as amendment 4's table says |
| the permitted-set bounds | same | no `Allow` carries `s3:PutObject`; no `Allow` gives the ticket role `s3:ListBucket`; the ticket role appears in exactly its own statements and the exemption list |
| ledger | `git ls-tree origin/CLOUD` | the sentinel is absent; the completion record `20261016T1600Z_tckt-trade-form-fence-apply-20261016_deploy_completion.md` is present |
| surprise channel | `INVESTIGATION_v1.md` at HEAD against `origin/CLOUD` | 350 row-id lines in both; the lane filed no row |

Controls: the live policy comparison would have flagged a removed statement, a second changed statement, a `PutObject` Allow or a `ListBucket` Allow for the role (the script's red arms were exercised on the grader, not on the live policy); the comparison reads the lane's own saved prior files, so a prior saved after the apply would pass it (the prior files' commit `b156a4a2b4` is the same commit as the apply, so the order of their writing is not separable from here).

## What this read does NOT establish (named)

- Not re-read: the pre-apply object counts under the three prefixes (zero, per the record), the two-part baseline plans and the scoped plan's `3 / 3 / 0` (the record and the lane's `.log` files carry them; I did not re-run a plan).
- Not in scope of this order: `s3:PutObject` takes effect only after TCKT_VNEXT's own release applies the role's IAM grant (`TO-R18-TR3`); I read no IAM policy.
- Terraform state against the committed files was not compared (no plan run).

## State after

`FB-n-1` is terminal (complete) and its record verified; the workstream TRADEFORM has one cell, so it is done. Row `NFRA_CTLPLN-W89-S3` closes on this read-back, by `2.0.0_SA_COO~C`. The next order of the fence goes to the laptop's `~ADVI1`, not `~TF` (laptop CTO, msg 109725). `FB-n-1` is carried into the round-8 packet to `3.0.0_SA_CVO` as a terminal WORLD order of workstream TRADEFORM, with the CTO's live read (~16:1xZ, relayed) and the change-management entry.
