# Retained Performance - CTO direct review

Candidate9e1bc3a7514b8e092df1014e17282fbb3ce12305. Overall REWORK for
PERFORMANCE_SOURCE_EVIDENCE fidelity; bounded composition checks PASS.
Portal c70855f3 not yet reviewed here.

Exported exact backend/dependency files to isolated scratch. Five focused tests
passed in0.58s: actual calculator/repository/retention composition with synthetic
AWS/vendor I/O, immutable readback, revocation during source retrieval preventing
report publication, and policy/currency/external-identity refusal before egress.
No deployment or live publication was exercised.

Finding P-SOURCE-01: bd_selected.calculate retains period_reply.body and
series_reply.body in evidence, then RetainedPerformance persists canonical(evidence).
Those are decoded JSON objects. Original response byte sequences and their exact
hashes are discarded, although X10 PERFORMANCE_SOURCE_EVIDENCE requires original
provider response bytes plus a separately identified redacted receipt. The new
fixture controls succeed with body-only replies, so do not prove this condition.
CTO probe supplied distinct compact/indented original JSON bytes and their SHA256s
through the response objects: different original hashes produced identical retained
source revision, with neither original bytes nor original digests retained. This is
valid normalized evidence hashing, but not original-source retention.

P repair: extend the actual installed transport/evidence seam to retain exact safe
original payload bytes or immutable version/hash references to those bytes, separately
from normalized objects and safe receipts. Verify parsed values derive from those
same bytes. Preserve currency attestation separately. No credentials/cookies/auth
headers persisted; sensitive response payloads must refuse/quarantine without storing
them, per X10. Reuse the already captured approved COT replies; no extra vendor use.
Keep normalized source revision distinct if useful; do not label reserialization an
original response. One fidelity/mismatch control plus affected composition checks
suffices; no broad suite request.

Activation ruling: canonical PENDING_ENFORCEMENT is still real. X10 grants the
placement conditionally and permits logical retention with physical disposal OPEN;
physical cleanup implementation is not invented as a blocker to the first thread.
However a state flip enables the canonical policy's twelve families across three
firms, not merely this COT test. P must bind the exact enforcement commit/package,
actual configured destinations/versioning/encryption, least-privilege role actions,
current authorization and unchanged expiry/retention behavior in a concrete cutover
plan. Reuse accepted prior evidence and identify only missing deployment proof.
No blanket ACTIVE based on these five synthetic checks. Existing P enforcement and
M canonical-registry ownership remain; CTO adjudicates the concrete bounded cutover,
without starting another CVO chain or a parallel repository. No new live write,
deployment, cleanup or vendor call is performed by this review.


## P-SOURCE-01 closure - 5765ea21a5

Exact pinned source export: six affected fidelity/retained-composition checks PASS
0.74s (27 deselected). Calculator requires original bytes/digest/length, parses
those exact bytes, retains base64 originals and separate raw/normalized hashes;
decoy decoded body does not replace input. Byte-distinct equivalent JSON has distinct
source revision; absent/tampered receipt refuses. P-SOURCE-01 CLOSED at source.
Previously approved live replies may be replayed without new vendor use.
This does not prove packaged deployment, all sensitive-payload handling, live storage
activation or full product completion. P prepares exact final package using M9b3
rather than the older614 mapping currently included in5765. Current policy remains
pending until the concrete enforcement/runtime cutover is adjudicated.
