# AMGT_RESAPP DATA SHAPE INVENTORY -- measured 2026-09-18

Author: subagent of `4.0.0_SA_CRO~Z`. READ-ONLY pass: no writes, no commits, no messages.
Every count below is from a live paginated API call made this session, denominator printed.
Repo vintage: working tree at branch SITEZ, HEAD `7fd48dac8b`.

## 0. HOW THIS WAS MEASURED (instruments, so a reader can disagree with the right one)

| Claim class | Instrument | Denominator |
|---|---|---|
| S3 objects + bytes | `boto3 list_objects_v2` paginated, no `--no-paginate` | 1333 objects / 2 pages / `IsTruncated=False` on the final page |
| S3 version plane | `list_object_versions` paginated | 1965 versions, 632 non-latest, 0 delete markers |
| DynamoDB counts | live `scan` (NOT `describe-table`; `dynamodb.tf` itself warns ItemCount is a ~6h cache) | 284 items, 1 page |
| Triggers | `events:list_rules` AND `scheduler:list_schedules` (two different APIs) | 144 rules + 23 schedules |
| Lambdas | `lambda:list_functions` paginated | 217 functions |
| Code writers/readers | native `Grep`/`Glob` over the worktree (raw Bash grep is rail-denied) | `lib/research` 134 `.py` files |

**Instrument trap caught here, MEASURED:** `events:list_rules` returned **0 of 144** rules matching
any RESAPP token. That reads as "RESAPP has no schedule" and is WRONG -- the one RESAPP schedule is
an `aws_scheduler_schedule` (EventBridge **Scheduler**), which `list_rules` cannot see at all. The
correct read is `scheduler:list_schedules`, where `amgt-resapp-chatter-axis-daily` is ENABLED.
A single-instrument answer here would have been a confident false negative.

## 1. THE STREAM TABLE

Bucket totals, MEASURED: `s3://opal-data-harvest` holds **1333 objects / 31,901,561 bytes** across
**16 top-level prefixes**. Bucket created 2026-09-11; versioning ENABLED; SSE-S3; all four public
blocks on; no lifecycle, no bucket policy, no S3 notification (`infra/aws/terraform/harvest/s3.tf`).

Tier codes: BR=bronze, SI=silver, GO=gold, PL=platinum, ST=state. `M`=MEASURED from the object's
own shape, `I`=INFERRED. Byte counts are the sum of current-version sizes only.

| # | Stream | Address today | Tier | Objs | Bytes | Writer (`file:line`) | Write path | Readers | Trigger | Vintage | Source |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Crosswalk | `s3://opal-data-harvest/crosswalk/v1/<date>.json` | SI (M) | 1 | 188,380 | `lib/research/identity/crosswalk.py:688` | `write_pool` | `crosswalk.py:518-529`; `lib/research/scores/run_scores.py:84-91`; `integrations/bloomberg/research/management_posture_batch.py:47` | manual | date in key; accumulate | derived from repo coverage corpus + ETF holdings |
| 2 | Union universe | `universe/v1/<date>.json` | SI (M) | 2 | 383,492 | `lib/research/identity/build_universe.py:862` | `write_pool` | `peers/engine.py:1168-1178`; `posture/membership.py:91-114`; `price/generation.py:134`; `metrics/chatter_axis.py:241`; `management/enrich.py:50`; `filings/batch.py:78`; `api/scoped_amgt.py:2756` | manual | date in key; accumulate | `s3://opal-data-etfs` holdings + coverage |
| 3 | Identity residue crossref | `identity/v1/<date>-coverage-residue-crossref.json` | ST (I) | 1 | 47,229 | `lib/research/identity/coverage_residue.py` | `write_pool` | none found in `lib/research` (134 files) | one-off (TO rk-21) | date in key | internal |
| 4 | Filing source (resolved) | `filings/v1/<security_key>/<accession>.source.json` | **AMBIGUOUS BR/SI (M)** | 13 | (in 4,597,976) | `lib/research/filings/fetch.py:462`; batch `filings/batch.py:239` | `write_pool` | `filings/analyze.py:1012`; `management/roster.py:492-498`; `api/scoped_amgt.py:1913` | manual | accession in key; no date | EDGAR |
| 5 | Filing source (unresolved marker) | `filings/v1/<security_key>/UNRESOLVED-SOURCE.source.json` | ST (M) | 176 | (in 4,597,976) | `lib/research/filings/batch.py:138` | `write_pool` | same as #4 | manual | **none in key -- overwritten** | EDGAR (negative result) |
| 6 | Filing analysis | `filings/v1/<security_key>/<accession>.analysis.json` | SI (M) | 13 | (in 4,597,976) | `lib/research/filings/analyze.py:1038,1143` | `write_pool` | `api/scoped_amgt.py:1913`; `posture/packs.py` | manual | accession in key | Claude over #4 |
| 7 | Drafted sections | `drafting/v1/<security_key>.json` | GO (M) | 12 | 1,127,014 | `lib/research/filings/analyze.py:1215`; `filings/batch.py:150` | `write_pool` | `api/scoped_amgt.py:1438` (`read_drafted_sections`); `posture/packs.py:107` | manual | **none in key -- overwritten** | Claude over #6 |
| 8 | Management roster | `management/v1/<security_key>/<date>.json` | SI (M) | 12 | 41,298 | `lib/research/management/enrich.py:621` | `write_pool` | `api/scoped_amgt.py:2305` (`read_management`); `management/enrich.py:592` | manual | date in key; accumulate | EDGAR Item 6 + Lusha + Bright Data SERP |
| 9 | Management pool stat | `management/v1/_pool/<date>.json` | GO (M) | 2 | (in 41,298) | `lib/research/management/enrich.py:630` | `write_pool` | `management/enrich.py:576` | manual | date in key | aggregate of #8 |
| 10 | Posture verdict | `posture/v1/<security_key>/<date>.json` | GO (M) | 33 | 376,437 | `lib/research/posture/judge.py:290` | **own `write_pool_object`** | `api/scoped_amgt.py:2437` (`read_posture`) | manual (`management_posture_batch.py`) | date in key but **31 of 33 written LATER than that date -- overwrite in place** | derived from #2/#8/#11/#12 |
| 11 | Peer sets | `peers/v1/<security_key>/<date or ISO stamp>.json` | GO (M) | 797 | 19,414,414 | `lib/research/peers/engine.py:1143` | **own `write_pool_object`** | `api/scoped_amgt.py:1244` (`read_peer_set`); `scores/run_scores.py:71`; `posture/comparable.py:39` | manual | **two grammars** (`<date>.json` 220, `<ISO stamp>.json` 567); accumulate | scanner universe (`opal-data-portal-v2`) |
| 12 | Scores (canonical) | `scores/v1/<security_key>/<date>.json` | GO (M) | 33 | (in 220,820) | `lib/research/scores/run_scores.py:231` | `write_pool` | `api/scoped_amgt.py:2374` (`read_scores`) | manual | date in key | derived from #11/#13 |
| 13 | Scores (superseded twin) | `scores/v1/<security_key>.json` | GO (M) | 31 | (in 220,820) | prior generation, writer not in tree | **direct put (no metadata)** | none -- read is pinned to #12 | none | none in key | same |
| 14 | Model block | `derived/model_block/<security_key>/<stamp>/model_block.json` | SI (M) | 47 | 4,304,966 | `integrations/bloomberg/research/model_block_pull.py:198` (`derived_key` :453) | **direct `put_object`** | `api/scoped_amgt.py:924` (`read_model_block`); `peers/universe.py:256`; `scores/run_scores.py:70` | manual, on the Bloomberg terminal box | stamp dir; accumulate | Bloomberg DAPI, derived from #16 |
| 15 | Model block FYE | `derived/model_block_fye/<security_key>/<stamp>/model_block_fye.json` | SI (M) | 3 | 20,175 | `integrations/bloomberg/research/derive_fye_fixed.py` / `fye_join.py` | direct `put_object` | none found | manual, one-off | stamp dir | derived from #14/#16 |
| 16 | Bloomberg raw | `raw/bloomberg/<security_key>/<stamp>/{refdata,histdata,histdata_daily_px}.json` | **BR (M)** | 79 | 431,376 | `model_block_pull.py:198` (keys :242-243) | direct `put_object` | `model_block_pull.py:375-376`; `api/scoped_amgt.py:2831` (names only) | manual, Bloomberg terminal box | stamp dir; accumulate | Bloomberg DAPI, **response as the client returns it** |
| 17 | Seeking Alpha raw | `raw/seekingalpha/<security_key>/<stamp>/{symbol,report,analysis,news,article_<id>}.json` | **BR (M)** | 18 | 209,361 | `integrations/seekingalpha/rest_fetch.py` (`config.json` `store_bucket`) | direct put | `api/scoped_amgt.py:2831` (names only) | manual | stamp dir; accumulate | Seeking Alpha REST, raw JSON:API envelope |
| 18 | Publication bodies | `publications/v1/<publisher>/<sha256>.json` | **AMBIGUOUS BR/SI (M)** | 7 | 66,021 | `lib/opal_data_harvest/uploads.py:76` (key `catalog.py:69`) | direct `put_object` | `lib/research/coverage/pool_reader.py:74`; `metrics/chatter_axis.py` | local Windows Scheduled Task, **on-demand by default** | content hash; immutable | SA / FT / WSJ / Bloomberg / Barron's via browser session |
| 19 | Publication links | `publication-links/v1/<ROOT>/<publisher>/<sha256>.json` | SI (M) | 7 | 1,839 | `lib/opal_data_harvest/uploads.py:76` (key `catalog.py:74`) | direct `put_object` | `lib/research/coverage/pool_reader.py:73` | same as #18 | content hash; immutable | same as #18 |
| 20 | Pack input ledger | `packs/<security_key>/input_ledger.json` | ST (M) | 36 | (in 12,879) | `lib/research/ledger/ledger.py:87` (key :70) | direct `put_object` | `api/scoped_amgt.py:2894` (`read_input_ledger`) | manual | **none -- append by read-modify-write** | internal |
| 21 | Pack status | `packs/<security_key>/status.json` | ST (M) | 1 | (in 12,879) | `integrations/bloomberg/research/pull_consumer.py:57` | direct put | `api/scoped_amgt.py:2837` | SQS consumer (`opal-research-pull-enqueue`) | **none -- overwritten in place by design** | internal |
| 22 | Social measurement | `social/v1/_measurement/<date>.json` | GO (M) | 1 | 12,088 | `lib/research/social/collect.py:492` (prefix :468) | own `write_pool_object` | none in the served API (prefix deliberately ungranted) | manual; collection RESERVED and OFF | date in key | Bright Data SERP |
| 23 | Local-worker release | `lib/local-publications/<ver>/<hash>/{*.zip,manifest.json}` | ST (M) | 6 | 445,796 | `lib/opal_data_harvest/build_release.py:65` | direct `put_object` | the local worker's installer | manual | content hash | **repo source code, not data** |
| 24 | Security metrics | DynamoDB `opal-harvest-security-metrics` | GO (M) | **284 items** (live scan) | 118,618 | `lib/research/metrics/chatter_axis.py:750-766`; `lib/research/price/generation.py:458-476`; `lib/research/watchlist/store.py:83` | `put_item` x3 modules | `api/scoped_amgt.py:382-782` (`read_rankings`, `read_point`, ...) | **`amgt-resapp-chatter-axis-daily`, cron(0 10 * * ? *) UTC, ENABLED** (chatter only) | `axis_date` sort key | derived from #2 + #18 + price |
| 25 | Article store | DynamoDB `opal-harvest-articles` | -- | **0 items** (live scan) | 0 | none | -- | none | none | -- | **declared, never written** |

### Read-only upstream (AMGT_RESAPP READS, NEVER WRITES -- MEASURED)

| Stream | Address | Objs | Bytes | Last write | Reader (`file:line`) |
|---|---|---|---|---|---|
| ETF gold holdings | `s3://opal-data-etfs/gold/holding/date=<date>/holding.parquet` | 18 | 792,677 | 2026-09-18 | `lib/research/identity/build_universe.py:444,572-576` |
| ETF snapshots | `s3://opal-data-etfs/snapshots/snapshot_<date>.json` | 99 | 285,822 | 2026-09-18 | `build_universe.py:445,565` |
| ETF Bloomberg plane | `s3://opal-data-etfs/bbg/<date>/*.{csv,parquet}` | 311 | 3,247,617 | 2026-09-18 | `lib/research/identity/positioning_chain.py:65,211-232` |
| Security scanner | `s3://opal-data-portal-v2/json/security_scanner/latest/...` | 19 | 171,914,443 | **2026-08-07 (42 days stale)** | `lib/research/peers/universe.py:61-63,175,360` |
| ETF classifications | DynamoDB `etf-classifications` (HASH `ticker`) | 285 (cached) | 64,314 | -- | `positioning_chain.py:68` |
| Trade security identifiers | DynamoDB `trade-security-identifiers` (HASH `ticker`) | 92 (cached) | 10,726 | -- | `positioning_chain.py:69` |

`build_universe.py:409` states the contract in code: *"C-ETF-PLANE-READ: AMGT_RESAPP READS
s3://opal-data-etfs and NEVER writes it."*

### Absence claim, with the full set searched

**AMGT_RESAPP writes NOTHING to `s3://opal-data-assets`.** MEASURED: the literal string
`opal-data-assets` occurs **0 times** across `lib/research` (134 `.py` files) and **exactly once**
across `integrations/` -- at `integrations/bloomberg/READ_HERE.md:175`, a documentation table
describing the *ETF* pipeline's bronze landings, not RESAPP, and not code. So Andrew's
"opal-data-assets should exclusively be for client assets" costs AMGT_RESAPP zero migration on the
write side; the whole estate is already in `opal-data-harvest`.

## 2. KEY SKELETONS -- one real object per stream

Keys only, two levels, with types and array lengths. No values, no credentials.

### 1. crosswalk -- `crosswalk/v1/2026-09-15.json` (188,380 B, meta: document-sha256, schema-version)
```
schema_version: int | as_of: str(10) | coverage_source: str(82)
coverage_vintage: dict[5] {corpus_root_mtime, read_started_at, read_finished_at,
                           denominator_folders:int, ticker_status_partition:{MEASURED,UNRESOLVED}}
key_conventions: list[6] of dict   [0] {convention, form, measured_on}
denominators: dict[6] {input_names, records, MEASURED, UNRESOLVED, with_association_keys,
                       association_conventions: list[6] of str}
records: list[89] of dict  [0] {association_keys, bloomberg, display_ticker, exchange, model_key,
                                provenance, raw_identifier, resolution, security_key, share_class,
                                source_row}
```

### 2. universe -- `universe/v1/2026-09-16.json` (197,564 B)
```
as_of: str(10) | snapshot_date: str(10) | schema_version: int | coverage_source: str(82)
holdings_source: dict[4] {DIVZ, IDVZ, PFDE, PFOE}   -- four ETF books
names: list[250] of dict  [0] {books, cik, filing_identity, name, resolution, resolution_reason,
                               security_key, source, ticker, weight_by_book}
denominators: dict[7] {coverage, holdings_distinct, union, both, resolved, unresolved, with_cik}
```

### 4. filings source -- `filings/v1/BA_US_Equity/000162828026004357.source.json` (149,333 B)
```
security_key: str | status: str | filing_identity: dict[3] {source, cik:int, form_expected}
entity_name | accession | accession_raw | form | filing_date | url | primary_document
retrieved_at | parser_version | document_bytes: int | document_sha256: str(64)
document_text_chars: int
excerpt: dict[8] {items: list[2] of str, item_keys: list[2] of str,
                  text: str(len=137314),          <-- RAW EDGAR TEXT, the bronze payload
                  chars: int, excerpt_sha256: str(64), truncated_items: list[1],
                  item_chars: {risk,mdna}, item_full_chars: {risk,mdna}}
officer_section: dict[6] {item, text: str(9409), chars, sha256, extracted: bool, extraction_owner}
```

### 5. filings unresolved marker -- `filings/v1/2317_TT_Equity/UNRESOLVED-SOURCE.source.json` (422 B)
```
security_key | status: "UNRESOLVED-SOURCE" | reason: str(70)
filing_identity: dict[1] {source} | retrieved_at | parser_version
accession: None | form: None | url: None | document_sha256: None | excerpt: None
officer_section: None
```

### 6. filings analysis -- `filings/v1/BA_US_Equity/000162828026004357.analysis.json` (279,875 B)
```
security_key | accession | form | filing_date
source: dict[8] {url, document_sha256, excerpt_sha256, retrieved_at, parser_version,
                 excerpt_items: list[2], excerpt_chars, pool_key}
model | analyzer_version | prompt_version
passage_map: list[282] of dict  [0] {ascii_replacements, chars, end, id, location, start, text}
items: dict[6] {guidance:list[15], segments:list[11], risks:list[24], commentary:list[18],
                big_bets:list[11], big_challenges:list[13]}
held_uncited: list[0] | thesis_driver: dict[8] | thesis_driver_record: dict[1]
denominators: dict[8] {passages, items_total, items_cited, items_held, cited_pct,
                       citations, citations_resolved, items_source}
passes: dict[2] {pass_1: dict[9] {model,input_tokens,output_tokens,stop_reason,seconds,usd,
                                  citations_enabled,answer,cached},
                 pass_2: dict[8]}
usage: dict[4] {input_tokens, output_tokens, seconds, usd}
citations: list[103] of dict  [0] {cited_text, passage_ids, resolved, shape, span, tag}
ascii_normalisation: dict[4] | pass_1_text: str(14273) | generated: bool
```

### 7. drafting -- `drafting/v1/BA_US_Equity.json` (106,588 B)
```
security_key | accession | form | filing_date | source: dict[8] | model | analyzer_version
generated: bool
sections: list[5] of dict         [0] {section, sentences}
evidence_records: list[86] of dict [0] {id, passage, source}
dropped: int | dropped_reasons: dict[1] {risks: list[2] of str} | thesis_driver: dict[8]
denominators: dict[6] {sentences, with_evidence, verbatim_pass, quoted, evidence_records, dropped}
```

### 8. management -- `management/v1/ASML_NA_Equity/2026-09-18.json` (1,779 B)
```
as_of | roster_status | roster_reason | source_accession | source_key | source_item
parse_strategy: None | parser_version | text_normalization
officers: list[0] | avg_tenure_years: None | generated: bool | generated_at | security_key
lusha_enrichment: dict[9] {status, domain, credits_used:int, results_returned, results_total,
                           matched, contact_keys_removed:int, reason, absence_reason_class}
ceo_public_profile: dict[9] {url, title, snippet, status, basis, ceo_name, query, ir_domain,
                             absence_class}
absence_reason_class | absence_reason_evidence
```

### 9. management pool -- `management/v1/_pool/2026-09-15.json` (180 B)
```
as_of | pool_avg_tenure_years: float
pool_denominator: dict[3] {names_in_union, names_with_roster, officers_with_role_start}
```

### 10. posture -- `posture/v1/2317_TT_Equity/2026-09-16.json` (4,548 B)
```
schema_version | security_key | as_of | verdict | comparable: None | comparable_name: None
marked | notice | reason | basis: list[0] | dropped_claims: list[0]
cites_validated: int | cites_total: int | generation: None
membership: dict[14] {security_key, held: bool, books: list[0], weight_by_book: dict[0],
                      snapshot_date, as_of, in_universe: bool, held_basis, identity: dict[5],
                      universe_source, universe_row_source, candidate_holding_rows: list[0],
                      holdings_source: dict[4], denominators: dict[5]}
comparable_membership: None
comparable_selection: dict[12] {comparable, comparable_held, rung_reached, log_cap_distance,
                               basis, subject_side, comparable_name, reason, peer_set_source,
                               candidates: list[0], denominators: dict[8], rerun: dict[12]}
fit: dict[0] | packs: dict[0] | sources: dict[0] | absence_reason_class
```

### 11a. peers, dated grammar -- `peers/v1/2317_TT_Equity/2026-09-15.json` (7,340 B)
```
as_of: str(10) | basis | csc_columns: dict[11] | denominators: dict[1] {database}
identity: dict[4] {matched_as, raw_identifier, resolution, security_key}
member_count: int | members: list[0] | reason | rungs: list[4] of dict [0] {field,name,rung,test}
sa_candidates: dict[9] | schema_version | security_key | subject: None | test
union_universe_source | universe_vintage | vintage
```

### 11b. peers, stamped grammar -- `peers/v1/2317_TT_Equity/2026-09-17T0240Z.json` (47,059 B)
```
as_of: str(16)  <-- note: 16 chars, not 10; the two grammars differ INSIDE the document too
basis | country_map: dict[6] | csc_columns: dict[14] | denominators: dict[14]
fit_denominators: dict[9] | horizon_census: dict[5] | identity: dict[4]
member_count: int
members: list[12] of dict  [0] {cap_currency, cap_ratio_to_subject, cap_source, cap_vintage,
                                country, factor_horizons, factors, factors_basis,
                                factors_denominator, fx_basis, horizon, horizon_label,
                                horizons_labelled, identity, industry_group, log_cap_distance,
                                market_cap_musd, name, rung_name, rung_reached, sector,
                                size_band_basis, ticker, universe_weights}
reason | rungs: list[4] | sa_candidates: dict[9] | schema_version | sector_map: dict[8]
security_key | subject: dict[23] | test | union_universe_source | universe_vintage | vintage
```
**The dated object carries `members: list[0]` and `subject: None`; the stamped object carries
`members: list[12]` and `subject: dict[23]`.** These are not two vintages of one shape; they are
two shapes.

### 12. scores canonical -- `scores/v1/2317_TT_Equity/2026-09-17.json` (3,251 B, meta present)
```
as_of | divergence: dict[6] {D,Delta,U,absent_reason,dispersion,state}
peers_v: dict[6] {K:int, M:list[0], V, measures:dict[6], reason, state}
robustness: dict[8] {absent_reason, dropped_constraints, grain, n, n_constraints,
                     per_constraint_absent, state, value}
schema_version: int | security_key | sources: dict[2] {model_block_key, peer_set_key}
```

### 13. scores superseded twin -- `scores/v1/2317_TT_Equity.json` (3,432 B, **meta: NONE**)
```
divergence: dict[8] {D,Delta,U,absent_reason,dispersion,state,status,value}   <- +status,+value
generated_at | inputs: dict[6] {crosswalk_source, model_block_key, model_block_status,
                                peer_member_count, peer_set_key, peer_set_status}
peers_v: dict[8] {K,M,V,measures,reason,state,status,value}                   <- +status,+value
producer: str(60)
robustness: dict[12] {S, absent, constraints, dropped_constraints, eligible, grain, n,
                      n_constraints, reason, security_key, status, value}
schema_version: str(11)   <- STRING here; INT in the canonical twin
security_key
```
Two differences that matter: `schema_version` is a **string** in one and an **int** in the other,
and the twin adds a `status` field per score that the canonical shape does not carry. An adapter
written against one will silently mis-read the other.

### 14. model block -- `derived/model_block/2317_TT_Equity/20260916T201816Z/model_block.json` (94,051 B, meta NONE)
```
security | security_key | raw_stamp_used | fiscal_years: list[10] of str
fiscal_year_row_count: int | orphan_price_rows: int
figures: list[205] of dict  [0] {basis, currency_caveat, fiscal_year, mnemonic, scope, sign,
                                 source, unit, value, vintage}
unresolved: list[0]
```

### 15. model block FYE -- `derived/model_block_fye/BABA_US_Equity/20260911T073934Z/model_block_fye.json` (6,385 B)
```
security | security_key | join | hist_source | dense_price_source
fiscal_years: list[10] of dict  [0] {BOOK_VAL_PER_SH, CAPITAL_EXPEND, CF_FREE_CASH_FLOW, EBITDA,
                                     EBITDA_ADJUSTED, EBITDA_MARGIN, IS_DIV_PER_SHR, IS_EPS,
                                     IS_OPER_INC, IS_SH_FOR_DILUTED_EPS, OPER_MARGIN,
                                     RETURN_COM_EQY, RETURN_ON_ASSET, SALES_REV_TURN,
                                     fiscal_year, gap_days, period_end, price, price_date}
max_gap_days: int
```

### 16a. Bloomberg raw refdata -- `raw/bloomberg/2317_TT_Equity/20260916T201805Z/refdata.json` (546 B, meta NONE)
```
"2317 TT Equity": dict[15] {NAME, CRNCY, CNTRY_OF_DOMICILE, GICS_SECTOR_NAME, PX_LAST,
                            CUR_MKT_CAP, NET_DEBT, CURR_ENTP_VAL, VOLUME_AVG_30D,
                            EQY_SH_OUT_REAL, EQY_FREE_FLOAT_PCT, EQY_BETA, EQY_DVD_YLD_IND,
                            SHORT_INT_RATIO, SI_PERCENT_EQUITY_FLOAT}
```
Top-level key is **the Bloomberg identifier with spaces** (`2317 TT Equity`), not the security_key.

### 16b. Bloomberg raw histdata -- same stamp, `histdata.json` (6,743 B)
```
"2317 TT Equity": list[12] of dict
  [0] {BOOK_VAL_PER_SH, CAPITAL_EXPEND, CF_FREE_CASH_FLOW, CURRENT_EV_TO_T12M_EBITDA, EBITDA,
       EBITDA_ADJUSTED, EBITDA_MARGIN, EQY_DVD_YLD_IND, IS_DIV_PER_SHR, IS_EPS, IS_OPER_INC,
       IS_SH_FOR_DILUTED_EPS, OPER_MARGIN, PE_RATIO, PX_LAST, PX_TO_BOOK_RATIO, RETURN_COM_EQY,
       RETURN_ON_ASSET, SALES_REV_TURN, date}
```

### 17a. SA raw symbol -- `raw/seekingalpha/BABA_US/20260911T040211Z/symbol.json` (21,084 B)
```
data: dict[5] {id, type, attributes: dict[33], relationships: dict[6], meta: dict[2]}
included: list[4] of dict  [0] {attributes, id, meta, type}
meta: dict[6] {marketData: dict[3], chartTimes: dict[12], contentCounters: dict[22],
               showRatings: dict[4], availableData: dict[20], routesData: dict[57]}
```
This is the **unaltered JSON:API envelope** -- `data`/`included`/`meta` is Seeking Alpha's own
wire shape, including 57 `routesData` entries the estate has no use for. Textbook bronze.

### 17b. SA raw news -- `raw/seekingalpha/BABA_US/20260911T040221Z/news.json` (15,233 B)
```
data: list[2] of dict     [0] {attributes, id, links, relationships, type}
included: list[3] of dict [0] {attributes, id, links, type}
meta: dict[2] {page: dict[10], mone: dict[1]}
```

### 18. publication body -- `publications/v1/bbg/7231...4308.json` (12,715 B)
```
schema_version | record_type: "publication_article" | article_key | publisher | article_id  <-- CORRECTED 2026-09-22 by 4.0.0_SA_CRO~Z (flagged by 1.0.0_SA_CTO~Z msg 24243): live value is "publication_article" on 7 of 7 objects
url | title | published | fetched_at
body_blocks: list[22] of str   <-- the extracted article text, block by block
text: str(5825) | words: int | expected_words: None
body_sha256: str(64) | response_sha256: str(64) | transport | content_status
```

### 19. publication link -- `publication-links/v1/BA/bbg/7231...4308.json` (250 B)
```
schema_version | record_type: "security_article" | security_key: str(len=2)  <-- "BA"  <-- CORRECTED 2026-09-22 by 4.0.0_SA_CRO~Z (flagged by 1.0.0_SA_CTO~Z msg 24243): live value is "security_article" on 7 of 7 objects
company | ticker | article_key | publisher | first_discovered_at
```

### 20. pack input ledger -- `packs/2317_TT_Equity/input_ledger.json` (346 B, meta NONE)
```
security_key
entries: list[1] of dict  [0] {detail, input_class, outcome, source, stamp}
```

### 21. pack status -- `packs/NVDA_US_Equity/status.json` (504 B, meta NONE)
```
state | ticker | security_key | requested_at | updated_at | reason: None
raw_stamp | derived_stamp | ref_key | hist_key | derived_key
```

### 22. social measurement -- `social/v1/_measurement/2026-09-15.json` (12,088 B)
```
as_of | cost: dict[7] {basis, claim, estimate_usd, unit, unit_price_usd, usd, usd_cap}
delivery: dict[9] {admitted, capped, fresh, invalid, provisional, records, rejected_by_rule,
                   stale, valid}
generated_at | generated_by
job: dict[10] {completed_at, errors, id, ledger_path, request_sha256, resumed, retrieval_flow,
               state, submitted_at, vendor_status}
latency_seconds: float | method: dict[11] | method_version | normalisation: dict[3]
quality: dict[4] {aboutness_note, relevance_sample: list[10], relevance_sample_denominator,
                  verdict_counts: {PASS, PROVISIONAL, REFUSE}}
second_candidate: dict[7] | security_key | security_name
```

### 24. DynamoDB item -- `opal-harvest-security-metrics`
```
KeySchema: HASH axis_date (S), RANGE ticker (S); GSI axis-rank-index: HASH axis_date, RANGE rank_sort
Sample item attribute types:
  ticker:S  axis_date:S  axis:S  as_of_date:S  rank_sort:S  rank:N  score:N  source:S
  px_end:N  px_end_date:S  px_start:N  px_start_date:S  window_days:N  trading_days_observed:N
  computed_at:S
Attribute presence across the live 284-item scan (denominator 284):
  ticker 284 | axis_date 284 | axis 284 | as_of_date 284
  score 272 | rank 272 | rank_sort 272 | window_days 272 | computed_at 272
  subject 230 | movement 230 | movement_measure 230 | movement_basis 230
  px_* 192 | security_key 146 | identity_status 146 | generation_id 158
  raw_chatter_count 80 | movement_raw_score 70 | window_total_count 70 | pct_jump 64
  baseline_mean 64 | run_id 12 | coverage_vintage 12 | payload_hash 12 | row_count 12
  written_at 12 | record_type 12 | state 12
```
**Only 146 of 284 items carry `security_key` at all.** 138 items are addressable only by `ticker`.

## 3. THE AMBIGUOUS TIERS, ARGUED FROM THE OBJECT'S OWN SHAPE

Three streams cannot be tiered from their prefix name. These are the cases the plan has to decide.

### A. `filings/v1/<key>/<accession>.source.json` -- BRONZE AND SILVER IN ONE OBJECT (MEASURED)

The object holds, in the same document:
- **raw as EDGAR delivered it:** `excerpt.text` at 137,314 characters, plus `document_sha256`
  over the original bytes and `document_bytes`. That is a bronze payload by any definition.
- **a typed derivation over it:** `excerpt.items`, `excerpt.item_keys`, `item_chars{risk,mdna}`,
  `item_full_chars`, `truncated_items`, `officer_section{item,text,chars,sha256,extracted,
  extraction_owner}` and `parser_version`. Those are the output of a parser making choices --
  which Item sections to cut, where to truncate, which section is the officer section.

The discriminator: **`document_sha256` is over bytes this object does not contain.** The original
EDGAR document is never stored anywhere in the estate -- the key census found 0 of 1333 objects
holding a raw filing. So this one object is simultaneously the only bronze evidence for the filing
and a silver product, and the bronze half is a *truncated excerpt*, not the source.
**Consequence for the plan: a re-parse with a new `parser_version` cannot be replayed.** The
input is gone. This is the single most important shape finding in the inventory.
Recommended split: `bronze/edgar/<cik>/<accession>/<primary_document>` holding the fetched bytes
verbatim, and `silver/filings/...` holding everything else, citing the bronze key.

### B. `publications/v1/<publisher>/<sha256>.json` -- BRONZE OR SILVER (MEASURED, leans SILVER)

Carries `response_sha256` (over the vendor response) beside `body_sha256` (over the extracted
text), and `body_blocks: list[22] of str` plus `text: str(5825)` and `words: int`. The vendor's
actual HTTP response is **not** in the object and is not anywhere in the bucket -- a `transport`
field names how it was fetched but the bytes are gone. So like case A, the raw is attested by hash
and not retained. Unlike case A, what remains is *entirely* derived (block-segmented text), with no
verbatim vendor envelope at all. **Classify SILVER, and record that its bronze does not exist.**
Compare `raw/seekingalpha/.../symbol.json`, which is unambiguous bronze precisely because it keeps
the `data`/`included`/`meta` envelope intact, 57 useless `routesData` entries and all.

### C. `scores/v1/...` -- GOLD, but which of the two? (MEASURED, already ruled)

Both shapes are gold (firm-attributable derived product, three scores per name). The ambiguity is
not the tier but the address, and it was already adjudicated: `AMGT_RESAPP/surprise-channel/
remediations/REMEDIATION_v13.md:108-112` rules the **date-partitioned shape canonical** and the
flat set "a superseded artifact left in place". The served read resolves the date-partitioned key
only. The 31 flat objects remain and are unreferenced. See hazard H-2.

### D. `derived/model_block/...` -- SILVER, not GOLD (MEASURED)

Argued because the name "derived" invites gold. Every entry in `figures: list[205]` carries
`{value, unit, sign, basis, vintage, source}` and the module docstring
(`model_block_pull.py:17-22`) states Bloomberg's field definitions are "adopted as-is; no other
vendor's per-share earnings adjustment is reconstructed here." A typed, unit-tagged restatement of
one vendor's fields with no firm judgment applied is **silver**. The gold layer above it is
`scores/` and `posture/`, which apply Opal's rules.

### E. `management/v1/<key>/<date>.json` -- SILVER with a GOLD field (INFERRED)

The roster itself is a parse of EDGAR Item 6 (silver). But `avg_tenure_years` is an Opal-computed
statistic, and `management/v1/_pool/<date>.json` is purely that statistic across the universe --
firm-attributable, hence gold. Today they share a prefix. The `_pool` object should move up a tier;
the per-name roster should not.

### F. `packs/<key>/input_ledger.json` -- STATE, not data (MEASURED)

`entries: list[1] of dict {detail, input_class, outcome, source, stamp}` is a run log. The module
says so: `lib/research/ledger/ledger.py:9` -- "This is the ONE artifact under packs/ that is
[appended]". It belongs under `state/`, not beside the packs.

## 4. COLLISIONS AND HAZARDS THE PLAN MUST HANDLE

**H-1. The slash-inside-the-security-key defect is LIVE, in 10 keys across 6 prefixes.**
`BP/_LN_Equity` and `NG/_LN_Equity` are not path segments -- they are one security key whose
Bloomberg root contains `/` (`BP/ LN Equity`, `NG/ LN Equity`). S3 has no directories, so the key
silently acquires an extra level and every `key.split("/")` in the estate reads the security as
`BP`. MEASURED occurrences (denominator 1333):
```
derived/model_block/BP/_LN_Equity/20260916T201840Z/model_block.json
derived/model_block/NG/_LN_Equity/20260916T201927Z/model_block.json
filings/v1/BP/_LN_Equity/UNRESOLVED-SOURCE.source.json
filings/v1/NG/_LN_Equity/UNRESOLVED-SOURCE.source.json
packs/BP/_LN_Equity/input_ledger.json
packs/NG/_LN_Equity/input_ledger.json
peers/v1/BP/_LN_Equity/{2026-09-15.json,2026-09-16T1930Z.json,2026-09-17T0215Z.json,2026-09-17T0240Z.json}
peers/v1/NG/_LN_Equity/{same four}
posture/v1/BP/_LN_Equity/2026-09-16.json
posture/v1/NG/_LN_Equity/2026-09-16.json
raw/bloomberg/BP/_LN_Equity/20260916T201833Z/{refdata,histdata}.json
raw/bloomberg/NG/_LN_Equity/20260916T201916Z/{refdata,histdata}.json
scores/v1/BP/_LN_Equity.json  AND  scores/v1/BP/_LN_Equity/2026-09-17.json
scores/v1/NG/_LN_Equity.json  AND  scores/v1/NG/_LN_Equity/2026-09-17.json
```
The depth histograms prove it independently: `peers/` is `{3: 787, 4: 10}` -- ten objects one level
deeper than their 787 siblings. Every prefix-scoped count in the estate is off by these, and every
`list_objects_v2(Delimiter='/')` sees a phantom security called `BP`.
Fix in the plan: the security_key must be percent-encoded or the `/` mapped (e.g. `BP.SLASH_LN`)
at `lib/research/identity/crosswalk.py` before it ever reaches a key builder.

**H-2. `scores/v1/` holds TWO grammars written by TWO generations -- 33 + 31 objects.**
`scores/v1/<key>/<date>.json` (33, metadata present, written via `run_scores.py:231` ->
`crosswalk.write_pool`) and `scores/v1/<key>.json` (31, **metadata absent**, no writer in the tree).
The depth histogram is the tell: `{2: 31, 3: 33, 4: 2}`. Already filed and ruled canonical-plus-
orphan (`REMEDIATION_v13.md:108`), but the 31 orphans are still in the bucket, still match the IAM
grant `scores/v1/*`, and their `schema_version` is a **string** where the canonical is an **int**.

**H-3. `peers/v1/` holds TWO grammars and they are not two vintages of one shape.**
220 objects at `<key>/<date>.json` and 567 at `<key>/<ISO-stamp>.json` (189 x 3 stamp batches).
Beyond the key: the dated form carries `as_of: str(10)`, `members: list[0]`, `subject: None`,
`csc_columns: dict[11]`, `denominators: dict[1]`; the stamped form carries `as_of: str(16)`,
`members: list[12]`, `subject: dict[23]`, `csc_columns: dict[14]`, `denominators: dict[14]`.
`api/scoped_amgt.py`'s "latest .json in key order" convention resolves `2026-09-17T0240Z.json`
after `2026-09-16.json` **by luck of ASCII ordering**, not by rule. A 2026-10 dated object would
sort after every 2026-09 stamped one and serve the empty shape.
Writer: `lib/research/peers/engine.py:1143`.

**H-4. `posture/v1/` is OVERWRITTEN IN PLACE and the key lies about when. 31 of 33 (MEASURED).**
The key carries `as_of`, but `LastModified` is later than that date for 31 of the 33 objects --
e.g. `posture/v1/2317_TT_Equity/2026-09-16.json` was last written `2026-09-18T14:08:14Z`. The
prefix's own last-write is `2026-09-18T14:12:29Z`. So "the 2026-09-16 posture" is whatever the last
re-run produced, and nothing in the key or the document distinguishes the two.
Writer: `lib/research/posture/judge.py:290`.

**H-5. The bucket's own declared contract is FALSIFIED on the applied plane.**
`infra/aws/terraform/harvest/s3.tf` states: *"Nothing is ever written to a path that already
exists"* and *"versioning below is the safety net for an accidental overwrite, not the mechanism
the grammar relies on."* MEASURED against `list_object_versions`: **632 non-latest versions**
across 1965 total, 0 delete markers, distributed:
```
filings 506 | peers 99 | drafting 9 | posture 7 | social 6 | management 4 | packs 1
```
`filings/` alone carries 506 non-latest versions over 202 current objects -- because
`UNRESOLVED-SOURCE.source.json` has no vintage in its key at all and is rewritten every batch run.
The DECLARED grammar in the same file is also absent from the store: `packs/<security_key>/
<YYYYMMDDTHHMMSSZ>/pack.json` matches **0 of 1333** keys. The live `packs/` grammar is
`packs/<security_key>/{input_ledger,status}.json`, two levels shallower and with no stamp.

**H-6. FIVE competing security-key conventions, all live, enumerated by the estate itself.**
`lib/research/identity/crosswalk.py:103-145` names them (`bare-root-pilot-key <ROOT>`,
`security-hash-key security-<16hex>`, `pack-key <ROOT>_<CC>`, `model-key <ROOT>_<CC>_Equity`,
`bloomberg-identifier "<ROOT> <CC>"`). MEASURED distinct first-segments per prefix:
```
peers/v1/              191   <ROOT>_<CC>_Equity
filings/v1/            190   <ROOT>_<CC>_Equity
packs/                  37   MIXED: BABA_US, BA_US, COST_US alongside 34 <ROOT>_<CC>_Equity
derived/model_block/    34   <ROOT>_<CC>_Equity
raw/bloomberg/          34   <ROOT>_<CC>_Equity
scores/v1/              33   <ROOT>_<CC>_Equity
posture/v1/             33   <ROOT>_<CC>_Equity
management/v1/          13   <ROOT>_<CC>_Equity
drafting/v1/            12   <ROOT>_<CC>_Equity
raw/seekingalpha/        3   <ROOT>_<CC>          -- BABA_US, BA_US, COST_US
publication-links/v1/    3   <ROOT>               -- BA, COST, HD
```
`raw/bloomberg/` and `raw/seekingalpha/` are **sibling prefixes under one parent using different
conventions**. `packs/` carries both in one prefix (`packs/BABA_US/` and `packs/BABA_US_Equity/`
are the same company at two addresses; likewise `BA_US`/`BA_US_Equity`, `COST_US`/`COST_US_Equity`
-- 3 duplicate pairs of 37). Inside the raw Bloomberg documents the top-level JSON key is the
**space-separated Bloomberg identifier** (`"2317 TT Equity"`), a sixth form.

**H-7. Keyed by a NAME, not a security_key -- four surfaces.**
- `publication-links/v1/{BA,COST,HD}/` -- bare ticker root, 7 of 7 objects.
- DynamoDB `opal-harvest-security-metrics` RANGE key is `ticker`; only **146 of 284** items carry
  `security_key` at all (live scan). 138 items cannot be joined to the crosswalk.
- DynamoDB `etf-classifications`, HASH key `ticker` (285 items) -- read by
  `lib/research/identity/positioning_chain.py:68`.
- DynamoDB `trade-security-identifiers`, HASH key `ticker` (92 items) -- `positioning_chain.py:69`.

**H-8. A `v1` in the prefix on 10 of 16 top-level prefixes, and it means nothing.**
`crosswalk/v1/`, `universe/v1/`, `identity/v1/`, `filings/v1/`, `drafting/v1/`, `management/v1/`,
`posture/v1/`, `peers/v1/`, `scores/v1/`, `publications/v1/`, `publication-links/v1/`,
`social/v1/`. No prefix has ever had a `v2`; meanwhile the documents carry their own
`schema_version` field (int in most, **string** in the superseded scores twin) which is the field
that actually moved. The path version is decorative and it costs: `infra/aws/terraform/harvest/
scoped-amgt-api.tf:151` documents that the IAM grant had to be written as `scores/v1/` WITH the
trailing slash precisely because `scores` or `scores/v1` would also match a future `scores_v2/`.
Note the inconsistency it already produced: `derived/model_block/` has no `v1` and sits one
character away from `derived/model_block_fye/`, which the same comment flags as the identical
hazard one level over.

**H-9. FOUR independent implementations of one "write to the pool" contract.**
```
lib/research/identity/crosswalk.py:609   write_pool()            -- put + read-back + metadata
lib/research/posture/judge.py:285        write_pool_object()     -- its own copy
lib/research/peers/engine.py:1138        write_pool_object()     -- its own copy
lib/research/social/collect.py:479       write_pool_object()     -- its own copy
```
plus **five direct `put_object` writers with no metadata and no read-back**:
`integrations/bloomberg/research/model_block_pull.py:198`, `lib/research/ledger/ledger.py:87`,
`integrations/bloomberg/research/pull_consumer.py:57`, `lib/opal_data_harvest/uploads.py:76`,
`lib/opal_data_harvest/build_release.py:65`.
The consequence is MEASURED and visible in the head metadata: objects written through a
`write_pool*` path carry `Metadata={document-sha256, schema-version}`; `derived/model_block/`,
`raw/`, `packs/`, `lib/` and the 31 superseded `scores/v1/<key>.json` carry **`Metadata=[]`**.
So integrity metadata exists on some streams and not others, by accident of which module wrote it.

**H-10. `packs/_template/` is cited by code and does not exist. 0 of 1333.**
`lib/research/print/render_pack.py:71-73` sets `TEMPLATE_PREFIX = "packs/_template/"` and
`TEMPLATE_KEY = TEMPLATE_PREFIX + TEMPLATE_NAME`, read by `read_template_block_headers()`.
Census of the live store for `packs/_template`: **0 hits across 1333 keys.**

**H-11. Source code is stored in the data bucket.**
`lib/local-publications/0.1.0/<hash>/local-publications-0.1.0.zip` + `manifest.json`, 6 objects /
445,796 bytes, written by `lib/opal_data_harvest/build_release.py:65`. The manifest lists 38 repo
**source files** including `org/tier1_exec/4.0.0_SA_CRO/scripts/*.py` and
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~3/universe.json`. A release
artifact belongs in an artifacts bucket, not beside bronze.

**H-12. Pool-grade data living in worker DELIVERABLES folders in the repo.**
MEASURED: 380 files under `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/`, of which **79** are
`.json` over 20 KB. The largest are data, not evidence:
```
1,000,578 B  .../0.9.0_WK_AMGT_RESAPP~21/candidate_universe.json
  212,933 B  .../0.9.0_WK_AMGT_RESAPP~25/peers_batch.2026-09-17T0240Z.json   (= a peers/ batch)
  212,933 B  .../0.9.0_WK_AMGT_RESAPP~25/peers_batch.2026-09-17T0215Z.json
  204,556 B  .../0.9.0_WK_AMGT_RESAPP~21/peers_batch.2026-09-16T1930Z.json
  188,380 B  .../0.9.0_WK_AMGT_RESAPP~19/crosswalk.v1.2026-09-15.json        (= crosswalk/v1/, byte-identical size)
  185,928 B  .../0.9.0_WK_AMGT_RESAPP~19/universe.v1.2026-09-15.json         (= universe/v1/)
  163,772 B  .../0.9.0_WK_AMGT_RESAPP~1/model_block_BABA_US_Equity.json      (= derived/model_block/)
  116,222 B  .../0.9.0_WK_AMGT_RESAPP~3/universe.json
```
`.../~3/universe.json` is not merely a copy -- `lib/opal_data_harvest/config.json` names it as the
**live `universe_source`** for the local publication harvester. A production input is a file in a
worker's deliverables folder, and it is also listed inside the S3 release manifest (H-11).

**H-13. Exactly ONE of 25 streams has a trigger. MEASURED.**
Of 217 Lambda functions, 3 are RESAPP's: `amgt-resapp-chatter-axis` (producer),
`opal-amgt-scoped-api` (the serving API), `opal-research-pull-enqueue` (SQS enqueue).
Of 23 EventBridge Scheduler schedules, exactly one is RESAPP's:
`amgt-resapp-chatter-axis-daily`, ENABLED, `cron(0 10 * * ? *)` UTC, target
`amgt-resapp-chatter-axis`. Of 144 EventBridge rules, **zero**.
So `crosswalk`, `universe`, `filings`, `drafting`, `management`, `posture`, `peers`, `scores`,
`model_block`, `model_block_fye`, `raw/bloomberg`, `raw/seekingalpha`, `publications`,
`publication-links`, `packs`, `social` -- **16 of 17 S3 streams -- are produced by a human or an
agent running a module by hand.** Two of them (`raw/bloomberg`, `derived/model_block`) can only run
on the Bloomberg terminal box; two more (`publications`, `publication-links`) can only run on a
signed-in Windows desktop with Chrome, via a Scheduled Task whose config ships
`recurring_schedule_enabled: false` and `automatic_uploads_enabled: false`.
This is the single largest structural fact for a management plan, and it is not a defect of any
one stream -- it is the shape of the whole estate.

**H-14. An upstream RESAPP depends on has not moved in 42 days, and it lives in a PORTAL bucket.**
`s3://opal-data-portal-v2/json/security_scanner/latest/` -- 19 objects, 171,914,443 bytes,
**last modified 2026-08-07** (measured 2026-09-18). `lib/research/peers/universe.py:61-63` reads it
as the peer-candidate database; `peers/v1/` objects carry `"database_vintage"` from it. A
`latest/` prefix with no date partition cannot be asked "which day is this"; the only vintage
signal is `LastModified`, and 42 days of it is invisible to every consumer.

**H-15. A declared table that has never held a row.**
`opal-harvest-articles` -- live scan **0 items**, 0 bytes, with two GSIs (`platform_date_index`,
`ticker_date_index`) and point-in-time recovery ENABLED. Declared at
`infra/aws/terraform/harvest/dynamodb.tf`. Article content went to `publications/v1/` in S3
instead. Dead resource, and PITR on it is a standing cost.

**H-16. One DynamoDB table, two partition-key grammars.**
Live scan of `opal-harvest-security-metrics` found **23 distinct `axis_date` partitions** across
284 items, in two shapes:
```
<AXIS>#<date>                          e.g. TRENDING_PRICE#2026-09-15          (33 items)
<AXIS>#<date>#<generation_id>          e.g. TRENDING_PRICE#2026-09-15#20260917T222503Z-c35c454d1e4f  (32 items)
```
Both shapes exist for the SAME axis and the SAME date. `lib/research/price/generation.py:9`
documents the cause in its own docstring: an earlier writer "writes bare rows at
`<AXIS>#<as_of_date>` with `table.put_item` and stops -- no generation". Three modules write this
table (`metrics/chatter_axis.py:750-766`, `price/generation.py:458-476`, `watchlist/store.py:83`)
and the `generation_id` attribute is present on only **158 of 284** items.

**H-17. Six axis prefixes in one table, never enumerated anywhere.**
Measured from the live partition list: `PRICE`, `TRENDING_PRICE`, `BREAKOUT_PRICE`, `CHATTER`,
`TRENDING_CHATTER`, `BREAKOUT_CHATTER`. `CHATTER#2026-09-11` (10 items) is a seventh, retired form
with no `TRENDING_`/`BREAKOUT_` qualifier. Partition sizes range 1 to 33; the 1-item partitions
(`BREAKOUT_CHATTER#2026-09-16/17/18`, `TRENDING_CHATTER#2026-09-16/17/18`) are pointer or marker
rows sharing the key space with data rows -- `record_type`/`state`/`row_count` appear on exactly
12 items.

## 5. WHAT ELSE SHARES THE BUCKET

**Almost nothing, and this is the good news.** MEASURED: all 16 top-level prefixes of
`opal-data-harvest` are AMGT_RESAPP's, with exactly one exception.

| Prefix | Objects | Bytes | AMGT_RESAPP? |
|---|---|---|---|
| `crosswalk/` | 1 | 188,380 | yes |
| `derived/` | 50 | 4,325,141 | yes |
| `drafting/` | 12 | 1,127,014 | yes |
| `filings/` | 202 | 4,597,976 | yes |
| `identity/` | 1 | 47,229 | yes |
| `lib/` | 6 | 445,796 | **NO -- release artifact (source code), see H-11** |
| `management/` | 14 | 41,298 | yes |
| `packs/` | 37 | 12,879 | yes |
| `peers/` | 797 | 19,414,414 | yes |
| `posture/` | 33 | 376,437 | yes |
| `publication-links/` | 7 | 1,839 | yes |
| `publications/` | 7 | 66,021 | yes |
| `raw/` | 97 | 640,737 | yes |
| `scores/` | 66 | 220,820 | yes |
| `social/` | 1 | 12,088 | yes |
| `universe/` | 2 | 383,492 | yes |
| **TOTAL** | **1333** | **31,901,561** | 15 of 16 prefixes |

The bucket was created 2026-09-11 specifically for this project and tagged
`project=AMGT_RESAPP, directive=D5, owner=2.0.0_SA_COO` (`s3://` tags read from
`infra/aws/terraform/harvest/s3.tf`). There is no other tenant. `infra/.../scoped-amgt-api.tf:161`
corroborates the same 16-prefix denominator from an independent read on 2026-09-18, and records
that 13 are IAM-granted to the serving role; the three ungranted are `identity/`, `lib/` and
`social/` -- `social/` deliberately, because collection is RESERVED and OFF.

**So "we can run bronze and silver inside the opal-data-harvest bucket" costs nothing to adopt on
the tenancy axis.** The work is entirely in the key grammar above the bucket, not in moving data
between buckets. The only cross-bucket reads are the four upstream planes in section 1, all
read-only and all outside this project's write surface.

## 6. WHAT THE PLAN INHERITS -- the short version

1. **No layer boundary exists today.** 16 top-level prefixes named after *engines*
   (`peers`, `posture`, `scores`, `drafting`, `filings`) rather than *layers*. Bronze
   (`raw/`), silver (`derived/`, `management/`) and gold (`scores/`, `posture/`, `peers/`) are
   peers in the namespace, so nothing about an address tells a reader what it may trust.
2. **The two true bronze streams retain their source; the two most important ones do not.**
   `raw/bloomberg/` and `raw/seekingalpha/` keep vendor bytes. EDGAR filings and publisher
   articles keep only a `sha256` of bytes nobody stored (section 3, A and B). A re-parse is
   impossible for both.
3. **One schedule, sixteen manual streams** (H-13), two of which are pinned to physical machines.
4. **Six identity conventions, one of which produces a `/` inside the key** (H-6, H-1).
5. **The write path is forked four ways plus five raw puts** (H-9), so integrity metadata is
   present or absent by accident.
6. **The declared contract in `s3.tf` is falsified by 632 non-latest versions** (H-5) -- the
   "never overwrite" grammar is aspirational, and `filings/` breaks it 506 times.

---
Scratchpad artifacts for this pass (not repo files):
`scan_bucket.py`, `grammar.py`, `skeleton.py`, `vintage.py`,
`keys_opal_data_harvest.tsv` (1333 rows), `skeleton.txt` (1136 lines).
