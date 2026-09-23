# Accepted custody reader: exact interface draft

Status: LOCAL DRAFT FOR M/Y CONTRACT REVIEW. This document adds no runtime,
schema fields, storage authority, producer acceptance or deployment permission.

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
`original_rows` references the same scoped `source_receipt_id` and zero-based
per-object `row_index` as positions. It carries canonical account ID, source
security identity, exact signed value/quantity and authoritative economic facts
needed by Y. Missing cash/side/security/unit facts remain unavailable; positive
market value alone does not prove eligibility. Exact economic-fact field names
are still required from M/Y before closing this internal schema.

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
   is distinct per receipt. Repeated identical receipt/row references refuse.
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
the private reader. Exact decimal size/scale limits remain an explicit M/Y
agreement item; values must never be rounded to fit a limit. Decimal/text
preserves typed Parquet values, not historical pre-Parquet lexical formatting.

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
| Different objects, each physical row 0 | Distinct immutable receipts | Keep both distinct; repeated same receipt/row refuses |

Before implementation: M/Y confirm remaining economic-fact names and decimal
bounds; P identifies concrete trusted binding writer/store and read surface,
then pins the complete closed schema and unchanged-factory adapter contract.
No accepted reader is claimed merely by defining callbacks. CTO remains direct
reviewer. No cloud write, production source activation, IAM change, vendor
request or public field emission follows from this draft.
