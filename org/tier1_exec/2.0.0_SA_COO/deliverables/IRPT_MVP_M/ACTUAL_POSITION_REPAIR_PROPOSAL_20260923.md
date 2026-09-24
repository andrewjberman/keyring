# Bounded actual-position producer repair proposal

Status: PROPOSED for CTO adjudication; source-only, no producer or cloud execution.
Owner: 2.0.0_SA_COO~M. Request: CTO exact inbox `20260923T152513Z`.
Authority: IRPT MVP completion CONTRACT v1.2 and current narrower source-proposal
assignment. P's live-scope ownership transfer and exact holdings/entry exception
remain operative. No repair scope or deployment is activated by this document.

## Finding and source boundary

Reusable actual-position sources are located for all three firms. The existing
IRPT display tree does not consume them as a complete accepted security census.
The immediate gap is a bounded actual-custody producer/adapter plus acceptance
controls, not permission to reconstruct actual holdings from model targets.

Source pin: `1067e472a4298085e768bb03df10a5d16e3456e2`. Companion
[JSON inventory](ACTUAL_POSITION_REPAIR_PROPOSAL_20260923.json) pins the twelve
B00/B01/B03/runner_common files by Git blob, SHA256 and definition line numbers.
Working files matched that pin after newline normalization. Only source bytes
were read; no production module was imported or invoked. Exact current cloud
versions, completion and availability for a requested account/date are NOT
established by this inspection. Prior nine-path handoff remains
`abfb3eaf8242cf5df26c7e1074e0e555245d969a` and its two separately pinned trees.

## Exact located inputs and firm-specific repair

### 49 Financial: Schwab master 08335338 only

Source directory: `data/assets/scripts/gold/runners_49f/`.

- `b01_canonical_positions.py:build_canonical_positions` reads
  `s3://opal-data-assets/schwab/08335338/silver/dim_position/date={D}/`
  (all parquet members). It emits
  `s3://opal-data-49financial/gold/advi/canonical/canonical_positions/date={D}/data.parquet`
  with adjacent `manifest.json`. Grain is account, business date, CUSIP, position
  side (`l_s`); account IDs are padded to ten characters. It retains vendor
  `market_value_settled_unsettled`, quantities, factored/unfactored closing price,
  factor and asset-backed factor. `dimensions/dim_security` supplies security_key
  and rate_bearing; `dimensions/dim_boundary` supplies boundary_version, under
  the same `gold/advi` root and date grammar.
- `b00_canonical_valuation.py:build_canonical_valuation` reads the same silver
  root's `dim_balance/date={D}/`; authoritative account value is
  `net_mv_plus_cash`, restricted to IN_CLIENT_BOOK. Its output is
  `gold/advi/canonical/canonical_valuation/date={D}/data.parquet` in the firm bucket.
  It carries long/short/position and cash/MM/sweep/bank/margin decomposition.
  Accrued income is zero with explicit PENDING-RULING, not an established
  economic absence of accrual.
- `b03_valuation_integrity.py:build_valuation_integrity` is a flag plane, not an
  acceptance gate. It fills missing quantities/prices with zero, missing or zero
  factor with one, absent grouped positions with zero, and computes quantity x
  closing_price x factor plus selected cash components. That is not sufficient
  for IRPT complete-custody admission, and does not independently settle short
  sign/factor/cash overlap semantics.

Proposed repair: independently enumerate selected boundary accounts; project
all actual position rows, preserving side and vendor signed economic values;
carry exact cash/debt components separately and establish non-overlap against
security rows before summing. Use vendor position value as the sourced value;
retain quantity/price/factor decomposition for validation, never double-apply a
factor or infer a short sign twice. Refuse ambiguous security joins (B01 currently
keeps first duplicate CUSIP), missing boundary, nonfinite values, unknown sign or
currency, and missing accounts. Do not use B01's allow-missing-boundary option.
Compare each account to authoritative balance with an explicit formula and
approved tolerance; a residual is a finding, not a synthetic security/cash row.

Availability limit: this is a located master-specific Schwab chain. It does not
prove coverage of every 49F custody account or any other master. Earlier measured
September 21 canonical rows are historical evidence, not September 23 freshness.
SmartX allocation/model rows and its separate valuation facts cannot fill
missing custody rows or establish whole-account security coverage.

### Cottonwood: actual Black Diamond custody rows

Source directory: `data/cot/scripts/gold/runners_cot/`.

- `runner_common.py:read_fact` resolves latest partition <= requested date from
  `s3://opal-data-assets/blackdiamond/cottonwood/silver/` (bucket can be explicitly
  overridden by COT_ASSETS_BUCKET). `b01_canonical_positions.py:build` reads
  `fact_holdings/date={resolved_hold_date}/data.parquet`. This source, not the
  legacy opal-data-cot silver twin, is the runner's selected input plane.
- Actual grain is Relationship ID x AccountID x AssetID. B01 maps account,
  custody_account_number, asset_id, symbol/ticker/CUSIP, market_value,
  unaccrued_market_value, accrued_income, units and cash_equivalent. It preserves
  relationship rows, null-value flags, position_vintage and boundary version.
- `b00_canonical_valuation.py:build` sums vendor Market Value through
  `runner_common.py:collapse_relationship_grain`, one account/asset position.
  Native Market Value includes accrual; do not add Accrual again. ALL-ROWS-NULL
  and SOURCE-ABSENT carry null. Partially null accounts can still be marked OK,
  with null_row_count: that is not complete-value acceptance.
- `b03_valuation_integrity.py:build` separates a shared-derivation collapse
  identity from the independent vendor account number in
  `fact_allocations/date={resolved_alloc_date}/data.parquet`, column
  `Account Market Value` keyed by AccountID. This roster value is a check only,
  not target allocations substituted for holdings or a new B00 authority.
  Different custody/roster vintages mean no independent tie.

Proposed repair: keep relationship provenance, then use the sanctioned collapse
with exact raw/unique/duplicate denominators. Its current equality check rounds
Market Value to cents and treats all invalid numeric states as one sentinel;
add adapter preconditions requiring finite, known values and equality of all
consumed economic/security fields (units, accrual, currency and identifier), not
just rounded MV. Refuse conflicting duplicates rather than keep first. Validate
all repeated roster totals before the B03 keep-first projection. Require each
selected account's full custody census, native MV=UMV+Accrual decomposition, and
same-vintage independent roster tie; partial-null, source-absent or missing
independent surface stays explicitly incomplete, not accepted.

Availability limit: custody and independent roster source paths exist in code;
current complete object sets are unmeasured here. B00/B01/B03 output roots are
injected `--output-root`; files are `{root}/{table}/date={requested_D}/data.parquet`
and manifests `{root}/_manifests/{requested_D}/{process_ts}__{table}.json`.
Do not invent a current published root from this harness. The exact admitted
root/run manifest must be supplied or located under an authorized later probe.
No vendor stale-price field is supplied by B01; no fabricated price date.

### Inflection: actual Orion positions

Source directory: `data/inf/scripts/gold/runners_inf/`.

- `runner_common.py:read_api_dim` resolves latest snapshot <= requested date.
  Default source is `s3://opal-data-inf/silver/api_dims/` (explicit INF_S3_BUCKET
  override is possible). `b01_canonical_positions.py:build` reads
  `positions_mv/snapshot_date={resolved_position_date}/data.parquet`.
  Vendor current_shares/current_price/current_value become shares/price/
  position_value. It conditionally carries ticker, name, ISIN, account,
  is_custodial_cash, custodian and reconciliation/source dates. It explicitly
  discards legacy interpolated/carry-forward canonical price series.
- `b00_canonical_valuation.py:build` reads
  `activity/snapshot_date={resolved_activity_date}/data.parquet`, authoritative
  `ending_mv`, with a positions discriminator. It declares the known activity
  window/parse-dollar defect. Missing ending_mv is nonetheless filled to zero
  in fair_value; zero contradiction checks only positive net position sums.
  Offset long/short or negative net positions must not be mistaken for empty.
  A latest-<= positions read is printed but not enforced as same-vintage there.
- `b03_valuation_integrity.py:build` ties B01 vendor values to ending_mv, flags
  vintage skew and explained/unexplained variances. It fills absent position
  sums/ending_mv with zero. VARIANCE-EXPLAINED is a defect classification, not
  acceptance of a complete portfolio.

Proposed repair: preserve every vendor position and explicit cash classification;
retain stable vendor row/security identity before projection (B01's CARRY list
has no mandatory unique position/product ID). Never deduplicate by ticker/name.
Resolve stable identities from an exact owner-approved source or refuse the
ambiguous rows. Require selected-account boundary and actual position completeness,
finite signed vendor values and declared currency, same effective valuation dates,
and an account-level independent tie. Keep SOURCE-ABSENT and contradicted/unknown
zero as null/unavailable in the IRPT result. No reconstruction of authoritative
ending_mv from positions; repairing upstream activity coercion/window semantics
requires its own DS/CTO adjudicated patch. No old interpolated price fallback.

Availability limit: current positions are located as a source family, not a
fresh complete receipt. Current reliable account-total coverage, stable vendor
position IDs and explicit currency for all rows are not established. Injected
Gold output-root and manifest grammar are the same pattern as COT; exact run/root
must be pinned later. No current accepted IRPT security census was found in the
nine-path handoff.

## Responsible owners and exact proposed edit boundary

| Responsibility | Responsible owner / integration constraint |
|---|---|
| This IRPT custody projection, census and publication acceptance | COO~M under completion contract, after CTO adjudicates this bounded proposal |
| Canonical financial computation, upstream source ambiguity and any change to the twelve runner files | DS/0.4.0_DS_ClientPlatform semantic owner; historical harness headers identify ~A for INF and ~B for COT. Those historical author lanes are not a new worker activation. CTO resolves/assigns any needed upstream repair. |
| Schedule, IAM, compute and later producer/cloud execution | AE/CloudOps operational owner; none included in this source-only scope |
| Current directory, scope/auth/bootstrap/header and holdings/entry.py exception; shared schema/package/API integration | COO~P remains sole integrator; M supplies requirements and paired examples, no parallel edits |
| Freezing/normalization, signed-value recipe support and custody factory | COO~Y; producer admission must not be bypassed by factory test callbacks |
| Scope adjudication / direct review | CTO adjudicates and directly reviews the later candidate under Andrew's September 23 11:18 Eastern instruction; no separate CVO gate |

Requested first implementation scope, if adjudicated: M's existing
`data/assets/scripts/gold/investor_reporting/holdings_snapshot.py` source-loading,
actual-custody projection and pre-publication acceptance sections, with the
existing `tests/test_holdings_snapshot.py`, `tests/test_economic_regressions.py`
and `tests/test_source_inputs.py` in that same directory. Keep TARGET/model
attribution separate and preserve unresolved actual value. Reuse B01 inputs and
B00/B03 evidence without editing or executing those runners in this tranche.
No new destination, standing dual writer, broad migration, P entry/scope edit,
Y freezer edit, or operational invocation is in the proposed M patch.

Before implementation, CTO disposition must select any firm whose necessary
currency, cash/sign semantics, stable identity or independent total is unresolved
as blocked, or assign an exact additional upstream owner patch. This proposal
never upgrades an unavailable source to complete. Three-firm target remains;
one admitted firm is only a milestone.

## Minimal output contract for owner agreement

Extend the accepted S2 contract through existing authoritative schema owners,
not a parallel public wire schema. Required information (field spellings subject
to P/M/Y integration):

1. Envelope: firm, explicit custody basis, schema and producer code revisions,
   immutable snapshot/revision identity, requested date plus actual position and
   valuation dates, boundary/census revision, and complete source receipts with
   bucket/key/object version/length/SHA256. Full revision identity binds original
   accepted bytes; selection decoration/projection hashes are separate.
2. Account census: exact canonical and vendor account IDs, selected membership,
   counts before/after documented grain collapse, missing/outside-boundary rows,
   completeness/value statuses. A zero-row account needs affirmative same-date
   empty-account evidence, not an absent partition or missing join.
3. Position: stable source position identity with source grain/side and retained
   row provenance; account, canonical and vendor security identifiers plus
   resolution revision; signed finite quantity and USD/native value, declared
   currency, cash/debt classification and actual value status. Preserve zero and
   negative rows. Ambiguous/unresolved identifiers remain findings and cannot
   enter an analysis recipe as invented ticker IDs.
4. Valuation: vendor authoritative account total and method, nonoverlapping cash
   and liability components, signed economic decomposition, explicit accrual
   treatment. Price/quantity/factor/date/source receipts are required only where
   share conversion is requested; sourced USD values do not require a quote.
5. Acceptance: per-account reconciliation equation, input/unique/output counts,
   unknown/null/nonfinite/duplicate counts, residual and approved tolerance,
   comparison vintages and independent/shared derivation label. Known-value
   subtotal is never labeled the complete account total when unknowns remain.

The current HoldingsSnapshot node schema has additionalProperties=false and no
complete price/quantity receipt surface. P integrates any shared schema revision;
M cannot attach undocumented fields. Existing retained publication versions and
source digest validation should be reused, but snapshot-id-to-immutable-revision
authorization remains an explicit missing callback. No same-day corrected
publication may silently satisfy a request for an older snapshot revision.

## Acceptance and downstream gate

Proposed IRPT publication gate requires all selected accounts admitted, no hidden
unknowns, documented collapse with conserved economics, independent same-vintage
per-account reconciliation and immutable source receipts. Existing B03 1bp
provisional flags are evidence only: do not silently treat their tolerance or
VARIANCE-EXPLAINED state as an IRPT gate. Retain the approved IRPT policy or obtain
an explicit tolerance ruling before acceptance; never tune to green the data.
Cash/short/factor and accrual equations must be firm-specific and reviewed.

Later local candidate validation must include cash-only and truly empty accounts,
zero and negative positions/net values, offset long/short, missing/nonfinite
values, duplicate or conflicting security/relationship rows, missing selected
accounts, source vintage skew, changed object revision, COT partial-null and
conflicting roster totals, INF false zero and absent identity, and 49F factored
prices/cash overlap. Each mutant must refuse or preserve an explicit incomplete
result before any pointer advance. A same-input replay must preserve revision
identity; retained old snapshot retrieval must not drift after correction.
Tests are proposed here, not run or claimed as producer acceptance.

Y message `20260923T153024Z` reported signed policy proposal LOCAL `5d7da1aa49`.
CTO message `20260923T153215Z` directed its incorporation; the exact adjudication
was read at `7a3fd28e11` in
`org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/LOCAL_LIVE_PARTNER_SCOPE_20260923.md`.
The adopted boundary preserves exact signed/zero source facts and refuses the
whole selected portfolio under the present positive-only recipe when any original
row is unsupported, BEFORE equal-security or account consolidation. No abs,
drop, net, invented cash or target substitution; positive net cannot hide shorts.
A valid custody snapshot remains representable even when this recipe refuses it.

No global positive-helper relaxation, historical frozen-request mutation, new
artifact family or public refusal enum is proposed. Preserve current supported
refusal envelopes; P owns future public mappings. Y must identify the concrete
producer interface before implementing its owned eligibility controls. Signed
recipe/reporting completion remains unproven. Both production callbacks remain
unconfigured/refusing until exact accepted identity and complete security source
are implemented and directly reviewed by CTO. Local factory/parser review
`8653eb6cd4` accepts only its tested boundary, not production/live acceptance.
The same ruling file records Andrew's direct-review instruction: CTO is the
reviewer for this resumed work, superseding earlier separate CVO requirements.

## Compiler and validation receipt

Bare comp-which preceded source inspections. The routed comp-dataflow origin
on 49F B01 extracted zero reads because IO is delegated through runner_common;
that bounded AST result is not absence of IO. Bare comp-pipescript IO did not
resolve these B01 runner names in bd/cot/inf catalogues. Exact scoped source
reads plus twelve pinned-file AST inventories resolved the source paths.
All twelve working files matched pinned bytes after newline normalization.
No source module import, producer invocation, cloud read/write or implementation
test was performed for this proposal. Only M evidence/status files are changed.
