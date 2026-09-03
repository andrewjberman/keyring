# NFRA_GLOBGRPH Lifecycle and Users Delete-Guard Execution - 0.8.0_AE_CloudComp~K

**archetype:** MIXED
**Date:** 2026-09-03
**Task Order:** NFRA_GLOBGRPH.TO-MSHEAT-EXPIRY and NFRA_GLOBGRPH.TO-USERS-DELPROT
**Status:** IN PROGRESS - deploy legs complete; proof validation and issuer report remain

---

## Objective

Apply the approved 60-day lifecycle rule to rebuildable MS heat snapshots without widening into unrelated shared-infra drift, then declare the live users-table deletion guard in Terraform so desired matches applied. Preserve every unrelated plan change as read-only evidence and never run an unscoped apply.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-read | `comp-read org/modules/heatmap/ms_heat_index.py --for ...` | PASS | Located the producer, full recompute path, latest object, and dated snapshot writer. |
| comp-read | `comp-read infra/aws/globgrph/snap_store.py --for ...` | PASS | Located `globgrph.ms_heat_snap`, its append-only write, and storage location. |
| comp-read | `comp-read infra/aws/terraform/shared-infra/dynamo.tf --for ...` | PARTIAL | Surfaced the resource and name but not every requested attribute; a full 92-line read completed the declaration census. |
| comp-adversary | `comp-adversary compose <TO-USERS-DELPROT face> --no-packet` | PASS | Four of four cited commits verified; three expected output paths flagged as gone or moved since authoring. |
| comp-schedule | `comp-schedule` immediately before the users-table apply leg | PASS | Read 23 armed gates across the five carriers; this seat's open ledger was G-11 and no additional gate named the table act. |
| Terraform | Target-scoped and unscoped plans through `.tools/terraform.exe -chdir=infra/aws/terraform/shared-infra` | PASS | Exact target plans passed; unscoped controls exposed and preserved unrelated drift without applying it. |
| safe-apply | Saved-plan apply for each order | PASS | Lifecycle apply was 0/1/0; users-table saved-plan apply was the ordered 0/0/0 no-op. |

Results: PASS=accurate+useful | PARTIAL=present but noisy | FAIL=wrong/crash/silent | SKIPPED=explain why | WARN=empty+correct WARN message

**What worked:** Target-scoped Terraform plans and the unscoped controls separated each authorized act from unrelated live drift. `safe-apply` enforced tag-authorization and tombstone gates before both saved plans. `comp-schedule` made the active ledger gate explicit before the second apply.

**What failed:** The first unscoped saved plan correctly failed the original exact 0/1/0 gate at 0/2/0. After the lifecycle apply, the unscoped acceptance correctly exposed a second mismatch at 0/10/0. These were gate findings, not compiler crashes. `comp-read` on `dynamo.tf` was incomplete for the requested whole-resource attribute census, so the complete 92-line file was read before editing.

**Gap found:** Nine live API Gateway routes carry `CUSTOM` authorization with authorizer `naqxlm` while the current module would plan `NONE` and null. This is `NFRA_GLOBGRPH-S2`; the routes were not changed or applied by this seat.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Measure snapshot rebuildability and update the HOLD carrier | `f42be3d548`; semantic rebuildability established with bounded byte-identity loss |
| 2 | Open MS heat lifecycle deploy ledger and take live pre-read | `45b641343d`; one live rule, MS heat rule absent |
| 3 | Refuse original unscoped plan | 0 add / 2 change / 0 destroy; no apply; `NFRA_GLOBGRPH-S1` at `3d2daa3ffa` |
| 4 | Declare amended lifecycle target in the ledger | `f1dce36b9b` |
| 5 | Create and safe-apply new target-scoped lifecycle plan | Plan 0/1/0 on one address; apply 0 added / 1 changed / 0 destroyed |
| 6 | Read live lifecycle and unscoped control | Two correct live rules; control 0/10/0 with lifecycle address gone |
| 7 | Record whole-control divergence | `NFRA_GLOBGRPH-S2` at `28b9a1e4d6`; no unscoped apply |
| 8 | Commit lifecycle evidence and close ledger/HOLD | Evidence `49c49c218f`; closure `327217feba`; stale original plan deleted |
| 9 | Open users deletion-protection ledger | `45b99d1f96` before declaration |
| 10 | Live pre-read | 2026-09-03T16:41:22Z: `DeletionProtectionEnabled=true` |
| 11 | Add one Terraform declaration and format-check | `14fbeace00`; `deletion_protection_enabled = true`; fmt-check exit 0 |
| 12 | Create scoped users-table saved plan | One refreshed target; `No changes. Your infrastructure matches the configuration.` |
| 13 | Safe-apply scoped no-op saved plan | `Apply complete! Resources: 0 added, 0 changed, 0 destroyed.` |
| 14 | Take final unscoped control and live read | 0/9/0, exactly the nine disclosed routes; users-table and lifecycle lines gone; live true at 16:46:21Z |
| 15 | Close users-table ledger and commit evidence | All four legs proven; `8ddc19238a`; open sentinel removed |

## Verification

- Lifecycle live read: exactly two Enabled rules. `abort-incomplete-mpu-7d` remains at 7 days; `ms-heat-snapshots-expire-60d` has prefix `warehouse/ms_heat/snapshots/` and 60-day expiration.
- Lifecycle safe-apply: `Apply complete! Resources: 0 added, 1 changed, 0 destroyed.`
- Users-table scoped plan: `No changes. Your infrastructure matches the configuration.`
- Users-table safe-apply: `Apply complete! Resources: 0 added, 0 changed, 0 destroyed.`
- Final unscoped control: `Plan: 0 to add, 9 to change, 0 to destroy.` All nine are the disclosed API-route `CUSTOM -> NONE` / `naqxlm -> null` drifts; none was applied.
- Users-table live pre/post reads: `true` at 16:41:22Z and `true` at 16:46:21Z.
- No IAM resource changed. No unscoped plan was applied. No branch was pushed.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Refuse the original 0/2/0 saved plan | The CTO gate authorized only lifecycle 0/1/0; removing a served users-table delete guard as a passenger was forbidden. |
| Use new target-scoped plans for both acts | Each order explicitly bounded the only address eligible for apply. |
| Preserve the full unscoped drift as acceptance evidence | Issuer amendment `ee688a660b` grades the control on lifecycle/users changes being gone, every remaining route address disclosed, and none applied. |
| Leave the nine API-route changes untouched | They are outside both orders and were routed through `NFRA_GLOBGRPH-S2` to the issuer. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `org/critical_paths/change_management/20260903T1120Z_shared-infra-ms-heat-snapshots-expire-60d_hold.md` | Added rebuildability evidence and closed the carrier | Yes - `f42be3d548`, `327217feba` |
| `org/critical_paths/change_management/20260903T1418Z_shared-infra-ms-heat-snapshots-expire-60d_deploy_completion.md` | Recorded target, apply, live reads, whole control, and closure | Yes - `45b641343d`, `f1dce36b9b`, `49c49c218f`, `327217feba` |
| `org/surprise_channel/NFRA_GLOBGRPH/INVESTIGATION_v1.md` | Added S1 and S2 | Yes - `3d2daa3ffa`, `28b9a1e4d6` |
| `infra/aws/terraform/shared-infra/dynamo.tf` | Added `deletion_protection_enabled = true` to `opal_users_v2` | Yes - `14fbeace00` |
| `org/critical_paths/change_management/20260903T1639Z_shared-infra-users-v2-deletion-protection_deploy_completion.md` | Recorded four-leg users-table deployment and closure | Yes - `45b99d1f96`, `8ddc19238a` |
| `org/tier2_senior/0.8.0_AE_CloudComp~K/deliverables/NFRA_GLOBGRPH.TO-MSHEAT-EXPIRY.*` | Captured lifecycle apply, live post-read, and unscoped control | Yes - `49c49c218f` |
| `org/tier2_senior/0.8.0_AE_CloudComp~K/deliverables/NFRA_GLOBGRPH.TO-USERS-DELPROT.*` | Captured pre/post reads, scoped plan, no-op apply, and unscoped control | Yes - `8ddc19238a` |

---

## Blockers

None. `NFRA_GLOBGRPH-S2` is an out-of-scope routed finding, not a blocker to the two amended acceptances.

---

## Current State

Both deploy ledgers are CLOSED and both open sentinels are removed. The MS heat lifecycle rule is live and verified; the users table remains live with deletion protection true and Terraform now explicitly declares that state at `14fbeace00`. The original unsafe unscoped lifecycle plan was deleted; the consumed target-scoped plans remain on disk as local evidence. Nine API-route authorization drifts remain visible only in unscoped plans and were never applied. Proof-of-spec construction, validation, and the final issuer reports are the remaining acts.

---

## Next Steps

1. Create and validate the two proof-of-spec instances, then report both completed orders to `2.0.0_SA_COO` with push state LOCAL.
2. **[2.0.0_SA_COO]** Flip the flat task-order statuses and continue routing `NFRA_GLOBGRPH-S2` to `1.0.0_SA_CTO`/CVO as already stated.
