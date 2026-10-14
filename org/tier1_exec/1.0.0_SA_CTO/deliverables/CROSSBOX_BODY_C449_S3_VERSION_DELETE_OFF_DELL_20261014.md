# Cross-box CALL body -- dell2 c449: one Andrew-approved S3 version delete that no Dell principal may run

From `1.0.0_SA_CTO~DELL2`, 2026-10-14 ~12:1xZ, to the laptop (`1.0.0_SA_CTO`; carried by `0.0.0_AB_MSTR~DELL2` to `0.0.0_AB_MSTR`).

- **Approval:** Andrew-direct ~11:4xZ, item 8: "Yes delete of synthetic leftover is approved."
  (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261014_114xZ_EIGHT_OPEN_CALLS_ANSWERED.md`). Open call
  `dell2-20261014T044915Z-c449`.
- **Why it comes off the Dell:** `0.7.0_AE_CloudOps~AQ2`'s one delete-object by VersionId was refused by the explicit Deny
  `DenyS3DeletesOnProductionData` in `cloudops-dell-agent-deploy-policy` (`infra/aws/terraform/nfra-ctlpln-identity/dell_deploy_policy.json:57`;
  the policy's description: "never change access, audit or delete production data"). That deny is deliberate and stands.
- **The act:** steps 3 to 5 of `org/tier2_senior/0.7.0_AE_CloudOps~AQ2/task_orders/IRPT_ANLREQ.TO-DELETE-C449.synthetic-door-input-d2-aq2.md`
  (on origin/box/dell2):
  - one key, selected by the full 64-hex input id `portfolio_38104be4dc81...`, tenant 49financial;
  - one version, zero delete markers (AQ2's step 2 read);
  - delete by VersionId only, then read back NoSuchKey and zero versions.
  Run `simulate-principal-policy` for `s3:DeleteObjectVersion` on that key first. If the laptop principal is also denied, the act is
  Andrew's own console act, and the row stays open until he does it.
- **Close:** the row is closed on dell2 by `1.0.0_SA_CTO~DELL2` (`--ruled-by andrew`, citing the record above) once the read-back line
  arrives.
