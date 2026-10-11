# ADVI_FIRMBKTS task order -- `FB-g-32` -- THE CENSUS OF EVERY PUBLISHER THAT REACHES THE SEV1 SMS SUBSCRIPTION (THE CTO'S AMENDMENT 5, c290)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R4.md</decomp_doc>
<owned_cells>FB-g-32</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_FIRMBKTS~52</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a read-only census; nothing is changed or applied.
comp-iam: DECLARED-NOT-APPLICABLE -- reads only (`sns list-*`, `cloudwatch describe-alarms`, `events list-*`, repository files). No grant, no publish. If a read is denied to your identity, say which and continue with the others: a denied read is a finding, not a failure.
comp-adversary: RUN by the issuer -- at base the census file does not exist and `r4_smscensus.py` reads 0 of 4 (S1 to S4 FAIL by construction). Blindness: the census proves the file's shape and that cited code lines exist; it cannot prove a publisher is complete (the AWS reads are the denominator, the code search its complement).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `FB-g-32` (round 4, workstream `SMSFIX`; the CTO's ruling AMENDMENT 5, msg 4005)

Andrew's word: the one test text ARRIVED, so the registered toll-free number works and the fault is SNS's origination choice
('No origination identity available to send to destination number'). The CTO ruled the fix's form: every publisher that reaches
the SEV1 SMS subscription sets the message attribute `AWS.MM.SMS.OriginationNumber` from ONE Terraform-managed value (SNS has
no account-level default origination number). The first step is the census, with N printed.

### 1a. What to produce (the whole spec)

One JSON file `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~52/SEV1_SMS_PUBLISHER_CENSUS.json`: an object with:
- `topics`: a list, one entry per SNS topic that has at least one subscription whose protocol is `sms` (read with
  `aws sns list-subscriptions` and `list-subscriptions-by-topic`, region `us-east-1`; print COUNTS only, never an endpoint):
  `topic_arn`, `sms_subscriptions` (an integer), `publishers` (a list), `alarm_actions` (a list of alarm names whose
  `AlarmActions` or `OKActions` include the topic), `eventbridge_targets` (a list of rule names that target the topic);
- each `publishers` entry: `kind` `"code"` with `where` `"path:line"` of a repository line that publishes to the topic (an
  `sns.publish(TopicArn=...)` whose topic resolves, by an environment variable or a Terraform value you read, to this topic),
  or `kind` `"aws_service"` with `where` the resource id (an alarm, a rule, a Budgets action, a Lambda destination);
  `can_set_message_attributes`: `true` for code, `false` for an AWS service resource;
- `n_publishers`: the number of publisher entries across all topics (N); `n_unable`: how many cannot set a message attribute;
- `terraform_value_candidates`: a list of `"path:line"` of existing Terraform that already carries the toll-free number's
  identifier (its ARN, its id or the E.164 number in a variable's description, never the number itself), or the empty list if
  none does.

### 1b. Rules

1. Read only. Do not publish, subscribe, unsubscribe, change an attribute, put an alarm or edit any file in the repository.
2. NEVER write a phone number (or an endpoint, an email, an account id of a person) into any file or row: a count and a topic
   ARN are the most you print. The check refuses a run of ten or more digits.
3. If `aws sns` is denied to your identity, record it as a surprise row naming the denied call and fill what the code search
   alone can give, marking `topics[].sms_subscriptions` with `-1` where unreadable.

## 2. BOUNDS

1. The only file you write is `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~52/SEV1_SMS_PUBLISHER_CENSUS.json`, plus your surprise rows and proof instance under your own deliverables folder.
2. ASCII only. If something cannot be met, file a surprise row and stop.

## 3. SURFACES

<paths>
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~52/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository, the checks under `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/`.

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~52/ADVI_FIRMBKTS.TO-FB-g-32.sev1-sms-publisher-census.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-g-32"><invocation>cd /c/dev/wk-firmbkts-52 &amp;&amp; timeout 118 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_smscensus.py --arms census --file org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~52/SEV1_SMS_PUBLISHER_CENSUS.json --root /c/dev/wk-firmbkts-52; echo "exit=$?"</invocation><expect>ROUND 4 SMS CENSUS: 4 of 4 arms</expect></criterion>
</proof_of_spec>

AC1 reads the file against the tree: a non-empty topics list with every key, every publisher typed and located, N printed and
equal to the entries, and no phone number anywhere. The invocation terminates inside its bound.

## 5. WHEN YOU ARE DONE

Instance at `D/ADVI_FIRMBKTS.TO-FB-g-32.sev1-sms-publisher-census.proof_of_spec.json`, `D` = `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~52`.
Commit the census, your rows, then the instance second. **Do not flip this order's `<status>`** (the issuer drains it). Row ids:
`ADVI_FIRMBKTS-D1-W52-S<k>`, `k` from 1, `surfaced_at` from `date -u +%FT%TZ`. Report once: AC1's output, N and the unable
count, the topics' ARNs with their counts, any denied read, and the commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** cut on Andrew's word (c290 ARRIVED) and the CTO's AMENDMENT 5 (msg 4005). The next cells: the one
Terraform-managed value (a variable or an SSM parameter), the publisher edits (`N - n_unable` code sites), and the carrier for
the `n_unable` AWS-service publishers (CloudWatch alarm actions cannot set a message attribute: a different carrier is the CTO's
call). `0.7.0_AE_CloudOps~FBL` reads the pool and protect configuration, the EUM spend limit and the number's state with the
laptop identity before any apply. Workstream `SMSFIX`. Class LOCAL (read-only).

<status>complete</status>
<round>4</round>
<workstream>SMSFIX</workstream>
<to_id>ADVI_FIRMBKTS.TO-FB-g-32</to_id>
<slot>~52</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
