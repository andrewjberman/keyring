# W1 causal request correlation repair

Exact source **fe0ec628c24af3cc8915bfe6899c5295f50a64f9**, parent
4173322f457aeeb390033b410e85bebadc49a3e3, LOCAL branch irpt-mvp-y-20260922.
Direct CTO review requested under the existing local W1 mandate. Full W1 remains
OPEN; no runtime installation, live call, login, host action, deploy or push.

CTO's exact193152 message independently reproduced the prior54 session tests and
separate regression, but found a missing correlation: a recognized401 application
failure followed by a healthy diagnostic read returned NOT_AN_EVICTION because
the broker consulted its latest observation. That prior source behavior violated
the requirement that a healthy probe cannot override a failed application endpoint.

## Repaired contract

Each broker observer has a fresh random attempt identifier and a request counter.
It returns an opaque **recovery_observation_id** in request info alongside the
unaltered response bytes. The observer retains a bounded map of safe classifications
(action, reason, status, operation, body hash, observation ID), never raw bodies.
The existing recipe step helpers propagate that ID. GenerationJob returns the
failed step's ID as **failure_observation_id**, including its reconciliation read.

run_with_recovery resolves only that exact ID against its own current-attempt map.
It never infers the cause from status, a self-reported decision, the latest probe,
or any earlier eviction. Other broker consumers must return this internal failure
ID too; omission, unknown IDs and IDs from another attempt fail closed.
This is an internal server-consumer contract, not a new HTTP request field.

Healthy diagnostic reads leave the causal receipt resolvable. A later contract
failure names its own non-evicting receipt. Every non-GET/HEAD request clears older
receipts before dispatch and cannot itself authorize refresh. Transport or
classification exceptions clear all prior receipts. The map retains at most256
receipts; a pruned ID cannot be resolved. Mutation reconciliation and the existing
one-refresh/checkpoint rules remain in force.

## Measured evidence

- **65 session tests passed**, no skips:30 broker controls plus35 existing lease
  and controller tests. The prior54-test candidate is a subset, not additive.
- Exact synthetic failure-then-probe case now returns RECOVERED with one refresh
  and recovery_pull.status401. Paired old-eviction-then-contract and mutation
  failures return NOT_AN_EVICTION with zero refreshes and the causal422 receipt.
- The actual GenerationJob regression also runs with a healthy step_identity
  probe inserted after step_read_back. It preserves the application's failed
  observation, recovers with exactly one create, and parks a repeated eviction.
- Explicit controls refuse unknown/missing/cross-attempt IDs, IDs invalidated by
  mutation or exception, classifier exceptions and pruned history entries.
- Full generation suite: **236 passed +32 subtests**, no skips, using the existing
  pinned paired dependency environment. Intake was not rerun for this repair.
- Separate rotation/eviction/controls/netguard regression reported all_pass=true.
  It ran before the final exception-clear refactor; the final65-test session run
  includes the actual checkpoint regression and the additional exception controls.
- git diff --check and safe-commit source gates passed for all four changed files:
  session/broker.py, session/tests/test_broker_recovery_evidence.py,
  generate/recipe.py and generate/job.py under ycharts/.
  Risk reflex again cited unrelated org/mcp/broker.py LD-0125, previously read;
  no MCP broker was edited.

The observer does not enforce installed account leases or wall-time interruption.
Durable D2 execution, complete runtime consumer coverage and end-to-end feature
acceptance remain open. The historical transport.decision table is unchanged.
The source additions must be consumed together: broker-only integration would
omit the actual GenerationJob failure-ID propagation and fail closed.

Run the same session command in W1_BROKER_BODY_EVIDENCE_REPAIR_20260923.md and:

```powershell
python -m pytest infra/aws/lambda/investor-reporting/ycharts/generate/tests -q
```
