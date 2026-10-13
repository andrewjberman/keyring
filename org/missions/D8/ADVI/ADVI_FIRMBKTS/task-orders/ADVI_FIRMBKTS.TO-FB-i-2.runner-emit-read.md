# ADVI_FIRMBKTS task order -- `FB-i-2` -- THE EXEC-SUMMARY TRIGGER: THE RUNNER-SIDE READ OF THE EMIT PATH, THEN AT MOST ONE NON-MATCHING TEST EVENT

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R6.md</decomp_doc>
<owned_cells>FB-i-2</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~FB1</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no rule, schedule or cadence is added or changed; the one probe event matches no rule.
comp-iam: RUN by the actor -- reads (`s3api list-objects-v2`/`get-object`, `ssm get-document`/`get-command-invocation`, `lambda get-*`, `iam get-*`, `ec2 describe-*`, `cloudwatch list-metrics`) with the dell1 identity; the ONE conditional write is a single `events:PutEvents` of a non-matching probe, sent from the runner's own instance profile (`bd-exporter-ec2-role` already holds `events:PutEvents` on the default bus, round 5 `FB-h-6`). No grant is added or changed. If `ssm:SendCommand` to the runner is denied to your identity, the probe is NOT sent: that is a BLOCKING row, not a workaround.
comp-adversary: RUN by the issuer -- at base the record does not exist (AC1 FAIL); the grader rejects a record whose `calls` holds a write other than the one probe, a probe count that disagrees with `test_event`, a probe sent without `indeterminate_before_test`, and a verdict outside the closed set. Blindness: the grader proves shape and discipline, not that the findings are true; the issuer re-reads the cited logs.
EGRESS CLASS, declared: NONE (one event to the account's own default bus, matching no rule).
</preflight>

## 1. THE ACT -- `FB-i-2` (round 6, enrichment item 2; row `ADVI_FIRMBKTS-D1-W65-S1`; the CTO's ruling, `ledger/ROUND_ANALYSIS.round5.md` section 2)

The exec-summary generator has not run since 2026-05-03. Round 5's read-only diagnosis (`FB-h-6`) found the bus, the rule, the Lambda
permission and the dispatcher role's `events:PutEvents` all correct, and CloudTrail holding NO PutEvents call in 17 regions over 90
days, so the dispatcher's WARN `EventBridge chain-complete put-events failed` fires WITHOUT the call reaching the events API. The
failure is upstream, in the runner's emit path: client construction, credentials, region, or a caught exception. You find out which.

**The ruling, in order (do not skip step 1; step 2 only if step 1 leaves the cause open):**

### 1a. Step 1 -- the runner-side READ (reads only)

1. **The dispatcher's own log.** The dispatcher uploads its chain logs to `s3://opal-data-bd/gold/logs/<file>`
   (`data/black_diamond/scripts/gold/gold_dispatch.sh:686`). List `gold/logs/` (paginated; print the denominator), take the newest 10
   chain logs by `LastModified`, read each (`get-object`), and record per chain: whether the WARN line is present; the 3 lines before
   and after it, verbatim; every other `aws` line or error text in the log; any `SHUTDOWN_ARMED` or `SHUTDOWN_DEFERRED` line. If a log
   carries no text from the failing call (the script merges stderr into `grep -q`, so the CLI's own error text is discarded), say so.
2. **The emit path in code**, from the repository at HEAD: `gold_dispatch.sh` lines 835-855 (the call) and the whole script for any
   `--region`, `AWS_DEFAULT_REGION`, `AWS_REGION` or `aws configure`: the issuer's grep found NONE in the script. Then find what
   launches the script on the runner (`bd-gold-layer-runner`; the comments name the Lambda `bd-gold-trigger` and an SSM result): read
   that Lambda's source or configuration and the SSM document it sends (`ssm get-document`), and say whether either sets a region or
   exports one. Name the CLI client (`aws` and its version if any log prints it), the region source and the credential source (the
   instance profile `bd-exporter-profile` / role `bd-exporter-ec2-role`).
3. **The positive control the issuer measured** (re-read it, do not copy it): the dispatcher's OTHER regional calls swallow their
   errors (`>/dev/null 2>&1 || true`): `aws cloudwatch put-metric-data --namespace BD/GoldRunner` at lines 1346, 1598 and 1604 and
   `aws ec2 describe-tags` at line 1584. `cloudwatch list-metrics --namespace BD/GoldRunner` returned 0 metrics in us-east-1,
   us-east-2, us-west-1, us-west-2, eu-west-1 and eu-central-1 on 2026-10-13 ~07:5xZ (list-metrics shows the last two weeks only)
   while a control namespace (`AWS/Lambda`) returned metrics. Re-run it, and set it beside the chain logs' `SHUTDOWN_ARMED` lines:
   a printed line with no metric is a regional call failing silently on the runner.
4. **Verdict**, one of `REGION_UNSET` (a regional call cannot resolve a region on the runner), `CREDENTIALS`, `CLI_OR_OUTPUT_FORMAT`,
   `EXCEPTION_NAMED` (a log or a step names the exception verbatim), `STILL_INDETERMINATE`. Each claim carries `measured`, `inferred`,
   `held` or `absent`; `REGION_UNSET` from the absence of a region setting plus the empty namespace is `inferred` unless a line proves it.

### 1b. Step 2 -- ONE non-matching test event (ONLY if step 1 ends `STILL_INDETERMINATE`)

The CTO's word authorizes EXACTLY this one event and no other write (ROUND_ANALYSIS.round5.md section 2): a `PutEvents` from the
dispatcher's own identity with a `detail-type` that no rule matches. It writes to the events API with no consumer and moves nothing served.

1. Do NOT start any instance. Use the next chain window in which `bd-gold-layer-runner` is already RUNNING and SSM-online (the
   scheduled chains launch it at 04:00Z and 23:00Z; read `ec2 describe-instances` and `ssm describe-instance-information` first).
   Send ONE `ssm send-command` (`AWS-RunShellScript`) whose script is exactly:
   `aws events put-events --entries '[{"Source":"opal.fb-i-2.probe","DetailType":"fb-i-2-emit-probe","Detail":"{\"probe\":true}","EventBusName":"default"}]' > /tmp/fb_i_2_probe.out 2>&1; echo "rc=$?"; cat /tmp/fb_i_2_probe.out`.
   Read the result with `ssm get-command-invocation` (a read). Record the exit code and the text verbatim. No retry.
2. If the runner is not up in your window, or `ssm:SendCommand` is denied, DO NOT send: record `test_event.sent` false, file a BLOCKING
   row `ADVI_FIRMBKTS-D1-S<k>` naming which, set this order's `<status>` to `parked`, and stop. Owner `1.0.0_SA_CTO~DELL1`; condition: the
   next chain window with the runner up.
3. The probe's `Source` is `opal.fb-i-2.probe` and its DetailType `fb-i-2-emit-probe`: neither equals the rule's
   (`bd-pipeline.gold-chain` / `chain-complete`), so `exec-summary-trigger` cannot match it. Confirm that against the rule's pattern
   (`events describe-rule`) before you send.

### 1c. The record: `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/RUNNER_EMIT_READ.json`

Keys exactly (`claim` is one of `measured`, `inferred`, `held`, `absent`):

```json
{"order": "FB-i-2", "read_at": "<ISO UTC>",
 "calls": ["aws s3api list-objects-v2 ...", "aws ssm get-document ...", "..."],
 "warn_context": {"chains_read": 0, "warn_lines": 0, "text": "<the WARN's neighbouring lines, verbatim, or 'no exception text in any log'>", "claim": "measured"},
 "emit_path": {"client": "aws cli <version or unknown>", "region_source": "<none|env|config|...>", "credential_source": "<instance profile ...>",
               "launcher": "<the Lambda and the SSM document>", "claim": "inferred"},
 "positive_control": {"note": "<BD/GoldRunner metrics per region, SHUTDOWN_ARMED lines in the logs>", "claim": "measured"},
 "verdict": "REGION_UNSET | CREDENTIALS | CLI_OR_OUTPUT_FORMAT | EXCEPTION_NAMED | STILL_INDETERMINATE",
 "verdict_reason": "<two sentences>",
 "indeterminate_before_test": false,
 "test_event": {"sent": false, "count": 0, "detail_type": "", "matches_any_rule": false, "rc": null, "text": ""},
 "fix_proposal": "<the one-line change the cause implies, and whose file it is; NOT applied>"}
```

`calls` lists every AWS call, one string each, beginning `aws <service> <verb>`; the one probe is the single `ssm send-command` (or
`events put-events`) entry. Also write `RUNNER_EMIT_READ.md` (one page) in the same folder.

## 2. BOUNDS

1. Reads, plus at most ONE probe event under 1b. No other write; no deploy; no change to the dispatcher script, the Lambda, the
   SSM document, the role or the rule; no start or stop of an instance; no manual invoke of the generator.
2. Print no secret, key or token. Log lines may name accounts and ARNs, never a client name or an account number.
3. The FIX is not this order's: it is a later cell under its own never-widen pair (round-3 ADDENDUM 12: up to 158 summary keys, a
   sample read first, prior VersionIds as rollback). `fix_proposal` names it and applies nothing.

## 3. SURFACES

<paths>
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/ADVI_FIRMBKTS.TO-FB-i-2.runner-emit-read.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-i-2"><invocation>timeout 30 python C:/dev/ajb_workspace/org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round6/checks/r6_checks.py runner --file C:/dev/ajb_workspace/org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/RUNNER_EMIT_READ.json</invocation><expect>^RUNNER record ok calls=[0-9]+ verdict=(REGION_UNSET|CREDENTIALS|CLI_OR_OUTPUT_FORMAT|EXCEPTION_NAMED|STILL_INDETERMINATE) test_event_sent=(True|False)$</expect></criterion>
</proof_of_spec>

AC1 grades the record's shape and the discipline of its calls (read verbs, at most one probe, sent only when indeterminate). The
truth of the findings is read by the issuer from the cited logs and calls.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/ADVI_FIRMBKTS.TO-FB-i-2.runner-emit-read.proof_of_spec.json`. Commit the record and the prose file FIRST, your rows and the instance second; flip `<status>` to `complete` in
the SAME commit only when AC1 passes. Row ids: `ADVI_FIRMBKTS-D1-S<k>` (the row gate refuses other patterns), `surfaced_at` from
`date -u +%FT%TZ`. Report once to `2.0.0_SA_COO~B1`: the verdict, the verbatim exception text (or that no log holds one), the
region source, whether the probe was sent and its result, AC1 and the FULL commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** the CTO's ruling (round-5 analysis section 2, `D1-W65-S1`), in order: the runner-side READ, then ONE non-matching test event only if still
indeterminate, then the fix as its own cell under a pair. The issuer's own measurements at the cut (06:5xZ-07:5xZ today): the dispatcher script
has no `--region`, no `AWS_DEFAULT_REGION` and no `aws configure` (native grep); `BD/GoldRunner` holds 0 metrics in 6 regions while `AWS/Lambda`
holds metrics; the SSM document read (`advi-49f-chain-dispatch`) belongs to the 49F chain, not this dispatcher, so the gold trigger's own launcher
is yours to find. HYPOTHESIS (not a finding): the runner's CLI has no default region, so every regional call fails silently (S3 does not need
one) -- which would explain a WARN with no CloudTrail record. The estate's own code says boto3 and the CLI do not take a region from IMDS
(`estate_report_runner.py:188`). The disarm of `D1-W65-S1` is the fix cell, round 7, not this order. Class WORLD (the conditional probe write
and a live runner), reads otherwise.

<status>complete</status>
<round>6</round>
<workstream>EXECSUM</workstream>
<to_id>ADVI_FIRMBKTS.TO-FB-i-2</to_id>
<slot>~FB1</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
