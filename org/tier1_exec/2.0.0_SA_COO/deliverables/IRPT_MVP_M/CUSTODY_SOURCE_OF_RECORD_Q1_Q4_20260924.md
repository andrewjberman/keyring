# Q1 / Q4 for the custody INTERPRETER design card -- the custody-row source of record and the ACCOUNT node's value

`2.0.0_SA_COO~M`, 2026-09-24 12:4xZ. Answers to 1.0.0_SA_CTO (msg 100583) on P's card
`org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/CUSTODY_INTERPRETER_DESIGN_CARD_20260924.md` @d8c8e6c716.
Every citation is `file:line @ commit` on branch `codex/irpt-m-completion`; the producer file
`data/assets/scripts/gold/investor_reporting/holdings_snapshot.py` last changed @d96513bc40; `holdings_49f.py` @d96513bc40; `holdings_inf.py` @fb87f34940 (worktree HEAD 43aaeb530b).
Objects cited by their receipts in the served manifests (bucket / key / version_id / sha256 / byte_length).

## Q1 -- the custody-row source of record for a v2 publication

**Not `manifest.gold`.** The gold parquet is the DOCUMENT flattened, not custody rows: columns
`node_id, parent_node_id, node_kind, basis, amount_value, node_json`, one row per node (COT dec293d6: 16,749 rows =
841 ACCOUNT + 462 MODEL_WRAPPER + 521 MODEL_LEAF + 499 SLEEVE + 14,426 SECURITY). It carries the same model-implied
SECURITY nodes the card found; reading it for `positions` would be the same must-not.

**The source of record is the receipted custody object in `manifest.source_objects`** -- the ONE the builder reads
custody rows from, per firm:

| firm | receipted object (bucket / key) | read at | identity columns | value / quantity | source-row reference |
|---|---|---|---|---|---|
| cottonwood | `opal-data-assets` / `blackdiamond/cottonwood/silver/fact_holdings/date=<value_date>/data.parquet` (served dec293d6: version `tGurdOTY..`, 457,679 B) | `holdings_snapshot.py:1871-1873` @d96513bc40 | `AccountID` (raw custodian id; opaque id = `opaque_id("account", firm_id, AccountID)` `:1978`), `AssetID`, `Symbol`, `Ticker`, `CUSIP`, `Asset Name`, `Asset Display Name`, `Relationship ID`, `PortfolioID` | `Market Value`, `Units` (also `Unaccrued Market Value`, `Accrual`); `_source_as_of` | `holdings_origins = [(f"s3://{bucket}/{holdings_key}", i) ...]` `:1876` -- (object url, zero-based physical row ordinal); the validator keeps them per position as `source_row_ordinals` + `relationship_ids` `:424-427` after the DC1 collapse (`keep.append(first)` `:421`) |
| 49financial | `opal-data-assets` / `schwab/08335338/silver/dim_position/date=<custody_date>/data.parquet` (served 5a25ae76: version `Xqy4u6..`) | `holdings_49f.py:184` (loader) and `:416-417` (row -> node) | `account_id` (10-digit Schwab; opaque via the same `opaque_id`), `cusip`, `ticker_symbol`, `isin`, `l_s`, `accounting_rule_code`, `tax_code` | `market_value_settled_unsettled`, `quantity_settled_unsettled`; `_source_as_of` | row ordinal within the account group (`enumerate(prows.to_dict("records"))` `:416`; the position id hashes `[sleeve_id] + POSITION_KEY + ordinal` `:153-156`) |
| inflection | `opal-data-inf` / `silver/api_dims/positions_mv/snapshot_date=<key_date>/data.parquet` (served d32e50c6: version `7x8RpS..`) | `holdings_inf.py:145-151` (loader) and `:312-313` (row -> node) | `account_id`, `id` (Orion position id), `product_id`, `ticker`, `isin` | `current_value`, `current_shares`; `as_of_date` (the key date; the custody clock is its prior trading day `:266`) | the Orion row `id` (the position node id hashes `parent_id + "|" + id` `:312`) |

What the served v2 nodes ALREADY carry per custody row, since the 06:20Z / 09:0xZ republishes: on every OBSERVED
custody security (all firms) and on every COT component row the account holds, a `CUSTODY_UNITS` fact whose
`source_revision` IS the receipted custody object's sha256 (`_receipt_sha` `:550-563`; `_custody_units_fact` `:566-579`)
and whose `source_scope` is the account's opaque id -- a pointer to the object, never a row reference; and on COT
component rows the capability fact `"observed custody position for this asset: <USD> (a FACT, not this node's amount)"`
(Anna's 68 of 68 carry it; 62 of 68 carry units). Those are facts ABOUT the custody row for display; the interpreter
reads the row from the object. `reference(source_row)` = (receipt bucket/key/version_id/sha256, row ordinal) for COT
and 49F; (receipt, Orion `id`) for INF.

## Q4 -- the ACCOUNT node's `fact_holdings (Market Value, deduped DC1)` value

**It is a SUM over the position rows in the same build, not a custodian-supplied account row.**
- `account_value = control_values[external_id]` `:1990`; `control_values = {account_id: float(r["position_value"]) ...}`
  over `actual_controls["reconciliation"]` `:1932-1933`;
- `position_value` is `account_values[account]`, accumulated as `economics.add(account_values.get(account, 0),
  values[first]["Market Value"])` over the DC1-collapsed `fact_holdings` rows `:422-423` (duplicates across the
  relationship grain collapsed to `first` `:412-421`; the sum is over `Market Value` per kept row).
- The node states this truthfully: `join_method "fact_holdings (Market Value, deduped DC1)"` `:2009`.

**The independent, custodian-supplied account-level value EXISTS as its own row in a SECOND fact table**, and the
build reconciles the sum against it to USD 0.01 before any node is minted:
- object: `opal-data-assets` / `blackdiamond/cottonwood/silver/fact_allocations/date=<total_date>/data.parquet`
  (`totals_key` `:1872`, read `:1874`; served dec293d6 receipt version `WeqLRnnX..`, 128,660 B), columns `AccountID`,
  `Account Market Value` (also `Relationship Market Value`, `Cash Market Value`, `Account Allocation`, `Custodian`,
  `Account Number`, `_source_as_of`) -- one row per account (1,495 rows in the 2026-09-23 partition);
- `totals[account] = number(row["Account Market Value"])` `:429-437` (`:433` the value, `:436` the row), conflicting duplicates refused `:434-435`;
- the tie: `difference = position_value - independent_value`, `> tolerance (0.01 USD)` REFUSES the build `:446-449`;
- the control row carries both values and the independent source reference: `{"account_id", "position_value",
  "independent_value", "difference", "independent_source_row_ordinals", "independent_source_origins"}` `:450-454`
  (origins = `(s3 url of totals_key, ordinal)` `:1877`) and lands in the manifest as
  `manifest["actual_custody_controls"]["reconciliation"]` `:2099`.

So for the interpreter: the ACCOUNT node's amount is the position sum (correct to the cent, but a derivation of the
same rows); the INDEPENDENT value is `fact_allocations.Account Market Value` for that `AccountID`, reachable either
from the receipted `fact_allocations` object (its own row) or from the served manifest's
`actual_custody_controls.reconciliation[].independent_value` with its source origin. The card's row moves as the CTO's
conditional said. 49F's analogue is `schwab dim_balance.net_mv_plus_cash` (`holdings_49f.py:183` the read, `:284` the account value, the balance row per
account, reconciled to the position rows `:403-411` with a DRILL WITHHELD control on a miss); INF's is
`accounts_v2.current_value` (`holdings_inf.py:150`, `:273` validate call).

Not answered here (not mine): Q2 (ruled), Q3 (Y). No egress; nothing served moved.

## CORRECTION 2026-09-24 13:2xZ (Y 100635, second finding) -- the reconciliation control row is NOT served

The Q4 section above says the control row "lands in the manifest as `manifest["actual_custody_controls"]["reconciliation"]`
`:2099`". That manifest is the build's INTERNAL manifest (`extra["manifest"]`, returned as `snapshot["_manifest"]`
`:2277` and landed locally by `land()` `:2351`), and the producer says so one paragraph above the validate call: "This
result is INTERNAL evidence only; publishing extra actual_custody wire fields needs P/Y agreement" `:1933-1934`. The
SERVED revision manifest is built by `publication.py:269-288` from the body, the gold bytes and `source_objects` only
(keys: business_date, clocks, firm_id, gold, partitions, platinum_header, revision, schema_version, source_objects,
source_set_revision); the platinum header carries attribution_holdouts, clocks, coverage, custody_totals, scope,
source_set_revision. Y read the served dec293d6 manifest by version and found no `actual_custody_controls`; that read is
right and my sentence was wrong at the "served" grain.

So the interpreter's read path for the independent value is the receipted `fact_allocations` object itself
(`source_objects[0]`, by version_id, sha256 verified): `Account Market Value` for the account's `AccountID`, its row
ordinal(s) as `independent_source_rows` (Anna: 2 equal duplicate rows, admitted by `:433-436`). The rest of Q4 stands:
the ACCOUNT node's amount is the DC1 position sum; the build ties it to that object within 0.01 USD or refuses.

Y's other producer reading also verified by line: the no-position exclusion (all four facts null) is
`:1904-1922` with its origins recorded in `absence_control` (`excluded_source_origins` `:1919`); a zero lot
(Market Value 0 AND Units 0, not null) is NOT that rule -- it stays an active row the validator counts as
unsupported (`Market Value <= 0` `:409`) and keeps in the DC1 sum at 0. Whether the interpreter excludes zero lots
is Y's proposal for the CTO; it moves no value.

## ADDENDUM 2026-09-24 14:0xZ -- the 49F and INF lines for the per-firm admission (CTO 100676; Y 100672)

**49F, which total the producer ties:** `dim_balance.net_mv_positions`. `holdings_49f.py:285` reads it beside the
ACCOUNT amount `net_mv_plus_cash` (`:284`); `:403-404` ties `sum(dim_position._mv)` to it within `RECON_TOLERANCE_USD`,
and a miss withholds the drill (`:405-414`). Cash is a DERIVED remainder node, `cash = account_value - net_positions`
(`:429-434`, security_id CASH/SCHWAB_CASH, fact "custody cash remainder") -- never a source row. `dim_position` carries no
cash row: `accounting_rule_code` is the holding's account type (CASH 102,608 / MARGIN 2,589 / SHORT 1,300 / blank 2 in
the served partition); `dim_balance` carries the cash FIELDS on its one row per account. The Q4 table's
"net_mv_plus_cash" names the ACCOUNT-level total; the position-row tie is to `net_mv_positions`. Ruling (a) matches.

**INF, the key-date rule and inactive rows:** `holdings_inf.py:145-151` reads accounts_v2 and positions_mv at the
partition `hs._inf_positions_source_key` selects (`holdings_snapshot.py:1425-1446`: the latest `snapshot_date <= as_of`;
for as_of 2026-09-23 that is 2026-09-23), refusing unless both partitions agree (`:146-147`); the custody clock is the
prior trading day (`:266`) = the manifest's business_date. Rows with `is_active = false` are SUMMED as ordinary rows:
`inf_positions.py:121-124` @a700417729 sums every positions_mv row of the account (`rows = p.loc[p.account_id ==
account]; observed = sum(rows.current_value, Decimal(0))`) against `accounts_v2.current_value`, no filter on is_active /
is_managed / is_custodial_cash anywhere in the validator or the builder's row path; the docstring says "No position
deduplication is permitted". Every validated row becomes a SECURITY node under namespace VENDOR (`holdings_inf.py:312-313`),
custodial cash included.
