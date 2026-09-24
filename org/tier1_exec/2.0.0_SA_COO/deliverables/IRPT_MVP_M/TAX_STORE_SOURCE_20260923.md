# Bounded Tax disposition persistence candidate

Authority: exact CTO98209e201b module/test grant and215227 continuation. M owns only
the existing S3DispositionStore and necessary serialization helpers in
data/mdpf/scripts/gold/taxsma_membership.py, with its existing test file.
The grant was read at its committed pin. No new path grant was authored by M.

## Implemented

The existing constructor accepts an injected S3 client and bounded max_attempts
(default3). It derives the sole object from dispositions_address(), retaining the
canonical JSON-array history. Reads require non-null VersionId and ETag, validate
records and available SHA metadata, and expose last_receipt with exact object/version,
ETag, SHA256 and length. Missing key alone means no history; access errors and malformed
history propagate rather than becoming an empty success.

Append requires bucket versioning Enabled. Initial create uses IfNoneMatch:*;
update uses the just-read ETag in IfMatch. Only explicit conditional conflicts retry,
and only within the configured bound. Other failures propagate. Every successful PUT
is read back by its returned VersionId and must equal the intended bytes exactly.
An ambiguous write response is not blindly repeated: subsequent invocation reads
accepted history and deduplicates the logical observation.

Existing classification/emission/date-resolution functions and LocalDispositionStore
are unchanged. Same-observation contradictions are refused; late history emitted with
the existing order-conflict reason is retained without changing current membership.
If history advances underneath a caller and its pending late event lacks that reason,
append refuses and requires rebuilding from current history. Historical replays use
account/snapshot identity even when the preceding-event hash changed. Manual/legacy
events remain evidence only, never activation. FIRST_OBSERVED_UTC is not backdated.

## Discriminating evidence

`python -m pytest data/mdpf/tests/taxsma/test_taxsma_membership.py -q`
Result:36 passed in0.57s, including7 new injected-transport cases:

- create/update/restart, exact-version readbacks and exclusive inactive date;
- response lost after commit, and replay after newer observation, without duplicate writes;
- same-observation conflict and late retained history without rollback;
- two-account CAS race preserves both writers; perpetual contention exhausts bounded retries;
- suspended versioning, corrupt readback and access-denied each refuse;
- stale unflagged append refuses; manual replay is idempotent and non-activating;
- malformed existing history cannot become an empty current history.

These are source/persistence-protocol tests with an injected transport. No real S3
operation, vendor acquisition, gateway deployment or Holdings publication was executed.
No full Tax suite/round or scheduler was activated.

## Next owned work and actual runtime prerequisites

M next builds the narrow one-shot callable from the existing snapshot/Silver/membership
modules in TAX_BOUNDED_ACTIVATION_RECIPE_20260923.md@55145056df. Stop after the membership
receipt; no full consolidator/category publisher. A partial multi-account invocation is
recoverable by replay, but this single-object append API does not claim whole-snapshot
transactionality. Its caller must not publish a successful full membership result after
any append failure. Each invocation must consume the complete validated Silver census.

Existing gateway/runtime owners, coordinated by CTO, still owe the distinct canonical
capability route/secret binding assessment and exact authorized source invocation.
Runtime requires GetBucketVersioning on the resolved bucket; GetObject/GetObjectVersion
and PutObject only on the derived protected disposition object, with existing KMS controls
where applicable. The runtime SDK must support PutObject IfMatch/IfNoneMatch. Source
tests do not prove those installed capabilities. No missing permission is self-granted.
On a failed or ambiguous write, retain immutable versions; never delete or rewind history.

Real canonical workbook Bronze/Silver and history are still needed. The retained research
workbook envelope is not substituted. A first observation today cannot certify yesterday's
Tax membership. Canonical custody value is moved once from Client into SMAs/ALT Strategies/Tax
only for supported account/date membership; workbook AUM never supplies custody dollars.

Cottonwood remains the primary live thread: publication accepted9709e10c59; P's reader
cutover is pending. M's exact two-file manifest repair5c2773e97b unblocks the current
canonical build. Authenticated API/screen checks remain prepared at472f6f8c3a.
