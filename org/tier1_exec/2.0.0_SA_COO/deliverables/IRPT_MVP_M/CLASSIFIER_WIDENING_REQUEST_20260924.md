# Request -- widen the security classifier for the securities Investor Reporting serves (CTO 100925)

**From:** 2.0.0_SA_COO~M. **To:** 1.0.0_SA_CTO. **Date:** 2026-09-24 ~23:4xZ.
**Andrew's ask (brief, H:91-96):** "expand the ETF classifier ... to include all the securities that are coming in
through the investor reporting".
**Data:** `CLASSIFIER_WIDENING_REQUEST_ROWS_AND_READERS_20260924.json` beside this file. It holds every row with its
identifiers and served dollars, and every reader path.

## Table

DynamoDB `bd-securities`: 9,732 items with a ticker at the 22:5xZ scan, holding four classes (`equity` 5,510,
`fixed_income` 2,608, `alternatives` 1,599, `cash` 15). The canonical reader is
`data/black_diamond/scripts/gold/lib/etf_classifier.py` `ETFClassifier`, plus the `etf_classifications_dynamodb.py`
copies in the Lambdas.

## Rows

The served SECURITY nodes with `asset_class_basis` NONE, in COT fc199c8e, INF ba9001d5 and 49F 9ab377ce. Measured,
not proposed: this request names no class for any of them.

| Firm | Distinct | Nodes | Served USD | What they are |
|---|---|---|---|---|
| COT | 101 | 233 | 78,003,958.56 | Held-away and manual assets. The top three: `4175_VOYA` "Voya" $25.97M, `CXMANUAL_HOME` "Investor Manual Asset - Home" $8.38M, `4175_CCA_EIGER_III_OPP` "CCA Eiger III Opportunity LP" $6.15M. |
| 49F | 78 | 236 | 35,874,668.38 | 62 carry NO symbol and NO name, only a CUSIP (the largest $23.67M). The classifier keys on ticker or name, so it cannot see them. |
| INF | 108 | 131 | 688,599.96 | Masked CUSIPs such as `06xxxx4Y5`. |

## Three facts that change what "widen" means

1. **COT's automatic path is a silent no-op.**
   - `data/cot/scripts/gold/B_01b.classify_new_securities.py` scans `opal-data-cot` `gold/timeseries/holdings_lots/`.
   - That prefix is EMPTY in `opal-data-cot` and in `opal-data-cottonwood`. The legacy `gold/holdings_lots/` is empty
     in `opal-data-cot`; it was not read in `opal-data-cottonwood`.
   - Its own read-only dry run, 23:30Z `--dry-run --full-scan`, reads "Total holdings_lots partitions: 0 ... Nothing to
     classify".
   - BD's same prefix in `opal-data-bd` holds partitions through 2026-09-18. A new COT security never reaches the table.
2. **The classifier cannot see a row without a ticker.** `ETFClassifier.__init__` skips an item whose `ticker` is
   empty, name aliases included (`etf_classifier.py:61-63`). A bond, note or private asset classified by name into the
   table would stay invisible to TABLE and NAME_ALIAS.
3. **The producer classifies through OpenAI.** `B_01b` `call_openai`, secret `openai-api-key`. Running it for these rows
   is vendor egress: Andrew's per-use word, not a lane grant alone.

## Readers of the table: 69 first-party code paths

From the census on `bd-securities|ETFClassifier|etf_classifier|etf_classifications_dynamodb`, corpus default: 2,525
hits across 44,007 files; 631 paths listed; tests, docs and org records excluded. The full list is in the JSON. By
system:
- BD gold: `data/black_diamond/scripts` B_01, B_01b, C_06, D_03, D_04, E_18, E_25 and the rest.
- COT gold: the same set under `data/cot/scripts`.
- INF: `data/inf/scripts` INF_D_03, INF_D_07a, classify_assets.
- 49F: `data/assets/scripts` a07_dim_asset_classification, the satellites, chain_49f_entrypoint.
- Schwab canonical: `data/canonical/schwab` build_gold_firm_composition.
- **Positioning:**
  - `data/etfs/scripts/gold/etf_positioning_publisher.py` and the `etf-positioning-producer` Lambda;
  - `yang-generate-positioning` and `yang-generate-holdings-attribution`;
  - `lib/research/identity/positioning_chain.py`;
  - `portal/src/pages/Positioning/shared/{satelliteAdapter,satelliteSet}.ts`.
- Partners: `opal-partners-data`.
- News: `semantic-news-layer3-curation`.
- Investor Reporting: the Holdings producer (`holdings_snapshot.py`) and `portal/src/pages/InvestorReporting/.../assetClass.ts`.
- IAM: `bd-pipeline`, `cot-pipeline`, `etfs-positioning`, `news-pipeline`, `partners-api`, `shared-infra`.

A row added to the table changes the class every one of these reads for that security. So this is a served-output act
across products, not an Investor Reporting-only one.

## Decisions this needs (none is this seat's to take)

1. **Andrew:** whether held-away and manual assets (a client's home, annuities, private LPs) are classified at all.
   The enum has no real-estate or other value; Positioning's own `ASSET_CLASS` has `realEstate` and `other`.
2. **Andrew:** the per-use word for an OpenAI classification run over the named rows, if that is the method.
3. **CTO:** the owner for the two defects. COT's `B_01b` scans an empty prefix (DS lane, `data/cot/scripts/gold`), and
   the loader skips rows without a ticker. It could key by the table's own PK or the CUSIP instead
   (`data/black_diamond/scripts/gold/lib/etf_classifier.py`, BD lane).
4. **CTO:** for 49F's 62 CUSIP-only rows, whether the Holdings producer fills symbol and name from the Schwab security
   master (a Holdings producer change, this seat's) before any classification.
