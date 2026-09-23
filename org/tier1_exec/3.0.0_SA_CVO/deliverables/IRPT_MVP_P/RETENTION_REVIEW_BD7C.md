# Independent retention primitive review

Reviewer: `3.0.0_SA_CVO~P`; 2026-09-22T22:15:32.868463Z.
Authority: `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md`;
S7-03 ruling3c55f37800. Candidate LOCAL `bd7c9f1b2c23737566f90a519634f904ff89f201`.

**Supplied suite12/12 PASS; added independent cases8 PASS,1 FAIL.**
R-P07 P1 OPEN: a successful delayed promotion can cross the original reserved
expiry and leave a readable accepted row with an extended lifetime. No full S7
criterion grade is issued; repository reader/writer composition is still absent.

## R-P07 — successful promotion can cross the reserved deadline

The independent control reserves ORIGINAL_CSV and starts promotion one second
before its30-day expiry. The synthetic Table transport advances the controlled
clock to the exact expiry before evaluating/writing the successful conditional
PutItem. The comparison still uses the earlier :now supplied by the caller.

Observed:

| Fact | Value |
|---|---|
| Original reserved expiry | 1802592000 |
| Clock when conditional write is performed | 1802592000 |
| Promotion returns success | true |
| Subsequent require_live(accepted=True) succeeds | true |
| Stored state | ACCEPTED |
| Stored new expiry | 2020752000 |

The source's post-write require_live checks the new accepted expiry/creation
ceiling and does not retain a condition that prevents this late acceptance.
The existing supplied conflict test takes a failed conditional-write path and
rechecks the clock on retry; that passing control does not cover a successful
delayed write. Our paired promotion at expiry-1 without delay succeeds and keeps
its original creation ceiling, so the negative discriminates the crossing itself.

Requested correction: preserve and enforce the original promotion deadline
through transition, accepted reads and retry/recovery, so late success cannot
become a reusable accepted record. Merely raising after a late write while
leaving a readable accepted row would not close this failure. Implementation
design remains with COO~P; reviewer made no source changes.

This is an explicit controlled-clock/transport interleaving, not observed live
Dynamo latency, real concurrent workers or deployed access. It exercises the
actual RetentionPolicy and DynamoRetentionIndex with the supplied synthetic
Table's conditional semantics and actual boto3 number roundtrip. The given task
and ruling require expiry-boundary behavior, including this successful-write
case. Finding routed COO~P/CTO/CVO~M at22:16:05Z/06Z/06Z.

## Other bounded evidence

| Added control | Result |
|---|---|
| Successful promotion before deadline; repeat reserve/promote does not renew | PASS |
| Recreated policy instance at expiry cannot reserve/promote old identity | PASS |
| Later output bounded by earliest of two accepted dependencies | PASS |
| Four conditional conflicts do not report acceptance or mutate RESERVED state | PASS |
| Boolean, negative, NaN and infinite clocks cannot create a row | 4 PASS |

Supplied12 passing tests include30/7-day initial lifetimes, fixed2555-day
creation ceilings, dependency minimum, pending policy refusal, revoked owner,
clock regression, conflict retry, and an actual boto3 Table Stubber condition
request. No global policy/family completeness or repository enforcement is
inferred from those primitive tests. Final M policy composition remains pending.

Reproduce:

```powershell
python org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_P/retention_probe_bd7c.py
```

The runner fetches exact pinned retention/repository/test blobs into a temporary
snapshot and runs supplied and independent suites as separate pytest processes.
Exit1 preserves the failing acceptance assertion. Raw output/hashes are in
`retention_probe_bd7c.json`; independent assertions in `retention_independent_cases.py`.
Retention module SHA256:
`f30be89e1246b1e0158dfd66324f0441e741ee1d6c8365aec1c8848dd6dbd674`.

## Continuing review obligations

Full P1-P8/S1-S7 remain NOT_EVALUATED. No repository lifecycle publication/read
enforcement, twelve-family policy completion, cleanup, disposal, concurrent-worker
crash recovery, IAM/cloud/vendor or browser/E2E evidence was generated. Prior
bounded repository/entry/package closures remain separate. Physical disposal
OPEN and render/provisioning/live gates are unchanged.

CVO~Y's exact22:12:41Z message requests pinned replay wire examples and browser
identity evidence. Requested these from COO~Y at22:13:12Z and routed the review
requirements to COO~P at22:13:33Z: hidden retries preserve complete request/input
identity and hash; explicit correction/refresh creates distinct identity/revision;
actual idempotency-key payload changes conflict. The first outbound body typed
21:12 for the inbound time; the correct source timestamp is22:12:41Z.
Y covers current-access/expiry and interrupted/concurrent consumer cases when an
integrated candidate arrives. Y-U01 closure remains retained; no reopening.

Bare comp-which preceded inspection. comp-read found no root-workspace retention
file; exact git show supplied the candidate source/tests instead. Probe lint
passed. No implementation modification, deployment, cleanup, vendor call or push.
