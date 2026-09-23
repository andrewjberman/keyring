# W1 broker recovery: actual response evidence

Source **4173322f457aeeb390033b410e85bebadc49a3e3**, parent
5609c2e46a2d36716743f21a8e6a5eec6876e5d8, branch irpt-mvp-y-20260922.
Bounded LOCAL candidate under the existing broker/W1 mandate; direct CTO review
requested. This is not full W1 closure or a runtime installation claim.

The historical eviction_verdict fabricated an application/json reply with body{}
from each failed step's status. The old transport table then classified any401
as REFRESH. This lost the actual response evidence and could misclassify an
unknown auth failure. It could also miss the recognized403 session-loss body.

The broker now wraps each attempt's installer-supplied transport in its own
reply observer. It passes the actual status/body/content-type/WAF action to the
existing session/controller.py classifier, retaining only its action, reason,
status, operation and body hash. Neither raw body nor headers/URLs are persisted.
Only the latest observed read with REFRESH_ONCE and EVICTED/SIGNED_OUT may enter
the existing one-refresh rule. A later request clears earlier evidence before
dispatch, so even an exception cannot reuse stale eviction evidence.

Unknown401/403, generic login HTML, WAF, entitlement and404 do not refresh.
Non-GET/HEAD operations cannot trigger refresh; they require reconciliation.
The wrapper supplies no transport, login, network call, operation lease or cloud
action of its own. Existing operation-fenced transports can be passed through
the same factory. Existing broker verification and checkpoint resumption remain.
Legacy direct eviction_verdict(job_record) calls without the observer now return
None: step status and self-reported decision are insufficient evidence.

## Evidence and precise bounds

- **54 session tests PASS**:19 new broker controls plus existing35 operation-lease
  and controller tests. No skips. Uses the previously extracted exact
  FirmDestinationPolicy from CLOUD b475b96309c0034b513f19393138984d05716d0e.
- The real GenerationJob checkpoint regression independently counted one create
  on recovery, two in its deliberate restart negative control, and parked a
  repeat eviction after the one allowed refresh.
- Separate run_session_suite.py reported c_rotation=true, d_eviction=true,
  controls=true and netguard_positive_control=true; all_pass=true.
- The old positive fixture used generic sign-in HTML at401. It now explicitly
  uses the known signed-out phrase. Generic HTML is retained as a negative
  control in the new tests; it is no longer mislabeled proof of session loss.
- Source gates passed for exactly broker.py, tests/run_session_suite.py and
  tests/test_broker_recovery_evidence.py under ycharts/session. No generation
  transport/job file changed. Risk reflex again matched the unrelated
  org/mcp/broker.py LD-0125 basename warning previously read; that file is untouched.
- The first regression-output decoder assumed UTF-8, but Windows PowerShell
  redirection emitted UTF-16. The regression itself exited0; decoding with its
  actual encoding verified all_pass and saved normalized UTF-8 local evidence.

Full generation/intake suites were not rerun for this broker-only repair. These
measurements are local author evidence, pending direct CTO review. The Kimi
deadline closure df23c8e35a applies to its prior exact source pin, not automatically
to this new candidate's overall behavior.

W1 remains OPEN for installed consumer coverage, shared account operation lease,
total wall-time interruption, durable D2 interpreter and actual runtime proof.
The historical transport.decision table itself remains unchanged; consumers
outside run_with_recovery must not claim this observer's conservative behavior.
No live calls, credentials, host actions, deployment or push occurred.

```powershell
$env:IRPT_FIRM_DESTINATION_POLICY = (Resolve-Path '.runtime/firm_destination_policy.json').Path
python -m pytest infra/aws/lambda/investor-reporting/ycharts/session/tests/test_broker_recovery_evidence.py infra/aws/lambda/investor-reporting/ycharts/session/tests/test_operation_lease.py infra/aws/lambda/investor-reporting/ycharts/session/tests/test_controller.py -q
python infra/aws/lambda/investor-reporting/ycharts/session/tests/run_session_suite.py
```
