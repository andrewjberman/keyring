# GATEWAY_DATA_CONTRACTS_20261014 -- index (4.0.0_SA_CRO~Z)

- **Directive:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTOZ_DIRECTIVE_20261014_GATEWAY_DATA_CONTRACTS_CENSUS.md` @06ae2a3485.
- **Shape:** one file per group, each with one JSON contract per bucket -> table (directive section 4).
- **Subagent brief:** `parts/_SUBAGENT_BRIEF.md`.
- **G2 assembly:** G2 is fanned out into four parts (`parts/G2a`-`G2d`) and assembled into `G2_assets_silver.md` when all four land.

| group | file | status | tables found | contracts written | tools proposed | open items |
|---|---|---|---|---|---|---|
| G1 harvest | `G1_harvest.md` | DELIVERED 2026-10-14 | 78 datasets (58,639 keys; 18 Parquet tables) | 78 (47 research, 31 plumbing) | 12 typed tools + the 2 deployed raw tools kept | catalog grain split (50 of 78 covered only by a source-level row; 2 with none); producer schedules unread; defects D1-D9 of the assessment @eea2acd58e |
| G2 assets silver | `G2_assets_silver.md` (parts G2a BD, G2b Orion+Eclipse, G2c SmartX, G2d Schwab+others, G2e Tax SMA assets gold, G2f 49F BD live prefixes) | DELIVERED 2026-10-14 (G2e ~14:3xZ on msg 34115; G2f ~15:1xZ on msg 34128) | BD 32; Orion+Eclipse 9; SmartX 11 + 2 drafts; Schwab 57 + Commonwealth 12 + Tax SMA 1 + own ETFs 8 + Yahoo 1 | 133 (G2e: 2, `opal-data-{49financial,cottonwood}/mdpf/<firm>/gold/taxsma_assets/`, 13 + 2 accounts, 0 behind) | 41 (+ `client_get_taxsma_accounts`) | last-4 never unique (candidate lists); firm fence is a row filter for SmartX and Tax SMA (Z-S109); live 49F BD and the Schwab skill tables are in opal-data-bd; 08403355 half-wired; 49f OOM (Z-S110); Eclipse stall (Z-S111) |
| G3 portal-v2 | `G3_portal_v2.md` | DELIVERED 2026-10-14 | 4,851 objects, 84 dataset groups; 10 certified pages diffed (33 key rows: 22 live, 8 frozen, 1 unread, json/mdpf gone); 3 uncertified pages contracted | 42 (30 served, 10 platinum, 2 DynamoDB) | 9 new + 5 kept + `gateway_query_catalog` extended + `mdpf` channel retired | /json-tiered/* served with no edge auth (Z-S114); catalog names gone json/mdpf/**; pages request 8 missing keys; perfrp last-4 collides 2,826 of 6,183 |
| G4 mdpf gold delta | `G4_mdpf_delta.md` | DELIVERED 2026-10-14 | 3,248 of 3,248 keys; 20 dataset rows. OVERLAP: all 4 gold tables equal portal-v2 leaf for leaf (173/173, 550/550 leaves; 17,360/17,360 cells over 496 dates; 8,493 = 8,493). DELTA: the feed layer + 1 classification index | 7 (4 servable, 3 do-not-serve on record) | 3 new (`mdpf_get_account_model_aua`, `mdpf_get_model_composition`, `mdpf_get_security_classification`); 4 existing kept | CENSUS GAP: `opal-data-assets/portal/gold/mdpf/` (808 keys, the true producer of the served files) and `opal-data-{49financial,inflection,cottonwood}` (499 keys) are covered by no group; feeder chain NOT-YET 10-13/10-14; feed file date runs one trading day ahead of its values; last-4 here is of the SmartX account UUID, not the custodian number |
| G5 ETFs | `G5_etfs.md` | DELIVERED 2026-10-14 | 27 Parquet tables + 9 JSON/CSV objects (16,098 keys; 10,491 footers) | 36 | 15 new + `etfs_get_positioning` extended | monthly run = `etfs-reports-monthly-run` -> `etfs-reports-orchestrator`; every tool needs a never-widen read grant; canon fan-in fails daily (Z-S112); Sept report coverage contradiction (Z-S113); DIVZ/PFDE have no peer group |
| G6 news | `G6_news.md` | DELIVERED 2026-10-14 | 8 DynamoDB tables + news S3 (opal-data-news-v2, opal-data-news-av, portal-v2 news keys) | 12 | 5 (`news_search_articles`, `news_trending_topics`, `news_keyword_intelligence`, `news_market_mood`, `news_for_security`) | no news table is keyed by security (harvest mention is the ticker index); semantic chain frozen 160 trading days (revive or retire is Andrew's); `opal-harvest-articles` empty, retire candidate; sparse `source_date_index` GSI |

**G2f (`parts/G2f_bd_live_prefixes.md`, msg 34128):** the 8 `silver_legacy` 49F BD contracts map to live `opal-data-bd/silver/<table>/YYYY-MM-DD.parquet`.
- Schemas: 4 EQUAL, 3 live-is-a-subset (transactions -5, allocations snake_case-only, realized -1), 0 differ.
- Lag: current 0-2 trading days behind (fees, transactions, realized, prices, allocations, unrealized); assets 80 and transactions_enriched 122 behind.
- Every account id is `z08`, so the bucket is 49F only.
- The 4 `49f` dims and 3 insurance tables have no live counterpart.

**Census total: 308 contracts across the 6 groups (78 + 133 + 42 + 7 + 36 + 12); surprise rows NFRA_OPLGTW-Z-S109 to Z-S114.**
