# Deploy Completion Record
**Date opened:** 2026-10-11T16:05:09.202097+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261011T160837Z
**Deploy:** ADVI_FIRMBKTS TO-FB-f-17 (act 3c): the exec-summary generator's fence row applied to s3://opal-data-49financial -- ONE bucket policy (aws_s3_bucket_policy.opal_data_49financial, root infra/aws/terraform/shared-infra), 29 to 34 statements (3 Deny + 2 Allow added; fence exemption +1: exec-summary-generator-role, Get/List/Put exempt under advi/49financial/platinum/advisors/ only; Allow side read-only); pair COO half @3d5185f9de + CTO half @6f5335f5c0; rollback = the prior policy put back verbatim; inert until act 4b
**Authored by:** 0.7.0_AE_CloudOps~FB1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | pre-write reads: pair SIGNED at the current bytes, the live policy printed to deliverables/PRIOR_opal-data-49financial_policy_<UTC>.json reading 29 statements, the planned policy checked against the actor's own access | the entry carries the read lines and the prior file path | COO half 3d5185f9de and CTO half 6f5335f5c0 SIGNED at the current bytes (0 uncommitted); prior policy printed to org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/PRIOR_opal-data-49financial_policy_20261011T160524Z.json reading 29 statements before any plan; Deny statements of the prior (control) and the planned policy evaluated for user/cloudops-dell1-agent-user: Get/Put/DeleteBucketPolicy, GetObject on KEY, ListBucket not denied in either | CLOSED 20261011T160837Z |
| L2 | activation | scoped plan of shared-infra reads Plan: 0 to add, 1 to change, 0 to destroy, one resource in place, 29 to 34 statements; .tools/safe-apply.sh on the saved plan | plan summary line, the policy diff hunk, apply result line | scoped plan Plan: 0 to add, 1 to change, 0 to destroy (1 resource in place, attribute policy only; 29 to 34 statements; 28 others byte-equal; fence exemption +1 -0 exec-summary-generator-role; no Put/Delete/s3:*/bucket-wide Allow); --dry-seat-gates read first (OVERLAP clear; the two hits as act 3b, row ADVI_FIRMBKTS-D1-S30); .tools/safe-apply.sh on the saved plan 16:07:00Z-16:07:36Z: Apply complete! Resources: 0 added, 1 changed, 0 destroyed | CLOSED 20261011T160837Z |
| L3 | verify | AC1 r4_act3b.py --arms live reads 3 of 3 arms (34 statements: 21 Deny, 13 Allow); AC2 the scoped plan reads No changes | the two outputs quoted | live policy 34 statements (21 Deny, 13 Allow) read 16:07:36Z; AC1 r4_act3b.py --arms live: ROUND 4 ACT 3B LIVE: 3 of 3 arms (live equals rendered 0 differing; no violating Allow; unsigned GET of the ownership key 403); AC2 scoped plan: No changes. Your infrastructure matches the configuration. | CLOSED 20261011T160837Z |
| L4 | git | proof instance and prior policy file written, status flipped complete in one commit | commit hash | proof instance, prior policy file and act3c evidence committed with this entry; TO-FB-f-17 status flipped complete in the same commit; commit hash is this commit | CLOSED 20261011T160837Z |

## Log

- 20261011T160509Z OPENED by 0.7.0_AE_CloudOps~FB1 with 4 leg(s)
- 20261011T160837Z LEG L1 closed: COO half 3d5185f9de and CTO half 6f5335f5c0 SIGNED at the current bytes (0 uncommitted); prior policy printed to org/mis
- 20261011T160837Z LEG L2 closed: scoped plan Plan: 0 to add, 1 to change, 0 to destroy (1 resource in place, attribute policy only; 29 to 34 statements; 
- 20261011T160837Z LEG L3 closed: live policy 34 statements (21 Deny, 13 Allow) read 16:07:36Z; AC1 r4_act3b.py --arms live: ROUND 4 ACT 3B LIVE: 3 of 3 a
- 20261011T160837Z LEG L4 closed: proof instance, prior policy file and act3c evidence committed with this entry; TO-FB-f-17 status flipped complete in th
- 20261011T160837Z CLOSED -- all 4 legs proven

## ACT 3C OUTCOME (0.7.0_AE_CloudOps~FB1, 2026-10-11T16:08:36Z)

- **Pair:** COO half (`3d5185f9de`) and CTO half (`6f5335f5c0`), SIGNED at the current bytes, 0 uncommitted; `FB-g-27` merged @deb92d1530.
- **Prior policy printed before any plan:** `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1\PRIOR_opal-data-49financial_policy_20261011T160524Z.json`, 29 statements (the rollback artifact).
- **Plan (scoped, saved):** `Plan: 0 to add, 1 to change, 0 to destroy`; one resource in place, attribute `policy` only. 29 to 34
  statements (21 Deny, 13 Allow); the 28 other statements byte-equal to the prior; the blanket fence's exemption list gains exactly 1
  principal (`exec-summary-generator-role`) and loses 0; the five new statements are the generated scoped row 9: three Deny
  (`DenyScopedExemption9AnyOtherAction`, `...ObjectsOutsidePrefix`, `...ListingOutsidePrefix`) and two Allow
  (`AllowScopedExemption9Objects`: `s3:GetObject`; `AllowScopedExemption9Listing`: `s3:ListBucket` under the directory prefix); no
  Allow writes, deletes, names `s3:*` or the whole bucket. `evidence/act3c/analysis_plan_vs_prior.txt`, `scoped_plan_with_policy_diff.out`.
- **Self-access before the apply:** prior (control) and planned Deny statements evaluated for `user/cloudops-dell1-agent-user` on
  GetBucketPolicy, PutBucketPolicy, DeleteBucketPolicy, GetObject (KEY), ListBucket: not denied in either, no unevaluated condition.
- **Seat gates:** `--dry-seat-gates` first: OVERLAP clear; OPEN-CALL XB-20261011T082334Z-282f and OPEN-DEPLOY iamroles-r7-narrow-portal-s3,
  the same two read and found disjoint for act 3b (row `ADVI_FIRMBKTS-D1-S30`). WARN mode.
- **Apply:** 16:07:00Z to 16:07:36Z, `Apply complete! Resources: 0 added, 1 changed, 0 destroyed.`
- **Live after (16:07:36Z):** 34 statements, 21 Deny, 13 Allow. AC1 `ROUND 4 ACT 3B LIVE: 3 of 3 arms` (live equals rendered, 0 differing;
  no violating Allow; an unsigned GET of the ownership key returns 403). AC2 `No changes.`
- **Not read by this lane (the issuer's close):** the generator role's simulation with the live policy as `ResourcePolicy` (Get and List
  in the directory allowed; Put allowed only after `FB-f-18`).
- **Rollback, unused:** put `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1\PRIOR_opal-data-49financial_policy_20261011T160524Z.json` back as the bucket policy, verbatim, the same hour.
