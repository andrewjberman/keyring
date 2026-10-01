# Cash and no-ticker holdings: what each surface does today, and what the feeds state

**Author:** 4.0.0_SA_CRO~X (Chief Research Officer, lane X)
**Home:** org/tier1_exec/4.0.0_SA_CRO~X/deliverables/
**Asked by:** 1.0.0_SA_CTO, msg 103794 (RULINGS batch 90 item 4 @59e643e4b8), on `2.0.0_SA_COO~M`'s measure
`org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/COT_THREAD_UNCLASSIFIED_MEASURE_20261001.md` @8e4b81eec7.

Prepared by 4.0.0_SA_CRO~X on 2026-10-01 (read 14:16Z to 14:48Z). Read-only: source at CLOUD, the
classification contract, the canonical table, and the 2026-09-30 partition of three custody feeds. No vendor call, no
write. Feed figures are firm-level aggregates; names quoted are security names. Local copies were deleted.

## The answer in three sentences

**No surface classes cash or a no-ticker holding from a feed field today: every one of them reads a name, a ticker
table, or guesses.** Two of the three custody feeds state cash in a field that is present on every row, and the
contract already says cash is classed by the producers' own cash rule and is not a row of the table. For a no-ticker
holding no feed states the instrument's type at all; what the feed does state, on every such row, is an identifier.

## 1. What each surface does today

| Surface | Cash | A holding with no ticker | The class comes from |
|---|---|---|---|
| Holdings tab, all three firms (one function, `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py:922-956`) | Four paths, two classes. Black Diamond's own line (ticker CASH and description CASH) reads `cash` (`:932-937`). A ticker the canonical table holds reads its row: the table's cash-like rows are `fixed_income`. A ticker the fallback table holds reads that row (FCASH: `cash` / Money Market). `CASH_USD` and any name with cash wording read `fixed_income` (`bd_securities_fallback.py:127-128`, `:152-153`). | The canonical table is skipped (`:868-870`). The fallback tries the name as an alias, then three name patterns, then answers nothing: `unclassified` (`bd_securities_fallback.py:150-167`; the ticker-shape guess at `:164` needs a ticker). | a name, or a ticker table |
| Black Diamond gold, 49 Financial (`data/black_diamond/scripts/gold/C_06.client_mix_timeseries.py:180-193`, `:196-240`; `D_03.composition_artifacts.py:116-145`) | A ticker the canonical table lacks reads `cash` when its NAME contains CASH, SWEEP, MONEY MARKET or MMKT. Upstream, `B_00.canonical_holdings.py:140-154` also finds cash by name. | `other`, unless the name has cash wording. | a name |
| Cottonwood gold (deployed library; `2.0.0_SA_COO~M`'s measure) | Cash wording reads `fixed_income`. | A bond-shaped name reads `fixed_income`; every other name reads `equity`. 101.3 million USD in 491 rows. | a name, else a guess |

Three facts about that table.

- **Cash has no single class across the estate.** The Holdings contract's enum has `cash`
  (`holdings_snapshot.py:830-831`); the canonical table has none; the same fund (FCASH) reads `cash` on one path and
  would read `fixed_income` on another. `2.0.0_SA_COO~M` measured that on the tab: FCASH `cash` / Money Market, 9.20
  million USD at Cottonwood and 1.45 million at Inflection; FIGXX `fixed_income` / Cash, 2.74 million.
- **`cash` and `other` exist in Cottonwood's mix and nothing fills them.** `data/cot/scripts/gold/C_06.client_mix_timeseries.py:173`
  lists five classes; the deployed classifier returns three.
- **At CLOUD the Cottonwood library is already re-pointed** to the canonical table only
  (`data/cot/scripts/gold/lib/etf_classifier.py:10-17`, build-only). Under it a no-ticker holding reads unclassified.
  That is the 37 percent cliff the ruling holds.

Not read for this table: the served Holdings snapshots themselves, and the deployed bytes of either gold tree. The
rules are CLOUD source; the two dollar figures are `2.0.0_SA_COO~M`'s.

## 2. What each custody feed states

Measured on the 2026-09-30 partition, rows with a positive market value.

| Feed | Rows, USD | Field that states cash | Field that states instrument type | No-ticker rows |
|---|---|---|---|---|
| Black Diamond holdings, Cottonwood (`blackdiamond/cottonwood/silver/fact_holdings`) | 13,136 rows, 556.19 million | `Cash Equivalent`: present on 13,136 of 13,136 rows. True on 696 rows, 22.65 million (4.1%). | NONE. 26 columns; the only other descriptive fields are the names and `Holding Supervised`. | 495 rows, 101.54 million (18.3%) |
| Orion positions, Inflection (`orion/inflection/silver/fact_positions`) | 12,415 rows, 206.55 million | `isCustodialCash`: 12,415 of 12,415. True on 206 rows (0.9% of USD). Also `productSubType` = "Cash or Equivalent": 837 rows (5.6%). | `productCategory` (Equity, Bond, Money Market), `productType` (Stock/ETF, Mutual Fund, CD) and `productSubType` (9 values): each on 12,415 of 12,415 rows, 100% of USD. | 0 |
| Schwab positions, 49 Financial (`schwab/08335338/silver/dim_position`) | 105,744 rows, 1,777.54 million | NONE as a flag. The measurable rule is the shape test of IRPT ruling 14 (no identifier, price 1.00, quantity equal to value): 21 rows, 22.04 million. The same shape on rows that do carry a ticker: 74 rows, 5.63 million. Cash outside positions is in `dim_balance`. | NONE. 30 columns; `tax_code` has 11 values whose meaning is not recorded in the repo. | 198 rows, 40.72 million (2.3%) |

**Cash.** The Black Diamond flag and the Holdings tab's name rule do not agree on scope, which is the point of the
test. The feed marks four securities as cash at Cottonwood: FCASH (16.71 million), a Fidelity government cash
reserve fund (4.23 million), the line CASH (1.72 million) and a bank sweep. All 696 rows carry a ticker. Orion's two
fields mean different things: `isCustodialCash` is the custodian's cash line (0.9%), `productSubType` adds money
market funds (5.6%). A rule must say which one it means.

**No ticker.** The feed gives every such row a key and no type.

| Feed | No-ticker rows | CUSIP present | Other identifier | Neither |
|---|---|---|---|---|
| Black Diamond, Cottonwood | 495 rows, 101.54 million | 340 rows, 30.33 million | `Alternative Identifier` on the other 155 rows, 71.20 million (91 Supervised, 50.06 million; 64 Unsupervised, 21.14 million) | 0 |
| Schwab, 49 Financial | 198 rows, 40.72 million | 157 rows, 13.97 million | none | 41 rows, 26.75 million: 21 are cash by the ruling-14 shape (22.04 million), 20 are not (4.71 million) |
| Orion, Inflection | 0 | -- | -- | -- |

So at Cottonwood 495 of 495 no-ticker rows carry a feed identifier (a CUSIP or the vendor's alternative identifier),
and `AssetID` is on every row of the feed. None of the 495 is flagged cash.

## 3. What the contract already says

- **Cash is outside the table, by the contract's own words.** `org/standards/MDPF_SECCLASS_CONTRACT.json` (v0.3.0),
  `instrument_kind`, the subtraction record: "the remainder after subtracting both is cash and cash-equivalent lines,
  which are not rows of this table (cash rows are classified by the holdings producers' cash rule, PRD v0.20 rulings
  of IRPT_BCKEND)".
- **That cash rule is a measured-field rule.** `org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md:540-542`
  (ruling 14): a row with no identifier whose price is 1.00 and whose quantity equals its value is cash. The
  holdings-performance producer carries the per-source form as data: `cash_flag_column` (`isCustodialCash` for
  Orion, `Cash Equivalent` for Black Diamond) and `cash_columns` for Schwab's balance
  (`data/assets/scripts/gold/irpt_holdings_performance/sources.json`).
- **A key for a security with no ticker already exists.** The same contract's `identifier_namespace` admits `CUSIP`,
  written `CUSIP:<9 chars>` in the ticker column. The table holds 348 such rows of 2,671.
- **`other` is not in the contract.** The file has no class named `other` and no class list at all: the class
  columns are POSN_ASTTAX's. Measured on the table: five classes (equity 2,057, fixed_income 594, commodities 9,
  alternatives 6, structured 5), no `cash`, no `other`; 18 rows whose sub class is Cash or Money Market, all under
  `fixed_income`.
- **The Holdings contract is wider than the table.** Its node enum admits `cash`, `other` and `unclassified` beside
  the five (`holdings_snapshot.py:830-831`).

## 4. The test, applied to the fork (PROPOSAL -- the CTO rules)

The question a rule must pass: does the class come from a measured field of the feed, or from a name.

- **Cash passes at two feeds and half-passes at the third.** A caller rule that reads `Cash Equivalent` (Black
  Diamond) and a named Orion field takes its class from the feed on 100% of rows. At Schwab the only measured form is
  ruling 14's shape, already ratified. This is option (ii), and the contract's subtraction record already assumes it.
  What it still needs ruled is the label: `cash`, as the Holdings contract has it, or `fixed_income` / Cash, as the
  table's 18 rows have it. Today both are served.
- **A no-ticker holding with a CUSIP is option (i) without a vocabulary change.** The namespace exists. What is
  missing is the carrier: `2.0.0_SA_COO~M` measured that Cottonwood's gold positions carry no CUSIP column, while the
  silver they are built from carries one on 340 of the 495 rows (30.33 million). The individual bonds in that measure
  (25.9 million, right today by a name pattern) are the population this recovers by key instead of by name.
- **A no-ticker holding with no CUSIP cannot pass the test by class.** No feed field states what a manual or
  held-away asset is. The feed states only that it exists, who supervises it, and its vendor identifier (71.20
  million at Cottonwood; 4.71 million at Schwab with no identifier at all). The honest choices are a table row keyed
  by the vendor identifier, which is a new namespace value and so the four-postulate record of option (i), or the
  accepted residue of option (iii) under one name. `2.0.0_SA_COO~M` notes the knowledge was written once already: 941
  rows in the fallback table class these names.
- **The test also fails things that are served today.** Every cash and no-ticker answer in section 1 comes from a
  name. A rule that passes the test changes served classes on the Holdings tab too, not only on Cottonwood gold.

## Evidence anchors and limits

Machine-readable evidence: `org/tier1_exec/4.0.0_SA_CRO~X/deliverables/cash_class_research_20261001/EVIDENCE.json`.

Limits. One partition per feed, one day. The served Holdings snapshots were not read; section 1 is the rule at CLOUD.
The deployed gold scripts were not compared to CLOUD. The overlay feeds (SmartX, Eclipse, the Rebalancer) were not
measured: they carry models, not custody. Schwab's `tax_code` may encode a security type; its code list is not in the
repo and was not interpreted. The contents of `Alternative Identifier` were not printed or examined, only its
presence. The Orion rows counted are those with a positive value: 23,695 further rows carry zero value.

- `data/assets/scripts/gold/investor_reporting/{holdings_snapshot.py,bd_securities_fallback.py}`
- `data/black_diamond/scripts/gold/{B_00.canonical_holdings.py,C_06.client_mix_timeseries.py,D_03.composition_artifacts.py}`
- `data/cot/scripts/gold/{C_06.client_mix_timeseries.py,lib/etf_classifier.py}`
- `org/standards/MDPF_SECCLASS_CONTRACT.json`; `org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md:538-542`
- `data/assets/scripts/gold/irpt_holdings_performance/sources.json`
- DynamoDB `etf-classifications` (2,671 rows, one scan)

## Andrew-direct request -- verbatim record

Channel: Andrew at the `1.0.0_SA_CTO` terminal, 2026-10-01 about 04:23Z, recorded in
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261001_042xZ_SELF_DRIVE_60M_LAPTOP_FABRIC_FINAL_SAY_CLOSER_DRIVE_IRPT_FIRST.md`;
this ask reached this seat as msg 103794.

> You have 4.0.0_SA_CRO~X as your research partner so as you see projects developing, if you assess there needs to be
> higher resolution on any part of the development process, you have CRO~X run /closer trace on the given surface and
> assess the strategic way forward.
