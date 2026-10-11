# ADVI_FIRMBKTS task order -- `FB-g-35` -- THE ACCOUNT'S SNS SMS PREFERENCES GAIN `default_sms_type = "Transactional"` (c290, THE CTO'S AMENDMENT 6)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R4.md</decomp_doc>
<owned_cells>FB-g-35</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_FIRMBKTS~55</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one repository file; no cron, rule, schedule or cadence is added or changed and nothing is applied.
comp-iam: DECLARED-NOT-APPLICABLE -- repository file only: no AWS act. The apply is a separate staged order for the laptop lane under the CTO's ruling (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_SEV1_SMS_DELIVERY_STATUS_LOGGING_20261011.md`, AMENDMENT 6).
comp-adversary: RUN by the issuer -- at base `r4_smstype.py` reads 3 of 4 (T2, T3 and T4 PASS as controls; T1 FAILS as expected: no such attribute). Blindness: the check reads the file as text; whether SNS honors the attribute for the registered number is the act's pre-read and its one real SEV1 publish.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `FB-g-35` (round 4, workstream `SMSTYPE`; c290; the CTO's AMENDMENT 6, msg 4021)

Andrew's word: the one test text ARRIVED, so the registered toll-free number works. The CTO's reading of the cause: our
`aws_sns_sms_preferences` leaves `DefaultSMSType` unset, so SNS sends as promotional, while the account's only origination
number is registered for TRANSACTIONAL: 'No origination identity available to send to destination number'. The fix is ONE
attribute on the existing preferences, which covers all 54 publishers (16 in code, 38 alarms and rules).

### 1a. Behavior (the whole spec)

In `infra/aws/terraform/inf-pipeline/inf-ops-alerts-sms-delivery-status.tf`, resource `aws_sns_sms_preferences` `account`: add ONE attribute line `default_sms_type = "Transactional"` after
`delivery_status_success_sampling_rate` and before `depends_on`, with the file's own alignment; and add one comment line above
the resource's attributes saying why (c290, the toll-free number is Transactional, AMENDMENT 6). Nothing else changes: the
spend limit, the role, the sampling rate, `depends_on` and every other resource of the file stay character for character.
`terraform fmt` must read clean on the file.

## 2. BOUNDS

1. One file changes: `infra/aws/terraform/inf-pipeline/inf-ops-alerts-sms-delivery-status.tf`. No other file, no apply, no plan in the `inf-pipeline` root, no AWS call.
2. ASCII only; keep the file's own line endings. If the commit is refused by a gate, do not override or force: file a BLOCKING
   row with the gate's lines.

## 3. SURFACES

<paths>
infra/aws/terraform/inf-pipeline/inf-ops-alerts-sms-delivery-status.tf
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~55/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the rest of the repository, the checks under `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/`.

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~55/ADVI_FIRMBKTS.TO-FB-g-35.sms-default-type.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-g-35"><invocation>cd /c/dev/wk-firmbkts-55 &amp;&amp; timeout 118 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_smstype.py --arms pref --root /c/dev/wk-firmbkts-55 --base 83995c26e6; echo "exit=$?"</invocation><expect>ROUND 4 SMS TYPE: 4 of 4 arms</expect></criterion>
  <criterion id="AC2" cell_refs="FB-g-35"><invocation>cd /c/dev/wk-firmbkts-55 &amp;&amp; timeout 60 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_scope.py --root /c/dev/wk-firmbkts-55 --allow infra/aws/terraform/inf-pipeline/inf-ops-alerts-sms-delivery-status.tf --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~55/ --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md --require infra/aws/terraform/inf-pipeline/inf-ops-alerts-sms-delivery-status.tf; echo "exit=$?"</invocation><expect>ROUND 4 SCOPE: OK</expect></criterion>
</proof_of_spec>

AC1 reads the one attribute, that the others are the base's, that every base line is kept and that the formatter is clean. AC2
is the write-surface bound. Each invocation terminates inside its bound.

## 5. WHEN YOU ARE DONE

Instance at `D/ADVI_FIRMBKTS.TO-FB-g-35.sms-default-type.proof_of_spec.json`, `D` = `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~55`. Commit the
file and your rows, then the instance second. **Do not flip this order's `<status>`**. Row ids: `ADVI_FIRMBKTS-D1-W55-S<k>`,
`k` from 1, `surfaced_at` from `date -u +%FT%TZ`. Report once: AC1 and AC2 outputs and the commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** the CTO withdrew form (a) (a re-publisher is refused by the moratorium; message attributes cannot be set by
alarm actions) and ruled one attribute on the existing preferences (msg 4021). Before the apply `0.7.0_AE_CloudOps~FBL` prints
`get-sms-attributes`, the number's region against the topics' region and its MessageType: a reading that contradicts the
CTO's is a STOP and a re-rule. Plan: 1 to change, that attribute. Close: one real SEV1 publish delivered, which waits on Andrew's
word (the CTO is asking). Workstream `SMSTYPE`. Class WORLD by the path floor.

<status>complete</status>
<round>4</round>
<workstream>SMSTYPE</workstream>
<to_id>ADVI_FIRMBKTS.TO-FB-g-35</to_id>
<slot>~55</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
