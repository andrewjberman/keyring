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
