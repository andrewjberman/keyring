# M corrections to P accepted-custody reader draft

Review request: exact P message 20260923T160015Z. Reviewed draft `7e9baf3064`,
`IRPT_MVP_P/ACCEPTED_CUSTODY_READER_DRAFT_20260923.md`; helper exact candidate
`b3e63a795e0b8c7399619dbc545745786add4eb7`; three-firm runner source pin
`1067e472a4298085e768bb03df10a5d16e3456e2` (twelve-file inventory remains in
ACTUAL_POSITION_REPAIR_PROPOSAL_20260923.json). Read-only source review; no code,
producer, cloud, shared schema, binding store or callback changes.

Current interface reconciliation: Y `605449f4cc` adopts these nested fields and
1100-character transport bound. M accepts Y's canonical-security additions and
original-row correspondence below for P's closed-schema decision. This supersedes
Y's earlier flat field proposal; it supplies no missing source authority.

## Signature and boundary: retain, with these corrections

P's proposed `AcceptedCustodyReader.authorize_snapshot(principal, owner) -> bool`
and `read(principal, owner) -> dict` are suitable separation points. The latter
returns selected accepted input plus ORIGINAL rows, or refuses; neither is
implemented by M's helper. Keep the existing factory callback signature.

Actual helper signature is:

```python
validate_cot_actual_positions(
    holdings, account_totals, *, custody_as_of, valuation_as_of,
    expected_account_ids=None, holdings_row_origins=None, total_row_origins=None
)
# -> (unique Decimal-valued DataFrame, PRIVATE raw-ID evidence dict)
```

The optional expected IDs are RAW source IDs, not canonical selection IDs.
`build_cot` does not supply them. P must independently authorize the canonical
selected census, validate a one-to-one source mapping where required, then check
coverage; equality of two frames is not that proof. Origins supplied by callers
are checked structurally, not verified against an immutable receipt by this
helper. Without origins, row_index means input-frame ordinal only. With origins,
physical row identity is the pair (exact source object, zero-based row index).
P must bind this to its scoped receipt IDs and verify index bounds against parsed
object rows. Do not expose the helper's raw IDs, URI references or whole frames.

The helper evidence does NOT contain an admitted security resolution, cash or
side classification, source quantity-unit authority, immutable snapshot binding,
current owner proof or empty-account census receipt. Do not copy its dictionary
and label the result AcceptedCustodyInputV1. A future mapper needs these facts
from the exact receipts/owner-approved interpretation. Its exceptions yield no
partial accepted envelope. Legacy input without actual custody remains unavailable.

## Exact proposed economic-fact additions (internal draft only)

Retain P's agreed `market_value`, nullable `quantity` and `source_security_id`.
Each original row has singular `source_row` with scoped `source_receipt_id`,
nonnegative physical `row_index` and nullable `relationship_id`; positions retain
plural `source_rows`. Add `economic_facts` to BOTH each original row and each unique
position; these facts participate in duplicate equality. The shapes below are
proposed for P/Y agreement, not implemented or emitted fields. `EvidenceRef` is
P's scoped `{source_receipt_id: string, row_index: integer >= 0}`; column names
below identify fields within those exact rows, not a public object location.

| Field within economic_facts | Exact proposed type | Meaning / refusal rule |
|---|---|---|
| `cash` | object `{source_field: string|null, source_value: boolean|null, classification: "CASH"|"CASH_EQUIVALENT"|"NON_CASH"|null, evidence: EvidenceRef[]}` | Preserve the exact typed flag. A classification needs a bound source interpretation; unknown is null, not NON_CASH. CASH_EQUIVALENT must never become the literal cash security. |
| `side` | object `{source_field: string|null, source_value: string|null, position_side: "LONG"|"SHORT"|null, sign_rule_revision: string|null, evidence: EvidenceRef[]}` | Preserve vendor position side. No side from transaction direction, positive net, or sign guessing. A bound sign rule must state whether value/quantity are already signed; do not apply a sign twice. A source without a separate side field needs an explicit owner-admitted signed-value rule, not a fabricated LONG. |
| `security` | object `{resolution_revision: string|null, resolved_identifier: {namespace: "TICKER"|"CUSIP"|"CASH", value: string}|null, security_key: string|null, resolution_source_receipt_id: string|null, evidence: EvidenceRef[]}` | Source identifier is still separate in source_security_id. Resolution must be maintained, firm/vendor scoped and tied to that identifier; no fabricated ticker-based provider ID. Key and receipt are Y's required additions; null preserves an unresolved draft fact, never an accepted recipe identity. |
| `source_quantity` | object `{value: decimal-text|null, source_field: string|null, source_units: string|null, unit_rule_revision: string|null, evidence: EvidenceRef[]}` | Retain signed native numeric quantity even when its unit interpretation is unavailable. Populate the existing `quantity` SHARES object only when this exact source/asset supports SHARES; otherwise quantity is null. No guessing from column label alone for every instrument. |
| `accrual` | object `{treatment: "INCLUDED_IN_MARKET_VALUE"|"EXCLUDED_FROM_MARKET_VALUE"|null, value: decimal-text|null, unaccrued_market_value: decimal-text|null, rule_revision: string|null, evidence: EvidenceRef[]}` | Native value plus an explicit interpretation; no default zero. COT equation is MV=UMV+Accrual, with accrual already in MV. EXCLUDED is a possible declared fact, not permission to add accrual automatically or change a firm's valuation law. |

Currency stays `market_value.currency`, supported by that row or an exact bound
currency declaration referenced in `source_rows`; add no guessed currency.
If P prefers source facts in private binding metadata, equivalent receipt-bound
rules may be referenced from rows rather than duplicated, but read() must expose
the exact resolved facts Y needs. Raw private account/storage IDs remain private;
clarify the draft's blanket raw-ID sentence so it does not silently remove the
instrument identifier that `source_security_id` is required to convey. A vendor
instrument ID is not a canonical security and may require an opaque private
crosswalk reference if its raw spelling cannot leave the reader.

These internal proposed enum spellings do not authorize new public refusal enums.
Use existing refusal envelopes; missing required facts refuse the whole requested
input. Cash/side/unit/security facts cannot be inferred from a successful MV tie.

The one security object projects to Y's existing CANONICAL_SECURITY identity;
resolved_identifier supplies its canonical identifier and namespace. The mapping
receipt must resolve to actual immutable maintained mapping evidence within the
binding. No such accepted mapping receipt has been established by M's source
review. CASH requires sourced classification and `$:CASH`; cash equivalents keep
their resolved instrument identity. There is no parallel resolution authority.

Each original physical receipt/row pair occurs once and belongs to exactly one
economic position. Reusing that reference in its position's source_rows is
required correspondence, not an illegal duplicate. The union of position refs
equals all original refs; consumed facts agree before relationship collapse.
Known SHORT or negative native quantity refuses Y's positive-only recipe even
when MV is positive or interpreted SHARES quantity is null. Signed custody facts
remain intact; unknown interpretation never becomes LONG or an eligibility fact.

## What the pinned sources establish, and what they do not

**Cottonwood:** `data/cot/scripts/gold/runners_cot/b01_canonical_positions.py`
POSITION_MAP carries AccountID/AssetID, Relationship ID, CUSIP/Ticker/Symbol,
Market Value, Unaccrued Market Value, Accrual, Units and Cash Equivalent.
B00's native-decomposition contract plus B01 fields supports a proposed
INCLUDED_IN_MARKET_VALUE rule with MV=UMV+Accrual; actual row receipt and the
cent-level decomposition control remain required. Do not add accrual again.
`Cash Equivalent` is only a source cash-equivalent flag: it does not distinguish
literal cash from every cash-like security, nor does a false value itself settle
all NON_CASH classification rules. AssetID supplies source grain; the other
identifiers are candidates for resolution, not proof of it. Units has no explicit
per-instrument SHARES declaration here. No separate side field or currency
field is in POSITION_MAP. If an added Currency column existed, this runner's
undeclared-column guard would reject it without a corresponding source contract
amendment; M's local helper requiring Currency did not implement that amendment.
The source helper compares optional cash/security fields only when present and
never turns their absence into accepted economics. Missing authoritative
currency, side/sign/unit/security/cash interpretation remains unresolved.

**Inflection:** `data/inf/scripts/gold/runners_inf/b01_canonical_positions.py`
renames current_shares/current_price/current_value and conditionally carries
is_custodial_cash, ticker, ISIN, asset_class and product_category. These locate
vendor facts and a possible explicit cash flag, not an accepted classification
for every row. CARRY has no mandatory stable vendor position/product ID, separate
side or explicit currency column. Field names current_shares/shares identify the
intended quantity but do not establish every asset's unit/sign semantics. B00's
N-A-BY-CONSTRUCTION accrued_income=0 is a builder declaration, not in-row vendor
proof that every position lacks accrued income. Its activity missing/zero
coercion remains unresolved; independent total correctness is not repaired here.
No legacy interpolated price source is an acceptable substitute.

**49F:** `data/assets/scripts/gold/runners_49f/b01_canonical_positions.py`
explicitly carries l_s as position_side (SHORT sign carrier, never transaction
direction), CUSIP, security_key through A03, quantities, vendor position MV and
factored/unfactored price/factor/asset-backed-factor tuple. That establishes the
source-side field and required decomposition surface. It does not settle whether
each value is already signed or prove a valid unique security join (A03 keeps
first CUSIP duplicate). B00 separate cash/MM/sweep/bank/margin components need
non-overlap proof against security rows; no cash residual may be invented. B00
accrual is PENDING-RULING, so zero must not become an accepted accrual treatment.
Explicit currency/asset-unit interpretation and coverage outside Schwab master
08335338 remain unproved. None of this changes SmartX-primary performance.

All three are SOURCE-LOCATED facts, not fresh live data/census acceptance.
Current versioned numeric Arrow schemas and actual precision/scale were not
measured by this review. No new source read or producer execution is authorized.

## Decimal precision: distinguish actual guard, source contract and transport

Exact b3e63 helper behavior:

- `Decimal(str(value))`; rejects null/bool, invalid/nonfinite decimal and values
  whose float conversion is nonfinite; coefficient digit count <=1000 and
  absolute Decimal exponent <=1000. Arithmetic uses explicit precision 4096.
- These are local validation/resource bounds, NOT measured vendor precision or
  a ratified transport scale. A tiny finite decimal can underflow to zero during
  float conversion without failing the finite check. The helper retains its
  Decimal/text, but legacy build_cot account nodes later use floats and existing
  rounded totals; that display path is not the exact-text accepted reader.
- `str(Decimal)` can use exponent notation and retains representable trailing
  scale; it is not a canonical plain-decimal grammar. A binary float input becomes
  Decimal of its shortest Python string, not recovery of a pre-Parquet decimal
  or the exact binary rational. Source receipts preserve original typed bytes.

**Proposed bounded reader transport:** signed finite decimal TEXT parsed directly
as Decimal, at most 1100 characters, at most 1000 coefficient digits, absolute
exponent <=1000; permit Decimal exponent notation explicitly. Never round,
quantize, truncate or float-convert to fit. This reuses the local ceiling as a
conservative implementation bound ONLY, subject to P/Y agreement and exact
source numeric contracts. It does not prove current vendor/recipe coverage.
Oversize or incompatible values refuse. Arithmetic must remain exact under the
chosen bound (do not inherit a low caller context); the maximum reconciliation
difference remains Decimal('0.01'), not rounded cents or a basis-point rule.

The immutable binding should additionally pin private numeric metadata for each
consumed numeric column: `source_numeric_type` (exact Arrow type text),
`source_precision` and `source_scale` (integers or null when not declared),
`numeric_rule_revision`, and an exact schema/source receipt. Decimal Arrow values
preserve their declared p/s; strings require an admitted grammar/conversion rule.
Floating Arrow values require an explicit admitted conversion/precision policy,
not a claim of exact vendor decimals. Missing source p/s does not license a
fabricated scale, and a schema declaration alone does not prove monetary units.
No exact per-firm source p/s is currently established by the inspected code.

Y605449f4cc accepts this transport proposal and specifies string-only full-match
ASCII grammar `[+-]?(?:[0-9]+(?:\.[0-9]*)?|\.[0-9]+)(?:[eE][+-]?[0-9]+)?`.
No whitespace, JSON numeric coercion, NaN or infinity. This does not widen M's
existing float-finiteness guard. Separately, Y's current original-dollar analysis
domain is strictly positive, at most 28 coefficient digits and absolute exponent
18; its normalized output bridge has 128 characters, 80 digits and exponent 80.
These are consumer constraints reported in Y's pinned review, not newly exercised
by M. Quantity is not a dollar amount; preserve its sign and admitted unit rule.
Do not strip trailing zeros or round to fit any bound. The accepted interface's
reconciliation tolerance should be decimal text "0.01" or an admitted stricter
value; M's current PRIVATE float tolerance metadata is not that interface.

## Handoff disposition

Retain P's proposed signatures and accepted-vs-local separation. Add the concrete
facts above or equivalent bound rule references; resolve numerical representation
before claiming exact accepted text. Original rows must carry these facts before
any relationship/security collapse, including signed/zero rows. Counts/empty
shape agreed at P155115 remain unchanged: conflict_original_row_count singular;
COMPLETE describes custody observation, never positive-only recipe eligibility.
Complete empty-account proof and its census receipt capability remain unavailable;
local empty inputs refuse. Immutable binding writer/store and public S2/schema
remain P-owned unresolved. This review proposes corrections only; callbacks stay
closed and no shared runtime edits are requested by this document.
P can now close the proposed field shape using Y605449f4cc and this review;
source mapping receipts, numeric contracts and admitted economic interpretation
remain acceptance prerequisites, not a new authority to activate the reader.
