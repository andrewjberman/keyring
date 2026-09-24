# CTO direct review: Y accepted-custody consumer

Source `10627906f24aa42db4c08fd66105599f35bf7819`; evidence handoff
`63d5727e89`; paired P reader/store/test support extracted from
`e36b007fa1a85414e8453608dc2803b8c947c290`.
Reviewer `1.0.0_SA_CTO`, per Andrew; authority `999998e448`.

**Bounded PASS for local Y consumer integration with the P reader.**
All five handoff file hashes and Git blob identities match exact committed bytes.
Read the complete added consumer, both source changes and added tests. The
consumer preserves the full selected private evidence, checks every original
before collapsing relationship duplicates, checks census/reconciliation and
maps one contribution per economic position into the existing freezer. Replay
rebuilds this branch from retained evidence and compares the normalized document.
The factory binds one supplied reader to authorization and normalization ports;
no production default is installed.

## Direct execution

Isolated Y source archive, with repository dependencies from the same source pin:
`C:/Users/ANDREW~1/AppData/Local/Temp/irpt-cto-consumer-ae42d28b7a47416b9ab873241049cc2b/source`.
`IRPT_ACCEPTED_READER_TEST_ROOT` points to sibling `reader/`, containing the exact
P `accepted_custody.py`, `custody_binding.py` and `test_custody_binding.py` Git
bytes from the paired pin. No source or test changes were made.

Separate processes, avoiding the reported cross-directory fixture collision:

```text
python -m pytest infra/aws/lambda/investor-reporting/intake/tests -q -p no:cacheprovider --tb=short --maxfail=3
94 passed, 18 subtests passed in 1.06s; exit 0

python -m pytest infra/aws/lambda/investor-reporting/ycharts/generate/tests -q -p no:cacheprovider --tb=short --maxfail=3
212 passed, 32 subtests passed in 16.41s; exit 0
```

Total: 306 tests and 50 subtests; no skipped paired-reader tests. This includes
actual P reader/store feeding Y normalization, guarded factory, exact retained
bytes, retry and revoked-capability refusal. These paired tests supply synthetic
publication, economic evidence and current-selection authority. Actual M replay
was exercised separately through P in review `d8d88388ab`; it was not the
publication implementation inside these Y paired tests. Do not sum these results
into a claim that one real-source, packaged, deployed end-to-end thread passed.

## Next integration and acceptance boundary

P may integrate Y's five-file pin and must include flat `custody_portfolio.py`
alongside the changed `portfolio.py` and `custody_submission.py` in its package.
Next handoff should pin the integrated source and exact archive/member hashes,
with the previously requested committed-byte manifest correction. Exercise the
actual packaged imports and a single composed M-publication/P-binding/Y-consumer
path using synthetic storage if necessary, explicitly distinguishing that test
from economic source admission. Do not replace M's publication reader with a
SimpleNamespace in that composed-path proof.

Missing source interpretation, receipt authority, admitted economic validation
and real current-selection configuration remain blocking for activation. Keep
those ports absent/refusing. Same-day-only dates, 10000-row caps, explicit accrual
arithmetic, positive-only originals and no native-unit conversion are disclosed
conservative limits; this verdict does not turn them into upstream source facts.
No cloud write, vendor call, attachment, deployment or full-product completion is
authorized or established here.
