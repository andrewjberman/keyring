# Independent retained submission review

Reviewer `3.0.0_SA_CVO~Y`, September 22, 2026.
Authority: `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md` v1.2.
Candidate `6cbb71404003a4d2ba7bcfa8871e5149e97256e2`.

**Y-S01 P2 OPEN:** missing retention service silently downgrades known retained
input/composition. Supplied **52 tests plus24 subtests PASS**; independent
**6 PASS / 2 FAIL**. This is a bounded SubmissionService finding, not a
demonstrated queue/vendor execution or full integrated criterion verdict.
Routed to COO~Y and CVO~P with the exact trigger and expected behavior.

## Reproduction

```powershell
python org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_Y/probe_upload_consumer.py --pin 6cbb714040 --output org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_Y/UPLOAD_CONSUMER_6cbb714040.json
python org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_Y/probe_retained_submission.py --source-evidence org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_Y/UPLOAD_CONSUMER_6cbb714040.json --output org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_Y/RETAINED_SUBMISSION_6cbb714040.json
```

The independent probe verifies289 snapshot hashes and executes actual Y
SubmissionService and P retained artifact/retention code. Acceptance lookup,
accept and dispatch use the supplied Mock; storage and clocks are controlled
doubles. Socket connections are forbidden. Exit1 records the two failed
independent controls; the supplied suite exits0. The17 upload tests in the
snapshot command overlap the52 suite and are not an additional denominator.

## Y-S01: known retained records require a retention service

Source: `ycharts/generate/submission_service.py`, `_retained_input` and
`_verify_retained_composition`. Both return immediately when
`getattr(self.artifacts, "retention", None) is None`, without inspecting whether
the input or accepted composition already carries a retention_ref.

1. Create a real retained upload and request composition. Its accepted ref
   contains a retention_ref and inherits the normalized input's day30 deadline.
   Set the clock to that exact deadline. Normal replay refuses RetentionExpired
   before dispatch: zero calls.
2. Keep that same accepted record, request, owner and deadline, but remove the
   repository retention service, modeling a missing dependency during service
   composition/restart. Replay now returns RECEIVED with dispatch_pending=false
   and invokes acceptance.dispatch once. Provider resolution is forbidden and
   is not called; the expiration check itself was skipped.
3. In a fresh world, resolve a valid retained input, then remove the retention
   service before its first submission. The service persists/accepts a bare
   REQUEST_COMPOSITION with no retention_ref and invokes dispatch once, despite
   the input_ref retaining its retention_ref.

Expected: known retained input/composition must refuse missing retention service
before storage/acceptance/dispatch. A genuinely unretained offline fixture is a
separate compatibility case; it cannot justify downgrading retained records.
Keep both exact negative controls and the configured-service positives for
independent retest. The observed dispatch is a Mock call, not proof that a real
queue or worker would perform a vendor action. This identifies the service
boundary's behavior if miscomposed; no deployed misconfiguration is claimed.

## Passing controls

| Control | Observation |
|---|---|
| First request20 days after input creation | Composition depends on exact normalized retention ref and inherits its original deadline |
| Live unchanged replay | Same result, zero new blobs, no provider resolution |
| Configured retention at exact expiry | RetentionExpired; zero dispatch calls |
| Changed input artifact version receipt | RETAINED_INPUT_BINDING before storage/acceptance/dispatch |
| Expiry during post-acceptance composition blob read | RetentionExpired; zero dispatch calls |
| Policy becomes pending after acceptance | RetentionRefused; zero dispatch calls |

Complete SubmissionService, new retained-submission tests and relevant changes
were read. Recovery/outbox worker composition, dispatch-time races, persistent
transactions, policy activation, browser and end-to-end acceptance remain
unproven. The upload dependency reviewdb30f876fa stays separate and valid for
its controls. P history closure452f8d589f is attributed, not rerun by Y.
All fourteen integrated criteria remain NOT_EVALUATED. LOCAL evidence only;
no implementation edit, vendor/session access or real queue send by reviewer.

-- 3.0.0_SA_CVO~Y
