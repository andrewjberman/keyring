# ADVI_FIRMBKTS task order -- `FB-f-20` -- c290: THE ACCOUNT'S SNS DEFAULT SMS TYPE APPLIED (ONE ATTRIBUTE, `1 to change`)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R4.md</decomp_doc>
<owned_cells>FB-f-20</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~FBL</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one account-level SNS preference changes in place; no cron, rule, schedule or cadence is added or changed.
comp-iam: RUN by the actor at step 1 (the laptop identity applied the SMS delivery-status role and preferences in `FB-f-12`; the same `sns:SetSMSAttributes` is this act's one call). No grant is created.
comp-adversary: RUN by the issuer -- before the act the live preferences carry no DefaultSMSType (the CTO's reading; the actor's pre-read confirms or contradicts it). The repository carries the attribute at `FB-g-35` (merged @f55374d418, `r4_smstype.py` 4 of 4). Blindness: nothing proves SNS will pick the number for the subscriber until a real SEV1 publish: that close waits on Andrew's word (the CTO is asking).
EGRESS CLASS, declared: NONE (no text is sent by this act).
</preflight>

## 1. THE ACT -- `FB-f-20` (round 4, c290; the CTO's ruling `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_SEV1_SMS_DELIVERY_STATUS_LOGGING_20261011.md` AMENDMENT 6, msg 4021)

Andrew: the one test text ARRIVED, so the registered toll-free number works. The CTO: `aws_sns_sms_preferences.account` leaves
`DefaultSMSType` unset (promotional) while the account's only number is registered TRANSACTIONAL, which is the fault
('No origination identity available to send to destination number'). One attribute is added in Terraform
(`infra/aws/terraform/inf-pipeline/inf-ops-alerts-sms-delivery-status.tf`: `default_sms_type = "Transactional"`); this act applies it.

### 1a. The steps, in order

0. **Gate.** The laptop checkout reads the attribute at the file (`git log` shows `FB-g-35`'s commit @b0455c7972 or its merge
   @f55374d418, on `CLOUD`); the CTO's ruling is at HEAD. Any not so: STOP.
1. **Pre-read, print each (never a phone number: print the LAST FOUR digits at most):**
   `aws sns get-sms-attributes --region us-east-1` (the `DefaultSMSType` value or its absence, `MonthlySpendLimit`,
   `DeliveryStatusIAMRole` presence, `DeliveryStatusSuccessSamplingRate`); the registered number's region, status and
   `MessageType` (`aws pinpoint-sms-voice-v2 describe-phone-numbers`); the SMS topics' region (us-east-1). **A reading that
   CONTRADICTS the CTO's (the number is not Transactional-capable, is in another region, or `DefaultSMSType` is already
   Transactional) is a STOP: file a BLOCKING row with the readings and do not apply.**
2. **The entry.** Open the change-management entry BEFORE the write: scope the `inf-pipeline` root, ONE resource
   (`aws_sns_sms_preferences.account`), the pre-read values, rollback = the attribute unset again (re-apply the file at the
   prior commit, or `aws sns set-sms-attributes` with `DefaultSMSType` removed as recorded).
3. **Plan, scoped.** `.tools/safe-apply.sh` plan limb with `-target=aws_sns_sms_preferences.account`: exactly ONE resource to
   change in place, and the diff names `default_sms_type` alone (`"" -> "Transactional"` or `null -> "Transactional"`).
   `Plan: 0 to add, 1 to change, 0 to destroy`. Anything else: STOP, a BLOCKING row.
4. **Apply** through `.tools/safe-apply.sh` (never a bare `terraform apply`) on that saved plan.
5. **Read after.** `get-sms-attributes`: `DefaultSMSType` reads `Transactional`; every other preference equals its pre-read
   (the spend limit `50`, the delivery-status role, sampling `0`). A post-apply scoped plan reads `No changes`.
6. **Close the entry** with the outputs. DO NOT send a text. The act's real close (one SEV1 publish moving
   `NumberOfNotificationsDelivered`) waits on Andrew's word, which the CTO has asked for.

## 2. BOUNDS

1. One resource, one attribute, one account. No topic, subscription, alarm, number or role change; no text sent; no spend limit
   change.
2. No apply if the plan names a second resource or a second attribute.
3. If `sns:SetSMSAttributes` is refused, STOP and file a BLOCKING row; do not widen anything.

## 3. SURFACES

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FBL/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FBL/ADVI_FIRMBKTS.TO-FB-f-20.sms-default-type-apply.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-f-20"><invocation>timeout 60 aws sns get-sms-attributes --region us-east-1 --query "attributes.DefaultSMSType" --output text</invocation><expect>^Transactional$</expect></criterion>
  <criterion id="AC2" cell_refs="FB-f-20"><invocation>timeout 60 aws sns get-sms-attributes --region us-east-1 --query "attributes.[MonthlySpendLimit,DeliveryStatusSuccessSamplingRate]" --output text</invocation><expect>^50\s+0$</expect></criterion>
  <criterion id="AC3" cell_refs="FB-f-20"><invocation>cd infra/aws/terraform/inf-pipeline &amp;&amp; timeout 118 terraform plan -input=false -lock=false -refresh=true -no-color -target=aws_sns_sms_preferences.account 2&gt;&amp;1 | grep -E "^(Plan:|No changes)"</invocation><expect>^No changes\.</expect></criterion>
</proof_of_spec>

AC1 reads the one attribute, AC2 that the other two preferences did not move, AC3 that the scoped plan is empty after the
apply. Each invocation terminates inside its bound.

## 5. WHEN YOU ARE DONE

Close the change-management entry in the SAME commit as the proof instance; flip `<status>` to `complete` only when AC1 to AC3
pass. Report once to `2.0.0_SA_COO~B1` through the laptop manager: the pre-read lines (masked), the plan's one-resource summary,
the entry id, AC1 to AC3 outputs and the commit hash. State that no text was sent.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** cut on the CTO's AMENDMENT 6 (msg 4021) after `FB-g-32`'s census read 54 publishers, 38 of them AWS services
that cannot set a per-publish attribute. The close (one real SEV1 publish delivered) is Andrew's word, asked by the CTO.
Workstream `SMSAPPLY`.

<status>pending</status>
<round>4</round>
<workstream>SMSAPPLY</workstream>
<to_id>ADVI_FIRMBKTS.TO-FB-f-20</to_id>
<slot>~FBL</slot>
<fabric>laptop</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
