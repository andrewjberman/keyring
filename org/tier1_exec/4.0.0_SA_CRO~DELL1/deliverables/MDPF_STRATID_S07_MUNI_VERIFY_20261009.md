# MDPF_STRATID S07 -- the Muni read: what `Opal_Muni_Income` and `Opal_Muni_Sleeve` are

- **Author:** `4.0.0_SA_CRO~DELL1`, 2026-10-09 ~04:3xZ. Read-only. Track A of unblock UB-20261009T040755Z-d866.
- **Serves:** PRD row S07 (`org/missions/D8/MDPF/MDPF_STRATID/prd/MDPF_STRATID_PRD.md:187`) and contract C-MUNI-VERIFY
  (`:143-145`): "verified by a person as Opal Muni, or excluded with the reason recorded, before any Muni dollars count
  at Global (FWD-3). Until then it stays where it is and appears on the C-UNIDENTIFIED list."
- **What this is NOT:** the person's verification. The contract reserves the verdict for a person. This read hands that
  person the evidence and the precise question to answer (section 4).
- **S04 (Eclipse census):** not repeated. It ran in round 1 as TO-ST-t4:
  `org/missions/D8/MDPF/MDPF_STRATID/deliverables/0.9.0_WK_MDPF_STRATID~3/ECLIPSE_SLEEVE_NAME_CENSUS.md` @59a3be55de
  (denominator 1363 names on 2026-10-08, NONE-FOUND, graded MET @3a839f7006). The PRD's S04 row still reads "held (no
  census yet)". That row is stale.
- **PII:** no account number, account name or client name appears here. The account is "account M" (masked last 4:
  0127; sha1 of the vendor account id, first 8: 1c69d492).

## 1. Verdict

**UNDETERMINED by data. Leaning: an Opal muni ETF MODEL, not an SMA.** Every field the vendor data carries is
consistent with an Opal-built Rebalancer model of six third-party short-duration municipal ETFs. The account holds
exactly that model's six ETFs plus cash. The vendor's own SMA flags read false. Nothing in the data says whether
Andrew's "Muni SMA" is this product. A person must decide that (section 4).

The CTO record's figure reproduces exactly. Account M is $64,119,753.85 on value date 2026-10-07: in the served
`custom_residual_detail` (`Opal_Muni_Income`, 1 account, `auto_classified: true`), in gold `dim_model_portfolio`
(date=2026-10-08) and in silver `fact_holdings` (date=2026-10-07).

## 2. Evidence chain (each read 2026-10-09 ~04:2xZ-04:3xZ, S3 GetObject)

| # | source | what it shows |
|---|---|---|
| E1 | `s3://opal-data-assets/portal/gold/mdpf/cottonwood/aggregate-aua-timeseries/2026-10-07.json`, `meta.custom_residual_detail.by_date["2026-10-07"]` | one entry: `Opal_Muni_Income`, accounts 1, dollars 64,119,753.85, `auto_classified` true. The detail carries 1 date only. |
| E2 | `.../cottonwood/category-views/2026-10-07.json` | `Opal Muni Sleeve` (`opal_muni_sleeve`) is a member of Models > Custom (Custom aum 24,897,543.82). SMA > ALT Strategies > `Muni SMA` has aum null. `Opal_Muni_Income` is not a named member; its dollars sit in the Custom catch-all (E1). |
| E3 | `s3://opal-data-assets/blackdiamond/cottonwood/gold/dim_model_portfolio/date=*/data.parquet`, 4 partitions 10-05..10-08 | `Opal_Muni_Income` first appears on date=2026-10-08 (value_date 2026-10-07): type Model, is_opal true, 1 account, $64,119,753.85. The 17-row partitions of 10-05/06/07 do not carry it (10-08 has 18 rows). Partition total moves $208,299,906.63 (10-07) -> $273,201,220.58 (10-08). |
| E4 | `s3://opal-data-assets/blackdiamond/cottonwood/silver/fact_model_definition/date=2026-10-08` (1713 rows) | `Opal_Muni_Income`: is_opal true, rebalance_model_type Model and Strategy (depth 0 and 1), six components: SHYD 0.2005, EVSM 0.1600, SUB 0.1600, SHM 0.1598, MEAR 0.1598, VTES 0.1599. date=2026-10-07 (1701 rows) carries 0 rows for it. None of the six is an Opal ETF (DIVZ, IDVZ, PFDE, PFOE). |
| E5 | `.../silver/fact_model_assignment/date=2026-10-08` (992 rows) | Account M: strategy_name `Opal_Muni_Income`, program_name `Cottonwood`, can_rebalance true, **is_sma false, allow_sma false**, is_rebalancer_uma false, is_uma_sleeve_account false, is_managed false. |
| E6 | `.../silver/fact_holdings/date=2026-10-07` (21,126 rows) | Account M: 8 rows, Supervised, $64,119,753.85: SHYD 12,513,943.86; EVSM 9,946,921.50; SUB 9,932,244.00; SHM 9,929,900.80; VTES 9,929,602.35; MEAR 9,925,459.60; CASH 1,941,681.74; margin interest 0.00. The six ETF weights match E4. |
| E7 | `.../silver/fact_holdings/`, all 89 partitions (date=2026-06-09 .. 2026-10-07) | Account M is present in 12 of 89. The first is date=2026-09-22 ($64,411,328.84), the latest is 2026-10-07. Before the model and assignment appeared (E3-E5), its dollars sat in Cottonwood's non-model population. |

**Opal_Muni_Sleeve** (same sources): is_opal true, type Model and Strategy, four components: SHM 0.3005, MEAR 0.2993,
SUB 0.2504, SHYM 0.1498, none of them Opal ETFs. 1 account. Dollars on 4 consecutive dim partitions: $549,435.18
(10-05), $550,514.08 (10-06), $551,951.53 (10-07), $550,823.07 (10-08). `is_decomposed_target` true and
`is_direct_assignment` false on every partition, so it is reached as a component of another strategy, not by direct
assignment. Its parent was not traced (section 5).

## 3. What this means for FWD-3

- Both Muni objects are structurally the same kind of thing as the other Opal Custom models: Opal-named Rebalancer
  models of third-party ETFs. They are not sleeves named after an Opal ETF, so FWD-5's ETF Strategy rule (Andrew's
  restatement, CTO msg 1135) does not reach them.
- The registry's `muni` member (`mdpf_category_registry.py:343-368`) is declared CARVE_OUT and UNVERIFIED. If a person
  verifies `Opal_Muni_Income` as "Muni SMA", moving $64.1M from Custom to SMA > ALT Strategies is a relabel inside
  Cottonwood's view. At Global, its basis decides whether the move adds or relabels. Both branches belong in the
  never-widen pair under C-GLOBAL-PAIR.
- Size: on 10-08 this one account is about 23% of the $273.2M partition total (E3). A wrong label moves Global
  materially either way, which is why the contract asks a person.

## 4. The question for the person (C-MUNI-VERIFY)

One decision, two objects:
1. Is the Rebalancer model `Opal_Muni_Income` (six muni ETFs, first seen in the 10-08 definition pull,
   one $64.1M account funded 2026-09-22) the product Andrew calls "Muni SMA" under ALT Strategies? Yes -> map it to
   registry member `muni`. No -> it stays a Custom model, with the reason recorded.
2. The same question for `Opal_Muni_Sleeve` ($0.55M, reached as a component of another strategy).

Until answered: both stay where they are (Custom), and `Opal_Muni_Income` belongs on the C-UNIDENTIFIED list (S08) as
"Opal-named, Muni-shaped, unverified".

## 5. Not measured

- Who owns account M or what the client is. Not read, deliberately (PII). Whether a single $64M supervised account is
  one client, an omnibus or an institutional mandate is not determined.
- The parent strategy of `Opal_Muni_Sleeve` (the decomposition link). A strategy named
  `Opal_Tax_Efficient_Income/Muni60/40` exists in the 10-08 assignments and is a candidate parent, but it was not
  traced.
- Black Diamond bronze, and the Rebalancer API beyond the silver tables. Nothing older than the 89 holdings partitions
  (from 2026-06-09).
- 49financial and Inflection custody for Muni-named strategies. Only Cottonwood was read. The Eclipse census above
  covers Inflection names only.
- Any served Global file. The Global side of FWD-3 was not read.
