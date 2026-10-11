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
