# NFRA_GLOBGRPH — surprise channel, INVESTIGATION v1 (round 1, laptop fabric)

**Home:** `org/surprise_channel/NFRA_GLOBGRPH/INVESTIGATION_v1.md`  
**Append-only during round.** Denominator at this write: 2 rows.

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
  },
  {
    "id": "NFRA_GLOBGRPH-S2",
    "project": "NFRA_GLOBGRPH",
    "fabric": "laptop",
    "surfaced_by": "0.8.0_AE_CloudComp~K",
    "surfaced_at": "2026-09-03T16:27:14Z",
    "one_line": "After the authorized target-scoped lifecycle apply succeeded, the required unscoped control plan was 0 add / 10 change / 0 destroy rather than the amended acceptance's 0/1/0: nine API Gateway routes would lose CUSTOM authorization in addition to the known users-table drift.",
    "spec_asserts": "Issuer amendment 4fa04d9c1f and Msg-ID 93783 require the post-apply UNSCOPED shared-infra plan to be exactly 0 add / 1 change / 0 destroy with aws_dynamodb_table.opal_users_v2 deletion protection as the one change and NOTHING else, or 0/0/0 if TO-USERS-DELPROT lands first.",
    "world_is": "The fresh post-apply unscoped plan is 0 add / 10 change / 0 destroy: the known opal_users_v2 deletion_protection_enabled true -> null drift plus nine aws_apigatewayv2_route resources changing authorization_type CUSTOM -> NONE and authorizer_id naqxlm -> null. The lifecycle address is absent from the plan, but the NOTHING-else acceptance is false.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/tier2_senior/0.8.0_AE_CloudComp~K/deliverables/NFRA_GLOBGRPH.TO-MSHEAT-EXPIRY.safe-apply-output.txt ends Apply complete! Resources: 0 added, 1 changed, 0 destroyed for aws_s3_bucket_lifecycle_configuration.global_graph.",
        "The live post-read in NFRA_GLOBGRPH.TO-MSHEAT-EXPIRY.lifecycle-post-read.json has exactly two Enabled rules: abort-incomplete-mpu-7d with DaysAfterInitiation 7 and ms-heat-snapshots-expire-60d with prefix warehouse/ms_heat/snapshots/ and Expiration Days 60.",
        "NFRA_GLOBGRPH.TO-MSHEAT-EXPIRY.unscoped-post-plan.txt reports Plan: 0 to add, 10 to change, 0 to destroy after refreshing live state.",
        "The same unscoped plan names aws_dynamodb_table.opal_users_v2 plus nine routes: r_as2dsme, r_c0k8rl0, r_gwygx58, r_m8wdq80, r_mxus2bs, r_o2xr1ct, r_ruzaqhq, r_sogv7z9, and r_t81twif; each route would change CUSTOM -> NONE and naqxlm -> null.",
        "No unscoped apply was attempted; the unscoped plan was an acceptance read only and was not saved for application."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "The lifecycle act itself is landed and its live read-back passes. The existing lifecycle deploy ledger cannot close because L5 is false. The nine-route authorization drift is left untouched; issuer disposition is required."
  }
]
```

## Rows routed by 2.0.0_SA_COO~B1 (ADVI_FIRMBKTS round 3 analysis): comp-pipescript (org/modules/graph/pipeline_cli.py)

```json
[
  {
    "id": "NFRA_GLOBGRPH-D1-S1",
    "project": "NFRA_GLOBGRPH",
    "fabric": "dell1",
    "surfaced_by": "2.0.0_SA_COO~B1",
    "surfaced_at": "2026-10-11T11:38:38Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "one_line": "comp-pipescript io UNDER-REPORTS D_04's platinum WRITES (one printed, 25 in the code) and lists a READ as a write",
    "spec_asserts": "comp-pipescript io <script> --pipeline bd-gold --no-portal prints each script's WRITES (the order face of ADVI_FIRMBKTS FB-f-6 step 1).",
    "world_is": "Measured by worker ~16 on 2026-10-11: `io D_04 --pipeline bd-gold --no-portal --json` prints one write (partner_analytics_key); D_04 line 1974-1975 READS it. The 25 platinum writes go through _write_batch and _write_json_to_s3, which the graph does not resolve.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ADVI_FIRMBKTS-D1-W16-S1 in org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md",
        "org/modules/graph/pipeline_cli.py (the resolver behind the .tools shim)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Routed from ADVI_FIRMBKTS round 3 analysis (CTO, section 2). The ADVI_FIRMBKTS census used line reads and the AST read census, not the graph, for write attribution: the instruments of record there are the AST census and the builder's target list (CTO ADDENDUM 7). Routed to the tool's owner as one row."
  },
  {
    "id": "NFRA_GLOBGRPH-D1-S2",
    "project": "NFRA_GLOBGRPH",
    "fabric": "dell1",
    "surfaced_by": "2.0.0_SA_COO~B1",
    "surfaced_at": "2026-10-11T11:38:38Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "one_line": "comp-pipescript resolves 1 of the 26 E-series bd-gold ids, and E_01 and E_24 write served keys with no dispatch entry",
    "spec_asserts": "comp-pipescript io <script> --pipeline bd-gold prints each bd-gold script's writes, so every writer script can be read by its id.",
    "world_is": "Measured by worker ~16: 'Script not found' (rc 1) for 25 ids E_00..E_17 and E_19..E_25; only E_18 resolves. E_01 and E_24 write gold/artifacts keys with no E_ id in gold_dispatch.sh's CATALOG or PHASE_* blocks.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ADVI_FIRMBKTS-D1-W16-S3 in the ADVI_FIRMBKTS investigation channel",
        "comp-pipescript io E_01... output (rc 1)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Routed from ADVI_FIRMBKTS round 3 analysis (CTO, section 2). Routed as one row: the graph's script universe omits the E-series; the ADVI_FIRMBKTS round 3 close found E_01 non-served and E_24 dead by CloudTrail, which the graph could not."
  }
]
```
