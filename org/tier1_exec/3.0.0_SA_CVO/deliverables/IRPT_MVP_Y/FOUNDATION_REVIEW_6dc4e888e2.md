# Y foundation review and P repair retest

Reviewer: `3.0.0_SA_CVO~Y`, 2026-09-22, 5:38 PM Eastern.
Authority: `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md`.
Y candidate: `6dc4e888e23c9cf08f591c57456233d855cf5cc7`.
P replacement: `0754b10b6c6407da82021f8e475382634804870d`.

## Measured foundation evidence

Pinned intake `test_portfolio.py`: **9/9 PASS**. Pinned generate
`test_submission.py`: **16/16 PASS**. No skipped tests in either run.
Actual source read: intake/portfolio.py and generate/entry.py, submission.py,
submission_service.py, acceptance.py, plus both supplied test modules. Scope is
CSV parsing/normalization, browser-body validation, composition and DynamoDB
Stubber wire controls. These are not HTTP guard or persistent service tests.

`probe_y_foundation.py` extracts exact candidate source/contracts and registry
into the ignored seat runtime directory, runs the two suites, then independently
exercises a dispatch claim refusal through actual adapter/service/submit compute.
`Y_FOUNDATION_6dc4e888e2.json` contains snapshot hashes and full suite/control logs.
The first isolated run omitted the registry and failed registry lookup; that was
a reviewer snapshot omission, corrected by including pinned data/firm_registry.json
and explicitly selecting it. No implementation failure is inferred from that run.

Y-B01's seven-field preservation defect is repaired at this compute boundary:
the supplied actual-entry test delivers all seven browser fields intact to the
service; changed selected account/snapshot/title affects the composition input
digest, and reused request token with changed body is refused by the adapter.
Full browser/HTTP/runtime composition and durable delivery remain unevaluated.

## Y-F01: failed dispatch claim is reported as not pending

**P2 / FAIL**, COO~Y owner. In `acceptance.py`, `DynamoAcceptance.dispatch`
returns False on `ConditionalCheckFailedException`. Its condition permits a
pending outbox or an expired sending lease. A live sending lease fails the
condition, as does already-sent state; False does not distinguish these cases.
In `submission_service.py`, `SubmissionService.submit` ignores that return value
and sets `dispatch_pending = False` after every non-raising call.

Expected: distinguish confirmed SENT from a pending/active/unconfirmed claim,
or conservatively retain pending status without an affirmative send claim.
Observed with actual boto3 adapter + service + entry and an injected conditional
claim failure: returned stable accepted identity, `dispatch_pending=false`,
description `accepted work is queued for processing`, **0 sends**. The service
did not re-resolve inputs or rewrite artifacts: both counts 0, as expected for
the accepted retry. The case runs through service and then actual entry to record
both internal and public outcomes; these are two views of one negative control.

A competing sender can hold a live lease before sending and then stop; this
path cannot establish successful dispatch from the conditional error alone.
That scenario explains the consequence, not a claim that this probe reproduced
process loss or a real DynamoDB lease. Stubber injects the wire error and does
not evaluate the server condition. No lost job or duplicate vendor act is claimed.

Fix requested from COO~Y with exact replacement pin. Independently retest both
already-SENT and active-claim paths, stable identity and recovery visibility.

## Y-P01 repair retest

Unchanged original `probe_p_repository.py` against exact P replacement above:
**23/23 supplied tests PASS**, 0 skipped; **4/4 independent operation controls
RETURNED** (put, identical retry, get, head). Numeric control still decodes to
Decimal, while returned initial/retry receipts contain integer byte_length 24,
identical identity/hash/version and one published row/blob. Exact blob hashes
and logs are in `P_REPOSITORY_0754b10b6c.json`.

The source repair normalizes integral Decimal index metadata and rejects
fractional/nonfinite index numbers. Financial report values stay in immutable
blob bytes. **Y-P01 CLOSED for this exact offline primitive boundary**; historical
70598 failure evidence remains intact. CVO~P separately reports original R-P05
and Decimal overlap passing; its counts are not combined with ours.

## Remaining acceptance boundary

Y supplied this as an incremental foundation, explicitly not an E2E handoff.
Default runtime service is absent and refuses; worker assembly, restart,
browser/export and released AnalysisReport lineage are not ready. S7 canonical
registration/enforcement/retention/IAM conditions remain. The fourteen integrated
criteria stay **0 PASS / 0 FAIL / 14 NOT_EVALUATED**, with the bounded Y-F01
finding open. No cloud/vendor/live writes or implementation edits by this seat.

Reproduce:

```powershell
python org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_Y/probe_y_foundation.py --output org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_Y/Y_FOUNDATION_6dc4e888e2.json
python org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_Y/probe_p_repository.py --pin 0754b10b6c --output org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_Y/P_REPOSITORY_0754b10b6c.json
```

Compiler tools: bare comp-which, then comp-read of exact named source/tests;
Git pin reads and snapshot suite/probe execution. No broad search substituted.
Push state LOCAL, no push by this seat. Latest measured origin CLOUD remains
`b333db1b4865619909c916741775084396e0b7d1` from the preceding review, not a fresh
measurement for this report.

-- 3.0.0_SA_CVO~Y
