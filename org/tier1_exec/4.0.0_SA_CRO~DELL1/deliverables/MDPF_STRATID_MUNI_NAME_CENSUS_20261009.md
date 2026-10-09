# MDPF_STRATID S07 -- census of every Muni-named sleeve, account and model (SmartX, Rebalancer, Eclipse)

- **Author:** `4.0.0_SA_CRO~DELL1`, 2026-10-09 ~05:4xZ-06:0xZ. Read-only (S3 GetObject/List). Zero Bloomberg calls.
- **Asked by:** `1.0.0_SA_CTO~DELL1` msg 1787, PRD `org/missions/D8/MDPF/MDPF_STRATID/prd/MDPF_STRATID_PRD.md`
  ADDENDUM v0.5 @a3cf95f254 (line 234 on): "a CRO census of sleeves or accounts named Muni across SmartX, Rebalancer and
  Eclipse ... with the denominator printed. If that census finds no Muni SMA dollars at any firm, FWD-3 cannot be
  EXERCISED."
- **Match rule:** case-insensitive regex `(?<![A-Za-z])muni`, applied to every string column of each table. It catches
  "Muni", "MUNI" and "Municipal" at a word start, and not "communication".
- **Builds on:** this seat's S07 read `org/tier1_exec/4.0.0_SA_CRO~DELL1/deliverables/MDPF_STRATID_S07_MUNI_VERIFY_20261009.md`
  @67e20ee89f, and the round-1 Eclipse census
  `org/missions/D8/MDPF/MDPF_STRATID/deliverables/0.9.0_WK_MDPF_STRATID~3/ECLIPSE_SLEEVE_NAME_CENSUS.md` @59a3be55de.
- **PII:** accounts appear only as masked last 4 plus the first 8 characters of a sha1 of the vendor account id. No
  account or client names appear.

## 1. Verdict

**NONE FOUND: no Muni SMA dollars at any firm in the scanned population. No vendor SMA flag is true on any
Muni-named object.** The scan finds one Opal Muni-named object with dollars that Andrew's ~05:3xZ word did not already
rule: `Opal_Muni_Sleeve`, $550,823.07 (value date 2026-10-07). It is the 40% Muni sleeve of one blended Cottonwood
account (`Opal_Tax_Efficient_Income/Muni60/40`), with `is_sma` false. Whether that sleeve is "the Muni SMA" is a person's
call, as C-MUNI-VERIFY requires. If it is not, FWD-3 has no dollars to exercise against, and that is the re-entry
addendum v0.5 provides for.

## 2. Hits (all firms)

| firm | source | object | name | dollars (as of) | is_sma (field) | Opal |
|---|---|---|---|---|---|---|
| cottonwood | BD Rebalancer | model, 1 account (last4 0127, 1c69d492) | `Opal_Muni_Income` | $64,119,753.85 (2026-10-07) | false (`fact_model_assignment.is_sma`; `allow_sma` false) | yes. **Excluded on Andrew's word** (v0.5): a Custom model, not ALT |
| cottonwood | BD Rebalancer | sleeve model (child at 0.4 of the blend below) | `Opal_Muni_Sleeve` | $550,823.07 (2026-10-07; `dim_model_portfolio` date=2026-10-08) | no direct assignment (`is_direct_assignment` false). Its one account's flag is false | yes. **Open: the candidate** |
| cottonwood | BD Rebalancer | blended model, 1 account (last4 8686, b744908f; Trust) | `Opal_Tax_Efficient_Income/Muni60/40` | $1,377,057.67 account total (`fact_holdings` 2026-10-07, 12 rows) | false (`fact_model_assignment.is_sma`; `allow_sma` false) | yes. Blend: 0.6 `Opal_Moderate_Income_Tax_Efficient` + 0.4 `Opal_Muni_Sleeve` (`fact_model_blend`) |
| 49financial | Schwab custody (0824 and 0833 `fact_acc`) | 2 accounts per master | `PIMCO Municipal Bond Ladders` (money manager PIMCO) | not read: `fact_acc` carries no value column | no field | **no**: a third-party manager's SMA |

Arithmetic check: 0.4 x $1,377,057.67 = $550,823.07, exactly the sleeve's served dollars. The sleeve's dollars are
therefore a decomposition of the blend account, not separate money. They are inside Cottonwood's Models (Custom) today
(S07 read, E2).

## 3. Denominators (per source; UTC; latest partition unless stated)

| source | table / partition | names scanned (distinct, the name columns) | Muni hits |
|---|---|---|---|
| SmartX (49financial) | `opal-data-assets/smartx/platform/silver/fact_model_allocation_roster/date=2026-10-08` (10,208 rows) | `model_name` 8; `advisor_name` 4 | 0 |
| SmartX | same table, ALL 87 partitions date=2026-07-14..2026-10-08 | `model_name` 10 over history | 0 |
| SmartX | `.../fact_allocation_account_map/date=2026-10-08` (7,612 rows) | `account_name` 5,850 | 0 |
| SmartX | `.../fact_model_holdings/date=2026-10-08` (168 rows) | `company_name` 91 (the securities held by the models) | 0 |
| SmartX | `.../fact_model_aum_daily/date=2026-10-08` (4,758 rows) | `enterprise_name` 1 | 0 |
| SmartX | `fact_account_detail`, `fact_nonzerosleeve`, `fact_account_allocations`, date=2026-10-07 and 10-08 | 0 rows in each partition | n/a (empty) |
| BD Rebalancer (cottonwood) | `opal-data-assets/blackdiamond/cottonwood/silver/fact_model_assignment/date=2026-10-08` (992 rows) | `strategy_name` 55; `account_name` 949 | 2 strategy names; 0 account names |
| BD Rebalancer | `.../fact_model_definition/date=2026-10-08` (1,713 rows) | `model_name` 91; `sleeve_name` 42; `component_name` 271 | 3 model, 2 sleeve, 13 component (the components are securities, see 4) |
| BD Rebalancer | `.../fact_model_roster/date=2026-10-08` (71 rows) | `model_name` 71 | 3 |
| BD Rebalancer | `.../fact_model_blend/date=2026-10-08` (128 rows) | `model_name` 53; `child_model_name` 22 | 3; 2 |
| BD Rebalancer | `.../gold/dim_model_portfolio/date=2026-10-08` (18 rows) | `model_name` 18 | 2 |
| BD custody | `.../silver/fact_allocations/date=2026-10-07` (1,516 rows) | `Account Strategy Name` 53; `Portfolio Name` 217; `Relationship Name` 221 | 2; 0; 0 |
| BD custody | `.../silver/fact_holdings/date=2026-10-07` (21,126 rows) | `Asset Name` 1,580 | 35 (securities, see 4) |
| Eclipse (inflection) | `opal-data-assets/eclipse/inflection/silver/fact_models/date=2026-10-08` (18 rows) | `name` 18; `description` 17 | 0 |
| Eclipse | `.../fact_model_composition/date=2026-10-08` (9 rows) | `name` 9; `modelDetail` 9 (JSON with Security Set children); `sleeveSuffix` 4 | 0 |
| Eclipse | `.../fact_portfolios_full/date=2026-10-08` (863 rows) | `name` 861; `model` 18 | 0 |
| Eclipse | `.../fact_portfolios_simple/date=2026-10-08` (846 rows) | `name` 846; `accountName` 459 | 0 |
| Schwab 0824 (49financial) | `opal-data-assets/schwab/08242234/silver/fact_acc/date=2026-10-07` (7,533 rows) | `managed_account_investment_strategy` 7 | 1 (PIMCO) |
| Schwab 0833 (49financial) | `opal-data-assets/schwab/08335338/silver/fact_acc/date=2026-10-07` (7,620 rows) | `managed_account_investment_strategy` 9 | 1 (PIMCO) |

Eclipse history: the round-1 census scanned all 132 partitions (2026-05-15..2026-10-08) of the same four tables, pooling
1,418 distinct names. Its listed Opal names contain no Muni name. This census did not re-scan Eclipse history for "muni"
specifically.

Partitions for date=2026-10-09 did not exist at read time (~05:4xZ) on any of the BD or Eclipse tables listed above.

## 4. What the security-name hits are, and why they do not count

- BD `fact_holdings.Asset Name` (35 distinct) and `fact_model_definition.component_name` (13 distinct) are municipal
  SECURITIES held by accounts or used as model components: for example "EATON VANCE SHORT DURATION MUNICIPAL INCOME ETF"
  and "ISHARES SHORT-TERM NATIONAL MUNI BOND ETF". One ticker is literally `MUNI`. Holding a municipal fund does not
  make an account a Muni SMA. FWD-3 is about a Muni STRATEGY, and these hits are not Muni strategies. Direct holdings
  are also out of scope by Andrew's restatement (CTO msg 1135).
- SmartX `fact_model_holdings.company_name` carries no municipal security in its 91 holdings.

## 5. What this means for FWD-3

- SmartX and Eclipse carry no Muni-named model, sleeve or account. On SmartX this holds over the full roster history.
- At Cottonwood, the only Opal Muni-named dollars are `Opal_Muni_Income` (ruled a Custom model, out) and
  `Opal_Muni_Sleeve` ($550,823.07, the 40% sleeve of one blended Trust account). No vendor flag marks either as an SMA.
- The only Muni SMA a vendor identifies by name is PIMCO's at Schwab: a third-party manager, not Opal.
- So FWD-3 has, at most, one candidate: `Opal_Muni_Sleeve`. The decision for a person is: "Is the 40% Muni sleeve
  inside `Opal_Tax_Efficient_Income/Muni60/40` the Muni SMA that belongs under ALT Strategies?"
  - Yes: FWD-3 can be EXERCISED on $550,823.07 at Cottonwood, as a sleeve carved out of a blended Custom model.
    Note: the same Custom model's other 60% would stay in Custom.
  - No: no Muni SMA dollars exist at any firm, and FWD-3 goes to re-entry as addendum v0.5 states.

## 6. Not measured

- Schwab dollars for the two PIMCO accounts per master (`fact_acc` has no value column; positions were not joined), and
  whether the 0824 and 0833 rows are the same two accounts.
- Eclipse holdings and sleeve names. As the round-1 census states, Eclipse silver carries no per-sleeve holdings or
  sleeve-name column. A sleeve named Muni at Inflection would be invisible to this census.
- Bronze layers of all three vendors, and the SmartX per-model bronze under `smartx/model/<id>/` (11 model ids).
- History for BD beyond date=2026-10-08 (S07 read covered `dim_model_portfolio` 10-05..10-08 and `fact_holdings` 89
  partitions for account M only).
- Commonwealth, Orion, Pathfinder, TrueShares and the other source prefixes under `opal-data-assets/`. They are outside
  the three systems named in the ask.
