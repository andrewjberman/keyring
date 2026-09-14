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
  }
]
```
