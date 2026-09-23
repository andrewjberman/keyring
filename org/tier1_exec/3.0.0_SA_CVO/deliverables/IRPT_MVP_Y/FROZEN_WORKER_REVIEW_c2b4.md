# Frozen worker preparation independent review

Reviewer `3.0.0_SA_CVO~Y`, 2026-09-23 UTC. Authority:
`org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md`.
Exact candidate: `c2b467fa474d6e8ffb2b3ac6b26c41ddd0850b28`.

**Bounded PASS:26 independent controls and49 supplied tests PASS.** No reproduced
defect within the read-only frozen-consumer boundary. Driver:
`probe_frozen_worker_c2b4.py`; complete controls, exceptions, source SHA256 values
and supplied output: `FROZEN_WORKER_c2b467fa.json`. Run the driver with Python
from the repository; it archives the exact candidate and blocks network sockets.

The review exercises actual FrozenCompositionWorker, OwnedRequestReader,
DynamoAcceptance, DynamoGenerationStore, CompositionAdmission, retained artifact
repositories, normalized upload preparation and recipe generation_body. Canonical
source readers, S3/Dynamo transaction effects and an already-acquired lease row
are synthetic. It does not execute a lease acquisition or prove atomicity/races.

## Independent evidence

One positive control verifies exact recipient and six frozen source descriptors,
profile/provenance, settings and normalized upload12.03. Optional phone remains
null in retained profile and becomes an empty cover string. Clearing live source
and settings objects, poisoning resolver calls, then mutating every returned
nested surface does not change the next preparation. Acceptance/retention rows
and S3 write count remain unchanged; job update is never called, state RECEIVED.

Eight early controls refuse wrong principal/tenant/request/composition, changed
fence/lease owner, exact lease deadline and missing claim before any blob fetch.
Eight late controls mutate state after actual upload preparation and before final
checks: principal grant, fence, lease owner, lease deadline, job composition hash,
accepted record, policy state and retention service. All refuse without writes.

Two adapter fault controls preserve a real artifact read then alter returned
composition or normalized-input bytes; both refuse. Five authentic stored rewrite
controls use real repository writes for the attack fixture: missing declared
source dependencies, missing recipient, recipient mismatch, changed browser token
with matching digest, and changed settings. All refuse preparation. The browser
token case reaches the derived accepted-request ID binding; the dependency case
reaches FROZEN_WORKER_SOURCE_DEPENDENCY_MISSING.

One additional late control injects a refusal for a single retained source after
upload preparation. The final recursive retention check propagates that refusal.
This is an injected source-grant response, not a live IAM or directory revocation.
One actual generation_body control verifies exact recipient duplication across
outer and nested cover fields using a synthetic Overview template/primary ID.

The supplied49tests cover test_frozen_worker.py, test_composition_admission.py
and test_normalized_input.py at the same pin. Counts are separate from the26
independent controls; no producer-only result is folded into the verdict.

## Limits and next evidence

This stage has no session/vendor/queue ports, writes no job state, and returns no
READY claim. The effecting caller must repeat current preparation and acquire the
durable mutation intent before transport. No guarantee is made about access or
lease changes after this read-only function returns.

The positive fixture is prospect Overview with no comparisons. Actual custody
economics, selected-comparison entitlement, canonical installed source readers,
current vendor template/settings admission and vendor readback remain separate.
Cover field equality proves neither hostile-text rendering safety nor a rendered
PDF. No browser/export/runtime/package/cloud/deploy or physical-disposal grade.
No implementation edits by the reviewer. All14 integrated criteria remain
**0 PASS /0 FAIL /14 NOT_EVALUATED**. Push state LOCAL.
