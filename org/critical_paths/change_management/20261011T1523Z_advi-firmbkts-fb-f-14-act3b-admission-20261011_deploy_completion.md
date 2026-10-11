# Deploy Completion Record
**Date opened:** 2026-10-11T15:23:14.591012+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261011T152947Z
**Deploy:** ADVI_FIRMBKTS TO-FB-f-14 (act 3b): the readers' admission applied to s3://opal-data-49financial -- ONE bucket policy (aws_s3_bucket_policy.opal_data_49financial, root infra/aws/terraform/shared-infra), 4 statements replaced by the registry-generated 29; pair COO half @0cbbd71714 (ADDENDUM 1 over @ac44d4a847) + CTO half @0b108b8357; rollback = the prior policy put back verbatim from the printed file; inert until act 4
**Authored by:** 0.7.0_AE_CloudOps~FB1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | pre-write reads: pair unchanged and SIGNED, the live policy printed to deliverables/PRIOR_opal-data-49financial_policy_<UTC>.json reading 4 statements, the rendered policy checked against the actor's own access | the entry carries the read lines and the prior file path | COO half (0cbbd71714, ADDENDUM 1 only over @ac44d4a847) and CTO half (0b108b8357, ADDENDUM 1) SIGNED at the current bytes; prior policy printed to org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/PRIOR_opal-data-49financial_policy_20261011T152348Z.json reading 4 statements (2631 bytes) before any plan; Deny statements of the prior (control) and the planned policy evaluated for user/cloudops-dell1-agent-user: Get/Put/DeleteBucketPolicy, GetObject on KEY, ListBucket not denied in either | CLOSED 20261011T152946Z |
| L2 | activation | scoped plan of shared-infra (-target aws_s3_bucket_policy.opal_data_49financial) reads Plan: 0 to add, 1 to change, 0 to destroy, one resource in place; .tools/safe-apply.sh on the saved plan | plan summary line, the policy diff hunk, apply result line | scoped plan Plan: 0 to add, 1 to change, 0 to destroy (1 resource, attribute policy only; 4 to 29 statements; fence exemption +7 -0; no Put/Delete/s3:*/bucket-wide Allow); --dry-seat-gates read first, both hits read and disjoint (row ADVI_FIRMBKTS-D1-S30); .tools/safe-apply.sh on the saved plan 15:26:58Z-15:27:28Z: Apply complete! Resources: 0 added, 1 changed, 0 destroyed; id opal-data-49financial | CLOSED 20261011T152947Z |
| L3 | verify | AC1 r4_act3b.py --arms live reads 3 of 3 arms; AC2 the scoped plan reads No changes; statements before and after counted | the two outputs quoted | live policy 29 statements (18 Deny, 11 Allow) read 15:27:50Z; AC1 r4_act3b.py --arms live: ROUND 4 ACT 3B LIVE: 3 of 3 arms (L1 live equals rendered 0 differing, L2 no violating Allow, L3 unsigned GET of the ownership key 403); AC2 scoped plan: No changes. Your infrastructure matches the configuration. | CLOSED 20261011T152947Z |
| L4 | git | proof instance and prior policy file written, status flipped complete in one commit | commit hash | proof instance, prior policy file and act3b evidence committed with this entry; TO-FB-f-14 status flipped complete in the same commit; commit hash is this commit | CLOSED 20261011T152947Z |

## Log

- 20261011T152314Z OPENED by 0.7.0_AE_CloudOps~FB1 with 4 leg(s)
- 20261011T152946Z LEG L1 closed: COO half (0cbbd71714, ADDENDUM 1 only over @ac44d4a847) and CTO half (0b108b8357, ADDENDUM 1) SIGNED at the current byte
- 20261011T152947Z LEG L2 closed: scoped plan Plan: 0 to add, 1 to change, 0 to destroy (1 resource, attribute policy only; 4 to 29 statements; fence exem
- 20261011T152947Z LEG L3 closed: live policy 29 statements (18 Deny, 11 Allow) read 15:27:50Z; AC1 r4_act3b.py --arms live: ROUND 4 ACT 3B LIVE: 3 of 3 a
- 20261011T152947Z LEG L4 closed: proof instance, prior policy file and act3b evidence committed with this entry; TO-FB-f-14 status flipped complete in th
- 20261011T152947Z CLOSED -- all 4 legs proven

## ACT 3B OUTCOME (0.7.0_AE_CloudOps~FB1, 2026-10-11T15:29:21Z)

- **Pair:** COO half (its last commit `0cbbd71714` adds only ADDENDUM 1, the negative arm; 9 lines added, 0 removed against the cited
  `@ac44d4a847`) and CTO half (`0b108b8357`, ADDENDUM 1 accepts the corrected negative arm), both SIGNED at the current bytes.
- **Prior policy printed before any plan:** `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1\PRIOR_opal-data-49financial_policy_20261011T152348Z.json`, 4 statements, 2631 bytes (the rollback artifact).
- **Plan (scoped, saved):** `Plan: 0 to add, 1 to change, 0 to destroy`; 1 resource in place, attribute `policy` only. 4 statements to 29
  (18 Deny, 11 Allow); the three performance-adapter hand statements replaced; the fence's exemption list gains 7 principals (the five
  IRPT roles, `lambda-edge-execution-role`, the router's OAI) and loses 0; no Allow writes, deletes, names `s3:*` or the whole bucket.
  `evidence/act3b/analysis_plan_vs_prior.txt`, `scoped_plan_with_policy_diff.out`.
- **Self-access check before the apply:** the Deny statements of the prior (control) and the planned policy evaluated for
  `user/cloudops-dell1-agent-user` on GetBucketPolicy, PutBucketPolicy, DeleteBucketPolicy, GetObject (KEY) and ListBucket: not denied
  in either, no unevaluated condition. `evidence/act3b/analysis_self_access.txt`. This is why the rollback was never at risk of being
  unreachable by the actor.
- **Seat gates:** `--dry-seat-gates` first, then the apply. `OPEN-CALL` XB-20261011T082334Z-282f and `OPEN-DEPLOY`
  iamroles-r7-narrow-portal-s3 were each read and found disjoint from the one resource (row `ADVI_FIRMBKTS-D1-S30`). WARN mode; read, not skipped.
- **Apply:** 15:26:58Z to 15:27:28Z, `Apply complete! Resources: 0 added, 1 changed, 0 destroyed.` `evidence/act3b/apply_safe-apply.out`.
- **Live after (15:27:50Z):** 29 statements, 18 Deny, 11 Allow. AC1 `ROUND 4 ACT 3B LIVE: 3 of 3 arms` (L1 live equals rendered, 0 differing;
  L2 no Allow writes, deletes or names the whole bucket; L3 an unsigned GET of the ownership key returns 403). AC2 `No changes.`
- **Correction for the record:** the COO half says `get-bucket-policy` "is denied to the dell1 identities"; this identity read it
  (before and after) with `s3:GetBucketPolicy`, so the half's stated unknown on the live bytes is read here.
- **Not read by this lane (the issuer's close):** the ten-principal simulation and the two negative-arm simulations, run by the laptop lane.
- **Rollback, unused:** put `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1\PRIOR_opal-data-49financial_policy_20261011T152348Z.json` back as the bucket policy, verbatim, the same hour.
