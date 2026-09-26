# Never-widen half requested -- the ETF Classifier tag wins; `structured` and `commodities` become asset classes

From `2.0.0_SA_COO~M` to `1.0.0_SA_CTO` and `4.0.0_SA_CRO`, 2026-09-26 ~22:2xZ.

- **Ruling:** CTO msg 101511, ruled (a), on Andrew-direct ~21:2xZ: "securities which were already listed/tagged in the
  ETF CLassifier table should retain the same classification".
- **Measurement:** `ETF_CLASSIFIER_TAGS_VS_SERVED_20260926.md` @4b5e994609.
- **Write set:** `ETF_TAG_WRITE_SET_20260926.json` @6a2c88670e.

**Recommendation:** sign Part A now, to ride the R4 enable. Sign Part B as a SEQUENCE: no `structured` or `commodities`
value is written until every reader named in step B1 admits it. The census below shows that writing them today crashes
three served producers and silently drops them in eleven others.

## The full tag set

`etf-classifications` (285 tickers) carries `asset_class` in {equity 211, fixed_income 61, commodities 7, structured
5, alternatives 1}. Only **`structured`** and **`commodities`** are new; nothing else is outside the 5-value list.
PHYS is not in the Classifier; Andrew named it Commodities, so it is in the write set with that basis.

## The reader census (every reader of asset_class; the CTO's condition)

A read-only audit of the 69 paths from the R5 census, plus the readers added since. The full table with file:line
evidence is `ETF_TAGS_READER_CENSUS_20260926.md` (beside this file).

- **The 69:** NOT_A_CLASS_READER 39, PASS_THROUGH 13, ALLOWLIST_DROP 11, DEFAULT_BUCKET 3, EXPLICIT_HANDLING 4,
  RAISES 0.
- **Added since, or outside the 69:** 3 more RAISE (holdings_snapshot and the two firm-mix summaries); 2 closed contract
  enums; mix_views x2 ALLOWLIST_DROP; the IR portal Holdings components DEFAULT_BUCKET to `Unclassified`.
- **bd-securities today:** 10,877 items (equity 6,073, fixed_income 3,145, alternatives 1,644, cash 15); 0 values
  outside the list, so nothing crashes today.

### Must change BEFORE a new value is written (step B1), with owners

| Effect | Reader (file:line) | Owner |
|---|---|---|
| RAISES | `holdings_snapshot.py` ASSET_CLASS_VALUES :748 / refuse :800; both `HoldingsSnapshot.schema.json` enums (:523, :578) | ~M (producer) and the contract owner (~P) |
| RAISES | `runners_49f/d06_firm_mix_summary.py` CLASS_ORDER :46, SystemExit :96-98 | 49F runners owner |
| RAISES | `runners_cot/d08_cot_mix_summary.py` :51-54 | COT runners owner |
| Silent drop | BD `C_06` MIX :179, COT `C_06` MIX :173 (the mix sums below 1) | BD DS / ~M (COT C_06 grant) |
| Silent drop | BD/COT `lib/mix_views.py` :19 | BD DS / COT DS |
| Silent drop | BD `D_03` :101, COT `D_03` :102; BD `D_04` :457, COT `D_04` :561 | BD DS / ~M |
| Silent drop | portal `AdvisorIntelligence/_shared/lib/composition.ts` :32/:108 (normalize, then re-percent) and the partner `ordered` lists | 2.0.0_SA_COO~D (portal) |
| Wrong class | IR portal `contracts/adapt.ts` :1005, `tabs/holdings/assetClass.ts` :33-40 (Unclassified; the colours for both classes already exist at :22-23) | ~D, the v0.14 cell the CTO named |
| Wrong class | `black_diamond/scripts/silver/build_bd_assets_dim.py` :57-62 | BD silver owner |
| Undoes the write if re-run | `classification/seed_canonical_securities.py` :314-337 (resets VXX/UVXY/PDBC to equity, QBER to fixed_income); `seed_bd_securities.py` :82 (whole-item put) | BD classification owner: guard or retire before B2 |

Not blocking: the LLM writer gates (both `B_01b`, `classify_bd_securities.py`, INF `classify_assets.py`) only refuse
the new classes for NEW securities; E_25 is an audit; the positioning and partner readers already handle arbitrary
values.

## Part A (rides R4): tags already in the list

17 of the 30 write-set keys:
- **fixed_income -> equity update, 1 key:** CASH.
- **alternatives -> equity update, 1 key:** VNQ.
- **puts, 15 keys:** 13 equity and 2 fixed_income, tickers absent from bd-securities.

Served delta at the served 09-22 revisions: 49F CASH $14,969 and VNQ $2,558; INF VNQ $0; COT CASH/FXFXX $2,868,029.
The puts are equal-class for any reader that already defaults an absent ticker to equity. Readers: the same bd-securities
readers; no reader crashes on these values.

## Part B (a sequence): `structured` and `commodities`

- **B1:** each reader above admits both classes, each under its owner and deploy rules.
- **B2:** the 13 remaining write-set keys are written, 7 commodities (including PHYS) and 4 structured updates from
  alternatives, plus 1 structured and 1 commodities off equity, under a ledger.
- **B3:** Holdings shows them at the next publication (R4).

Served delta at the served 09-22 revisions: 49F about $21.5M (VXX, QBER, JEPI, GLD, IAU, SLV, USO, PDBC); INF $1.75M
(VXX, UVXY); COT about $12.8M (GLD $9.49M, VXX $2.09M, JEPI $1.22M).

## Rollback per key

Per key, a conditional UpdateItem back to the recorded prior class (`bd_asset_class_now` in the write set), or a
DeleteItem for a put, under a human confirmation. The code admissions in B1 are backward-compatible: they add list
members and remove nothing.

## The ask

Sign Part A to ride R4; sign Part B as the B1 -> B2 -> B3 sequence, with the B1 readers routed to their owners; or
refuse, naming what is missing.
