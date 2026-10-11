# AMGT_RESAPP task order -- `AMGT-aa-3` -- READ, DO NOT CHANGE: THE CAUSE OF THE TWO HTTP 500s ON `/compare` DURING THE CVO'S WALK (ROW C-S82)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-aa-3</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~RA1</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-aa-3.read-the-two-compare-500s-to-their-cause</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a read-only reading; nothing is scheduled.
comp-iam: DECLARED-NOT-APPLICABLE -- reads only (logs:FilterLogEvents or GetLogEvents, cloudwatch:GetMetricData, lambda:GetFunctionConcurrency / GetAccountSettings, apigateway GET); no grant is added or used for a write.
comp-adversary: RUN at the cut -- r95_reading_check.py reads NO at the base (no reading exists) and YES against a throwaway sample reading that carries every heading, three denominated sources, both metrics, a reserved-concurrency line, one CAUSE token and WRITES: none.
EGRESS CLASS, declared: NONE (AWS control-plane and CloudWatch reads from the runner's own credentials).
</preflight>


## 1. THE ACT -- `AMGT-aa-3` (round 95, decomposition s.103): A READING, NOTHING CHANGED

CTO~DELL1 round-94 analysis item 3 (row `AMGT_RESAPP-D1-C-S82`, INERT). During the CVO's browser walk of portal DEV (`http://localhost:5174`, 2026-10-11 15:34Z to 15:44Z; the
walk's own files are `tmp/ui-walk/20261011T153440Z/netlog.tsv`, `findings.json` and `summary.md` in the dell1 checkout), 2 of 70 `GET /api/scoped/amgt/security/<ticker>/compare`
calls answered HTTP 500: `/api/scoped/amgt/security/ROG/compare` on the Model tab and `/api/scoped/amgt/security/BA/compare` on the Posture tab. The other 68 answered 200
(14 and 15 of them for those same names), the CVO's direct Lambda invokes of the same paths answer 200, and the function's log group `/aws/lambda/opal-amgt-scoped-api` shows 0
ERROR, Traceback, timeout or runtime-exit lines over 15:34Z-15:44Z. So the 500 was not raised by the function's code. The request crosses: the dev server's proxy (`portal/vite.config.ts`,
`/api/scoped/*` -> `https://d2n2nzpeqf34ge.cloudfront.net`), CloudFront, the API behind it, and the Lambda. A REST API answers 500 when the Lambda invoke itself is refused
(throttling included) and a browser walk fires parallel calls. That is a reading to MEASURE, not a cause to assume.

READ, with your own credentials, and write ONE reading to `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~RA1/C-S82_COMPARE_500_READING_20261011.md` in the shape
`checks/r95_reading_check.py` grades (its docstring is the template: headings Sources, Requests, Metrics, Concurrency, Layers, Cause, Not changed):

1. The API layer's own log lines for the two requests: find which API and stage serve `d2n2nzpeqf34ge.cloudfront.net`'s `/api/scoped/*` origin (read the distribution's origins
   and the API's stage settings; say if execution or access logging is not enabled, which is itself a finding), then the lines for the two paths in 15:30Z-15:50Z. Print the
   request id where one exists, the integration status and latency.
2. The function's `Throttles` and `ConcurrentExecutions` (and `Errors`, `Invocations`) at 1-minute grain over 15:30Z-15:50Z; the function's reserved concurrency
   (`get-function-concurrency`) and the account's concurrency limit (`get-account-settings`).
3. What each layer shows, or `not readable: <why>` (the dev-server proxy has no log you can read: say so; CloudFront standard logs or real-time logs only if they exist).
4. The cause as ONE token (THROTTLED, GATEWAY-INTEGRATION, DEV-PROXY, CLOUDFRONT, FUNCTION, UNDETERMINED) with the reasoning, and for UNDETERMINED the one source that would
   decide it. A fix is NOT part of this order: it is cut only after the reading, as its own cell, by the issuer.

WRITE NOTHING anywhere else: no change to any function, API, stage, log setting, alarm, concurrency or metric filter, and no test traffic against the live API beyond the CVO's
two direct GET invokes you may repeat (each answers from a read-only route). The reading is the whole deliverable.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-RA1-S<k>`, `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Reads only. No function, role, route, stage, log-group setting, alarm, schedule or other write; no S3 delete, ever. No Bloomberg, SEC or model call.
2. No `bun`, `npm` or `pip install`.
3. Standing: no push of shared branches. Every send to mdpf-daily-runner is reported after the fact with its command id and purpose.
4. 49 Financial data never goes into another firm's tree. The reading names no client, firm or account.
5. A source you cannot read is a finding in the reading (`not readable: <why>`), never a reason to guess a cause.

## 3. SURFACES

<paths>
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~RA1/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-aa-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round95_prep/checks/r95_reading_check.py" "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~RA1/C-S82_COMPARE_500_READING_20261011.md"; echo "exit=$?"</invocation><expect>PASS S1 (every heading present, in order, non-empty), PASS S2 (at least three sources, each with an n= denominator), PASS S3, PASS S4, PASS S5 (exactly one allowed CAUSE token), PASS S6 (WRITES: none); R95 READING SHAPE: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-aa-3" judgment="true"/>
</proof_of_spec>


<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO~DELL1 round-94 analysis item 3: "C-S82, read only: API Gateway execution/access log lines for the two failing request ids, the function's Throttles and ConcurrentExecutions over the walk window, and the function's reserved concurrency. The reading names the cause. A fix is cut only after it, as its own cell." The walk's netlog carries method, status and path only (no request id, no time): the reading finds the lines by path and window. AC2 is the CVO's judgment: the reading's cause follows from its evidence and its denominators; a CAUSE the evidence does not support, or an UNDETERMINED that names no deciding source, is NO. A seat order (not a spawned worker); LOCAL risk (a record only).

<status>pending</status>
<round>95</round>
<slot>0.7.0_AE_CloudOps~RA1</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
