# COMM_ASSIST -- surprise channel, INVESTIGATION v1 (laptop fabric)

**Opened by:** `2.0.0_SA_COO~R`, 2026-10-08, on `1.0.0_SA_CTO` msg 107481. **Home:** the project tree's channel; the gate
`.tools/surprise-row-gate.py` validates every NEW row (schema `org/surprise_channel/schemas/investigation_item.schema.json`). Lane
`ANY`. A seat's row is `COMM_ASSIST-S<k>`; a worker's is `COMM_ASSIST-W<n>-S<k>`. **Append-only during the round.** Never edit an
existing row.

**Carried by reference from NFRA_CTLPLN's channel** (`org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md`;
the rows stay there): `NFRA_CTLPLN-S33`, `NFRA_CTLPLN-S34` (ARMED, disarmed in code by CT-i-13, closing on the FWD-3 full-day read),
`NFRA_CTLPLN-W36-S2` (handed to NFRA_TRNSPT in round 8's issuance).

## COMM_ASSIST-S1 -- carry record: S33 and S34 move here by reference, closing on FWD-3's full-day read

```json
{
  "id": "COMM_ASSIST-S1",
  "project": "COMM_ASSIST",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~R",
  "surfaced_at": "2026-10-09T00:04:35Z",
  "one_line": "Carry record: NFRA_CTLPLN-S33 (a refused End of Day redraft failed silently) and NFRA_CTLPLN-S34 (a chat's later drafts within a week were never texted) move to COMM_ASSIST by reference; both are disarmed in code (CT-i-13, live 2026-10-08 22:32Z) and close on FWD-3's full-day read.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md rows NFRA_CTLPLN-S33, NFRA_CTLPLN-S34",
      "NFRA_CTLPLN.TO-CT-i-13 merged 75420934c2; TO-APPLY-20 live 22:31:55Z/22:32:01Z, CodeSha256 xWURpe/nRkiZAc8Uui+arsJpSeVnUErNEHBWqtvrM5Q= (read by the issuer)",
      "1.0.0_SA_CTO msg 107481: 'run round 8 under COMM_ASSIST, carrying S33/S34/W36-S2 by reference'"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "FWD-3: no refusal fails silently, and every texted outcome is a text he got.",
  "world_is": "Fixed in code and applied; not yet exercised on a day with traffic (2026-10-08 22:31Z-23:22Z: 0 handler invocations).",
  "notes": "W36-S2 is handed to NFRA_TRNSPT (row file in that channel) and disarmed at NFRA_CTLPLN by S35."
}
```

## COMM_ASSIST-S2 -- W39-S1 does not bind: the gateway's Teams identity is unscoped (site Z code read); r29's read-back confirms

```json
{
  "id": "COMM_ASSIST-S2",
  "project": "COMM_ASSIST",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~R",
  "surfaced_at": "2026-10-09T02:12:50Z",
  "one_line": "Disarm read for NFRA_CTLPLN-W39-S1 (the gateway's caller map omits two Graph scopes the channel routes need): site Z reads MS_INGEST_IDENTITY as UNSCOPED, so its consent is the full GRAPH_SCOPES envelope and the omission does not bind; to confirm at r29's ENV read-back.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "site Z 1.0.0_SA_CTO~O msg 32269 (relay 0.0.0_AB_MSTR 107632): identity_scope.py:54-77 and identity_tool_allowlist.txt:19,25 scope exactly one identity, opalbloomberg@opalinvest.com; config.py:224; consent_scopes() returns None for an unscoped identity (:135-137)",
      "org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~39/CHANNEL_READ_SCOPES_MEASURED.md (both scope lists carry Team.ReadBasic.All, Channel.ReadBasic.All, ChannelMessage.Read.All)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "The channel routes shipping in NFRA_OPLGTW r29 get the Graph scopes they need.",
  "world_is": "True by code read on site Z; the host .env value of MS_INGEST_IDENTITY is not read (site Z's limit, stated).",
  "notes": "Closes when r29's ENV read-back shows MS_INGEST_IDENTITY is not the one scoped identity; then the first channel_poll line reads failed=0."
}
```

## COMM_ASSIST-Z-S1 -- PHASE A blocked: the shared transcripts root carries a required variable with no default, and this cell forbids -var

```json
{
  "id": "COMM_ASSIST-Z-S1",
  "project": "COMM_ASSIST",
  "fabric": "site-z",
  "surfaced_by": "0.7.0_AE_CloudOps~CA",
  "surfaced_at": "2026-10-09T12:28:26Z",
  "one_line": "PHASE A of CA-d-2 cannot take its preview plan: the shared root infra/aws/terraform/transcripts now carries a REQUIRED variable with no default (second_reader_trust_principal_arns, readers.tf:15, added by NFRA_TRNSPT), so terraform plan -target=module.ldo_001 exits 1 before evaluating anything, and this cell's rules forbid -var.",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~ZZ",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "PHASE_A_PLAN.txt (org/missions/D9/COMM/COMM_ASSIST/deliverables/0.7.0_AE_CloudOps~CA/): rc=1, 'Error: No value for required variable ... on readers.tf line 15: variable \"second_reader_trust_principal_arns\"'. No plan body was produced.",
      "DENOMINATOR: 6 of 6 root .tf files parsed (chat_assist.tf, commentary.tf, mail_pull.tf, main.tf, pull.tf, readers.tf); 6 root variables total; EXACTLY 1 has no default -- second_reader_trust_principal_arns. 0 .tfvars/.auto.tfvars present in the root, 0 tracked by git.",
      "POSITIVE CONTROL, same scratch TF_DATA_DIR and same init: 'terraform validate' -> rc=0 'Success! The configuration is valid.' The init took the declared s3 backend with no migrate or reconfigure prompt. So the failure is the missing variable VALUE alone, not the scratch setup, the backend or the config.",
      "DELIBERATE BY DESIGN, and the design is root-wide: readers.tf:12-13 -- 'var.second_reader_trust_principal_arns has NO default on purpose: the issuer's pair names the principal with Andrew's routing, and a plan without it is refused by terraform (a required variable).' Added by 0.9.0_WK_NFRA_TRNSPT~2 in 0693227a69 (2026-10-09 04:32 local, TO-TR-p18) and 3c68dab9c9 (07:52 local, TO-TR-r21).",
      "THE COLLISION: NFRA_TRNSPT TO-APPLY-a18 line 34 supplies it at ITS apply as `-var second_reader_trust_principal_arns=[\"arn:aws:iam::313476888478:user/Opal_Terminal\"]` and commits no default. CA-d-2's RULES FOR THIS CELL say 'Never `-var`' (and PHASE A says 'no -var'), because a -var on this shared root silently unwires the mail key on the next apply (COO half lines 11-13). The two orders are mutually unsatisfiable on the same root.",
      "STEP 4 and STEP 5 of PHASE A both read as expected and are NOT part of this block: both functions at CodeSha256 xWURpe/nRkiZAc8Uui+arsJpSeVnUErNEHBWqtvrM5Q= (LastModified 2026-10-08T22:32:01Z / 22:31:55Z), neither carries MAIL_BEARER_SECRET, policy teams-global-chat-assist-policy default v3, live zip 219476 bytes hashing to the same xWURpe/n... value; both builds rc=0; the COO half's Branch B import test rc=0 against dist/pkg."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "PHASE A takes a scratch, locked-off, targeted preview plan of module.ldo_001 with the variable at its committed default \"\" and no -var, reading '0 to add, 2 to change, 0 to destroy' with the two functions' source_code_hash/last_modified as the only changes.",
  "world_is": "No plan of ANY target in this root evaluates without a value for second_reader_trust_principal_arns. PHASE A produced no plan body, applied nothing, opened no ledger, read no secret and called no route. PHASE B is blocked by the same wall, since step 6 takes the same targeted plan under the same no--var rule.",
  "notes": "ID GRAMMAR: the order prescribes COMM_ASSIST-Z-AE-S<k>, which .tools/surprise-row-gate.py REFUSES (grammar <CODE>-(Z-)?(W<n>-|C-)?S<k>, annex v3.2 section 4 -- there is no AE- segment). Filed as the nearest grammatical seat-row id on the site-z fabric, COMM_ASSIST-Z-S1; COMM_ASSIST-Z-C-S1 (the CVO's, in surprise-channel/adjudications/ADJUDICATION_v1.Z.md) was the only Z- id already taken. No override was taken. The order's row-id line is the issuer's to correct. Not this seat's to widen: naming who may assume the second reader's role is NFRA_TRNSPT's never-widen pair with Andrew's routing, and passing it as -var here would be the exact unwiring CA-d-2 forbids. Three dispositions exist and all are the issuer's with the CTO: (a) NFRA_TRNSPT commits a default for the trust list, restoring a plannable shared root for every project; (b) CA-d-2 is amended to permit a -var for that one variable only, with the unwire risk re-signed; (c) the two roots are split. This seat STOPS here per PHASE A and holds, applying nothing."
}
```

```json
{
  "id": "COMM_ASSIST-Z-S2",
  "project": "COMM_ASSIST",
  "fabric": "site-z",
  "surfaced_by": "2.0.0_SA_COO~ZZ",
  "surfaced_at": "2026-10-09T12:50:17Z",
  "one_line": "Issuer ruling on COMM_ASSIST-Z-S1: CA-d-2 may pass -var for the ONE foreign variable second_reader_trust_principal_arns, with the value READ from the live role's trust policy at the act; its own mail-key variable stays a committed default; Branch A is unchanged.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~ZZ (disarm of COMM_ASSIST-Z-S1 executed by this row; amendment A3 to TO-CA-d-2)",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "NFRA_TRNSPT a18 is APPLIED: iam get-role teams-global-transcripts-second-reader-role -> CreateDate 2026-10-09T09:55:13Z, trust Principal AWS arn:aws:iam::313476888478:user/Opal_Terminal (read 12:4xZ); record b39a2d9dd1 'apply complete'.",
      "THE DEPENDENCY THE -var TOUCHES: module.ldo_001 takes aws_kms_key.transcripts (chat_assist.tf:81-82); that key's NamedReadersUseTheKey principal is local.named_reader_arns (main.tf:101-103), which includes aws_iam_role.second_reader.arn (readers.tf:25). So -target=module.ldo_001 plans the key and the second-reader role as dependencies. With the live trust value both read 'no changes'; with any other value they would change and Branch A's 'nothing outside the module' STOPs the act.",
      "The COO half's no--var reason binds OUR variable only (chat_assist_mail_bearer_secret_arn: a -var would be unwired by the next apply of the shared root). The foreign variable passed at its LIVE value is what NFRA_TRNSPT's own apply passes (TO-APPLY-a18:34), so no later apply moves it."
    ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Ruled inside the issuer's decomposition (amendment A3 to TO-CA-d-2): option (b), narrowed to the live value and to the one variable. Options (a) and (c) are NFRA_TRNSPT's or the CTO's and are not needed for this act. The three halves' blast radius is unchanged: Branch A still admits only module.ldo_001's two functions plus one policy ARN.",
  "spec_asserts": "CA-d-2 plans module.ldo_001 with no -var at all.",
  "world_is": "The shared root has a required variable with no default (by NFRA_TRNSPT's design), so every plan of it needs that one -var; the value that changes nothing is the live trust principal.",
  "notes": "The order's row-id line also moves to the gate grammar COMM_ASSIST-Z-S<k> in A3 (Z-S1's note)."
}
```

## COMM_ASSIST-Z-S3 -- PHASE B is BRANCH B: the plan reads Branch A exactly, but the package carries 827 lines the halves never reviewed (opal_naming.py among them)

```json
{
  "id": "COMM_ASSIST-Z-S3",
  "project": "COMM_ASSIST",
  "fabric": "site-z",
  "surfaced_by": "0.7.0_AE_CloudOps~CA",
  "surfaced_at": "2026-10-09T16:43:11Z",
  "one_line": "PHASE B went BRANCH B and applied nothing: the targeted plan reads Branch A's exact shape (0 add / 3 change / 0 destroy, module only, no key line), but the package it would ship is built from 827 lines of packaged-path change since the halves' baseline b1b8f5b4fe -- including lib/opal_naming.py, which all three halves declare UNCHANGED. The plan cannot see this, because source_code_hash moves identically either way.",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~ZZ",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "PHASE_B_PLAN_NOT_APPLIED.txt: 'Plan: 0 to add, 3 to change, 0 to destroy'; the three addresses are module.ldo_001.aws_iam_policy.exec (:44), .aws_lambda_function.handler (:100), .ingress[0] (:124). No aws_kms_key, no silver_reader, no second_reader. That IS Branch A as the COO half re-cut 1 states it -- the counts alone would have authorised the apply.",
      "BRANCH B LIMB, COO half Branch B: 'a packaged-path diff since b1b8f5b4fe outside the table above'. Measured git diff --stat b1b8f5b4fe..HEAD over EVERY path build.sh packages (handlers.py, modules/ldo/runtime/ldo.py, data/transcripts/scripts/teams_chat, daily_reports/eod/{post_format.py,VOICE.md}, lib/opal_naming.py, org/standards/NAMING_SCHEMA.json, infra/logic/registry/*.json): 7 files, +827 -6.",
      "LIMB 1 -- lib/opal_naming.py CHANGED (+2 -1): _is_cadence now also matches cadence.interval_form.token_regex. The COO half says verbatim 'Unchanged since the live build: handlers.py, ldo.py, daily_reports/eod/, lib/opal_naming.py, NAMING_SCHEMA.json'; the CTO half's signing table repeats it ('opal_naming.py and daily_reports/ are unchanged'). A packaged file all three halves recorded as unchanged has changed.",
      "LIMB 2 -- infra/logic/registry/reporting_policies.json has a CHANGED LEAF, not an addition: firms [\"cottonwood\"] -> [\"cottonwood\", \"49financial\", \"inflection\"] on the irpt reporting policy. Both halves measured the registry as '0 removed, 0 changed' leaf by leaf; this is a changed value, and it names two further firms inside a package deployed from a COMM tree.",
      "LIMB 3 -- infra/logic/registry/legacy_addresses.json changed (+20) and is NOT one of the seven registry files either half's table names (event_rules, key_rulings, name_rulings, reporting_policies, root_map, scopes, systems). It is packaged all the same: build.sh:28 copies infra/logic/registry/*.json by glob, so the half's enumeration is narrower than the build's.",
      "NOT A DEFECT, checked and cleared before filing: opal_naming.py's new branch reads cad['interval_form']['token_regex'], and NAMING_SCHEMA.json is unchanged since the baseline, so a KeyError in the Lambda looked possible. The packaged schema DOES carry cadence.interval_form.token_regex, and _is_cadence('daily') returns True against the built dist/pkg. No runtime break; the import test (rc=0) would not have caught one anyway, since the call is not at import.",
      "THE BUILD IS DETERMINISTIC, so the hash move is evidence of input change and not of build noise: build.sh:7 'Zipped with fixed timestamps so identical inputs give an identical zip (source_code_hash is stable)'. The same tree built 261471 bytes / +VT4f32xh... at 13:0xZ and 261765 bytes / hnffNee... at 16:2xZ.",
      "Steps 1-5 all read as expected and are not the blocker: secret ARN recorded by describe-secret (value never read), variable default committed 780f31c7cd, ledger opened and its entry AND sentinel committed d109b36f3c BEFORE the act, both functions still xWURpe/n... with MAIL_BEARER_SECRET null, policy still v3, rollback zip saved and hashing to the live value, both builds rc=0, import test rc=0. Act time 16:16Z, outside the 20:00Z-21:45Z End of Day stop."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Branch A is 0 add / 3 change / 0 destroy over module.ldo_001 only, and the package deployed is the one the halves reviewed: the measured 12-file diff a5fde91788..b1b8f5b4fe, with opal_naming.py, handlers.py, ldo.py, daily_reports/eod/ and NAMING_SCHEMA.json unchanged and the 7 registry files purely additive.",
  "world_is": "The plan satisfies Branch A exactly. The PACKAGE does not: 7 packaged files moved +827 -6 since b1b8f5b4fe, one of them a file the halves call unchanged, one a changed registry leaf naming two more firms, one a registry file outside the halves' enumeration. Nothing was applied: no safe-apply ran, no lock was taken (-lock=false), no function, policy or key changed, no mail was sent and nothing was invoked. Both functions remain at xWURpe/n... with no MAIL_BEARER_SECRET and the policy at v3.",
  "notes": "ARMED, and this is the part that needs a decision rather than a note: step 2's commit 780f31c7cd leaves the secret ARN as the variable's COMMITTED DEFAULT while the act is deferred. That is deliberate under the halves (committed, never -var, because the root is shared) but it now means ANY apply of infra/aws/terraform/transcripts by any project -- NFRA_TRNSPT owns the rest of it -- lands MAIL_BEARER_SECRET and this unreviewed package without passing Branch A. Three dispositions, all the issuer's with the signers: (a) re-sign the halves on the measured b1b8f5b4fe..HEAD packaged diff and re-cut the apply; (b) revert 780f31c7cd to default \"\" until the re-sign, which re-disarms the shared root; (c) pin the package by building at b1b8f5b4fe. This seat applied nothing and holds. ALSO FOR THE RECORD: the halves' Branch B enumerates 7 registry files by name while build.sh:28 packages them by glob, so the enumeration cannot keep up with the build -- the durable fix is to state the packaged set as the glob."
}
```

```json
{
  "id": "COMM_ASSIST-Z-S4",
  "project": "COMM_ASSIST",
  "fabric": "site-z",
  "surfaced_by": "2.0.0_SA_COO~ZZ",
  "surfaced_at": "2026-10-09T17:07:37Z",
  "one_line": "Issuer ruling on COMM_ASSIST-Z-S3 (amendment A6): the PHASE B GO is withdrawn, the committed mail-key default is reverted to empty until re-issue, the build is pinned at 2ad98c2e3a, and the COO half is re-cut (re-cut 2) on the measured drift. None of the drift reaches C-MAIL's sender set.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~ZZ (disarm of COMM_ASSIST-Z-S3 executed by this row; the revert of the default is A6's first act, by 0.7.0_AE_CloudOps~CA)",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "Issuer read b1b8f5b4fe..2ad98c2e3a over the packaged paths: 7 files +857/-6; COMM code 0 lines; the registry leaf census shows 4 changed leaves (key_rulings x3 metadata, reporting_policies policies[2].firms), the rest additive; legacy_addresses.json new.",
      "mail_requests.firm_domains() reads reg['scopes'] (scopes.json) and MAIL_PARTIES_PATH (mail_parties.json), both unchanged in that span; reporting_policies.json is not read by the mail path.",
      "name(teams, global, chat-assist, lambda, handler) at the pin = teams-global-chat-assist-handler-lambda (unchanged)."
    ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Ruled inside the issuer's decomposition: re-cut on the measured diff and the pinned build; the CTO and CVO re-sign before Phase B is re-issued. The hazard (a committed default with no signed package) is disarmed by A6's revert.",
  "spec_asserts": "The package Phase B ships equals the halves' measured table.",
  "world_is": "The trunk kept moving under the packaged paths after the halves were measured; a pinned build is the only way the measured table equals what ships."
}
```

```json
{
  "id": "COMM_ASSIST-Z-S5",
  "project": "COMM_ASSIST",
  "fabric": "site-z",
  "surfaced_by": "2.0.0_SA_COO~ZZ",
  "surfaced_at": "2026-10-09T19:22:53Z",
  "one_line": "Since the 18:33Z mail deploy, the poller's mail route has LISTED ZERO messages across 10 polls / 36 calls in ~48 min, every party domain included (Opal internal among them, Friday afternoon). Calls succeed (failed 0, refused 0), so either no party mail arrived or the route reads a mailbox or cursor other than the one intended.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~ZZ",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~ZZ/r12/checks/d2_mail_day.py --day 2026-10-09 at 19:21Z: poll_lines=10 domains=40 listed=0 fetched=0 sent=0 calls=36 refused=0 failed=0; considered_lines=0.",
      "Deploy a3057a3ed1: the mail step went live at 18:33Z (mail_poll calls 4, domains 4, failed 0)."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "FWD-4: mail from the five parties naming Andrew reaches the poller.",
  "world_is": "Zero listed in ~48 min. The discriminating act is the close plan's 19:30Z driver: one Opal-staff mail naming Andrew. If it is listed, the zero was organic; if not, the route's mailbox or cursor is the defect.",
  "notes": "Not BLOCKING: the close plan's driver mail is the falsifier and is already scheduled. The issuer resolves this row on that read."
}
```

## COMM_ASSIST-Z-S6 -- channel_poll fails its one call on EVERY ingress invocation and never raises ingress_step_failed; 63 of 63 in the hour BEFORE this deploy

```json
{
  "id": "COMM_ASSIST-Z-S6",
  "project": "COMM_ASSIST",
  "fabric": "site-z",
  "surfaced_by": "0.7.0_AE_CloudOps~CA",
  "surfaced_at": "2026-10-09T19:39:55Z",
  "one_line": "The ingress's channel_poll step has been failing its one call on EVERY invocation, long before this deploy: 63 occurrences of {\"event\": \"channel_poll\", \"failed\": 1, \"channels\": 0, \"mentions\": 0, \"read\": 0} in the hour BEFORE the apply, and it continues after. Found while reading step 7's log window; not caused by the mail deploy and not a rollback trigger.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "POST-APPLY window (18:33:30Z onward), /aws/lambda/teams-global-chat-assist-ingress-lambda: every invocation logs {\"calls\": 1, \"channels\": 0, \"event\": \"channel_poll\", \"failed\": 1, \"mentions\": 0, \"read\": 0}.",
      "CONTROL, the hour BEFORE the apply (17:30Z-18:33Z), same log group, filter-pattern channel_poll: 63 of 63 messages carry \"failed\": 1 and none carries \"failed\": 0. Denominator printed by a uniq -c over the extracted field. So the condition PRE-DATES the apply and this act did not cause it.",
      "The same window shows the deploy's own steps healthy: ingress_poll continuing, 0 ingress_step_failed, 0 not-configured, and mail_poll {calls:4, domains:4, failed:0, sent:0}. So channel_poll is an isolated step, not a symptom of the mail change.",
      "Read as log lines only, per the order's step 7; no message content was read."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "The ingress's steps either succeed or log ingress_step_failed. FWD-3: no refusal fails silently.",
  "world_is": "channel_poll fails its single call on every invocation and does NOT raise ingress_step_failed, so the failure is counted in a field and never escalated. 0 channels and 0 mentions are read as a result. Whether any product outcome depends on that step is NOT established here -- this seat only measured the counter, and naming the consequence needs the ingress owner.",
  "notes": "NOT this seat's and NOT part of CA-d-2: step 8's rollback fires on an AFTER failure CAUSED by the act, and the control shows this is not one, so the deploy correctly stood. Filed because a per-invocation failure that never escalates is exactly the FWD-3 silent-refusal shape. Owner is the COMM ingress's issuer; routed by filing rather than by message, since the CTO is copied on decisions only."
}
```

## COMM_ASSIST-Z-S7 -- cites Z-S5: the mail route LISTS (the zero was organic); the one mail considered was refused before the model as body_no_andrew; FWD-4 still not exercised

```json
{
  "id": "COMM_ASSIST-Z-S7",
  "project": "COMM_ASSIST",
  "fabric": "site-z",
  "surfaced_by": "2.0.0_SA_COO~ZZ",
  "surfaced_at": "2026-10-10T21:05Z",
  "one_line": "Z-S5's falsifier read: the mail route is NOT blind. Full day 2026-10-09 lists 42 and fetches 1; that one mail reached the considered step and was refused before the model as considered_body_no_andrew, so texted_ok=0. Day 2026-10-10 (to ~21:0xZ) lists 246 across 246 poll lines and fetches 0. FWD-4 stays APPLIED, not EXERCISED.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~ZZ",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~ZZ/r12/checks/d2_mail_day.py --day 2026-10-09 at ~21:05Z 2026-10-10: poll_lines=64 domains=256 listed=42 fetched=1 sent=1 calls=253 refused=0 failed=0 considered_lines=1 considered_ok=0 considered_body_no_andrew=1; MAIL-CLOSE texted_ok=0 refused_before_model=1 exercised=False.",
      "Same reader, --day 2026-10-10: poll_lines=246 domains=984 listed=246 fetched=0 sent=0 calls=984 refused=0 failed=0 considered_lines=0; exercised=False.",
      "Counted from log lines only; no mail content was read (the reader counts, never reads)."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "FWD-4: mail from the five parties naming Andrew reaches the poller and is texted to him.",
  "world_is": "The route lists and fetches, so Z-S5's 'mailbox or cursor is the defect' branch is falsified and its zero was organic. The single considered mail failed the names-Andrew test. Whether that mail was the 19:30Z driver mail is NOT established from counts. The 10-10 shape (listed equals poll lines, fetched 0) reads as one already-seen message re-listed each poll and skipped, and is unconfirmed.",
  "notes": "Resolves Z-S5's open question (the listing). What remains is FWD-4's exercise: one party mail whose body names Andrew. If the 19:30Z driver mail did name him, the body_no_andrew test is the defect. That is the discriminating question for the round-12 analysis, and only the sender or the CVO's flag judgment can answer it without this seat reading content."
}
```

## COMM_ASSIST-Z-S8 -- round 13 E1: no seat can send the driven mail from a non-Andrew Opal mailbox; routed to Andrew

```json
{
  "id": "COMM_ASSIST-Z-S8",
  "project": "COMM_ASSIST",
  "fabric": "site-z",
  "surfaced_by": "2.0.0_SA_COO~ZZ",
  "surfaced_at": "2026-10-10T23:30Z",
  "one_line": "Round 13 E1 needs ONE mail to Andrew from an Opal mailbox other than his own. The issuer names opalbloomberg@opalinvest.com, but no seat can send from it today: the estate's only application-credential path (irpt/graph/app-registration) does not exist, and the gateway's Graph access is delegated per user, with this seat's identity reading Andrew@opalinvest.com.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~ZZ",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "aws secretsmanager describe-secret --secret-id irpt/graph/app-registration at ~23:1xZ 2026-10-10: ResourceNotFoundException.",
      "opalgateway whoami from this seat at ~23:0xZ: userPrincipalName Andrew@opalinvest.com.",
      "infra/aws/lambda/investor-reporting/intake/graph_client.py auth_state(): the gateway's Graph model is DELEGATED per user and establishes no application grant.",
      "check_e1_body_considered.py at base a89f5575b1: the driven body passes considered() as ok in plain-text and HTML shapes; the nameless control is refused as body_no_andrew."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Round-12 analysis E1: a seat sends ONE mail from an Opal-domain mailbox other than Andrew's; if no seat can send from one, the cell's first act records that and the row goes to Andrew.",
  "world_is": "No seat holds a sending identity other than Andrew's. The send needs Andrew's hand: either an Opal colleague sends the exact text in decompositions/COMM_ASSIST_DECOMP.round13.md (cell CA-e-1) to Andrew@opalinvest.com, or he names or signs in a sending identity a seat may use. The rest of the round (E2, E3) does not wait on it.",
  "notes": "Routed to Andrew through 0.0.0_AB_MSTR~Z as one ask. On the send, the issuer runs check_e1_mail_day.py for the send day and resolves this row with a new citing row."
}
```
