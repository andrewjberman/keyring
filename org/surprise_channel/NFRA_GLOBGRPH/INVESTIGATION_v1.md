# NFRA_GLOBGRPH — surprise channel, INVESTIGATION v1 (round 1, laptop fabric)

**Home:** `org/surprise_channel/NFRA_GLOBGRPH/INVESTIGATION_v1.md`  
**Append-only during round.** Denominator at this write: 1 row.

```json
[
  {
    "id": "NFRA_GLOBGRPH-S1",
    "project": "NFRA_GLOBGRPH",
    "fabric": "laptop",
    "surfaced_by": "0.8.0_AE_CloudComp~K",
    "surfaced_at": "2026-09-03T15:48:48Z",
    "one_line": "The saved unscoped shared-infra plan is 0 add / 2 change / 0 destroy: it adds the ordered MS heat lifecycle rule but also removes live deletion protection from aws_dynamodb_table.opal_users_v2, so the exact 0/1/0 apply gate refuses it.",
    "spec_asserts": "The CTO gate GO (Msg-ID 93750) and the bound task order authorize safe-apply only when the saved plan is exactly 0 add / 1 change / 0 destroy on aws_s3_bucket_lifecycle_configuration.global_graph, followed by an unscoped 0/0/0 plan; any disagreement must STOP with no second apply.",
    "world_is": "The current unscoped saved plan is 0 add / 2 change / 0 destroy because it also proposes deletion_protection_enabled = true -> null on aws_dynamodb_table.opal_users_v2; therefore both the apply gate and the required post-apply unscoped 0/0/0 acceptance condition are unsatisfied.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "terraform show -no-color ms-heat-snapshots-expire-60d.tfplan reports Plan: 0 to add, 2 to change, 0 to destroy and names aws_dynamodb_table.opal_users_v2 plus aws_s3_bucket_lifecycle_configuration.global_graph.",
        "The saved-plan rendering reports aws_dynamodb_table.opal_users_v2 deletion_protection_enabled = true -> null while adding the expected Enabled 60-day warehouse/ms_heat/snapshots/ lifecycle rule.",
        "Live aws dynamodb describe-table for opal-users-v2 returned TableStatus ACTIVE, DeletionProtectionEnabled true, and ARN arn:aws:dynamodb:us-east-1:313476888478:table/opal-users-v2 before any apply.",
        "No apply command was run; infra/aws/terraform/shared-infra/ms-heat-snapshots-expire-60d.tfplan remains unconsumed evidence and must not be applied."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "The ordered S3 lifecycle pre-read and rebuildability statement remain valid. Work stopped at the saved-plan gate. No retry or second apply is permitted; issuer disposition is required before this order can continue."
  }
]
```
