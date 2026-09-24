# Accepted custody binding: implementation ruling

CTO, 2026-09-23. Local implementation authority under Andrew's delegated
worker-fork adjudication. Andrew's instruction that CTO is the reviewer remains
in force. This does not restart the held canonical rounds or authorize deployment.

## Decision and evidence

Adopt the private reader contract in P `f6babe048f`, incorporating M
`44e3a52fa3` and Y `605449f4cc`. Nested economic facts, one evidenced security
authority, exact original-row correspondence, and the separate source transport
and analysis bounds are settled for this tranche. Missing source declarations
remain missing; this ruling supplies no currency, sign, unit, cash, numeric
conversion, security mapping or empty-census evidence.

Direct source inspection at P `f0075287c4` establishes a usable implementation
base: `_scope/selection_store.py` has tenant-keyed conditional immutable records
in `IRPT_REQUESTS_TABLE`; `holdings/publication.py` already pins S3 object
versions/hashes and conditionally publishes an index; `holdings/snapshot.py`
currently resolves a date through the current index. That date lookup is not an
immutable historical binding. An existing accepted model/display publication
is also not proof of complete security-level actual custody.

P and M should now implement the private binding seam locally. Do not wait for
all three firms' economics to implement and test exact-reference storage and
refusal behavior. The production actual-custody callback remains closed until
the complete integrated candidate and real source capability are reviewed.

## One writer per surface

**P:** implement the trusted binding store and `AcceptedCustodyReader` under
`infra/aws/lambda/investor-reporting/_scope/`, with owned tests. Reuse the
configured `IRPT_REQUESTS_TABLE` and its existing key attributes. Reserve
`CUSTODY_BINDING#<server-generated snapshot id>` in `request_revision`, keyed
by the exact report firm in `tenant`; do not use the SELECTION namespace or a
new table. This is a private process record, not a new retained artifact family.
Use canonical JSON, an explicit byte cap no greater than the existing 300000,
conditional create, strong readback and exact idempotent equality. A conflicting
existing record must refuse, never overwrite. No browser-supplied reference,
storage key, economic declaration or source row may create a trusted binding.

The binding records a versioned private schema; firm and snapshot id; exact
selection reference/revision and selected account set; original full snapshot
revision; acceptance-index object reference and selected date row; manifest
reference; ordered source receipts; and revision references for account mapping,
security mapping and admitted economic/numeric policies. Include a digest of
the canonical record payload excluding its own digest. Missing required
evidence prevents an accepted binding. Current principal authorization must be
checked independently on every read, including recheck after source loading;
a historical record is not a perpetual permission grant. Return only the
approved private input to Y, never private provenance in public error envelopes.

**M:** extend only these existing backend source/test paths for exact publication
receipt capture and reading, in addition to the earlier four-file producer scope:

- `infra/aws/lambda/investor-reporting/holdings/publication.py`
- `infra/aws/lambda/investor-reporting/holdings/snapshot.py`
- `infra/aws/lambda/investor-reporting/holdings/tests/test_publication.py`
- `infra/aws/lambda/investor-reporting/holdings/tests/test_snapshot.py`

Expose a private pinned read/capture interface to P. Capture the observed index
VersionId, byte length and SHA-256 along with the validated date row and exact
manifest reference. Replay must read that exact index version and establish
that it accepted that exact manifest/revision/date, then read the pinned
manifest and selected partitions using existing validation. Preserve all
inventory/header validation and selected-account census checks. Never resolve
the current index or substitute its newer same-day publication on replay.
An orphan manifest, modified receipt, unavailable version, or incompatible
firm/date must refuse. Keep original snapshot identity distinct from selected
or decorated document bytes. Current-date loaders remain compatible.

M owns these publication/snapshot changes; P does not acquire their write
ownership or additional holdings Entry scope. P owns shared schema and package
integration. Share the concrete method signature once, then publish pinned code.

**Y:** consume the paired P/M private interface in the owned factory/freezer,
preserving the original-row eligibility check before aggregation and the current
positive-only recipe. Do not normalize away signed/zero/unknown originals or
invent missing economic facts. No public status/schema expansion. Identify any
actual signature mismatch with a minimal failing caller example; no further
parallel field-name proposals are needed.

## Three completion checks for this tranche

1. A server-authorized binding reads exactly the originally accepted source
   after a same-date publication changes; conflicting writes, orphan manifests,
   tampered hashes/versions, and stale or wrong-owner authorization refuse.
2. The actual Y consumer receives the paired reader output with exact original
   row coverage and private provenance. Unsupported or unproved originals refuse
   before aggregation; missing source capability cannot produce acceptance.
3. P provides one integrated pinned candidate, changed-file manifest and focused
   seam-test results for CTO direct review. Distinguish synthetic storage/source
   tests from actual source receipts and from any deployed/live evidence.

Existing source-only restrictions continue: no producer invocation, cloud
read/write, new IAM resource, vendor call, runtime attachment or promotion is
authorized here. Missing upstream facts should be reported as a single concrete
capability gap with the exact field and source, not repeatedly recirculated
contract prose. Firm browsing/bootstrap remains a separate completion slice;
actual-custody admission must not be claimed from its success.
