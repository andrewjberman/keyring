# ADVI_FIRMBKTS -- surprise channel, INVESTIGATION v1 (laptop fabric)

**Home:** the project tree's channel (`org/standards/PROJECT_TREE.contract.json` `surprise_channel_glob`);
the gate `.tools/surprise-row-gate.py` validates every NEW row (schema
`org/surprise_channel/schemas/investigation_item.schema.json`, identity, folder == project, the allocator
coordinate). Lane `ANY`.
**Id grammar (laptop fabric):** a seat's row is `ADVI_FIRMBKTS-S<k>`; a worker's row is
`ADVI_FIRMBKTS-W<n>-S<k>`; the CVO's adjudication rows live in `../adjudications/` as `ADVI_FIRMBKTS-C-S<k>`.
**Append-only.** Never edit an existing row.
**This file opened by** `0.7.0_AE_CloudOps` under the non-pipeline order `card3-read-logging`
(`org/tier2_senior/0.7.0_AE_CloudOps/task_orders/card3-read-logging-cot-org-trail-to-terraform-firmsep-drop-cot.md`
@`9674549204`, issuer `2.0.0_SA_COO~E`), whose `<surprise_channel>` names this file. Denominator at this
write: **1 row** (`S1`).

```json
[
  {
    "id": "ADVI_FIRMBKTS-S1",
    "project": "ADVI_FIRMBKTS",
    "fabric": "laptop",
    "surfaced_by": "0.7.0_AE_CloudOps",
    "surfaced_at": "2026-09-13T23:28:00Z",
    "one_line": "card3-read-logging Phase 2 cannot be met as written: portal-auth already plans one unrelated in-place update (aws_wafv2_web_acl.opal_cloudfront_protection) BEFORE any edit, so its apply would carry 2 changes, not 1, and R-AC12's 0-diff cannot read true without sweeping the WAF update -- the portal-auth apply, and the trail-selector apply sequenced behind it, are HELD.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "terraform -chdir=infra/aws/terraform/portal-auth plan -detailed-exitcode -input=false (.tools/terraform.exe v1.9.8, main tree, no edit by this seat), 2026-09-13 ~23:02-23:05Z: PLAN_RC=2, 'Plan: 0 to add, 1 to change, 0 to destroy.', the one change 'aws_wafv2_web_acl.opal_cloudfront_protection will be updated in-place'",
        "the change's body: three managed-rule-group rule blocks (ip-reputation p3, common-rule-set p4, known-bad-inputs p5) each REMOVED and RE-ADDED with the same name, priority, override_action count, vendor/name and visibility_config; the removed side carries '(1 unchanged attribute hidden)' inside managed_rule_group_statement and the added side does not",
        "aws wafv2 get-web-acl --scope CLOUDFRONT --region us-east-1 --name opal-cloudfront-protection --id a09833c0-4043-49fc-a92c-0dcdeaff9abd, same session: each of the three live ManagedRuleGroupStatements carries only VendorName and Name (no Version, no RuleActionOverrides, no ManagedRuleGroupConfigs) with OverrideAction Count -- the content the plan would re-add. The equality is GROUNDED; that the diff is a set-representation artifact rather than a content change is INFERRED",
        "git log -- infra/aws/terraform/portal-auth/waf-cloudfront.tf: last commit 3758b14afc 2026-09-04 00:46 (0.7.0_AE_CloudOps~T, NFRA_OPSEC202609), after 2026-09-03 commits by 0.7.0_AE_CloudOps~S and 0.7.0_AE_CloudOps~Z",
        "the order's Phase 2 step 1 <expect> 'Exactly 1 in-place update, aws_cloudwatch_event_rule.firmsep_s3_bypass; 0 to add; 0 to destroy.' and <if_mismatch> 'STOP. Unrelated drift in portal-auth is NOT swept into this apply; surface it as a row and hold.'"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "card3-read-logging Phase 2 step 1 expects the portal-auth plan to show exactly 1 in-place update (the FIRMSEP rule), R-AC12 expects 'terraform -chdir=infra/aws/terraform/portal-auth plan -detailed-exitcode' to read PLAN_RC=0 after the apply, and <do_not> forbids sweeping unrelated portal-auth drift into the apply.",
    "world_is": "Before any edit, portal-auth's full plan already reads PLAN_RC=2 on one unrelated resource, the CloudFront WAF ACL opal-cloudfront-protection, whose three managed-rule blocks plan as remove-and-re-add of content identical to live. A full apply would sweep an UpdateWebACL on the production front door into this order; a -target apply would satisfy the 1-change plan but leave R-AC12 unable to read 0. Choosing between them is not this seat's.",
    "notes": "HELD at the portal-auth apply; nothing in portal-auth is edited or applied. S0 (ledger card3-read-logging, opened 2026-09-13T23:26:28Z), S1 (the four pre-state captures) and S2 (the trail import to shared-infra at 0-diff, a state-only act that moves no selector) proceed, because none of them touches portal-auth or arms anything. S3's edits are NOT made or committed while held: a committed-but-unapplied selector change in the shared tree would let any other shared-infra apply turn on cot logging BEFORE the rule narrows -- the order this sequence exists to prevent. Routes for 2.0.0_SA_COO~E: (a) permit -target=aws_cloudwatch_event_rule.firmsep_s3_bypass and re-cut R-AC12 to accept the WAF update as the only remaining diff; (b) hold until the WAF diff's owner clears it; (c) another route. INERT: left alone it changes nothing live; the exposure is only that a future full portal-auth apply re-sends identical rules to the production WAF."
  }
]
```

```json
[
  {
    "id": "ADVI_FIRMBKTS-S2",
    "project": "ADVI_FIRMBKTS",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~E",
    "surfaced_at": "2026-09-14T00:01:41Z",
    "one_line": "card3-read-logging's S2 import put opal-organization-trail into shared-infra's REMOTE state, but its config exists only in checkouts at or after 9f3fd2cf4a. So a full shared-infra apply from ANY older checkout plans the organisation audit trail's DESTROY. That covers this device's older worktrees, origin/CLOUD until the next push, and SITEZ until the CLOUD->SITEZ merge. prevent_destroy cannot refuse it there, because prevent_destroy lives in the missing config.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "0.0.0_AB_MSTR -- the next CLOUD push (LD-0522, on Andrew's word), then the CLOUD->SITEZ merge. Each carries 9f3fd2cf4a's config to every checkout that pulls it. This device's older linked worktrees under .worktrees/ disarm only when they take CLOUD, or are removed.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "0.7.0_AE_CloudOps msg 96438 (2026-09-13T23:46:59Z). S2 declared the trail in infra/aws/terraform/shared-infra/cloudtrail-organization-trail.tf: the aws_cloudtrail resource only, prevent_destroy, an untagged provider alias. It was imported 23:37:27-23:37:35Z and R-AC2 read PLAN_RC=0 at 23:37:47Z; commit 9f3fd2cf4a. That seat recorded this exposure in the card3-read-logging ledger notes and did not remediate it.",
        "2.0.0_SA_COO~E, 2026-09-14T00:01:41Z, main tree. git merge-base --is-ancestor 9f3fd2cf4a CLOUD returns YES (the positive control). The same test against 82c00bd4ef (origin/CLOUD per git ls-remote at 23:55Z) returns NO, rc=1. Against c47fc5f8c9 (origin/SITEZ per the same ls-remote; object present locally, cat-file -t = commit) it returns NO.",
        "2.0.0_SA_COO~E, same time. git cat-file -e reports infra/aws/terraform/shared-infra/cloudtrail-organization-trail.tf PRESENT at 9f3fd2cf4a and ABSENT at 82c00bd4ef.",
        "2.0.0_SA_COO~E, native Grep of .tools/safe-apply.sh. The pattern 'destroy|DESTROY|to destroy|delete' matches only the TOMBSTONE pre-apply gate's comment block at :222-230 (a gate against RESURRECTING a deleted resource). There is no match for '-target|TARGET'. :274 and :291 forward \"$@\" to terraform. So safe-apply.sh itself carries no destroy refusal. NOT READ: halt-gate-check.sh, which it sources."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "card3-read-logging S2: 'Import the aws_cloudtrail resource ONLY -- its log bucket, bucket policy, KMS key and any other dependency stay unmanaged, referenced by literal. R-AC2 gates S3.' The order bounds the import's write set and requires a 0-diff plan from the importing checkout. It says nothing about checkouts that do not yet carry the new config.",
    "world_is": "The import is a write to a SHARED remote state, so it takes effect for every checkout at once, while the config that makes the state safe travels only by git. Until 9f3fd2cf4a reaches a checkout, a full shared-infra plan there reads the trail as state-without-config and plans its DESTROY. The controls that remain are terraform's interactive apply approval, which -auto-approve skips, and whatever halt-gate-check.sh does, which was not read.",
    "notes": "Surfaced by the order's issuer because the exposure comes from the order's own S2. It lands as an ARMED row rather than a ledger note (no disarm owner) or a broker message (never the carrier). NOT remediated here: no guard is built (CLAUDE.md 'never implement an approval gate unless Andrew explicitly asks') and no push is made (LD-0522). Candidate remedies, NONE adopted, each named with whose it is: (1) the CLOUD push and the CLOUD->SITEZ merge, the disarm owner's act on Andrew's word; (2) removing or refreshing stale linked worktrees that carry shared-infra, each worktree's owner's; (3) a safe-apply refusal of any plan that DESTROYS an aws_cloudtrail, which is an approval gate and so is Andrew's call alone. The order's S3 still proceeds: its trail apply runs from a checkout at or after 9f3fd2cf4a, so it is not exposed."
  }  ,
  {
    "id": "ADVI_FIRMBKTS-S3",
    "project": "ADVI_FIRMBKTS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-14T00:44:17Z",
    "one_line": "L8 INTAKE ON S2, RE-MEASURED: the origin half of S2's exposure is CLOSED -- origin/CLOUD 37931439cf now carries 9f3fd2cf4a and the trail's config -- but 22 linked worktrees on this device still carry shared-infra without it, and neither control S2 left unread refuses a plan that destroys a resource.",
    "class": "OBSERVATION",
    "spec_asserts": "ADVI_FIRMBKTS-S2: the exposure covers 'this device's older worktrees, origin/CLOUD until the next push, and SITEZ until the CLOUD->SITEZ merge'; the remaining controls are terraform's interactive approval 'and whatever halt-gate-check.sh does, which was not read'.",
    "world_is": "Measured 2026-09-14T00:44:17Z. ORIGIN: CLOUD is 37931439cf (ls-remote); 9f3fd2cf4a is its ancestor, and 37931439cf carries exactly 1 aws_cloudtrail block in shared-infra/cloudtrail-organization-trail.tf -- the push window Andrew granted ~00:0xZ (3accded80e) has landed it, so a checkout that pulls CLOUD is no longer exposed. SITEZ: SITEZ 28ccac62c9 is not in this clone, so its ancestry is UNREAD. THIS DEVICE: of 24 linked worktrees, 22 carry infra/aws/terraform/shared-infra at a HEAD that does not contain 9f3fd2cf4a (a further 1 are stale but carry no shared-infra); a full shared-infra apply from any of the 22 plans the organisation trail's DESTROY. THE UNREAD CONTROLS, read: .tools/safe-apply.sh (292 lines) names 'destroy' 1 time(s) and 'auto-approve' 0 time(s); .tools/halt-gate-check.sh (456 lines) names 'destroy' 0 time(s), 'auto-approve' 0 time(s) and 'cloudtrail' 0 time(s). Neither carries a rule that refuses a destroy plan, so terraform's interactive approval is the only control left, and -auto-approve skips it.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git ls-remote origin refs/heads/CLOUD -> 37931439cf; git merge-base --is-ancestor 9f3fd2cf4a 37931439cf -> yes",
        "git show 37931439cf:infra/aws/terraform/shared-infra/cloudtrail-organization-trail.tf -- 1 aws_cloudtrail block",
        "git worktree list: 24 trees; 22 exposed, each checked by merge-base --is-ancestor and a shared-infra directory test",
        ".tools/safe-apply.sh and .tools/halt-gate-check.sh read in full by a word count, printed in world_is"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "hazard_standing": "INERT",
    "notes": "INERT because the hazard is S2's and stays there, ARMED with 0.0.0_AB_MSTR as disarm owner; this row only re-measures its reach. What S2's disarm still waits on: the 22 exposed worktrees taking CLOUD or being removed (each worktree's owner; removal needs a human OK -- several are held for one), and the SITEZ leg as stated. The 22, by HEAD and path: 544877cc2e C:/tmp/staudt_layerD_T0; f177240b75 C:/tmp/staudt_layerD_T1; ae759bbb32 C:/tmp/staudt_layerD_T2; cd17755343 C:/tmp/staudt_layerD_T3; 1b51bf78a1 C:/tmp/wk-compeff-8-1; 87185ad3f2 C:/tmp/wk-dsgn-1e; b0b0d2202e C:/tmp/wk-etfs-3-21; 8ba3b35a57 C:/tmp/wk-etfs-3-30; 7ba94b5b46 C:/tmp/wk-etfs-3-31; 1082067648 C:/tmp/wk-irpt-2-2c; 86f2959ab1 C:/tmp/wk-irpt_fntend-4-1-fe-s-25; 55887ce562 C:/tmp/wk-irpt_fntend-4-2-fe-s-26; 10093a2dff C:/tmp/wk-irpt_fntend-4-3-fe-s-27; c0eb49d1e1 C:/tmp/wk-irpt_fntend-4-4-fe-s-28; 85259e922e C:/tmp/wk-irpt_fntend-4-5-fe-s-18; 6ad371c88e C:/tmp/wk-irpt_fntend-5-4-fe-s-29; c8cd12b2c0 C:/Users/AndrewBerman/Desktop/ajb_workspace/.worktrees/d13-visual-elevation; 3cbcba4f80 C:/Users/AndrewBerman/Desktop/ajb_workspace/.worktrees/krny-c3-access-pair-fixture-20260910; f303236817 C:/Users/AndrewBerman/Desktop/ajb_workspace/.worktrees/krny-c3-kernel-design-20260910; 32c3ef69b7 C:/Users/AndrewBerman/Desktop/ajb_workspace/.worktrees/krny-c3-offline-fixture-20260910; 985453d506 C:/Users/AndrewBerman/Desktop/ajb_workspace/.worktrees/krny-c3-report-admission-20260910; 8b24cd2bbf C:/Users/AndrewBerman/Desktop/scty-build. Not remediated and no guard built: a refusal of destroy plans would be an approval gate, which is Andrew's call alone (CLAUDE.md)."
  }
]
```
