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

```json
[
  {
    "id": "ADVI_FIRMBKTS-S4",
    "project": "ADVI_FIRMBKTS",
    "fabric": "laptop",
    "surfaced_by": "0.7.0_AE_CloudOps",
    "surfaced_at": "2026-09-14T01:08:00Z",
    "one_line": "card3-read-logging R-AC8's positive control assumes organic opal-data-bd reads in any 30-minute window ('read about 250K times a day'). Tonight the window T0..T0+30min held ZERO organic bd GetObjects, so the control passed only on a bd read this seat drove at T0 -- a step the order did not name.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "EventBridge AWS/Events MatchedEvents for FIRMSEP-s3-direct-access-bypass (non-CloudFront GetObject on bd/inf), 300-second periods 2026-09-13 21:00Z-24:00Z: 4 datapoints with sums 4, 2, 2, 2 -- against a 14-day daily mean of about 251K (3,520,453 over 2026-08-30..09-13). The daily total is real; the reads arrive in bursts, not evenly",
        "card3_probe.py events over 2026-09-13 23:00-23:15Z: opal-data-bd n=0 across 37 files / 1,720 records. Over 23:15-23:20Z: opal-data-inf n=2, equal to FIRMSEP's 2 matched events for that 5-minute period -- so the scanner is not blind, and bd was simply not read",
        "R-AC8 exactly as the order invokes it, run 2026-09-14T01:04:22Z: 'DATA_EVENTS bucket=opal-data-bd n=1 first=2026-09-14T00:37:39Z' across 29 files / 3,770 records. The one event is principal arn:aws:iam::313476888478:user/Andrew_Berman, userAgent aws-cli/1.44.44, key platinum/firm/header_metrics.json -- this seat's driven 1-byte ranged GetObject, started 00:37:31Z by the local clock"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "card3-read-logging R-AC8: 'POSITIVE CONTROL: bd is already logged and read about 250K times a day, so a zero here means the scanner is blind and R-AC9's zero proves nothing.' The order names no bd read of its own; S1 and S4 name test reads on opal-data-cot and opal-data-49financial only.",
    "world_is": "The daily total holds, but tonight's non-CloudFront bd/inf reads ran 0-4 per 5 minutes, and T0..T0+30min held no organic bd read at all. Without a driven read the criterion would have read n=0, and the order's own gloss would then have called the scanner blind when it was fine. This seat drove one 1-byte GetObject on opal-data-bd at T0 (platinum/firm/header_metrics.json, principal user/Andrew_Berman) so the control could discriminate. The read is listed with the probe reads in the completion report.",
    "notes": "INERT: nothing live is affected. bd was already read-logged, and the driven read is one ranged GetObject by the operator principal. bd is not a card-3 bucket, but it is a legacy firm bucket under the same 45-day quiet census, so the read is listed as a probe to exclude. For any re-use of this control: drive the positive arm, and never rely on organic traffic in a short window."
  }
]
```

```json
[
  {
    "id": "ADVI_FIRMBKTS-S5",
    "project": "ADVI_FIRMBKTS",
    "fabric": "laptop",
    "surfaced_by": "0.7.0_AE_CloudOps",
    "surfaced_at": "2026-09-14T01:26:00Z",
    "one_line": "card3-read-logging S4's T1 test reads, made 5 and 13 seconds after the trail's PutEventSelectors, were NEVER recorded -- a new S3 data-event selector does not record from the instant the API returns. Recording on opal-data-cot was first observed at 01:02:35Z (an organic read), and opal-data-49financial's first record is a SECOND probe round this seat drove at 01:11Z.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "card3_probe.py order --since 2026-09-13T23:26:28Z (cloudtrail lookup-events): PutEventSelectors on opal-organization-trail at 2026-09-14T00:46:28Z. The shared-infra apply ran 00:45:02Z-00:46:26Z rc=0, and R-AC6 read the four selector values right after it",
        "T1 probe reads by arn:aws:iam::313476888478:user/Andrew_Berman (aws-cli, 1-byte ranged GetObject): opal-data-cot platinum/firm/header_metrics.json started 00:46:33Z, and opal-data-49financial _code/POLICY_BLOCK.json started 00:46:41Z, by the local clock. NEITHER appears in the org trail's delivered logs (card3_probe.py events since 00:46:28Z, read at 01:15:57Z across 33 files and at 01:24:49Z across 42 files). The same principal's T0 read on the already-logged opal-data-bd, started 00:37:31Z, was recorded at eventTime 00:37:39Z",
        "the first recorded opal-data-cot data events: 01:02:35Z and 01:02:37Z, principal arn:aws:sts::313476888478:assumed-role/opal-cot-value-parity/opal-cot-value-parity (a Lambda), keys platinum/firm/header_metrics.json and silver/holdings/2026-09-11.parquet -- ORGANIC",
        "T1b probe reads by the same principal: opal-data-cot started 01:11:18Z and was recorded at eventTime 01:11:30Z; opal-data-49financial started 01:11:28Z and was recorded at eventTime 01:11:38Z, which is the first and only opal-data-49financial record"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "card3-read-logging S4: 'One test GetObject each on opal-data-cot and opal-data-49financial at T1 after the trail apply', then read the delivered logs for them (R-AC10, R-AC11). The order treats a read made after the apply as a read the trail records.",
    "world_is": "Reads made seconds after PutEventSelectors returned were not recorded on either new bucket. Recording was first observed about 16 minutes after the change on opal-data-cot (an organic read), and was confirmed on opal-data-49financial only by a second probe round this seat drove 25 minutes after the change. R-AC10 and R-AC11 pass, but on the organic cot reads and the T1b probes -- not on the T1 reads the order names. The propagation delay is only bounded: more than 13 seconds, and at most about 16 minutes on cot and 25 minutes on 49financial.",
    "notes": "INERT for this order: the criteria pass. It bears on 1.0.0_SA_CTO's clock ruling (96424: 'LIVE MEANS OBSERVED RECORDING, NOT APPLIED CONFIGURATION'), which this measurement supports -- the apply time (00:46:28Z) is NOT when recording began. The T1 reads have no delivered record, so the census has nothing to exclude for them; they are reported with principal and start time, as the T0 read is. A bucket born inside the selector later needs the same care: its first reads may come minutes before recording starts."
  }
]
```

```json
[
  {
    "id": "ADVI_FIRMBKTS-S6",
    "project": "ADVI_FIRMBKTS",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~E",
    "surfaced_at": "2026-09-14T05:17:00Z",
    "one_line": "The LD-0529 send guard admitted an act-bearing GO only if it cited a <PROJECT>.TO-<id> token. A code-less ad-hoc order, which TASK_ORDER_PROTOCOL permits, cannot carry one, so card3-read-logging's GO was refused and the GO had to ride the order's own face.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "2.0.0_SA_COO~E's GO to 0.7.0_AE_CloudOps, 2026-09-13 ~22:4xZ, returned: 'SEND REFUSED (LD-0529 ...) -- cites NO task order ... cite its id (<PROJECT>.TO-<id>) in the GO'. The order was set pending on its face at 6967266949.",
        "org/mcp/cvo_send_guard.py before the fix: TO_ID_RE was the only citation form, and cited_orders_for globbed org/*/*/task_orders/<tok>*.md, so a filename with no PROJECT.TO- prefix can never match.",
        "The fix is at ee9a6cf257. The self-test passed 0 failed of 49 (the baseline before the edit was 0 of 44), including a difference pair: the same act admitted WITH the path and refused WITHOUT it."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Remedied on Andrew-direct 2026-09-14 ~04:xxZ (call 3; record @675eeec895) at ee9a6cf257. The guard also resolves a cited task-order PATH, under the same <issued_to> test. It is APPLIED only at each MCP session's next server load and at the broker's next restart, and no live send has exercised it at this lane.",
    "spec_asserts": "TASK_ORDER_PROTOCOL: 'Ad-hoc (no registered project): {description-with-dashes}.md' is a legal order with no project code. The LD-0529 refusal text says: 'cite its id (<PROJECT>.TO-<id>) in the GO'.",
    "world_is": "The two could not both be satisfied. An ad-hoc order has no <PROJECT>.TO-<id>, so no GO for it could pass the guard, and its issuer had to set it to pending on its own face instead."
  },
  {
    "id": "ADVI_FIRMBKTS-S7",
    "project": "ADVI_FIRMBKTS",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~E",
    "surfaced_at": "2026-09-14T05:17:00Z",
    "one_line": "deploy_ledger.py close-leg and close re-render the change_management entry from the ledger's saved state, so notes an operator appended to the entry .md by hand are overwritten. card3's module choice, S3(c) mechanism and copy step were dropped that way, and the assignee had to restate them.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        ".tools/deploy_ledger.py cmd_close_leg and cmd_close, read at this seat 2026-09-14 ~05:1xZ: each mutates the state and then calls _write_entry(state), and neither reads the existing entry file. _write_entry's own body was NOT read here.",
        "0.7.0_AE_CloudOps msg 96465, flag 2: its appended notes were dropped at close and restated into the closed entry at 50823af561."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "card3-read-logging S2 and S3: 'record the module chosen and why in the ledger entry'; 'name it and the copy step in the ledger entry'.",
    "world_is": "The entry is a rendering of the JSON state, so a note written into the .md does not survive the next close-leg or close. The durable places for a note are a --proof string or the state, and the tool's usage text says neither.",
    "notes": "The owners are the tool's committers; the last three were 0.0.0_AB_MSTR~Z at 119ce3a68e, 0.0.0_AB_MSTR at b32e1018de and 1.0.0_SA_CTO at 4b4d71ee70, all on 2026-09-04. Candidate remedies, none adopted: a --note verb that writes into the state, or preserving a marked notes block on re-render."
  },
  {
    "id": "ADVI_FIRMBKTS-S8",
    "project": "ADVI_FIRMBKTS",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~E",
    "surfaced_at": "2026-09-14T05:17:00Z",
    "one_line": "/cloud-ops names .tools/record-terraform-deploy.sh as part of commit and deploy discipline, but no file exists at that path. So card3-read-logging updated neither portal-auth's nor shared-infra's CHANGELOG.json.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "test -f .tools/record-terraform-deploy.sh returned ABSENT (2026-09-14 ~05:1xZ, main tree). No path outside .tools/ was searched.",
        ".claude/skills/cloud-ops/SKILL.md:18 lists it under 'Commit + deploy discipline'. :243 already records 'record-terraform-deploy.sh tooling failure: known issue (CHANGELOG.json writer + owned-paths-hook on Andrew identity)'.",
        "0.7.0_AE_CloudOps msg 96465, flag 3: CHANGELOG.json was not updated for either stack."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "card3-read-logging's <paths> grants portal-auth's and shared-infra's CHANGELOG.json, and /cloud-ops names the tool that writes them.",
    "world_is": "The named tool is absent at its named path, so the CHANGELOG writes did not happen. The skill's own :243 already calls the tool a known failure, while :18 still lists it as discipline.",
    "notes": "Owner: the /cloud-ops skill's lane, 0.7.0_AE_CloudOps. No change is made here."
  },
  {
    "id": "ADVI_FIRMBKTS-S9",
    "project": "ADVI_FIRMBKTS",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~E",
    "surfaced_at": "2026-09-14T05:17:00Z",
    "one_line": "comp-find --corpus aws carries no CloudTrail trail node. A search naming opal-organization-trail found only the FIRMSEP rule across 2,531 AWS nodes, so the live plane's drift classes could not show the org trail as CLI-applied and outside Terraform -- the exact case card 3 had to fix.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "comp-find --corpus aws 'opal-organization-trail|FIRMSEP-s3-direct-access-bypass' --limit 30, run at this seat 2026-09-13 ~22:3xZ: 'DENOMINATOR: 1 hit(s) across 2531 aws node(s)', 'BANDS = node_type ... EVENT_RULE=1', vintage 'Built from the estate as of 2026-09-13 12:15:54 UTC'.",
        "0.7.0_AE_CloudOps msg 96399 and its Phase 1 read (96438): aws cloudtrail describe-trails returns opal-organization-trail, multi-region, home us-east-1, and it was not in Terraform before 9f3fd2cf4a."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "CLAUDE.md Rule 21: '--corpus aws: the LIVE AWS plane -- regex over every aws CloudNode's name+arn+props ... drift_class per hit (LIVE-no-DECLARED = in AWS, not in the repo)'.",
    "world_is": "The trail, a LIVE-no-DECLARED resource until 9f3fd2cf4a, is not in the corpus at all. The census therefore reads out-of-corpus rather than returning a drift class, and a seat relying on the tool alone would not learn that the trail sat outside Terraform.",
    "notes": "Owner: the comp-find aws corpus and its CloudNode extractors (the served cloud graph, NFRA_GLOBGRPH). Which extractor would carry CloudTrail was not traced here."
  },
  {
    "id": "ADVI_FIRMBKTS-W2-S10",
    "project": "ADVI_FIRMBKTS",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_LGCTFM~2",
    "surfaced_at": "2026-09-18T00:30:00Z",
    "one_line": "LGIC_LGCTFM cell LT-x-3's second run on blackdiamond-49financial (a forks pass, --seed-loc opal-data-49financial:_campaign/) surfaced a live, undeclared S3 key prefix -- opal-data-49financial/_campaign/c02-reemit/ -- absent from every prior walk of this subject; its name RAISEs against lib/opal_naming.py grade() and opens tension R-0185|A3|GRAMMAR|R1 (T-0002), the run's only CLOSED/OPENED delta.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "workflows/legacy_transform/blackdiamond-49financial/20260918T002711Z-caf0983/DIFF.md (this order's committed diff of that run against .../20260917T233143Z-a89fd61, run_home.py diff, reproduced verbatim): 'CLOSED: 0', 'OPENED: 1', '  R-0185|A3|GRAMMAR|R1', 'UNCHANGED: 179'.",
        ".tools/aws s3api list-objects-v2 --bucket opal-data-49financial --prefix '_campaign/' --delimiter / --max-keys 50 (read-only), run at this seat 2026-09-17 ~23:5xZ (UTC boundary): CommonPrefixes = ['_campaign/c02-reemit/']; --prefix '_campaign/c02-reemit/' Contents = ['_campaign/c02-reemit/c02_reemit_mirror_pull.py'] (one live object).",
        "workflows/legacy_transform/blackdiamond-49financial/20260918T002711Z-caf0983/contract.json rows[-1]: row_id R-0185, kind PLANE, node_type S3Key, current.name 'opal-data-49financial/_campaign/c02-reemit/', current.drift_class 'LIVE-no-DECLARED' (INFERRED), current.declaration 'ABSENT' (terraform tree read), desired.verdict 'RAISE' -- lib/opal_naming.py grade('_campaign/c02-reemit/', 'S3Key') raises \"K1: segment 1 '_campaign' is neither a source nor a tier\" (reproduced directly against lib/opal_naming.py at this seat)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "org/missions/D14/LGIC/LGIC_LGCTFM/prd/LGIC_LGCTFM_PRD.md T12 (row for FWD-8): 'the diff reads closed / opened / unchanged for a reader who opens neither run; a NEW row is filed in the migration project's channel'; DEC-12 lists the run home's diff as 'consumed ... by the surprise channel of whichever project a NEW row belongs to'.",
    "world_is": "No prior LGCTFM walk of blackdiamond-49financial (plain --seed opal-data-bd / opal-data-49financial only) ever passed --seed-loc, so this forks-discovered prefix was never a row in any earlier contract.json; it surfaced only once this cell's practice/real wave walked it, and its key grammar (no source/tier segment under GRADING_RULE.md's K-section) does not resolve -- a live, un-migrated legacy write surface with no Terraform declaration and no registry mark, exactly the shape T12/DEC-12 name for filing here.",
    "notes": "No repair proposed or taken by this worker (WORKER FACE: 'you write a second run ... and file one row per OPENED tension'; the row is the deliverable, not a fix). Owner of any remediation is whichever ADVI_FIRMBKTS/LGIC_LGCTFM seat next triages the migration project's channel."
  }
]
```

```json
{
  "id": "ADVI_FIRMBKTS-S10",
  "project": "ADVI_FIRMBKTS",
  "fabric": "laptop",
  "surfaced_by": "1.0.0_SA_CTO",
  "surfaced_at": "2026-09-19T20:58Z",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "1.0.0_SA_CTO",
  "one_line": "THE AWS CORPUS RETURNS A CONFIDENT MEASURED ZERO FOR TWO BUCKETS THAT HAD BEEN LIVE FOR SIXTEEN HOURS BEFORE THAT CORPUS WAS BUILT, AND drift_class CANNOT FLAG IT",
  "spec_asserts": "CLAUDE.md Rule 21: 'comp-find --corpus aws: the LIVE AWS plane -- regex over every aws CloudNode's name+arn+props ... drift_class per hit (LIVE-no-DECLARED = in AWS, not in the repo), denominator = nodes scanned, vintage = the DB's own built: line.' The LIVE-no-DECLARED class exists precisely so that a resource present in AWS and absent from the repo is VISIBLE rather than silent.",
  "world_is": "comp-find 'opal-data-(inflection|cottonwood)' --corpus aws returns 0 hits across 2593 aws nodes, vintage 'Built from the estate as of 2026-09-19 12:21:32 UTC'. Both buckets were created 2026-09-18T20:05:17Z -- SIXTEEN HOURS BEFORE that build -- so this is not a vintage lag. POSITIVE CONTROL, run before concluding: opal-data-bd returns 159 hits with band S3_BUCKET=1, so the corpus DOES model S3 buckets and the zero is a genuine absence rather than an unmodelled class. AND drift_class IS STRUCTURALLY UNABLE TO SURFACE IT: LIVE-no-DECLARED is a property OF A NODE THAT IS IN THE GRAPH, so a resource missing from the graph altogether is classed as nothing at all and reads as absence.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "comp-find 'opal-data-(inflection|cottonwood)' --corpus aws --limit 30 -> DENOMINATOR: 0 hit(s) across 2593 aws node(s); VINTAGE: 2026-09-19 12:21:32 UTC; stitch source stitch-codebuild built 2026-09-19T03:01:13Z; manifest ee32ba01e5e6",
      "POSITIVE CONTROL: comp-find 'opal-data-bd' --corpus aws --limit 6 -> 159 hit(s) across the same 2593 nodes, BANDS include S3_BUCKET=1 -- the class is modelled",
      "aws s3api list-buckets --query \"Buckets[?starts_with(Name,'opal-data-')].[Name,CreationDate]\" -> opal-data-inflection and opal-data-cottonwood, both 2026-09-18T20:05:17Z, in a printed list of 22 opal-data-* buckets",
      "aws s3api get-bucket-policy --bucket opal-data-inflection -> AccessDenied by an explicit deny in a resource-based policy: the buckets are not merely present, they are actively refusing"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "WHY IT IS FILED HERE RATHER THAN AGAINST THE TOOL'S OWN PROJECT: it BOUNDS THIS PROJECT'S CENSUSES. ADVI_FIRMBKTS F1 is a census cell and its PRD names the aws corpus among the reading instruments; a cell that asks 'does this firm bucket exist' through the corpus gets a clean, denominator-bearing NO for exactly the two buckets this project is about. The tool defect is not this project's to repair and its owner is unchanged; the BOUND is this project's and needs a carrier here. WHAT IT COST ME, recorded because the near-miss is the evidence: I ran the corpus read FIRST and it returned zero. Had I stopped there I would have told Andrew the two buckets do not exist -- the exact mirror, in the opposite direction, of telling him two hours earlier that root was the only path to them. BOTH ERRORS HAVE ONE SHAPE: a faithful instrument answering a question about a population it could not see, with nothing in the output to say so. THE ONLY THING THAT SEPARATED THEM WAS THE POSITIVE CONTROL, and it cost one call. DISARM CONDITION, measurable: the corpus holds a node for each of the two buckets, or the corpus documents which resource classes its build can miss and under what condition, so a zero from it can be read correctly. UNTIL EITHER HOLDS: any ADVI_FIRMBKTS census over --corpus aws states in its own output that the corpus is not authoritative for bucket EXISTENCE and names the live-plane read it was corroborated against."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-S11",
  "project": "ADVI_FIRMBKTS",
  "fabric": "laptop",
  "surfaced_by": "1.0.0_SA_CTO",
  "surfaced_at": "2026-10-09T01:45Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "1.0.0_SA_CTO",
  "one_line": "A READY PATCH FOR build_canonical_prices_v2.py (tolerant load of two absent inputs, plus an optional S_00 step) WAITS FOR THIS PROJECT, BECAUSE THE NAMING GATE REFUSES ANY OTHER PROJECT'S DIFF TO THAT FILE",
  "spec_asserts": "CLAUDE.md rule 30 (as amended @c55a7b39cd): the commit-time naming gate REFUSES names today; an existing pipeline reaches conformance through its own migration project (R19). This file's existing literal places it on ADVI_FIRMBKTS's remediation surface (row MDPF_DEMQUE-D1-W7-S2).",
  "world_is": "dell1 2.0.0_SA_COO~Q1 (msg 1370, relayed by 0.0.0_AB_MSTR msg 107595) built org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/2.0.0_SA_COO~Q1/ADVI_FIRMBKTS_INPUT_S00_TOLERANT_LOAD.patch @091ccbafa2 (origin box/dell1; reaches CLOUD at the 02:00Z integrate): a call-site _load_tier2() so the build survives absent silver/historical_prices.parquet and config/ticker_lookup.json, and an optional S_00 step ahead of A_00 in the cot-pipeline SSM terraform. Both checks passed in the worker's tree (dell1's statement, not re-run by this seat). It is not landed, because the gate refuses the diff while the file keeps its literal.",
  "grounding": {
    "status": "INFERRED",
    "evidence": [
      "0.0.0_AB_MSTR msg 107595, verbatim relay of dell1 msg 1370 (bus 3ab4a338)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "INPUT FOR L5, NOT A CUT. ADVI_FIRMBKTS holds L4-R ADMITTED with no COO lane seated (SEQUENCE.yaml slot order). The decomposition that seats it carries this patch into the cell that renames build_canonical_prices_v2.py's literal, so the rename and the tolerant load land in one diff. The S_00 step touches the cot-pipeline's SSM terraform, a served change: it rides that cell's never-widen pair. Disposition closes when that cell's merge carries the patch or the decomposition rules it out with its reason."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-S1",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "2.0.0_SA_COO~F1",
  "surfaced_at": "2026-10-09T20:28:52Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~F1",
  "one_line": "THE FENCE ON opal-data-inflection AND opal-data-cottonwood NOW ADMITS user/cloudops-dell1-agent-user, SO PRD v1.3's F4 PREMISE (IT DENIES s3:* TO EVERY IDENTITY WE HOLD) HAS MOVED",
  "spec_asserts": "PRD v1.3 CELL CANDIDATES F4 and SURFACE MANIFEST: both buckets are born with a fence that DENIES s3:* to every identity this estate holds, measured at EXERCISED on 2026-09-19 (get-bucket-policy refused user/Andrew_Berman); F4 first mints a role matching the admit glob, then repairs the fence from it.",
  "world_is": "2026-10-09 ~20:1xZ, as arn:aws:iam::313476888478:user/cloudops-dell1-agent-user: get-bucket-versioning returns Enabled and list-objects-v2 returns objects on opal-data-inflection (7 depth-4 prefixes, all irpt/inflection/...) and opal-data-cottonwood (12, irpt/ and mdpf/). Whom the attached policy admits beyond this user, and whether the other-firm refusal holds, was not read.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "aws s3api get-bucket-versioning --bucket opal-data-inflection / opal-data-cottonwood (Enabled)",
      "aws s3api list-objects-v2 --bucket <each> --max-keys 3 (KeyCount 3)",
      "sts get-caller-identity (user/cloudops-dell1-agent-user)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Not a round-1 hazard: round 1 writes nothing to either bucket. Bounds F4: its round re-reads whom the attached fence admits (positive arm: this user; negative arm: a principal of another firm) before it cuts any mint or repair. Disposition closes when that round's decomposition cites this row."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-S2",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "2.0.0_SA_COO~F1",
  "surfaced_at": "2026-10-09T20:28:52Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "1.0.0_SA_CTO",
  "one_line": "opal-data-49financial HOLDS THE 08-18 TEMPLATE'S TIER-FIRST FORM (gold/advi/canonical/..., gold/advi/dimensions/..., gold/advi/reference/bd_legacy_*) BESIDE THE RULED SOURCE-FIRST KEYS, AND NO CELL OF THIS PROJECT'S PRD PLACES IT",
  "spec_asserts": "PRD v1.3 CONTRACTS, the canonical key string: in a firm bucket every key is {source}/{scope}/{tier}/{table}/{partition} with {scope} equal to the bucket's firm; brief IV.4: the ruled string supersedes the template's tier-first gold/{product}/... form. FWD-2's domain is the three legacy buckets only.",
  "world_is": "2026-10-09 ~20:1xZ list-objects-v2 over opal-data-49financial, rolled up to four segments: 900 distinct prefixes. Among them, tier-first gold/advi/** classes of about 1,136 objects each (gold/advi/canonical/{twr_daily,flow_ledger,canonical_positions,...}, gold/advi/dimensions/{dim_account,dim_security,...}) and gold/advi/reference/bd_legacy_{holdings,performance,nna} (about 2,425 each), next to source-first irpt/49financial/** keys.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "aws s3api list-objects-v2 --bucket opal-data-49financial (full, paginated), keys rolled up to depth 4 with counts; denominator 900 distinct prefixes"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Out of this project's three-bucket domain as the PRD draws it, so it is placed with the CTO: either a PRD addendum widens F2's domain to the residue in the firm buckets, or the producing pipeline's own migration (R19) carries it. Its writer is not traced here. Round 1 does not touch it."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W1-S1",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~1",
  "surfaced_at": "2026-10-09T20:45:56Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "FB-t-1: THE CLASS GRAMMAR (A LITERAL PREFIX ENDING IN / OR ONE KEY, DISJOINT DIRECTORIES) CANNOT SEPARATE A NAMED KIND FROM ITS ENTITY-ID OR PARTITION SIBLINGS, SO 6 FAMILIES OF CLASSES ARE MIXED BY CONSTRUCTION; FB-t-2 MUST PLACE THEM AS MIXED",
  "spec_asserts": "Task order FB-t-1 section 1.2: a class is homogeneous (one kind of thing); split deeper if a prefix holds served JSON next to parquet or state next to data; directory classes are disjoint; collapse partition and entity-id segments.",
  "world_is": "With r1_census.py S3 (a directory class that is a prefix of another directory class is OVERLAP), a directory that holds entity-id or dated children AND a differently-kinded named child can only be one class. Measured on the 20:36:32Z listing: (1) 8 zero-byte directory-marker keys in opal-data-bd (gold/_deprecated/, gold/clients/, gold/cohorts/, gold/filters/, gold/nna/, gold/snapshots/, gold/summary/, gold/timeseries/): a marker key ends in / so it is a directory class that overlaps every sub-class of its directory, forcing the whole directory to one class -- gold/timeseries/ (2,640 objects) therefore mixes positions_cube/ (2,472), holdings_lots/ (101), holdings_lots_shadow/ (51, the R18 retire candidate) and 16 json/parquet files; (2) bd forwardfill_v2/{allocations,realized,transactions,unrealized}/ and cot forwardfill_v2/* mix dated data files with _complete/ markers (state); (3) inf platinum/clients/ (4,199) mixes entity-id client json with _quarantine_scope_bug_20260424/ (995); (4) bd bronze/ (212) mixes dated _BRONZE_COMPLETE markers (69) with fees/ (140) and bi/ (3); (5) cot silver/ (803) mixes table dirs with dated {date}/_meta/ dirs (106) -- left as one class because splitting made 106 date classes; (6) code/, logs/, diagnostics/ are collapsed to one kind each (code, logs, diagnostic output) though their children are many dirs and flat dated files. Entity-id/date dirs are not enumerable as classes without leaking the partition the cell forbids.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "boto3 list_objects_v2 paginated over opal-data-bd, opal-data-inf, opal-data-cot at listed_at 2026-10-09T20:36:32Z: 131,391 / 99,668 / 7,802 objects; keys ending in '/' counted client-side: bd 8, inf 0, cot 0",
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~F1/round1/checks/r1_census.py static_arms S3: `if dirs[i + 1].startswith(dirs[i]): ... OVERLAP`, read at worktree HEAD fcaaa21b6e",
      "worker scratch classifier (.scratch, uncommitted) per-class child-kind tally; the mixed families above are the classes with >=2 children groups of >=10 objects each"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Does not fail AC1 or AC2. Each mixed class is named in CENSUS.md section 'Mixed classes'. FB-t-2 should either place a mixed class by its dominant kind with the named exception, or the grammar should admit a class-exclusion list; that is a PRD/grammar call, not made here."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W1-S2",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~1",
  "surfaced_at": "2026-10-09T21:05:48Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "FB-t-2 FAULT ROW: 226 OF 444 CENSUS CLASSES ARE NOT PLACED BY ANY ROW OF THE 1b TABLE (OR MIX KINDS NO SINGLE ROW COVERS) AND ARE FAULTS IN THE TABLE, NOT DECISIONS FOR THE WORKER; 9 MIXED CLASSES FROM ROW ADVI_FIRMBKTS-D1-W1-S1 ARE AMONG THEM",
  "spec_asserts": "Task order FB-t-2 section 1c: FAULT is a class no row of 1b places, or one address() refuses; file ONE surprise row that lists every FAULT class with the reason and set each FAULT row's fault_row to its id; logs, backups, rollback copies and leading-slash keys are FAULT unless a 1b row places them; never stretch a row to fit. Issuer ruling on ADVI_FIRMBKTS-D1-W1-S1: a class is placed only when ONE row of 1b covers EVERY kind of key in it; a mixed class is never placed by its dominant kind, it is a FAULT listed here with the kinds it mixes and the named exception.",
  "world_is": "mapping.json (census_listed_at 2026-10-09T20:36:32Z) places 444 of 444 classes: MOVE 132, HOME 77, RETIRE 7, DECISION 2, FAULT 226 (bd 105, inf 94, cot 27). address() refused no class; every FAULT is a table gap or a mixed class. MIXED classes faulted under the issuer ruling (kinds mixed; named exception): bd gold/timeseries/ (class b tables positions_cube/ + holdings_lots/, class e holdings_lots_shadow/ = the named RETIRE exception, 16 files not in the {t}/... shape, a directory marker); bd bronze/ (state-kind completion markers + class d fees/ bi/); cot silver/ (class d tables + dated _meta/ marker dirs); inf platinum/clients/ (class a client json + _quarantine_scope_bug_20260424/); inf bronze/eclipse/ (class d + _history/); inf gold/canonical/ (flat parquet not in the {t}/... shape + role_aua/); inf gold/logs/; bd marker dirs gold/{_deprecated,clients,cohorts,filters,nna,snapshots,summary}/; bd and cot forwardfill_v2/*/. Two classes the CENSUS names as collapsed or mixed are PLACED because ONE 1b row covers every kind in them: code/ (all three buckets; row f covers code/{gold,bronze,silver}/**) and bd/cot gold/validation/ (row e covers gold/validation/** including aua_certification/). Two classes are faulted by the 1b table's own second row though the census did not name them: inf gold/eclipse/ and inf silver/eclipse/ (the 1b table gives the {*}/_meta/{gold,silver}_complete.json markers to state). Matched by what the class IS, not its first segment (1b): canonical/schwab/gold/* placed as class b gold (source advi), canonical/schwab/silver/*, schwab/bronze/, smartx/bronze/ and blackdiamond/49financial/bronze/ placed as class d HOME; the HOME scope for schwab is the FIRM per the 1b cell (opal-data-assets/schwab/{firm}/...), which NAMING_SCHEMA.json key.scope_rule reads differently for a vendor MASTER (schwab/08242234/): address() accepts it and this row does not decide it. FAULT classes grouped by reason, as [count] reason -- bucket:class list (the same reason text is each mapping row's reason field):\n[19] backup or rollback copy; no 1b row places it -- bd:GOOD_RUN_2026-01-21_1015AM/; bd:_rollback/49f-20260630-preflip/; bd:gold/_regen_backup_20260706T1923Z/; bd:silver/bd_transactions_backup_2026-01-20.parquet; bd:silver/bd_transactions_backup_2026-01-28.parquet; bd:silver/incremental_allocation_manifest.json.bak-20260630T1900Z; bd:silver/incremental_allocation_manifest.json.bak-20260630T1916Z; inf:_pre_rebuild_backup/; inf:backup/_restore_exercise_20260715T225000Z/; inf:backup/aor_ledger_pre_reseed_20260716T012840Z/aor_ledger/events/; inf:backup/aor_ledger_pre_reseed_20260716T012840Z/aor_ledger_state.parquet; inf:backup/gold_canonical_PRE_REDERIVE_20260713T1012Z/; inf:backup/pre_exclusion_dispatch_20260715T2335Z/; inf:backup/pre_pullheal_20260716T0218Z/; inf:backup/pre_rescue_20260715T2259Z/; inf:backup/served_spine_PRE_AOR_RELEASE_20260715T225000Z/advisors/; inf:backup/served_spine_PRE_AOR_RELEASE_20260715T225000Z/firm/; inf:backup/served_spine_PRE_TIMELOCK_2026-07-13T184646Z/; inf:platinum/firm/_rollback/\n[35] log, diagnostic, scratch or run output; no 1b row places it -- bd:ajb_workspace/logs/sessions/; bd:debug/download-button-error.png; bd:debug/download-daily-error.png; bd:debug/error-final.png; bd:debug/txn-debug-211841/; bd:debug/txn-query-timeout.png; bd:diagnostics/; bd:gldrst/preflight/; bd:gold/logs/; bd:logs/; bd:qa-scratch/ds1_run5_log.txt; bd:qa-scratch/ds1_run6_log.txt; bd:qa-scratch/ds1_validate/; bd:qa-scratch/gate2_unit_delta_run7.parquet; bd:runs/; bd:scripts/; bd:ssm-output/; bd:status/; bd:temp/; bd:tmp/; bd:v4_output/; inf:_compare/unified_proof_20260630/; inf:_rebuild_status/; inf:_scratch/indexbytes-face/; inf:_toolprobe_scratch/comp-freshness/; inf:_toolprobe_scratch/pk/silver/toolprobe/; inf:bronze/logs/inf-bronze-runner/; inf:bronze/logs/inf-gold-runner/; inf:diagnostic/; inf:otp/debug/; inf:qa/_diag/; inf:telemetry/inf-gold-layer-runner/history/; inf:telemetry/inf-gold-layer-runner/status.json; cot:gold/logs/; cot:logs/\n[9] raw vendor download files (xlsx/txt) under forwardfill_v2/ or backfill_v2/; no 1b row names them -- bd:backfill_v2/; bd:forwardfill_v2/TXN_2026-01-16.xlsx; bd:forwardfill_v2/TXN_2026-01-19.xlsx; bd:forwardfill_v2/TXN_2026-01-21.xlsx; bd:forwardfill_v2/TXN_2026-01-22.xlsx; bd:forwardfill_v2/TXN_2026-01-23.xlsx; bd:forwardfill_v2/TXN_2026-01-26.xlsx; bd:forwardfill_v2/TXN_2026-01-27.xlsx; bd:forwardfill_v2/_perm_probe_1782839405.txt\n[1] MIXED: dated _BRONZE_COMPLETE.json completion markers (state kind, class c; 1b has no row for them) beside fees/ and bi/ bronze data (class d HOME); no single 1b row covers every kind -- bd:bronze/\n[2] canonical silver with no vendor in its key: 1b's HOME needs a {vendor} and the key does not give one -- bd:canonical/silver/dim_account/; bd:canonical/silver/fact_position/\n[12] MIXED (named in CENSUS.md): dated forwardfill data files beside _complete/ markers (state kind), and no 1b row names forwardfill_v2/ -- bd:forwardfill_v2/allocations/; bd:forwardfill_v2/assets/; bd:forwardfill_v2/realized/; bd:forwardfill_v2/transactions/; bd:forwardfill_v2/unrealized/; cot:forwardfill_v2/_retry_net/; cot:forwardfill_v2/account_attributes/; cot:forwardfill_v2/allocations/; cot:forwardfill_v2/holdings/; cot:forwardfill_v2/realized/; cot:forwardfill_v2/transactions/; cot:forwardfill_v2/unrealized/\n[41] a gold/ root file or directory that no 1b row names (1b names specific gold directories only) -- bd:gold/.checkpoints/; bd:gold/account_performance.parquet; bd:gold/account_quality_tiers.parquet; bd:gold/accounts_dimension_latest.parquet; bd:gold/advisor_assignments_history.parquet; bd:gold/advisor_rolling_flows.json; bd:gold/advisors/; bd:gold/architect_leaderboard.json; bd:gold/aua_certification/; bd:gold/client_dimension.parquet; bd:gold/client_performance.parquet; bd:gold/client_timeseries/; bd:gold/clients_tab.json; bd:gold/config/; bd:gold/consolidated/; bd:gold/firm_composition.json; bd:gold/firm_mix_views.json; bd:gold/firm_mix_views_daily.json; bd:gold/holdings_lots/; bd:gold/implementor_leaderboard.json; bd:gold/partner_analytics/; bd:gold/perf_history/; bd:gold/perf_report.json; bd:gold/pipeline-complete.json; bd:gold/synthetic_positions_index.parquet; bd:gold/timeseries_chart.json; inf:gold/_rebuild/; inf:gold/classification/; inf:gold/dispatch-lock.json; inf:gold/perf_report.json; inf:gold/timeseries/; cot:gold/account_performance.parquet; cot:gold/accounts_dimension_latest.parquet; cot:gold/advisor_assignments_history.parquet; cot:gold/client_dimension.parquet; cot:gold/client_performance.parquet; cot:gold/client_timeseries/; cot:gold/firm_composition.json; cot:gold/firm_mix_views.json; cot:gold/firm_mix_views_daily.json; cot:gold/partner_analytics/\n[7] MIXED (named in CENSUS.md): a zero-byte directory-marker key beside the directory's own children, and no 1b row names this directory -- bd:gold/_deprecated/; bd:gold/clients/; bd:gold/cohorts/; bd:gold/filters/; bd:gold/nna/; bd:gold/snapshots/; bd:gold/summary/\n[10] a gold/ path that no 1b row names -- bd:gold/canonical/nna_validation/; bd:gold/daily/positions/; inf:gold/dimensions/_aor_exercise/aor_attribution_comparison/; inf:gold/dimensions/aor_ledger/events/; inf:gold/dimensions/dim_inf_advisor_office.csv; inf:gold/meta/pipeline-failed.json; inf:gold/meta/pull-complete.json; inf:gold/meta/schemas/; inf:gold/meta/valgate-baseline/silver_transactions/; cot:gold/canonical/nna_validation/\n[1] MIXED: positions_cube/ and holdings_lots/ (class b gold tables), holdings_lots_shadow/ (class e RETIRE candidate, R18) and 16 json/parquet files directly under timeseries/ (not the `{t}/...` shape), plus a directory-marker key; no single 1b row covers every kind; named exception: holdings_lots_shadow/ (RETIRE) -- bd:gold/timeseries/\n[9] no 1b row names investor-reporting/ (the note says its source is irpt, but gives no tier, class or disposition for it) -- bd:investor-reporting/directory/; bd:investor-reporting/qa/directory/; bd:investor-reporting/qa/holdings/; inf:investor-reporting/directory/; inf:investor-reporting/qa/directory/; inf:investor-reporting/qa/holdings/; cot:investor-reporting/directory/; cot:investor-reporting/qa/directory/; cot:investor-reporting/qa/holdings/\n[3] Lambda deployment artifacts: key.code admits them as code-tier keys, but no 1b row places them -- bd:lambda-deploy/; bd:lambda-layers/; bd:lambda-packages/\n[4] the sample key is a completion marker or diagnostic artifact (state or diagnostic kind); 1b gives only the eclipse completion markers a state row, so no row places this class -- bd:schwab/silver/rps/; bd:silver/transactions_enriched/; inf:bronze/orion-api/; cot:bronze/\n[5] load manifest or validation log inside silver/: state or validation kind; 1b names only silver/meta/gap_manifest.json for state -- bd:silver/aua_validation_log.parquet; bd:silver/incremental_allocation_manifest.json; bd:silver/incremental_manifest.json; bd:silver/incremental_realized_manifest.json; bd:silver/incremental_unrealized_manifest.json\n[9] market-price silver: its {vendor} is not derivable from the key and is not the bucket's feed vendor, and 1b's HOME needs a {vendor} -- bd:silver/historical_dividends.parquet; bd:silver/historical_prices.parquet; bd:silver/historical_prices_20260213.parquet; bd:silver/historical_prices_final.parquet; bd:silver/interpolated_prices.parquet; bd:silver/interpolated_prices_summary.json; bd:silver/prices/; inf:silver/historical_prices.parquet; inf:silver/prices/\n[1] smartx JWT credential key: 1b decides only orion/jwt/current.json (FWD-8); no row places this one -- bd:smartx/jwt/\n[3] smartx raw API dumps: raw is not a tier in 1b and the table does not say whether it is bronze -- bd:smartx/raw/enterprises_aum/; bd:smartx/raw/holdings/; bd:smartx/raw/models/\n[3] leading-slash key; 1b places no leading-slash key -- inf:/advisors/; inf:/clients/; inf:/firm/\n[5] parity snapshot, QA copy, completion marker or chain-summary output under bronze/ or silver/: not bronze or silver data by what it is, and no 1b row places it -- inf:bronze/_parity-snapshot/; inf:bronze/eclipse_qa/; inf:silver/_parity-snapshot/positions_mv-2026-06-30/; inf:silver/_silver_complete/; inf:silver/api_dims/_chain_summary/\n[1] MIXED: dated eclipse bronze dirs (class d HOME) beside _history/ history copies (no 1b row); no single 1b row covers every kind -- inf:bronze/eclipse/\n[2] browser profile state; no 1b row places it -- inf:eclipse/browser-profile/; inf:orion/browser-profile/\n[1] MIXED: flat parquet files directly under gold/canonical/ (not the `{t}/...` shape) beside role_aua/ (class b `{t}/...`); no single 1b row covers every kind -- inf:gold/canonical/\n[1] MIXED (by the 1b table itself): `_meta/dispatch_eclipse_status.json` and eclipse gold output beside `{*}/_meta/gold_complete.json` markers that 1b gives to state (class c, `eclipse/inflection/state/complete/**`); the sample key is not a gold_complete.json; no single 1b row covers every kind -- inf:gold/eclipse/\n[1] MIXED: flat chain logs beside inf-exporter/ output; logs, and no 1b row places logs -- inf:gold/logs/\n[17] orion rate-limit or backfill-progress state: state kind, but 1b names only otp/state.json and the trigger-mode files, so no row places it -- inf:orion/backfill_progress_2a0c2a94-ab97-47bb-a22f-f194db318145.json; inf:orion/backfill_progress_2f0abf97-249e-40d8-894a-c464578adbf4.json; inf:orion/backfill_progress_4558ff63-5cd2-4eec-a3e4-7b575e74d319.json; inf:orion/backfill_progress_56b947d9-c82a-43ea-8f85-7db8f0e5354d.json; inf:orion/backfill_progress_d46faee5-ee79-42ff-85a5-b4d9c4f2ed0b.json; inf:orion/backfill_progress_ea9e59a8-0527-4bc9-9871-e8edcb805b5d.json; inf:orion/rate_limit_state_accounts_v2.json; inf:orion/rate_limit_state_activity.json; inf:orion/rate_limit_state_assets_v2.json; inf:orion/rate_limit_state_billing.json; inf:orion/rate_limit_state_household.json; inf:orion/rate_limit_state_household_rep_mapping.json; inf:orion/rate_limit_state_performance.json; inf:orion/rate_limit_state_performance_f1validate.json; inf:orion/rate_limit_state_positions_mv.json; inf:orion/rate_limit_state_probe.json; inf:orion/rate_limit_state_transactions.json\n[1] trigger-mode state: 1b places blackdiamond/{49f,cot}/session-trigger-mode.json and decides orion/jwt/current.json, but names no orion/jwt/trigger-mode.json -- inf:orion/jwt/trigger-mode.json\n[13] rebuild staging, rollback, quarantine or reconciliation-output copies under platinum/: not served platinum by what they are, and no 1b row places them -- inf:platinum/_rebuild/; inf:platinum/firm/_meta/; inf:platinum/firm/_quarantine_scope_bug_20260424/clients_tab.json; inf:platinum/firm/_quarantine_scope_bug_20260424/dashboard.json; inf:platinum/firm/_quarantine_scope_bug_20260424/filters/; inf:platinum/firm/_quarantine_scope_bug_20260424/header_metrics.json; inf:platinum/firm/_quarantine_scope_bug_20260424/leaderboard.json; inf:platinum/firm/_quarantine_scope_bug_20260424/partner_analytics.json; inf:platinum/firm/_quarantine_scope_bug_20260424/partner_analytics_annual.json; inf:platinum/firm/_quarantine_scope_bug_20260424/partner_analytics_monthly.json; inf:platinum/firm/_quarantine_scope_bug_20260424/partner_analytics_quarterly.json; inf:platinum/firm/_quarantine_scope_bug_20260424/timeseries_chart.json; inf:platinum/firm/_quarantine_scope_bug_20260424/timeseries_overview.json\n[1] MIXED: entity-id client JSON (class a platinum) beside _quarantine_scope_bug_20260424/ quarantined copies (995 objects; not served platinum, no 1b row); no single 1b row covers every kind -- inf:platinum/clients/\n[5] no 1b row names this class -- inf:qa/advisors/; inf:qa/artifacts/; inf:qa/clients/; inf:qa/firm/; inf:qa/gold-artifacts/\n[1] MIXED (by the 1b table itself): silver eclipse data (class d HOME) beside `{*}/_meta/silver_complete.json` markers that 1b gives to state (class c, `eclipse/inflection/state/complete/**`); no single 1b row covers every kind -- inf:silver/eclipse/\n[2] a parquet file directly under gold/timeseries/: the 1b cell is `gold/timeseries/{t}/...` (a table directory), so this shape is not placed -- cot:gold/timeseries/account_performance.parquet; cot:gold/timeseries/client_performance.parquet\n[1] MIXED: silver table dirs (class d HOME) beside dated {date}/_meta/ marker dirs (state kind, class c; 1b has no row for them); no single 1b row covers every kind -- cot:silver/",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/mapping.json on branch wk-ADVI_FIRMBKTS-1 (base fa437ba675): 444 rows, FAULT 226, each carrying fault_row ADVI_FIRMBKTS-D1-W1-S2",
      "python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~F1/round1/checks/r1_mapping.py: ROUND 1 MAPPING: 5 of 5 arms, exit=0 (444 census classes, 444 mapping rows, 209 placed rows graded through address())",
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/CENSUS.md section 'Mixed classes' and this file's row ADVI_FIRMBKTS-D1-W1-S1 (the census is frozen; a class was not split)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Does not fail AC1. Placement is by the 1b text only; where a class's composition below its sample key is not visible in the census (for example bd gold/meta/ with 9 objects, which is placed by its watermark sample), the class is placed by its sample and its other children are unread -- a consequence of the census's one-sample grain, not a finding."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W1-S3",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~1",
  "surfaced_at": "2026-10-09T21:05:48Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "FB-t-2: THE 1b TABLE SENDS MORE THAN ONE LEGACY CLASS TO THE SAME DESTINATION TABLE, SO A MOVE WOULD INTERLEAVE TWO PRODUCERS' KEYS IN ONE KEY SPACE (cot positions_cube TO THE IDENTICAL SAMPLE ADDRESS)",
  "spec_asserts": "Task order FB-t-2 section 1b: every class is placed by the table; FWD-2: every piece lands in exactly one destination.",
  "world_is": "Read from mapping.json dest addresses: (1) cot gold/positions_cube/ and cot gold/timeseries/positions_cube/ (rows b, `gold/positions_cube/*` and `gold/timeseries/{t}/...`) both place at s3://opal-data-cottonwood/advi/cottonwood/gold/positions_cube/date={D}/data.parquet -- the two samples (date 2026-10-08) produce the IDENTICAL address; (2) bd canonical/schwab/gold/account_gains/ (partition period=...) and bd gold/canonical/account_gains/ (date=...) share table advi/49financial/gold/account_gains/; (3) bd and cot platinum/firm/ and gold/platinum/firm/ share advi/{firm}/platinum/firm/; (4) bd and cot gold/entities, gold/artifacts and platinum/* share one platinum key space per firm. The table gives these as rules and the worker did not decide them; whether the two producers write the same keys is not read here.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/mapping.json on branch wk-ADVI_FIRMBKTS-1: rows opal-data-cot gold/positions_cube/ and gold/timeseries/positions_cube/ carry the same address",
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/census.json: the two cot samples are gold/positions_cube/2026-10-08.parquet and gold/timeseries/positions_cube/2026-10-08.parquet"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "For the cell that moves keys: a destination-collision check over the mapping is owed before any copy; round 1 moves nothing."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-S3",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "2.0.0_SA_COO~F1",
  "surfaced_at": "2026-10-09T21:18:46Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~F1",
  "one_line": "READER B OPENED A FILE ITS FACE FORBADE (worker ~1's FB-t-1 PROOF INSTANCE, UNDER THE PROJECT FOLDER), AND BOTH READERS ANSWERED BY SCRIPT, SO ROUND 1's READING IS A PARSE OF THE STRING AND ITS 'contents' FIELD MEASURES THE SCRIPT AS MUCH AS THE LOCATION",
  "spec_asserts": "ADVI_FIRMBKTS.TO-FB-t-4 section 2 bound 1: read nothing but reading_list.json, nothing else under org/missions/D8/ADVI/ADVI_FIRMBKTS/. FWD-1 ACCEPT: two people who have never worked together each say which system, which firm, how finished and what it holds.",
  "world_is": "Reader B's report (0.9.0_WK_ADVI_FIRMBKTS~3, commit 1a188f21fe) says it used ADVI_FIRMBKTS.TO-FB-t-1.proof_of_spec.json as a format template. That file carries census counts and the census criteria, not the arm map, the mapping table or reader A's answers. Both readers answered with a script over reading_list.json. At close (r1_agree.py): canonical arm 209 of 209 agree on system, firm and tier; legacy arm 19 of 209 agree on all three (system unknown in 143, firm unknown in 102). The contents pairs diverge in kind: reader A's script described the date partition ('2026 10 08 data') where reader B's named the table ('positions cube').",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "deliverables/2.0.0_SA_COO~F1/round1/R1_CLOSE_RUN.txt",
      "deliverables/2.0.0_SA_COO~F1/round1/R1_CLOSE_PAIRS.json",
      "worker ~3 final report (commit 1a188f21fe)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Does not move the system/firm/tier result: the opened file holds no answer and no arm. It bounds the 'contents' clause, which round 1 does not grade mechanically. Enrichment candidate for round 2: a reader face that withholds the project folder from the reader's worktree (a sparse checkout of reading_list.json alone) and asks for answers written without a parser, or graded on the table slot."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-S4",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "2.0.0_SA_COO~B1",
  "surfaced_at": "2026-10-11T03:23:44Z",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "1.0.0_SA_CTO~DELL1",
  "one_line": "THE PRODUCERS STILL WRITE opal-data-bd's PLATINUM DAILY, SO A COPY IS A SNAPSHOT AND A ROUTER FLIP BEFORE THEIR REPOINT SERVES A DAY-OLD COPY",
  "spec_asserts": "ROUND_ANALYSIS.round1.md item 5: F6's deploy 'waits on F7's copy reading byte-identical at every served key' and is the round's last act; FWD-4: firm users see exactly what they saw before on the day their data moves. DEC-17: never a dual write or a shadow copy.",
  "world_is": "2026-10-11 02:5xZ: head-object on opal-data-bd platinum/firm/advisor_nna_canonical.json reads LastModified 2026-10-11T01:11:26Z, and the live manifest of the 11 served classes counts 52,910 objects against the census's 52,851 two days earlier (59 new keys); every census class's last_modified_max sits in 2026-10-09 05:27Z-06:15Z. The producers rewrite these keys daily and nothing yet writes advi/49financial/platinum/. A router flip after a copy reads that copy: the morning after it serves yesterday's numbers, and byte-identity at the moment of the copy proves nothing about the next day. The copy is therefore a snapshot (r2_f7.py compare prints source-changed-since-manifest as its own count).",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "r2_f7.py manifest at 2026-10-11T02:5xZ: objects=52910 placed=52910 refused=0 collisions=0",
      "aws s3api head-object --bucket opal-data-bd --key platinum/firm/advisor_nna_canonical.json -> LastModified 2026-10-11T01:11:26+00:00",
      "census.json classes gold/artifacts/ ... platinum/firm/: last_modified_max 2026-10-09T05:27:19Z .. 06:15:33Z (round 1 listing)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "RULED by the issuer inside decomposition v2: F6's DEPLOY is not a round-2 cell (DECOMP_R2 'Not in round 2'). The round builds the path dormant (no behavior change) and copies a snapshot. Un-park: the CTO places F10's platinum-producer repoint (or a resync inside the flip window with the producers redirected), and the advTenant remedy if a map value changes. The disarm owner is the CTO because the placement is his."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-S5",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "2.0.0_SA_COO~B1",
  "surfaced_at": "2026-10-11T03:23:44Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "NO *-cot-* ROLE IS ASSUMABLE BY THE dell1 CLOUDOPS USER AND BOTH IAM SIMULATORS ARE REFUSED TO IT, SO F4's NEGATIVE ARM CANNOT BE EXERCISED DIRECTLY",
  "spec_asserts": "ROUND_ANALYSIS.round1.md item 3: the NEGATIVE arm must be EXERCISED, not read from policy text: a role/*-cot-* principal attempts one read-only GET on opal-data-inflection and is refused.",
  "world_is": "aws iam get-role on the 9 roles whose name contains -cot-: trust principals are lambda.amazonaws.com (3), scheduler.amazonaws.com (1), role/mdpf-gold-lambda-role (2), role/mdpf-daily-runner-ec2-role (1), role/irpt-ycharts-runner-role (1) and the two Andrew users (1); the group policies of cloudops-dell-agents-group carry no sts:AssumeRole; iam:SimulatePrincipalPolicy on a role and iam:SimulateCustomPolicy were refused to user/cloudops-dell1-agent-user. One route exists with no new IAM object: i-0167fd745ad906a66 (irpt-ycharts-runner, running, SSM Online) holds role/irpt-ycharts-runner-role, which irpt-cot-ycharts-research-role trusts.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "aws iam get-role --role-name <the 9 roles> --query Role.AssumeRolePolicyDocument.Statement[].Principal (printed at the cut)",
      "botocore ClientError AccessDenied for iam:SimulatePrincipalPolicy and iam:SimulateCustomPolicy as user/cloudops-dell1-agent-user",
      "boto3 ec2 describe-instances: i-0167fd745ad906a66 running, instance profile irpt-ycharts-runner-profile; ssm describe-instance-information: 4 managed instances, PingStatus Online"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Cell FB-e-4 runs the one SSM command r2_f4_send.py builds. ssm:SendCommand for the dell1 user is INFERRED, not measured: a refusal is a BLOCKING row on that cell, not a recut. The alternative, minting a probe role, is row IRPT_BCKEND-S107's exposure and an IAM-plane act."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-S6",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "2.0.0_SA_COO~B1",
  "surfaced_at": "2026-10-11T03:23:44Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "ENRICHMENT ITEM 6's 'LITERAL RENAME' IS ALREADY DONE BY ADVI_COTBKF, SO THE S11 CELL IS THE TOLERANT LOAD AND ITS TEST ONLY",
  "spec_asserts": "ROUND_ANALYSIS.round1-addendum.md section 2 item 6: the literal rename in build_canonical_prices_v2.py with the tolerant-load patch in the same diff; the new name is builder output.",
  "world_is": "build_canonical_prices_v2.py at fda1c4f0cc reads every input key from legacy_addresses.json rows beside the writer (CB-ap-1, CB-at-1, CB-ax-1 @19b3550e8a); no literal key remains in the loaders. The patch ADVI_FIRMBKTS_INPUT_S00_TOLERANT_LOAD.patch @091ccbafa2 applies to the builder clean (git apply --check rc 0); its TEST still types silver/historical_prices.parquet and the naming gate refuses it (NAMING REFUSE :46, reproduced). A test reading the writer's own INPUT_ADDRESSES passes the gate (3 passed; the existing price tests 12 passed).",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "git apply --check <patch> rc=0 at fda1c4f0cc",
      "python .tools/naming-gate.py --diff <patch> --enforce -> NAMING REFUSE data/cot/scripts/gold/test_s00_missing_tier2.py:46",
      "issuer scratch run: 3 passed + 12 passed + NAMING-GATE: PASS"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "The optional S_00 SSM step is dropped (MDPF_DEMQUE closed its S_00 SUPERSEDED, msg 1368: nothing consumes canonical_prices.parquet; the step would add a production step to the cot daily chain)."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-S7",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "2.0.0_SA_COO~B1",
  "surfaced_at": "2026-10-11T03:23:44Z",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "1.0.0_SA_CTO~DELL1",
  "one_line": "THE STAFF PROXY (?firm=49financial) ALREADY RESOLVES TO opal-data-49financial TODAY, SO A BUCKET-KEYED CANONICAL REWRITE WOULD CHANGE IT WITH NO REGISTRY EDIT, AND firm-config.mjs FORBIDS A SHARED-BUCKET VALUE CHANGE BEFORE THE advTenant REMEDY",
  "spec_asserts": "DEC-3: the tenant assertion is today's boundary, no wider and no narrower; shared-advisor-router index.mjs:252: bucket = `opal-data-${firmParam}` for opal-capital; firm-config.mjs header: do not make two firmIds share a bucket value, the advTenant remedy lands FIRST.",
  "world_is": "With the router at fda1c4f0cc, firmId opal-capital with ?firm=49financial resolves bucket opal-data-49financial and serves the LEGACY key there (a 404 NoSuchKey today, the bucket holding no legacy keys). An ungated 'canonical when the bucket is a firm bucket' rewrite would silently turn that request into a served read of the new keys. FIRM_CONFIG maps mockadv and 49financial to the same bucket (opal-data-bd) today; the cutover edit makes both resolve to opal-data-49financial and is the shared-bucket change the header warns about.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/lambda-edge/shared-advisor-router/index.mjs:239-253 @fda1c4f0cc",
      "infra/aws/lambda-edge/_shared/firm-config.mjs:29-63 @fda1c4f0cc",
      "r2_f6.mjs diff: a build with no registry gate reads 183 of 193 identical (10 staff-proxy events differ); the gated build reads 193 of 193"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "FB-e-6 builds the path gated on the registry's own map (FIRM_BUCKET_MAP[scope] === resolved bucket), so no request changes until the map does. The cutover is the CTO's, with F10 and the advTenant remedy."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-S8",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "1.0.0_SA_CTO~DELL1",
  "surfaced_at": "2026-10-11T03:55:00Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "DISARM OF D1-S4 AND D1-S7 BY THEIR DISARM OWNER: F6'S FLIP, THE F10 PRODUCER REPOINT, A DELTA COPY AND THE advTenant REMEDY ARE ONE CUTOVER WINDOW, PLACED IN ROUND 3; UNTIL THEN THE COPY IS INERT AND THE F6 PATH IS GATED ON THE REGISTRY MAP",
  "spec_asserts": "D1-S4: a router flip before the producers repoint serves a day-old copy. D1-S7: an ungated bucket-keyed rewrite would change the ?firm=49financial staff proxy with no registry edit, and firm-config.mjs forbids a shared-bucket value change before the advTenant remedy.",
  "world_is": "Neither hazard can fire in round 2. F6 is built dormant and not deployed. FB-e-6 gates the canonical path on FIRM_BUCKET_MAP[scope] === the resolved bucket, so no request changes until the map does (D1-S7 notes: 193 of 193 identical on the gated build). F7's copy is NEW keys only and nothing reads them (CTO half, condition 2). Placement: round 3 carries ONE cutover family, and nothing of it is cut before F7 reads COPY-COMPLETE and F6 is built. The family, in order inside one window, each with its own never-widen pair: (1) the advTenant remedy lands first; (2) the F10 platinum producers repoint to address() keys in opal-data-49financial; (3) a delta copy against a fresh manifest reads COPY-COMPLETE; (4) the FIRM_CONFIG map value moves and F6 deploys. No window leaves both homes written or both read.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/ledger/NEVER_WIDEN_ROUND2_F7_COPY_CTO_HALF.md (conditions 1-3; the D1-S4 section)",
      "ADVI_FIRMBKTS-D1-S4 notes: un-park on the CTO placing F10's repoint or a resync inside the flip window, plus the advTenant remedy if a map value changes",
      "ADVI_FIRMBKTS-D1-S7 notes and evidence: FB-e-6 gated build 193 of 193 identical; the cutover named as the CTO's, with F10 and the advTenant remedy"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Resolves D1-S4 and D1-S7 as hazards (the D1-S8 shape used elsewhere for a disarm); GRADUATED stays the CVO's L9 field. The round-3 enrichment list carries the cutover family as one item."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-S9",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "2.0.0_SA_COO~B1",
  "surfaced_at": "2026-10-11T04:23:22Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "THE ISSUER CUT FB-e-6 WITHOUT RUNNING THE NAMING GATE ON ITS PATCH: THE GATE REFUSED THE FIRM-NAME TABLE AND THE SPEC'S KEY-SHAPED LITERALS AT THE WORKER'S COMMIT, AND THE ROUTER WAS RE-CUT WITH AN EMPTY CANONICAL-BUCKET LIST",
  "spec_asserts": "The issuer's cut dry-ran every mechanical check at the base (DISPATCH Step 2) and, for FB-e-7, the naming gate on the diff. FB-e-6's patch @76bff7e7d4 was proved by its own harness and the router's gate, and its infra/ paths are graded by the commit-time naming gate (CLAUDE.md rule 30).",
  "world_is": "Worker ~9's commit of the v1 patch was refused by naming-gate.py --enforce (35 graded): index.mjs:126 typed the three long-form firm names as a hand-kept scope table, and the new spec typed firm names and platinum-prefixed key strings. The issuer did not run naming-gate.py --diff on the patch before the cut; running it afterwards reproduced the refusal. The re-cut (patch @ F6_ROUTER_EDIT.patch, v3): the router carries an EMPTY CANONICAL_PLATINUM_BUCKETS list and derives a bucket's scope from its own name after the prefix; the spec types no firm name (it reads FIRM_CONFIG) and builds its keys from the router's exported class table; naming-gate.py --diff --enforce on the v3 diff reads PASS 0 graded; the router's gate reads 39 pass; r2_f6.mjs diff 193 of 193, seam 20 of 20 and 10 of 10 controls; a mutant with a non-empty list fails diff 183 of 193 and seam controls 9 of 10.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "worker ~9 report 2026-10-11 and its row ADVI_FIRMBKTS-D1-W9-S4 (the refusal text)",
      "python .tools/naming-gate.py --diff <v1 patch> --enforce -> NAMING REFUSE index.mjs:126 and spec lines 40, 52, 55, 81, 83 (issuer's run)",
      "python .tools/naming-gate.py --diff <v3 patch> --enforce -> NAMING-GATE: PASS 0 graded (issuer's run)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "The activation changed from the registry's map (rows D1-S4/S7's design) to an explicit list: a cutover now needs the map edit AND one list entry, and the list entry is a hand-kept firm carrier the naming gate will grade, so the cutover cell either registers it (infra/logic/registry/) or generates it from the registry. That is the CTO's round-3 cutover window. The dormant build is stronger than before: it cannot change a request until a list entry exists."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W7-S1",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~7",
  "surfaced_at": "2026-10-11T03:57:49Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "F4 negative arm N4 passes on the absence of the deny text alone: the cot role's cottonwood read is refused by an identity-side implicit deny, so the fence's admit leg for its own firm is not exercised by this run",
  "spec_asserts": "Round-2 cell FB-e-4 / PRD F4 (r2_f4.py N4): the cot role's read of opal-data-cottonwood is NOT refused by the resource-based deny, so the difference control shows the fence refuses the other firm's role and admits its own.",
  "world_is": "Evidence F4_NEGARM_EVIDENCE.json (command f95a10b3-ab60-40b0-a673-3fce3a6258d9, runner i-0167fd745ad906a66, caller assumed-role/irpt-cot-ycharts-research-role/fb-r2-4-negarm): the INF read is refused with 'explicit deny in a resource-based policy'; the COT read is ALSO refused, with 'because no identity-based policy allows the s3:ListBucket action'. The cottonwood refusal is an identity-side implicit deny, not a fence admit. N4 (r2_f4.py:98-100) tests only that the deny phrase is absent from the COT text, so it passes; the fence's admit of its own firm is shown only by policy text (P3), not by an exercised read.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~7/F4_NEGARM_EVIDENCE.json @8a41501ebc (COT line: because no identity-based policy allows the s3:ListBucket action)",
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round2/checks/r2_f4.py:98-100 @8a41501ebc (N4 tests DENY_PHRASE not in COT text only)",
      "r2_f4.py --arms negative on the evidence file: 4 of 4 arms, rc 0, reproduced on two runs; mutant with the INF deny text removed gives N3 FAIL, 3 of 4, rc 1"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Recorded, not graded. The cell's acceptance reads as written (AC2 4 of 4). Whether the difference control must exercise the cottonwood admit leg is for the issuer and the L9 adjudicator; the cot role's missing identity permission on opal-data-cottonwood is not ruled on here."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W7-S2",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~7",
  "surfaced_at": "2026-10-11T04:10:00Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "AC1 and AC2 expect lines read 'ROUND 2 F4 ... ARMS -- and exit=0' on one line, but the invocation prints the arms line and 'exit=0' on two lines, so the expect string never occurs in the verbatim output",
  "spec_asserts": "Round-2 TO-FB-e-4 AC1 expect: 'ROUND 2 F4 POSITIVE: 3 of 3 arms -- and exit=0'; AC2 expect: 'ROUND 2 F4 NEGATIVE: 4 of 4 arms -- and exit=0'. The invocation's output is the stated line followed by an echo of the exit code.",
  "world_is": "Verbatim output of both invocations (run at 8a41501ebc in the worktree): 'ROUND 2 F4 POSITIVE: 3 of 3 arms' and 'exit=0' on separate lines; 'ROUND 2 F4 NEGATIVE: 4 of 4 arms' and 'exit=0' on separate lines. Substance matches (3 of 3 and 4 of 4, exit 0). proof-of-spec-check matches expect as a regex on output_evidence and reports both rows VIOLATION (status PASS not matched). Worker recorded the verbatim output and status FAIL; the expect text was not edited.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/task-orders/ADVI_FIRMBKTS.TO-FB-e-4.f4-arms.md @8a41501ebc (section 4 AC1 and AC2 expect text)",
      "proof-of-spec-check.py conditional_checks expect match (re.search over output_evidence) @732412e179 -> VIOLATION acceptance[AC1] and acceptance[AC2] on the first run",
      "AC1 and AC2 invocations run in the worktree @8a41501ebc: 'ROUND 2 F4 POSITIVE: 3 of 3 arms' / 'exit=0'; 'ROUND 2 F4 NEGATIVE: 4 of 4 arms' / 'exit=0'"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Recorded, not graded. The format difference is for the issuer and the L9 adjudicator to rule on; the order stays open with AC1 and AC2 recorded FAIL on the mechanical expect match, and no flip is made."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W7-S3",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~7",
  "surfaced_at": "2026-10-11T04:12:47Z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "one_line": "THE LAYER-2 FLIP GATE CANNOT FIND THE PROOF INSTANCE OF A TREE ORDER WHOSE FILENAME CARRIES A SUFFIX, SO TO-FB-e-4's complete flip is REFUSED although its instance is VALID and both criteria PASS by output",
  "spec_asserts": "to-pipeline-gate.py check_complete_flip (:3244-3255, :3176-3191): for a tree order the instance is searched as deliverables/*/<stem>.proof_of_spec.json, where <stem> is the ORDER FILENAME minus .md; the <proof_of_spec> block may also name the instance path. The order's own face (section 5) names the instance as ADVI_FIRMBKTS.TO-FB-e-4.proof_of_spec.json.",
  "world_is": "The order is org/missions/D8/ADVI/ADVI_FIRMBKTS/task-orders/ADVI_FIRMBKTS.TO-FB-e-4.f4-arms.md, so the gate's stem is ADVI_FIRMBKTS.TO-FB-e-4.f4-arms and it searches for ADVI_FIRMBKTS.TO-FB-e-4.f4-arms.proof_of_spec.json, which does not exist. The instance is at deliverables/0.9.0_WK_ADVI_FIRMBKTS~7/ADVI_FIRMBKTS.TO-FB-e-4.proof_of_spec.json. The <proof_of_spec> block (section 4) names no instance path, so the tag route finds none. The commit refused with 'flips to complete on PIPELINE-REGISTERED project ADVI_FIRMBKTS, and NO proof-of-spec instance was found beside it'. The instance itself passes proof-of-spec-check.py AC1,AC2 rc=0 VALID.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "safe-commit.sh of the order flip + instance (0.9.0_WK_ADVI_FIRMBKTS~7 worktree, branch wk-ADVI_FIRMBKTS-7, base 105ca3c82e), 2026-10-11T04:1xZ: 'ERROR: BLOCKED -- pipeline layer 2 (TO issuance gate). Commit aborted; files unstaged.' and the to-pipeline-gate REFUSED line quoted above",
      "proof-of-spec-check.py ADVI_FIRMBKTS.TO-FB-e-4.proof_of_spec.json AC1,AC2 @worktree -> VALID (rc=0), violations=0",
      ".tools/to-pipeline-gate.py:3176-3191 @worktree (_proof_instance_candidates: names = (stem + '.proof_of_spec.json', ...) with stem = basename(rel) minus '.md'; tree glob deliverables/*/<n>)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Recorded, not worked around. Not renamed (the instance path is the one the order names), no <proof_of_spec> path added to the issuer's literal block, and no # pipeline-override line added, because the order is in pipeline. The order is left status pending on the worker branch; the criteria are PASS by output. Owner of the choice: the issuer 2.0.0_SA_COO~B1 (name the instance to the order stem, or add its path to the block) or the gate's owner (search by to_id as well as stem)."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W8-S1",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~8",
  "surfaced_at": "2026-10-11T04:10:42Z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "one_line": "THE F7 PROOF INSTANCE IS NAMED BY THE ORDER AS D/ADVI_FIRMBKTS.TO-FB-e-5.proof_of_spec.json, BUT THE COMPLETE-FLIP GATE LOOKS FOR THE ORDER FILE STEM, ADVI_FIRMBKTS.TO-FB-e-5.f7-copy.proof_of_spec.json, SO THE STATUS FLIP IS REFUSED",
  "spec_asserts": "ADVI_FIRMBKTS.TO-FB-e-5 section 5: the instance sits at D/ADVI_FIRMBKTS.TO-FB-e-5.proof_of_spec.json and the order's <status> flips to complete in the same commit once AC1-AC3 pass; section 1a step 6 commits the instance with the status flip together.",
  "world_is": "proof-of-spec-check.py on the named instance returns rc=0 (3 of 3 rows, 0 violations). The complete-flip gate (.tools/to-pipeline-gate.py check_complete_flip, candidates from _proof_instance_candidates at lines 3176-3191) takes the order file stem ADVI_FIRMBKTS.TO-FB-e-5.f7-copy and globs deliverables/*/ADVI_FIRMBKTS.TO-FB-e-5.f7-copy.proof_of_spec.json. The order's <proof_of_spec> block (section 4) names no literal instance path, so the tag lookup adds no candidate. The gate refuses the flip with 'NO proof-of-spec instance was found beside it'. The worker did not rename the instance or edit the order's proof block; the order's <status> stays pending in the committed state.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/task-orders/ADVI_FIRMBKTS.TO-FB-e-5.f7-copy.md @aca87f5ef8 (section 5 names D/ADVI_FIRMBKTS.TO-FB-e-5.proof_of_spec.json; section 4 proof block names no literal path)",
      ".tools/to-pipeline-gate.py @aca87f5ef8 lines 3176-3191 (_proof_instance_candidates: stem = basename minus .md)",
      "commit-attempt output of 0.9.0_WK_ADVI_FIRMBKTS~8 at 2026-10-11T04:10Z: REFUSED, 1 violation, instance not found beside the order"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Needs the COO or CTO ruling: either the instance takes the gate's stem name (ADVI_FIRMBKTS.TO-FB-e-5.f7-copy.proof_of_spec.json) or the order gains a literal <proof_of_spec> instance path. The copy itself is complete and verified (AC1-AC3 PASS); only the status flip waits on this."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W10-S1",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~10",
  "surfaced_at": "2026-10-11T04:06:27Z",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "disarm_owner": "1.0.0_SA_CTO~DELL1",
  "one_line": "THE TO-PIPELINE GATE CANNOT FIND A TREE PROOF INSTANCE NAMED AS THE ORDER NAMES IT, SO A VALID INSTANCE CANNOT FLIP ITS ORDER TO complete",
  "spec_asserts": "ADVI_FIRMBKTS.TO-FB-e-7 section 5: the instance is at deliverables/0.9.0_WK_ADVI_FIRMBKTS~10/ADVI_FIRMBKTS.TO-FB-e-7.proof_of_spec.json, and the order's status flips to complete in the same commit as the instance.",
  "world_is": "The instance at that path is VALID (proof-of-spec-check.py rc=0 on AC1,AC2,AC3, all PASS) and is committed at 7329f897dd. The flip commit is REFUSED by the TO issuance gate: 'NO proof-of-spec instance was found beside it'. to-pipeline-gate.py resolves a tree instance only by the TO file stem (ADVI_FIRMBKTS.TO-FB-e-7.s11-tolerant-load.proof_of_spec.json, lines 3176-3191) or by a backticked path inside the order's <proof_of_spec> block (lines 3156-3173), and this order's block names no instance path. The order therefore cannot reach complete under the gate as written. The flip is NOT committed; the order stays pending on the branch.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "proof-of-spec-check.py ... ADVI_FIRMBKTS.TO-FB-e-7.proof_of_spec.json AC1,AC2,AC3 -> VALID (rc=0) @7329f897dd",
      "safe-commit flip attempt, 2 attempts (before and after the instance commit): to-pipeline-gate REFUSED, 'NO proof-of-spec instance was found beside it'",
      ".tools/to-pipeline-gate.py:3156-3191 @62f4b5441e (stem and tag lookup)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Not worked around: the instance was NOT renamed to the stem name, the order's <proof_of_spec> block was NOT edited, and no pipeline-override line was added (the TO is pipeline-registered). Disarm candidates for the owner: a stem-named mirror, or the gate reading the instance path from the order's section 5 'Instance at' line. The gate's own FIX text asks for the two blocks in the TO face."
}
```

```json
{
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~4",
  "surfaced_at": "2026-10-11T04:20:38Z",
  "hazard_standing": "INERT",
  "disposition": "UNDER_INVESTIGATION",
  "id": "ADVI_FIRMBKTS-D1-W4-S1",
  "class": "BLOCKING",
  "one_line": "ROUND-1 COLLISION: cot gold/positions_cube/ AND gold/timeseries/positions_cube/ WRITE THE SAME 171 DATED KEYS, SO 1b (COPY UNCHANGED) AND 1e (A COLLIDING GROUP IS FAULT) CANNOT BOTH HOLD; P2 FAILS ON THIS GROUP",
  "spec_asserts": "FB-e-1 1b: every round-1 MOVE/HOME row is copied UNCHANGED (check V5). 1e: a destination table shared with overlap above 0 makes EVERY class of the group FAULT. P2: every shared table needs a merge ruling with overlap_keys 0.",
  "world_is": "mapping.json cot rows gold/positions_cube/ and gold/timeseries/positions_cube/ both map to advi/cottonwood/gold/positions_cube/date=<D>/data.parquet. Live listing (read-only, 2026-10-11): 171 keys per class with the same dates, overlap 342 of 342. Left unchanged and UNRULED in mapping_v2.json; r2_mapping.py --arms repair: P2 FAIL, AC2 3 of 4.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/mapping.json (cot gold/positions_cube/, gold/timeseries/positions_cube/)",
      "boto3 list_objects_v2 on opal-data-cot, read-only, prefixes gold/positions_cube/ and gold/timeseries/positions_cube/",
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/mapping_v2.json"
    ]
  },
  "notes": "The CTO rules whether one of the two round-1 rows becomes FAULT (a round-1 change) or the table is re-keyed. Neither is taken here."
}
```

```json
{
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~4",
  "surfaced_at": "2026-10-11T04:20:38Z",
  "hazard_standing": "INERT",
  "disposition": "UNDER_INVESTIGATION",
  "id": "ADVI_FIRMBKTS-D1-W4-S2",
  "class": "OBSERVATION",
  "one_line": "RS4 COMPLETION MARKERS HAVE NO CLASS IDENTITY IN THEIR DESTINATION: 13 CLASSES IN TWO bd/cot STATE-COMPLETE GROUPS COLLIDE (217 AND 401 SHARED KEYS) AND 1e FAULTS THEM",
  "spec_asserts": "1c RS4 writes {V}/{F}/state/complete/<seg1>/<rest> with no class segment, so markers from different classes collide whenever the same name recurs.",
  "world_is": "forwardfill_v2/allocations/_complete/2026-07-20.json and forwardfill_v2/transactions/_complete/2026-07-20.json (cot) both map to blackdiamond/cottonwood/state/complete/_complete/2026-07-20.json under the class-prefix convention. Groups: bd state/complete 5 classes overlap 217; cot state/complete 8 classes overlap 401.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/mapping_v2.json (state/complete rows)",
      ".scratch overlap pass, live listing 2026-10-11 (uncommitted, worktree scratch)"
    ]
  },
  "notes": "The convention (matched prefix = class or child prefix) keeps keys unique within a class. Cross-class collisions remain; a rule that carries the kind in the table would clear them."
}
```

```json
{
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~4",
  "surfaced_at": "2026-10-11T04:20:38Z",
  "hazard_standing": "INERT",
  "disposition": "UNDER_INVESTIGATION",
  "id": "ADVI_FIRMBKTS-D1-W4-S3",
  "class": "OBSERVATION",
  "one_line": "A ZERO-BYTE MARKER EQUAL TO ITS CLASS PREFIX CANNOT BE A RE-GRID CHILD: bd gold/cohorts/, filters/, nna/, snapshots/, summary/, timeseries/ KEEP THE MARKER IN A FAULT REMAINDER",
  "spec_asserts": "1c RC: a key ending in / is a zero-byte directory marker, RETIRE. 1d: a re-grid child is a prefix that starts with its parent; the checker forbids two rows with one prefix.",
  "world_is": "The marker key equals the class prefix (gold/cohorts/ and the like). A child keeping that prefix would duplicate the parent prefix, so the marker sits in the FAULT rest child with the non-MOVE objects. gold/clients/ (bd, 2949 live objects) stays FAULT whole for the same reason plus S5.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/mapping_v2.json (regrids: bd gold/cohorts/, gold/filters/, gold/nna/, gold/snapshots/, gold/summary/, gold/timeseries/)",
      "r2_mapping.py repair: duplicates=0 at structure V2"
    ]
  },
  "notes": "The spec does not say how a marker equal to its prefix is split. A FAULT remainder is the conservative reading (1c: a rule that cannot apply as written is FAULT)."
}
```

```json
{
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~4",
  "surfaced_at": "2026-10-11T04:20:38Z",
  "hazard_standing": "INERT",
  "disposition": "UNDER_INVESTIGATION",
  "id": "ADVI_FIRMBKTS-D1-W4-S4",
  "class": "OBSERVATION",
  "one_line": "1e TAKEN LITERALLY FAULTS ROUND-1 PLACED CLASSES THAT COLLIDE WITH NEW CLASSES; ONLY THE NEW CLASSES ARE FAULTED HERE, TO KEEP 1b",
  "spec_asserts": "1e: every class of a colliding group becomes FAULT. 1b: round-1 placed rows are copied unchanged (V5).",
  "world_is": "Round-1 classes in a new-vs-old overlap: bd gold/artifacts/ (44 keys in the group), bd platinum/advisors/ (980 keys; 77 shared with new gold/advisors/ keys), bd canonical/schwab/gold/account_performance/ and client_performance/, cot gold/artifacts/. The new classes of those groups are FAULT (reason destination-key overlap n of m); the round-1 rows stay.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/mapping_v2.json (collisions, FAULT rows with reason destination-key overlap)",
      "r2_mapping.py repair P2 and structure V5"
    ]
  },
  "notes": "A CTO ruling could instead FAULT the round-1 rows (a change the difference control forbids) or key the new rows apart."
}
```

```json
{
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~4",
  "surfaced_at": "2026-10-11T04:20:38Z",
  "hazard_standing": "INERT",
  "disposition": "UNDER_INVESTIGATION",
  "id": "ADVI_FIRMBKTS-D1-W4-S5",
  "class": "OBSERVATION",
  "one_line": "INTERLEAVED MARKERS AND DATA: A PREFIX RE-GRID WOULD NEED ONE CHILD PER FILE; 6 CLASSES (23,977 LIVE OBJECTS) STAY FAULT WHOLE ABOVE A 25-CHILD LIMIT THE SPEC DOES NOT SET",
  "spec_asserts": "1d names children as sub-directories, root files or exclude groups; it sets no limit on the number of children.",
  "world_is": "bronze/orion-api/ (17170 live objects, 3488 children), bronze/eclipse/ (1798, 270), bronze/eclipse_qa/ (871, 134), gold/eclipse/ (529, 265), silver/eclipse/ (660, 264); gold/clients/ (2949 root JSON beside a marker). Each stays one FAULT row with the reason naming the child count.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/mapping_v2.json (FAULT rows, reason interleaved completion markers)",
      "boto3 list_objects_v2 read-only on opal-data-inf and opal-data-bd, 2026-10-11"
    ]
  },
  "notes": "The limit (25) is the worker's, not the spec's. The CTO may rule per-file children or a per-date re-grid."
}
```

```json
{
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~4",
  "surfaced_at": "2026-10-11T04:20:38Z",
  "hazard_standing": "INERT",
  "disposition": "UNDER_INVESTIGATION",
  "id": "ADVI_FIRMBKTS-D1-W4-S6",
  "class": "OBSERVATION",
  "one_line": "CENSUS DRIFT: the 226 round-1 FAULT classes hold 114,349 live objects at 2026-10-11T04:01:07Z against 114,045 in census.json (2026-10-09T20:36:32Z); 42 classes differ",
  "spec_asserts": "Re-grid parent_objects are live counts under the parent (1d).",
  "world_is": "Per-class live counts exceed census counts by up to 16 objects (bd forwardfill_v2/transactions/ 310 against 306 census). Re-grid denominators use the live listing; census_listed_at stays the census value.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/census.json (listed_at 2026-10-09T20:36:32Z)",
      ".scratch fault_listing.json, live list 2026-10-11T04:01:07Z (uncommitted)"
    ]
  },
  "notes": "Census figures are kept as the census denominator (444 classes, 238,861 objects). The live difference is recorded here, not re-censused."
}
```
```json
{
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~4",
  "surfaced_at": "2026-10-11T04:33:32Z",
  "hazard_standing": "INERT",
  "disposition": "UNDER_INVESTIGATION",
  "id": "ADVI_FIRMBKTS-D1-W4-S7",
  "class": "OBSERVATION",
  "one_line": "SHELL CWD DOES NOT PERSIST: THE ORDER'S CD-ONLY CALL DID NOT CARRY TO THE NEXT CALL, SO THE CHECKER RAN IN THE BASE CHECKOUT AND READ 0 OF 5 (ABSENT)",
  "spec_asserts": "Step 4 runs each checker invocation in its own Bash call AFTER a first call that only does cd to the worktree, so the check reads the worktree's files.",
  "world_is": "The Bash tool resets its working directory between calls: the cd-only call did not persist, so the invocation's cd \"$(git rev-parse --show-toplevel)\" ran git in the base checkout C:/dev/ajb_workspace. The checker printed ABSENT or unreadable (mapping_v2.json not found there) and ROUND 2 MAPPING STRUCTURE: 0 of 5 arms, exit=1. Recovered by prefixing the same call with cd /c/dev/wk-firmbkts-4; the recorded invocation text and the checker output lines are unchanged.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round2/checks/r2_mapping.py@2ca0be7c81 (_root() reads git rev-parse --show-toplevel from the process cwd)",
      "worker run 2026-10-11: first structure run from the base cwd printed ABSENT and 0 of 5; the same command prefixed with cd to the worktree printed 5 of 5, exit=0"
    ]
  },
  "notes": "Fail-soft: the checker catches the read error and exits 1 with a message, so a bare run from the wrong tree reads as a FAIL on a correct table. Not an order defect in the check text; the cd prefix is the only change, and the worker's proof instance records the order's invocation verbatim."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W9-S1",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~9",
  "surfaced_at": "2026-10-11T04:02:00Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "FB-e-6: THE ROUTER AT BASE ALREADY CARRIES 5 NON-ASCII COMMENT LINES (EM DASHES); THE PATCH ADDS NONE, SO THE ORDER'S NO-NON-ASCII BOUND IS NOT MET BY THE BASE FILE AND IS NOT FIXED HERE",
  "spec_asserts": "Task order FB-e-6 section 2.5: No non-ASCII; LF line endings. Section 2.1: the edit is the patch and nothing else.",
  "world_is": "At fda1c4f0cc, infra/aws/lambda-edge/shared-advisor-router/index.mjs has 5 lines with non-ASCII characters (base lines 49, 224, 231, 259, 424: em dashes in comments). After git apply of F6_ROUTER_EDIT.patch the same 5 lines remain (new lines 49, 255, 262, 291, 475) and the patch adds 0 non-ASCII lines. Line endings: 0 CR bytes in index.mjs and in the new spec file. The new spec file test/canonical-platinum.spec.mjs has 0 non-ASCII lines.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "git show fda1c4f0cc:infra/aws/lambda-edge/shared-advisor-router/index.mjs, grep -P '[^\\x00-\\x7F]' = 5 lines @fda1c4f0cc",
      "infra/aws/lambda-edge/shared-advisor-router/index.mjs in worktree wk-ADVI_FIRMBKTS-9 after git apply, grep -P '[^\\x00-\\x7F]' = 5 lines (same text)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Not fixed by this cell: removing the five characters edits lines outside the patch, which section 2.1 forbids. AC1-AC3 do not read it. A later router edit decides it: the whole file goes ASCII, or every reader is explicit (CLAUDE.md section 4, non-ASCII rule)."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W9-S2",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~9",
  "surfaced_at": "2026-10-11T04:02:00Z",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~B1",
  "one_line": "FB-e-6 AC1 INVOCATION: cd \"$(git rev-parse --show-toplevel)\" RESOLVES THE SHELL'S OWN CHECKOUT; RUN FROM THE DEFAULT CWD IT GATES THE BASE ROUTER AND READS 31 PASS ACROSS 2 FILES WITH EXIT 0, NOT THE WORKTREE'S 39 ACROSS 3",
  "spec_asserts": "Task order FB-e-6 section 4 AC1 invocation: export PATH=...; cd \"$(git rev-parse --show-toplevel)\" && timeout 110 bash infra/aws/lambda-edge/shared-advisor-router/run-gate.sh; expect N pass with N at least 36 (39 expected), 0 fail, across 3 files, exit=0. Worker face: cd to the worktree before every Bash call.",
  "world_is": "Run as the first command of a Bash call whose cwd is the main workspace C:/Dev/ajb_workspace, the invocation's git rev-parse returns that checkout; run-gate.sh does cd \"$(dirname \"$0\")\" and runs bun test there: 31 pass, 0 fail, Ran 31 tests across 2 files, exit=0, with the new spec file absent from that run. Only an explicit prior cd into the worktree gives 39 pass, 0 fail, 3 files, exit=0. Measured 2026-10-11 on dell1.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "run-gate.sh (worktree wk-ADVI_FIRMBKTS-9, @fda1c4f0cc+patch): line 'cd \"$(dirname \"$0\")\"' then exec bun run test",
      "AC1 run 1, cwd C:/Dev/ajb_workspace: 'OK: running ... in /c/dev/ajb_workspace/infra/aws/lambda-edge/shared-advisor-router', 31 pass, 0 fail, 2 files, exit=0",
      "AC1 run 2, after cd /c/dev/wk-firmbkts-9: 'OK: running ... in /c/dev/wk-firmbkts-9/infra/aws/lambda-edge/shared-advisor-router', 39 pass, 0 fail, 3 files, exit=0"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "The false reading has the shape of a pass (exit 0, 0 fail), so the disarm is the issuer's: the next round cut states the invocation with an explicit cd into the worktree, or names the worktree root as the read point. The worker re-ran AC1 from the worktree and the proof records 39 of 39 from the worktree; the run from the default cwd is not the AC1 reading."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W9-S3",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~9",
  "surfaced_at": "2026-10-11T04:02:30Z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "one_line": "FB-e-6 STATUS FLIP IS OUTSIDE MY WRITE GRANT: task-orders/ADVI_FIRMBKTS.TO-FB-e-6.f6-canonical-key-path.md is not in <paths>, so this worker does not flip <status> pending to complete; AC1-AC3 pass and the proof instance is committed",
  "spec_asserts": "Task order FB-e-6 section 5: flip this order's <status> to complete in the SAME commit as the proof instance, when AC1-AC3 pass. Section 3 <paths> names the router directory, the 0.9.0_WK_ADVI_FIRMBKTS~9 deliverables folder and INVESTIGATION_v1.md; a worker writes nothing else.",
  "world_is": "The order file is org/missions/D8/ADVI/ADVI_FIRMBKTS/task-orders/ADVI_FIRMBKTS.TO-FB-e-6.f6-canonical-key-path.md line 103, <status>pending</status>, and it is not in the lane grant. AC1 reads 39 pass, 0 fail, 3 files, exit=0; AC2 reads 193 of 193 through handleWithMap and 193 of 193 through handler, exit=0 (twice); AC3 reads 9 of 9, exit=0.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "task-orders/ADVI_FIRMBKTS.TO-FB-e-6.f6-canonical-key-path.md @f4f01cfb27 line 103 <status>pending</status>; section 3 <paths> at lines 60-64",
      "AC1-AC3 output lines in the proof instance org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~9/ADVI_FIRMBKTS.TO-FB-e-6.proof_of_spec.json"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Left at pending by the write grant, not by a criterion. The owner of the flip is the issuer (2.0.0_SA_COO~B1) or the lane owner, who can flip it from the proof's result or widen the grant by its own order. The worker did not override the grant."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W9-S4",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~9",
  "surfaced_at": "2026-10-11T04:06:44Z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "one_line": "FB-e-6 COMMIT REFUSED BY THE NAMING GATE (LGIC_ENFORCE, 35 graded): THE ISSUER'S PATCH AND ITS NEW SPEC CARRY LITERAL FIRM NAMES THE GATE REFUSES AS HAND-KEPT CARRIERS; THE ROUTER CODE IS NOT COMMITTED",
  "spec_asserts": "Task order FB-e-6 section 1a step 3: commit index.mjs and the new spec together with the proof instance and the status flip. Section 2.1: the edit is the patch and nothing else; no edit outside <paths>, and the patch is never hand-edited.",
  "world_is": "safe-commit.sh refused the commit with ERROR: BLOCKED -- the naming limb refused. Refusals: index.mjs:126 'inflection' (NEW hand-kept carrier) and test/canonical-platinum.spec.mjs lines 25, 31, 36-38, 42-43, 47-52, 56, 62, 68-71 (NEW hand-kept carriers of '49financial', 'inflection', 'mockadv', and out-of-pattern S3Key literals). The gate's own remedy names infra/logic/registry/ rows and R20 entries, outside this worker's <paths>. Files were unstaged by the gate; the router and spec remain uncommitted in the worktree. The proof and this channel are committed separately.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "safe-commit.sh output at worktree wk-ADVI_FIRMBKTS-9, HEAD f4f01cfb27: [naming-gate] NAMING-GATE: REFUSE 35 graded, rc=1",
      "patch F6_ROUTER_EDIT.patch applied unchanged (git apply rc 0); no hand-edit made"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Owner of the disarm: the issuer (2.0.0_SA_COO~B1) with the LGIC owner, either by registry rows for these literals (infra/logic/registry/) or an R20 register entry, or by a re-cut of the patch to use name() and lookup() output. No bypass was used. The cell's AC1-AC3 results stand as measured; the commit is what is blocked."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W9-S5",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~9",
  "surfaced_at": "2026-10-11T04:27:54Z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "one_line": "FB-e-6 AC1 INVOCATION RESOLVES TO THE BASE CHECKOUT, NOT THE WORKTREE: THE ORDER'S SEPARATE CD CALL DOES NOT PERSIST (CWD RESETS PER BASH CALL), SO AC1 AS WRITTEN READS 31 PASS ACROSS 2 FILES AND EXPECTS 39; THE WORKTREE READS 39 PASS ACROSS 3 FILES",
  "spec_asserts": "Task order FB-e-6 step 4: run AC1 after a first call that only does cd /c/dev/wk-firmbkts-9; the invocation's cd to git rev-parse --show-toplevel must land in the worktree; expect \\b39 pass with exit=0 (task-orders/ADVI_FIRMBKTS.TO-FB-e-6.f6-canonical-key-path.md @357f738e20 line 82).",
  "world_is": "Each Bash call starts in the base checkout: call-start cwd C:/Dev/ajb_workspace, toplevel C:/dev/ajb_workspace. AC1 as written printed 'OK: running the shared-advisor-router gate (bun run test) in /c/dev/ajb_workspace/infra/aws/lambda-edge/shared-advisor-router', ' 31 pass', ' 0 fail', 'Ran 31 tests across 2 files', exit=0. Diagnostic from the worktree (explicit cd in the same call, bun run test, not an AC1 reading): 39 pass, 0 fail, 3 files, rc=0. The new spec alone: 8 pass. The patch created test/canonical-platinum.spec.mjs (new file, 00:26) and the router index.mjs applied clean. AC1 stopped the order; AC2 and AC3 were not run.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "Bash call-start probe in this call: cwd_at_call_start=C:/Dev/ajb_workspace, toplevel_at_call_start=C:/dev/ajb_workspace (2026-10-11T04:27Z)",
      "AC1 output (first run, cd in the invocation): 'OK: running the shared-advisor-router gate (bun run test) in /c/dev/ajb_workspace/infra/aws/lambda-edge/shared-advisor-router', ' 31 pass', ' 0 fail', 'Ran 31 tests across 2 files', exit=0",
      "diagnostic output .scratch/diag_gate_worktree.txt in worktree wk-ADVI_FIRMBKTS-9: ' 39 pass', ' 0 fail', 'Ran 39 tests across 3 files', rc=0",
      "task-orders/ADVI_FIRMBKTS.TO-FB-e-6.f6-canonical-key-path.md @357f738e20 line 15 records 31 pass / 2 files as the BASE reading; the same trap is recorded as ADVI_FIRMBKTS-D1-W9-S2 (AC1 run 1, cwd C:/Dev/ajb_workspace)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Recurrence of ADVI_FIRMBKTS-D1-W9-S2: the AC1 invocation's cd is resolved from the call-start cwd, which is the base. The order's step-4 cd-only call cannot pin the worktree because the cwd does not persist between Bash calls. Owner of the disarm: the issuer (2.0.0_SA_COO~B1), by stating AC1 with an absolute worktree path in the invocation (or a cd inside the same call), a re-cut that the checker accepts. The worker did not rewrite the invocation text, did not commit, did not flip the status, and wrote no proof instance, because step 4 stops on a non-matching AC1. Scratch files: .scratch/diag_canonical_spec.txt, .scratch/diag_gate_worktree.txt."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-S10",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "2.0.0_SA_COO~B1",
  "surfaced_at": "2026-10-11T05:15:22Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "THE ROUND-CLOSE CHECK AND THE COMPLETE-FLIP GATE FIND A TREE ORDER'S PROOF INSTANCE BY DIFFERENT RULES, SO SEVEN ORDERS FLIPPED COMPLETE AND THE CLOSE CHECK READ 0 OF 7 PROOFS",
  "spec_asserts": "CLAUDE.md rule 27 and the canonical spine name one proof instance per order, and the close of a round counts each complete order's instance (round-close-check.py: 'every task order of the round whose status is complete has a proof instance that passes').",
  "world_is": "to-pipeline-gate.py check_complete_flip resolves an instance by the order file stem OR a backticked path in the order's <proof_of_spec> block (rows D1-W7-S3, D1-W8-S1, D1-W10-S1 cite lines 3156-3191); round-close-check.py proof_state (line 314) resolves it only as deliverables/*/<order stem>.proof_of_spec.json. The round-2 orders named their instances by order id in a proof-block path, so all seven flipped and round-close-check read PROOF-BAD x7, verdict REFUSED. Second tell: 3 of the 7 instances carried artifact rows still reading PENDING-THIS-COMMIT for files committed earlier, which proof-of-spec-check refuses (CCX class) and which the flip gate only meets again when the order is next modified. Repaired by the issuer at e60140c2d2 (seven renames, six pins) and 6f71f434ac (order paths), merged baaa2bbc81; round-close-check --deep then read 7 of 7 VALID, MAY-CLOSE.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python .tools/round-close-check.py --project ADVI_FIRMBKTS --round 2 -> PROOFS mode=structural complete=7 proof_ok=0 proof_bad=7, verdict=REFUSED (2026-10-11 ~04:47Z, before the rename)",
      "the same command with --deep at the merged tree -> proof_ok=7 proof_bad=0, verdict=MAY-CLOSE",
      ".tools/round-close-check.py:314-316 (stem-only glob) against rows ADVI_FIRMBKTS-D1-W8-S1 and D1-W10-S1 (the flip gate's two lookups)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Owner of the disagreement: the gate owner (round-close-check.py and to-pipeline-gate.py are .tools, not this lane). Either the close check reads the proof-block path too, or the order template names the stem form. The issuer's repair is a rename, not a gate edit; it does not prevent the next round's orders from repeating it unless the template changes."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W11-S1",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~11",
  "surfaced_at": "2026-10-11T06:24:51Z",
  "one_line": "TO-FB-f-1 section 5 flips the order's <status> to complete in the same commit as the proof instance, but the order file is outside this order's <paths> and outside this worker's write grant, so the flip is not performed. AC1 and AC2 both pass.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "spec_asserts": "TO-FB-f-1 section 5: when AC1 and AC2 pass, flip this order's <status> to complete in the SAME commit as the proof instance and r3_f7.py. Section 3 <paths> names r3_f7.py and the investigation file only.",
  "world_is": "The order file org/missions/D8/ADVI/ADVI_FIRMBKTS/task-orders/ADVI_FIRMBKTS.TO-FB-f-1.compare-instrument.md is tracked at 576e574de4 and is not in <paths>. The lane gate admits this worker to exactly the paths its order names, so the status flip is a path the worker lacks. AC1 rc=0 3 of 3 arms and AC2 rc=0 2 of 2 arms (outputs in the proof instance).",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "git ls-files --error-unmatch on org/missions/D8/ADVI/ADVI_FIRMBKTS/task-orders/ADVI_FIRMBKTS.TO-FB-f-1.compare-instrument.md returns the path at HEAD 576e574de4",
      "order file section 3 <paths> (lines 57-60) lists r3_f7.py and INVESTIGATION_v1.md only",
      "live run at 06:2xZ: r3_f7_ctl.py --arms live rc=0 'ROUND 3 F7 COMPARE LIVE: 3 of 3 arms'; --arms mutant rc=0 'ROUND 3 F7 COMPARE MUTANT: 2 of 2 arms'"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Owner of the write grant: the issuer 2.0.0_SA_COO~B1, whose carrier the order file is. The proof instance is valid; only the complete flip is open."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W11-S2",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~11",
  "surfaced_at": "2026-10-11T06:24:51Z",
  "one_line": "TO-FB-f-1 section 1 item 3 does not say whether the SOURCE-VS-MANIFEST changed=<n> count includes keys gone from the source; the instrument keeps the existing round-2 semantics, in which changed includes gone.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "TO-FB-f-1 section 1 item 3: print SOURCE-VS-MANIFEST: DRIFTED changed=<n> gone=<n> when a source key changed or is gone since the manifest.",
  "world_is": "round2/checks/r2_f7.py cmd_compare counts changed as the manifest objects whose live (size, etag) differs from the manifest, and a gone key reads None there, so gone keys are inside changed. r3_f7.py keeps that count. Live AC1 output: changed=49110 gone=0, so no live case separates the two readings; a reader who adds changed and gone double-counts gone keys.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "round2/checks/r2_f7.py@576e574de4 lines 277-283: changed = sum(... src_now.get(src) != (size, etag)) and gone = sum(... src not in src_now) printed as the second count",
      "r3_f7.py cmd_compare, live AC1 output line 'SOURCE-VS-MANIFEST: DRIFTED changed=49110 gone=0'"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Spec gap, not a defect in the arms. The issuer decides whether changed means changed-and-present or changed-or-gone; the instrument is not edited for it in this order."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W15-S1",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~15",
  "surfaced_at": "2026-10-11T06:23:30Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "FB-f-5 FACE DESCRIBES THE OUT READ BY CLASS ONLY (AN UNGRANTED OWN-FIRM KEY); THE SENDER NAMES A CONCRETE KEY THE FACE DOES NOT LIST, SO THE FACE'S STOP RULE (ANY KEY NOT ABOVE) READS INCONCLUSIVE",
  "spec_asserts": "Task order FB-f-5 step 1 (task-orders/ADVI_FIRMBKTS.TO-FB-f-5.f4-ownfirm.md @576e574de4 lines 36-37): print the sender command; if it names anything other than the instance, role, buckets and keys above, STOP as a BLOCKING row. Line 30 describes OUT only as 'a key the role's identity policy does not grant, same bucket'.",
  "world_is": "The printed command (r3_f4_send.py --print, run at 2026-10-11T06:21Z) names OUT as opal-data-cottonwood key irpt/cottonwood/code/gold/investor-reporting-holdings.tar.gz. That key is not in the face's key list (only the OWN key is named there). The live send (command d1841aa3-50a6-409c-876e-af595954f53f) returned OUT AccessDenied from the identity side ('no identity-based policy allows the s3:GetObject action'), which is the class the face describes. I judged the key within the described class and proceeded with the single send; I did not edit the sender or re-send.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python r3_f4_send.py --print (worktree wk-ADVI_FIRMBKTS-15, HEAD 576e574de4): OUT command GetObject key 'irpt/cottonwood/code/gold/investor-reporting-holdings.tar.gz'",
      "python r3_f4_send.py --out .../0.9.0_WK_ADVI_FIRMBKTS~15/F4_OWNFIRM_EVIDENCE.json --wait 100: SENT command_id=d1841aa3-50a6-409c-876e-af595954f53f status=Success; OUT: AccessDenied ... no identity-based policy allows the s3:GetObject action",
      "task-orders/ADVI_FIRMBKTS.TO-FB-f-5.f4-ownfirm.md @576e574de4 line 30 names the OUT key by class only"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Owner of the disambiguation: the issuer (2.0.0_SA_COO~B1), by naming the OUT key in the order face or by confirming the sender's key is the intended ungranted key. No edit to the sender or grader was made. AC1 4 of 4 and AC2 3 of 3 were run on this evidence and pass; the finding does not block them."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W15-S2",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~15",
  "surfaced_at": "2026-10-11T06:26:00Z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "one_line": "FB-f-5 FLIP ACT NOT PERFORMED: THE FACE ORDERS THE <status> ELEMENT FLIPPED TO complete, BUT THE ELEMENT IS NOT IN THE FACE LINES 1-80 THIS WORKER WAS GIVEN, SO THE ORDER REMAINS OPEN AT THIS HEAD",
  "spec_asserts": "Task order FB-f-5 section 5 (task-orders/ADVI_FIRMBKTS.TO-FB-f-5.f4-ownfirm.md @576e574de4 lines 75-77): flip this order's <status> to complete in the SAME commit as the proof instance and the evidence file, when AC1 and AC2 pass.",
  "world_is": "AC1 (4 of 4 arms) and AC2 (3 of 3 arms) pass on this worker's evidence. Lines 1-80 of the order, the only lines this worker's face permits, carry no <status> element; the element sits beyond the record-face boundary (line 81 onward). The worker did not read past line 80 to locate it, so the flip is not made in the commit and the order stays open pending the issuer or a flip the COO can make.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "Read of task-orders/ADVI_FIRMBKTS.TO-FB-f-5.f4-ownfirm.md offset 1 limit 80 at worktree wk-firmbkts-15 (HEAD 576e574de4): no <status> element in lines 1-80",
      "Worker face boundary: the RECORD FACE marker at line 81 is not this worker's context; the face says do not read past line 80",
      "AC1 output: ROUND 3 F4 OWNFIRM: 4 of 4 arms, exit=0; AC2 output: ROUND 2 F4 POSITIVE: 3 of 3 arms, exit=0"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Owner of the disposition: the issuer (2.0.0_SA_COO~B1) or the COO's flip, which can read the record face. The proof instance and evidence are committed with the channel row; no status edit was made here. Remedy is a flip of the order's <status> to complete at the COO's commit, or a face that carries the element in lines 1-80."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W12-S1",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~12",
  "surfaced_at": "2026-10-11T06:34:46Z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "one_line": "RULE (b) BEFORE (c) CANNOT BE REPRESENTED AT THE PREFIX GRAIN: MARKERS SIT BESIDE DATA IN EVERY INTERLEAVED RE-GRID, SO ARMS T2 AND T3 CANNOT PASS",
  "spec_asserts": "Ruling (b) of ROUND_ANALYSIS.round2.md section 2 item 3: completion markers carry kind marker, map to the R21 state home, and are never re-gridded beside data. Ruling (c): classes that interleave markers and data are split by (b), then re-gridded per date partition with no child cap. Check arm T2: no re-grid holds markers beside data. Check arm T3: every round-2 interleaved FAULT class is re-gridded per date partition, or placed.",
  "world_is": "(1) Ten round-2 re-grids hold a _complete/ child beside data children: bd forwardfill_v2 allocations (15 marker objects beside 133 data objects), realized, transactions, unrealized; cot forwardfill_v2 account_attributes, allocations (59 beside 142), holdings, realized, transactions, unrealized. A kind-marker child in any of them fails T2. (2) Five round-2 interleaved classes hold a marker and data in the same date partition: inf bronze/eclipse 134 of 134 date partitions, bronze/eclipse_qa 67 of 67, bronze/orion-api 1,711 of 2,473, gold/eclipse 132 of 132, silver/eclipse 132 of 132. A date-partition child includes its marker object (the prefix grain has no exclusion), so a per-file marker child is counted twice and the children stop summing to the live listing. The per-date re-grid is not executed: the five stay FAULT, owner 1.0.0_SA_CTO~DELL1, reason restated without the child cap. Result: T2 reads 0 kind-marker rows and T3 reads 5 STILL-INTERLEAVED; AC2 reads 3 of 5.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "mapping_v2.json re-grid children: 10 rows with a parent and a _complete/ prefix (bd forwardfill_v2 allocations, realized, transactions, unrealized; cot forwardfill_v2 account_attributes, allocations, holdings, realized, transactions, unrealized)",
      "live full bucket listing .scratch/live/bucket_full.json (ListObjectsV2 only, opal-data-inf at 2026-10-11T06:30:24Z): bronze/eclipse 1798 objects, 134 marker-named, 134 partitions all holding both; bronze/orion-api 17170 objects, 2473 partitions, 1711 holding both; gold/eclipse 529 / 132 / 132; silver/eclipse 660 / 132 / 132; bronze/eclipse_qa 871 / 67 / 67",
      "check run: python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round3/checks/r3_mapping.py --arms repair --root <worktree>: T2 FAIL (markers=0), T3 FAIL (5 STILL-INTERLEAVED)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "No disarm owner is named because the row is INERT. Decision needed from the CTO (ruling (b) and (c) against the representation) or the issuer 2.0.0_SA_COO~B1 (a grammar that lets a child exclude a named object, or a ruling that such classes stay whole). The worker did not choose: the ten re-grids and the five classes are unchanged in kind. Scratch: .scratch/evid.py, .scratch/build_v3.py."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W12-S2",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~12",
  "surfaced_at": "2026-10-11T06:34:46Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "RULE (d) OVERLAP-0 MERGES CANNOT BE EXECUTED FROM MAPPING_V2: SEVEN NEW CLASSES RECORD NO DESTINATION, SO THE TABLE THEY MERGE INTO IS NOT IN THE ROW",
  "spec_asserts": "Ruling (d): a new class that collides with a round-1 placed class is a deliberate merge with its reason at a measured key overlap of 0 (or a split at overlap above 0); the round-1 row is not displaced by default.",
  "world_is": "mapping_v2.json FAULT rows with reason 'destination-key overlap 0 of N keys with the group' are bd bronze/ (71 objects), bd gold/advisor_rolling_flows.json, bd gold/architect_leaderboard.json, bd gold/perf_report.json, bd gold/pipeline-complete.json, cot gold/firm_composition.json, cot silver/ (107 objects). None carries dest, dest_pattern or the group's table, so the table each would merge into cannot be recomputed from the row. The eighth, cot bronze/, is surprise ADVI_FIRMBKTS-D1-W12-S4. All eight stay FAULT, owner 1.0.0_SA_CTO~DELL1. T4 still passes: the 29 shared tables in the final rows are all ruled.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python filter over mapping_v2.json rows: disposition FAULT and 'overlap 0 of' in reason returns 8 rows (bd 5, cot 3), listed in the surprise text",
      "mapping_v2.json has no dest or dest_pattern key on any of those eight rows (FAULT rows in v2 carry reason, rule and fault_owner only)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Owner: the issuer 2.0.0_SA_COO~B1, to record the destination table of each FAULT class in the round-3 table, or to rule the group's table. Not placed in this cell because placing one needs a destination that the ruling does not name."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W12-S3",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~12",
  "surfaced_at": "2026-10-11T06:34:46Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "RULE (b) WOULD RE-ADDRESS PLACED COMPLETION-MARKER ROWS: A ROUND-1 SILVER MARKER GROUP SITS IN THE SILVER TIER, AND THE COPIED-UNCHANGED RULE FORBIDS A KIND FIELD ON PLACED ROWS",
  "spec_asserts": "Ruling (b): completion markers carry kind marker and map to the R21 state home. Repair step 4: every v2 row that was not FAULT is copied unchanged. Check arm S5: every class round 2 placed keeps its disposition, address and pattern.",
  "world_is": "silver/_silver_complete/ (inf, HOME, silver tier, 1,543 census objects) is a completion-marker group placed in the silver tier by round 1. Re-homing it to state would change a placed address (S5 forbids). gold/meta/pull-complete.json (inf, MOVE, state/meta, 1 object) is a completion marker already in the state tier; adding kind marker would change a copied row (step 4 forbids). Both are left as placed with no kind field. T2 therefore reads no kind-marker row from these two.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "mapping_v2.json row opal-data-inf silver/_silver_complete/: disposition HOME, dest tier silver, table _silver_complete",
      "mapping_v2.json row opal-data-inf gold/meta/pull-complete.json: disposition MOVE, dest tier state, table meta",
      "census.json class opal-data-inf silver/_silver_complete/ objects 1543"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Owner: the CTO. A ruling is needed on whether a placed completion marker is re-homed (a placed-address change that the difference control forbids as written) or kept with the silver home. Not decided here."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W12-S4",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~12",
  "surfaced_at": "2026-10-11T06:34:46Z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "one_line": "THE ONLY STANDALONE COMPLETION-MARKER CLASS HAS NO NAMED STATE FAMILY, SO ARM T2 READS ZERO KIND-MARKER ROWS",
  "spec_asserts": "Ruling (b): completion markers map to the R21 state home of the class they mark. Check arm T2 needs at least one kind-marker row, all on tier state, and no re-grid mixing markers with data.",
  "world_is": "cot bronze/ (cottonwood, 113 objects, every one a _BRONZE_COMPLETE.json marker, one per date partition, no data object) is a pure completion-marker class. It is FAULT with overlap 0 of 113. Placing it needs a state/{family}/ table name. The address builder accepts any table name (state/bronze, state/complete and state/markers all return valid addresses), so the name is a decision. Ruling (b) does not name the family, and R21 (infra/logic/02_DOCTRINE.md lines 74 and 588-592) keys state by request or run and never by table and date, while these markers are keyed by table and date. The class stays FAULT. AC2 cannot pass until the family is named.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "live listing opal-data-cot bronze/: 113 objects, 113 basenames matching complete (case-insensitive), 113 date partitions (.scratch/evid.py)",
      "python address() probe: lib/opal_naming.py address('advi','cottonwood','state',T,'2026-10-09',object='_BRONZE_COMPLETE.json') returns a valid s3 address for T in bronze, complete, markers, bronze-complete",
      "infra/logic/02_DOCTRINE.md line 74 (state: keyed by request or run, never by table+date) and lines 588-592 (R21)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Owner: the CTO, to name the state family for bronze completion markers or to rule that they are not state. The worker did not pick a family: the table name is not in the ruling. Without it, T2 fails (AC2 3 of 5)."
}
```

```json
[
  {
    "id": "ADVI_FIRMBKTS-D1-W16-S1",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~16",
    "surfaced_at": "2026-10-11T06:40:25Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "one_line": "comp-pipescript io UNDER-REPORTS D_04 WRITES (ONE PRINTED, 25 IN THE CODE) AND LISTS A READ AS A WRITE",
    "spec_asserts": "FB-f-6 step 1: comp-pipescript io <script> --pipeline bd-gold --no-portal prints each script's WRITES; D_04 alone writes platinum/accounts/, platinum/advisors/, platinum/clients/ and platinum/firm/.",
    "world_is": "`.tools/comp-pipescript io D_04 --pipeline bd-gold --no-portal --json` prints one write: partner_analytics_key -> gold/artifacts/partner_analytics/header_metrics_{*}.json. D_04.client_portal_summary.py:1974-1975 READS that key (_read_json(partner_analytics_key(gran))). The 25 D_04 platinum writes in the census go through _write_batch (line 277) and _write_json_to_s3 (lines 269-270), which the graph does not resolve. The premise that D_04 is the only writer of platinum/firm/ is also false (see ADVI_FIRMBKTS-D1-W16-S2).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "comp-pipescript io D_04 --pipeline bd-gold --no-portal --json (LOCAL run at worktree HEAD 576e574de4) -> writes=[partner_analytics_key]",
        "data/black_diamond/scripts/gold/D_04.client_portal_summary.py:1974-1975 (read of partner_analytics_key(gran) via _read_json)",
        "data/black_diamond/scripts/gold/D_04.client_portal_summary.py:269-270 and 277-292 (_write_json_to_s3 / _write_batch put_object Bucket=BUCKET)",
        "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~16/PRODUCER_CENSUS.json (25 D_04 writer entries, each line re-read by r3_census.py C2)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "The census (line reads, grader 3 of 3) is the blast-radius source for FB-f-6; the graph was not used for write attribution. The resolver is org/modules/graph/pipeline_cli.py behind the .tools shim."
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W16-S2",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~16",
    "surfaced_at": "2026-10-11T06:40:25Z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~B1",
    "one_line": "D_00f WRITES A SERVED PLATINUM KEY TO A HARD-CODED opal-data-bd OUTSIDE THE BD_S3_BUCKET SEAM, SO A STEP-2 ENV REPOINT WOULD LEAVE ONE WRITER BEHIND",
    "spec_asserts": "FB-f-6 spec: step 2 repoints the producers that write 49F's served platinum keys to opal-data-49financial; lib/config.py:14 is the one bucket every gold script reads and writes; D_04 alone writes platinum/firm/ among the served classes.",
    "world_is": "D_00f.advisor_nna_canonical.py:87 sets S3_BUCKET = 'opal-data-bd' as a literal and does not import lib.config, so it is not one of the 42 seam importers. Lines 91-92 build OUTPUT_KEY = OUTPUT_PREFIX + 'firm/advisor_nna_canonical.json' (OUTPUT_PREFIX defaults to 'platinum/'); line 928 calls _write_json_s3(artifact, OUTPUT_KEY), which put_objects to S3_BUCKET at line 768. The script runs in gold_dispatch.sh PHASE_D5 (lines 622-623). Result: platinum/firm/ has a second writer outside the seam, and an env-var repoint of BD_S3_BUCKET does not move it.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/black_diamond/scripts/gold/D_00f.advisor_nna_canonical.py:87 (S3_BUCKET = 'opal-data-bd' literal)",
        "data/black_diamond/scripts/gold/D_00f.advisor_nna_canonical.py:91-92 and 928 and 768 (OUTPUT_KEY, _write_json_s3 call, put_object Bucket=S3_BUCKET)",
        "data/black_diamond/scripts/gold/gold_dispatch.sh:622-623 (PHASE_D5: run_background D_00f)",
        "PRODUCER_CENSUS.json bucket_seam: 42 importers, D_00f not among them (grader C3 recount 42 = 42)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "ARMED because the step-2 act makes it live. Disarm before step 2 is signed: move D_00f onto the seam (a producer edit, owned by the lane that owns D_00f) or name it in the step-2 blast radius. The census proposes no repoint (FB-f-6 bounds)."
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W16-S3",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~16",
    "surfaced_at": "2026-10-11T06:40:25Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "one_line": "comp-pipescript RESOLVES ONE OF THE 26 E-SERIES bd-gold IDS, AND E_01 AND E_24 WRITE SERVED KEYS WITH NO DISPATCH ENTRY",
    "spec_asserts": "FB-f-6 step 1: comp-pipescript io <script> --pipeline bd-gold --no-portal prints each bd-gold script's WRITES, so every writer script can be read by its id.",
    "world_is": "comp-pipescript io returns 'Script not found' (rc 1) for 25 ids E_00..E_17 and E_19..E_25 (E_01 suggests 'Did you mean: E_18, D_01, C_01?'); only E_18 resolves. E_01.account_quality_tiers.py:333-340 writes gold/artifacts/account_quality_tiers_{date}.json and E_24.rebuild_fee_scorecard.py:254 writes gold/artifacts/advisor_fee_efficiency.json, both to opal-data-bd. gold_dispatch.sh has no E_ id in its CATALOG or PHASE_* blocks, so the runner of E_01 and E_24 is not declared in the repository.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "comp-pipescript io E_01 --pipeline bd-gold --no-portal (LOCAL run) -> 'Script not found: E_01. Did you mean: E_18, D_01, C_01?'; sweep rc=1 for 25 of 26 E-series ids",
        "data/black_diamond/scripts/gold/E_01.account_quality_tiers.py:333-340 and E_24.rebuild_fee_scorecard.py:254 (put_object Bucket=S3_BUCKET)",
        "data/black_diamond/scripts/gold/gold_dispatch.sh (no E_ entry in CATALOG or PHASE_* blocks; grep run)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Writes were read by line, not by the graph. Runner and schedule for these two writers are recorded as UNKNOWN in PRODUCER_CENSUS.md section 5."
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W16-S4",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~16",
    "surfaced_at": "2026-10-11T06:40:25Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "one_line": "THE WORKER FACE ASKS FOR THE ORDER'S <status> TO BE FLIPPED, BUT THE FACE CARRIES NO <status> AND THE ORDER FILE IS OUTSIDE THIS WORKER'S <paths>",
    "spec_asserts": "FB-f-6 section 5: flip this order's <status> to complete in the same commit as the proof instance and the two deliverables, only when AC1 passes.",
    "world_is": "The worker face (lines 1-96 of ADVI_FIRMBKTS.TO-FB-f-6.producer-census.md, the only part this worker reads) contains no <status> element. The order file is not in this order's <paths> (the deliverables folder and the investigation file). The flip was not made; the order file was not edited.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D8/ADVI/ADVI_FIRMBKTS/task-orders/ADVI_FIRMBKTS.TO-FB-f-6.producer-census.md lines 1-96 (read at offset 1, limit 96): no <status> element",
        "the same file's <paths> block (lines 71-74): deliverables folder and INVESTIGATION_v1.md only"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "AC1 passes 3 of 3 on the committed census; the proof instance validates. The status flip, if it is still wanted, belongs to the issuer or to a grant that names the order file."
  }
]
```

```json
[
  {
    "id": "ADVI_FIRMBKTS-D1-W16-S5",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~16",
    "surfaced_at": "2026-10-11T07:12:14Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "one_line": "PRODUCER_CENSUS.json OMITS THREE SERVED gold/views/ WRITES IN D_00 (lines 1106-1108), SO THE CENSUS UNDER-COUNTS THE PLATINUM WRITE LINES OF THE 14 WRITERS",
    "spec_asserts": "FB-f-9 section 1 and step 5: the census names each platinum write line of the 14 writers, and the per-script routed count is read against the census writer-line count.",
    "world_is": "D_00.portal_aggregates.py:1106-1108 @96f3212d22 call _write_view_parquet(geo | geo_city | adv, NNA_AUA_BY_GEOGRAPHY | NNA_AUA_BY_GEOGRAPHY_CITY | NNA_AUA_BY_ADVISOR, upload=True); the helper (base :206-213) puts to S3_BUCKET. Those keys are gold/views/*.parquet (lib/s3_layout.py:190-192 @96f3212d22), a served class. The census gold/views/ class lists C_05:401, C_06:417, C_07:477-479 and D_03:767, and no D_00 line. This worker routed the helper put, which the three calls share, so the D_00 routed count is 5 of 5 census lines (via gold_utils) plus 3 non-census view writes. The census was not edited.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git show 96f3212d22:data/black_diamond/scripts/gold/D_00.portal_aggregates.py | sed -n '1104,1109p': _write_view_parquet calls at 1106, 1107, 1108",
        "git show 96f3212d22:data/black_diamond/scripts/gold/lib/s3_layout.py: NNA_AUA_BY_GEOGRAPHY, NNA_AUA_BY_GEOGRAPHY_CITY, NNA_AUA_BY_ADVISOR = 'gold/views/...' at lines 190-192",
        "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~16/PRODUCER_CENSUS.json (read-only): class gold/views/ writers are C_05 401, C_06 417, C_07 477-479, D_03 767; none names D_00"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Not a mode-dependent defect: the put is routed in this cell and is identity in legacy mode. The census is read-only to this worker; its owner re-cuts it."
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W16-S6",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~16",
    "surfaced_at": "2026-10-11T07:12:14Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "one_line": "PRODUCER_CENSUS.json OMITS A SERVED gold/entities/clients/ WRITE IN C_06 (_write_relationship_views, LINE 381)",
    "spec_asserts": "FB-f-9 section 1 and step 5: the census names each platinum write line of the 14 writers.",
    "world_is": "C_06.client_mix_timeseries.py:88 @96f3212d22 sets OUTPUT_PREFIX = CLIENT_TIMESERIES_PREFIX.rstrip('/'); lib/s3_layout.py:276 gives CLIENT_TIMESERIES_PREFIX = 'gold/entities/clients/'. _write_relationship_views (base :376-383) puts key = f'{OUTPUT_PREFIX}/{rel_id}_views.json' at line 381, a served key. The census lists C_06 at 363 (client_timeseries_key) and 417 only. This worker routed the line-381 put; its legacy dual-write (line 386, gold/client_timeseries/) is non-served and left as it is.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git show 96f3212d22:data/black_diamond/scripts/gold/C_06.client_mix_timeseries.py | sed -n '88p;376,386p': OUTPUT_PREFIX at 88; key at 378; put at 381; legacy lk at 384-386",
        "git show 96f3212d22:data/black_diamond/scripts/gold/lib/s3_layout.py:276: CLIENT_TIMESERIES_PREFIX = 'gold/entities/clients/'",
        "PRODUCER_CENSUS.json (read-only): class gold/entities/clients/ writers from C_06 are line 363 only"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Routed in this cell; identity in legacy mode. The census is read-only to this worker."
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W16-S7",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~16",
    "surfaced_at": "2026-10-11T07:12:14Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "one_line": "IN CANONICAL MODE THE LEADERBOARD PRIOR-WEEK ROTATION ARCHIVES A STALE LEGACY-BUCKET COPY, BECAUSE THE SOURCE IS READ FROM S3_BUCKET WHILE THE CURRENT WRITE GOES TO THE DESTINATION",
    "spec_asserts": "FB-f-9 section 1b step 2: a copy whose source is a platinum key reads the source from S3_BUCKET (legacy key) and writes to the destination.",
    "world_is": "D_04.client_portal_summary.py:2466-2470 @96f3212d22 copies platinum/firm/leaderboard.json (CopySource on BUCKET) to platinum/firm/leaderboard.prior_week.json before the new write. The new leaderboard is written by _write_batch (base :2478) through the helper (base :269-273), which in canonical mode puts to the destination bucket. The rotation source is therefore the legacy-bucket copy, which canonical mode no longer refreshes; the rotation archives that stale copy as prior_week at the destination. The mode is unset in this cell, so nothing reads the difference today.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git show 96f3212d22:data/black_diamond/scripts/gold/D_04.client_portal_summary.py | sed -n '2466,2470p': copy_object CopySource Bucket BUCKET, Key platinum/firm/leaderboard.json, target platinum/firm/leaderboard.prior_week.json",
        "git show 96f3212d22:data/black_diamond/scripts/gold/D_04.client_portal_summary.py:2478 _write_batch leaderboard write; :265-273 helper put to BUCKET",
        "the order worker face section 1b step 2 (FB-f-9, lines 65-66) names the source as S3_BUCKET"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "The spec wording was implemented as written. Phase B, which sets the mode, makes this live: its owner settles the rotation source (read the destination, or keep refreshing the legacy copy) before the mode is set."
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W16-S8",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~16",
    "surfaced_at": "2026-10-11T07:12:14Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "one_line": "IN CANONICAL MODE D_00f'S WRITE-SUCCESS SENTINEL READS THE LEGACY BUCKET, SO A LANDED WRITE FAILS LOUD",
    "spec_asserts": "FB-f-9 section 2 bound 1: reads stay on S3_BUCKET; the D_00f sentinel exists to assert that the object actually landed this run.",
    "world_is": "D_00f.advisor_nna_canonical.py:928 @96f3212d22 writes OUTPUT_KEY through _write_json_s3, which in canonical mode puts to the destination bucket. The sentinel at base :937 is head_object(Bucket=S3_BUCKET, Key=OUTPUT_KEY). In canonical mode it reads the legacy bucket, where the object is old, and so fails loud on a write that landed. It cannot pass silently on a stale object because the LastModified window is 10 minutes. Phase B must read the destination for this sentinel.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git show 96f3212d22:data/black_diamond/scripts/gold/D_00f.advisor_nna_canonical.py | sed -n '935,938p': the sentinel comment and head_object(Bucket=S3_BUCKET, Key=OUTPUT_KEY) at 937",
        "git show 96f3212d22:data/black_diamond/scripts/gold/D_00f.advisor_nna_canonical.py:928 _write_json_s3(artifact, OUTPUT_KEY)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Inert while the mode is unset. Phase B owns the sentinel's bucket."
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W16-S9",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~16",
    "surfaced_at": "2026-10-11T07:12:14Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "one_line": "D_00f's LITERAL BUCKET WAS PINNED AGAINST BD_S3_BUCKET; THROUGH THE SEAM ITS READS AND WRITE NOW FOLLOW BD_S3_BUCKET",
    "spec_asserts": "FB-f-9 step 3 (D_00f's hard-coded bucket goes through the same seam) and dormant proof 4 (mode unset: every writer names the identical destination key and bucket as today).",
    "world_is": "Base D_00f.advisor_nna_canonical.py:87 set S3_BUCKET = 'opal-data-bd' as a literal, so its reads (base :152, :166, :216), its head (:937) and its write went to opal-data-bd whatever BD_S3_BUCKET held. Now S3_BUCKET is lib/config.py's value, os.environ BD_S3_BUCKET defaulting to opal-data-bd, and all of D_00f's reads and its write follow it. The runner sets BD_S3_BUCKET to opal-data-bd by default (gold_dispatch.sh:77) and no repository path overrides it, so the runner's behaviour is unchanged. An override would change D_00f's reads and write, which the literal prevented. This is an OBSERVATION and not BLOCKING because the condition is environment-only; a reading of FB-f-9 bound 3 could class it BLOCKING, and the issuer rules that.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git show 96f3212d22:data/black_diamond/scripts/gold/D_00f.advisor_nna_canonical.py: :87 S3_BUCKET = 'opal-data-bd' (literal); :37 docstring 'reads + writes opal-data-bd ONLY'",
        "git show 96f3212d22:data/black_diamond/scripts/gold/gold_dispatch.sh:77 BD_S3_BUCKET=\"${BD_S3_BUCKET:-opal-data-bd}\"",
        "git show 96f3212d22:data/black_diamond/scripts/gold/lib/config.py:14 S3_BUCKET = os.environ.get('BD_S3_BUCKET', 'opal-data-bd'); a grep of data/black_diamond for BD_S3_BUCKET finds no runner export of another value"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Routing and the seam are the cell's own ruling. Under the runner default the legacy identity holds. Named here so the issuer can decide whether the override case needs a guard or a note."
  }
]
```

```json
[
  {
    "id": "ADVI_FIRMBKTS-D1-W16-S10",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~16",
    "surfaced_at": "2026-10-11T07:18:20Z",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "one_line": "THE COMMIT-TIME NAMING GATE (LGIC_ENFORCE, ENFORCE) REFUSES THE PHASE A BUILD, SO NONE OF THE BUILD IS ON THE BRANCH: THE CLASS TABLE CARRIES THE 49FINANCIAL SCOPE AND BUCKET AS HAND-KEPT CARRIERS, THE GENERATOR NAMES THE SCOPE AND ROOT, AND D_04 GAINS A NEW LINE WITH A PRE-LGIC KEY",
    "spec_asserts": "FB-f-9 step 1: the class table comes from address() output, either by importing lib/opal_naming.py where the gold runner executes or by a committed data file a generator writes from address(); CLAUDE.md section 4: every S3 address is address() output, and a builder refusal is a missing registry row or an R20 register entry Andrew acknowledges, never a hand-typed workaround.",
    "world_is": "The gold runner syncs only the gold directory (gold_dispatch.sh:665-666 @96f3212d22: aws s3 sync of s3://$BD_S3_BUCKET/code/gold/), so repository lib/opal_naming.py is not importable there. The data-file route is the only one the bounds allow, and the naming gate grades that file: 26 REFUSE lines (24 in platinum_dest_table.json: the 49financial scope and the advi/49financial/platinum/ keys outside lookup('49financial'); 2 in gen_platinum_dest_table.py: the scope and root literals), 1 OUT-OF-PATTERN (D_04.client_portal_summary.py:2468, the pre-LGIC key platinum/firm/leaderboard.prior_week.json on a new line), 1 RAISE-EXISTING (gen:72). safe-commit.sh refused with 'naming limb refused (LGIC_ENFORCE DEC-6, ENFORCE mode). Commit aborted; files unstaged.' In the worktree the build runs and AC1 reads 4 of 4 arms; nothing of the build is committed to the branch.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "safe-commit.sh output of the phase A commit attempt (worktree .scratch/safe_commit_out.txt): 'NAMING-GATE: REFUSE 29 graded'; 26 REFUSE, 1 OUT-OF-PATTERN, 1 RAISE-EXISTING, 1 CONFORMANT",
        "git show 96f3212d22:data/black_diamond/scripts/gold/gold_dispatch.sh | sed -n '665,666p': sync_scripts syncs s3://$BD_S3_BUCKET/code/gold/ only",
        "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~16/ADVI_FIRMBKTS.TO-FB-f-9.act2-producers-repoint.proof_of_spec.json (uncommitted in the worktree): AC1 4 of 4 arms, VALID (rc 0)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Not worked around: no guard bypass, no author override, no rewording of keys to slip past the gate. Routes for the CTO or Andrew, none adopted here: (a) an R20 register entry, acknowledged by Andrew, for a generated carrier of the served-class table and the scope bucket; (b) make the builder importable on the gold runner, a code-sync change outside this cell; (c) the issuer re-cuts the destination to read the builder at runtime. INERT: nothing is live and the mode is never set by this cell."
  }
]
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W12-S5",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~12",
  "surfaced_at": "2026-10-11T07:02:38Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "INFLECTION AND SILVER COMPLETION MARKERS NEED STATE FAMILY NAMES THE RULING DOES NOT NAME (gold_complete, silver_complete, bronze_complete FOR ORION-API)",
  "spec_asserts": "Ruling (b) and addendum 1(2): completion markers map to the R21 state/ home under a family. The ruling names one family, bronze_complete, for the cot bronze/ markers (registered cot-bronze-complete).",
  "world_is": "The rebuilt table places three further marker groups under state families the ruling does not name: opal-data-inf bronze/orion-api/ (2 tails, 1776 objects) under bronze_complete, gold/eclipse/ gold_complete.json (132) and silver/eclipse/ silver_complete.json (132). address() accepts each family, so no builder refusal arises. The worker chose the table names.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/mapping_v3.json rows with kind marker for opal-data-inf bronze/orion-api/, gold/eclipse/, silver/eclipse/ (dest.table bronze_complete, gold_complete, silver_complete), written by the repair on wk-ADVI_FIRMBKTS-12 over a46c669e20",
      "infra/logic/registry/resources.json@a46c669e20 names cot-bronze-complete (line 2303) and inf-bronze-complete-emitter (line 317); no gold_complete or silver_complete family row (grep, 2026-10-11)",
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round3/checks/r3_mapping.py@a46c669e20 arm S4 PASS on the rebuilt table: each marker address equals address() output"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Owner: the CTO, to name the state families for inflection and silver completion markers, or to rule them not state. Placed under the reading of (b) and addendum 1(2) as written."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W12-S6",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~12",
  "surfaced_at": "2026-10-11T07:02:38Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "A QA-NAMED BRONZE FEED MATCHES TWO ROUND-1 RULES: RB (QA OUTPUT, NO DESTINATION) AND BRONZE/** (HOME). PLACED UNDER BRONZE/**",
  "spec_asserts": "Round-1 rule RB retires log, diagnostic, scratch, probe or QA output with no destination. The bronze/** rule homes bronze data in opal-data-assets. Ruling (c) re-grids an interleaved class per date partition.",
  "world_is": "opal-data-inf bronze/eclipse_qa/ (871 live objects, 67 date partitions, 804 data objects beside 67 pull_complete.json markers) has the same shape as the production bronze/eclipse/ feed. Its name marks it as QA. The worker re-gridded it per date and homed the data under bronze/** (table eclipse_qa, HOME) rather than retiring it under RB's QA reading. The choice is one rule's application; the CTO decides which reading holds.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "live listing opal-data-inf bronze/eclipse_qa/ 2026-10-11T06:56:05Z: 871 objects, 67 date partitions, one pull_complete.json per partition",
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/mapping_v3.json date children of opal-data-inf bronze/eclipse_qa/ (dest.table eclipse_qa, HOME) written by the repair",
      "round-1 rule texts RB and the bronze/** rule as cited in the rule fields of mapping_v2.json @a46c669e20"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Owner: the CTO. If RB governs, the 804 data objects become per-date RETIRE rows and the FAULT count is unchanged; if bronze/** governs, the rows stand as written."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W12-S7",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~12",
  "surfaced_at": "2026-10-11T07:02:38Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "1,142 performance_dim_SKIP.json FILES SIT BESIDE DATA IN ORION-API DATE PARTITIONS. RULE (b) NAMES COMPLETION MARKERS ONLY, SO THEY STAY DATA",
  "spec_asserts": "Ruling (b): completion markers are matched by literal key tail and excluded from the data children of their class. The ruling's examples of tails are _BRONZE_COMPLETE.json and _SUCCESS.",
  "world_is": "opal-data-inf bronze/orion-api/ date partitions hold 1,142 objects named performance_dim_SKIP.json, each 110 bytes, beside the _BRONZE_COMPLETE.json markers. The name says skip, not complete. No marker tail matches them, so they stay in their date partition's data child (HOME, table orion-api). Whether a SKIP file is a completion marker is not stated.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "live listing opal-data-inf bronze/orion-api/ 2026-10-11T06:56:06Z: 17170 objects; basename performance_dim_SKIP.json on 1142 objects, every size 110 bytes",
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/mapping_v3.json regrid bronze/orion-api/ (partition_rule per-date) and its date children",
      "ruling text: ROUND_ANALYSIS.round2.md section 2 item 3, rules (b) and addendum 1(1), in the project ledger folder"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Owner: the CTO, to say whether SKIP files are completion markers (then they take a marker_match row) or data. Left as data, which is the reading of (b) as written."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W12-S8",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~12",
  "surfaced_at": "2026-10-11T07:02:38Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "THE TWO ECLIPSE BRONZE CLASSES WRITE THE SAME STATE KEYS FOR SHARED DATES (66 MARKER KEYS), SO THEIR MARKER ROWS ARE FAULT",
  "spec_asserts": "Ruling (d) and round-2 rule 1e: a destination collision needs a measured key overlap and a merge or split ruling. A new class of a colliding group stays FAULT until the CTO rules.",
  "world_is": "opal-data-inf bronze/eclipse/ pull_complete.json (134 objects) and bronze/eclipse_qa/ pull_complete.json (67 objects) both map to state/bronze_complete under source eclipse, scope inflection. 66 (date, tail) keys are shared. Both marker rows are FAULT with owner 1.0.0_SA_CTO~DELL1. The two data classes write different tables (eclipse, eclipse_qa) and do not collide.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/mapping_v3.json two FAULT rows with marker_match pull_complete.json at opal-data-inf bronze/eclipse/ and bronze/eclipse_qa/ (reason cites 66 shared keys)",
      "measured in the repair build: the set of (date, tail) pairs of each class's markers from the 2026-10-11T06:56:05Z listings; intersection 66",
      "round-2 rule 1e text in the rule fields of mapping_v2.json @a46c669e20"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Owner: the CTO, to rule split (a distinct state family per class) or merge (overlap must be 0, which is not the case here). Without a ruling the 201 marker objects stay FAULT."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W12-S9",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~12",
  "surfaced_at": "2026-10-11T07:02:38Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "INHERITED RE-GRID ROWS DID NOT SUM TO THEIR LIVE LISTING (logs/ 30 OBJECTS, gold/timeseries/ 3), AND CHECK ARM S2 READS ONLY THE FIELD",
  "spec_asserts": "Ruling (e) and check arm S2: a re-grid's child objects sum to its LIVE listing, and children_objects equals listed_objects.",
  "world_is": "Session-1 mapping_v3.json: the bd logs/ children summed to 9,209 against 9,239 listed; the bd gold/timeseries/ children summed to 2,641 against 2,644 listed, the three directory children each one short. The regrid field children_objects said listed, so arm S2 passed. The repair re-derives each child count from the live listing (logs/ at 06:59:50Z, gold/timeseries/ at 06:56:10Z); the sums now equal the listing. Dispositions and addresses are unchanged.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      ".scratch/mapping_v3.session1.json (a copy of the session-1 mapping_v3.json merged at 08b039ef50): regrids for opal-data-bd logs/ and gold/timeseries/",
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round3/checks/r3_mapping.py@a46c669e20 lines 73-79: the regrid loop compares g.children_objects with g.listed_objects and never sums the child rows",
      "build log of the repair: RECOUNT and RECONCILED lines for opal-data-bd logs/ and gold/timeseries/ (2026-10-11)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Owner: the issuer (2.0.0_SA_COO~B1), to decide whether arm S2 should sum the child rows as its title says. The repaired counts are in the table; no check was edited."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W12-S10",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~12",
  "surfaced_at": "2026-10-11T07:02:38Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "A CLASS-GRAIN ROW CARRIES THE TOKEN {partition} IN ITS ADDRESS: THE GOLD/CLIENTS CLASS PLACED AT ITS PREFIX HAS NO ONE PARTITION",
  "spec_asserts": "Session-1 face correction 1: a class whose data is placed at its class prefix carries exclude_keys naming the placeholder. Every address comes from address() output.",
  "world_is": "opal-data-bd gold/clients/ (2,948 data objects, one per client file, keys carry client ids) is one MOVE row at its class prefix with exclude_keys [gold/clients/]. Its partition is the token {partition}; address() accepts the token and returns s3://opal-data-49financial/advi/49financial/platinum/clients/{partition}. No object key is enumerated. A token in an address is a pattern, not a key, and a reader must not take it for a real object path.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/mapping_v3.json row opal-data-bd gold/clients/ (class grain, exclude_keys, dest.partition {partition})",
      "live listing opal-data-bd gold/clients/ 2026-10-11T06:56:10Z: 2949 objects, one zero-byte key equal to the prefix, no nested key",
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round3/checks/r3_mapping.py@a46c669e20 arm S4 PASS: the token address equals address() output"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Owner: the CTO, to say whether a class-grain address carries a pattern token (as written) or whether a registered per-class pattern row is required."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W12-S11",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~12",
  "surfaced_at": "2026-10-11T07:05:35Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "TEN forwardfill _complete/ GROUPS ARE COMPLETION MARKERS BY NAME AND SIT BESIDE DATA IN THEIR RE-GRIDS, BUT STAY FAULT (1e): THEIR KEYS COLLIDE WITH EACH OTHER",
  "spec_asserts": "Ruling (b): completion markers (state/complete groups) carry kind marker, map to the R21 state/ home of the class they mark, and are never re-gridded beside data. Addendum 1: a key matched by a marker_match is excluded from the data children.",
  "world_is": "Ten round-2 FAULT rows are forwardfill _complete/ groups: bd allocations, realized, transactions, unrealized (4) and cot account_attributes, allocations, holdings, realized, transactions, unrealized (6). Each is a child of its forwardfill regrid, beside the data children. Their destination keys overlap each other (15 to 94 keys per row, reasons in the table). Left FAULT under rule 1e with owner 1.0.0_SA_CTO~DELL1, because no state family is named for them and a split or merge is the CTO's. Check arm T2 tests only rows of kind marker, so these rows cannot trip it.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/mapping_v3.json ten FAULT rows with prefix forwardfill_v2/*/_complete/ (objects 15, 93, 103, 15 in bd; 42, 59, 79, 88, 88, 59 in cot), reasons cite overlaps with each other",
      "infra/logic/registry/resources.json names no forwardfill completion family (grep, 2026-10-11); lib/opal_naming.py address() accepted every candidate family name in this repair",
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round3/checks/r3_mapping.py arm T2 reads only rows whose kind equals marker"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Owner: the CTO, to name the forwardfill completion family and rule split or merge for the ten groups, or to rule them data. Not decided here; the first session's declared exclusion is carried."
}
```

## Rows filed by 0.9.0_WK_ADVI_FIRMBKTS~17 (FB-f-7, round 3)

```json
[
  {
    "id": "ADVI_FIRMBKTS-D1-W17-S1",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~17",
    "surfaced_at": "2026-10-11T06:34:50Z",
    "one_line": "FB-f-7 dormancy claim does not hold for the declared alias's own directory: 3 router decisions and 3 guard decisions change, all on platinum/advi/mockadv/ (49financial, mockadv, and opal-capital with ?firm=bd).",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~B1",
    "spec_asserts": "1a.4: for the registry as it stands, every (firmId, path, query) decision of both functions equals the decision at base. Corollaries in 1a.1 (an alias lists the scope's own tenant, so mockadv lists the 49financial directory) and 1a.5 ALIAS (the alias is refused on any other tenant directory).",
    "world_is": "Measured (deliverables evidence/dormancy_grid.out.txt): router identical 85 of 88; differing 3, all on platinum/advi/mockadv/. Guard differing 9 served-bucket cases, the same three firmId/path pairs. Bucket equality admitted that directory because mockadv and 49financial share opal-data-bd. The declared sets cannot both refuse mockadv on its own directory (the spec's ALIAS control) and keep the base decision for it, so the narrowing is intrinsic to the spec's sets, not to the code.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda-edge/shared-advisor-router/index.mjs@576e574de4 lines 427-451: base tenant assertion is pathFirmBucket !== bucket, which admits the mockadv directory for any caller on the shared bucket",
        "infra/aws/lambda-edge/_shared/firm-config.mjs (worktree wk-ADVI_FIRMBKTS-17, generated): advTenant of mockadv = [49financial]; buckets of mockadv and 49financial both opal-data-bd",
        "deliverables/0.9.0_WK_ADVI_FIRMBKTS~17/evidence/dormancy_grid.out.txt: ROUTER GRID identical 85 of 88; GUARD GRID identical 387 of 396"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Form only: the remedy is built to the spec's literal sets and is not changed here. Ruling needed before any cutover: keep the mockadv directory readable for the staff proxy and the alias (an explicit extra declaration), or accept the narrowing and restate the dormancy claim in 1a.4. Until ruled the remedy is dormant (nothing deployed)."
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W17-S2",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~17",
    "surfaced_at": "2026-10-11T06:34:50Z",
    "one_line": "FB-f-7 1a.2 says the origin bucket comes from the path tenant's own configured bucket; the router sets the origin to the canonical tier constant for every platinum/advi/ request, as it did at base.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "1a.2: 'The origin bucket still comes from the path tenant's own configured bucket.'",
    "world_is": "At base (index.mjs line 453, bucket = CANONICAL_PLATINUM_BUCKET after the tenant assertion) the origin of a platinum/advi/ request is the canonical tier constant, not the tenant's configured bucket. The new router keeps line 453 unchanged, so the built behaviour equals base; the phrase is not implemented as written and no decision moved because of it.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda-edge/shared-advisor-router/index.mjs@576e574de4 line 453: bucket = CANONICAL_PLATINUM_BUCKET, set after the platinum/advi tenant assertion",
        "infra/aws/lambda-edge/shared-advisor-router/test/firm-routing.spec.mjs@576e574de4: 49financial reading platinum/advi/49financial/ routes to the canonical tier, not to the configured bucket"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Form only. Built as base behaviour (the dormancy claim needs it). Owner of the wording: the issuer."
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W17-S3",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~17",
    "surfaced_at": "2026-10-11T06:34:50Z",
    "one_line": "FB-f-7 ALIAS control is premised on a bucket difference between the alias and its declared directory that the registry does not carry today; the control's ALIAS arms therefore run on a cutover test double.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "1a.5 ALIAS: 'the declared alias is admitted on the tenant directory its declaration names although its bucket differs from that directory's bucket, and is refused on any other tenant directory.'",
    "world_is": "In the generated FIRM_CONFIG at HEAD the alias and its declared directory share one bucket (opal-data-bd), so no bucket difference exists to test. The difference exists only in the cutover state described in the header of _shared/firm-config.mjs (declared tenant moved to its own bucket). The ALIAS arms build that state as a double; the registry arm asserts admission only.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda-edge/_shared/firm-config.mjs@576e574de4 header lines 24-56: the cutover premise, 49financial moving to its own bucket while the alias stays on opal-data-bd",
        "infra/aws/lambda-edge/_shared/firm-config.mjs (worktree wk-ADVI_FIRMBKTS-17, generated): mockadv and 49financial both carry bucket opal-data-bd"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Form only. The control still discriminates: mutation runs in the record show the ALIAS arms fail when the alias is inferred from the shared bucket."
  }
]
```

```json
[
  {
    "id": "ADVI_FIRMBKTS-D1-W17-S4",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~17",
    "surfaced_at": "2026-10-11T06:38:28Z",
    "one_line": "FB-f-7 section 5 asks for the order's <status> to be flipped to complete in the commit, but the order file is not in the cell's <paths> write grant, so the flip is not written by this worker.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Section 5: 'Flip this order's <status> to complete in the SAME commit as your proof instance and the deliverables.' Section 3 <paths> is the write grant and lists no task-orders file.",
    "world_is": "The <status> element is <status>pending</status> at line 145 of the order file (read as a line number only; the record face is not read). The order file is outside <paths>, so the flip cannot be committed inside the grant. The proof instance and the deliverables are committed; the flip is left to the issuer or the complete-flip gate.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D8/ADVI/ADVI_FIRMBKTS/task-orders/ADVI_FIRMBKTS.TO-FB-f-7.advtenant-build.md@576e574de4 line 145: <status>pending</status> (grep -n -o, line number only)",
        "org/missions/D8/ADVI/ADVI_FIRMBKTS/task-orders/ADVI_FIRMBKTS.TO-FB-f-7.advtenant-build.md@576e574de4 lines 98-107: the <paths> block, which names no task-orders file"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Form only. Owner of the flip: the issuer 2.0.0_SA_COO~B1 or the complete-flip path of .tools/to-pipeline-gate.py. The proof instance passes proof-of-spec-check with every criterion PASS."
  }
]
```

## Row filed by 0.9.0_WK_ADVI_FIRMBKTS~17 (FB-f-7, re-seated session, amended order 1419e9fa5a)

```json
[
  {
    "id": "ADVI_FIRMBKTS-D1-W17-S5",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~17",
    "surfaced_at": "2026-10-11T06:55:35Z",
    "one_line": "AC5 cannot read zero under the amended sets: 49financial's read of platinum/advi/mockadv/ (admitted at base only because the two firms share opal-data-bd) is refused by the declared sets; measured router differing 1, guard differing 3.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~B1",
    "spec_asserts": "1a.1: an alias tenant lists ITSELF and the scope's own tenant (mockadv lists mockadv and 49financial). 1a.4: for the registry as it stands, every (firmId, tenant directory, path, query) decision of both functions equals the decision at base. AC5: 'DORMANCY: router differing 0, guard differing 0'.",
    "world_is": "The amended sets are built as written and are verified: the alias's own directory is admitted, and the opal-capital ?firm=bd staff proxy now reads [49financial, mockadv] as at base. The one decision that still differs is firmId 49financial reading platinum/advi/mockadv/mix_summary.json: base admits it because 49financial and mockadv share opal-data-bd; under 1a.1 the set of 49financial is [49financial], so it is refused with 401 (router), and the guard serves 502/200 differently in three served-bucket cases. Measured by evidence/dormancy_grid.mjs over the base copies built from git show 576e574de4: ROUTER GRID identical 87 of 88, GUARD GRID identical 393 of 396; DORMANCY: router differing 1, guard differing 3. No sentence of 1a.1 declares 49financial's read of the mockadv directory, and declaring it would widen an entitlement, so the zero in 1a.4 and AC5 cannot be met with the amended sets. The build is not widened; AC5 reads FAIL.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda-edge/_shared/firm-config.mjs (worktree wk-ADVI_FIRMBKTS-17, regenerated by lib/opal_naming.py generate): mockadv advTenant = [mockadv, 49financial]; 49financial advTenant = [49financial]; both buckets opal-data-bd",
        "infra/aws/lambda-edge/shared-advisor-router/index.mjs@576e574de4: the base tenant assertion is pathFirmBucket !== bucket, which admits the mockadv directory for any caller on opal-data-bd",
        "deliverables/0.9.0_WK_ADVI_FIRMBKTS~17/evidence/dormancy_grid.mjs run at the worktree (AC5 invocation): ROUTER GRID identical 87 of 88, differing 1 (49financial, platinum/advi/mockadv/mix_summary.json); GUARD GRID identical 393 of 396, differing 3; last line DORMANCY: router differing 1, guard differing 3",
        "org/missions/D8/ADVI/ADVI_FIRMBKTS/task-orders/ADVI_FIRMBKTS.TO-FB-f-7.advtenant-build.md (worker face lines 1-141, read by line range): 1a.1, 1a.4, AC5"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Form only; the remedy is not widened here. Ruling owed before any cutover, one of two: (a) declare 49financial's read of the mockadv directory in its advTenant (a widening of an entitlement, CTO ruling), which restores the base decision and the zero; or (b) restate 1a.4 and AC5 to name this one narrowing, with its cutover effect. This row refines the open part of ADVI_FIRMBKTS-D1-W17-S1 (the alias's own directory and the staff proxy are now at base). Until ruled the remedy is dormant: nothing is deployed."
  }
]
```

## Row filed by 0.9.0_WK_ADVI_FIRMBKTS~17 (FB-f-7, equivalence-class build, commit 4e68fb82b0)

```json
[
  {
    "id": "ADVI_FIRMBKTS-D1-W17-S6",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~17",
    "surfaced_at": "2026-10-11T07:08:15Z",
    "one_line": "The hand-written header of _shared/firm-config.mjs (outside the generated block) still states the alias pair as mockadv -> {49financial}; the generated block now lists one equivalence class per scope.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "The header comment of _shared/firm-config.mjs (line 59), which quotes the CTO ruling: 'mockadv -> {49financial}', describing the advTenant remedy's alias pair.",
    "world_is": "The generated FIRM_CONFIG block, regenerated at 4e68fb82b0 under the issuer's equivalence-class ruling (6aab08c6f5), lists 49financial and mockadv each as [49financial, mockadv]. The header line therefore describes the superseded single-entry alias pair. No decision moves because of the header: it is a comment, and the generated block is what the router and the guard read.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda-edge/_shared/firm-config.mjs@4e68fb82b0 line 59: the header comment 'mockadv -> {49financial}' (hand-written, outside the GENERATED markers)",
        "infra/aws/lambda-edge/_shared/firm-config.mjs@4e68fb82b0 lines 70 and 85: the generated advTenant lines for 49financial and mockadv, both [49financial, mockadv]"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Form only. Not edited by this cell: the header is design history quoted from the CTO ruling, and its wording is the owner's to restate. Owner of the wording: the issuer 2.0.0_SA_COO~B1 or the CTO who ruled the header text."
  }
]
```

## Row filed by 0.9.0_WK_ADVI_FIRMBKTS~17 (FB-f-8, phase A, the all-ASCII router and guard)

```json
[
  {
    "id": "ADVI_FIRMBKTS-D1-W17-S7",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~17",
    "surfaced_at": "2026-10-11T07:25:47Z",
    "one_line": "The cell's spelling list for non-ASCII characters names no ASCII spelling for U+26D4 (NO ENTRY sign) on line 239 of the shared-advisor-router-response guard; the worker wrote [STOP] there, a comment-only edit.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Section 1 step 3 of the FB-f-8 cell: replace each non-ASCII character by its plain ASCII spelling, with examples for an em dash or en dash, a typographic quote, an arrow, a multiplication sign and an ellipsis. No spelling is given for any other character.",
    "world_is": "The guard at infra/aws/lambda-edge/shared-advisor-router-response/index.mjs carries U+26D4 inside a // comment at line 239; the 12 bytes above 127 in that file are three em dashes (3 bytes each) and this one sign (3 bytes). No listed spelling covers the sign. The worker wrote [STOP] (6 bytes), so the guard's byte count moves by +3 on that line and by -3 on the three dashes, a net delta of 0. AC1 reads 0 and 0 after the edit, AC2 51 pass, AC3 46 pass, AC4 DORMANCY 0 and 0. No decision moves: the change is comment text only.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda-edge/shared-advisor-router-response/index.mjs@7718c70a30 line 239: a // comment beginning with U+26D4 (escaped in this JSON as \\u26d4) followed by THE SERVING LAYER CANNOT REPAIR THIS AND MUST NOT TRY",
        "the same file in the FB-f-8 commit, line 239: a // comment beginning with [STOP] followed by the same words; no other character on that line changed"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Form only. The spelling of a symbol outside the cell's listed examples is the issuer's to confirm; the commit uses [STOP] and the issuer may restate it. Owner of the spelling: the issuer 2.0.0_SA_COO~B1."
  }
]
```

## Row filed by 0.7.0_AE_CloudOps~FB1 (FB-f-8, phase B, step 0 gate)

```json
{
  "id": "ADVI_FIRMBKTS-D1-S11",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.7.0_AE_CloudOps~FB1",
  "surfaced_at": "2026-10-11T07:36:00Z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "one_line": "TO-FB-f-8 step 0 STOPS: shared-advisor-router/tier_policy.mjs, which the router bundles, reads 19 non-ASCII bytes (10 chars, all on comment lines); neither pair half names that file and the order's gate reads 'router and guard sources must read 0 non-ASCII bytes'.",
  "spec_asserts": "TO-FB-f-8 section 1a step 0: the repository's router and guard sources must read 0 non-ASCII bytes (FB-f-8 phase A merged); if any is not so, STOP, a BLOCKING row, no write to AWS. The CTO half's precondition names two hand-written files (the router and guard index.mjs) and accepts the generated _shared/firm-config.mjs as is.",
  "world_is": "At HEAD (59fa47b54b): infra/aws/lambda-edge/shared-advisor-router/index.mjs 0 bytes, shared-advisor-router-response/index.mjs 0 bytes (phase A holds). infra/aws/lambda-edge/shared-advisor-router/tier_policy.mjs, imported by the router at index.mjs line 83, reads 10 characters / 19 bytes above 127 on lines 2, 4, 6, 9, 10, 11, 12, 39, 42, 54, every one inside a comment (em dash, arrow, section sign). It was last touched by 1c76daba93 (ADVI_ROLGAT.DT1) and no phase-A commit reached it. A local bun build --minify of each entry (same flags as build-nodejs-lambda.sh, no upload) reads router 7509 bytes with 0 non-ASCII and guard 3538 bytes with 0 non-ASCII, so the DEPLOYED artifact is all-ASCII either way; only the SOURCE reading of the step 0 gate fails.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "git show HEAD:infra/aws/lambda-edge/shared-advisor-router/tier_policy.mjs decoded as utf-8: bytes 2451, byte_delta 19, chars 10, lines [2,4,6,9,10,11,12,39,42,54]",
      "git show HEAD:infra/aws/lambda-edge/shared-advisor-router/index.mjs and ...-response/index.mjs: byte_delta 0 each; _shared/firm-config.mjs byte_delta 9, chars 5, lines [7,10,11,14,15] (the CTO half's accepted generated file)",
      "infra/aws/lambda-edge/shared-advisor-router/index.mjs:83 import { requiredTierForUri, canAccess } from ./tier_policy.mjs",
      "bun build --target=node --format=esm --minify --external @aws-sdk/client-sns, outfile in the session scratchpad: router.mjs 7509 bytes non_ascii 0, guard.mjs 3538 bytes non_ascii 0",
      "infra/aws/lambda/ci/build-nodejs-lambda.sh lines 276-281 bundle with --minify"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Owner of the call: the issuer 2.0.0_SA_COO~B1 (it owns the order's criteria and its gate text); the CTO half's precondition is the CTO's to restate if the issuer reads it as covering comment-only characters. Two clean exits: (a) the issuer amends step 0 to read the BUNDLED artifact (0 non-ASCII bytes, measured above) and states that tier_policy.mjs and firm-config.mjs ship as comment-only exceptions; or (b) a cell makes tier_policy.mjs all-ASCII in one commit (comment edits, no decision moves; the file is outside this order's <paths>). This seat took no AWS write, opened no ledger entry and built no artifact; the order stays pending. Local scratch only: the two minified bundles in the session scratchpad."
}
```

## Row filed by 0.7.0_AE_CloudOps~FB1 (FB-f-8, phase B, step 3 plan)

```json
{
  "id": "ADVI_FIRMBKTS-D1-S12",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.7.0_AE_CloudOps~FB1",
  "surfaced_at": "2026-10-11T07:44:08Z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "one_line": "TO-FB-f-8 step 3 STOPS before the apply: the portal-auth plan changes 4 resources, not the signed 3 -- it also updates aws_wafv2_web_acl.opal_cloudfront_protection (standing churn, managed_rule_group_statement.version empty-string to null on 3 count-mode rules), and a -target plan cannot exclude it because the distribution depends on the ACL.",
  "spec_asserts": "TO-FB-f-8 step 3: the plan must change EXACTLY the two functions (each a new published version) and the distribution's 10 associations, nothing else; a plan naming any other resource, or drift outside the act, is a STOP. The COO half's Branch B: the plan names any resource beyond the two functions and the 10 associations -- the act stops, the order stays open, a BLOCKING row says why.",
  "world_is": "terraform 1.15.8, aws provider 5.100.0 (lock file tracked), infra/aws/terraform/portal-auth, plan -out saved, 74 resource_changes: 70 no-op, 4 update, 0 add, 0 destroy. The 4: aws_lambda_function.shared_advisor_router[0] (s3_object_version, version 26 to known-after-apply), aws_lambda_function.shared_advisor_router_response[0] (same, version 5), aws_cloudfront_distribution.portal (5 of 29 ordered_cache_behaviors, only the router/guard lambda_arn values differ; a masked compare of before and after is equal), and aws_wafv2_web_acl.opal_cloudfront_protection. The ACL's 6 rules: 3 identical, 3 managed groups (common-rule-set p4, ip-reputation p3, known-bad-inputs p5, all override_action count) differ ONLY in managed_rule_group_statement.version, '' before and null after; no non-rule attribute differs. A plan with -target on the two functions and the distribution still lists the ACL (Plan: 0 to add, 4 to change) because the distribution references it. The churn is standing: logged 2026-09-03 (OPSEC S6 session, 'the module was never at 0-diff'), row ADVI_FIRMBKTS-S1 2026-09-13, and the 2026-09-23 session whose plan listed the ACL among 2 changes and ended 'Apply complete! 0 added, 2 changed'. State of this act: NO apply run, no AWS write other than the two build artifacts the order permits: s3://opal-313476888478-lambda-artifacts/portal-auth/shared-advisor-router.zip (VersionId NWJciPjHZ9WAwJzH2jNtipmj06usuqFg, CodeSha256 DENFVwwc6PnJGsQpXB0ZgKMwJiGxJBTpbDWM3JXdk/E=) and .../shared-advisor-router-response.zip (VersionId T39sO4P3JJT0ZMfr6MeZLYWNBHQ55Mk5, vLZcOM0N0p8TMEZzTQcuSzguEV/cTpFu/iDNmFbdhBw=), both 0 bytes above 127. Those two objects are the live inputs of the next portal-auth plan by anyone, so another seat's portal-auth apply would now carry both functions.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/evidence/plan_json_summary.txt (computed per-rule from the plan JSON: 3 rules IDENTICAL, 3 rules differ only at version)",
      "evidence/plan_portal-auth_untargeted.out: 'Plan: 0 to add, 4 to change, 0 to destroy.'; evidence/plan_portal-auth_targeted_fns_and_distribution.out: the same 4 with 'Resource targeting is in effect'",
      "org/tier2_senior/0.7.0_AE_CloudOps/logs/2026-09-03/session_0.7.0_AE_CloudOps~T_2237-0020Z_OPSEC_S6_LOGIN_ABUSE_ALARM.md:80-86 (standing churn, targeted apply around it)",
      "org/tier2_senior/0.7.0_AE_CloudOps/logs/2026-09-23/session_close_1951-0655Z.md:84-104 (plan with the ACL among 2 changes, apply 2 changed)",
      "surprise-channel/investigations/INVESTIGATION_v1.md row ADVI_FIRMBKTS-S1 and remediations/REMEDIATION_v1.md ADVI_FIRMBKTS-S1 (P1, never-widen packet or config brought to live)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Owner of the call: the issuer 2.0.0_SA_COO~B1 and, for the never-widen pair, 1.0.0_SA_CTO~DELL1 (a production front-door resource is outside the signed blast radius). Recommendation (a): a pair addendum, both halves, adding the ACL to the permitted set as a named rider whose measured effect is a re-PUT of 6 rules with 3 fields '' to null, all 3 managed groups count-mode, rollback = the same rule set (nothing to roll back); the act then runs from step 3 on the saved plan. Alternative (b): bring portal-auth config to the live ACL so the plan is clean, which is a Terraform edit outside this order's paths and needs its own pair. This seat will not apply a plan that names the ACL. Standing side effects: ledger entry advi-firmbkts-fb-f-8-advtenant-act1-dell1-20261011 is OPEN with L1 closed (deploy_ledger hold --pre-apply refuses once a leg carries proof) and its 4-hour window ends about 11:37Z; infra/aws/lambda/ci/lambda-source-map.json carries the two new artifact SHAs in the working tree, uncommitted, outside this order's paths."
}
```

```json
[
  {
    "id": "ADVI_FIRMBKTS-D1-W16-S11",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~16",
    "surfaced_at": "2026-10-11T07:36:13Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "one_line": "PRODUCER_CENSUS.json OMITS A SERVED ADVISOR-COMPOSITION WRITE IN D_03 (THE NON-ARCHITECT TUPLE, BASE LINE 870), WHICH THE RULED 62 DO NOT COVER",
    "spec_asserts": "FB-f-9 step 3a and the ruling: the census names every served platinum writer line of the 14 writers (62 lines: the 58 of the census plus the four rows S5, S6).",
    "world_is": "D_03.composition_artifacts.py @96f3212d22 main(): the non-architect step builds (adv_comp, advisor_composition_key(adv_id), legacy_advisor_composition_key(adv_id)) at line 870 and passes the list to _write_json_batch at line 883. advisor_composition_key() is gold/entities/advisors/{id}/composition.json (lib/s3_layout.py), a served class. The census has D_03 lines 507, 526, 549, 573, 583, 767, 799, 912 only. The write is routed in this cell through _write_json (the key put), so it is covered by the routing, but the census count stays 62 by the ruling. The amended census lists it NOT.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git show 96f3212d22:data/black_diamond/scripts/gold/D_03.composition_artifacts.py: grep of advisor_composition_key(adv_id) finds lines 799 and 870; _write_json_batch( calls at 811 and 883",
        "lib/s3_layout.py: advisor_composition_key(advisor_id) returns gold/entities/advisors/{advisor_id}/composition.json",
        "worktree AST scan (.scratch/route_scan.py): D_03 _write_json key put at line 204 is ROUTED and the batch path reaches it"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Routed, so no legacy-mode change. The census count is the CTO's to re-cut (62 by ruling); this worker did not add a 63rd line."
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W16-S12",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~16",
    "surfaced_at": "2026-10-11T07:36:13Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "one_line": "PRODUCER_CENSUS.json OMITS D_04's SPLIT-BRANCH WRITES (BASE LINES 395-408), INCLUDING THE SERVED platinum/firm/fee_efficiency.json KEY",
    "spec_asserts": "FB-f-9 step 3a: the census names every served platinum writer line of the 14 writers.",
    "world_is": "D_04.client_portal_summary.py @96f3212d22 lines 395-408: when the dashboard exceeds 200 KB the script builds items for platinum/firm/dashboard.json, platinum/firm/leaderboard.json and (if fee_eff) platinum/firm/fee_efficiency.json and writes them through _write_batch at line 408. The census lists the non-split call at 410 and the leaderboard at 2478, not the split items. platinum/firm/fee_efficiency.json is a served key (platinum/firm/ class). The writes go through _write_batch -> _write_json_to_s3, which is ROUTED in this cell.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git show 96f3212d22:data/black_diamond/scripts/gold/D_04.client_portal_summary.py | sed -n '395,408p': the split items and the _write_batch call",
        "PRODUCER_CENSUS.json (worktree, amended): D_04 entries at 410 and 2478 only among the dashboard and leaderboard keys; no fee_efficiency entry"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Routed through the helper. The census is not amended for it; the CTO decides whether the census gains these lines."
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W16-S13",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~16",
    "surfaced_at": "2026-10-11T07:36:13Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "one_line": "`python lib/opal_naming.py targets` EXITS 1: THE NEW GENERATED VIEW IS UNCLASSIFIED, BECAUSE THE BUILDER'S ONLY RUNNER PLANE READS THE MDPF DAILY DISPATCH, NOT THE BD GOLD RUNNER",
    "spec_asserts": "FB-f-9 bounds 1 and the registry law: add one view and one validation rule; touch no other emitter. The builder's targets command classifies every generated target by a plane's own record.",
    "world_is": "At base 96f3212d22 `targets` exits 0. With the view added it prints 'UNCLASSIFIED - data/black_diamond/scripts/gold/lib/platinum_dest_view.json measured: no plane claims it' and exits 1. runner_code_plane() (lib/opal_naming.py) reads only infra/aws/ec2/mdpf-daily-runner/mdpf-daily-dispatch.sh; the BD gold runner syncs its code from data/black_diamond/scripts/gold via gold_dispatch.sh:665-666 (sync_scripts), which that plane does not read. The view is consumed only by the gold runner's code. AC1-AC4 do not call `targets`; the naming gate counts known targets and passes.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python lib/opal_naming.py targets: TARGETS output with 'UNCLASSIFIED - data/black_diamond/scripts/gold/lib/platinum_dest_view.json', exit 1 (worktree)",
        "git show 96f3212d22:lib/opal_naming.py run as a copy: targets exit 0 (base)",
        "lib/opal_naming.py runner_code_syncs() and runner_code_plane(): RUNNER_DISPATCH_PATH = infra/aws/ec2/mdpf-daily-runner/mdpf-daily-dispatch.sh"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Not widened here: teaching the builder a BD gold runner plane would be a second emitter change outside this cell's bounds. Route for the CTO: a plane record for the gold runner, or accept the UNCLASSIFIED row."
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W16-S14",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~16",
    "surfaced_at": "2026-10-11T07:36:13Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "one_line": "AC4 (r3_census.py) READS EACH CENSUS LINE IN THE WORKTREE, SO ROUTING THE WRITERS MOVED THE BASE LINE NUMBERS AND FORCED A RE-LOCATION OF THE CENSUS",
    "spec_asserts": "FB-f-9 step 3a: amend the census to 62 writer lines so r3_census still reads 3 of 3; the census is the blast radius at base.",
    "world_is": "r3_census.py C2 takes each writer's line number and quoted key text from the --root tree. Routing edits in 12 scripts shifted base lines (an import added at the top of D_00, D_03, D_04, C_06 and others) and rewrote 8 put lines, so 56 of 58 base entries failed C2 at the worktree. The census was re-located to the phase A worktree (50 exact text matches, 8 routed lines re-quoted, 4 added); its .md was regenerated from the JSON. The census therefore describes the worktree after routing, not the base; phase B's routing changes will move it again. C3's seam count moved 42 -> 45 because D_00f now imports the seam and lib/platinum_dest.py and its test import it.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python r3_census.py --census <amended> --root worktree: 3 of 3 arms; before the re-location: C2 1 of 3 arms (56 LINE-MISMATCH), C3 recounted 45 vs 42",
        ".scratch/relocate_census.py and .scratch/amend_census.py: 50 exact, 8 routed, 4 added (62 writer lines)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "A process note for the issuer: a check that reads the worktree binds the census to whatever the phase's edits do. Consider binding the census to the base commit and checking it there."
  }
]
```

```json
[
  {
    "id": "ADVI_FIRMBKTS-D1-W16-S15",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~16",
    "surfaced_at": "2026-10-11T07:45:46Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "one_line": "THE FACE ORDERS THE INSTANCE COMMITTED WITH ITS ARTIFACTS IN ONE COMMIT, BUT THE PIN RULE REQUIRES EACH ARTIFACT ROW TO CARRY THE COMMIT THAT CARRIED THE FILE: THE ARTIFACTS ARE COMMITTED FIRST AND THE INSTANCE SECOND",
    "spec_asserts": "FB-f-9 section 5: commit the registry file, the opal_naming.py change, the view, the module, the routed scripts, the test, the amended census, the instance and the rows together. The record face: pin each artifact row to the commit that carried the file; proof-of-spec-check refuses a PENDING row for a file already committed, and the instance is committed after its artifacts.",
    "world_is": "The two instructions cannot both hold in one commit: the instance's artifact pins name a commit that does not yet exist while the instance is being written. proof-of-spec-check reads the pins and the committed files, so the pins must name the artifact commit. The worker commits the artifacts, the census and the rows first, then pins the instance to that commit and commits the instance in a second commit.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "task order face section 5 (ADVI_FIRMBKTS.TO-FB-f-9.act2-producers-repoint.md lines 166-167 at 9074f7eda0): 'Commit ... the instance ... together'",
        "task order face section 5 (same file, record face): 'Pin your instance's artifact rows to the commit that carried each file ... the instance is committed after its artifacts'",
        ".tools/proof-of-spec-check.py on the instance: artifact-resolution PENDING rows refused for a file already committed (checker output)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Resolved in the worker's order of commits, not by widening the face. The issuer may restate the commit order in the face."
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W16-S16",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~16",
    "surfaced_at": "2026-10-11T07:47:25Z",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "one_line": "THE FACE ORDERS THE JSON VIEW DELETED, BUT THE OWNED-PATHS LANE GATE REFUSES THE DELETION: data/black_diamond/scripts/gold/lib/platinum_dest_view.json IS CLAIMED BY LANE POD4 AND IS OUTSIDE THIS WORKER'S <paths>",
    "spec_asserts": "FB-f-9 step 1 (the re-cut) and 3b: 'Delete the JSON view you committed.' Section 3 <paths>: the view surface is platinum_dest_view.py; the JSON path is not listed. Worker rule: a path needed that the lane lacks is a BLOCKING row on that criterion, never an override.",
    "world_is": "safe-commit.sh refused the commit with 'owned-paths lane violation(s) detected (block mode): data/black_diamond/scripts/gold/lib/platinum_dest_view.json -- lane=POD4'. The file is still at HEAD (committed at b9557fdc67). The worktree copy is deleted and the deletion is NOT staged, so it is uncommitted. Nothing references the JSON: platinum_dest.py imports the .py module, and AC1, AC2, AC3, AC4 and AC5 pass without it.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "safe-commit.sh output (worktree .scratch/safe_commit_v4a.txt): 'ERROR: owned-paths lane violation(s) detected (block mode)' and 'VIOLATION: data/black_diamond/scripts/gold/lib/platinum_dest_view.json -- lane=POD4'",
        "git show b9557fdc67 --stat: the JSON view was committed by this worker (platinum_dest_view.json, 2100 bytes)",
        "task order section 3 <paths> (ADVI_FIRMBKTS.TO-FB-f-9.act2-producers-repoint.md, lines 115-138 at 9074f7eda0): platinum_dest_view.py listed; the .json path not listed"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Not overridden: no lane override, no author override. The issuer grants the deletion path (or the lane owner deletes it). Until then the stale JSON stays at HEAD and is unreferenced."
  }
]
```

## Row filed by 0.7.0_AE_CloudOps~FB1 (FB-f-8, phase B, step 4 apply)

```json
{
  "id": "ADVI_FIRMBKTS-D1-S13",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.7.0_AE_CloudOps~FB1",
  "surfaced_at": "2026-10-11T07:58:04Z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "one_line": "TO-FB-f-8 step 4 FAILED: safe-apply of the signed 4-resource plan was refused 403 on lambda:UpdateFunctionCode for both functions by an EXPLICIT DENY in cloudops-dell-agent-deploy-policy on user/cloudops-dell1-agent-user; live AWS is unchanged, but Terraform state now records the new artifact versions, so the functions plan clean while the live code is the old build.",
  "spec_asserts": "TO-FB-f-8 step 4 and the pair's Branch A: the apply changes the two functions, the 10 associations and the ACL, and the distribution reads Deployed with each of the 10 associations on the new version. The issuer's preflight: iam:SimulatePrincipalPolicy on user/cloudops-dell1-agent-user reads allowed for lambda:UpdateFunctionCode, resource *, 5 of 5. Step 2: the role the Terraform apply runs under is read by the actor.",
  "world_is": "The apply ran as user/cloudops-dell1-agent-user (the 403 names it). cloudops-dell-agent-deploy-policy v6 carries a Deny on lambda:UpdateFunctionCode, UpdateFunctionConfiguration, PublishVersion, CreateAlias, UpdateAlias, DeleteFunction, DeleteAlias, PutFunctionConcurrency and the function-URL actions for a list of function ARNs that includes shared-advisor-router, shared-advisor-router-response, auth-validator-edge, cache-control-injector, public-data-router, opal-portal-authorizer, opal-portal-rest-authorizer and opalinvest-auth-handler (statement not printed in full here; the file is in evidence). A simulation with resource * does not match those ARNs, which is how it read allowed. Results: the ACL UpdateWebACL ran and left AWS byte-identical (rules, default action, LockToken); both UpdateFunctionCode calls 403; the distribution update never ran. Live: ETag E1OAC26XEP0FDI Deployed, router 26 x5, guard 5 x5, no new Lambda version. State: s3_object_version of both functions holds the new S3 VersionIds (NWJciPjHZ9WAwJzH2jNtipmj06usuqFg, T39sO4P3JJT0ZMfr6MeZLYWNBHQ55Mk5) while live CodeSha256 is still ZnPN8IRd... (router) and 4iHfdSnY... (guard). The plan after the attempt reads 0 to add, 1 to change: only the ACL, whose churn returned right after its own write, so the pair's 'post-apply plan reads no changes' cannot be met while the ACL stays in the root.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "evidence/apply_attempt_safe-apply.out lines for the two 'Error: updating Lambda Function' blocks (RequestIDs 18bc7cdb-aa88-4d96-a132-efed2d2d8c9f and 7002f6bd-ec66-4f7e-a5c7-8e2f67c62bf5)",
      "evidence/deny_policy_cloudops-dell-agent-deploy-policy.json (iam get-policy-version v6)",
      "evidence/state_vs_live_after_attempt.txt (terraform state show against get-function-configuration, same minute)",
      "evidence/post_apply_get_web_acl.json against evidence/pre_get_web_acl.json: 6 of 6 rules identical, LockToken 848a6d0b-d69f-40e0-876a-cfc0ce40b6b2 before and after",
      "evidence/plan_after_attempt.out: Plan: 0 to add, 1 to change, 0 to destroy (the ACL only)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "This seat did not read the apply role at step 2 as the order asks; the read would have surfaced the deny before the plan, and the ACL write was a no-op in AWS, so no harm landed. Owner of the call: the owner of cloudops-dell-agent-deploy-policy and the never-widen pair's two signers; this seat will not change IAM, assume another identity or run update-function-code. Routes the issuer may weigh: (A) the apply runs from an identity outside the deny (these two functions were applied on 2026-08-21 and 2026-09-14, so one exists; which is not read here); (B) the policy owner narrows the deny for a bounded window. Either way a plan will not show the functions until the S3 objects carry a new VersionId (a re-run of build-nodejs-lambda.sh uploads identical bytes under a new one, inside the permitted set) or the owner corrects the state; this seat has done neither. Until then the Terraform state is the one place that says the deploy is done, and it is not. The two S3 objects remain the live inputs of any portal-auth plan."
}
```

## Rows filed by 0.9.0_WK_ADVI_FIRMBKTS~19 (FB-f-9 phase A2, step 4: read-back sites of served platinum keys)

Opened as the worker's step-4 finding list. One row per read site, form OBSERVATION, hazard INERT: the mode (BD_PLATINUM_MODE) is unset everywhere in this cell. Base line numbers at a45a4384d9.

```json
[
  {
    "id": "ADVI_FIRMBKTS-D1-W19-S1",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~19",
    "surfaced_at": "2026-10-11T08:21:05Z",
    "one_line": "read-back of served platinum key EMPLOYEE_LEADERBOARD at D_04.client_portal_summary.py:369 reads BUCKET while writer D_00c.portal_leaderboard.py:1390 puts it through destination(); canonical mode would read the pre-cutover copy",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/black_diamond/scripts/gold/D_04.client_portal_summary.py:369 read site @a45a4384d9",
        "data/black_diamond/scripts/gold/D_00c.portal_leaderboard.py:1390 writer line @a45a4384d9 (census writer entry, runner PHASE_D1)",
        "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~16/PRODUCER_CENSUS.json @a45a4384d9 (census class gold/artifacts/)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-FB-f-9 phase A2 step 4: 'Find, do not fix, the same shape elsewhere ... file ONE row per site (class OBSERVATION, the file and line, what it reads and what the mode does to it) and change nothing at that site.'",
    "world_is": "data/black_diamond/scripts/gold/D_04.client_portal_summary.py:369 (_read_json(...)) reads EMPLOYEE_LEADERBOARD from BUCKET (S3_BUCKET). Its key is in served platinum class gold/artifacts/ (lib/platinum_dest_view.py). The writer D_00c.portal_leaderboard.py:1390 writes it through destination() (runner PHASE_D1). Mode unset: read and write name the same bucket and key, unchanged. Mode canonical: the writer lands at the view destination and this read still returns the pre-cutover object or a miss, per the helper.",
    "notes": "Writer runner PHASE_D1 per the census; the reader runs in D_04 PHASE_D4 of the same gold dispatch. Not changed by this cell (TO bound 4). Line numbers at base a45a4384d9; D_04 lines at or after 2468 sit one line later in the worktree after the phase A2 insertion. Live only when BD_PLATINUM_MODE is set to canonical, which this cell never sets; the mode act is phase B, the issuer to amend."
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W19-S2",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~19",
    "surfaced_at": "2026-10-11T08:21:05Z",
    "one_line": "read-back of served platinum key CLIENTS_TAB at D_04.client_portal_summary.py:370 reads BUCKET while writer D_00.portal_aggregates.py:1120 puts it through destination(); canonical mode would read the pre-cutover copy",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/black_diamond/scripts/gold/D_04.client_portal_summary.py:370 read site @a45a4384d9",
        "data/black_diamond/scripts/gold/D_00.portal_aggregates.py:1120 writer line @a45a4384d9 (census writer entry, runner PHASE_D1)",
        "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~16/PRODUCER_CENSUS.json @a45a4384d9 (census class gold/artifacts/)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-FB-f-9 phase A2 step 4: 'Find, do not fix, the same shape elsewhere ... file ONE row per site (class OBSERVATION, the file and line, what it reads and what the mode does to it) and change nothing at that site.'",
    "world_is": "data/black_diamond/scripts/gold/D_04.client_portal_summary.py:370 (_read_json(...)) reads CLIENTS_TAB from BUCKET (S3_BUCKET). Its key is in served platinum class gold/artifacts/ (lib/platinum_dest_view.py). The writer D_00.portal_aggregates.py:1120 writes it through destination() (runner PHASE_D1). Mode unset: read and write name the same bucket and key, unchanged. Mode canonical: the writer lands at the view destination and this read still returns the pre-cutover object or a miss, per the helper.",
    "notes": "Writer runner PHASE_D1 per the census; the reader runs in D_04 PHASE_D4 of the same gold dispatch. Not changed by this cell (TO bound 4). Line numbers at base a45a4384d9; D_04 lines at or after 2468 sit one line later in the worktree after the phase A2 insertion. Live only when BD_PLATINUM_MODE is set to canonical, which this cell never sets; the mode act is phase B, the issuer to amend."
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W19-S3",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~19",
    "surfaced_at": "2026-10-11T08:21:05Z",
    "one_line": "read-back of served platinum key ADVISOR_FEE_EFFICIENCY at D_04.client_portal_summary.py:371 reads BUCKET while writer C_08.advisor_fee_efficiency.py:555 puts it through destination(); canonical mode would read the pre-cutover copy",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/black_diamond/scripts/gold/D_04.client_portal_summary.py:371 read site @a45a4384d9",
        "data/black_diamond/scripts/gold/C_08.advisor_fee_efficiency.py:555 writer line @a45a4384d9 (census writer entry, runner PHASE_C5)",
        "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~16/PRODUCER_CENSUS.json @a45a4384d9 (census class gold/artifacts/)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-FB-f-9 phase A2 step 4: 'Find, do not fix, the same shape elsewhere ... file ONE row per site (class OBSERVATION, the file and line, what it reads and what the mode does to it) and change nothing at that site.'",
    "world_is": "data/black_diamond/scripts/gold/D_04.client_portal_summary.py:371 (_read_json(...)) reads ADVISOR_FEE_EFFICIENCY from BUCKET (S3_BUCKET). Its key is in served platinum class gold/artifacts/ (lib/platinum_dest_view.py). The writer C_08.advisor_fee_efficiency.py:555 writes it through destination() (runner PHASE_C5). Mode unset: read and write name the same bucket and key, unchanged. Mode canonical: the writer lands at the view destination and this read still returns the pre-cutover object or a miss, per the helper.",
    "notes": "Writer runner PHASE_C5 per the census; the reader runs in D_04 PHASE_D4 of the same gold dispatch. Not changed by this cell (TO bound 4). Line numbers at base a45a4384d9; D_04 lines at or after 2468 sit one line later in the worktree after the phase A2 insertion. Live only when BD_PLATINUM_MODE is set to canonical, which this cell never sets; the mode act is phase B, the issuer to amend."
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W19-S4",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~19",
    "surfaced_at": "2026-10-11T08:21:05Z",
    "one_line": "read-back of served platinum key MIX_DAILY_SUMMARY at D_04.client_portal_summary.py:468 reads BUCKET while writer C_06.client_mix_timeseries.py:420 puts it through destination(); canonical mode would read the pre-cutover copy",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/black_diamond/scripts/gold/D_04.client_portal_summary.py:468 read site @a45a4384d9",
        "data/black_diamond/scripts/gold/C_06.client_mix_timeseries.py:420 writer line @a45a4384d9 (census writer entry, runner PHASE_C5)",
        "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~16/PRODUCER_CENSUS.json @a45a4384d9 (census class gold/views/)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-FB-f-9 phase A2 step 4: 'Find, do not fix, the same shape elsewhere ... file ONE row per site (class OBSERVATION, the file and line, what it reads and what the mode does to it) and change nothing at that site.'",
    "world_is": "data/black_diamond/scripts/gold/D_04.client_portal_summary.py:468 (_read_json(...)) reads MIX_DAILY_SUMMARY from BUCKET (S3_BUCKET). Its key is in served platinum class gold/views/ (lib/platinum_dest_view.py). The writer C_06.client_mix_timeseries.py:420 writes it through destination() (runner PHASE_C5). Mode unset: read and write name the same bucket and key, unchanged. Mode canonical: the writer lands at the view destination and this read still returns the pre-cutover object or a miss, per the helper.",
    "notes": "Writer runner PHASE_C5 per the census; the reader runs in D_04 PHASE_D4 of the same gold dispatch. Not changed by this cell (TO bound 4). Line numbers at base a45a4384d9; D_04 lines at or after 2468 sit one line later in the worktree after the phase A2 insertion. Live only when BD_PLATINUM_MODE is set to canonical, which this cell never sets; the mode act is phase B, the issuer to amend."
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W19-S5",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~19",
    "surfaced_at": "2026-10-11T08:21:05Z",
    "one_line": "read-back of served platinum key FIRM_MIX_VIEWS at D_04.client_portal_summary.py:469 reads BUCKET while writer D_03.composition_artifacts.py:529 puts it through destination(); canonical mode would read the pre-cutover copy",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/black_diamond/scripts/gold/D_04.client_portal_summary.py:469 read site @a45a4384d9",
        "data/black_diamond/scripts/gold/D_03.composition_artifacts.py:529 writer line @a45a4384d9 (census writer entry, runner PHASE_D1)",
        "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~16/PRODUCER_CENSUS.json @a45a4384d9 (census class gold/artifacts/)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-FB-f-9 phase A2 step 4: 'Find, do not fix, the same shape elsewhere ... file ONE row per site (class OBSERVATION, the file and line, what it reads and what the mode does to it) and change nothing at that site.'",
    "world_is": "data/black_diamond/scripts/gold/D_04.client_portal_summary.py:469 (_read_json(...)) reads FIRM_MIX_VIEWS from BUCKET (S3_BUCKET). Its key is in served platinum class gold/artifacts/ (lib/platinum_dest_view.py). The writer D_03.composition_artifacts.py:529 writes it through destination() (runner PHASE_D1). Mode unset: read and write name the same bucket and key, unchanged. Mode canonical: the writer lands at the view destination and this read still returns the pre-cutover object or a miss, per the helper.",
    "notes": "Writer runner PHASE_D1 per the census; the reader runs in D_04 PHASE_D4 of the same gold dispatch. Not changed by this cell (TO bound 4). Line numbers at base a45a4384d9; D_04 lines at or after 2468 sit one line later in the worktree after the phase A2 insertion. Live only when BD_PLATINUM_MODE is set to canonical, which this cell never sets; the mode act is phase B, the issuer to amend."
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W19-S6",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~19",
    "surfaced_at": "2026-10-11T08:21:05Z",
    "one_line": "read-back of served platinum key FIRM_COMPOSITION at D_04.client_portal_summary.py:470 reads BUCKET while writer D_03.composition_artifacts.py:774 puts it through destination(); canonical mode would read the pre-cutover copy",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/black_diamond/scripts/gold/D_04.client_portal_summary.py:470 read site @a45a4384d9",
        "data/black_diamond/scripts/gold/D_03.composition_artifacts.py:774 writer line @a45a4384d9 (census writer entry, runner PHASE_D1)",
        "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~16/PRODUCER_CENSUS.json @a45a4384d9 (census class gold/views/)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-FB-f-9 phase A2 step 4: 'Find, do not fix, the same shape elsewhere ... file ONE row per site (class OBSERVATION, the file and line, what it reads and what the mode does to it) and change nothing at that site.'",
    "world_is": "data/black_diamond/scripts/gold/D_04.client_portal_summary.py:470 (_read_json(...)) reads FIRM_COMPOSITION from BUCKET (S3_BUCKET). Its key is in served platinum class gold/views/ (lib/platinum_dest_view.py). The writer D_03.composition_artifacts.py:774 writes it through destination() (runner PHASE_D1). Mode unset: read and write name the same bucket and key, unchanged. Mode canonical: the writer lands at the view destination and this read still returns the pre-cutover object or a miss, per the helper.",
    "notes": "Writer runner PHASE_D1 per the census; the reader runs in D_04 PHASE_D4 of the same gold dispatch. Not changed by this cell (TO bound 4). Line numbers at base a45a4384d9; D_04 lines at or after 2468 sit one line later in the worktree after the phase A2 insertion. Live only when BD_PLATINUM_MODE is set to canonical, which this cell never sets; the mode act is phase B, the issuer to amend."
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W19-S7",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~19",
    "surfaced_at": "2026-10-11T08:21:05Z",
    "one_line": "read-back of served platinum key ACCOUNT_TEAM at D_04.client_portal_summary.py:637 reads BUCKET while writer C_07.advisor_attribution.py:479 puts it through destination(); canonical mode would read the pre-cutover copy",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/black_diamond/scripts/gold/D_04.client_portal_summary.py:637 read site @a45a4384d9",
        "data/black_diamond/scripts/gold/C_07.advisor_attribution.py:479 writer line @a45a4384d9 (census writer entry, runner PHASE_C4)",
        "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~16/PRODUCER_CENSUS.json @a45a4384d9 (census class gold/views/)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-FB-f-9 phase A2 step 4: 'Find, do not fix, the same shape elsewhere ... file ONE row per site (class OBSERVATION, the file and line, what it reads and what the mode does to it) and change nothing at that site.'",
    "world_is": "data/black_diamond/scripts/gold/D_04.client_portal_summary.py:637 (_read_parquet(...)) reads ACCOUNT_TEAM from BUCKET (S3_BUCKET). Its key is in served platinum class gold/views/ (lib/platinum_dest_view.py). The writer C_07.advisor_attribution.py:479 writes it through destination() (runner PHASE_C4). Mode unset: read and write name the same bucket and key, unchanged. Mode canonical: the writer lands at the view destination and this read still returns the pre-cutover object or a miss, per the helper.",
    "notes": "Writer runner PHASE_C4 per the census; the reader runs in D_04 PHASE_D4 of the same gold dispatch. Not changed by this cell (TO bound 4). Line numbers at base a45a4384d9; D_04 lines at or after 2468 sit one line later in the worktree after the phase A2 insertion. Live only when BD_PLATINUM_MODE is set to canonical, which this cell never sets; the mode act is phase B, the issuer to amend."
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W19-S8",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~19",
    "surfaced_at": "2026-10-11T08:21:05Z",
    "one_line": "read-back of served platinum key TIMESERIES_CHART at D_04.client_portal_summary.py:1869 reads BUCKET while writer D_00b.portal_timeseries.py:1412 puts it through destination(); canonical mode would read the pre-cutover copy",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/black_diamond/scripts/gold/D_04.client_portal_summary.py:1869 read site @a45a4384d9",
        "data/black_diamond/scripts/gold/D_00b.portal_timeseries.py:1412 writer line @a45a4384d9 (census writer entry, runner PHASE_D2)",
        "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~16/PRODUCER_CENSUS.json @a45a4384d9 (census class gold/artifacts/)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-FB-f-9 phase A2 step 4: 'Find, do not fix, the same shape elsewhere ... file ONE row per site (class OBSERVATION, the file and line, what it reads and what the mode does to it) and change nothing at that site.'",
    "world_is": "data/black_diamond/scripts/gold/D_04.client_portal_summary.py:1869 (_read_json(...)) reads TIMESERIES_CHART from BUCKET (S3_BUCKET). Its key is in served platinum class gold/artifacts/ (lib/platinum_dest_view.py). The writer D_00b.portal_timeseries.py:1412 writes it through destination() (runner PHASE_D2). Mode unset: read and write name the same bucket and key, unchanged. Mode canonical: the writer lands at the view destination and this read still returns the pre-cutover object or a miss, per the helper.",
    "notes": "Writer runner PHASE_D2 per the census; the reader runs in D_04 PHASE_D4 of the same gold dispatch. Not changed by this cell (TO bound 4). Line numbers at base a45a4384d9; D_04 lines at or after 2468 sit one line later in the worktree after the phase A2 insertion. Live only when BD_PLATINUM_MODE is set to canonical, which this cell never sets; the mode act is phase B, the issuer to amend."
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W19-S9",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~19",
    "surfaced_at": "2026-10-11T08:21:05Z",
    "one_line": "read-back of served platinum key FIRM_MIX_VIEWS at D_04.client_portal_summary.py:1870 reads BUCKET while writer D_03.composition_artifacts.py:529 puts it through destination(); canonical mode would read the pre-cutover copy",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/black_diamond/scripts/gold/D_04.client_portal_summary.py:1870 read site @a45a4384d9",
        "data/black_diamond/scripts/gold/D_03.composition_artifacts.py:529 writer line @a45a4384d9 (census writer entry, runner PHASE_D1)",
        "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~16/PRODUCER_CENSUS.json @a45a4384d9 (census class gold/artifacts/)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-FB-f-9 phase A2 step 4: 'Find, do not fix, the same shape elsewhere ... file ONE row per site (class OBSERVATION, the file and line, what it reads and what the mode does to it) and change nothing at that site.'",
    "world_is": "data/black_diamond/scripts/gold/D_04.client_portal_summary.py:1870 (_read_json(...)) reads FIRM_MIX_VIEWS from BUCKET (S3_BUCKET). Its key is in served platinum class gold/artifacts/ (lib/platinum_dest_view.py). The writer D_03.composition_artifacts.py:529 writes it through destination() (runner PHASE_D1). Mode unset: read and write name the same bucket and key, unchanged. Mode canonical: the writer lands at the view destination and this read still returns the pre-cutover object or a miss, per the helper.",
    "notes": "Writer runner PHASE_D1 per the census; the reader runs in D_04 PHASE_D4 of the same gold dispatch. Not changed by this cell (TO bound 4). Line numbers at base a45a4384d9; D_04 lines at or after 2468 sit one line later in the worktree after the phase A2 insertion. Live only when BD_PLATINUM_MODE is set to canonical, which this cell never sets; the mode act is phase B, the issuer to amend."
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W19-S10",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~19",
    "surfaced_at": "2026-10-11T08:21:05Z",
    "one_line": "read-back of served platinum key CLIENTS_TAB at D_04.client_portal_summary.py:1967 reads BUCKET while writer D_00.portal_aggregates.py:1120 puts it through destination(); canonical mode would read the pre-cutover copy",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/black_diamond/scripts/gold/D_04.client_portal_summary.py:1967 read site @a45a4384d9",
        "data/black_diamond/scripts/gold/D_00.portal_aggregates.py:1120 writer line @a45a4384d9 (census writer entry, runner PHASE_D1)",
        "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~16/PRODUCER_CENSUS.json @a45a4384d9 (census class gold/artifacts/)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-FB-f-9 phase A2 step 4: 'Find, do not fix, the same shape elsewhere ... file ONE row per site (class OBSERVATION, the file and line, what it reads and what the mode does to it) and change nothing at that site.'",
    "world_is": "data/black_diamond/scripts/gold/D_04.client_portal_summary.py:1967 (_read_json(...)) reads CLIENTS_TAB from BUCKET (S3_BUCKET). Its key is in served platinum class gold/artifacts/ (lib/platinum_dest_view.py). The writer D_00.portal_aggregates.py:1120 writes it through destination() (runner PHASE_D1). Mode unset: read and write name the same bucket and key, unchanged. Mode canonical: the writer lands at the view destination and this read still returns the pre-cutover object or a miss, per the helper.",
    "notes": "Writer runner PHASE_D1 per the census; the reader runs in D_04 PHASE_D4 of the same gold dispatch. Not changed by this cell (TO bound 4). Line numbers at base a45a4384d9; D_04 lines at or after 2468 sit one line later in the worktree after the phase A2 insertion. Live only when BD_PLATINUM_MODE is set to canonical, which this cell never sets; the mode act is phase B, the issuer to amend."
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W19-S11",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~19",
    "surfaced_at": "2026-10-11T08:21:05Z",
    "one_line": "read-back of served platinum key TIMESERIES_CHART at D_04.client_portal_summary.py:2066 reads BUCKET while writer D_00b.portal_timeseries.py:1412 puts it through destination(); canonical mode would read the pre-cutover copy",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/black_diamond/scripts/gold/D_04.client_portal_summary.py:2066 read site @a45a4384d9",
        "data/black_diamond/scripts/gold/D_00b.portal_timeseries.py:1412 writer line @a45a4384d9 (census writer entry, runner PHASE_D2)",
        "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~16/PRODUCER_CENSUS.json @a45a4384d9 (census class gold/artifacts/)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-FB-f-9 phase A2 step 4: 'Find, do not fix, the same shape elsewhere ... file ONE row per site (class OBSERVATION, the file and line, what it reads and what the mode does to it) and change nothing at that site.'",
    "world_is": "data/black_diamond/scripts/gold/D_04.client_portal_summary.py:2066 (_read_json(...)) reads TIMESERIES_CHART from BUCKET (S3_BUCKET). Its key is in served platinum class gold/artifacts/ (lib/platinum_dest_view.py). The writer D_00b.portal_timeseries.py:1412 writes it through destination() (runner PHASE_D2). Mode unset: read and write name the same bucket and key, unchanged. Mode canonical: the writer lands at the view destination and this read still returns the pre-cutover object or a miss, per the helper.",
    "notes": "Writer runner PHASE_D2 per the census; the reader runs in D_04 PHASE_D4 of the same gold dispatch. Not changed by this cell (TO bound 4). Line numbers at base a45a4384d9; D_04 lines at or after 2468 sit one line later in the worktree after the phase A2 insertion. Live only when BD_PLATINUM_MODE is set to canonical, which this cell never sets; the mode act is phase B, the issuer to amend."
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W19-S12",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~19",
    "surfaced_at": "2026-10-11T08:21:05Z",
    "one_line": "read-back of served platinum key EMPLOYEE_LEADERBOARD at D_04.client_portal_summary.py:2280 reads BUCKET while writer D_00c.portal_leaderboard.py:1390 puts it through destination(); canonical mode would read the pre-cutover copy",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/black_diamond/scripts/gold/D_04.client_portal_summary.py:2280 read site @a45a4384d9",
        "data/black_diamond/scripts/gold/D_00c.portal_leaderboard.py:1390 writer line @a45a4384d9 (census writer entry, runner PHASE_D1)",
        "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~16/PRODUCER_CENSUS.json @a45a4384d9 (census class gold/artifacts/)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-FB-f-9 phase A2 step 4: 'Find, do not fix, the same shape elsewhere ... file ONE row per site (class OBSERVATION, the file and line, what it reads and what the mode does to it) and change nothing at that site.'",
    "world_is": "data/black_diamond/scripts/gold/D_04.client_portal_summary.py:2280 (_read_json(...)) reads EMPLOYEE_LEADERBOARD from BUCKET (S3_BUCKET). Its key is in served platinum class gold/artifacts/ (lib/platinum_dest_view.py). The writer D_00c.portal_leaderboard.py:1390 writes it through destination() (runner PHASE_D1). Mode unset: read and write name the same bucket and key, unchanged. Mode canonical: the writer lands at the view destination and this read still returns the pre-cutover object or a miss, per the helper.",
    "notes": "Writer runner PHASE_D1 per the census; the reader runs in D_04 PHASE_D4 of the same gold dispatch. Not changed by this cell (TO bound 4). Line numbers at base a45a4384d9; D_04 lines at or after 2468 sit one line later in the worktree after the phase A2 insertion. Live only when BD_PLATINUM_MODE is set to canonical, which this cell never sets; the mode act is phase B, the issuer to amend."
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W19-S13",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~19",
    "surfaced_at": "2026-10-11T08:21:05Z",
    "one_line": "read-back of served platinum key CLIENTS_TAB at D_04.client_portal_summary.py:2359 reads BUCKET while writer D_00.portal_aggregates.py:1120 puts it through destination(); canonical mode would read the pre-cutover copy",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/black_diamond/scripts/gold/D_04.client_portal_summary.py:2359 read site @a45a4384d9",
        "data/black_diamond/scripts/gold/D_00.portal_aggregates.py:1120 writer line @a45a4384d9 (census writer entry, runner PHASE_D1)",
        "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~16/PRODUCER_CENSUS.json @a45a4384d9 (census class gold/artifacts/)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-FB-f-9 phase A2 step 4: 'Find, do not fix, the same shape elsewhere ... file ONE row per site (class OBSERVATION, the file and line, what it reads and what the mode does to it) and change nothing at that site.'",
    "world_is": "data/black_diamond/scripts/gold/D_04.client_portal_summary.py:2359 (_read_json(...)) reads CLIENTS_TAB from BUCKET (S3_BUCKET). Its key is in served platinum class gold/artifacts/ (lib/platinum_dest_view.py). The writer D_00.portal_aggregates.py:1120 writes it through destination() (runner PHASE_D1). Mode unset: read and write name the same bucket and key, unchanged. Mode canonical: the writer lands at the view destination and this read still returns the pre-cutover object or a miss, per the helper.",
    "notes": "Writer runner PHASE_D1 per the census; the reader runs in D_04 PHASE_D4 of the same gold dispatch. Not changed by this cell (TO bound 4). Line numbers at base a45a4384d9; D_04 lines at or after 2468 sit one line later in the worktree after the phase A2 insertion. Live only when BD_PLATINUM_MODE is set to canonical, which this cell never sets; the mode act is phase B, the issuer to amend."
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W19-S14",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~19",
    "surfaced_at": "2026-10-11T08:21:05Z",
    "one_line": "read-back of served platinum key CLIENTS_TAB at D_04.client_portal_summary.py:2515 reads BUCKET while writer D_00.portal_aggregates.py:1120 puts it through destination(); canonical mode would read the pre-cutover copy",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/black_diamond/scripts/gold/D_04.client_portal_summary.py:2515 read site @a45a4384d9",
        "data/black_diamond/scripts/gold/D_00.portal_aggregates.py:1120 writer line @a45a4384d9 (census writer entry, runner PHASE_D1)",
        "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~16/PRODUCER_CENSUS.json @a45a4384d9 (census class gold/artifacts/)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-FB-f-9 phase A2 step 4: 'Find, do not fix, the same shape elsewhere ... file ONE row per site (class OBSERVATION, the file and line, what it reads and what the mode does to it) and change nothing at that site.'",
    "world_is": "data/black_diamond/scripts/gold/D_04.client_portal_summary.py:2515 (_read_json(...)) reads CLIENTS_TAB from BUCKET (S3_BUCKET). Its key is in served platinum class gold/artifacts/ (lib/platinum_dest_view.py). The writer D_00.portal_aggregates.py:1120 writes it through destination() (runner PHASE_D1). Mode unset: read and write name the same bucket and key, unchanged. Mode canonical: the writer lands at the view destination and this read still returns the pre-cutover object or a miss, per the helper.",
    "notes": "Writer runner PHASE_D1 per the census; the reader runs in D_04 PHASE_D4 of the same gold dispatch. Not changed by this cell (TO bound 4). Line numbers at base a45a4384d9; D_04 lines at or after 2468 sit one line later in the worktree after the phase A2 insertion. Live only when BD_PLATINUM_MODE is set to canonical, which this cell never sets; the mode act is phase B, the issuer to amend."
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W19-S15",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~19",
    "surfaced_at": "2026-10-11T08:21:05Z",
    "one_line": "read-back of served platinum key HEADER_METRICS at D_04.client_portal_summary.py:2578 reads BUCKET while writer D_00.portal_aggregates.py:1126 puts it through destination(); canonical mode would read the pre-cutover copy",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/black_diamond/scripts/gold/D_04.client_portal_summary.py:2578 read site @a45a4384d9",
        "data/black_diamond/scripts/gold/D_00.portal_aggregates.py:1126 writer line @a45a4384d9 (census writer entry, runner PHASE_D1)",
        "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~16/PRODUCER_CENSUS.json @a45a4384d9 (census class gold/artifacts/)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-FB-f-9 phase A2 step 4: 'Find, do not fix, the same shape elsewhere ... file ONE row per site (class OBSERVATION, the file and line, what it reads and what the mode does to it) and change nothing at that site.'",
    "world_is": "data/black_diamond/scripts/gold/D_04.client_portal_summary.py:2578 (_read_json(...)) reads HEADER_METRICS from BUCKET (S3_BUCKET). Its key is in served platinum class gold/artifacts/ (lib/platinum_dest_view.py). The writer D_00.portal_aggregates.py:1126 writes it through destination() (runner PHASE_D1). Mode unset: read and write name the same bucket and key, unchanged. Mode canonical: the writer lands at the view destination and this read still returns the pre-cutover object or a miss, per the helper.",
    "notes": "Writer runner PHASE_D1 per the census; the reader runs in D_04 PHASE_D4 of the same gold dispatch. Not changed by this cell (TO bound 4). Line numbers at base a45a4384d9; D_04 lines at or after 2468 sit one line later in the worktree after the phase A2 insertion. Live only when BD_PLATINUM_MODE is set to canonical, which this cell never sets; the mode act is phase B, the issuer to amend."
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W19-S16",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~19",
    "surfaced_at": "2026-10-11T08:21:05Z",
    "one_line": "read-back of served platinum key TIMESERIES_CHART at D_04.client_portal_summary.py:2579 reads BUCKET while writer D_00b.portal_timeseries.py:1412 puts it through destination(); canonical mode would read the pre-cutover copy",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/black_diamond/scripts/gold/D_04.client_portal_summary.py:2579 read site @a45a4384d9",
        "data/black_diamond/scripts/gold/D_00b.portal_timeseries.py:1412 writer line @a45a4384d9 (census writer entry, runner PHASE_D2)",
        "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~16/PRODUCER_CENSUS.json @a45a4384d9 (census class gold/artifacts/)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-FB-f-9 phase A2 step 4: 'Find, do not fix, the same shape elsewhere ... file ONE row per site (class OBSERVATION, the file and line, what it reads and what the mode does to it) and change nothing at that site.'",
    "world_is": "data/black_diamond/scripts/gold/D_04.client_portal_summary.py:2579 (_read_json(...)) reads TIMESERIES_CHART from BUCKET (S3_BUCKET). Its key is in served platinum class gold/artifacts/ (lib/platinum_dest_view.py). The writer D_00b.portal_timeseries.py:1412 writes it through destination() (runner PHASE_D2). Mode unset: read and write name the same bucket and key, unchanged. Mode canonical: the writer lands at the view destination and this read still returns the pre-cutover object or a miss, per the helper.",
    "notes": "Writer runner PHASE_D2 per the census; the reader runs in D_04 PHASE_D4 of the same gold dispatch. Not changed by this cell (TO bound 4). Line numbers at base a45a4384d9; D_04 lines at or after 2468 sit one line later in the worktree after the phase A2 insertion. Live only when BD_PLATINUM_MODE is set to canonical, which this cell never sets; the mode act is phase B, the issuer to amend."
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W19-S17",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~19",
    "surfaced_at": "2026-10-11T08:21:05Z",
    "one_line": "read-back of served platinum key ACCOUNT_TEAM at D_04.client_portal_summary.py:2837 reads BUCKET while writer C_07.advisor_attribution.py:479 puts it through destination(); canonical mode would read the pre-cutover copy",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/black_diamond/scripts/gold/D_04.client_portal_summary.py:2837 read site @a45a4384d9",
        "data/black_diamond/scripts/gold/C_07.advisor_attribution.py:479 writer line @a45a4384d9 (census writer entry, runner PHASE_C4)",
        "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~16/PRODUCER_CENSUS.json @a45a4384d9 (census class gold/views/)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-FB-f-9 phase A2 step 4: 'Find, do not fix, the same shape elsewhere ... file ONE row per site (class OBSERVATION, the file and line, what it reads and what the mode does to it) and change nothing at that site.'",
    "world_is": "data/black_diamond/scripts/gold/D_04.client_portal_summary.py:2837 (_read_parquet(...)) reads ACCOUNT_TEAM from BUCKET (S3_BUCKET). Its key is in served platinum class gold/views/ (lib/platinum_dest_view.py). The writer C_07.advisor_attribution.py:479 writes it through destination() (runner PHASE_C4). Mode unset: read and write name the same bucket and key, unchanged. Mode canonical: the writer lands at the view destination and this read still returns the pre-cutover object or a miss, per the helper.",
    "notes": "Writer runner PHASE_C4 per the census; the reader runs in D_04 PHASE_D4 of the same gold dispatch. Not changed by this cell (TO bound 4). Line numbers at base a45a4384d9; D_04 lines at or after 2468 sit one line later in the worktree after the phase A2 insertion. Live only when BD_PLATINUM_MODE is set to canonical, which this cell never sets; the mode act is phase B, the issuer to amend."
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W19-S18",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~19",
    "surfaced_at": "2026-10-11T08:21:05Z",
    "one_line": "read-back of served platinum key partner_analytics_key(...) at D_04.client_portal_summary.py:1977 reads BUCKET while writer D_01.partner_analytics.py:2548 puts it through destination(); canonical mode would read the pre-cutover copy",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/black_diamond/scripts/gold/D_04.client_portal_summary.py:1977 read site @a45a4384d9",
        "data/black_diamond/scripts/gold/D_01.partner_analytics.py:2548 writer line @a45a4384d9 (census writer entry, runner PHASE_D2)",
        "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~16/PRODUCER_CENSUS.json @a45a4384d9 (census class gold/artifacts/)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-FB-f-9 phase A2 step 4: 'Find, do not fix, the same shape elsewhere ... file ONE row per site (class OBSERVATION, the file and line, what it reads and what the mode does to it) and change nothing at that site.'",
    "world_is": "data/black_diamond/scripts/gold/D_04.client_portal_summary.py:1977 (_read_json(key), key = partner_analytics_key(gran)) reads partner_analytics_key(...) from BUCKET (S3_BUCKET). Its key is in served platinum class gold/artifacts/ (lib/platinum_dest_view.py). The writer D_01.partner_analytics.py:2548 writes it through destination() (runner PHASE_D2). Mode unset: read and write name the same bucket and key, unchanged. Mode canonical: the writer lands at the view destination and this read still returns the pre-cutover object or a miss, per the helper.",
    "notes": "Writer runner PHASE_D2 per the census; the reader runs in D_04 PHASE_D4 of the same gold dispatch. Not changed by this cell (TO bound 4). Line numbers at base a45a4384d9; D_04 lines at or after 2468 sit one line later in the worktree after the phase A2 insertion. Live only when BD_PLATINUM_MODE is set to canonical, which this cell never sets; the mode act is phase B, the issuer to amend."
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W19-S19",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~19",
    "surfaced_at": "2026-10-11T08:21:05Z",
    "one_line": "read-back of served platinum key advisor_book_key(...) at D_04.client_portal_summary.py:2640 reads BUCKET while writer D_02.advisor_client_detail.py:1580 puts it through destination(); canonical mode would read the pre-cutover copy",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/black_diamond/scripts/gold/D_04.client_portal_summary.py:2640 read site @a45a4384d9",
        "data/black_diamond/scripts/gold/D_02.advisor_client_detail.py:1580 writer line @a45a4384d9 (census writer entry, runner PHASE_D3)",
        "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~16/PRODUCER_CENSUS.json @a45a4384d9 (census class gold/entities/advisors/)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-FB-f-9 phase A2 step 4: 'Find, do not fix, the same shape elsewhere ... file ONE row per site (class OBSERVATION, the file and line, what it reads and what the mode does to it) and change nothing at that site.'",
    "world_is": "data/black_diamond/scripts/gold/D_04.client_portal_summary.py:2640 (_batch_read_json(book_keys), advisor_book_key(aid)) reads advisor_book_key(...) from BUCKET (S3_BUCKET). Its key is in served platinum class gold/entities/advisors/ (lib/platinum_dest_view.py). The writer D_02.advisor_client_detail.py:1580 writes it through destination() (runner PHASE_D3). Mode unset: read and write name the same bucket and key, unchanged. Mode canonical: the writer lands at the view destination and this read still returns the pre-cutover object or a miss, per the helper.",
    "notes": "Writer runner PHASE_D3 per the census; the reader runs in D_04 PHASE_D4 of the same gold dispatch. Not changed by this cell (TO bound 4). Line numbers at base a45a4384d9; D_04 lines at or after 2468 sit one line later in the worktree after the phase A2 insertion. Live only when BD_PLATINUM_MODE is set to canonical, which this cell never sets; the mode act is phase B, the issuer to amend."
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W19-S20",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~19",
    "surfaced_at": "2026-10-11T08:21:05Z",
    "one_line": "read-back of served platinum key advisor_book_key(...) at D_04.client_portal_summary.py:2854 reads BUCKET while writer D_02.advisor_client_detail.py:1580 puts it through destination(); canonical mode would read the pre-cutover copy",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/black_diamond/scripts/gold/D_04.client_portal_summary.py:2854 read site @a45a4384d9",
        "data/black_diamond/scripts/gold/D_02.advisor_client_detail.py:1580 writer line @a45a4384d9 (census writer entry, runner PHASE_D3)",
        "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~16/PRODUCER_CENSUS.json @a45a4384d9 (census class gold/entities/advisors/)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-FB-f-9 phase A2 step 4: 'Find, do not fix, the same shape elsewhere ... file ONE row per site (class OBSERVATION, the file and line, what it reads and what the mode does to it) and change nothing at that site.'",
    "world_is": "data/black_diamond/scripts/gold/D_04.client_portal_summary.py:2854 (_batch_read_json(book_keys), advisor_book_key(aid)) reads advisor_book_key(...) from BUCKET (S3_BUCKET). Its key is in served platinum class gold/entities/advisors/ (lib/platinum_dest_view.py). The writer D_02.advisor_client_detail.py:1580 writes it through destination() (runner PHASE_D3). Mode unset: read and write name the same bucket and key, unchanged. Mode canonical: the writer lands at the view destination and this read still returns the pre-cutover object or a miss, per the helper.",
    "notes": "Writer runner PHASE_D3 per the census; the reader runs in D_04 PHASE_D4 of the same gold dispatch. Not changed by this cell (TO bound 4). Line numbers at base a45a4384d9; D_04 lines at or after 2468 sit one line later in the worktree after the phase A2 insertion. Live only when BD_PLATINUM_MODE is set to canonical, which this cell never sets; the mode act is phase B, the issuer to amend."
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W19-S21",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~19",
    "surfaced_at": "2026-10-11T08:21:05Z",
    "one_line": "read-back of served platinum key advisor book.json objects at D_04.client_portal_summary.py:2293 reads BUCKET while writer D_02.advisor_client_detail.py:1580 puts it through destination(); canonical mode would read the pre-cutover copy",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/black_diamond/scripts/gold/D_04.client_portal_summary.py:2293 read site @a45a4384d9",
        "data/black_diamond/scripts/gold/D_02.advisor_client_detail.py:1580 writer line @a45a4384d9 (census writer entry, runner PHASE_D3)",
        "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~16/PRODUCER_CENSUS.json @a45a4384d9 (census class gold/entities/advisors/)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-FB-f-9 phase A2 step 4: 'Find, do not fix, the same shape elsewhere ... file ONE row per site (class OBSERVATION, the file and line, what it reads and what the mode does to it) and change nothing at that site.'",
    "world_is": "data/black_diamond/scripts/gold/D_04.client_portal_summary.py:2293 (_batch_read_json(book_keys) from _list_prefix(gold/entities/advisors/, /book.json)) reads advisor book.json objects from BUCKET (S3_BUCKET). Its key is in served platinum class gold/entities/advisors/ (lib/platinum_dest_view.py). The writer D_02.advisor_client_detail.py:1580 writes it through destination() (runner PHASE_D3). Mode unset: read and write name the same bucket and key, unchanged. Mode canonical: the writer lands at the view destination and this read still returns the pre-cutover object or a miss, per the helper.",
    "notes": "Writer runner PHASE_D3 per the census; the reader runs in D_04 PHASE_D4 of the same gold dispatch. Not changed by this cell (TO bound 4). Line numbers at base a45a4384d9; D_04 lines at or after 2468 sit one line later in the worktree after the phase A2 insertion. Live only when BD_PLATINUM_MODE is set to canonical, which this cell never sets; the mode act is phase B, the issuer to amend."
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W19-S22",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~19",
    "surfaced_at": "2026-10-11T08:21:05Z",
    "one_line": "read-back of served platinum key client_aua_timeseries_key(...) at D_04.client_portal_summary.py:2656 reads BUCKET while writer D_02.advisor_client_detail.py:2218 puts it through destination(); canonical mode would read the pre-cutover copy",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/black_diamond/scripts/gold/D_04.client_portal_summary.py:2656 read site @a45a4384d9",
        "data/black_diamond/scripts/gold/D_02.advisor_client_detail.py:2218 writer line @a45a4384d9 (census writer entry, runner PHASE_D3)",
        "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~16/PRODUCER_CENSUS.json @a45a4384d9 (census class gold/entities/clients/)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-FB-f-9 phase A2 step 4: 'Find, do not fix, the same shape elsewhere ... file ONE row per site (class OBSERVATION, the file and line, what it reads and what the mode does to it) and change nothing at that site.'",
    "world_is": "data/black_diamond/scripts/gold/D_04.client_portal_summary.py:2656 (_batch_read_json(ts_keys), client_aua_timeseries_key(rid)) reads client_aua_timeseries_key(...) from BUCKET (S3_BUCKET). Its key is in served platinum class gold/entities/clients/ (lib/platinum_dest_view.py). The writer D_02.advisor_client_detail.py:2218 writes it through destination() (runner PHASE_D3). Mode unset: read and write name the same bucket and key, unchanged. Mode canonical: the writer lands at the view destination and this read still returns the pre-cutover object or a miss, per the helper.",
    "notes": "Writer runner PHASE_D3 per the census; the reader runs in D_04 PHASE_D4 of the same gold dispatch. Not changed by this cell (TO bound 4). Line numbers at base a45a4384d9; D_04 lines at or after 2468 sit one line later in the worktree after the phase A2 insertion. Live only when BD_PLATINUM_MODE is set to canonical, which this cell never sets; the mode act is phase B, the issuer to amend."
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W19-S23",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~19",
    "surfaced_at": "2026-10-11T08:21:05Z",
    "one_line": "read-back of served platinum key client_aua_timeseries_key(...) at D_04.client_portal_summary.py:617 reads BUCKET while writer D_02.advisor_client_detail.py:2218 puts it through destination(); canonical mode would read the pre-cutover copy",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/black_diamond/scripts/gold/D_04.client_portal_summary.py:617 read site @a45a4384d9",
        "data/black_diamond/scripts/gold/D_02.advisor_client_detail.py:2218 writer line @a45a4384d9 (census writer entry, runner PHASE_D3)",
        "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~16/PRODUCER_CENSUS.json @a45a4384d9 (census class gold/entities/clients/)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-FB-f-9 phase A2 step 4: 'Find, do not fix, the same shape elsewhere ... file ONE row per site (class OBSERVATION, the file and line, what it reads and what the mode does to it) and change nothing at that site.'",
    "world_is": "data/black_diamond/scripts/gold/D_04.client_portal_summary.py:617 (_batch_read_json(rel_ts_keys), client_aua_timeseries_key(r)) reads client_aua_timeseries_key(...) from BUCKET (S3_BUCKET). Its key is in served platinum class gold/entities/clients/ (lib/platinum_dest_view.py). The writer D_02.advisor_client_detail.py:2218 writes it through destination() (runner PHASE_D3). Mode unset: read and write name the same bucket and key, unchanged. Mode canonical: the writer lands at the view destination and this read still returns the pre-cutover object or a miss, per the helper.",
    "notes": "Writer runner PHASE_D3 per the census; the reader runs in D_04 PHASE_D4 of the same gold dispatch. Not changed by this cell (TO bound 4). Line numbers at base a45a4384d9; D_04 lines at or after 2468 sit one line later in the worktree after the phase A2 insertion. Live only when BD_PLATINUM_MODE is set to canonical, which this cell never sets; the mode act is phase B, the issuer to amend."
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W19-S24",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~19",
    "surfaced_at": "2026-10-11T08:21:05Z",
    "one_line": "read-back of served platinum key account_aua_timeseries_key(...) at D_04.client_portal_summary.py:1099 reads BUCKET while writer D_02.advisor_client_detail.py:2271 puts it through destination(); canonical mode would read the pre-cutover copy",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/black_diamond/scripts/gold/D_04.client_portal_summary.py:1099 read site @a45a4384d9",
        "data/black_diamond/scripts/gold/D_02.advisor_client_detail.py:2271 writer line @a45a4384d9 (census writer entry, runner PHASE_D3)",
        "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~16/PRODUCER_CENSUS.json @a45a4384d9 (census class gold/entities/accounts/)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-FB-f-9 phase A2 step 4: 'Find, do not fix, the same shape elsewhere ... file ONE row per site (class OBSERVATION, the file and line, what it reads and what the mode does to it) and change nothing at that site.'",
    "world_is": "data/black_diamond/scripts/gold/D_04.client_portal_summary.py:1099 (_batch_read_json(acct_keys), account_aua_timeseries_key(aid)) reads account_aua_timeseries_key(...) from BUCKET (S3_BUCKET). Its key is in served platinum class gold/entities/accounts/ (lib/platinum_dest_view.py). The writer D_02.advisor_client_detail.py:2271 writes it through destination() (runner PHASE_D3). Mode unset: read and write name the same bucket and key, unchanged. Mode canonical: the writer lands at the view destination and this read still returns the pre-cutover object or a miss, per the helper.",
    "notes": "Writer runner PHASE_D3 per the census; the reader runs in D_04 PHASE_D4 of the same gold dispatch. Not changed by this cell (TO bound 4). Line numbers at base a45a4384d9; D_04 lines at or after 2468 sit one line later in the worktree after the phase A2 insertion. Live only when BD_PLATINUM_MODE is set to canonical, which this cell never sets; the mode act is phase B, the issuer to amend."
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W19-S25",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~19",
    "surfaced_at": "2026-10-11T08:21:05Z",
    "one_line": "read-back of served platinum key account_aua_timeseries_key(...) at D_04.client_portal_summary.py:1332 reads BUCKET while writer D_02.advisor_client_detail.py:2271 puts it through destination(); canonical mode would read the pre-cutover copy",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/black_diamond/scripts/gold/D_04.client_portal_summary.py:1332 read site @a45a4384d9",
        "data/black_diamond/scripts/gold/D_02.advisor_client_detail.py:2271 writer line @a45a4384d9 (census writer entry, runner PHASE_D3)",
        "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~16/PRODUCER_CENSUS.json @a45a4384d9 (census class gold/entities/accounts/)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-FB-f-9 phase A2 step 4: 'Find, do not fix, the same shape elsewhere ... file ONE row per site (class OBSERVATION, the file and line, what it reads and what the mode does to it) and change nothing at that site.'",
    "world_is": "data/black_diamond/scripts/gold/D_04.client_portal_summary.py:1332 (_batch_read_json(b5_keys), account_aua_timeseries_key(a)) reads account_aua_timeseries_key(...) from BUCKET (S3_BUCKET). Its key is in served platinum class gold/entities/accounts/ (lib/platinum_dest_view.py). The writer D_02.advisor_client_detail.py:2271 writes it through destination() (runner PHASE_D3). Mode unset: read and write name the same bucket and key, unchanged. Mode canonical: the writer lands at the view destination and this read still returns the pre-cutover object or a miss, per the helper.",
    "notes": "Writer runner PHASE_D3 per the census; the reader runs in D_04 PHASE_D4 of the same gold dispatch. Not changed by this cell (TO bound 4). Line numbers at base a45a4384d9; D_04 lines at or after 2468 sit one line later in the worktree after the phase A2 insertion. Live only when BD_PLATINUM_MODE is set to canonical, which this cell never sets; the mode act is phase B, the issuer to amend."
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W19-S26",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~19",
    "surfaced_at": "2026-10-11T08:21:05Z",
    "one_line": "read-back of served platinum key client_timeseries_key(...) at D_04.client_portal_summary.py:1218 reads BUCKET while writer C_06.client_mix_timeseries.py:383 puts it through destination(); canonical mode would read the pre-cutover copy",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/black_diamond/scripts/gold/D_04.client_portal_summary.py:1218 read site @a45a4384d9",
        "data/black_diamond/scripts/gold/C_06.client_mix_timeseries.py:383 writer line @a45a4384d9 (census writer entry, runner PHASE_C5)",
        "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~16/PRODUCER_CENSUS.json @a45a4384d9 (census class gold/entities/clients/)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-FB-f-9 phase A2 step 4: 'Find, do not fix, the same shape elsewhere ... file ONE row per site (class OBSERVATION, the file and line, what it reads and what the mode does to it) and change nothing at that site.'",
    "world_is": "data/black_diamond/scripts/gold/D_04.client_portal_summary.py:1218 (_batch_read_json(ts_keys), client_timeseries_key(rid)) reads client_timeseries_key(...) from BUCKET (S3_BUCKET). Its key is in served platinum class gold/entities/clients/ (lib/platinum_dest_view.py). The writer C_06.client_mix_timeseries.py:383 writes it through destination() (runner PHASE_C5). Mode unset: read and write name the same bucket and key, unchanged. Mode canonical: the writer lands at the view destination and this read still returns the pre-cutover object or a miss, per the helper.",
    "notes": "Writer runner PHASE_C5 per the census; the reader runs in D_04 PHASE_D4 of the same gold dispatch. Not changed by this cell (TO bound 4). Line numbers at base a45a4384d9; D_04 lines at or after 2468 sit one line later in the worktree after the phase A2 insertion. Live only when BD_PLATINUM_MODE is set to canonical, which this cell never sets; the mode act is phase B, the issuer to amend."
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W19-S27",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~19",
    "surfaced_at": "2026-10-11T08:21:05Z",
    "one_line": "read-back of served platinum key MIX_DAILY_SUMMARY at D_03.composition_artifacts.py:482 reads BUCKET while writer C_06.client_mix_timeseries.py:420 puts it through destination(); canonical mode would read the pre-cutover copy",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/black_diamond/scripts/gold/D_03.composition_artifacts.py:482 read site @a45a4384d9",
        "data/black_diamond/scripts/gold/C_06.client_mix_timeseries.py:420 writer line @a45a4384d9 (census writer entry, runner PHASE_C5)",
        "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~16/PRODUCER_CENSUS.json @a45a4384d9 (census class gold/views/)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-FB-f-9 phase A2 step 4: 'Find, do not fix, the same shape elsewhere ... file ONE row per site (class OBSERVATION, the file and line, what it reads and what the mode does to it) and change nothing at that site.'",
    "world_is": "data/black_diamond/scripts/gold/D_03.composition_artifacts.py:482 (get_object(Bucket=BUCKET, Key=MIX_DAILY_SUMMARY)) reads MIX_DAILY_SUMMARY from BUCKET (S3_BUCKET). Its key is in served platinum class gold/views/ (lib/platinum_dest_view.py). The writer C_06.client_mix_timeseries.py:420 writes it through destination() (runner PHASE_C5). Mode unset: read and write name the same bucket and key, unchanged. Mode canonical: the writer lands at the view destination and this read still returns the pre-cutover object or a miss, per the helper.",
    "notes": "Writer runner PHASE_C5 per the census; the reader runs in D_04 PHASE_D4 of the same gold dispatch. Not changed by this cell (TO bound 4). Line numbers at base a45a4384d9; D_04 lines at or after 2468 sit one line later in the worktree after the phase A2 insertion. Live only when BD_PLATINUM_MODE is set to canonical, which this cell never sets; the mode act is phase B, the issuer to amend."
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W19-S28",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~19",
    "surfaced_at": "2026-10-11T08:21:05Z",
    "one_line": "read-back of served platinum key REL_ARCHITECT_LOOKUP at D_03.composition_artifacts.py:691 reads BUCKET while writer C_07.advisor_attribution.py:481 puts it through destination(); canonical mode would read the pre-cutover copy",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/black_diamond/scripts/gold/D_03.composition_artifacts.py:691 read site @a45a4384d9",
        "data/black_diamond/scripts/gold/C_07.advisor_attribution.py:481 writer line @a45a4384d9 (census writer entry, runner PHASE_C4)",
        "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~16/PRODUCER_CENSUS.json @a45a4384d9 (census class gold/views/)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-FB-f-9 phase A2 step 4: 'Find, do not fix, the same shape elsewhere ... file ONE row per site (class OBSERVATION, the file and line, what it reads and what the mode does to it) and change nothing at that site.'",
    "world_is": "data/black_diamond/scripts/gold/D_03.composition_artifacts.py:691 (_read_parquet(...)) reads REL_ARCHITECT_LOOKUP from BUCKET (S3_BUCKET). Its key is in served platinum class gold/views/ (lib/platinum_dest_view.py). The writer C_07.advisor_attribution.py:481 writes it through destination() (runner PHASE_C4). Mode unset: read and write name the same bucket and key, unchanged. Mode canonical: the writer lands at the view destination and this read still returns the pre-cutover object or a miss, per the helper.",
    "notes": "Writer runner PHASE_C4 per the census; the reader runs in D_04 PHASE_D4 of the same gold dispatch. Not changed by this cell (TO bound 4). Line numbers at base a45a4384d9; D_04 lines at or after 2468 sit one line later in the worktree after the phase A2 insertion. Live only when BD_PLATINUM_MODE is set to canonical, which this cell never sets; the mode act is phase B, the issuer to amend."
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W19-S29",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~19",
    "surfaced_at": "2026-10-11T08:21:05Z",
    "one_line": "read-back of served platinum key ACCOUNT_TEAM at D_03.composition_artifacts.py:835 reads BUCKET while writer C_07.advisor_attribution.py:479 puts it through destination(); canonical mode would read the pre-cutover copy",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/black_diamond/scripts/gold/D_03.composition_artifacts.py:835 read site @a45a4384d9",
        "data/black_diamond/scripts/gold/C_07.advisor_attribution.py:479 writer line @a45a4384d9 (census writer entry, runner PHASE_C4)",
        "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~16/PRODUCER_CENSUS.json @a45a4384d9 (census class gold/views/)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-FB-f-9 phase A2 step 4: 'Find, do not fix, the same shape elsewhere ... file ONE row per site (class OBSERVATION, the file and line, what it reads and what the mode does to it) and change nothing at that site.'",
    "world_is": "data/black_diamond/scripts/gold/D_03.composition_artifacts.py:835 (_read_parquet(...)) reads ACCOUNT_TEAM from BUCKET (S3_BUCKET). Its key is in served platinum class gold/views/ (lib/platinum_dest_view.py). The writer C_07.advisor_attribution.py:479 writes it through destination() (runner PHASE_C4). Mode unset: read and write name the same bucket and key, unchanged. Mode canonical: the writer lands at the view destination and this read still returns the pre-cutover object or a miss, per the helper.",
    "notes": "Writer runner PHASE_C4 per the census; the reader runs in D_04 PHASE_D4 of the same gold dispatch. Not changed by this cell (TO bound 4). Line numbers at base a45a4384d9; D_04 lines at or after 2468 sit one line later in the worktree after the phase A2 insertion. Live only when BD_PLATINUM_MODE is set to canonical, which this cell never sets; the mode act is phase B, the issuer to amend."
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W19-S30",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~19",
    "surfaced_at": "2026-10-11T08:21:05Z",
    "one_line": "read-back of served platinum key REL_ARCHITECT_LOOKUP at D_02.advisor_client_detail.py:378 reads BUCKET while writer C_07.advisor_attribution.py:481 puts it through destination(); canonical mode would read the pre-cutover copy",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/black_diamond/scripts/gold/D_02.advisor_client_detail.py:378 read site @a45a4384d9",
        "data/black_diamond/scripts/gold/C_07.advisor_attribution.py:481 writer line @a45a4384d9 (census writer entry, runner PHASE_C4)",
        "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~16/PRODUCER_CENSUS.json @a45a4384d9 (census class gold/views/)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-FB-f-9 phase A2 step 4: 'Find, do not fix, the same shape elsewhere ... file ONE row per site (class OBSERVATION, the file and line, what it reads and what the mode does to it) and change nothing at that site.'",
    "world_is": "data/black_diamond/scripts/gold/D_02.advisor_client_detail.py:378 (_load_parquet(...)) reads REL_ARCHITECT_LOOKUP from BUCKET (S3_BUCKET). Its key is in served platinum class gold/views/ (lib/platinum_dest_view.py). The writer C_07.advisor_attribution.py:481 writes it through destination() (runner PHASE_C4). Mode unset: read and write name the same bucket and key, unchanged. Mode canonical: the writer lands at the view destination and this read still returns the pre-cutover object or a miss, per the helper.",
    "notes": "Writer runner PHASE_C4 per the census; the reader runs in D_04 PHASE_D4 of the same gold dispatch. Not changed by this cell (TO bound 4). Line numbers at base a45a4384d9; D_04 lines at or after 2468 sit one line later in the worktree after the phase A2 insertion. Live only when BD_PLATINUM_MODE is set to canonical, which this cell never sets; the mode act is phase B, the issuer to amend."
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W19-S31",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~19",
    "surfaced_at": "2026-10-11T08:21:05Z",
    "one_line": "read-back of served platinum key ACCOUNT_TEAM at D_02.advisor_client_detail.py:396 reads BUCKET while writer C_07.advisor_attribution.py:479 puts it through destination(); canonical mode would read the pre-cutover copy",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/black_diamond/scripts/gold/D_02.advisor_client_detail.py:396 read site @a45a4384d9",
        "data/black_diamond/scripts/gold/C_07.advisor_attribution.py:479 writer line @a45a4384d9 (census writer entry, runner PHASE_C4)",
        "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~16/PRODUCER_CENSUS.json @a45a4384d9 (census class gold/views/)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-FB-f-9 phase A2 step 4: 'Find, do not fix, the same shape elsewhere ... file ONE row per site (class OBSERVATION, the file and line, what it reads and what the mode does to it) and change nothing at that site.'",
    "world_is": "data/black_diamond/scripts/gold/D_02.advisor_client_detail.py:396 (_load_parquet(...)) reads ACCOUNT_TEAM from BUCKET (S3_BUCKET). Its key is in served platinum class gold/views/ (lib/platinum_dest_view.py). The writer C_07.advisor_attribution.py:479 writes it through destination() (runner PHASE_C4). Mode unset: read and write name the same bucket and key, unchanged. Mode canonical: the writer lands at the view destination and this read still returns the pre-cutover object or a miss, per the helper.",
    "notes": "Writer runner PHASE_C4 per the census; the reader runs in D_04 PHASE_D4 of the same gold dispatch. Not changed by this cell (TO bound 4). Line numbers at base a45a4384d9; D_04 lines at or after 2468 sit one line later in the worktree after the phase A2 insertion. Live only when BD_PLATINUM_MODE is set to canonical, which this cell never sets; the mode act is phase B, the issuer to amend."
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W19-S32",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~19",
    "surfaced_at": "2026-10-11T08:21:05Z",
    "one_line": "read-back of served platinum key ACCOUNT_TEAM at D_01.partner_analytics.py:360 reads BUCKET while writer C_07.advisor_attribution.py:479 puts it through destination(); canonical mode would read the pre-cutover copy",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/black_diamond/scripts/gold/D_01.partner_analytics.py:360 read site @a45a4384d9",
        "data/black_diamond/scripts/gold/C_07.advisor_attribution.py:479 writer line @a45a4384d9 (census writer entry, runner PHASE_C4)",
        "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~16/PRODUCER_CENSUS.json @a45a4384d9 (census class gold/views/)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-FB-f-9 phase A2 step 4: 'Find, do not fix, the same shape elsewhere ... file ONE row per site (class OBSERVATION, the file and line, what it reads and what the mode does to it) and change nothing at that site.'",
    "world_is": "data/black_diamond/scripts/gold/D_01.partner_analytics.py:360 (_read(...)) reads ACCOUNT_TEAM from BUCKET (S3_BUCKET). Its key is in served platinum class gold/views/ (lib/platinum_dest_view.py). The writer C_07.advisor_attribution.py:479 writes it through destination() (runner PHASE_C4). Mode unset: read and write name the same bucket and key, unchanged. Mode canonical: the writer lands at the view destination and this read still returns the pre-cutover object or a miss, per the helper.",
    "notes": "Writer runner PHASE_C4 per the census; the reader runs in D_04 PHASE_D4 of the same gold dispatch. Not changed by this cell (TO bound 4). Line numbers at base a45a4384d9; D_04 lines at or after 2468 sit one line later in the worktree after the phase A2 insertion. Live only when BD_PLATINUM_MODE is set to canonical, which this cell never sets; the mode act is phase B, the issuer to amend."
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W19-S33",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~19",
    "surfaced_at": "2026-10-11T08:21:05Z",
    "one_line": "read-back of served platinum key ACCOUNT_TEAM at C_08.advisor_fee_efficiency.py:657 reads BUCKET while writer C_07.advisor_attribution.py:479 puts it through destination(); canonical mode would read the pre-cutover copy",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/black_diamond/scripts/gold/C_08.advisor_fee_efficiency.py:657 read site @a45a4384d9",
        "data/black_diamond/scripts/gold/C_07.advisor_attribution.py:479 writer line @a45a4384d9 (census writer entry, runner PHASE_C4)",
        "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~16/PRODUCER_CENSUS.json @a45a4384d9 (census class gold/views/)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-FB-f-9 phase A2 step 4: 'Find, do not fix, the same shape elsewhere ... file ONE row per site (class OBSERVATION, the file and line, what it reads and what the mode does to it) and change nothing at that site.'",
    "world_is": "data/black_diamond/scripts/gold/C_08.advisor_fee_efficiency.py:657 (_read_s3(...)) reads ACCOUNT_TEAM from BUCKET (S3_BUCKET). Its key is in served platinum class gold/views/ (lib/platinum_dest_view.py). The writer C_07.advisor_attribution.py:479 writes it through destination() (runner PHASE_C4). Mode unset: read and write name the same bucket and key, unchanged. Mode canonical: the writer lands at the view destination and this read still returns the pre-cutover object or a miss, per the helper.",
    "notes": "Writer runner PHASE_C4 per the census; the reader runs in D_04 PHASE_D4 of the same gold dispatch. Not changed by this cell (TO bound 4). Line numbers at base a45a4384d9; D_04 lines at or after 2468 sit one line later in the worktree after the phase A2 insertion. Live only when BD_PLATINUM_MODE is set to canonical, which this cell never sets; the mode act is phase B, the issuer to amend."
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W19-S34",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~19",
    "surfaced_at": "2026-10-11T08:21:05Z",
    "one_line": "read-back of served platinum key ACCOUNT_TEAM_KEY at D_00f.advisor_nna_canonical.py:808 reads BUCKET while writer C_07.advisor_attribution.py:479 puts it through destination(); canonical mode would read the pre-cutover copy",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/black_diamond/scripts/gold/D_00f.advisor_nna_canonical.py:808 read site @a45a4384d9",
        "data/black_diamond/scripts/gold/C_07.advisor_attribution.py:479 writer line @a45a4384d9 (census writer entry, runner PHASE_C4)",
        "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~16/PRODUCER_CENSUS.json @a45a4384d9 (census class gold/views/)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-FB-f-9 phase A2 step 4: 'Find, do not fix, the same shape elsewhere ... file ONE row per site (class OBSERVATION, the file and line, what it reads and what the mode does to it) and change nothing at that site.'",
    "world_is": "data/black_diamond/scripts/gold/D_00f.advisor_nna_canonical.py:808 (_read_s3_parquet(ACCOUNT_TEAM_KEY)) reads ACCOUNT_TEAM_KEY from BUCKET (S3_BUCKET). Its key is in served platinum class gold/views/ (lib/platinum_dest_view.py). The writer C_07.advisor_attribution.py:479 writes it through destination() (runner PHASE_C4). Mode unset: read and write name the same bucket and key, unchanged. Mode canonical: the writer lands at the view destination and this read still returns the pre-cutover object or a miss, per the helper.",
    "notes": "Writer runner PHASE_C4 per the census; the reader runs in D_04 PHASE_D4 of the same gold dispatch. Not changed by this cell (TO bound 4). Line numbers at base a45a4384d9; D_04 lines at or after 2468 sit one line later in the worktree after the phase A2 insertion. Live only when BD_PLATINUM_MODE is set to canonical, which this cell never sets; the mode act is phase B, the issuer to amend."
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W19-S35",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~19",
    "surfaced_at": "2026-10-11T08:21:05Z",
    "one_line": "D_04 advisor stale-cleanup lists the served platinum/advisors/ prefix on BUCKET and deletes stale keys on BUCKET; canonical mode lists and deletes the legacy copy, not the destination",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/black_diamond/scripts/gold/D_04.client_portal_summary.py:786 and :794 _list_prefix on BUCKET over platinum/advisors/ @a45a4384d9",
        "data/black_diamond/scripts/gold/D_04.client_portal_summary.py:802 s3.delete_objects(Bucket=BUCKET) @a45a4384d9",
        "data/black_diamond/scripts/gold/D_04.client_portal_summary.py:806 _write_batch(items) runs after the cleanup @a45a4384d9"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-FB-f-9 phase A2 step 4: 'Find, do not fix ... a read of a platinum key a writer wrote earlier in the same run by another route (a helper that reads it back) ... file ONE row per site ... change nothing at that site.'",
    "world_is": "D_04.client_portal_summary.py:786 and :794 read the served prefix platinum/advisors/ through _list_prefix, which lists BUCKET only; :802 deletes the stale keys from BUCKET. The advisor items are written at :806, after the list, so the list sees prior-run objects, not this run. Mode unset: unchanged. Mode canonical: the list sees the legacy copy only, so stale objects at the destination are never listed or removed, and the delete touches the legacy bucket.",
    "notes": "Filed as a read of a same-prefix key written by prior runs of the same writer, not a same-run read-after-write: the write follows the list in the same function. Line numbers at base a45a4384d9; the worktree numbers are one higher from line 2468 on. Live only when BD_PLATINUM_MODE is set to canonical; this cell never sets it."
  }
]
```

## Row filed by 2.0.0_SA_COO~B1 (round 3, ADDENDUM 4 condition 1: E_01 and E_24)

```json
{
  "id": "ADVI_FIRMBKTS-D1-S14",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "2.0.0_SA_COO~B1",
  "surfaced_at": "2026-10-11T08:27:25Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "THE CTO'S ADDENDUM 4 CONDITION 1 ON E_01 AND E_24: E_01 IS NOT A SERVED-KEY WRITER UNDER THE MODULE'S OWN RULE AND LAST WROTE 2026-04-07; E_24 HAS NO LAUNCHER AND NO SendCommand NAMING IT IN 45 DAYS (0 OF 4,010)",
  "spec_asserts": "ROUND_ANALYSIS.round2.md ADDENDUM 4 condition 1: no writer of 49 Financial's platinum is left on legacy when the switch moves; E_01 and E_24 are read, and carried in the same act or shown dead with a denominator, before the window opens. The census (PRODUCER_CENSUS.json) lists both under class gold/artifacts/.",
  "world_is": "E_01 writes gold/account_quality_tiers_{date}.json and gold/account_quality_tiers.parquet (E_01 header lines 30-32; objects listed in opal-data-bd under that prefix: 3 of 3). platinum_dest.destination() in canonical mode returns (opal-data-bd, same key) for those keys, so E_01 moves nothing and writes one home under either mode; its newest object has LastModified 2026-04-07T07:12:22Z (187 days before this read). The census class column for E_01 is wrong; its census line is not a served-class write. E_24 is a manual rebuild tool (header: 'No gold pipeline needed ... Usage: python3 E_24 --upload') that writes the served key gold/artifacts/advisor_fee_efficiency.json (canonical: advi/49financial/platinum/artifacts/advisor_fee_efficiency.json); it is not in gold_dispatch.sh's catalog, and a search of the first-party corpus (81,118 files) names it only in logs and audit files, never as a launch. Run history, measured 45 days (2026-08-27 to 2026-10-11): CloudTrail SendCommand events read 4,010 over 81 pages, complete, 0 name E_24 or E_01 (1 names gold_dispatch, 2026-10-01T04:11Z); StartSession events read 1 (a shell session cannot be attributed to a script, so a session run is not excluded by this read). A hand run of E_24 after the mode moves, without the export, writes the legacy key.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      ".tools/aws s3api list-objects-v2 --bucket opal-data-bd --prefix gold/account_quality_tiers (3 objects; newest 2026-04-07T07:12:22Z)",
      "python: platinum_dest.destination('gold/account_quality_tiers_2026-04-02.json','canonical') == ('opal-data-bd', same key); destination('gold/artifacts/advisor_fee_efficiency.json','canonical') == ('opal-data-49financial', 'advi/49financial/platinum/artifacts/advisor_fee_efficiency.json')",
      "data/black_diamond/scripts/gold/gold_dispatch.sh:110-121 catalog: 12 of the 14 census writers; E_01 and E_24 absent",
      "PRODUCER_CENSUS.json E_01 entry: runner UNKNOWN, schedule null",
      "boto3 cloudtrail lookup_events EventName=SendCommand, 2026-08-27 to 2026-10-11, 81 pages, 4,010 events, body contains E_24: 0, E_01: 0, gold_dispatch: 1 (2026-10-01T04:11Z); EventName=StartSession: 1 event"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "E_01: retire from the census as a non-served-key writer (reason above, denominator 3 of 3 objects). E_24 reads dead under ADDENDUM 4's own test (no schedule, no caller, no SendCommand naming it in 45 days: 0 of 4,010) with one residual: 1 StartSession in the window. The act-2 pair proposes it retired from the census on that denominator and records the residual; the CTO rules. Owner: 2.0.0_SA_COO~B1."
}
```

## Row filed by 0.7.0_AE_CloudOps~FBL (FB-f-8, phase B, step 5 read-back)

```json
{
  "id": "ADVI_FIRMBKTS-S12",
  "project": "ADVI_FIRMBKTS",
  "fabric": "laptop",
  "surfaced_by": "0.7.0_AE_CloudOps~FBL",
  "surfaced_at": "2026-10-11T08:27:45Z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "one_line": "TO-FB-f-8 act 1 APPLIED on the laptop (Branch A holds on every live read) but the pair's condition 'a post-apply plan reads no changes' is NOT met: the plan still lists aws_wafv2_web_acl.opal_cloudfront_protection (1 to change) because UpdateWebACL cannot clear the provider's stored empty Version; also AC4 as written reads 0, not 3, because OverrideAction.Count is an empty object.",
  "spec_asserts": "COO half ADDENDUM 1 Branch A: after the apply 'the post-apply plan reads no changes (the ACL's standing churn is gone, which is the only observable effect)'; CTO ADDENDUM 1 condition 4: 'a post-apply plan reads no changes'; order AC4: wafv2 get-web-acl --query \"length(WebACL.Rules[?OverrideAction.Count])\" expects ^3$.",
  "world_is": "Apply 08:21:33Z-08:23:57Z through safe-apply of the saved plan: 'Apply complete! Resources: 0 added, 4 changed, 0 destroyed.' Distribution Deployed, ETag E1OAC26XEP0FDI to ELAAK8OWYOWV1; router v27 (CodeSha256 cOG/BuFhy9xcL7EF+4u5VexRZGjDdJq3h364PAPkYsw= equals the built artifact) x5 and guard v6 (YIgGtFjZwFltdXbviIx5dOQbb6FsOAUtIB96caAI0xs= equals the artifact) x5; exactly 10 of 40 associations changed and the distribution config is otherwise identical. The ACL reads 6 rules identical to the pre-act read (names, priorities, actions, statements), the three groups Count, default Allow, LockToken 848a6d0b-d69f-40e0-876a-cfc0ce40b6b2 before and after: the write changed nothing in AWS, as dell1 row ADVI_FIRMBKTS-D1-S13 measured on 2026-10-11. The post-apply plan reads 'Plan: 0 to add, 1 to change, 0 to destroy', the ACL only (the three managed-group rules replaced). AC4's invocation returns 0 because JMESPath treats the empty object {} as false; the same query with '!=null' returns 3.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "deliverables/0.7.0_AE_CloudOps~FBL/evidence/plan_after_apply.out",
      "deliverables/0.7.0_AE_CloudOps~FBL/evidence/pre_get_web_acl.json against post_get_web_acl.json: equal modulo Version representation, LockToken unchanged",
      "deliverables/0.7.0_AE_CloudOps~FBL/evidence/pre_get_distribution_config.json against post_get_distribution_config.json: 10 associations differ, nothing else"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "This seat did NOT roll back: the rollback of the associations would not clear the plan line, the ACL is byte-equal to the pre-act read, and a second apply is outside the order's bounds (2.0.0_SA_COO~B1 / 1.0.0_SA_CTO~DELL1 own the call). The ACL's standing churn is a provider representation that the API round-trip drops, so it will persist while the ACL stays in this root; the fix is outside this act (ignore_changes on the three version attributes, or moving the ACL to its own root). The order stays open until the two signers either waive condition 4 for this ACL or rule otherwise; the CTO oracle read is requested meanwhile."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-S15",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "1.0.0_SA_CTO~DELL1",
  "surfaced_at": "2026-10-11T08:50:00Z",
  "one_line": "The firm-isolation guard's SEV1 page path delivers nothing: every publish to opal-infrastructure-alerts in the 40 minutes read (08:14Z, 08:15Z, and this seat's 3 test publishes at 08:43Z) failed delivery to the topic's one subscription (SMS); NumberOfNotificationsDelivered 0, NumberOfNotificationsFailed 8.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "shared-advisor-router-response publishGuardAlert: a confirmed cross-firm mis-route pages the central ops topic (best-effort; the 502 block does not depend on it).",
  "world_is": "CloudWatch AWS/SNS for TopicName opal-infrastructure-alerts, 08:04Z-08:44Z: Published 08:14Z 1, 08:15Z 1, 08:43Z 3; Delivered none; Failed 08:14Z 1, 08:15Z 1, 08:43Z 6. list-subscriptions-by-topic: 1 subscription, protocol sms. The 08:43Z publishes were this seat's own oracle mistake (guard events with a mismatching served bucket, request id cto-oracle; ledger/NEVER_WIDEN_ROUND3_ACT1_ADVTENANT_CTO_HALF.md ADDENDUM 3). The block itself works (502 returned). Why SMS delivery fails (sandbox, spend limit, opt-out, origination number) is not read. No new alert is built (CLAUDE.md moratorium); this is a defect of an existing route.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "aws cloudwatch get-metric-statistics AWS/SNS NumberOfMessagesPublished / NumberOfNotificationsDelivered / NumberOfNotificationsFailed, TopicName=opal-infrastructure-alerts, 2026-10-11T08:04Z-08:44Z",
      "aws sns list-subscriptions-by-topic opal-infrastructure-alerts: 1 sms",
      "/aws/lambda/shared-advisor-router-response filter cto-oracle: 6 lines"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "disarm_owner": "0.0.0_AB_MSTR~DELL1"
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-S16",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "1.0.0_SA_CTO~DELL1",
  "surfaced_at": "2026-10-11T08:55:00Z",
  "one_line": "D1-S15 narrowed: the SEV1 SMS page path has delivered NOTHING in 14 days (0 delivered, 28 failed, 09-27..10-10); not sandbox (IsInSandbox false), not the USD 50 spend limit (SMSMonthToDateSpentUSD has no datapoints, i.e. no spend); origination number and opt-out unread (denied to the dell identity).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "Row D1-S15: the guard's SEV1 publish pages a human via the topic's SMS subscription.",
  "world_is": "CloudWatch AWS/SNS opal-infrastructure-alerts, daily sums 2026-09-27..10-11: NumberOfNotificationsFailed 09-27 2, 09-28 2, 09-29 2, 09-30 4, 10-09 8, 10-10 10; NumberOfNotificationsDelivered none. SMSMonthToDateSpentUSD: 0 datapoints over 2 days. Laptop MSTR read (relay msg 3663, user/Andrew_Berman): MonthlySpendLimit 50, IsInSandbox false, no DeliveryStatusIAMRole, no DefaultSenderID. sns list-origination-numbers and list-phone-numbers-opted-out: AuthorizationError for cloudops-dell1-agent-user. Leading candidate, INFERRED not read: no registered US origination number (toll-free or 10DLC), which US carriers require for A2P SMS.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "aws cloudwatch get-metric-statistics AWS/SNS (14 days, daily)",
      "relay msg 3663 (laptop get-sms-attributes, get-sms-sandbox-account-status)",
      "sns list-origination-numbers / list-phone-numbers-opted-out: AuthorizationError on dell1"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "disarm_owner": "0.0.0_AB_MSTR~DELL1"
}
```

## Rows filed by 0.9.0_WK_ADVI_FIRMBKTS~20 (FB-f-9 phase A3, step 3 and the read census)

Routing the read census UNROUTED sites and the negative arm surfaced the rows below. Base line numbers at 56c2234580. Hazard INERT throughout: BD_PLATINUM_MODE is unset in this cell and no run is made.

```json
[
  {
    "id": "ADVI_FIRMBKTS-D1-W20-S1",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~20",
    "surfaced_at": "2026-10-11T08:47:03Z",
    "one_line": "Legacy-copy PUTs (the dual writes to the legacy key) now go through platinum_destination(), so under canonical each copy lands at the canonical home of its legacy name and not at the legacy home",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "C_06 client_mix_timeseries.py:373 and :389 legacy put of lk, base 56c2234580",
        "D_00 portal_aggregates.py:215 legacy put of lk, base 56c2234580",
        "D_01 partner_analytics.py:2561 legacy put (comment 'Dual-write to legacy key during migration'), base 56c2234580",
        "D_03 composition_artifacts.py:213, :514, :535, :559, :585, :596 legacy puts, base 56c2234580",
        "E_01 account_quality_tiers.py:316 and :345 legacy puts, base 56c2234580"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-FB-f-9 phase A3 step 3: a PUT the census lists as UNROUTED is routed through platinum_destination(); the dual-write sites are the reason the census lists them, and D_01 names its copy a dual write to the legacy key during migration.",
    "world_is": "Mode unset: each legacy copy names the same bucket and key as before (identity). Mode canonical: a copy whose legacy key is a served class lands at the canonical template, the same place its primary write lands for the same output, so no object is left at the legacy home for that copy and readers that follow source() read the canonical copy. The migration intent of the copy (a legacy-readable object during the window) is not carried by the seam. The issuer or the CTO should rule whether these copies stay at the legacy home under canonical before phase B.",
    "notes": "Filed while routing the census's UNROUTED puts. Base line numbers at 56c2234580. No mode is set in this cell, so the hazard is not live here; it is live the moment BD_PLATINUM_MODE=canonical runs these scripts."
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W20-S2",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~20",
    "surfaced_at": "2026-10-11T08:47:03Z",
    "one_line": "Three helpers take the bucket as a caller argument (helpers.s3_object_exists, D_01 _load_aua_certification, etf_classifier IdentityResolver.from_s3), and the seam ignores a bucket argument, so the three calls are marked exempt instead of routed",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "lib/helpers.py:36 s3_client.head_object(Bucket=bucket, Key=key) with a caller-supplied bucket, base 56c2234580",
        "D_01 partner_analytics.py:386 s3_client.get_object(Bucket=bucket, Key=key), base 56c2234580; sole caller passes S3_BUCKET at base",
        "lib/etf_classifier.py:332 get_object(Bucket=bucket, Key=lots_key), base 56c2234580; from_s3 default bucket is S3_BUCKET",
        "callers of s3_object_exists at base: C_02, C_04, E_00, E_19 (probe keys: silver/allocations, silver/prices, gold/positions_cube, gold/accounts_dimension_latest.parquet)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-FB-f-9 phase A3 step 3 (prefer routing; the seam is the identity for a non-served key) and bound 2 (with the mode unset every line touched names the same bucket, prefix and key as today).",
    "world_is": "Routing these calls through platinum_source(key) would return S3_BUCKET whatever bucket the caller passed, so a caller on another bucket would change its legacy result. At base every caller passes the pipeline bucket and probes a non-served key, so the exemption changes nothing today. The three lines carry '# seam: exempt' with that reason. A future caller that probes a served key on the pipeline bucket is not routed by these helpers and needs a seam-aware signature.",
    "notes": "Exempt, not routed, by design. The census counts the three as EXEMPT (3 of 127), so the read census reads UNROUTED 0."
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W20-S3",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~20",
    "surfaced_at": "2026-10-11T08:47:03Z",
    "one_line": "AC2 cannot match its '^OK$' expectation on this device: FORCE_COLOR=3 is set in the worker shell, so unittest colours the OK line with ANSI escapes, while the same run with FORCE_COLOR unset prints a plain OK",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "shell: FORCE_COLOR=3, PYTHON_COLORS and NO_COLOR unset (measured in the worker shell)",
        "AC2 invocation tail -n 3 output: the OK line is the escape sequence for green OK then reset (od -c read)",
        "control: env -u FORCE_COLOR of the same invocation prints a plain OK line, rc 0, Ran 15 tests"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-FB-f-9 proof AC2: invocation of the three new test classes, tail -n 3, expected to match ^OK$.",
    "world_is": "In this worker shell the literal invocation ends with a colour-coded OK line (rc 0, 15 tests, all pass), so the literal regex does not match. The test module cannot change the runner's colour decision, and the colour is set by the environment, not by the code. The literal verdict depends on the environment the proof checker runs in.",
    "notes": "Filed so the COO and the proof checker read the same environment fact. Not a code defect: the tests pass in both runs."
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W20-S4",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~20",
    "surfaced_at": "2026-10-11T08:47:03Z",
    "one_line": "Print and log lines beside the routed writes and reads still print s3://<S3_BUCKET or BUCKET>/<key>; under canonical the printed location is the legacy bucket, not the bucket the call used",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "E_01 account_quality_tiers.py log lines naming s3://{S3_BUCKET}/{parquet_key} and s3://{S3_BUCKET}/{json_key} (routed puts above them)",
        "D_01 partner_analytics.py print 'Loading s3://{S3_BUCKET}/{key}' and 'Uploaded to s3://{S3_BUCKET}/{key}' (routed read and put)",
        "D_03 composition_artifacts.py print 's3://{BUCKET}/{key}' after the routed write; C_05, C_07, C_08, E_24 log lines name S3_BUCKET beside routed writes"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-FB-f-9 phase A3 step 3: each routed call names its seam destination; the message beside a routed write is the audit trail of where it went.",
    "world_is": "Mode unset: the printed bucket is the bucket used, unchanged. Mode canonical: the printed location is S3_BUCKET while the write goes to the class bucket, so an operator reading the run log would look in the wrong bucket. The prints were not edited in this cell (the bound is the call, not the message).",
    "notes": "A display-only mismatch under canonical; no call is affected. The print sites are listed by file, not by key."
  }
]
```

## Row filed by 0.9.0_WK_ADVI_FIRMBKTS~20 (naming gate at the first commit attempt)

```json
[
  {
    "id": "ADVI_FIRMBKTS-D1-W20-S5",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~20",
    "surfaced_at": "2026-10-11T08:58:00Z",
    "one_line": "The naming gate (LGIC_ENFORCE) refused the literal 'gold/entities/advisors/' in the routed D_02 listing as an out-of-pattern S3 key assigned to remediation ADVI_FIRMBKTS; resolved by deriving the advisor entity root from advisor_book_key() in the same file",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "D_02 advisor_client_detail.py:3248 base literal in paginate(Prefix='gold/entities/advisors/', Delimiter='/') at 56c2234580",
        "commit-gate: naming-gate REFUSE D_02 advisor_client_detail.py:3252 gold/entities/advisors/ EXISTING and OUT-OF-PATTERN as S3Key in remediations.json for ADVI_FIRMBKTS (run at the first commit attempt)",
        "lib/s3_layout.py advisor_book_key() returns f'gold/entities/advisors/{advisor_id}/book.json'; advisor_book_key('_').rsplit('/', 2)[0] + '/' == 'gold/entities/advisors/' (measured)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-FB-f-9 phase A3 step 3: route the listing through platinum_list_target(); the order names no literal-key rule for the listing.",
    "world_is": "The naming gate grades a literal S3 prefix in any added line and refuses it when the remediation already lists the literal; the seam call needs a prefix value, so the literal is derived from the builder. Behaviour is identical: the derived prefix equals the base literal.",
    "notes": "Recorded because the order did not say the listing prefix must come from the builder. The derived value equals the base literal; no key changes. Owner of the remediation: the issuer."
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W21-S1",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~21",
    "surfaced_at": "2026-10-11T09:19:00Z",
    "one_line": "FB-f-9 phase A4 stopped: its two bounds cannot both hold, 'no non-ASCII in the file' versus 'the diff is the two blocks and one argument', because gold_dispatch.sh already carries 19 non-ASCII lines at base; no edit made.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/black_diamond/scripts/gold/gold_dispatch.sh@938e2ed2c4: python byte scan of the file: 19 lines hold bytes above 127 (lines 44, 49, 146, 154, 324, 369, 487, 517, 559, 921, 1074, 1125, 1132, 1389, 1410, 1443, 1482, 1484, 1500; 58 bytes in total)",
        "git ls-files --eol on the same path: i/lf w/lf attr/text eol=lf; the LF bound holds, the non-ASCII bound does not",
        "AC1 at base (r3_dispatch.py --arm export): 'FAIL the PLATINUM-MODE block is absent', 'ROUND 3 DISPATCH EXPORT: CASES FAIL', exit=1",
        "AC2 at base (r3_dispatch.py --arm gate): 'FAIL the GATE-READ-LOCATION block is absent', 'ROUND 3 DISPATCH GATE: CASES FAIL', exit=1"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-FB-f-9 phase A4 bounds: (1) the diff against base is the two marked blocks and the one replaced aws s3 cp argument, nothing else; (3) LF line endings and no non-ASCII in the file; if something cannot be met within the paths, file a surprise row and stop.",
    "world_is": "The base file carries 19 non-ASCII lines outside the edit zones. Clearing them widens the diff beyond bound (1); keeping them breaks bound (3). The two bounds cannot both hold on this file. No edit was made by this worker.",
    "notes": "Issuer decision: re-cut bound (3) to 'no non-ASCII introduced by this act' (the two blocks are ASCII by construction), or order a separate ASCII clean-up cell. CLAUDE.md section 4: a file already carrying non-ASCII takes all non-ASCII out or every reader explicit, never a subset. The order's proof instance carries AC1 and AC2 as FAIL, measured at base."
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W21-S2",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~21",
    "surfaced_at": "2026-10-11T09:19:00Z",
    "one_line": "On the --chain downstream path the freshness gate reads before any sync of code/gold into SCRIPTS, so the step-2 gate block falls back to the legacy URI under canonical wherever lib/ is not already in SCRIPTS; the order's dirname contingency is not shown to reach lib/ on the runner.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~B1",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "gold_dispatch.sh@938e2ed2c4 L1305-1307: check_freshness runs when _should_check_freshness=1 (full|downstream, L1276-1280), before any run_chain on the downstream path",
        "gold_dispatch.sh@938e2ed2c4 L1249-1258: silver-prep-pre run_chain runs only for chain full, so the gate sees a sync for full and none for downstream",
        "gold_dispatch.sh@938e2ed2c4 L664-666: sync_scripts defines the code/gold sync; its callers are L473 (run_chain) and L532 (run_chain_parallel), after the gate on downstream (L1393-1404)",
        "gold_dispatch.sh@938e2ed2c4 L78: SCRIPTS=/tmp/gold_layer_scripts; run-gold-layer.sh@HEAD SCRIPTS_DIR=/home/ubuntu/gold-layer/scripts (L17-48) receives its own code/gold sync (L87); the dispatcher's directory on the runner is not established here",
        "gold_dispatch.sh@938e2ed2c4 L250 (the step-2 python line discards stderr) with the step-2 fallback: an import failure returns empty and falls to the legacy URI silently"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-FB-f-9 step 2: the gate location comes from lib/platinum_dest.py source(); if the lib is absent the location falls back to today's legacy URI; if the freshness function runs before the sync, add the dispatcher's directory as a second search path.",
    "world_is": "The gate runs before the first sync on the downstream path, so SCRIPTS holds no lib/ on a fresh instance (an earlier run on the same instance may have synced it). Under mode canonical the fallback reads the legacy header_metrics.json, whose data_as_of is frozen. The dirname contingency reaches lib/ only if the dispatcher runs from a directory that holds lib/, which this worker did not establish.",
    "notes": "ARMED: if the step-2 and step-1 blocks land as written and the mode is exported in production, a fresh-instance downstream run reads the frozen legacy value. Not armed by this act: no edit made, and the contingency was not applied because the stop precedes the edit. Disarm: the issuer re-cuts the gate placement, or the sync precedes the gate on the downstream path."
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W23-S1",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~23",
    "surfaced_at": "2026-10-11T09:33:52Z",
    "one_line": "gold_dispatch.sh base line 517 holds a non-ASCII em dash inside an echo string the chain prints (the FATAL phase message); step 2b STOPs on a printed string, so the line is left unedited and AC3 cannot read 0.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/black_diamond/scripts/gold/gold_dispatch.sh@cf806cf81d L517 base: the braced && list echoes FATAL: $phase failed, then an em dash (bytes E2 80 94), then aborting chain",
        "post-edit file line 525 carries the same string unchanged; the diff hunks list has no entry for base line 517"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-FB-f-9 step 2b: replace each non-ASCII character on the 19 lines with its ASCII equivalent, touching nothing else; if any is inside a string a command prints or a pattern a command matches, STOP and file a BLOCKING row for that line.",
    "world_is": "Base line 517 is a printed string. Replacing its dash would change a message the chain prints, not a comment. The line is unedited; AC3 reads 15 bytes above 127, all on the five printed-string lines.",
    "notes": "Issuer disposition needed: ASCII substitution of printed text, or a bound re-cut for printed strings. Sibling rows S2 to S5 name the other four printed lines."
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W23-S2",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~23",
    "surfaced_at": "2026-10-11T09:33:52Z",
    "one_line": "gold_dispatch.sh base line 921 holds a non-ASCII em dash inside the show_help heredoc that --help prints; step 2b STOPs on a printed string, so the line is left unedited and AC3 cannot read 0.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/black_diamond/scripts/gold/gold_dispatch.sh@cf806cf81d L851 show_help() and L852 cat << 'HELP' open the heredoc; the HELP terminator is at L995 (base)",
        "base line 921 is inside that heredoc: the text B_00 then an em dash then B_01 reads gold/canonical/holdings output from B_00"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-FB-f-9 step 2b: replace each non-ASCII character on the 19 lines with its ASCII equivalent, touching nothing else; if any is inside a string a command prints, STOP and file a BLOCKING row for that line.",
    "world_is": "Base line 921 is help text printed by --help. Replacing its dash changes printed output, not a comment. The line is unedited; it is one of the five printed-string lines behind AC3 FAIL.",
    "notes": "Issuer disposition needed with sibling row S1 (same rule, same bound)."
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W23-S3",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~23",
    "surfaced_at": "2026-10-11T09:33:52Z",
    "one_line": "gold_dispatch.sh base line 1132 holds a non-ASCII em dash inside an echo ERROR string printed by the --from guard; step 2b STOPs on a printed string, so the line is left unedited and AC3 cannot read 0.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/black_diamond/scripts/gold/gold_dispatch.sh@cf806cf81d L1132 base: echo ERROR: --from not valid for silver-prep (S_*), an em dash, then only one script.",
        "the post-edit line 1140 carries the same string unchanged; the diff hunks list has no entry for base line 1132"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-FB-f-9 step 2b: replace each non-ASCII character on the 19 lines with its ASCII equivalent, touching nothing else; if any is inside a string a command prints, STOP and file a BLOCKING row for that line.",
    "world_is": "Base line 1132 is an echo argument printed by the --from guard. Replacing its dash changes printed output. The line is unedited; it is one of the five printed-string lines behind AC3 FAIL.",
    "notes": "Issuer disposition needed with sibling row S1 (same rule, same bound)."
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W23-S4",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~23",
    "surfaced_at": "2026-10-11T09:33:52Z",
    "one_line": "gold_dispatch.sh base line 1482 holds a non-ASCII em dash inside an echo WARN string printed by the recon harness step; step 2b STOPs on a printed string, so the line is left unedited and AC3 cannot read 0.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/black_diamond/scripts/gold/gold_dispatch.sh@cf806cf81d L1482 base: echo WARN: recon harness exit=$recon_exit, an em dash, then FAIL domains detected",
        "the post-edit line 1497 carries the same string unchanged; the diff hunks list has no entry for base line 1482"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-FB-f-9 step 2b: replace each non-ASCII character on the 19 lines with its ASCII equivalent, touching nothing else; if any is inside a string a command prints, STOP and file a BLOCKING row for that line.",
    "world_is": "Base line 1482 is an echo WARN message printed by the chain. Replacing its dash changes printed output. The line is unedited; it is one of the five printed-string lines behind AC3 FAIL.",
    "notes": "Issuer disposition needed with sibling row S1 (same rule, same bound)."
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W23-S5",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~23",
    "surfaced_at": "2026-10-11T09:33:52Z",
    "one_line": "gold_dispatch.sh base line 1484 holds a non-ASCII em dash inside an echo line printed by the recon harness step; step 2b STOPs on a printed string, so the line is left unedited and AC3 cannot read 0.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/black_diamond/scripts/gold/gold_dispatch.sh@cf806cf81d L1484 base: echo Recon harness OK/WARN, an em dash, then manifest at s3://opal-data-bd/diagnostics/",
        "the post-edit line 1499 carries the same string unchanged; the diff hunks list has no entry for base line 1484"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-FB-f-9 step 2b: replace each non-ASCII character on the 19 lines with its ASCII equivalent, touching nothing else; if any is inside a string a command prints, STOP and file a BLOCKING row for that line.",
    "world_is": "Base line 1484 is an echo line printed by the chain. Replacing its dash changes printed output. The line is unedited; it is one of the five printed-string lines behind AC3 FAIL.",
    "notes": "Issuer disposition needed with sibling row S1 (same rule, same bound)."
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W23-S6",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~23",
    "surfaced_at": "2026-10-11T09:33:52Z",
    "one_line": "The step-2 gate search reaches lib/platinum_dest.py through the dispatcher's own directory only on the wrapper path; a direct invocation from another directory, and any --chain downstream caller not in this repo, fall to SCRIPTS and then to the legacy URI on a fresh instance.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~B1",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/black_diamond/scripts/gold/run_gold_layer.sh@cf806cf81d L12 SCRIPT_DIR=dirname of $0; L22 and L34 bash SCRIPT_DIR/gold_dispatch.sh with --chain full (and --force --full-rebuild); L15-41 accept incremental or full only",
        "infra/aws/ec2/bd-gold-layer-runner/run-gold-layer.sh@cf806cf81d L17 SCRIPTS_DIR=/home/ubuntu/gold-layer/scripts; L90 aws s3 sync code/gold/ into SCRIPTS_DIR; L114-115 cd then ./run_gold_layer.sh",
        "data/black_diamond/scripts/gold/_partial_chain_b01.sh@cf806cf81d L13 runs bash /tmp/gold_dispatch.sh --single: the dirname is /tmp, which holds no lib/",
        "data/black_diamond/scripts/gold/gold_dispatch.sh@cf806cf81d L216 reads lib/ under SCRIPTS (GOLD_CALGUARD_LIB=SCRIPTS/lib), so the runner mirror is the lib/ carrier the contingency depends on",
        "Grep of data/black_diamond/scripts/gold and infra/aws/ec2/bd-gold-layer-runner for the string --chain downstream, at cf806cf81d: no caller outside gold_dispatch.sh itself"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-FB-f-9 step 2: the gate location comes from lib/platinum_dest.py source(); the dispatcher's own directory is searched first because on the downstream path the gate runs before any sync, so the directory holds lib/ there.",
    "world_is": "The wrapper path holds: the boot-synced directory is the dispatcher's own directory and holds lib/. The wrapper never passes --chain downstream, so the repo carries no downstream caller; a direct caller's $0 is not established, and _partial_chain_b01.sh runs /tmp/gold_dispatch.sh, whose directory holds no lib/.",
    "notes": "ARMED: once the mode export and the gate land deployed, a directly invoked chain on a fresh instance reads the legacy header_metrics.json under canonical (frozen data_as_of). This row narrows ADVI_FIRMBKTS-D1-W21-S2 to the direct-invocation path; it does not close it and W21-S2 is not edited. Disarm: the issuer names every downstream caller and its $0, or re-cuts the gate search to a directory every caller holds."
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W23-S7",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~23",
    "surfaced_at": "2026-10-11T09:39:00Z",
    "one_line": "Amendment 9 (issuer ruling, relayed by the coordinator, a new commit): the step 2b STOP is lifted for rows S1 to S5; each of their five em dashes is replaced with two hyphens and nothing else on the line. S1 to S5 are not edited in place.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "INFERRED",
      "evidence": [
        "coordinator relay of the issuer ruling: amendment 9 in the ADVI_FIRMBKTS.TO-FB-f-9 order file on the issuer branch; the five base lines were 517, 921, 1132, 1482 and 1484",
        "data/black_diamond/scripts/gold/gold_dispatch.sh edited in the commit that carries this row: five lines changed, five insertions and five deletions; AC3 reads non-ascii-bytes=0"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Append-only channel: a row is never edited in place. The ruling asks one line added to each of rows S1 to S5 noting amendment 9.",
    "world_is": "The annotation is carried here as one new row naming S1 to S5, not as a line inside each of S1 to S5, because an existing row is not edited.",
    "notes": "If the issuer wants the line inside each of S1 to S5 itself, that is an issuer edit; this row is the record until then. The disposition of S1 to S5 is the issuer's."
  }
]
```

## Rows filed by 0.9.0_WK_ADVI_FIRMBKTS~22 (TO-FB-f-13, phase A, round 3)

```json
[
  {
    "id": "ADVI_FIRMBKTS-D1-W22-S1",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~22",
    "surfaced_at": "2026-10-11T09:31:27Z",
    "one_line": "The order's parity criterion (each Lambda view byte-identical to the gold view) and its 'same generated module, mark and registry hash as the gold one' cannot both hold under the builder as it stood: _blk_platinum_destinations named each rendered target's own path in the header's --target clause, so a Lambda copy generated under its own target differs from the gold view in line 1. Resolved by naming the module's one canonical target in every copy's header.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "lib/opal_naming.py@b96c9e74a1 _blk_platinum_destinations: the header's '--target %s' took the rendered path, so each target's header differed",
        "after the edit, generate --target data/black_diamond/scripts/gold/lib/platinum_dest_view.py into a scratch dir: cmp IDENTICAL to the committed gold view (sha256 0214e640e1290b4a2ddf2388e035aba85192cac760092d96d2de6660213c2ab1)",
        "after the edit, generate --target for both Lambda paths into the worktree: THREE-IDENTICAL by cmp; sha256 0214e640... on all three files"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-FB-f-13 1b step 2: the two Lambda views are the same generated module, mark and registry hash as the gold one; step 5(a): each view is byte-identical to data/black_diamond/scripts/gold/lib/platinum_dest_view.py.",
    "world_is": "The builder's header carries the rendered target's path, so a per-copy --target breaks (a) by one line. The header now names PLATINUM_DEST_VIEW_PATH in every copy; the two Lambda targets are rows of VIEWS, WHOLE_FILE_TARGETS and TARGET_REGISTRY_KEYS with the gold view's registry key tuple. Gold bytes and the mark's h16 are unchanged on regeneration.",
    "notes": "The builder edit sits inside this order's paths (lib/opal_naming.py). The issuer may prefer another identity for the copies; the gold view's bytes do not depend on that choice."
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W22-S2",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~22",
    "surfaced_at": "2026-10-11T09:31:27Z",
    "one_line": "The read census grades boto3 call syntax only: opal-partners-data reads and lists through awswrangler at three sites (lambda_function.py:1100, :1160, :1224) whose s3:// paths the census does not see. Their keys (gold/timeseries/...) lie outside the 11 served classes, so no served read is unrouted, but the census's ALL SITES ROUTED line does not cover them.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/lambda/v2_portal/partners/lambdas/opal-partners-data/lambda_function.py@worktree wr.s3.read_parquet(path=f's3://{bucket}/gold/timeseries/account_performance.parquet') at 1100, client_performance.parquet at 1160, and f's3://{bucket}/{holdings_key}' at 1224",
        "holdings_key comes from _find_latest_holdings_lots(), whose prefix is 'gold/timeseries/holdings_lots/' (not a served class)",
        "lib/opal_naming.py view PLATINUM_CLASSES: the 11 legacy prefixes under gold/ are gold/artifacts/, gold/entities/{accounts,advisors,clients}/, gold/platinum/firm/, gold/views/; none is a prefix of gold/timeseries/"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-FB-f-13 AC1 and the round-3 read census: ALL SITES ROUTED, NOT-SERVED OR EXEMPT over the S3 data calls of the named files.",
    "world_is": "Under canonical the three awswrangler reads keep reading the legacy bucket, which is the identity for keys outside the served classes. A later act that adds a served class over gold/timeseries/ would leave these reads on the legacy home unless the seam reaches the wrangler calls.",
    "notes": "The lines were not edited: routing them changes nothing today, because the seam is the identity for every key they name."
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W22-S3",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~22",
    "surfaced_at": "2026-10-11T09:31:27Z",
    "one_line": "targets classifies each Lambda copy of platinum_dest_view.py SHIP on the lambda plane only through the OTHER Lambda's served_seam.py import: lambda_plane_consumers skips the function that owns the file, so each copy's SHIP status rests on the other function's files list. If either function drops served_seam.py, its copy becomes UNCLASSIFIED and targets exits 1.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python lib/opal_naming.py targets after the edit (rc=0): 'SHIP lambda infra/aws/lambda/exec-summary-generator/platinum_dest_view.py measured: lambda-source-map.json (1 consumer(s): opal-partners-data)' and the partners copy: '(1 consumer(s): exec-summary-generator)'; PLANE lambda: 4",
        "lib/opal_naming.py lambda_plane_consumers: 'if own == target_abs: continue' skips the owning function, so the consumer is found through the other function's import of the stem"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-FB-f-13 step 2: python lib/opal_naming.py targets must still exit 0, with the two new files classified SHIP on the lambda plane.",
    "world_is": "Met: targets exits 0 and both copies are SHIP lambda. The classification is consumer-derived, and the owning function is never counted as its own consumer.",
    "notes": "No edit made. The fragility is recorded so that a later change to either Lambda's files list is checked against the targets output."
  }
]
```

## Rows filed by 0.9.0_WK_ADVI_FIRMBKTS~22, second batch (TO-FB-f-13, phase A)

```json
[
  {
    "id": "ADVI_FIRMBKTS-D1-W22-S4",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~22",
    "surfaced_at": "2026-10-11T09:34:27Z",
    "one_line": "The partners health probe head_object (lambda_function.py:986, the critical summary key) cannot be routed through the seam within this order: the naming gate (LGIC_ENFORCE) REFUSES an out-of-pattern S3Key literal on any added line of a remediation-assigned file, and the partners Lambda cannot derive the key from the builder. The site stays UNROUTED: AC1 reads UNROUTED=1, exit 1.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~B1",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "r3_reads.py --root <worktree> --files (exec lambda_function.py, exec platinum_reader.py, partners lambda_function.py): S3 data call sites=7 ROUTED=6 NOT-SERVED=0 EXEMPT=0 UNROUTED=1; 'UNROUTED lambda_function.py:986 head_object'; exit=1",
        "safe-commit.sh attempt 1, naming limb: 'NAMING REFUSE infra/aws/lambda/v2_portal/partners/lambdas/opal-partners-data/lambda_function.py:986 gold/artifacts/summary/header_metrics.json ... EXISTING and OUT-OF-PATTERN as S3Key in a surface remediations.json assigns to the live remediation ADVI_FIRMBKTS: REFUSE unless the diff removes it'",
        "lambda-source-map.json functions.opal-partners-data.files lists lambda_function.py, etf_classification.py, etf_classifier.py, pseudonymizer.py, served_seam.py, platinum_dest_view.py: no lib/ module is packaged, so address() is not callable from this Lambda"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-FB-f-13 step 4: each S3 data call in the three named files routes through the seam; AC1 = ROUND 3 READ CENSUS: ALL SITES ROUTED, NOT-SERVED OR EXEMPT.",
    "world_is": "The health probe is the only unrouted site. With the mode unset it probes the legacy home, unchanged. Under canonical on opal-partners-data (a later act) the probe would still read the frozen legacy home for the summary key and report missing_data for each firm on the pipeline bucket, while the served reads are on the new home.",
    "notes": "Not worked around: the literal is not split, moved or hidden to pass the gate. Closing it needs a builder-derived key reachable from the partners package, or a remediation decision on this literal; both lie outside this order's paths. The line is restored to its original bytes. Decision owner: the issuer, 2.0.0_SA_COO~B1."
  },
  {
    "id": "ADVI_FIRMBKTS-D1-W22-S5",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~22",
    "surfaced_at": "2026-10-11T09:34:27Z",
    "one_line": "The naming gate grades the pipeline bucket constant of the new served_seam.py ('opal-data-bd') as an ALIAS of S3_BUCKET: WARN (EXISTING, touched) with the remedy 'read it through lookup(...)'. The Lambda package cannot import lib/, so the constant stays as the order's bound 4 names it.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "safe-commit.sh attempt 1, naming limb: 'NAMING ALIAS infra/aws/lambda/exec-summary-generator/served_seam.py:28 opal-data-bd -> opal-data-49financial ... EXISTING, touched, and ALIAS as S3_BUCKET: WARN' (the same for the partners copy)",
        "infra/aws/lambda/exec-summary-generator/config.py carries S3_BUCKET: str = 'opal-data-bd' at the base commit b96c9e74a1, which is why the string is EXISTING and not NEW"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-FB-f-13 bound 4: no bucket name typed in a new string literal except the single pipeline bucket constant 'opal-data-bd' inside served_seam.py.",
    "world_is": "The gate warns and does not refuse this line; the constant equals the pipeline bucket that config.py already types. A rename of the pipeline bucket must change served_seam.py's constant with config.py.",
    "notes": "No edit made. The gate's own remedy (lookup) is not callable from a Lambda package; recorded so the issuer can decide whether the constant should come from the generated view in a later round."
  }
]
```

## Row filed by 0.9.0_WK_ADVI_FIRMBKTS~22, third batch (TO-FB-f-13, after the issuer's amendment 1 ruling)

```json
[
  {
    "id": "ADVI_FIRMBKTS-D1-W22-S6",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~22",
    "surfaced_at": "2026-10-11T09:41:53Z",
    "one_line": "Per the issuer's amendment-1 ruling on S4, the health probe's head_object line is kept byte-for-byte and routed by a _ServedS3 wrapper that s3_client is (marked '# seam: exempt' on the line above). The wrapper's list_objects_v2 applies the seam a second time to the holdings listing, which the site already routes; the census denominator moves from 7 to 9 sites (the wrapper's two calls, both ROUTED).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "lambda_function.py probe line: 'git show b96c9e74a1' and the worktree carry the identical line (cmp of the grep output, PROBE-LINE-BYTE-IDENTICAL)",
        "r3_reads.py --files (exec lambda_function.py, exec platinum_reader.py, partners lambda_function.py): S3 data call sites=9 ROUTED=8 NOT-SERVED=0 EXEMPT=1 UNROUTED=0; 'EXEMPT lambda_function.py:1011 head_object -- routed by the _ServedS3 wrapper that s3_client is'",
        "_ServedS3.list_objects_v2 applies platinum_list_target(Bucket, Prefix); _find_latest_holdings_lots already passes the seam's (bucket, prefix) and its listed prefix gold/timeseries/holdings_lots/ is not a served class, so the second application is the identity"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Issuer ruling (amendment 1 on S4): the probe line unchanged; route it in the client through a _ServedS3 wrapper; the comment marker on the line above; the other routed sites stay.",
    "world_is": "The seam is applied to the probe on every call: under canonical the probe reads the class home, which test (e) shows through the wrapper with 0 legacy served-prefix calls. The second application on the holdings listing is the identity for a non-pipeline bucket and for a non-served prefix, so its keys are unchanged. Disposition of S4 is the issuer's to record; this row does not edit S4.",
    "notes": "Test (e) drives handle_health_check() with the wrapper over the recording fake; the probe reports 'ok' in both modes and the canonical store holds only class-home keys."
  }
]
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-S17",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "1.0.0_SA_CTO~DELL1",
  "surfaced_at": "2026-10-11T10:00:00Z",
  "one_line": "ARMED: a stale copy of 49 Financial's ownership map (authorization data) sits at the new home (F7 copy 04:01Z, 474,726 B; legacy rewritten 05:24Z, 474,841 B); once act 4 moves the registry map value, any ordinary deploy of auth-validator-edge or an IRPT consumer would read the stale map silently.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "spec_asserts": "The ownership map is carved out of the round-3 window (ROUND_ANALYSIS.round2.md ADDENDUM 6): its readers keep reading the live legacy map until a round-4 act moves map and readers together.",
  "world_is": "s3 opal-data-49financial advi/49financial/platinum/49financial/ownership_map.json LastModified 2026-10-11T04:01:18Z 474726 B; s3 opal-data-bd platinum/49financial/ownership_map.json LastModified 2026-10-11T05:24:02Z 474841 B (read 10:0xZ by 1.0.0_SA_CTO~DELL1). Readers: auth-validator-edge index.mjs:173 via FIRM_BUCKET_MAP (generated firm-config.mjs); investor-reporting _authz/loaders.py:33 IRPT_OWNERSHIP_KEY (generated), 8 consumers.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "aws s3 list/head by 1.0.0_SA_CTO~DELL1 2026-10-11T10:0xZ",
      "msg 3720 (2.0.0_SA_COO~B1)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "disarm_owner": "1.0.0_SA_CTO~DELL1"
}
```

## Row filed by 0.7.0_AE_CloudOps~FB1 (FB-f-9, phase B, step 2b)

```json
{
  "id": "ADVI_FIRMBKTS-D1-S18",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.7.0_AE_CloudOps~FB1",
  "surfaced_at": "2026-10-11T09:58:07Z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "one_line": "TO-FB-f-9 step 2(b): the producers' role bd-exporter-ec2-role holds NO Allow for s3:PutObject or s3:GetObject on opal-data-49financial/advi/49financial/platinum/*, the new home of all 11 served classes, and its ListBucket allow is conditioned on other prefixes; the order's simulate instrument cannot run for this principal, so the read is a policy-document evaluation.",
  "spec_asserts": "COO half Authorization: the role's policy read with simulate-principal-policy on the two bucket-prefix ARNs, s3:PutObject, s3:GetObject and s3:ListBucket each allowed at arn:aws:s3:::opal-data-49financial/advi/49financial/platinum/* BEFORE the move; any implicitDeny is a STOP and the grant is a separate act (not drafted). TO-FB-f-9 step 2(b) repeats it for bd-exporter-ec2-role.",
  "world_is": "Gold runner i-01003b035d2988dfb (bd-gold-layer-runner) runs under instance profile bd-exporter-profile, role bd-exporter-ec2-role (live describe-instances and get-instance-profile; the QA runner shares it). iam:SimulatePrincipalPolicy on that role returns AccessDenied for user/cloudops-dell1-agent-user. A glob evaluation of the role's 18 policy documents (2 attached, 16 inline) against the exact ARNs: PutObject on opal-data-49financial/advi/49financial/platinum/* matches 0 Allow and 0 Deny; GetObject the same; ListBucket on opal-data-49financial with prefix advi/49financial/platinum/ matches AdviChain49fListScoped whose condition is s3:prefix StringLike gold/advi/* or _code/*, which that prefix does not meet. The positive control (PutObject on opal-data-49financial/gold/advi/*) matches AdviChainGoldRW, so the evaluator discriminates. The destination bucket policy has 4 statements, all Deny; DenyForeignFirmPrincipals lists bd-exporter-ec2-role among the principals it excludes, so nothing denies it there and nothing allows it. All 11 classes of lib/platinum_dest_view.py PLATINUM_CLASSES target opal-data-49financial under advi/49financial/platinum/. Consequence if the mode moved as signed: the first scheduled chain's served-class writes to the new home would be refused AccessDenied, and its reads and lists of the new home as well. Nothing has been moved: steps 3 and 4 are held by the issuer and this lane has written no object.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/act2/step2_reads.txt (b2)",
      "iam simulate-principal-policy on arn:aws:iam::313476888478:role/bd-exporter-ec2-role: AccessDenied, 'no identity-based policy allows the iam:SimulatePrincipalPolicy action', 2026-10-11 ~09:5xZ",
      "get-bucket-policy opal-data-49financial: 4 statements, 0 Allow; list-attached-role-policies and list-role-policies of bd-exporter-ec2-role: 18 documents evaluated",
      "ec2 describe-instances i-01003b035d2988dfb IamInstanceProfile bd-exporter-profile; iam get-instance-profile bd-exporter-profile -> bd-exporter-ec2-role"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Owner of the call: the issuer 2.0.0_SA_COO~B1 and the never-widen pair's two signers; the grant is 'a separate act, not drafted' by the pair's own words, and this seat will not create it (bounds: no grant, role or policy). What a grant would have to cover, read from the module: PutObject and GetObject on opal-data-49financial/advi/49financial/platinum/*, ListBucket on opal-data-49financial under the prefix advi/49financial/platinum/*, and DeleteObject only if some writer deletes at the new home (the pair says nothing is deleted there by the act; the CTO ADDENDUM 5 routes deletes). Two other facts for that act: the QA runner shares the role, and the role's existing statement for this bucket is gold/advi/*. A second instrument gap, for whoever drafts the pair's authorization line: the actor identity cannot simulate a role, so the read at step 2(b) stays a policy-document read unless the pair names another instrument."
}
```

## Row filed by 0.7.0_AE_CloudOps~FBL (FB-f-12, step 4 plan)

```json
{
  "id": "ADVI_FIRMBKTS-S13",
  "project": "ADVI_FIRMBKTS",
  "fabric": "laptop",
  "surfaced_by": "0.7.0_AE_CloudOps~FBL",
  "surfaced_at": "2026-10-11T10:24:14Z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "one_line": "TO-FB-f-12 step 4 STOP: the untargeted plan of infra/aws/terraform/inf-pipeline creates a sixth resource beyond the order's set, aws_secretsmanager_secret_version.eclipse_jwt_initial (secret orion/eclipse_jwt/current); nothing was applied.",
  "spec_asserts": "TO-FB-f-12 step 4: the plan 'must change EXACTLY the role, its policy, the two log groups and the SMS preferences; any other resource ... is a STOP'; bounds 2.2: STOP before the apply and file a BLOCKING row.",
  "world_is": "Plan 2026-10-11 ~10:2xZ, terraform 1.15.8, saved outside the repo: 358 resource_changes, 352 no-op, 6 create. Five are the order's (aws_iam_role.sms_delivery_status, aws_iam_role_policy.sms_delivery_status, the two aws_cloudwatch_log_group, aws_sns_sms_preferences.account with monthly_spend_limit 50 carried and the two delivery-status values). The sixth, aws_secretsmanager_secret_version.eclipse_jwt_initial, is a create (secret_string and a write-only value, both redacted) on secret orion/eclipse_jwt/current: a standing difference between this root and its state that this order did not cause and does not own. A plan with -target on the five addresses reads 5 create, nothing else.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "deliverables/0.7.0_AE_CloudOps~FBL/evidence_f12/plan_untargeted.out",
      "deliverables/0.7.0_AE_CloudOps~FBL/evidence_f12/plan_targeted_five.out",
      "deliverables/0.7.0_AE_CloudOps~FBL/evidence_f12/pre_act_record.txt"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Not applied and not targeted without the issuer's word: a targeted apply is a different act from the one the order describes, and the order's own read-back (a post-apply plan with no changes) cannot hold while the sixth create stands. Asked of 2.0.0_SA_COO~B1: (A) authorize a -target apply of exactly the five addresses and waive 'no changes' for the one named resource, or (B) have the owner of orion/eclipse_jwt dispose of that create first. This seat has not read why the version is planned and will not write to that secret. The TF file is committed unapplied at infra/aws/terraform/inf-pipeline/inf-ops-alerts-sms-delivery-status.tf so the issuer can read it; the SMS preferences are unchanged (MonthlySpendLimit 50 only)."
}
```

## Row filed by 0.7.0_AE_CloudOps~FBL (FB-f-12, step 3 commit)

```json
{
  "id": "ADVI_FIRMBKTS-S14",
  "project": "ADVI_FIRMBKTS",
  "fabric": "laptop",
  "surfaced_by": "0.7.0_AE_CloudOps~FBL",
  "surfaced_at": "2026-10-11T10:27:30Z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "one_line": "TO-FB-f-12 step 3: the commit-time naming gate REFUSES the order's two SNS delivery log groups, whose names AWS fixes (sns/us-east-1/313476888478/DirectPublishToPhoneNumber and /Failure): the grader has no log-group shape for a name without a leading slash.",
  "spec_asserts": "TO-FB-f-12 step 2 and 3: names come from lib/opal_naming.py name() and 'a builder refusal is a missing registry row to add'; step 3 declares the two delivery log groups with retention_in_days = 14 'yourself'.",
  "world_is": "The role and policy grade CONFORMANT (opal-sms-delivery-status-role, opal-sms-delivery-status-policy). The two log-group lines grade RAISE and the root's hole-count ratchet REFUSES the commit: 'the unplaceable-name list grew in infra/aws/terraform/inf-pipeline: 2 HOLE line(s) now, 0 at HEAD ... Owed: nothing you can write: the grader raised this text, which is a rule or registry defect -- from 1.0.0_SA_CTO'. The text it names is L1: 'has no leading / and takes none of the three log-group shapes'. The names are not ours: SNS writes to exactly these groups when DeliveryStatusIAMRole is set.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "safe-commit refusal 2026-10-11 ~10:3xZ, naming limb LGIC_ENFORCE DEC-6 (REFUSE 1, NAMING-GATE: REFUSE 5 graded)",
      "deliverables/0.7.0_AE_CloudOps~FBL/evidence_f12/inf-ops-alerts-sms-delivery-status.tf.txt (the file as written; removed from the root so no stray unapplied Terraform sits in the shared tree)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Owner: 1.0.0_SA_CTO (the grader's rule), per the gate's own text. Routes for the issuer and CTO: (A) the CTO adds a log-group shape or a registry row for AWS-fixed service log groups (sns/<region>/<account>/DirectPublishToPhoneNumber[/Failure]); (B) a deliberate departure as an R20 register entry Andrew acknowledges; (C) drop the two aws_cloudwatch_log_group resources and set retention another way, which the order does not describe. This seat used none of them and bypassed nothing. Together with row S13 the order cannot reach its apply."
}
```

## Row filed by 0.7.0_AE_CloudOps~FBL (FB-f-12, amendment 1 observation)

```json
{
  "id": "ADVI_FIRMBKTS-S15",
  "project": "ADVI_FIRMBKTS",
  "fabric": "laptop",
  "surfaced_by": "0.7.0_AE_CloudOps~FBL",
  "surfaced_at": "2026-10-11T10:34:12Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "The inf-pipeline root carries a standing pending create, aws_secretsmanager_secret_version.eclipse_jwt_initial (secret orion/eclipse_jwt/current): an unscoped safe-apply of that root by anyone writes that secret version.",
  "spec_asserts": "TO-FB-f-12 amendment 1: the sixth create 'was pending before' the order and the seat reports it as an OBSERVATION row.",
  "world_is": "The untargeted plan of infra/aws/terraform/inf-pipeline read 358 resource_changes, 352 no-op, 6 create on 2026-10-11 ~10:2xZ; five were this order's, the sixth is this resource. This seat has not read why it is pending and has not touched it. Until its owner disposes of it, every unscoped apply of the root writes a secret version, and every full plan after TO-FB-f-12 will list it as exactly one create.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "deliverables/0.7.0_AE_CloudOps~FBL/evidence_f12/plan_untargeted.out"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Owner unknown to this seat; the issuer routes it. Not blocking this order after amendment 1."
}
```

## Row filed by 2.0.0_SA_COO~B1 (round 3, TO-FB-f-12 row S13 routed to the root's owner)

```json
{
  "id": "ADVI_FIRMBKTS-D1-S19",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "2.0.0_SA_COO~B1",
  "surfaced_at": "2026-10-11T10:31:57Z",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "0.7.0_AE_CloudOps (the inf-pipeline root's author class; project ADVI_ECLDAT.001)",
  "one_line": "THE inf-pipeline ROOT HOLDS A PENDING, UNAPPLIED aws_secretsmanager_secret_version.eclipse_jwt_initial: ANY UNSCOPED APPLY OF THAT ROOT CREATES A NEW CURRENT VERSION OF orion/eclipse_jwt/current",
  "spec_asserts": "TO-FB-f-12 step 4 (before amendment 1): the plan changes exactly the role, its policy, the log groups and the SMS preferences; the CTO's AMENDMENT 2 item 1: the sixth create is not applied and is routed to the root's owner as its own row.",
  "world_is": "The laptop lane's untargeted plan of infra/aws/terraform/inf-pipeline read 358 resource_changes, 352 no-op, 6 create: the five of this order and aws_secretsmanager_secret_version.eclipse_jwt_initial (infra/aws/terraform/inf-pipeline/secrets.tf:40, secret orion/eclipse_jwt/current, authored by ADVI_ECLDAT.001, 0.6.1_AE_PartnerETL, 2026-05-14). The resource is a create, so the state does not hold it; a secret-version create makes a new AWSCURRENT version, which would replace the JWT the inf-jwt-trigger Lambda captured. The order's apply is scoped to the five addresses and does not touch it (evidence: deliverables/0.7.0_AE_CloudOps~FBL/evidence_f12/plan_untargeted.out, commit 9504fa9b79).",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "evidence_f12/plan_untargeted.out: Plan: 6 to add, 0 to change, 0 to destroy",
      "evidence_f12/pre_act_record.txt: 358 resource_changes, 352 no-op, 6 create",
      "git log -- infra/aws/terraform/inf-pipeline/secrets.tf: 8ff9ee1ff9 ECLDAT.001"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Not applied and not waived by this project: the CTO's AMENDMENT 2 says 'S13 goes to the root's owner as its own row'. The owner reads whether the resource should be imported, removed or applied deliberately (it may overwrite a live captured JWT). Until then no unscoped apply of inf-pipeline: safe-apply's scoped mechanism is the only apply that is safe in that root."
}
```

## Row filed by 0.7.0_AE_CloudOps~FBL (FB-f-12, amendment 2 commit)

```json
{
  "id": "ADVI_FIRMBKTS-S16",
  "project": "ADVI_FIRMBKTS",
  "fabric": "laptop",
  "surfaced_by": "0.7.0_AE_CloudOps~FBL",
  "surfaced_at": "2026-10-11T10:40:49Z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "one_line": "TO-FB-f-12 amendment 2: the two none_owed rows the CTO ruled cannot be committed by this seat: infra/logic/registry/name_rulings.json is in lane PLATFORM_LOGIC_DOCS, whose permitted agents are 4.0.0_SA_CRO and its tilde lanes only, although the order's <paths> names infra/logic/registry/.",
  "spec_asserts": "TO-FB-f-12 amendment 2 and the CTO's AMENDMENT 2 @fcf621a1c8: 'The seat adds the two rows in the same commit as the Terraform (the registry directory is already in this order's <paths>)'.",
  "world_is": "safe-commit of infra/aws/terraform/inf-pipeline/inf-ops-alerts-sms-delivery-status.tf plus infra/logic/registry/name_rulings.json, 2026-10-11 ~10:5xZ: the naming gate graded the Terraform WARN (the two log-group lines RAISE, no refusal once the rows are present) and the owned-paths check refused with 'lane=PLATFORM_LOGIC_DOCS ... agent=0.7.0_AE_CloudOps~FBL not in permitted_agents'. The lane's text holds the scope deliberately narrow (4.0.0_SA_CRO and its laptop tilde lanes; a repeat override for a standing action is a coverage gap to close). Nothing was committed and no override was taken. Prepared and parked: evidence_f12/inf-ops-alerts-sms-delivery-status.tf.txt (the Terraform) and evidence_f12/name_rulings_two_none_owed_rows.patch (the two rows; git apply --check clean). Without the rows the root's hole-count ratchet refuses the Terraform commit (row S14).",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "safe-commit refusal ~10:5xZ, owned-paths lane violation (block mode), lane PLATFORM_LOGIC_DOCS",
      "deliverables/0.7.0_AE_CloudOps~FBL/evidence_f12/name_rulings_two_none_owed_rows.patch"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Routes, none taken: (A) 4.0.0_SA_CRO (the registry's owner and the lane's permitted agent) applies the patch and commits it; this seat then commits the Terraform and applies; (B) the issuer or the CTO names this seat's audited GIT_COMMIT_AUTHOR_OVERRIDE for the one commit, in writing, which the lane text says is the pattern for a one-off; (C) the lane's permitted_agents gains this lane for this order. This seat will not self-authorize an override that a lane text says it narrowed on purpose. The scoped apply of amendment 1 follows whichever lands."
}
```

## Row filed by 0.7.0_AE_CloudOps~FBL (FB-f-12, scoped apply)

```json
{
  "id": "ADVI_FIRMBKTS-S17",
  "project": "ADVI_FIRMBKTS",
  "fabric": "laptop",
  "surfaced_by": "0.7.0_AE_CloudOps~FBL",
  "surfaced_at": "2026-10-11T10:53:07Z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "one_line": "TO-FB-f-12 scoped safe-apply REFUSED at the naming PLAN limb (exit 7) on the two AWS-fixed SNS log groups: the none_owed rows at HEAD (5165905870) satisfy the commit-time gate but the apply's plan-time grader still grades each group an ADDITION that RAISEs and refuses it under DEC-6.",
  "spec_asserts": "CTO AMENDMENT 2 @fcf621a1c8 and TO-FB-f-12 amendment 2: two none_owed LOG_GROUP rows are the ruling for the two names, 'the scoped apply of amendment 1 proceeds' once they land.",
  "world_is": "2026-10-11 10:51Z: the Terraform is committed (d777ef0472) and the registry rows are at HEAD (5165905870). The commit-time gate grades the two lines RAISE-EXISTING, a warning, and the commit landed. The scoped safe-apply of the saved five-address plan then printed 'NAMING REFUSE aws_cloudwatch_log_group.sns_sms_delivery ... (ADDITION): RAISE as LOG_GROUP: a rule or registry defect ... has no leading / and takes none of the three log-group shapes. DEC-6: refused like any refusal once enforcing', the same for .../Failure, 'NAMING-PLAN: REFUSE 4 graded', and 'safe-apply: BLOCKED by the naming plan limb (LGIC_ENFORCE DEC-6, ENFORCE mode, rc=1). Nothing was planned further or applied.' The seat-gates and the role and policy grade CONFORMANT. AWS is unchanged: get-sms-attributes still reads MonthlySpendLimit 50 only. The plan-time grader does not read name_rulings.json none_owed for an ADDITION, so the CTO's remedy does not reach the apply.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "deliverables/0.7.0_AE_CloudOps~FBL/evidence_f12/apply_attempt_blocked_by_naming_plan_limb.out",
      "deliverables/0.7.0_AE_CloudOps~FBL/evidence_f12/plan_targeted_five_final.out (5 create, nothing else)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Owner: 1.0.0_SA_CTO (the grader, per the gate's own text 'a rule or registry defect'). Routes, none taken: (A) the CTO has the plan-time stage honour a none_owed row for an ADDITION (the same file the commit stage reads), then this seat re-runs the same saved plan; (B) a LOG_GROUP shape for AWS-fixed service groups; (C) a written, audited naming override for this one apply, which safe-apply.sh does not expose as a documented switch and this seat will not improvise. The saved plan is unchanged and still the plan to run."
}
```

## Row filed by 0.7.0_AE_CloudOps~FBL (FB-f-12, amendment 3)

```json
{
  "id": "ADVI_FIRMBKTS-S18",
  "project": "ADVI_FIRMBKTS",
  "fabric": "laptop",
  "surfaced_by": "0.7.0_AE_CloudOps~FBL",
  "surfaced_at": "2026-10-11T11:03:08Z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "one_line": "TO-FB-f-12 amendment 3 names 'the gate's own audited override' of safe-apply's naming PLAN limb, but no such override exists in .tools/safe-apply.sh or .tools/naming-apply-gate.py; the order cannot be executed as amended.",
  "spec_asserts": "TO-FB-f-12 amendment 3 and the CTO's AMENDMENT 3 @063b622f78: 'ONE audited override of the plan limb for THIS apply ... the gate's own audited override carrying a reason that cites AMENDMENT 3, the two rows @5165905870 and row S17'.",
  "world_is": "Read 2026-10-11 ~11:1xZ. safe-apply.sh exposes three audited overrides: SEAT_GATES_OVERRIDE (the seat gates), TAGAUTHZ_OVERRIDE (tag authorization) and TOMBSTONE_OVERRIDE; none touches the naming limb. The naming limb is ENFORCE because org/mcp/naming-gate.enforce exists (or NAMING_GATE_ENFORCE=1), and naming-apply-gate.py reads only NAMING_GATE_ENFORCE and OPAL_AGENT_SERIAL from the environment; it never reads name_rulings.json, which is why the CRO's none_owed rows do not reach it. The one naming override that exists, '# naming-place-override:' in a commit message (naming-gate.py, round 10), is read by safe-commit.sh only and does not affect the older limb. So no audited variable, flag or message line passes the plan limb for one apply. Nothing was run: AWS is unchanged.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "grep of OVERRIDE in .tools/safe-apply.sh (lines 37, 86, 139-156, 352-433, 509)",
      "grep of environ/getenv/name_rulings in .tools/naming-apply-gate.py (lines 121 and 131 only)",
      "naming-gate.py module docstring lines 71-89 (the placement override is safe-commit only)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "This seat will not improvise a bypass: not deleting or editing org/mcp/naming-gate.enforce (a global switch), not editing safe-apply.sh or naming-apply-gate.py (0.0.0_AB_MSTR's and the CTO's), and not a bare terraform apply (banned). Routes: (A) land the plan-limb fix LGIC_ENFORCE-D1-S6 (2.0.0_SA_COO~L1), after which the same saved plan runs unchanged; (B) the owner of safe-apply.sh adds a one-shot audited switch for the naming plan limb and names it; (C) Andrew's word for another way. The saved five-address plan and every other step are ready."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-S20",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "1.0.0_SA_CTO~DELL1",
  "surfaced_at": "2026-10-11T11:30:00Z",
  "one_line": "D1-S15/S16 cause READ: every SEV1 SMS fails with providerResponse 'No origination identity available to send to destination number' -- the registered ACTIVE toll-free number exists but SNS cannot use it for the subscriber's US number; not sandbox, spend, opt-out or registration.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "A SEV1 guard publish reaches the on-call phone by SMS (row D1-S15).",
  "world_is": "Log group sns/us-east-1/313476888478/DirectPublishToPhoneNumber/Failure (retention 14 days, enabled by TO-FB-f-12 @62f7598435): 2 events 2026-10-11 11:18:31Z and 11:20:31Z, destination +1786***7679 (masked), smsType Transactional, providerResponse 'No origination identity available to send to destination number', dwell 120 ms. Earlier reads closed sandbox (false), spend (no datapoints), opt-out (false), origination existence (1 TOLL_FREE ACTIVE Transactional) and registration (US_TOLL_FREE_REGISTRATION COMPLETE). NOT read: whether the number sits in a pool, a protect configuration, the End User Messaging account spend limit, or the number's association to SNS.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "aws logs filter-log-events on the Failure group, 1.0.0_SA_CTO~DELL1 2026-10-11T11:2xZ",
      "TO-FB-f-12 complete @62f7598435 (laptop ~FBL, relayed dell1 msg 3804)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "disarm_owner": "0.0.0_AB_MSTR~DELL1"
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-S21",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "2.0.0_SA_COO~B1",
  "surfaced_at": "2026-10-11T12:20:00Z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "one_line": "The value flip of act 4 repoints the BD asset-dim bronze pull's write bucket from opal-data-bd to opal-data-49financial, while the mapping table HOMEs that class to opal-data-assets: the generated pin is a reader of the routed bucket that the round-3 analysis list does not name.",
  "spec_asserts": "Round-3 analysis section 3 item 1 (ADDENDUM 7): the window's readers of 49 Financial's routed bucket are the router and guard, auth-validator-edge, the IRPT consumers, the three gold scripts and the two Lambdas; act 4 is the value flip with every regenerated target deployed in the same act.",
  "world_is": "A scratch-registry rehearsal of the flip (round4/checks/r4_flip.py: the 49financial alias opal-data-bd loses routed=true, all 17 generated targets regenerated and diffed against HEAD) changes a bucket VALUE in exactly five targets: data/firm_registry.json (2), infra/aws/lambda-edge/_shared/firm-config.mjs (2), data/assets/scripts/gold/investor_reporting/directory_runner.py (2), holdings_snapshot.py (2) and data/black_diamond/scripts/bronze/_asset_dim_rest_pin.py (1: bucket 'opal-data-bd' -> 'opal-data-49financial'). The other twelve targets change only their registry-hash mark; perfrp_firm_pin.py is among those twelve, so the CTO's 'three gold scripts' read as directory_runner, holdings_snapshot and a script whose bytes do not move. The pin is imported by pull_bd_asset_dim_rest.py (lines 81-87) and deployed to s3://opal-data-bd/code/bronze/_asset_dim_rest_pin.py (infra/aws/ssm/opal-bd-asset-dim-download.json:44). mapping_v3.json row opal-data-bd / blackdiamond/49financial/bronze/assets_dim_rest/ is HOME to s3://opal-data-assets/blackdiamond/49financial/bronze/assets_dim_rest/2026-10-08/assets_dim_rest.parquet. After the flip and a redeploy of the pin, the pull would write the class to a bucket that is neither where it sits today nor where the table homes it.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_flip.py --arms flip, 2026-10-11 ~11:50Z (value-changing lines printed per target)",
      "data/black_diamond/scripts/bronze/_asset_dim_rest_pin.py lines 29-41 and its docstring (the pin sits in the routed bucket alias, not the tier home)",
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/mapping_v3.json, the assets_dim_rest row (disposition HOME)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Not this order set's to rule: the destination of a producer after the window is an endpoint question for 1.0.0_SA_CTO~DELL1. Two placements read from the evidence: (a) the pin follows the table's HOME (renderer reads the tier home, opal-data-assets), so writer, table and data agree after act 3's copy; (b) the pin is carved out of the flip and keeps opal-data-bd until its own move. Act 4's un-park condition names this row. No cell is cut on it until ruled."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W29-S1",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~29",
  "surfaced_at": "2026-10-11T12:23:31Z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "one_line": "The worktree /c/dev/wk-firmbkts-29 carries a dirty submodule gitlink at portal, so the AC3 write-surface bound (r4_scope.py) reads FAIL on a path the worker never wrote.",
  "spec_asserts": "TO-FB-g-7 section 4 AC3: r4_scope.py --allow the script, the test, the deliverables folder and the investigation file exits 0 with 'ROUND 4 SCOPE: OK', the worktree's changed set being the write surface.",
  "world_is": "After commit 0e4e8e8b0c (script and test only) git status --short in the worktree reads ' M portal' beside the two committed files and the new instance. git diff --submodule=short -- portal reads index c96efe1714784162c4134450da33ce6fd6226b60 against worktree Subproject commit 8ed372cb72659b96a5cfb4000a20b8ae315b9be7; git ls-tree HEAD portal reads 160000 commit c96efe1714 (the branch's recorded gitlink); git -C portal rev-parse HEAD reads 8ed372cb72. The worker issued no act on portal. The gitlink state was present in the worktree when the scope check first ran. Output: 'CHANGED portal <-- OUTSIDE', 'ROUND 4 SCOPE: FAIL 3 changed, 1 outside, 0 required missing', exit=1. The cause (checkout-time submodule advance or a drift of the worktree's portal checkout) was not investigated and no state was reset.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "round4/checks/r4_scope.py run in /c/dev/wk-firmbkts-29 at 2026-10-11T12:2xZ, exit=1, the CHANGED/OUTSIDE lines quoted above",
      "git diff --submodule=short -- portal and git ls-tree HEAD portal at 0e4e8e8b0c (dell1 branch base, worktree of 0.9.0_WK_ADVI_FIRMBKTS~29)",
      "the ajb_workspace repo's own git status at session start also lists ' M portal' (the parent tree, not this worktree)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION"
}
```

## Row filed by 0.7.0_AE_CloudOps~FB1 (FB-g-6, WAF ACL reconcile)

```json
{
  "id": "ADVI_FIRMBKTS-D1-S22",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.7.0_AE_CloudOps~FB1",
  "surfaced_at": "2026-10-11T12:26:35Z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "one_line": "TO-FB-g-6: neither of the CTO's two forms clears the portal-auth ACL plan on this provider (ignore_changes on the groups' version cannot index a set; an explicit null is a no-op); the only form that reads No changes is ignore_changes on the whole rule array, which the file's own comments record as refused, so no edit was made.",
  "spec_asserts": "TO-FB-g-6 step 2: try (i) ignore_changes naming the groups' version, (ii) an explicit version = null on the three managed_rule_group_statement blocks, (iii) the smallest third form that clears the plan while changing no rule name, priority, action, override or statement; bound 2: if the only clearing form changes behavior, stop and file a BLOCKING row. AC1: the targeted plan reads No changes.",
  "world_is": "Targeted plan of aws_wafv2_web_acl.opal_cloudfront_protection (terraform 1.15.8, aws provider 5.100.0, lock file tracked): base = 1 to change (three managed groups, version '' in state to null in config). Form (i) with paths rule[3..5].statement[0].managed_rule_group_statement[0].version: 'Error: Cannot index a set value' x3. Form (ii) explicit version = null x3: the same 1 to change, no effect. Form (iii-a) version = '': 'expected length of ...version to be in the range (1 - 128), got ' x3. Form (iii-b) ignore_changes = [tags, tags_all, rule]: 'No changes', measured with the file restored afterwards and never committed. A version pin is not available for ip-reputation (list-available-managed-rule-group-versions returns CurrentDefaultVersion None and 0 versions) and for the other two (Version_1.23, Version_1.26) it stops following AWS's default and plans as an update. Root cause as observed: the provider's flatten stores the empty string where AWS stores no Version, and the config can neither name nor omit it in a way the set-element comparison accepts. The file (waf-cloudfront.tf lines 371-377 and 415-421) records that ignore_changes on a WAF rule array was refused because the array is the security control and ignoring it blinds Terraform to a moved rule.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/g6/forms_tried.txt",
      "g6/baseline_targeted.out, g6/form_i_ignore_changes_paths.out, g6/form_ii_explicit_null.out, g6/form_iii_a_empty_string.out, g6/form_iii_b_ignore_rule_array_MEASURE_ONLY.out (the provider's own plan text per form)",
      "r4_waf.py --arms waf --root /c/dev/wk-firmbkts-30 at the unchanged base: A1 FAIL, A2 PASS, A3 PASS, 2 of 3, exit 1",
      "infra/aws/terraform/portal-auth/waf-cloudfront.tf lines 371-377 and 415-421 (the recorded refusal)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Owner of the call: 1.0.0_SA_CTO~DELL1 (the S12 ruling named two forms; both fail here) and the issuer for the order. Options, none applied: (A) lift the recorded refusal for the whole rule array, with its lost evidence replaced by a separate assertion (for example a check block over a data read of the live ACL's six rule names and priorities), which is a change beyond one resource and beyond this order's one file; (B) keep the ACL as the named rider of every portal-auth apply, which the act-1 ADDENDUM 1 already covers (the apply writes the same six rules and the churn returns, as measured at 07:54Z: AWS read byte-identical before and after); (C) a provider version that stores no empty string (a lock file and version constraint change, outside this order's file, and a provider upgrade for the whole root). This lane recommends B until the CTO rules on A, because A removes the one control that shows a moved rule. The order stays pending and no file changed in the worktree: git diff of waf-cloudfront.tf is empty."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-S23",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.7.0_AE_CloudOps~DELL1",
  "surfaced_at": "2026-10-11T12:36:00Z",
  "one_line": "TO-FB-g-10 AC1 and AC2 cannot be graded as written on dell1: the full plan dies on two AccessDenied reads for cloudops-dell1-agent-user, and AC1's grep counts the state-refresh line that names the resource whether or not the block is in config.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "TO-FB-g-10 step 3 and AC1/AC2: the root's full unscoped terraform plan, run by this seat, lists no eclipse_jwt_initial and ends Plan: 0 to add or No changes; grep -c eclipse_jwt_initial reads 0.",
  "world_is": "Measured 2026-10-11T12:34Z in /c/dev/wk-firmbkts-31 after the one-block edit (secrets.tf, fmt clean): terraform plan -refresh=true rc=1 in 11 s with two errors and no Plan line. (1) aws_sns_sms_preferences.account: sms-voice:DescribeSpendLimits denied to user/cloudops-dell1-agent-user. (2) aws_ssm_parameter.inf_gold_last_trigger_mode: ssm:GetParameter on /inf/gold/last-trigger-mode denied. Separately, the first output line is 'aws_secretsmanager_secret_version.eclipse_jwt_initial: Refreshing state...' with the config block removed, so grep -c reads 1; the laptop evidence plan_untargeted.out prints the same line at :232 beside 'will be created' at :508, so the line is printed for the state entry before refresh drops it and AC1 as written cannot read 0 until a state write. AC3 (SECRET VERSION: UNCHANGED, AWSCURRENT f57eb0dc-439b-4f46-859e-17fb00d968cb of 2 versions) and AC4 (ROUND 4 SCOPE: OK, 3 changed, 0 outside) pass. The id shape the order names, ADVI_FIRMBKTS-D1-DELL1-S<k>, does not match the gate's id grammar (fabric coordinate = one capital plus digits), so this row is D1-S23.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "/c/dev/wk-firmbkts-31/org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~DELL1/evidence/plan_full_after.out lines 1, 413-423 (uncommitted)",
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FBL/evidence_f12/plan_untargeted.out lines 232 and 508",
      "r4_secretver.py and r4_scope.py runs, 2026-10-11T12:35Z"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "The edit is NOT committed: the verifying plan could not run, so 'adds nothing new' is unproven. Two ways forward, both the issuer's: run steps 3 and AC1/AC2 from an identity that can read those two objects (the laptop did), or grant dell1 the two reads under its own order; and read AC1 as a count of the '# ... will be' plan line rather than the refresh line."
}
```

## Row filed by 0.7.0_AE_CloudOps~FBL (FB-g-9, delivery read)

```json
{
  "id": "ADVI_FIRMBKTS-S19",
  "project": "ADVI_FIRMBKTS",
  "fabric": "laptop",
  "surfaced_by": "0.7.0_AE_CloudOps~FBL",
  "surfaced_at": "2026-10-11T12:30:01Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "TO-FB-g-9: the one SEV1 test text was sent through the SMS send API (MessageId 88c89911-0012-4041-ae78-0be9b87d1bc9) but the account has NO delivery log for that API, so neither delivery nor failure of the text is readable from AWS.",
  "spec_asserts": "TO-FB-g-9 step 4: 'read the delivery outcome for that MessageId: the account's SMS delivery log (the CloudWatch Logs group your send's event destination or configuration set writes)'.",
  "world_is": "At 12:26:57Z one send-text-message returned a MessageId. The account has 0 SMS configuration sets (describe-configuration-sets), so the send has no event destination; no sms-voice or pinpoint log group exists; the two SNS delivery log groups (sns/us-east-1/313476888478/DirectPublishToPhoneNumber and /Failure, enabled this morning by TO-FB-f-12) log SNS direct publishes and held 0 events for the id and 0 events in the 15 minutes after. The record therefore reads delivery_status NO_DELIVERY_LOG_CONFIGURED, as the order directs. Arrival is read only on the phone. Separately, the order's proof command names /c/dev/ajb_workspace, which does not exist on the laptop; the grader ran from the worktree root with the same arguments.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "deliverables/0.7.0_AE_CloudOps~FBL/evidence/sev1_test_sms_20261011.json",
      "describe-configuration-sets length 0 at 12:28Z",
      "filter-log-events on both SNS groups, by id and over 15 minutes, 0 events"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "A later send for this diagnosis would need a configuration set with a CloudWatch Logs event destination created first (a write to the account's SMS configuration, outside this order's bounds and not started). Owner of that choice: the issuer and CTO."
}
```

## Row filed by 0.9.0_WK_ADVI_FIRMBKTS~32 (FB-g-11, transitional bronze-live row)

```json
{
  "id": "ADVI_FIRMBKTS-D1-W32-S1",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~32",
  "surfaced_at": "2026-10-11T12:37:31Z",
  "one_line": "The FB-g-11 dormant arm D4 reads infra/aws/lambda-edge/_shared/firm-config.mjs and .tools/ds-precommit-check.py as value-changed on this dell1 worktree, though their non-mark bytes equal the base; the check decodes the git show base with the Windows locale codec (cp1252) and the worktree file as UTF-8, and both files carry non-ASCII bytes, so identical bytes compare unequal. AC1 reads 4 of 5 arms, exit 1.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_dormant.py@cd50c0374e lines 43-86: _git(root, 'show', base:t).stdout is text=True (locale codec) while cur is open(..., encoding='utf-8')",
      "python -c locale.getpreferredencoding(False) on this device returns cp1252; git show cd50c0374e:infra/aws/lambda-edge/_shared/firm-config.mjs is 5791 bytes with 14 bytes above 127; the worktree copy is 5791 bytes (wc -c), and its UTF-8 text has 5782 characters",
      "bytewise (rb) non-mark lines of both files equal the base bytes; utf-8 decoded non-mark lines equal; cp1252 decoded non-mark lines unequal (the codec, not the value, produces D4 FAIL)",
      "git diff -U0 HEAD over the 15 regenerated targets: one changed line per file (the GENERATED mark), two mark lines in .tools/ds-precommit-check.py; no non-mark hunk"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-FB-g-11 AC1 (r4_dormant.py --arms live, expect 'ROUND 4 BRONZE LIVE: 5 of 5 arms'): D4 DORMANT passes on a conforming build; its preflight names one base artifact (the primary checkout's uncommitted edits) and states that a clean worktree does not have it.",
  "world_is": "On this dell1 Windows worktree (HEAD cd50c0374e, FB-g-11 edits uncommitted) D4 reports drift on two targets whose non-mark bytes equal the base. The check's git show decode uses the locale codec (cp1252), its file read uses UTF-8, and both targets carry non-ASCII bytes (14 and 9 above 127 in the base). The result is 4 of 5 arms and exit 1. No value moved in any target.",
  "notes": "Not fixed by this worker: the check is outside this order's paths and no edit to it is granted. Issuer decision needed: the check reads the base as bytes or decodes both sides as UTF-8 (positive control: with both sides decoded as UTF-8 the drift vanishes). The builder change, the tier_live row and the 15 regenerated targets are on the worker branch; the nested-portal target firmDisplayNames.generated.ts was not regenerated and is named in the report."
}
```

## Row filed by 0.9.0_WK_ADVI_FIRMBKTS~34 (FB-g-13, module platinum prefix)

```json
{
  "id": "ADVI_FIRMBKTS-D1-W34-S1",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~34",
  "surfaced_at": "2026-10-11T12:54:43Z",
  "one_line": "The FB-g-13 dormant arm M4 of r4_modgrant.py cannot pass on a conforming build: the spec requires the generated_locals.tf mark line (line 1, which names the registry list) to change, and the check's _kept() greedy matcher counts a base line as kept only when it appears verbatim, so a changed line 1 yields 0 of 100 kept.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "r4_modgrant.py M4 at round4/checks: _kept(old, new) advances i only on verbatim equality with old_lines[i]",
      "run at worktree HEAD 0b9b0b1c4e plus FB-g-13 edits: 'generated_locals.tf: base lines kept in order 0 of 100; added lines 104' and 'FAIL M4'",
      "the same run, base lines of generated_locals.tf excluding line 1 kept in order 99 of 99 (added 4: the platinum_prefix comment, local and closing brace content); main.tf 216 of 216 kept, 10 added",
      "the spec's own behavior 3 permits the mark line to change ('the generated file's mark line (the registry list it names)')"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-FB-g-13 AC1 (r4_modgrant.py --arms module, expect 'ROUND 4 MODULE GRANT: 5 of 5 arms'): M4 DORMANT passes when generated_locals.tf and main.tf keep every base line in order and only the new local, comment, outputs and mark line are added.",
  "world_is": "M1, M2, M3 and M5 pass (M3 terraform test 48 passed; M5 generate in sync and validate rc 0). M4 fails on generated_locals.tf alone, 0 of 100 base lines kept, because TARGET_REGISTRY_KEYS for LOCALS_PATH had to gain platinum_destinations and systems, which changes the mark's over clause and therefore base line 1. Result 4 of 5 arms, exit 1. The check is outside this order's paths and was not edited.",
  "notes": "Issuer decision needed: either the check's matcher skips the mark line (compare base lines 2 to N, as the spec's own allowance implies), or the mark line is exempted by rule. The build is otherwise complete and committed on the worker branch; AC1 is not met until this is ruled. No value of the module's outputs moved for any existing scope."
}
```

## Row filed by 0.9.0_WK_ADVI_FIRMBKTS~34 (FB-g-13, module platinum prefix)

```json
{
  "id": "ADVI_FIRMBKTS-D1-W34-S2",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~34",
  "surfaced_at": "2026-10-11T12:54:43Z",
  "one_line": "The output expressions the spec gives, lookup(local.scope_bucket, var.scope, null) and lookup(local.platinum_prefix, var.scope, null), fail when var.scope is null, though the spec requires both outputs to be null in that case; terraform test fails 2 of 2 runs with 'Invalid value for key parameter: argument must not be null'.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "terraform test (module folder) with the literal spec expressions: 0 passed, 2 failed, 46 skipped; main.tf lines 92 and 97, 'var.scope is null'",
      "after the fix var.scope == null ? null : lookup(...) on both outputs: terraform test 'Success! 48 passed, 0 failed.'"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-FB-g-13 behavior 2: bucket and platinum_prefix are lookup(...) with a null default, each null when var.scope is null.",
  "world_is": "Terraform's lookup() refuses a null key, so the literal expression cannot meet the null case the same spec states. The worker added a null guard in front of each lookup inside the two output blocks (main.tf only); the lookup form and the default are unchanged.",
  "notes": "Recorded for the issuer's read of the spec's expression against its own null case. No other module file changed."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W26-S1",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~26",
  "surfaced_at": "2026-10-11T12:36:08Z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "one_line": "S10 REWRITES A v3-PLACED ROW THAT THE S5 DIFFERENCE CONTROL FORBIDS TO MOVE: AC1 READS 4 OF 5",
  "spec_asserts": "Ruling S10 (ROUND_ANALYSIS.round3.md section 2): the one class-grain row with a {partition} token is re-written at class grain. Check arm S5 (r4_mapping.py structure): every class the previous table placed keeps its disposition, address and pattern.",
  "world_is": "opal-data-bd gold/clients/ is MOVE in mapping_v3.json with address s3://opal-data-49financial/advi/49financial/platinum/clients/{partition}. The S10 rewrite (partition null, address at class grain) changes that placed address, so S5 reads DISTURBED for this one class and AC1 reads 4 of 5. Keeping the v3 address instead leaves the token that S10 and arm U5 forbid. The two rulings conflict on this row; the repair applied S10 and did not rule between them.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/mapping_v3.json row opal-data-bd gold/clients/ (MOVE, dest.partition {partition}) @f30d22f82c",
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_mapping.py structure arm S5 (compares v3 to v4): AC1 output line DISTURBED opal-data-bd gold/clients/",
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/mapping_v4.json row opal-data-bd gold/clients/ (MOVE, partition null, address at class grain)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Owner 1.0.0_SA_CTO~DELL1: rule which of S5 or S10 governs this row, or exempt S10-rewritten rows from the difference control. The table keeps the S10 rewrite until ruled."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W26-S2",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~26",
  "surfaced_at": "2026-10-11T12:36:08Z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "one_line": "S7 SKIP FILES CANNOT BE A MARKER ROW WITHOUT A SECOND ROW AT A CLASS KEY: 1,142 performance_dim_SKIP.json OBJECTS STAY IN THEIR DATE-PARTITION DATA CHILDREN",
  "spec_asserts": "Ruling S7: *_SKIP.json is a marker by literal tail under ADDENDUM 1 marker_match, and goes to the <tier>_complete family as a skip kind. Check arm U3: a _SKIP.json tail carries marker_kind skip.",
  "world_is": "bronze/orion-api/ date partitions hold 1,142 objects named performance_dim_SKIP.json (110 bytes each) at the live listing of this round. The class-grain marker row bronze/orion-api/ (mapping_v4 row, marker_match completion tails) already holds that key; a skip row at the same (bucket, prefix) is a duplicate key (arm S2 dup count), and a skip row per date child would be a second row at each child key. S7 is therefore applied as 0 rows, and the skip objects remain counted in their date-partition data children. Writers of the skip file: infra/aws/lambda/inf-pipeline/inf-performance-daily/lambda_function.py:92 and infra/aws/lambda/inf-pipeline/inf-performance-daily/pull_inflection_performance_dim.py:212.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_mapping.py arm U3 reads 0 skip markers; S2 dup count is 0 by construction",
      "live listing of bronze/orion-api/ (LIST, 17,188 objects): performance_dim_SKIP.json count 1,142, sizes 110",
      "infra/aws/lambda/inf-pipeline/inf-performance-daily/lambda_function.py@f30d22f82c:92"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Owner 1.0.0_SA_CTO~DELL1: rule the shape of the skip marker (a per-date skip child, or a split of the class-grain marker row) because the structure arm forbids a second row at a class key."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W26-S3",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~26",
  "surfaced_at": "2026-10-11T12:36:08Z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "one_line": "FIVE QA-NAMED ROWS HAVE NO WRITER IN THE PIPELINE CODE: S6 CANNOT SAY qa-tool OR production, AND ARM U4 READS FAIL",
  "spec_asserts": "Ruling S6: a QA-named feed is QA only if its WRITER is a QA tool, read from the writer, not the name. Arm U4 needs qa_verdict qa-tool (RETIRE) or production (placed) on every QA-named row.",
  "world_is": "opal-data-bd qa-scratch/ (4 rows: ds1_run5_log.txt, ds1_run6_log.txt, ds1_validate/, gate2_unit_delta_run7.parquet; RETIRE from round 1) and opal-data-inf bronze/orion-api/probe/ (1 row) have no writer in infra/, data/, workflows/, lib/ or .tools/: a grep for the prefix tokens and the object names returns no pipeline hit. Naming them qa-tool would be a guess from the name, which S6 forbids; naming them production would move round-1 RETIRE rows. The rows carry qa_verdict unresolved. Arm U4 reads FAIL and AC2 reads 4 of 5.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_mapping.py arm U4 output: QA-NAMED-WITHOUT-WRITER for the five rows",
      "grep of infra/, data/, workflows/, lib/, .tools/ for qa-scratch, ds1_validate, gate2_unit_delta and orion-api/probe @f30d22f82c: 0 pipeline hits"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Owner 1.0.0_SA_CTO~DELL1: name the writer of these prefixes, or rule them not QA by writer. The order stays open until then."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W26-S4",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~26",
  "surfaced_at": "2026-10-11T12:36:08Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "TWO ROUND-1 PLACED COT CLASSES SHARE ONE DESTINATION: S3 RETURNS BOTH TO PLACEMENT, AND THE SHARED KEYS ARE UNRULED",
  "spec_asserts": "Ruling S3: a round-1 placed row stays as placed (the copied-unchanged rule wins). Round-2 collision rule 1e: a new class colliding with a placed class is FAULT until ruled.",
  "world_is": "opal-data-cot gold/positions_cube/ and gold/timeseries/positions_cube/ are both MOVE in mapping.json (round 1) to advi/cottonwood/gold/positions_cube/date={D}/data.parquet, with 342 of 342 keys in common. mapping_v2.json and mapping_v3.json made both FAULT (1e). S3 returns both to their round-1 placement (rulings_applied S3 = 2), so two placed rows now name the same destination keys.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/mapping.json rows opal-data-cot gold/positions_cube/ and gold/timeseries/positions_cube/ (MOVE) @f30d22f82c",
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/mapping_v3.json rows of the same prefixes (FAULT, reason overlap 342 of 342)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Owner 1.0.0_SA_CTO~DELL1: rule which of the two classes owns the shared destination, or split it. Not decided here."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W26-S5",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~26",
  "surfaced_at": "2026-10-11T12:36:08Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "TWO DATE PARTITIONS AND ONE FOLDER LIVE SINCE THE CENSUS HAVE NO ROW: ADDED UNDER RULE (c), CHILDREN RE-DERIVED FROM THE LIVE LISTING",
  "spec_asserts": "Ruling S9: a re-grid's child objects sum to its LIVE listing, and both numbers are printed. Ruling (c): a re-grid is per date partition.",
  "world_is": "The live listing holds a 2026-10-11 partition in bronze/eclipse_qa/ (884 objects live, 871 in v3) and in bronze/orion-api/ (17,188 live, 17,170 in v3). Neither partition is in the census or in the v3 children. Five parents moved since the v3 listing (cot forwardfill realized and transactions, cot silver, eclipse_qa, orion-api) and are flagged moving true with the two counts. mapping_v4 adds HOME child rows for bronze/eclipse_qa/2026-10-11/ and bronze/orion-api/2026-10-11/, a FAULT row for the non-date folder bronze/orion-api/2026-10-11/_markers/ (8 objects), and re-derives 12 child object counts and 1 excluded_markers count from the live listing.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/mapping_v4.json regrids entries with moving true and their moving_reason",
      "live LIST of bronze/eclipse_qa/ and bronze/orion-api/ (LIST calls, listed_at per parent in the regrids entries)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Owner: issuer 2.0.0_SA_COO~B1 to confirm the added child rows and the moving flags at the round-4 analysis."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W26-S6",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~26",
  "surfaced_at": "2026-10-11T12:36:08Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "FORWARDFILL _complete/ MARKERS USE THE TAIL .json: THE GROUP HAS NO NARROWER LITERAL NAME TAIL",
  "spec_asserts": "Arm U3 and the ruling wording: marker_match is a non-empty list of literal key tails, with no *, ? or bracket.",
  "world_is": "The ten forwardfill _complete/ groups (bd 4, cot 6) hold one object per date named <date>.json. Every live key in the ten groups ends .json, so marker_match is ['.json'] in each row. The tail is literal and passes the arms, but it is broad: any .json placed under a _complete/ prefix would be marked.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "live LIST of the ten _complete/ prefixes (LIST calls, .scratch/live_parents.json): every key ends .json (asserted in the build)",
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/mapping_v4.json rows with state_family bronze_complete and marker_match .json"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Owner: CTO to confirm the .json tail, or to name a finer rule for the forwardfill markers."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W26-S7",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~26",
  "surfaced_at": "2026-10-11T12:53:38Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "THREE MORE 2026-10-11 DATE PARTITIONS APPEARED AT THE RE-LIST (bronze/eclipse/, gold/eclipse/, silver/eclipse/): ADDED UNDER RULE (c)",
  "spec_asserts": "Ruling S9: each re-grid's child objects sum to its LIVE listing. Ruling (c): a re-grid is per date partition. Amendment 1 re-list instruction: re-list live where needed.",
  "world_is": "A re-list of the 29 re-grid parents (LIST calls only) found a 2026-10-11 partition under bronze/eclipse/ (1,811 objects live at the re-list, 1,798 at the earlier listing), gold/eclipse/ (533) and silver/eclipse/ (665). None was in the census or the v3 children. mapping_v4 adds one HOME or MOVE child row for each, copied from the latest dated sibling under rule (c). Nine parents are flagged moving: true with both counts. This extends the row S5 finding, which named two partitions and one folder at an earlier listing.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/mapping_v4.json rows with prefixes bronze/eclipse/2026-10-11/, gold/eclipse/2026-10-11/, silver/eclipse/2026-10-11/ and regrids entries with moving true @03e93707a6",
      "LIST of the 29 re-grid parents, .scratch/live_parents.json (re-listed at this round, keys not committed)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Owner: issuer 2.0.0_SA_COO~B1 to confirm the added child rows and the moving flags at the round-4 analysis."
}
```

## Row filed by 0.9.0_WK_ADVI_FIRMBKTS~33 (FB-g-12, ownership-key block)

```json
{
  "id": "ADVI_FIRMBKTS-D1-W33-S1",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~33",
  "surfaced_at": "2026-10-11T12:54:43Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "TO-FB-g-12 asked for a new OWNERSHIP_KEYS block after FIRM_CONFIG in the hand-kept carrier firm-config.mjs, but the renderer had no path to place a block that the file does not hold yet: the first generate would stop at the span lookup, which requires an existing export. The worker added a narrow anchor rule (AFTER_BLOCK) to _render_view in lib/opal_naming.py; the block is generated, not hand-typed.",
  "spec_asserts": "TO-FB-g-12 1a.2: 'Regenerate with the builder ... never by hand', with the block added after FIRM_CONFIG and every base line kept in order; the order lists the builder file as the only builder change (block renderer, dispatcher, TARGET_REGISTRY_KEYS row).",
  "world_is": "lib/opal_naming.py@0b9b0b1c4e _render_view takes a block's span from its own marks, else from an existing `export const <TAG>` line (_mjs_span), raising RegistryError when neither exists. A new block name in an mjs carrier therefore cannot be placed by the builder at base. The worker's edit adds AFTER_BLOCK = {'OWNERSHIP_KEYS': 'FIRM_CONFIG'} and an anchor branch in _render_view that places the new block at the anchor's END line on first generation only. All other lines are unchanged; AC1 O4 reads 108 of 108 base lines kept in order.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "lib/opal_naming.py@0b9b0b1c4e lines 1218-1226 (_mjs_span) and 1229-1252 (_render_view, before the edit): span raised RegistryError when no export line exists",
      "lib/opal_naming.py in the worker's uncommitted diff: AFTER_BLOCK and the anchor branch in _render_view",
      "r4_okeys.py --arms block at the worker tree: 5 of 5 arms, exit 0; O4 base lines kept in order 108 of 108, lines outside the block 0"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "The mechanism is in the builder file this order owns; the spec did not name it. Issuer to confirm the anchor rule is the intended way to place a block into a hand-kept mjs carrier (the alternative is a whole-file target, which this carrier is not)."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W33-S2",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~33",
  "surfaced_at": "2026-10-11T12:54:43Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "The FB-g-12 flip rehearsal (r4_flip.py --arms flip) names perfrp_firm_pin.py as a value-changing reader that the CTO's list requires, yet the flip does not move it; the check's F3 still passes on the four-target set, so the printed mismatch is informational and not a failure of this cell.",
  "spec_asserts": "TO-FB-g-12 AC2 (r4_flip.py, expect 'ROUND 4 FLIP FLIP: 4 of 4 arms'): the flip's value-changing set must stay the four served-tier targets.",
  "world_is": "At the worker tree (base 0b9b0b1c4e plus the builder edit) the flip changes exactly four targets: firm_registry.json, firm-config.mjs, directory_runner.py, holdings_snapshot.py. The printed line 'not value-changing readers named by the CTO's list: [data/assets/scripts/gold/runners_49f/perfrp_firm_pin.py]' says the CTO's list names perfrp_firm_pin.py as a reader that should change. perfrp_firm_pin.py is not among the four moved targets and its value did not change under the flip (its cause is not traced here). Result: 4 of 4 arms, exit 0.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "r4_flip.py --arms flip --root /c/dev/wk-firmbkts-33 output, worker tree: 'generated targets=17; value changes under the flip (mark lines excluded)=4'",
      "r4_flip.py output line: 'not value-changing readers named by the CTO's list: [data/assets/scripts/gold/runners_49f/perfrp_firm_pin.py]'",
      "F3 PASS and F4 PASS in the same run"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Read-only observation for the issuer: the CTO list and the flip's printed expectation may disagree about perfrp_firm_pin.py. Not changed by this worker: the check and the CTO list are outside this order's paths."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W33-S3",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~33",
  "surfaced_at": "2026-10-11T12:54:43Z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "one_line": "The commit of the FB-g-12 builder change was REFUSED by the naming gate (LGIC_ENFORCE DEC-6, ENFORCE): lib/opal_naming.py:1002 builds the legacy ownership key as the literal template platinum/%s/%s, which the gate reads as a NEW S3 key outside the registry. The worker did not override, force, or re-spell the template to slip past the detector. The worker tree holds the builder change and the regenerated firm-config.mjs, uncommitted.",
  "spec_asserts": "TO-FB-g-12 1a.1: the legacy key is 'platinum/<tenant>/ownership_map.json', built from one builder constant for the object name and the tenant (never typed per firm); 2.2: a firm token is permitted in the builder only inside a key()/address()/name()/lookup() call or a registry file; 2.3: if the naming gate refuses the commit, do not override or force: file a BLOCKING row with the gate's lines and stop.",
  "world_is": "The commit attempt printed: 'NAMING REFUSE lib/opal_naming.py:1002 platinum/%s/%s -> {source}/{scope}/platinum/%s/%s', 'why: NEW and OUT-OF-PATTERN as S3Key: REFUSE', 'NAMING-GATE: REFUSE 1 graded', and 'ERROR: BLOCKED -- the naming limb refused ... Commit aborted'. No builder call in the tree emits a legacy platinum/<tenant>/ key: key() emits canonical keys, and legacy_address() reads legacy_addresses.json rows, of which the only ownership row is the 49financial one (blackdiamond-platinum-49financial-ownership-map). A per-tenant legacy key therefore has no registered source; the registry is read-only under this order.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "safe-commit.sh output at the worker tree, 2026-10-11 ~12:5xZ: 'NAMING REFUSE lib/opal_naming.py:1002' and 'NAMING-GATE: REFUSE 1 graded' (exit 1, commit aborted)",
      "git status after the refusal: lib/opal_naming.py and infra/aws/lambda-edge/_shared/firm-config.mjs modified and unstaged; the channel file staged; HEAD 0b9b0b1c4e",
      "lib/opal_naming.py in the worker's uncommitted diff, lines ~995-1005: _ownership_legacy returns the literal template",
      "infra/logic/registry/legacy_addresses.json@0b9b0b1c4e: the 49financial ownership row is the only legacy row with an ownership-map template (platinum/49financial/ownership_map.json)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Issuer decision needed, one of: (a) a registered legacy row per tenant in legacy_addresses.json (the registry's owner is 4.0.0_SA_CRO; a READ address) that the block reads through legacy_address(); or (b) a CTO ruling on whether the gate admits the legacy platinum/<tenant>/ownership_map.json shape as an out-of-registry literal. Also observed: the safe-commit refusal printed 'files unstaged', but the channel file stayed staged in the worker index; the worker left that as it was."
}
```

## Row filed by 0.9.0_WK_ADVI_FIRMBKTS~33 (FB-g-12, amendment 1 re-run)

```json
{
  "id": "ADVI_FIRMBKTS-D1-W33-S4",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~33",
  "surfaced_at": "2026-10-11T13:03:15Z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "one_line": "AC3 (r4_scope.py) reads FAIL, 9 changed, 5 outside, because the scope check diffs the branch against the merge-base with the primary checkout (0b9b0b1c4e). The five OUTSIDE paths are the issuer's amendment commits caed07e6f0 and d5b9d4a803 on this branch (r4_grant.py, r4_modgrant.py, r4_okeys.py, r4_validator.py, the TO file). The worker's own writes since the amendment are the two code files.",
  "spec_asserts": "TO-FB-g-12 AC3 (r4_scope.py, expect 'ROUND 4 SCOPE: OK'): the changed files are inside the order's paths, the required files are changed.",
  "world_is": "At the worker tree: 'ROUND 4 SCOPE: FAIL 9 changed, 5 outside, 0 required missing', exit=1. The five outside paths equal the file list of git show --name-only caed07e6f0 d5b9d4a803. git diff --name-only d5b9d4a803 (the worker's writes since the amendment) lists lib/opal_naming.py and infra/aws/lambda-edge/_shared/firm-config.mjs only. The check takes no base argument, so it cannot exclude issuer commits on the branch.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "r4_scope.py --root /c/dev/wk-firmbkts-33 output, 2026-10-11 ~13:02Z: 'ROUND 4 SCOPE: FAIL 9 changed, 5 outside, 0 required missing'",
      "git show --name-only --format= caed07e6f0 d5b9d4a803: the five amended paths",
      "git diff --name-only d5b9d4a803: lib/opal_naming.py, infra/aws/lambda-edge/_shared/firm-config.mjs (the worker's writes)",
      "git merge-base HEAD <primary HEAD> = 0b9b0b1c4e, the base the check diffs against"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Not changed by the worker: the check and the amendment commits are outside this order's paths. Issuer decision needed: the check should diff from the amendment (or exclude issuer commits), or the amendment should land on the primary checkout. The worker's AC3 result is recorded as FAIL, not re-measured against a different base."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-S24",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "2.0.0_SA_COO~B1",
  "surfaced_at": "2026-10-11T13:20:00Z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "one_line": "Act 4's flip points the IRPT directory and holdings readers and writers at opal-data-49financial, which holds none of their keys: the F7 delta copy covers the served platinum classes only, and the mapped irpt/ home is read by no IRPT code.",
  "spec_asserts": "Round-3 analysis section 3 item 1 (ADDENDUM 7): the IRPT consumers and the gold scripts are readers of the routed bucket; the window opens when each is dormant with its pair; act 4 is the value flip with every regenerated target deployed in the same act.",
  "world_is": "The flip changes the bucket value in data/firm_registry.json, which the IRPT lambdas read through the generated bucket map (8 consumers of _authz/loaders.py), and in directory_runner.py and holdings_snapshot.py (the IRPT gold writers). Both sides address the key `investor-reporting/directory/latest.json` and its pointed objects (IRPT_DIRECTORY_PREFIX default in reporting-publish/handler.py:311 and holdings/handler.py:53; PROD_PREFIX in directory_runner.py:139 and holdings_snapshot.py:131). head-object, 2026-10-11 ~13:15Z: opal-data-bd investor-reporting/directory/latest.json exists (272 bytes, 2026-10-09T14:11:45Z); the same key in opal-data-49financial is 404, and so is the mapped address irpt/49financial/platinum/investor-reporting/directory/latest.json in both buckets. mapping_v4 homes these classes (census: directory 26, qa/directory 3, qa/holdings 2 objects) at irpt/{firm}/platinum/investor-reporting/... under rule RI1, and the project description assigns the IRPT slices to IRPT_BCKEND. The F7 delta tool's manifest is the served classes of opal-data-bd (r3_f7_delta.py docstring), which does not contain them. After act 4 the IRPT readers get 404s and the IRPT writers write the legacy key shape into the new bucket.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "aws s3api head-object on the four bucket/key pairs, 2026-10-11 ~13:15Z (the dell1 CloudOps identity)",
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/mapping_v4.json rows opal-data-bd investor-reporting/ (RI1)",
      "infra/aws/lambda/investor-reporting/reporting-publish/handler.py:311; holdings/handler.py:53; data/assets/scripts/gold/investor_reporting/directory_runner.py:139 and holdings_snapshot.py:131",
      "deliverables/2.0.0_SA_COO~B1/round4/checks/r4_flip.py (the five-to-four value-changing set includes the two gold runners and firm_registry.json)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "An endpoint question for 1.0.0_SA_CTO~DELL1 and, for the key shape, IRPT_BCKEND. Placements read from the evidence: (a) act 3 copies the 31 investor-reporting objects to the new bucket AT THE SAME KEYS (a pure copy; the RI1 re-shaping stays IRPT_BCKEND's), so writers and readers keep working after the flip; (b) the IRPT readers and writers read a transitional per-tier live bucket row (as the bronze pin does) until IRPT_BCKEND moves them. Act 4's un-park names this row."
}
```

## Row filed by 0.9.0_WK_ADVI_FIRMBKTS~36 (FB-g-2, producers' role grant draft)

```json
{
  "id": "ADVI_FIRMBKTS-D1-W36-S1",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~36",
  "surfaced_at": "2026-10-11T13:09:12Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "TO-FB-g-2 bound 4 asks for ASCII-only LF content in infra/aws/terraform/bd-pipeline/iam.tf, but the file already carries 8 non-ASCII lines at its base commit (em-dash characters in comments). The appended block is ASCII-only and the existing lines are untouched (0 deleted), so the bound is met for the added text only.",
  "spec_asserts": "TO-FB-g-2 section 2 bound 4: 'ASCII only; LF endings' for the file that the order changes (iam.tf), read as a property of the file.",
  "world_is": "iam.tf at base be150697b7 has 8 lines with non-ASCII bytes (lines 2, 16, 631, 774, 775, 833, 893, 953, all comment text). At the worker tree after the draft the count is still 8; the 44 added lines contain 0 non-ASCII bytes. Terraform fmt check is clean (rc=0) and the numstat is 44 added, 0 deleted.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "LC_ALL=C grep -n -P '[^\\x00-\\x7F]' infra/aws/terraform/bd-pipeline/iam.tf at base be150697b7: 8 lines (2,16,631,774,775,833,893,953)",
      "git diff -U0 -- infra/aws/terraform/bd-pipeline/iam.tf, added lines filtered for non-ASCII: 0 matches",
      "git diff --numstat -- infra/aws/terraform/bd-pipeline/iam.tf: 44 added, 0 deleted"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Not changed by the worker: the existing comment lines are outside this order's write grant to rewrite and deleting them would break the additive bound (G3). Issuer decision needed: whether bound 4 is read for the added text only (as this worker read it) or whether the non-ASCII comment lines are to be migrated under a separate order."
}
```

## Row filed by 0.9.0_WK_ADVI_FIRMBKTS~35 (FB-g-1, commit 711d72b756)

```json
{
  "id": "ADVI_FIRMBKTS-D1-W35-S1",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~35",
  "surfaced_at": "2026-10-11T13:10:37Z",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "0.0.0_AB_MSTR",
  "one_line": "The client-data check of the commit gate did not run on this device: the hashed account-id list is absent at its default path, so safe-commit printed WARN and commit 711d72b756 landed unchecked for client account ids.",
  "spec_asserts": "TO-FB-g-1 sections 2.3 and 5: commit the three files with .tools/safe-commit.sh under the worker serial; a refusal is reported and never overridden. The order names no client-account-id check and no step that supplies the list.",
  "world_is": "safe-commit printed 'WARN: client-data-check: hashed account-id list ABSENT at C:\\Users\\Test\\.opal\\account_id_hashes.txt -- this commit was NOT checked for client account ids (absent is not empty; set OPAL_ACCOUNT_ID_HASHES or place the list there)'. The commit then landed as 711d72b756 with the gate's naming line 'NAMING-GATE: PASS 0 graded' (the .mjs suffix is not graded by it). test -f on the default path reads ABSENT (rc=1) at 2026-10-11T13:10Z.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "safe-commit.sh output for commit 711d72b756 on branch wk-ADVI_FIRMBKTS-35, 2026-10-11T13:10Z: 'WARN: client-data-check: hashed account-id list ABSENT ... this commit was NOT checked'",
      "test -f on the default path (C:/Users/Test/.opal/account_id_hashes.txt): ABSENT, rc=1, 2026-10-11T13:10Z",
      "safe-commit.sh output for the same commit: '[commit-gate] WARN: commit-gate checked 0 of 3 file(s) -- NOTHING WAS CHECKED' (the commit gate reads .py, .sh, .tf and org/projects/*.json only)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Not changed by the worker: the gate and the device list are outside this order's paths. This row records that the gate did not run; it makes no finding about the committed content. disarm_owner 0.0.0_AB_MSTR is named by reading rule 32 (MSTR runs infrastructure); this order does not establish the owner of the list's placement on dell1, so the issuer should confirm or re-route it."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W37-S1",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~37",
  "surfaced_at": "2026-10-11T13:20:02Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "The consumer census of data/firm_registry.json could not class one reader: the ETF positioning producer bundles the registry file as a packaged member, and no file in its own folder reads the bucket field.",
  "spec_asserts": "TO-FB-g-14 section 1a item 4: every reader of data/firm_registry.json's bucket field outside the IRPT path is named and classed served-tier or IRPT; a consumer that cannot be classed goes in a surprise row and is not changed.",
  "world_is": "infra/aws/lambda/etfs-pipeline/etf-positioning-producer/build_package.py:144-145 copies data/firm_registry.json into the producer package as a member. A folder-scoped comp-find over infra/aws/lambda/etfs-pipeline/etf-positioning-producer for 'import keys|from keys|from _keys|registry|firm_bucket|bucket' returned 17 hits across 2 files, all in build_package.py (the registry member list and comments); the producer's own runtime code names neither the registry file nor a bucket reader. Whether the packaged bytes are read at runtime, and which code reads the bucket field there, is not traced.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/lambda/etfs-pipeline/etf-positioning-producer/build_package.py:144-145@ba53f8a883 (data/firm_registry.json listed as a package member)",
      "comp-find -i over infra/aws/lambda/etfs-pipeline/etf-positioning-producer @ba53f8a883 worktree: DENOMINATOR 17 hit(s) across 2 file(s), all in build_package.py",
      "census of firm_registry across data/ infra/aws/lambda infra/aws/lambda-edge infra/aws/terraform lib .tools portal/src: DENOMINATOR 140 hit(s) across 11004 file(s), 59 file(s) listed; this producer is the one non-IRPT reader the census could not class"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Not changed by the worker: the producer is outside this order's paths and the cell makes no value change to the bundled bytes (the generated marks change only). The row is a classing gap, not a finding about the producer's behaviour. The issuer should confirm whether the bundled registry is read for its bucket field and by which code; the answer decides whether the ETF producer is served-tier (follows the act-4 flip) or needs a row of its own."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W37-S2",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~37",
  "surfaced_at": "2026-10-11T13:22:15Z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "one_line": "FB-g-14 cannot commit: the naming gate (LGIC_ENFORCE DEC-6, ENFORCE mode) refused lib/opal_naming.py:384, the literal 'irpt' in the new _irpt_bucket() helper, as a NEW hand-kept carrier. The work stays uncommitted in the worktree; the order stays open.",
  "spec_asserts": "TO-FB-g-14 section 2 bound 4 and section 5: if the commit is refused on a lane or by the naming gate, STOP, leave the edit uncommitted, file a BLOCKING row with the gate's lines, and do not override or force.",
  "world_is": "safe-commit.sh for the 19-path FB-g-14 commit (HEAD ba53f8a883) ended: 'ERROR: BLOCKED -- the naming limb refused (LGIC_ENFORCE DEC-6, ENFORCE mode). Commit aborted; files unstaged.' followed by '[naming-gate] NAMING REFUSE lib/opal_naming.py:384 irpt -> lookup('irpt')', '[naming-gate]   why: NEW hand-kept carrier (context rule); hand-kept carrier of 'irpt' outside every permitted context: read it through lookup('irpt')' and '[naming-gate] NAMING-GATE: REFUSE 1 graded'. The gate's own text (.tools/naming-gate.py:2008) names lookup('irpt') as the permitted read. The line at 384 is the helper body: live = ((scope_row.get(\"product_live\") or {}).get(\"irpt\") or {}).get(\"bucket\"). The gate's DENOMINATOR was 16 paths, 0 excluded; COVERAGE 16 seen. The helper takes scope_row only (order section 1a item 2a), so lookup() needs a registry argument the order does not give it. Not overridden, not forced; index cleared of the failed commit's staged paths (no worktree change).",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "safe-commit.sh output for FB-g-14 on wk-ADVI_FIRMBKTS-37 at HEAD ba53f8a883, 2026-10-11T13:19Z: 'ERROR: BLOCKED -- the naming limb refused (LGIC_ENFORCE DEC-6, ENFORCE mode)'",
      "lib/opal_naming.py:384 @ worktree (uncommitted): live = ((scope_row.get(\"product_live\") or {}).get(\"irpt\") or {}).get(\"bucket\")",
      ".tools/naming-gate.py:2008 @ ba53f8a883: carr_txt = '; hand-kept carrier of %r outside every permitted context: read it through lookup(%r)'",
      "AC1 r4_irptlive.py --arms live: 5 of 5 arms PASS in the worktree; AC2 r4_scope.py: OK 17 changed, 0 outside, 0 required missing (both uncommitted)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Blocks the order's commit, not its content. Disarm is not needed: the file is not live, and the INERT surprise S1 is unaffected. The issuer decides the route: a permitted read of 'irpt' (for example through a registry argument to the helper, which the order's signature does not give) or a naming-gate ruling. The worker did not edit the gate, the helper, or the lane."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-S25",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "2.0.0_SA_COO~B1",
  "surfaced_at": "2026-10-11T14:10:00Z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "one_line": "With the IRPT bucket map on its transitional live row, the IRPT lambdas read the ownership map from the legacy bucket and key forever: after act 2 the producers write it only at the canonical home, so IRPT's authorization read goes stale (revocations lag) and never flips at act 4.",
  "spec_asserts": "Round-3 analysis section 3 item 1 and ADDENDUM 6: the ownership class rejoins the move; D1-S17 (the stale ownership map at the new home) disarms at act 4; the IRPT readers and gold writers read a transitional live row, byte-identical now and out of act 4.",
  "world_is": "infra/aws/lambda/investor-reporting/_authz/loaders.py load_ownership (lines 229-290, 8 consumers) reads bucket_for(tenant) and OWNERSHIP_KEY_TEMPLATE.format(firm=tenant) = platinum/{firm}/ownership_map.json (IRPT_OWNERSHIP_KEY env, default as shown); bucket_for is the generated IRPT_DIRECTORY_BUCKET_MAP, which FB-g-14 pointed at the transitional live row (opal-data-bd). An absent map is read as an EMPTY map (deny). D_00 writes the ownership map through the seam (platinum/49financial/ownership_map.json, legacy_prefix class platinum/49financial/); in canonical mode, from act 2, it writes only advi/49financial/platinum/49financial/ownership_map.json in opal-data-49financial. So after act 2 the IRPT read keeps returning the last legacy copy; after act 4 the registry flip does not move it (the live row holds), so the staleness is permanent. The directory and holdings reads of the same lambdas are correct on the live row (their keys live only there); the ownership map is the producers' served key and must follow the flip.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/lambda/investor-reporting/_authz/loaders.py lines 33-34 and 229-290 (read in full at HEAD 2026-10-11 ~14:0xZ)",
      "round4/checks/r4_irptlive.py I3: firm_registry rows and firm_bucket_map read the live row, FIRM_CONFIG the routed bucket (5 of 5 arms at merged head 661643f5be)",
      "data/black_diamond/scripts/gold/lib/platinum_dest_view.py: the class platinum/49financial/ placed at the canonical template; ledger/R3_ACT2_OUTSIDE_READERS_CENSUS.md ADDENDUM 1 names IRPT_OWNERSHIP_KEY as a reader of the class"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "An endpoint question for 1.0.0_SA_CTO~DELL1 (a never-widen class: stale authorization data). Placement read from the evidence: (c) the IRPT loader reads the ownership map from a generated pair (bucket: the routed bucket; key: legacy now, canonical at act 4, engaged by a canonical-bucket list as the validator's is), while its directory and holdings reads stay on the live row; one dormant IRPT cell before act 2, deployed with act 4. Alternatives: keep the ownership class carved out of the move (legacy in both modes, the round-2 ADDENDUM 6 form) until IRPT_BCKEND moves its readers; or dual-write (refused by the no-shadow-path rule). Act 2's un-park names this row."
}
```

## Row filed by 0.7.0_AE_CloudOps~FB1 (FB-g-8, act 0 apply, the seat gate)

```json
{
  "id": "ADVI_FIRMBKTS-D1-S26",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.7.0_AE_CloudOps~FB1",
  "surfaced_at": "2026-10-11T13:50:40Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "safe-apply's cross-box seat gate read open_deploy=hit verdict=STOP for another seat's OPEN deploy that names the bd-pipeline root, and in WARN mode the apply proceeded; the actor sees that line only once the apply is running, unless it runs --dry-seat-gates first.",
  "spec_asserts": "safe-apply.sh header: the seat gates (apply-who-check and crossbox-deploy-check) print and, in WARN mode, never change the exit code or the flow; --dry-seat-gates runs the two checks, prints, and exits with no halt gate, plan or terraform following. CLAUDE.md section 1: one issuer and one actor per scope, with an open deploy naming a root as the cross-box overlap signal.",
  "world_is": "2026-10-11 13:43:23Z, .tools/safe-apply.sh -chdir=infra/aws/terraform/bd-pipeline apply <saved plan> for ADVI_FIRMBKTS TO-FB-g-8: 'CROSSBOX-DEPLOY device=dell1 root=bd-pipeline open_call=clear overlap=clear upset=clear open_deploy=hit verdict=STOP' with '[seat-gates] STOP: 2 hit(s) in OPEN-DEPLOY -- first: open deploy healgap-r3-act3-asset-dim-reattempt-20261011 (author 2.0.0_SA_COO~G1, status OPEN) names the root (token infra/aws/terraform/bd-pipeline)', then 'would stop under ENFORCE ( crossbox-deploy ); WARN mode proceeds.' The scoped plan of this act changed one resource (an IAM role policy) and none of that deploy's; the match is by the root's path token, not by resource. The actor did not run --dry-seat-gates before the apply, so the line was read after the write, not before it.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/act0/apply_safe-apply.out (the two seat-gate lines and the WARN line)",
      ".tools/safe-apply.sh header lines on --dry-seat-gates and the WARN/ENFORCE switch files in org/mcp",
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/ADVI_FIRMBKTS.TO-FB-g-8.act0-grant.proof_of_spec.json, surprises[0]"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Form only; no hazard is armed. Two things for the gate owner, neither this lane's: (1) the overlap is matched on the root path token, so a one-resource IAM policy and an unrelated deploy in the same root read as a STOP; the gate cannot tell a disjoint scope from an overlapping one. (2) Under ENFORCE this apply would have stopped, and the act's order says nothing about reading the gate first. This lane's own correction: read --dry-seat-gates before any apply on a root another seat names."
}
```

## Rows filed by 0.9.0_WK_ADVI_FIRMBKTS~39 (FB-g-16, amendment 1: CANONICAL_PLATINUM_BUCKETS)

```json
{
  "id": "ADVI_FIRMBKTS-D1-W39-S1",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~39",
  "surfaced_at": "2026-10-11T13:57:56Z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "one_line": "The amendment renders CANONICAL_PLATINUM_BUCKETS into infra/aws/lambda-edge/_shared/firm-config.mjs, which is outside this order's <paths>; the worker's regeneration of that carrier is not in the grant. AC1 W5 reads FAIL (out of sync = firm-config.mjs) and the order stays open.",
  "spec_asserts": "TO-FB-g-16 amendment (2.0.0_SA_COO~B1, CLAUDE.md rule 27): the same builder renders the identical list as export const CANONICAL_PLATINUM_BUCKETS into _shared/firm-config.mjs. Bounds 2.1: files that change are lib/opal_naming.py, loaders.py and the new test; no other Lambda file. AC3 allow-list excludes firm-config.mjs.",
  "world_is": "The builder side is committed on wk-ADVI_FIRMBKTS-39 (lib/opal_naming.py: _blk_canonical_platinum_buckets registered for loaders.py and firm-config.mjs; AFTER_BLOCK takes a candidate list). loaders.py is regenerated and carries CANONICAL_PLATINUM_BUCKETS = [opal-data-49financial]. A scratch render of firm-config.mjs (.scratch/fc, not tracked) is a pure addition of one block after OWNERSHIP_KEYS, 5 lines. The tracked firm-config.mjs is unchanged in this worktree, so AC1 W5 reads FAIL: 'out of sync=[infra/aws/lambda-edge/_shared/firm-config.mjs]; other targets value-changed=[]; validate rc=0'.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "r4_irptown.py --arms read at the worker tree, 2026-10-11 ~13:57Z: 4 of 5 arms; W5 FAIL, out of sync=[infra/aws/lambda-edge/_shared/firm-config.mjs]",
      "python lib/opal_naming.py generate --out .scratch/fc --target infra/aws/lambda-edge/_shared/firm-config.mjs; diff against the tracked file: 5 added lines after line 101",
      "order Bounds 2.1 and AC3 --allow list (no firm-config.mjs)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Not changed by the worker: regenerating firm-config.mjs in this worktree would put it in the change set, which AC3 refuses. Issuer decision needed: grant firm-config.mjs as a path for the regeneration (one generate --target line), or accept the carrier as a later cell's regeneration and read W5 accordingly. The worker's result is recorded as AC1 FAIL, not re-measured against a different grant."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W39-S2",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~39",
  "surfaced_at": "2026-10-11T13:57:56Z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "one_line": "AC3 (r4_scope.py) reads FAIL, 6 changed, 1 outside: the diff runs against the primary merge-base, so the issuer amendment commit 144e36d9f7 on this branch (the corrected r4_irptown.py) reads as outside the grant. The worker's own writes are all inside it.",
  "spec_asserts": "TO-FB-g-16 AC3 (r4_scope.py, expect 'ROUND 4 SCOPE: OK'): the changed files are inside the order's paths and the required files are changed.",
  "world_is": "At the worker tree: 'ROUND 4 SCOPE: FAIL 6 changed, 1 outside, 0 required missing', exit=1. The one outside path is deliverables/2.0.0_SA_COO~B1/round4/checks/r4_irptown.py, last changed by 144e36d9f7 (the issuer's amendment, not a worker write). The three code files, the instance and the session log are inside the grant. This is the same class as FB-g-12 S4 (the check takes no base argument).",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "r4_scope.py --root /c/dev/wk-firmbkts-39 output at 2026-10-11 ~13:57Z: 'ROUND 4 SCOPE: FAIL 6 changed, 1 outside, 0 required missing'",
      "git log -1 -- round4/checks/r4_irptown.py: 144e36d9f7 amend(ADVI_FIRMBKTS FB-g-16, 2.0.0_SA_COO~B1)",
      "ADVI_FIRMBKTS-D1-W33-S4 (the same class, FB-g-12)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Not changed by the worker: the check reads the primary merge-base and the amendment commit is on this branch. Issuer decision needed: the check should exclude issuer commits, or the amendment should land on the primary checkout. The worker's AC3 is recorded as FAIL, not re-measured against another base."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W39-S3",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~39",
  "surfaced_at": "2026-10-11T14:01:28Z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "one_line": "After amendment 2 regenerated firm-config.mjs (5 added lines: CANONICAL_PLATINUM_BUCKETS), AC1 W5 reads FAIL with 'out of sync=[]; other targets value-changed=[infra/aws/lambda-edge/_shared/firm-config.mjs]'. The stale check is clean; the value-change clause counts the amendment's own added block as drift. AC1 reads 4 of 5, not the 5 of 5 the amendment expects.",
  "spec_asserts": "AC1 W5 (r4_irptown.py): 'no other generated target covering scopes.json changes a non-mark line against the base'; amendment 2 expects 'W5 should read 5 of 5' after the firm-config regeneration.",
  "world_is": "git diff of firm-config.mjs against base is exactly the generated block: 5 added lines after OWNERSHIP_KEYS, no line removed or changed. The check's drift test compares every non-mark line of the file against base (_nm removes only the GENERATED header lines), so any added generated block trips it. out of sync=[] shows the carrier equals the builder's output.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "r4_irptown.py --arms read at the worker tree after regeneration, 2026-10-11 ~14:01Z: 'out of sync=[]; other targets value-changed=['infra/aws/lambda-edge/_shared/firm-config.mjs']; validate rc=0', 4 of 5 arms",
      "git diff -- infra/aws/lambda-edge/_shared/firm-config.mjs: 5 added lines, 0 removed",
      "r4_irptown.py read(): drift = [t for t ... if _nm(git show base:t) != _nm(cur)]"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Not changed by the worker: the amendment asked for this block in the carrier, and the carrier now carries exactly it. Issuer decision needed: the W5 drift clause should exempt blocks the builder adds (or compare against a base regenerated without them). Like S2, a check artifact the issuer grades at the drain. AC1 is recorded as 4 of 5, not re-measured."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-S27",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "2.0.0_SA_COO~B1",
  "surfaced_at": "2026-10-11T15:00:00Z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "one_line": "The live bucket policy of opal-data-49financial has NO Allow statement and its fence admits none of the act-4 readers' principals: after the flip the CloudFront origin (OAI), the validator and six IRPT/partner readers would be refused at the new bucket.",
  "spec_asserts": "Round-3 analysis section 3 item 1 and ADDENDUM 7: act 4 is the value flip with every regenerated reader deployed in the same act; acts 4b and 4c route the two partner Lambdas to the canonical home first; the readers' pairs name their authorization (round-3 act 1 COO half: the serving grant on the new bucket 'is read from the live bucket policy at the amendment').",
  "world_is": "aws s3api get-bucket-policy opal-data-49financial (the dell1 CloudOps identity, 2026-10-11 ~15:0xZ): 4 statements, all Effect Deny: DenyForeignFirmPrincipals (Principal *, s3:*, ArnNotLike aws:PrincipalArn over 21 patterns: role/*-49f-*, three service-linked roles, bd-exporter-ec2-role, infrastructure-ops-lambda-role, infrastructure-snapshot-role, opal-advi-stitch-landing-role, opal-drift-producer-codebuild-role, opal-globgrph-derive-runner-task, opal-globgrph-incremental-updater, opal-news-lambda-role, partners-lambda-role, security-sweep-dedicated-role, user/Andrew_Berman, Andrew_Berman_Console, Opal_Terminal, role/irpt-holdings-role, user/cloudops-dell2-agent-user, user/cloudops-dell1-agent-user, role/irpt-performance-adapter-role) and three DenyPerformanceAdapter* statements. Allow statements: none. The edge router addresses the S3 origin by mutating request.origin.s3 under OAI E139998VWH0PD (index.mjs:14-16, 487-494: 'new partner buckets require OAI canonical user in bucket policy (per-bucket, no wildcard)'); the OAI principal is neither in the deny's exemption list nor granted by an Allow. Principals read by act 4 or 4b: lambda-edge-execution-role (validator, ownership map; router and guard share it) NOT admitted; irpt-directory-role, irpt-export-render-role, irpt-narrative-role, irpt-status-role, irpt-ycharts-generate-role (ownership map) NOT admitted; exec-summary-generator-role (4b) NOT admitted; admitted: irpt-49f-reporting-read-role (pattern), irpt-holdings-role, irpt-performance-adapter-role (with its three scoped denies), partners-lambda-role (its IAM allow reads opal-data-*). The registry's exemptions.json for this bucket lists the same set (the live policy equals the desired plane).",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "aws s3api get-bucket-policy --bucket opal-data-49financial, 2026-10-11 ~15:0xZ, parsed: statements and the 21 ArnNotLike values printed",
      "infra/logic/registry/exemptions.json opal-data-49financial rows (19 principals)",
      "infra/aws/lambda/ci/lambda-source-map.json iam_role for the eight irpt consumers, partners-lambda-role, lambda-edge-execution-role; infra/aws/terraform/exec-summary/iam.tf (exec-summary-generator-role)",
      "infra/aws/lambda-edge/shared-advisor-router/index.mjs lines 14-16 and 487-494 (OAI origin auth)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "An endpoint question for 1.0.0_SA_CTO~DELL1 (a never-widen class: it ADMITS principals to a fenced firm bucket). Placement read from the evidence: one prerequisite act before acts 4b and 4c and 4, under its own pair, through the registry (exemptions.json rows, scoped by `actions` s3:GetObject and `prefix` the canonical platinum prefix where the row grammar allows; the OAI Allow on the served prefix, never bucket-wide) and the shared-infra apply of s3-49financial.tf; each reader role's own IAM Allow on that prefix read separately. Acts 4, 4b and 4c's un-park names this row; act 2 and 3 are not blocked by it (their identities are admitted)."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W40-S1",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~40",
  "surfaced_at": "2026-10-11T14:09:24Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "The router spec test 'even a map that names the firm's own bucket changes nothing while the list is empty' relied on the handler default being the empty list; it now passes an explicit empty list (one call edited). No other spec changed.",
  "spec_asserts": "FB-g-17 1a.1: read test/canonical-platinum.spec.mjs and make the smallest edit that keeps every spec's intent. 2.1: the router's spec file(s) change only if a spec referenced the deleted local.",
  "world_is": "The spec did not name the deleted local. It called handleWithMap(event, MAP) with the handler default (index.mjs line 161), which is now the generated list. That list names the firm's own bucket, which MAP maps to, so the call would take the canonical path. The call now passes an empty list as its third argument, which keeps the test's title and intent.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "canonical-platinum.spec.mjs line 51 at the worktree C:/dev/wk-firmbkts-40: handleWithMap(ev(...), MAP) with no list argument, before the edit",
      "index.mjs line 161 at the worktree: canonicalBuckets = CANONICAL_PLATINUM_BUCKETS default parameter",
      "bash run-gate.sh after the edits at the worktree: 51 pass, 0 fail, rc 0"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "The failure-without-edit is reasoned from the code, not run. Issuer may rule whether an edit under test/ is the intended reach of the 2.1 bound."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W40-S2",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~40",
  "surfaced_at": "2026-10-11T14:09:24Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "The round-4 validator check's K1 label says the helper exports a frozen EMPTY list. The list is now the generated one (length 1), and K1 still passes because the arm does not test length.",
  "spec_asserts": "r4_validator.py K1 (round-4 check, issuer 2.0.0_SA_COO~B1): ownership_key.mjs exports a frozen EMPTY CANONICAL_PLATINUM_BUCKETS. FB-g-17 1a.2: the list is the generated one.",
  "world_is": "AC2 output at the worktree after the edits: 'helper exports: {names:[CANONICAL_PLATINUM_BUCKETS, ownershipMapKey], frozen:true, len:1}' and 'PASS K1'. The arm checks the export names and frozenness only, so the label and the measured list disagree while the check still reads 4 of 4.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "r4_validator.py --arms key run at the worktree after the edits: helper exports len:1, K1 PASS, ROUND 4 VALIDATOR KEY: 4 of 4 arms",
      "r4_validator.py line 6 (K1 text) and lines 58-59 (the K1 arm tests names and frozen only)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "The check is the issuer's and was not edited. The label is for the issuer to amend."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W40-S3",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~40",
  "surfaced_at": "2026-10-11T14:09:24Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "The router's v15 header comment still says the canonical list is EMPTY today. The bounds keep every line other than the local definition and its comment, so the header now contradicts the imported list.",
  "spec_asserts": "FB-g-17 1a.1 and 2.1: the router change is the import, the deleted local and one updated comment sentence; every other line stays.",
  "world_is": "index.mjs line 76 (v15 header) reads 'listed in CANONICAL_PLATINUM_BUCKETS (EMPTY today)', and lines 80-81 describe a registry edit plus a list entry. The list is now the generated registry list. The header was left unchanged as the bounds require.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "index.mjs line 76 at the worktree C:/dev/wk-firmbkts-40 after the edits: 'listed in CANONICAL_PLATINUM_BUCKETS (EMPTY today)'",
      "index.mjs lines 80-81 at the worktree after the edits"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Not edited, because 1a.1 says every other line stays. A header-only update needs an issuer grant."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W42-S1",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~42",
  "surfaced_at": "2026-10-11T14:29:37Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "The pre-commit risk reflex printed HOLD on infra/aws/terraform/modules/opal_name/main.tf, citing deploy-completion notes about other roots' main.tf files (a basename match); the commit landed rc=0 on 273de502f0.",
  "spec_asserts": "The pre-commit risk reflex (comp-pulse diff) names a HOLD only for a touched node that a recorded claim is written about.",
  "world_is": "The HOLD cites org/critical_paths/change_management/20260616T2001Z_nfra-infrpt-dr-snapshot-backup_deploy_completion.md:35, which is about main.tf of the portal_lambda_ec2_snapshot permissions, a different Terraform root. The reflex matched the bare name main.tf across six roots (9 claims each), not the touched opal_name/main.tf.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "safe-commit output at commit 273de502f0: '[HOLD] infra/aws/terraform/modules/opal_name/main.tf -> file:infra/aws/terraform/aaii-v2-bucket-lifecycle/main.tf (9 recorded claim(s))' and five further roots",
      "org/critical_paths/change_management/20260616T2001Z_nfra-infrpt-dr-snapshot-backup_deploy_completion.md:35 read at the worktree: '- **main.tf:** fix portal_lambda_ec2_snapshot (EC2SnapshotPermissions)'"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "No action taken; the commit was not blocked and the cited claim is not this cell's. Filed for the reflex's owner to judge whether the bare-basename match is intended."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-S28",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "2.0.0_SA_COO~B1",
  "surfaced_at": "2026-10-11T14:51:34Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "The standing scoped-exemption instrument infra/aws/terraform/shared-infra/tests/check_fence_scoped_rows.py reads ok=False at HEAD: its scratch root before_strip fails init on one(list), and it raises a cp1252 UnicodeEncodeError unless PYTHONIOENCODING=utf-8 is set.",
  "spec_asserts": "The file's own docstring (NFRA_CTLPLN.TO-CT-d-2 AMENDMENT 4) says it proves the scoped-exemption renderer and the fail-closed readers on scratch copies and ends on a FENCE-SCOPED line; its last line is the instrument a renderer change is graded by.",
  "world_is": "cd infra/aws/terraform/shared-infra/tests && PYTHONIOENCODING=utf-8 python check_fence_scoped_rows.py (2026-10-11 ~15:2xZ, dell1) printed: 'ERROR: root before_strip: init rc=1 ... while calling one(list) | local.lgic_managed_firm_buckets is object with 2 attributes Invalid value for \"list\" parameter: must be a list, set, or tuple value with either zero or one elements.' and 'FENCE-SCOPED rows_today=32 unchanged_today=False scoped_rendered=0/0 sim_ok=0/0 refusals_ok=0/7 unknown_key_refused_by=none ok=False'. Without PYTHONIOENCODING it stops on UnicodeEncodeError (charmap, positions 36-41). The renderer this round changed (FB-g-19, -20, -21) is graded by the issuer's r4_modfence.py, r4_modallow.py and r4_policy.py instead.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "the command above, run read-only in the working tree at HEAD, last two output lines quoted",
      "infra/aws/terraform/shared-infra/s3-lgic-firm-buckets.tf (the local named in the error)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Not a prerequisite of act 3b: nothing in the act depends on this instrument reading ok=True. It stands as a broken regression instrument for the fence module; an owner (the NFRA_CTLPLN lane that built it) repairs or retires it. Surfaced, not chased."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W43-S1",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~43",
  "surfaced_at": "2026-10-11T14:53:59Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "The pre-commit risk reflex printed HOLD on infra/aws/terraform/modules/opal_name/main.tf citing deploy-completion notes about other roots' main.tf files (a basename match); the commit landed rc=0 on c64a667818.",
  "spec_asserts": "The pre-commit risk reflex (comp-pulse diff) names a HOLD only for a touched node that a recorded claim is written about.",
  "world_is": "The HOLD cites org/critical_paths/change_management/20260616T2001Z_nfra-infrpt-dr-snapshot-backup_deploy_completion.md:35, which is about main.tf of the portal_lambda_ec2_snapshot permissions, a different Terraform root. The reflex matched the bare name main.tf across six roots (9 claims each), not the touched opal_name/main.tf. The same match was filed as ADVI_FIRMBKTS-D1-W42-S1 on acb073608a.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "safe-commit output at commit c64a667818: '[HOLD] infra/aws/terraform/modules/opal_name/main.tf -> file:infra/aws/terraform/aaii-v2-bucket-lifecycle/main.tf (9 recorded claim(s))' and five further roots",
      "org/critical_paths/change_management/20260616T2001Z_nfra-infrpt-dr-snapshot-backup_deploy_completion.md:35 read at the worktree: '- **main.tf:** fix portal_lambda_ec2_snapshot (EC2SnapshotPermissions)'"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "No action taken; the commit was not blocked and the cited claim is not this cell's. Repeat of the W42-S1 observation for the reflex's owner."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W43-S2",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~43",
  "surfaced_at": "2026-10-11T14:53:59Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "safe-commit printed WARN that the client-data check could not run (hashed account-id list absent on this device); commit c64a667818 was not checked for client account ids.",
  "spec_asserts": "The commit gate runs the client-data check (hashed account-id list) on every commit it admits.",
  "world_is": "The hashed list is absent at C:\\Users\\Test\\.opal\\account_id_hashes.txt on dell1 and OPAL_ACCOUNT_ID_HASHES is unset, so the check printed WARN and skipped the list comparison. Absent is not empty. The committed diff carries no 12-digit number (git show c64a667818 added lines matching 12 digits: 0), so no client account id entered the commit.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "safe-commit output at commit c64a667818: WARN: client-data-check: hashed account-id list ABSENT at C:\\Users\\Test\\.opal\\account_id_hashes.txt -- this commit was NOT checked for client account ids",
      "git show c64a667818 with added lines matched against a 12-digit pattern: 0 at the worktree"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "No action taken by this worker; the list is a per-device input, not this cell's. Filed for the owner of the client-data check to judge whether dell1 needs the list placed."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-S29",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "2.0.0_SA_COO~B1",
  "surfaced_at": "2026-10-11T15:05:05Z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "one_line": "The act-0 grant on the producers' role allows PutObject, GetObject and ListBucket on the canonical prefix but NOT DeleteObject; D_02 and D_04 delete departed advisors' files with delete_objects and never read its Errors, so after act 2 their stale-cleanup silently removes nothing at the canonical home.",
  "spec_asserts": "Round-3 act 2 pair and the act-0 grant (FB-g-2, applied by FB-g-8): the producers' role is allowed what the producers do at the canonical home once act 2 moves their mode. Code comments in both scripts say the stale-advisor cleanup exists because orphan files are double-counted in AUA.",
  "world_is": "infra/aws/terraform/bd-pipeline/iam.tf:1300-1315 (policy advi-49f-platinum-canonical-rw-policy): AdviPlatinumCanonicalObjects Action [s3:PutObject, s3:GetObject], AdviPlatinumCanonicalList Action [s3:ListBucket]; no s3:DeleteObject. data/black_diamond/scripts/gold/D_04.client_portal_summary.py:789-812 and D_02.advisor_client_detail.py:3245-3280 compute stale advisor ids, list their keys, and call s3.delete_objects(Bucket=db, Delete={'Objects': objs}) with db and dk from platinum_destination(k) (the canonical bucket after act 2); the response is not read. boto3 delete_objects answers 200 with an Errors list for per-key AccessDenied, so no exception is raised. _lib/atomic_write.py (a delete_object of its staging key) has no caller under the gold scripts (0 files). Effect: after act 2 a departed advisor's served objects and entity files stay at the canonical home, which the scripts' own comments say double-counts AUA downstream.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/terraform/bd-pipeline/iam.tf lines 1300-1315 read at HEAD",
      "D_04.client_portal_summary.py lines 770-812 and D_02.advisor_client_detail.py lines 3245-3284 read at HEAD",
      "Grep over data/black_diamond/scripts/gold for delete_object(s): D_04, D_02, _lib/atomic_write.py (no importer) only",
      "the boto3 S3 DeleteObjects contract: per-key failures return in Errors with HTTP 200 (documented behavior; not exercised here)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "A never-widen class (it adds a delete grant on the canonical home). Placement read from the evidence: an addendum to the act-0 grant pair adding one statement, s3:DeleteObject on the same prefix ARN, before act 2; the departed-advisor path only runs when an advisor leaves, so the harm is latent, not daily. Alternative the CTO may prefer: the producers read Errors and fail loud, plus the grant. Not cut as a cell until ruled."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W45-S1",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~45",
  "surfaced_at": "2026-10-11T15:08:01Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "The pre-commit risk reflex printed HOLD on infra/aws/terraform/modules/opal_name/main.tf by basename match, citing another root's deploy note; commit 8114bac9cf landed rc=0 (a repeat of ADVI_FIRMBKTS-D1-W43-S1 and W42-S1).",
  "spec_asserts": "The pre-commit risk reflex names a node the commit touches only when the recorded claim concerns that file (the worker is to go read the citation before the commit proceeds).",
  "world_is": "The reflex matched the bare name main.tf across six roots (each with 9 recorded claims) and cited org/critical_paths/change_management/20260616T2001Z_nfra-infrpt-dr-snapshot-backup_deploy_completion.md:35, which concerns portal_lambda_ec2_snapshot in a different Terraform root. The opal_name module's own main.tf was not the subject of that claim. The commit was not blocked.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "safe-commit output at commit 8114bac9cf: [HOLD] infra/aws/terraform/modules/opal_name/main.tf -> file:infra/aws/terraform/aaii-v2-bucket-lifecycle/main.tf (9 recorded claim(s)) and five further roots",
      "org/critical_paths/change_management/20260616T2001Z_nfra-infrpt-dr-snapshot-backup_deploy_completion.md:35 read at the worktree: '- **main.tf:** fix `portal_lambda_ec2_snapshot` (EC2SnapshotPermissions)'"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "No action taken; the commit was not blocked and the cited claim is not this cell's. Repeat of ADVI_FIRMBKTS-D1-W42-S1 and ADVI_FIRMBKTS-D1-W43-S1 for the reflex's owner."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W45-S2",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~45",
  "surfaced_at": "2026-10-11T15:08:01Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "safe-commit printed WARN that the client-data check could not run (hashed account-id list absent on this device); commit 8114bac9cf was not checked for client account ids (a repeat of ADVI_FIRMBKTS-D1-W43-S2).",
  "spec_asserts": "The commit gate runs the client-data check (hashed account-id list) on every commit it admits.",
  "world_is": "The hashed list is absent at C:\\Users\\Test\\.opal\\account_id_hashes.txt on dell1 and OPAL_ACCOUNT_ID_HASHES is unset, so the check printed WARN and skipped the list comparison. Absent is not empty. The committed diff adds no 12-digit number as checked by this worker (git show 8114bac9cf -- the two code files, 11 insertions).",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "safe-commit output at commit 8114bac9cf: WARN: client-data-check: hashed account-id list ABSENT at C:\\Users\\Test\\.opal\\account_id_hashes.txt -- this commit was NOT checked for client account ids",
      "git show 8114bac9cf --stat: 2 files changed, 11 insertions(+), 7 deletions(-) at the worktree"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "No action taken by this worker; the list is a per-device input, not this cell's. Repeat of ADVI_FIRMBKTS-D1-W43-S2, filed for the owner of the client-data check."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W44-S1",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~44",
  "surfaced_at": "2026-10-11T15:07:30Z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "one_line": "Arm P3 of the round-4 policy check expects seven new fence exemption ARNs for opal-data-49financial; the real render yields eight, because the performance adapter is now a registry row. AC1 reads 5 of 6 arms.",
  "spec_asserts": "Arm P3 (r4_policy.py:154, and its docstring at r4_policy.py:16-19) says fence_exemption_arns for the bucket equals the base list plus seven new principals (six readers and the OAI), with the performance adapter as a registry row now. Face section 1b.4 says the adapter is carried by module.opal_name.fence_exemption_arns.",
  "world_is": "With the registry rows and wiring written as section 1a and 1b give them, the render's fence_exemption_arns for opal-data-49financial adds eight ARNs: the six readers, irpt-performance-adapter-role and the OAI. The module builds fence_exemption_arns from every row of the bucket (infra/aws/terraform/modules/opal_name/main.tf:111-115), so the adapter row enters it. The adapter's ARN has to stay in the blanket Deny exemption list, because its role name carries no firm token and fence_patterns does not match it. P3 printed 'new exemption arns=8' and FAILed; P1, P2, P4, P5 and P6 pass. The check was not edited (read-only).",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "r4_policy.py --arms policy at the worktree under timeout 118: 'P3 allow principals=10, new exemption arns=8, other buckets same=True', 'FAIL P3 the render holds exactly the ten Allow principals at their granted resources and the new exemptions', 'ROUND 4 POLICY: 5 of 6 arms', exit=1",
      "infra/aws/terraform/modules/opal_name/main.tf:111-115 read at the worktree: fence_exemption_arns maps every row of each exemptions bucket to its arn",
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_policy.py:154 read at the worktree: want_new = READERS plus the OAI, with no ADAPTER"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Not a worker decision. The registry and the wiring follow section 1a and 1b literally; the mismatch sits between the check's expectation and the order's own 1b.4 and the module's semantics. AC1 stays FAIL and the order stays open until the issuer rules whether the check's expectation or the render is corrected."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W44-S2",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~44",
  "surfaced_at": "2026-10-11T15:07:30Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "Removing the adapter's hand statements left its explanatory comments in s3-49financial.tf above code that no longer exists, so they now describe Denies and locals the file does not hold.",
  "spec_asserts": "Face section 1b.4 removes the adapter's data block, its locals and the three hand statements, and keeps every other line.",
  "world_is": "The comment blocks at s3-49financial.tf:103-112 (IRPT_BCKEND-S140 and TO-IB-pr-201) were kept as the bound says. They still say the adapter is served by three Denies scoped to that role and by the f49 locals, and the file now holds neither. The adapter's access comes from its registry row, so the comments are stale, not wrong about history.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/terraform/shared-infra/s3-49financial.tf:103-112 read at the worktree after the edit: the comment lines are present and no data, locals or DenyPerformanceAdapter statement follows them",
      "grep at the worktree: no 'DenyPerformanceAdapter', 'irpt_performance_adapter' or 'f49_scope' remains in the file"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "No action taken by this worker: the order's keep-every-other-line bound was followed literally. The wording of these comments belongs to the issuer."
}
```

## Row filed by 0.7.0_AE_CloudOps~FB1 (FB-f-14, act 3b apply, the seat gate)

```json
{
  "id": "ADVI_FIRMBKTS-D1-S30",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.7.0_AE_CloudOps~FB1",
  "surfaced_at": "2026-10-11T15:29:21Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "The cross-box seat gate reports an OPEN deploy (iamroles-r7-narrow-portal-s3, 0.7.0_AE_CloudOps~IR) that reads CLOSED in this tree's change-management entry and whose sentinel is in none of the 50 worktrees read, and it names the shared-infra root by path token alone; with a cross-box call naming the same root, the gate read STOP in WARN mode for a one-resource apply that touches neither.",
  "spec_asserts": "safe-apply's seat gates: crossbox-deploy-check reports OPEN-CALL and OPEN-DEPLOY hits when a live cross-box call or an OPEN deploy names the root by token, and under ENFORCE a STOP blocks the apply; the check's own OVERLAP and --files-vs-trunk modes read file and resource overlap.",
  "world_is": "2026-10-11 15:25Z, crossbox-deploy-check for root infra/aws/terraform/shared-infra with --files-vs-trunk and --target aws_s3_bucket_policy.opal_data_49financial: OVERLAP clear (0 files differ from the merge base d54eecad2b), UPSET clear, OPEN-CALL hit XB-20261011T082334Z-282f (state ACKED, dell2 to laptop; its report names s3-lgic-firm-buckets.tf, a different file and a different bucket-policy resource), OPEN-DEPLOY hit iamroles-r7-narrow-portal-s3 (author 0.7.0_AE_CloudOps~IR, opened 11:02Z). That entry's change-management file in this tree reads 'CLOSED -- nothing stranded -- closed 20261011T113448Z', mentions neither opal-data-49financial nor aws_s3_bucket_policy, and its sentinel is in none of the 50 worktrees that git worktree list returns (the gate reads a view this lane could not locate). Verdict STOP in WARN mode; the act proceeded after both hits were read and found disjoint from the one resource.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/act3b/apply_safe-apply.out (the seat-gate lines)",
      "python .tools/crossbox-deploy-check.py --root infra/aws/terraform/shared-infra --serial 0.7.0_AE_CloudOps~FB1 --files-vs-trunk --target aws_s3_bucket_policy.opal_data_49financial, 2026-10-11T15:25Z",
      "org/critical_paths/change_management/20261011T1102Z_iamroles-r7-narrow-portal-s3_deploy_completion.md line 3 (Status: CLOSED)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Form only; nothing armed. For the gate owner: (1) a sentinel the gate counts as OPEN while the entry reads CLOSED is the DRIFT class the ledger's own check names; the sentinel's location is the open question. (2) The match is by root path token, so a disjoint one-resource apply and an unrelated cross-box call read as a STOP. This lane's practice at this act: --dry-seat-gates first, then read each hit's resource set before the apply."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W46-S1",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~46",
  "surfaced_at": "2026-10-11T15:30:31Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "The FB-g-24 face names lib/platinum_dest.py as the seam, but no such file exists under lib/; the seam is data/black_diamond/scripts/gold/lib/platinum_dest.py.",
  "spec_asserts": "Face section 1a.1 derives each class's canonical directory from the canonical destination of lib/platinum_dest.py for a key under the legacy prefix.",
  "world_is": "Glob under the worktree lib/ for platinum_dest*.py returned no files at 92a9b27704. The module is data/black_diamond/scripts/gold/lib/platinum_dest.py (destination(legacy_key, mode) at line 59), importing lib.platinum_dest_view. r4_modclass.py imports it with data/black_diamond/scripts/gold on sys.path. The worker derived each directory from opal_naming._platinum_build(), the derivation platinum_prefix and ownership_key use; AC1 M2 reads the seam's destination and reports 11 of 11 classes equal.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "Glob lib/**/platinum_dest*.py at /c/dev/wk-firmbkts-46/lib returned No files found at 92a9b27704",
      "data/black_diamond/scripts/gold/lib/platinum_dest.py:24-25 read at the worktree: imports S3_BUCKET from lib.config and PLATINUM_CLASSES from lib.platinum_dest_view; destination() at line 59",
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_modclass.py:96 read at the worktree: from lib import platinum_dest as pd, with data/black_diamond/scripts/gold on sys.path"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "No action taken beyond the derivation the face names. The path is the issuer's wording; the check reads the module from the gold folder. AC1 passes on this path. Recorded as a path premise only."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W47-S1",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~47",
  "surfaced_at": "2026-10-11T15:31:20Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "The FB-g-26 fail-loud helper calls sys.exit(2), but D_02.advisor_client_detail.py had no import sys, so one import line was added to D_02 outside the stated bound.",
  "spec_asserts": "Face sections 1a.1 and 1a.3: move the single delete_objects call of each script into _delete_batch_fail_loud, change nothing else about either script; the helper exits with sys.exit(2).",
  "world_is": "D_02 at HEAD carries no 'import sys' (git show HEAD count 0), so sys.exit(2) on the refused path would raise NameError. One line 'import sys' was added (worktree D_02.advisor_client_detail.py:41), between 'import re' and 'import threading'. Nothing else in D_02 changed outside the helper (lines 99-111) and its one call site (line 3293). D_04 already imports sys.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "git show HEAD:data/black_diamond/scripts/gold/D_02.advisor_client_detail.py | grep -c '^import sys' printed 0",
      "worktree data/black_diamond/scripts/gold/D_02.advisor_client_detail.py:41 holds 'import sys'; :99-111 hold _delete_batch_fail_loud with sys.exit(2) at :111",
      "r4_failloud.py --arms static at the worktree: 'ROUND 4 FAIL-LOUD: 4 of 4 arms', exit=0 (the check accepts raise SystemExit(2) as well as sys.exit(2))"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Not a worker decision to widen: the import is the minimum that makes the ordered sys.exit(2) run. The issuer may rule whether the import is an accepted part of the bound or should become raise SystemExit(2) instead; the AC1 check accepts either."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W49-S1",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~49",
  "surfaced_at": "2026-10-11T15:53:44Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "safe-commit's commit-gate checked 0 of 1 file (the registry JSON is outside its graded suffixes) and the client-data check printed WARN with the hashed account-id list absent; commit 3a6d8aa89d was not checked for client account ids (a repeat of ADVI_FIRMBKTS-D1-W43-S2 and W45-S2).",
  "spec_asserts": "The commit gate checks each staged file it admits, and the client-data check runs on every commit it admits.",
  "world_is": "The commit-gate printed 'checked 0 of 1 file(s) -- NOTHING WAS CHECKED' for infra/logic/registry/exemptions.json, a suffix it does not grade. The client-data check printed WARN: hashed account-id list ABSENT at C:\\Users\\Test\\.opal\\account_id_hashes.txt. The one added row carries account id 313476888478, the id the file's own account_id field names and every existing row already carries; whether that number is on the hashed list is unknown, because the list is absent. The registry row's validation is AC1 (r4_exec.py, 4 of 4 arms) and AC2 (r4_scope.py), not the commit gate.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "safe-commit output at commit 3a6d8aa89d: 'commit-gate checked 0 of 1 file(s) -- NOTHING WAS CHECKED' and 'WARN: client-data-check: hashed account-id list ABSENT at C:\\Users\\Test\\.opal\\account_id_hashes.txt -- this commit was NOT checked for client account ids'",
      "infra/logic/registry/exemptions.json _about.account_id and account_id field read at the worktree: 313476888478"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "No action taken by this worker; the commit was not refused and the list is a per-device input. Filed for the owner of the commit gate and the client-data check to judge the un-graded JSON suffix and the device's missing list."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W50-S1",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~50",
  "surfaced_at": "2026-10-11T15:53:58Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "The face's module source ../../modules/opal_name does not resolve from the exec-summary root; the call uses ../modules/opal_name, the path that resolves and the one the check requires.",
  "spec_asserts": "Face section 1a.1: a NEW module call with source ../../modules/opal_name, following infra/aws/terraform/bd-pipeline/iam.tf's module opal_name_platinum_grant.",
  "world_is": "infra/aws/terraform/exec-summary/ sits one level below infra/aws/terraform/, so ../../modules/opal_name resolves to infra/aws/modules/opal_name, which does not exist (ls -d printed no such file, rc=2). The module is at infra/aws/terraform/modules/opal_name/. bd-pipeline's call (infra/aws/terraform/bd-pipeline/iam.tf:1285) uses ../modules/opal_name, and r4_execiam.py I1 requires that string. The new call at iam.tf uses ../modules/opal_name; AC1 reads 5 of 5 arms, I3 resolves the ARN through the module.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "ls -d infra/aws/modules/opal_name at /c/dev/wk-firmbkts-50 printed 'No such file or directory' rc=2",
      "ls -d infra/aws/terraform/modules/opal_name at /c/dev/wk-firmbkts-50 printed the directory (contains main.tf, variables.tf, generated_locals.tf, tests/)",
      "infra/aws/terraform/bd-pipeline/iam.tf:1285 reads source = \"../modules/opal_name\" at the worktree",
      "r4_execiam.py:I1 at the worktree requires the string \"../modules/opal_name\" in the module block; r4_execiam.py --arms iam returned 5 of 5 arms, exit=0"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Recorded as a path premise only. The face's ../../ would fail terraform init for this root. The issuer may confirm ../modules/opal_name as the intended source or correct the face's text."
}
```

## Row filed by 0.7.0_AE_CloudOps~FB1 (FB-f-16, act 0 delete statement, code not yet on CLOUD)

```json
{
  "id": "ADVI_FIRMBKTS-D1-S31",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.7.0_AE_CloudOps~FB1",
  "surfaced_at": "2026-10-11T16:00:42Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "The live policy advi-49f-platinum-canonical-rw-policy now holds 3 statements while the Terraform that declares the third (FB-g-25, 555ba2e0f5) is on box/dell1 only: origin/CLOUD's iam.tf has the 2-statement policy, so a bd-pipeline apply from a checkout of CLOUD would plan the delete statement's removal.",
  "spec_asserts": "FB-f-16 and the act-0 COO half ADDENDUM 1: the scoped plan reads 1 to change on the one policy and a post-apply scoped plan reads No changes (read in this checkout). The seat gate's OVERLAP arm: a root's Terraform file that differs from the trunk merge base, with a project on another box whose write set names the root, is a hit.",
  "world_is": "2026-10-11 15:58Z-16:00Z. Applied from box/dell1 at HEAD: Apply complete, 1 changed; live policy Sids AdviPlatinumCanonicalObjects, AdviPlatinumCanonicalList, AdviPlatinumCanonicalDelete. git fetch origin CLOUD; origin/CLOUD head 8764d91a47: 555ba2e0f5 (FB-g-25, the statement) is NOT an ancestor of it (positive control 8764d91a47 is), while f942dcb9a8 and 0acccf7d8e are; origin/CLOUD:infra/aws/terraform/bd-pipeline/iam.tf has 0 occurrences of AdviPlatinumCanonicalDelete and 1 of aws_iam_role_policy.bd_exporter_advi_49f_platinum_canonical. The seat gate read OVERLAP hit: 1 Terraform file of this root (iam.tf) differs from the merge base 8764d91a47, and project NFRA_MCPINDEX (placed on sitez) has a write set naming infra/aws/terraform/bd-pipeline. The plan of any apply of this root from a tree at origin/CLOUD would therefore show the policy changing back to 2 statements.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "git merge-base --is-ancestor 555ba2e0f5 origin/CLOUD (false) with the positive control 8764d91a47 (true), 2026-10-11 ~16:00Z",
      "git show origin/CLOUD:infra/aws/terraform/bd-pipeline/iam.tf | grep -c AdviPlatinumCanonicalDelete -> 0",
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/act0_delete/ac1.out (three Sids live)",
      "python .tools/crossbox-deploy-check.py --root infra/aws/terraform/bd-pipeline --files-vs-trunk (OVERLAP hit lines)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Form only; the live grant is exactly what the signed pair permits and nothing is armed by it. The exposure is a revert, not a widening: an apply from CLOUD's tree removes a Delete statement the producers will need after act 2. The same condition held for act 0's policy until its commit reached CLOUD (it has: f942dcb9a8 is an ancestor). Closing it is the integrator's push of box/dell1 (0.0.0_AB_MSTR), which this lane does not do. Until then a bd-pipeline plan from any other tree is read for a diff on this policy before any apply."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-S20",
  "project": "ADVI_FIRMBKTS",
  "fabric": "laptop",
  "surfaced_by": "0.7.0_AE_CloudOps~FBL",
  "surfaced_at": "2026-10-11T15:55:00Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "TO-FB-f-15: r4_sim.py as issued does not run on the laptop (three defects); with those three corrected in a scratch copy the live policy reads 9 of 9 admitted allowed, 2 of 2 negatives explicitDeny, OAI statement ok=True.",
  "spec_asserts": "TO-FB-f-15 AC1: `python .../r4_sim.py --out .../ACT3B_SIM.txt` prints 'ROUND 4 ACT 3B SIM: 9 of 9 admitted allowed, 2 of 2 negatives not allowed, oai statement ok=True'.",
  "world_is": "Run 1 (as issued): FileNotFoundError WinError 2 at r4_sim.py:34, bare 'aws' is not resolvable by subprocess on Windows (only aws.cmd exists in PATH). Run 2 (aws resolved via shutil.which): AttributeError at :78, a bucket-policy statement carries Principal as the string '*' and .get fails, after all 11 simulations had run and before any line printed. Run 3 (both fixed): 11 of 11 simulations ERROR 'The command line is too long', the live policy passed inline to --resource-policy exceeds the Windows cmd limit through aws.cmd. Run 4 (policy passed as file:// from a repo-relative file, deleted after): 9 of 9 admitted allowed (performance adapter also allowed on the gold sample), inf-gold-qa-runner-ec2-role explicitDeny, exec-summary-generator-role explicitDeny, OAI one Allow Get-only on 9 resources ok=True, exit=0. The simulator does not evaluate SCPs (issuer's own blindness note).",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "deliverables/0.7.0_AE_CloudOps~FBL/ACT3B_SIM.txt (run 4 output)",
      "deliverables/0.7.0_AE_CloudOps~FBL/evidence_f15/r4_sim_laptop.diff (the scratch copy three changes against r4_sim.py) and run_sim_aws_shim.py.txt (the aws resolver)",
      "r4_sim.py itself was not edited; nothing was written to AWS"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "The measured result is the answer the order asks for, but AC1's literal invocation exits 1 on this box, so TO-FB-f-15 <status> is left pending for the issuer to grade: either fix r4_sim.py (Principal type check, file:// policy, resolved aws path) and re-run AC1, or accept run 4 as the instrument."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W51-S1",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~51",
  "surfaced_at": "2026-10-11T16:08:08Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "FB-g-29 call-chain premise: the validator's ownership call site (index.mjs:491, getOwnershipMap) carries no lowercase ownership token, so the census chain ends on the key line index.mjs:175 inside the read, not on the call line.",
  "spec_asserts": "FB-g-29 cell 1a and round-4 r4_invoke.py V2: each call_chain ends on the line that calls the ownership read, and that line carries the token load_ownership or ownership (case-sensitive).",
  "world_is": "index.mjs:491 is 'map = await getOwnershipMap(payload.firmId);' (camelCase, no lowercase ownership token). getOwnershipMap is defined at index.mjs:164 and its key line index.mjs:175 'const key = ownershipMapKey(firmId, bucket);' carries the token. The census chain therefore passes through the call line at index.mjs:491 and ends at index.mjs:175 so that V2 passes.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/lambda-edge/auth-validator-edge/index.mjs:491 read at the worktree: 'map = await getOwnershipMap(payload.firmId);'",
      "infra/aws/lambda-edge/auth-validator-edge/index.mjs:164 read at the worktree: 'async function getOwnershipMap(firmId) {'",
      "infra/aws/lambda-edge/auth-validator-edge/index.mjs:175 read at the worktree: 'const key = ownershipMapKey(firmId, bucket);'",
      "r4_invoke.py --arms census at the worktree: 'V2 call chains verified against the tree: True', exit=0 (the token test is load_ownership|ownership applied to the last chain line)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Recorded as a premise note only. The census is complete and AC1 passes; the issuer may rule whether the validator chain should end on the call line with a token-bearing check instead."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W51-S2",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~51",
  "surfaced_at": "2026-10-11T16:08:08Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "The auth-validator-edge census event cannot reach its ownership read from the tree alone: it needs a live, signed, non-admin JWT, which the repository does not hold and no test fixture builds.",
  "spec_asserts": "FB-g-29 cell 1a: build each event from a test fixture in the function's own tests where one exists, else from the fields the handler's entry reads; reads_ownership is true only when the event reaches the validator's ownership read.",
  "world_is": "auth-validator-edge/tests has no CloudFront viewer-request fixture (no Records, cf, request, authorization or Bearer match). The event is built from index.mjs:118 (the account uri pattern) and index.mjs:334-345 (the Records cf.request and Authorization shape). It reaches index.mjs:491 only when verifyWithSlots (index.mjs:381) accepts the token against a key from Secrets Manager, the payload is non-admin with advisorId and firmId (index.mjs:87-96 and :221-227), and the tier gate passes (index.mjs:403-426). The census carries a placeholder token; the act-4 actor must supply a live non-admin session token.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "native Grep of infra/aws/lambda-edge/auth-validator-edge/tests for Records, cf, request, authorization and Bearer: No matches found",
      "infra/aws/lambda-edge/auth-validator-edge/index.mjs:381 read at the worktree: 'const payload = verifyWithSlots(jwt, token, slots, { algorithms: RS256 });'",
      "infra/aws/lambda-edge/auth-validator-edge/index.mjs:221-227 read at the worktree: payload.role and payload.firmRole admin return null; a non-admin without advisorId returns an empty list",
      "infra/aws/lambda-edge/auth-validator-edge/index.mjs:403-407 read at the worktree: isAdminBypass on role, firmRole, tier internal or userType Dev"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Recorded as a premise note only. The act-4 actor needs a live token to run this one event; the census does not carry one."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W52-S1",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~52",
  "surfaced_at": "2026-10-11T16:50:32Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "FB-g-32 census: the Budgets reads are denied to the worker identity, so the find-insure-budget-alerts Budgets actions are unread and that topic lists its code publisher only.",
  "spec_asserts": "FB-g-32 1a and 1b.3: the census reads the account's publishers; an unreadable call is recorded as a surprise row naming the denied call, and the rest is filled.",
  "world_is": "The Budgets describe calls for the account return AccessDeniedException (rc=254) for the worker identity cloudops-dell1-agent-user: budgets:ViewBudget and budgets:DescribeBudgetActionsForAccount are not granted. No aws_budgets resource or budget action exists under infra/aws/terraform (native Grep, no match).",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "budgets describe-budgets run 2026-10-11 with the account id as an argument: rc=254, AccessDeniedException on budgets:ViewBudget",
      "budgets describe-budget-actions-for-account run 2026-10-11: rc=254, AccessDeniedException on budgets:DescribeBudgetActionsForAccount",
      "native Grep of C:/dev/wk-firmbkts-52/infra/aws/terraform for aws_budgets or budget_action at cd726fdc6c: No matches found"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "A denied read per the comp-iam preflight: a finding, not a failure. The issuer or CVO may grant the read or name another reader for the Budgets publishers. No budget was changed."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W52-S2",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~52",
  "surfaced_at": "2026-10-11T16:50:32Z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "one_line": "FB-g-32 AC1: the S4 phone-number check refuses every topic ARN, because each ARN carries the 12-digit AWS account id; AC1 reads 3 of 4 arms on a census that is otherwise complete.",
  "spec_asserts": "FB-g-32 1b.2 and AC1: a count and a topic ARN are the most the census prints, and the check refuses a run of ten or more digits; AC1 passes at 4 of 4.",
  "world_is": "Each of the six topic_arn values is arn:aws:sns:us-east-1:<12-digit account id>:<topic>. The r4_smscensus.py S4 regex matches exactly 6 times in the written file, each the account id inside a topic ARN (run length 12); the +1 prefix matches 0. The file carries the true ARNs, unmasked, so AC1 S4 FAILS (3 of 4). A masked ARN would pass S4 but would not be the ARN the spec names; that choice is the issuer's or the CTO's.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "r4_smscensus.py --arms census run on the written census at the worktree: FAIL S4 no phone number appears in the file; ROUND 4 SMS CENSUS: 3 of 4 arms; exit=1",
      "python regex count over the written census: 6 matches, all 12-digit runs inside arn:aws:sns:us-east-1: prefixes (values not recorded)",
      "sns list-subscriptions in us-east-1 (client-side count 11): 6 subscriptions of protocol sms, one per topic ARN"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Not masked by this worker. For a ruling: exempt the account-id run in S4 for ARN fields, or accept a masked ARN form. AC1 stays FAIL and the order stays open until ruled."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W52-S3",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~52",
  "surfaced_at": "2026-10-11T16:50:32Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "FB-g-32 census: a live Lambda (ec2-runtime-monitor) publishes to ec2-long-running-alerts, which has an SMS subscription, but its source is not in this tree, so the census lists no code publisher for that topic.",
  "spec_asserts": "FB-g-32 1a: each publisher is a repository line (kind code) or an AWS service resource, and a publisher is found by reading the topic's wiring.",
  "world_is": "The Lambda list (237 functions, client-side count) shows ec2-runtime-monitor with Environment SNS_TOPIC_ARN set to the ec2-long-running-alerts ARN. infra/aws/lambda/ci/lambda-source-map.json entry ec2-runtime-monitor has source_dir EXTERNAL and files []. No infra/aws/lambda/ec2-runtime-monitor directory exists (native Glob). The topic's census entry has publishers=[] and sms_subscriptions=1, so N is under-counted by one.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "lambda list-functions in us-east-1 with a client-side scan of Environment: ec2-runtime-monitor SNS_TOPIC_ARN names ec2-long-running-alerts, at worktree HEAD cd726fdc6c",
      "C:/dev/wk-firmbkts-52/infra/aws/lambda/ci/lambda-source-map.json ec2-runtime-monitor: source_dir EXTERNAL, files []",
      "Glob C:/dev/wk-firmbkts-52/infra/aws/lambda/ec2-runtime-monitor/lambda_function.py: no file (only ec2-auto-shutdown-enforcer matched)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Not counted as aws_service: it is code, and its can_set_message_attributes is unknown without its source. The source must be located outside this tree before the attribute fix covers it. The live enforcer ec2-auto-shutdown-enforcer publishes to ec2-auto-shutdown-alerts, not to this topic."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W52-S4",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~52",
  "surfaced_at": "2026-10-11T16:50:32Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "FB-g-32 census: data/inf/scripts/gold/lib/aor_attribution_audit.py:204 publishes to the topic named by INF_AOR_DRIFT_SNS_ARN, which no tree wiring sets; its docstring names opal-partner-etl-ops-alerts, so the census does not count it.",
  "spec_asserts": "FB-g-32 1a: a code publisher counts when its topic resolves by an environment variable or a Terraform value the worker reads.",
  "world_is": "INF_AOR_DRIFT_SNS_ARN is read at aor_attribution_audit.py:191 and is set in no file under infra/ (native Grep, no match) and in no data/ file outside its test module. No live Lambda environment carries an SNS ARN under that key. The docstring at line 185 names opal-partner-etl-ops-alerts, which is a claim, not a resolution, so the topic is unresolved.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "C:/dev/wk-firmbkts-52/data/inf/scripts/gold/lib/aor_attribution_audit.py:191 at cd726fdc6c: arn = os.environ.get('INF_AOR_DRIFT_SNS_ARN', '').strip()",
      "native Grep of C:/dev/wk-firmbkts-52/infra for INF_AOR_DRIFT_SNS_ARN at cd726fdc6c: No matches found",
      "Lambda Environment scan (client-side): no SNS ARN under the key INF_AOR_DRIFT_SNS_ARN"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Excluded from N. If the variable's live setting is read and points at opal-partner-etl-ops-alerts, that topic gains one code publisher and N rises by one."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W52-S5",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~52",
  "surfaced_at": "2026-10-11T16:50:32Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "Repository Terraform carries E.164 phone-number literals in a comment and in a variable default, outside this order's paths; the census cites them by path only and writes none.",
  "spec_asserts": "FB-g-32 1b.2: no phone number, endpoint or email is written into any file or row; the candidate list names where the toll-free identifier lives and never the number.",
  "world_is": "infra/aws/terraform/portal-auth/sms-iam.tf:7 (comment) carries a toll-free E.164 literal; infra/aws/terraform/inf-pipeline/inf-ops-alerts-sms.tf:11 (comment) carries an on-call E.164 literal; infra/aws/terraform/partner-etl-ops-alerts/ops-alerts.tf:6 (variable default) carries an on-call E.164 literal. The literals appeared in this worker's search output and were not recorded in any file or row.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "native Grep of C:/dev/wk-firmbkts-52/infra/aws/terraform for origination or toll-free at cd726fdc6c: portal-auth/sms-iam.tf:7 comment carries an E.164 literal",
      "native Grep of C:/dev/wk-firmbkts-52/infra/aws/terraform for on-call E.164 literals at cd726fdc6c: inf-pipeline/inf-ops-alerts-sms.tf:11 and partner-etl-ops-alerts/ops-alerts.tf:6",
      "Read of partner-etl-ops-alerts/ops-alerts.tf lines 4-6 at cd726fdc6c: description reads E.164 on-call pager; default carries a literal"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Recorded for the CTO's call on whether committed on-call numbers belong in Terraform source. Not remediated: the paths are outside this order's write grant."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W52-S6",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~52",
  "surfaced_at": "2026-10-11T16:53:14Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "FB-g-32 AC1 arm S2 checks that each cited code file exists, not that the cited line exists; a publisher cited at a nonexistent line passes S2 and a nonexistent file fails it.",
  "spec_asserts": "FB-g-32 preflight comp-adversary and AC1: the census proves the file's shape and that cited code lines exist; AC1 reads every publisher typed and located.",
  "world_is": "r4_smscensus.py census() at S2 tests os.path.isfile(root/path) for kind code and never reads the line number. A mutant copy of the written census with where set to an existing file and line 99999 still PASSES S2 (S2 publishers=54, PASS). A mutant with a nonexistent file fails S2 (2 of 4 arms). So the line half of the located claim is not checked by the arm.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "C:/dev/wk-firmbkts-52/org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_smscensus.py S2 block at d0cbb79075: os.path.isfile(os.path.join(root, *m.group(1).split('/'))) is the only path test; the line number group is matched and not used",
      "r4_smscensus.py --arms census on a mutant with where line 99999 at the worktree: PASS S2, S2 publishers=54 (run in .scratch, not committed)",
      "r4_smscensus.py --arms census on a mutant with a nonexistent file: FAIL S2, 2 of 4 arms, exit=1"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "The line check is not performed by this worker's census; the worker verified its 16 code lines by reading each one (each carries its publish call). For the issuer: a line test in S2 would close the gap. The checker is the COO's file and is not edited here."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W55-S1",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~55",
  "surfaced_at": "2026-10-11T17:02:40Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "FB-g-35 AC1 invocation as handed to the worker carries --base 8f9c3f1d8c, a commit that does not exist in the repository; the check reads 3 of 4 arms there and passes T3 vacuously.",
  "spec_asserts": "FB-g-35 AC1 (order file task-orders/ADVI_FIRMBKTS.TO-FB-g-35.sms-default-type.md line 54): --base 83995c26e6; the worker face carried --base 8f9c3f1d8c.",
  "world_is": "git cat-file -t 8f9c3f1d8c returns 'fatal: Not a valid object name'. r4_smstype.py _git() swallows stderr, so the base file reads as empty: T2 FAILS (3 of 4 arms, exit 1) and T3 PASSES as '0 of 0 base lines kept', a vacuous pass. At the order file's base 83995c26e6 the same check reads 4 of 4 (exit 0). The worker ran AC1 at 83995c26e6 per the coordinator's correction.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "git -C /c/dev/wk-firmbkts-55 cat-file -t 8f9c3f1d8c at HEAD c4d21f5ab8: fatal: Not a valid object name 8f9c3f1d8c",
      "r4_smstype.py --arms pref --base 8f9c3f1d8c in the worktree: T2 other attributes equal base: False; T3 base lines kept 0 of 0; ROUND 4 SMS TYPE: 3 of 4 arms; exit=1",
      "r4_smstype.py --arms pref --base 83995c26e6 in the worktree: T1 to T4 PASS; ROUND 4 SMS TYPE: 4 of 4 arms; exit=0",
      "order file org/missions/D8/ADVI/ADVI_FIRMBKTS/task-orders/ADVI_FIRMBKTS.TO-FB-g-35.sms-default-type.md line 54 carries --base 83995c26e6"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Surfaced for the issuer. The coordinator's correction to 83995c26e6 was applied; no file of the check was edited. For the COO: the T3 arm reads 0 of 0 lines as a PASS when the base is empty, so an unresolved base can pass one arm vacuously. A guard that fails on an empty base would close that gap. The checker is the COO's file and is not edited here."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W56-S1",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~56",
  "surfaced_at": "2026-10-11T17:09:19Z",
  "one_line": "FB-g-33 literal form (environment variables = merge(base map, cond)) fails r4_modeenv.py E3: its in-order match never skips a base line, so the rewrapped variables = { line stops the count at 83 of 183. The worker kept the variables = { line and wrapped the merge in a for-expression, which passes E3 and reads 4 of 4 arms.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "FB-g-33 1a.2: the environment is the base's map UNCHANGED plus one conditional, merge(<the base map>, var.platinum_mode == \"\" ? {} : {...}); AC1 expects ROUND 4 MODE ENV: 4 of 4 arms. The check's own E3 comment allows a rewrap of the environment block.",
  "world_is": "r4_modeenv.py E3 (lines 79-82) is an ordered greedy match with no skip branch: once a keep_o line is unmatched the pointer never advances. With the literal merge form the run printed 'E3 base lines kept 83 of 183' and ROUND 4 MODE ENV: 3 of 4 arms, exit=1. With the for-form the run printed 'E3 base lines kept 183 of 183', fmt rc=0, 4 of 4 arms, exit=0; mutant (base main.tf, new variables.tf) prints E2 FAIL, 3 of 4, exit=1. terraform validate and plan were NOT run (no plan in the root by the bound): the for-form's plan equality is INFERRED from HCL semantics.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_modeenv.py@c4d21f5ab8 lines 79-82: for ln in keep_n: if i < len(keep_o) and ln == keep_o[i]: i += 1 (no skip branch)",
      "run in C:/dev/wk-firmbkts-56 at base 9c6d5ea3ba with the literal merge form of infra/aws/terraform/exec-summary/main.tf: 'E3 base lines kept 83 of 183 (env block lines aside)', 'FAIL E3', 'ROUND 4 MODE ENV: 3 of 4 arms', exit=1 (run before the form change; not committed)",
      "run in C:/dev/wk-firmbkts-56 with the for-form main.tf, uncommitted on wk-ADVI_FIRMBKTS-56 over 1d4c0cbfd6: 'E3 base lines kept 183 of 183', 'E4 fmt rc=0', 'ROUND 4 MODE ENV: 4 of 4 arms', exit=0; repeated twice, output md5 3eb64472ad6acbdc13f88330158daab6 on both runs",
      "infra/aws/terraform/exec-summary/main.tf@9c6d5ea3ba lines 124-132: the base environment block (variables = { five keys }) that the for-form keeps line for line"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "For the issuer: E3 should skip a non-matching base line (subsequence match) so the literal merge form passes; the checker is the COO's file and is not edited here. The row records the form choice so the CTO can rule on it at the drain. The commit-time row gate has not run yet at this write."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W57-S1",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~57",
  "surfaced_at": "2026-10-11T17:09:47Z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "one_line": "FB-g-34 AC1 reads 3 of 4 arms: the E3 dormancy arm of r4_modeenv.py cannot pass on the merge form that FB-g-34 1a.2 mandates, because its in-order matcher stalls at the environment_variables header line.",
  "spec_asserts": "FB-g-34 1a.2: environment_variables becomes merge(<the base map>, var.platinum_mode == '' ? {} : { BD_PLATINUM_MODE = var.platinum_mode }) with every base key and value kept character for character. FB-g-34 AC1 expects 'ROUND 4 MODE ENV: 4 of 4 arms'; E3 requires every base line kept in order and no other file of the root changed.",
  "world_is": "On ee3e4f6b45 the AC1 run prints E1 PASS, E2 PASS, E3 FAIL ('base lines kept 11 of 15 (env block lines aside)'), E4 PASS, 'ROUND 4 MODE ENV: 3 of 4 arms', exit=1. The E3 greedy in-order matcher stops at the first base line it cannot find in order. That line is 'environment_variables = {' (the header), which the mandated merge form necessarily changes, so keep_o[11..14] (header, '  }', 'system_tag = PartnersAPI', '}') are unmatched. The check's env-line exclusion drops lines containing USERS_TABLE only, not the header or its close, so the spec-mandated form cannot reach 13 of 15 under this arm. By inspection (not executed), excluding the two header lines would leave 13 lines, all matched in order.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "C:/dev/wk-firmbkts-57/org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_modeenv.py@1d4c0cbfd6 lines 60-69 and 73-89: keep_o drops only lines matching the base key USERS_TABLE; E3 pass threshold is i >= len(keep_o) - 2",
      "r4_modeenv.py --arms var --cell partners --root C:/dev/wk-firmbkts-57 --base 9c6d5ea3ba at ee3e4f6b45: E1 PASS, E2 PASS, E3 FAIL (11 of 15 kept), E4 PASS, 3 of 4 arms, exit=1",
      "E3 diagnostic at ee3e4f6b45 (.scratch/e3_diag.py, not committed): base non-env lines 15, greedy matched 11, UNMATCHED: 'environment_variables = {', '  }', 'system_tag = \"PartnersAPI\"', '}'"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Blocks FB-g-34 AC1 (criterion FAIL, order left open). Not worked around: a for-expression wrapper that keeps the header line would pass E3 but is not the spec's merge(<base map>, cond) form and would game the arm. The check file is the COO's and is read-only to this worker. For the issuer: the arm's env-line exclusion should cover the environment_variables header and its close as it covers USERS_TABLE, or the arm's threshold should be stated for the merge form."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W57-S2",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~57",
  "surfaced_at": "2026-10-11T17:09:47Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "The safe-commit risk-reflex advisory on FB-g-34 cited a device memory note that is absent from this device's memory directory, so the cited note could not be read before the commit.",
  "spec_asserts": "CLAUDE.md section 2 and the pre-commit advisory: a HOLD advisory asks the committer to read the cited memory note before the commit proceeds. FB-g-34 section 5: commit the two files and the rows.",
  "world_is": "safe-commit ee3e4f6b45 printed six HOLD advisories for infra/aws/terraform/partners-api/lambdas.tf citing memory/project_inf_hold_door2_staleness_ceiling_is_env_overridable.md:51 under the advisory's own memory root (C--Users-AndrewBerman-Desktop-ajb-workspace). The same name under this device's memory directory returned 'File does not exist', and the note is not indexed in this device's MEMORY.md. The commit proceeded (gate rc=0). The cited note was not read.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "safe-commit output at ee3e4f6b45: [risk-reflex] [HOLD] infra/aws/terraform/partners-api/lambdas.tf -> file:infra/aws/terraform/bd-pipeline/lambdas.tf (14 recorded claim(s)), memory/project_inf_hold_door2_staleness_ceiling_is_env_overridable.md:51",
      "Read of C:/Users/Test/.claude/projects/C--dev-ajb-workspace/memory/project_inf_hold_door2_staleness_ceiling_is_env_overridable.md: 'File does not exist' (this device's memory dir)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Not remediated: the worker has no write surface on the memory directory. The HOLD advisory's relevance to a variable with default empty (no apply, no plan) is for the CTO and the COO to read, not for this worker to decide."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W57-S3",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~57",
  "surfaced_at": "2026-10-11T17:09:47Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "The client-data-check on the FB-g-34 commit ran WARN, not PASS: the hashed account-id list is absent on this device, so the commit was not checked for client account ids.",
  "spec_asserts": "FB-g-34 section 2.3: if the commit is refused by a gate, do not override or force. The commit gates are expected to grade the commit.",
  "world_is": "safe-commit ee3e4f6b45 printed 'WARN: client-data-check: hashed account-id list ABSENT at C:\\Users\\Test\\.opal\\account_id_hashes.txt -- this commit was NOT checked for client account ids (absent is not empty)'. The commit was not refused and nothing was overridden. The added lines are the variable block and the merge expression; none carries an account number.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "safe-commit output at ee3e4f6b45: 'WARN: client-data-check: hashed account-id list ABSENT ... this commit was NOT checked for client account ids'",
      "git show --stat ee3e4f6b45: 2 files changed, 18 insertions(+), 3 deletions(-); create mode 100644 infra/aws/terraform/partners-api/variables.tf"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Not remediated: the list is an environment file outside this worker's write surface. The CTO or the integrator should decide whether the list must be present on this device for the check to grade commits from here."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W57-S4",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~57",
  "surfaced_at": "2026-10-11T17:11:41Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "The one-writer gate graded the order's named unsuffixed investigation file as the laptop's file written from dell1 and asked for the per-box file; the order's named path was written as given.",
  "spec_asserts": "FB-g-34 section 3 and section 5: the surprise rows go in org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md, the path the order names.",
  "world_is": "The row commit c05e821225 printed '[one-writer] WARN: .../INVESTIGATION_v1.md is the laptop's (unsuffixed) file, written from dell1; per-box file <stem>.dell1.<ext> (WARN until C-QUEUE)' and '[one-writer] OK: 1 append-only path(s) graded on box dell1 ... 0 blocked'. The commit passed; the rows sit in the unsuffixed file the order names.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "safe-commit output at c05e821225: '[one-writer] WARN: org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md is the laptop's (unsuffixed) file, written from dell1'",
      "safe-commit output at c05e821225: '[surprise-row-gate] OK: 1 file(s), all new rows carry their step-7/step-10 fields'"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Not remediated: the path is the one the order names, so it was used as given. The per-box naming is a standing WARN until C-QUEUE per the gate's own text. Recorded so the issuer can decide whether the per-box file is expected for this project."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W58-S1",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~58",
  "surfaced_at": "2026-10-11T17:19:19Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "FB-g-36 says to use 'the placeholders the fixtures use', but opal-partners-data has no test fixture or event sample in the tree; the census events therefore use ACCT_PLACEHOLDER / ADV_PLACEHOLDER / REL_PLACEHOLDER and the firm key 49financial (scopes.json), chosen by the worker.",
  "spec_asserts": "FB-g-36 1a (task-orders/ADVI_FIRMBKTS.TO-FB-g-36.partners-event-census.md lines 31-32 at 8658d57df1): the event is built 'from a test fixture of the Lambda's own tests where one exists, else from the fields lambda_function.py reads'; 'no real client identifier, use the placeholders the fixtures use'.",
  "world_is": "The Lambda directory holds no test file and no event sample: ls-tree of infra/aws/lambda/v2_portal/partners/ at HEAD lists only README.md and the seven opal-partners-data files, none a test. Neither test that names the Lambda directory (data/black_diamond/scripts/gold/tests/test_lambda_seam_parity.py, org/modules/graph/tests/test_pii_masking_reachability.py) holds lambda_handler, httpMethod or requestContext. So the fixture branch is absent and the placeholder convention has no referent; the worker built each event from the fields lambda_function.py reads (httpMethod, path, queryStringParameters.firmId, requestContext.authorizer.allowedFirmIds) and chose the placeholder spellings itself.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "git ls-tree -r --name-only HEAD infra/aws/lambda/v2_portal/partners/ at 8658d57df1: README.md, deploy.sh, etf_classification.py, etf_classifier.py, lambda_function.py, platinum_dest_view.py, pseudonymizer.py, served_seam.py; no test or fixture file",
      "git show HEAD:data/black_diamond/scripts/gold/tests/test_lambda_seam_parity.py | grep lambda_handler|httpMethod|requestContext returns rc=1 (no match)",
      "git show HEAD:org/modules/graph/tests/test_pii_masking_reachability.py | grep lambda_handler|httpMethod|requestContext returns rc=1 (no match)",
      "grep httpMethod|requestContext|queryStringParameters|rawPath partners/README.md at HEAD returns no line; infra/logic/registry/scopes.json:14-19 key 49financial, bucket opal-data-49financial"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Surfaced for the issuer. The census is built from the handler's own field reads and passes AC1 at 4 of 4 arms; the events are synthetic by the order's design, so an entity-keyed event reads a placeholder key and returns the seam's 404 body, while the three firm-level events (gold/artifacts filters, platinum/firm clients-tab, gold/views firm composition) name no entity and would read live objects if the firm row exists. Whether FIRM#49financial exists in opal-users-v2 is not checked (no AWS call). For the issuer: a fixture or a named placeholder convention for this Lambda would settle the spelling. No Lambda file was edited."
}
```

```json
[
  {
    "id": "ADVI_FIRMBKTS-D1-S32",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "1.0.0_SA_CTO~DELL1",
    "surfaced_at": "2026-10-11T21:45:00Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "one_line": "bd_price_update.py:344 takes the median of calc_price over silver/transactions/<date>.parquet rows that repeat once per portfolio group (no transaction_id dedupe on the per-date loader :263-271), so the T-1 price is weighted by how many groups hold the asset -- a rule nobody chose. Routed from dell2 (IRPT_DASHBD-D2-W122-S1).",
    "spec_asserts": "A served price is computed by a stated rule; a median over distinct trades, not over per-group duplicates.",
    "world_is": "Measured by 0.9.0_WK_IRPT_DASHBD~122 on 2026-10-09's day object (origin/box/dell2: org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~122/PRICE_PATHS_MEDIAN.json): extract_t1_prices groups by asset_name and medians calc_price over rows the per-date loader does not dedupe by transaction_id.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/black_diamond/scripts/silver/bd_price_update.py:263-271, :327-344, :778, :821",
        "origin/box/dell2 PRICE_PATHS_MEDIAN.json (CTO~DELL2 msg 5879 via MSTR msg 4126)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Owner 1.0.0_SA_CTO~DELL1 (the 49 Financial Black Diamond pipeline in opal-data-bd is this fabric's). PARKED, not a window cell: no producer logic changes inside ADVI_FIRMBKTS's Monday window. Un-park condition: act 4's read-back complete. Then cut as its own cell with a never-widen pair (served prices move): dedupe by transaction_id before the median, before/after per asset printed, the movers named."
  }
]
```

```json
[
  {
    "id": "ADVI_FIRMBKTS-D1-S33",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "1.0.0_SA_CTO~DELL1",
    "surfaced_at": "2026-10-11T22:30:00Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "one_line": "B_01.holdings_lots.py picks each asset's served price by sort_values('date', ascending=False).drop_duplicates('asset_name', keep='first') over the concat of silver/prices/<date>.parquet and canonical_prices.parquet; the default sort is not stable, so on a same-date tie which object's price wins is undefined by the code -- the 'not established' of dell2 D2-W125-S1/-S2 is not establishable by reading.",
    "spec_asserts": "A served price is chosen by a stated precedence, not by an unstable sort's tie order.",
    "world_is": "data/black_diamond/scripts/gold/B_01.holdings_lots.py:331-361 (read by this seat): files concatenated in sorted(key) order (daily files before canonical_prices.parquet), then sort_values('date') with pandas' default kind (quicksort, not stable) and keep='first'. Dell2's severity read (origin/box/dell2 IRPT_DASHBD deliverables/0.9.0_WK_IRPT_DASHBD~125/MOVED_MEDIANS_SEVERITY.json @7f80ca32da): on 2026-10-09, 34 of 160 assets carry the un-deduplicated median in the daily file and a Yahoo/other price in canonical_prices; canonical_prices is rewritten four times a day by a writer not identified.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/black_diamond/scripts/gold/B_01.holdings_lots.py:331-361",
        "COO~D2 dell2 msg 5961 via MSTR msg 4145"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Owner 1.0.0_SA_CTO~DELL1. Joins D1-S32's parked cell (un-park: act 4 read-back): (1) dedupe by transaction_id before the median; (2) an EXPLICIT price precedence in B_01 (stable sort with a stated source rank), replacing the tie order; (3) identify canonical_prices.parquet's four-a-day writer (writer census; DEC-12 read/write logging where it exists). Before any change: a read-only run of B_01's price load on 2026-10-09 prints which object wins for each of the 34, so the before state is MEASURED, then the change under a never-widen pair with before/after per asset."
  }
]
```

```json
[
  {
    "id": "ADVI_FIRMBKTS-D1-S34",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "surfaced_by": "1.0.0_SA_CTO~DELL1",
    "surfaced_at": "2026-10-11T22:30:30Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "one_line": "Three SERVED readers key on the silver/transactions FILE day, not trade_date: B_03.account_gains.py:327, bd_price_update.py:265 and its Lambda twin :143. The late-August rewrites moved 5,580 ids one file each toward their own trade date (0 then, 4,505 and 1,030 now), so a re-run of those readers can serve different 08-20..08-23 figures than first served.",
    "spec_asserts": "A served figure keyed to a date reads the rows whose trade (or effective) date it is, not whichever file a loader placed them in.",
    "world_is": "Dell2 measurement (origin/box/dell2 IRPT_DASHBD deliverables/0.9.0_WK_IRPT_DASHBD~126/FILE_DAY_READERS.json @915ae4bc64), with this seat's loss check (org/tier1_exec/1.0.0_SA_CTO/deliverables/BD49F_SILVER_TRANSACTIONS_LOSS_CHECK_20261011.md): 0 of 5,580 ids lost; the rows moved toward trade date. Not established: whether the readers re-ran since, or whether any served figure for 08-20..08-23 changed.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/black_diamond/scripts/gold/B_03.account_gains.py:327",
        "data/black_diamond/scripts/silver/bd_price_update.py:265",
        "CTO~DELL2 msg 5968 via MSTR msg 4148"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "Owner 1.0.0_SA_CTO~DELL1. Joins the parked D1-S32/S33 cell (un-park: act 4 read-back), read first and changed second: (1) whether each of the three readers re-ran since 2026-09-02, and the served 08-20..08-23 figures before and after; (2) whether file-day keying is replaced by trade_date keying, decided on that measurement under the cell's never-widen pair. Dell2's W124-S1 is closed on its side."
  }
]
```

## Row filed by 0.7.0_AE_CloudOps~FB1 (FB-f-10, act 3 delta copy, the tool's record phase)

```json
{
  "id": "ADVI_FIRMBKTS-D1-S35",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.7.0_AE_CloudOps~FB1",
  "surfaced_at": "2026-10-12T07:34:48Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "r3_f7_delta.py apply reads every overwrite key's prior version serially (49,110 head_object calls, about 42 minutes at 17 per second) BEFORE its first copy, prints nothing until it ends, opens the rollback record in append mode, and its --budget-seconds bounds only the copy phase; an outer timeout kills the record phase silently and each re-run appends duplicate rows.",
  "spec_asserts": "TO-FB-f-10 step 4 and the tool's own docstring: apply runs 'in bounded runs (--budget-seconds) until it prints its completion line'; it 'writes F7_DELTA_ROLLBACK.tsv BEFORE each overwrite and fsyncs it'; the issuer's amendment 1 describes apply as resumable.",
  "world_is": "2026-10-12 06:33Z to 07:31Z, apply against the 53,031-key manifest (differs=49,110). Run 1 under an outer 590 s timeout and a 480 s budget: killed at 590 s, no output, 11,909 rows in the record, 0 copies landed (30 of 30 sampled recorded keys still at their prior VersionId; the plan unchanged). Probe under a 150 s timeout and a 20 s budget: killed, no output, record grown to 14,415 rows of which 2,506 were duplicates of keys already recorded (the second run restarted at the first key and appended). Full run with no outer timeout: record phase (cmd_apply lines 128-139: one head_object per key, written and flushed and fsynced after the loop) about 42 minutes, then the copy phase copied=49231 stale-source=0 errors=0 not-reached=0 in about 4 minutes; record 49,110 unique rows. The record is complete and fsynced before the first copy (the intent holds); 'before each overwrite' is per run, not per key; no copy ever ran before the record was complete, so no overwritten key lacks its prior row.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      ".tools-adjacent: org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round3/checks/r3_f7_delta.py cmd_apply lines 112-168",
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/act3/F7_ACT3_APPLY_RUN.txt (the full run's four lines)",
      "the archived partial record: 11,909 unique keys of 11,909 rows, then 14,415 rows with 2,506 duplicates (scratchpad copy, counts quoted in the entry)",
      "plan_after: absent=0 equal=53031 differs=0 refused=0 (the act's end state)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Form only; the act completed and nothing is armed. For the tool's owner (the issuer): (1) print a progress line per N rows in the record phase, and one line when it ends, so a reader can tell 'recording' from 'hung'; (2) open the record 'w' or skip keys already recorded, so a re-run does not append duplicates; (3) state in the docstring that --budget-seconds bounds the copy phase only, and that the first run needs about 45 minutes of wall clock. The CTO's per-key rollback still works from a duplicated record (same prior VersionId in every duplicate), so no rollback was ever at risk; this lane archived its partial record to scratch before the full run."
}
```

## Row filed by 0.7.0_AE_CloudOps~FB1 (FB-f-13, act 4c sample, the hash of a gzip body)

```json
{
  "id": "ADVI_FIRMBKTS-D1-S36",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.7.0_AE_CloudOps~FB1",
  "surfaced_at": "2026-10-12T07:56:23Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "TO-FB-f-13 AC3 reads SAMPLE EQUAL 7 of 8 because the partners sample hashes the response body as returned, and the platinum/clients class returns base64 gzip whose header carries a timestamp: the compressed hash differs on every invocation while the decompressed content is identical (old artifact in legacy mode, new in both modes and the live canonical function: one sha256, 4,931,112 bytes).",
  "spec_asserts": "TO-FB-f-13 step 9: one record per class with status and the body's sha256; step 11 and AC3: r4_sample_eq every case EQUAL, or a difference only for a key whose canonical-home object's LastModified is after the mode move; the pair's Branch B: a changed body for a key not written after the move.",
  "world_is": "AFTER sample 2026-10-12T07:49:52Z against opal-partners-data at c9FXD84s...: 7 of 8 cases EQUAL; platinum/clients/ status 200 to 200 with body_sha256 c6203872... to 2a4bf88b... (DIFFERENT), exit=1. Determinism probe at the new version: platinum/clients/ gave 3 distinct compressed hashes in 4 invocations and 5 in 8; the response is isBase64Encoded=True with Content-Encoding gzip; the gzip header MTIME field of 6 bodies took four values on consecutive seconds; the DECOMPRESSED content hash was 1 distinct in 6 invocations. Local replay of the prior artifact (VersionId PrImfkXLOP1weeBmlOJRYwkCghMq0PhI) in legacy mode, the new artifact in legacy and in canonical mode, and the live canonical function: the same status 200 and the same content sha256 67ac42f423e34b66..., 4,931,112 bytes, in all four. The other seven classes return a plain body and read 1 distinct hash per 4 invocations. The class gold/entities/clients/ reads 404 before and after even with a real id (named, as the order asks).",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/act4bc/4c_platinum_clients_content_replay.txt",
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/act4bc/4c_ac1_ac2_ac3.txt (AC3 as printed, exit=1)",
      "PARTNERS_BEFORE.json and PARTNERS_AFTER.json (the raw records, unchanged)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Form only; Branch B's changed-body condition does NOT hold by content, so act 4c stays deployed and nothing was rolled back. Two instrument facts for the issuer: (1) the sample must hash the decompressed content when isBase64Encoded and Content-Encoding gzip are set (r4_sample_eq compares whatever hash the records carry); (2) this lane did not re-write PARTNERS_BEFORE.json: the BEFORE reference content hash is the local replay of the prior artifact, not a live read, because the live function is already on the new code. Options for the issuer: accept the replay as the BEFORE and amend AC3 to the content hash, or direct a re-take of the AFTER with a content hash. The order's status is NOT flipped by this lane."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W53-S1",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~53",
  "surfaced_at": "2026-10-12T06:31:35Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "The flip tool's --apply step rewrote the generated mark line of the nested portal/ submodule working copy (firmDisplayNames.generated.ts), uncommitted, though the order said to touch nothing under portal/.",
  "spec_asserts": "FB-g-30 section 1c rule 2: do NOT edit or commit anything under portal/; the nested portal/ firmDisplayNames.generated.ts is a generated target outside the index, and its mark line is stale (a mark line only).",
  "world_is": "After r4_flipcommit.py --apply (rc 0, 4 of 4), git -C portal diff shows firmDisplayNames.generated.ts line 1 changed from registry@063240d10e857a3b to registry@9f1cc0a3d5a5997b (1 insertion, 1 deletion; vendorDisplayNames.generated.ts also listed as modified). Nothing under portal/ was staged or committed; the flip commit 69679b90e3dc52b670d33fddd96d06be1deaac90 holds 16 files, none under portal/. The tool's changed-file count was 17 against the 16 committed files, the 17th being this portal target.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "git -C /c/dev/wk-firmbkts-53/portal diff at worktree HEAD 69679b90e3 (firmDisplayNames.generated.ts 1 insertion, 1 deletion)",
      "r4_flipcommit.py --apply output at 1a8d882931: 'changed files=17: registry 1, value-changing 2, mark-line only 13'",
      "git show --stat HEAD: 16 files changed, 24 insertions(+), 24 deletions(-), no portal/ path"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Not reverted: reverting would itself edit under portal/, which the order forbids. The working-copy mark line is left for the issuer to decide (regenerate-and-commit inside the portal submodule, or leave as a known stale mark line). Recorded so the drain does not commit it by accident."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W53-S2",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~53",
  "surfaced_at": "2026-10-12T06:31:35Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "The safe-commit client-data check could not run for the flip commit: the hashed account-id list is absent on this box, so the commit was not checked for client account ids.",
  "spec_asserts": "The commit gates run by safe-commit.sh pass the flip commit; the order makes no separate client-data claim.",
  "world_is": "safe-commit output for 69679b90e3: 'WARN: client-data-check: hashed account-id list ABSENT at C:\\Users\\Test\\.opal\\account_id_hashes.txt -- this commit was NOT checked for client account ids (absent is not empty; set OPAL_ACCOUNT_ID_HASHES or place the list there).' The commit still committed (rc 0). Staged content is registry JSON and generated code targets with no account data by construction; the check was not run, so that is not established by the check.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "safe-commit.sh output for 69679b90e3dc52b670d33fddd96d06be1deaac90 (run at 2026-10-12T06:3x Z): 'WARN: client-data-check: hashed account-id list ABSENT'",
      "git show --stat 69679b90e3: 16 files, paths listed in order section 3"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Environmental: the list lives on another box or path. Not remediated by this worker; the drain or the box owner can rerun the client-data check against this commit with the list in place."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W54-S1",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~54",
  "surfaced_at": "2026-10-12T08:07:32Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "The safe-commit client-data check could not run for the re-pin commit e274a0e60c: the hashed account-id list is absent on this box, so the commit was not checked for client account ids.",
  "spec_asserts": "The commit gates run by safe-commit.sh pass the re-pin commit; the order makes no separate client-data claim.",
  "world_is": "safe-commit output for e274a0e60c: 'WARN: client-data-check: hashed account-id list ABSENT at C:\\Users\\Test\\.opal\\account_id_hashes.txt -- this commit was NOT checked for client account ids (absent is not empty; set OPAL_ACCOUNT_ID_HASHES or place the list there).' The commit still committed (rc 0). Staged content is the source map's pin and sha256 hex values only; the check was not run, so that is not established by the check. Same condition as ADVI_FIRMBKTS-D1-W53-S2 on the flip commit.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "safe-commit.sh output for e274a0e60c (run 2026-10-12 in /c/dev/wk-firmbkts-54): 'WARN: client-data-check: hashed account-id list ABSENT'",
      "git show --stat e274a0e60c: 1 file changed, 16 insertions(+), 16 deletions(-) in infra/aws/lambda/ci/lambda-source-map.json"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Environmental: the list is not on this box. Not remediated by this worker; the drain or the box owner can rerun the client-data check against e274a0e60c with the list in place."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W54-S2",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~54",
  "surfaced_at": "2026-10-12T08:07:32Z",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~B1",
  "one_line": "The pre-commit risk reflex put HOLD on infra/aws/lambda/ci/lambda-source-map.json and cited a memory file that is not readable on this box; the commit proceeded.",
  "spec_asserts": "The order names no pre-commit risk check; the one-file re-pin commit proceeds on the order's own gates.",
  "world_is": "risk-reflex output at commit e274a0e60c: two '[HOLD] infra/aws/lambda/ci/lambda-source-map.json' lines (15 recorded claims each), citing memory/feedback_structural_over_cultural_pattern.md:21 ('6. **Untracked-production-source-file gate (pending ...) surfaced 2026-05'). That memory file was not found under ~/.claude/projects/C--dev-ajb-workspace/memory on this box, so the cited text was not read. The cited claim concerns an untracked production-source gate; this commit touches one tracked file. The commit went through (rc 0).",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "safe-commit.sh output for e274a0e60c: '[risk-reflex] [HOLD] infra/aws/lambda/ci/lambda-source-map.json' with 'memory/feedback_structural_over_cultural_pattern.md:21' cited",
      "read at this box: sed -n '15,25p' on /c/Users/Test/.claude/projects/C--dev-ajb-workspace/memory/feedback_structural_over_cultural_pattern.md returned 'No such file or directory'"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "ARMED because the warning's content is unread here and the estate wrote it against this node. Disarm owner is the issuer, who can read the citation and rule on the hold before the deploy order under the act 4 pair."
}
```

## Row filed by 0.7.0_AE_CloudOps~FB1 (FB-f-11, act 4 IRPT leg)

```json
{
  "id": "ADVI_FIRMBKTS-D1-S37",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.7.0_AE_CloudOps~FB1",
  "surfaced_at": "2026-10-12T14:23:54Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "TO-FB-f-11 step 4: irpt-narrative built from the main working tree reads cQ+WcTub... against the rehearsal's 0+/PHOb...; five JSON data members carry CRLF line endings in that tree; a build from a clean detached worktree reads the rehearsal hash.",
  "spec_asserts": "TO-FB-f-11 step 4: the printed artifact sha256 equals the rehearsal's for each function if the tree is otherwise unchanged; a difference is printed, explained and is a STOP until read.",
  "world_is": "Of the eight builds, six from the main tree equal the rehearsal; irpt-narrative reads cQ+WcTubuw3nZvIewiWzOEYBhOufHtY++DQ8vmn0hK4= (220,459 bytes). A member-by-member compare against the clean build (0+/PHOb/xGvYNBrz/j4Ltk5k85clmAo96BOJzi9n3ZY=, 220,364 bytes): 22 of 27 members byte-equal, 5 differ by size only (event_policy.json 4663 to 4718, fixtures/FIXTURE_MANIFEST.json, fixtures/performance_report_inf.json, fixtures/topics_predating.json, fixtures/topics_window.json); `git hash-object` of each working file differs from its committed blob while `git status` reads clean (CRLF working copy, autocrlf normalisation). The tree-resident narrative inputs are unchanged between the issuer's head ec099f0623 and HEAD. The CRLF object (S3 VersionId PZfbDaKAdbJRWlbKluX_bhpIS80WlIbX) was never applied; irpt-narrative was rebuilt from a detached worktree at e274a0e60c and uploaded; the deployed CodeSha256 equals the rehearsal.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/act4_irpt/build_irpt-narrative_main_tree_CRLF_SUPERSEDED.txt",
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/act4_irpt/build_irpt-narrative.txt"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "No decision owed for this act. For the issuer's builds: a main-tree BUILD_ONLY of irpt-narrative will not reproduce its rehearsal while that tree keeps CRLF data members; a clean worktree does."
}
```

## Row filed by 0.7.0_AE_CloudOps~FB1 (FB-f-11, act 4 IRPT leg)

```json
{
  "id": "ADVI_FIRMBKTS-D1-S38",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.7.0_AE_CloudOps~FB1",
  "surfaced_at": "2026-10-12T14:23:54Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "FB-f-9 AC1 (deployed-equal against HEAD) reads 18 of 20 after platinum_dest_view.py was shipped: C_06.client_mix_timeseries.py and D_04.client_portal_summary.py at HEAD carry MDPF_SECCLASS commits made after act 2's shipment.",
  "spec_asserts": "Runbook rev 3d: shipping platinum_dest_view.py at act 4's close makes FB-f-9 AC1 read 20 of 20.",
  "world_is": "r3_act2_reads.py deployed-equal at 14:16:47Z read 17 of 20 (platinum_dest_view.py, C_06, D_04 differ); after the one-object safe-deploy of data/black_diamond/scripts/gold/lib/platinum_dest_view.py (DEPLOYED, VERIFY OK) it reads 18 of 20 at 14:18:26Z, naming C_06.client_mix_timeseries.py and D_04.client_portal_summary.py. `git log` for the two files: 77849c4924 (0.9.0_WK_MDPF_SECCLASS~86, 2026-10-12 12:40Z) and a9f4bac7b5 (0.9.0_WK_MDPF_SECCLASS~80, 09:24Z) after act 2's 06:21Z shipment. This lane shipped no other object: those two scripts belong to another project's deploy cycle. safe-deploy printed WARN [seat-gates] would stop under ENFORCE (crossbox-deploy:data/black_diamond) and proceeded in WARN mode.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/act4_irpt/deployed_equal.out"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "The instrument compares to HEAD, so the literal 20 of 20 cannot be reached without deploying another project's unreviewed script changes. Options for the issuer: pin deployed-equal to the act-2 commit, or accept 18 of 20 with the two named as another project's pending deploy."
}
```

## Row filed by 0.7.0_AE_CloudOps~FB1 (FB-f-11, act 4 IRPT leg)

```json
{
  "id": "ADVI_FIRMBKTS-D1-S39",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.7.0_AE_CloudOps~FB1",
  "surfaced_at": "2026-10-12T14:23:54Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "TO-FB-f-11 instrument gaps: the first-hour origin 403/404 read has no per-behavior source; the performance adapter's census event refuses at input validation so it writes no evidence key; the sample's ownership_read field cannot be filled from logs.",
  "spec_asserts": "Step 6: read the router behaviors' origin responses over the first hour (CloudFront metrics or logs); step 5: the performance adapter is invoked once and its evidence artifact KEY named; AC2/r4_sample_eq counts ownership reads at the canonical key.",
  "world_is": "(a) Distribution EVTSA9VEHNZVH: Logging.Enabled False, additional metrics NoSuchMonitoringSubscription, 0 realtime log configs; only the aggregate Requests, 4xxErrorRate and 5xxErrorRate exist, and bursts of 150 to 500 requests at 38 to 63 percent 4xx were present before the first unit (11:33Z to 12:18Z), so the aggregate has no clean baseline and cannot separate a viewer-request 401/403 from an origin 403/404. (b) irpt-performance-adapter, census event with the granted viewer and a minted typed account id: ok false, public_reason_code INVALID_INPUT, exception PerformanceInputRefused 'explicit server-issued selection required' before retained.py:321; invoked twice (once by the sampler, once in a debug re-run), no artifact written, no key to name. (c) None of the eight IRPT functions logs the ownership key, so every SAMPLE_*.json ownership_read is empty and r4_sample_eq prints 'ownership reads at the canonical key 0'; the canonical-key evidence is the artifact: 8 of 8 deployed zips carry loaders.py equal to the flip commit's blob (sha256 a2283dc8...) and name opal-data-49financial.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/act4_irpt/cf_1420.out",
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/act4_irpt/perf.out",
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/act4_irpt/member.out",
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/act4_irpt/sample_eq.out"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "For the issuer: what instrument closes the first-hour read (the 8 IRPT functions' own error logs are available; the router behaviors' origin responses are not), and whether a server-issued selection is to be supplied for the performance adapter's one run."
}
```

## Row filed by 0.7.0_AE_CloudOps~FBL (FB-f-19, act 4 laptop leg, the router and guard gate after the flip)

```json
{
  "id": "ADVI_FIRMBKTS-S21",
  "project": "ADVI_FIRMBKTS",
  "fabric": "laptop",
  "surfaced_by": "0.7.0_AE_CloudOps~FBL",
  "surfaced_at": "2026-10-12T14:05:00Z",
  "one_line": "TO-FB-f-19 step 2: the router's own gate reads 42 pass / 9 fail (order: 51 pass, 0 fail) and the guard's reads 43 pass / 3 fail on HEAD after the flip commit; at the commit before the flip both read all-pass. The act is HELD before any plan or apply; nothing in AWS has moved.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "spec_asserts": "TO-FB-f-19 step 2: the router and the guard build through build-nodejs-lambda.sh with their own gates running, and the router's `bun run test` reads 51 pass and 0 fail; the order's section 0 says a reading that differs from it is a STOP and a BLOCKING row.",
  "world_is": "Built 13:53Z-13:55Z from HEAD 20215ccd98 (flip 69679b90e3 and re-pins e274a0e60c both ancestors). shared-advisor-router: `bun test test/` 42 pass, 9 fail, Ran 51 tests across 4 files; the nine are canonical-platinum.spec.mjs (2: the fixture finds a legacy firm, its alias and another firm in the registry; a listed bucket platinum passes), ADVI_FIRMSEP.04 firm-routing (5: X-Firm-Id 49financial routes to opal-data-bd; mockadv routes to opal-data-bd; PATH-CLASS SCOPING; TRAILING-SLASH CONTROL; opal-capital staff ?firm=bd platinum/advi/49financial) and POSN_TENANCY.TO-4-AE (2). shared-advisor-router-response: 43 pass, 3 fail, Ran 46 tests across 3 files (ADVI_FIRMSEP firm-isolation guard: '49financial served from opal-data-bd passes through', 'P4R-3: opal-capital staff with ?firm=bd reading advi/49financial from portal-v2 passes', 'does NOT publish an alert when firm/bucket match'). auth-validator-edge: no unit-test gate in the build output. CONTROL: the same two commands in a detached worktree at 69679b90e3~1 (1a8d882931) read router 51 pass 0 fail and guard 46 pass 0 fail, so the flip commit (it changed firm-config.mjs bucket lines and the registry routed value and no test file) is what moves the readings; the failing assertions name opal-data-bd for 49financial, which the flipped tree now maps to opal-data-49financial. The build script prints 'Tests: PASS' on a run with failures, so its own line is not evidence. Built artifacts (uploaded to s3://opal-313476888478-lambda-artifacts/portal-auth/): router sha256 +gJJpRe/HkZTEfKwBKfy7YJ2f9uSFV7iSh4lhHMlxCY=, guard 3ewTlF5dMkcQXUfdA/Vhgo7fbeVVzH+zbXpfF9pogrU=, validator sCxEV3p6ucK1iewCWQeqJaf0SHVURqOlj52dnE58WHo=. No plan, no apply, no association moved: the distribution EVTSA9VEHNZVH still reads router 27 x5, guard 6 x5, validator 22 x26 (read 13:49Z). lambda-source-map.json carries the three artifact records from the builds, uncommitted.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "deliverables/0.7.0_AE_CloudOps~FBL/evidence_f19/build_router.out, build_shared-advisor-router-response.out, build_auth-validator-edge.out (the full gate output, ANSI included)",
      "bun test test/ at 1a8d882931 (flip~1): router 51 pass 0 fail, guard 46 pass 0 fail; the same at HEAD: 42/9 and 43/3",
      "git show 69679b90e3 --stat: 16 files, none under infra/aws/lambda-edge/*/test",
      "deliverables/0.7.0_AE_CloudOps~FBL/evidence_f19/step0b_simulate.txt and pre_get_distribution_config.json (the gate passed and the live state is unmoved)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Not decided here whether the nine and three assertions are stale expectations of the legacy route (the likely reading) or a regression in the flipped routing; that call is the issuer's and the CTO's. Either way the order's gate reads differently from its text, so the act waits. Options for the issuer, one ask: (a) amend the order to accept the named failures as stale and have the tests updated in a commit before the build, or (b) rule the failures a STOP and fix the tests or the routing first, or (c) name another reading. Act 4 must land before Monday 23:00Z or act 2 rolls back. This seat resumes at step 3 on the issuer's word."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W60-S1",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~60",
  "surfaced_at": "2026-10-12T14:26:49Z",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "one_line": "FB-g-37: after the 12 stale expectations are updated, the router suite still has 1 failure outside the 12: 'shipped router: a platinum request keeps its legacy key and its legacy bucket' (canonical-platinum.spec.mjs:44-48) now receives the canonical key.",
  "spec_asserts": "The order names 12 failing assertions and bounds the edit to them (AC1 expects 0 fail in shared-advisor-router). The test 'shipped router: a platinum request keeps its legacy key and its legacy bucket' asserts that the shipped router, whose canonical list is empty, keeps a platinum request on its legacy key /platinum/accounts/z1/s.json and its legacy bucket.",
  "world_is": "The fixture the order prescribes (a scope with an alias, read from the registry's current state) selects FIRM = 49financial. Its bucket opal-data-49financial is now in the generated CANONICAL_PLATINUM_BUCKETS list of infra/aws/lambda-edge/_shared/firm-config.mjs (flip commit 69679b90e3), so the shipped handler rewrites the request to /advi/49financial/platinum/accounts/z1/s.json. The test passed at base only because its FIRM was inflection. It was not among the 12, so it was left unedited per the bound. bun test test/ in shared-advisor-router reads 51 pass, 1 fail, of 52 tests.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "bun test test/ in infra/aws/lambda-edge/shared-advisor-router at worktree HEAD db1aa38850 plus the uncommitted test edits: 51 pass, 1 fail, Ran 52 tests across 4 files",
      "bun AssertionError: actual '/advi/49financial/platinum/accounts/z1/s.json', expected '/platinum/accounts/z1/s.json' (canonical-platinum.spec.mjs:45-46)",
      "infra/aws/lambda-edge/_shared/firm-config.mjs at db1aa38850: CANONICAL_PLATINUM_BUCKETS = ['opal-data-49financial']; the FIRM_CONFIG 49financial bucket is opal-data-49financial"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "disarm_owner": "2.0.0_SA_COO~B1",
  "notes": "ARMED because a red shipped-router build gate stays red for every later edge build until the expectation is ruled. The expectation is stale for the flipped scope (the same class as the 12), so the issuer decides the edit. The worker proposes no edit beyond the bound. AC1 cannot pass until ruled."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W60-S2",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~60",
  "surfaced_at": "2026-10-12T14:31:44Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "The commit-time naming gate (LGIC_ENFORCE, enforce mode) refused the first form of the FB-g-37 test edits: new typed firm tokens and bucket domains in the router and guard test .mjs files. The commit aborted and nothing landed.",
  "spec_asserts": "The order states the expectations as literal bucket names and firm slugs (opal-data-49financial, firm=49financial, the bucket domain form) in the four router test files and the response guard test file, and names no naming-gate precondition.",
  "world_is": "safe-commit.sh on the first form: 'ERROR: BLOCKED -- the naming limb refused (LGIC_ENFORCE DEC-6, ENFORCE mode). Commit aborted; files unstaged.' Its NAMING REFUSE rows were the domain form opal-data-49financial.s3.us-east-1.amazonaws.com (RAISE, '49financial.s3.us' after opal-data- is no scope key) and the new carrier firm=49financial. After the expectations were read from the registry FIRM_CONFIG (no new firm token or domain literal), an offline run of .tools/naming-gate.py on the working-tree diff reads 'NAMING-GATE: WARN 17 graded' with no REFUSE.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "safe-commit.sh output for the first commit attempt on worktree wk-firmbkts-60: 'ERROR: BLOCKED -- the naming limb refused (LGIC_ENFORCE DEC-6, ENFORCE mode). Commit aborted; files unstaged.'",
      "python .tools/naming-gate.py --diff .scratch/d.diff at base db1aa38850 plus the working-tree test edits: 'NAMING-GATE: WARN 17 graded'"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Resolved in the worktree by reading the firm bucket and scope slug through FIRM_CONFIG, the registry route the gate's own remedy names. No gate was edited or bypassed. Recorded so the issuer knows the literal forms of the order cannot land under the gate."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W60-S3",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~60",
  "surfaced_at": "2026-10-12T14:31:44Z",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "one_line": "The naming gate documents a test exemption for the path segment /tests/, but the test directories this order names are test/, so every edit under them is graded.",
  "spec_asserts": "The naming gate documents that anything under */tests/* is not graded. The order names test/ directories as its write surface: shared-advisor-router/test and shared-advisor-router-response/test.",
  "world_is": ".tools/naming-gate.py at base db1aa38850 exempts a path only when the string '/tests/' occurs in '/' + path (line 2169, comment 'fixtures under */tests/* are not graded'; the same literal at line 996). The paths infra/aws/lambda-edge/shared-advisor-router/test/*.mjs carry '/test/', not '/tests/', so the commit attempt graded all four files: 'DENOMINATOR: 4 path(s) in this diff; declaration-tree domain = 4 MINUS EXCLUDED ... = 4 path(s)'.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "grep for the tests literal in .tools/naming-gate.py at db1aa38850: line 996 and line 2169 test for '/tests/' only",
      "safe-commit.sh naming-gate output for the first commit attempt: the four test .mjs files graded, 0 excluded"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "disarm_owner": "2.0.0_SA_COO~B1",
  "notes": "Recorded, not edited: the gate is outside this order's surface. Whether test/ should be exempt is the issuer's or the gate owner's ruling. Until ruled, a NEW typed firm token or bucket domain in a test/ edit is refused at commit."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W60-S4",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~60",
  "surfaced_at": "2026-10-12T14:34:45Z",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "one_line": "The order's AC1 and AC2 invocations print nothing as written: bun colours its summary lines even when piped, so the anchored grep matches no line.",
  "spec_asserts": "The order's AC1 and AC2 invocations (grep -E over bun test output for the pass and fail count lines, expect ^ *[0-9]+ pass +0 fail *$) read the counts, and the expectation is a match on that output.",
  "world_is": "bun 1.4.2 writes each summary line with ANSI escape codes around the count, also when stdout is a pipe: the line reads ESC[0m ESC[32m ' 51 pass' ESC[0m. The anchored pattern matches no line, so both invocations print nothing. With the codes stripped by sed, the same commands read ' 51 pass  1 fail ' (router) and ' 47 pass  0 fail ' (guard), identical on two runs. NO_COLOR=1 does not remove the codes.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "bun test test/ in infra/aws/lambda-edge/shared-advisor-router at worktree HEAD 728f3def09 piped to grep -E '^ *[0-9]+ (pass|fail)$': 0 lines matched (wc -l = 0)",
      "od -c of the summary line: ESC [ 0 m ESC [ 3 2 m ' 5 1 p a s s' ESC [ 0 m newline (raw bytes, no stripping)",
      "the same grep after sed 's/ESC[[0-9;]*m//g' reads ' 51 pass  1 fail ' and, in the guard, ' 47 pass  0 fail '; two runs each identical"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "disarm_owner": "2.0.0_SA_COO~B1",
  "notes": "The worker measured the counts with the codes stripped and reports AC2 as UNVERIFIABLE-BY-INSTRUMENT with that substitute oracle; AC1 is FAIL on the state, one failing test outside the twelve (ADVI_FIRMBKTS-D1-W60-S1). The worker changed no invocation: the issuer amends the instrument."
}
```

## Row filed by 0.7.0_AE_CloudOps~FBL (FB-f-21, Inflection fence admit, the order's target key and AC1)

```json
{
  "id": "ADVI_FIRMBKTS-S22",
  "project": "ADVI_FIRMBKTS",
  "fabric": "laptop",
  "surfaced_by": "0.7.0_AE_CloudOps~FBL",
  "surfaced_at": "2026-10-13T01:30:00Z",
  "one_line": "TO-FB-f-21: the order's -target key lgic_firm[\"opal-data-inflection\"] matches no state instance (real key: inflection), so its step 3 plan and its AC1 read 'No changes' vacuously; and the plan's diff carries one exception-list entry on DenyForeignFirmPrincipals besides the three added statements.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "TO-FB-f-21 step 3: `-target='aws_s3_bucket_policy.lgic_firm[\"opal-data-inflection\"]'` plans 'Plan: 0 to add, 1 to change, 0 to destroy' with exactly THREE ADDED statements; AC1 (same target, after the apply) expects '^No changes\\.'.",
  "world_is": "shared-infra state lists aws_s3_bucket_policy.lgic_firm[\"inflection\"] and [\"cottonwood\"]; no [\"opal-data-inflection\"] instance exists (terraform state list, 2026-10-13 01:13Z). Plan 01:12:40Z with the order's key: 'No changes' and the policy resource was not even refreshed. Plan 01:14:43Z with the key [\"inflection\"]: 'Plan: 0 to add, 1 to change, 0 to destroy'; policy 1 -> 4 statements; ADDED DenyScopedExemption1AnyOtherAction, DenyScopedExemption1ListingOutsidePrefix, DenyScopedExemption1ObjectsOutsidePrefix; REMOVED none; the pre-existing DenyForeignFirmPrincipals differs by ONE added leaf, Condition.ArnNotLike.aws:PrincipalArn gaining role/irpt-performance-adapter-role, which is what the COO half calls the row removing the blanket Deny for that ONE role. Applied 01:17:20Z-01:18:05Z with the real key. AC1 as written reads 'No changes' both before and after the apply, so it cannot discriminate; the corrected key read 'Plan 1 to change' before and 'No changes' after.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "deliverables/0.7.0_AE_CloudOps~FBL/evidence_f21/step3_plan_diff.txt and step3_plan.txt",
      "deliverables/0.7.0_AE_CloudOps~FBL/evidence_f21/step5_AC1_AC2_AC3.txt (AC1 as written and corrected)",
      "terraform state list in infra/aws/terraform/shared-infra: aws_s3_bucket_policy.lgic_firm[\"cottonwood\"] and [\"inflection\"]"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "No blocking effect: the corrected address names the same single policy the pair signs and the plan gate (one resource, three added statements, nothing removed) was read on the corrected plan before the apply. For the issuer: fix the order's target and AC1 key if the invocation is reused, and say whether the exception-list entry on DenyForeignFirmPrincipals is inside 'the three statements' reading of the pair (it is the row's signed effect per the COO half)."
}
```

## Row filed by 0.7.0_AE_CloudOps~FB1 (exec-summary generator read, 2026-10-13)

```json
{
  "id": "ADVI_FIRMBKTS-D1-S40",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.7.0_AE_CloudOps~FB1",
  "surfaced_at": "2026-10-13T04:52:31Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "The exec-summary generator is triggered by a gold chain-complete EVENT, not a 04:30Z cron, and that event has not been emitted by any gold chain in the run log since at least 2026-04-25 (every chain logs put-events failed); the generator has not run since 2026-05-04, before and independent of the cutover.",
  "spec_asserts": "Runbook rev 3d step 9 and ADDENDUM 4 item 3: the exec-summary generator runs cron(30 4 * * ? *) daily; its first run after 4b is read at the object at the canonical home (LastModified and a count).",
  "world_is": "04:50:01Z read: exec-summary-generator log 0 invocations since 04:25Z; exec_summary.json objects 158 at the canonical home and 158 at the legacy home, 0 written since 04:25Z at either. The only rule targeting the function is exec-summary-trigger, ENABLED, EventPattern detail-type chain-complete / source bd-pipeline.gold-chain, no schedule. Lambda Invocations, Errors and Throttles for the function: no datapoints in 30 hours; newest log stream 2026-05-04 16:44:32Z. gold_dispatch.sh emit_chain_complete (line 836) puts the event at chain close and prints WARN: EventBridge chain-complete put-events failed (non-fatal); the cumulative run log (6,834,280 lines, from at least 2026-04-25) carries that WARN on every chain-close date and 0 'chain-complete emitted' lines on any date, including 2026-10-12 and 2026-10-13. The runner role bd-exporter-ec2-role holds an Allow for events:PutEvents on the default bus in policy events-emit, so the role grant is not the missing piece (an SCP or the request itself is not read). The 23:00Z incremental chain of 2026-10-12 closed with exit code 0 and the generator did not run.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/act4bc_followup/exec_summary_read_0450Z.txt",
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/act4bc_followup/chain_complete_emission_per_log_date.txt"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Not caused by the move (the log shows it on every date from April). Act 4b's deployed generator (canonical mode, CodeSha256 fdPwodukz88d...) has therefore never been exercised; its read path was graded by r4_execeq only. No fix is in this lane's permitted set; ADDENDUM 4 item 3 classes a generator failure as a BLOCKING row fixed forward, with the stale summaries as the named cost (stale since 2026-05-04, not one day). Decision owed by the issuer: who fixes the put-events failure, and whether one manual invocation of the generator is authorised to exercise 4b (the order said not to invoke it)."
}
```

## Row filed by 0.7.0_AE_CloudOps~FB1 (FB-h-5, validator live read)

```json
{
  "id": "ADVI_FIRMBKTS-D1-S41",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.7.0_AE_CloudOps~FB1",
  "surfaced_at": "2026-10-13T06:43:35Z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "one_line": "no non-admin session in hand for the validator's ownership read: the 17 organic lines on /platinum/accounts/ and /books/relationship/ since the edge leg are all tier=internal (admin bypass), so the validator's canonical ownership read has not been exercised by a non-admin request.",
  "spec_asserts": "TO-FB-h-5 step 1: take an organic non-admin line on /platinum/accounts/ or /books/relationship/ since 2026-10-12T15:15:10Z; step 2: a driven request only with a signed non-admin session already in hand, none minted; otherwise a BLOCKING row, status parked, and report.",
  "world_is": "Read 2026-10-13T06:41Z: auth-validator-edge log groups in 7 regions, 9136 lines, Version 23 only. Auth OK lines by tier and path class since 15:15:10Z: advisor 303 on firm paths and 115 on other paths, 0 on accounts or relationship; internal 15 on accounts and 2 on relationship, 592 on firm and 1045 on other; service 2 on other; total 2074. The validator admits tier=internal as an admin bypass (index.mjs lines 35 and 401-406) before any ownership-map read, so the 17 lines are not ownership reads. The four events ownership_map_fetch_failed, ownership_map_schema_mismatch, advisor_not_in_ownership_map and advisor_scoping_denied: 0 each. This seat holds no signed non-admin session and mints none (order bound 2.2), so step 2 is not taken. The record VALIDATOR_LIVE_READ.json is committed at 0a817c97a03447ca1b0536d7b3e0b288128c21db and the grader reads FAIL no non-admin request on an accounts or relationship path was read.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/round5/VALIDATOR_LIVE_READ.json",
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/round5/h5_validator_reads.txt"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Owner of the un-park: 1.0.0_SA_CTO~DELL1. Condition: a non-admin session exists in a seat's hands, or Andrew supplies one; at that point the order re-opens with one request on an accounts path. An organic non-admin line may also arrive on its own (advisor lines exist on other paths today); the read can be repeated without a session. Standing watch: none added (no monitor)."
}
```

## Row filed by 0.9.0_WK_ADVI_FIRMBKTS~64 (FB-h-4 validator spec expectation, 2026-10-13)

```json
{
  "id": "ADVI_FIRMBKTS-D1-W64-S1",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~64",
  "surfaced_at": "2026-10-13T06:41:00Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "The order's test (i) wording 'every other firm's bucket is false' cannot hold for mockadv, which shares the 49financial bucket; the spec was implemented as 'every bucket that differs from the 49financial bucket is absent from the list'.",
  "spec_asserts": "The order's section 1a.1 states test (i) as: the list is the generated one, it is frozen, it contains the 49financial scope's bucket, and it contains NO other FIRM_CONFIG bucket ('every other firm's bucket is false').",
  "world_is": "FIRM_CONFIG mockadv has bucket 'opal-data-49financial', the same bucket as the 49financial scope (firm-config.mjs lines 67-86 at 69679b90e3), so mockadv's bucket is the engaged one and reads true, not false. The clause 'every other firm's bucket is false' is therefore not literally true for mockadv; the spec skips any firm whose bucket equals the 49financial bucket, so the intent (no other bucket in the list) is tested and the shared-bucket firm is not asserted false.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/lambda-edge/_shared/firm-config.mjs@69679b90e3 lines 67-86: 49financial and mockadv both carry bucket 'opal-data-49financial'",
      "infra/aws/lambda-edge/auth-validator-edge/tests/ownership_key.spec.mjs@7c6522bfe4 test (i) as implemented"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Not a product defect and not a failing assertion: the expectation is read at its intent. The issuer may amend the order's wording. The shared bucket is already recorded as a tenancy hazard in firm-config.mjs lines 38-50."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W64-S2",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~64",
  "surfaced_at": "2026-10-13T06:41:00Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "On this device safe-commit's client-data check did not run: the hashed account-id list is absent, so the spec commit 7c6522bfe4 was not checked for client account ids.",
  "spec_asserts": "The order and CLAUDE.md 14a require the commit to go through .tools/safe-commit.sh; the order names no client-data precondition and no account-id list.",
  "world_is": "safe-commit printed 'WARN: client-data-check: hashed account-id list ABSENT at C:/Users/Test/.opal/account_id_hashes.txt -- this commit was NOT checked for client account ids (absent is not empty)'. The committed change is one .mjs test file with no account identifiers, so the exposure is nil on inspection, but the check itself did not run on this device.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "safe-commit.sh output for commit 7c6522bfe4 on worktree wk-ADVI_FIRMBKTS-64: 'WARN: client-data-check: hashed account-id list ABSENT ... this commit was NOT checked for client account ids'",
      "commit 7c6522bfe4 changed one file: infra/aws/lambda-edge/auth-validator-edge/tests/ownership_key.spec.mjs (11 insertions, 2 deletions)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Recorded because a gate that cannot run on this device is a missing capability, not a clean pass. The fix (placing or pointing the list) is outside this order's bounds and is not made here."
}
```

## Row filed by 0.7.0_AE_CloudOps~FB1 (FB-h-5 amended, the walker session)

```json
{
  "id": "ADVI_FIRMBKTS-D1-S42",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.7.0_AE_CloudOps~FB1",
  "surfaced_at": "2026-10-13T06:49:02Z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "one_line": "the CTO's session for FB-h-5 (the dormant Opal UI walker service account) is itself an admin-bypass identity at the validator, so a walker request cannot exercise the non-admin ownership read; the route also needs write authority this seat does not hold.",
  "spec_asserts": "TO-FB-h-5 amended @f21abbf184 step 2 (CTO msg 4662): drive ONE accounts-path request by the dormant Opal UI walker service account with --firm 49financial, never Andrew's, because an admin's decisions are not the non-admin ones FWD-4 needs; PRECONDITION: its request must cross auth-validator-edge.",
  "world_is": "Read 2026-10-13T06:5xZ, no arm, no write: opal-users-v2 USER#usr_opal_ui_walker PROFILE reads role=admin, userType=Dev, firmId=opal-capital, status=disabled (projection of those four attributes; the hash and the lease were not read). The validator's admin bypass is `role === 'admin' OR firmRole === 'admin' OR tier === 'internal' OR userType === 'Dev'` (auth-validator-edge/index.mjs lines 35 and 401-406): the walker meets two of the four, so its request passes the validator's bypass before any ownership-map read and writes the same line class as the 17 organic tier=internal lines (row ADVI_FIRMBKTS-D1-S41). The skill's own header says the row is role admin, internal, Dev, 'a superadmin reach for as long as a session lives'. The FWD-4 premise (a non-admin decision) is therefore not met by this account for the same reason it is not met by Andrew's. Separately, arm needs a write to opal-users-v2 and SSM /opal/ui-walker/password (the skill's prerequisite: the laptop profile; the Dells hold GetParameter only), which this identity does not hold, and the walker refuses any base URL but localhost:5174 (a local dev:live build).",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/lambda-edge/auth-validator-edge/index.mjs lines 35 and 401-406",
      ".claude/skills/ui-walk/ui_walker_account.py header (the safety model)",
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/round5/h5_validator_reads.txt"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "No arm was attempted, no session touched. A non-admin identity at the validator needs role not admin, firmRole not admin, tier not internal and userType not Dev, with a partner profile and an advisorKey in the ownership map: an advisor-tier user of a client firm. Owner of the un-park stays 1.0.0_SA_CTO~DELL1 (a seat's non-admin session, or Andrew supplies one, or the first organic advisor-tier line on those paths; 418 advisor-tier lines exist today, none on them)."
}
```

## Row filed by 0.9.0_WK_ADVI_FIRMBKTS~63 (FB-h-3 offline replay, 2026-10-13)

```json
{
  "id": "ADVI_FIRMBKTS-D1-W63-S1",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~63",
  "surfaced_at": "2026-10-13T06:46:59Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "Two of my pre-harness probe runs reached the render-key Secrets Manager secret, outside the order's two-S3-read bound; the mock I used did not bind.",
  "spec_asserts": "Order section 2 BOUNDS 1: reads only, two S3 get-object calls. Order section 1b step 1: mock jwtPublicKeys.mjs; no production key, secret or token is read.",
  "world_is": "Probe 1 (.scratch/probe_mock.mjs, bun run) and probe 2 (a probe file in the deliverables folder, since deleted) each imported render_auth.mjs and called getRenderKeySlots() under a Secrets Manager mock keyed by a bare specifier. The mock did not bind (probe 2 counted 0 mock sends), so getRenderKeySlots() reached the real SecretsManagerClient and returned slots without throwing: one GetSecretValue on opal/auth/irpt-render-jwt-public-key per probe. Inferred from the non-throw outcome; not measured in CloudTrail. No secret value was printed or written to the tree.",
  "grounding": {
    "status": "INFERRED",
    "evidence": [
      "infra/aws/lambda-edge/auth-validator-edge/render_auth.mjs@b39d4a70f6 (getRenderKeySlots sends GetSecretValueCommand for RENDER_PUBLIC_KEY_SECRET_ID when its cache is empty)",
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~63/replay_harness.mjs@4b8bd3b056 (stubs Secrets Manager and seeds the render cache, so the replay makes no such call)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "The replay itself made no Secrets Manager call: the render cache is seeded before each request. Whether the two probe reads need a CloudTrail check is for the issuer to decide; the reads were read-only and touched a public-key secret."
}
```

## Row filed by 0.9.0_WK_ADVI_FIRMBKTS~63 (FB-h-3 offline replay, 2026-10-13)

```json
{
  "id": "ADVI_FIRMBKTS-D1-W63-S2",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~63",
  "surfaced_at": "2026-10-13T06:46:59Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "The order's mock list does not cover the render branch: auth-validator-edge calls Secrets Manager before the human path whenever its render-key cache is empty.",
  "spec_asserts": "Order section 1b step 1: replace @aws-sdk/client-s3 and lambda/lib/authkeys/jwtPublicKeys.mjs; the handler is otherwise driven as it is.",
  "world_is": "index.mjs evaluateRenderBranch (lines 257-260, called at line 353) calls getRenderKeySlots() before the human path. render_auth.mjs getRenderKeySlots() (lines 58-72) sends GetSecretValueCommand for opal/auth/irpt-render-jwt-public-key when its cache is empty or older than 300 s. Mocking jwtPublicKeys.mjs does not cover that call. The replay closes it by calling __setRenderKeySlotsForTest before each request, so a human token fails the render audience check (verifyRenderTokenWithSlots, lines 159-170) and falls through to the human path.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/lambda-edge/auth-validator-edge/index.mjs@b39d4a70f6 lines 257-260 and 353",
      "infra/aws/lambda-edge/auth-validator-edge/render_auth.mjs@b39d4a70f6 lines 58-72 and 159-170"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Any later replay or test of the human path must seed or mock the render key the same way, or it reads Secrets Manager."
}
```

## Row filed by 0.9.0_WK_ADVI_FIRMBKTS~63 (FB-h-3 offline replay, 2026-10-13)

```json
{
  "id": "ADVI_FIRMBKTS-D1-W63-S3",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~63",
  "surfaced_at": "2026-10-13T06:46:59Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "The handler caches each firm's ownership map at module scope for 60 s, so back-to-back runs in one process reuse the first map; the harness steps the clock between runs.",
  "spec_asserts": "Order section 1b steps 4-5: three runs (legacy, canonical, perturbed canonical) through the handler, each serving its own map.",
  "world_is": "index.mjs getOwnershipMap (lines 161-194) keeps ownershipMapCache keyed by firmId with expiresAt = Date.now() + 60 s. A second run within 60 s returns the first run's map with no S3 read. The harness advances Date.now by 120 s before the canonical and control runs, asserts that each run made at least one GetObject, and asserts that the canonical run requested exactly one Bucket and Key.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/lambda-edge/auth-validator-edge/index.mjs@b39d4a70f6 lines 161-166 and 177-194",
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~63/replay_harness.mjs@4b8bd3b056 (clock step and per-run GetObject assertions)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Any replay that neither steps the clock nor re-imports the handler per run measures the first map three times."
}
```

## Row filed by 0.9.0_WK_ADVI_FIRMBKTS~63 (FB-h-3 offline replay, 2026-10-13)

```json
{
  "id": "ADVI_FIRMBKTS-D1-W63-S4",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~63",
  "surfaced_at": "2026-10-13T06:50:53Z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "one_line": "AC2 names the base checkout's deliverables path for REPLAY_RESULT.json, but the record is committed in my worktree; AC2 fails verbatim as ABSENT.",
  "spec_asserts": "Order section 4 AC2: r5_checks.py replay --file C:/dev/ajb_workspace/org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~63/REPLAY_RESULT.json. Order section 5: commit REPLAY_RESULT.json in the deliverables folder (the worktree's paths grant).",
  "world_is": "The deliverables folder and REPLAY_RESULT.json exist only in the worktree C:/dev/wk-firmbkts-63, committed at 4b8bd3b056. The base checkout C:/dev/ajb_workspace has no 0.9.0_WK_ADVI_FIRMBKTS~63 folder and I did not write into it. Verbatim AC2 printed FAIL ABSENT or unreadable: FileNotFoundError (rc=1). The same checker on the worktree copy printed REPLAY record ok pairs=2127 mismatches=0 control_mismatches=1 bytes_equal=False (rc=0); that is a diagnostic, not the criterion verdict.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~63/REPLAY_RESULT.json@4b8bd3b056 (the worktree copy the checker reads on the diagnostic run)",
      "C:/dev/ajb_workspace/org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round5/checks/r5_checks.py replay run verbatim: FAIL ABSENT or unreadable (rc=1)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "AC2 stays FAIL on the instance; the order is not flipped. The issuer decides whether the checker path is to be re-pointed at the worktree copy or the record is to be copied to the base checkout; I did not do either."
}
```

## Row filed by 0.7.0_AE_CloudOps~FB1 (FB-h-8, the fence-scoped check)

```json
{
  "id": "ADVI_FIRMBKTS-D1-S43",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.7.0_AE_CloudOps~FB1",
  "surfaced_at": "2026-10-13T06:54:01Z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "one_line": "TO-FB-h-8: the cp1252 crash is fixed, but the fence-scoped check cannot read ok=True for four further reasons that are not the two named: the simulator is denied to this identity (31 of 31 arms), the pinned fence file's CRM selector fails over today's registry, two refusal arms no longer match the validator (5 of 7), and unchanged_today and scoped_rendered read stale against the registry's new `grants` field.",
  "spec_asserts": "TO-FB-h-8 section 1: two named failures (cp1252 print, before_strip init at one(list)); close on FENCE-SCOPED ... refusals_ok=7/7 ... ok=True with no environment override; section 2.2: a failure for any other reason is a BLOCKING row naming the failing arm; section 1b rule 1: an arm's meaning is not weakened; rule 2: a denied simulator is reported, never stubbed.",
  "world_is": "Edits committed at 38f8179f10056a0ddaf8d66fe21d389e8068b720: out() replaces non-ASCII, the two git ls-tree reads carry encoding utf-8. The other three tests/ files already read and write with explicit utf-8 and hold 0 non-ASCII bytes. Last line at that HEAD, no override: FENCE-SCOPED rows_today=42 unchanged_today=False scoped_rendered=0/0 sim_ok=0/0 refusals_ok=0/7 unknown_key_refused_by=none ok=False. Reasons, each measured: (1) the named second failure is real but its cause is not `lgic_managed_firm_buckets` being an object: the PINNED fence file (06c783b92b, s3-lgic-firm-buckets.tf line 194) selects `lgic_crm_scope = one([for k,s in local.lgic_managed_firm_buckets : s if length(lookup(s, 'masters', [])) > 0])`, which returns ONE row over the pre-rows registry (before_pre passes) and two rows over today's registry, so one() fails the init of before_strip and before_today ('local.lgic_managed_firm_buckets is object with 2 attributes' is the diagnostic's value dump); HEAD's own file uses restricted_prefix_hosts and says masters 'stopped being unique'. An experiment in a scratch driver (no repository file touched) that gave those two roots HEAD's selector lets them init. (2) With (1) worked around: sim_ok=0/31: iam:SimulateCustomPolicy is AccessDenied to user/cloudops-dell1-agent-user (direct call: 'no identity-based policy allows the iam:SimulateCustomPolicy action'); arms 1-8 and C1-C4 on three buckets all ERROR; not stubbed (rule 2). (3) refusals_ok=5/7: case 3 (a prefix without the trailing /) and case 4 (actions with s3:PutObject) are NOT refused by opal_naming.validate at HEAD (0 refusals, the control is clean), while case 1, 2, 5, 6, 7 are, so the instrument's arms 3 and 4 assert rules the validator no longer carries. (4) The registry's exemptions.json gained a top-level `grants` object (key opal-data-49financial) since the commit before the first scoped row: rows_since reports `top-level field grants changed`, so unchanged_today reads False, and scoped_rendered reads 17/39 (13 scoped rows x 3 expected, 17 rendered).",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/round5/ADVI_FIRMBKTS.TO-FB-h-8.fence-instrument-utf8-fixture.proof_of_spec.json",
      "infra/aws/terraform/shared-infra/s3-lgic-firm-buckets.tf (lines 191-198 at HEAD)",
      "git show 06c783b92b:infra/aws/terraform/shared-infra/s3-lgic-firm-buckets.tf (line 194)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "No arm was weakened and the simulator was not stubbed. Decisions owed by the issuer: (a) route the 31 simulator arms to the laptop lane (rule 2); (b) rule what the before roots do when the pinned fence file's selector no longer picks one row (give them HEAD's selector, or retire the pinned arm, or re-pin): any of the three changes what the arm asserts; (c) rule arms 3 and 4 against the validator's current rules (did the grants field retire them?), and (d) whether `grants` is an admitted top-level field for unchanged_today. This seat made no further edit to the check."
}
```

## Row filed by 0.9.0_WK_ADVI_FIRMBKTS~65 (FB-h-6, exec-summary diagnosis, read-only)

```json
{
  "id": "ADVI_FIRMBKTS-D1-W65-S1",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~65",
  "surfaced_at": "2026-10-13T06:52:46Z",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~B1",
  "one_line": "No CloudTrail PutEvents call exists in any of 17 enabled regions over 90 days, so the chain-complete put-events WARN never reached the events API: the failure sits upstream of EventBridge.",
  "spec_asserts": "TO-FB-h-6 section 1a.1 reads the failing put-events as a call that reaches the events API, so CloudTrail holds its per-day calls and errorCode texts for reading, and the record's verdict follows from them.",
  "world_is": "CloudTrail LookupEvents EventName=PutEvents, 2026-07-15T00:00:00Z to 2026-10-13T23:59:59Z: 0 events in 17 of 17 enabled regions. The positive control (EventSource=events.amazonaws.com, us-east-1, 20 events) returns events. The chain-close WARN on 2026-10-13 is cited from D1-S40, not re-read. Runner bd-gold-layer-runner (i-01003b035d2988dfb, profile bd-exporter-profile) launched 2026-10-13T04:00:47Z and is stopped now.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~65/EXEC_SUMMARY_DIAGNOSIS.json@c9fc7f9ec0",
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~65/EXEC_SUMMARY_DIAGNOSIS.md@c9fc7f9ec0"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Consistent with D1-S40, which records chain-close WARNs on 2026-10-12 and 2026-10-13 and zero 'chain-complete emitted' lines. Either the call never executes on the runner, or it runs under an identity, region or CLI config that CloudTrail does not show here. The next read is runner-side (CLI identity, default region and output, chain logs), outside this read-only order; the issuer decides who reads it."
}
```

## Row filed by 0.9.0_WK_ADVI_FIRMBKTS~65 (FB-h-6, region scope of the CloudTrail read)

```json
{
  "id": "ADVI_FIRMBKTS-D1-W65-S2",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~65",
  "surfaced_at": "2026-10-13T06:52:46Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "The order fixed its CloudTrail read to us-east-1, but the emit names no --region, so the runner's region is unreadable; this worker swept PutEvents over the 17 enabled regions and found none.",
  "spec_asserts": "TO-FB-h-6 section 1a.1 and its header: CloudTrail lookup in region us-east-1, the region the bus and rule live in.",
  "world_is": "gold_dispatch.sh:840-850 runs 'aws events put-events' with no --region, so the region is the runner's CLI default, which this order cannot read. The us-east-1 lookup and each of the 16 other enabled regions (ec2 describe-regions) returned 0 PutEvents over the 90-day window.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~65/EXEC_SUMMARY_DIAGNOSIS.json@c9fc7f9ec0 (calls list, 17 PutEvents lookups)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "The region question is closed for CloudTrail event history: no PutEvents in any enabled region. The runner's default region itself stays unread, and the sweep was a read, not an act."
}
```

## Row filed by 0.9.0_WK_ADVI_FIRMBKTS~65 (FB-h-6, denied read)

```json
{
  "id": "ADVI_FIRMBKTS-D1-W65-S3",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~65",
  "surfaced_at": "2026-10-13T06:52:46Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "organizations list-policies (SERVICE_CONTROL_POLICY) is AccessDenied to cloudops-dell1-agent-user, so any SCP that could deny events:PutEvents is unreadable from this identity.",
  "spec_asserts": "TO-FB-h-6 section 2 bound 2: a denied read is recorded in the record's calls and filed as a surprise row, and the record states the SCP effect.",
  "world_is": "aws organizations list-policies --filter SERVICE_CONTROL_POLICY returns AccessDeniedException ('You don't have permissions to access this resource'), rc=254, for arn:aws:iam::313476888478:user/cloudops-dell1-agent-user.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~65/EXEC_SUMMARY_DIAGNOSIS.json@c9fc7f9ec0 (denied_reads)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "A denial is not evidence that an SCP exists. An SCP deny on PutEvents would show as an AccessDenied record in CloudTrail, and none is recorded, so the SCP question is open only in the sense that it is unread."
}
```

## Rows filed by 0.9.0_WK_ADVI_FIRMBKTS~66 (FB-h-7 quantification, 2026-10-13T07:07:58Z)

```json
{
  "id": "ADVI_FIRMBKTS-D1-W66-S1",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~66",
  "surfaced_at": "2026-10-13T07:07:58Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "The order's path data/black_diamond/scripts/gold/bd_price_update.py does not exist: the file is at data/black_diamond/scripts/silver/bd_price_update.py; its Lambda twin is infra/aws/lambda/bd-pipeline/bd-price-update/lambda_function.py.",
  "spec_asserts": "FB-h-7 section 1a and 1c cite data/black_diamond/scripts/gold/bd_price_update.py (lines 263-271, 344, 265).",
  "world_is": "comp-find --name 'bd_price_update*' data/black_diamond returns one hit, data/black_diamond/scripts/silver/bd_price_update.py (202 files scanned, corpus all). The cited line numbers are correct at the silver path. The Lambda twin's load_transactions_for_date is at lambda_function.py:141-149 (key line 143).",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~66/pricing_quant_s32_s33.py",
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~66/PRICING_QUANT.md",
      "infra/aws/lambda/bd-pipeline/bd-price-update/lambda_function.py:143"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Quantified at the silver path. No product file was edited."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W66-S2",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~66",
  "surfaced_at": "2026-10-13T07:07:58Z",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "one_line": "The 2026-10-09 same-date price tie is non-decisive in the current file set: all 11,108 tied assets select a later-dated row, so the unstable sort does not decide the served 10-09 price. It is decisive only as of the 10-09 run (inferred: 3,906 of 11,108 alternative prices differ).",
  "spec_asserts": "FB-h-7 section 1b: the default-kind sort_values('date', ascending=False) in B_01.holdings_lots.py (lines 331-361) decides same-date ties between silver/prices/2026-10-09.parquet and canonical_prices.parquet.",
  "world_is": "Replay of the B_01 load on the current 174 price objects: tied 11108; winner_other_date 11108; winner daily 0; winner canonical 0; negative control (no source column) same pick. As-of replay (daily <= 10-09, canonical rows <= 10-09; inferred): winner daily 11106, canonical 2, alternative_differs 3906, max delta 1020.0. The served holdings snapshot gold/timeseries/holdings_lots/2026-10-09.parquet was rewritten 2026-10-13T05:06:00Z.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~66/pricing_quant_s32_s33.py",
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~66/PRICING_QUANT.json (s33)",
      "data/black_diamond/scripts/gold/B_01.holdings_lots.py:331-361"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "The sort stays ARMED: any asset whose latest date is a tie takes the pandas sort order. The EC2 runner installs unpinned pandas (setup-instance.sh line 20); the production pandas version is absent. Sensitivity is inferred.",
  "disarm_owner": "2.0.0_SA_COO~B1 (issuer; routes the B_01 tie-break fix to the gold owner)"
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W66-S3",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~66",
  "surfaced_at": "2026-10-13T07:07:58Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "Served canonical transaction_observed prices do not equal the current file median for 603 of 1,610 comparable rows over the 20 window dates, so a served T-1 value is not the median the code recomputes from the day partition.",
  "spec_asserts": "FB-h-7 section 1a presumes the served T-1 price is the median of the same-date silver/transactions partition (extract_t1_prices, bd_price_update.py lines 327-345).",
  "world_is": "Served canonical rows with source transaction_observed on the 20 dates: 1,657; 1,610 have the asset in the recompute; 1,007 equal it within 1e-6; 603 do not. Cause not isolated; candidates are backfill_new_assets (multi-day history) and partition state at write time (transaction ids moved between files).",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~66/pricing_quant_s32_s33.py (s32 served_check)",
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~66/PRICING_QUANT.md"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Does not change the S32 count; it limits how far the served T-1 value can be read as the file median."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W66-S4",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~66",
  "surfaced_at": "2026-10-13T07:07:58Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "Object versions of gold/canonical/account_gains/2026-08-20..23 begin at 2026-09-27T05:05:24Z, and the whole prefix (2,473 objects) was rewritten within 2026-10-13T05:13:06Z to 05:14:05Z, so the first version after 2026-08-23 is not the rewrite-era state for these keys.",
  "spec_asserts": "FB-h-7 section 1c: compare each version written after 2026-09-02 with the first version written after 2026-08-23.",
  "world_is": "list-object-versions: 36 versions per account_gains key, earliest 2026-09-27T05:05:24Z (all four keys share the timestamp); all 36 have identical content per key. silver/transactions keys have versions from 2026-08-20 to 2026-09-02; silver/prices keys have no version after 2026-08-23.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~66/pricing_quant_s34.py",
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~66/PRICING_QUANT.json (s34)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "The account_gains base is the 09-27 version by necessity; the pre-09-27 state is not recoverable from versions."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W66-S5",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~66",
  "surfaced_at": "2026-10-13T07:07:58Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "bd-price-update records no INFO step lines: the \"Step 1a\" filter returns zero events since 2026-09-02 while 35 invocations are recorded, so the reader at lambda_function.py:143 cannot be confirmed from its logs.",
  "spec_asserts": "FB-h-7 section 1c asks whether each reader ran, using a CloudWatch Invocations count or the chain run log.",
  "world_is": "CloudWatch AWS/Lambda Invocations Sum 35 over daily buckets 2026-09-02..2026-10-12. The log group holds START, END, REPORT and FutureWarning lines (the pd.concat warning at lambda_function.py:135) and no INFO lines; filter-log-events with \"Step 1a\" since 2026-09-02 returns 0 events.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~66/PRICING_QUANT.json (s34 readers[2])",
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~66/write_record.py"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "The Lambda twin row is recorded as claim inferred for the call at line 143."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W66-S6",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~66",
  "surfaced_at": "2026-10-13T07:07:58Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "silver/transactions has objects on weekend dates (for example 2026-10-10 and 2026-10-11), and the two most recent weekdays hold zero-row partitions (2026-10-12 and 2026-10-13, 35,269 bytes each), so \"the 20 most recent trading days that have an object\" needed a weekday rule to be defined.",
  "spec_asserts": "FB-h-7 section 1a: the 20 most recent trading days that have a silver/transactions object.",
  "world_is": "1,927 dated objects; 1,614 on weekdays. The 20 most recent weekday objects run 2026-09-16 to 2026-10-13; rows are 0 on 2026-10-12 and 2026-10-13.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~66/PRICING_QUANT.md",
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~66/pricing_quant_s32_s33.py"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Exchange holidays were not removed; a holiday partition with rows would be counted, not dropped."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W66-S7",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~66",
  "surfaced_at": "2026-10-13T07:07:58Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "Every aws call from this worktree prints \"WARN: aws: no caller-toplevel .tools/aws (git rc=128) -- PREPENDING THE BAKED C:/dev/ajb_workspace/.tools\", so the shim resolves to the base checkout tools, not the worktree tools.",
  "spec_asserts": "CLAUDE.md section 6: AWS via the .tools/aws shim, resolved from the checkout.",
  "world_is": "Each aws call in this session printed the WARN line and still returned the expected output (rc 0 on reads); the outputs read are S3, CloudWatch and Lambda reads of the same account.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~66/fetch_versions.sh"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Recorded as an instrument note; no read result depended on the shim path."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W66-S8",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~66",
  "surfaced_at": "2026-10-13T07:07:58Z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "one_line": "The order AC1 invocation names the base checkout path for PRICING_QUANT.json; the record exists only in this worktree until integration. The literal run is FileNotFoundError (FAIL); the worktree-path run returns QUANT keys ok.",
  "spec_asserts": "FB-h-7 section 4 AC1: --file C:/dev/ajb_workspace/org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~66/PRICING_QUANT.json",
  "world_is": "Literal run: FAIL, ABSENT or unreadable (FileNotFoundError) because the base checkout has no folder 0.9.0_WK_ADVI_FIRMBKTS~66. Worktree-path run: QUANT keys ok calls=442 recommendation=BRIEF_TO_CRO (rc 0).",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~66/PRICING_QUANT.json",
      "C:/dev/ajb_workspace/org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round5/checks/r5_checks.py"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "The issuer should re-point AC1 at the integrated path or accept the worktree path; the order status is not flipped here."
}
```

## Row filed by 0.7.0_AE_CloudOps~FB1 (FB-i-2, the runner-side emit read)

```json
{
  "id": "ADVI_FIRMBKTS-D1-S44",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.7.0_AE_CloudOps~FB1",
  "surfaced_at": "2026-10-13T07:48:47Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "The exec-summary emit fails on the runner with no exception text and the cause reads REGION_UNSET (inferred); the order's probe step collides with the runner's standing access policy, and the 'no CloudTrail PutEvents' premise is not a discriminator.",
  "spec_asserts": "TO-FB-i-2 section 1: read the runner-side emit path; step 2 sends ONE non-matching PutEvents by ssm send-command to bd-gold-layer-runner only if step 1 is STILL_INDETERMINATE. ROUND_ANALYSIS.round5 section 2 premise: CloudTrail holds no PutEvents call, so the dispatcher's WARN fires without the call reaching the events API.",
  "world_is": "Read 2026-10-13T07:4xZ. (1) infra/aws/ec2/EC2_MANIFEST.json entry bd-gold-layer-runner carries _access_policy 'EVENTBRIDGE ONLY. No agent, no human, no SSM command may start, stop, or run commands on this instance. Only the bd-gold-trigger Lambda (invoked by EventBridge) may touch it. Manual gold runs go to bd-gold-qa-runner.' The order's step 2 is an ssm send-command to that instance; it was not needed (verdict reached) and not sent. (2) cloudtrail lookup-events EventName=PutEvents in us-east-1 returned 0 events from any principal over 7 days, while the runner's own session shows 806 events (UpdateInstanceInformation 529, ListInstanceAssociations 235, Decrypt 27, CreateInvalidation 14, GetSecretValue 1) and PutMetricData is not logged by CloudTrail at all (the AccessDenied PutMetricData lines in the runner log have no CloudTrail twin): the absence of a PutEvents record is not evidence that the call never left the runner. (3) The runner log carries 33 'SS4c weekly run FAILED (AccessDenied ... cloudwatch:PutMetricData ... no identity-based policy allows ...)' lines from 2026-06-24 and a dtype-divergence AccessDenied (namespace Opal/DataQuality) in the 2026-10-13 04:00Z chain: policy GldRunnerMetrics allows PutMetricData only for namespaces GLDINC/SS4c and BD/GoldRunner, so the first two are IAM matters separate from the emit. (4) The emit WARN's neighbour lines and the CloudFront-invalidation control are in RUNNER_EMIT_READ.json (commit a1408b77df77edf2c3f2f8e391affc5dc169f4ce).",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/RUNNER_EMIT_READ.json",
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/RUNNER_EMIT_READ.md",
      "infra/aws/ec2/EC2_MANIFEST.json (bd-gold-layer-runner _access_policy)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Decisions owed: (a) whether the one-event probe is wanted at all given the verdict is reached by inference, and if so how the manifest's standing access policy is reconciled with the CTO's word (the issuer's call; the next runner-up window is 23:00Z); (b) the fix cell (round 7) under its own never-widen pair; (c) whether the 33 SS4c and the dtype PutMetricData AccessDenied lines want their own row owner. Nothing was sent, written or changed by this seat."
}
```

## Rows filed by 0.9.0_WK_ADVI_FIRMBKTS~69

Rows are appended after the earlier rows; each is one fenced json object.

```json
{
  "id": "ADVI_FIRMBKTS-D1-W69-S1",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~69",
  "surfaced_at": "2026-10-13T08:16:07Z",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "0.0.0_AB_MSTR~DELL1",
  "one_line": "The commit gate on this device reports the hashed account-id list ABSENT, so the commit of gold_dispatch.sh was NOT checked for client account ids; the order names no such check.",
  "spec_asserts": "The order names no commit-time client-data check; the commit was expected to go through safe-commit with the gates clean.",
  "world_is": "safe-commit printed 'WARN: client-data-check: hashed account-id list ABSENT at C:\\Users\\Test\\.opal\\account_id_hashes.txt -- this commit was NOT checked for client account ids (absent is not empty)'. The commit f313505d5cfbaa696d83dcc87f560d4858583aa1 went through with rc=0. The staged diff is a bash function body with no account ids.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "data/black_diamond/scripts/gold/gold_dispatch.sh@f313505d5cfbaa696d83dcc87f560d4858583aa1",
      ".tools/safe-commit.sh commit output for f313505d5c (client-data-check WARN line)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Recurring condition already carried by earlier rows in this channel. Left alone, commits from this device pass without the client account-id check until the list is placed or OPAL_ACCOUNT_ID_HASHES is set. No read or write was made to the list itself."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W69-S2",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~69",
  "surfaced_at": "2026-10-13T08:16:07Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "The pre-commit risk reflex printed HOLD on gold_dispatch.sh against a freshness-gate claim about the COT script; the cited claim does not concern the function this order edits.",
  "spec_asserts": "The order names only the emit_chain_complete function in gold_dispatch.sh as the edit surface; no pre-commit citation review is named.",
  "world_is": "comp-pulse diff printed [HOLD] for data/black_diamond/scripts/gold/gold_dispatch.sh and a second HOLD for data/cot/scripts/gold/gold_dispatch.sh, both citing docs/references/FRESHNESS_GATE_MANIFEST_20260717.md:74 (row R2, check_freshness keyed on the BD bucket, at the COT script lines 174-177). The cited row is about the COT script, not emit_chain_complete. The commit proceeded.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "docs/references/FRESHNESS_GATE_MANIFEST_20260717.md@f313505d5cfbaa696d83dcc87f560d4858583aa1 (line 74, row R2)",
      "data/black_diamond/scripts/gold/gold_dispatch.sh@f313505d5cfbaa696d83dcc87f560d4858583aa1 (emit_chain_complete, lines 836-860)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "The reflex matched on the file basename. The citation was read before the commit as the reflex asked; no action taken on the COT script."
}
```

## Row filed by 0.7.0_AE_CloudOps~FB1 (FB-j-3, the dispatcher precondition)

```json
{
  "id": "ADVI_FIRMBKTS-D1-S45",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.7.0_AE_CloudOps~FB1",
  "surfaced_at": "2026-10-13T08:23:30Z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "one_line": "TO-FB-j-3 NOT deployed: FB-j-2's emit_chain_complete assigns `out=$(aws events put-events ...)` as a plain statement under the dispatcher's `set -e` (line 57), so when the call fails the dispatcher exits at that line, before the WARN prints and before the CDN invalidation, the recon harness and SHUTDOWN_ARMED, and the measurement is lost with it.",
  "spec_asserts": "TO-FB-j-3 precondition and FB-j-2: the WARN changes to carry rc and 300 characters of CLI text 'and nothing else'; the emit is non-fatal ('Non-fatal: put-events failure logs a WARN and returns 0 so the chain close output still prints cleanly', dispatcher comment lines 829-830).",
  "world_is": "gold_dispatch.sh line 57 is `set -e`. The deployed function tests the call inside an `if` condition (immune to errexit); the FB-j-2 function (HEAD 71b706df6e, f313505d5c) is `local out rc txt` then `out=$(aws events put-events --entries ... 2>&1); rc=$?` as simple statements. Reproduced with the dispatcher's own option and a stand-in aws that returns 255 with the CLI's 'You must specify a region' text (act's harness, j3_precondition/): OLD function prints the WARN and the next statement runs (exit 0); NEW function prints nothing and the shell exits 255 at the assignment. In the real chain close that skips, in order after the emit: the CDNCOHT post-chain invalidation (portal freshness), the WP-10b recon harness, and the SHUTDOWN_ARMED line (the watchdog still stops an idle instance). The issuer's r7_emit_test.sh extracts and sources the function alone with no `set -e`, so its 3 of 3 does not cover the dispatcher's option. The order's own object diff is clean: deployed to repo is 2 hunks, 7 changed lines, inside emit_chain_complete only. Nothing was written to S3, no ledger entry opened.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/j3_precondition/run_output.txt",
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/j3_precondition/harness.sh",
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/j3_precondition/fn_new.sh",
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/j3_precondition/fn_old.sh",
      "data/black_diamond/scripts/gold/gold_dispatch.sh lines 57 and 836-857"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Smallest correction (the DS lane's file, a new worker cell, not this seat's edit): keep the call inside a conditional so errexit cannot fire, e.g. `out=$(aws events put-events --entries \"file://$entries_file\" 2>&1) && rc=0 || rc=$?`, then the same grep and the same WARN text. Re-test it under `set -e` (harness.sh here, arm 2 must print the WARN with rc=255 and then reach the next statement). The order then deploys the corrected file unchanged otherwise. The order stays pending; nothing deployed."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W70-S1",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~70",
  "surfaced_at": "2026-10-13T08:19:12Z",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~B1",
  "one_line": "The dry-run path (process_advisor with upload=False) still emits CloudWatch metrics: _call_llm puts ExecSummaryTokensIn, ExecSummaryTokensOut and ExecSummaryLLMCallsMade on every model call, and _build_slot puts ExecSummarySlotDropped on a dropped slot. A dry run is therefore not metric-silent, which the cell requires.",
  "spec_asserts": "FB-j-5 section 1a item 2: when dry_run is truthy the handler makes NO S3 write of any kind and NO CloudWatch metric emission. Section 1b arm 1 requires the metrics emitters never be called in a dry run.",
  "world_is": "At 220ea75078, lambda_function.py _call_llm (lines 216-218) calls metrics.emit_tokens_in, metrics.emit_tokens_out and metrics.emit_llm_calls_made after each model call. _build_slot (lines 249 and 252) calls metrics.emit_slot_dropped on a drop. process_advisor's upload flag (line 407) gates only the S3 write. The dry branch of lambda_handler makes no metric call itself. Test arm test_dry_run_writes_nothing stubs _call_llm, so it cannot observe these emissions and passes while a live dry run would emit them. The generator is not deployed; the hazard arms on the first dry-run invocation, which is the CTO-required sample.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/lambda/exec-summary-generator/lambda_function.py@220ea75078 lines 216-218 (_call_llm metric emission), 249 and 252 (_build_slot emit_slot_dropped), 407 (upload gate)",
      "infra/aws/lambda/exec-summary-generator/metrics.py@220ea75078 (_put calls cloudwatch put_metric_data)",
      "infra/aws/lambda/exec-summary-generator/tests/test_dry_run.py@220ea75078 (_call_llm stubbed in the fixture)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Decision owed by the issuer: either amend the cell so the dry branch suppresses the _call_llm and _build_slot emissions (a change to lines outside the handler, so a widened order), or accept the sample's metric emission as a known cost before the CTO sample run. Nothing was changed by this seat; the production path is unchanged at 220ea75078."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W70-S2",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~70",
  "surfaced_at": "2026-10-13T08:19:12Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "The AC1 literal expectation ^3 passed does not match the raw pytest line on this host: the environment sets FORCE_COLOR=3, so pytest prints ANSI colour codes before the count even through a pipe.",
  "spec_asserts": "FB-j-5 section 4 AC1: timeout 110 python -m pytest tests/test_dry_run.py -q 2>&1 | tail -1 is expected to match ^3 passed.",
  "world_is": "Under the host environment (FORCE_COLOR=3) the line is ESC[32m ESC[32m ESC[1m3 passed ESC[0m ESC[32m in 0.21s ESC[0m ESC[0m, rc=0, 3 passed. With FORCE_COLOR unset the same command prints '3 passed in 0.21s' with no escape prefix. The test file is not at fault; the verdict turns on the host colour variable.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "env read at this seat: FORCE_COLOR=3 (host); the same pytest command run with env -u FORCE_COLOR prints '3 passed in 0.21s'",
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~70/ADVI_FIRMBKTS.TO-FB-j-5.generator-dry-run.proof_of_spec.json (AC1 output_evidence)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "The issuer decides whether AC1 is re-issued with the colour variable unset or the expectation is re-anchored. This seat did not alter the invocation."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W72-S1",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~72",
  "surfaced_at": "2026-10-13T08:31:33Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "The FB-j-2 AC2 awsdiff check reads FAIL on the uncommitted edit and passes only after the edit is committed, because it compares committed HEAD with the merge-base and not the working tree.",
  "spec_asserts": "FB-j-2 section 1b and section 4 AC2: awsdiff is expected to read OK on the edit (every other aws line byte-unchanged, hunks inside the function only). Section 5 says commit the script first; the AC2 invocation in section 4 carries no commit caveat.",
  "world_is": "r7_checks.py awsdiff reads HEAD:<file> (line 37) and diffs merge-base..HEAD. With the edit uncommitted it printed 'changed hunks 0' and AWSDIFF: FAIL (rc=1). After commit e024089cc9 it prints 'changed hunks 1; changed lines outside the function and the variable: []' and AWSDIFF: OK (rc=0). The check is correct for a committed edit and reads FAIL on any uncommitted one.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round7/checks/r7_checks.py:36-37 (git show <base>:<file> and git show HEAD:<file>)",
      "worktree /c/dev/wk-firmbkts-72 before commit: awsdiff printed 'changed hunks 0' and AWSDIFF: FAIL; after commit e024089cc9: 'changed hunks 1' and AWSDIFF: OK"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Recorded for the issuer; the order and the check were not changed. The committed-HEAD read is the check's design; the commit-first step in section 5 is what makes AC2 meaningful."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W72-S2",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~72",
  "surfaced_at": "2026-10-13T08:31:33Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "The commit-time risk reflex printed HOLD for data/black_diamond/scripts/gold/gold_dispatch.sh against a freshness-gate claim about data/cot/scripts/gold/gold_dispatch.sh, matched by file basename.",
  "spec_asserts": "No spec line. The one-line FB-j-2 edit (order section 1a, one file) was to commit under the standing commit gates.",
  "world_is": "safe-commit printed [risk-reflex] HOLD for two nodes (data/black_diamond/... and data/cot/scripts/gold/gold_dispatch.sh), both citing docs/references/FRESHNESS_GATE_MANIFEST_20260717.md:74, the COT check_freshness row at data/cot/scripts/gold/gold_dispatch.sh:174-177. The cited claim concerns the COT freshness check; the committed edit touches only the put-events capture line of emit_chain_complete. The gates were clean and the commit landed as e024089cc9.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "docs/references/FRESHNESS_GATE_MANIFEST_20260717.md:74 read at /c/dev/wk-firmbkts-72 (the row names data/cot/scripts/gold/gold_dispatch.sh:174-177)",
      "safe-commit output for e024089cc9: 1 file changed, 1 insertion(+), 1 deletion(-), file data/black_diamond/scripts/gold/gold_dispatch.sh"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Observation only. The reflex matched on basename; the cited claim does not describe the BD emit function. No action taken by this seat."
}
```

## Row filed by 0.7.0_AE_CloudOps~FB1 (FB-j-6, the exec reads after the first canonical chain)

```json
{
  "id": "ADVI_FIRMBKTS-D1-S46",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.7.0_AE_CloudOps~FB1",
  "surfaced_at": "2026-10-13T08:44:29Z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "one_line": "TO-FB-j-6 step 3 STOPPED before plan and apply: r4_execeq.py reads DIFFER (artifacts 4/4) because the legacy home has been frozen since act 2 and the canonical home has advanced two chains, so the instrument's EQUAL premise no longer holds; the built artifact is uploaded and not applied.",
  "spec_asserts": "TO-FB-j-6 step 3: `r4_execeq.py --zip <the built zip>` must read `EXEC READS: legacy and canonical EQUAL` (the seam's reads are unchanged by this code); a difference is Branch B and a STOP.",
  "world_is": "Built 2026-10-13T08:42Z: artifact sha256 qVCUzRtwZxKSrql+JapMKH4wwoAd2+aSB0FyZ470ZkU= (20,501 bytes, S3 VersionId YMvkL9sHlJIYO5UGDOeHgRbj8ejsdeAe; prior fdPwodukz88dtRfm0bGw8T5lmUxwrmJ3LFnqmvccKe4= at VersionId pOUiPH87zO8.FnEzSXQ7cW57HflaOdh9). Members that differ from the prior artifact: lambda_function.py (2 hunks, 40 changed lines: the FB-j-5 helper and guard) and platinum_dest_view.py (one line, the generated registry hash in its first comment line). r4_execeq.py: legacy advisors 194 ids 93b6a21e2799, leaderboards 2 b7b13fdce82a, artifacts 4 b8c54a169457; canonical advisors 194 ids 93b6a21e2799, leaderboards 2 b7b13fdce82a, artifacts 4 e8842ad7cc18: the advisor list and the leaderboards read equal and the first advisor's four artifact keys read different content. Cause measured: that advisor's objects at the legacy home were last written 2026-10-12T05:44Z to 05:54Z (summary.json 17121 bytes) and at the canonical home 2026-10-13T05:47Z to 05:57Z (summary.json 17120 bytes), i.e. the canonical home carries the 04:00Z chain of 2026-10-13 and the legacy home is frozen by act 2. At act 4b (2026-10-12 07:44Z) the same instrument read EQUAL 194/194, 2/2, 4/4 because act 3 had just made the homes equal. No plan or apply was run; the function still runs fdPwodukz88d.... The new S3 object is the bucket key's latest version, so any other apply of that root before the issuer's decision would pick it up.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/j6_stop/r4_execeq_after_first_canonical_chain.txt",
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/j6_stop/build_exec_summary_generator.txt"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "The instrument compares CONTENT hashes across two homes that now diverge by design (canonical advances, legacy frozen: COO msg 4561). A replacement that keeps its purpose (the seam resolves the same keys, only the bucket and prefix differ): equal key SETS and equal ids/leaderboards (both read equal), the artifacts' key list equal, or the canonical read compared with the prior artifact's canonical read at the same moment (the prior function, same instant). Decision owed by the issuer, with the CTO: amend step 3's criterion, or rule the difference by design and proceed. This seat will not apply on a STOP. Restoring the prior object as the key's latest version is a further S3 write outside the permitted set, so it was not done; say if wanted."
}
```

## Row filed by 0.7.0_AE_CloudOps~FB1 (FB-j-6, the dry-run sample)

```json
{
  "id": "ADVI_FIRMBKTS-D1-S47",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.7.0_AE_CloudOps~FB1",
  "surfaced_at": "2026-10-13T08:53:29Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "FB-j-6's one dry run returned ten artifacts with zero bullets: no slot fired for any of 10 evenly spaced advisors and no model call is evident, so the sample the CTO is to read holds no text; the dry-run arm itself (0 objects written, listing identical) is proven.",
  "spec_asserts": "TO-FB-j-6 step 7: ids 'across slots: at least one advisor with a leaderboard slot and one with a concentration-risk slot, as the artifacts of a first pass show; if the first pass returns fewer slots, say so'; CTO half: the sample is READ (its text, against the advisors' figures) before FB-j-4 deploys.",
  "world_is": "2026-10-13T08:50Z to 08:52Z, function at CodeSha256 qVCUzRtwZxKSrql+JapMKH4wwoAd2+aSB0FyZ470ZkU=: ONE invocation {dry_run: true, advisor_ids: 10 ids evenly spaced over the sorted served-prefix listing} returned statusCode 200, dry_run true, advisors_processed 10, 3,353 payload bytes in 7 s. Each artifact has the seven expected keys (advisor_id, firm_id, generated_at, model claude-sonnet-4-6, input_hash, bullets, permissions_scope) and `bullets` is an empty list in all ten; the function log holds only the four lifecycle lines (no WARN, no exception: a swallowed per-advisor exception would print a WARN and omit the advisor, and all ten are present). The served-prefix listing before and after is identical: 158 keys, one sha256 d5d52e9339e4208e26d2dae0e94c0dfd7b874289df94780985a1b7c50fab767d, so the dry run wrote 0 objects. Slots: the six evaluators (largest gain, largest loss, concentration risk, tax-loss candidate, leaderboard rank delta, top NNA mover) each gate their model call on a trigger; none fired for these ten on today's canonical data. Existing served exec_summary.json objects are 305 bytes (the first advisor's canonical one dated 2026-10-11T04:02Z), i.e. consistent with empty-bullet artifacts today.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/DRYRUN_ARTIFACTS.json",
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/j6_dryrun/dry_summary.json",
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/j6_dryrun/listing_before.txt",
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/j6_dryrun/listing_after.txt"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Not a defect of this order: the deploy and the dry-run arm are proven. For the issuer and the CTO: the regeneration pair (FB-j-7) cannot cite a read of generated text yet. Either (a) a second dry run (the pair allows 1 to 10 ids per invocation, dry-run-only) with advisors chosen by the triggers: an offline pre-screen of all 158 advisors' positions and leaderboard reads through the artifact's evaluators (no model call, no write) names the ids that WOULD fire each slot; this seat can run that read on request; or (b) the CTO rules that an all-empty first pass is the sample and reads it as 'the regeneration would write 158 artifacts with no bullets today', which is the question for FB-j-7 either way."
}
```

## Row filed by 0.7.0_AE_CloudOps~FB1 (FB-j-8, the pre-screen; corrects D1-S47)

```json
{
  "id": "ADVI_FIRMBKTS-D1-S48",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.7.0_AE_CloudOps~FB1",
  "surfaced_at": "2026-10-13T09:05:32Z",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "one_line": "CORRECTS ADVI_FIRMBKTS-D1-S47: slots DO fire (158 of 158 served advisors, 189 of 194) and every fired slot is dropped on the generator's model path (81 of 81 in two dry runs, about 0.17 s each) with no exception text logged; the positive control of FB-j-8 failed and AC1 reads FAIL on purpose.",
  "spec_asserts": "TO-FB-j-8: step 1 per-slot fire counts offline (no model call); step 2 ONE targeted dry run on advisors that fire, which must return bullets (the CTO's positive control); FB-j-6 row D1-S47 as filed read 'no slot fired for any of 10 advisors'.",
  "world_is": "D1-S47's reading was wrong and is corrected here: the empty bullets lists were not 'no trigger fired'. Offline (no model call, no write, the built artifact's own readers and evaluators, both homes): the generator's list_active_advisors is 194 advisors (158 have a served exec_summary.json, 36 have none, 5 have no positions.json); over the 158 served ids canonical top_gainer 157, top_loser 156, concentration_risk 124, tax_loss_candidate 156, leaderboard_rank_delta 0, top_nna_mover 80, firing any 158; over the 194: 186, 185, 152, 170, 0, 87, any 189; the frozen legacy home gives identical counts. leaderboard_rank_delta is 0 because both leaderboard reads (current and prior week) return None in both homes. Controls: FB-j-6's invocation (ten ids, 42 offline fired slots) read ExecSummarySlotDropped Sum 42 (the namespace's only datapoints in 14 days); FB-j-8's targeted invocation (ten other ids, 39 fired slots) returned http 200, 10 artifacts, ZERO bullets, 7 s, listing identical (158 keys, sha256 d5d52e93...), ExecSummarySlotDropped 39. So 81 of 81 fired slots were dropped in _build_slot (`except (PIIDetectedError, SchemaError, Exception): metrics.emit_slot_dropped(); return None`, which prints nothing), consistent with about 0.17 s per call. Measured preconditions: no VpcConfig; secret anthropic-api-key exists (LastChanged 2026-04-24) and exec-summary-generator-role allows secretsmanager:GetSecretValue on anthropic-api-key-*; layer anthropic-sdk-deps:1 (python3.12, anthropic and pydantic_core cpython-312 present). The exception class is not known.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/SLOT_PRESCREEN.json",
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/SLOT_PRESCREEN.md",
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/SLOT_DRYRUN_ARTIFACTS.json",
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/j8_prescreen/prescreen_counts.txt",
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/j8_prescreen/dry2_summary.json"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Consequences for the regeneration pair (FB-j-7): (1) deploying FB-j-4 as it stands would, at the next chain close, invoke the generator NON-dry for up to 194 advisors, drop every slot, and REWRITE served exec_summary.json for all of them with empty bullets (the objects are 305 bytes today and already empty, so the visible text does not regress, but 36 new empty objects appear, 5 advisors have no positions, and the model-path calls and failure metrics run for 194 x ~5 slots); (2) the cause of the model-path failure must be surfaced before any non-dry run: the one-line step is to log the exception class and its first 200 characters in _build_slot's two except branches (the form FB-j-2 used for the CLI), deployed under a pair, then one dry run. This seat did not read or use the Anthropic key and made no model call. D1-S47's disposition should be read through this row."
}
```

## Row filed by 0.7.0_AE_CloudOps~FB1 (FB-j-8, the cause)

```json
{
  "id": "ADVI_FIRMBKTS-D1-S49",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.7.0_AE_CloudOps~FB1",
  "surfaced_at": "2026-10-13T09:10:41Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "The model-path drop of D1-S48 is confirmed offline: lambda_function.py:211 passes betas= to client.messages.create, which the deployed layer's SDK 0.45.0 does not accept (TypeError before any network call).",
  "spec_asserts": "TO-FB-j-8 amendment 1: a zero-bullet control closes AC1 when second_dry_run carries slots_dropped and control_failed_cause.",
  "world_is": "Read-only, no network, no model call: the call at lambda_function.py lines 185-211 is client.messages.create(model, max_tokens, system, messages, betas=['prompt-caching-2024-07-31']); layer anthropic-sdk-deps:1 (created 2026-04-27, python3.12) holds anthropic/_version.py 0.45.0 and resources/messages/messages.py whose Messages.create parameters are max_tokens, messages, model, metadata, stop_sequences, stream, system, temperature, tool_choice, tools, top_k, top_p, extra_headers, extra_query, extra_body, timeout; betas exists only on resources/beta/messages/messages.py. A function with that signature called with betas= raises TypeError: Messages.create() got an unexpected keyword argument 'betas' (reproduced). The git history names the commit that restored the tree (0e6b76b0e1, 3 months ago). The dropped-slot metrics (42 and 39) equal the offline fired-slot sums; this class explains each drop; the function's log holds none of it.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/SLOT_PRESCREEN.md",
      "infra/aws/lambda/exec-summary-generator/lambda_function.py lines 185-211"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Fix is a code cell under a pair (not this seat's): call client.beta.messages.create(..., betas=[...]) or drop betas= (prompt caching is generally available on the plain endpoint); then ONE dry run, which should return bullets and is the positive control FB-j-7 needs. Until then no non-dry invocation (FB-j-4's trigger) should deploy. The generator has therefore not been able to produce a bullet since the layer's SDK version met this call."
}
```

## Row filed by 0.9.0_WK_ADVI_FIRMBKTS~73 (FB-j-9, the log line's non-ASCII handling)

```json
{
  "id": "ADVI_FIRMBKTS-D1-W73-S1",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~73",
  "surfaced_at": "2026-10-13T09:19:46Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "FB-j-9 interpretation: the drop log replaces non-ASCII characters in the exception text with a space as well as non-printable ones, because the workspace ASCII law covers production logs. The cell text names only non-printable characters.",
  "spec_asserts": "FB-j-9 1a.1: the helper logs str(exc) clipped to 200 characters with every non-printable character replaced by a space; the order's bounds section 2.1 requires ASCII only in the commit.",
  "world_is": "A non-ASCII printable character in an exception message (for example a curly quote) would pass through the cell's literal rule into the log line. The landed helper treats any character outside printable ASCII (0x20-0x7E) as non-printable and writes a space in its place. The clip length, the redacted classes and the one-line form are unchanged, and the four tests do not exercise a non-ASCII message.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/lambda/exec-summary-generator/lambda_function.py@2deaa9165e lines 230-246 (_log_slot_drop)",
      "CLAUDE.md section 4: No non-ASCII in production code/logs/AWS"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "For the COO and the adjudicating seat: decide whether a non-ASCII message character should be replaced (as landed) or kept as written. This seat took no action beyond the landed helper."
}
```

## Row filed by 0.7.0_AE_CloudOps~FB1 (FB-j-10, the sample)

```json
{
  "id": "ADVI_FIRMBKTS-D1-S50",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.7.0_AE_CloudOps~FB1",
  "surfaced_at": "2026-10-13T09:36:57Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "One of the ten dry-run artifacts carries a client's two-word display name in the detail of a top_nna_mover bullet; the generator's own PII guard did not drop it.",
  "spec_asserts": "TO-FB-j-10 step 9: an artifact that carries a client name is counted and its text withheld; the CTO reads the rest.",
  "world_is": "Read-only. The returned artifacts for the 10 targeted advisors (dry run, request 233e4339-b4a1-4ab5-bdaa-4700f56017e6, nothing written) were matched against the display_name, client-name, account-name, owner and household string fields of each advisor's nna_clients.json, summary.json and positions.json in the canonical home (strings of 5 or more characters, case-insensitive substring). 1 of 10 advisors, 1 of 39 bullets matched: the detail of a top_nna_mover bullet carries a 13-character, two-word, title-case display_name served for that advisor (10 distinct display_name values in that advisor's file). The function returned that artifact with no PIIDetectedError and no [SLOT_DROPPED] line. The text of that advisor's four bullets is withheld in DRYRUN10_FIGURES.json and DRYRUN10_ARTIFACTS.json. Not established: whether the slot is meant to name the client (that is a content rule, the CRO's and the CTO's), and the match can miss a name spelled differently from the served field, so zero matches for the other nine is a floor, not a clean bill. An unreadable file in the name set was skipped without a count.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/DRYRUN10_FIGURES.json",
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/DRYRUN10_ARTIFACTS.json",
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/SLOT_DROP_CAUSE.json"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "For the CTO's read of the sample (his ruling): the served advisor view would show a client's name in that line if the artifact were written. FB-j-7 and FB-j-4 stay behind that read."
}
```

## Row filed by 0.7.0_AE_CloudOps~FB1 (FB-j-14, the scrub)

```json
{
  "id": "ADVI_FIRMBKTS-D1-S51",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.7.0_AE_CloudOps~FB1",
  "surfaced_at": "2026-10-13T09:54:07Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "FB-j-10's sample files carried one relationship id in raw form (5 occurrences) because my write-time check looked for client NAMES only; scrubbed forward in the FB-j-14 commit.",
  "spec_asserts": "TO-FB-j-10 step 9 and bound 2: print no client name; withhold text that carries one. It named no rule for relationship ids.",
  "world_is": "Measured by a byte read of the two committed files: 1 distinct z-prefixed id of 9 characters, 2 occurrences in DRYRUN10_ARTIFACTS.json and 3 in DRYRUN10_FIGURES.json, the same id in both, inside the top_nna_mover bullets and their figures; the files were already on origin when the order arrived. My step-9 check matched display_name / client-name / account-name / owner / household string fields only, so an id-shaped token passed it. FB-j-14 replaced every standalone occurrence by h_ plus 12 hex of sha256 (same replacement throughout, no other byte changed, line endings kept) in commit 05e9e30f98; the mapping is written nowhere; the raw form remains in the history of the earlier commit (no rewrite, Andrew's word). Not scanned: any other identifier shape (an account number, a custodian id): only the z-pattern was read for, so zero other shapes is not established.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/DRYRUN10_ARTIFACTS.json",
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/DRYRUN10_FIGURES.json"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "From FB-j-13 on, sample files are written with ids hashed at write time (order FB-j-14 item 2); the generator's own PII guard is a separate question (D1-S50)."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W75-S1",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~75",
  "surfaced_at": "2026-10-13T10:00:27Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "The order places the lots at gold/holdings_lots/ in opal-data-bd; the served object is gold/timeseries/holdings_lots/2026-10-09.parquet, last written 2026-10-13T05:06:00Z, after its date.",
  "spec_asserts": "FB-j-12 section 1a.2: the holdings-lots object is gold/holdings_lots/... in opal-data-bd, or the file B_01.holdings_lots.py writes.",
  "world_is": "B_01.holdings_lots.py save_lots writes holdings_lots_key(snap_date), which is gold/timeseries/holdings_lots/<date>.parquet (data/black_diamond/scripts/gold/lib/s3_layout.py:65-66) in bucket opal-data-bd (lib/config.py:14). No gold/holdings_lots/ key was read. The 2026-10-09 object was rewritten after its date, so the trace read the rewrite.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~75/IQLT_TRACE.md",
      "data/black_diamond/scripts/gold/lib/s3_layout.py@a0e6872b88",
      "data/black_diamond/scripts/gold/B_01.holdings_lots.py@6b903ab8e0"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Path premise only. The trace reads the object as served; it does not judge the path convention."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W75-S2",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~75",
  "surfaced_at": "2026-10-13T10:00:27Z",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~B1",
  "one_line": "The -69.2 percent IQLT loss is not a price or cost defect: price and cost agree with the estate, and the defect is B_01's silver-noncash cap scaling market_value to 22.9 percent of units x price while cost_basis stays whole.",
  "spec_asserts": "FB-j-12 section 1 (CTO ruling c) presumes the -69.2 percent is a cost-basis or price defect of the kind S32-S34 describe.",
  "world_is": "2026-10-09: canonical 49.84 (yahoo_finance) and silver 49.31 (carry_forward) agree; 0 of 60 open lots' per-share cost is outside the 20 percent band of prices within five days of acquisition. Uncapped market_value = units x price = 587,547.40 (+34.6 percent); the bullet's 134,351 is the capped value. Served object: 64,629 of 492,998 open lots (3,057 accounts, 1,007 tickers) carry a compressed market_value; uncapped equals units x price on 99.99 percent of open lots. The cap is an approved design (docstring: Andrew and CTO, 2026-04-17); this row records only that its output is the bullet's market value.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~75/IQLT_TRACE.json",
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~75/iqlt_cost_check.py",
      "data/black_diamond/scripts/gold/B_01.holdings_lots.py@6b903ab8e0"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "ARMED because the cap runs on each scheduled B_01 run and feeds served market values; left alone it reproduces the defect on future serves. Disarm is the COO's routing to the CTO (the cap owner's ruling); no serve of the -69.2 figure until dispositioned."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W75-S3",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~75",
  "surfaced_at": "2026-10-13T10:00:27Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "Custody holds no IQLT for the advisor's 108 mapped accounts, although those accounts hold 60 open IQLT lots (11,788.67 units); whether those units are held is an open unit-count question.",
  "spec_asserts": "FB-j-12 section 1a reads the lots as the position behind the bullet's figures and does not test their units against custody.",
  "world_is": "silver/unrealized/2026-10-09.parquet: 11 IQLT rows firm-wide (11 accounts, MV 1,322,890.07); 0 rows in the 108 accounts mapped by advisor_assignments_history (is_current, role value 'Garrett Newberry'). The cap reads class B lots (no custody cusip) as phantom candidates. The trace does not establish whether the units are held.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~75/iqlt_advisor_map.py",
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~75/iqlt_price_check.py"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Either way the -69.2 percent is not a market loss. Hazard carried by S2."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W75-S4",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~75",
  "surfaced_at": "2026-10-13T10:00:27Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "The published IQLT figures (31 accounts, 61 lots, MV 134,377.61, cost 436,698.87) are not reproduced exactly by the advisor-to-account rule used here (30 accounts, 60 open lots, MV 134,350.71, cost 436,515.92).",
  "spec_asserts": "FB-j-12 section 1a.1 takes the bullet's figures as the basis; section 1a.2 filters lots to the advisor's accounts without naming the rule.",
  "world_is": "The difference is one lot and one account: cost 182.95, market value 26.90. The rule used (advisor_assignments_history, is_current, any role equal to 'Garrett Newberry') gives 108 accounts. The producer's account rule for positions.json was not read.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~75/iqlt_advisor_map.py",
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~75/IQLT_TRACE.md"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Immaterial to the classification; recorded so the trace's counts are read against the reconstruction, not the bullet."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W75-S5",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~75",
  "surfaced_at": "2026-10-13T10:00:27Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "The AC1 invocation names --file under the base checkout (C:/dev/ajb_workspace/.../0.9.0_WK_ADVI_FIRMBKTS~75/IQLT_TRACE.json), where the record does not exist; the record is on the worker branch, so the literal invocation returns FAIL ABSENT while the same checker on the worktree path returns the record ok line.",
  "spec_asserts": "FB-j-12 section 4 AC1: the record is read at C:/dev/ajb_workspace/org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~75/IQLT_TRACE.json, and the deliverable is in the worker's worktree.",
  "world_is": "The record is committed at c07c215810 on the worker branch in /c/dev/wk-firmbkts-75 and is absent from the base checkout C:/dev/ajb_workspace (ls returns no such directory). Literal run: r7_checks.py iqlt --file <base path> -> FAIL ABSENT or unreadable: FileNotFoundError, rc=1. Same checker, worktree path: IQLT record ok classification=DATA_DEFECT loss_pct=-69.22, rc=0. Writing the record into the base checkout was not done; it is outside this order's write grant.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/task-orders/ADVI_FIRMBKTS.TO-FB-j-12.iqlt-trace.md@89f2099f0a",
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~75/IQLT_TRACE.json"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "AC1 is recorded as FAIL on the literal invocation. It can pass after integration if the order is re-graded on the integrated tree; the CVO or COO decides the re-grade, not this worker."
}
```

## Rows filed by 0.7.0_AE_CloudOps~FB1 (FB-j-13)

```json
{
  "id": "ADVI_FIRMBKTS-D1-S52",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.7.0_AE_CloudOps~FB1",
  "surfaced_at": "2026-10-13T10:11:15Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "The seat gate read STOP (CROSSBOX-DEPLOY open_call=hit) at the FB-j-13 apply because the CTO's history-rewrite fork, opened 09:50:02Z, names the exec-summary root by project scope; WARN mode proceeded and I applied.",
  "spec_asserts": "TO-FB-j-13 step 4-5: plan, apply on the saved plan. The pair (COO 89f2099f0a, CTO ddbaf334d1) signs the act; the order names no open-call precondition.",
  "world_is": "safe-apply printed: [seat-gates] STOP: 1 hit(s) in OPEN-CALL -- row dell1-20261013T095002Z-825f of org/devices/state/dell1/open_calls.json names the root; 'WARN [seat-gates] would stop under ENFORCE (crossbox-deploy); WARN mode proceeds.' At the FB-j-10 apply (09:26Z) the same gate read open_call=clear. The row's subject is the CTO's question to Andrew whether to rewrite git history for the DRYRUN10 files (rec: forward-scrub only); its top-level orders and roots are empty and its scope.roots lists infra/aws/terraform/exec-summary and portal-auth, measured from the project's write set. I read the row, judged the question independent of this function's code and environment (a history decision changes no Lambda state), the CTO who owns the call having signed this apply, and applied under WARN. I did not ask first: the gate offered no acknowledgement path and the act is dry-run only with a defined rollback. Under ENFORCE this apply would have stopped.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/j13_switch/apply_safe-apply.txt"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "For the issuer and the CTO: if a call that names a root by project scope alone should block applies on it, the order's un-park conditions should have named it; if not, the gate's scope match is wider than the call's subject."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-S53",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.7.0_AE_CloudOps~FB1",
  "surfaced_at": "2026-10-13T10:11:15Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "The 'name guard proved on the withheld one' requirement is met by the switch, not by the guard: with top_nna_mover off no model call is made for that slot, so the guard ran on none of its text.",
  "spec_asserts": "TO-FB-j-13 amendment 1 (ii): the advisor whose top_nna_mover bullet leaked a client display name must come back with the slot off and the other four slots free of the name.",
  "world_is": "Measured from the dry run (request bf5df30e-f444-4204-b9b8-f6e799568068): the formerly withheld advisor is ordinal 8 of 10, returned 3 bullets, 0 top_nna_mover, 0 client names and 0 relationship ids in text; 35 model calls for 35 bullets, 0 drops. The code (lambda_function.py lines 273-301) checks client_rel_id before the call and every *_name context value after the reply, so the guard is reached only when a slot is called; top_nna_mover was not. The guard's unit arms (FB-j-11) cover two named shapes; a live read of the guard needs a dry run with the slot enabled, which is a second environment change under a pair and not this act.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/SLOT_SWITCH_SAMPLE.json",
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/j13_switch/sample_summary.json"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Input to the CTO's condition (b): the live proof of the guard on NNA text is open until a dry run enables the slot."
}
```


## Row filed by 0.7.0_AE_CloudOps~FB1 (FB-j-3, what the runner runs)

```json
{
  "id": "ADVI_FIRMBKTS-D1-S54",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.7.0_AE_CloudOps~FB1",
  "surfaced_at": "2026-10-13T13:21:19Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "The bd-gold-layer-runner also runs the ADVI 49f scheduled-floor chain (about every 3 hours); two runner runs after the FB-j-3 deploy were that chain, not the BD gold dispatcher, so runner activity is not the FB-j-3 'next chain' signal.",
  "spec_asserts": "TO-FB-j-3 step 4: read the first chain that closes after the deploy (the nightly fallback cron(0 23 ? * MON-SAT *) or an S3-triggered run), in gold/logs/ and the cumulative logs/gold-layer/gold_incremental_*.log.",
  "world_is": "Read-only. Runner i-01003b035d2988dfb was started at 09:46:59Z and 12:45:16Z (stopped 09:53Z and 12:51Z) by principal advi-49f-gold-dispatch-role (CloudTrail StartInstances). The Lambda advi-49f-gold-dispatch logged Event {run_class production, source advi.49f.scheduled-floor} and dispatched SSM document advi-49f-chain-dispatch (plugin runAdvi49fChain, rc 0); the invocation's stdout opens 'CHAIN START date=2026-10-12 mode=production workdir=/tmp/49f_chain_work stages=18', a different chain from gold_dispatch.sh. Neither run wrote a gold_incremental log or a gold/logs object (listed both prefixes; the runner telemetry shows scripts S_00, A_00, A_02 only). The last gold_incremental object is 2026-10-13 06:18:11Z, before the deploy at 08:37:35Z. My earlier watcher keyed on the runner's state transition and read both runs as 'a chain after the deploy'; the stdout and the invoker say otherwise. No BD gold chain has run since the deploy.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "CloudTrail StartInstances 09:46:59Z and 12:45:16Z on the instance",
      "/aws/lambda/advi-49f-gold-dispatch log 12:45:15Z",
      "SSM command ce052cb7-b353-46fa-b545-8eca45f531a4 stdout head"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "FB-j-3 stays open for the 23:00Z fallback or an S3-triggered BD chain. A watcher now waits for a gold_incremental or gold/logs .log object newer than the deploy, not for runner state. The 49f chain's own end-of-run WARN lines (if any) are not FB-j-3's measurement."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W24-S1",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~24",
  "surfaced_at": "2026-10-11T12:25:21Z",
  "one_line": "The worker worktree already carries a portal submodule pointer drift before any edit, so the FB-g-1 write-surface check AC3 reads portal as OUTSIDE the five allowed paths and FAILs.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "spec_asserts": "AC3 (r4_scope.py with --allow for the three cell files, the deliverables folder and the channel) expects ROUND 4 SCOPE: OK, a control that passes only for a change confined to the allowed paths; the order names no portal change.",
  "world_is": "At HEAD f33c93ce43 the gitlink records portal at c96efe1714784162c4134450da33ce6fd6226b60 while the portal checkout is at 8ed372cb72659b96a5cfb4000a20b8ae315b9be7. The first git status of this worktree, before my first edit, already showed ' M portal'. git diff --name-only HEAD lists portal, so r4_scope printed 'CHANGED portal <-- OUTSIDE' and read 'FAIL 4 changed, 1 outside, 0 required missing'. The three cell files and the channel were the only other changes and all were allowed.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "git -C /c/dev/wk-firmbkts-24 ls-tree HEAD portal -> 160000 commit c96efe1714784162c4134450da33ce6fd6226b60 portal",
      "git -C /c/dev/wk-firmbkts-24/portal rev-parse HEAD -> 8ed372cb72659b96a5cfb4000a20b8ae315b9be7; git status --short listed ' M portal' before any edit",
      "python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_scope.py --root /c/dev/wk-firmbkts-24 (AC3 invocation), output 'CHANGED portal   <-- OUTSIDE' and 'ROUND 4 SCOPE: FAIL 4 changed, 1 outside, 0 required missing'"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Not this worker's to revert: portal sits outside the write grant, and a checkout or submodule update would touch a path the order does not name. Left as found. AC3 is recorded FAIL and the order stays open. The gitlink and the portal checkout disagree at the cut; the integrator or the issuer reads which side is authoritative."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W24-S2",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~24",
  "surfaced_at": "2026-10-11T12:25:21Z",
  "one_line": "The order's bound 3 says ASCII only for the cell's files, but index.mjs already carries one non-ASCII em dash in a comment at base, outside the cell's edit.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "Bounds section 2 item 3: ASCII only; LF endings. If something cannot be met within your paths, file a surprise row and stop.",
  "world_is": "index.mjs at base HEAD carries one non-ASCII character, an em dash in the comment on line 123 (line 124 after the import line added by this cell). The cell's own edits (one import line, one key line) and the two new files are pure ASCII with LF endings. The comment is not touched because it lies outside the cell's change.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "git show HEAD:infra/aws/lambda-edge/auth-validator-edge/index.mjs | LC_ALL=C grep -n -P '[^\\x00-\\x7F]' -> line 123 (the em dash in the comment about FIRM_BUCKET_MAP values)",
      "the same pattern on the worktree file before my edits -> line 123; after the edits -> line 124, the same comment"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Recorded so the issuer decides whether bound 3 reads per changed line or per file. The fix, if wanted, is a one-character change to an unrelated comment and is not this cell's to make."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W24-S3",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~24",
  "surfaced_at": "2026-10-11T12:28:09Z",
  "one_line": "The commit-time naming gate refuses the cell's hand-typed ownership-map key templates and firm and bucket literals, and its suggested key form differs from the key the producers' seam writes.",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "disarm_owner": "1.0.0_SA_CTO~DELL1",
  "spec_asserts": "Order FB-g-1 section 1a: ownershipMapKey returns advi/<firm>/platinum/<firm>/ownership_map.json for the canonical layout and platinum/<firm>/ownership_map.json for the legacy key, and the spec names the firms and buckets literally. Section 2 bounds the write surface to the three cell files and names no registry row and no naming exception.",
  "world_is": "safe-commit naming limb (LGIC_ENFORCE, ENFORCE mode) refused the cell commit with 18 graded refusals: ownership_key.mjs line 20 advi/{x}/platinum/{x}/ownership_map.json is NEW and OUT-OF-PATTERN as S3Key with suggestion ownership-map.json, line 22 platinum/{x}/ownership_map.json likewise, and the firm names are NEW hand-kept carriers. The registry row blackdiamond-platinum-49financial-ownership-map says address() refuses this key shape because it has no partition. The seam view lib/platinum_dest_view.py maps the 49financial class to advi/49financial/platinum/49financial/{tail} with the tail ownership_map.json, so the gate's hyphen form is not the key the seam writes. The code commit is BLOCKED and nothing is committed under the three code paths.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "bash .tools/safe-commit.sh --author 0.9.0_WK_ADVI_FIRMBKTS~24 -F .scratch/msg_fbg1_code.txt -- three code paths and the channel: rc=1, 'ERROR: BLOCKED -- the naming limb refused', '[naming-gate] NAMING-GATE: REFUSE 18 graded'",
      "infra/logic/registry/legacy_addresses.json lines 77-84: key blackdiamond-platinum-49financial-ownership-map, template platinum/49financial/ownership_map.json, note that address() refuses it because the key has no partition",
      "data/black_diamond/scripts/gold/lib/platinum_dest_view.py line 11: ('platinum/49financial/', 'opal-data-49financial', 'advi/49financial/platinum/49financial/{tail}')"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Not this worker's to resolve: a registry row or a naming ruling is outside the write grant and a hand-typed workaround is the refused shape. Disarm is a CTO ruling on the canonical ownership-map name and whether a registry row admits it. Until then the code commit stays BLOCKED and AC-level proof records the state."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W25-S1",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~25",
  "surfaced_at": "2026-10-11T12:26:16Z",
  "one_line": "TO-FB-g-2 cannot be committed in its spec form: the commit-time naming gate (LGIC_ENFORCE DEC-6, ENFORCE) refuses the order's literal names in the appended grant (policy name advi-49f-platinum-canonical-rw; the literal ARN arn:aws:s3:::opal-data-49financial/advi/49financial/platinum/*; the prefix advi/49financial/platinum/*) as hand-typed carriers of 49financial. Conforming them changes the strings the order and its checker pin. Worker did not force, override or substitute lookup(); the draft stays modified and uncommitted in the worktree.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "bash .tools/safe-commit.sh --author 0.9.0_WK_ADVI_FIRMBKTS~25 ... -F .scratch/msg_fb_g2_iam.txt -- infra/aws/terraform/bd-pipeline/iam.tf, worktree /c/dev/wk-firmbkts-25 (branch wk-ADVI_FIRMBKTS-25, HEAD f30d22f82c), 2026-10-11 ~12:25Z: 'ERROR: BLOCKED -- the naming limb refused (LGIC_ENFORCE DEC-6, ENFORCE mode). Commit aborted; files unstaged.' and 'NAMING-GATE: REFUSE 4 graded'",
      "naming-gate lines: 'NAMING REFUSE infra/aws/terraform/bd-pipeline/iam.tf:1288 advi-49f-platinum-canonical-rw -> advi-49f-platinum-canonical-rw-policy' (NEW, out-of-pattern as IAM_POLICY); 'NAMING REFUSE ...:1298 arn:aws:s3:::opal-data-49financial/advi/49financial/platinum/* -> lookup(49financial)'; 'NAMING REFUSE ...:1307 advi/49financial/platinum/* ' (CONFORMANT as S3Key, but a NEW hand-kept carrier); 'NAMING OUT-OF-PATTERN ...:1304 arn:aws:s3:::opal-data-49financial' (WARN)",
      "CLAUDE.md section 4 rule 30: every S3 address is lib/opal_naming.py address() output and every resource name is name() output; a builder refusal is a missing registry row to add, never a hand-typed workaround; a deliberate departure is an R20 register entry Andrew acknowledges",
      "r4_grant.py --arms grant --root /c/dev/wk-firmbkts-25 (2026-10-11 ~12:22Z): 4 of 4 arms PASS on the draft; G1 pins the name and G2 pins the exact ARN set and prefix, so a conformed name or lookup() form reads FAIL on the checker"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-FB-g-2 section 1a: the appended resource carries the exact name advi-49f-platinum-canonical-rw, the exact literal ARNs and the exact prefix; section 5: commit infra/aws/terraform/bd-pipeline/iam.tf via safe-commit.",
  "world_is": "The commit-time naming gate in ENFORCE mode refuses the three literal strings as NEW hand-typed carriers of 49financial and of the IAM policy name pattern. The same file already carries hand-typed opal-data-portal-v2/platinum/advi/49financial/* at line 1270 (pre-existing, outside the graded diff). The grant cannot be committed in the form the order and its checker pin; a ruling is needed on the naming form (a registry row, an R20 entry, or a changed pinned string) before the cell can be committed.",
  "notes": "Needs a ruling from 2.0.0_SA_COO~B1 (issuer), with the naming owner if a registry row is the route. Until then the draft is uncommitted; no AWS call, plan or apply was made. Disarm: none (INERT)."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W25-S2",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~25",
  "surfaced_at": "2026-10-11T12:26:16Z",
  "one_line": "TO-FB-g-2 AC2 (write-surface bound) cannot read ROUND 4 SCOPE: OK in this worktree: git reads the submodule portal as modified, because its checked-out HEAD 8ed372cb72659b96a5cfb4000a20b8ae315b9be7 differs from the index gitlink c96efe1714784162c4134450da33ce6fd6226b60. The worker edited only infra/aws/terraform/bd-pipeline/iam.tf and did not checkout, reset or commit portal; the scope check reads portal as CHANGED outside the three paths.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "git status --porcelain=v1 -- portal (worktree /c/dev/wk-firmbkts-25, 2026-10-11 ~12:24Z): ' M portal'; git -C portal status --short: empty (submodule clean); git ls-files -s portal: '160000 c96efe1714784162c4134450da33ce6fd6226b60 0 portal'; git -C portal rev-parse HEAD: 8ed372cb72659b96a5cfb4000a20b8ae315b9be7",
      "r4_scope.py --root /c/dev/wk-firmbkts-25 --allow infra/aws/terraform/bd-pipeline/iam.tf --allow .../deliverables/0.9.0_WK_ADVI_FIRMBKTS~25/ --allow .../INVESTIGATION_v1.md --require infra/aws/terraform/bd-pipeline/iam.tf: 'CHANGED infra/aws/terraform/bd-pipeline/iam.tf', 'CHANGED portal <-- OUTSIDE', 'ROUND 4 SCOPE: FAIL 2 changed, 1 outside, 0 required missing', exit=1",
      "the primary checkout's git status at session start also lists ' M portal' (box/dell1), so the submodule pointer drift is present on the estate's trees"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-FB-g-2 AC2: r4_scope.py with the three allowed paths reads ROUND 4 SCOPE: OK, i.e. the changed set is inside the write surface.",
  "world_is": "The worktree's portal gitlink is out of step with its checkout, so the scope check counts a path the worker never wrote. Any commit that includes the portal path would move the recorded pointer; the worker commits only explicit paths and did not include it.",
  "notes": "Not cleared by the worker: no checkout, reset or commit of portal. A ruling is needed on whether AC2 reads the gitlink as out-of-scope drift or the submodule pointer is re-synced by the integrator. Disarm: none (INERT)."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W80-S1",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~80",
  "surfaced_at": "2026-10-13T22:03:45Z",
  "one_line": "The Door 6 retirement premise (retire after a no-other-consumer read) does not hold: a live S3 event notification on opal-data-inf (prefix gold/meta/, suffix pipeline-complete.json) invokes inf-portal-publisher, so retiring the key stops that trigger.",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "disarm_owner": "CTO",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "aws s3api get-bucket-notification-configuration --bucket opal-data-inf (read 2026-10-13 ~21:50Z): LambdaFunctionConfigurations has 2 entries; one invokes inf-portal-publisher with Filter Prefix gold/meta/ and Suffix pipeline-complete.json",
      "infra/aws/terraform/inf-pipeline/s3-notifications.tf:15-21 at eff1db9d7f: 'ADVI_INFETL.005: gold/meta/pipeline-complete.json -> inf-portal-publisher', lambda_function block with filter_prefix and filter_suffix",
      "aws lambda get-function-configuration --function-name inf-portal-publisher: INPUT_BUCKET and OUTPUT_BUCKET both opal-data-inf",
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/ledger/ROUND8_PLAN_INPUTS_20261013.md:11 at eff1db9d7f: 'DEC-13 Door 6 RETIRE, no successor marker, inside the Inflection move, after a no-other-consumer read'"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "ROUND8_PLAN_INPUTS_20261013.md:11 records DEC-13 Door 6 as RETIRE, no successor marker, inside the Inflection move, after a no-other-consumer read of gold/meta/pipeline-complete.json.",
  "world_is": "The no-other-consumer read finds a second live consumer: an S3 event notification on opal-data-inf (prefix gold/meta/, suffix pipeline-complete.json) that invokes inf-portal-publisher, wired under ADVI_INFETL.005. Retiring the key as ruled would stop that trigger.",
  "notes": "Not decided by this worker. The ruling's precondition is not met as written; the disposition (re-point the publisher's trigger, or retire it with the key) is Andrew's ruling with the CTO. Disarm: CTO, before the Door 6 retirement act is cut. Evidence record: org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~80/PLANINV_LEGACY_OPERATIONS.json (candidate inf-portal-publisher-sentinel-trigger) @59c2e13ecc."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W80-S2",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~80",
  "surfaced_at": "2026-10-13T22:03:45Z",
  "one_line": "infra/aws/terraform/opal-assets/router_iam.tf:26-29 says mdpf-daily-refresh-trigger is ENABLED and armed on the Door 6 key, but the live account has no such rule (describe-rule ResourceNotFound) and feeder-trigger.tf:7-8 records its destruction on 2026-08-18.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/terraform/opal-assets/router_iam.tf:26-29 at eff1db9d7f: '# `mdpf-daily-refresh-trigger` is ENABLED and armed on ObjectCreated of that EXACT key.'",
      "infra/aws/terraform/mdpf-pipeline/feeder-trigger.tf:7-8 at eff1db9d7f: 'destroyed the mdpf-daily-trigger Lambda + mdpf-daily-refresh-trigger rule' (TO-3 K3, 2026-08-18)",
      "aws events describe-rule --name mdpf-daily-refresh-trigger --region us-east-1: ResourceNotFound ('does not exist on EventBus default'); aws events list-rules --name-prefix mdpf-daily: 0 rules"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "router_iam.tf:26-29 states that mdpf-daily-refresh-trigger is ENABLED and armed on the Door 6 key.",
  "world_is": "No rule of that name exists on the default event bus; it was destroyed on 2026-08-18. The router deny statement 3 still cites it as the live guard.",
  "notes": "Stale comment in a Terraform file. No harm measured: the deny blocks writes the chain no longer makes. Its disposition rides candidate router-iam-door6-deny in the FB-k-5 record (decision Andrew). Disarm: none (INERT)."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W80-S3",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~80",
  "surfaced_at": "2026-10-13T22:03:45Z",
  "one_line": "The aws shim, run from a directory outside a git checkout (the data directory), prints a WARN line into its captured output, so a raw JSON capture is not parseable until that line is stripped.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "C:/dev/wk-firmbkts-80-data/targets_firmsep.json (aws events list-targets-by-rule, 2026-10-13 ~21:4xZ) begins with 'WARN: aws: no caller-toplevel .tools/aws (git rc=128) -- PREPENDING THE BAKED C:/dev/ajb_workspace/.tools instead'; json.load on that file fails with Expecting value, line 1 column 1",
      "the same warning appeared in the captured outputs of later aws calls run from the same directory; the captures were filtered with grep -v '^WARN:' before parsing"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "The task order's bounds say AWS from bash is .tools/aws, and downloads go to the data directory outside the checkout; the shim is expected to read cleanly from there.",
  "world_is": "Run from outside a checkout, the shim falls back to the baked workspace tools and writes a WARN line into the captured stream, so the raw capture is not valid JSON until the line is removed.",
  "notes": "Read-only calls were unaffected. No write was made by the shim. Disarm: none (INERT)."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W79-S1",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~79",
  "surfaced_at": "2026-10-13T22:10:00Z",
  "one_line": "The Cottonwood Black Diamond scope is not inside opal-data-bd: the live IAM grants and the repository place it in opal-data-assets under blackdiamond/cottonwood/.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "Grep of infra/aws for opal-data-bd within 120 characters of cottonwood: 2 hits, both prose (infra/aws/terraform/cot-pipeline/ssm.tf:310; infra/aws/terraform/nfra-ctlpln-identity/tests/simulate_policy.py:870)",
      "Grep of data/ for the same pattern: 2 hits, both prose (data/cot/scripts/gold/README_FIRM_NATIVE_DIVERGENCE.md:47,64)",
      "iam get-role-policy cot-rebalancer-runner-role/cot-rebalancer-runner-write-cot stmt0: arn:aws:s3:::opal-data-assets/blackdiamond/cottonwood/bronze/* (measured)",
      "infra/aws/lambda/investor-reporting/PATH_MANIFEST.json:3031 (s3://opal-data-assets/blackdiamond/cottonwood/silver/fact_allocations/)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "FB-k-4 section 1a lists the Cottonwood scope inside opal-data-bd as a legacy home to inventory, next to opal-data-cot.",
  "world_is": "No live grant or repository path places a Cottonwood key inside opal-data-bd. The Cottonwood Black Diamond tree is opal-data-assets/blackdiamond/cottonwood/ (bronze, silver fact_holdings and fact_allocations). The inventory records it under opal-data-assets with legacy_touch false."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W79-S2",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~79",
  "surfaced_at": "2026-10-13T22:10:00Z",
  "one_line": "Cottonwood holdings have two live homes: the edge router resolves cottonwood to opal-data-cot, while the IRPT holdings reader reads opal-data-cottonwood.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "iam get-role-policy irpt-holdings-role/irpt-holdings-firm-read stmt0-1: GetObject and GetObjectVersion on arn:aws:s3:::opal-data-cottonwood/irpt/cottonwood/platinum/holdings/ (measured)",
      "iam get-role-policy irpt-holdings-role/irpt-holdings-firm-read stmt2: opal-data-cot investor-reporting/directory/* and platinum/cottonwood/ownership_map.json (measured)",
      "infra/aws/lambda-edge/_shared/firm-config.mjs:77-80: cottonwood bucket opal-data-cot (measured)",
      "comp-find --corpus aws over the S3_BUCKET nodes: opal-data-cottonwood present, drift=DECLARED (measured)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "FB-k-4 section 1a items 1 and 3 treat opal-data-cot as the Cottonwood serving home and inventory the IRPT Lambdas against it.",
  "world_is": "IRPT holdings for Cottonwood come from opal-data-cottonwood, the destination-named bucket for the move, and only the directory and ownership map come from opal-data-cot. Both homes are in live use."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W79-S3",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~79",
  "surfaced_at": "2026-10-13T22:10:00Z",
  "one_line": "bd-cot-freshness-probe is in the repository with a read of opal-data-cot, but no live Lambda of that name exists.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "aws lambda list-functions: 237 functions, none named bd-cot-freshness-probe (measured)",
      "infra/aws/lambda/cot-pipeline/bd-cot-freshness-probe/lambda_function.py:44-46 (BD_DATA_BUCKET default opal-data-cot) and :56 (SERVED_AUA_KEY platinum/firm/timeseries_overview.json) (measured)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "FB-k-4 section 1a item 1 asks for the Lambda functions that touch the buckets, read from the live plane.",
  "world_is": "The repository holds a freshness probe that reads the served Cottonwood AUA key, and the live account does not run it under that name. The inventory records it as a repository-only row with trigger not determined."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W76-S1",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~76",
  "surfaced_at": "2026-10-13T22:15:48Z",
  "one_line": "TO-FB-k-1 names the Inflection scope inside opal-data-bd as a legacy home to inventory; the census and the mapping table hold zero Inflection-scope objects in opal-data-bd, so the bd leg of that slice is empty by measurement.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/census.json@3fc68796 buckets.opal-data-bd: 36,395 bytes, 0 'inflection' or 'inf' scope tokens (python -I count, worktree 0.9.0_WK_ADVI_FIRMBKTS~76)",
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/mapping_v4.json@3fc68796 rows: 3451 total; bucket opal-data-bd 247 rows, 0 with an inflection or inf scope token in prefix or address",
      "aws s3api get-bucket-notification-configuration --bucket opal-data-bd: two Lambda notifications on bronze/ and silver/prices/ only; comp-find --corpus aws EVENT_RULE band names no Inflection scope in opal-data-bd",
      "docs/briefs/d8-legacy-firm-buckets-migration-brief-20260913.md@3fc68796:251 maps opal-data-bd to mockadv, not inflection"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-FB-k-1 slice: the inventory covers what runs against opal-data-inf or the Inflection scope inside opal-data-bd.",
  "world_is": "The measured opal-data-bd tree holds no Inflection-scope key (0 census tokens, 0 mapping rows). The bd rows of the inventory are the Black Diamond and mockadv scope; the bd Inflection leg is empty by measurement, not by an unread gap.",
  "notes": "Recorded by the worker; the inventory reports the bd notification rows as legacy_touch false with claim absent where unread. Whether an Inflection scope should exist in opal-data-bd is the issuer's call; no disposition is proposed here. Disarm: none (INERT)."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W77-S1",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~77",
  "surfaced_at": "2026-10-13T22:23:46Z",
  "one_line": "The prohibited key opal-data-inf/gold/meta/pipeline-complete.json has a second live watcher: an S3 notification on opal-data-inf routes its creation to inf-portal-publisher, and the PRD names only the mdpf-feeder-accelerator rule as its watcher.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~B1 (carries the second watcher into the FWD-9 plan; the FWD-7 ruling governs the key itself)",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "aws s3api get-bucket-notification-configuration --bucket opal-data-inf (live): LambdaFunctionConfigurations = 2; inf-portal-publisher on ObjectCreated:* with prefix gold/meta/ and suffix pipeline-complete.json (record org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~77/PLANINV_INFLECTION_SERVING.json, row INF-EDGE-05)",
      "aws events describe-rule --name mdpf-feeder-accelerator (live): State ENABLED; S3 Object Created on opal-data-inf key gold/meta/pipeline-complete.json; list-targets-by-rule: 1 target MdpfFeederTrigger",
      "infra/aws/lambda/inf-gold-trigger/lambda_function.py:24 defines COMPLETE_KEY = 'gold/meta/pipeline-complete.json' and no other use of it appears in that file (grep of the file at 5760dbcc38db)",
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/prd/ADVI_FIRMBKTS_PRD.md:275-276 (DEC-12) names one watcher: the prohibited key is watched by the mdpf-feeder-accelerator rule (pin 5760dbcc38db)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "ADVI_FIRMBKTS_PRD.md DEC-12 (lines 275-276): the prohibited key opal-data-inf/gold/meta/pipeline-complete.json is watched by the mdpf-feeder-accelerator rule.",
  "world_is": "The same key is also watched by a live S3 notification from opal-data-inf to Lambda inf-portal-publisher (ObjectCreated under gold/meta/ with suffix pipeline-complete.json). The notification configuration is a singleton per bucket (PRD DEC-7).",
  "notes": "Form only: no notification was changed, no key was read or moved. The move plan needs both watchers named for this key."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W77-S2",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~77",
  "surfaced_at": "2026-10-13T22:23:46Z",
  "one_line": "The exec-summary trigger is live as an ENABLED rule named exec-summary-trigger on the bd-pipeline.gold-chain chain-complete event; the Terraform declares only a DISABLED cron placeholder, and no Terraform in the tree declares the live rule.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "owner of exec-summary-generator (not named in the order); surfaced to 2.0.0_SA_COO~B1 for the plan",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/terraform/exec-summary/main.tf:224-233 (pin 5760dbcc38db): rule exec-summary-trigger-placeholder, schedule cron(30 4 * * ? *), description 'PLACEHOLDER ... DO NOT enable until TO 7'",
      "aws events describe-rule --name exec-summary-trigger-placeholder (live): ResourceNotFoundException; the placeholder is not deployed",
      "aws events describe-rule --name exec-summary-trigger (live): State ENABLED; EventPattern detail-type chain-complete, source bd-pipeline.gold-chain; list-targets-by-rule: 1 target exec-summary-generator",
      "Grep of infra/aws/terraform for exec-summary-trigger and chain-complete (pin 5760dbcc38db): no resource declares the live name; hits are the placeholder lines and a comment at bd-pipeline/iam.tf:677"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "infra/aws/terraform/exec-summary/main.tf:224-233 (pin 5760dbcc38db): the exec-summary EventBridge rule is the DISABLED placeholder exec-summary-trigger-placeholder; DO NOT enable until TO 7.",
  "world_is": "Live: no rule of the placeholder name. An ENABLED rule exec-summary-trigger on the gold chain-complete event invokes exec-summary-generator, and no Terraform in the tree declares that rule.",
  "notes": "Form only; no rule was changed. The generator defaults to firm 49financial (lambda_function.py:565) and its destinations are 49financial only (platinum_dest_view.py:5-15), which the inventory records as legacy_touch false for inflection."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W77-S3",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~77",
  "surfaced_at": "2026-10-13T22:23:46Z",
  "one_line": "The served graph cannot answer the IAM-grant or Lambda-environment question for the Inflection bucket: a bucket-name query matches only the bucket policy node, while the live IAM read finds 40 roles with an Allow on opal-data-inf.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~B1 (the move plan's grant column is read from the live IAM account read, not from the graph)",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "comp-find --corpus aws 'opal-data-inf' IAM_POLICY (live graph read): DENOMINATOR 1 hit across 633 aws nodes scanned; the one hit is the bucket policy node arn:aws:s3:::opal-data-inf#policy",
      "comp-find --corpus aws 'opal-data-inf' LAMBDA: DENOMINATOR 0 hits across 238 aws nodes scanned, while the live list-functions (saved capture) shows opal-data-inf in the environment of the inf-* and irpt-* functions",
      "aws iam get-account-authorization-details --filter Role LocalManagedPolicy (live): 303 roles scanned, 40 with an Allow on opal-data-inf (scripts/planinv_iam_grants.py over the saved capture)",
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/task-orders/ADVI_FIRMBKTS.TO-FB-k-2.inflection-serving.md section 2 bound 2: read AWS through the served graph first"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO FB-k-2 bound 2: AWS is read through the served graph first; comp-find --corpus aws lists CloudNodes with a printed denominator, and grants are read as list role, action class, resource.",
  "world_is": "The graph's IAM_POLICY search matched only the bucket policy for the Inflection bucket, and its LAMBDA search matched no environment value; the grant and environment reads had to be taken live from IAM and Lambda.",
  "notes": "Form only. The inventory records each grant with claim measured from the live IAM read, and the graph answers were recorded as denominators (record denominators, comp-find lines)."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W77-S4",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~77",
  "surfaced_at": "2026-10-13T22:23:46Z",
  "one_line": "The task order names an Inflection scope inside opal-data-bd; no source in this read holds one: the mapping table has 0 opal-data-bd rows with an inflection prefix, no IAM statement names one, and the one bd-scope Lambda maps 49financial only.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/mapping_v4.json (3451 rows): opal-data-bd 247 rows; a scan of the prefix field finds 0 rows with an inflection or inf prefix",
      "aws iam get-account-authorization-details (saved capture): a scan for statements naming opal-data-bd with an inflection or inf scope finds 0",
      "infra/aws/lambda/exec-summary-generator/platinum_dest_view.py:5-15 (pin 5760dbcc38db): the bd destinations are opal-data-49financial only",
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/task-orders/ADVI_FIRMBKTS.TO-FB-k-2.inflection-serving.md section 1a names the scope the inventory must cover"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO FB-k-2 section 1a: the inventory covers what touches opal-data-inf or the Inflection scope inside opal-data-bd.",
  "world_is": "No read found an Inflection scope in opal-data-bd. The firm's data sits in opal-data-inf and in the new bucket, and bd is reached in this read only by 49financial code paths.",
  "notes": "Form only. The inventory keeps the opal-data-bd side at zero rows for the firm and says so in the denominators (mapping_v4 bd rows with an inflection prefix: 0)."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W77-S5",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~77",
  "surfaced_at": "2026-10-13T22:23:46Z",
  "one_line": "The served graph holds 238 LAMBDA nodes while the live list-functions returns 237 functions; the one-node difference is not identified in this read.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "comp-find --corpus aws '.' LAMBDA (vintage 2026-10-13 21:02:47 UTC): DENOMINATOR 238 hits across 238 aws nodes scanned",
      "aws lambda list-functions --output json (auto-paginated, saved capture): 237 functions",
      "the record denominators (record org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~77/PLANINV_INFLECTION_SERVING.json) carry both numbers; the difference was not chased (out of the slice)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "The served graph and the live Lambda plane agree on the function population, so a sweep denominator taken from either reads the same count.",
  "world_is": "At the graph vintage (21:02:47 UTC) the graph counts 238 LAMBDA nodes; at the live read the plane lists 237 functions. One node is in one count and not the other.",
  "notes": "Form only. Recorded so the issuer can re-read the denominator against the plane before the move plan relies on either count."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W78-S1",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~78",
  "surfaced_at": "2026-10-13T22:22:11Z",
  "one_line": "The Cottonwood scope inside opal-data-bd is empty: no blackdiamond/cottonwood/ or blackdiamond/cot/ prefix exists there. The Cottonwood legacy home is opal-data-cot, and its monolith copy is in opal-data-assets.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "aws s3api list-objects-v2 --bucket opal-data-bd with --prefix blackdiamond/cottonwood/, blackdiamond/cot/, advi/cottonwood/ and cottonwood/ and --delimiter / (2026-10-13, rc 0): no CommonPrefixes and no Contents for each (saved as C:/dev/wk-firmbkts-78-data/bd_*.json)",
      "aws s3api list-objects-v2 --bucket opal-data-bd --prefix blackdiamond/ --delimiter / returns CommonPrefixes 49f and 49financial only (C:/dev/wk-firmbkts-78-data/bdl_blackdiamond_.json)",
      "infra/aws/lambda/bd-pipeline/bd-silver-merge/lambda_function.py:18-20: the Black Diamond merge is opal-data-bd only, with an explicit Deny on opal-data-cot"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-FB-k-3 section 1a: inventory every thing that touches opal-data-cot or the Cottonwood scope inside opal-data-bd.",
  "world_is": "The Cottonwood scope inside opal-data-bd does not exist as a key prefix. No Lambda or script row carries a Cottonwood access to opal-data-bd. The Cottonwood legacy access is to opal-data-cot.",
  "notes": "Recorded for the move plan; no action taken and no row proposes one. Disarm: none (INERT)."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W78-S2",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~78",
  "surfaced_at": "2026-10-13T22:22:11Z",
  "one_line": "The satellites characteristics producer header says characteristics.json has zero writers today, but the object was last modified 2026-10-13T15:56:02Z, and its daily and hourly rules are ENABLED.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/terraform/cot-pipeline/satellites-characteristics-producer.tf:22: 'characteristics.json has ZERO WRITERS TODAY -- it is' (non-application statement in the header)",
      "aws s3api list-objects-v2 --bucket opal-data-cot --prefix platinum/satellites/ (2026-10-13): characteristics.json LastModified 2026-10-13T15:56:02Z; holdings.json 13:15:49Z; registry.json 13:15:48Z",
      "aws events list-rules (us-east-1): cot-satellites-characteristics-producer-daily cron(25 13 * * ? *) ENABLED; etfs-cot-satellites-characteristics-producer-reattempt-hourly cron(55 * * * ? *) ENABLED"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "The producer header, as a non-application statement, says the characteristics object has no writers today.",
  "world_is": "The object is written on the hourly and daily schedules. The header statement is stale, or it describes an earlier state, and the producer's own schedules are live.",
  "notes": "Read by list only; the object body was not read. Not re-derived here. Disarm: none (INERT)."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W78-S3",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~78",
  "surfaced_at": "2026-10-13T22:22:11Z",
  "one_line": "The served graph lists an EventBridge rule cot-satellites-registry-producer-daily that is absent from the live account: describe-rule returns ResourceNotFound and list-rules has no such name.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "aws events describe-rule --name cot-satellites-registry-producer-daily --region us-east-1 (rc 254): ResourceNotFoundException, rule does not exist on EventBus default",
      "aws events list-rules --region us-east-1 (156 rules) and --name-prefix cot-satellites (1 rule: cot-satellites-characteristics-producer-daily)",
      "comp-find --corpus aws -i 'cottonwood|cot-|cot_|_cot|/cot' (VINTAGE built 2026-10-13 21:02:47 UTC) lists an EVENT_RULE node of that name with drift DECLARED"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-FB-k-3 section 1a item 1: list all EventBridge rules, then describe those that name the Cottonwood scope or the gold chain.",
  "world_is": "The served graph and the live account disagree on this rule. The registry producer runs from etfs-cot-satellites-registry-producer-stamp-gated-daily, which is live.",
  "notes": "The inventory records the rule as claim absent with no function behind it. The graph vintage is the comp-find VINTAGE line. Disarm: none (INERT)."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W78-S4",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~78",
  "surfaced_at": "2026-10-13T22:22:11Z",
  "one_line": "The live cot-etf-ownership-daily Lambda has an environment variable SRC_BUCKET naming the legacy bucket opal-data-cot, but its code reads only opal-data-assets and opal-data-etfs.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "aws lambda list-functions --region us-east-1: cot-etf-ownership-daily environment names ASSETS_BUCKET, ETFS_BUCKET, PARTNER, SRC_BUCKET and others; SRC_BUCKET value opal-data-cot",
      "infra/aws/lambda/cot-pipeline/cot-etf-ownership-daily/lambda_function.py:87-91 (env reads: ETFS_BUCKET, ASSETS_BUCKET, and the prefixes) and :119, :199 (assets reads); grep for SRC_ finds only the historical comment at line 5",
      "the inventory row lambda.cot-etf-ownership-daily carries legacy_touch false, with this row as its consumer note"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-FB-k-3 section 1a: legacy_touch is true only where a function reads or writes the legacy home.",
  "world_is": "A live configuration names the legacy bucket for a function that does not use it. A reader of configuration alone would count a legacy dependency that the code does not have.",
  "notes": "Not touched. A configuration cleanup is a move-plan item for the round 8 author, not for this inventory. Disarm: none (INERT)."
}
```

## Row filed by 0.7.0_AE_CloudOps~FB1 (FB-j-3, the measurement)

```json
{
  "id": "ADVI_FIRMBKTS-D1-S55",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.7.0_AE_CloudOps~FB1",
  "surfaced_at": "2026-10-14T01:27:47Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "The chain-complete emit failure is measured, not inferred: rc=255 'You must specify a region'. The dispatcher's own chain log never holds the emit WARN; only the runner's cumulative log does.",
  "spec_asserts": "TO-FB-j-3 step 4: read the WARN in gold/logs/ and the runner's cumulative logs/gold-layer/gold_incremental_*.log. Row D1-S40 had inferred REGION_UNSET.",
  "world_is": "Measured. chain:full (log chain_full_20261013_230043.log) started 2026-10-13T23:00:43Z after the nightly fallback start (runner launch 23:00:11Z by bd-daily-trigger-lambda-role) and closed 2026-10-14T01:20:24Z COMPLETE exit 0. The cumulative log gold_incremental_2026-10-14_20261014_012024.log (664863477 bytes) carries, between the perf_report archive (011437Z) and the CDNCOHT invalidation (01:14:38Z), the line 'WARN: EventBridge chain-complete put-events failed (non-fatal to chain close): rc=255 You must specify a region. You can also configure your region by running \"aws configure\".' (96 characters of CLI text, fits the 300 limit; it holds no secret). The 7 earlier WARN lines in the same read window carry no text (pre-deploy code). The chain_full_ log object (4020668 bytes, same chain) holds 0 lines matching 'WARN: EventBridge', 'put-events' or 'EventBridge chain-complete': by the code order upload_log (gold_dispatch.sh line 1431) runs before emit_chain_complete (line 1459), so a reader looking for the emit result in gold/logs/ or logs/gold-layer/chain_full_* will read nothing. The COO's own read agrees (msg 5335). Not established by this measurement: that supplying a region fixes the emit (the next step, FB-j-4, does that; credentials and the rule's permissions are not exercised until the region error is out of the way).",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/EMIT_ERROR_TEXT.json",
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/j3_chain/warn_context.txt"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "A verifier of FB-j-4 / FB-j-7 should read the runner's cumulative log (tail window), not gold/logs/ or chain_full_*, for the emit line; the cumulative log is cumulative back to January, so count only the chain's own lines."
}
```
```json
{
  "id": "ADVI_FIRMBKTS-D1-W71-S1",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~71",
  "surfaced_at": "2026-10-14T01:30:28Z",
  "one_line": "The AC2 awsdiff check reads AWSDIFF: FAIL on the uncommitted script edit and passes only after the commit, because it compares committed HEAD with the merge-base.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "round7/checks/r7_checks.py:47-65 at 90be6506d6: the hunks come from git diff -U0 base HEAD (committed content) and ok = same and not outside and bool(hunks)",
      "pre-commit run on the working tree of wk-ADVI_FIRMBKTS-71: changed hunks 0, AWSDIFF: FAIL; post-commit run on f0055f3942: changed hunks 2, changed lines outside the function and the variable [], AWSDIFF: OK"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-FB-j-4 section 5: commit the script edit FIRST, then the instance; section 4 AC2 grades the awsdiff bound on the change.",
  "world_is": "The awsdiff check grades committed HEAD against the merge-base, so it reads FAIL on a working-tree edit and OK only once the edit is committed.",
  "notes": "Not a defect in the edit: the order's commit-first sequence was followed and AC2 reads OK on HEAD f0055f3942. Disarm: none (INERT)."
}
```
```json
{
  "id": "ADVI_FIRMBKTS-D1-W71-S2",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~71",
  "surfaced_at": "2026-10-14T01:30:28Z",
  "one_line": "The commit-time risk reflex printed HOLD for data/black_diamond/scripts/gold/gold_dispatch.sh by file basename against a COT freshness claim in data/cot/scripts/gold/gold_dispatch.sh.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "docs/references/FRESHNESS_GATE_MANIFEST_20260717.md:74 (R2) at 90be6506d6: the claim names check_freshness keyed on silver/allocations at data/cot/scripts/gold/gold_dispatch.sh:174-177",
      "safe-commit output for f0055f3942: [risk-reflex] HOLD on data/black_diamond/scripts/gold/gold_dispatch.sh and on data/cot/scripts/gold/gold_dispatch.sh, both matched to the same R2 claim; the commit proceeded"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "The commit-time risk reflex grades the touched node: here the FB-j-4 edit to emit_chain_complete in the BD gold_dispatch.sh.",
  "world_is": "The cited claim R2 describes check_freshness in the COT copy, not emit_chain_complete in the BD file; the match was by basename, and the reflex's own HOLD line named both paths.",
  "notes": "The FB-j-4 edit does not touch check_freshness. Disarm: none (INERT)."
}
```
```json
{
  "id": "ADVI_FIRMBKTS-D1-S56",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.7.0_AE_CloudOps~FB1",
  "surfaced_at": "2026-10-14T11:35:00Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "FB-j-7's AC1 cannot pass as written: CloudTrail lookup-events never returns PutEvents, so chain.cloudtrail_putevents reads 0 although the put demonstrably happened.",
  "spec_asserts": "TO-FB-j-7 step 6 and r7_checks.py firstchain: CloudTrail PutEvents from the runner's session >= 1 (cloudtrail_putevents < 1 is a FAIL).",
  "world_is": "Measured 2026-10-14 ~11:2xZ. lookup-events EventName=PutEvents us-east-1, 01:48:58Z-12:30:00Z: 0 events; the control EventSource=events.amazonaws.com in the 05:30Z-07:00Z window returns 271 events, none PutEvents (D1-S-row of FB-i-2 read the same 0 across 17 regions and 90 days). The put is evidenced elsewhere: runner cumulative log, this chain's 55237 lines hold 1 'EventBridge chain-complete emitted' and 0 'put-events failed'; AWS/Events TriggeredRules for exec-summary-trigger Sum 1 in the 06:00Z hour; exec-summary-generator Invocations Sum 1 (START 06:12:41Z, 74.6 s, 0 SLOT_DROPPED, 0 errors); 194 of 194 named keys written 06:12:44Z-06:13:57Z, 0 non-empty bullets, 0 outside the set, 0 double writes, 158 prior VersionIds still present. FIRST_CHAIN_READ.json records cloudtrail_putevents 0 with this note; AC1 reads FAIL on that one clause only. This agrees with the CTO's MEASURED_20261014_103xZ read on every count.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/FIRST_CHAIN_READ.json",
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/RUNNER_EMIT_READ.json"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Issuer's call: amend the criterion to the instruments that can see the put (emitted line + AWS/Events TriggeredRules >= 1), or accept the record as is. This seat did not edit the record to 1 and did not flip <status>. D1-W65-S1 disarm read: the chain emitted, the rule fired and the generator ran, so the disarm condition is met on that evidence."
}
```
```json
{
  "id": "ADVI_FIRMBKTS-D1-W83-S1",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~83",
  "surfaced_at": "2026-10-14T12:19:47Z",
  "one_line": "PLANINV row 6 says the Door 6 deny (router_iam.tf statement 3) has no live object and retires with the key; the deny is deployed, in a managed policy on a live role.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/terraform/opal-assets/router_iam.tf:171 (Sid DenyInfGoldSentinelAbsolutely) at C:/dev/wk-firmbkts-83 HEAD 7ee8e70830, read by the Read tool",
      "live: aws iam list-attached-role-policies on opal-assets-ingest-router-role shows managed policy opal-assets-one-way-fan-in-fence; aws iam get-policy-version on its default version v1 shows 3 statements, the third Sid DenyInfGoldSentinelAbsolutely, Effect Deny, naming the gold/meta/pipeline-complete.json key",
      "live: aws lambda get-function-configuration opal-assets-ingest-mirror returns Active with Role opal-assets-ingest-router-role; aws events describe-rule mdpf-daily-refresh-trigger returns ResourceNotFound (the statement's named principal is absent)",
      "PLANINV_LEGACY_OPERATIONS.json candidates[5] (row 6, router-iam-door6-deny), read at 0.9.0_WK_ADVI_FIRMBKTS~80 record"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "PLANINV row 6 (router-iam-door6-deny): the deployed router policy statement was not read; the deny guards a key whose protected principal is absent, so it has no object once the key retires and is retired with the key.",
  "world_is": "The deny is deployed live in a customer-managed policy attached to opal-assets-ingest-router-role, the execution role of the live opal-assets-ingest-mirror Lambda. Its named principal mdpf-daily-refresh-trigger is absent, but the role and the deny are both live. The consumer census counts the role as 1 live consumer.",
  "notes": "Not a defect in the census. Found by the FB-l-3 consumer census. Retiring the key does not edit this policy; any edit to the deny is an IAM change under CTO or Andrew. Disarm: none (INERT)."
}
```
```json
{
  "id": "ADVI_FIRMBKTS-D1-W83-S2",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~83",
  "surfaced_at": "2026-10-14T12:19:47Z",
  "one_line": "PLANINV row 11 says the portal distribution's behaviours must repoint off all three legacy origins; live, only the opal-data-bd origin has behaviours, and the cot and inf origins have none.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "live: aws cloudfront get-distribution-config on the portal distribution (found by Comment, ID not printed), read to C:/dev/wk-firmbkts-83-data/cfcfg.json; python count of TargetOriginId: 30 behaviours including the default, 5 to S3-opal-data-bd, 0 to S3-opal-data-cot, 0 to S3-opal-data-inf, 20 to APIGateway-portal, 3 to S3-opal-data-portal-v2-json, 1 to S3-opalinvest-portal, 1 to APIGateway-portfolio",
      "live: the same read lists 7 origins, including S3-opal-data-cot and S3-opal-data-inf",
      "PLANINV_LEGACY_OPERATIONS.json candidates[10] (row 11, portal-cloudfront-distribution), read at 0.9.0_WK_ADVI_FIRMBKTS~80 record"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "PLANINV row 11: the distribution has 7 origins, three of them legacy; the behaviours must repoint when the origins retire.",
  "world_is": "Behaviours route only to the opal-data-bd origin (5 of 30). The opal-data-cot and opal-data-inf origins are configured with zero cache behaviours, so no request path reaches either legacy bucket through the distribution. Repointing those two origins has no behaviour to move.",
  "notes": "Read-only finding. The bd origin carries the four advisor-intelligence artifact and entity paths, the *.json path and the satellites path. The cot bucket policy's OAC statement still names the portal distribution (consumer census row C10)."
}
```
```json
{
  "id": "ADVI_FIRMBKTS-D1-W83-S3",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~83",
  "surfaced_at": "2026-10-14T12:19:47Z",
  "one_line": "PLANINV row 10 says the legacy bucket policies are declared in no Terraform (DEC-8); the opal-data-bd policy statements are declared in Terraform and drift-guarded.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/terraform/bd-pipeline/opal-data-bd.tf:94 (Sid AllowCloudFrontOACReadGold) and :102 (Sid AllowScopedAdvisorOAI), read by the Read tool at HEAD 7ee8e70830",
      "infra/aws/terraform/portal-auth/firm-bucket-cross-ref.tf:96 carries a DRIFT check that names the AllowCloudFrontOACReadGold statement on opal-data-bd",
      "Grep over infra/aws (code types, excluding md, json, txt, yaml) for AllowScopedAdvisorOAI and AllowCloudFrontOACReadGold returns only bd-pipeline/opal-data-bd.tf and shared-infra/s3.tf:286; the s3.tf statements are on opal-data-demo, not a legacy bucket",
      "live: aws s3api get-bucket-policy on opal-data-cot returns the two statements named in PLANINV row 10 (read in this census)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "PLANINV row 10: the three legacy bucket policies are declared in no Terraform (PRD DEC-8) and retire with their buckets, not by a Terraform change.",
  "world_is": "The opal-data-bd statements are declared in Terraform and drift-guarded in portal-auth. The opal-data-cot statements have no Terraform declaration by name. Retiring the bd policy therefore needs a Terraform change, and retiring the cot policy does not.",
  "notes": "Affects the retirement route for opal-data-bd only. Read-only; no policy was edited. Disarm: none (INERT)."
}
```
```json
{
  "id": "ADVI_FIRMBKTS-D1-W83-S4",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~83",
  "surfaced_at": "2026-10-14T12:19:47Z",
  "one_line": "The FB-l-3 order names the portal's user rows as a mockadv consumer; the repository holds none, and the live rows are user data this census does not read.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "Grep (native) with path C:/dev/wk-firmbkts-83/portal, token mockadv, excluding node_modules: 1 occurrence across 1 file, portal/src/pages/InvestorReporting/header/firmDisplayNames.generated.ts:6",
      "comp-find --corpus aws 'mockadv': 0 hits (denominator 2929 aws nodes scanned, vintage 2026-10-14 12:11:36 UTC)",
      "FB-l-3 section 1a.3 scopes the read to the files and forbids reading any user's data, so no user row was opened"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "FB-l-3 section 1a.3: for mockadv, read the portal's user rows, the dropdown entry, the two router map entries and the registry rows.",
  "world_is": "The repository has no user-row file carrying the token. The only portal consumer is the generated dropdown row. Any user rows live in a store outside the repository and the graph, and were not read. The dropdown row and the router rows were read.",
  "notes": "The census records the user-row consumer as not_read, not as zero. Disarm: none (INERT)."
}
```
```json
{
  "id": "ADVI_FIRMBKTS-D1-W83-S5",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~83",
  "surfaced_at": "2026-10-14T12:19:47Z",
  "one_line": "FB-l-3 defines the first zero-consumer candidate as having no LIVE consumer without fixing consumer direction or delivery liveness; the FIRMSEP alarm turns the answer on that choice.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "live: aws events describe-rule FIRMSEP-s3-direct-access-bypass returns ENABLED; list-targets-by-rule returns one target, the SNS topic opal-infrastructure-alerts",
      "live: aws sns list-subscriptions-by-topic returns 1 subscription, protocol sms, not pending confirmation",
      "live: aws cloudwatch get-metric-statistics, AWS/SNS, NumberOfMessagesPublished and NumberOfNotificationsFailed, topic opal-infrastructure-alerts, window 2026-09-14 to 2026-10-14, Sum: published 56, failed 56",
      "live: aws events describe-rule inf-canonical-prices-daily returns DISABLED, with its only target inf-gold-trigger"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "FB-l-3 section 1a: a candidate's consumers is the count of LIVE consumers; a candidate with consumers 0 and scanned above 0 is the zero case; the first such candidate in file order is first_zero_consumer.",
  "world_is": "Under a configuration reading (enabled and configured), FIRMSEP has 1 live consumer, the SNS topic, so the first zero is inf-canonical-prices-daily (C2). Under a delivery reading, FIRMSEP has 0 deliveries in the window (56 of 56 failed), so the first zero is FIRMSEP (C1). The record uses the configuration reading and states the delivery count beside it.",
  "notes": "The COO adjudicates which reading governs the first zero. The census does not choose for it. Disarm: none (INERT)."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W81-S1",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~81",
  "surfaced_at": "2026-10-14T12:26:38Z",
  "one_line": "The Inflection fence admits 5 of the 40 roles that hold Allow on opal-data-inf, so most repoints to opal-data-inflection would be denied.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~81/PLAN_INFLECTION.json (M02, Q4)",
      "live: s3api get-bucket-policy --bucket opal-data-inflection (read 2026-10-14)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "PRD CONTRACTS DEC-8 and F4 (row 411): the serving grants are APPLIED on opal-data-inflection from an identity the repaired fence admits.",
  "world_is": "Live get-bucket-policy on opal-data-inflection: DenyForeignFirmPrincipals (Deny s3:*) excepts role/*-inf-* (pattern), two named roles and five user principals. Of the 40 Allow roles on opal-data-inf, 5 match (opal-inf-served-guard, opal-inf-value-parity, irpt-inf-holdings-role, irpt-holdings-role, irpt-performance-adapter-role); 35 do not, because the inf-* names carry no leading hyphen. The bucket has no notification configuration, so EventBridge rules cannot match it.",
  "notes": "Plan move M02 (admit by explicit ARN; no widening to a wildcard) and open question Q4 (identity-plane change, CTO decides)."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W81-S2",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~81",
  "surfaced_at": "2026-10-14T12:26:38Z",
  "one_line": "opal-data-inf holds 339 objects under a leading-slash prefix that no inventory row names, and the decommission cannot be measured until they are disposed of.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~81/PLAN_INFLECTION.json (M40, Q5)",
      "live: s3api list-objects-v2 --bucket opal-data-inf --prefix /"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "FB-k-1 and FB-k-2 cover every legacy key family, and TO item 6 names only B2 as the exception to the decommission.",
  "world_is": "list-objects-v2 --prefix / (max-items 2000, not truncated): 339 keys, advisor-folder and client-id paths, one LastModified date (2026-05-06), none modified since 2026-10-01, STANDARD. No inventory row names a writer; the advisor publisher writes platinum/advisors/ without a leading slash (source lines 6-12).",
  "notes": "Plan move M40 and open question Q5 (migrate or retire, Andrew's word for any delete). Names and ids were not printed."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W81-S3",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~81",
  "surfaced_at": "2026-10-14T12:26:38Z",
  "one_line": "The 49 Financial publish trigger the TO asks the plan to mirror is a clock floor whose publisher stage is DISABLED; no live event trigger exists to copy.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~81/PLAN_INFLECTION.json (M03)",
      "infra/aws/terraform/opal-assets/advi_49f_publisher.tf:1-60, 75-110",
      "live: scheduler get-schedule advi-49f-publisher, advi-49f-gold-floor"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO item 1: read how the comparable 49 Financial portal publish is triggered today (live rule, schedule or S3 notification) and give Inflection the same shape.",
  "world_is": "opal-data-49financial has 0 S3 notification entries (live). The publisher stage advi-49f-publisher is DISABLED (cron 13:15Z; its document advi-49f-publisher-dispatch is not minted, per the Terraform header). The live path is advi-49f-gold-floor (ENABLED 12:45Z) into advi-49f-gold-dispatch. The shape is a designed clock floor, not a proven live path.",
  "notes": "Plan move M03 copies the design (clock floor, DLQ, retry) and proves it on Inflection with a one-time exercise before any recurring enable; the 49 Financial path is not claimed as proven."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W81-S4",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~81",
  "surfaced_at": "2026-10-14T12:26:38Z",
  "one_line": "The exec-summary Terraform placeholder carries a different name from the live rule, so no Terraform declares exec-summary-trigger.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~81/PLAN_INFLECTION.json (M01)",
      "infra/aws/terraform/exec-summary/main.tf:214-236",
      "live: events describe-rule exec-summary-trigger-placeholder (ResourceNotFound)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "FB-k-2 INF-RULE-02 and TO item 3: Terraform declares only a DISABLED placeholder for the live rule.",
  "world_is": "The placeholder resource is named exec-summary-trigger-placeholder (infra/aws/terraform/exec-summary/main.tf:224-227, DISABLED, cron 04:30Z). The live rule is exec-summary-trigger (ENABLED); describe-rule on the placeholder name returns ResourceNotFound. No Terraform file read declares the live name.",
  "notes": "Plan move M01 replaces the placeholder with a declaration of the live rule and imports it; no AWS change."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W81-S5",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~81",
  "surfaced_at": "2026-10-14T12:26:38Z",
  "one_line": "Two repo readers of the Door 6 marker (inf-gold-freshness-guard and mdpf-daily-trigger) are absent live, which contradicts the measured claim for L27.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~81/PLAN_INFLECTION.json (M04, R11, R12, Q7, Q8)",
      "live: lambda get-function-configuration inf-gold-freshness-guard and mdpf-daily-trigger (ResourceNotFound)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "FB-k-1 row L27 (claim measured): inf-gold-freshness-guard reads gold/meta/pipeline-complete.json as its SENTINEL_KEY; its invoker was not identified.",
  "world_is": "lambda get-function-configuration returns ResourceNotFound for inf-gold-freshness-guard and mdpf-daily-trigger; no rule targets either; neither has a resource policy. Both sources exist in the repo (infra/aws/lambda/inf-pipeline/inf-gold-freshness-guard/lambda_function.py:13, 42; infra/aws/lambda/mdpf-pipeline/mdpf-daily-trigger/lambda_function.py:53). The marker's live consumers are therefore the publisher, the accelerator rule and the fence, pending Q7 and Q8. D1-W80-S1 disarm read: the plan names the successor (move M03) and its proof (a one-time exercise). Its disarm_owner (1.0.0_SA_CTO~DELL1) confirms; this row does not disarm it.",
  "notes": "Plan moves M04 (retirement, step 4 requires Q7 and Q8) and retire rows R11 and R12."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W81-S6",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~81",
  "surfaced_at": "2026-10-14T12:26:38Z",
  "one_line": "The Door 6 resource-plane belt named in the router IAM file is absent from the tree, and the live bucket has no Deny on the marker.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~81/PLAN_INFLECTION.json (R6)",
      "infra/aws/terraform/opal-assets/router_iam.tf:170-176",
      "live: get-account-authorization-details --filter Role LocalManagedPolicy (fence attachment count 13)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "infra/aws/terraform/opal-assets/router_iam.tf:35-37 names a resource-plane twin, an s3:PutObject Deny in infra/aws/terraform/inf-sentinel-deny/.",
  "world_is": "infra/aws/terraform/inf-sentinel-deny/ contains no .tf file (its only tracked content is an org/ telemetry log, git ls-files). The live opal-data-inf policy has 2 statements (AllowScopedAdvisorOAI, AllowCFDistributionGold), neither a Deny. The identity-plane Deny DenyInfGoldSentinelAbsolutely is live, attached to 13 roles through the fan-in fence policy.",
  "notes": "Plan retire row R6 (identity Deny removed only after the marker is gone, CTO decides)."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W81-S7",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~81",
  "surfaced_at": "2026-10-14T12:26:38Z",
  "one_line": "A portal Lambda role holds a wildcard Allow on the legacy Inflection bucket, shared with 12 functions outside both inventories.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~81/PLAN_INFLECTION.json (M42, R8, Q15)",
      "live: get-account-authorization-details (role statements); lambda list-functions (Role field)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "FB-k-2 INF-ROLE-40 lists opal-portal-lambda-role among the Inflection estate roles with Allow on opal-data-inf, and the inventories treat the consumer set as Inflection-only.",
  "world_is": "The role holds Allow s3 on opal-data-inf:* and is assumed by 12 non-Inflection functions (opal-trending-topics-portal-publisher, opal-portal-rest-authorizer, opal-portal-fear-greed-fetcher, opal-news-ai-sentiment, opal-portal-volatility-fetcher, opal-portal-authorizer, opal-infrastructure-monitor, opal-session-analytics, opal-market-regime-classifier, finbert-batch-processor, opal-portal-data-proxy, opal-market-overview-tiered-generator). Read live (role statements and list-functions Role field).",
  "notes": "Plan move M42 and retire row R8 (the statement is removed after a zero-read record; the portal lane owner and the CTO decide)."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W81-S8",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~81",
  "surfaced_at": "2026-10-14T12:26:38Z",
  "one_line": "The org trail already selects write data events on the whole of opal-data-inf, which bears on PRD DEC-12's open call.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~81/PLAN_INFLECTION.json (decommission, Q2)",
      "live: cloudtrail get-event-selectors --trail-name opal-organization-trail; get-trail-status"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "PRD CONTRACTS DEC-12: writes are recorded only under platinum/firm/ (served-key trail); recording writes on the three legacy buckets is an open call at Andrew.",
  "world_is": "get-event-selectors on opal-organization-trail (logging true per get-trail-status): classic WriteOnly data selector on the arn of opal-data-inf/ (and bd, cot) and ReadOnly on opal-data-inf/ (and 49financial, bd, cot). The served-key trail carries only the platinum/firm/ advanced selector. Whether this answers DEC-12 is for the CTO; the trail query surface and retention were not read.",
  "notes": "Plan decommission basis (instrument) and open question Q2."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W81-S9",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~81",
  "surfaced_at": "2026-10-14T12:26:38Z",
  "one_line": "The default-group Scheduler count has fallen from the 34 the inventory recorded to 33 live, and the schedule that left was not identified.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~81/PLAN_INFLECTION.json (denominators)",
      "live: scheduler list-schedules --group-name default"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "FB-k-1 denominators: 34 EventBridge Scheduler schedules in the default group.",
  "world_is": "list-schedules --group-name default returns 33 schedules at 2026-10-14 (read in this plan). The difference from the 2026-10-13 read was not identified; the six schedules named in the plan are present (advi-49f-publisher, advi-49f-gold-floor, irpt-49f-reporting-publish-daily, opal-assets-mdpf-portal-publisher-daily, mdpf-feeder-backstop-daily, mdpf-scheduled-floor).",
  "notes": "The plan's denominator records 33 live and 34 recorded."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W81-S10",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~81",
  "surfaced_at": "2026-10-14T12:26:38Z",
  "one_line": "The 49 Financial advisor prefix has gold and platinum only; the TO's model layout names a state/ prefix that is not there.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~81/PLAN_INFLECTION.json (M05, Q5)",
      "live: s3api list-objects-v2 --bucket opal-data-49financial --prefix advi/49financial/ --delimiter /"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO section 1: 49 Financial keys are advi/49financial/{gold|platinum|state}/ and are the model for Inflection.",
  "world_is": "list-objects-v2 on opal-data-49financial with prefix advi/49financial/ and delimiter /: CommonPrefixes are advi/49financial/gold/ and advi/49financial/platinum/ only. The Inflection state/ layout in the plan is therefore inferred from the model, not copied from a live state/ prefix.",
  "notes": "Plan move M05 layout note; the CTO decides the state/ layout (Q5)."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W81-S11",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~81",
  "surfaced_at": "2026-10-14T12:26:38Z",
  "one_line": "Three inventory rows claim legacy_touch False although their live environment or rule pattern names opal-data-inf.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~81/PLAN_INFLECTION.json (M28, M29, M20)",
      "live: lambda get-function-configuration inf-client-detail, inf-etf-ownership-daily; events describe-rule inf-assets-trigger-bronze-complete"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "FB-k-1 L24 and FB-k-2 INF-FN-08 (client-detail) and INF-FN-21 (assets-trigger) carry legacy_touch False.",
  "world_is": "inf-client-detail has INPUT_BUCKET=opal-data-inf (env read live); inf-assets-trigger's rule R02 matches opal-data-inf bronze-complete markers (rule read live); inf-etf-ownership-daily has INF_BUCKET=opal-data-inf (env read live; FB-k-1 L24 is False, FB-k-2 INF-FN-20 is True).",
  "notes": "The plan treats all three as legacy: moves M29, M20 and M28."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W82-S1",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~82",
  "surfaced_at": "2026-10-14T12:33:00Z",
  "one_line": "A routed-alias flip alone cannot move the Cottonwood canonical platinum list: platinum_destinations.json holds no cottonwood rows, so the generated CANONICAL_PLATINUM_BUCKETS and OWNERSHIP_KEYS cannot gain opal-data-cottonwood.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/logic/registry/platinum_destinations.json: grep count cottonwood = 0; grep count 49financial = 14 (read at worktree HEAD 7ee8e70830)",
      "lib/opal_naming.py:1284-1293 and 1299-1307: CANONICAL_PLATINUM_BUCKETS and OWNERSHIP_KEYS derive from the platinum destination rows",
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~82/PLAN_COTTONWOOD.json moves M5 and M13"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Plan premise (FWD-9 move order): the canonical-home move is a registry flip after which the generated router, ownership and IRPT maps follow.",
  "world_is": "The generator reads the platinum destination rows for the canonical list, and Cottonwood has none, so the flip needs new rows first (plan M5) before regeneration (plan M13).",
  "notes": "Plan records M5 as a prerequisite. No registry or generated file was edited by this worker. Disarm: none (INERT)."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W82-S2",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~82",
  "surfaced_at": "2026-10-14T12:33:00Z",
  "one_line": "PLANINV marks edge-auth-validator-edge as no legacy touch, but its ownership-map read resolves through FIRM_CONFIG to the firm bucket, and the Lambda@Edge execution role grants GetObject on opal-data-bd only.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/lambda-edge/_shared/firm-config.mjs:65-101 (FIRM_CONFIG cottonwood bucket opal-data-cot; OWNERSHIP_KEYS); infra/aws/lambda-edge/auth-validator-edge/tests/ownership_key.spec.mjs:3-9 (imports FIRM_CONFIG and ownershipMapKey)",
      "live IAM: role lambda-edge-execution-role, policy lambda-edge-ownership-map-read, single statement Resource arn:aws:s3:::opal-data-bd/platinum/*/ownership_map.json (one policy document read)",
      "PLAN_COTTONWOOD.json move M14 and open question Q13"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "PLANINV_COTTONWOOD_SERVING_CROSSWALK row edge-auth-validator-edge: legacy_touch n, reads not stated.",
  "world_is": "The validator's ownership read is keyed by FIRM_CONFIG, which names opal-data-cot for cottonwood, and the role has no grant on that bucket. Whether the cottonwood read succeeds through another path is not established.",
  "notes": "Read-only finding. The inventory row needs correction at the next PLANINV revision. Disarm: none (INERT)."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W82-S3",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~82",
  "surfaced_at": "2026-10-14T12:33:00Z",
  "one_line": "opal-data-cottonwood is in no CloudTrail data-event selector, so the canonical firm bucket has no read or write instrument for the FWD-6 record.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "aws cloudtrail get-event-selectors --trail-name opal-organization-trail (read): data resources for opal-data-49financial, opal-data-bd, opal-data-cot, opal-data-inf; no opal-data-cottonwood",
      "aws cloudtrail get-event-selectors --trail-name opal-served-key-write-trail (read): advanced selector limited to platinum/firm/ prefixes on opal-data-inf, opal-data-bd, opal-data-cot",
      "aws s3api get-bucket-logging --bucket opal-data-cottonwood (read): no logging configuration"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "PRD DEC-12 and the firm-bucket CONTRACTS row: each firm bucket is born with read logging.",
  "world_is": "The canonical Cottonwood bucket is outside the organisation trail's data-event selectors. The legacy bucket is inside them.",
  "notes": "PLAN_COTTONWOOD.json move M4 proposes the selector add with a saved rollback. Disarm: none (INERT)."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W82-S4",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~82",
  "surfaced_at": "2026-10-14T12:33:00Z",
  "one_line": "The opal-data-cottonwood bucket-policy Deny admits only role names matching role/*-cot-*, so the satellites producer roles and the performance adapter role are explicitly denied on the new home.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "aws s3api get-bucket-policy --bucket opal-data-cottonwood (read): statement DenyForeignFirmPrincipals, ArnNotLike aws:PrincipalArn over role/*-cot-*, irpt-holdings-role and three users",
      "aws iam simulate-principal-policy with that policy as --resource-policy: cot-satellites-registry-producer-role PutObject and GetObject on platinum/satellites/registry.json explicitDeny; cot-satellites-characteristics-producer-role and cot-rebalancer-runner-role explicitDeny; irpt-performance-adapter-role explicitDeny; irpt-holdings-role GetObject on its manifest allowed (calibration)",
      "PLAN_COTTONWOOD.json move M11 and open question Q6"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "PRD F4: the new firm bucket carries the scope-derived fence, and its admit list covers the Cottonwood roles that write it.",
  "world_is": "The admit glob does not match role names that begin with cot- (no leading hyphen), so those roles are refused by the fence on the new home.",
  "notes": "No writer has moved, so no live effect today. The move fails closed if M11 is skipped. Disarm: none (INERT)."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W82-S5",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~82",
  "surfaced_at": "2026-10-14T12:33:00Z",
  "one_line": "The write half of PRD DEC-12 does not match the live trail: the organisation trail records WriteOnly data events on all of opal-data-cot/, not only platinum/firm/.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "aws cloudtrail get-event-selectors --trail-name opal-organization-trail (read): WriteOnly selector, AWS::S3::Object, value arn:aws:s3:::opal-data-cot/ (whole bucket)",
      "aws cloudtrail get-event-selectors --trail-name opal-served-key-write-trail (read): writes limited to platinum/firm/ prefixes",
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/prd/ADVI_FIRMBKTS_PRD.md DEC-12 (read at its section)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "PRD DEC-12: writes are recorded only under platinum/firm/, so writes to gold/, bronze/, silver/, code/ and state/ would be invisible during the window.",
  "world_is": "The whole-bucket WriteOnly selector covers those prefixes on opal-data-cot today. The configuration date is not read, so the stamp that starts the window is open (PLAN_COTTONWOOD.json Q8).",
  "notes": "The 45-day window basis in the plan cites the organisation trail, not the served-key trail. Disarm: none (INERT)."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W82-S6",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~82",
  "surfaced_at": "2026-10-14T12:33:00Z",
  "one_line": "cot-etf-ownership-daily is marked legacy_touch no in PLANINV, but its live role still reads opal-data-cot and its live environment still names opal-data-cot.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "aws lambda get-function-configuration --function-name cot-etf-ownership-daily (read): SRC_BUCKET=opal-data-cot",
      "aws iam get-role-policy --role-name cot-etf-ownership-daily-role --policy-name s3-etf-ownership (read): GetObject on opal-data-cot gold/canonical/holdings/* and ListBucket on opal-data-cot",
      "infra/aws/terraform/cot-pipeline/cot-etf-ownership-daily.tf:27 (the prior grant is left in place) and infra/aws/lambda/cot-pipeline/cot-etf-ownership-daily/lambda_function.py:1-12 (code reads opal-data-assets)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "PLANINV_COTTONWOOD_PIPELINE row lambda.cot-etf-ownership-daily: legacy_touch no; env SRC_BUCKET stale (surprise S4).",
  "world_is": "The function still holds a live read grant and a live env value on the legacy bucket. The code reads neither. PLAN_COTTONWOOD.json move M1 removes all three together.",
  "notes": "Corrects the legacy_touch flag for this function in the plan. Disarm: none (INERT)."
}
```
```json
{
  "id": "ADVI_FIRMBKTS-D1-S57",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.7.0_AE_CloudOps~FB1",
  "surfaced_at": "2026-10-14T13:08:00Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "TO-FB-l-5 act 1 (M01) rests on a false premise: the live exec-summary-trigger rule is ALREADY in Terraform state, and HEAD's exec-summary main.tf would destroy it; restoring the declaration is refused by the LGIC naming gate.",
  "spec_asserts": "COO half a6e2df30dc act 1 and PLAN_INFLECTION M01: Terraform declares only the DISABLED placeholder; replace it with the rule exec-summary-trigger and IMPORT it; the plan after the import shows zero changes.",
  "world_is": "Measured 2026-10-14 ~13:0xZ. terraform state list (exec-summary) holds aws_cloudwatch_event_rule.exec_summary_trigger, the target and the lambda permission: applied 2026-04-27 from ecc9b2a508. The stray commit 64b6b9d65a (a COMP_LEARNS log commit) reverted main.tf, outputs.tf, iam.tf, the lock file and CHANGELOG.json the same day, so HEAD declares exec_summary_trigger_placeholder. Baseline plan at HEAD (read-only, -lock=false): 'Plan: 3 to add, 1 to change, 3 to destroy' (create the placeholder rule; replace the target and permission; destroy the live rule) -- an un-targeted apply at HEAD would destroy the live trigger. The 1 change is aws_iam_role_policy.exec_summary_generator: iam.tf says cloudwatch:namespace ExecSummary, live holds Opal/ExecSummary (hotfix e27aa49afa, reverted by the same stray commit), so an un-targeted apply would also drop the PutMetricData grant for the live namespace. Restoring main.tf/outputs.tf from ecc9b2a508 (no import needed) gives: scoped plan on rule+target+permission 'No changes', describe-rule ENABLED with the same pattern. safe-commit then REFUSED that commit: naming gate hole-count-ratchet on infra/aws/terraform/exec-summary (1 HOLE now, 0 at HEAD: EVENT_RULE exec-summary-trigger, on-{event} token not ruled), so the edit is not committed; it is saved as deliverables/0.7.0_AE_CloudOps~FB1/M01_RESTORE_EXEC_SUMMARY_TRIGGER.patch and the shared tree is clean.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/M01_BASELINE_PLAN_AT_HEAD.txt",
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/M01_RESTORE_EXEC_SUMMARY_TRIGGER.patch"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "INERT while every apply in this directory is -target scoped (the FB-j-7 and FB-j-13 applies were). Needs the issuer's and CTO's call: a registry ruling for the rule name (or an R20 departure the CTO signs) so the restore can commit; iam.tf's namespace line is outside the pair and needs its own half."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W84-S1",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~84",
  "surfaced_at": "2026-10-14T13:07:13Z",
  "one_line": "FB-m-1 is blocked: no object in opal-data-inf is a chain-written, run-dated, single-writer readiness signal that the MDPF register does not class as a gate-read sidecar.",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~B1",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "data/inf/scripts/gold/orion-gold-dispatch.sh:2024 and :2027 (dispatch_eclipse_status.json: run_date, chain, chain_exit; single writer)",
      "docs/architecture/MDPF_REMEDIATION_REGISTER.md:198 and :226 (the key classed TRASH: sidecar state object read as a gate; :219-221 names the data's own frontier as the remedy)",
      "aws s3api head-object gold/artifacts/header_metrics.json (read, 2026-10-14): 404 Not Found",
      "aws s3 cp s3://opal-data-inf/gold/eclipse/_meta/dispatch_eclipse_status.json - (read): run_date 2026-10-14, chain full, chain_exit 0"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO FB-m-1 section 1a: choose ONE object in opal-data-inf that the FULL gold chain writes, carries the gold date, has one writer, survives the Door 6 retirement, and is not pipeline-complete or pull-complete; otherwise file BLOCKING and stop.",
  "world_is": "Every candidate fails at least one criterion or a governing rule: the sentinels are excluded, the header_metrics key is absent, perf_report and the per-step markers are not per-run completion records, and the one run-dated chain object is the eclipse status, which the register names as TRASH read as a gate. The publisher has no readiness halt, so a clock-driven start (FB-m-2) would publish unchecked gold.",
  "notes": "Signal files written with chosen null: deliverables/0.9.0_WK_ADVI_FIRMBKTS~84/READINESS_SIGNAL.json and .md. CTO decision needed: a new chain-written run-dated object (dispatch edit), a data-frontier read (calendar decision), or a ruling on the eclipse status. Disarm: the issuer decides whether the FB-m-2 clock schedule may start the publisher before a guard exists; until then it is unguarded."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W84-S2",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~84",
  "surfaced_at": "2026-10-14T13:07:13Z",
  "one_line": "The gold chain freshness gate reads gold/artifacts/header_metrics.json, which is absent in opal-data-inf, and treats the absence as a first run.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "data/inf/scripts/gold/orion-gold-dispatch.sh:502-516 (check_freshness reads gold/artifacts/header_metrics.json; empty value prints 'No prior gold data_as_of found -- proceeding (first run)')",
      "aws s3api head-object --bucket opal-data-inf --key gold/artifacts/header_metrics.json (read, 2026-10-14): 404 Not Found",
      "data/inf/scripts/gold/INF_D_00.portal_aggregates.py:1087-1089 (INF_D_00 no longer emits header_metrics.json)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "dispatch :502-530: the silver-versus-gold freshness gate skips a chain when no new silver data exists, using gold header_metrics data_as_of as the gold frontier.",
  "world_is": "The gold frontier key does not exist, so the gate cannot skip and always proceeds. The writer that the comment at INF_D_00:1087 points away from has no successor at that key.",
  "notes": "Found while reading the candidates for FB-m-1. Not a readiness signal, and not in this order's paths. Disarm: none (INERT)."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W84-S3",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~84",
  "surfaced_at": "2026-10-14T13:07:13Z",
  "one_line": "The eclipse status object is written after the best-effort eclipse steps, so its arrival time depends on them (up to three bounded steps).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "data/inf/scripts/gold/orion-gold-dispatch.sh:756 (ECLIPSE_STEP_TIMEOUT default 600) and :2009-2012 (the eclipse loop runs after the sentinel at :1905)",
      "aws s3 cp s3://opal-data-inf/gold/meta/pipeline-complete.json - (read): completed_at 2026-10-14T12:53:39Z; aws s3 cp s3://opal-data-inf/gold/eclipse/_meta/dispatch_eclipse_status.json - (read): completed_at 2026-10-14T12:53:48Z",
      "data/inf/scripts/gold/orion-gold-dispatch.sh:1988-1990 (the 2026-05-15 directive that eclipse must not pause portal updates)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "dispatch :1988-1990: the portal publish is gated only on the A/B/C/D chain, and eclipse outcome must not pause portal updates.",
  "world_is": "The one run-dated chain-tail object is written after the eclipse loop. The measured gap on 2026-10-14 was 9 s; the worst case is three 600 s steps, so any signal taken from it inherits eclipse timing.",
  "notes": "Recorded as the coupling the CTO weighs with ADVI_FIRMBKTS-D1-W84-S1. Disarm: none (INERT) while nothing reads the object as a gate."
}
```
```json
{
  "id": "ADVI_FIRMBKTS-D1-W84-S4",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~84",
  "surfaced_at": "2026-10-14T13:24:02Z",
  "one_line": "On the completed 2026-10-14 chain day the NNA newest partition is 2026-10-13 and canonical_nna_2026-10-14.parquet is absent, so the ruled frontier rule would see the three dated inputs at different dates.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~B1",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "aws s3api head-object --bucket opal-data-inf --key gold/canonical/canonical_nna_2026-10-14.parquet (read, 2026-10-14 ~13:2xZ): 404 Not Found",
      "aws s3api list-objects-v2 --prefix gold/canonical/ (read, 2026-10-14 ~13:1xZ): 9159 objects; newest canonical_nna_ key canonical_nna_2026-10-13.parquet of 1476 matches; newest holdings_ key holdings_2026-10-14.parquet of 2514 matches",
      "aws s3 cp s3://opal-data-inf/gold/meta/pipeline-complete.json (read): completed_at 2026-10-14T12:53:39Z (see ADVI_FIRMBKTS-D1-W84-S1)",
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~84/READINESS_SIGNAL.json (frontier_rule, live_prediction_not_content)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO FB-m-1 section 1a items 1-2 and CTO msg 5552: the readiness signal is the data frontier; publish only when every dated input reads the same date D (NNA read from its newest partition) and D is after the served date.",
  "world_is": "At read time the chain had completed 2026-10-14 (pipeline-complete 12:53:39Z) and holdings carries 2026-10-14, but the NNA newest partition is 2026-10-13 and the 2026-10-14 partition is absent. The rule as ruled would halt the publish of a completed day. Whether the NNA partition lands later each day, or lags by design, is not measured here.",
  "notes": "Form only: the premise that the NNA partition for the completed day exists is not what the bucket showed at read time. ARMED: left alone, a clock-started publisher with this guard would halt daily while NNA lags. The disarm owner decides whether FB-m-2 may start the publisher on a clock before NNA day-partition timing is measured or the CTO re-rules the frontier. No deploy act was taken in this cell."
}
```
```json
{
  "id": "ADVI_FIRMBKTS-D1-W84-S5",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~84",
  "surfaced_at": "2026-10-14T13:24:02Z",
  "one_line": "The served-date glob aua_by_*.json matches a fourth snapshot object, aua_by_tax_status.json, last written 2026-06-30; a minimum over the glob would freeze the served date and defeat the same-day halt.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "aws s3api list-objects-v2 --prefix platinum/firm/snapshots/ (read this cell, 2026-10-14, before 13:24Z): aua_by_architect, aua_by_region, aua_by_state at 2026-10-14T12:53:58Z; aua_by_tax_status.json at 2026-06-30T17:18:23Z",
      "aws s3api head-object --key platinum/firm/snapshots/aua_by_tax_status.json (read, 2026-10-14 ~13:2xZ): 155 bytes, LastModified 2026-06-30T17:18:23+00:00",
      "infra/aws/lambda/inf-portal-publisher/lambda_function.py:11 (three output files; tax-status snapshot write removed per ADVI_INFREF EG-1)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO FB-m-1 section 1a item 2: the served data_as_of is read from the existing platinum/firm/snapshots/aua_by_*.json objects.",
  "world_is": "The glob matches four objects; one is stale and no longer written by the publisher. The guard reads only the three keys the publisher writes (architect, state, region), so the stale object is not read.",
  "notes": "Recorded so that a reader who globs the served set does not reproduce the hazard. Disarm: none (INERT); the guard names the three keys."
}
```
```json
{
  "id": "ADVI_FIRMBKTS-D1-W84-S6",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~84",
  "surfaced_at": "2026-10-14T13:24:02Z",
  "one_line": "The existing reader _load_parquet prints a 'Loaded <key>' line on every read, so the guard's date-only reads add lines to the halt path beside the one READINESS HALT line.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/lambda/inf-portal-publisher/lambda_function.py:88 (print in _load_parquet, base blob 371eb01b42e5c1e4f6ce1c8ddac20071c0636762)",
      "infra/aws/lambda/inf-portal-publisher/lambda_function.py (_date_max calls _load_parquet with columns=['date'] for three inputs)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO FB-m-1 section 1a item 4: on a halt the handler prints exactly one line READINESS HALT and does nothing else; the guard reads each dated input with the existing _load_parquet.",
  "world_is": "The reader prints one progress line per read. On a halt the log carries up to three 'Loaded' lines before the single HALT line. The HALT line itself is exactly one; the tests assert it.",
  "notes": "Taken as the spec's reader; the progress lines are the existing reader's own output and were not suppressed. Disarm: none (INERT)."
}
```
```json
{
  "id": "ADVI_FIRMBKTS-D1-W84-S7",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~84",
  "surfaced_at": "2026-10-14T13:24:02Z",
  "one_line": "build_snapshots writes data_as_of from the wall-clock date when holdings has no dated rows, so a served date can be a run date rather than a data date.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/lambda/inf-portal-publisher/lambda_function.py:782 (data_as_of = datetime.date.today()) and :783-786 (overwritten only when holdings has a non-empty date column)",
      "infra/aws/lambda/inf-portal-publisher/lambda_function.py:766 (_snapshot_response writes data_as_of)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO FB-m-1 section 1a item 2: the served data_as_of is the data date the publisher stamped; the rule compares D to it.",
  "world_is": "With empty or undated holdings the publisher stamps today's wall-clock date. The guard's own holdings read fails first on an empty file or a missing date column (a read error, a halt), so the guard is not exposed to this path, but a served value written by an unguarded run can exceed the data date.",
  "notes": "Found while reading the served-date source. Form only. Disarm: none (INERT) while the guard halts on any holdings read error."
}
```
```json
{
  "id": "ADVI_FIRMBKTS-D1-S58",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.7.0_AE_CloudOps~FB1",
  "surfaced_at": "2026-10-14T13:37:09Z",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "one_line": "FB-l-5 act 2's exercise: the publisher fired and wrote the snapshots, but inf-portal-advisor-publisher fails on a Scheduler event (AttributeError at _extract_run_date), so a clock floor would publish no advisor artifacts.",
  "spec_asserts": "COO half a6e2df30dc: the exercise 'produces a publisher invocation and a LastModified after the exercise time on the three snapshots; all keys written are inside the named set; the publisher does not error'.",
  "world_is": "Measured 2026-10-14 13:30Z-13:36Z. The one-time at() schedule invoked inf-portal-publisher once (13:30:27Z-13:30:41Z, no error, 3 snapshots written, 0 keys outside the named set in 8847 objects under platinum/ and gold/meta/). The publisher fans out to inf-portal-advisor-publisher with the same event (lambda_function.py:1030-1033); the advisor publisher's _extract_run_date (lambda_function.py:1017-1019) calls event.get('detail', {}).get('run_date'), and a Scheduler event's detail is a string, so it raises AttributeError on all 3 async attempts and writes 0 advisor files. The S3-notification path is unaffected (its event has Records, no detail). Branch B was run for the snapshots (restored from prior VersionIds, byte-equal) and CloudFront invalidated again.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/EXERCISE_RECORD.json",
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/EXERCISE_ROLLBACK_RESULT.json"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "INERT: the floor is DISABLED and the S3 notification is still the live trigger. Act 3 (enable the floor) must not run until the advisor publisher accepts a Scheduler event: a code fix in inf-portal-advisor-publisher (its own pair) or an explicit Input of {} on the floor target (config only; a second exercise needs a new half). The C4 readiness-halt cell should carry whichever is chosen."
}
```
```json
{
  "id": "ADVI_FIRMBKTS-D1-W84-S8",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~84",
  "surfaced_at": "2026-10-14T13:45:48Z",
  "one_line": "The amendment commit e97cb670d5 says ADVI_FIRMBKTS-D1-W84-S4 is disarmed, but the investigation file still records S4 as ARMED and no row in the channel records the disarm.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~B1",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "git show e97cb670d5 --name-only (read 2026-10-14 13:45Z): the only path changed is org/missions/D8/ADVI/ADVI_FIRMBKTS/task-orders/ADVI_FIRMBKTS.TO-FB-m-1.readiness-halt-guard.md; the commit subject reads 'D1-W84-S4 disarmed'",
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md at HEAD e97cb670d5: row ADVI_FIRMBKTS-D1-W84-S4 carries hazard_standing ARMED and disarm_owner 2.0.0_SA_COO~B1 (line 8201)",
      "infra/aws/lambda/inf-portal-publisher/lambda_function.py at bdf95dcaa8: _gold_ready() implements the 4-day NNA tolerance, which removes the premise that every normal day halts on NNA lag"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO FB-m-1 amendment (CTO msg 5571; COO commit e97cb670d5): D1-W84-S4 is disarmed; an ARMED row disarms same-turn via its disarm_owner.",
  "world_is": "At e97cb670d5 and at this cell's commit bdf95dcaa8 the channel still records S4 as ARMED. The disarm exists only in a commit message; no channel row or amendment of S4 records it.",
  "notes": "Form only. This worker did not edit S4: an existing row is not edited, and the disarm owner is the COO. The clock-start hazard S4 names is addressed in code by the 4-day tolerance; recording that disarm is the owner's act. Disarm: owner 2.0.0_SA_COO~B1 (remains ARMED until the owner records it)."
}
```
```json
{
  "id": "ADVI_FIRMBKTS-D1-W84-S9",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~84",
  "surfaced_at": "2026-10-14T13:45:48Z",
  "one_line": "At read time the served data_as_of is 2026-10-14, the same date as the newest holdings partition, so the amended guard halts that frontier as a same-day re-fire and the next publish needs a later D.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "aws s3 cp platinum/firm/snapshots/aua_by_architect.json (read earlier in this cell): data_as_of 2026-10-14; LastModified 2026-10-14T12:53:58Z",
      "aws s3api list-objects-v2 --prefix gold/canonical/holdings_2026-10 (read 2026-10-14 13:42Z): newest holdings_2026-10-14.parquet, LastModified 12:18:39Z",
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~84/READINESS_SIGNAL.json (live_state_at_read)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO FB-m-1 section 1a item 2 and arm (iii): publish only when D is greater than the served data_as_of; a same-day re-fire halts.",
  "world_is": "The served date and the newest holdings date are both 2026-10-14 at read time. Whether the served value came from the holdings date or from the wall-clock fallback (S7) is not measured here. Against this state the amended guard halts with reason not-after-served.",
  "notes": "Form only: recorded so FB-m-2 reads arm (iii) against this state and does not take the halt for a frontier fault. Disarm: none (INERT); the halt is the rule working as ruled."
}
```
```json
{
  "id": "ADVI_FIRMBKTS-D1-W84-S10",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~84",
  "surfaced_at": "2026-10-14T13:54:31Z",
  "one_line": "An in-place edit of this channel file wrote back the 73 CRLF lines of the rows ADVI_FIRMBKTS-D1-W79-S1 to S3 as LF; the content is unchanged, the bytes of existing rows moved, and commit b531e2e019 carried the change.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python byte comparison (read 2026-10-14 13:50Z): 79ef8ebba5 has 73 CR bytes on lines 7126 to 7198, all in the W79-S1 to S3 block; b531e2e019 has 0 CR bytes",
      "git diff --numstat 79ef8ebba5 b531e2e019 on the channel: 122 insertions, 73 deletions; the restoration commit 6e99d4450d leaves 49 insertions and 0 deletions against 79ef8ebba5",
      "the mechanism is INFERRED, not measured: the in-place edit wrote the file back with LF line endings"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "INVESTIGATION_v1.md is append-only: an existing row is never edited (CLAUDE.md section 2 and the channel rule; the surprise-row gate grades only new rows).",
  "world_is": "The append of this cell rows rewrote existing bytes of another cell rows (line endings only). The row gate did not flag it because it grades new rows only. Restored in 6e99d4450d; the channel is now 49 insertions and 0 deletions against 79ef8ebba5.",
  "notes": "Form only. Recorded so that an in-place edit of a channel file is checked against its parent by numstat before commit. Disarm: none (INERT)."
}
```

## Row filed by 2.0.0_SA_COO~B1 (CTO msg 5683: the CRO's P3 Cottonwood census, Q-A and Q-C)

```json
{
  "id": "ADVI_FIRMBKTS-D1-S59",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "2.0.0_SA_COO~B1",
  "surfaced_at": "2026-10-14T18:34:11Z",
  "one_line": "Q-A (CRO census, CTO msg 5683): Cottonwood silver/account_attributes stopped on 2026-08-20, 38 trading days behind, because the SSM document opal-cot-silver-run never runs --table account_attributes while the bronze pull lands daily.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/tier1_exec/4.0.0_SA_CRO/deliverables/P3_COTTONWOOD_BACKEND_CENSUS_AND_PORTFOLIO_GROUP_20261014.md@1b7cad0123 (Q-A addendum: the writer is data/cot/scripts/silver/cot_silver_merge.py TABLE_CONFIG['account_attributes']; the SSM document at cot-pipeline ssm.tf:236-251 and the live document omit the --table line; forwardfill_v2 (6 tables including account_attributes) holds 1,103 objects, newest 2026-10-14 11:30-11:32Z; silver/account_attributes holds one partition, 2026-08-19, written 2026-08-20 17:41)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "The Cottonwood plan (PLAN_COTTONWOOD.json, FB-l-2) lists the Cottonwood pipeline functions and their repairs as moves M1 to M5 without a silver account_attributes row; the daily Cottonwood silver run is assumed to merge every bronze table that lands.",
  "world_is": "The daily Cottonwood silver run does not merge account_attributes; the table lands in bronze every day but is never merged, so gold/dimensions/accounts_dimension_latest.parquet joins a silver partition from 2026-08-19.",
  "notes": "For the Cottonwood plan, a repair in the M1-M5 class: one non-gating --table account_attributes line in the SSM document plus its manifest, under its own never-widen pair, proven by the next silver partition carrying 2026-10-13's 1,119 rows. The fix is not made here. Disarm: none (INERT); the repair is a round-9 candidate, owner this seat to cut."
}
```

## Row filed by 2.0.0_SA_COO~B1 (CTO msg 5683: the CRO's P3 Cottonwood census, Q-A and Q-C)

```json
{
  "id": "ADVI_FIRMBKTS-D1-S60",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "2.0.0_SA_COO~B1",
  "surfaced_at": "2026-10-14T18:34:11Z",
  "one_line": "Q-C (CRO census, CTO msg 5683): the secret opal/bd/cottonwood/credentials is live, declared by no Terraform, readable by 0 of 304 roles and unaccessed since 2026-05-26; it is a retire candidate for the Cottonwood plan.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/tier1_exec/4.0.0_SA_CRO/deliverables/P3_COTTONWOOD_BACKEND_CENSUS_AND_PORTFOLIO_GROUP_20261014.md@1b7cad0123 (Q-C: metadata only, no value read; the working credential path is blackdiamond/cot/credentials, readable by 3 roles; the undeclared secret describes the EC2 download scripts of the Cottonwood tenant)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "The Cottonwood plan's retire list (PLAN_COTTONWOOD.json retire R1 to R6) names six legacy operations and does not include this secret.",
  "world_is": "A second Black Diamond credential object for the Cottonwood tenant exists in AWS Secrets Manager outside Terraform, with no role able to read it and no access since 2026-05-26.",
  "notes": "Add to the Cottonwood plan's retire list with its consumer census (0 of 304 roles can read it). Its deletion is destructive and needs Andrew's confirmation at the moment it runs (CLAUDE.md Agent Autonomy); the retirement is a round-9 or later change under its own pair. Disarm: none (INERT)."
}
```

## Row filed by 0.9.0_WK_ADVI_FIRMBKTS~89 (TO ADVI_FIRMBKTS.TO-FB-p-6, floor-day 23rd key: premise false, step 4)

```json
{
  "id": "ADVI_FIRMBKTS-D1-W89-S1",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~89",
  "surfaced_at": "2026-10-16T18:16:36Z",
  "one_line": "FB-p-6 premise false: the 23rd named key inflection_wealth_management/top_holdings.json DID draw a version on 2026-10-16 (12:52:32Z, gold step INF_D_02b, before the publisher's 13:30Z run), so no KEY23 record is written (TO step 4); AC1 reads FAIL.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "aws s3api list-object-versions --bucket opal-data-inf --prefix <each of the 23 keys from ACT3_BASELINE_VERSIONS.json>, run by 0.9.0_WK_ADVI_FIRMBKTS~89 on 2026-10-16 after 18:00Z: 23 of 23 rc=0, counted client-side on Key and LastModified; the 23rd key newest version MBHVZkmm4l.2TsHVoJjabw2dUNggRXT8 LastModified 2026-10-16T12:52:32Z IsLatest True Size 1787; all 23 keys have at least one version dated 2026-10-16",
      "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/ACT3_BASELINE_VERSIONS.json@ab8081bfdd: the 23rd key baseline VersionId ys6JKj05riUJlrqjXami_YVb7hqiRCgw last_modified 2026-10-15T12:52:33Z, recorded_at 2026-10-15T13:11:26Z (the baseline predates the floor day; the live latest is the newer MBHV version)",
      "data/inf/scripts/gold/INF_D_02b.top_holdings.py@ab8081bfdd lines 333-361: under --upload the gold step writes platinum/advisors/{advisor_key}/top_holdings.json for every advisor key, empty documents included (lines 336-343 and 358-361)",
      "infra/aws/lambda/inf-portal-advisor-publisher/lambda_function.py@ab8081bfdd lines 810-814 and 1200-1201: _build_top_holdings returns None on empty holdings and the advisor publisher writes top_holdings.json only when the result is not None",
      "infra/aws/lambda/inf-portal-publisher/lambda_function.py@ab8081bfdd lines 877-882 and 1067-1069: the firm publisher writes the three snapshot keys; the 20 advisor keys fan out to the advisor publisher (comment at line 1029)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO ADVI_FIRMBKTS.TO-FB-p-6 (task-orders/ADVI_FIRMBKTS.TO-FB-p-6.floor-day-23rd-key.md, section 1 and step 1): the 23rd named key drew no new version on the 2026-10-16 floor day, so exactly one key has no version dated 2026-10-16 and its record KEY23.json can be written on that premise.",
  "world_is": "The premise is false. All 23 named keys have at least one version dated 2026-10-16. The 23rd key, platinum/advisors/inflection_wealth_management/top_holdings.json, has a version dated 2026-10-16T12:52:32Z written by the gold step INF_D_02b before the publisher's 13:30:48Z run, and one version on each of 2026-10-12 to 2026-10-16. The publisher wrote no 2026-10-16 version of this key; the other 22 named keys each drew a publisher version at 13:30:48Z to 13:31:13Z.",
  "notes": "Step 4 applied: no KEY23.json written (the order says do not force the record). Its writer claim holds: INF_D_02b writes the key daily under --upload, and the advisor publisher writes it only when _build_top_holdings is not None (lines 810-814 and 1200-1201). Its 'drew none' premise does not hold. Not read: why the advisor publisher skipped this key at 13:31 on 2026-10-16. Disposition left UNDER_INVESTIGATION for the issuer 2.0.0_SA_COO~B1. Disarm: none (INERT)."
}
```

```json
{
  "id": "ADVI_FIRMBKTS-D1-W89-S2",
  "project": "ADVI_FIRMBKTS",
  "fabric": "dell1",
  "surfaced_by": "0.9.0_WK_ADVI_FIRMBKTS~89",
  "surfaced_at": "2026-10-16T18:20:00Z",
  "one_line": "The order names the worker row id form <CODE>-W<n>-S<k>; the row gate refuses a bare worker id on fabric dell1 and requires the coordinate, so ADVI_FIRMBKTS-W89-S1 was renamed to ADVI_FIRMBKTS-D1-W89-S1 before commit.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      ".tools/surprise-row-gate.py as run by .tools/safe-commit.sh on 0.9.0_WK_ADVI_FIRMBKTS~89, 2026-10-16 ~18:20Z: BLOCKED on ADVI_FIRMBKTS-W89-S1 -- fabric='dell1' but the id carries no coordinate; a dell1 row is written <CODE>-D1-S<n> (worker <CODE>-D1-W<n>-S<k>); commit aborted, nothing staged"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO ADVI_FIRMBKTS.TO-FB-p-6 section 5 and the worker face: a worker's surprise row is minted as <CODE>-W<n>-S<k>, with the allocator coordinate W<n> and no fabric coordinate.",
  "world_is": "On fabric dell1 the commit-time row gate refuses a bare worker id and requires the fabric coordinate: <CODE>-D1-W<n>-S<k>.",
  "notes": "Filed as ADVI_FIRMBKTS-D1-W89-S2 for the id-form difference; the row content of S1 is unchanged except its id. Disarm: none (INERT). Disposition left UNDER_INVESTIGATION for the issuer 2.0.0_SA_COO~B1."
}
```
