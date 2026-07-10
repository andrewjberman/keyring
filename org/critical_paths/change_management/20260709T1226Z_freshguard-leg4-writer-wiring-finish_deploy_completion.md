# Deploy Completion Record
**Date opened:** 2026-07-09T12:26:09.108694+00:00
**Status:** HELD-SOVEREIGN-GATED -- gate: external / L4 RE-SPECCED (CTO 232022Z) + TRIGGER-MODEL CORRECTED (0.7.0_AE_CloudOps 020930Z, grounded on live AWS).

=== TWO CORRECTIONS TO THIS LEDGER'S OWN PRIOR GATE TEXT -- both were CLOCK assumptions on an EVENT trigger ===
(C1) The derive is cron(0 2 * * ? *) = 02:00Z, NOT "~02:10Z". Rule opal-globgrph-derive-runner-nightly, ENABLED.
(C2) incremental_updater is NOT "hourly". It is SQS-EVENT-DRIVEN: event-source-mapping on
     arn:aws:sqs:us-east-1:313476888478:opal-globgrph-incremental-events (Enabled), and ZERO EventBridge rules
     target arn:aws:lambda:us-east-1:313476888478:function:opal-globgrph-incremental-updater
     (`aws events list-rule-names-by-target` returns empty). "Hourly" was an OBSERVED CADENCE, never a schedule.
     Observed fires 07-09/10: 22:11,22:16,22:21,23:01,23:56,00:01,00:16,00:21,00:56,01:01,02:01Z -- irregular.
     => DO NOT WAIT FOR A CLOCK. "~03:00Z" is unfounded. Gate on the EVENT, or you measure at the wrong moment
     (the exact LD-0267(C) trap this re-spec exists to prevent).

=== EVIDENCE ALREADY BANKED -- the derive limb of the criterion is SATISFIED and CAPTURED ===
Tonight's derive stamped 4 tables at 2026-07-10T02:09:13Z (caught live by a marker-transition poller):
    writer_id=derive_runner  tables=[cse,graph_contracts,graph_edges,graph_nodes]  cse=PRESENT
    ETag "94ab4adc17ca85fc0d8681c5c8bfd09a"  LastModified 2026-07-10T02:09:13Z  size 1502
Bucket versioning is OFF (Andrew-locked #5), so the next incremental stamp DESTROYS this object unrecoverably.
Snapshot preserved off-bucket: scratchpad/leg4_derive_4table_marker_20260710T0209Z.json
That snapshot is why limb (A) survives the clobber. WITHOUT IT, after the overwrite you CANNOT observe that the
derive ever stamped 4, and the criterion becomes un-evaluable rather than failed.

=== THE CRITERION, RESTATED IN EVENT TERMS (any lane may execute; do NOT close on a 4-table read) ===
Let T_d = 2026-07-10T02:09:13Z (the derive's 4-table stamp, ETag above).
PASS  iff (>=1 incremental_updater invocation COMPLETED at t > T_d) AND (live marker STILL lists all 4 tables).
FAIL  iff (>=1 such invocation) AND (marker lists 3; cse ABSENT).            <-- EXPECTED TONIGHT, BY DESIGN.
CANNOT-EVALUATE iff (zero such invocations). Then the ledger STAYS OPEN and you report exit 2. NEVER a PASS.
      A quiet SQS queue is not evidence the merge works. It is evidence you did not test it.

=== EXACT READ COMMANDS ===
# 1. Has >=1 incremental_updater invocation completed since T_d?
aws cloudwatch get-metric-statistics --namespace AWS/Lambda --metric-name Invocations \
  --dimensions Name=FunctionName,Value=opal-globgrph-incremental-updater \
  --start-time 2026-07-10T02:09:13Z --end-time "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
  --period 300 --statistics Sum --query 'Datapoints[?Sum>`0`].[Timestamp,Sum]' --output text
#    (empty output => CANNOT-EVALUATE. Stop. Do not close. Do not pass.)

# 2. Does the live marker still list all 4 cadence-configured tables?
aws s3 cp s3://opal-313476888478-globgrph/warehouse/_branch_head.main.json - | python -c \
  "import sys,json; d=json.load(sys.stdin); tm=d.get('table_metadata',{}) or {}; \
   print('writer',d.get('writer_id'),'n',len(tm),sorted(tm),'cse','PRESENT' if 'cse' in tm else 'ABSENT')"
#    n=4 & cse PRESENT => PASS (merge landed).   n=3 & cse ABSENT => FAIL, correctly, merge not landed.

# 3. Corroborate the reader-honesty fix b9f991994 is what surfaces it (must print ABSENT FROM MARKER, not silence).

=== WHY IT STILL FAILS, AND WHY THAT IS THE DELIVERABLE ===
stamp_marker rebuilds table_metadata from its caller's table_names and put_objects the WHOLE marker
(_provenance.py:203-235); incremental_updater passes 3 (lambda_function.py:575), derive passes 4
(derive_runner.py:413 / cse_store.py:91). So every incremental stamp ERASES cse. The merge fix is HELD by CTO
pending compare-and-swap: put_object(IfMatch=<ETag of the read>) + bounded 412 retry + LOUD raise on exhaustion
AND on ParamValidationError (stamp_marker is best-effort/never-raises, so an unsupported IfMatch would be
swallowed into a WARN and SILENTLY STOP STAMPING). Probe built 8c0b67afd, UNRUN, hard-gated to first light:
IfMatch must be confirmed in the DEPLOYED runtimes (Lambda bundled botocore + derive image pinned boto3), never
inferred from the dev box. Three verdicts; IGNORED (param accepted and silently dropped) is the one that kills us.

L4 STAYS OPEN. Ledger STAYS OPEN. This is a REFUSAL, not a failure to finish. (held since 2026-07-09T13:11:12.866381+00:00)
**Deploy:** FRESHGUARD leg-4 finish: wire all 3 writers (derive_runner/incremental_updater/cse_store) to the centralized _provenance.stamp_marker so per-table last_write_iso lands live. GROUNDED: leg-4 is SOURCE-INCOMPLETE (unwired), not merely undeployed -- the centralized stamp has ZERO call sites; all 3 writers stamp their own local marker with no last_write_iso field. HELD on CTO approach-gate (A centralize-import vs B 3-copy).
**Authored by:** 0.7.0_AE_CloudOps
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD: wire 3 writers -> _provenance.stamp_marker + Dockerfile COPY _provenance.py + Lambda zip vendors _provenance.py | hash pushed | committed 86ab291f8 (6 files, +61/-133), pushed origin/CLOUD edc6790c4..86ab291f8. All 3 writers delegate to _provenance.stamp_marker; Dockerfile COPY _provenance.py; zip vendors _provenance.py (sha256 9dC0bal9...); source map updated. commit-gate clean; grep-proven zero residual local marker-write (only _provenance.py:227). | CLOSED 20260709T125750Z |
| L2 | activation | derive image CodeBuild rebuild+push (derive_runner+cse_store call shared stamp; image carries _provenance.py) | CodeBuild build-id + image digest | CodeBuild globgrph-derive-build:fb7b48b9 SUCCEEDED/COMPLETED. APPLIED-truth: ECR opal-globgrph-derive-runner:latest pushed 2026-07-09T13:06Z, tag 20260709-130548, digest sha256:2b7f5ec0bfdb329d25cef5adeaad9ba1abc23904ada56aefd68d87a4990e821a. Image carries _provenance.py + derive_runner/cse_store delegation (P3-FREE: motif reverted to fad55a83c^, signature-free per CTO sequencing). Task-def globgrph-derive-runner references :latest -> nightly auto-picks up (no revision needed). | CLOSED 20260709T130943Z |
| L3 | activation | incremental_updater Lambda: rebuild zip(+_provenance.py) + safe-apply TF (source_code_hash tracks) | get-function CodeSha256 + 0-diff plan | safe-apply complete 0-add/1-change/0-destroy (HALT-gate clean). APPLIED-truth (Rule22a): get-function-configuration opal-globgrph-incremental-updater CodeSha256=9dC0bal9JcpQ9D0CuBaeXOT1E9LY80btOGR6lsHmzTA= (== rebuilt zip w/ _provenance.py vendored), State=Active, LastUpdateStatus=Successful, LastModified 2026-07-09T13:07:33Z; targeted 0-diff plan = No changes. Lambda now delegates to _provenance.stamp_marker. | CLOSED 20260709T130834Z |
| L4 | verify | live marker last_write_iso POPULATED all 3 tables, EXERCISED (real incremental write + nightly derive), APPLIED-truth Rule22a | marker read per-table non-null + writer_id |  | OPEN |

## Log

- 20260709T122609Z OPENED by 0.7.0_AE_CloudOps with 4 leg(s)
- 20260709T125750Z LEG L1 closed: committed 86ab291f8 (6 files, +61/-133), pushed origin/CLOUD edc6790c4..86ab291f8. All 3 writers delegate to _provenance
- 20260709T130834Z LEG L3 closed: safe-apply complete 0-add/1-change/0-destroy (HALT-gate clean). APPLIED-truth (Rule22a): get-function-configuration opal
- 20260709T130943Z LEG L2 closed: CodeBuild globgrph-derive-build:fb7b48b9 SUCCEEDED/COMPLETED. APPLIED-truth: ECR opal-globgrph-derive-runner:latest push
- 20260709T131112Z HELD-SOVEREIGN-GATED gate=external/next nightly derive_runner ECS run ~02:10Z (last_write_iso all 4 tables) + next 
- 20260709T232036Z HELD-SOVEREIGN-GATED gate=external/GATE RESTATED 2026-07-09T23:20Z (0.7.0 finding 231918Z, source+applied+exercised
- 20260709T232058Z HELD-SOVEREIGN-GATED gate=external/GATE RESTATED 2026-07-09T23:20Z (0.7.0 finding 231918Z; source + applied + exerc
- 20260709T232435Z HELD-SOVEREIGN-GATED gate=external/L4 RE-SPECCED (CTO 232022Z) -- the old criterion ('last_write_iso populated on a
- 20260710T021104Z HELD-SOVEREIGN-GATED gate=external/L4 RE-SPECCED (CTO 232022Z) + TRIGGER-MODEL CORRECTED (0.7.0_AE_CloudOps 020930Z
