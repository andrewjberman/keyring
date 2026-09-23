# Accepted custody reader: exact interface draft

Status: LOCAL P/M/Y CONSUMER COMPOSED; INTEGRATED REVIEW PENDING.
Measured source `e3ad48ca23` includes Y consumer `10627906f2`; source package
closure and extracted Linux factory construction pass. Exact source/archive
hashes and composed control are in `ACCEPTED_CUSTODY_PACKAGE_EVIDENCE_20260923.json`.
CTO ruling `999998e448` authorizes this local tranche. P `00b54afab1` implements
the private store/reader; `c607ee7461` records 115 passing offline seam tests.
Integration `515fba746a` includes M's wording-only correction `200ba442f5`.
Economic ports in the successful storage tests are synthetic. Actual source
admission, a production installation and deployment permission are not proved.

Paired review incorporated: Y `ff982c0e3012c611d96f3ef5b0ac541dbb0ed11d`
(includes `605449f4cc`, supersedes `b799b5a6fc`),
`IRPT_MVP_Y/ACCEPTED_READER_REVIEW_20260923.md`; M
`44e3a52fa3353ea94b3a473547efef77847e0d52`,
`IRPT_MVP_M/ACCEPTED_READER_FIELD_REVIEW_20260923.md`. Both preserve the methods
below. P adopts M/Y's nested economic facts and 1100-character transport limit
for this paired interface draft, with Y's canonical security-key and actual
mapping-receipt requirements in the one nested security object. Source facts
and a trusted binding are not supplied by a field definition. This revision
supersedes `7e9baf3064` and the crossed flat-field proposal in `34a9c33800`.
The selected fingerprint and retained-source mapping below correct the omission
in `f6babe048f`. The implementation status above supersedes the original draft's
absent-store statement; the economic requirements below remain mandatory.

## Measured boundary

P baseline `f0075287c426cbe9eea04f0165bc179147918ce1` has mandatory factory
ports `authorize_snapshot(principal, owner)` and
`load_normalized(browser, principal, owner)`. `CustodyAccess.current()` rebuilds
the selection owner before and after snapshot authorization. The factory checks
the returned frozen document's owner, snapshot and account IDs and reauthorizes
before retaining it. These guards do not manufacture an accepted source.

CTO notice 20260923T155646 reports direct review at `1ada74ee5c` of M source
`b3e63a795e0b8c7399619dbc545745786add4eb7`: 114 tests PASS, local guard only.
P has read the notice and source diff stat; P has not independently rerun that
suite. M's private evidence and optional expected raw account IDs are not
independently authorized census. Audited COT currency remains unestablished.
Empty inputs refuse; no accepted complete empty-account census capability exists.

## Implemented export and consumer composition

P owns `_scope/accepted_custody.py` with these internal methods:

```python
class AcceptedCustodyReader:
    def __init__(self, store, *, current_selection, publication_for,
                 interpret_source=None, validate_evidence=None): ...
    def create(self, principal, selection_owner, *, as_of) -> dict: ...
    def authorize_snapshot(self, principal, owner) -> bool: ...
    def read(self, principal, owner) -> dict: ...
```

`read` either returns the closed `AcceptedCustodyInputV1` below or raises the
existing custody permission refusal. `authorize_snapshot` performs the same
binding/current-authority checks and returns literal True only on success.
Neither method accepts browser rows, raw account mappings, bucket/key, dates as
lookup substitutes, or a caller-provided manifest. The installation is a
request-local server configuration; no warm caller's identity is retained.

`create` generates the snapshot ID on the server, captures the exact M
publication receipt and conditionally persists the immutable private binding.
No HTTP writer is installed. `current_selection(principal, owner)` must resolve
the current verified selection fingerprint. `publication_for(firm)` supplies
M's capture/load_pinned service. Both economic callbacks are mandatory for a
successful create/read; missing capability refuses. Their production source
implementation and the canonical selection adapter remain integration work.

Y supplies the existing factory callback:

```python
def load_normalized(browser, principal, owner):
    accepted = reader.read(principal, owner)
    # Verify exact browser selection/snapshot equality, then evaluate every
    # original row's recipe prerequisites before any aggregation or freezing.
    # Emit one money row per admitted economic position, not per relationship.
    # Return existing verified frozen-portfolio envelope; otherwise refuse.
```

No change to `build_custody_entry(**ports)` or its existing callback signature
is proposed. M's pure `validate_cot_actual_positions` stays a source validator;
its DataFrame/private evidence is never this accepted result or factory input.

## AcceptedCustodyInputV1 (internal, not a new HTTP response)

Exactly these top-level fields are proposed:

| Field | Type and meaning |
| --- | --- |
| `schema_version` | literal `accepted-custody-input-v1` |
| `owner` | exact existing `custody-owner-v1` object; current account set and revisions |
| `snapshot_id` | exact owner snapshot ID |
| `snapshot_revision` | digest of the original complete accepted snapshot bytes, never a selected projection hash |
| `binding_revision` | immutable accepted binding record digest, covering ordered receipts and canonical account mapping |
| `selected_account_set_fingerprint` | exact fingerprint from current verified `_scope/selection.py` selection result, bound to this accepted result |
| `actual_custody` | selected-only economics/census/reconciliation shape below |
| `original_rows` | one normalized evidence row per original selected-account economic row, before collapse |

All original rows must be represented, including relationship duplicates, zero
and negative values. No target/model/allocation positions replace actual rows.
Each original row has exactly `account_id`, `position_id`, `source_security_id`,
`market_value`, `quantity`, `source_row`, `economic_facts`.
`source_row` is singular `{source_receipt_id, row_index, relationship_id}`;
positions retain plural `source_rows`. Both original and unique positions carry
the resolved economics/security below; duplicates must agree across all consumed
economic and identity fields. Row-level evidence references can differ because
the physical origins differ.

Every original receipt/row pair occurs once in `original_rows`, belongs to exactly
one position, and the union of positions' provenance equals the original set.
Reuse from an original into its position or economic evidence is expected and
is not a duplicate-input error. No orphan, omitted, extra or multiply assigned
original is allowed. This corrects the earlier blanket duplicate-reference rule.

## Immutable binding requirements

1. Resolve `(report firm, snapshot_id)` only through a server-controlled accepted
   binding. P implements the local conditional store/reader under ruling999998;
   M implements exact publication capture/replay. Absent binding means refuse.
   Never fall back to
   a date's current index, newest object, browser manifest or unversioned key.
2. The binding must pin original snapshot revision, exact canonical account
   census/mapping revision, source-set revision and ordered immutable receipts.
   Each receipt binds exact object/version/byte SHA256, source role, firm scope
   and the evidence for account coverage. All locations/raw IDs remain private.
3. P issues opaque scoped `source_receipt_id` values in that binding; they are
   immutable references, not array indexes. Changing receipt order, bytes,
   version or account mapping changes the binding revision. Multi-file row zero
   is distinct per receipt. Duplicate original entries or assignment of one
   original to multiple positions refuse; legitimate cross-structure references
   to the same original remain required.
4. Read the exact pinned bytes and verify hashes/versions before parsing. Preserve
   per-object physical row ordinal before filtering, sorting or concatenation.
   Validate raw-to-canonical mapping and exact requested account coverage using
   independently authorized current selection/census, not equality of two
   potentially incomplete input frames.
5. Validate currency, source completeness, same-vintage independent account
   totals and source economics. Build selected-only opaque provenance; do not
   copy M's private `actual_custody_controls`, raw IDs or object locations.
6. Recheck current principal/home/report firm, selection, directory/entitlement
   revisions and exact binding before returning. Revocation or changed owner
   refuses. The factory's later release checks remain necessary.

The binding digest also covers the admitted economic policy/version, exact
security resolution and raw-to-canonical mapping evidence, numeric column
interpretation and selected binding semantics. Opaque receipt IDs only resolve
inside that bound scope and source role. A selected old snapshot never advances
silently to a later publication. Its current authorization is a separate check.
Both snapshot and binding revisions, and relevant opaque receipt references,
must survive normalization/retention using the mapping below. No new artifact
family is proposed.

The selected fingerprint comes from `resolve_selection(...)._view` under current
verified scope: canonical account IDs, entitlement revision, viewer policy and
verified request firm. It is NOT the owner's `ownership_fingerprint`, the
permitted-account fingerprint, account_set_id or an ad hoc account-list digest.
The reader must bind and recheck this exact selection result before return and
release; current `CustodyAccess` owner alone does not carry it. Reader
implementation must obtain it through the canonical verified selection path.

## Retained source projection for the new accepted-reader branch

Y's proposed projection is adopted into this interface specification:

| Normalized document.source member | Exact value |
| --- | --- |
| `lane` | `CUSTODY` |
| `source_revision` | accepted.snapshot_revision, the original complete snapshot digest |
| `selected_set_fingerprint` | accepted.selected_account_set_fingerprint |
| `as_of` | accepted.actual_custody.custody_as_of, after the admitted valuation-date rule passes |
| `account_ids` | sorted exact accepted.owner.account_ids |
| `snapshot_id` | accepted.snapshot_id, equal to owner and browser snapshot IDs |
| `accepted_custody` | full deep copy of the selected-only closed AcceptedCustodyInputV1 |

The embedded contract retains owner, both revisions, selection fingerprint,
economic facts, originals, positions, census/reconciliation and scoped opaque
receipt references. No raw account/storage IDs or private DataFrame are copied.
All duplicate outer/embedded fields must match exactly; rehashing a substituted
owner, snapshot, binding or selected fingerprint cannot establish acceptance.
Validate the same embedded contract and current authority at retained replay;
never reload a newer source to reconstruct the old evidence.

Source inspection at P's unchanged runtime baseline confirms
`intake/portfolio.py:_source` deep-copies CUSTODY source, requires
source_revision/selected_set_fingerprint/as_of and validates/sorts account IDs.
This is structural preservation, not validation of this new embedded contract.
Y's future adapter/replay path must enforce its full semantics; the existing
freezer hash and NORMALIZED_PORTFOLIO reference retain the resulting exact bytes.
Existing historical documents and other source lanes are not reinterpreted.

Preserve every original relationship row inside source.accepted_custody, but
emit exactly one money row per admitted economic position only AFTER original
eligibility, complete correspondence and duplicate-fact equality checks. Retain
its position_id and source_rows in contribution provenance. Existing subsequent
same-security aggregation may then combine these economic contributions. Two
equal relationship rows of 100 produce one contribution of 100, never 200.

## Agreed mapping and remaining choices

`actual_custody` uses M's envelope names: `schema_version`, `firm_id`,
`custody_as_of`, `valuation_as_of`, `account_ids`, `positions`, `census`,
`reconciliation`. `account_ids` equals the owner's canonical selected set.

Positions preserve stable source-grain `position_id`, canonical `account_id`,
`source_security_id` (`namespace`, `value`), signed decimal-text `market_value`
(`value`, authoritative `currency`), nullable `quantity` (decimal-text `value`,
explicitly sourced `units: SHARES`) and `source_rows`. Provenance is scoped
`source_receipt_id`, integer `row_index >= 0`, nullable `relationship_id`.
Relationship identifiers must be scoped opaque identifiers if exposed outside
the private reader. The private-account-ID prohibition does not remove the
instrument identity required by `source_security_id`: use scoped vendor identity
inside this internal boundary, or a bound opaque instrument reference when raw
spelling cannot leave the reader. Neither form is a canonical security resolution.

### Resolved facts and private source evidence

`economic_facts` has exactly the five M/Y nested members below. EvidenceRef is
`{source_receipt_id: string, row_index: integer >= 0}` inside the exact binding.
Source-field names identify columns, not storage locations. Null preserves an
unknown observed fact; an unknown required interpretation cannot pass acceptance.

| Field | Required interpretation |
| --- | --- |
| `cash` | `{source_field: string|null, source_value: boolean|null, classification: CASH|CASH_EQUIVALENT|NON_CASH|null, evidence: EvidenceRef[]}`; classification requires bound interpretation; a Cash Equivalent flag alone proves neither literal cash nor blanket NON_CASH |
| `side` | `{source_field: string|null, source_value: string|null, position_side: LONG|SHORT|null, sign_rule_revision: string|null, evidence: EvidenceRef[]}`; absent source side may use an exact admitted signed-value rule, never fabricated LONG/NOT_APPLICABLE or a second application of sign |
| `security` | `{resolution_revision: string|null, resolved_identifier: {namespace: string, value: string}|null, evidence: EvidenceRef[], security_key: string|null, resolution_source_receipt_id: string|null}`; this is the sole canonical resolution authority; absent/ambiguous required mapping refuses |
| `source_quantity` | `{value: decimal-text|null, source_field: string|null, source_units: string|null, unit_rule_revision: string|null, evidence: EvidenceRef[]}`; retain signed native quantity even when SHARES interpretation is unavailable |
| `accrual` | `{treatment: INCLUDED_IN_MARKET_VALUE|EXCLUDED_FROM_MARKET_VALUE|null, value: decimal-text|null, unaccrued_market_value: decimal-text|null, rule_revision: string|null, evidence: EvidenceRef[]}`; COT MV = UMV + Accrual, included once; other treatment requires its actual admitted source equation |

The binding must resolve the exact economic interpretation revisions and
underlying source evidence, including supplied native USD value basis. Policy
revision labels cannot be invented by the reader. This first adapter uses
native signed dollar value, never reconstructed share-price value or notional;
no parallel `value_basis` alias is added to rows. A null side is usable only
when its bound sign rule independently establishes all necessary semantics.

The top-level `quantity` is SHARES only when the exact asset/source unit rule
establishes it. Preserve supplied native quantity in `source_quantity` even when
that rule is unavailable; null SHARES must not erase a negative native quantity.
Missing mandatory unit/sign interpretation refuses accepted input. Absent
quantity may be permitted only by an explicit admitted native-USD policy; no
zero is fabricated. Y must evaluate native quantity sign before aggregation,
check correspondence with resolved quantity where supplied, and reject negative
quantity or SHORT for the present recipe even with positive MV. Zero quantity
does not by itself establish cash or zero value.

The nested security member projects to existing Y canonical fields without
inference: `identity_kind: CANONICAL_SECURITY`, `security_key`,
`canonical_identifier = resolved_identifier.value`,
`canonical_identifier_namespace = resolved_identifier.namespace` (restricted
to `TICKER`, `CUSIP`, `CASH`) and `resolution_revision`. No parallel top-level
`security_resolution` exists. `resolution_source_receipt_id` must identify actual
admitted immutable mapping evidence, not a fabricated ticker crosswalk. CASH
requires `$:CASH` and sourced CASH classification; CASH_EQUIVALENT keeps its
actual resolved instrument. Conflicting keys/identifiers or unavailable required
evidence refuse. Unknown resolved facts never become default enums.

### Numeric transport versus recipe eligibility

ASCII string-only grammar, matched as a whole string:

```text
[+-]?(?:[0-9]+(?:\.[0-9]*)?|\.[0-9]+)(?:[eE][+-]?[0-9]+)?
```

Paired source-evidence cap: 1100 characters,
1000 Decimal coefficient digits, absolute Decimal exponent <= 1000, finite.
Y `605449f4cc` accepts M's 1100 in place of its earlier 2048. This is not an
assertion of measured vendor precision. Parse directly as Decimal. No whitespace,
JSON numbers/bools, separators, nonfinite values, rounding, quantization, float
conversion or scale stripping to fit. Preserve signed zero/trailing scale.
M's stricter float-finiteness guard remains unchanged and is not overridden.
Use exact arithmetic with explicit sufficient precision for exponent alignment
and the actual bounded row count; detect inexact/rounded operations and refuse.
Neither caller-default Decimal context nor an unbounded row population is valid.

Pin each consumed column's Arrow type, precision/scale when declared, schema
receipt and numeric interpretation revision privately in the immutable binding.
Binary-float shortest-string conversion is not exact vendor-decimal recovery;
absent an admitted conversion/precision rule, refuse that numeric source. String
sources require an admitted grammar; no invented p/s or monetary-unit inference.

Y's existing dollar analysis domain stays strictly positive, <= 28 coefficient
digits and absolute exponent <= 18, evaluated on every original before collapse.
The normalized output/upload bounds stay 128 characters, 80 digits and absolute
exponent <= 80. Source acceptance cannot widen either consumer domain. Aggregated
values must satisfy those bounds exactly. Independent account tolerance of 0.01
does not authorize approximate duplicate equality, row rounding or changed sums.

Per-account census fields: `account_id`, `raw_row_count`,
`unique_position_count` (integer or null on invalid collapse),
`duplicate_relationship_row_count`, `unsupported_original_row_count`,
`conflict_original_row_count`, `completeness`, `empty_account_evidence`.
Raw counts include every original row. Unsupported counts original MV <= 0,
including repeats; conflict counts every member of a conflicting account/asset
group. Diagnostics overlap. Duplicates require equality across ALL consumed
fields. `raw = unique + duplicate` holds only for valid complete collapse.
Unknown/unmapped/conflicting source data cannot be accepted. Completeness
describes custody observation, not vendor eligibility; complete signed data
may remain recipe-ineligible. Proposed COMPLETE/UNAVAILABLE/INCOMPLETE values
are not yet adopted public schema enums.

Per-account reconciliation: `account_id`, decimal-text `position_value`,
`independent_value`, `absolute_difference`, `tolerance_usd: "0.01"`,
authoritative `currency: "USD"`, `custody_as_of`, `valuation_as_of`,
`independent_source_rows`. Evaluate the signed native position sum, including
native accrual exactly once, against the independent same-date USD account
total. Absolute difference must be <= 0.01. No inferred USD, conversion, netting
to positive or unknown components. Exact value-fact evidence must establish
native accrual treatment rather than assuming it from a field label.

`empty_account_evidence` is null or exactly:
`position_census_receipt_id`, `independent_source_rows`, `position_count: 0`,
`independent_value` (exact zero decimal text), authoritative `currency`,
`custody_as_of`, `valuation_as_of`. The census receipt must prove complete
selected-account zero enumeration, and independent rows separately prove the
same-date zero total. No fabricated physical row is required in an empty source;
no rows/missing partition or zero net value alone establishes this proof. This
capability is currently unavailable, so actual empty inputs continue to refuse.

## Review examples and implementation gates

| Input | Census/value outcome | Admission implication |
| --- | --- | --- |
| Two equal relationship rows of 100 | raw 2, unique 1, duplicate 1, value 100 | Still requires independently authorized census, receipts and reconciliation |
| Distinct +100/-25/0 | raw 3, unique 3, unsupported 2, value 75 | Can be complete custody; current vendor recipe refuses originals |
| +25/-25 | raw 2, unique 2, value 0 | Not an empty account; recipe refuses |
| Same-grain 100/101 conflict | raw 2, unique null, conflict 2 | Refuse; no forced raw-count equation |
| No rows, independent zero total only | No complete zero-position proof | Refuse |
| No rows plus both exact empty proofs | All counts 0 | Valid custody in principle; current empty-portfolio recipe still refuses |
| Account missing from both frames | Expected census not covered | Refuse |
| Unknown currency | No currency substitution | Refuse |
| Different objects, each physical row 0 | Distinct immutable receipts | Keep both distinct; duplicate original entry refuses |
| Original receipt reused in its position | Expected correspondence | Allow; reject assignment to a second position |
| Negative native quantity, positive MV | Preserve sign even without SHARES | Current recipe refuses; missing unit policy also blocks accepted input |
| Positive positions omit a negative original | Broken complete correspondence | Refuse |
| Cash label conflicts with canonical security | Inconsistent admitted facts | Refuse |
| 29-digit dollar or exponent 19 | May fit source transport | Current Y analysis refuses without normalization to fit |
| Changed policy/mapping/binding revision | Exact evidence mismatch | Refuse |

## Concrete source blockers, with owners

| Blocker | Current evidence and owner |
| --- | --- |
| Trusted accepted binding writer/store/read surface | P local implementation00b54afab1 and real M replay integrated515fba746a; 115 offline tests. Production adapters/installation remain absent |
| Economic interface versus actual evidence | Nested names and 1100 text cap aligned with M44e3/Y6054; admitted rules and actual evidence remain absent; Y's security key/receipt additions require concrete maintained mapping |
| COT source contract | M source review: B01 has no currency/side declaration, Cash Equivalent is insufficient, Units is not universal SHARES; adding Currency would require a source-map amendment, not a helper default |
| INF source contract | M source review: optional facts, missing stable mandatory instrument grain/currency/side; builder zero accrued income is not vendor economic proof |
| 49F source contract | M source review: l_s exists but signed-value rule, security-join uniqueness, cash non-overlap, currency/units and pending accrual ruling remain unresolved |
| Current numeric schema and security mapping receipts | Not supplied by either review; P cannot invent a receipt or conversion policy; M identifies source capability, CTO adjudicates needed source interpretation |
| Empty-account census | No admitted complete-zero receipt capability; actual empty inputs refuse |
| Retained revision/provenance implementation | Y10627906f2 implements adapter/embedded semantic validation/reconstruction; composed source e3ad48ca23 tested with actual M/P/Y code and synthetic evidence. Integrated review pending |

These are source-located findings from the exact M review, not fresh cloud
measurements. No producer execution or new source-read authority is inferred.
The local binding mechanism and Y consumer are composed. Next obtain integrated
review and prove actual economic source evidence separately; storage success does not
supply that evidence. CTO remains direct
reviewer. No cloud write, production source activation, IAM change, vendor
request or public field emission follows from this draft.
