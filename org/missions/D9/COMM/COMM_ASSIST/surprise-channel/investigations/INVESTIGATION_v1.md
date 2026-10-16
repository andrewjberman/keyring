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

## COMM_ASSIST-Z-W7-S1 -- cites Z-S6: channel_poll 59 of 59 failed; dependent outcome is channel @mentions reaching Andrew's phone

```json
{
  "id": "COMM_ASSIST-Z-W7-S1",
  "project": "COMM_ASSIST",
  "fabric": "site-z",
  "surfaced_by": "0.9.0_WK_COMM_ASSIST~7",
  "surfaced_at": "2026-10-10T23:30Z",
  "one_line": "Cites COMM_ASSIST-Z-S6: channel_poll failed on 59 of 59 invocations in the last hour (calls=1, channels=0); the call most plausibly failing is teams (GET /teams). The code now names and raises it; the cure is unknown until the error field is read after deploy.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~ZZ",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "logs filter-log-events, /aws/lambda/teams-global-chat-assist-ingress-lambda, us-east-1, last 3600 s, pattern channel_poll: 59 lines, 59 of 59 failed=1, all calls=1 channels=0 read=0 mentions=0 (max-items 200, not cut short).",
      "data/transcripts/scripts/teams_chat/channel_mentions.py poll(): calls=1 with an empty team list is the gw.teams() call; the deployed code logs no error text, so the call is inferred, not read.",
      "infra/aws/ec2/opal-gateway/app/teams_route.py and server.py:1118-1121: the teams, channels and channel_messages routes exist in source; their deployed state and ALB routing are not established.",
      "deliverables/0.9.0_WK_COMM_ASSIST~7/CHANNEL_POLL_RULING.md"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "COMM_ASSIST-Z-S6 / FWD-3: no refusal fails silently; channel @mentions of Andrew reach his phone.",
  "world_is": "The outcome that depends on the channels step is FWD-3's 'every Teams message reaches his phone' for channel @mentions: 0 channel mentions are read while channel_poll fails 59 of 59 per hour. After the next deploy the channel_poll line carries error and the step logs ingress_step_failed; whether the cure is COMM's own code or the gateway (another project) is not established until that error is read.",
  "notes": "The order named id COMM_ASSIST-W7-S1; the row gate requires the site-z coordinate, so it is filed as Z-W7-S1. Z-S6 is cited, not edited. Ruling file in the worker deliverables folder."
}
```

## COMM_ASSIST-Z-S9 -- the COO half's import test run from the pinned worktree root resolves tenant from the REPO, not the package

```json
{
  "id": "COMM_ASSIST-Z-S9",
  "project": "COMM_ASSIST",
  "fabric": "site-z",
  "surfaced_by": "0.7.0_AE_CloudOps~CA",
  "surfaced_at": "2026-10-11T02:21:26Z",
  "one_line": "The COO half's import test, run from the pinned worktree root as TO-CA-f-1 step 1 directs, imports the REPO's data.transcripts.scripts.teams_chat.tenant rather than the built package's: the worktree root's data/ shadows the pkg namespace portion through the cwd entry on sys.path. It passed either way at this pin, so nothing is blocked, but from that cwd the test is not an oracle for the package.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~ZZ",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "cwd C:/tmp/ca-f1-pin (the pinned worktree root), command exactly as the COO half writes it: handlers.__file__ = <pkg>/handlers.py but tenant.__file__ = C:/tmp/ca-f1-pin/data/transcripts/scripts/teams_chat/tenant.py -- the repo tree, not the package. rc=0.",
      "cwd a neutral empty directory outside the repo, same command, same absolute pkg path: handlers.__file__ AND tenant.__file__ both under <pkg>/. rc=0. This is the reading the half's Branch B is graded on, and it PASSES.",
      "python -I against the same pkg is NOT a valid control: -I implies -s, which drops user site-packages, so it fails in assist.py at zoneinfo.ZoneInfo('America/New_York') with ZoneInfoNotFoundError for a missing tzdata wheel. On the Lambda (python3.12, Linux) the system tz database is present, so that failure is an artifact of the control, not of the package.",
      "d1_live.py's own probe carries the same hazard in a comment and defends against it with cwd=tmp; the half's one-line import test has no such defence."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "COO never-widen half @3d80c80db2, Branch B: 'the import test failing against the built dist/pkg' -- python -c \"import sys; sys.path[:0]=['<pkg>']; import handlers, data.transcripts.scripts.teams_chat.tenant\". TO-CA-f-1 step 1: every build and test runs FROM the pinned worktree.",
  "world_is": "From the pinned worktree root those two instructions compose into a test that resolves tenant out of the repo working tree. A regular package (repo data/ with __init__.py) beats a namespace portion (pkg/data without one) regardless of sys.path order, so prepending the pkg path does not win. CA-f-1 satisfied Branch B on the neutral-cwd reading, which is sound; the row is filed so a later half does not inherit the unsound form. Fix, if the issuer wants one: run the import test from a directory holding no data/, or pass the cwd explicitly as d1_live.py does.",
  "notes": "Found off-task during CA-f-1 step 4. Nothing was widened and nothing waits on this row. Not a defect in the deployed package: the live package was proved by CAf1-AC1 (served zip == CodeSha256, both round-13 files byte-equal the pin, served code refuses a sixth firm)."
}
```

## COMM_ASSIST-Z-S10 -- cites Z-W7-S1 / Z-S6: the now-readable error names the failing call as route=teams status=404

```json
{
  "id": "COMM_ASSIST-Z-S10",
  "project": "COMM_ASSIST",
  "fabric": "site-z",
  "surfaced_by": "0.7.0_AE_CloudOps~CA",
  "surfaced_at": "2026-10-11T02:23:56Z",
  "one_line": "Cites COMM_ASSIST-Z-W7-S1 and COMM_ASSIST-Z-S6: the error field the CA-f-1 deploy made readable now NAMES the failing call -- route=teams status=404 error=None, on every post-deploy invocation. The question Z-W7-S1 left open (COMM's code or the gateway) is answered on the evidence: a 404 on the gateway's /teams route, which is not COMM's write surface.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~ZZ",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "logs filter-log-events, /aws/lambda/teams-global-chat-assist-ingress-lambda, us-east-1, from the ingress LastModified 2026-10-11T02:17:01Z: 39 events, 19 carrying an event field -- ingress_poll 6, channel_poll 6, ingress_step_failed 6, mail_poll 1 (max-items 500, not cut short).",
      "channel_poll payload, verbatim log fields only: {\"calls\": 1, \"channels\": 0, \"error\": \"route=teams status=404 error=None\", \"event\": \"channel_poll\", \"failed\": 1, \"mentions\": 0, \"read\": 0}.",
      "ingress_step_failed by step: {'channels': 6} -- channels only; never mail, chats or eod.",
      "ingress_poll continues: {\"chats_read\": 2, \"event\": \"ingress_poll\", \"events\": 0, \"first_run\": false, \"messages\": 0, \"pages\": 1}. mail_poll logged once in the window.",
      "Base reading for contrast (COO half, Z-W7-S1): 59-60 channel_poll per hour, all failed, 0 with an error, 0 ingress_step_failed."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "FWD-3: channel @mentions of Andrew reach his phone. Round-14 D2 cures the call the new error field names.",
  "world_is": "The call is GET /teams against GATEWAY_BASE https://mcp.opalinvest.dev and it returns HTTP 404. status=404 with error=None means the response carried no parsable error code, which is the shape of a route that is not served rather than a request the route rejected. What this row does NOT establish: whether the gateway's teams route is undeployed, unrouted at the ALB, or served under a different path -- that plane is NFRA_OPLGTW's and this seat did not read it. The CVO half named exactly this as BLIND to CA-f-1.",
  "notes": "Filed by the applier because CA-f-1's whole purpose was to make this datum readable, and it is now read. Z-W7-S1 and Z-S6 are cited, not edited. D2's owner can start from the 404 rather than re-deriving it. Non-application: this row proposes no fix and no gate."
}
```

## COMM_ASSIST-Z-S11 -- cites Z-S10: the 404 is the DEPLOYED gateway lacking /hx/teams/teams; the client path is right; D2's cure is NFRA_OPLGTW's release

```json
{
  "id": "COMM_ASSIST-Z-S11",
  "project": "COMM_ASSIST",
  "fabric": "site-z",
  "surfaced_by": "2.0.0_SA_COO~ZZ",
  "surfaced_at": "2026-10-11T02:55Z",
  "one_line": "Cites Z-S10: COMM's client calls GET /hx/teams/teams (assist.py:169 + :209), exactly the route the gateway SOURCE declares (teams_route.py:13/:55, added 2026-10-08 by NFRA_CTLPLN CT-i-11 @863e37d1f9). Chats on the same /hx/teams prefix are served live (ingress_poll chats_read=2). So the deployed gateway does not serve the teams/channels routes. The cure is a gateway release, which COMM cannot write: D2 is routed to NFRA_OPLGTW.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~ZZ",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "d1_errorfield.py at 02:50Z: channel_poll=33, failed=33, with_error=33, ingress_step_failed[channels]=33 since the 02:17:01Z deploy; error values: 30 x 'route=teams status=404 error=None' in the last 30 min.",
      "data/transcripts/scripts/teams_chat/assist.py:169 url = base + '/hx/teams' + path; :209 teams() calls GET '/teams'.",
      "infra/aws/ec2/opal-gateway/app/teams_route.py:13 'GET /hx/teams/teams', :51 PREFIX = '/hx/teams', :55 TEAMS_ROUTE = PREFIX + '/teams'; git log -S: introduced by 863e37d1f9 (0.9.0_WK_NFRA_CTLPLN~39, 2026-10-08).",
      "Z-S10: ingress_poll continues with chats_read=2, so /hx/teams/chats is served by the same gateway."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Round-14 D2: fix the cause the error field names, or route it to the owner it names (gateway route, load balancer or token scope).",
  "world_is": "The owner is the gateway's release: the teams/channels routes are in source and not served. Not established here: whether the gap is the deployed gateway build or the load balancer's path rules, since both are NFRA_OPLGTW's plane. COMM needs no code change; once the route serves, channel_poll should read failed=0 with no COMM deploy.",
  "notes": "Routed as one ask to NFRA_OPLGTW's issuer. Resolves when one hour of ingress reads channel_poll failed=0 and one real channel @mention reaches Andrew (D2's done-when)."
}
```

```json
{
  "id": "COMM_ASSIST-Z-S12",
  "project": "COMM_ASSIST",
  "fabric": "site-z",
  "surfaced_by": "3.0.0_SA_CVO~Z",
  "surfaced_at": "2026-10-11T22:45Z",
  "one_line": "Cites COMM_ASSIST-Z-S10 and Z-S6: channel_poll is HEALTHY since the gateway's /hx/teams release -- 29 of 29 channel_poll events in the 30 minutes to ~22:4xZ 2026-10-11 read failed=0 with channels=8, after failing every minute on route=teams status=404.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~ZZ",
  "spec_asserts": "Z-S10's remedy: a gateway release that serves the teams and channels routes; then COMM reads D2's done-when (an hour of channel_poll failed=0 and one real channel @mention reaching Andrew).",
  "world_is": "NFRA_OPLGTW OG-ap-7 released CT-i-11's /hx/teams/* (release 28ba9532b6, GET /hx/teams/teams 200; NFRA_OPLGTW round-34 packet @fd3f189ece). COMM's ingress log now reads failed=0 with 8 channels listed. This seat read 30 minutes, not the hour D2 names, and read no mention; the mention half is the issuer's read.",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "aws logs filter-log-events /aws/lambda/teams-global-chat-assist-ingress-lambda, filter channel_poll, last 1800 s at ~22:4xZ: 29 x 'failed': 0, 29 x 'channels': 8",
      "NFRA_OPLGTW ADJUDICATION_v25.Z.md header (this seat, @8503c3f3e8)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Filed by the CVO as a carrier: this seat cannot message the issuer. The issuer's D2 read (one hour, one mention) resolves Z-S10 and Z-S6 with a citing row."
}
```

## COMM_ASSIST-Z-S13 -- the released gateway's channel_messages route answers 502 about once every two hours

```json
{
  "id": "COMM_ASSIST-Z-S13",
  "project": "COMM_ASSIST",
  "fabric": "site-z",
  "surfaced_by": "2.0.0_SA_COO~ZZ",
  "surfaced_at": "2026-10-11T23:40Z",
  "one_line": "Cites Z-S12: since the 18:49Z /hx/teams release, 2 of about 285 channel_poll runs failed, both 'route=channel_messages status=502 error=None' (21:27:39Z and 23:30:36Z). Each is a single call; the next poll re-reads that channel on its kept cursor, so no mention is lost, but each one fails D2's strict hour of failed=0 for an hour.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~ZZ",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "aws logs filter-log-events /aws/lambda/teams-global-chat-assist-ingress-lambda, filter channel_poll, last 21600 s at ~23:38Z: 360 channel_poll lines; failures after 18:49:30Z: 2, both route=channel_messages status=502 error=None.",
      "channel_mentions.poll(): a channel whose read raises keeps its old cursor and read_at, so it is read first next poll (channel_mentions.py _read_channel / poll)."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "D2 done-when (round-14 analysis): one hour of ingress reads channel_poll failed=0, and one real channel @mention reaches Andrew.",
  "world_is": "The released gateway's GET /hx/teams/channels/{team}/{channel}/messages returns HTTP 502 intermittently, about once per 140 polls. A 502 with no error body is the shape of an upstream (Graph) or proxy failure, not a missing route. Whose plane: the gateway's (NFRA_OPLGTW). Not established: whether Graph throttled or the gateway's upstream call timed out; this seat read only COMM's log.",
  "notes": "Non-blocking for D2's mention arm. If the 502 rate holds, D2's hour arm can still pass in any clean hour; the issuer grades D2 on a clean hour plus the mention. A retry in channel_mentions would hide the gateway's 502s, not cure them, so none is proposed here. Pointed to NFRA_OPLGTW's issuer as one line."
}
```

## COMM_ASSIST-W8-S1 -- the default AWS executable name and the repo shim do not launch bare from Python on this laptop

```json
{
  "id": "COMM_ASSIST-W8-S1",
  "project": "COMM_ASSIST",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_COMM_ASSIST~8",
  "surfaced_at": "2026-10-13T18:30:01Z",
  "one_line": "TO CA-h-1 BUILD 1 names MUSE_AWS_BIN default 'aws' and the repo shim .tools/aws as the working form; from Python on this Windows laptop, bare 'aws' fails to launch and bare 'bash' hits the WSL stub.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "Measured 2026-10-13 ~18:2xZ from Python 3.12.10 on this laptop, worktree wk-COMM_ASSIST-8 at base 3477d67af5: subprocess.run(['aws','--version']) raised FileNotFoundError [WinError 2]; subprocess.run([C:\\Program Files\\Git\\usr\\bin\\bash.exe, '.tools/aws', '--version']) returned rc 0 (aws-cli/1.44.44); subprocess.run(['bash', ...]) returned rc 1 with 'WSL ... execvpe(/bin/bash) failed'.",
      "shutil.which('aws') returned C:\\Users\\AndrewBerman\\bin\\aws.CMD and subprocess on that path returned rc 0; refresh.py aws_bin() resolves MUSE_AWS_BIN with shutil.which, so the default works here. The repo shim was not the form used; .tools/aws is a bash script and needs Git Bash."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO COMM_ASSIST.TO-CA-h-1 BUILD 1: AWS reads go through the AWS CLI by subprocess, executable name from MUSE_AWS_BIN, default aws; on this laptop the working form is the repo shim .tools/aws.",
  "world_is": "On this laptop the default 'aws' resolves only through shutil.which to aws.CMD (the ~/bin forwarder), not through CreateProcess; the repo shim works only when launched by Git Bash. dell2's launch form is unmeasured here (CA-h-2 reads it on the host). A launch failure is caught per source and shows as unreadable, so the failure is loud, not silent.",
  "notes": "No disarm needed: refresh.py already uses the shutil.which form measured here. CA-h-2 must measure the launch form on dell2 before scheduling. Pointed to the CA-h-2 seat via this row."
}
```

## COMM_ASSIST-W8-S2 -- drafts: pending is not a table attribute; it sits inside the state row's data JSON

```json
{
  "id": "COMM_ASSIST-W8-S2",
  "project": "COMM_ASSIST",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_COMM_ASSIST~8",
  "surfaced_at": "2026-10-13T18:30:01Z",
  "one_line": "TO CA-h-1 BUILD 3 reads the rows 'whose pending is non-null'; in teams-global-chat-assist-table pending is a key inside a JSON string in the data attribute of the sk='state' row, not a top-level attribute.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/terraform/modules/ldo/runtime/ldo.py at base 3477d67af5: load() lines 145-152 reads item['data']['S'] as JSON and item['version']['N']; the commit writes pk=object id, sk='state', data=S(json.dumps(state)), version=N (lines 236-241). Index rows are pk='#index#<namespace>'; event markers are sk='event#<id>' (lines 223-258).",
      "data/transcripts/scripts/teams_chat/tenant.py lines 17-19 at base 3477d67af5: STATE chat {title, chat_type, recent, tag, pending}, eod {day, tag, pending, done}; pending = {tag, kind, draft, version, incoming, chat_title, texted_at, status, send_at}."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO COMM_ASSIST.TO-CA-h-1 BUILD 3: drafts = the rows of teams-global-chat-assist-table whose pending is non-null; read how the table is keyed and how pending is shaped in tenant.py and assist.py.",
  "world_is": "Keyed by pk (the object id: a chat id, eod:<day>, inbox:owner) and sk ('state' for the state row). The reader parses data and reads state['pending']. The table also holds index and event rows, which the reader skips. Measured: one whole-table scan read 556 to 558 rows over 2 pages (the count moves, the table is live) and returned 4 pending rows.",
  "notes": "The reader treats a state row whose data does not parse as unreadable for the whole source, rather than dropping it silently."
}
```

## COMM_ASSIST-W8-S3 -- the AWS CLI prints nothing for a get-item whose row is absent

```json
{
  "id": "COMM_ASSIST-W8-S3",
  "project": "COMM_ASSIST",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_COMM_ASSIST~8",
  "surfaced_at": "2026-10-13T18:30:01Z",
  "one_line": "aws dynamodb get-item for a missing row returns rc 0 with EMPTY stdout, not a JSON document; a reader that parses stdout reads absence as a failure.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "Measured 2026-10-13 ~18:2xZ: get-item --table-name teams-global-chat-assist-table --key {pk: eod:2026-10-13, sk: state} --consistent-read: rc 0, stdout 0 bytes, stderr 0 bytes (the day's End of Day row does not exist yet).",
      "Positive control, same call shape on an existing state row (pk taken from a scan page): rc 0, stdout 794 bytes, JSON with an Item key. The key file form file://<drive>/<path> resolved in both."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO COMM_ASSIST.TO-CA-h-1 BUILD 3: eod_today reads the single row eod:<today>; no such row raises Absent.",
  "world_is": "The AWS CLI emits nothing for a get-item response with no Item. Absence is therefore empty stdout with rc 0, which the reader must map to Absent, never to a parse error or an empty list. refresh.py does so (text.strip() empty -> no Item -> Absent).",
  "notes": "Any other command with an empty-response shape (a query with no items, for one) can read the same way; the reader that parses it must treat empty stdout explicitly."
}
```

## COMM_ASSIST-W8-S4 -- sprint_today: the publisher takes a report day from a person and defines no today

```json
{
  "id": "COMM_ASSIST-W8-S4",
  "project": "COMM_ASSIST",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_COMM_ASSIST~8",
  "surfaced_at": "2026-10-13T18:30:01Z",
  "one_line": "The sprint key is formed by daily_reports/scripts/publish_daily_report.py from an explicit --date; nothing in the producer names 'today', so the reader defines today itself.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "daily_reports/scripts/publish_daily_report.py at base 3477d67af5: PREFIX 'daily-reports/' (line 41), BUCKET 'opal-data-portal-v2' (line 40), _key(day, variant) = PREFIX + day + '/' + variant + '_DAILY_REPORT_' + day + '.html' (lines 54-55); main() takes --date as required input (line 143).",
      "data/transcripts/scripts/teams_chat/tenant.py eod_today(now) = now in America/New_York, strftime %Y-%m-%d (line 76-77); the reader uses the same zone and form."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO COMM_ASSIST.TO-CA-h-1 BUILD 3: sprint_today lists today's prefix under s3://opal-data-portal-v2/daily-reports/; read how daily_reports keys are formed; do not guess.",
  "world_is": "The key form is measured from the producer. 'Today' is not in the producer; refresh.py takes the New York date, the same as the End of Day key. A report published under another day reads as absent for today. Measured: today's prefix daily-reports/2026-10-13/ lists 0 objects (absent); the prefix daily-reports/ lists keys from 2026-08-27 on (positive control, first page of 5, truncated).",
  "notes": "Judgment, not measurement: New York date chosen to match the End of Day key. The sprint publisher's day rule is owned by its producer; this row only records that the reader supplies it."
}
```

## COMM_ASSIST-W8-S5 -- a whole-repo content search exceeds the bounded call

```json
{
  "id": "COMM_ASSIST-W8-S5",
  "project": "COMM_ASSIST",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_COMM_ASSIST~8",
  "surfaced_at": "2026-10-13T18:30:01Z",
  "one_line": "comp-find with a content pattern and no pathspec (DAILY_REPORT_, 81,506 files in scope) did not return inside the 120 s bound; the name search for the same file answered at once.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "timeout 120 comp-find 'DAILY_REPORT_' from the worktree root: moved to background, ended with exit 143 at the bound, no output recorded.",
      "timeout 100 comp-find --name publish_daily_report --files: returned in time with DENOMINATOR 1 hit across 81506 files, HEAD=1, daily_reports/scripts/publish_daily_report.py."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO COMM_ASSIST.TO-CA-h-1 navigation: comp-find and comp-read; navigate to the paths given, do not hunt.",
  "world_is": "A content search over the default corpus without a pathspec is not usable inside the bound from this laptop. A name search is. The worker narrowed by name and read the named files directly.",
  "notes": "Recorded for the tooling owner. Not a block: each file was reached by its named path or a name search."
}
```

## COMM_ASSIST-W8-S6 -- the stale-version refusal (unseen) is not reached by the edit (redraft) branch of on_sms_reply

```json
{
  "id": "COMM_ASSIST-W8-S6",
  "project": "COMM_ASSIST",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_COMM_ASSIST~8",
  "surfaced_at": "2026-10-13T18:49:41Z",
  "one_line": "on_sms_reply calls unseen() (the stale-version refusal) only for send and drop; the edit (redraft) branch applies Andrew's notes to whatever draft is pending, so a redraft answer to a draft that changed is not refused.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "data/transcripts/scripts/teams_chat/tenant.py@38ac43222d:497 reads 'if action in (\"send\", \"drop\") and unseen(ctx, p):'",
      "data/transcripts/scripts/teams_chat/tenant.py@38ac43222d:527-530 the edit branch pushes the dialog and redrafts the current pending p with no unseen() call",
      "data/transcripts/scripts/teams_chat/tenant.py@38ac43222d:137-138 unseen() returns True on a version mismatch, so the check exists and the edit branch does not reach it"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "tenant.py@38ac43222d:498-499: a reply to a draft that changed is refused with 'changed just before your reply, so nothing was done'.",
  "world_is": "A redraft (edit) reply is applied to the current pending draft without the version check. The new version is texted for approval and nothing is posted, so no Teams post follows from it. Measured by reading the code only; not exercised.",
  "notes": "MUSE_ANSWER_PATH_DESIGN.md section 4 relies on the assistant's check, which does not hold for edit. The fix sits in tenant.py, outside CA-h-3; the forwarder's version check is the only guard for edit until then."
}
```

## COMM_ASSIST-W8-S7 -- the muse public key the design relies on is not named anywhere in the repo

```json
{
  "id": "COMM_ASSIST-W8-S7",
  "project": "COMM_ASSIST",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_COMM_ASSIST~8",
  "surfaced_at": "2026-10-13T18:49:41Z",
  "one_line": "The CA-h-3 premise that muse's public key is already in the boxes' administrators_authorized_keys cannot be checked from the repo: no muse key, principal or device row exists in org/devices/ or .tools/.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/devices/DEVICES.json@38ac43222d:105-120 holds the dell2 row only; no muse row",
      ".tools/ssh-tailnet-enable.ps1@38ac43222d:40 KeysPath, :254 AuthorizedKeysFile for Match Group administrators, :496 keys-file ACL; no muse key in the file",
      "content search for muse over org/devices/ and .tools/ at base 38ac43222d returned no match"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "CA-h-3 cell, section 1 choice (a): a signature made with muse's own key, whose public key is already in administrators_authorized_keys.",
  "world_is": "The repo does not name muse's key, principal or fingerprint. Whether the key is on the box is not measured; the design states choice (a) on the premise and marks the fingerprint not measured.",
  "notes": "The design does not depend on the key being named in the repo; it depends on a pinned allowed_signers that the build cell creates from muse's key once it is read on the box."
}
```

## COMM_ASSIST-W8-S8 -- drafts.json carries no object id, and the assistant routes sms.reply by object id

```json
{
  "id": "COMM_ASSIST-W8-S8",
  "project": "COMM_ASSIST",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_COMM_ASSIST~8",
  "surfaced_at": "2026-10-13T18:49:41Z",
  "one_line": "The forwarder cannot route an answer from the CA-h-1 reader folder alone: drafts.json rows carry tag and version but no object id, and sms.reply is delivered to the object id found through the sms-tag index.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "data/transcripts/scripts/muse_reader/refresh.py@38ac43222d:230-234 _draft_row keeps tag, kind, version, status, texted_at, send_at, draft, chat_title; no object id",
      "data/transcripts/scripts/teams_chat/tenant.py@38ac43222d:1157 the text path resolves oid = ldo.lookup('sms-tag', tag) and sends sms.reply to oid",
      "infra/aws/terraform/modules/ldo/runtime/ldo.py@38ac43222d:152-155 lookup reads the item at pk '#index#' + namespace, sk key"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "CA-h-3 section 5: the forwarder writes one sms.reply entry for the draft's object, found from the reader folder's tag and version.",
  "world_is": "The object id is not in the reader folder. The design makes the forwarder read the #index#sms-tag row (a DynamoDB GetItem), or asks CA-h-1's layout to carry object_id. The design names the read; it does not change refresh.py.",
  "notes": "A read of the state table is needed beyond the SQS write statement in section 5 of the design."
}
```

## COMM_ASSIST-W8-S9 -- the CA-h-1 reader folder has no answers location for muse's answer file

```json
{
  "id": "COMM_ASSIST-W8-S9",
  "project": "COMM_ASSIST",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_COMM_ASSIST~8",
  "surfaced_at": "2026-10-13T18:49:41Z",
  "one_line": "The CA-h-3 cell says muse writes an answer file into the CA-h-1 reader folder, but the CA-h-1 layout has no answers location: refresh.py writes only its six fixed names.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "data/transcripts/scripts/muse_reader/refresh.py@38ac43222d:57-68 the README text lists open_calls.json, drafts.json, eod_today.json, sprint_today.json, INDEX.json and README.txt; no inbox",
      "data/transcripts/scripts/muse_reader/refresh.py@38ac43222d:182-183 the only writes are INDEX.json and README.txt, with each source written by name at :178"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "CA-h-3 cell: muse writes an ANSWER FILE into the dell2 reader folder laid out in CA-h-1.",
  "world_is": "No answers folder exists in the CA-h-1 layout. The design names <reader root>/answers/ as a folder the CA-h-2 or later build must create; refresh.py does not create it and was not changed here.",
  "notes": "A refresh that rewrites only its named files leaves an answers/ folder untouched, so the two do not collide."
}
```

## COMM_ASSIST-S3 -- NFRA_CTLPLN round 12 has no cell that reads muse's key on dell2

```json
{
  "id": "COMM_ASSIST-S3",
  "project": "COMM_ASSIST",
  "fabric": "laptop",
  "surfaced_by": "2.0.0_SA_COO~CA",
  "surfaced_at": "2026-10-13T19:07:29Z",
  "one_line": "NFRA_CTLPLN round 12 has no cell that reads muse's key on dell2, and the CTO direction makes that a precondition of grading FWD-6 (muse to dell2 over tailnet SSH by key).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/tier1_exec/1.0.0_SA_CTO/deliverables/PIVOT_DIRECTION_20261013/DIRECTION_COO_CA_COMM_ASSIST_MUSE_20261013.md section 2 point 5: before FWD-6 is graded, round 12's SSH cell must read back muse's key on dell2; if it does not cover muse to dell2, file a surprise row naming it",
      "org/missions/D0/NFRA/NFRA_CTLPLN/task-orders/NFRA_CTLPLN.TO-CT-ab-7.ssh-tools-kbdint-and-replan.md THE CELL: scoped to the verify tool's password grading, the -i key choice and the enable script's default rule; the word muse occurs 0 times in it (case-sensitive count)",
      "org/missions/D0/NFRA/NFRA_CTLPLN/task-orders/ round-12 orders TO-CT-ab-1,3,4,5,7,8,9,11,12 listed by name; none names muse (the one case-insensitive hit in ab-1 is the substring in 'IamUsers')"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Direction section 2 point 5: round 12's SSH cell reads back muse's key on dell2, so FWD-6's exercise (muse to dell2 over tailnet SSH by key) rests on a measured key.",
  "world_is": "Round 12's SSH cell (CT-ab-7) fixes how the laptop verifies and enables SSH on the boxes; it does not install or read back muse's public key on dell2. Whether muse's key is already in dell2's administrators_authorized_keys is not measured here; row W8-S7 found the key in no repo file.",
  "notes": "CA-h-2 (host act on dell2) includes one SSH read from muse; its order will carry the key read-back as its own first step unless NFRA_CTLPLN adds the cell first. Owner of the gap: 1.0.0_SA_CTO."
}
```

## COMM_ASSIST-W11-S1 -- an unreadable drafts.json would make the once-only rejection permanent, so the forwarder defers instead

```json
{
  "id": "COMM_ASSIST-W11-S1",
  "project": "COMM_ASSIST",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_COMM_ASSIST~11",
  "surfaced_at": "2026-10-13T22:37:00Z",
  "one_line": "The BUILD rule rejects an answer file whose tag has no drafts.json row, and rejection writes a permanent marker. A refresh that could not read drafts writes items null, so the literal rule would reject every valid answer for good. The forwarder defers those files instead: no marker, no send, retried next run.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "data/transcripts/scripts/muse_reader/refresh.py@8bf64bac36:80-84 the README the refresh writes: an unreadable source has items null; absent and unreadable are never an empty list",
      "data/transcripts/scripts/muse_reader/forwarder.py@8bf64bac36 (new file, CA-i-3 commit) _draft_rows raises DraftsUnreadable when items is not a list; forward() counts the file failed and writes no marker",
      "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r17/checks/check_i3_forward.py@8bf64bac36:30 the check always writes drafts.json with a list, so the deferral arm is not exercised by the issuer's check"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO CA-i-3 BUILD step 1: a file whose tag has no row in root/drafts.json with a non-empty object_id is written to answers/rejected/<sha>.json with reason tag-not-waiting; a rejected marker makes later runs skip the same bytes.",
  "world_is": "refresh.py writes drafts.json with items null when the drafts read is unreadable, and the README says items null is not an empty list. Read literally, the BUILD rule treats that as no row and makes the rejection permanent. The forwarder treats an unreadable drafts.json as no verdict: it writes no marker and sends nothing, counts the file under failed, and retries next run.",
  "notes": "The deferral is the forwarder's only departure from the BUILD rule list, and the CLI reports deferred files under failed. The issuer should confirm the reading. Edge arm measured in scratch only (.scratch/edge_ca_i3.py T1), not in the issuer's checks."
}
```

## COMM_ASSIST-W11-S2 -- the forwarder routes on object_id, which the refresh at this base does not write

```json
{
  "id": "COMM_ASSIST-W11-S2",
  "project": "COMM_ASSIST",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_COMM_ASSIST~11",
  "surfaced_at": "2026-10-13T22:37:00Z",
  "one_line": "THE CONTRACT says the refresh cell adds object_id to each drafts.json row this round. At this base refresh.py does not write object_id, so every answer would be rejected tag-not-waiting until the CA-i-1 refresh change lands in the reader folder.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~CA",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "data/transcripts/scripts/muse_reader/refresh.py@8bf64bac36:230-234 _draft_row keeps tag, kind, version, status, texted_at, send_at, draft and chat_title; no object_id",
      "data/transcripts/scripts/muse_reader/refresh.py@8bf64bac36 a path-scoped search of the muse_reader folder for object_id returns zero matches in refresh.py",
      "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r17/checks/check_i1_live.py@8bf64bac36:43-50 the CA-i-1 check requires every drafts item to carry a non-empty object_id, so that change is a separate cell"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO CA-i-3 THE CONTRACT: the refresh cell adds object_id to each drafts.json row this round, and BUILD step 1 routes each answer on that row's object_id.",
  "world_is": "At 8bf64bac36 the drafts rows carry no object_id, so the forwarder finds no waiting row for any tag. Under THE CONTRACT a rejected marker is permanent, so installing this forwarder before the CA-i-1 object_id change lands would reject every answer for good. The forwarder is not installed by this cell; the install cell CA-i-5 must sequence after CA-i-1.",
  "notes": "This cell does not edit refresh.py: its <paths> do not name it. The check suite for this cell passes on synthetic drafts rows that carry object_id."
}
```

## COMM_ASSIST-W11-S3 -- a permanent tag-not-waiting rejection can fire on a lagging drafts.json snapshot

```json
{
  "id": "COMM_ASSIST-W11-S3",
  "project": "COMM_ASSIST",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_COMM_ASSIST~11",
  "surfaced_at": "2026-10-13T22:37:00Z",
  "one_line": "A tag-not-waiting rejection is permanent by the BUILD rule, but drafts.json is a scheduled refresh snapshot. An answer for a draft that is waiting in the cloud and not yet in the snapshot would be rejected for good, and the forwarder cannot tell the two cases apart.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~CA",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "data/transcripts/scripts/muse_reader/refresh.py@8bf64bac36:155-184 refresh() writes drafts.json on each scheduled run, carrying read_at; the snapshot is whatever the last run read",
      "data/transcripts/scripts/muse_reader/forwarder.py@8bf64bac36 the tag-not-waiting branch writes answers/rejected/<sha>.json, and the once-only check at the top of the loop skips any sha with a marker in done/ or rejected/"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO CA-i-3 BUILD step 1: no drafts.json row with a non-empty object_id for the tag writes answers/rejected/<sha>.json; a rejected marker stops any later run from acting on the same bytes.",
  "world_is": "drafts.json is a snapshot written by the scheduled refresh, so it can lag the cloud table by one refresh interval. A draft that became waiting after the last refresh is absent from the snapshot, and the marker then makes that rejection permanent. The BUILD rule does not say the snapshot is current at the time of the answer.",
  "notes": "Not mitigated in this cell: a retry-on-newer-snapshot rule would change the BUILD rule list and needs an issuer ruling. The rejection marker's at field is the run time, not the snapshot's read_at, so a later reader cannot tell from the marker which snapshot judged the answer."
}
```

## COMM_ASSIST-W9-S1 -- the S3 listing's LastModified carries a millisecond fraction that the cell's two example forms do not name

```json
{
  "id": "COMM_ASSIST-W9-S1",
  "project": "COMM_ASSIST",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_COMM_ASSIST~9",
  "surfaced_at": "2026-10-13T22:40:09Z",
  "one_line": "The S3 listing's LastModified is 2026-10-13T20:13:51.000Z, a millisecond fraction the cell's two example forms do not name; the first parser read all three sprint objects as having no time.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "Measured 2026-10-13 ~22:3xZ from this laptop: aws s3api list-objects-v2 --bucket opal-data-portal-v2 --prefix daily-reports/2026-10-13/ --max-items 5 returned LastModified \"2026-10-13T20:13:51.000Z\" on each Contents entry (rc 0).",
      "data/transcripts/scripts/muse_reader/refresh.py@8bf64bac36 read_sprint_today passed c.get(\"LastModified\") through unchanged; the scratch run before the parser fix (.scratch/muse_i1/sprint_today.json, 3 items) carried age_minutes null and age_from null on all 3; after the fix the same run carries 144 and last_modified on all 3."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO CA-i-1 BUILD 1: with_age ages from the first key whose value parses as an ISO UTC time in the Z or +00:00 form; a value that does not parse is aged None, never guessed.",
  "world_is": "S3 emits the listing time with a .000 fraction before the Z. refresh.parse_utc now accepts an optional fraction of a second (microseconds kept) and still only the Z and +00:00 offsets; no other offset parses. The widening is my reading of 'ISO UTC time' and is recorded for the L9 read; no criterion changed.",
  "notes": "The other sources are unaffected: drafts texted_at and eod send_at are written by assist.iso() as %Y-%m-%dT%H:%M:%SZ (teams_chat/assist.py:96, no fraction), and open_calls opened_at by now_utc() in the same form (.tools/open-calls.py:170)."
}
```

## COMM_ASSIST-W9-S2 -- the eod_today draft row carries object_id too, because one row builder serves both draft readers

```json
{
  "id": "COMM_ASSIST-W9-S2",
  "project": "COMM_ASSIST",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_COMM_ASSIST~9",
  "surfaced_at": "2026-10-13T22:40:09Z",
  "one_line": "The cell names object_id on drafts rows; the shared draft-row builder also serves the eod_today reader, so the End of Day draft row carries object_id as well (its pk, eod:<day>).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "data/transcripts/scripts/muse_reader/refresh.py@8bf64bac36 read_eod_today reads the row by key eod:<day> and built its one row with _draft_row(state, pending); read_drafts builds its rows with the same helper.",
      "org/missions/D9/COMM/COMM_ASSIST/surprise-channel/investigations/INVESTIGATION_v1.md COMM_ASSIST-W8-S2 (world_is): a state row's pk is the object id (a chat id, eod:<day>, or inbox:owner)."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO CA-i-1 BUILD 3: drafts rows carry object_id, the id of the DynamoDB state row the draft was read from; every draft row has a non-empty string object_id.",
  "world_is": "eod_today's row also carries object_id = eod:<day>, the pk of the row it was read from, so one helper serves both readers and 'every draft row' holds for the End of Day draft. The cell named the drafts reader only; this is my judgment and it changes no criterion. The live run found eod:2026-10-13 with pending=no, so no eod draft row was present and the field is unmeasured on a live eod draft.",
  "notes": "An eod row without a pk raises, so the source reads unreadable rather than emitting an empty object_id, the same rule the drafts reader applies to a state row without one."
}
```

## COMM_ASSIST-W10-S1 -- the owner.text redraft sends its edit WITH a version, so the W8-S6 stale check reaches it

```json
{
  "id": "COMM_ASSIST-W10-S1",
  "project": "COMM_ASSIST",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_COMM_ASSIST~10",
  "surfaced_at": "2026-10-13T22:43:46Z",
  "one_line": "CA-i-2 says a text-path edit carries no version, but the owner.text redraft path sends its edit with a version, so the W8-S6 stale check now reaches those redrafts.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "data/transcripts/scripts/teams_chat/tenant.py@8bf64bac36:874-876 on_owner_text sends sms.reply with action edit and version = act.get('version') or item['version'] for every non-send, non-dev action",
      "data/transcripts/scripts/teams_chat/tenant.py@8bf64bac36:497 the send and drop stale check that the edit now shares, for an edit that carries a version",
      "data/transcripts/scripts/teams_chat/tenant.py@8bf64bac36:1110-1165 route_text (the #N text path) sends sms.reply with no version key, and is unchanged by this cell"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "CA-i-2 step 3: a text-path edit carries no version in its payload, so its behaviour must not change; the stale check covers an edit that carries a version.",
  "world_is": "The premise holds for the #N text path but not for owner.text. An owner.text redraft of a draft that has moved on is now refused as unseen (the changed-just-before text) where it used to redraft. The #N text path, which sends no version, is not checked and its behaviour is unchanged.",
  "notes": "Chosen in the worker commit: the edit check runs only when the payload carries a version (on_sms_reply), so every version-less edit is untouched. The owner-path change is a consequence of the order's wording, not a separate decision; the CVO grades whether it is wanted."
}
```

## COMM_ASSIST-W10-S2 -- the sms.reply path has no origin check of its own, so a queued sms.reply is acted on as Andrew's text

```json
{
  "id": "COMM_ASSIST-W10-S2",
  "project": "COMM_ASSIST",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_COMM_ASSIST~10",
  "surfaced_at": "2026-10-13T22:43:46Z",
  "one_line": "The sms.reply handler trusts any sms.reply event; the only sender check is the SNS originationNumber test in route_text, so an sms.reply put on the queue directly is acted on as Andrew's text.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~CA",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "data/transcripts/scripts/teams_chat/tenant.py@8bf64bac36:469-470 on_sms_reply reads the payload's tag, action and notes and acts on them, with no origin check",
      "data/transcripts/scripts/teams_chat/tenant.py@8bf64bac36:1110-1111 route_text compares originationNumber to a.secret(a.PHONE_SECRET); this is the only sender check, and it runs only on the SNS ingress",
      "data/transcripts/scripts/teams_chat/tenant.py@8bf64bac36:955 dispatch routes kind sms.reply to on_sms_reply for any event on the queue, so an event put there directly is not checked"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "CA-i-2 rules: a forged sms.reply that imitates the text path is a pre-existing weakness of the text path and is outside this cell; if confirmed from the code, file one row naming it.",
  "world_is": "Confirmed from the code, not exercised: an sms.reply event on the queue with action send posts the chat's draft to Teams, and one with action drop cancels it, with no text from Andrew behind it. The muse receiver does not change this, because the muse path is a separate kind and this one is still open.",
  "notes": "Left alone by this cell (outside its rules). Remedy belongs to a later cell; the disarm owner is the issuing COO, who routes the ruling to 1.0.0_SA_CTO. No AWS call was made to test it."
}
```

## COMM_ASSIST-W10-S3 -- the order names no reason for a verified answer that is not the contract, or for a pinned line that is not a key

```json
{
  "id": "COMM_ASSIST-W10-S3",
  "project": "COMM_ASSIST",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_COMM_ASSIST~10",
  "surfaced_at": "2026-10-13T22:43:46Z",
  "one_line": "CA-i-2 names reasons no-signature, no-key-configured and bad-signature only; a verified answer whose payload is not the contract, and a pinned key line that does not parse, have no named reason.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "data/transcripts/scripts/teams_chat/muse_verify.py (new in the worker commit on wk-COMM_ASSIST-10): _pinned_key returns None for a line that does not parse as ssh-ed25519, and verify() then reports no-key-configured",
      "data/transcripts/scripts/teams_chat/tenant.py (new in the worker commit on wk-COMM_ASSIST-10): _muse_fields returns None for a signed payload that is not the contract, and on_muse_reply refuses it with reason bad-payload"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "CA-i-2 step 2 names the refusal reasons no-signature, no-key-configured and bad-signature; step 1 says a malformed signature is bad-signature.",
  "world_is": "Two cases had no named reason. A signed payload that is not JSON, not an object, has no string tag, has an action outside send, drop and edit, or has a non-integer version is refused as bad-payload and recorded with its tag if one parses. A pinned line that is not an ssh-ed25519 key is treated as no key, so it fails closed as no-key-configured.",
  "notes": "Both choices are the worker's, made so that nothing is sent. Both are recorded in the refusal list. The CVO grades whether bad-payload should exist as a reason."
}
```

## COMM_ASSIST-W10-S4 -- a muse answer addressed to the owner object cannot answer a K### confirmation

```json
{
  "id": "COMM_ASSIST-W10-S4",
  "project": "COMM_ASSIST",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_COMM_ASSIST~10",
  "surfaced_at": "2026-10-13T22:43:46Z",
  "one_line": "A verified muse answer sent to the owner object runs on_sms_reply, which has no pending draft there, so muse cannot answer a K### confirmation.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "data/transcripts/scripts/teams_chat/tenant.py@8bf64bac36:955 dispatch sends only sms.reply on the owner object to on_owner_reply; a muse.reply on that object falls through to ROUTES",
      "data/transcripts/scripts/teams_chat/tenant.py@8bf64bac36:899-921 on_owner_reply is the only code that answers a K### confirmation (st['confirm'])"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "CA-i-2 step 2: a verified answer is run through the same code on_sms_reply runs for the same tag, action, notes and version.",
  "world_is": "The order names only on_sms_reply. For a muse answer addressed to the owner object, on_sms_reply finds no pending draft and answers nothing-open, so the K### confirmation is not answered. Nothing is sent by this path, and the action set is limited to send, drop and edit, so dev and close cannot be reached through muse.",
  "notes": "Left as the order says. A later cell that wants muse to answer K### confirmations needs on_owner_reply on the same verified fields; that is a decision for the issuer."
}
```

## COMM_ASSIST-W13-S1 -- the footer every mail text carries names #dev and 0 only, so the approve and redraft replies are not stated where he reads them

```json
{
  "id": "COMM_ASSIST-W13-S1",
  "project": "COMM_ASSIST",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_COMM_ASSIST~13",
  "surfaced_at": "2026-10-13T23:17:35Z",
  "one_line": "The mail text footer (_mail_text) says Reply #dev [notes] to open a job / 0 drop; it does not name 1 (approve) or notes (redraft), which CA-i-7 now answers.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "data/transcripts/scripts/teams_chat/mail_requests.py@90adf8a007:229 the footer line of _mail_text: Reply #dev [notes] to open a job / 0 drop",
      "data/transcripts/scripts/teams_chat/mail_requests.py (worker commit on wk-COMM_ASSIST-13): on_mail_reply now answers 1 with the final draft and notes with a redraft, and the footer is unchanged"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "CA-i-7 step 2: his notes redraft the mail draft and his 1 approves it, so he can finish the item by text.",
  "world_is": "Every mail text, first or redrafted, ends with a footer that names only #dev and 0. Nothing in the text he receives says that 1 approves or that notes redraft. The chat text names 1 and notes (its offer text); the mail text does not.",
  "notes": "Not changed here: the footer is the first-text format and the order names no footer change. The issuer decides the wording. The mail item's approve and redraft replies work regardless of the footer."
}
```

```json
{
  "id": "COMM_ASSIST-W14-S1",
  "project": "COMM_ASSIST",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_COMM_ASSIST~14",
  "surfaced_at": "2026-10-13T23:36:01Z",
  "one_line": "The CA-i-8 base-footer control cannot be run from a scratch copy of the data subtree: the footer check imports the mail harness and its import chain reaches the ldo runtime, lib, infra/logic/registry and org/standards.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r17/checks/check_i8_footer.py@35a3560b52: ROOT = Path.cwd(); sys.path gains ROOT/infra/aws/terraform/modules/ldo/runtime; the harness is loaded by ROOT-relative path",
      "scratch run in the worktree (untracked .scratch/mut, base mail_requests.py from 35a3560b52, HEAD 31fa72418c): data/ copied, then lib/, infra/logic/registry/ and org/standards/ copied, each step failing on the next missing module (lib.opal_naming, then systems.json, then NAMING_SCHEMA.json, then ldo) -- I8-FOOTER ok=False reason=ModuleNotFoundError: No module named 'ldo'; no footer text was read"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "The CA-i-8 order says the issuer's check prints ok=False at the base, and the proof schema requires a mutant control that fires on the base arm.",
  "world_is": "The check can only read a base footer when the whole repo import chain is present, so a scratch copy of the data subtree cannot run it; the base reading is the issuer's r17 measurement, not this worker's. The worktree run at HEAD 31fa72418c is unaffected (I8-FOOTER ok=True).",
  "notes": "Not fixed here: the check and the order are not this worker's to change. Measuring a base control needs a full-tree scratch or a base worktree. The proof's mutant entry carries this limit."
}
```

## COMM_ASSIST-W16-S1 -- the acted-result set in CA-i-10 step 4 is not the full set: three closure results also clear a draft

```json
{
  "id": "COMM_ASSIST-W16-S1",
  "project": "COMM_ASSIST",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_COMM_ASSIST~16",
  "surfaced_at": "2026-10-14T00:47:22Z",
  "one_line": "CA-i-10 step 4 lists seven result words that mean a draft moved and says to read on_sms_reply for the full set; the read finds three more that also clear the draft (expired, already-posted, test-not-posted), so the receiver records those three as acted too.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "data/transcripts/scripts/teams_chat/tenant.py@7ba1998bf5:100 return \"expired\" in expire_eod, which sets pending None and done True",
      "data/transcripts/scripts/teams_chat/tenant.py@7ba1998bf5:441 return \"test-not-posted\" and :450 return \"already-posted\" in post_eod_now, both after pending is cleared; post_eod_now is reached from on_sms_reply for a send on an End of Day draft",
      "wk-COMM_ASSIST-16 worktree, tenant.py MUSE_ACTED: the ten words, the last three marked as closing a draft"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "CA-i-10 step 4: an answer acted when its result is one of sent, dropped, redrafted, approved, posted, mail-approved, job-opened, read from on_sms_reply and mail_requests.on_mail_reply for the full set.",
  "world_is": "on_sms_reply also returns expired, already-posted and test-not-posted, each after clearing the pending draft. Recording those three as acted refuses a replay the seven-word list would let through. A replay of such an answer already finds nothing open, so no first answer is refused by the wider set.",
  "notes": "Only the record moves: a wider set refuses more replays and never a first answer. The COO rules whether the three stay in MUSE_ACTED."
}
```

## COMM_ASSIST-W16-S2 -- four existing muse tests signed no seq, so the seq binding would refuse them; their signed payloads now name the draft's seq

```json
{
  "id": "COMM_ASSIST-W16-S2",
  "project": "COMM_ASSIST",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_COMM_ASSIST~16",
  "surfaced_at": "2026-10-14T00:47:22Z",
  "one_line": "CA-i-10 step 5 names only the tests whose signed payload lacks version; with the seq binding live, four signed-answer tests against a seq-bearing chat draft (the verified send, the edit then drop, the answer for no open draft, the stale signed edit) would be refused seq-mismatch before the path they test; each signed payload now carries the draft's seq. The receiver logic does not depend on this.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "data/transcripts/scripts/tests/test_teams_chat_tenant.py@7ba1998bf5:395-401, :405-414, :418-423, :457-468: signed payloads with version and no seq, against a _drafted pending that carries seq (assign_seq at tenant.py@7ba1998bf5:119-122)",
      "wk-COMM_ASSIST-16 worktree after the change: the same four tests pass with seq=st[\"pending\"][\"seq\"] in each signed payload; tests run 59 passed"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "CA-i-10 step 5: existing tests must still pass; a test whose signed payload lacks version now expects bad-payload.",
  "world_is": "A signed answer with a version and no seq is refused seq-mismatch against any chat draft that carries a seq, so four existing tests that did not name the seq could not pass unchanged. Their payloads were changed to name the seq; no assertion's expected result was changed.",
  "notes": "The check CAi10-AC2 (check_i2_receiver.py) already signs the draft's seq, which is the same change made by the issuer."
}
```

## COMM_ASSIST-W16-S3 -- CA-i-10 step 5 names test_muse_verify.py for a version rule, but that file holds no receiver test

```json
{
  "id": "COMM_ASSIST-W16-S3",
  "project": "COMM_ASSIST",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_COMM_ASSIST~16",
  "surfaced_at": "2026-10-14T00:47:22Z",
  "one_line": "CA-i-10 step 5 asks for test_muse_verify.py to be updated where a signed payload lacks version; that file tests muse_verify.verify on raw bytes and never calls the receiver, so no test in it changes and the file was not edited.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "data/transcripts/scripts/tests/test_muse_verify.py@7ba1998bf5 (112 lines): zero references to tenant, on_muse_reply or on_sms_reply; 18 calls to mv.verify and mv._ed25519_verify",
      "data/transcripts/scripts/tests/test_teams_chat_tenant.py@7ba1998bf5: the receiver tests (on_muse_reply) live in this file only"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "CA-i-10 step 5: update test_teams_chat_tenant.py and test_muse_verify.py; any test whose signed payload lacks version now expects bad-payload.",
  "world_is": "test_muse_verify.py has no test whose signed payload reaches the receiver, so the version rule changes none of its tests. The receiver tests, including the new CA-i-10 tests, are all in test_teams_chat_tenant.py.",
  "notes": "Not edited. The version and seq rules are covered in test_teams_chat_tenant.py, which is the file that holds the receiver."
}
```

## COMM_ASSIST-D2-S1 -- CA-i-5 step 3 assumes the forwarder creates answers/; it does not

```json
{
  "id": "COMM_ASSIST-D2-S1",
  "project": "COMM_ASSIST",
  "fabric": "dell2",
  "surfaced_by": "0.7.0_AE_CloudOps~CA2",
  "surfaced_at": "2026-10-14T02:05:31Z",
  "one_line": "CA-i-5 step 3 says the by-hand forwarder run creates answers/, answers/done/ and answers/rejected/; forwarder.py returns at once when answers/ is absent, so it created none and answers/ had to be made by hand.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "data/transcripts/scripts/muse_reader/forwarder.py lines 115-121: `if not answers.is_dir(): return counts`, and only after that `done_dir.mkdir(exist_ok=True)` / `rej_dir.mkdir(exist_ok=True)`",
      "dell2 run before any folder existed: `MUSE-FORWARD sent=0 rejected=0 failed=0` and Test-Path false for answers, answers/done and answers/rejected",
      "after creating an empty answers/ and rerunning: done/ and rejected/ exist, 0 files"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "CA-i-5 step 3: the by-hand run must print MUSE-FORWARD sent=0 rejected=0 failed=0 and leave answers/, answers/done/ and answers/rejected/ in place.",
  "world_is": "The line printed but no folder was left: the forwarder only makes done/ and rejected/ under an answers/ that already exists. The empty answers/ was created by hand (a named dell2 write in the order), then the run created the other two. A reader folder built fresh by refresh.py has no answers/ either, so a rebuilt box would repeat this.",
  "notes": "Also: the AC3 test file e2e-20261014T020311Z.json stays in answers/ (the forwarder never moves a file's bytes); only its sha256 marker is in answers/done/. The order text says the file stays in done/. The id is COMM_ASSIST-D2-S1, not the COMM_ASSIST-CA2-S<k> the order names: the row grammar (investigation_item.schema.json id pattern) allows one capital letter and optional digits before S<n>, so CA2 would be refused, and the gate then requires the coordinate to be a registered device (D2 = dell2) matching the row's fabric. A2 (tried first) was refused for that reason."
}
```

## COMM_ASSIST-W18-S1 -- CA-i-13 step 4 names test_muse_verify.py for a signed_at update, but that file holds no receiver test

```json
{
  "id": "COMM_ASSIST-W18-S1",
  "project": "COMM_ASSIST",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_COMM_ASSIST~18",
  "surfaced_at": "2026-10-14T01:53:33Z",
  "one_line": "CA-i-13 step 4 asks for test_muse_verify.py to be updated for signed_at; that file tests muse_verify.verify on raw bytes and never calls the receiver, so none of its tests changes and it was not edited.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "data/transcripts/scripts/tests/test_muse_verify.py@c34826c3eb (112 lines): imports only teams_chat.muse_verify (line 14); no tenant or on_muse_reply reference",
      "data/transcripts/scripts/tests/test_teams_chat_tenant.py@c34826c3eb: the receiver tests (on_muse_reply) live in this file"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "CA-i-13 step 4: update test_teams_chat_tenant.py and test_muse_verify.py; every signed payload in a test carries a signed_at near the test context's clock.",
  "world_is": "test_muse_verify.py signs bare messages for mv.verify and holds no muse answer that reaches the receiver, so the signed_at rule changes none of its tests. The same premise was filed for CA-i-10 as COMM_ASSIST-W16-S3.",
  "notes": "Not edited. The receiver's time bound is covered in test_teams_chat_tenant.py."
}
```

## COMM_ASSIST-W18-S2 -- the receiver now requires signed_at, but no code in the repo emits a signed muse answer; the emitter's field rests on the design document

```json
{
  "id": "COMM_ASSIST-W18-S2",
  "project": "COMM_ASSIST",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_COMM_ASSIST~18",
  "surfaced_at": "2026-10-14T01:53:33Z",
  "one_line": "The receiver refuses any muse answer without a UTC signed_at, but the signing side is not in this worktree's .tools or data/transcripts/scripts folders, so the field the cell calls already present is attested only by the design document.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D9/COMM/COMM_ASSIST/deliverables/0.9.0_WK_COMM_ASSIST~8/MUSE_ANSWER_PATH_DESIGN.md@c34826c3eb line 33: 'Signed payload: one JSON object {tag, action, notes, version, signed_at}'",
      "named-folder Grep of .tools and data/transcripts/scripts at c34826c3eb: signed_at appears only in test_teams_chat_tenant.py and in .tools/prd_signoff_lib.py"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "CA-i-13 BUILD preface: the signed payload already carries signed_at (the time muse signed), so the receiver can require it as a bounded time.",
  "world_is": "The design document says the payload carries signed_at, and no emitter in the two folders writes it. An answer muse signed without the field is refused bad-payload and recorded; it is not sent.",
  "notes": "Not measured against a live muse answer in this cell. A live answer's signed_at is the observation to take before the deploy cell."
}
```

## COMM_ASSIST-W20-S1 -- forward() now creates a missing reader folder as well as answers/ (answers.mkdir with parents=True), where the old early

```json
{
  "id": "COMM_ASSIST-W20-S1",
  "project": "COMM_ASSIST",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_COMM_ASSIST~20",
  "surfaced_at": "2026-10-14T03:08:46Z",
  "one_line": "forward() now creates a missing reader folder as well as answers/ (answers.mkdir with parents=True), where the old early return created nothing; the CLI cannot reach this because main() refuses a missing --root before forward() runs.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "data/transcripts/scripts/muse_reader/forwarder.py@063dff2307 forward(): the old 'if not answers.is_dir(): return counts' guard, replaced by answers, done and rejected each mkdir(parents=True, exist_ok=True)",
      "data/transcripts/scripts/muse_reader/forwarder.py@063dff2307 main(): 'if not os.path.isdir(args.root)' refuses with rc 2 before forward() is called"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "CA-j-4 BUILD step 1: create answers/, answers/done/ and answers/rejected/ with parents=True, exist_ok=True, and nothing else.",
  "world_is": "parents=True on answers/ also creates a reader folder (the root) that is absent when forward() is called directly; the old early return created nothing in that case. The edit is kept exactly as the order states it.",
  "notes": "Not changed and not widened. Whether forward() should refuse a missing root rather than create it is the issuer's call. Checks J4-DIRS 3 of 3 and I3-FORWARD 6 of 6 pass with the edit."
}
```

## COMM_ASSIST-W19-S1 -- the task order places two sms.reply re-sends in on_owner_text; one is in on_owner_text and the other in on_owner_reply

```json
{
  "id": "COMM_ASSIST-W19-S1",
  "project": "COMM_ASSIST",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_COMM_ASSIST~19",
  "surfaced_at": "2026-10-14T03:23:18Z",
  "one_line": "The task order says on_owner_text holds two ctx.send of sms.reply; on_owner_text holds one, and the second sits in on_owner_reply. The count of four producer sites holds, and all four are stamped.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "data/transcripts/scripts/teams_chat/tenant.py@063dff2307 line 999: ctx.send(item['object_id'], 'sms.reply', ...) inside on_owner_text, the one re-send in that function",
      "data/transcripts/scripts/teams_chat/tenant.py@063dff2307 line 1043: ctx.send(act['object_id'], 'sms.reply', ...) inside on_owner_reply, the #1 confirmation re-send"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "CA-j-1 build step 2: in on_owner_text there are two ctx.send of sms.reply (the handler's own re-sends); read the whole file, there may be others. Four producer sites in total.",
  "world_is": "on_owner_text holds one ctx.send of sms.reply; the second is in on_owner_reply. The four sites at 063dff2307 are _route_commands owner.text (line 1263), _route_commands sms.reply (line 1287), on_owner_text (line 999) and on_owner_reply (line 1043). All four are stamped at 7af9d5d1f4.",
  "notes": "Both re-sends are stamped; the check's source arm reads four sites. No scope change; the premise wording only."
}
```

## COMM_ASSIST-W19-S2 -- test_teams_chat_natural.py compares the handler re-sends as exact payloads, is outside the grant, and now fails

```json
{
  "id": "COMM_ASSIST-W19-S2",
  "project": "COMM_ASSIST",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_COMM_ASSIST~19",
  "surfaced_at": "2026-10-14T03:23:18Z",
  "one_line": "test_teams_chat_natural.py compares the sms.reply payloads of on_owner_text and on_owner_reply as exact dicts; the mark now sits in those payloads, so the test fails, and the file is not in the task order's paths.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "data/transcripts/scripts/tests/test_teams_chat_natural.py@063dff2307 lines 49-50 and 58: sent_events == [('19:yang', 'sms.reply', {tag C608, action edit, notes, version 2})] and reply.sent_events == [('19:aj', 'sms.reply', {... version 1})]",
      "measured at 7af9d5d1f4 with PYTHONPATH on the tests dir: FAILED test_teams_chat_natural.py::test_a_send_is_echoed_for_a_1_and_a_redraft_goes_at_once; the 15-file set reads 174 passed, 1 failed"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "CA-j-1 build step 4 and the rules: existing tests must still pass; CAj1-AC2 is the assistant's flow tests, the text path included; the order's paths are the write grant.",
  "world_is": "The two handler re-sends now carry mark_at and mark, so their exact-payload assertions fail. The file that holds them is not in the order's paths, so this worker could not update it. CAj1-AC2's invocation (test_teams_chat_tenant.py only) prints I2-REGRESSION ok=True passed=64, so the bound does not reach the sibling file.",
  "notes": "Not edited: outside the grant. The stamp is required by CAj1-AC1 (the source arm reads every site), so the two assertions cannot pass unchanged. The issuer decides: add the file to the paths and compare unmarked(payload), or rule otherwise. Blocks the order's proof row CAj1-AC2 until ruled."
}
```

## COMM_ASSIST-W19-S3 -- INGRESS_MARK_MODE with a value other than off, record or enforce is not specified; the handler raises for a text-driven event

```json
{
  "id": "COMM_ASSIST-W19-S3",
  "project": "COMM_ASSIST",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_COMM_ASSIST~19",
  "surfaced_at": "2026-10-14T03:23:18Z",
  "one_line": "The task order gives three mode values and says unset or empty means off; it says nothing about any other value. The handler raises ValueError on a text-driven event for an unknown value, so the event is not acted on and the mode is not silently off.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "data/transcripts/scripts/teams_chat/tenant.py@7af9d5d1f4 _mark_mode(): raises ValueError when the stripped value is not in MARK_MODES; dispatch calls it only when ctx.kind is in ingress_mark.KINDS",
      "data/transcripts/scripts/tests/test_ingress_mark.py@7af9d5d1f4 test_an_unknown_mode_is_loud_on_a_text_event: the value enforced raises and acts on nothing"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "CA-j-1 THE CONTRACT: INGRESS_MARK_MODE values off (unset or empty means off: no check at all), record, enforce; read at call time.",
  "world_is": "A typo such as enforced neither turns enforcement off nor acts unverified: a text-driven event fails loud, and other event kinds are not touched. A failing text is a dropped text until the variable is corrected.",
  "notes": "The choice is the worker's. The issuer may rule a different value (for example, treat an unknown value as enforce). Not deployed; this order sets no mode anywhere."
}
```

## COMM_ASSIST-W19-S4 -- the flow-test harness reaches the ingress secret through a private cache, because a patch of a.secret inside the harness is overwritten by the issuer check's own patch

```json
{
  "id": "COMM_ASSIST-W19-S4",
  "project": "COMM_ASSIST",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_COMM_ASSIST~19",
  "surfaced_at": "2026-10-14T03:23:18Z",
  "one_line": "The order does not say how the flow tests keep stamped sends off AWS. Patching a.secret inside the harness's Fakes overrode the issuer check's own a.secret patch (J1-MARK read 5 of 9); the harness now seeds the module secret cache instead.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "data/transcripts/scripts/tests/test_teams_chat_tenant.py@7af9d5d1f4 Fakes.__init__: monkeypatch.setitem(a._SECRETS, the ingress_mark secret name, MARK_KEY)",
      "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r18/checks/check_j1_mark.py@063dff2307 arm(): patches a.secret, then calls fresh(mp), which constructs Fakes(mp)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "CA-j-1 step 4 and the rules: no AWS call, no network. The issuer check patches a.secret for each arm and then builds the harness.",
  "world_is": "With a.secret patched in Fakes, the stamp and the verify used different keys and J1-MARK read 5 of 9. With the cache seeded instead, the check reads 9 of 9. The harness now depends on the private name assist._SECRETS.",
  "notes": "Test-only seed. If assist renames _SECRETS, monkeypatch.setitem fails loudly rather than reading AWS. Surfaced for the issuer; not a production change."
}
```

## COMM_ASSIST-W19-S5 -- test_teams_chat_natural.py does not collect when run alone from the root; the directory run collects it

```json
{
  "id": "COMM_ASSIST-W19-S5",
  "project": "COMM_ASSIST",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_COMM_ASSIST~19",
  "surfaced_at": "2026-10-14T03:38:07Z",
  "one_line": "test_teams_chat_natural.py does not collect when run alone from the root: it imports its sibling test module by bare name, and pytest.ini does not put the tests directory on the path. The directory run collects it.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "data/transcripts/scripts/tests/test_teams_chat_natural.py@53be82a3cd line 6: from test_teams_chat_tenant import CHAT, NOW, Ctx, Fakes, a, msg, t",
      "pytest.ini@53be82a3cd: pythonpath = data/black_diamond/scripts and . (the tests directory is not on the path)",
      "measured at 53be82a3cd: python -m pytest data/transcripts/scripts/tests/test_teams_chat_natural.py -q gives ModuleNotFoundError: No module named 'test_teams_chat_tenant', rc 2; with PYTHONPATH=data/transcripts/scripts/tests it gives 8 passed, rc 0",
      "measured on the working tree after the edit: python -m pytest data/transcripts/scripts/tests -q from the root gives 544 passed, rc 0, the natural file collected"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "CA-j-1 AC2 and its order text: run the whole flow-test set under data/transcripts/scripts/tests from the worktree root; if test modules do not import from the root, run it the way check_i2_regression.py runs them and say which.",
  "world_is": "The natural file's bare import resolves only when the tests directory is on sys.path. Run alone from the root it fails at collection. Run as part of the directory it is collected and passes (8 of 8), by a path this worker did not identify.",
  "notes": "Pre-existing: the import line is unchanged from its only commit fa2e17f953. Not fixed here: the file is outside this order's work except for the two exact-payload asserts. The set run was used for the wider count; the single-file run used PYTHONPATH on the tests directory and is named as such in the proof."
}
```

## COMM_ASSIST-W19-S6 -- CAj1-AC2's invocation runs the tenant file only, so its ok=True does not show the sibling flow file

```json
{
  "id": "COMM_ASSIST-W19-S6",
  "project": "COMM_ASSIST",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_COMM_ASSIST~19",
  "surfaced_at": "2026-10-14T03:38:07Z",
  "one_line": "CAj1-AC2's invocation, check_i2_regression.py, runs test_teams_chat_tenant.py only, so its printed ok=True does not show the sibling flow file the criterion names.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r17/checks/check_i2_regression.py@53be82a3cd: TARGET = data/transcripts/scripts/tests/test_teams_chat_tenant.py, one pytest run on that file",
      "measured on the working tree: check_i2_regression.py prints I2-REGRESSION ok=True passed=64 failed=0 reason=none (rc 0); the directory run over data/transcripts/scripts/tests prints 544 passed (rc 0)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "CAj1-AC2: the bound, a control that PASSES at the base and must still pass with the updated and added tests: the assistant's flow tests, the text path included. Invocation: check_i2_regression.py, expect I2-REGRESSION ok=True.",
  "world_is": "The invocation's own scope is one file. The printed ok=True is true of that file (64 of 64) and says nothing about test_teams_chat_natural.py, which the criterion's scope includes (row S2 measured it failing at 7af9d5d1f4).",
  "notes": "The criterion was run as written and recorded. The wider scope was measured by the directory run (544 of 544, the natural file 8 of 8) and recorded beside it. The invocation is the issuer's and was not edited."
}
```

## COMM_ASSIST-W21-S1 -- the commit gate's client-data check printed WARN on this box (no hashed account-id list), so commit 6cfb79f314 was not checked for client account ids

```json
{
  "id": "COMM_ASSIST-W21-S1",
  "project": "COMM_ASSIST",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_COMM_ASSIST~21",
  "surfaced_at": "2026-10-14T03:56:52Z",
  "one_line": "The commit gate's client-data check printed WARN because the hashed account-id list is absent on this box, so commit 6cfb79f314 was not checked for client account ids.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "UNMEASURED: no file this worker read names the owner of the box's account-id list at C:\\Users\\AndrewBerman\\.opal\\account_id_hashes.txt",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "safe-commit.sh run for 6cfb79f314 (branch wk-COMM_ASSIST-21, this worktree) printed: WARN: client-data-check: hashed account-id list ABSENT at C:\\Users\\AndrewBerman\\.opal\\account_id_hashes.txt -- this commit was NOT checked for client account ids",
      "the same run printed [commit-gate] OK for 1 of 3 files and the naming, to-pipeline and surprise-row gates; only the client-data check reported the absent list"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "safe-commit.sh's client-data-check checks each commit's content for client account ids against the hashed list at OPAL_ACCOUNT_ID_HASHES or the default path, and a commit it cannot check is reported as checked-or-not.",
  "world_is": "On this box the list is absent at the default path and OPAL_ACCOUNT_ID_HASHES is not set in this worker's shell, so the check printed WARN and recorded the commit as not checked. Every commit from this box is unchecked until the list is in place.",
  "notes": "Observed, not fixed: placing the list and naming its owner are outside this order's <paths>. The commit touches chat_assist.tf, the order file and this worker's deliverables. The base chat_assist.tf already carries the account number 313476888478 inside its ARNs; this worker did not compare it with the list, which it does not hold. The gate's own WARN states the not-checked outcome."
}
```

## COMM_ASSIST-W23-S1 -- BUILD step 2 names two shapes of legacy state entry; _held_marks met a third (a dict whose "at" cannot be read) and dated it now

```json
{
  "id": "COMM_ASSIST-W23-S1",
  "project": "COMM_ASSIST",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_COMM_ASSIST~23",
  "surfaced_at": "2026-10-14T10:58:27Z",
  "one_line": "The order specifies a bare mark string as the legacy entry and a {mark, at} dict as the new one, and says nothing about a dict whose at is unreadable; the code re-dates such an entry to now.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "data/transcripts/scripts/teams_chat/tenant.py@b4c5218661: _held_marks, the except (AttributeError, KeyError, TypeError, ValueError) branch sets entry to {mark, at: iso(now)} and treats it as held",
      "org/missions/D9/COMM/COMM_ASSIST/task-orders/COMM_ASSIST.TO-CA-j-9.ingress-mark-four-hour-freshness.md@349d687606 BUILD step 2: 'Tolerate a legacy entry (a bare mark string, as CA-j-1 wrote)... No crash on either shape.'"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "CA-j-9 BUILD step 2: state[\"marks_seen\"] entries are {mark, at}; a legacy bare mark string is treated as held, dated now; no crash on either shape.",
  "world_is": "The code accepts the two named shapes, and a third that the order does not name: a dict with no readable at. That entry is kept as held and rewritten with at = now, so it ages out four hours after the check that found it. No test covers the third shape. The order's text does not say what an unreadable at should do.",
  "notes": "Chosen by the worker so that the handler never raises on state it did not write. Not ruled by the CTO or the issuer. The state is written only by _mark_refused, so the third shape is reachable only by a foreign writer; this was not measured. Left for the issuer to rule."
}
```

## COMM_ASSIST-W23-S2 -- BUILD step 3 names five new tests; the worker added a sixth for the legacy bare-string tolerance that step 2 requires

```json
{
  "id": "COMM_ASSIST-W23-S2",
  "project": "COMM_ASSIST",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_COMM_ASSIST~23",
  "surfaced_at": "2026-10-14T10:58:27Z",
  "one_line": "BUILD step 3 lists five new tests and no test for the legacy bare-string tolerance; the worker added a sixth test to cover that tolerance.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "data/transcripts/scripts/tests/test_ingress_mark.py@b4c5218661: test_a_legacy_bare_mark_string_is_held_dated_now_and_ages_out_four_hours_later, added after the five named tests",
      "org/missions/D9/COMM/COMM_ASSIST/task-orders/COMM_ASSIST.TO-CA-j-9.ingress-mark-four-hour-freshness.md@349d687606 BUILD step 3 names five new tests; step 2 names the legacy tolerance"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "CA-j-9 BUILD step 3: add the five named new tests; step 2: tolerate a legacy bare mark string, no crash on either shape.",
  "world_is": "Six new tests were added: the five named ones and one that drives a legacy bare-string entry through a replay (held, dated now, rewritten as {mark, at}) and past the four-hour window. The three existing tests were updated as step 3 names. The full flow set is 550 passed, 0 failed.",
  "notes": "The sixth test is in the order's test file, so it stays inside <paths>. It is recorded so the count of new tests is not read as five."
}
```

```json
{
  "id": "COMM_ASSIST-W26-S1",
  "project": "COMM_ASSIST",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_COMM_ASSIST~26",
  "surfaced_at": "2026-10-14T14:10:43Z",
  "one_line": "The safe-commit.sh call for the one-line Terraform edit ran past the 120-second tool bound and was moved to a background task; its exit code (0) and its commit (da4014f5b2) were read afterwards from git log.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/terraform/transcripts/chat_assist.tf@da4014f5b2: the one-line default edit landed (git log -n1 shows da4014f5b2 for this path)",
      "background task b3x97w0wx: the commit-gate printed OK for 1 of 1 file(s); the wrapper reported completed with exit code 0"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "The order says to commit the edit first with bash .tools/safe-commit.sh and to read the commit's short hash afterwards; it states no duration for the commit call.",
  "world_is": "For a one-file, one-line commit the safe-commit call took longer than the 120-second bound of this worker's Bash tool; the call was moved to a background task and completed with rc 0 and the commit landed.",
  "notes": "Recorded as observed, with no verdict on its cause. The commit-gate output in the background file showed the pre-commit reflex and naming gate running on the one file, and the client account-id list WARN named in the order was not printed."
}
```

## COMM_ASSIST-W25-S1 -- the H1 control pins SOURCES to the four original names; the cell's contract makes it six, so the two checks cannot both pass

```json
{
  "id": "COMM_ASSIST-W25-S1",
  "project": "COMM_ASSIST",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_COMM_ASSIST~25",
  "surfaced_at": "2026-10-14T14:00:00Z",
  "one_line": "CAj13-AC3 (check_h1_failure_shape.py) requires sorted(SOURCES) to equal the four original names; the cell's contract makes SOURCES six names, so AC3 reads ok=False after the cell is built, while AC1 (check_k2_reader.py) requires both new names in SOURCES.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r16/checks/check_h1_failure_shape.py@4b23bc3cce: lines 23-25 -- names = list(getattr(m, 'SOURCES', ())); if sorted(names) != ['drafts', 'eod_today', 'open_calls', 'sprint_today']: out(False, 'SOURCES=%r')",
      "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r18/checks/check_k2_reader.py@4b23bc3cce: line 122 -- if 'mentions' not in R.SOURCES or 'mail_log' not in R.SOURCES ... return False",
      "org/missions/D9/COMM/COMM_ASSIST/task-orders/COMM_ASSIST.TO-CA-j-13.reader-publishes-mentions-and-mail-log.md@4b23bc3cce: THE CONTRACT sets SOURCES to six names; CAj13-AC3 says the H1 check passes at base and must still pass",
      "data/transcripts/scripts/muse_reader/refresh.py@81fb6249fb: SOURCES = ('open_calls', 'drafts', 'eod_today', 'sprint_today', 'mentions', 'mail_log'); measured: check_h1_failure_shape.py prints H1-FAILURE-SHAPE ok=False reason=SOURCES=[six names] at this commit"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "CAj13 CONTRACT: SOURCES becomes ('open_calls', 'drafts', 'eod_today', 'sprint_today', 'mentions', 'mail_log'). CAj13-AC3: check_h1_failure_shape.py ok=True arms as named, passes at base and must still pass.",
  "world_is": "Both premises were built as written and they conflict. check_h1_failure_shape.py prints H1-FAILURE-SHAPE ok=False reason=SOURCES=['open_calls', 'drafts', 'eod_today', 'sprint_today', 'mentions', 'mail_log'] at commit 81fb6249fb. check_k2_reader.py prints K2-READER ok=True arms=7 of 7 at the same commit. No repair and no widening were made, as the order's RULES require; CAj13-AC3 is recorded FAIL and the order stays pending.",
  "notes": "The issuer chooses between the two checks (or amends H1 as a control). The order is not flipped to complete while AC3 fails. Filed under the order's surprise rule; no hazard is armed (no deploy)."
}
```

## COMM_ASSIST-W25-S2 -- the order does not say what an expiry time that is null or unparsable does; the reader keeps such an entry

```json
{
  "id": "COMM_ASSIST-W25-S2",
  "project": "COMM_ASSIST",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_COMM_ASSIST~25",
  "surfaced_at": "2026-10-14T14:00:00Z",
  "one_line": "THE CONTRACT drops an entry whose seen_at (mentions) or considered_at (mail_log) is older than 7 days and says nothing about a null or unparsable value; the reader keeps such an entry, with a null age, rather than dropping it.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "data/transcripts/scripts/muse_reader/refresh.py@81fb6249fb: read_mentions and read_mail_log -- 'if seen is not None and seen < cutoff: continue' and 'if considered is not None and considered < cutoff: continue'",
      "data/transcripts/scripts/muse_reader/refresh.py@81fb6249fb: newest_first -- an item with no parsable time sorts last",
      "org/missions/D9/COMM/COMM_ASSIST/task-orders/COMM_ASSIST.TO-CA-j-13.reader-publishes-mentions-and-mail-log.md@4b23bc3cce: THE CONTRACT, the 7-day drop sentence (no null rule)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "CAj13 CONTRACT: entries whose seen_at is older than 7 days before now_dt are dropped; mail entries likewise by considered_at. No rule for a missing or unparsable time.",
  "world_is": "A null or unparsable expiry time is kept with age_minutes null, following with_age's existing rule that an item with no parsable time is kept. No test covers this branch. Not measured on the live table.",
  "notes": "Kept rather than dropped so that an entry is never hidden on a guess. Left for the issuer to confirm or change; a change is one comparison in each reader."
}
```

## COMM_ASSIST-W25-S3 -- two strings still describe the four-source reader: the CLI --root help and the scan label

```json
{
  "id": "COMM_ASSIST-W25-S3",
  "project": "COMM_ASSIST",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_COMM_ASSIST~25",
  "surfaced_at": "2026-10-14T14:00:00Z",
  "one_line": "The CLI --root help text still says 'the four files', and scan_table prints 'READ drafts' on every scan, including the new mentions and mail_log scans.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "data/transcripts/scripts/muse_reader/refresh.py@81fb6249fb: main() add_argument('--root', help='the folder to write (the four files, INDEX.json, README.txt)')",
      "data/transcripts/scripts/muse_reader/refresh.py@81fb6249fb: scan_table -- print('READ drafts table=%s rows_scanned=%d pages=%d' ...)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "CAj13: nothing else changes (the CLI, the exit codes, INDEX.json's shape now lists six).",
  "world_is": "Both strings are unchanged per the order's CLI rule, so the help text is stale (it says four files) and the scan label names drafts for every scan. Cosmetic; no behaviour depends on either.",
  "notes": "Not changed here: the order fixes the CLI. The issuer may amend the help text in a later cell."
}
```

## COMM_ASSIST-W24-S1 -- test_inbound_mail_draft.py arm client_no_request fails at the base, on a stale end-of-text assertion

```json
{
  "id": "COMM_ASSIST-W24-S1",
  "project": "COMM_ASSIST",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_COMM_ASSIST~24",
  "surfaced_at": "2026-10-14T14:11:54Z",
  "one_line": "Arm client_no_request of data/transcripts/scripts/tests/test_inbound_mail_draft.py fails at the base 4b23bc3cce, before any edit by this order: its assertion expects the text to end with 'Reply #dev [notes] to open a job / 0 drop', and the handler texts 'Reply 1 to approve ... / notes to redraft / 0 drop / #dev [notes] to open a job'.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "data/transcripts/scripts/tests/test_inbound_mail_draft.py@4b23bc3cce: line 127, body.rstrip().endswith(...) assertion in client_no_request",
      "data/transcripts/scripts/teams_chat/mail_requests.py@4b23bc3cce: _mail_text, the final reply line (lines 233-234)",
      "measured at 4b23bc3cce: body.rstrip().endswith('Reply #dev [notes] to open a job / 0 drop') is False; the draft line and the CLIENT line are True"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "The order says to add mail-log arms to this file and keep every test file under data/transcripts/scripts/tests that touches mail passing; this file is in the order's <paths>.",
  "world_is": "Before this order's edits the file already printed MAIL-DRAFT ok=False arms=6/7, with client_no_request the failing arm, so the file is not green at the base. The text is not changed by this order (the order forbids changing what is texted), and the stale assertion was left unedited rather than rewritten to fit the text. After the order's edits: arms=11/12, the same arm failing, the five new mail-log arms pass. base_texts_client_no_request=-1 because that arm aborts before it sets the base count.",
  "notes": "Which side is stale (the assertion or the text) is for the owner to rule. The order's keep-passing rule is not met for this file at the base; this row records it rather than editing an existing assertion."
}
```

## COMM_ASSIST-W24-S2 -- test_inbound_mail.py is 11 of 15 at the base, outside this order's paths

```json
{
  "id": "COMM_ASSIST-W24-S2",
  "project": "COMM_ASSIST",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_COMM_ASSIST~24",
  "surfaced_at": "2026-10-14T14:11:54Z",
  "one_line": "data/transcripts/scripts/tests/test_inbound_mail.py prints INBOUND-MAIL-TEST ok=False cases=11/15 at the base 4b23bc3cce (4 cases fail: three named by the run, one above the captured tail), before any edit by this order.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "measured at 4b23bc3cce by python data/transcripts/scripts/tests/test_inbound_mail.py: INBOUND-MAIL-TEST ok=False cases=11/15 model_calls_on_failed=0; FAIL a_party_not_marked_considered_is_not_admitted; FAIL a_domain_whose_claim_is_not_measured_is_not_admitted; FAIL a_missing_mail_parties_file_leaves_the_firms_working",
      "measured after this order's edits: the same 11/15, so the count is unchanged by this order"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "The order says every test file under data/transcripts/scripts/tests that touches mail or mentions keeps passing, and a test outside the order's paths passes unmodified.",
  "world_is": "This file is outside <paths> and was not edited. It already fails four of fifteen cases at the base, so the keep-passing rule cannot hold for it at the base. The count is the same before and after this order.",
  "notes": "Not edited by this worker. The three failing cases named are the ones the run printed in its tail; the fourth is not named here."
}
```

## COMM_ASSIST-W24-S3 -- the pytest set run does not collect the plain-script mail and mention files

```json
{
  "id": "COMM_ASSIST-W24-S3",
  "project": "COMM_ASSIST",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_COMM_ASSIST~24",
  "surfaced_at": "2026-10-14T14:11:54Z",
  "one_line": "python -m pytest data/transcripts/scripts/tests -q reports 562 passed and 0 failed, while the plain-script files test_inbound_mail.py and test_inbound_mail_draft.py fail when run as python files; pytest does not collect them, so the pytest total does not cover their failures.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "measured after the code commit 5041e19001: python -m pytest data/transcripts/scripts/tests -q -p no:cacheprovider, output 562 passed in 233.47s, rc 0",
      "data/transcripts/scripts/tests/test_inbound_mail_draft.py and test_inbound_mail.py each define main() and carry no def test_ function: the header probe of this worker's run printed pytest=0 for both files (worktree at 5041e19001)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "The order asks for the whole set under pytest and for every mail or mention test file to pass.",
  "world_is": "The pytest total and the script results measure different sets. A green pytest total does not show that the two script files are green.",
  "notes": "Recorded so the 562 figure is not read as covering the plain-script files. The order's pytest figure is reported as measured."
}
```

```json
{
  "id": "COMM_ASSIST-W27-S1",
  "project": "COMM_ASSIST",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_COMM_ASSIST~27",
  "surfaced_at": "2026-10-14T23:08:34Z",
  "one_line": "test_inbound_mail_draft.py already fails its client_no_request arm at the base (11/12) before any CA-k-1 edit: the arm asserts a footer text that mail_requests.py no longer writes.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python data/transcripts/scripts/tests/test_inbound_mail_draft.py at ad67a9b9a4 (parent of the CA-k-1 commit 41cd03765f): MAIL-DRAFT ok=False arms=11/12 base_texts_client_no_request=-1",
      "traceback of client_no_request at ad67a9b9a4: data/transcripts/scripts/tests/test_inbound_mail_draft.py line 127 assert body.rstrip().endswith('Reply #dev [notes] to open a job / 0 drop') raises AssertionError",
      "data/transcripts/scripts/teams_chat/mail_requests.py at ad67a9b9a4 line 235 writes the footer 'Reply 1 to approve ... / notes to redraft / 0 drop / #dev [notes] to open a job'"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-CA-k-1 says test_inbound_mail_draft.py must be kept passing, and that only test_inbound_mail.py fails at the base (4 of its 15 cases).",
  "world_is": "test_inbound_mail_draft.py already fails one arm at the base: client_no_request asserts a footer text that mail_requests.py no longer writes. The file reads 11/12 before any CA-k-1 edit.",
  "notes": "Not repaired here: the arm sits outside the CA-k-1 cell and the order forbids widening the edit. After commit 41cd03765f the file reads 16/17, the new CA-k-1 arms pass and client_no_request is the only failure. Measured, not judged."
}
```

## COMM_ASSIST-W28-S1 -- the naming gate refuses the hand-typed transcripts path; --tf is made required

```json
{
  "id": "COMM_ASSIST-W28-S1",
  "project": "COMM_ASSIST",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_COMM_ASSIST~28",
  "surfaced_at": "2026-10-15T01:03:31Z",
  "one_line": "The LGIC naming gate refused the script's hand-typed default --tf path (the literal transcripts); no registry row carries a Terraform file path, so --tf is now required and the default is removed.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "git commit attempt on branch wk-COMM_ASSIST-28 at cd1e04765b (safe-commit.sh, naming limb in ENFORCE): NAMING REFUSE .tools/ldo001-mode-default-check.py:33 transcripts -> lookup('transcripts'); commit aborted, rc 1",
      "infra/logic/registry/root_map.json:1749-1753 (key transcripts) carries system, scope, source and fills only; infra/logic/registry/scopes.json:354-359 (scope transcripts) carries a bucket and no file path; lib/opal_naming.py:366 lookup() returns the scope row only",
      "commit 935a400f14: --tf required; python .tools/ldo001-mode-default-check.py with no --tf prints NO-VERDICT and exits 2; check_l2_gate.py still L2-GATE ok=True arms=13 of 13 (every caller passes --tf)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "The order's contract is `.tools/ldo001-mode-default-check.py [--tf PATH] [--live-json PATH]`: the flag is optional, and the order names no default path. A builder refusal of a name is answered by a missing registry row to add (CLAUDE.md rule 30).",
  "world_is": "No registry row gives the Terraform file path of the module, so the naming gate's read-through-lookup rule has no row to read. The default path was removed and --tf became required; an absent --tf is the existing NO-VERDICT rc 2 arm. The criteria are unchanged: the issuer check, safe-apply.sh's covered block and the order's live read all pass --tf explicitly.",
  "notes": "Not decided by this worker. The COO or the CVO decides whether a registry row for the root's path should be added, or the optional flag restored with a sanctioned route."
}
```

## COMM_ASSIST-W28-S2 -- the commit's Co-Authored-By line names Haiku 5.5, not the Sonnet 5.5 the order gives

```json
{
  "id": "COMM_ASSIST-W28-S2",
  "project": "COMM_ASSIST",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_COMM_ASSIST~28",
  "surfaced_at": "2026-10-15T01:03:31Z",
  "one_line": "The order's step 3 asks for a Co-Authored-By line naming Claude Sonnet 5.5; the worker runs as Claude Haiku 5.5, and commit 935a400f14 carries the Haiku line.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "order COMM_ASSIST.TO-CA-k-2 step 3 (the worker face's closing instruction) names Co-Authored-By: Claude Sonnet 5.5",
      "git log -1 --format=%B 935a400f14 line 20: Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>; the session's attribution rule and the model id claude-haiku-5-5 name Haiku 5.5"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "The order says the commit message ends with Co-Authored-By: Claude Sonnet 5.5.",
  "world_is": "The worker's model is Haiku 5.5, and the harness attribution rule for commits names Haiku 5.5, so the Haiku line was written. The order's Sonnet line was not used.",
  "notes": "Recorded as a departure from the order's text. The COO decides whether the attribution line for this worker should read Haiku 5.5 or be corrected in a later commit."
}
```

## COMM_ASSIST-W28-S3 -- a refused safe-commit left the safe-apply hunk staged in the index

```json
{
  "id": "COMM_ASSIST-W28-S3",
  "project": "COMM_ASSIST",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_COMM_ASSIST~28",
  "surfaced_at": "2026-10-15T01:03:31Z",
  "one_line": "After the naming refusal, safe-commit.sh printed 'files unstaged', but git status still showed .tools/safe-apply.sh staged; the next commit took the explicit paths and was unaffected.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "safe-commit.sh output on the refused attempt at cd1e04765b: 'ERROR: BLOCKED -- the naming limb refused ... Commit aborted; files unstaged.'",
      "git status --short in the worktree straight after that refusal: 'M  .tools/safe-apply.sh' (staged) and '?? .tools/ldo001-mode-default-check.py' (untracked)",
      "the next safe-commit (935a400f14) reported '2 files changed, 223 insertions(+)' with the two named paths; the worktree index is private to wk-COMM_ASSIST-28"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "The refusal message says 'Commit aborted; files unstaged.'",
  "world_is": "The index kept the staged safe-apply.sh hunk after the refusal. No commit went through with it, and the worktree's index is not shared with another seat.",
  "notes": "Recorded as a claim-versus-world mismatch of the refusal message. Not repaired here: git reset and restore are outside this order."
}
```

## COMM_ASSIST-W29-S1 -- the scan log line needed the source name, so scan_table took a source argument (the order said two text lines)

```json
{
  "id": "COMM_ASSIST-W29-S1",
  "project": "COMM_ASSIST",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_COMM_ASSIST~29",
  "surfaced_at": "2026-10-15T01:25:16Z",
  "one_line": "The order's cell (c) said the reader repair was two text lines; naming the source in the scan log needed scan_table to receive the source, a signature change plus two call-site edits in refresh.py. Behaviour is unchanged.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "commit 8454482177 on wk-COMM_ASSIST-29: data/transcripts/scripts/muse_reader/refresh.py, def scan_table(source: str) at the nested reader scope; print line now READ %s table=%s rows_scanned=%d pages=%d; callers scan_table('drafts') in read_drafts and scan_table(list_key) in read_state_lists",
      "check_l3_batch.py arm refresh_same passes at 8454482177 (folder byte-identical to the merge-base text on a fixed stub); arm scan_log_truth passes; the drafts line text is unchanged"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-CA-k-3 cell (c): 'Make the help name the sources from refresh.SOURCES and make the scan log line name the source actually read'; the same cell and the order's RULES say NO product code changes, only the test files and the two reader text lines.",
  "world_is": "The scan log line is printed inside scan_table(), which received no source; naming the source read required passing it in. That is one parameter and two call-site edits in refresh.py, not a text-only change. The output bytes of the folder are unchanged.",
  "notes": "Done as the cell asks, with the minimum signature change. Form only: the order's 'two text lines' undercounts the edit. No behaviour changed; the refresh_same arm is the bound."
}
```

## COMM_ASSIST-W29-S2 -- the commit gate's client-data check did not run: the hashed account-id list is absent on this box

```json
{
  "id": "COMM_ASSIST-W29-S2",
  "project": "COMM_ASSIST",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_COMM_ASSIST~29",
  "surfaced_at": "2026-10-15T01:25:16Z",
  "one_line": "Every safe-commit on this worktree prints WARN client-data-check: the hashed account-id list is ABSENT, so the commit is not checked for client account ids; the check cannot run here.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "0.0.0_AB_MSTR",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "safe-commit output for commit 8454482177: 'WARN: client-data-check: hashed account-id list ABSENT at C:\\Users\\AndrewBerman\\.opal\\account_id_hashes.txt -- this commit was NOT checked for client account ids (absent is not empty; set OPAL_ACCOUNT_ID_HASHES or place the list there).'",
      "measured at filing: test -f on C:/Users/AndrewBerman/.opal/account_id_hashes.txt rc=1 (absent); OPAL_ACCOUNT_ID_HASHES unset in the worker shell"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-CA-k-3 says: 'Commit with .tools/safe-commit.sh as your serial'; the commit gate is the mechanism the order relies on for the commit step.",
  "world_is": "The gate ran and passed its other checks, but its client-data leg reported the list absent and therefore did not check this commit for client account ids. Absent is not empty.",
  "notes": "This commit adds only three test files and one reader file, with no account ids in the diff as far as the worker read it. The row records that the check was not run, not that a leak occurred. The disarm owner is named as the infrastructure seat (MSTR runs infrastructure) and was not contacted."
}
```

## COMM_ASSIST-W31-S1 -- the round-19 check's no_product_change allowlist does not admit the three sibling test repairs, so CAl3-AC3 prints ok=False arms=7 of 8

```json
{
  "id": "COMM_ASSIST-W31-S1",
  "project": "COMM_ASSIST",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_COMM_ASSIST~31",
  "surfaced_at": "2026-10-15T07:40:26Z",
  "one_line": "The round-19 check's no_product_change arm allows four files, so the three sibling test repairs this order requires make CAl3-AC3 print ok=False arms=7 of 8 (expected ok=True arms=8 of 8).",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r19/checks/check_l3_batch.py@f28047c1f5: ALLOWED (line 25) names four paths (test_inbound_mail.py, test_inbound_mail_draft.py, test_teams_chat_natural.py, refresh.py); arm_no_product_change (lines 197-203) fails any tracked data/infra/.tools path changed against the merge-base outside ALLOWED.",
      "measured at HEAD f28047c1f5 from the worktree root: python \"org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~CA/r19/checks/check_l3_batch.py\" printed 'L3-BATCH ok=False arms=7 of 8' and 'FAIL no_product_change: files changed outside the four allowed: data/transcripts/scripts/tests/test_teams_chat_eod_republish.py, data/transcripts/scripts/tests/test_teams_chat_jobs.py, data/transcripts/scripts/tests/test_teams_chat_stale_eod.py'; the process exit code printed rc=0 beside it."
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-CA-l-3 CAl3-AC3: python check_l3_batch.py expect 'L3-BATCH ok=True arms=8 of 8', described as a control that passes at the base; and the cell text, which requires the three sibling files to be edited with no other change.",
  "world_is": "Both cannot hold as written: the three files are the order's only edits, and the round-19 check's no_product_change arm grades them as stray changes. The other seven arms pass at HEAD f28047c1f5 (alone 14/12/14, combined 112 passed in pytest, AC1 6 of 6, AC2 64 passed).",
  "notes": "Form only. The order forbids editing the check file and any path outside its <paths>, so the arm was not widened or repaired by this worker. The order stays open; the COO decides whether the criterion is re-cut against the three files. Hazard is INERT so no disarm owner is named."
}
```

## COMM_ASSIST-D2-S2 -- the commit gate's client-data check did not run on dell2 either: the hashed account-id list is absent at this box's path

```json
{
  "id": "COMM_ASSIST-D2-S2",
  "project": "COMM_ASSIST",
  "fabric": "dell2",
  "surfaced_by": "0.7.0_AE_CloudOps~CA2",
  "surfaced_at": "2026-10-15T07:45:00Z",
  "one_line": "safe-commit on dell2 prints WARN client-data-check: the hashed account-id list is ABSENT at C:\\Users\\Test\\.opal\\account_id_hashes.txt, so commit 5bab1a0866 was not checked for client account ids.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "0.0.0_AB_MSTR",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "safe-commit output for commit 5bab1a0866 on box/dell2: 'WARN: client-data-check: hashed account-id list ABSENT at C:\\Users\\Test\\.opal\\account_id_hashes.txt -- this commit was NOT checked for client account ids (absent is not empty; set OPAL_ACCOUNT_ID_HASHES or place the list there).'"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-CA-l-1 says: 'Commit with .tools/safe-commit.sh under your own serial'; the commit gate is the mechanism the order relies on for the commit step.",
  "world_is": "The gate ran and passed its other checks, but its client-data leg reported the list absent on dell2 and did not check the commit. Same hazard as COMM_ASSIST-W29-S2, a different box and path. Absent is not empty.",
  "notes": "The commit adds ten small evidence files (command outputs, status words, file names and row counts); the seat read no item text and none is recorded. The row records that the check was not run, not that a leak occurred. Nothing was installed or placed to cure it: the order forbids edits beyond its paths."
}
```

## COMM_ASSIST-W32-S1 -- the order's "raise active to it" reads two ways, and the literal one keeps every read thread tracked forever

```json
{
  "id": "COMM_ASSIST-W32-S1",
  "project": "COMM_ASSIST",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_COMM_ASSIST~32",
  "surfaced_at": "2026-10-16T20:53:08Z",
  "one_line": "TO-CA-n-1 item 3 says the thread cursor is set to the newest created seen, or a.iso(now) on an empty page, and then 'raise active to it when newer'; read literally, active would become the read time on every empty page, so the drop rule never fires and the thread budget starves.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "INFERRED",
    "evidence": [
      "org/missions/D9/COMM/COMM_ASSIST/task-orders/COMM_ASSIST.TO-CA-n-1.read-replies-of-recent-threads.md@1ca38ef17f item 3 (WHAT TO BUILD) and item 4 (drop rule)",
      "data/transcripts/scripts/teams_chat/channel_mentions.py@c08d686f69 _read_threads: 't[\"cursor\"] = max(t[\"cursor\"] or \"\", newest or a.iso(now))' then 'if newest > t[\"active\"]' (raise only to the newest created seen)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-CA-n-1 item 3: 'Then set the thread's cursor to the newest created seen (or a.iso(now) when the page is empty) and raise active to it when newer'; item 4: drop a tracked root that is not pinned and whose active is older than THREAD_DAYS.",
  "world_is": "Read with 'it' = the parenthetical cursor value, every thread read on an empty page gets active = the read time, so it is never older than THREAD_DAYS and is never dropped, and the ordering by active (newest first) keeps the most recently read threads first, so unread tracked threads starve at THREAD_MAX. The build takes 'it' = the newest created seen (an empty page raises nothing). Not run against live traffic; read from the code.",
  "notes": "The build follows the second reading. The order should say which value active carries. No hazard is live: commit c08d686f69 is not deployed by this order."
}
```

## COMM_ASSIST-W32-S2 -- a thread whose replies call keeps failing holds its whole channel's cursor, so no top-level mention in that channel is read either

```json
{
  "id": "COMM_ASSIST-W32-S2",
  "project": "COMM_ASSIST",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_COMM_ASSIST~32",
  "surfaced_at": "2026-10-16T20:53:08Z",
  "one_line": "A GatewayError from one thread's replies read counts as a channel failure, so the channel keeps its old cursor and is read again first next poll; a replies route that keeps failing for one root blocks every mention in that channel, measured in a scratch run: 3 polls, cursor None, the new mention never sent.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D9/COMM/COMM_ASSIST/task-orders/COMM_ASSIST.TO-CA-n-1.read-replies-of-recent-threads.md@1ca38ef17f item 4: 'A GatewayError from _read_threads counts in failed and errors exactly like a channel read failure, and the other channels still run.'",
      "data/transcripts/scripts/teams_chat/channel_mentions.py@c08d686f69 poll: the GatewayError branch restores threads[ck] and continues; the channel cursor is not advanced",
      "scratch run .scratch/ground_freeze.py in the worktree (one root whose replies always raises; one new top-level mention): first poll and polls at 300s, 600s, 900s each failed=1 route=replies status=500; cursors t1|c1 None; mention p2 sent=0; replies attempts p1,p2,p1,p2,p1,p2,p1"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-CA-n-1 item 4: a GatewayError from _read_threads counts like a channel read failure, and the other channels still run.",
  "world_is": "The other channels run, but the failing channel itself is blocked for as long as the replies route fails for any one of its tracked roots (the cursor never moves, so its top-level mentions are never read). The worker also restores that channel's thread state on failure, which the order does not say; without the restore the cursor freeze is the same.",
  "notes": "Form only. The order was built as written. The freeze needs a persistent per-thread replies failure (a deleted root, a permission change); the owner decides whether a failing thread should be skipped for the poll instead. Not deployed: the hazard is inert until a deploy of c08d686f69, which this order does not perform."
}
```

## COMM_ASSIST-W32-S3 -- a reply can be sent twice across polls when the thread read is cut by the call budget after the channel read sent it

```json
{
  "id": "COMM_ASSIST-W32-S3",
  "project": "COMM_ASSIST",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_COMM_ASSIST~32",
  "surfaced_at": "2026-10-16T20:53:08Z",
  "one_line": "The emitted set is per poll, so a reply that _read_channel sent in one poll can be sent again by _read_threads in a later poll when the thread's cursor did not move; the repeat carries the same event id, so it depends on event-id de-duplication downstream.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "INFERRED",
    "evidence": [
      "org/missions/D9/COMM/COMM_ASSIST/task-orders/COMM_ASSIST.TO-CA-n-1.read-replies-of-recent-threads.md@1ca38ef17f item 3: 'its id is added to emitted' (the set is built in poll from the channel's events of that poll)",
      "data/transcripts/scripts/teams_chat/channel_mentions.py@c08d686f69 poll: emitted = {ev[2][\"message\"].get(\"id\") for ev in events} then _read_threads; the channel cursor advances in the same poll"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-CA-n-1 item 3: each reply 'becomes ONE event', and its id is added to emitted.",
  "world_is": "Across polls the only guard is the event id ('mention-<reply id>'), not the emitted set: when the channel read advances the channel cursor past a reply and the same poll's thread read is cut by MAX_CALLS before that root, the next poll sends the reply again under the same event id. Not run; read from the code.",
  "notes": "The poll's own comment states that event ids de-duplicate, which is the only guard this path has. Not deployed; hazard inert."
}
```

## COMM_ASSIST-W32-S4 -- BLOCKING for CAn1-AC3: this worktree's sparse checkout omits daily_reports/, so the assistant flow tests cannot import post_format

```json
{
  "id": "COMM_ASSIST-W32-S4",
  "project": "COMM_ASSIST",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_COMM_ASSIST~32",
  "surfaced_at": "2026-10-16T21:00:47Z",
  "one_line": "CAn1-AC3 (check_i2_regression.py) prints I2-REGRESSION ok=False passed=0 failed=1 in this worktree: assist.py _post_format() raises ModuleNotFoundError for post_format, because the worktree's sparse checkout does not materialise daily_reports/eod/.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "C:/Users/AndrewBerman/Desktop/ajb_wk/commassist-32 at c08d686f69: timeout 280 python -m pytest data/transcripts/scripts/tests/test_teams_chat_tenant.py -q -x -p no:cacheprovider -> 'ModuleNotFoundError: No module named post_format' at data/transcripts/scripts/teams_chat/assist.py:861 (_post_format), 1 failed in 0.65s",
      "git config core.sparseCheckout = true; git sparse-checkout list = .tools, data/transcripts/scripts, infra/aws/terraform/modules/ldo, infra/logic/registry, lib; daily_reports/eod/ is absent on disk (ls: cannot access) though git ls-tree HEAD lists daily_reports/eod/post_format.py",
      "diagnostic only, no write: PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=<main workspace>/daily_reports/eod python -B -m pytest data/transcripts/scripts/tests/test_teams_chat_tenant.py -q -p no:cacheprovider -> 64 passed in 66.33s (rc 0) at c08d686f69"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-CA-n-1 CAn1-AC3: the I2 regression is a control that PASSES at the base (64 passed); the order names the worktree paths it may write, and a path it needs that the worktree lacks is a BLOCKING row on that criterion.",
  "world_is": "The control cannot pass in this worktree as written: the worktree is a sparse checkout that does not carry daily_reports/eod/, a runtime import of assist.py that is outside the order's grant. The worker did not rebuild or copy the directory in. With the module put on the path (diagnostic only), the same 64 tests pass at c08d686f69, so the two-file diff does not break them. The base-commit run in this sparse tree was not measured; the failure is at the module import, not in any line the order changes.",
  "notes": "Blocks CAn1-AC3 only; CAn1-AC1 (7 of 7) and CAn1-AC2 (7/7, 4/4) pass at c08d686f69. The order stays open. The owner decides whether the worktree is re-cut with daily_reports/eod in its sparse set, or the criterion is re-cut. Nothing was widened or repaired by this worker."
}
```

## COMM_ASSIST-S4 -- a targeted plan of module.ldo_001 from a clean detached checkout fails until transcripts-pull.zip is built, and the order's steps do not build it

```json
{
  "id": "COMM_ASSIST-S4",
  "project": "COMM_ASSIST",
  "fabric": "laptop",
  "surfaced_by": "0.7.0_AE_CloudOps~COMM1",
  "surfaced_at": "2026-10-16T22:33:10Z",
  "one_line": "terraform plan -target=module.ldo_001 in infra/aws/terraform/transcripts from a clean detached worktree at 1aa63bde67 exits rc=1 with three filebase64sha256 errors (commentary.tf:283, mail_pull.tf:106, pull.tf:113) because lambda/transcripts-pull/dist/transcripts-pull.zip is gitignored and absent; step 4 of TO-CA-n-2 builds only teams-chat-assist.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~CA",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "r21/CAn2_PLAN_BRANCH_A.txt first run at 2026-10-16T22:10:05Z: plan rc=1, 3 errors, all 'local.pull_zip is ./../../lambda/transcripts-pull/dist/transcripts-pull.zip ... cannot find the path specified'",
      "after bash infra/aws/lambda/transcripts-pull/build.sh in the pinned worktree (built 100 files, dist gitignored, git status --porcelain 0 lines), the same plan read rc=2, 0 add 2 change 0 destroy at 22:11:27Z"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-CA-n-2 steps 1, 4 and 5: a clean detached worktree at the pin, build.sh of teams-chat-assist only, then a saved targeted plan of module.ldo_001.",
  "world_is": "The root evaluates filebase64sha256 for three untargeted Lambdas at config load, so a targeted plan needs their dist zip too. The applier built it in the pinned worktree with that directory's build.sh; its hash touches no targeted resource (the saved plan's 2 changes name only module.ldo_001's handler and ingress[0]). The act was not blocked or widened.",
  "notes": "Later COMM deploy orders that plan this root from a clean checkout should name the transcripts-pull build in their steps. No hazard is live."
}
```
