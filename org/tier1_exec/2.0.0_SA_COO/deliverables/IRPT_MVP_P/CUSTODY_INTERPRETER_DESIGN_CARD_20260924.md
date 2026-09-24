# DESIGN CARD -- the accepted-custody ECONOMIC INTERPRETER for the Analysis custody branch ((i-b))

Author 2.0.0_SA_COO~P, 2026-09-24 12:2xZ, on 1.0.0_SA_CTO 100558 (2): "P drafts the interpreter's
DESIGN CARD NOW, as an act ... the inputs, the output, the open questions named plainly." Nothing here is
built; nothing is stubbed. Every shape below is READ from one live capture of M's served Cottonwood
publication for Anna Thiessen's account `acc_d486fc9455d6b2aa18e13af1` (read-only S3 through
`holdings/publication.py:HoldingsPublication`, no vendor, no write; keys and counts printed, values not).

## 1. What the branch needs (Y's code, at irpt-smoke-p-backend-20260923 HEAD)

`ycharts/generate/custody_submission.py:140` `build_accepted_custody_entry(reader, **ports)` binds ONE
`_scope/accepted_custody.py:AcceptedCustodyReader(store, *, current_selection, publication_for,
interpret_source, validate_evidence)`. `read()` / `create()` (:96-155) call
`publication_for(firm).capture(as_of, account_ids)` (create) or `.load_pinned(receipt, account_ids)` (read),
then `interpret_source(document, manifest, principal=, owner=, publication_receipt=)` which must return
EXACTLY `{actual_custody, original_rows, source_receipts, revision_refs}` (:14, :66), then
`validate_evidence(evidence, principal=, owner=, publication_receipt=) is True` (:77). Anything else
refuses `CustodyOwnershipRefused`. The docstring (:27-28): "Both economic ports are mandatory for
acceptance and intentionally have no default implementation. A fake/local validator is not a deployed
capability." Repo-wide census: 0 implementations (P 100556; CRO addendum 2 on a second instrument).

The evidence then passes `intake/custody_portfolio.py:135-215 _validated(accepted, owner)` inside
`AcceptedCustodyNormalizer.load_normalized` -- the closed contract in section 3.

## 2. The INPUT, measured (M's publication, manifest v2, business_date 2026-09-22)

| object | shape (keys) | for Anna's account |
|---|---|---|
| index `irpt/cottonwood/platinum/holdings/current/manifest.json` (bucket `opal-data-cottonwood`) | `dates, firm_id, latest_date, schema_version`; date row `{revision, manifest}` | 1 date, latest 2026-09-22 |
| manifest (`<revision>.manifest.json`) | `business_date, clocks{as_of_timestamp, business_date, custody_as_of, overlay_as_of, source_as_of}, firm_id, gold{bucket,key,version_id,sha256,byte_length}, partitions[{account_ids, object}], platinum_header{ref}, revision, schema_version=irpt-holdings-manifest-v2, source_objects[8 x {bucket,key,version_id,sha256,byte_length}], source_set_revision` | 24 partitions; `custody_as_of == business_date` |
| document (selected parts) | `attribution_holdouts{assigned_without_custody, reconcile, unassigned}, clocks, coverage{nodes_attempted, nodes_resolved, remainder{amount, reason, units}}, custody_totals{deduplicated, total_market_value{currency,value}, unique_account_count, unique_position_count}, nodes[], scope{account_ids, firm_id, resolved_scope_fingerprint}, source_set_revision` | scope.account_ids = the FIRM's full list (841 accounts), not the selection; custody_totals: 841 accounts, 14,426 unique positions, USD, deduplicated; coverage 462 of 841 resolved ("carry an assigned Rebalancer strategy"); holdouts 3 / 5 / 7 |
| nodes for the one account | 75: ACCOUNT 1, SLEEVE 1, MODEL_WRAPPER 1, MODEL_LEAF 4, SECURITY 68. Every node: `amount{value, units, denominator{kind..}}, basis, classification{advisory_status, authoritative, capability_facts, fee_taking_status, hierarchy_path, vendor_account_supervised}, clocks{custody_as_of, overlay_as_of}, display{description, label, symbol}, level, node_id, node_kind, parent_node_id, percentages, provenance{claim, join_attempted, join_matched, join_method, producer}`; SECURITY adds `security_id{namespace, value}` and `valuation_facts[{fact_kind, source_as_of, source_revision, source_scope, units, value}]` | provenance.claim `measured` on 75 of 75; producer `holdings_snapshot.build_cot` |
| provenance.join_method (the load-bearing column) | `fact_holdings (Market Value, deduped DC1)` x1 (the ACCOUNT node); `fact_model_assignment strategy_name -> fact_model_roster` x1; `fact_model_blend child of the assigned strategy; account value x absolute_allocation` x4; `component of <Opal model> (fact_model_definition); account value x component weight` x67; `account value minus assigned constituent leaves (the plug)` x1 | **0 of 68 SECURITY nodes join a custody row.** |

THE MATERIAL FINDING: for an account with an assigned Rebalancer strategy (Anna's; 462 of 841 at
Cottonwood), the publication's SECURITY nodes are MODEL-IMPLIED allocations (account market value x
component weight), not held positions. The only custody FACT at node grain is the ACCOUNT node's market
value (`fact_holdings, deduped DC1`). Position-grain custody facts exist in the source (custody_totals
counts 14,426 unique positions firm-wide; the gold parquet `manifest.gold` and the 8 `source_objects`
carry them) but the served document does not present them as nodes for an assigned account. So an
interpreter that reads ONLY the document cannot produce `original_rows` / `positions` that are
custody rows; it would have to read the gold parquet (or the fact_holdings source objects the manifest
receipts) for the selected accounts.

## 3. The OUTPUT contract (Y's `_validated`, quoted by rule, :135-215)

- `accepted_custody_input-v1`: `owner` (custody-owner-v1, OPAL_GLOBAL, home opal-capital, advisor null),
  `snapshot_id` == owner.snapshot_id, `snapshot_revision` / `binding_revision` /
  `selected_account_set_fingerprint` 64-hex, `ownership_fingerprint` = sha256(canonical owner minus itself).
- `actual_custody`: closed `{schema_version, firm_id, custody_as_of, valuation_as_of, account_ids, positions,
  census, reconciliation}`; `custody_as_of == valuation_as_of` (ISO dates); `account_ids` == owner's, sorted, unique.
- `original_rows` (1..MAX_ROWS): closed `COMMON | {source_row}`; each `account_id` in the set; `economics(row)`
  admits; `reference(source_row, relationship=True)` unique across rows.
- `positions` (1..MAX_ROWS): closed `COMMON | {source_rows}`; unique `(account_id, position_id)` and
  `(account_id, source_security_id.namespace, .value)`; every `source_rows` entry references a distinct
  original row whose `source_row` equals it, and `same_facts(position, original)` holds; the union of
  references == the set of original rows (nothing uncovered, nothing extra).
- `census`: one row per account, closed `{account_id, raw_row_count, unique_position_count,
  duplicate_relationship_row_count, unsupported_original_row_count, conflict_original_row_count, completeness,
  empty_account_evidence}`; completeness `COMPLETE`, evidence null, counts exactly derived from the rows.
- `reconciliation`: one row per account, closed `{account_id, position_value, independent_value,
  absolute_difference, tolerance_usd, currency, custody_as_of, valuation_as_of, independent_source_rows}`;
  `currency USD`, `tolerance_usd "0.01"`, `position_value` == the summed position economics,
  `absolute_difference` == |sum - independent_value| <= 0.01, `evidence(independent_source_rows)` admits.
- plus `source_receipts` and `revision_refs` (immutable receipts the reader re-verifies on every read: :144-147).

## 4. The MAPPING this card proposes (each line is a question until Y or the CTO rules)

| output | proposed source | open question |
|---|---|---|
| `custody_as_of` / `valuation_as_of` | manifest.clocks.custody_as_of (== business_date, measured) | none |
| `account_ids` | the owner's selected set (validated against scope and the partitions' account_ids) | none |
| `original_rows` | the fact_holdings rows for the selected accounts at the receipted revision, read from `manifest.gold` (parquet) or the `source_objects` the manifest receipts -- NOT from the document's SECURITY nodes | Q1: which object is the custody row source of record for a v2 publication -- the gold parquet or a source_object? (M) |
| `positions` | the same rows collapsed to `(account, security)` grain with `source_rows` back-references | Q2: for an ASSIGNED account, is the accepted custody the held positions (custody rows) or the model-implied allocation the page shows? The contract says custody rows; the page shows the model. (Y + CTO) |
| `census` | derived from the rows (counts), `COMPLETE` only if every selected account has >= 1 row | Q3: an account with 0 custody rows (a cash-only or empty account) cannot be COMPLETE by `_validated` -- refuse, or is that Y's `empty_account_evidence` path? (Y) |
| `reconciliation.independent_value` | the ACCOUNT node's `amount.value` (the `fact_holdings (Market Value, deduped DC1)` join -- the custodian's own account total), with that node as `independent_source_rows` | Q4 (the CTO's question): is the custodian's account-level market value INDEPENDENT of the position rows it is summed from? It is a separate fact table row (DC1 dedupe), so the CTO's leaning (the custody fact tables' receipted values are the independent source, the publication's own row the evidence) holds if M confirms `fact_holdings` account value is not derived from the position rows in the same build. (M) |
| `source_receipts` / `revision_refs` | manifest.source_objects (8 refs with version_id + sha256), manifest.gold, the receipt's index ref, source_set_revision | none -- these are exactly the immutable refs the reader re-verifies |

## 5. Where it lives, what it costs, what it must NOT do

- Lane: the interpreter is Y's semantics (`intake/` or `_scope/`, beside custody_portfolio.py); M supplies
  the row-source answer (Q1) and the independence answer (Q4); P composes (the hour: CustodyBindingStore on
  IRPT_REQUESTS_TABLE, HoldingsPublication(s3, firm), the (principal, owner) re-shaping of
  `holdings/entry.py:_current_selection` through `_scope/selection_store`, the ports the prospect branch
  holds) and deploys (the generate role needs GetObject on `opal-data-<firm>/irpt/<firm>/platinum/holdings/*`
  and `.../gold/holdings/*` plus KMS via S3 -- the publication lives in the FIRM buckets, not opal-data-irpt;
  and PutItem on irpt-requests for the binding row).
- Tests: Y's doubles in `_scope/tests/test_custody_binding.py` and `ycharts/generate/tests/test_custody_retained.py`
  show the shapes; the interpreter's arms are one real capture replayed offline (record the document / manifest
  / receipt for Anna's account as a fixture) plus `_validated` as the oracle.
- It must NOT: invent a position from a model weight; accept a publication whose account has 0 custody rows as
  COMPLETE; reconcile a value against itself; run before the composition's grants are planned and applied
  under a ledger.
- Cottonwood specifically: the data window starts ~2026-04-22 (COT in BD is a sliver before May 2026; box
  memory); the first live custody submission on Anna's account reads the 2026-09-22 publication, inside the window.

## 7. v2 -- 2026-09-24 12:5xZ: Q1, Q2, Q4 RULED; the two moved rows; one design across three firms

Authority: 2.0.0_SA_COO~M's answers (org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/CUSTODY_SOURCE_OF_RECORD_Q1_Q4_20260924.md,
every claim file:line @ commit: holdings_snapshot.py @d96513bc40, holdings_49f.py @d96513bc40, holdings_inf.py @fb87f34940) and
1.0.0_SA_CTO's rulings (batch 48: Q2; batch 50: Q1, Q4). Q3 stays with 2.0.0_SA_COO~Y (the CTO's provisional read: a selected
account with 0 custody rows REFUSES by the contract as written; widening is Y's amendment).

**Q2 (ruled, batch 48):** the ACCEPTED CUSTODY is the HELD POSITIONS -- the custody rows for the selected accounts at the
receipted revision -- never the model-implied allocation the page shows for an assigned account. The document's nodes are
consulted for scope, clocks and receipts only.

**Q1 (ruled, batch 50) -- the row `original_rows` / `positions` MOVES:** the source of record is the ONE receipted custody
object in `manifest.source_objects` that the builder reads rows from, NEVER `manifest.gold` (the gold parquet is the
document flattened: one row per node, the same model-implied SECURITY nodes -- reading it reproduces 0-of-68 under another
name). The served v2 SECURITY nodes' CUSTODY_UNITS fact (`source_revision` = the receipted object's sha256,
holdings_snapshot.py:550-579) is a pointer to the object, not a row reference; the interpreter reads rows from the object.

**Q4 (ruled, batch 50; the CTO's leaning WITHDRAWN) -- the row `reconciliation.independent_value` MOVES:** the ACCOUNT node's
`fact_holdings (Market Value, deduped DC1)` amount is the POSITION SUM (holdings_snapshot.py:422-423, :1932-1933, :1990) --
correct to the cent, a derivation of the same rows, NOT independent. The independent custodian-supplied total is its own row
in a second fact table, `fact_allocations/date=<total_date>/data.parquet` column "Account Market Value" per AccountID
(:429-437; served receipt WeqLRnnX.., 1,495 rows), which the build already ties to the position sum within 0.01 USD or
REFUSES (:446-449) and writes into `manifest.actual_custody_controls.reconciliation` as {account_id, position_value,
independent_value, difference, independent_source_row_ordinals, independent_source_origins} (:450-454, :2099; origins =
(s3 url of totals_key, ordinal) :1877). So `independent_value` = fact_allocations "Account Market Value" for the account at
the receipted revision and `independent_source_rows` = that totals row reference, read from the served manifest's control
row and re-verifiable against the receipted object. The ACCOUNT node is NOT cited as the independent source.

| firm | rows object (original_rows / positions) | identity columns the rows carry | source_row reference | totals object (independent_value) | totals column |
|---|---|---|---|---|---|
| cottonwood (COT) | `opal-data-assets/blackdiamond/cottonwood/silver/fact_holdings/date=<value_date>/data.parquet` (holdings_snapshot.py:1871-1873; served dec293d6 receipt tGurdOTY.., 457,679 B) | AccountID (raw -> opaque_id("account", firm, AccountID) :1978), AssetID / Symbol / Ticker / CUSIP / Asset Name / Asset Display Name / Relationship ID / PortfolioID, Market Value, Units, _source_as_of | (object url, zero-based physical row ordinal), holdings_origins :1876; kept per position as source_row_ordinals + relationship_ids :424-427 after the DC1 collapse :412-421 | `.../silver/fact_allocations/date=<total_date>/data.parquet` (totals_key :1872, read :1874; served receipt WeqLRnnX.., 128,660 B) | "Account Market Value" per AccountID (:429-437; conflicting duplicates refused) |
| 49financial (49F) | `schwab/08335338/silver/dim_position` (holdings_49f.py:184 loader, :416-417 row -> node) | account_id, cusip / ticker_symbol / isin, market_value_settled_unsettled, quantity_settled_unsettled | row ordinal within the account group | `dim_balance` (holdings_49f.py:183, :284; DRILL WITHHELD on a miss :403-411) | net_mv_plus_cash |
| inflection (INF) | `opal-data-inf/silver/api_dims/positions_mv` (holdings_inf.py:145-151, :312-313) | account_id, id, product_id, ticker, current_value, current_shares | the Orion row id | `accounts_v2` (holdings_inf.py:150, :273) | current_value |

Consequences for section 5 (the composition, still GATED behind a planned ledger): the generate role's read set is per FIRM
and per OBJECT -- the rows object AND the totals object each firm's manifest receipts (COT's live under
`opal-data-assets/blackdiamond/cottonwood/silver/...`, not the cottonwood platinum prefix; 49F under the schwab silver
prefix; INF under `opal-data-inf/silver/...`) plus the platinum publication index / manifest / parts and KMS via S3 -- so the
cross-firm gate's enumeration (`.tools/ds-precommit-check.py` `_CROSS_FIRM_FOREIGN_*`) is read BEFORE the plan and the plan
names every firm bucket it touches. The offline oracle records keys and counts of BOTH objects for Anna's account, never
values. No code is cut on this card until the grants are applied under a ledger; Y's cell owns the interpreter.

## 8. v2 -- 2026-09-24 13:0xZ: Q3 RULED by 2.0.0_SA_COO~Y (accepted by the CTO); the card is CLOSED on all four questions

**Q3 (Y, 100612; CTO 100614 accepted; M 100615 one per-firm note):** a selected account with 0 admissible custody rows
REFUSES the submission with a named reason and the selection is re-cut; the contract is NOT widened --
`empty_account_evidence` stays reserved and null in v1 (custody_portfolio.py:201). Producer facts: M's COT build already
refuses "account census differs from independent totals; missing is not empty" (holdings_snapshot.py:438-439 @d96513bc40)
and an expected account absent from BOTH inputs (:440-443); cash is a custody ROW, not an absence; an empty account
contributes nothing a vendor upload can carry. Per firm (M): at 49F a custody account with 0 dim_position rows is still
built (a dim_balance row -> a CASH remainder node), so the interpreter's refusal fires on the ROWS OBJECT, never on the
served tree.

**The two refusal classes and their PUBLIC spelling (P rules, as the card's owner):** internal classes
`CustodyAccountNotInSource` (the selected account has no row in the receipted rows object) and `CustodyUnsupportedRows`
(rows present, none admissible; the COUNT is carried, never ids or values); both are INPUT refusals on the selection and
answer the closed vocabulary's `INVALID_INPUT` (the same public code the upload validator's refusals use), never
NOT_AUTHORIZED (authority is not in question) and never UNEXPECTED; the sink records the class and the count. The
selection is re-cut by the viewer without the account.

**NAMED OPEN (the CTO, 100614):** the mixed-rows case -- positive rows beside Market Value <= 0 lots -- is measured on
Anna's account first (keys and counts from the receipted rows object) before the admissibility rule is written; it is
not decided here.

## 6. What this card does not decide

The first live Analysis submission (100554 (b)) stays Andrew's browser act on whichever composition lands
first; the prospect upload's two egress questions are on Andrew's card; this card carries NO egress question.
