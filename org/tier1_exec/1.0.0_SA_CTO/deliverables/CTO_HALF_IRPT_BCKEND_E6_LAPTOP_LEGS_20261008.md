# CTO never-widen half -- IRPT_BCKEND release 2 (E6), the laptop's legs (1.0.0_SA_CTO, 2026-10-08 ~19:3xZ)

**Read in full:** dell2's pair `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~Y2/release2_ycg/NEVER_WIDEN_PAIR_RELEASE2_E6.md`
(origin CLOUD, @8c11ac4ff1; pin 1b94d50b8c on origin) and the laptop order
`org/tier2_senior/0.7.0_AE_CloudOps/task_orders/IRPT_BCKEND.TO-APPLY-E6.ycharts-generate-partner-read-grant-and-fenced-admit-cleanup-laptop.md`
@4598d513c5 (2.0.0_SA_COO~C, msg 107155). **Not read:** the plan, the build, the served.py diff.
**Scope of this half:** the laptop's legs only. The code release and the test-row writes are dell2's, under dell2's own pair
and `1.0.0_SA_CTO~DELL2`'s rulings.

## What this half signs

- **Leg 0, the dry probe:** a conditional `delete-item` on a key that cannot exist in `irpt-requests`; expected
  `ConditionalCheckFailedException`. Writes nothing.
- **Leg 1, the grant:** one statement on `irpt-ycharts-generate-role`, `dynamodb:GetItem` on exactly `opal-partner-49financial`,
  `-cottonwood`, `-inflection` (not demo); targeted `0 add, 1 change, 0 destroy`; rollback = targeted apply at the pre-grant
  revision, read back by `iam get-role-policy`. In plain words: the report generator can look up one advisor's partner profile
  at those three firms, by email, and nothing else.
- **Leg 2, the fenced cleanup:** for each key in dell2's keys file only, `get-item`, `delete-item`, `get-item` NOT FOUND on the
  test admit's `irpt-requests` row. No other key is touched.

## Not signed here -- an act only Andrew can do

The test admit's S3 object (`head-object` / `delete-object` / `head-object` 404) is an S3 delete: CLAUDE.md Agent Autonomy
reserves S3 deletes for human confirmation. It stays held for Andrew's word, as the issuer wrote.

## Conditions

1. The issuer's order and dell2's pair conditions stand; branch B of the pair (roll back code, clean up, roll back the grant).
2. Leg 1 applies only after leg 0 reads `ConditionalCheckFailedException`; if leg 0 fails, nothing else runs and dell2 is told.
3. Leg 2 reads dell2's keys file and touches no key not in it; its result file goes back to dell2 via 0.0.0_AB_MSTR.

**SIGNED** -- `1.0.0_SA_CTO`
