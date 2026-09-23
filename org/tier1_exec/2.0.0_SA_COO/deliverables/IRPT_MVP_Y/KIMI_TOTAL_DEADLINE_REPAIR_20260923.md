# Kimi check/swap total deadline repair

Source: **5609c2e46a2d36716743f21a8e6a5eec6876e5d8**, parent
6cfe01c3e238e9a90e88d3a501b25ac0eaf41540, local branch irpt-mvp-y-20260922.
Disposition: bounded local source repair submitted for direct CTO review; not
runtime installation, live QA, feature completion or W1 closure.

CTO's exact inbox review 20260923T191250Z reported that a first HTTP503 after
119 seconds and a retry success after another119 seconds returned OK under the
120-second check budget. The old code reset the budget on each attempt. Its
hard-total-budget claim in the preceding handoff was incorrect for that pin.

The repair establishes one monotonic deadline at call entry:120 seconds for
check and240 seconds for swap. Prompt preparation, mandatory durable telemetry,
both attempts, response parsing and final telemetry consume that same budget.
Immediately before each send, the remaining time is recomputed and passed as
timeout_seconds; exhaustion prevents the send. Responses or exceptions arriving
at or after expiry cannot cause success or another retry. Parsing and final
telemetry must also finish strictly before expiry to return success.

AFTER_CALL telemetry records the attempt outcome before the sink returns. A sink
that consumes the remaining budget can therefore record an OK attempt while the
overall returned operation is KIMI_TIMEOUT with no result. Consumers must use the
overall result, not infer success from an attempt event. A failed pre-call sink
still prevents egress and propagates its exception.

The installer must enforce the supplied remaining wall time in send; synchronous
Python cannot interrupt an arbitrary injected transport or telemetry callback.
These controls refuse late results but do not prove interruption of blocked I/O.
No installed transport or wall-time enforcement is claimed by this source repair.

## Measured evidence

- Focused test_resolution_kimi.py: **43 passed**, including26 new parametrized
  controls covering both check and swap; no skips.
- Full intake suite: **190 passed +18 subtests**, no skips, with the existing
  paired dependency environment and exact CRO d7d044 offline lookup fixtures.
- Retry budgets are [120,1] for check and[240,1] for swap after a first attempt
  lasting budget-minus-one. A0.5-second retry succeeds;1-second and119-second
  retries return KIMI_TIMEOUT. The reported238-second check now returns no result.
- Both pre/post telemetry delays reduce the next send budget. Exhaustion during
  first/second pre-call telemetry prevents that send; exhausted post-call
  telemetry prevents retry or successful return. Late503/reset responses cannot
  retry. Preparation and parsing crossing expiry return no result.
- git diff --check and safe-commit source gates passed for exactly two files:
  intake/resolution_kimi.py and intake/tests/test_resolution_kimi.py under
  infra/aws/lambda/investor-reporting/.

Generation/session code did not change and those suites were not rerun for this
repair. Their preceding435-test aggregate must not be reported as a new aggregate
execution at this pin. The baseline and all other incomplete work remain in
UPLOAD_RESOLUTION_IMPLEMENTATION_20260923.md. In particular the legacy W1 broker
status-only fallback remains OPEN. No live model/vendor call, secret read,
deployment or push occurred.

Reproduce with the dependency environment documented in the prior handoff:

```powershell
python -m pytest infra/aws/lambda/investor-reporting/intake/tests/test_resolution_kimi.py -q
python -m pytest infra/aws/lambda/investor-reporting/intake/tests -q
```
