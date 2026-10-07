# What is ambiguous under "six classes only": the `multi_asset` census (answer to Andrew's word ~00:4xZ 2026-10-07)

**Author:** `2.0.0_SA_COO~M`, 2026-10-07 ~00:5xZ. **Claim:** measured (the live `etf-classifications` table, a full scan of 3,507 rows; the batch-183 row set; the three firms' Holdings reads).
**His word (verbatim, record `ANDREW_DIRECT_20261007_004xZ_NO_MULTI_ASSET_CLASS_SIX_CLASSES_ONLY.md`):** six classes only (cash, fixed income, equity, structured, alternatives, commodities); ambiguity is shown, then remediated into one of them.

## 1. What the ambiguity is

A fund whose stated category is a mix (target-date, balanced, allocation, multi-asset income) has no single home among the six. The CTO's batch 164 gave those funds their own class,
`multi_asset`, "inferred from each fund's own name"; the batch-183 packet wrote it. The table holds **33 rows** in it: **21 ticker rows and 12 `CUSIP:` rows, covering 19 distinct funds** (the rest are share classes and CUSIP twins).
Seven of the 33 were MOVED from another class; 26 were new rows (before them the fund read through a fallback label or as unclassified).

Nothing in our own data says how a given fund splits between equity and bonds. The table row carries a name and a sub-class that describes HOW the mix is set (Target Date, Fixed Mix, Flexible), not what it holds.
So the choice of one class per fund is a judgment, or a look-through read of each fund's actual holdings (a vendor read, which needs his word).

## 2. The 19 funds (what each is, what it read before, who holds it)

Held counts are Holdings nodes in the latest served read (cottonwood and inflection 2026-10-02, 49financial 2026-10-05). `before` = the class the row had before the packet (`--` = no row).

| fund | rows | stated mix (sub-class) | before | held by |
|---|---|---|---|---|
| American Funds 2030 Target Date Retirement A | AAETX, CUSIP:02630T712 | Target Date | -- | nobody |
| Vanguard Target Retirement 2030 | VTHRX, VTTHX | Target Date | equity (VTHRX) | nobody |
| Vanguard Target Retirement 2035 | CUSIP:92202E508 | Target Date | -- | nobody |
| Vanguard Target Retirement 2045 | VTIVX | Target Date | fixed_income / Cash | nobody |
| BlackRock LifePath Index 2050 | LIPKX | Target Date | -- | nobody |
| Fidelity Freedom Index 2055 | FTYPX | Target Date | -- | nobody |
| American Funds American Balanced | ABALX, CLBAX, CUSIP:024071508 | Fixed Mix | equity (ABALX) | inflection 4, 49f 7 |
| Fidelity Balanced | FBALX, CUSIP:316345206 | Fixed Mix | -- | inflection 1 |
| iShares Core Growth Allocation ETF | AOR | Fixed Mix | equity | nobody |
| Impax Sustainable Allocation | CUSIP:704223205 | Fixed Mix | -- | nobody |
| "BALANCED FUND" (Schwab; sponsor not named in the feed) | SCGB1, CUSIP:808516306 | Fixed Mix | -- | 49f 9 |
| Vanguard LifeStrategy Moderate Growth | VSMGX | Fixed Mix | fixed_income / Intermediate | nobody |
| Vanguard Wellington | VWELX, VWENX | Fixed Mix | equity | inflection 4, 49f 2 |
| American Funds Income Fund of America | AMECX, CUSIP:453320103 | Flexible | -- | inflection 4, 49f 3 |
| American Funds Capital Income Builder | CAIBX, CFIHX, CUSIP:140193103, CUSIP:140193780 | Flexible | -- | inflection 3, 49f 4 |
| First Eagle Global | SGIIX, CUSIP:32008F606 | Flexible | -- | cottonwood 5, inflection 4, 49f 3 |
| Franklin Income | FKIQX, CUSIP:353496490 | Flexible | -- | 49f 5 |
| Kensington Dynamic Allocation | KAGIX, CUSIP:56167N274 | Flexible | -- | nobody |
| BlackRock Global Allocation | MDLOX | Flexible | -- | 49f 2 |

Held in the six-class world today (the dollars that would move): cottonwood $159,905.56 (5 nodes, 10-02; its gold also drops $266,651.67 of SGIIX), inflection $40,560.31 (20 nodes, 10-02), 49 Financial $2,515,601.18 (35 nodes, 10-05;
the Black Diamond composition shows $5,438,537.07 on its own 10-02 base).

## 3. Rules he can choose from (he picks; the table of 19 is then mapped mechanically)

- **A. Majority sleeve by look-through.** Each fund goes to the larger of its equity and bond sleeves, read from its actual holdings. Principled, per fund; needs a fund-composition source we do not hold (a vendor read: his word, per use).
- **B. One stated rule by category, no look-through.** For example: target-date, balanced and allocation funds go to equity; income-oriented funds go to fixed income. Mechanical and reviewable today, likely wrong at the margins (a 2030 target-date or an income fund may not be equity-majority; not checked, since our data has no look-through).
- **C. Restore what each fund read before, and decide the 26 that had no row case by case.** Honest about what was served, but covers only 7 of the 19 funds' history, and VTIVX's old `fixed_income / Cash` looks wrong for a 2045 target-date fund.
- **D. His own fund-by-fund list.** The table in section 2 is the list; he writes the class beside each name.

**Recommendation: B or D for speed, A where he wants precision on the held ones.** Only 9 of the 19 funds are held at all today (ABALX, FBALX, "BALANCED FUND", Wellington, Income Fund of America, Capital Income Builder, First Eagle, Franklin Income, BlackRock Global Allocation); the other 10 have no served dollars and can follow whatever rule he picks.

## 4. What rests on `multi_asset` (surfaced to the CTO; none of it is touched until he has chosen)

- The table rows above, and the Holdings contract's `asset_class` enum, the Holdings producer and reader, the portal's class lists and legends (census `COT_REPOINT_READER_CENSUS_20261001.md`, `MULTI_ASSET_LEG_V_*_20261005.json`).
- The S29 gold fix (Cottonwood and Black Diamond class lists, signed @6cf5f02f14, already uploaded to S3, served at the next scheduled runs): it publishes `multi_asset` as a seventh class on client mixes. Row S35.
- PRD FWD-16's "stated mapping" job and `MULTI_ASSET_ROW_SET_20261003.tsv` (batch 183).
