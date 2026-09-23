# Y review of accepted custody reader draft

Reviewed P `7e9baf3064`, `IRPT_MVP_P/ACCEPTED_CUSTODY_READER_DRAFT_20260923.md`, in response to exact P160015.
Y source: `819c9e399086cffb2876a21fbc2cee01724b0bd7`; producer helper: M `b3e63a795e0b8c7399619dbc545745786add4eb7`.
Status: CONDITIONAL INTERFACE AGREEMENT; no consumer implementation, schema emission or activation.

## Accepted structure and required binding checks

Keep `AcceptedCustodyReader.authorize_snapshot(principal, owner)` and `read(principal, owner)`, plus the existing Y `load_normalized(browser, principal, owner)` callback. The proposed top-level fields are sufficient if the closed definitions below and their evidence are bound to the immutable reader result. M's private DataFrame result remains outside this interface.

The reader must return exact `owner` equality, not a subset: actor principal and home firm, concrete report firm, canonical selected account set, account-set ID, directory/entitlement revisions, snapshot ID and ownership fingerprint. Match top-level snapshot to owner and browser; never derive tenant from an arbitrary position. Match actual_custody.firm_id and account_ids to owner, unique sorted canonical sets. All original rows, positions, census and reconciliation must cover that exact selection without foreign accounts; proved empty accounts must be represented explicitly. No actor or snapshot identity may be cached across callers.

`snapshot_revision` identifies original complete accepted bytes. `binding_revision` must bind that revision plus the immutable receipt registry, source-set and raw-to-canonical mapping revisions, publication acceptance policy/version and selected binding semantics. P owns the concrete writer/store and digest algorithm. Neither value may be computed from the selected/decorated payload and called the whole snapshot revision. A changed latest publication does not silently rebind an old snapshot ID; current authorization of the pinned old revision and source selection are separate checks. Recheck exact binding/current authority after reads and at factory release. Normalized bytes must retain both revisions and relevant source receipt references through the existing source/provenance structure, with P/Y agreement on its exact shape; a new artifact family is unnecessary and not authorized.

Opaque receipt IDs must resolve within this exact binding and firm/account scope to verified immutable bytes and source role. Physical row references must be in range for their particular object, not a post-filter frame. Each original physical receipt/row pair occurs once in original_rows. Referencing that same original from its collapsed position is expected and must not trigger a blanket cross-structure duplicate rejection. Every original maps to exactly one admitted economic position, and the union of positions' source_rows equals the original-row set. No orphan, extra, missing or multiply assigned original. Corresponding values, identity, quantity and economic facts must agree across duplicate relationships before collapse. This correspondence check prevents a positive sanitized positions array from hiding a negative original.

## Exact proposed original-row and economic-fact fields

P owns adoption into the closed internal schema. These names are the requested concrete Y proposal; they are not emitted public fields or newly implemented source facts. Unknown required facts must refuse AcceptedCustodyInputV1 instead of inventing a value. Complete known signed custody can still be returned but is ineligible for the positive-only recipe.

Each `original_rows[]` entry should have exactly:

- `account_id`, `position_id`: canonical account and stable economic-position identity matching one positions[] member. Relationship duplicates may share position_id; their physical origins remain distinct.
- `source_security_id`: existing `{namespace, value}` from the original source, without ticker/vendor-prefix inference.
- `market_value`: existing `{value, currency}` with signed exact decimal text and authoritative USD for this first consumer.
- `quantity`: existing `{value, units: "SHARES"}` or null when quantity is not supplied/needed for sourced USD. Do not fabricate zero quantity.
- `source_row`: exactly `{source_receipt_id, row_index, relationship_id}`; nonnegative physical integer row, nullable scoped opaque relationship ID. This singular member is the one original; positions[] keeps its existing plural source_rows.
- `economic_facts`: the closed object below.
- `security_resolution`: the closed maintained-resolution object below.

Proposed `economic_facts` fields:

| Field | Exact type / semantics |
| --- | --- |
| `cash_classification` | `CASH` or `NON_CASH`, established by the admitted source/policy; never inferred from ticker spelling, zero quantity or a cash-like display name. A cash-equivalent flag is not automatically canonical cash. |
| `position_side` | `LONG`, `SHORT`, or `NOT_APPLICABLE`. NOT_APPLICABLE requires an explicit admitted rule, such as sourced cash; it is not a missing-value fallback. Side is evidence, never an instruction to negate market value or quantity again. |
| `value_basis` | Literal `SIGNED_NATIVE_USD` for the first adapter: supplied native dollar value, no weight notional or share-price reconstruction. A future conversion branch requires a separate admitted quote contract. |
| `accrual_treatment` | `INCLUDED`, `EXCLUDED`, or `NOT_APPLICABLE`, as established by the firm/source policy. COT native Market Value uses INCLUDED; never add Accrual again. EXCLUDED/NOT_APPLICABLE require a reviewed source-specific equation, not a Y default. |
| `policy_revision` | Nonempty exact revision of the admitted firm/source economic interpretation, resolved through the binding. It must cover cash, side, value basis and accrual treatment; a made-up label is not authority. |
| `source_rows` | Nonempty list of existing opaque receipt/physical-row references supporting these facts, with roles verified by P. These may reference source dimensions as well as the position object. Policy-only interpretation is traceable to policy_revision; absent source evidence still refuses. |

Proposed `security_resolution` fields: `identity_kind: "CANONICAL_SECURITY"`, `security_key`, `canonical_identifier`, `canonical_identifier_namespace` (`TICKER`, `CUSIP`, `CASH`), `resolution_revision`, `resolution_source_receipt_id`. The first five identity/revision fields retain existing Y `_security_resolution` semantics. The extra opaque receipt identifies the admitted immutable mapping evidence in P's binding; it is not a fabricated ticker crosswalk. P/M should identify that actual maintained evidence surface or mark it unavailable. CASH requires canonical identifier `$:CASH` and consistent sourced cash classification; noncash must not use that identifier. Multiple canonical keys for one namespace/identifier, conflicting resolutions of one key, absent resolution or unavailable mapping provenance refuse.

No new `negative_quantity` boolean is required: derive the sign exactly from `quantity.value` when present, before aggregation, and cross-check any producer diagnostic. Negative quantity with positive MV is not automatically a supported long position. For this positive-only consumer, any negative quantity or known SHORT side refuses the whole selection until a separately admitted recipe/source policy supports it. A zero quantity is not automatically a zero value or proof of cash; only an explicitly admitted cash/unit policy could make that combination usable. No default cash/side/security interpretation is introduced by this document.

## Exact decimal contract and distinct limits

Use string-only ASCII decimal grammar, anchored at both ends:

```text
[+-]?(?:[0-9]+(?:\.[0-9]*)?|\.[0-9]+)(?:[eE][+-]?[0-9]+)?
```

No whitespace, currency symbols, separators, percent, JSON numbers, boolean, NaN or infinity. Preserve supplied typed-Parquet Decimal/text representation (including signed zero) with its source receipt; this is not a claim to reconstruct earlier vendor text. Parse with Decimal directly, never float as an intermediate. Exponent notation is allowed because the pinned producer uses str(Decimal); canonical source byte identity remains distinct from numeric equality.

Two limits must remain explicit:

1. **Proposed internal source-evidence transport bound:** at most2048 characters, at most1000 Decimal coefficient digits and absolute Decimal exponent at most1000, finite, with exact bounded-context arithmetic. This reflects the producer's bounded numeric intent, not an expansion of Y analysis eligibility. P/M must confirm before schema adoption. The current M helper additionally checks float-finiteness and can refuse a stricter range; this proposal does not relax that helper or make a refused source accepted. Out-of-bound evidence refuses the internal transfer without rounding, truncation or relabeling custody as zero.
2. **Existing Y first-consumer input domain:** every supplied original analysis dollar amount must be strictly greater than zero, with at most28 coefficient digits and absolute exponent at most18, exactly as `intake/portfolio.py:_number`. Check source rows before consolidation. Trailing zeros count under the current Decimal tuple rule; do not strip precision to force acceptance. A source can be valid custody yet outside this recipe domain. Reference notional and quote helpers are unchanged. A supplied quantity is not fed into the dollar helper or converted to money; its sign/units and source-evidence bounds are checked separately.

The normalized output/upload bridge retains its existing positive exact-string limit: length128, coefficient digits80 and absolute exponent80. Totals and aggregated positions must meet it and reconcile exactly before dispatch; do not inherit the default Decimal context or sum floats. Account reconciliation uses the separately admitted maximum0.01 USD tolerance against independent same-date evidence; this never licenses row rounding or duplicate approximate equality. `tolerance_usd` should remain decimal text `"0.01"` (or an explicitly stricter admitted value), not a JSON float.

## Before consumer implementation

P/M should confirm or counter the concrete economic fields, mapping-evidence receipt, original-to-position correspondence, and source transport bounds above. Pin the closed internal schema and the trusted accepted binding writer/store/reader with source and policy evidence. Missing prerequisites refuse; callbacks remain unconfigured. Y can then implement original-row eligibility and the trusted parsed-row adapter without weakening the existing freezer or importing the gold producer into Lambda.

Required paired examples add: negative quantity with positive MV; cash label/security mismatch; unsupported side with positive total; malformed exponent/nonfinite/over-bound exact text; boundary28/29 digits and exponent18/19; original negative row omitted from positive positions; same receipt/row assigned twice; receipt reused correctly as an original's position reference; mismatched binding/policy/mapping revision. These are proposed controls, not executed tests. CTO remains the direct reviewer. This review changes no code, public schema, live source, IAM or production configuration.
