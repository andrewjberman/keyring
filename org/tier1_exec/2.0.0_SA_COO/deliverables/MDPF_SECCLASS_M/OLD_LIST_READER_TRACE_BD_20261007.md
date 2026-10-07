DENOMINATOR: 13 files of the Black Diamond tree census (git grep -l -E "bd-securities|BD_SECURITIES_TABLE" -- data/black_diamond/, minus test files; 66 naming lines and 32 table-call lines swept, all 13 files read); run-time names: 2 builder lines in 2 files plus 10 caller-supplied-name lines in 4 files, 6 importer lines; roles: 290 IAM roles + 9 users + 2 groups scanned (769 policy attachments and inline documents, 55 distinct managed documents), 10 principals can read the table (8 roles); assumers mapped over 232 Lambda functions, 33 EC2 instances (24 roles in instance profiles), 9 active ECS task-definition families, 5 CodeBuild projects (Glue UNREAD: glue:GetJobs is denied to this principal); etf-classifications 3,507 rows scanned for the CANONICAL-PRODUCER counts; old-list table activity read from CloudWatch for 2026-09-23..2026-10-07.

# OLD LIST READER TRACE, THE WIDENED CENSUS -- MDPF_SECCLASS SC-e-41 (FWD-5), 2026-10-07, 0.9.0_WK_MDPF_SECCLASS~31

Instrument: `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R11_CHECKS/old_list_reader_census_bd.py` (read-only; prints the census, the run-time names, the role grants, the canonical write census and the old list's own request counts). Round 8's trace is `OLD_LIST_READER_TRACE_20261007.md` (TO-SC-e38, 46 files outside the Black Diamond tree).
The old list is DynamoDB `bd-securities`, us-east-1, hash key `ticker`, 10,965 items, status ACTIVE (describe_table 2026-10-07). Every rule below is read from the reader's own code at the cited line at the round-9 base b55059ee33, never predicted.

Live-plane facts, read 2026-10-07 (read-only; no code downloaded, no function invoked), that the verdicts lean on:
- The table is read every day. CloudWatch request counts by day, 2026-09-23..2026-10-06 UTC: Scan pages 312, 168, 327, 192, 91, 415, 370, 381, 321, 264, 252, 207, 243, 382 (09-23 to 10-06; the weekend days 09-27 and 10-04 read 91 and 207 scan pages, so the readers are not weekday-only); GetItem is quiet (1 to 16 a day) except 1,151 on 09-25, 5,337 on 09-29, 307 on 10-01 and 7,034 on 10-06; PutItem 1,145 on 09-25, 52 on 09-26 and 36 on 10-03; UpdateItem 6 on 09-25; Query none. The GetItem bursts are not explained by any scheduled reader in the census (row MDPF_SECCLASS-W31-S3).
- The Black Diamond host role `bd-exporter-ec2-role` holds the grant (managed `bd-securities-access`, Scan and GetItem and write verbs; inline `advi-49f-chain-access`, Scan) and is on 14 EC2 instances, all STOPPED at read time; `bd-gold-layer-runner` (i-01003b035d2988dfb) last launched 2026-10-07T09:47Z, so the nightly Black Diamond gold chain (`gold_dispatch.sh` catalog lines 101-102: B_01b and E_18 with --upload) is live. The deployed bytes of the runner (firm bucket `opal-data-bd`) are UNREAD (row W25-S1: this principal is denied the firm buckets), so what the runner executes is read from the repo copy.
- etf-classifications write census by `updated_by` (3,507 rows, scanned 2026-10-07): `<none>` 1,926; `rivalfunds-backfill` 640 (626 at 2026-10-05T12Z, 6 at 2026-10-05T21Z, 8 at 2026-10-06T14Z, matching the 10:00 ET fire of the enabled schedule `mdpf-secclass-new-security-daily`, Lambda `mdpf-secclass-new-security-lambda`); `mdpf-secclass-scheduled` 348 (all `CUSIP:`-keyed, last 2026-09-30T16:44Z); `seed-etf-constituents` 179 and 59; `seed-script` 177; `mdpf-secclass-bd-mapped` 67; `mdpf-secclass-cusip-rows` 65; `mdpf-secclass-remap-b` 33; `mdpf-secclass-model` 13 (last 2026-10-01T11:05Z); `e18-scheduled` 0.
- Therefore the canonical producers for a security FIRST HELD BY A CLIENT after the old-list writers stop are: `e18-scheduled` 0 rows (and it cannot resolve one by construction, row W31-S1); the AI runner `classify-residual-model.py` (stamp `mdpf-secclass-model`, 13 rows, an operator-run CLI, not scheduled); the one recurring producer (`rivalfunds-backfill`) reaches only a US bare-ticker stock that newly enters an Opal or rival ETF's holdings, not a client holding as such (row W31-S2). Each real reader's CANONICAL-PRODUCER line below reads from this list.

Summary of verdicts (full sections follow). NEEDS-OLD-LIST: `resolve_tickers.py` (named by round 8) and the IRPT Holdings fallback (named by round 8, here through its run-time name). REPOINTABLE: the Black Diamond `E_18.detect_new_securities.py` (a live read of the old list on a host that holds the grant; NOT named by round 8). DEAD-READ: the two caller-supplied-name paths (`default_bd_securities_lookup` and the `classify-residual-model.py` CLI flag). NOT-A-READER: the five old-list writers and seeders (`backfill_name_aliases.py`, `classify_bd_securities.py`, `seed_bd_securities.py`, `seed_canonical_securities.py` and the nightly `B_01b`, whose scan is its own existence check), the five comment or docstring hits (`B_01.holdings_lots.py`, `build_canonical_prices_v2.py`, `gold_dispatch.sh`, `lib/s3_layout.py`, `build_bd_assets_dim.py`), `lib/etf_classifier.py` (reads the canonical table only), and the role grants (no function that assumes a role-only-reach role names the table).

## READER: data/black_diamond/scripts/classification/backfill_name_aliases.py

READS: a full scan of bd-securities (lines 57-70, called at 128) to learn which tickers exist, then `update_item ... ADD name_aliases` for each (line 163, `--upload` only); it WRITES the old list and reads it only to choose which rows to update. It has no caller anywhere in the repo (git grep of the file name outside docs finds only its own text) and no scheduler; it is a manual CLI.
EVIDENCE: data/black_diamond/scripts/classification/backfill_name_aliases.py:163
VERDICT: NOT-A-READER -- a writer: the scan only selects the rows its own update touches, and the update is the retired path (SC-e-35 governs the writers); it serves nothing. If the table were gone before the writer is stopped, a manual run would fail at line 128, nothing scheduled would.

## READER: data/black_diamond/scripts/classification/classify_bd_securities.py

READS: a full scan of bd-securities (lines 75-87, called at 135) used as the exclusion set of existing keys before it classifies net-new keys by OpenAI and `put_item`s them (line 228); a manual CLI with no caller (git grep outside docs: README listing only).
EVIDENCE: data/black_diamond/scripts/classification/classify_bd_securities.py:228
VERDICT: NOT-A-READER -- a writer: its scan is the idempotence check for its own put_item and it serves nothing; the nightly path uses B_01b, not this file.

## READER: data/black_diamond/scripts/classification/resolve_tickers.py

READS: a full scan of bd-securities (lines 152-166, called at 599) and the attributes asset_name_raw, name_aliases and ticker, held as a NAME-to-TICKER dictionary for resolution methods 2 (exact, lines 191-214), 3 (prefix, 217-243), 5 (individual-stock stem, 263-345) and 6 (mutual-fund stem, 347-384) that build gold/dimensions/ticker_resolution.parquet (lines 689-715); a manual CLI (no caller, no scheduler in the repo), whose OUTPUT the nightly Black Diamond B_01 reads to fill missing tickers (B_01.holdings_lots.py:2633) and E_18 reads to skip resolved names (E_18.detect_new_securities.py:133); the freshness config expects it weekly (gold_freshness_config.yaml:364-370, warn 192 h)
EVIDENCE: data/black_diamond/scripts/classification/resolve_tickers.py:152
VERDICT: NEEDS-OLD-LIST -- it reads asset_name_raw and name_aliases, which etf-classifications does not carry (round 8's attribute union: ticker, asset_class, sub_asset_class, name on 883 rows, no asset_name_raw, no name_aliases), so a repoint is a new name field, not a switch; named by round 8, confirmed here at the Black Diamond tree. Unmeasured: when it last ran (the parquet is in the firm bucket, denied).
MISSING-ROW: resolve_tickers.py:191-214, 217-243, 263-345, 347-384: a name with no old row is not resolved by methods 2, 3, 5 (db stem; the yfinance guess at 318-336 still runs) or 6, and is left out of the resolution table, which is built from the resolved rows only (line 689)
SERVED-NEW: a name first held after the writers stop is not resolved through the old list; ticker_resolution.parquet keeps no row for it (apart from method 1, a ticker already in holdings_lots, method 4, the etf_classification.py alias dict, and a method 5 yfinance guess), so B_01's COALESCE leaves that holding tickerless; no error, nothing dropped by this reader
CANONICAL-PRODUCER: NONE: no producer gives a first-held security an etf-classifications row that carries a name-to-ticker mapping (the table's 'name' attribute is on 883 of 3,507 rows, written by seeds and mdpf-secclass-* one-offs; e18-scheduled 0; the recurring rivalfunds-backfill rows are bare-ticker stocks of ETF holdings, 8 on 2026-10-06T14Z)

## READER: data/black_diamond/scripts/classification/seed_bd_securities.py

READS: a full scan of the CANONICAL table etf-classifications (lines 54-64) as its source; it WRITES the old list (`put_item`, line 97). It names bd-securities only as TARGET_TABLE (line 22). A one-time seed with no caller.
EVIDENCE: data/black_diamond/scripts/classification/seed_bd_securities.py:97
VERDICT: NOT-A-READER -- a writer and seeder: it reads the canonical table, never the old list.

## READER: data/black_diamond/scripts/classification/seed_canonical_securities.py

READS: nothing from the old list: `update_item` upserts into bd-securities (line 333) and, with --yang, into etf-classifications (line 358); its one get_item (line 273) reads the canonical table. No caller; a manual seeder.
EVIDENCE: data/black_diamond/scripts/classification/seed_canonical_securities.py:333
VERDICT: NOT-A-READER -- a writer: its update_item calls never read an old-list row.

## READER: data/black_diamond/scripts/gold/B_01.holdings_lots.py

READS: nothing: line 3011 is a docstring sentence in save_lots naming B_01b as a downstream consumer of the holdings_lots partitions; the file holds no DynamoDB call (the census counts 1 naming line, 0 table-call lines)
EVIDENCE: data/black_diamond/scripts/gold/B_01.holdings_lots.py:3011
VERDICT: NOT-A-READER -- a comment describing a downstream writer, not a read.

## READER: data/black_diamond/scripts/gold/B_01b.classify_new_securities.py

READS: a full scan of bd-securities for existing keys (lines 155-167, called at 256) before it classifies the net-new (ticker, asset_name) pairs by OpenAI and `put_item`s them (line 330); it WRITES the old list, nightly (gold_dispatch.sh catalog line 101 `B_01b|...|--upload`, chain CHAIN_CANONICAL line 162), and PutItem requests hit the table on 2026-09-25 (1,145), 09-26 (52) and 10-03 (36). The scan runs only when a new holdings_lots partition exists (return at lines 234-236 otherwise).
EVIDENCE: data/black_diamond/scripts/gold/B_01b.classify_new_securities.py:330
VERDICT: NOT-A-READER -- the old list's nightly WRITER; its scan is the writer's own existence check and it serves nothing. ORDERING HAZARD stated, not graded: B_01b is not in NONFATAL_IDS (gold_dispatch.sh:165, only E_18 is), the scan at line 256 has no handler, so a table removed before B_01b is taken off the chain fails the nightly Black Diamond gold chain at B_01b on the next day with a new partition (row W31-S4); the writer stop (SC-e-35) must land first.

## READER: data/black_diamond/scripts/gold/E_18.detect_new_securities.py

READS: three reads of the old list on every run: load_known_tickers (lines 118-130, called at 215) is a full scan of keys; _scan_db_asset_names (150-168, called at 218 when ticker_resolution.parquet exists) is a full scan of ticker and asset_name_raw used for the prefix match; default_bd_securities_lookup(BD_SECURITIES_TABLE) (line 291) is a GetItem per candidate handed to the canonical producer's plan_rows as its classification input. The writes were removed (docstring lines 12-18): it WRITES only etf-classifications rows, through etf_classification_scheduled.write, stamped 'e18-scheduled'. It is LIVE: in the nightly chain after B_01b (gold_dispatch.sh:162 and catalog line 102), a NON-FATAL step (NONFATAL_IDS, gold_dispatch.sh:165, 446-453) on the host that holds the grant.
EVIDENCE: data/black_diamond/scripts/gold/E_18.detect_new_securities.py:215
VERDICT: REPOINTABLE -- the key set at line 215 swaps for the canonical key set the same function already loads at line 288 (existing_tickers(classifier)), the prefix map at line 218 only skips candidates and has no canonical source (asset_name_raw absent) so its repoint is lossy and changes a statistic and a skip, and the old-list GetItem at line 291 can never return a row (see MISSING-ROW), so nothing resolvable is lost by dropping it. Removal of the table first would abort the script at line 215 with an unhandled ResourceNotFoundException (the chain continues, NON-FATAL) and write no canonical row. NOT graded by round 8 (it named this script only as a caller of the producer, and it was outside that census); this is a switch cell for the issuer.
MISSING-ROW: E_18.detect_new_securities.py:247 (a pair whose key is already an old-list key is skipped) and 267-274 (a real-ticker pair not in `known` is a canonical candidate), then 289-291 hands each candidate to plan_rows with the old-list GetItem as the only wired input; classify_asset_class returns (None, None, None) when the old list has no usable row (etf_classification_scheduled.py:371-388, GICS and Schwab lookups default to None) and the ticker is listed unresolved, no row planned. A candidate is by construction a ticker with NO old row, so the lookup never hits.
SERVED-NEW: nothing is served from this script (its output is a stdout summary and, only on a resolved candidate, a canonical row); a security first held after the writers stop is a candidate with no old row, is listed 'unresolved' (summary line 'Scheduled-classification unresolved') and gets NO canonical row; identical to today, since the same construction already yields 0 rows
CANONICAL-PRODUCER: ITSELF, measured: updated_by 'e18-scheduled' 0 rows in the 3,507-row table scanned 2026-10-07; the candidate set excludes every ticker the lookup can answer (line 247), so it cannot resolve one; the 348 'mdpf-secclass-scheduled' rows are CUSIP-keyed and written once (2026-09-30); the AI runner classify-residual-model.py (13 'mdpf-secclass-model' rows, last 2026-10-01) is operator-run, not scheduled

## READER: data/black_diamond/scripts/gold/build_canonical_prices_v2.py

READS: nothing: line 398 is a docstring phrase ("bd-securities validated") describing a Yahoo ticker in resolve_prices_for_asset; the file holds no DynamoDB call (census: 1 naming line, 0 table-call lines)
EVIDENCE: data/black_diamond/scripts/gold/build_canonical_prices_v2.py:398
VERDICT: NOT-A-READER -- a comment, not a read.

## READER: data/black_diamond/scripts/gold/gold_dispatch.sh

READS: nothing: line 554 is a stale comment saying B_01b classifies into DynamoDB bd-securities "that B_02 reads"; B_02 and every other Black Diamond gold script outside the classification, B_01b and E_18 files hold no DynamoDB call (git grep -i dynamodb over data/black_diamond finds only the library, comments and manifests). The dispatcher is how B_01b and E_18 reach the host (catalog lines 101-102).
EVIDENCE: data/black_diamond/scripts/gold/gold_dispatch.sh:554
VERDICT: NOT-A-READER -- a comment; the readers it launches are B_01b (a writer) and E_18, graded in their own sections.

## READER: data/black_diamond/scripts/gold/lib/etf_classifier.py

READS: etf-classifications through the shared client; its docstring (line 89) states it "never opens bd-securities and never writes any table"; line 113 is the same docstring naming the real client constructor
EVIDENCE: data/black_diamond/scripts/gold/lib/etf_classifier.py:89
VERDICT: NOT-A-READER -- this library is the canonical-only classifier the Black Diamond C_06 and D_03 use (their comments, C_06.client_mix_timeseries.py:187 and D_03.composition_artifacts.py:113); it holds no old-list read.

## READER: data/black_diamond/scripts/gold/lib/s3_layout.py

READS: nothing: line 303 is a comment beside the CLASSIFY_WATERMARK S3 key constant naming what B_01b's watermark is for
EVIDENCE: data/black_diamond/scripts/gold/lib/s3_layout.py:303
VERDICT: NOT-A-READER -- a comment beside an S3 key constant, not a read.

## READER: data/black_diamond/scripts/silver/build_bd_assets_dim.py

READS: nothing: line 166 is a docstring saying the old print naming a bd-securities scan "is stale (SC-t-1 retired that read path)"; the file reads the canonical client only (ETFClassifier.instance(), the same docstring) and holds no DynamoDB call
EVIDENCE: data/black_diamond/scripts/silver/build_bd_assets_dim.py:166
VERDICT: NOT-A-READER -- a docstring recording that the read was retired.

## READER: runtime-name builder, the IRPT Holdings fallback -- data/assets/scripts/gold/investor_reporting/bd_securities_fallback.py (table name '%s-securities' from the naming registry)

READS: LEGACY_TABLE is assembled at import time (bd_securities_fallback.py:35-46) as '%s-securities' % the `serving-route` alias of lookup('49financial'), which the registry resolves to 'bd' (measured by the instrument: lookup('49financial') serving-route alias = 'bd', so the table is bd-securities); ETFClassifier.instance() (lines 84-117) does a full paginated scan of it (ticker, asset_class, sub_asset_class, name_aliases, asset_name_raw). The only importer of the module is holdings_snapshot.py (lines 898 and 910, canonical_classifier and the normalize_name helper); the Holdings builders holdings_49f.py, holdings_inf.py and holdings_membership.py import holdings_snapshot, and the three roles irpt-49f-holdings-role, irpt-cot-holdings-role and irpt-inf-holdings-role (each: dynamodb:Scan on the table) are assumed from mdpf-daily-runner-ec2-role (instance i-02448edb624a7a7cf, last launch 2026-10-06T13:30Z, stopped at read time). The other run-time spelling, holdings_snapshot.py:851, builds the served LABEL '%s-securities-fallback', not a table name.
EVIDENCE: data/assets/scripts/gold/investor_reporting/bd_securities_fallback.py:43
VERDICT: NEEDS-OLD-LIST -- Holdings reads etf-classifications first and falls to this module for a ticker the canonical table lacks (holdings_snapshot.py:954-967), and canonical_classifier() refuses to run (ValueError, line 913) if the fallback loads no rows, so a table removed before this reader is repointed stops Holdings rather than degrading it; the same finding as round 8's, reached here from the run-time name (the order's FWD-6 declared fallback; removal is FWD-13's).
MISSING-ROW: bd_securities_fallback.py:119-167 classify(): a ticker with no old row and no alias row -> name patterns (alternatives; cash and fixed-income both -> fixed_income) -> a 1-5 letter ticker (optional .X) is 'equity' -> '' (line 167); holdings_snapshot.py:954-971 maps '' to 'unclassified'
SERVED-NEW: the Holdings node for a security first held after the writers stop reads 'equity' (basis TICKER_SHAPE) for a 1-5 letter ticker, 'fixed_income' or 'alternatives' (basis NAME_PATTERN) by name, else 'unclassified' (basis NONE); never an error and never dropped; the CASH-named cash line is 'cash' before either table
CANONICAL-PRODUCER: NONE reaching a client-first-held security: e18-scheduled 0 rows (2026-10-07 scan); the 348 mdpf-secclass-scheduled rows are CUSIP-keyed and written once; the recurring rivalfunds-backfill rows (640 total, 8 on 2026-10-06T14Z) are stocks entering ETF holdings, so a held stock outside every ETF gets none

## READER: runtime-name, caller-supplied table name -- infra/aws/lambda/v2_portal/_shared/etf_classification_scheduled.py default_bd_securities_lookup(table_name) and its callers

READS: default_bd_securities_lookup (lines 526-541) takes the old list's name from its CALLER and returns a per-ticker GetItem; callers: the Black Diamond E_18 (E_18.detect_new_securities.py:291, constant BD_SECURITIES_TABLE, graded above), the Cottonwood E_18 (data/cot/scripts/gold/E_18.detect_new_securities.py:322, constant; round 8 graded it DEAD-READ because the host role cot-exporter-ec2-role and cot-gold-layer-ec2-role hold no grant), and the CLI of this module (`--legacy-fork-table`, lines 568 and 582-583, refuses to run without --dry-run, lines 572-573). No caller in the repo (git grep over py, sh, json, yaml, tf) passes the flag; the CLI default is None, which wires no old-list read. The name is therefore spelled at run time only by an operator.
EVIDENCE: infra/aws/lambda/v2_portal/_shared/etf_classification_scheduled.py:526
VERDICT: DEAD-READ -- the one scheduled caller (Black Diamond E_18) asks only for tickers the table has no row for (E_18:247), so the GetItem cannot return a row; the Cottonwood caller cannot read the table; the CLI is a manual dry-run whose flag nobody passes. The helper already degrades quietly if the table is gone: ClientError and BotoCoreError are caught (lines 537-539), logged at ERROR and returned as None.
MISSING-ROW: etf_classification_scheduled.py:371-388: lookup None (no row, or a read error) -> GICS None -> Schwab None -> (None, None, None) and the ticker is listed unresolved
SERVED-NEW: nothing is served; a security first held after the writers stop is listed unresolved by the producer, no etf-classifications row is planned; with the table removed the same result plus an ERROR log line per ticker ('bd-securities read error'), no exception
CANONICAL-PRODUCER: ITSELF through E_18: 'e18-scheduled' 0 live rows (2026-10-07 scan of 3,507 rows); no other scheduled producer takes the lookup

## READER: runtime-name, caller-supplied table name -- infra/aws/lambda/v2_portal/yang_pipeline/classify-residual-model.py (the AI classifier's `--legacy-fork-table` flag)

READS: the optional flag `--legacy-fork-table` (lines 253-255, default None, "never a default baked in here") is passed to default_bd_securities_lookup (lines 265-266) and on to plan_rows (line 201, `bd_securities_lookup=bd_lookup`); without the flag bd_lookup is None and no old-list read happens. It is an operator-run CLI: its docstring (line 38) says no scheduling, role or function is created, and no caller in the repo passes the flag.
EVIDENCE: infra/aws/lambda/v2_portal/yang_pipeline/classify-residual-model.py:265
VERDICT: DEAD-READ -- the old list is read only when an operator passes the flag, and nothing in the repo does; the runner's real path (the model, FWD-11) does not read the old list.
MISSING-ROW: classify-residual-model.py:201 then etf_classification_scheduled.py:371-388: with no flag, no old-list input; a pair the direct-match plan leaves unresolved goes to the model (lines 105-160)
SERVED-NEW: when an operator runs it with --model and --write, a security first held after the writers stop gets a canonical row from the model (asset_class within the six classes, sub_asset_class from the table's own values, classified_by 'model', low_confidence flagged, never held back), written by a conditional put so a present key is never replaced; otherwise it is left unresolved; nothing is read from the old list either way
CANONICAL-PRODUCER: ITSELF, measured: updated_by 'mdpf-secclass-model' 13 rows, last_updated 2026-10-01T11:05Z, operator-run (not scheduled); the first-held-security route a scheduled run would give is this runner, which no schedule fires

## READER: role grants -- every IAM principal that can read bd-securities without the table being named in the code of the function that assumes it (live IAM read 2026-10-07, read-only)

READS: 290 roles, 9 users and 2 groups were read (list-attached-*-policies, list-*-policies, get-policy-version, get-role-policy; each Allow statement graded against the table ARN arn:aws:dynamodb:us-east-1:313476888478:table/bd-securities with wildcard matching). Ten principals can read it:
- bd-exporter-ec2-role (managed bd-securities-access; inline advi-49f-chain-access): 14 EC2 instances, all stopped at read time (bd-gold-layer-runner last launch 2026-10-07T09:47Z, bd-assets, bd-allocations, bd-transactions, bd-fees, bd-gold-qa-runner, historical-prices-fetcher x8). Code naming the table: the Black Diamond tree above and a07_dim_asset_classification.py (round 8).
- irpt-49f-holdings-role, irpt-cot-holdings-role, irpt-inf-holdings-role (inline, dynamodb:Scan): assumed from mdpf-daily-runner-ec2-role; code: bd_securities_fallback.py (section above).
- partners-lambda-role (managed bd-securities-access): Lambda opal-partners-data; code: its etf_classifier.py (round 8: DEAD-READ).
- lambda-execution-role (inline layer3-bd-securities-read, dynamodb:Scan): 13 functions assume it (semantic-news-layer3-curation, opal-pm-optimization-autosave-put, semantic-trending-topics-portal-publisher, opal-portfolio-autosave-put, opal-portfolio-funds-list, opal-pm-upload-urls, news-semantic-clustering, opal-portfolio-autosave-get, opal-pm-optimization-loader, opal-portfolio-versions-list, opal-pm-snapshot-handler, opal-portfolio-pickle-parser, opal-portfolio-version-get); only semantic-news-layer3-curation names the table in code (round 8: no trigger, DEAD-READ); the other 12 name it nowhere in the repo, and none carries an environment variable naming it (all 13 configurations read).
- opal-news-lambda-role (AWS-managed AmazonDynamoDBFullAccess, dynamodb:* on *): one function, opal-news-layer3-curation (python3.12, modified 2026-09-16, environment keys SOURCE_TABLE, TARGET_TABLE and others, none naming the table); its repo code (news_layer3_curation/lambda_function.py:55-56) reads opal-news-articles and writes opal-news-trending-daily and names no securities table.
- opal-drift-producer-codebuild-role (AWS-managed ReadOnlyAccess grants dynamodb Scan, Get*, BatchGet*, Query): CANNOT read it: the inline DriftProducerWritesAndDataDeny explicitly Denies GetItem, BatchGetItem, Query and Scan on *; assumed by the one CodeBuild project opal-drift-producer.
- groups AdministratorAccessOpalCapital (members Andrew_Berman_Console, Andrew_Berman, Opal_Terminal; AdministratorAccess) and cloudops-dell-agents-group (members cloudops-dell1-agent-user, cloudops-dell2-agent-user; managed cloudops-dell-agent-deploy-policy, GetItem, Query, Scan, BatchGetItem on *): humans and agent principals, not a function path.
UNMEASURED: the deployed code of the 13 + 1 Lambda functions was not downloaded (bound: no download), so the finding "none of them names the table" rests on the repo copy, the 14 live configurations (Runtime, LastModified, environment) and the table's own request counts; Glue is UNREAD (glue:GetJobs denied to this principal); only us-east-1 was scanned for assumers; the old list's GetItem bursts (row W31-S3) are unattributed.
EVIDENCE: infra/aws/nfra_terraform_p1/desired_index.json:8550
VERDICT: NOT-A-READER -- no role reaches the table without a reader that is already graded above: every role whose assuming function or instance names the table in code appears in a section of this trace or round 8's, and the roles that reach it with no code naming it (opal-news-lambda-role, 12 functions of lambda-execution-role, the humans and agents) have no repo code that reads it; opal-drift-producer-codebuild-role is denied. The grants are not read paths and need no switch; they are removed with the table (IAM clean-up is the act's, not this census's).
