# Independent fenced report-index review

Reviewer `3.0.0_SA_CVO~Y`, September 22, 2026.
Authority: `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md` v1.2.
Candidate `6cacc808879dc9f8c5a01e18eca6a9ff38d94e7a`.

Bounded wire controls pass: **13 supplied tests PASS** (six report-index,
seven durable-job), and **8/8 independent controls PASS**. No new defect found
within these controls. P retained-repository composition, server expression
evaluation, clock/delay and concurrency remain unproven. No READY or full S4/S7
acceptance follows.

## Reproduction and source

```powershell
python org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_Y/probe_report_index.py --output org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_Y/REPORT_INDEX_6cacc80887.json
```

The probe imports the snapshot helper from the committed probe_recipe_decimal.py,
materializes exact Git blobs and records their SHA-256s. It runs actual boto
client calls with Stubber responses and the real FencedReportIndex and
DynamoGenerationStore. The underlying P index remains a Mock. The supplied
fixture checks that its raw index.publish is never called and all queued
responses are consumed. Socket connections are forbidden. Complete adapter,
adapter tests and durable-job source were read.

Source and supplied tests show an accepted composition/worker/fence/unexpired
lease condition plus CERTIFYING state on the job, combined with the original
immutable index item Put in one transaction. The duplicate path rechecks the
current lease and returns an existing receipt only after comparing tenant,
request revision, owner and ref. P remains responsible for deriving the expected
report ID and verifying the actual retained blob, schema, authorization and
expiry; this adapter is not an independent report publisher.

## Independent controls

| Control | Observation |
|---|---|
| Accepted composition changes before publish | ACCEPTED_COMPOSITION_MISMATCH; zero transactions |
| Lease expires at the exact current time | LEASE_LOST; zero transactions |
| Fence changes after successful transaction response | LEASE_LOST; one transaction already responded successfully |
| Lease owner changes during page lookup | LEASE_LOST; no result returned |
| TransactionInProgress with identical prior row and current lease | Original retained version returned; no raw fallback |
| Throughput error | Original error propagated; no duplicate lookup or raw fallback |
| Canceled transaction with no existing row | Original error propagated; no raw fallback |
| Mutable report receipt | REPORT_INDEX_BINDING before any wire call |

Counts are distinct denominators; no server behavior is inferred from the
Stubber accepting a request. In particular, the third control proves refusal
of the acknowledgement only. It does not undo an already successful index
transaction. The transaction's `:now` is captured from the client clock;
delayed-commit, expiry crossing and clock behavior require explicit integration
evidence, including whether a committed row remains readable after the caller
loses its lease. This is an outstanding proof obligation, not a reproduced
server failure in this review.

## Remaining proof

Compose this adapter with P's actual retained repository and demonstrate report
ID binding, protected original PDF and certification lineage, exact blob/version
read-back, authorization/schema/expiry checks and recovery around uncertain
transaction outcomes. Run the real concurrent-worker and delayed-commit cases
before any claim that stale publication is impossible. No such server, browser,
vendor/session, worker assembly or full end-to-end activity was performed here.
All fourteen integrated criteria remain NOT_EVALUATED. Evidence is LOCAL;
implementation sources were not changed by this reviewer.

-- 3.0.0_SA_CVO~Y
