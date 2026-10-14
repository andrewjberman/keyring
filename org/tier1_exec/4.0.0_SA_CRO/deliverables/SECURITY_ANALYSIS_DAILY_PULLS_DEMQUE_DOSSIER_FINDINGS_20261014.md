# Security Analysis daily pulls, schedules, MDPF_DEMQUE accounting and the JSON dossier -- findings

**Author:** 4.0.0_SA_CRO (laptop). **Date:** 2026-10-14, measured ~19:30-20:20Z (15:30-16:20 ET).
**Order:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261014_191xZ_AMGT_SECURITY_ANALYSIS_DAILY_PULLS_AND_DOSSIER.md` @7c663b2a90
([file](file:///C:/Users/AndrewBerman/Desktop/ajb_workspace/org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261014_191xZ_AMGT_SECURITY_ANALYSIS_DAILY_PULLS_AND_DOSSIER.md)).
**Scope:** research only. No served change, no AWS write, no POST route call, no Bloomberg pull. Live reads were
read-only `s3 ls` / `s3api list-objects-v2` / `s3 cp` to scratch, `dynamodb get-item|describe-table`,
`lambda get-function-configuration`, `scheduler get-schedule`, `events describe-rule`, `logs filter-log-events`, and
GET-only `lambda invoke` of `opal-amgt-scoped-api` (`/thesis`, `/print`, `/print?format=rich|json`).
**Claim basis:** every value below is MEASURED (live read or file:line) unless marked INFERRED or UNREAD. Box-side Windows
tasks (site Z, Bloomberg terminal box) are UNREAD from this laptop (`Get-ScheduledTask` here holds none of them);
their cadence is INFERRED from object write times. Code was read at workspace `box/laptop` @7c663b2a90, portal `DEV` @97c66c93.
**Repo paths** are relative to `file:///C:/Users/AndrewBerman/Desktop/ajb_workspace/`.

## Conclusion (read this first)

The page is **not** pulled daily as a whole:
- **Four inputs are on an applied daily trigger.** The PRICE ranking and price history (Bloomberg box, 07:00 ET) are at the
  trading-day frontier (as-of 2026-10-13, 94 rows). The model block, packs ledger and Bloomberg reference data
  (site Z, ~13:00Z) are current, but 2026-10-13 was missed when the Terminal was signed out.
- **One daily job runs but serves nothing.** The CHATTER axes (AWS, 10:00Z) commit EMPTY every day: 0 of 242 rows.
- **About fifteen producers are run by hand, with no trigger anywhere.** These are dossier, peers, drafting/filings,
  management, posture, scores, universe, crosswalk, the news/chatter gold and tone. Their lag runs from 1 trading day
  (peers) to about 19 (posture).
- **Seeking Alpha has stopped** (bronze dead since 09-22, articles since 10-12).
- **Bright Data SERP is empty** (0 objects).
- **AI fill is fresh but held off the page** by a deliberate round-105 ruling.

DEMQUE meters only four one-off AMGT research requests, and none has drawn. The page's largest Bloomberg draw, the daily
model-block refresh of 96 names, bypasses the queue. It is ledgered after the fact with `cells: null`, about 94,900 cells
a day by DEMQUE's own rule (INFERRED upper bound). The price leg, induction reference data, officers and the on-demand
SQS seam are unmetered.

There is **no JSON download**: the server refuses `format=json` with 400, measured live. A cited JSON dossier exists in S3
gold. Every present value has a source, but 0 research values carry an as-of, and only team-sheet labels carry a claim
field. Neither the PDF nor the Markdown export includes the team's research.

## Security denominator

**95 names, measured. Not 93.**
- The page's universe is the folder listing
  `s3://opal-data-harvest/amgt/harvest/gold/research_dossier/security_key=<K>/`. The reader is
  `lib/research/coverage/covered_universe.py:26-48 covered_security_keys()`, which calls the list "THE ONE NAMED PAGE
  UNIVERSE".
- `bash .tools/aws s3 ls s3://opal-data-harvest/amgt/harvest/gold/research_dossier/ | grep -c 'PRE security_key='` = **95**
  (re-read by this seat at ~20:10Z).
- The served freshness snapshot (written 2026-10-14T12:30Z) agrees: `denominators.covered_names = 95`.
- 93 is the older AMGT_CORPUS FWD-19 population; see row `AMGT_RESAPP-D1-W408-S2` at
  `org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md:25482-25497`.

Other lists in play disagree with the 95:

| List | Count | Who reads it |
|---|---|---|
| `universe/v1/2026-10-06.json` | 302 names (242 keyed) | freshness, PRICE and CHATTER producers |
| PRICE generation 2026-10-13 | 94 rows | Lead Panel price face |
| model-block pull log | 99 keys | daily refresh |
| `derived/model_block/` | 102 prefixes | page model reads |
| `packs/` | 105 prefixes | ledger |

The 95 keys are listed in the Appendix.

---

# Part 1 -- What each security displays, per tab and component, and where it comes from

The lists below give the served object (O-n), its reader, its producer, its deploy shape and its upstream. The per-tab
table after them cites the O-n labels.

## Path legend

All repo paths are relative to file:///C:/Users/AndrewBerman/Desktop/ajb_workspace/

| Short form | Means |
|---|---|
| `SA/` | `portal/src/pages/SecurityAnalysis/` |
| `API.ts` | `portal/src/api/endpoints/amgt-lead-panel.ts` (BASE `/api/scoped/amgt`, :51) |
| `SAMG` | `lib/research/api/scoped_amgt.py` |
| `POOL` | `s3://opal-data-harvest/` |
| `MTAB` | DynamoDB `opal-harvest-security-metrics` (HASH `axis_date`, RANGE `ticker`; GSI `axis-rank-index`; 6,845 items by describe-table) |

**Bucket resolution.** `pool_reader.POOL_BUCKET = os.environ.get("AMGT_POOL_BUCKET", "opal-data-harvest")`
(`lib/research/coverage/pool_reader.py:73`). The live Lambda `opal-amgt-scoped-api` has only three
environment variables: `HARVEST_METRICS_TABLE=opal-harvest-security-metrics`,
`HARVEST_ARTICLES_TABLE=opal-harvest-articles` and `AMGT_AIFILL_ROOT=/var/empty/aifill-hold`
(get-function-configuration read; LastModified 2026-10-14T13:01:34Z). It has no `AMGT_POOL_BUCKET`, so
every pool read goes to `opal-data-harvest`. The drafting bucket is `crosswalk.POOL_BUCKET`, also
`opal-data-harvest` (`SAMG:2956`, `lib/research/identity/crosswalk.py:70`). Gold reads use
`store.HARVEST_BUCKET = "opal-data-harvest"` (`lib/research/harvest/store.py:36`).

**Serving Lambda.** `opal-amgt-scoped-api`, python3.11, 29 s timeout, 1769 MB, artifact
`research/opal-amgt-scoped-api.zip` (`infra/aws/terraform/harvest/scoped-amgt-api.tf:459-520`). The route
table `SAMG:7906-7939` lists 18 routes; the handler is `SAMG:7523-7828`.

**Prefix constants.** These come from `lib/research/api/_harvest_prefixes.py`, which is generated:

| Constant | Value |
|---|---|
| `AI_FILL_GOLD_PREFIX` | `amgt/harvest/gold/ai_fill/` |
| `BLOOMBERG_BRONZE_PREFIX` | `bloomberg/harvest/bronze/` |
| `BRIGHT_DATA_SERP_BRONZE_PREFIX` | `bright-data/harvest/bronze/serp/` |
| `FILING_ATTEMPT_STATE_PREFIX` | `amgt/harvest/state/filing_attempt/` |
| `SEEKING_ALPHA_BRONZE_PREFIX` | `seeking-alpha/harvest/bronze/` |
| `SEEKING_ALPHA_JOB_RECORD_STATE_PREFIX` | `seeking-alpha/harvest/state/job_record/` |

## The served-object index

The main table cites these objects by their `O-n` label.

| ID | Served object (exact) | Reader | Producer (file:function) | Deploy shape | Upstream |
|---|---|---|---|---|---|
| O-1 | `POOL derived/model_block/<slash-safe key>/<YYYYMMDDTHHMMSSZ>/model_block.json`, newest stamp | `SAMG:2123 _read_model_block_pool`, via `read_model_block` :2067 | `integrations/bloomberg/research/model_block_pull.py:stage_derive` (put :1810-1812) | (i) Windows task, daily 13:00Z: `lib/research/corpus/schedule_induction.ps1` -> `induction_scheduled.py:main` (admit + refresh). (ii) On demand: Lambda `opal-research-pull-enqueue` -> SQS `opal-research-pull-requests` -> `pull_consumer.py:process_one`, a poller started by hand (`api-gateway.tf:68-110`, `sqs.tf:19-31`) | Bloomberg direct BLPAPI on the terminal box. The Seeking Alpha forecast fallback is disabled in refresh (`model_block_pull.py:2417-2421`) |
| O-1b | `derived/model_block_fye/...` (corrected fiscal price overlay) | `SAMG:2197 _apply_corrected_overlay` with root `AMGT_MODEL_BLOCK_ROOT` (`SAMG:178`) | `derive_fye_fixed.py` (run by hand, 3 names) | n/a | **Not reached in production.** The live Lambda has no `AMGT_MODEL_BLOCK_ROOT`, so the overlay root is `""` and the overlay is never applied. The IAM grant excludes the prefix (`scoped-amgt-api.tf:99-106`) |
| O-2 | `MTAB` partitions `<MOVEMENT>_<SUBJECT>#<date>`, read through the `_CURRENT` generation pointer -> generation rows (GSI `axis-rank-index`, `ScanIndexForward` true) | `SAMG:452 read_generation_pointer`, `:519 read_generation_rows`, `:1538 read_rankings`, `:1692 read_point_record` | CHATTER: `lib/research/metrics/chatter_axis.py:compute_chatter_axis` (:802). PRICE: `integrations/bloomberg/research/price_axis_pull.py:main` (:341, generation write :412-430). Registry: `lib/research/metrics/movement_gate.py:196-199` | CHATTER: Lambda `amgt-resapp-chatter-axis`, `cron(0 10 * * ? *)` UTC (`chatter-axis-schedule.tf:175-246`). PRICE: Windows task `OPAL_BBGTML_daily_pull`, 07:00 NY, terminal box (`register_daily_task.ps1:24-32`; `integrations/bloomberg/pipeline/scheduled_daily_pull.cmd:353`) | CHATTER: internal derivation from harvested publications (`publication-links/v1`, `publications/v1`). PRICE: Bloomberg BLPAPI PX_LAST over the `universe/v1` list |
| O-2w | `MTAB` `TRENDING_PRICE_90D` / `_365D` (and `BREAKOUT_*`) `#<date>` | `SAMG:1613 read_window_rankings` | `integrations/bloomberg/research/price_history_pull.py` (:24-26, :72) | **Run by hand.** No .cmd/.ps1/.bat under `integrations/bloomberg` calls it (Grep) | Bloomberg BLPAPI |
| O-3 | DynamoDB `etf-classifications`, GetItem on `ticker` (bare ticker; 11,362 items) | `SAMG:710-825` (`_classification_for_ticker`, `_prefetch_classifications`, `_join_classification`) | (a) `infra/aws/lambda/v2_portal/_shared/etf_classification_scheduled.py:write` (565-578). (b) `mdpf-secclass-sector-writer-lambda`. (c) `mdpf-secclass` new-security classifier. (d) Seed script `yang_pipeline/seed-etf-classifications.py` | (a) EventBridge `bd-canonical-prices-daily` `cron(0 4 * * ? *)` -> bd-gold EC2. (b) `cron(30 10 ? * MON-FRI *)` NY. (c) `cron(0 10 ? * MON-FRI *)` NY | BD/Schwab security masters plus Bloomberg GICS |
| O-4 | `POOL crosswalk/v1/<as_of>.json`, newest. 8 objects; newest `2026-10-09.json` (s3 ls) | `SAMG:3649 resolve_identity` -> `crosswalk.resolve`; `name_search` | `lib/research/identity/crosswalk.py:main` (:1665) -> `write_pool` (:1533-1590); `add_security --batch --write-pool` | Run by hand, plus the induction task (O-1 (i)) through `add_security` | Internal (coverage folders + registrations), Bloomberg identity reference data, SEC `filing_source` issuer data |
| O-5 | `POOL amgt/harvest/gold/research_dossier/security_key=<K>/as_of=<date>.<hash>.json` | `SAMG:5586 _read_dossier_document` -> `lib/research/corpus/dossier.py:1626 read_dossier`. The folder listing is also the covered universe (`lib/research/coverage/covered_universe.py:26-48`) | `lib/research/corpus/dossier.py:write_one` (:1651) through `gold.gold_put` | Run by hand: `python -m lib.research.corpus.dossier --write` (`dossier.py:2255-2260`) | Internal composition from Opal's own research reports (PDF/workbook bronze) plus the newest model block. No vendor or LLM call (`dossier.py:9-16`) |
| O-6 | `POOL drafting/v1/<slash-safe key>.json`. 12 objects (s3 ls) | `SAMG:3031 _read_drafting_document`, `:3265 read_drafted_sections` | `lib/research/filings/analyze.py:write_outputs` (:1917-1963) | Run by hand, or `filings/batch.py`. The task `OpalResearch-FilingsAnalyzer` (weekly Sun 06:00) is **created DISABLED** (`batch.py:9-15, 300-305`) | LLM (Anthropic `claude-opus-5`, two passes with citations) over SEC EDGAR 10-K/20-F |
| O-7 | `POOL filings/v1/<slash-safe key>/<accession>.analysis.json`. 195 key folders (s3 ls) | `SAMG:4412 read_segment_breakdown`; `lib/research/filings/section_coverage.py:134` (passage coverage); thesis driver passages `SAMG:4475` | Same as O-6 (`analyze.write_outputs` :1943-1945) | Same as O-6 | Same as O-6 |
| O-8 | `POOL amgt/harvest/state/filing_attempt/<partition>/UNRESOLVED-SOURCE.json` and `UNRESOLVED-SOURCE.HELD.json` | `SAMG:4115`, `:4147` | `lib/research/harvest/filings.py:state_put_filing_attempt` (:369-455); `_put_filing_attempt_held_marker` (:326) | Run by hand (`fetch.persist`, filings batch, `analyze.main`) | SEC EDGAR attempt outcomes |
| O-9 | `POOL amgt/harvest/gold/ai_fill/security_key=<K>/ai_fill.json`. 95 key folders (s3 ls) | `SAMG:3398 _read_ai_fill_document`, `:3571 read_ai_fill` | `lib/research/aifill/store.py:write_document` (:57-73) via `aifill/run.py:main` | Run by hand (`--to-s3 --confirm-write`) | LLM (Anthropic `claude-opus-5` with web search). **HELD at read:** live env `AMGT_AIFILL_ROOT=/var/empty/aifill-hold` makes every name serve ABSENT with blocks `{}` (`scoped-amgt-api.tf:511-517`) |
| O-10 | `POOL peers/v1/<key>/<as_of>.json`, latest. 245 key folders | `SAMG:2387 read_peer_set` (`read_pool_object` :2293) | `lib/research/peers/engine.py:write_pool_object` (:1184-1199); entry point `lib/research/api/peers_rebuild.py:main` | Run by hand (`python -m lib.research.api.peers_rebuild --as-of ... --write-pool`) | Internal: the Security Scanner universe files `s3://opal-data-portal-v2/json/security_scanner/latest/universes/`, model-block headers, Seeking Alpha candidates (`sa_rest_fetch`). No Bloomberg call |
| O-11 | `POOL management/v1/<key>/<as_of>.json` + `management/v1/_pool/<as_of>.json`. 18 folders | `SAMG:5138 read_management`, `:5161`, `:5291`; F3 chain `lib/research/management/exec_roster_chain.py` (filing -> research notes -> stored Bloomberg officers) | `lib/research/management/enrich.py:write_document` (:918), `write_pool_object` (:1190) | Task `OpalResearch-ExecManagement` (weekly Sun 07:00) **created DISABLED** (`batch.py:9-17`), or by hand: `management_posture_batch.py management --write-pool` | SEC filing roster, Lusha v3, Bright Data SERP (CEO query), Bloomberg `COMPANY_EXEC_OFFICERS` fallback (BLPAPI; bronze `bloomberg/harvest/bronze/exec_officers/`) |
| O-12 | `POOL posture/v1/<key>/<as_of>.json`. 35 folders | `SAMG:5442 read_posture` | `lib/research/posture/judge.py:write_pool_object` (:298-303) | Run by hand (`management_posture_batch.py posture --write-pool` or `python -m lib.research.posture.judge`); "no schedule is created" (`judge.py:41-42`) | LLM: one `claude-opus-5` call per name over internal evidence packs |
| O-13 | `POOL scores/v1/<key>/<as_of>.json`. 35 folders + 33 loose objects at the prefix root | `SAMG:5358 read_scores` | `lib/research/scores/run_scores.py:run` (:307-341) | Run by hand | Internal (crosswalk + model block + peers). Peers V is structurally ABSENT (`run_scores.py:39-59`). **Served on /thesis but not drawn** |
| O-14 | `POOL bloomberg/harvest/bronze/segments/...` | `lib/research/api/segment_table.py:20`, `:124-136` via `segment_served.serve_segment_table` (`SAMG:4331`) | `research_pulls.py` (:43) | **UNRESOLVED schedule.** Not traced to a .cmd/.ps1/.tf | Bloomberg BLPAPI |
| O-15 | `POOL bloomberg/harvest/bronze/refdata/...` (name fallback) | `SAMG:1321-1346 _refdata_name` | `lib/research/harvest/bloomberg.py:bronze_write` (:100-112), called by `model_block_pull.stage_pull` | Same as O-1 | Bloomberg BLPAPI |
| O-16 | Gold parquet, newest `date=` partition: `POOL amgt/harvest/gold/article_security_mention/date=<d>/*.parquet`, `.../chatter_daily/...`, `.../chatter_event/...`. Newest partition for both mention and daily is `date=2026-10-08` (s3 ls) | `SAMG:7174 _timeline_snapshot_rows` -> `lib/research/harvest/publication_gold.py:1145 _latest_gold_snapshot_rows_cached` (prefix from `store.table_prefix("amgt","gold",table)`) | `publication_gold.py:build_daily` (:1051-1066), the mention build (:1314) and the event build (:1338), through `write_gold` (:534-550) | **Run by hand** (`python -m lib.research.harvest.publication_gold build-daily`, :1814-1838). **No scheduler found** (UNRESOLVED; searched .ps1/.cmd/.sh/.tf) | Internal derivation from publisher silver articles, which are browser-harvested (bbg, wsj, barrons, sa) |
| O-17 | `POOL amgt/harvest/gold/chatter_window/date=<d>/...` (tone, voters). Newest `date=2026-10-04` | `lib/research/api/monthly_chatter.py:41-42` | `lib/research/harvest/window_tone.py:build_window` (:113-125) | Run by hand. **Scheduler UNRESOLVED** | FinBERT sentiment over the publisher articles |
| O-18 | `POOL bloomberg/harvest/bronze/price_history_px_last/date=<as_of>/{year_pull,daily_30d}.json`. Newest `date=2026-10-13` | `lib/research/price/price_history.py:147 timeline_price_loader`; bucket from `naming.address` (:54-56) | `integrations/bloomberg/research/price_series_persist.py:run_daily_window_step`, called from `price_axis_pull.py:497-499` | Same Windows task as the O-2 PRICE leg (`OPAL_BBGTML_daily_pull`) | Bloomberg BLPAPI PX_LAST |
| O-19 | DynamoDB `MTAB` `WATCHLIST#<firm_id>` rows | `SAMG:6091 read_starred` -> `lib/research/watchlist/store.py:list_starred` (TABLE :43) | `watchlist/store.py:star`/`unstar` (:71-93) | The same Lambda on `POST /watchlist/{star,unstar}`. **No portal caller** | User action |
| O-20 | `POOL amgt/harvest/state/freshness_snapshot/current/snapshot.json` (1,221,162 bytes, written 2026-10-14 12:30Z) | `SAMG:6593 serve_coverage_freshness` -> `lib/research/freshness/snapshot.py read_freshness_snapshot` | `snapshot.py:write_freshness_snapshot` (:58-73) via `SAMG:6621 refresh_freshness_snapshot` | EventBridge Scheduler `amgt-global-freshness-snapshot-daily`, `cron(30 12 ? * MON-FRI *)` UTC, invoking `opal-amgt-scoped-api` (`freshness-snapshot-schedule.tf:100-119`) | Internal projection. It reads `universe/v1`, Bloomberg bronze, Seeking Alpha job records, Bright Data SERP bronze, `packs/` ledgers and the dossier listing (`SAMG:6444-6576`) |
| O-21 | `POOL universe/v1/<date>.json`, newest. 3 objects; newest `2026-10-06.json` | `SAMG:6381 read_universe` (freshness only); `crosswalk.py:1034` | `lib/research/identity/build_universe.py:union_main` (:973-1035) | Run by hand (`--write-pool`) | Union of the ETF holdings plane (`s3://opal-data-etfs/gold/holding/`), the crosswalk and SEC `company_tickers` |
| O-22 | `POOL packs/<key>/input_ledger.json`, `packs/<key>/status.json`. 105 key folders | `SAMG:6633 read_input_ledger` (`/ledger`; the overlay's `input_provenance` reaches it through the freshness snapshot's pack column) | `lib/research/ledger/ledger.py:record_run` (:107). `status.json` comes from the `pull_enqueue` Lambda and `pull_consumer._write_status` | Side effect of `model_block_pull.stage_pull` (class `market_data`) and `integrations/seekingalpha/rest_fetch.py` (class `sa`) | Bloomberg and Seeking Alpha run metadata |
| O-23 | `POOL seeking-alpha/harvest/state/job_record/...` (238 objects per the snapshot) | `lib/research/freshness/collector_read.py:seeking_alpha_by_security` | `lib/opal_data_harvest/job_record.py:write` (:112-123) from `worker.py` (:999-1023) | Windows task "Opal Data Harvest - Continuous Cycle", AtLogOn (`install-cycle-schedule.ps1`) | Seeking Alpha collector run metadata |
| O-24 | `POOL bright-data/harvest/bronze/serp/...` | `SAMG:6356 _bright_data_serp_stamps` (freshness) | `lib/research/harvest/bright_data_serp.py:harvest_serp` (:81) | **No production caller.** The module says "wired into nothing" (:19-24) | Bright Data SERP. **Measured absent:** `s3 ls bright-data/harvest/bronze/` shows no `serp/` prefix, and the snapshot reports `bright_data_serp_objects_listed: 0` |
| O-25 | Packaged `lib/research/lists/data/*.json` (in the Lambda zip, not S3) | `SAMG:6788 read_list_register` | Hand-edited repo files | Packaged at build | n/a |

## THE TABLE -- one row per (tab, component, field group)

The backend column names the function in `SAMG` that the route calls (handler arm line, then reader
line). The served-object column cites the O-n index above, which carries the producer, deploy shape and
upstream source.

### Header / top band

| Tab | Component (file:line) | Fields shown | Frontend route | Backend function (SAMG) | Served object(s) | Upstream |
|---|---|---|---|---|---|---|
| Header | `SA/components/SecurityOverlay.tsx:242-284` (`IdentityHeader`, mounted `SA/SecurityAnalysis.tsx:134`) | Company name `overlay.display_name`; ticker label `identity.display_ticker/requested/identity_status`; "identity as of" `identity.crosswalk_vintage`; sector and country from `header_figures[]`; Bloomberg session badge `bloomberg_session_state` (a hardcoded `"UNKNOWN"`, `SAMG:4100`) | `GET /security/{key}/overlay` (`API.ts:141`; `useSecurityOverlay`, `SA/hooks/useLeadPanelApi.ts:128`) | Handler :7730 -> `read_security_overlay` :3946; `resolve_identity` :3649; `_overlay_name` :1008; `_header_figures` :2869 | O-4 (identity), O-1 (header scope figures, including GICS/country mnemonics), O-15 (name fallback) | Bloomberg BLPAPI (model block); crosswalk (internal + Bloomberg identity) |
| Header | `SA/components/SecurityOverlay.tsx:286-325` (`identityDescriptionLine` :125) | One-line description: `top_band.description_line`, else the first sentence of `description.text`, else AI fill `thesis.ai_fill.blocks.identity_description` | overlay + `GET /security/{key}/thesis` (`API.ts:148`) | `read_description` :5827, in priority order: (1) model-block header `CIE_DES`/`CIE_DES_BULK`; (2) the first `company_description` sentence of the drafted document that passes the describes-the-business test; (3) ABSENT. `_overlay_top_band` :3880 -> `lib/research/api/top_band.py`; `read_ai_fill` :3571 | O-1, O-6, O-9 (held, so ABSENT) | Bloomberg CIE_DES; LLM drafting over SEC filings; LLM AI fill (held) |
| Header | `SA/components/HeaderCards.tsx:143-205` (mounted `SecurityOverlay.tsx:336`); format helpers from `StatTile.tsx` | Seven tiles: price, market cap, EV, net debt, beta, average volume, short interest. Each carries `header_figures[].{mnemonic,value,unit,currency,vintage,source,basis,reason}` | overlay | `_header_figures` :2869 (`HEADER_SEVEN` :2822); check face `lib/research/checkface/run_checks.check_block` (:4047-4049) | O-1 (header scope) | Bloomberg BLPAPI |
| Header | `SA/components/CardFooter.tsx:174` (at `SecurityOverlay.tsx:338`) | "date \| Source" from `header_figures[].vintage/source` | overlay | same | O-1 | Bloomberg |
| Header | `SA/components/SecurityOverlay.tsx:342-351` | "Chatter (this month)": `collected.rows[key].by_month[last].collected` | `GET /lead-panel/timeseries/collected/chatter` (`API.ts:104`; `useCollectedChatter`, `useLeadPanelApi.ts:91`) | Handler :7586-7606 -> `lib/research/api/monthly_chatter.py:read_monthly_chatter` | O-16 (chatter_daily `articles_total`; mention rows), O-5 listing (row set = covered names), O-17 (tone), O-3, O-2 (places moved) | Browser-harvested publisher articles (internal derivation) |
| Header | `SA/components/SecurityOverlay.tsx:352-365` | Breakout (price): `axis_reads[BREAKOUT,PRICE].row.{rank,pct_jump_pct,window_days,places_moved}`, else `absent_reason`/`point_status` | overlay | `read_security_overlay` :3991-4035 -> `read_point_record` :1692 (GetItem on the generation partition named by the `_CURRENT` pointer); `_join_places_moved` :1415 | O-2 (`BREAKOUT_PRICE#<date>`) | Bloomberg BLPAPI PX_LAST (`price_axis_pull`) |
| Header (TopBand) | `SA/components/TopBand.tsx:19` (returns null, never mounted; DEAD) | Nothing drawn. `top_band.{day,items_reason,items_without_link,social}` is served but unused | overlay | `_overlay_top_band` :3880 | O-16 (mention rows) | -- |
| Below header | `SA/components/CoverageNote.tsx:17-25` (mounted `SecurityAnalysis.tsx:163`) | "We do not cover this company" sentence: `research_coverage.{sentence,status}` | overlay | `_research_coverage` :3919 -> `covered_universe.covered_security_keys` -> `lib/research/api/coverage_marker.py` | O-5 (folder listing) | Internal |
| Below tabs | `SA/components/InputProvenance.tsx:49-70` (mounted `SecurityAnalysis.tsx:183`) | "About this data": `thesis.input_provenance[].{input,source,last_run,outcome,reason,form,filing_date,used_for[]}` | thesis | `read_thesis_bundle` :4338 -> `inputs_statement.statement(_overlay_input_provenance :3931)` -> `serve_coverage_freshness` :6593 | O-20 (which itself projects O-21, O-15/bloomberg bronze, O-23, O-24, O-22) plus O-6 provenance | Mixed vendor clocks |
| Page end | `SA/SecurityAnalysis.tsx:189` (`servedPageDate` :62) | Data-as-of day: `overlay.price.as_of_date`, else `axis_reads[].as_of_date` | overlay | `read_point_record` | O-2 (`TRENDING_PRICE#`) | Bloomberg |
| Not found | `SA/SecurityAnalysis.tsx:99-132` (`SA/notFound.ts`) | Candidate names from the overlay 404 body | overlay (error path) | Handler :7666-7729: `_covered_key_known` :1092 and `name_search.resolve_query`; `_covered_no_block_record` :1116 | O-5 listing, O-4 | Internal |
| Header actions | `SA/components/PrintExportAction.tsx:53-140` (mounted `SecurityAnalysis.tsx:96`) | PDF preview; `.md` export | `GET /security/{key}/print` and `?format=rich` (`API.ts:259`, `:276`; raw fetch, no hook) | Handler :7745 -> `_print_pack` :7831 -> `lib/research/print/render_pack.py build_pack` / `build_rich_text` (re-reads thesis, peers, posture, description) | O-1, O-6, O-7, O-10, O-12, O-5, plus the `packs/_template/` docx (writer UNRESOLVED) | As the tabs |

### Lead Panel (universe mode)

| Tab | Component (file:line) | Fields shown | Frontend route | Backend function (SAMG) | Served object(s) | Upstream |
|---|---|---|---|---|---|---|
| Lead Panel, Price face | `SA/components/PriceBars.tsx:124` (bars :172-260; mounted `LeadPanel.tsx:543`) | One bar per name: `rows[].{display_name,name,return_30d_pct,places_moved(_reason),classification,security_key,window_days}`, `ranking_status/reason` | `GET /lead-panel/rankings/trending/price?limit=500&days=` (`API.ts:67`; `useLeadPanelRankings` `useLeadPanelApi.ts:49`, enabled only on PRICE) | Handler :7560-7583 -> `read_rankings` :1538 (days 30), or `read_window_rankings` :1613 (90/365) -> `rolling_windows.price_window_not_produced` if absent. Names joined through `_join_classification` :825, `_fill_names_from_crosswalk` :1236, `_fill_names_from_model_block` :1390, `_refdata_name` :1325 | O-2 (`TRENDING_PRICE#<date>` generation), O-2w (90D/365D), O-3, O-4, O-1, O-15 | Bloomberg BLPAPI PX_LAST |
| Lead Panel, Price face | `SA/components/LeadPanel.tsx:202-220` (`SourceCaption`, mounted :572) | Generation line: `ranking.{generation_id,state,coverage_vintage,generation_row_count,as_of_date,requested_as_of,dated}` | rankings | `generation_fields` :479 | O-2 `_CURRENT` pointer | Internal |
| Lead Panel, Chatter face (default) | `SA/components/ChatterBubbles.tsx:609-750` (via `LeadPanel.tsx:390-420`) | Bubbles: radius `articles_total` / `by_month[*].collected`; label `display_name`; fill `tone` with `voters`; hover `ticker,classification,places_moved`; window caption; footer `as_of,source` | `GET /lead-panel/timeseries/collected/chatter?days=30\|90\|365` | Handler :7586-7606 -> `monthly_chatter.read_monthly_chatter(days)` | O-16, O-17, O-5 listing (row denominator), O-3, O-2 | Browser-harvested publisher articles; FinBERT tone |
| Lead Panel footer | `SA/components/CardFooter.tsx:198-200` (at `LeadPanel.tsx:578`) | Price: `ranking.as_of_date`, `rows[].source`. Chatter: `collected.as_of/source` | rankings / chatter | as above | O-2 / O-16 | -- |
| Lead Panel "Starred only" | `SA/components/LeadPanel.tsx:470-479` (toggle :512) | Filters to `StarredEntry[].ticker` | `GET /watchlist` (`API.ts:112`; `useStarredList` `useLeadPanelApi.ts:103`) | Handler :7617 -> `read_starred` :6091 -> `watchlist/store.list_starred` | O-19 | User action. **No star/unstar control on the page** (`useSetStarred` has no caller) |
| StarredList / RankedList / RankedChart / timeseries | `SA/components/StarredList.tsx:75`, `RankedChart.tsx:143`, `RankedList.tsx:181` -- **DEAD (no importer)** | -- | `GET /lead-panel/timeseries/{m}/{s}` (`getRankTimeSeries`) has no live caller | `read_rank_series` :1909 (BatchGetItem) | O-2 | -- |

### Tabs

| Tab | Component (file:line) | Fields shown | Frontend route | Backend function (SAMG) | Served object(s) | Upstream |
|---|---|---|---|---|---|---|
| Thesis | `SA/tabs/ThesisTab.tsx:111-213` (`ResearchTeamPillars`) | `dossier_fields.thesis_pillars[].{pillar,text,terms[],citation}` | thesis (`useThesisBundle` `useLeadPanelApi.ts:138`) | Handler :7737 -> `read_thesis_bundle` :4214 -> `_dossier_fields` :5607 | O-5 | Opal research reports (internal) |
| Thesis | `SA/components/AiFillBlock.tsx:150` (at `ThesisTab.tsx:121/150`) | `ai_fill.blocks.thesis_pillars` | thesis | `read_ai_fill` :3571 | O-9 (**held: ABSENT for every name**) | LLM + web search |
| Thesis | `SA/components/DossierSections.tsx:29` (at `ThesisTab.tsx:313`) | `dossier_sections[].{field,heading,status,text,reason,citation}` | thesis | `lib/research/api/dossier_sections.py` over the dossier read (:4280) | O-5 | Internal |
| Thesis | `SA/tabs/ThesisTab.tsx:300` header, `:314` empty state | `drafting_provenance.{form,filing_date}`, `drafting_source`, `generated_at`, `drafting_status/reason/read_completed`, `drafting_reason_held/newer*` | thesis | `read_drafted_sections` :3265 (`_read_drafting_document` :3031); ABSENT reason from `_read_filing_source_object` :4115 / `_apply_filing_attempt_held_state` :4178 | O-6, O-8 | LLM over SEC EDGAR |
| Thesis | `SA/components/SegmentTable.tsx:74` (at `ThesisTab.tsx:321`) | `segment_table.{status,reason,periods[],rows[].{segment,level,values[]},operating_income_rows,currency_note,period_note,source}` | thesis | `:4331 segment_served.serve_segment_table` -> `segment_table.read_segment_table` (`lib/research/api/segment_table.py:20,124`) | O-14 plus O-1 (revenue and currency) | Bloomberg BLPAPI segments |
| Thesis | `SA/components/SegmentBreakdown.tsx:37` (at `ThesisTab.tsx:322`) | `segment_breakdown.{rows[].{segment,text,cite,segment_reason},reason,source}` | thesis | `read_segment_breakdown` :4412 | O-7 | LLM over SEC EDGAR |
| Thesis | `SA/components/ThesisDriverChart.tsx:80` + `PassageTable.tsx:20` (only when drafting is SERVED) | `thesis_driver_chart.{status,source,driver_series,mnemonic,points[].{fiscal_year,value,passage_*}}` | thesis | `thesis_driver_chart` :4499 (`_point_passage` :4475) over `fiscal_year_figures` | O-6 (`thesis_driver`), O-7 (passages), O-1 (fiscal figures) | LLM + Bloomberg |
| Thesis | `SA/components/ThesisCards.tsx:510-556` (cards :39; `TeamCases` :165; `CheckFaceBadge` :314) | `drafted_sections[].{section_id,label,sentences[].{text,evidence[],verbatim_check}}`; company description; `model.team_cases.{base,upside,downside}` | thesis | `read_drafted_sections` :3265; `_team_cases` :5674 | O-6, O-5 | LLM over SEC; Opal research team |
| Thesis | `SA/tabs/ThesisTab.tsx:335-344` | `held_uncited_count/basis`; footer `generated_at`, filing date and form | thesis | `_held_uncited` :3216 | O-6 | -- |
| Thesis (passage coverage) | served at `SAMG:4335`; no named renderer in the table above | `passage_coverage` | thesis | `lib/research/filings/section_coverage.py:134` | O-7 | -- |
| News | `SA/components/HeaderBrief.tsx:290-300` (`FeedList` :221-276; at `SA/tabs/NewsTab.tsx:43`) | Merged list: `top_band.items[].{title,url,publisher,published_utc,mentions}` + `feed.items[].{article_key,title,url,publisher,published_at,mentions}`; `feed.{coverage_status,store_item_count,window,reason,social.status}` | overlay | `read_feed` :5975 and `_overlay_top_band` :3880 (one read shared via `rows_sink`), both through `_timeline_snapshot_rows("article_security_mention")` :7174 | O-16 (`article_security_mention`, 30-day window) | Browser-harvested publisher articles. Social is "no source measured (S13)" (:4761) |
| News | `SA/components/HeaderBrief.tsx:191` (`FeedTermFilters`, terms :184; at `NewsTab.tsx:32`) | Filters by `dossier_fields.thesis_pillars[].terms[1:]` | thesis | `_dossier_fields` | O-5 | Internal |
| News | `SA/components/TimelinePanel.tsx:523-719` (at `NewsTab.tsx:45`) | Bars `series[].articles_total` (z-score days marked); price line `price_series[].{date,close}` / `price_series_reason`; events `events[].{first_day,last_day,lead_headline}`; `floor_date`; tooltip `publishers_distinct, mention_count_total` | `GET /security/{key}/timeline` (`TimelinePanel.tsx:163`, `useTimelineRange` :175; own `apiRequest`) | Handler :7630-7637 -> `_serve_timeline` :7383 -> `lib/research/harvest/timeline_api.get_timeline` with `_timeline_daily_loader` :7204, `_timeline_event_loader` :7214, `price_history.timeline_price_loader` | O-16 (`chatter_daily`, `chatter_event`), O-18, O-4 (key -> Bloomberg ticker) | Publisher articles; Bloomberg PX_LAST |
| News | `SA/components/TimelinePanel.tsx:468-513` (`DayDissection`) | `articles[].{headline,publisher,published_utc,published_precision,mention_count,mention_in_title,mention_in_lead,signal_tier}`, `data_status` | `GET /security/{key}/timeline/day/{date}` (`TimelinePanel.tsx:166`, `useTimelineDay` :185) | `_serve_timeline_body` :7413 -> `get_timeline_day` with `_timeline_article_loader` :7218; `_day_origin_applied` :7433 | O-16 (`article_security_mention` + `chatter_daily`) | Publisher articles |
| News | `SA/components/TimelineWordCloud.tsx:59-109` (at `TimelinePanel.tsx:704`) | `range.word_cloud.{terms[].{term,count},window,reason}` | timeline | `_word_cloud_block` :7327 (counted at request time from mention titles) | O-16 | Publisher headlines |
| Exec Management | `SA/tabs/ExecManagementTab.tsx:382` (`ResearchTeamManagement`, mounted :471) | `dossier_fields.management.{value,citation,reason,status}`; AI fill `mgmt_team_view` | thesis | `_dossier_fields` :5607; `read_ai_fill` | O-5; O-9 (held) | Opal research; LLM |
| Exec Management | `SA/components/AiFillBlock` at `ExecManagementTab.tsx:473-474` | `ai_fill.blocks.mgmt_bio`, `.mgmt_recent` | thesis | `read_ai_fill` :3571 | O-9 (**held**) | LLM + web search |
| Exec Management | `SA/tabs/ExecManagementTab.tsx:248-368` (`ManagementBody`, mounted :480; `OfficerRow` :143; `CeoProfile` :188; `poolLine` :169) | `management.officers[].{name,role,role_start,tenure_years,profile_url,enrichment,source,confirmed}`; `management_status, roster_source/status/reason, avg_tenure_years, pool_avg_tenure_years, pool_denominator, lusha_enrichment, ceo_profile_reading, ceo_public_profile` | thesis | `read_management` :5138 -> `_serve_management_document` :5177; `_with_exec_roster_chain` :5082 (`exec_roster_chain`: filing -> notes -> stored Bloomberg); pool average `read_pool_object(MANAGEMENT_PREFIX,"_pool")` :5291; `ceo_profile_reading` :4912 | O-11; chain legs `sec/harvest/silver/filing_source/` (O-4 note), O-5 notes, `bloomberg/harvest/bronze/exec_officers/` | SEC filings, Lusha, Bright Data SERP, Bloomberg officers |
| Exec Management | `SA/components/CardFooter.tsx:179` (at `ExecManagementTab.tsx:483`) | `management.as_of`, `management_read.as_of`, `roster_source`, `officers[].source` | thesis | same | O-11 | -- |
| Peers | `SA/tabs/PeersTab.tsx:139-364` (`CscBody`, mounted :409; `BasisChip` :124; `SA/cscTable.ts`) | `peers.members[]`, `csc_columns.{columns,present[],absent[]}`, `basis,test,universe_vintage,as_of`, `subject.{cross_vintage_caveat,market_cap_vintage}` | `GET /security/{key}/peers` (`API.ts:154`; `usePeerSet` `useLeadPanelApi.ts:148`) | Handler :7739 -> `read_peer_set` :2387, then `_with_numeric_tickers` :2478, `_with_listed_identity` :2507, `_with_price_currency` :2546, `_with_subject_cap` :2607, `_with_member_display_names` :2655, `_with_reason_classes` :2688 | O-10 (+ O-1 subject cap, O-5 listing via `_held_name_index` :2443) | Internal (Security Scanner universes, model block, Seeking Alpha candidates) |
| Peers | `SA/tabs/PeersTab.tsx:148-160` (subject row) | Subject price, cap and EV from `overlay.header_figures[]`; `overlay.display_name` | overlay | `_header_figures` | O-1 | Bloomberg |
| Peers | `SA/tabs/PeersTab.tsx:390-407`, footer :415 | `peers.reason`, `peer_read.status/as_of`, `vintage`, `members[].cap_source` | peers | `read_pool_object` :2293 record | O-10 | -- |
| Model | `SA/tabs/ModelTab.tsx:595-659` (`ModelSummary`), `:703-945` (`ModelBody` grid), `CheckFaceBadge` :155 | `model.fiscal_year_figures[]`, `fiscal_years`, `model.line_names`, `model.forecast_figures`, `fiscal_unresolved`, `forecast_withheld`, `model.team_sheet.*`, `fiscal_currency_by_mnemonic`, `check_face[]`, `model_status` | thesis | `read_model` :5739 (fiscal + forecast scopes); `_model_line_names` :5515; `_team_sheet_from_dossier` :4201; `check_block` :4253-4255 | O-1 (fiscal/forecast BEST_*), O-5 (`team_sheet`) | Bloomberg BLPAPI; Opal research team sheet |
| Model | `SA/tabs/ModelTab.tsx:449-514` (`TeamBase`/`TeamCase`) | `model.team_cases.{base,upside,downside}.{table,citation,unit_as_written}` | thesis | `_team_cases` :5674 | O-5 | Opal research team |
| Model | `SA/tabs/ModelTab.tsx:953-994` (`ModelVersions`) | `versions.versions[].stamp`, `versions.read.{status,reason}` | `GET /security/{key}/versions` (`API.ts:166`; `useModelVersions` `useLeadPanelApi.ts:169`) | Handler :7757 -> `read_model_block_versions` :6870 (list only) | O-1 (every stamp under `derived/model_block/<key>/`) | Bloomberg |
| Model | `SA/components/model/WhatChangedPanel.tsx:561` (`PairFace` :415-518, `DefaultPair` :522-556) | `compare.denominators.{added,removed,changed}`; `compare.compared.changed[].{figure,mnemonic,fiscal_year,scope,from,to}`; `compare.reason` | `GET /security/{key}/compare?from&to` (`API.ts:172`; `useModelCompare` `useLeadPanelApi.ts:191`, probed repeatedly) | Handler :7765 -> `compare_model_blocks` :6917 | O-1 (two stamps) | Bloomberg |
| Model | `SA/tabs/ModelTab.tsx:1000-1021`, footer :1051 | `generated_at`; `model.generated_at`; `fiscal_year_figures[].vintage/source` | thesis | `read_model` | O-1 | -- |
| Model, input ledger | **Not rendered** (`useInputLedger` :180 has no caller) | -- | `GET /security/{key}/ledger` not called | `read_input_ledger_served` :6772 | O-22 | -- |
| Model, scores | **Served, not drawn** (`thesis.scores`; only a comment at `ModelTab.tsx:21-22`) | -- | thesis | `read_scores` :5358 | O-13 | -- |
| Posture | `SA/tabs/PostureTab.tsx:567-636` (`FundOfRecordLine`, mounted :691) | `dossier_fields.fund_of_record.{status,value,citation,reason}`, `last_stated_position.value.text` | thesis | `_dossier_fields` :5607 | O-5 | Opal research reports |
| Posture | `SA/tabs/PostureTab.tsx:384-496` (`ServedPosture`; verdict tile :409-462) | `posture.{verdict,comparable,comparable_name,comparable_identity,as_of,marked,generation.*,reason}`; link to the comparable | thesis | `read_posture` :5442 (`read_pool_object(POSTURE_PREFIX)` :5450; `_foreign` guard :2371) | O-12 | LLM (`claude-opus-5`) |
| Posture | `SA/tabs/PostureTab.tsx:247-292` (`CoverageSection`) | `posture.packs[key].{counts,absent[]}` | thesis | `read_posture` | O-12 | LLM evidence packs |
| Posture | `SA/tabs/PostureTab.tsx:347` (`ClaimCard`), `:312` (`CiteLine`); `SA/postureCites.ts:235` | `posture.basis[].{claim,cites[]}`, resolved against `posture.{membership,fit,packs}` and the subject's and comparable's thesis and peers bundles; `cites_validated/total` | thesis x2 + peers x2 (subject + comparable; `PostureTab.tsx:639-648`) | `read_thesis_bundle`, `read_peer_set` | O-12, O-6, O-10 (both names) | -- |
| Posture | `SA/tabs/PostureTab.tsx:505-551`, footer :703 | `posture.status/reason`, `posture_read.as_of`, `generation.generated_at`, `marked` | thesis | `read_posture` | O-12 | -- |

### Freshness / coverage

| Surface | Component | Route | Backend | Served object | Note |
|---|---|---|---|---|---|
| Freshness (separate page, not /security-analysis) | `portal/src/pages/Freshness/Freshness.tsx:23,31` | `GET /freshness?view=page` (`API.ts:240`) | Handler :7781-7797 -> `serve_coverage_freshness` :6593 + `page_body.page_view`, `stale_rule.annotate_row`, `owner_line.lists_statement(read_list_register())` | O-20, falling back to the live compute `read_coverage_freshness` :6444; O-25 | On this page it reaches the user only as `thesis.input_provenance` |
| Coverage tab (retired) | none; `useCoverageSet` :158 has no caller | `GET /security/{key}/coverage` not called | `read_coverage_set` :4643 -> `pool_reader.coverage_items` | `POOL publication-links/v1/`, `publications/v1/` | Producer `lib/opal_data_harvest/catalog.py:Catalog.store` + `uploads.py:Uploader.run`. Windows tasks "Opal Data Harvest - Continuous Cycle" / "Local Publications" |
| `/resolve`, `/lists`, `/refresh` | none on this page | -- | :7805, :7799, (`/refresh` is not in the route table) | O-4, O-25 | `requestRefresh` has zero callers; `/refresh` is not mounted |

---

# Part 2 -- Current schedule of each surface (DESIRED vs APPLIED, last success, as-of vs frontier)

## Frame

- Trading-day frontier (T-1): `lib/trading_calendar.py:191` `prev_trading_day(2026-10-14)` = **2026-10-13**
  (`expected_last_trading_day` = 2026-10-14, calendar source NYSE/pandas_market_calendars).
- POOL bucket: `pool_reader.POOL_BUCKET` = `opal-data-harvest` (`lib/research/coverage/pool_reader.py:73`).
  New-grammar prefixes are in `lib/research/api/_harvest_prefixes.py` (generated):
  ai_fill `amgt/harvest/gold/ai_fill/`, Bloomberg bronze `bloomberg/harvest/bronze/`, SA bronze
  `seeking-alpha/harvest/bronze/`, SERP `bright-data/harvest/bronze/serp/`, filing attempt `amgt/harvest/state/filing_attempt/`.
  Dossier: `amgt/harvest/gold/research_dossier/` (`lib/research/corpus/dossier.py:142,1561`).
- Live trigger census: `comp-trigger --list` = 155 EventBridge rules + 34 Scheduler schedules (one group, `default`).
  **Only two AWS triggers touch this surface**: `amgt-resapp-chatter-axis-daily` and `amgt-global-freshness-snapshot-daily`.
  Everything else that feeds the page is fired from a Windows Task Scheduler task on a Bloomberg/site-Z box, or by hand.
- comp-freshness `--list` has NO harvest/amgt entry. The graph manifest has no schedule-by-prefix query; comp-which routed to
  comp-trigger (used). comp-schedule is a gate ledger (not schedules).
- Box tasks: `Get-ScheduledTask` on this laptop (host ANDREW) shows none of them, so the box-side tasks' APPLIED state is
  **UNREAD from here**. Below, "observed firing" = write-time histogram of the produced objects (effect, not task state).

## Table

| store/prefix | producer (writer file:line) | DESIRED trigger | APPLIED trigger | last success (UTC) | as-of served vs frontier 2026-10-13 | daily? |
|---|---|---|---|---|---|---|
| DDB `opal-harvest-security-metrics` CHATTER axes (TRENDING_/BREAKOUT_CHATTER, `_CURRENT` pointers) | Lambda `amgt-resapp-chatter-axis` -> `lib/research/metrics/chatter_axis.py` | Scheduler `cron(0 10 * * ? *)` UTC, ENABLED, `infra/aws/terraform/harvest/chatter-axis-schedule.tf:235-238` | ENABLED `cron(0 10 * * ? *)` UTC -> amgt-resapp-chatter-axis (`scheduler get-schedule`) | pointer 2026-10-14T10:00Z, run R20261014T100006Z; log `OK: chatter axis as_of=2026-10-14 source=legacy ... rows_written=0` | as_of 2026-10-14 (run-date convention, AT/AHEAD of frontier) **but state=EMPTY, row_count=0** on 10-09, 10-12, 10-13 and 10-14; universe vintage frozen at `universe/v1/2026-10-06.json`. `CHATTER_AXIS_SOURCE="legacy"` (`chatter-axis-schedule.tf:72`) | DAILY (fires; serves empty) |
| DDB same table, PRICE axes (TRENDING_/BREAKOUT_PRICE) | `integrations/bloomberg/research/price_axis_pull.py` (subject registry `lib/research/metrics/movement_gate.py:196-198`) | PRICE LEG of Windows task `OPAL_BBGTML_daily_pull` (`integrations/bloomberg/pipeline/scheduled_daily_pull.cmd:351-388`), daily `-At 07:00` local (`register_daily_task.ps1:32,62`). Not its own schedule by design (`.cmd:319-323`) | Bloomberg box task: UNREAD from laptop. Observed firing: pointers written 2026-10-12T11:03Z, 10-13T14:40Z, 10-14T11:07Z | 2026-10-14T11:07Z, state COMPLETE, 94 rows (gen 20261014T110715Z) | as_of **2026-10-13 = frontier** (0 trading days behind). as_of 10-14 ABSENT (correct for T-1) | DAILY (box-side, rides models chain; skipped if DAPI down, rc 50) |
| DDB `etf-classifications` (GetItem by ticker) | (a) BD E_18 `detect_new_securities.py` via `etf_classification_scheduled.write` (conditional put, `infra/aws/terraform/bd-pipeline/iam.tf:727-733`); (b) Lambda `mdpf-secclass-new-security-lambda` | (a) EventBridge `bd-canonical-prices-daily` `cron(0 4 * * ? *)`; (b) Scheduler `cron(0 10 ? * MON-FRI *)` America/New_York, `infra/aws/terraform/mdpf-secclass/new-security-classifier/schedule.tf:47-51` | (a) ENABLED `cron(0 4 * * ? *)` -> bd-gold-trigger (`events describe-rule`/`list-targets-by-rule`); (b) ENABLED as declared (`scheduler get-schedule`) | (b) 2026-10-14T14:00:25Z `run_date=2026-10-14 ... written: 1, present: 3`; table ItemCount 11,362 | Insert-only reference table (no as-of); current through today | DAILY |
| `peers/v1/` | `lib/research/peers/engine.py:1184-1189` (`python -m lib.research.peers.engine`) | NONE found: no TF rule, no Task Scheduler script names the module | NONE in live census | 2026-10-11T11:23Z (n=1,727 objs; write days 09-15,16,17,24,30, 10-02, 10-11) | newest per-name as_of 2026-10-11 for 243/245 names -> **1 trading day behind** (10-12, 10-13 missed) | AD-HOC |
| `management/v1/` | `lib/research/management/enrich.py:1190` via `lib/research/management/batch` / `run_batch.cmd:12` | `run_batch.cmd:6` says "the scheduled task that calls this is created DISABLED: activation is Andrew's word"; no registration script exists | NONE | 2026-10-02T19:44Z (n=25, 18 names) | as_of stamp 2026-10-02T1840Z -> **7 trading days behind** | AD-HOC |
| `posture/v1/` | `lib/research/posture/judge.py:298-303` | NONE | NONE | 2026-10-02T08:34Z (n=35) | key as_of 2026-09-16 (31 names) / 09-15 (2) -> **~19 trading days behind** | AD-HOC |
| `scores/v1/` | `lib/research/scores/run_scores.py` (via `crosswalk.write_pool`, `lib/research/identity/crosswalk.py:1533`) | NONE | NONE | 2026-09-30T15:15Z (n=70) | as_of 2026-09-17 -> **~18 trading days behind** | AD-HOC |
| `derived/model_block/` | `integrations/bloomberg/research/model_block_pull.py:668` (`cmd_admit` :2256, `cmd_refresh` :2366) | Windows task `amgt-induction-daily` (name = `opal_naming.name("amgt",None,"induction","daily")`), `lib/research/corpus/schedule_induction.ps1:43,167` daily `-AtUtc 13:00`; steps induction -> admit -> refresh (`lib/research/corpus/induction_scheduled.py:1-20`) | site-Z task: UNREAD from laptop. Observed: 96 objects at 13:xxZ every day 10-07..10-12 and 10-14; **10-13 missing** (project.json:60: induction rc 4 when Terminal sign-in absent) | 2026-10-14T13:18:12Z (n=2,134) | pull stamp 2026-10-14 (>= frontier) | DAILY (box-side; fails silently-as-rc when Terminal not signed in) |
| `packs/` (input_ledger.json) | `lib/research/ledger/ledger.py:89` (called from model_block_pull `record_run`, :863); on-demand `packs/<key>/status.json` by box-side SQS consumer `integrations/bloomberg/research/pull_consumer.py` (`infra/aws/terraform/harvest/sqs.tf:7-18`) | rides `amgt-induction-daily` (above) + on-demand queue | as above; queue consumer UNREAD | 2026-10-14T13:18:10Z (n=106; 96 written 10-14) | ledger stamp 2026-10-14 | UPSTREAM-ONLY (rides induction) |
| `drafting/v1/` | `lib/research/drafting` (pool writer `crosswalk.write_pool`; adapter `scoped_amgt.py:2955-2957`) | NONE | NONE | 2026-10-11T13:12Z (n=12) | 3 names refreshed 10-11; rest 09-30..10-09 -> **>=1 trading day behind** | AD-HOC |
| `filings/v1/` | `lib/research/filings/fetch.py:63` + `filings/batch.py` (`run_batch.cmd:9`, "created DISABLED", :6) | NONE (task never registered) | NONE | 2026-10-11T13:11Z (n=208: 196 source, 12 analysis) | filing-dated, event-driven; 196 sources from one 2026-09-17 batch | AD-HOC |
| `universe/v1/` | `lib/research/identity/build_universe.py:448,1079` | NONE | NONE | 2026-10-06T04:10Z (n=3) | `universe/v1/2026-10-06.json` -> **5 trading days behind**; also pins the chatter axis's coverage vintage | AD-HOC |
| `amgt/harvest/state/filing_attempt/` | `lib/research/harvest/filings.py:326-356,405` | NONE | NONE | 2026-10-09T06:20Z (n=181; 180 written 2026-09-22) | state marker, no as-of | AD-HOC |
| AI-fill `amgt/harvest/gold/ai_fill/<key>/ai_fill.json` | `lib/research/aifill/store.py:57-66` via `python -m lib.research.aifill.run` (`run.py:3`) | NONE | NONE; **and the live Lambda env sets `AMGT_AIFILL_ROOT="/var/empty/aifill-hold"`** (`infra/aws/terraform/harvest/scoped-amgt-api.tf:517`) so the page serves ABSENT regardless | 2026-10-14T03:05-03:19Z, one batch, n=95 | written today but **NOT SERVED** (hold) | AD-HOC |
| Dossier `amgt/harvest/gold/research_dossier/` | `lib/research/corpus/dossier.py:1651` `write_one` (CLI `:2302`) | NONE | NONE | 2026-10-12T00:25Z (n=1,431) | newest as_of 2026-10-12 (74 names) / 2026-10-11 (21) -> **1-2 trading days behind** | AD-HOC (irregular batches 09-29..10-12) |
| Bloomberg bronze `refdata/`, `histdata/`, `bestdata/` | model_block_pull refresh | rides `amgt-induction-daily` | site-Z, UNREAD | 2026-10-14T13:18Z (refdata n=1,263) | 2026-10-14; **10-13 gap** (17 bronze objects that day vs ~294 normal) | UPSTREAM-ONLY (induction) |
| Bloomberg bronze `price_history_px_last/`, `price_history_tot_return/` | price_axis_pull (price leg) | rides `OPAL_BBGTML_daily_pull` | BG box, UNREAD | 2026-10-14T11:07Z | as_of 2026-10-13 = frontier | UPSTREAM-ONLY (rides models chain) |
| Bloomberg bronze `news_listing/`, `article/` | harvest cycle runner, publisher `bbg` (`lib/opal_data_harvest/cycle_runner.py:1-10`, PUBLISHERS :47) | Windows task "Opal Data Harvest - Continuous Cycle", `-AtLogOn`, no end (`lib/opal_data_harvest/install-cycle-schedule.ps1:3,51`) | site-Z; registered args `--publishers bbg wsj barrons --refresh-once` (`org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~ZW/round85/bz10_task.xml:77`); runner **stopped by operator 2026-10-13T23:53Z** (`.../round85/bz10_stopped.out`) | news_listing 2026-10-14T10:16Z; article 2026-10-13T16:59Z | continuous, not as-of | CONTINUOUS box process (logon-triggered; not a daily schedule) |
| Bloomberg bronze `identity/`, `exec_officers/`, `segments/`, `histdata_daily_px/` | add_security / management batch / segments run | NONE | NONE | identity 10-07T13:22Z; exec_officers 10-07T11:37Z; segments 10-07T14:59Z; histdata_daily_px 09-22 | 5 trading days behind (histdata_daily_px 15) | AD-HOC |
| Seeking Alpha bronze `symbol/`, `report/`, `analysis/`, `news/` (the four tables the freshness view reads, `scoped_amgt.py` `_SEEKING_ALPHA_BRONZE_TABLES`) | AMGT_HARVST SA publisher (lib/opal_data_harvest) | none for these four | NONE | 2026-09-22T04:54Z (3 objects each) | **~16 trading days behind** | AD-HOC (dead since 09-22) |
| Seeking Alpha bronze `article/`, `news_listing/` | cycle runner publisher `sa` | same AtLogOn runner | **`sa` is NOT in the registered `--publishers` list** (bz10_task.xml:77) | article 2026-10-12T12:06Z; news_listing 2026-10-12T12:01Z | stops at 10-12 -> 1 trading day behind and growing | NONE (de-registered) |
| Bright Data SERP bronze `bright-data/harvest/bronze/serp/` | builder home only (H5; `scoped_amgt.py` comment "0 objects at this vintage") | NONE | NONE | **0 objects** (list returned `None`) | ABSENT | NONE |
| (extra) freshness snapshot `amgt/harvest/state/freshness_snapshot/current/snapshot.json` | `lib/research/freshness/snapshot.py:34-70` via `scoped_amgt.refresh_freshness_snapshot` (:6621) | Scheduler `cron(30 12 ? * MON-FRI *)` UTC, `infra/aws/terraform/harvest/freshness-snapshot-schedule.tf:101-118` | ENABLED, same expr, target opal-amgt-scoped-api, input `{"amgt_scheduled_action":"refresh_freshness_snapshot"}` | 2026-10-14T12:30:45Z (1,221,162 bytes) | today | DAILY (weekdays) |
| (extra) `crosswalk/v1/` | `lib/research/identity/crosswalk.py:1533-1590` | NONE | NONE | 2026-10-09T17:20Z | `crosswalk/v1/2026-10-09.json` -> 2 trading days behind | AD-HOC |
| (extra) `amgt/harvest/gold/chatter_daily/` (pool_reader gold read) | `lib/research/harvest/publication_gold.py:534-550` | NONE | NONE | 2026-10-09T10:41Z (partition date=2026-10-08) | **3 trading days behind** | AD-HOC |
| (other) EventBridge `seeking-alpha-analysis-daily` / `-news-daily` | `infra/aws/terraform/seeking-alpha/main.tf:115-118,210-213` (no `state`, so DESIRED = ENABLED) | cron(0 21 *) / cron(0 14 *) | **DISABLED** live (comp-trigger census) -- DESIRED/APPLIED drift. Writes `opal-data-news-av`, NOT the harvest bucket, so it does not feed this page | n/a | n/a | n/a |

## Flags (not on a daily schedule, upstream-only, or by hand)

1. AD-HOC by hand, no trigger anywhere: peers, management, posture, scores, drafting, filings, filing_attempt state, universe,
   crosswalk, ai_fill, research_dossier, chatter_daily gold, Bloomberg identity/exec_officers/segments, SA symbol/report/analysis/news.
   The two `run_batch.cmd` launchers say their tasks are "created DISABLED: activation is Andrew's word"; no registration script exists.
2. UPSTREAM-ONLY: packs ledger and Bloomberg refdata/histdata/bestdata ride `amgt-induction-daily`; the price bronze rides the
   models chain of `OPAL_BBGTML_daily_pull`. Both are box-side Windows tasks whose APPLIED state cannot be read from the laptop.
   Both depend on a signed-in Bloomberg Terminal (induction rc 4 on 2026-10-13 -> no model block, no refdata that day).
3. NONE: SERP bronze is empty (0 objects); the SA article cycle is off because `sa` is not in the registered publishers list.
4. Daily but useless: the chatter axis fires every day at 10:00Z and commits EMPTY (0 rows) because its source is `legacy` and
   its universe is frozen at 2026-10-06. AI-fill is fresh (2026-10-14) but deliberately not served (Lambda env hold).
5. Only four AWS-native schedules touch this surface: chatter axis, freshness snapshot, secclass classifier, bd-canonical-prices-daily.

Commands (all read-only):

- `.tools/comp-trigger --list --budget 150` (census: 155 rules + 34 schedules); `aws scheduler list-schedule-groups` (only `default`).
- `aws scheduler get-schedule --name {amgt-global-freshness-snapshot-daily | amgt-resapp-chatter-axis-daily | mdpf-secclass-new-security-daily}`.
- `aws events describe-rule --name bd-canonical-prices-daily`; `aws events list-targets-by-rule --rule bd-canonical-prices-daily`.
- `aws dynamodb get-item --table-name opal-harvest-security-metrics --key '{"axis_date":{"S":"<AXIS>#<date>"},"ticker":{"S":"_CURRENT"}}'`
  for 4 axes x {10-09, 10-12, 10-13, 10-14}; `aws dynamodb describe-table --table-name etf-classifications`.
- `aws s3api list-objects-v2 --bucket opal-data-harvest --prefix <p> --query 'Contents[].[LastModified,Key]' --output text`
  (CLI auto-paginates; counted client-side with `grep -c`; raw listings saved beside this file as `ls_*.txt`).
- `aws s3api head-object --bucket opal-data-harvest --key amgt/harvest/state/freshness_snapshot/current/snapshot.json`.
- `aws logs filter-log-events --log-group-name /aws/lambda/{mdpf-secclass-new-security-lambda | amgt-resapp-chatter-axis} --start-time <2026-10-14T00:00Z>`.
- `Get-ScheduledTask` on this laptop (no harvest/BBG/induction task present -> box tasks UNREAD here).

---

# Part 3 -- How MDPF_DEMQUE accounts for each need

## Conclusion first

DEMQUE is a **file-based queue plus two ledgers. It has no DynamoDB table and no SQS queue.** By design it meters **Bloomberg and Yahoo only**. Of the AMGT page's needs, only **four one-off Bloomberg research requests** are queue rows (tier 4, surface D). **None of them has been drawn.**

The page's largest real Bloomberg draw, the **daily model-block refresh of 96 names**, bypasses the queue. It is written to the shared budget ledger **after the fact, with cells = null (claim `absent`)**, so it counts against no channel's ceiling or reserve. The 7:00 ET price-axis leg is not on the ledger at all. Seeking Alpha, Bright Data, SEC EDGAR and the LLM calls are out of DEMQUE's scope by contract.

The queue does **not** know the Security Analysis universe. No per-security daily demand exists for it.

## 1. What DEMQUE is

**Contracts:** `org/missions/D8/MDPF/MDPF_DEMQUE/prd/MDPF_DEMQUE_PRD.md`
- C-CELL: the unit is the cell, one row times one field (:139).
- C-METER: "Bloomberg and Yahoo only", with Bloomberg metered per channel (:143). Other vendors appear "only as named sources" (:107-108, :143).
- C-RESERVE: backfill allowance = CEILING - RESERVE - drawn today (:146-153).
- C-PRIORITY: tiers 1-5 (:155-159), research pages = tier 4.
- C-QUOTE: a request is priced before it draws (:161-162).
- Standing-request state object (:261-271).

**Queue store (APPLIED):** git-tracked JSON request files in `org/missions/D8/MDPF/MDPF_DEMQUE/requests/`.
- 16 requests plus `ENROLMENT_TIERS.json`.
- Each request has a frozen `*.quote.json` beside it.
- The drawer reads this folder: `data/mdpf/scripts/demque/standing_drawer.py:53` `REQUESTS_DIR = MISSION / "requests"`.
- The Yahoo daily draw reads its own local queue folder `$OPAL_DEMQUE_HOME|~/.opal/demque/queue` (`run_daily_draw.sh:9-10`) on the drawing Dell. That folder's contents are UNRESOLVED (another box).
- A Grep for `dynamodb|sqs` over `data/mdpf/scripts/demque/*.py` hit 2 files, both the SECCLASS sync (`secclass_sync.py` and its test, which write `etf-classifications`). Neither is a queue store.

**Request row schema:**
- `demand_queue.py:12-13,87-107` (Yahoo): `request_id, tier 1-5, reason, page, securities[{cusip,symbol}], fields, start, end`, optional `rank`.
- Round 9 adds `need_class` (client | non_client), `window_start` and `need_date`.
- Bloomberg rows also carry `vendor`, `channel` (reference | history | bql | model_block, `bbg_quote.py:87`), `filed_by`, `filed_for`, `authority` and `runs_at`. Example: `requests/AMGT_RESAPP-107a-ABNB-MODEL-BLOCK.json:1-30`.
- Refusal rules: 2012-01-01 floor; non-client limited to 365 days before need; one named exception, `research_app_model_history_2016`, for the AMGT model block (`bbg_quote.py:67-74,99-106`).

**Quota classes:**

| Allowance entry | Ceiling | Reserve |
|---|---|---|
| bql | 2,920,000 (measured floor, 2026-10-05 block) | 1,875 (held) |
| reference | 52 (held, one ledger day) | 25 (held) |
| history | 5,858 (measured) | 7,322 (held) |
| model_block | null (absent) | null (absent) |

- Source: `data/mdpf/scripts/demque/bbg_allowance.json:1-50`.
- A model_block request is priced on its component channels: header and forecast on reference, history on history (`bbg_quote.py:42-44`). ABNB = 989 cells (25 header + 83 hist x 11 years + 17 x 3 forecast).
- The older per-family rows gate: `data/etfs/scripts/rivalfunds/bbg_budget.py:94-136` with `bbg_budget.json` (ceiling 150,000 rows, reserve 30,000). `spent()` sums **every** mode's rows in the site Z local ledger (`bbg_budget.py:57-70`), so AMGT rows do reduce the rival-funds backfill room.
- Yahoo: daily cap of 400 vendor requests, one per security (`demand_queue.py:22-23,346`).
- Surface E (Opal ad-hoc): 10% of the history ceiling = 585 cells, enforced by NFRA_OPLGTW. Source: `org/tier1_exec/1.0.0_SA_CTO/deliverables/DEMQUE_QUEUE_FORM_ANDREW_20261013.md` ("Surface E: the starting cap").

**Who submits:** COO seats commit request files. The AMGT rows were filed by `2.0.0_SA_COO~R1` "for AMGT_RESAPP" (commits 3a9a64971e on 2026-10-08 and 21dda61a75 on 2026-10-13). `2.0.0_SA_COO~Q1` freezes the quotes. No producer code submits rows: a Grep of the DEMQUE folder for `research_dossier|covered_universe|scoped_amgt|lib.research|AMGT` found only a gap note at `reserve_estimate.py:53-54`.

**Drain cadence:**

| Component | DESIRED | APPLIED |
|---|---|---|
| Bloomberg standing drawer (site Z) | Fires every day, draws only on NON-trading days, history and reference channels only (`standing_drawer.py:1-25,61`; `drawer_schedule.py:1-10`). model_block is "its own producer" (`standing_drawer.py:324-325`). | `demque-backfill` rows exist only for 2026-10-10 and 2026-10-11 (Sat/Sun), 5,858 cells each. |
| Bloomberg ledger upload | Uploaded from the site Z local budget ledger by `bbg_ledger_upload.py:112-159` | 6 of 6 days, 2026-10-08 to 10-13, each object written at 08:30 local the next day |
| Yahoo draw | `run_daily_draw.sh` daily | Ledger objects for 6 of 6 days, 2026-10-08 to 10-13 |

**Live reads (denominators printed):**
- `bash .tools/aws s3 ls --recursive s3://opal-data-assets/bloomberg/global/bronze/demand_ledger/` -> 6 objects (dt=2026-10-08..13), **107 rows**.
- `bash .tools/aws s3 ls --recursive s3://opal-data-assets/yahoo/global/bronze/demand_ledger/` -> 6 objects, **30 rows**.
- `bash .tools/aws s3 ls s3://opal-data-assets/bloomberg/global/silver/demand_ledger/` -> empty.
- `.../silver/request_state/` -> 1 object, `request=ETFS_RIVALS-HISTORY-OWED-DAILY/`.
- Local actuals: `org/missions/D8/MDPF/MDPF_DEMQUE/ledger/BBG_ACTUALS.jsonl` has 5 rows and **0 AMGT rows**.
- Drawer survey (read-only, laptop tree): `python data/mdpf/scripts/demque/standing_drawer.py --open` -> 17 files = 6 open + 11 not_drawable.

## 2. Each AMGT need against DEMQUE

| Need | In DEMQUE? | Demand kind / quota | Cadence | Evidence |
|---|---|---|---|---|
| Bloomberg model block, **daily refresh + admit of the registered library (96 names)** | **BYPASS**, metered after the fact with **no cells** | No request. Ledger mode `amgt-model-block`: rows=6,320 returned records, `cells: null`, `channel: null`, `claim: absent`, basis "no unambiguous per-mode conversion/channel". It counts in the rival-funds rows budget, not in any DEMQUE channel. By DEMQUE's own rule about 96 x 989 = **~94,900 cells/day** (inferred upper bound: ~7,300 reference + ~87,600 history). Compare the history ceiling of 5,858 and the reference ceiling of 52. | Daily ~13:0xZ, every calendar day including weekends. Missed 2026-10-13 (Terminal signed out). | Producer: `integrations/bloomberg/research/model_block_pull.py:785,804,817,841` (vendor calls); `:2195-2226` (`record_fire_budget`, "a fire is never blocked or failed by bookkeeping"); `:2366-2433` (`cmd_refresh` re-pulls every registered name daily). Ledger batch_id `amgt-model-block:20261012T131238Z:calls=768:security_fields=14976:figures=70790:records=6320` (768/8 = 96; 14,976/156 = 96). Converter refusal: `data/mdpf/scripts/demque/bbg_ledger_upload.py:96-100`. Scheduler: `lib/research/corpus/induction_scheduled.py:10-16` (task `amgt-induction-daily`). Live pull_log: `s3 ls s3://opal-data-harvest/amgt/harvest/state/pull_log/` -> 99 keys; `BA_US_Equity` stamps 20261010/11/12/14 at ~13:02Z. |
| Model block for a **new** name (ABNB) | **ROW**, not drawn | `AMGT_RESAPP-107a-ABNB-MODEL-BLOCK`: tier 4, non_client, channel model_block, 989 cells (held). Queue form item D2. | One-off. Quote finish 2026-10-13 (held) has passed. The drawer says "model_block: its own producer". | `requests/AMGT_RESAPP-107a-ABNB-MODEL-BLOCK.json:1-30`, `.quote.json:1-13`; survey not_drawable. There is no `security_key=ABNB_US_Equity` under the pull_log (0 of 99). |
| Bloomberg refdata, ICT identity | **ROW**, stuck | `AMGT_RESAPP-493c-ICT-IDENTITY`: tier 4, reference, 4 fields, 1 security. Queue form D3 counts it as 1 cell. | One-off | Survey: "no frozen quote on file for channel reference". `requests/AMGT_RESAPP-493c-ICT-IDENTITY.json`. |
| Bloomberg refdata, peer price currency (scanner CRNCY) | **ROW** (slice 1 open; full list held) | SLICE1: 50 reference cells, tier 4, quote finish 2026-10-14 (held). FULL: 1,038 cells, finish 2026-12-04, `draw_hold` until slice 1 reads a non-USD currency. | Slice 1 draws on the next NON-trading-day fire (2026-10-17 at the earliest), so the 10-14 weekday-rule quote and the drawer disagree. | `requests/AMGT_RESAPP-S14-CRNCY-SCANNER-US-SLICE1.quote.json`; `...-SCANNER-US.quote.json`; survey open list. |
| Bloomberg price axis (PX_LAST + TR field; 30/90/365 rankings) | **BYPASS** (carded in the queue form as production surface A4, but **not metered**) | Queue form A4 holds it at ~3,000 history cells/day today and ~1,000/day under the 5-day incremental rule plus TR. `reserve_estimate.py:53-54` lists it as a named gap ("not readable from code"), so it is outside the history reserve. | Daily, in the 7:00 ET site Z vehicle (`PRICE LEG`) | `integrations/bloomberg/pipeline/scheduled_daily_pull.cmd:352-377`; `price_axis_pull.py:303,388` (`historical_data`). No ledger mode for it in any of the 107 rows. Modes seen: daily 8, backfill 5, names 4, demque-backfill 77, amgt-model-block 4, bbgtml-* 9. |
| Bloomberg refdata at induction (add a name) | **BYPASS**, unmetered | No row and no ledger record | Within the daily `amgt-induction-daily` run, per new name | `lib/research/identity/add_security.py:523`. A Grep of `lib/` and `integrations/` for `bbg_budget|record_fire_budget|demand_ledger` hit only `model_block_pull.py` and `etf_daily_pull.py` (4 files including tests). |
| Bloomberg management officers / one-time research pulls (segments, officers) | **BYPASS**, unmetered | Own call-count confirmation (`--confirm-calls`), not the queue | One-time / batch | `lib/research/management/bloomberg_fallback.py:197`; `integrations/bloomberg/research/research_pulls.py:1-30,159`; `management_posture_batch.py:1-15` |
| Bloomberg on-demand model block (ticker add from the page) | **BYPASS**: a separate SQS seam, unmetered | SQS `opal-research-pull-requests`; the consumer calls `stage_pull` directly, with no budget record | On demand, run by a person | `integrations/bloomberg/research/pull_consumer.py:1-30,45`. Live: `bash .tools/aws sqs get-queue-attributes --queue-url https://queue.amazonaws.com/313476888478/opal-research-pull-requests --attribute-names ApproximateNumberOfMessages ...` -> 0 visible, 0 in flight. |
| Bloomberg bronze landing | n/a (a writer, not a pull) | n/a | n/a | `lib/research/harvest/bloomberg.py` (`bronze_write`) |
| Scores | **ABSENT** (no vendor call) | Reads the stored model block and peers | UNRESOLVED | `lib/research/scores/run_scores.py:11,147` (`score_robustness_annual_variant`). The live quarterly fetcher `robustness.py:456-534` is not used by run_scores. |
| Peers | **ABSENT**, except the CRNCY rows above | Computed from stored data | UNRESOLVED | `lib/research/peers/engine.py:1-25`; currency gap = S14 rows |
| Seeking Alpha | **ABSENT** (C-METER) | none | UNRESOLVED (no scheduler found) | `integrations/seekingalpha/rest_fetch.py:1-35` (REST over a residential proxy) |
| Bright Data SERP (management / CEO search) | **ABSENT** (C-METER) | none | UNRESOLVED | `lib/research/management/ceo_search.py:309-334`; `enrich.py:553,713`; harvest writer `lib/research/harvest/bright_data_serp.py:1-25` ("wired into nothing") |
| SEC filings (EDGAR) | **ABSENT** (C-METER) | none | UNRESOLVED | `lib/research/filings/fetch.py:75-76,108`; writer `lib/research/harvest/filings.py` |
| News / chatter harvest (`opal-harvest-security-metrics`) | **ABSENT** (C-METER). The axis job reads the pool and calls no vendor. | none | Axis: `cron(0 10 * * ? *)` UTC. Article harvesters: UNRESOLVED. | `bash .tools/aws scheduler get-schedule --name amgt-resapp-chatter-axis-daily` -> Lambda `amgt-resapp-chatter-axis`; `lib/research/metrics/chatter_axis.py:1-12` |
| Posture, drafting, AI fill (Anthropic LLM) | **ABSENT** (C-METER) | none | UNRESOLVED. AI fill is held off the served API (`AMGT_AIFILL_ROOT=/var/empty/aifill-hold`). | `lib/research/posture/judge.py:126-136`; `lib/research/filings/analyze.py:321-334`; `lib/research/aifill/model.py:23`; `infra/aws/terraform/harvest/scoped-amgt-api.tf:517` |
| The Lambda itself (`scoped_amgt.py`) | n/a: it reads stores only | none | per request | `scoped_amgt.py:157,459,502` (DynamoDB reads). No vendor call: Grep for urlopen, requests or anthropic found none. |

## 3. Does the queue know the Security Analysis universe?

**No.**
- `requests/ENROLMENT_TIERS.json` names one daily tier (`ADVI_COTBKF-TIER2-15-FUNDS`) and one rolling tier (`IRPT_BCKEND-AS-TRADED-CLOSES-878`). It has no AMGT entry.
- DEMQUE code never reads `research_dossier`, the crosswalk or the AMGT library (Grep above).
- The universe lives only inside the producers:
  - `model_block_pull._registered_security_keys` (`:2112`), with 99 pull_log keys live;
  - `price_axis_pull` covered universe (`:22-29` of its docstring).
- The page list is measured at 95 in the Security denominator section above.

## 4. Quota usage and headroom (DEMQUE ledger, cells are held conversions)

**Bloomberg, 2026-10-13 (UTC day):**
- bql: 12,272 (production daily). That is far above the held bql reserve of 1,875 against the 2.92M ceiling, so the reserve understates production about 6.5 times.
- reference: 8.
- history: 12.
- model block: 0 (it did not fire).

**Bloomberg, 2026-10-12:**
- bql: 12,016.
- reference: 8.
- history: 34.
- model block: 6,320 records, cells null.

**Headroom by channel:**
- History backfill room on a trading day is **0**, because the reserve (7,322) exceeds the ceiling (5,858). Non-trading days draw at the 5,858 ceiling plus carry-over.
- Reference backfill room is **27 cells/day** (52 - 25). The AMGT model block's ~7,300 reference cells/day are invisible to it.
- model_block channel: no allowance (`absent`).
- Rival-funds rows budget (120,000 backfill rows): 2026-10-12 spent 7,096 rows (6,320 of them AMGT), leaving ~112,900. That figure is from the S3 copy. The site Z local file is the gate's real source and was not read: UNRESOLVED.

**Yahoo:** AMGT has 0 rows. 2026-10-13 total drawn 564,531 cells, mostly the standing T-1 extension.

**Unresolved:** the PRD's open item 1 ("AMGT daily draw ~132,000 cells vs 74,255 + 2,089", `MDPF_DEMQUE_PRD.md:211`) is still unmeasured on C-CELL. The ledger's null cells for `amgt-model-block` are that gap, live.

---

# Part 4 -- The downloadable dossier as clean JSON

## Headline

**No JSON download exists.** The page's two header buttons download a **PDF** ("Print") and a
**Markdown** file ("Export as a document"). `format=json` is refused with HTTP 400. A persisted,
per-value-cited **JSON dossier does exist** in S3 gold (`research_dossier`, 95 names, 1,431 objects),
but no route serves it whole, and neither export includes the team's own research content in it
(recommendation, why-we-own, positives/negatives, cases, pillars). In the persisted JSON, 100% of present
research-note values carry a SOURCE citation. **0% carry a per-value AS-OF date**, and **no value except
team-sheet row LABELS carries a CLAIM field** (measured/inferred/held/absent).

---

## Commands used (exact)

```
EV=<scratch>/dossier ; AWS=bash /cygdrive/c/Users/AndrewBerman/Desktop/ajb_workspace/.tools/aws
# event shape: lib/research/api/scoped_amgt.py:7033-7051 (_path/_method/_query), :7010-7022 (x-firm-id fails closed),
#              header value "opal" as in lib/research/api/tests/test_covered_no_block.py:35
printf '{"rawPath":"/api/scoped/amgt/security/<KEY>/<leaf>","requestContext":{"http":{"method":"GET"}},"headers":{"x-firm-id":"opal"},"queryStringParameters":{"format":"<fmt>"}}' > ev.json
$AWS lambda invoke --function-name opal-amgt-scoped-api --payload fileb://ev.json --cli-read-timeout 120 out.json
#   (the shim is AWS CLI v1: --cli-binary-format is an UNKNOWN option there -- dropped)
$AWS s3api list-objects-v2 --bucket opal-data-harvest --prefix amgt/harvest/gold/research_dossier/ --output json > ls_research_dossier.json
$AWS s3api list-objects-v2 --bucket opal-data-harvest --prefix packs/ --output json > ls_packs.json
$AWS s3 cp "s3://opal-data-harvest/<newest research_dossier key per name>" newest/<KEY>.json    # 95 GETs, 0 failures
python -I <scratch census script> <scratch>/dossier/newest ASML_NA_Equity                    # per-value census
```

Invocations made (all StatusCode 200 at the Lambda level, rc=0):

| Key | leaf / format | HTTP in body | Saved bytes |
|---|---|---|---|
| CAT_US_Equity | print?format=rich | 200 text/markdown | `CAT_US_Equity.rich.md` (45,327 B) |
| CAT_US_Equity | print (pdf) | 200 application/pdf, base64 | `CAT_US_Equity.pack.pdf` (71,331 B, `%PDF-1.4`) |
| CAT_US_Equity | print?format=json | **400** `{"refused": true, "reason": "unknown print format 'json': use format=pdf or format=rich"}` | `out_print_json.json` |
| CAT_US_Equity | thesis | 200 | `CAT_US_Equity.thesis.json` |
| BA_US_Equity | print?format=rich, thesis | 200, 200 | `BA_US_Equity.rich.md`, `BA_US_Equity.thesis.json` |
| ASML_NA_Equity | print?format=rich, print (pdf), thesis | 200, 200, 200 | `ASML_NA_Equity.rich.md` (181,414 B), `ASML_NA_Equity.pack.pdf` (148,205 B, 25 pages), `ASML_NA_Equity.thesis.json` |

---

## (1) Does a download exist, in which formats, and is JSON reachable from the UI?

- **Exists: YES, two formats. JSON: NO.**
- Frontend `portal/src/pages/SecurityAnalysis/components/PrintExportAction.tsx`:
  - "Print" button `:109-118` -> `handlePrint` `:63-76` -> `requestPrintPack` -> PDF blob shown in an iframe modal `:168-170`.
  - "Export as a document" button `:120-133` -> `handleExportRichText` `:87-105` -> downloads `${securityKey}.md` as
    `text/markdown` `:93-98`.
- Client `portal/src/api/endpoints/amgt-lead-panel.ts:249-252`: `printPackPath(securityKey, format?: 'rich')`. The type
  allows only `'rich'` or nothing, so the client cannot even form a JSON request. `requestPrintPack` `:259-270`,
  `requestRichText` `:276-287`.
- Backend: route `lib/research/api/scoped_amgt.py:7745-7748` -> `_print_pack` `:7831-7903`. The `fmt` whitelist
  is `("pdf","rich")`; anything else raises 400 at `:7848-7851`. This was measured live: `format=json` -> 400 (table above).
- Both formats delegate to `lib/research/print/render_pack.py`: `build_pack` (PDF) and `build_rich_text` `:1452-1642`
  (Markdown). The docstring calls it "machine-readable" (`:1461`, `:1560`), but it is GitHub-flavoured Markdown tables and
  block quotes, not JSON.
- **Built per request, not persisted.** `build_rich_text` writes `pack_<key>.md` to the Lambda temp dir (`:1638-1641`).
  `_print_pack` reads that file back and returns it (`:7882-7889`). No S3 write occurs on this path.

## (2) The JSON schema: top-level keys, per-value shape, any declared schema file?

There are two JSON objects to distinguish.

**(a) The persisted gold dossier: the only real "dossier JSON".** Producer `lib/research/corpus/dossier.py`,
`METHOD_VERSION = "amgt-corpus-dossier/15"` (`:151`). Its shape is declared **in the module docstring `:22-55`, not in a
schema file**. It is read by `read_dossier` `:1626-1640` (newest `as_of` date, then newest LastModified, current method
preferred `:1603-1623`).
- Top level (measured on ASML/BA objects): `artifact, method_version, subject{security_key}, as_of (UTC build date),
  inputs[{key, sha256}], fields{...}, content_sha256`.
- `fields` has 24 keys (measured): `cases{upside,base,downside}, company_description, comparison_set, fund_form_ref,
  fund_of_record, growth_algorithm, investment_thesis_summary, kpi_set, last_stated_position, management, model_rows,
  negatives, ownership, pack_shape, positives, recommendation, risks{+pre_mortem}, sector_template_ref, special_items,
  team_sheet, thesis_pillars, thesis_summary, typecast_ref, why_we_own`. Note: `team_sheet` (method /11-/15, `:147-150`)
  and `pack_shape` are **not in the docstring schema**, so the docstring has drifted from the bytes.
- Per-value shapes (measured across the 95 newest objects):
  - section text: `{"value": str, "citation": {report_key, report_id, locator, passage}}` or
    `{"value": null, "absent": "<reason>"}`. 21 of 95 `thesis_summary` values are a third shape, `{"value": "", "absent": ...}`.
  - continuation-carried (`thesis_summary`, `fund_of_record`, `last_stated_position`, pillars): citation is
    `{report_key, extract_key, locator, passage}`. Pillars are `{pillar, text, terms, citation}` (key `text`, not `value`).
  - `cases.<c>`: `{value: {metric: {year: str}}, unit_as_written, currency, currency_basis, citation}`.
  - `model_rows[]`: `{mnemonic, source, figure: {value, unit, fiscal_year, source, stamp}}` or `figure: {value: null, absent}`.
  - `kpi_set.<term>`: `{terms[], count, citations[]}`.
  - `*_ref`: `{uri, content_sha256}`, or absent.
  - `team_sheet`: `{workbook_key, sheet, class, rows[], row_labels[{code, text, source, cite, claim, why}], row_values[[n...]],
    row_classes, row_formats, row_numbers, blocks[], periods, reason}`.
- **Declared schema file: NONE.** Globbing `**/*{dossier,DOSSIER,Dossier}*.{json,ts,tsx,yaml,yml}` finds proof-of-spec
  records, two atom-decomposition catalog entries
  (`workflows/atom_decomposition/catalog_entries/harvest_research_dossier.yaml`, `harvest_research-dossier.yaml`) and the
  page component `portal/src/pages/SecurityAnalysis/components/DossierSections.tsx`. There is no `*.schema.json`, and
  `org/standards/` has 0 hits for "dossier". The nearest interface record is a worker deliverable,
  `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~1/DOSSIER_INTERFACE.md`. Its own surprise row
  (dossier.py `:115-120`) says it was built from quoted text, not from an independent read of `types.ts`.

**(b) The `/thesis` route body** (`scoped_amgt.py:4237-4321`): JSON, but it is a page bundle, not a dossier. It carries
dossier slices: `dossier_fields` (`:4279`, built by `_dossier_fields` `:5607-5670`), `dossier_sections` (`:4280`, 5 fields:
company_description, why_we_own, positives, negatives, special_items), `model.team_cases` (`:4241`), `model.team_sheet`
(`:4245`), and `management` (`:4321`). The status vocabulary is `SERVED`/`ABSENT`/`READ_FAILED` (`:5630`) or lowercase
`served`/`absent` in `dossier_sections`. It does **not** use measured/inferred/held/absent.

## (3) Does EVERY value carry source, as-of and claim? Counts

Census: a scratch census script (session scratchpad, not committed). Definitions: **source** is a per-value field naming the origin; **as-of** is a
per-value DATE field (a date inside a filename such as `ASML research pack 5_5_2026.pdf` is NOT counted); **claim** is a
per-value field whose value is one of measured/inferred/held/absent.

**ASML_NA_Equity, the newest gold object** (`as_of=2026-10-12`, 6 inputs, `content_sha256` 63c8e846...):

| value class | n | source | as-of | claim |
|---|---|---|---|---|
| 16 section fields + risks.pre_mortem (14 present, 3 absent) | 17 | 14 | 0 | 0 |
| cases (3 present) | 3 | 3 | 0 | 0 |
| thesis_pillars (2 present) | 2 | 2 | 0 | 0 |
| refs (2 present, 1 absent) | 3 | 2 | 0 | 0 |
| model_rows (92 present, 17 absent) | 109 | 92 | 92 (`stamp`) | 0 |
| kpi_set terms (13 cited, 12 count=0) | 25 | 13 | 0 | 0 |
| team_sheet row_labels | 37 | 37 | 0 | **37** (16 measured / 4 held / 17 absent) |
| **TOTAL** | **196** | **163** | **92** | **37** |

**All 95 newest gold objects:** 49,346 value units. 44,735 have a source (every PRESENT cited value does; the gaps are
ABSENT values and count-0 KPI terms). 7,707 have an as-of: only `model_rows[].figure.stamp`. **3,773 have a claim: only
`team_sheet.row_labels[].claim`** (1,345 measured / 993 held / 1,435 absent; 0 inferred). That count includes 31,259 team-sheet
number cells, which are bare numbers whose only source is the sheet-level `workbook_key`, with no per-cell source, as-of or claim.
Excluding those cells: 18,087 units, of which 13,476 have a source, 7,707 have an as-of, and 3,773 have a claim.

- **Source:** satisfied for every present research-note value (citation = S3 report key + locator + verbatim passage).
  ABSENT values carry a free-text `absent` reason instead.
- **As-of:** **missing on every research-note value.** Citations have no report date (keys `locator, passage, report_id,
  report_key` only). The only dates are the document-level build date `as_of` and the model-row `stamp`.
- **Claim:** **missing on every value except team-sheet labels.** "Absent" is expressed structurally (`value: null` +
  `absent`), not in a claim field. The empty-string + absent shape (21 thesis_summary values) is ambiguous to a consumer that
  branches on `value`.
- The **exports** (Markdown/PDF) carry no claim field at all. `grep -c claim ASML_NA_Equity.rich.md` = 0. Figure rows print
  `as of <vintage> - <source>` inline as prose (e.g. `CAT_US_Equity.rich.md` header table). Drafted sentences print an
  evidence id + accession + location (`render_pack.py:1002-1019`) with no date field.

## (4) One security end to end from the live route

**First choice CAT_US_Equity: NOT a dossier name.** `/thesis` returns `research_coverage.status = outside_coverage`
("covered_names": 95). `dossier_fields.*` and all 5 `dossier_sections` are absent ("We hold no research notes for this
company."). `drafting_status = ABSENT` (NoSuchKey `drafting/v1/CAT_US_Equity.json`). There is no
`security_key=CAT_US_Equity` partition among the 95 in `research_dossier`. BA_US_Equity is a dossier name, but its newest
object (`as_of=2026-10-12.e2e2cb6a8f3bb1a9.json`) holds almost nothing: every section is absent, with "no class A report for
this security". So I walked **ASML_NA_Equity**, the joint fullest dossier (16 present fields, tied with INTU/UBER/WDAY), which
also has a page fixture.

**ASML rich export (`ASML_NA_Equity.rich.md`, the bytes the "Export as a document" button downloads):**

| Section (line) | State | Cited? | As-of | Claim field |
|---|---|---|---|---|
| Header (5) | present, 10 rows + Description line | source text in each row | `as of 2026-10-14T13:03:15Z` per row (prose) | none |
| Fiscal year 2016-2025 (21-606) | present, figure tables | per-row source (bloomberg-dapi) | per-row vintage (prose) | none |
| Fiscal year 2026E-2028E (670-694) | present, consensus (BEST_*) | per-row "BBG" | per-row vintage | none |
| Recommendation (706) | present, 8 **machine-drafted** sentences from the 20-F | evidence id + accession + item/paragraph | none per value | none |
| Investment Thesis (742) | present, 5 drafted sentences | same | none | none |
| Risks and Considerations (766) | present, 3 drafted sentences | same | none | none |
| Management/Board (780) | present, 7 officers | "bloomberg" column | none (route carries `management.as_of = 2026-10-02`, not printed) | none |
| Peers (794) | present, 12 members + 12 ABSENT columns | registry code per column | none | none (prose says "inferred, not measured" once) |
| Analyst Posture (834) | **ABSENT** (no call; printed twice) | reason text | none | none |
| Model Notes (839) | ABSENT lines (y/y rows, chart) | reason text | none | none |
| Footer (846) | "Source: model block (870 figures) -- vintages 2026-10-14T13:03:15Z, 2026-10-14T19:58Z" | -- | -- | -- |

**What the export OMITS, though the route and the gold dossier hold it for ASML:** the team's own research. Measured
counts in `ASML_NA_Equity.rich.md`: "Why we own" 0, "Positives" 0, "Negatives" 0, "Special items" 0, "pillar" 0,
"PFOE"/"MAINTAIN POSITIONS" 0, "report_key" 0, "Upside" 0. The same holds in the PDF (pypdf over 25 pages: Why we own 0,
Positives 0, PFOE 0, Upside 0). Root cause: `render_pack.py` has **0** occurrences of `dossier|team_cases|team_sheet`, and
`_print_pack` passes it only model block, thesis bundle, peers, posture and description (`scoped_amgt.py:7872-7881`). The
`/thesis` route for ASML does serve them: `dossier_sections` 5/5 `served` with citations, `dossier_fields.thesis_pillars` (2,
cited), `management` SERVED (cited), `pack_shape` SERVED (basis = 2 S3 report keys), `fund_of_record`/`last_stated_position`
ABSENT, and `model.team_cases` base/upside/downside SERVED with citation.

**Persisted gold dossier walk (`newest/ASML_NA_Equity.json`, s3://opal-data-harvest/amgt/harvest/gold/research_dossier/security_key=ASML_NA_Equity/...):**
recommendation, company_description, growth_algorithm, investment_thesis_summary, risks (+pre_mortem), ownership,
management, special_items, why_we_own, positives, negatives, thesis_summary, pack_shape, and cases x3 are present and cited
(report_key + locator + passage), with no date and no claim. comparison_set, fund_of_record and last_stated_position are
absent with a reason. thesis_pillars has 2, cited. sector_template_ref and typecast_ref are present (uri+sha); fund_form_ref is
absent. model_rows has 109 (92 with value+source+stamp, 17 absent). kpi_set has 25 terms (13 cited). team_sheet has 37 labelled
rows with a claim and no numeric row values.

Inconsistency spotted (not chased): gold `recommendation` = "MAINTAIN POSITIONS IN PFOE AND IDVZ ..." (cited), yet
`last_stated_position` and `fund_of_record` are ABSENT with "no report carries a non-empty RECOMMENDATION line" and "no
report's RECOMMENDATION line names a fund token (IDVZ|PFOE|DIVZ)". Those two fields come from the continuation artifact,
not the section reader. This is a candidate surprise row for AMGT_CORPUS, not filed (read-only).

**Persisted or per request?**
- The **download** is per request (see (1)).
- `packs/` (`scoped_amgt.py:6132`) is **not** the dossier store. `s3api list-objects-v2 --prefix packs/` lists **106 objects**:
  104 `packs/<key>/input_ledger.json` + 2 `status.json` (NVDA, SAP) + 1 template under `packs/_template/`. Some keys are
  legacy duplicates (`BA_US/`, `BABA_US/`, `COST_US/`, `BP/_LN_Equity/`, `NG/_LN_Equity/`). Newest LastModified
  2026-10-14T13:18:10Z (`packs/ZURN_SW_Equity/input_ledger.json`), oldest 2026-09-11T19:18:56Z. There are no PDFs or
  dossiers there. `render_pack.py:79` reads only the DOCX template at `packs/_template/`.
- The persisted dossier JSON is gold: `s3://opal-data-harvest/amgt/harvest/gold/research_dossier/`. **1,431 objects, 95
  `security_key=` partitions** (not truncated), newest 2026-10-12T00:25:15Z (`2317_TT_Equity/as_of=2026-10-12...`), oldest
  2026-09-29T10:48:46Z. Never overwritten (dossier.py `:63-67`). The newest per name has `as_of` 2026-10-11 or 2026-10-12.

## (5) What is missing for a "clean JSON dossier with all necessary citations"

1. **A JSON format on the existing leaf.** Add `format=json` to `_print_pack` (`scoped_amgt.py:7848`), widen
   `printPackPath`'s type (`amgt-lead-panel.ts:249`), and add a third button or a format choice in `PrintExportAction.tsx`.
   Today the 400 refusal is the designed answer.
2. **Include the team's research.** Neither export includes `dossier_sections`, `dossier_fields`, `team_cases` or
   `team_sheet` (render_pack has 0 references). A clean dossier must compose the gold `research_dossier` fields alongside
   the model block, drafted filing sentences, management, peers and posture.
3. **A declared schema file.** There is none. The docstring schema (`dossier.py:22-55`) omits `team_sheet` and `pack_shape`.
   A `*.schema.json` under `org/standards/` or `lib/research/` is needed for a consumer to validate against.
4. **Per-value AS-OF.** Research-note citations carry no report date (only `report_key`, `report_id`, `locator`,
   `passage`). Only model rows (`stamp`) and the document `as_of` are dated. The report's date has to be lifted from the
   report or extract metadata into the citation.
5. **Per-value CLAIM field (measured/inferred/held/absent).** Present today only on 3,773 team-sheet labels. Missing on all
   research sections, cases, pillars, model rows (7,707 present figures), KPI terms and the drafted (machine-generated) filing
   sentences. Drafted sentences in particular should be distinguishable from team-authored text: they carry
   `generated: true` and `verbatim_check: PASS` on the route, but no claim value, and the export prints neither.
6. **One absent shape.** `{"value": null, "absent": r}` vs `{"value": "", "absent": r}` (21 thesis_summary values) vs
   `{"status": "ABSENT", "reason": r}` on the route vs `"status": "absent"` in `dossier_sections`. A consumer branching on one
   field cannot read all four (doctrine section 6).
7. **Team-sheet number cells** (31,259 across the 95 names) have no per-cell source, as-of or claim. Only the sheet-level
   `workbook_key` covers them.
8. **Coverage.** Only 95 names have a dossier. Fill is thin: comparison_set is 0/95, positives/negatives/special_items 13/95,
   and cases 34/95. BA's newest object is almost entirely absent.

---

# GAPS

Each gap gives the surface, what is missing, the proposed fix and the proposed dell1 project. All four candidate
projects are on the dell1 fabric:
- AMGT_RESAPP: active, round 106.
- AMGT_HARVST: active.
- AMGT_CORPUS: complete. Its producer `dossier.py` would be a RESAPP fold-in.
- MDPF_DEMQUE: active.

**Andrew's word** marks a gap whose fix waits on a recorded hold or a vendor word. Every fix proposes a schedule, a field
or a gate. None proposes an alert or monitor (moratorium). Any new schedule or name is built to LGIC (rule 30).

| # | Surface | What is missing | Proposed fix | Project | Andrew's word? |
|---|---|---|---|---|---|
| G1 | News, timeline, header chatter count, chatter bubbles (`amgt/harvest/gold/{article_security_mention,chatter_daily,chatter_event,chatter_window}`) | No trigger anywhere. Run by hand (`publication_gold.py build-daily`, `window_tone.py`). Newest partition is 2026-10-08, 3 trading days behind the 10-13 frontier. Tone is at 10-04. | One scheduled trading-day chain: publication gold (mention, daily, event), then window tone, after the harvest cycle. | AMGT_HARVST | no |
| G2 | Lead Panel chatter axes, header Breakout (chatter), `places_moved` (`opal-harvest-security-metrics` `TRENDING_/BREAKOUT_CHATTER`) | The daily job fires (Scheduler ENABLED, 10:00Z) but commits EMPTY: 0 of 242, reason `NO_SIGNAL_IN_WINDOW`, on 10-09, 10-12, 10-13 and 10-14. Cause: `CHATTER_AXIS_SOURCE="legacy"` (`infra/aws/terraform/harvest/chatter-axis-schedule.tf:72`), and the coverage vintage is frozen at `universe/v1/2026-10-06.json`. | Point the axis at the gold chatter source G1 produces, and read the covered list (G15) instead of a frozen universe file. Order it after G1. | AMGT_RESAPP | no |
| G3 | Dossier, crosswalk, universe, peers (Thesis pillars and sections, Exec research, Posture fund line, Model team sheet and cases, Peers tab, identity) | No trigger anywhere. Newest: dossier 10-12/10-11, peers 10-11 (243/245), crosswalk 10-09, universe 10-06 (5 trading days behind). This violates the CLAUDE.md rule that production pipelines are scheduled. | One trading-day chain: universe, crosswalk, dossier `--write`, peers rebuild. The dossier step rebuilds only names whose input reports changed (inputs sha256). | AMGT_RESAPP (dossier producer from AMGT_CORPUS) | no |
| G4 | LLM tier: drafting/filings analysis (Thesis drafted sections, segments, driver chart), management (Exec tab), posture (Posture tab), scores | No trigger. Management is at 10-02 (7 trading days behind), posture as-of 09-16 (~19 behind), scores 09-17, filings mostly 09-17. `run_batch.cmd` says the tasks are "created DISABLED: activation is Andrew's word", and no registration script exists. | Register the tasks with an event-driven trading-day trigger: re-run only on a new filing, new roster or new model block. | AMGT_RESAPP | **yes** (task activation) |
| G5 | Coverage fill behind the 95 | Posture 35, scores 35, management 18 (17 names plus pool), drafting 12. Dossier fields: `comparison_set` 0/95, positives/negatives/special_items 13/95, cases 34/95. BA's newest dossier is almost all absent. | Once G3 and G4 are scheduled, set a per-tab fill target over the 95 and work the batch toward it. | AMGT_RESAPP | no |
| G6 | Seeking Alpha (freshness and input provenance; peers candidates) | The four bronze tables the page reads (`symbol/report/analysis/news`) were last written 09-22, ~16 trading days behind. `sa` is missing from the site-Z cycle runner's registered `--publishers` (`AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~ZW/round85/bz10_task.xml:77`). The runner was stopped by an operator at 2026-10-13T23:53Z. | Re-register the runner with `sa` and restart it. Put the four SA tables on a trading-day trigger. | AMGT_HARVST | check whether the stop was on Andrew's word |
| G7 | Bright Data SERP (`bright-data/harvest/bronze/serp/`): freshness `serp` column, CEO search | 0 objects. The writer `lib/research/harvest/bright_data_serp.py` is "wired into nothing". The freshness column reads NEVER for every name. | Either wire it into the management chain (G4) or retire the column (YAGNI). The CTO picks. | AMGT_HARVST | no |
| G8 | Bloomberg-dependent box tasks (`amgt-induction-daily` on site Z; `OPAL_BBGTML_daily_pull` price leg) | A signed-out Terminal makes the run exit rc 4 with nothing written. 10-13 has no model block and only 17 bronze objects (normally ~294). The run does not catch up the missed day by itself. The box task state can only be read on the box. | Write a per-run state object to S3 (APPLIED cadence becomes readable off-box), have the next run backfill a missed trading day, and surface the failed run in the existing `input_provenance` row (a gate, not an alert). | AMGT_RESAPP | no |
| G9 | MDPF_DEMQUE: model-block daily refresh | Bypasses the queue. It is ledgered after the fact with `cells: null`, `claim: absent` (`model_block_pull.py:2195-2226`; refusal at `data/mdpf/scripts/demque/bbg_ledger_upload.py:96-100`). That is about 94,900 cells a day (INFERRED upper bound) against history 5,858 and reference 52, and the `model_block` allowance is null. PRD open item 1 (`MDPF_DEMQUE_PRD.md:211`) is still unmeasured. | Give `model_block` a cell conversion in the ledger upload (C-CELL), measure one day, and set the `model_block` ceiling and reserve from it. | MDPF_DEMQUE | no |
| G10 | MDPF_DEMQUE: other Bloomberg pulls | Unmetered: the price-axis leg (~3,000 history cells/day per queue form A4; named gap at `reserve_estimate.py:53-54`), induction refdata (`add_security.py:523`), officers and one-time research pulls, and the on-demand SQS seam `opal-research-pull-requests` (`pull_consumer.py`). The history reserve (7,322) exceeds the ceiling (5,858), so trading-day backfill room is 0. The bql reserve of 1,875 is far below actual use (~12,000/day). | Route each through `record_fire_budget` with a channel and cell count. Correct the history and bql reserves to measured use. | MDPF_DEMQUE | no |
| G11 | MDPF_DEMQUE: the page universe | The queue has no standing per-security demand for the 95. `ENROLMENT_TIERS.json` has no AMGT entry. | Enrol the covered list (G15) as a standing daily tier, so a page need becomes a priced, reserved demand row. | MDPF_DEMQUE | no |
| G12 | MDPF_DEMQUE: the four AMGT requests | ABNB model block (989 cells) is not drawable: the drawer says "model_block: its own producer" (`standing_drawer.py:324-325`). ICT identity has no frozen quote. The CRNCY slice-1 quote finished 10-14, but the drawer draws only on non-trading days. | Give the drawer a `model_block` path that hands off to `model_block_pull` admit. Freeze the ICT quote. Align the quote-finish rule with the drawer's days. | MDPF_DEMQUE | no |
| G13 | Downloadable dossier, JSON | No JSON format. The client type allows only `'rich'` (`portal/src/api/endpoints/amgt-lead-panel.ts:249`). The server whitelists `pdf`/`rich` and returns 400 otherwise (`lib/research/api/scoped_amgt.py:7848-7851`, measured live). Both exports omit the team's research: `render_pack.py` has 0 dossier references. No schema file exists; the docstring at `dossier.py:22-55` omits `team_sheet` and `pack_shape`. | Add `format=json` on the same `/print` leaf, composing the gold dossier with the model block, drafted sentences, management, peers and posture. Declare a `*.schema.json`. Add a JSON choice to `PrintExportAction.tsx`. Include the team research in the PDF and Markdown too. | AMGT_RESAPP | no (Opal-internal page) |
| G14 | Dossier citations | Source is on every present value. As-of: 0 research-note values; only 7,707 model `stamp`s. Claim: only 3,773 team-sheet labels; 0 on sections, cases, pillars, figures or drafted sentences. 31,259 team-sheet number cells have no per-cell citation. There are four absent shapes (`value:null`, `value:""`, `status:ABSENT`, `status:absent`). | Add the report date to each citation and a `claim` field (measured/inferred/held/absent) to every value. Drafted filing sentences read `inferred`, never team text. Use one absent shape. Cite team-sheet cells at row level. | AMGT_RESAPP (dossier producer fold-in) | no |
| G15 | Security list | Five lists disagree: 95 page / 94 price / 99 pull log / 102 model block / 105 packs / 302 universe. Each producer picks its own list. | Make `covered_security_keys()` the one input for every daily producer and for DEMQUE enrolment. Print the drift per producer. | AMGT_RESAPP | no |
| G16 | AI fill (Thesis pillars, Exec bio/recent, description fallback) | 95 `ai_fill.json` written 2026-10-14T03:05-03:19Z are served ABSENT on purpose: `AMGT_AIFILL_ROOT=/var/empty/aifill-hold` (`scoped-amgt-api.tf:511-517`; round 105, FWD-41, CTO ruling 2; "the restore is a later order"). The producer has no schedule. | No defect while the hold stands. When the restore is cut, schedule the AI-fill producer in the G4 chain. | AMGT_RESAPP | per the FWD-41 ruling |
| G17 | Corrected fiscal-price overlay (`derived/model_block_fye/`) | Never applied in production. `AMGT_MODEL_BLOCK_ROOT` is unset on the Lambda, so the overlay root is `""` and the prefix is outside the IAM grant (`scoped-amgt-api.tf:99-106`). `derive_fye_fixed.py` was run by hand for 3 names. | Fold the correction into `model_block_pull` derive, which avoids a second store and a never-widen grant. Otherwise set the root and grant it. | AMGT_RESAPP | no |
| G18 | 90/365-day price windows and earnings markers | `price_history_pull.py` has no wrapper and is run by hand. RESAPP v0.35 and v0.33 already carry these as qualified waits on Andrew's vendor word. | Add it to the 07:00 ET price leg once the word lands. | AMGT_RESAPP | **yes** (vendor word, already recorded) |
| G19 | Bloomberg bronze `segments/`, `exec_officers/`, `identity/` (Thesis segment table, Exec fallback) | Run ad hoc. Last 10-07, 5 trading days behind. No schedule was found for `research_pulls.py` segments. | Add them to the induction refresh at a lower cadence (weekly, or on a new filing). Meter them per G10. | AMGT_RESAPP | no |
| G20 | Page code hygiene | Nine dead components (`TopBand`, `RankedChart`, `StarredList`, `RankedList`, `ProvenanceLine`, `ResearchNoPermission`, `IdentityLine`, `StatTile`, `GenerationCaption`). `thesis.scores` is served but not drawn. `/ledger`, `/coverage`, rank `timeseries` and star/unstar have no caller. `requestRefresh` calls `/refresh`, which has no server route. | Remove the dead code, or wire scores and star/unstar. Low priority. | AMGT_RESAPP | no |
| G21 | ASML dossier consistency | The gold `recommendation` reads "MAINTAIN POSITIONS IN PFOE AND IDVZ", yet `fund_of_record` and `last_stated_position` are ABSENT with reasons saying no report names a fund. The continuation reader disagrees with the section reader. | Make the fund fields read the same section the recommendation reads. Not filed as a surprise row: this order is research only. | AMGT_RESAPP (dossier producer) | no |

Off-page observation, not a gap for this page: the EventBridge rules `seeking-alpha-analysis-daily` and
`seeking-alpha-news-daily` are DESIRED enabled (`infra/aws/terraform/seeking-alpha/main.tf:115-118,210-213`) but
APPLIED DISABLED. They write `opal-data-news-av`, not the harvest bucket.

**Proposed fold-in shape, for the CTO's ruling:**
- AMGT_RESAPP takes G2-G5, G8, G13-G21. That is one daily journey: covered list (G15), then producers on schedule (G3,
  G4, G8), then page, then JSON dossier.
- AMGT_HARVST takes G1, G6 and G7.
- MDPF_DEMQUE takes G9-G12.

**Uncertainty:**
1. The box task states are UNREAD from this laptop.
2. 94,900 cells/day is an INFERRED upper bound.
3. Lag is counted in trading days from object write times and as-of stamps on 2026-10-14.

## Appendix -- the 95 covered security keys (measured 2026-10-14)

1299_HK_Equity 2317_TT_Equity 8035_JP_Equity 8306_JP_Equity 8316_JP_Equity 8766_JP_Equity 939_HK_Equity 
9433_JP_Equity 992_HK_Equity ADBE_US_Equity AI_FP_Equity AMD_US_Equity AMXB_MM_Equity ASML_NA_Equity AZN_LN_Equity 
BABA_US_Equity BATS_LN_Equity BA_US_Equity BBSE3_BZ_Equity BNP_FP_Equity BP/_LN_Equity BZLFY_US_Equity CDNS_US_Equity 
CELH_US_Equity CLX_US_Equity CNR_CN_Equity COST_US_Equity CPA_US_Equity ENEL_IM_Equity GOOGL_US_Equity GPN_US_Equity 
GSK_LN_Equity HAL_US_Equity HD_US_Equity HEI_US_Equity HSBA_LN_Equity IBE_SM_Equity ICICIBC_IN_Equity ICT_PM_Equity 
IDXX_US_Equity IMB_LN_Equity INTU_US_Equity ISP_IM_Equity ISRG_US_Equity JD_US_Equity KMB_US_Equity KOFUBL_MM_Equity 
KPN_NA_Equity LLY_US_Equity MA_US_Equity MELI_US_Equity MER_PM_Equity ML_FP_Equity MNST_US_Equity MSCI_US_Equity 
NESN_SW_Equity NFLX_US_Equity NG/_LN_Equity NKE_US_Equity NOKIA_FH_Equity NOVN_SW_Equity NOW_US_Equity NU_US_Equity 
OMAB_MM_Equity ORA_FP_Equity PBR_US_Equity PWR_US_Equity QXO_US_Equity RIO_LN_Equity RKT_LN_Equity RMS_FP_Equity 
ROG_SW_Equity RWE_GR_Equity SAN_FP_Equity SAP_GY_Equity SHOP_CN_Equity SLB_US_Equity SNPS_US_Equity SPOT_US_Equity 
SSE_LN_Equity ST_SP_Equity TSM_US_Equity TTE_FP_Equity UBER_US_Equity UBSG_SW_Equity ULVR_LN_Equity UNH_US_Equity 
UNVGY_US_Equity VIVT3_BZ_Equity VLO_US_Equity V_US_Equity WALMEX*_MM_Equity WDAY_US_Equity ZTS_US_Equity 
ZURN_SW_Equity
