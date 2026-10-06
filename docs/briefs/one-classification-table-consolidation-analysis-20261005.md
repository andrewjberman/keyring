# ANALYSIS -- one table for all security classification: consolidating `bd-securities` into the canonical table

- **Author:** `4.0.0_SA_CRO` (base), 2026-10-05 ~21:2xZ (5:2x PM Eastern). Read-only; no table, code or page changed.
- **Order:** Andrew-direct 2026-10-05 ~21:1xZ, verbatim in
  `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261005_211xZ_ONE_CLASSIFICATION_TABLE_CONSOLIDATE_BD_SECURITIES.md`.
- **Companion brief (the L1 input to `1.0.0_SA_CTO`):**
  `docs/briefs/mdpf-secclass-one-classification-table-midstream-brief-20261005.md`.
- **Earlier check this builds on:** `docs/briefs/holdings-surfaces-canonical-classifier-check-20261005.md`.
- **Words:** "the canonical table" = DynamoDB `etf-classifications`, read through its one client
  `infra/aws/lambda/v2_portal/_shared/etf_classifications_dynamodb.py` (class `ETFClassifier`). "The legacy table" =
  DynamoDB `bd-securities`.
- **Claim marks:** MEASURED = read today from the live table, the served object or the file line named. NOT TRACED =
  found, not followed further. No client name, ticker list or amount appears here.

---

## 1. The answer in six lines

1. **The direction already exists as a ratified project.** `MDPF_SECCLASS` (PRD v0.6,
   `org/missions/D8/MDPF/MDPF_SECCLASS/prd/MDPF_SECCLASS_PRD.md`) already commits to one shared list for every
   holdings screen, to deleting the legacy table (its outcome FWD-5), and to sector on the shared list (FWD-12, from
   Andrew's words of today). This analysis does not propose a new direction; it sizes the remaining work and finds
   what that PRD does not yet cover.
2. **The gap is 1,671 securities.** Of 3,334 distinct securities held across the three firms on 2026-10-02, 1,663 have
   a row in the canonical table and 1,671 do not (MEASURED). Filling those rows is the whole "resolutely fill the gaps"
   job; the legacy table can supply a class for only 403 of them directly.
3. **Do not copy the legacy table across.** It has 10,873 rows; only 2,053 label anything held today. Its labels were
   mostly written by an outside AI model (9,939 rows), it knows four asset classes where the canonical table knows six,
   and 55 of the 2,378 securities present in both tables disagree on asset class. Andrew's standing rule of 2026-09-29
   already says the canonical table is never overwritten from it.
4. **The all-caps names are not from the legacy table.** The Investor Reporting Holdings tab prints the custody feed's
   own security description. The symptom Andrew saw is real; its cure is a clean name on every canonical row and a
   page that reads it. Today only 338 of the 1,663 held canonical rows carry any name.
5. **No portal page calls a classification table directly.** Every "frontend call to another table" is one of two
   things: a hardcoded list inside the portal (three of them), or a served field that a backend built from another
   table. So the frontend migration is deleting lists and one fallback function, plus one contract field.
6. **Sector is surgical if one question is settled first:** the canonical table has two fields that both hold
   sector-like words (`sector` and `sub_asset_class`). The Positioning ETF view's sectors already match
   `sub_asset_class` for the 166 of its 167 holdings the table carries.

---

## 2. The two tables, measured

| | Canonical `etf-classifications` | Legacy `bd-securities` |
|---|---|---|
| Rows | 3,493 | 10,965 (10,873 distinct once upper-cased: 92 differ only by letter case) |
| Key | `ticker`. 2,442 plain tickers; 425 keyed `CUSIP:<9 characters>`; 626 keyed with another prefix (the Rival Funds backfill) | `ticker`, or `NAME::<slug>` for a security with no ticker |
| Asset classes | six: equity 2,746; fixed income 671; multi-asset 33; structured 20; commodities 12; alternatives 11 | four: equity 6,135; fixed income 3,161; alternatives 1,654; cash 15 |
| Who wrote the rows | scheduled classifier 3,045; legacy 238; seed 197; model 13 | outside AI model 9,939 (two model versions); manual 910; two seeds 116 |
| Clean name (`name`) | 869 rows; 529 of those are all capitals; 20 are just the ticker | 60 rows, all just the ticker. The raw custody name (`asset_name_raw`) is on 10,904 rows, 10,231 of them all capitals |
| `sub_asset_class` | 3,256 rows, 37 values. Mixes size and region segments (US Large Cap 905, US Small Cap 474) with sector names (Financials 122) | 46 values, including ones the canonical table does not use (Options 811, Structured Notes 404) |
| `sector` | 179 rows, 37 values, and the values are segments, not sectors (Government, Investment Grade, US Large Cap) | 59 rows, same kind of value |
| Fund or single security (`instrument_kind`) | 988 rows (fund 193, single security 795); 2,505 blank | none |
| Name aliases | none | 6 rows carry 12 aliases; the name match in practice runs on `asset_name_raw` |

**Overlap:** 2,378 securities are in both tables; 8,495 are only in the legacy table; 1,115 are only in the canonical
table. Among the 2,378, 55 disagree on asset class. The largest groups: legacy "alternatives" where canonical says
structured (12), commodities (10) or multi-asset (6); legacy "fixed income" where canonical says multi-asset (9).

**Two other tables were checked and are not classification tables:** `trade-security-identifiers` (104 rows of
identifiers: FIGI, ISIN, SEDOL) and `opal-harvest-security-metrics` (2,257 rows of scores). Neither assigns a class.

---

## 3. The gap, measured on what is served

Source: the live Investor Reporting holdings snapshots for business date 2026-10-02, all three firms, de-duplicated
across firms by symbol (or by description where the symbol is blank).

| | Distinct securities |
|---|---|
| Held across the three firms | 3,334 |
| Have a canonical row (by symbol) | 1,663 |
| **Do not** | **1,671** (1,556 held at one firm only, 107 at two, 8 at all three) |

**How the 1,671 are labelled on the page today:**

| Layer that answers | Securities | What it means |
|---|---|---|
| Ticker shape | 668 | "a ticker of 1 to 5 letters is equity": a guess, with no row anywhere |
| Name alias | 506 | the custody name matched a raw name in the legacy table |
| Legacy table row | 403 | a direct symbol hit in the legacy table |
| Unlabelled | 52 | nothing answered |
| Name pattern | 42 | a word in the name (for example a coupon rate) decided it |

**What kind of security they are, by symbol:** 1,174 have an ordinary 1-to-5-letter ticker; 312 have a CUSIP-shaped
symbol (bonds and notes); 127 have another shape; 58 have no symbol at all.

**A fix that needs no new data:** 187 of the 1,671 already HAVE a canonical row, keyed `CUSIP:<symbol>`. The Holdings
producer looks the canonical table up by bare symbol only (`holdings_snapshot.py:882-887`), so it never finds them and
falls back. Teaching that one lookup the `CUSIP:` key moves 187 securities onto the canonical table with no row
written.

**So the fill is about 1,484 new rows** (1,671 less 187), of which roughly 400 can take the legacy row as an input, and
the rest (the 668 guessed ones first of all) have no row anywhere and need a real classification.

---

## 4. Every adapter that reads a class from somewhere other than the canonical table

"Demand" is the shape the consumer needs, which is what must not break.

### 4.1 Backend readers of the legacy table

| # | Component | What it does today | Demand it places | What the move changes |
|---|---|---|---|---|
| B1 | `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py:864-972` with `bd_securities_fallback.py` (feeds the Investor Reporting Holdings tab, all three firms) | canonical first; then the legacy table, name alias, name pattern, ticker shape | `asset_class` in a nine-value list; `sub_asset_class`; a `asset_class_basis` field in a published contract with five values; a cash rule keyed on the custody name | 1,671 securities change their source. Any of the 668 guessed ones could change class. The basis field loses three of its five values (a contract change the portal reads, F5) |
| B2 | `data/assets/scripts/gold/runners_49f/a07_dim_asset_classification.py:108-252` (49 Financial's data chain) | copies the legacy table at build time, then its own name patterns and ticker-shape rule | a three-way mix (equity, fixed income, alternatives) with money-market folded into fixed income | needs a stated mapping from six canonical classes into its three buckets; 49 Financial mix figures can move |
| B3 | `infra/aws/lambda/v2_portal/partners/lambdas/opal-partners-data/etf_classifier.py` and `lambda_function.py:1025-1040`; a second list in `etf_classification.py` beside it (the partner feed) | scans the legacy table; same four layers; unknown becomes "other" | four buckets where "other" is the cash residual | same mapping question; the partner mix can move |
| B4 | `infra/aws/lambda/semantic-news-layer3-curation/lambda_function.py:65-80` (news curation) | scans the legacy table for the set of equity and fixed-income tickers Opal's clients hold | a set of tickers, nothing else | **not in the MDPF_SECCLASS surface list.** It shows no class, but it is a live reader, so the legacy table cannot be deleted until it reads the canonical table. Its ticker set shrinks from the legacy universe to the canonical one unless the gap is filled first |
| B5 | `infra/aws/lambda/v2_portal/_shared/etf_classification_scheduled.py` (the scheduled classifier) | reads a legacy row once as an INPUT when writing a new canonical row | the legacy class only when it is already a canonical value | it is the consolidation mechanism; it needs the legacy rows exported and kept as a record after the table goes |
| B6 | `lib/research/identity/positioning_chain.py` | references the legacy table (3 places) | NOT TRACED | NOT TRACED |

### 4.2 Writers that still add rows to the legacy table

| # | Component | What it writes |
|---|---|---|
| W1 | `data/black_diamond/scripts/gold/B_01b.classify_new_securities.py` and the Cottonwood copy `data/cot/scripts/gold/B_01b.classify_new_securities.py` | new securities, classified by an outside AI model |
| W2 | `data/inf/scripts/classification/classify_assets.py` | Inflection's new securities, same method, into the same table |
| W3 | `data/black_diamond/scripts/classification/classify_bd_securities.py`, `seed_bd_securities.py`, `seed_canonical_securities.py`, `backfill_name_aliases.py` | seeds and name aliases |
| R1 | `data/black_diamond/scripts/gold/E_18.detect_new_securities.py` (and the Cottonwood copy), `classification/resolve_tickers.py` | READ the legacy table to work out which ticker a custody name belongs to. `E_18` no longer writes it |

While W1 to W3 run, the legacy table keeps growing and any count in this document ages. `resolve_tickers.py` matters
for a different reason: it uses the legacy table's raw names to resolve identity. That job (which security is this
name) has to keep a home after the table is gone.

### 4.3 Backends that classify from their own authority, not from either table

| # | Component | Authority | Note |
|---|---|---|---|
| A1 | `data/etfs/scripts/gold/etf_positioning_gold.py:1219-1249`, served by `etf_positioning_publisher.py:416-417` (Positioning, ETFs mode) | Bloomberg's cash flag and sector name | MDPF_SECCLASS FWD-12 already ends this. Measured: 167 holdings served, 166 have a canonical row, asset class agrees for all 166, sub-asset agrees for 109. The other 57 are BLANK on the page today and the canonical table HAS a sector name for them, so the move fills 57 blanks; it is still a change to a served page |
| A2 | `data/canonical/schwab/gold/build_gold_firm_composition.py` | Schwab's own security master | a declared exception in the PRD; Andrew's "only the canonical table" of today reopens whether it stays one |
| A3 | `data/inf/scripts/gold/INF_D_03.composition_artifacts.py`, `INF_D_07a.firm_concentrations.py` | Orion's own asset-type field | not in either table; NOT TRACED to a page |
| A4 | `infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-positioning/lambda_function.py:95` | an inline geography list (the canonical table has no geography field) | everything else in this producer is canonical |

### 4.4 Copies of the canonical client or its seed list

One home exists. Tracked copies beside it (MEASURED by file list): `yang-generate-positioning/etf_classifications_dynamodb.py`,
`yang-generate-holdings-attribution/etf_classifications_dynamodb.py`, `yang-generate-etf-returns/etf_classification.py`,
`opal-partners-data/etf_classification.py`. Whether each copy's bytes equal the home's was not compared today.

### 4.5 Frontend adapters

| # | File | What it does | Change |
|---|---|---|---|
| F1 | `portal/src/components/holdings/HoldingsBreakdownTable.tsx:109-126` (`getSubAssetClass`), with its display map (`:69-84`) and colour map | keeps a served sub-asset label only if the colour map knows it; otherwise substitutes the hardcoded list, then "Other". Called from the Investor Reporting Holdings tab (`SecurityList.tsx:273`) and Positioning (`HoldingsTab.tsx:575`, `:634`) | remove the substitution. Every canonical `sub_asset_class` and sector value then needs a colour and display entry, or it shows as "Other": 37 canonical values today |
| F2 | `portal/src/pages/Positioning/constants/etf-categories.ts` | 37 tickers with a class and segment | delete |
| F3 | `portal/src/pages/Attribution/constants/etf-categories.ts` and `constants/holdings-shared.tsx:142` (its own `getSubAssetClass`), used by `tabs/SelectionTab.tsx:141` | a second copy of F1 and F2 | delete. **The Attribution copy is not in the MDPF_SECCLASS surface list** |
| F4 | `portal/src/lib/tickerRegistry.ts` (322 lines), used by `components/market-performance/ExecutiveSummary.tsx` and `lib/dataLoader.ts` | a hardcoded ticker to name and class registry | replace with served values. **Not in the surface list** |
| F5 | `portal/src/pages/InvestorReporting/contracts/wire/HoldingsSnapshot.ts`, `contracts/adapt.ts` (4 reads of the basis field), `contracts/index.ts`, and three tests | read `asset_class_basis` and its five values | follows B1's contract change |
| F6 | `portal/src/pages/InvestorReporting/tabs/holdings/SecurityList.tsx:80-85` | prints the served `display.description`, which is the custody feed's string | print the canonical clean name when served; this is the all-caps fix |
| F7 | `portal/src/pages/Positioning/shared/etfAdapter.ts`, `satelliteAdapter.ts` | pass served class and sub-class through | no change expected; they render whatever A1 and the satellite producer serve |

### 4.6 Access grants that name the legacy table

Terraform files under `infra/aws/terraform/`: `bd-pipeline/iam.tf`, `cot-pipeline/iam.tf`, `news-pipeline/iam.tf`,
`partners-api/iam.tf`, `trade-pipeline/iam.tf` and `dynamodb.tf`, `shared-infra/main.tf`, `dynamo.tf` and
`lambda-execution-role.tf`, `investor-reporting/directory/holdings_refresh.tf`. Each is a reader or writer the code
census must agree with before deletion. The live grants were not read today.

---

## 5. Three findings that shape the plan

### 5.1 The names
- The Holdings tab's name is the custody description (`holdings_snapshot.py:687-700`). MEASURED: 2,311 of the 3,334
  distinct held securities are served in all capitals.
- The canonical table is not yet a name source: 869 of 3,493 rows have a name, and 529 of those are all capitals.
- MDPF_SECCLASS FWD-11 promises a clean, properly capitalized name only for rows the AI classifier makes. No outcome
  yet says every holdings screen shows the shared list's clean name. That is the missing outcome.

### 5.2 Sector
- The ETF view's "sector" already lives in `sub_asset_class` for single stocks, and the scheduled classifier is built
  on that reading (`etf_classification_scheduled.py:24-27`).
- The field actually called `sector` holds 179 rows of segment words. Two fields with overlapping meaning is a schema
  defect to settle before sector is "added": either sector is `sub_asset_class` for a single stock and the `sector`
  field is retired or renamed, or `sector` becomes the real sector and 179 rows are re-homed.
- Andrew's condition, recorded in the PRD: the table holds what kind of thing a security is, never measurements.

### 5.3 The class vocabulary
The legacy table has four classes and two quiet folds (hedge to alternatives; money market to fixed income). The
canonical table has six. Three consumers show a three- or four-bucket mix (B2, B3 and the Black Diamond mix). Each needs
one stated mapping from six classes to its buckets, or a switch silently moves money between buckets. The 55
disagreements in section 2 are the sample of what moves.

---

## 6. Implementation sketch

Each step names what must be true before it and how "nothing broke" is shown. The order of work inside the project is
the decomposition's, not this document's.

**Step 1 -- Stop the legacy table growing.** Turn W1 to W3 from writers of the legacy table into nothing, with new
securities going through the scheduled classifier into the canonical table. Until this lands, every count here ages.
*Not broken when:* a day with a new security produces a canonical row and no legacy row.

**Step 2 -- Settle the table's shape once.** Three fields: a clean display `name` for every row; the sector question of
5.2; the key forms (plain ticker, `CUSIP:`, and a form for a security with neither, which today is the legacy
`NAME::` key). Recorded in the existing contract file `org/standards/MDPF_SECCLASS_CONTRACT.json`.
*Not broken when:* every existing reader still gets the fields it reads today; new fields are additions.

**Step 3 -- Fill the gap for what is held (about 1,484 rows plus names).** In this order of trust:
1. the 187 `CUSIP:` rows: an adapter fix only;
2. securities with a legacy row whose class is already a canonical value: the scheduled classifier's existing rule;
3. securities with a legacy row whose class is NOT a canonical value (the Options and Structured Notes groups): a
   stated mapping, decided once;
4. the 668 guessed ones and anything left: a real classification. MDPF_SECCLASS FWD-11 records Andrew's approval today
   of the AI classifier for these, landing without review, with an index of every AI-made row;
5. a clean, properly capitalized name on every row held.
*Not broken when:* a rerun of the section 3 count reads zero held securities without a canonical row, per firm.

**Step 4 -- Move the readers, one surface at a time.** For each of B1 to B4 and A1: list every security whose class,
sub-class or name will change, before the move; make the move; read the same list on the served page after. This is
the estate's existing served-move rule (PRD contract C-SERVED). The mapping of 5.3 is fixed before B2 and B3 move.
*Not broken when:* the after-list equals the before-list's predicted values, and totals per account are unchanged.

**Step 5 -- Remove the portal's own lists.** F1 to F4, after the surface that feeds each page serves a label for
every row. F5 and F6 ride with B1.
*Not broken when:* each page is rendered and read; no row falls to "Other" that had a label before.

**Step 6 -- Prove nothing reads the legacy table, then delete it.** The code census (FWD-4) and the live access grants
(4.6) both read zero; the rows are exported to a kept record; the table is deleted on Andrew's confirmation (the PRD's
C-DELETE). The identity job of `resolve_tickers.py` has its new home before this.

---

## 7. What this analysis did not do

- It did not compare each copy in 4.4 with the home file.
- It did not read the live access grants, only the Terraform files that name the table.
- It did not trace B6, A3, `build_canonical_prices_v2.py`'s mention of a "validated" ticker, or the client-portal and
  advisor pages.
- It did not test how many of the 1,484 a given source can classify; the "roughly 400" in section 3 is the 403
  direct legacy hits, not a tested result of the scheduled classifier's vocabulary rule.
- "Has a canonical row" is by symbol today, against snapshots of 2026-10-02.
- It read the MDPF_SECCLASS PRD's endpoint, contracts and surface list. It did not read that project's task orders or
  status; what is already in flight there may cover part of sections 4 and 6.
