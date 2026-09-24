# CTO direct review: bounded Tax disposition store

Candidate d3a8c3e7e34a7c8769f916385b9057c3359f4406. Bounded source PASS.
CTO read the exact module delta, tests and source handoff. Only the granted
production store and its serialization helpers changed; classification, date
resolution and original LocalDispositionStore business rules are unchanged.

Exported candidate source, tests, Silver dependency, lib, naming registry and
standards into C:/Users/ANDREW~1/AppData/Local/Temp/irpt-cto-tax-d3a8-wbqrdrjo.
Executed pytest data/mdpf/tests/taxsma/test_taxsma_membership.py -q -k s3_history
--rootdir=. --confcutdir=. with plugin autoload and metadata access disabled.
Seven affected cases PASS in 0.12s; 29 unrelated cases deselected.

Evidence covers conditional initial create and ETag update, exact-version readback,
restart, lost response replay, historical replay after a newer event, observation
conflicts, late flagged history, competing accounts and bounded CAS exhaustion,
unversioned/corrupted/denied reads, stale unflagged append refusal, inert manual
history, and malformed-history refusal. Source verifies canonical address derivation,
non-null versions, optional metadata digest checking and full byte readback.
Only explicit conditional conflicts retry. Other transport failure propagates.

These are injected-transport tests, not a live S3 receipt or gateway run. The store
is single-object append persistence, not a transaction over the whole snapshot.
Caller must stop on any failed append and replay idempotently; it cannot advertise
complete snapshot membership after a partial failure. No historical backdating or
research-envelope conversion. Current source dates must retain canonical observed-at
semantics; a first observation today cannot establish yesterday's membership.

M proceeds with the already-authorized one-shot runner reusing canonical gateway,
snapshot and Silver modules. Return exact capability/secret binding, complete source
census, derived storage addresses, SDK conditional-write support and minimal runtime
permission/rollback/readback plan for execution adjudication. No vendor acquisition,
cloud write, scheduler or full Tax consolidation is authorized by this source review.
COT Holdings remains dependent on P's current reader cutover and actual API/browser
proof. All three IRPT products remain incomplete.
