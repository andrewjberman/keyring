# Custody interpreter -- design (Y's cell, Analysis custody branch)

Author `2.0.0_SA_COO~Y`, 2026-09-24 ~13:3xZ. Assignment: CTO batch 48 ("the interpreter is Y's cell on return"),
100609 (order of acts), 100619 (Q3 accepted), 100639 (zero-lot rule and the direct totals read accepted).
Inputs: P's card v2 `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/CUSTODY_INTERPRETER_DESIGN_CARD_20260924.md`
@4480b55e39; M's record `.../IRPT_MVP_M/CUSTODY_SOURCE_OF_RECORD_Q1_Q4_20260924.md` @ab16d8e750 plus its
CORRECTION (100643). Contract: `intake/custody_portfolio.py` `_validated` (:135-215) and `economics` (:69-123)
at Y 93ec16f4fe; the reader `_scope/accepted_custody.py` and the store `_scope/custody_binding.py` on P's branch
@irpt-smoke-p-backend-20260923.

Nothing here is deployed. No composition, grant or deploy happens until P's ledgered FIRM-bucket grant plan.

## 1. What is built

One module, `infra/aws/lambda/investor-reporting/intake/custody_interpreter.py` (Y lane), exporting a factory:

    build_custody_ports(get_object, *, firm_rules=COT_V1) -> (interpret_source, validate_evidence)

- `get_object(bucket, key, version_id) -> bytes` is the ONLY I/O port. P's composition installs it over S3 with the
  generate role's planned grants; the offline oracle installs it over a fixture. No boto3 import in this module.
- `interpret_source(document, manifest, *, principal, owner, publication_receipt)` returns exactly
  `{actual_custody, original_rows, source_receipts, revision_refs}` (the reader's EVIDENCE_FIELDS).
- `validate_evidence(evidence, *, principal, owner, publication_receipt)` returns True only when the evidence
  meets the full paired contract (section 6); anything else returns False, never raises past the reader.

Both are real implementations over receipted objects. There is no fake validator and no default source.

## 2. Firm scope in v1

Built for all three firms at Y b398d27731; the PRODUCTION DEFAULT admits COT only, and an installer passes
`admitted_firms` for 49F and INF once the CTO reads the pin. Per-firm rules (measured Y 100671, ruled CTO 100675 /
100686 / 100695, producer lines M 100693 / 100699):

| firm | rows / totals | grain | cash | accrual |
|---|---|---|---|---|
| COT | fact_holdings / fact_allocations "Account Market Value" | AssetID (relationship duplicates collapse) | Symbol CASH -> CASH; Cash Equivalent -> CASH_EQUIVALENT | reported, INCLUDED |
| 49F | dim_position / dim_balance.net_mv_positions (positions only; cash is not a position row) | (CUSIP, accounting_rule_code, tax_code); same-security positions consolidate in the freezer | NOT_REPORTED_BY_SOURCE | NOT_REPORTED_BY_SOURCE |
| INF | positions_mv / accounts_v2.current_value | native position id | is_custodial_cash -> CASH row, else NON_CASH | NOT_REPORTED_BY_SOURCE |

Shorts (49F l_s "S") and every negative or unpriced row refuse `CUSTODY_UNSUPPORTED_ROWS`; zero lots are excluded
at every firm; INF inactive rows are ordinary rows (all 1,701 are zero-valued and outside accounts_v2).

## 3. Reading the receipted objects

From `manifest.source_objects` (the served revision manifest; it carries no custody control row -- CTO 100639,
M 100643), select by key shape:

| role | key pattern (COT) | used for |
|---|---|---|
| `CUSTODY_ROWS` | `blackdiamond/cottonwood/silver/fact_holdings/date=<business_date>/data.parquet` | original_rows, positions |
| `INDEPENDENT_TOTALS` | `blackdiamond/cottonwood/silver/fact_allocations/date=<business_date>/data.parquet` | reconciliation.independent_value |

Exactly one object per role, bucket `opal-data-assets`, partition date == `publication_receipt.business_date`
(the producer's vintage rule, holdings_snapshot.py:1864-1865). Each is fetched BY VERSION, and its bytes must
match the receipt's `sha256` and `byte_length`, else `CustodyOwnershipRefused` (the reader re-raises it).
The manifest itself is the third receipt (`PUBLICATION_MANIFEST`), taken from `publication_receipt.date_row.manifest`.

## 4. Row admission (COT v1), in order, per selected account

The selected set is `owner.account_ids` (opaque). A raw row belongs to account `a` iff
`_ids.opaque("account", "cottonwood", AccountID) == a`. Rows are read in physical order; `row_index` is the
zero-based physical ordinal in the object (the producer's origin grammar, :1876).

1. NO-POSITION (producer rule, authority 5ee54ac0d4 / f307d58415): Market Value, Units, Unaccrued Market Value
   and Accrual all null -> excluded. Measured: Anna 21 of 78; firm 5,694 of 19,610; 0 partial-null rows.
2. ZERO LOT (Y rule, ACCEPTED 100639): Market Value exactly 0 AND Units exactly 0 -> excluded. Anna 2; firm 1,341.
3. Refusals, checked after 1-2 over the remaining active rows of the selected accounts:
   - `CUSTODY_ACCOUNT_NOT_IN_SOURCE` -- a selected account has no physical row, or no active row after 1-2 (Q3).
   - `CUSTODY_UNSUPPORTED_ROWS` -- an active row with Market Value < 0 (a debit; firm 29 rows), or Market Value 0
     with Units > 0 (unpriced; firm 9 rows), or any partial-null row. The COUNT is named; never an id or a value.
   - `CUSTODY_SECURITY_UNIDENTIFIED` -- an active positive row with neither Ticker nor CUSIP (firm 156 rows; Anna 0).
   - `CUSTODY_INDEPENDENT_TOTAL_ABSENT` / `CUSTODY_INDEPENDENT_TOTAL_CONFLICT` -- no totals row for a selected
     account, or its rows disagree (the producer refuses the same at :433-436).
   - `CUSTODY_RECONCILIATION_FAILED` -- the admitted position sum differs from the independent value by > 0.01 USD.
   The public spelling of each code is P's (build_entry vocabulary, hop 4b shape).
4. Numbers: every float64 cell becomes decimal text by `Decimal(str(value))`, the producer's own rule
   (holdings_snapshot.py `number`). Measured: 12,537 of 12,537 positive rows decompose EXACTLY
   (Market Value == Unaccrued Market Value + Accrual), which the contract requires (custody_portfolio.py:108-110).

The exclusions are recorded, not silent: `revision_refs.economic_policy.revision` carries the rule id and a
sha256 over the sorted list of excluded `(source_receipt_id, row_index, reason)` for the selected accounts.
`revision_refs` values are closed to `{revision, source_receipt_id}` (custody_binding.py validate_payload), so the
digest, not a list, is what fits; a grader re-derives the list from the receipted object and compares digests.
(The CTO's 100639 wording "origin recorded ... in revision_refs" is met in this digest form.)

## 5. Output mapping (against `_validated`)

Per admitted row (an original row), with `R` = the CUSTODY_ROWS receipt id:

| field | value |
|---|---|
| `account_id` | the opaque account id |
| `position_id` | `cpos_` + sha256("irpt-custody-position|cottonwood|<account_id>|<asset token>")[:24] |
| `source_security_id` | `{namespace: "COT_ASSET", value: <asset token>}`; asset token = `ast_` + sha256("irpt-custody-asset|cottonwood|<AssetID>")[:24] -- a private token inside the evidence, never a new estate id space (`_ids.KINDS` has no asset kind and refuses undeclared kinds) |
| `market_value` | `{value: <Market Value text>, currency: "USD"}` (COT currency is the attested authority, as the producer binds it) |
| `quantity` | `null` (COT Units are not asserted as SHARES; the Analysis thread's unit is normalized dollars) |
| `economic_facts.cash` | `{source_field: "Cash Equivalent", source_value: <bool>, classification, evidence: [R,row]}`; classification `CASH` iff Symbol == "CASH" (measured 45 rows firm-wide, all Cash Equivalent true), else `CASH_EQUIVALENT` iff Cash Equivalent true, else `NON_CASH` |
| `economic_facts.side` | `{source_field: null, source_value: null, position_side: "LONG", sign_rule_revision: "cot-positive-market-value-long-v1", evidence}` |
| `economic_facts.security` | `resolved_identifier`: `{CASH, "$:CASH"}` for a CASH row, else `{TICKER, Ticker}` when present, else `{CUSIP, CUSIP}`; `security_key` = `<namespace>:<value>`; `resolution_revision` = "cot-custody-identifier-v1"; `resolution_source_receipt_id` = R; `evidence` [R,row] |
| `economic_facts.source_quantity` | `{value: <Units text>, source_field: "Units", source_units: "COT_UNITS", unit_rule_revision: "cot-units-as-reported-v1", evidence}` |
| `economic_facts.accrual` | `{treatment: "INCLUDED_IN_MARKET_VALUE", value: <Accrual text>, unaccrued_market_value: <Unaccrued text>, rule_revision: "cot-accrual-included-v1", evidence}` |
| `source_row` | `{source_receipt_id: R, row_index, relationship_id: _ids.opaque("relationship", "cottonwood", Relationship ID)}` |

Positions: one per (account, AssetID); `source_rows` = every admitted row of that group (relationship duplicates;
the producer refuses incompatible duplicates at :413-420, so `same_facts` holds). Firm: 71 duplicate groups;
Anna 0.

`actual_custody`: `schema_version` "irpt-actual-custody-cot-v1"; `firm_id`; `custody_as_of` = `valuation_as_of`
= `publication_receipt.business_date`; `account_ids` = owner's (sorted); `positions`; `census` one row per
account (`raw_row_count` = admitted rows, `unique_position_count`, `duplicate_relationship_row_count` =
difference, `unsupported_original_row_count` 0, `conflict_original_row_count` 0, `COMPLETE`, evidence null);
`reconciliation` one row per account (`position_value` = sum of position market values; `independent_value` =
the account's Account Market Value text; `absolute_difference`; `tolerance_usd` "0.01"; `currency` "USD";
the two as-of dates; `independent_source_rows` = every totals row ordinal for the account under the
INDEPENDENT_TOTALS receipt id -- Anna has two equal rows).

`source_receipts` (validate_payload shape): three entries `{source_receipt_id, role, account_ids, object,
row_count}` -- CUSTODY_ROWS (row_count = physical rows of the selected accounts, before exclusion),
INDEPENDENT_TOTALS (row_count = totals rows of the selected accounts), PUBLICATION_MANIFEST (row_count 0,
account_ids = owner's). Receipt ids are `src_` + sha256(canonical object reference)[:24].

`revision_refs` (exactly the six keys): `account_mapping` ("_ids.opaque account, ID_NAMESPACE v1", R),
`security_mapping` ("cot-custody-identifier-v1", R), `economic_policy` ("cot-custody-economics-v1;
no-position=5ee54ac0d4; zero-lot=Y-100633/CTO-100639; excluded=<sha256>", R), `numeric_policy`
("decimal-of-str-float64-v1", R), `publication_policy` (the manifest revision dec293d6.., the manifest receipt
id), `source_set` (sha256 of the manifest's `source_set_revision` canonical bytes, the manifest receipt id).

## 6. validate_evidence

Pure; no I/O. True iff all hold:
1. keys are exactly EVIDENCE_FIELDS; `source_receipts` and `revision_refs` pass the same shape rules as
   `custody_binding.validate_payload`; roles are exactly {CUSTODY_ROWS, INDEPENDENT_TOTALS, PUBLICATION_MANIFEST};
   the PUBLICATION_MANIFEST object equals `publication_receipt.date_row.manifest`;
2. every `source_row` / fact `evidence` names the CUSTODY_ROWS receipt; every `independent_source_rows` entry
   names INDEPENDENT_TOTALS;
3. `_validated` admits the evidence when wrapped with the owner (the three top revisions are carried as the
   receipt's revision and digests of the evidence; `_validated` does not grade them beyond 64-hex);
4. the revision texts are exactly the admitted rule ids of section 5 (a changed rule is a new revision, never
   silently accepted);
5. `actual_custody.custody_as_of` == `publication_receipt.business_date`.

## 7. The offline oracle

A structural twin of Anna's capture: two parquet files written by the test from Anna's measured counts --
78 rows, 21 no-position, 2 zero lots (one Cash Equivalent), 55 positive with Ticker, 0 duplicates, one
relationship, exact decomposition, two equal totals rows -- with SYNTHETIC values that tie within 0.01 and
synthetic raw ids. No real value, id or name enters the repo. The fixture's manifest carries the served key
shapes. Arms: (a) the twin admits: 55 positions, census and reconciliation as above, `_validated` passes,
`freeze_accepted_custody` produces a frozen document; (b) each refusal code fires on a one-row mutation of the
twin (a negative row, MV0-with-units, a partial-null row, a missing Ticker and CUSIP, a missing totals row,
conflicting totals, a 0.02 tie break, a selected account absent); (c) a byte flip in either object refuses on
the receipt; (d) `validate_evidence` rejects each of: a wrong role, a foreign receipt id in a row, a changed
rule revision, a date mismatch; (e) the reader round-trip: `AcceptedCustodyReader.create` then `read` with an
in-memory store and publication double returns equal results (economics digest stable across reads). Arm (e)
needs `_scope/accepted_custody.py` and `_scope/custody_binding.py`, which exist only on P's branch, so it ships
as its own test file that runs in P's tree at integration (Y runs it there during review); arms (a)-(d) run on
the Y branch.

## 8. What this does not do

No stub, no fake validator, no vendor call, no write, no Terraform. It does not publish anything or widen
`_validated`. 49F and INF refuse until measured. The composition (store, publication port, selection
re-shaping, grants) is P's hour after the ledgered plan; the first live Analysis submission is Andrew's
browser act.
