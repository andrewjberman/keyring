# AMGT_RESAPP -- BACKFILL SCOPE PROPOSAL: security list (A) + channel inventory (B), for Andrew's confirmation

**Author:** `1.0.0_SA_CTO~Z`, 2026-09-22 ~12:5xZ. **Answers:** the Andrew-direct record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260922_1226Z_AMGT_BACKFILL_GATED_ON_SECURITY_LIST_AND_CHANNEL_INVENTORY.md`
@`2a192b6e07`. No backfill runs until Andrew confirms A and B. On his confirmation, both are written into the PRD as
contracts `C-BACKFILL-SECURITIES` and `C-CHANNEL-INVENTORY`.

**Sources:**
- A read-only research pass over the PRD at v0.21, every writer under `lib/research/harvest`, the Terraform, and live
  EventBridge (144 rules, 23 schedules) and Windows tasks (207).
- This seat's re-checks, each on a different instrument from the pass:
  - an S3 recount per prefix, which matches the pass;
  - the chatter schedule at `infra/aws/terraform/harvest/chatter-axis-schedule.tf:188-192`, which matches;
  - `integrations/bloomberg/pipeline/scheduled_daily_pull.cmd`, which has no price step;
  - `universe/v1/2026-09-16.json`, which gives the missing CIKs.

## A. SECURITY LIST

**Population:** `crosswalk/v1/2026-09-19.json` holds **96 records**. **36** carry a `security_key`, and **60** are
unresolved. A name without a key cannot be backfilled by any channel: every bronze and silver key is built from it.

| set | count | members |
|---|---|---|
| **Phase 1: validation** | 3 | CAT_US_Equity (CIK 18230), CSL_AU_Equity (CIK 1274152), 6861_JP_Equity (Keyence, no CIK) |
| **Phase 2: the rest of the managed set** | 12 | BA_US (12927), COST_US (909832), HD_US (354950), SAP_GY (1000184), BABA_US (1577552), ASML_NA (937966), HAL_US (45012), INTU_US (896878), KMB_US (55785), NU_US (1691493), PBR_US (1119639), VLO_US (1035002) |
| **Phase 3: the rest of the keyed coverage** | 21 | 2317_TT, 9433_JP, 992_HK, BBSE3_BZ, BP/_LN, ENEL_IM, HSBA_LN, ICICIBC_IN, IMB_LN, KPN_NA, NG/_LN, NOVN_SW, RKT_LN, RMS_FP, ROG_SW, RWE_GR, SSE_LN, ST_SP, ULVR_LN, WALMEX*_MM, ZURN_SW (all non-US, no CIK) |
| **Excluded: unresolved** | 60 | These need the add-security step (a Bloomberg identity pull) before any channel can key them |
| **Excluded: ETF holdings** | 161 (holdings-only, 2026-09-16 universe) | Not coverage names. Andrew 2026-09-18: no fleet re-runs until validated |

**Three keying questions to settle before the list locks:**
1. **Petrobras.** The key is `PBR_US_Equity` (the ADR), but the coverage folder says "PETR3 BZ" (the local share).
   Which listing is covered? REC: PBR US, because it has a CIK and so reaches SEC filings.
2. **RWE.** The key is `RWE_GR_Equity` (German composite), but the folder says "RWE GY" (Xetra). REC: GR. The composite
   is the standard research key, and no channel differs between the two.
3. **BP/ and NG/.** The two keys contain a slash. Every writer uses the slash-safe partition, so this is noted, not
   blocking.

## B. CHANNEL INVENTORY

**The layers in one line each:**
- **Bronze** is built and wired for every channel that has a writer.
- **Silver** is built for 7 channels, but written live today only by filings (1 SEC part, 1 issuer-site part).
- **Gold parquet does not exist for any channel.** Every page still reads the old served JSON. That re-homing is
  chain G, cut only after the backfill's silver is read back.
- **The only AMGT schedule running is the chatter axis:** daily at 10:00 UTC, writing DynamoDB, and it is not a
  backfill channel. Every backfill channel is a hand-run command today.

| # | channel | egress word? | bronze | silver | gold (parquet / json) | cycle: now -> REC after backfill | backfill? |
|---|---|---|---|---|---|---|---|
| 1 | Bloomberg model block (refdata / histdata / bestdata) | no (Terminal, box-side) | `bloomberg/harvest/bronze/{refdata,histdata,bestdata}/security_key=<k>/<stamp>.json`, client JSON, write-once; live 48/48/6 | `model_block` built, NOT wired; live 0 | parquet: none. JSON served: `derived/model_block/<k>/<stamp>/model_block.json` (122) | manual, 3 names per call -> **weekly** | **YES**, after its silver is wired (one code cell) |
| 2 | SEC EDGAR filings | **yes** | `sec/harvest/bronze/filing/cik=<10>/<accession>/<doc>`, as received; live 0 | `sec/harvest/silver/filing_source/date=/part-*.parquet`, key (security_key, accession); live 1 | parquet: none. JSON served: `filings/v1/*.analysis.json`, `drafting/v1/` | manual (Sunday task disabled) -> **weekly** | **YES** (B2) |
| 3 | SEC ticker table | **yes** | `sec/harvest/bronze/company_tickers/date=<d>/company_tickers.json`; live 0 | `company_ticker` not built | none | at most once per UTC day per run -> **with #2** | **YES**, rides B2 |
| 4 | Issuer-site / IR documents | **yes** | `issuer-site/harvest/bronze/document/security_key=<k>/doc-<sha16>/<file>`; live 0 | `issuer-site/harvest/silver/filing_source/`; live 1 (Keyence) | as #2 | as #2 -> **weekly** | **YES**, rides B2 |
| 5 | Lusha (officer match) | **yes, billed** | **none**, by C-LUSHA-EXCEPTION (the store refuses it) | `lusha/harvest/silver/contact_match/`, key (domain, person_id), allow-listed fields; live 0 | folded into served `management/v1` | per-use word -> **on demand only** | **YES** (B4), once round 27's roster/domain diagnosis is fixed |
| 6 | Seeking Alpha REST | **yes** | `seeking-alpha/harvest/bronze/{symbol,report,analysis,news,metrics}/security_key=<k>/<stamp>.json`; live 18 | `symbol_profile`, `news_item`; live 0 | the peers table (C-PEER-SET-SA) is not built | manual -> **on demand** | **HOLD** (B3). 0 of 96 records carry an SA symbol, and the session needs re-harvest |
| 7 | Bloomberg identity (add-security) | no | `.../bronze/identity/...`; live 3 | `security_identity` not built | served JSON `crosswalk/v1/<date>.json` | once per new security | **no**. It is the step that resolves the excluded 60, not a backfill |
| 8 | Bloomberg exec officers (management fallback) | no | `.../bronze/exec_officers/...`; live 4 | `executive_officer` not built | folded into served `management/v1` | weekly task, disabled | **no** (fallback only) |
| 9 | Bloomberg daily price (PX_LAST) | no | the ranking pull keeps NO bronze | `security_price_daily` not built | DynamoDB price metrics, served | PRD says daily; **no schedule exists** | **no**. It must first conform: bronze and a daily schedule |
| 10 | ESEF / UKSEF (filings.xbrl.org, by LEI) | **yes** | `filings-xbrl/harvest/bronze/filing/lei=<lei>/...` | shares `filing_source` | as #2 | not set | **no**. Writer built, not wired |
| 11 | Publications (Barron's, WSJ, FT, Bloomberg, SA articles) | **yes** | `{src}/harvest/bronze/article/article_hash=<h>/<stamp>.<ext>`; new grammar gated OFF | `{src}/harvest/silver/article/`; live 0 | served JSON `publications/v1/`, `publication-links/v1/` (legacy) | cadence reserved to Andrew; task disabled | **no** (his cadence call first) |
| 12 | Social feed (Bright Data Reddit) | **yes** | `bright-data/harvest/bronze/social_snapshot/date=<d>/...` | `social_post`; live 0 | none served | collection OFF (measure first, FWD-11) | **no** |
| 13 | Bright Data SERP (CEO profile search) | **yes** | `bright-data/harvest/bronze/serp/date=<d>/...` | `serp_result`, contact fields scrubbed | inside served `management/v1` | manual | **no**. Built, not wired |

**Common to every silver:** partitioned `date=<fetch date>`, one `part-<run stamp>.parquet` per run, write-once,
with lineage columns `bronze_key`, `fetched_at` and `record_hash`.
**Planned gold (chain G, not built):** `amgt/harvest/gold/{table}/date=/{table}_{stamp}.parquet`, plus the JSON
platinum layer the API reads.

## What Andrew confirms

1. **The list:**
   - Phase 1 is the 3 validation names.
   - Phases 2 and 3 are the other 33 keyed names, unlocked in turn after the phase before is read back.
   - The 60 unresolved names and the 161 ETF holdings are excluded.
   - Petrobras = PBR US; RWE = GR.
2. **The backfill channels: #1-#5 now.** #6 waits on its session and symbols. #7-#13 are not backfilled.
3. **The cycles after the backfill:**
   - Weekly: filings, issuer site and the Bloomberg model block.
   - On demand: Lusha and SA.
   - Price keeps its daily leg once it conforms.
4. **Gold is not part of the backfill.** The backfill fills bronze and silver only; gold/platinum (chain G) is built
   next, against the silver it produces.

-- `1.0.0_SA_CTO~Z`
