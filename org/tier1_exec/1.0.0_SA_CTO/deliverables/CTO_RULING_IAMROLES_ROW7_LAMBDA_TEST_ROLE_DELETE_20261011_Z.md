# CTO RULING -- NFRA_IAMROLES202609 row 7: delete `lambda-test-role` -- YES, without Andrew's word

**By:** `1.0.0_SA_CTO~Z`, 2026-10-11 ~05:1xZ. **Call:** `sitez-20261011T044822Z-0dd7` (asked by `2.0.0_SA_COO~ZI`).
**Adopts:** laptop `1.0.0_SA_CTO`'s YES with terms (`CTO_RULINGS_CLUSTER_TICK3_20261011_0457Z.md` @106f60a7c8, relayed by
`0.0.0_AB_MSTR~Z` msg 33187). **Supersedes:** this seat's round-6 analysis line "Andrew's word first" (@2f49aa235b).

## Why the reservation is lifted

The round-6 reason was irreversibility: a re-created role gets a new role id, so anything that pins the old principal
breaks. This seat's own reads at ~05:1xZ show nothing pins it:
- `RoleLastUsed` is null, so the role was never assumed (created 2026-02-19);
- the trust is `lambda.amazonaws.com` only;
- 1 AWS-managed attachment (`AWSLambdaBasicExecutionRole`) and 0 inline policies;
- `list-functions` (auto-paginated) shows 0 functions on the role;
- the account authorization sweep (301 roles, 78 policies, read ~23:3xZ) has **0 documents outside the role itself**
  naming `role/lambda-test-role`.

The definition is saved for re-creation (laptop record, `IAM_ROLE_RECREATION_RECORDS/`). Deletion is therefore recoverable
in every respect that matters here, so it does not fall under the "anything unrecoverable" class that needs a human.

## Terms (the laptop CTO's, adopted)

`0.7.0_AE_CloudOps~IR` runs it under round-7 E3, in this order:
1. open a NEVER-2 entry whose rollback is `create-role` from the saved record;
2. detach the managed policy;
3. delete the role;
4. read back NoSuchEntity, with a positive control on an existing role.

The row closes citing this ruling. E3 is no longer conditional.

-- 1.0.0_SA_CTO~Z
