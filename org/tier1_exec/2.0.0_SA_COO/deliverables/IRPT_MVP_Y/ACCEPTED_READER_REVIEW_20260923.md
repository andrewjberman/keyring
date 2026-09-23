# Y review of accepted custody reader draft

Reviewed P `f6babe048f`, `IRPT_MVP_P/ACCEPTED_CUSTODY_READER_DRAFT_20260923.md`, following original request P160015 and paired publication P160937.
Y source: `819c9e399086cffb2876a21fbc2cee01724b0bd7`; producer helper: M `b3e63a795e0b8c7399619dbc545745786add4eb7`.
Status: CONDITIONAL INTERFACE AGREEMENT; no consumer implementation, schema emission or activation. Current field proposal incorporates M review44e3a52fa3353ea94b3a473547efef77847e0d52 and supersedes the earlier flat Y economic-fact aliases.

## Accepted structure and required binding checks

Keep `AcceptedCustodyReader.authorize_snapshot(principal, owner)` and `read(principal, owner)`, plus the existing Y `load_normalized(browser, principal, owner)` callback. P f6babe incorporates the nested facts and correspondence requirements below. One additional exact selection-fingerprint field is needed for the existing freezer source contract, as detailed below. M's private DataFrame result remains outside this interface.

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
- `economic_facts`: the closed nested object below, also present on each unique position; all consumed facts participate in duplicate equality. Its security member is the single resolution authority, not a second conflicting top-level resolution object.

Proposed `economic_facts` uses M's nested fact names and shapes, with the explicit Y security additions below. These are internal owner-agreement requirements, not emitted fields. EvidenceRef is the existing scoped `{source_receipt_id, row_index}`; source column names identify columns within those verified rows. P's immutable binding must also pin the admitted interpretation rules. Null preserves an unknown source fact; it cannot be silently converted to a positive eligibility fact.

| Field | Current agreed-direction shape and Y constraints |
| --- | --- |
| `cash` | M `{source_field, source_value: boolean|null, classification: CASH|CASH_EQUIVALENT|NON_CASH|null, evidence: EvidenceRef[]}`. Preserve typed source flag and bound classification rule. Cash Equivalent is not literal cash, and false does not automatically prove NON_CASH. Only admitted CASH maps to `$:CASH`; CASH_EQUIVALENT keeps its actual resolved instrument identity. |
| `side` | M `{source_field, source_value, position_side: LONG|SHORT|null, sign_rule_revision, evidence}`. A source without explicit side may use an owner-admitted signed-value rule; never fabricate LONG or NOT_APPLICABLE. Rule states whether MV/quantity already carry sign. Null side is usable only when the exact admitted rule independently resolves necessary semantics; missing sign interpretation refuses. No sign is applied twice. |
| `security` | M `{resolution_revision, resolved_identifier: {namespace,value}|null, evidence}`, plus proposed `security_key` and `resolution_source_receipt_id` required by Y. This one object supplies canonical identity and actual immutable maintained-mapping proof; absent/ambiguous resolution refuses the recipe. |
| `source_quantity` | M `{value: decimal-text|null, source_field, source_units, unit_rule_revision, evidence}`. Preserve signed native quantity even when SHARES interpretation is unavailable. Existing row.quantity is populated only when an admitted source/asset rule proves SHARES; otherwise null, never zero. Missing interpretation required for side/value consistency remains refusal even when native USD MV exists. |
| `accrual` | M `{treatment: INCLUDED_IN_MARKET_VALUE|EXCLUDED_FROM_MARKET_VALUE|null, value: decimal-text|null, unaccrued_market_value: decimal-text|null, rule_revision, evidence}`. COT uses native MV=UMV+Accrual, included exactly once. EXCLUDED is a source fact, not permission to add accrual; a different firm's equation must be explicitly admitted. INF builder-declared zero and 49F pending-ruling zero are not vendor proof. |

For the first Y adapter, analysis value is the sourced signed native USD market_value under the bound policy, not converted quantity or weight notional. This value-basis interpretation must be explicit in the accepted binding; no additional parallel row alias is required. Cash/side/accrual/unit rules and evidence must support that interpretation or read/eligibility refuses. M's helper currently lacks these authorities; its private evidence cannot be copied into this object as acceptance.

The security member must project without inference to existing Y `{identity_kind: "CANONICAL_SECURITY", security_key, canonical_identifier, canonical_identifier_namespace, resolution_revision}`: canonical_identifier comes from resolved_identifier.value and namespace from resolved_identifier.namespace, limited to TICKER/CUSIP/CASH. `resolution_source_receipt_id` binds real maintained mapping evidence, not a fabricated crosswalk. P/M must identify its actual surface or refuse. CASH requires `$:CASH` and consistent sourced classification. Conflicting keys/resolutions or namespace/identifier aliases refuse. Source vendor instrument IDs remain distinct from canonical identity; private account/storage IDs must not leak, but privacy filtering must not silently erase required source_security_id provenance. P may use a scoped private crosswalk reference when needed.

No new negative_quantity boolean is required. Derive sign directly from economic_facts.source_quantity.value and, when present, quantity.value; check their exact correspondence through the admitted unit rule before aggregation. Do not bypass a negative native quantity by setting interpreted quantity to null. Any negative native/interpreted quantity or known SHORT side refuses this positive-only recipe until a separately admitted policy/recipe supports it. Zero quantity alone proves neither cash nor zero value; any allowed sourced-USD combination needs explicit cash/unit/sign rules. Positive MV cannot resolve these ambiguities.

## Exact decimal contract and distinct limits

Use string-only ASCII decimal grammar, anchored at both ends:

```text
[+-]?(?:[0-9]+(?:\.[0-9]*)?|\.[0-9]+)(?:[eE][+-]?[0-9]+)?
```

No whitespace, currency symbols, separators, percent, JSON numbers, boolean, NaN or infinity. Preserve supplied typed-Parquet Decimal/text representation (including signed zero) with its source receipt; this is not a claim to reconstruct earlier vendor text. Parse with Decimal directly, never float as an intermediate. Exponent notation is allowed because the pinned producer uses str(Decimal); canonical source byte identity remains distinct from numeric equality.

Two limits must remain explicit:

1. **Proposed internal source-evidence transport bound:** at most1100 characters, at most1000 Decimal coefficient digits and absolute Decimal exponent at most1000, finite, with exact bounded-context arithmetic. This reflects the producer's bounded numeric intent, not an expansion of Y analysis eligibility. Y accepts M's1100-character proposal in place of Y's earlier2048; P owns final schema adoption. The current M helper additionally checks float-finiteness and can refuse a stricter range; this proposal does not relax that helper or make a refused source accepted. Out-of-bound evidence refuses the internal transfer without rounding, truncation or relabeling custody as zero.
2. **Existing Y first-consumer input domain:** every supplied original analysis dollar amount must be strictly greater than zero, with at most28 coefficient digits and absolute exponent at most18, exactly as `intake/portfolio.py:_number`. Check source rows before consolidation. Trailing zeros count under the current Decimal tuple rule; do not strip precision to force acceptance. A source can be valid custody yet outside this recipe domain. Reference notional and quote helpers are unchanged. A supplied quantity is not fed into the dollar helper or converted to money; its sign/units and source-evidence bounds are checked separately.

P's immutable receipt metadata must pin each consumed numeric column's exact `source_numeric_type` (Arrow type text), `source_precision`, `source_scale` (declared integers or null), `numeric_rule_revision`, and schema/source receipt. These are private metadata, not new public fields. Decimal types preserve declared precision/scale; string conversion requires the admitted grammar; floating types require an explicit admitted conversion/precision policy and must not be represented as recovered vendor decimals. Unknown p/s stays unknown. No current per-firm Arrow numeric contract was measured by these source reviews. M's1000/1000 and Context4096 are implementation/resource bounds, not vendor precision evidence. An accepted reader must not reuse the rounded float-based legacy display nodes as exact input.

The normalized output/upload bridge retains its existing positive exact-string limit: length128, coefficient digits80 and absolute exponent80. Totals and aggregated positions must meet it and reconcile exactly before dispatch; do not inherit the default Decimal context or sum floats. Account reconciliation uses the separately admitted maximum0.01 USD tolerance against independent same-date evidence; this never licenses row rounding or duplicate approximate equality. `tolerance_usd` should remain decimal text `"0.01"` (or an explicitly stricter admitted value), not a JSON float.

## Before consumer implementation

### Concrete retained provenance mapping for P/Y agreement

Inspection at Y819c shows `intake/portfolio.py:_source` requires `source_revision`, `selected_set_fingerprint`, `as_of`, and account IDs for CUSTODY, deep-copies the source, and the freezer hashes the entire document. The published RequestComposition resolved.document schema is an object whose semantic validation belongs to Y, not a closed source-field schema. Thus the following is structurally compatible, but requires P/Y semantic agreement and validation before implementation; structural pass-through is not authority.

The reader draft does not yet return the exact selected-set fingerprint. `_scope/selection.py:_view` returns `selected_account_set_fingerprint` using account IDs, entitlement revision, viewer policy and verified firm. `_scope/custody.py`'s owner instead has `ownership_fingerprint`, a digest of the full owner. These are different identities. Add top-level `selected_account_set_fingerprint` to the closed AcceptedCustodyInputV1, obtained from the current verified selection and bound to the reader result. Do not substitute ownership_fingerprint, permitted-account fingerprint, account_set_id or an ad hoc account-list hash. Y can then map it to the freezer's existing `source.selected_set_fingerprint` without guessing.

For the new accepted-reader branch only, propose exact normalized document.source fields:

| Existing/new source member | Exact mapping |
| --- | --- |
| `lane` | `CUSTODY` |
| `source_revision` | accepted.snapshot_revision, the original complete snapshot digest |
| `selected_set_fingerprint` | accepted.selected_account_set_fingerprint from P's current verified selection |
| `as_of` | accepted.actual_custody.custody_as_of, with the admitted valuation-date rule already checked |
| `account_ids` | exact canonical accepted.owner.account_ids, sorted as the existing freezer requires |
| `snapshot_id` | accepted.snapshot_id == owner.snapshot_id == browser.snapshot_id |
| `accepted_custody` | Deep copy of the complete selected-only, closed AcceptedCustodyInputV1 result including owner, both immutable revisions, original_rows, positions, census/reconciliation, resolved facts and opaque receipt references |

Embedding the already closed selected reader result avoids inventing a second provenance schema or a new retained family. It must contain only its admitted opaque/internal evidence, never M's private raw-ID frame or storage locations. Validate all outer/embedded duplicate fields for exact agreement; rehashing cannot substitute a different snapshot, owner or binding. Existing `NORMALIZED_PORTFOLIO` bytes/hash then retain all evidence, and the composition's artifact reference continues to bind those exact bytes. Retained replay validates the same embedded contract and current authorization without loading a newer source. Existing historical documents and other source lanes are not rewritten or reinterpreted.

Original relationship rows must be retained in source.accepted_custody.original_rows but must NOT all be added as separate normalized money rows: that would double-count equal relationships. After original eligibility and exact correspondence checks, the trusted parsed adapter emits one row per valid economic position, retaining its position_id and source_rows; existing later same-security aggregation preserves those contribution rows. This is a required future consumer behavior, not a newly implemented adapter.

P/M should close the concrete nested economic fields, Y canonical security-key/mapping-receipt additions, source numeric metadata, and original-to-position correspondence above. Pin the closed internal schema and the trusted accepted binding writer/store/reader with source and policy evidence. Missing prerequisites refuse; callbacks remain unconfigured. Y can then implement original-row eligibility and the trusted parsed-row adapter without weakening the existing freezer or importing the gold producer into Lambda.

Required paired examples add: negative quantity with positive MV; cash label/security mismatch; unsupported side with positive total; malformed exponent/nonfinite/over-bound exact text; boundary28/29 digits and exponent18/19; original negative row omitted from positive positions; same receipt/row assigned twice; receipt reused correctly as an original's position reference; mismatched binding/policy/mapping revision. These are proposed controls, not executed tests. CTO remains the direct reviewer. This review changes no code, public schema, live source, IAM or production configuration.
