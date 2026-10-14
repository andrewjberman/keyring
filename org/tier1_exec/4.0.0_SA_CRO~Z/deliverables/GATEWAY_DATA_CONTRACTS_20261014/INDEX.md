# GATEWAY_DATA_CONTRACTS_20261014 -- index (4.0.0_SA_CRO~Z)

- **Directive:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTOZ_DIRECTIVE_20261014_GATEWAY_DATA_CONTRACTS_CENSUS.md` @06ae2a3485.
- **Shape:** one file per group, each with one JSON contract per bucket -> table (directive section 4).
- **Subagent brief:** `parts/_SUBAGENT_BRIEF.md`.
- **G2 assembly:** G2 is fanned out into four parts (`parts/G2a`-`G2d`) and assembled into `G2_assets_silver.md` when all four land.

| group | file | status | tables found | contracts written | tools proposed | open items |
|---|---|---|---|---|---|---|
| G1 harvest | `G1_harvest.md` | DELIVERED 2026-10-14 | 78 datasets (58,639 keys; 18 Parquet tables) | 78 (47 research, 31 plumbing) | 12 typed tools + the 2 deployed raw tools kept | catalog grain split (50 of 78 covered only by a source-level row; 2 with none); producer schedules unread; defects D1-D9 of the assessment @eea2acd58e |
| G2 assets silver | `G2_assets_silver.md` (parts G2a BD, G2b Orion+Eclipse, G2c SmartX, G2d Schwab+others) | DELIVERED 2026-10-14 | BD 32; Orion+Eclipse 9; SmartX 11 + 2 drafts; Schwab 57 + Commonwealth 12 + Tax SMA 1 + own ETFs 8 + Yahoo 1 | 131 | 40 | last-4 never unique (candidate lists); firm fence is a row filter for SmartX and Tax SMA (Z-S109); live 49F BD and the Schwab skill tables are in opal-data-bd; 08403355 half-wired; 49f OOM (Z-S110); Eclipse stall (Z-S111) |
| G3 portal-v2 | `G3_portal_v2.md` | DELIVERED 2026-10-14 | 4,851 objects, 84 dataset groups; 10 certified pages diffed (33 key rows: 22 live, 8 frozen, 1 unread, json/mdpf gone); 3 uncertified pages contracted | 42 (30 served, 10 platinum, 2 DynamoDB) | 9 new + 5 kept + `gateway_query_catalog` extended + `mdpf` channel retired | /json-tiered/* served with no edge auth (Z-S114); catalog names gone json/mdpf/**; pages request 8 missing keys; perfrp last-4 collides 2,826 of 6,183 |
| G4 mdpf gold delta | `G4_mdpf_delta.md` | IN PROGRESS (1 subagent, launched after G3 landed) | -- | -- | -- | due 2026-10-15 18:00Z |
| G5 ETFs | `G5_etfs.md` | DELIVERED 2026-10-14 | 27 Parquet tables + 9 JSON/CSV objects (16,098 keys; 10,491 footers) | 36 | 15 new + `etfs_get_positioning` extended | monthly run = `etfs-reports-monthly-run` -> `etfs-reports-orchestrator`; every tool needs a never-widen read grant; canon fan-in fails daily (Z-S112); Sept report coverage contradiction (Z-S113); DIVZ/PFDE have no peer group |
| G6 news | `G6_news.md` | DELIVERED 2026-10-14 | 8 DynamoDB tables + news S3 (opal-data-news-v2, opal-data-news-av, portal-v2 news keys) | 12 | 5 (`news_search_articles`, `news_trending_topics`, `news_keyword_intelligence`, `news_market_mood`, `news_for_security`) | no news table is keyed by security (harvest mention is the ticker index); semantic chain frozen 160 trading days (revive or retire is Andrew's); `opal-harvest-articles` empty, retire candidate; sparse `source_date_index` GSI |
