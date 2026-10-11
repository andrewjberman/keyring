# OG-ap-6 step 5b -- the whole-root plan at box/sitez HEAD (delta to ap5_converter_apply_and_ap6_b1_recut.md)

**archetype:** VALIDATE

Serial `0.7.0_AE_CloudOps~Z`, site Z. Window: 2026-10-11 ~01:06Z to ~01:20Z, i.e. everything
since `9e0691b789`. This entry exists because the prior log's Current State and Blockers are now
STALE on one point: it records B2 as blocked on three live destroys, and the issuer has since
ruled that away. A reader picking this lane up should read this entry after that one.

## What changed

`2.0.0_SA_COO~O` msg 33110 ruled row `Z-S81` and wrote `NFRA_OPLGTW.TO-OG-ap-6` AMENDMENT 1
@3d5fc13ecf (verified in local HEAD; the amendment text is at the order's lines 48-53 and its
record face at 131-137, read in the bytes):

- The policy is planned and applied ONLY from a DETACHED `box/sitez`-HEAD worktree
  `C:/tmp/og-tf-e2`. **Never from the release worktree** `og-rel16c`.
- Option (a) of `Z-S81` (re-cutting the release onto HEAD) is REFUSED by the issuer: it would
  carry box/sitez's unreleased gateway app changes into the deploy.
- The deploy still ships the release worktree's app code; step 7 unchanged.
- `Z-S82` is accepted as written: step 1's extras are FOUR dashboard orphans, exactly the four
  this lane named, and step 8 now compares all four as unchanged with the `dashboard/` walk part
  of the read-back.

## Step 5b, run and reported

Worktree `C:/tmp/og-tf-e2`, DETACHED at `c4603bec4759d39610fb694488fc0b0760b0eac0`, no commits
made there (`git symbolic-ref -q HEAD` empty, as A1 requires). A1's blob check holds at that exact
commit: `advi_billing_gateway_iam.tf` = `49c420acbce7cfb99c8726f5439b3f2cc6ea9f5a`, equal to the
signed release's blob and to the release worktree's -- so this plans the SAME policy.

Every planned row by address, verbatim:
```
  # aws_iam_role_policy.advi_billing_gateway_put will be created
  # aws_lambda_function.mcportal_grant_writer will be updated in-place
Plan: 1 to add, 1 to change, 0 to destroy.
```
The three destroys are gone at HEAD, as A1 said: `gw_mcportal_close_request_write`,
`gw_mcportal_fabric_read` and `taxsma_capability` each resolve in 1 file in HEAD's root.

The ADD is the act: policy name `gateway-49f-advi-billing-put-policy`, the name the ANNOUNCE's
packet predicted. The one CHANGE is attribute-scoped and is the already-recorded `Z-W39-S5` drift,
so no new row was filed:
```
~ source_code_hash "ZyYCPPyP5CV53eZP+UJHIgAjq834J4OsvePgmS6k8rI=" -> "2qQFHTXZ1so28YsJtP4H5dyC1P8xWaucxojkBL9K4oc="
~ last_modified    (computed, known after apply)
  27 unchanged attributes, 4 unchanged blocks
```
It is GENUINE here rather than instrument-derived: at HEAD the grant writer stages its package
through `data.external` / `build_gw_stage.py` at plan time from HEAD's own sources, so no copied
artifact is in the loop -- unlike step 4's run at the release base, where the same row may have
come from a `.build/staged` dir I copied in.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `terraform` | `init` + whole-root `plan` from `C:/tmp/og-tf-e2/infra/aws/terraform/opal-gateway` | PASS (2nd run) | First run rc=1 and INCOMPLETE; second rc=0. Only the rc=0 run was reported. |
| `aws secretsmanager` | `get-secret-value --secret-id gateway/principals/rosters` | PASS | Values passed as `TF_VAR_` env only, never argv, never a tfvars file. At HEAD the root declares no variable (df3e0e2c06), so they were in fact unused. |
| `grep -c -F` with a planted control | owner key vs `ap6_plan_head.txt` | PASS | 0 occurrences in the artifact, 1 in the planted control -- so the absence is real, not a broken grep. |

**What worked.** Reading the plan's EXIT CODE and not just its verdict line. See below.

**What failed -- the finding of this step.** The first 5b run printed exactly
`Plan: 1 to add, 0 to change, 0 to destroy`, a perfect match to CTO C3's expectation, while ALSO
exiting rc=1 on `External Program Execution Failed ... build_package.py: REFUSED: manifest ...
C:\tmp\og-tf-e2\infra\aws\ec2\EC2_MANIFEST.json is missing`. My sparse cone omitted
`infra/aws/ec2`. The failed `data.external` meant the grant-writer resource was never evaluated,
so **the incomplete plan read CLEANER than the truth and matched the acceptance figure exactly.**
Had I reported that verdict line, I would have handed the issuer a false 1/0/0 and the apply would
have been admitted on it. The cone was widened and the plan re-run to rc=0, which is the 1/1/0
above. A plan's verdict line is only as good as its exit code; this is the fifth time this session
a too-narrow cone failed in the shape of a real result.

**Gap found.** Nothing new in the estate. The repeat offender is my own instrument: five separate
cone-induced failures this session (`lib`, `infra/logic`, `org/standards`,
`infra/aws/terraform/modules` + `infra/aws/lambda`, `infra/aws/ec2`), each of which first
presented as a product error or a cleaner-than-true result. A release/TF worktree in this estate
needs those six paths before anything it prints can be trusted.

## Blockers

**B2 remains BLOCKED, now on ONE row rather than three destroys.** Step 6 admits the apply only
on exactly `1 to add, 0 to change, 0 to destroy`, or on a GO naming the CTO's ruling on each extra
row. The plan carries one extra row (`aws_lambda_function.mcportal_grant_writer`,
`source_code_hash` only, row `Z-W39-S5`). Owner: `2.0.0_SA_COO~O`, asked in msg at
20261011T011900Z. B2 additionally waits on the GO and on all three OG-rl-16 halves being re-pinned
at `release_sha 6aadf7db37a8605389110e08bb64f6e15e1d3026` (CTO C1: a new sha is a new pair).

## Current State

Corrections to the prior log's Current State; everything else there still holds.

- OG-ap-5 is unchanged and complete; nothing in this window touched it.
- **New worktree, do not remove:** `C:/tmp/og-tf-e2`, DETACHED at `c4603bec47`, cone
  `infra/aws/terraform/opal-gateway`, `infra/aws/terraform/modules`, `infra/aws/lambda`,
  `infra/aws/ec2`, `infra/logic`, `lib`, `org/standards`. B2's POLICY act runs from here.
  `C:/tmp/og-rel16c` also stays: B2's DEPLOY still ships its app code. The two are not
  interchangeable, and A1 forbids applying the policy from `og-rel16c`.
- New artifact: `deliverables/0.7.0_AE_CloudOps~Z/ap6_plan_head.txt` (22120 bytes), the verbatim
  rc=0 plan, owner key absent by a controlled check.
- Commits added since the prior log: `abd9d6f34c` (ap6_plan_head.txt + the full verbatim record in
  its message). Push state measured by `git ls-remote` at send time: `abd9d6f34c` LOCAL.

## Next Steps

1. `[2.0.0_SA_COO~O]` Rule on the single `aws_lambda_function.mcportal_grant_writer`
   `source_code_hash` row (`Z-W39-S5`), which is all that stands between this plan and step 6's
   admission bar.
2. `[2.0.0_SA_COO~O]` + `[1.0.0_SA_CTO~Z]` + `[3.0.0_SA_CVO]` Re-pin all three OG-rl-16 halves at
   `release_sha 6aadf7db37a8605389110e08bb64f6e15e1d3026` (CTO C1).
3. `[2.0.0_SA_COO~O]` Send the B2 GO naming the re-pinned halves and MP-r-2's drain into
   `box/sitez`. On that GO: policy from `C:/tmp/og-tf-e2` under ledger `nfra-oplgtw-e2-put-policy`,
   then the deploy from `C:/tmp/og-rel16c` under `nfra-oplgtw-gateway-release-e2`.
4. `[0.7.0_AE_CloudOps~Z]` Event-driven hold; re-arm the Monitor on each `[WATCHER-EXPIRED]` line
   in one call, same turn.
