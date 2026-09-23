# Accepted custody reader: exact interface draft

Status: LOCAL DRAFT FOR M/Y CONTRACT REVIEW. This document adds no runtime,
schema fields, storage authority, producer acceptance or deployment permission.

Paired review incorporated: Y `b799b5a6fc`,
`IRPT_MVP_Y/ACCEPTED_READER_REVIEW_20260923.md`; M
`44e3a52fa3353ea94b3a473547efef77847e0d52`,
`IRPT_MVP_M/ACCEPTED_READER_FIELD_REVIEW_20260923.md`. Both preserve the methods
below. P proposes Y's resolved economic fields plus M's native quantity evidence,
and the stricter 1100-character transport limit. These two choices still need
consumer/producer agreement; source facts and a trusted binding are not supplied
by a field definition. This revision supersedes the field placeholders in
`7e9baf3064`.

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

## Proposed export and composition

P owns proposed `_scope/accepted_custody.py` with these internal methods:

```python
class AcceptedCustodyReader:
    def authorize_snapshot(self, principal, owner) -> bool: ...
    def read(self, principal, owner) -> dict: ...
```

`read` either returns the closed `AcceptedCustodyInputV1` below or raises the
existing custody permission refusal. `authorize_snapshot` performs the same
binding/current-authority checks and returns literal True only on success.
Neither method accepts browser rows, raw account mappings, bucket/key, dates as
lookup substitutes, or a caller-provided manifest. The installation is a
request-local server configuration; no warm caller's identity is retained.

Y supplies the existing factory callback:

```python
def load_normalized(browser, principal, owner):
    accepted = reader.read(principal, owner)
    # Verify exact browser selection/snapshot equality, then evaluate every
    # original row's recipe prerequisites before any aggregation or freezing.
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
| `actual_custody` | selected-only economics/census/reconciliation shape below |
| `original_rows` | one normalized evidence row per original selected-account economic row, before collapse |

All original rows must be represented, including relationship duplicates, zero
and negative values. No target/model/allocation positions replace actual rows.
Each original row has exactly `account_id`, `position_id`, `source_security_id`,
`market_value`, `quantity`, `source_row`, `economic_facts`, `security_resolution`.
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
   binding. The concrete lookup/store and publication writer are NOT implemented
   or authorized by this draft. Absent binding means refuse. Never fall back to
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
must survive normalization/retention. The precise existing source/provenance
extension for that is still a P/Y schema task; no new artifact family is proposed.

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

P proposes Y's closed `economic_facts` names with one M evidence object:

| Field | Required interpretation |
| --- | --- |
| `cash_classification` | `CASH` or `NON_CASH` from admitted source interpretation; a Cash Equivalent flag alone establishes neither literal cash nor a blanket NON_CASH default |
| `position_side` | `LONG`, `SHORT`, or `NOT_APPLICABLE`; every value requires a bound sign rule, including absence of a vendor side column; never apply an already supplied sign twice |
| `value_basis` | literal `SIGNED_NATIVE_USD`; no reconstructed share-price value or weight notional |
| `accrual_treatment` | `INCLUDED`, `EXCLUDED`, or `NOT_APPLICABLE`, from an exact reviewed source equation; COT native MV = UMV + Accrual, with no second addition |
| `policy_revision` | exact admitted source/firm interpretation revision bound to this input, not a new label declared by the reader |
| `source_rows` | nonempty scoped row references supporting the source facts, with receipt roles checked; policy interpretation separately traced by revision |
| `source_quantity` | M object `{value, source_field, source_units, unit_rule_revision, evidence}`; exact native signed decimal text or null, source field/units/rule nullable when unavailable, scoped evidence references |

The top-level `quantity` is SHARES only when the exact asset/source unit rule
establishes it. Preserve supplied native quantity in `source_quantity` even when
that rule is unavailable; null SHARES must not erase a negative native quantity.
Missing mandatory unit/sign interpretation refuses accepted input. Absent
quantity may be permitted only by an explicit admitted native-USD policy; no
zero is fabricated. Y must evaluate native quantity sign before aggregation,
check correspondence with resolved quantity where supplied, and reject negative
quantity or SHORT for the present recipe even with positive MV. Zero quantity
does not by itself establish cash or zero value.

Keep M's raw cash flag, side spelling, source field, UMV/accrual observations and
their evidence in the private binding's source interpretation records. They
support these resolved fields rather than introducing a second competing
`cash`/`side`/`security`/`accrual` shape on the accepted boundary. Unknown required
resolved facts refuse the whole input; do not turn null into a default enum.

`security_resolution` has exactly `identity_kind: CANONICAL_SECURITY`,
`security_key`, `canonical_identifier`, `canonical_identifier_namespace`
(`TICKER`, `CUSIP`, `CASH`), `resolution_revision`,
`resolution_source_receipt_id`. This receipt must identify actual admitted
immutable mapping evidence. No fabricated ticker crosswalk. CASH requires
`$:CASH` and sourced CASH classification; noncash cannot use that identifier.
Conflicting canonical key/identifier assignments or unavailable evidence refuse.

### Numeric transport versus recipe eligibility

ASCII string-only grammar, matched as a whole string:

```text
[+-]?(?:[0-9]+(?:\.[0-9]*)?|\.[0-9]+)(?:[eE][+-]?[0-9]+)?
```

P counterproposal selects M's stricter source-evidence cap: 1100 characters,
1000 Decimal coefficient digits, absolute Decimal exponent <= 1000, finite.
Y proposed 2048 characters; this cap is an explicit pending agreement, not an
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
| Trusted accepted binding writer/store/read surface | P: absent; current mutable/date publication cannot stand in for an immutable snapshot lookup |
| Economic field pairing and 1100 versus 2048 text cap | P coordinates M/Y against these exact definitions; still conditional |
| COT source contract | M source review: B01 has no currency/side declaration, Cash Equivalent is insufficient, Units is not universal SHARES; adding Currency would require a source-map amendment, not a helper default |
| INF source contract | M source review: optional facts, missing stable mandatory instrument grain/currency/side; builder zero accrued income is not vendor economic proof |
| 49F source contract | M source review: l_s exists but signed-value rule, security-join uniqueness, cash non-overlap, currency/units and pending accrual ruling remain unresolved |
| Current numeric schema and security mapping receipts | Not supplied by either review; P cannot invent a receipt or conversion policy; M identifies source capability, CTO adjudicates needed source interpretation |
| Empty-account census | No admitted complete-zero receipt capability; actual empty inputs refuse |
| Retained revision/provenance shape | P/Y must pin exact schema-compatible normalized source extension |

These are source-located findings from the exact M review, not fresh cloud
measurements. No producer execution or new source-read authority is inferred.
Next implementable contract needs a concrete trusted binding and actual economic
source evidence; a closed schema alone cannot supply either. CTO remains direct
reviewer. No cloud write, production source activation, IAM change, vendor
request or public field emission follows from this draft.
