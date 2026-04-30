# Session Log — inf-pipeline KMS/SSM Fix + ADHC_COMPIL.007

**Agent:** 0.7.0_AE_CloudOps
**Date:** 2026-04-30
**GO Source:** COO inbox MCP (23:09Z + 23:17Z 2026-04-29)
**Status:** COMPLETE
**Tag:** `inf-pipeline-v1.7.1`

---

## Scope

Two structural fixes for `inf-jwt-trigger` pipeline shipped manually last night by COO,
now lifted into Terraform + code. Plus ADHC_COMPIL.007 (comp-validate hint, stretch TO).

---

## Issue 1: KMS IAM Policy Lift

**Root cause:** `inf-jwt-trigger-lambda-role` had no KMS permissions. When the Lambda
called `ec2:StartInstances` on the inf-exporter instance, the EC2 hypervisor could not
decrypt EBS volume `vol-09bece78f6a047f02` (encrypted with `alias/inf-ebs-key` /
`4ba4753c-98f4-47c0-9a47-6dacaa1b6370`). Instance went pending -> Server.InternalError -> stopped.

**Fix:** Added `aws_iam_role_policy.inf_jwt_trigger_kms` to `iam.tf`:
- `kms:CreateGrant` with `kms:GrantIsForAWSResource=true` — lets EC2 hypervisor create the EBS decrypt grant at attach time
- `kms:Decrypt/Encrypt/ReEncrypt*/GenerateDataKey*/DescribeKey` — uses `aws_kms_key.inf_ebs.arn` reference (not hardcoded ARN)

Terraform state now owns this inline policy. `terraform apply --replace` on the role will
no longer drop the KMS grant.

---

## Issue 2: Lambda SSM Dispatch Fix

**Root cause:** `_handle_jwt_extract()` wrote the S3 mode marker and started the EC2, but
never dispatched an SSM command. The Lambda docstring claimed systemd `inf-jwt-fetch.service`
would read the marker on boot — but that unit has never existed on the instance. The
`opal-inf-jwt-fetch` SSM document already exists in Terraform (`ssm-inf-jwt-fetch.tf`) but
was never being called from `_handle_jwt_extract()`.

**Fix (Option B — reuse existing SSM doc, already in TF):**
- Added `JWT_FETCH_SSM_DOCUMENT = 'opal-inf-jwt-fetch'` constant
- Added `_send_jwt_fetch_command()` (mirrors `_send_export_command()` pattern)
- Rewrote `_handle_jwt_extract()` to: write mode marker -> `_ensure_running()` -> `_wait_for_running()` -> `_send_jwt_fetch_command()`. Symmetric with `_handle_export()`
- Added `opal-inf-jwt-fetch` to `SendExportCommand` Sid resource list in `inf_jwt_trigger_policy`
- Updated docstring to reflect actual behavior (removed stale systemd reference)

Note: COO recommended Option A (add Mode param to `opal-inf-export-run`). Went with
Option B (use existing `opal-inf-jwt-fetch`) since that SSM document already handles
`EXPORT_MODE=jwt-extract` correctly and is already in Terraform — no doc changes needed.

---

## ADHC_COMPIL.007: comp-validate Hint Line

**Gate cleared:** ADHC_COMPIL.006 COMPLETE 2026-04-29 PM.

**Change:** Added 3-line block to `.tools/comp-validate`:
```bash
if [ $_exit -ne 0 ]; then
    echo "Hint: see COMP_VALIDATE_PROTOCOL.md §4 for retry policy"
fi
```

Section confirmed as §4 (retry policy) by reading the actual doc. TO draft had §3
which is severity levels, not retry.

**Acceptance:**
- AC1 PASS: `comp-validate cash_coverage_summary --artifact /tmp/empty.json` -> exit 1,
  "Hint: see COMP_VALIDATE_PROTOCOL.md §4 for retry policy" printed
- AC2 PASS: `comp-validate --list` -> exit 0, no hint line
- comp-validate was not git-tracked (gitignored .tools/); used `git add -f` per XXX.md pattern

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Commit IAM + Lambda source | `b831e55c4` |
| 2 | build-and-upload.sh inf-pipeline inf-jwt-trigger | SHA256: qvTuiYAHHYf6OjVL1/SJdqjA3/ORBu5BT+PsKH/LrqQ= |
| 3 | Commit source map | `adcb4ce2c` |
| 4 | terraform plan | 1 add, 2 change, 0 destroy |
| 5 | terraform apply | 1 added, 2 changed, 0 destroyed |
| 6 | 0-diff plan | No changes. Infrastructure is up-to-date. |
| 7 | record-deploy + tag | `c91f9d094` inf-pipeline-v1.7.1 |
| 8 | git push --follow-tags | CLOUD -> CLOUD, new tag inf-pipeline-v1.7.1 |

## Deployment Tags

| Pipeline | Tag | Commit |
|----------|-----|--------|
| inf-pipeline | `inf-pipeline-v1.7.1` | `c91f9d094` |

---

## Compiler Tools

| Tool | Command | Result |
|------|---------|--------|
| comp-iam service | N/A — IAM changes are in Terraform; verified via plan diff | Added KMS + SSM doc to JWT trigger role |
| py_compile | `python -m py_compile lambda_function.py` | OK |
| ds-commit-gate.sh | `.tools/ds-commit-gate.sh lambda_function.py` | All checks passed |

---

## Verification

- KMS policy: `aws_iam_role_policy.inf_jwt_trigger_kms` created in apply output
- SSM IAM: `inf_jwt_trigger_policy` updated — added `opal-inf-jwt-fetch` document ARN
- Lambda: `s3_object_version` updated from `ogW02vdcSwXfrZbwP.3a...` to `N6dm4otZUnlWBzg1...`
- 0-diff confirmed: "No changes. Infrastructure is up-to-date."

---

## Next Steps

- [DS] Can now invoke inf-jwt-trigger in `jwt-extract` mode; SSM will dispatch
  `opal-inf-jwt-fetch` automatically after instance reaches running state
- [COO] RAVC4 on ADHC_COMPIL.007 sent via MCP
- [AE self] No carry-forward blockers from this session
