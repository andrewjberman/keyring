# IRPT Y current status

Local accepted-custody consumer source `10627906f24aa42db4c08fd66105599f35bf7819` is ready for P integration and
CTO direct review under `999998e448`. Reader methods match P's implemented
interface; paired current P candidate `e36b007fa1a85414e8453608dc2803b8c947c290` retains the tested reader/store
runtime blobs. Handoff: `ACCEPTED_CUSTODY_CONSUMER_HANDOFF_20260923.md`.
Changed-file hashes and precise test boundaries:
`ACCEPTED_CUSTODY_CONSUMER_EVIDENCE_20260923.json`.

306 tests and 50 subtests pass across separately collected intake/generation
suites. Actual P reader/store plus Y factory/freezer/retention exercised with
synthetic economics, publication and storage. Current authorization, originals
before aggregation, selected fingerprint, retained provenance and replay checks
remain enforced. No current source capability or runtime activation established.

Next owner: P integrates/packages this source and returns one pinned candidate
for CTO review. Missing actual economic source facts still refuse. Y has not
changed shared schema, reader ownership, deployment, IAM or live service state.
Previous factory baseline819c and bounded package/runtime evidence remain in
prior handoff/evidence files and repository history; this replaces only the
current consumer-pending status.
