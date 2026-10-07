DENOMINATOR: 58874 files scanned by comp-find (corpus=all), 5471 hits; census 46 files of 189 raw git-grep files (CTO command at b07521c5dd: git grep -l -E "bd-securities|BD_SECURITIES_TABLE" over *.py *.ts *.tsx *.tf *.json, minus data/black_diamond/**, org/** and test files); plus resolve_tickers.py (named by the order face, in the excluded BD tree); aws nodes UNREAD (comp-find --corpus aws is BLOCKED for this principal, row MDPF_SECCLASS-W25-S3), replaced by a direct read-only live plane read: 290 IAM roles + 43 customer-managed policies + 232 Lambda functions + the etf-classifications table (3,507 rows) scanned 2026-10-07; portal origin/DEV 8ddfe409 searched for callers.

# OLD LIST READER TRACE -- MDPF_SECCLASS SC-e-38 (FWD-5), 2026-10-07, 0.9.0_WK_MDPF_SECCLASS~25

Instrument: `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/old_list_reader_trace.py` (read-only; prints the census and the live plane).
The old list is DynamoDB `bd-securities`, us-east-1, hash key `ticker`, 10,965 rows (describe_table 2026-10-07).
Every rule below is read from the reader's own code at the cited line, never predicted. A line number is at HEAD 1910d1f20f.

Live-plane facts, read 2026-10-07 with boto3 (read-only), that the verdicts lean on:
- IAM: 290 roles scanned. Customer-managed policy `bd-securities-access` is attached to `bd-exporter-ec2-role` and `partners-lambda-role` (the opal-partners-data role). Role-inline policies naming the table: `bd-exporter-ec2-role/advi-49f-chain-access`, `irpt-49f-holdings-role`, `irpt-cot-holdings-role`, `irpt-inf-holdings-role`, `lambda-execution-role/layer3-bd-securities-read`. No other role names it. `opal-news-lambda-role` carries the AWS-managed AmazonDynamoDBFullAccess (blanket, names no table). `cot-exporter-ec2-role` and `cot-gold-layer-ec2-role` carry no grant on the table.
- Lambda: 232 functions scanned; none carries an environment variable naming the table. `semantic-news-layer3-curation` has NO environment (the `SECURITIES_TABLE` default `bd-securities` applies); `opal-partners-data` has only `USERS_TABLE` (the table name is hard-coded in its code).
- etf-classifications write census by `updated_by` (3,507 rows): `<none>` 1,926; `rivalfunds-backfill` 640; `mdpf-secclass-scheduled` 348 (all `CUSIP:`-keyed, all last_updated 2026-09-30); `seed-etf-constituents (...)` 179 and 59; `seed-script` 177; `mdpf-secclass-bd-mapped` 67; `mdpf-secclass-cusip-rows` 65; `mdpf-secclass-remap-b` 33; `mdpf-secclass-model` 13; `e18-scheduled` 0. No row is stamped by a recurring producer for a ticker first held after 2026-09-30.
- The canonical-row producer `etf_classification_scheduled.py` has `bd-securities` as its ONLY wired live input (GICS and Schwab lookups default to None, lines 43-46 and 377-388), so when the old-list writers stop it cannot resolve a first-held security either.

Summary of verdicts (full sections follow): NEEDS-OLD-LIST -- the 49F/COT Advisor Intelligence mix artifacts via `a07_dim_asset_classification.py`; the IRPT Holdings fallback (`bd_securities_fallback.py` and `holdings_snapshot.py`); `resolve_tickers.py` (reads `asset_name_raw`, an attribute `etf-classifications` does not carry); `etf_classification_scheduled.py` (the canonical producer's only input). DEAD-READ -- `semantic-news-layer3-curation` (no trigger, no log stream), the opal-partners-data composition route (no portal caller; classifier loaded at every cold start), the Cottonwood E_18 and B_01b (the host role cannot read the table), `classify_assets.py` (no caller, no schedule). Everything else in the census is a grant, schema, census JSON, comment or doc: NOT-A-READER.

## READER: Advisor Intelligence screens -- firm and COT mix/composition artifacts via data/assets/scripts/gold/runners_49f/a07_dim_asset_classification.py

READS: the derived artifact dim_asset_classification (and alias_key_expansion), a parquet built from a full paginated scan of bd-securities at build time (ticker, asset_class, name_aliases, asset_name_raw); the 49F chain's d06_firm_mix_summary.py and COT's d08_cot_mix_summary.py join it to positions, and the portal's Advisor Intelligence mix and composition files (mix_summary.json, mix views, platinum summaries) are emitted from those joins
EVIDENCE: data/assets/scripts/gold/runners_49f/a07_dim_asset_classification.py:198
VERDICT: NEEDS-OLD-LIST -- the served Advisor Intelligence asset-class mix for 49F (and Cottonwood's mix_summary) is classified from bd-securities rows plus regex fallbacks, and a07 never reads etf-classifications (0 references), so it cannot be repointed by a switch alone; DDB_TABLE is hard-coded at line 58 and the chain role bd-exporter-ec2-role holds the Scan grant (bd-pipeline/iam.tf:1234).
MISSING-ROW: a07_dim_asset_classification.py:220-255 classify(): no ticker row and no alias row -> name regex (alternatives, cash, fixed_income) -> a 1-5 letter ticker (optional .X) is 'equity' -> else '' which line 374 writes as 'UNCLASSIFIED-LOUD'; STEP B (lines 356-378) retries the other firms' name variants for the same security key
SERVED-NEW: a security first held after the writers stop gets: 'equity' (source regex-name) if its ticker is 1-5 letters, 'alternatives' or 'fixed_income' if its name matches the regex families, else UNCLASSIFIED-LOUD; d06_firm_mix_summary.py:88-95 serves that as the Advisor mix's own 'unclassified' bucket (never an error, never dropped), while d08_cot_mix_summary.py:9-15 folds UNCLASSIFIED-LOUD into equity in the top-level COT mix and shows it as 'unclassified' only in mix_periods
CANONICAL-PRODUCER: NONE: a07 does not read the canonical table at all; no producer gives a first-held security a row it would read; the nearest, E_18, measured 0 live rows ('e18-scheduled') on 2026-10-07, and the 348 'mdpf-secclass-scheduled' rows are CUSIP-keyed and written once on 2026-09-30

## READER: Advisor Intelligence screens -- books composition route, infra/aws/lambda/v2_portal/partners/lambdas/opal-partners-data/lambda_function.py

READS: a module-level ETFClassifier.instance() (line 64) that scans bd-securities at every cold start (ticker, asset_class, sub_asset_class, name_aliases), used only by _classify_holding (lines 1025-1051) in handle_books_composition for GET /api/scoped/partners/books/{relationship|account}/{id}/composition
EVIDENCE: infra/aws/lambda/v2_portal/partners/lambdas/opal-partners-data/lambda_function.py:1254
VERDICT: DEAD-READ -- the table is read at every cold start (partners-lambda-role holds bd-securities-access) but its only consumer is a route that no portal screen calls: portal origin/DEV 8ddfe409 holds no request to books/relationship|account/{id}/composition (the Advisor Intelligence screens call platinum-summary and mix-views, which serve prebuilt S3 files without classifying), and the function's CloudWatch group (14-day retention, 3,517 invocations 2026-09-23..2026-10-07) holds 0 composition successes against 48 log lines naming platinum-summary; unmeasured: API-gateway access logs and any non-portal caller, so this is DEAD-READ for the screens, not proven for the API.
MISSING-ROW: lambda_function.py:1051 and etf_classifier.py:92-107: no row -> name regex (alternatives; cash returns ''; fixed_income) -> a 1-5 letter ticker is 'equity' -> '' which line 1051 maps to 'other'
SERVED-NEW: if the route were called: a security first held after the writers stop is 'equity' by ticker shape, 'alternatives'/'fixed_income' by name pattern, else 'other', which lines 1311-1313 count as the response's 'unclassified' {count, market_value}; no error, nothing dropped
CANONICAL-PRODUCER: NONE: this function never reads etf-classifications (0 references), and no producer gives a first-held security a canonical row (e18-scheduled 0 rows; 2026-10-07 scan)

## READER: infra/aws/lambda/v2_portal/partners/lambdas/opal-partners-data/etf_classifier.py

READS: full paginated scan of bd-securities on first instantiation (table_name default 'bd-securities'), building _ticker_map and _name_map (ticker, asset_class, sub_asset_class, name_aliases)
EVIDENCE: infra/aws/lambda/v2_portal/partners/lambdas/opal-partners-data/etf_classifier.py:41
VERDICT: DEAD-READ -- the library is the loader behind the opal-partners-data composition route (see the Advisor section for that file): a read at every cold start whose only consumer is a route the portal never calls; the deployed function has no environment variable for the table, so the hard-coded default is what the live function reads.
MISSING-ROW: etf_classifier.py:92-107 (name regex then 1-5 letter ticker -> equity, else '')
SERVED-NEW: the same as the Advisor books composition route: 'equity' by ticker shape, 'alternatives'/'fixed_income' by name, else '' which the caller reports as 'other'; a scan failure (lines 59-62) empties both maps and logs at ERROR, and the 14-day log group holds no such ERROR line
CANONICAL-PRODUCER: NONE (no canonical read; e18-scheduled 0 rows on 2026-10-07)

## READER: infra/aws/lambda/semantic-news-layer3-curation/lambda_function.py

READS: a cold-start scan of bd-securities projecting ticker and asset_class (lines 68-96), keeping non-NAME:: tickers whose asset_class is equity or fixed_income as OPAL_TICKERS, used to filter each narrative's mentioned_tickers (lines 749-758); SECURITIES_TABLE env default 'bd-securities' (line 65)
EVIDENCE: infra/aws/lambda/semantic-news-layer3-curation/lambda_function.py:65
VERDICT: DEAD-READ -- the function is deployed (python3.12, last modified 2026-04-09, role lambda-execution-role with layer3-bd-securities-read) but nothing runs it: news-pipeline/eventbridge.tf:11-17 records its two schedules DELETED, the live function has no environment, no resource policy and no event-source mapping, and its log group (14-day retention) stores 0 bytes, while the live curation function opal-news-layer3-curation (rule disabled, chain-invoked by news_trending_analysis/lambda_function.py:2078) has code that names no securities table; if it were invoked, the deployed config reads bd-securities by the code default.
MISSING-ROW: lambda_function.py:75-78 and 754-758: a ticker with no bd-securities row (or with a class other than equity/fixed_income) is not in OPAL_TICKERS and is removed from mentioned_tickers; a failed scan returns an empty set (lines 91-93) and then the filter is skipped entirely (line 750)
SERVED-NEW: if invoked: a security first held after the writers stop is dropped from every narrative's mentioned_tickers (kept: only the 3,660 tickers the old list calls equity or fixed_income; 2,350 of those 3,660 are in etf-classifications, 1,310 are not); today nothing is served because the function is never invoked
CANONICAL-PRODUCER: NONE: the function never reads etf-classifications (0 references); no producer gives a first-held security a canonical row

## READER: data/black_diamond/scripts/classification/resolve_tickers.py

READS: a full scan of bd-securities (lines 152-162) and the attributes asset_name_raw, name_aliases and ticker, used as a NAME-to-TICKER dictionary by resolution methods 2, 3, 5 and 6 (exact name, prefix, company-stem, fund-stem) to build gold/dimensions/ticker_resolution.parquet
EVIDENCE: data/black_diamond/scripts/classification/resolve_tickers.py:152
VERDICT: NEEDS-OLD-LIST -- it reads asset_name_raw (present on 10,905 of 10,965 old rows) and name_aliases, and etf-classifications carries neither attribute (live attribute union: ticker, asset_class, sub_asset_class, name on 883 rows, and others; no asset_name_raw, no name_aliases), so a repoint is a new name field, not a switch.
MISSING-ROW: resolve_tickers.py:191-214, 217-243, 263-345, 347-384: a name with no old row is not resolved by methods 2, 3, 5 (db stem; the yfinance guess at lines 318-336 still runs) or 6, and falls out of the resolution table unresolved (line 689 builds the table from the resolved rows only)
SERVED-NEW: a name first held after the writers stop is not resolved by the old list; ticker_resolution.parquet keeps no row for it (apart from method 1, a ticker already in holdings_lots, method 4, the etf_classification.py alias dict, and a method 5 yfinance guess), so the holding stays tickerless downstream; no error
CANONICAL-PRODUCER: NONE: no producer gives a first-held security an etf-classifications row carrying a name-to-ticker mapping (the table's 'name' attribute is on 883 of 3,507 rows, written by seeds and mdpf-secclass-* one-offs; e18-scheduled 0)

## READER: data/assets/scripts/gold/investor_reporting/bd_securities_fallback.py

READS: the IRPT Holdings declared FWD-6 fallback (PRD S21): a full paginated scan of the table named through the naming registry ('%s-securities', lines 35-46 and 95-109) -- ticker, asset_class, sub_asset_class, name_aliases, asset_name_raw -- loaded into _ticker_map and _name_map
EVIDENCE: data/assets/scripts/gold/investor_reporting/bd_securities_fallback.py:95
VERDICT: NEEDS-OLD-LIST -- Holdings reads etf-classifications first and falls to this module for a ticker the canonical table lacks, so the old list still decides the class of every held ticker the canonical table does not hold; the table name is assembled at run time, so a text census of the literal finds this file only through its docstrings (row MDPF_SECCLASS-W25-S5); removal is FWD-13's.
MISSING-ROW: bd_securities_fallback.py:127-167 classify(): a ticker with no row and no alias row -> name patterns (alternatives; cash and fixed-income both -> fixed_income) -> a 1-5 letter ticker (optional .X) is 'equity' -> '' (line 167)
SERVED-NEW: the Holdings node for a security first held after the writers stop reads: 'equity' (basis TICKER_SHAPE) for a 1-5 letter ticker, 'fixed_income' or 'alternatives' (basis NAME_PATTERN) by name, else 'unclassified' (basis NONE); never an error and never dropped (see holdings_snapshot.py:963-971)
CANONICAL-PRODUCER: NONE reaching a first-held security: the canonical-first branch needs an etf-classifications row and e18-scheduled wrote 0 rows (2026-10-07 scan); the 348 mdpf-secclass-scheduled rows are CUSIP-keyed, all 2026-09-30

## READER: data/assets/scripts/gold/investor_reporting/holdings_snapshot.py

READS: the IRPT Holdings builder (PRD S21): canonical_classifier() loads the bd_securities_fallback scan (lines 902-913) and classify_security() consults etf-classifications first, then the fallback, for every SECURITY node of 49financial, cottonwood and inflection; the three irpt-*-holdings roles carry the Scan grant
EVIDENCE: data/assets/scripts/gold/investor_reporting/holdings_snapshot.py:963
VERDICT: NEEDS-OLD-LIST -- the served Holdings asset_class for a ticker absent from etf-classifications comes from the old list's rows through the fallback; the builder refuses to run (lines 912-913, ValueError) if the fallback loads no rows, so a table removed before this reader is repointed stops Holdings rather than degrading it.
MISSING-ROW: holdings_snapshot.py:954-971 classify_security(): canonical_lookup miss (954) -> fallback classify (963) -> asset_class = answer or 'unclassified' (967), with the mirror-disagreement refusal at 964-966
SERVED-NEW: a security first held after the writers stop is served with the fallback's layer 3-4 answer: 'equity' for a 1-5 letter ticker, 'fixed_income' or 'alternatives' by name pattern, else 'unclassified' (asset_class_basis TICKER_SHAPE, NAME_PATTERN or NONE); the CASH-named cash line is 'cash' before either table (lines 948-952)
CANONICAL-PRODUCER: NONE reaching a first-held security (e18-scheduled 0 rows on 2026-10-07; the 348 mdpf-secclass-scheduled rows are CUSIP-keyed and written once, 2026-09-30)

## READER: data/cot/scripts/gold/E_18.detect_new_securities.py

READS: a full scan of bd-securities for known keys (lines 244-245, load_known_tickers) and for asset_name_raw prefix matching (line 248), plus default_bd_securities_lookup(BD_SECURITIES_TABLE) handed to plan_rows (line 322) as the classification input for each candidate
EVIDENCE: data/cot/scripts/gold/E_18.detect_new_securities.py:245
VERDICT: DEAD-READ -- on the Cottonwood host the scan is denied: cot-exporter-ec2-role and cot-gold-layer-ec2-role carry no bd-securities grant (IAM read 2026-10-07; cot-pipeline/iam.tf:363 and data/cot/scripts/gold/lib/etf_classifier.py:13-16 say the host never had access) and load_known_tickers has no handler, so the script aborts at line 245 before the canonical write at 317-330; unmeasured: no call was made, this is a policy read.
MISSING-ROW: E_18.detect_new_securities.py:277: a pair whose key is not in the old list's known set is a candidate; 305 feeds only real-ticker candidates to plan_rows, whose classify_asset_class returns (None, None, None) when the old list has no usable row (etf_classification_scheduled.py:371-375, 473-474) and lists it unresolved
SERVED-NEW: nothing is served from this script; a security first held after the writers stop is a candidate the script cannot classify (bd lookup None, GICS and Schwab lookups unwired), so it writes no canonical row and prints it as unresolved
CANONICAL-PRODUCER: NONE reaches a first-held security: E_18 (data/cot/scripts/gold/E_18.detect_new_securities.py:317-323, updated_by 'e18-scheduled') measured 0 live rows in etf-classifications on 2026-10-07 (scan of 3,507 rows); the 348 'mdpf-secclass-scheduled' rows are CUSIP-keyed, all written 2026-09-30; the Cottonwood host cannot read the table E_18 scans first, so the path aborts at E_18:245, and its only wired classification input is the old list (etf_classification_scheduled.py:371-375)

## READER: data/cot/scripts/gold/B_01b.classify_new_securities.py

READS: a full scan of bd-securities for existing keys (lines 156-168, called at 257) to decide which (ticker, asset_name) pairs are new; it then classifies them by OpenAI and WRITES them to bd-securities (an old-list writer as well as a reader)
EVIDENCE: data/cot/scripts/gold/B_01b.classify_new_securities.py:257
VERDICT: DEAD-READ -- the same host-role gap as E_18: the Cottonwood gold roles hold no bd-securities grant, so the scan at line 257 is denied, and the script returns at lines 235-236 when holdings_lots has no new partitions (E_18's docstring, lines 3-7, records the Cottonwood gold/holdings_lots/ prefix empty live, a held claim I could not re-read because the firm bucket reads deny this principal); its only effect was to create old-list rows, which the writers' retirement (SC-e-35) governs.
MISSING-ROW: B_01b.classify_new_securities.py:263: a pair whose key is not in the scanned existing set becomes a new row to classify by OpenAI and put into bd-securities
SERVED-NEW: nothing is served from this script; a security first held after the writers stop gets no old-list row from it on this host (the scan is denied before any write) and no canonical row either
CANONICAL-PRODUCER: NONE: B_01b writes only bd-securities; e18-scheduled wrote 0 rows (2026-10-07 scan)

## READER: data/inf/scripts/classification/classify_assets.py

READS: the Inflection classifier: a full scan of bd-securities for existing keys (lines 117-126, called at 257), a BatchGetItem library entry get_classifications (lines 225-242) returning asset_class, sub_asset_class, confidence, needs_review, classified_by; the CLI path then classifies net-new keys by gpt-4o-mini and WRITES them to bd-securities
EVIDENCE: data/inf/scripts/classification/classify_assets.py:257
VERDICT: DEAD-READ -- no caller of get_classifications and no scheduler, workflow or script that runs the CLI exists anywhere in the repo outside docs and the RCG label ledger (git grep over the whole repo, 2026-10-07), and Inflection's served mix no longer uses it (INF_D_03.composition_artifacts.py:560 replaced it); unmeasured: a manual run on a device, and no live schedule was searched for by name.
MISSING-ROW: classify_assets.py:260: a key not in the scanned existing set is a net-new key classified by gpt-4o-mini and put into bd-securities; get_classifications leaves a key with no row ABSENT from its result (docstring, line 232)
SERVED-NEW: nothing is served from this script; with no caller, a security first held after the writers stop is not read here at all
CANONICAL-PRODUCER: NONE: this script writes only bd-securities; no canonical producer reaches a first-held security (e18-scheduled 0 rows)

## READER: infra/aws/lambda/v2_portal/_shared/etf_classification_scheduled.py

READS: default_bd_securities_lookup (lines 526-541): a GetItem on bd-securities per ticker, used as the first and only wired live input to classify_asset_class (lines 371-375) and classify_cusip_asset_class (lines 227-228) for the canonical producer's new rows (the old row's asset_class and sub_asset_class, taken only when a member of the canonical vocabulary)
EVIDENCE: infra/aws/lambda/v2_portal/_shared/etf_classification_scheduled.py:536
VERDICT: NEEDS-OLD-LIST -- the one producer that is meant to give a first-held security an etf-classifications row has no input other than the old list wired (gics_lookup and schwab_lookup default to None; the module says so at lines 43-46), so when the old-list writers stop it resolves nothing new; a deliberate input change belongs to FWD-7's remaining work, not this trace.
MISSING-ROW: etf_classification_scheduled.py:371-388 and 473-474: no old row (or a row whose class is not a direct member of the canonical vocabulary) -> GICS None -> Schwab None -> (None, None, None) -> the ticker is listed unresolved and no row is planned
SERVED-NEW: nothing is served from this module; a security first held after the writers stop is listed unresolved and no etf-classifications row is written for it
CANONICAL-PRODUCER: ITSELF, measured: updated_by 'e18-scheduled' 0 rows and 'mdpf-secclass-scheduled' 348 rows (all CUSIP-keyed, last_updated 2026-09-30) in the 3,507-row table scanned 2026-10-07; its callers are E_18 (Cottonwood, denied the old-list scan) and Black Diamond's E_18 (data/black_diamond, outside the census)

## READER: data/assets/scripts/gold/runners_49f/chain_49f_entrypoint.py

READS: its docstring line naming the table as a07's substrate; the file composes stages and invokes a07 (line 164) but opens no table itself
EVIDENCE: data/assets/scripts/gold/runners_49f/chain_49f_entrypoint.py:61
VERDICT: NOT-A-READER -- the reader is a07_dim_asset_classification.py, traced above; this orchestrator names the substrate in a comment only.

## READER: data/canonical/schwab/gold/build_gold_firm_composition.py

READS: nothing: its docstring says NO DynamoDB bd-securities lookup and the class comes from the Schwab security master
EVIDENCE: data/canonical/schwab/gold/build_gold_firm_composition.py:7
VERDICT: NOT-A-READER -- the file states it does not read the table, and it holds no DynamoDB call.

## READER: data/cot/scripts/gold/B_01.holdings_lots.py

READS: a docstring naming B_01b's purpose; no table call in the file
EVIDENCE: data/cot/scripts/gold/B_01.holdings_lots.py:2967
VERDICT: NOT-A-READER -- a comment in save_lots describing a downstream consumer, not a read.

## READER: data/cot/scripts/gold/build_canonical_prices_v2.py

READS: a docstring phrase ('bd-securities validated') about a Yahoo ticker; the file has no DynamoDB call
EVIDENCE: data/cot/scripts/gold/build_canonical_prices_v2.py:390
VERDICT: NOT-A-READER -- a comment in resolve_prices_for_asset, not a read.

## READER: data/cot/scripts/gold/lib/etf_classifier.py

READS: etf-classifications through the shared client; the docstring states it never opens bd-securities
EVIDENCE: data/cot/scripts/gold/lib/etf_classifier.py:83
VERDICT: NOT-A-READER -- this library REPLACED the old scan and reads the canonical table only (lines 13-16 record that the old scan failed on every run on the Cottonwood host).

## READER: data/cot/scripts/gold/lib/s3_layout.py

READS: nothing: a comment naming the B_01b watermark's purpose
EVIDENCE: data/cot/scripts/gold/lib/s3_layout.py:258
VERDICT: NOT-A-READER -- a comment beside an S3 key constant, not a read.

## READER: data/inf/scripts/gold/INF_D_03.composition_artifacts.py

READS: nothing: comments say the class comes from Orion-native silver/assets_v2 and replaces the old bd-securities classifier
EVIDENCE: data/inf/scripts/gold/INF_D_03.composition_artifacts.py:560
VERDICT: NOT-A-READER -- the file states it replaced the old-list classifier and holds no DynamoDB call.

## READER: infra/aws/lambda/investor-reporting/ycharts/generate/comparison_catalogue.py

READS: the Opal model catalogue and etf-classifications; the docstring says it never reads bd-securities
EVIDENCE: infra/aws/lambda/investor-reporting/ycharts/generate/comparison_catalogue.py:10
VERDICT: NOT-A-READER -- a docstring ruling out the old list as a source, not a read.

## READER: infra/aws/lambda/v2_portal/yang_pipeline/set-instrument-kind.py

READS: etf-classifications only; the docstring says the script NEVER reads bd-securities
EVIDENCE: infra/aws/lambda/v2_portal/yang_pipeline/set-instrument-kind.py:25
VERDICT: NOT-A-READER -- a docstring ruling out the old list as a source, not a read.

## READER: docs/briefs/cmpaws-iam-axis-census-20260603.json

READS: an IAM census snapshot of 2026-06-03 recording the policy bd-securities-access
EVIDENCE: docs/briefs/cmpaws-iam-axis-census-20260603.json:1064
VERDICT: NOT-A-READER -- a dated census document, not code.

## READER: docs/briefs/irpt-manual-walk-v2-findings-20260929.json

READS: a findings document mentioning the producer's move to etf-classifications
EVIDENCE: docs/briefs/irpt-manual-walk-v2-findings-20260929.json:519
VERDICT: NOT-A-READER -- a findings document, not code.

## READER: docs/briefs/irpt-ui-review-findings-20260926.json

READS: a findings document mentioning the old list's class writes
EVIDENCE: docs/briefs/irpt-ui-review-findings-20260926.json:930
VERDICT: NOT-A-READER -- a findings document, not code.

## READER: docs/contracts/investor-reporting/v1/ComparisonCatalogue.schema.json

READS: nothing: a contract description saying the catalogue has no bd-securities substitution
EVIDENCE: docs/contracts/investor-reporting/v1/ComparisonCatalogue.schema.json:6
VERDICT: NOT-A-READER -- a schema description string, not a read.

## READER: infra/aws/lambda/investor-reporting/_contracts/ComparisonCatalogue.schema.json

READS: nothing: the same contract description in the deployed copy
EVIDENCE: infra/aws/lambda/investor-reporting/_contracts/ComparisonCatalogue.schema.json:5
VERDICT: NOT-A-READER -- a schema description string, not a read.

## READER: infra/aws/lambda/ci/shared-infra-resource-map.json

READS: a resource map entry for the table and its access policy
EVIDENCE: infra/aws/lambda/ci/shared-infra-resource-map.json:114
VERDICT: NOT-A-READER -- a registry listing of the table and policy, not a reader.

## READER: infra/aws/nfra_terraform_p1/desired_index.json

READS: a Terraform desired-state index entry for the table ARN and two policy attachments
EVIDENCE: infra/aws/nfra_terraform_p1/desired_index.json:9753
VERDICT: NOT-A-READER -- an infrastructure index, not a reader.

## READER: infra/aws/nfra_terraform_p1/slice_iam.json

READS: an IAM slice entry for the bd-securities-access policy
EVIDENCE: infra/aws/nfra_terraform_p1/slice_iam.json:1855
VERDICT: NOT-A-READER -- an infrastructure slice, not a reader.

## READER: infra/aws/nfra_terraform_p1/slice_storage.json

READS: a storage slice entry for the table
EVIDENCE: infra/aws/nfra_terraform_p1/slice_storage.json:338
VERDICT: NOT-A-READER -- an infrastructure slice, not a reader.

## READER: infra/aws/terraform/bd-pipeline/iam.tf

READS: a GRANT: AdviChainBdSecuritiesScan, dynamodb:Scan on the table, on bd-exporter-ec2-role (a07's build-time scan); comments at 735-751 record the BD writers' retirement
EVIDENCE: infra/aws/terraform/bd-pipeline/iam.tf:1242
VERDICT: NOT-A-READER -- a policy statement that lets the a07 reader scan the table, not a reader itself (the reader is a07, traced above).

## READER: infra/aws/terraform/cot-pipeline/iam.tf

READS: a comment: the Cottonwood host holds etf-classifications only, 'NOT bd-securities'
EVIDENCE: infra/aws/terraform/cot-pipeline/iam.tf:363
VERDICT: NOT-A-READER -- a comment recording the host never had the grant; this is the evidence behind the E_18 and B_01b verdicts.

## READER: infra/aws/terraform/investor-reporting/CHANGELOG.json

READS: a changelog entry describing the narrowed Holdings release with the declared fallback
EVIDENCE: infra/aws/terraform/investor-reporting/CHANGELOG.json:1679
VERDICT: NOT-A-READER -- a changelog, not a reader.

## READER: infra/aws/terraform/investor-reporting/directory/holdings_refresh.tf

READS: a GRANT: ClassifierScan, dynamodb:Scan on the declared fallback table for the three irpt-*-holdings roles
EVIDENCE: infra/aws/terraform/investor-reporting/directory/holdings_refresh.tf:128
VERDICT: NOT-A-READER -- a policy statement for the IRPT Holdings fallback reader (traced above), not a reader itself.

## READER: infra/aws/terraform/news-pipeline/CHANGELOG.json

READS: a changelog entry 'filter mentioned_tickers against Opal bd-securities table'
EVIDENCE: infra/aws/terraform/news-pipeline/CHANGELOG.json:507
VERDICT: NOT-A-READER -- a changelog, not a reader.

## READER: infra/aws/terraform/news-pipeline/cross-firm-bucket-read-deny.tf

READS: a comment naming layer3-bd-securities-read as living on lambda-execution-role
EVIDENCE: infra/aws/terraform/news-pipeline/cross-firm-bucket-read-deny.tf:60
VERDICT: NOT-A-READER -- a comment inside a deny policy, not a reader.

## READER: infra/aws/terraform/news-pipeline/cross-firm-bucket-write-deny.tf

READS: a comment naming layer3-bd-securities-read among the role's legitimate permissions
EVIDENCE: infra/aws/terraform/news-pipeline/cross-firm-bucket-write-deny.tf:8
VERDICT: NOT-A-READER -- a comment inside a deny policy, not a reader.

## READER: infra/aws/terraform/news-pipeline/iam.tf

READS: a GRANT: layer3-bd-securities-read (dynamodb read on the table) for the shared lambda-execution-role
EVIDENCE: infra/aws/terraform/news-pipeline/iam.tf:369
VERDICT: NOT-A-READER -- a policy for the semantic-news-layer3-curation reader (traced above), not a reader itself.

## READER: infra/aws/terraform/partners-api/iam.tf

READS: a GRANT: attaches the bd-securities-access managed policy to the partners role
EVIDENCE: infra/aws/terraform/partners-api/iam.tf:33
VERDICT: NOT-A-READER -- a policy attachment for the opal-partners-data reader (traced above), not a reader itself.

## READER: infra/aws/terraform/shared-infra/CHANGELOG.json

READS: a changelog entry listing the table and the access policy
EVIDENCE: infra/aws/terraform/shared-infra/CHANGELOG.json:523
VERDICT: NOT-A-READER -- a changelog, not a reader.

## READER: infra/aws/terraform/shared-infra/lambda-execution-role.tf

READS: a comment mapping layer3-bd-securities-read to the news pipeline
EVIDENCE: infra/aws/terraform/shared-infra/lambda-execution-role.tf:24
VERDICT: NOT-A-READER -- a comment, not a reader.

## READER: infra/aws/terraform/shared-infra/main.tf

READS: the table definition (aws_dynamodb_table bd_securities) and the bd-securities-access policy attached to bd-exporter-ec2-role and partners-lambda-role
EVIDENCE: infra/aws/terraform/shared-infra/main.tf:363
VERDICT: NOT-A-READER -- the table's own Terraform and a grant, not a reader.

## READER: infra/logic/registry/resources.json

READS: naming-registry entries for the table and the layer3-bd-securities-read policy
EVIDENCE: infra/logic/registry/resources.json:2261
VERDICT: NOT-A-READER -- a name registry, not a reader.

## READER: infra/system/ontology/worldmodel/10_census/instruments/ddb_configs_from_dr.json

READS: a census instrument entry listing the table
EVIDENCE: infra/system/ontology/worldmodel/10_census/instruments/ddb_configs_from_dr.json:5
VERDICT: NOT-A-READER -- a census instrument, not a reader.

## READER: infra/system/ontology/worldmodel/10_census/instruments/iam_policies_local.json

READS: a census instrument entry listing the policy
EVIDENCE: infra/system/ontology/worldmodel/10_census/instruments/iam_policies_local.json:79
VERDICT: NOT-A-READER -- a census instrument, not a reader.

## READER: infra/system/ontology/worldmodel/10_census/instruments/re_us-east-1.json

READS: a resource-explorer census entry for the policy and the table ARNs
EVIDENCE: infra/system/ontology/worldmodel/10_census/instruments/re_us-east-1.json:14978
VERDICT: NOT-A-READER -- a census instrument, not a reader.

## READER: infra/system/ontology/worldmodel/10_census/instruments/tagged_us-east-1.json

READS: a tagged-resources census entry for the table and the policy
EVIDENCE: infra/system/ontology/worldmodel/10_census/instruments/tagged_us-east-1.json:236
VERDICT: NOT-A-READER -- a census instrument, not a reader.

## READER: workflows/legacy_transform/blackdiamond-49financial/20260919T034609Z-c28c728/live-iam-census.json

READS: a live IAM census snapshot of 2026-09-19 listing which principals hold grants on the table
EVIDENCE: workflows/legacy_transform/blackdiamond-49financial/20260919T034609Z-c28c728/live-iam-census.json:2657
VERDICT: NOT-A-READER -- a dated census snapshot, not a reader.
