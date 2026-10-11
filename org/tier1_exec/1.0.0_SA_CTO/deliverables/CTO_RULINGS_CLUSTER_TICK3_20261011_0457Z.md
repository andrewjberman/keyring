# CTO rulings -- cluster-lead tick 3 (2026-10-11 04:57Z)

Read: `python .tools/open-calls.py list --all --cloud` at 04:57:52Z: 4 of 4 boxes, 10 OPEN (act 10), 77 closed.
keep-driving scan=off empty_tick=off on all four. dell1 1b2f closed (31 closed); dell1 e7f2 stays HELD for Andrew.

## sitez-20261011T044822Z-0dd7 -- retire (delete) IAM role `lambda-test-role` (NFRA_IAMROLES202609 round 7 E3)

**Ruling: YES. Delete it, after its definition is on record (done below), so the only irreversible part (the role id) is
the only thing lost.**

Measured by this seat at 04:5xZ (one `get-role`, `list-attached-role-policies`, `list-role-policies`, `list-functions`):
- Created 2026-02-19T16:00:44Z; `RoleLastUsed` absent (never assumed).
- One attached policy, AWS-managed `AWSLambdaBasicExecutionRole`; zero inline policies.
- Zero Lambda functions reference it (`list-functions` filter on Role).
- Repo references: 8 hits over 10,153 files, all census or inventory artifacts (`infra/system/ontology/worldmodel/...`,
  `infra/aws/nfra_terraform_p1/*.json`), none a Terraform resource or code path.

Recreation record (so a delete is reversible by name, not by id):
`org/tier1_exec/1.0.0_SA_CTO/deliverables/IAM_ROLE_RECREATION_RECORDS/lambda-test-role_get-role_20261011.json` and
`..._attached_20261011.json` (trust policy, path, tags, attached policy ARN).

Terms: the owning site Z applier (`0.7.0_AE_CloudOps~IR`, under E3 cut by `2.0.0_SA_COO~ZI`) runs `aws iam
detach-role-policy` then `delete-role`, with a `get-role` NoSuchEntity read-back and one positive control, under a
NEVER-2 ledger entry whose rollback is `create-role` from the record above. Nothing else is in the blast radius.

Why this seat rules it: Andrew's cluster-lead word covers the open calls; the delete is bounded to one unused test role and
is recreatable from the record, so the human-confirmation class ("anything unrecoverable") does not reach it.

## Reserved to Andrew (unchanged): sitez 058e, 21c5, f0d2, 8ed7, a519 (moot); dell2 01c5, 3cb1, fbb1. Held for Andrew: dell1 e7f2 (PROD promote).
