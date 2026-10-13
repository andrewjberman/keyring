# ADVI_FIRMBKTS task order -- `FB-h-6` -- THE EXEC-SUMMARY TRIGGER: WHY THE CHAIN-COMPLETE EVENT HAS NOT RUN THE GENERATOR SINCE MAY (READ-ONLY DIAGNOSIS)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R5.md</decomp_doc>
<owned_cells>FB-h-6</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_FIRMBKTS~65</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a read-only diagnosis; no rule, schedule or cadence is added or changed.
comp-iam: DECLARED-NOT-APPLICABLE -- reads only (`cloudtrail lookup-events`, `events describe-*`/`list-*`, `iam get-*`/`list-*`, `lambda get-policy`). No grant, no put, no invoke. A read denied to your identity is a finding.
comp-adversary: RUN by the issuer -- at base the record does not exist (AC1 FAIL); the grader rejects a record whose `calls` holds a write verb (a planted `put-events` entry reads FAIL), a verdict outside the closed set, and a measured error text with no source. Blindness: the grader proves the record's shape and read-only discipline, not that the findings are true; the issuer and the CVO re-read the cited calls.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `FB-h-6` (round 5, enrichment item 4; rows `D1-S40`, ROUND_ANALYSIS.round3.md ADDENDUM 12)

The exec-summary generator (`exec-summary-generator`, Lambda) runs only when an EventBridge rule `exec-summary-trigger`
matches an event the dispatcher emits at every chain close. It has not run since 2026-05-03 and its client summaries have
not refreshed since 2026-05-04. The dispatcher (`data/black_diamond/scripts/gold/gold_dispatch.sh`, `emit_chain_complete` at
lines 835-855 and its gate at lines 1450-1458) prints `WARN: EventBridge chain-complete put-events failed` at every chain close
since 2026-04-25. **You find out WHY, by reading, and write down what you read.** You fix nothing and you emit nothing.

### 1a. What to read (every call a READ verb: get, describe, list, lookup, filter; region us-east-1; `.tools/aws` from bash)

1. **The put-events error text.** The script discards the CLI's stderr into its success test, so no run log holds it.
   Find the real outcome from CloudTrail: `aws cloudtrail lookup-events --lookup-attributes AttributeKey=EventName,AttributeValue=PutEvents`
   over the longest window the service holds (90 days), paginated; keep client-side the events whose `userIdentity` is the
   dispatcher's role (named in 3 below) or whose `eventSource` is `events.amazonaws.com` with a `bd-pipeline.gold-chain`
   source in the request. Record per day: calls, calls with an `errorCode`, the distinct `errorCode` and `errorMessage` texts
   (verbatim), and whether `FailedEntryCount` in the response is 0. If CloudTrail holds NO PutEvents from that principal in
   the window, that is itself the result: say so.
2. **The bus and the rule as they exist:** `events describe-event-bus --name default`; `events describe-rule --name exec-summary-trigger`
   (state, EventPattern verbatim); `events list-targets-by-rule`; the target Lambda's resource policy (`lambda get-policy`). Compare the
   rule's `source` and `detail-type` with the script's emitted `Source` `bd-pipeline.gold-chain` and `DetailType` `chain-complete` and
   state whether the pattern would match the script's event.
3. **The dispatcher role's grant.** The script's comment names `bd-exporter-ec2-role` (instance profile shared by the PROD and QA
   runners). `iam get-role`, `list-attached-role-policies`, `list-role-policies`, `get-role-policy` and `get-policy` / `get-policy-version`
   for each policy; state whether any statement allows `events:PutEvents` on the default bus of this account, and name any
   permissions boundary or explicit Deny that would change it. (IAM simulation is not available to your identity; reading the
   documents is the method.) Say which role the runner actually uses if the instance profile read tells you.
4. **The script's own success test.** Read lines 840-846: `aws events put-events ... 2>&1 | grep -q '"FailedEntryCount": 0'`.
   State, from the code and the CLI's documented default output, whether a successful call on a runner configured with the
   default JSON output would match; and whether a different configured output format or CLI version on the runner could not
   match. The runner's own configuration is NOT readable by this order (reaching it is an act, not a read): mark that claim
   `inferred` or `absent`.

### 1b. The record: `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~65/EXEC_SUMMARY_DIAGNOSIS.json`

Every value carries its claim in a field a consumer can reject on: `measured` (you read it in this order, named source),
`inferred` (derived from measured values, the derivation stated), `held` (stated by a document, cited) or `absent` (could
not be read; why). Keys exactly:

```json
{"order": "FB-h-6", "read_at": "<ISO UTC>",
 "calls": ["aws cloudtrail lookup-events ...", "..."],
 "put_events_error_text": {"value": "<verbatim or null>", "claim": "measured", "source": "<call and window>"},
 "bus": {"name": "default", "exists": true, "claim": "measured"},
 "rule": {"name": "exec-summary-trigger", "state": "ENABLED", "event_pattern": {}, "targets": [], "claim": "measured"},
 "dispatcher_role": {"role": "...", "events_putevents_allowed": true, "evidence": "<policy names and statement ids>", "claim": "measured"},
 "cloudtrail": {"window_start": "...", "window_end": "...", "put_events_total": 0, "put_events_errors": 0,
                "error_codes": {}, "claim": "measured"},
 "dispatcher_test": {"line": "gold_dispatch.sh:<n>", "note": "<what the grep can and cannot match>", "claim": "inferred"},
 "verdict": "EMITTED_NOT_MATCHED | NOT_EMITTED_SCRIPT_TEST | DENIED | BUS_OR_RULE_ABSENT | INDETERMINATE",
 "verdict_reason": "<two sentences, citing the fields above>",
 "fix_owner_proposal": "<which seat's lane the fix is in, and why>"}
```

`calls` lists every AWS call you made, one string each, beginning `aws <service> <read-verb>`.
Also write a one-page `EXEC_SUMMARY_DIAGNOSIS.md` in the same folder: the same facts in prose, with the exact error text.

## 2. BOUNDS

1. READ verbs only. No `put-events`, no `invoke`, no `start-*`, no `update-*`, no `ssm send-command`, no write of any kind
   to AWS. Do not emit a test event. Do not touch `gold_dispatch.sh` or any product file.
2. If a read is denied to your identity, record the call and the denial in `calls`'s sibling field of the record you write
   (a surprise row too) and continue with the others: a denied read is a finding, not a failure.
3. Print no secret, no key, no token. Account ids and ARNs are fine.

## 3. SURFACES

<paths>
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~65/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~65/ADVI_FIRMBKTS.TO-FB-h-6.exec-summary-diagnosis.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-h-6"><invocation>timeout 30 python C:/dev/ajb_workspace/org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round5/checks/r5_checks.py diag --file C:/dev/ajb_workspace/org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~65/EXEC_SUMMARY_DIAGNOSIS.json</invocation><expect>^DIAG keys ok calls=[0-9]+ verdict=(EMITTED_NOT_MATCHED|NOT_EMITTED_SCRIPT_TEST|DENIED|BUS_OR_RULE_ABSENT|INDETERMINATE)$</expect></criterion>
  <criterion id="AC2" cell_refs="FB-h-6"><invocation>cd /c/dev/wk-firmbkts-65 &amp;&amp; timeout 60 python C:/dev/ajb_workspace/org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_scope.py --root /c/dev/wk-firmbkts-65 --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~65/ --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md</invocation><expect>^ROUND 4 SCOPE: OK [0-9]+ changed, 0 outside, 0 required missing$</expect></criterion>
</proof_of_spec>

AC1 grades the record's shape and the read-only discipline of its calls; AC2 is the write-surface bound. The truth of the findings is read by the issuer from the cited calls.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~65/ADVI_FIRMBKTS.TO-FB-h-6.exec-summary-diagnosis.proof_of_spec.json`. Commit the two files FIRST, your rows and the instance second. **Do not flip this order's `<status>`**. Row ids: `ADVI_FIRMBKTS-D1-W65-S<k>`, `k` from 1, `surfaced_at` from `date -u +%FT%TZ`. Report once: the verdict, the verbatim error text (or that CloudTrail holds none), the rule's pattern against the emitted event, the role's PutEvents statement, AC1 and AC2 outputs and the FULL commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO ADDENDUM 12 (round-3 analysis) and round-4 analysis section 3 item 4: read-only; the fix is a later cell under its own pair naming up to 158 summary keys. Row `D1-S40` (FB1) holds the facts to date: the rule is an event pattern with no schedule, TriggeredRules reads no data since 2026-09-01, the generator's newest log stream is 2026-05-04, the runner role holds events:PutEvents per FB1. The runbook's step-9 cron premise was the issuer's error (named in R4_CLOSE.md). Why a worker and not the seat: reads only, one chain, no deploy; FB1 holds the two seat orders of the round.

<status>complete</status>
<round>5</round>
<workstream>EXECSUM</workstream>
<to_id>ADVI_FIRMBKTS.TO-FB-h-6</to_id>
<slot>~65</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
