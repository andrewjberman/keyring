# AMGT_RESAPP -- THE SECURITY ANALYSIS PAGE, V2: one header, five tabs, one pool, one identity

**Author:** `1.0.0_SA_CTO~W`. **Date:** 2026-09-15 ~06:3xZ. **Governing text:** the PRD's CONTRACTS section
(`org/missions/D5/AMGT/AMGT_RESAPP/prd/AMGT_RESAPP_PRD.md`, v0.7: C-PAGE-LAYOUT, C-ONE-STORE, C-ONE-IDENTITY,
C-ETF-PLANE-READ, C-UNION-UNIVERSE, C-SIMILARITY-RANKER, C-POSTURE, C-FILINGS-ANALYZER, C-EXEC-MANAGEMENT). **Where
this drawing and a contract differ, the contract governs and this drawing is the defect.**

**Provenance note.** The transcript record `ANDREW_DIRECT_20260915_055xZ_TRANSCRIPT_SECURITY_ANALYSIS_PANELS_DRILL_DOWN.md`
@fbd5d91431 named this file as a drafted carrier at its line 80. It was NOT drafted at that time; `3.0.0_SA_CVO~W`
caught the absence (review @01e640925c). This file is created now, in the commit that also corrects that record, from
the `/draw` this seat emitted at ~04:5xZ (the AS-BUILT page at the round-10 drain, appendix below) and Andrew's page
words of ~05:0x-05:5xZ (records @7cf62a165f, @a5c6a066de, @fbd5d91431). Every name in section 1-3 is a contract
term or a measured resource; the one thing this drawing does NOT contain is a comparable's ticker, because no ranker
has run. Corrected in the v0.7 commit on `4.0.0_SA_CRO~W`'s read (msg 06:38Z): the price partitions are the crossed
`TRENDING_PRICE#<d>` / `BREAKOUT_PRICE#<d>` (`integrations/bloomberg/research/price_axis_pull.py` docstring lines 43-55),
not a single `PRICE#<d>`; the appendix keeps the historical label as history.

```
SECURITY ANALYSIS v2 (AMGT_RESAPP, PRD v0.7) -- one header, five tabs, one pool, one identity

1. The page plane -- what each panel shows, and the store that feeds it

   HEADER -- the discovery surface (C-PAGE-LAYOUT)                     FED BY (store, cadence)
   ┌────────────────────────────────────────────────────────────────┐
   │ Lead Panel: Trending | Breakout  x  Price | Chatter ; List|Chart│◄── DynamoDB opal-harvest-security-metrics
   │            Starred (firm-scoped)   ticker search                │    TRENDING_PRICE#<d>, BREAKOUT_PRICE#<d> (box-side, daily),
   │                                                                │    TRENDING_CHATTER#<d>, BREAKOUT_CHATTER#<d> (Lambda amgt-resapp-chatter-axis,
   │                                                                │    Scheduler ...-daily, 30-day window, TOP_N=10)
   │ Company feed: publisher items + social items, newest and       │◄── pool s3://opal-data-harvest (C-ONE-STORE):
   │   most-discussed first, each clickable to its source           │    publication-links/v1/{security_key}/{publisher}/{digest}.json
   │                                                                │    publications/v1/{publisher}/{digest}.json  (`published`)
   │                                                                │    social/v1 -- ONLY after S13 measures a supported input
   │ One-line description                                           │◄── derived/model_block/model_block_<key>.json header scalars
   │ Posture line: better | worse | hold | steer_clear vs <comparable>│◄── posture/v1/{security_key}/{as_of}.json (C-POSTURE)
   │ Print  (an export action, never a tab)                         │
   └────────────────────────────────────────────────────────────────┘

   TABS, in order (C-PAGE-LAYOUT)
   ┌ 1 Thesis ─────────────┐ ┌ 2 Exec Management ───┐ ┌ 3 Peers ──────────────┐ ┌ 4 Model ─────────┐ ┌ 5 Posture ──────────┐
   │ what the company does │ │ roster + role start   │ │ comparable set by     │ │ Adam's `Model`   │ │ membership at the   │
   │ now, biggest          │ │ from the FILING's     │ │ C-SIMILARITY-RANKER   │ │ sheet shape, the │ │ snapshot vintage    │
   │ challenges, biggest   │ │ officer section;      │ │ (sector > size band > │ │ same for every   │ │ (held / not held)   │
   │ bets -- machine prose,│ │ Lusha profile link on │ │ country > subsector); │ │ company, from    │ │ the COMPARABLE = the│
   │ EVERY sentence cited  │ │ each CONFIRMED officer│ │ Adam's `CSC` shape    │ │ the model block  │ │ most similar name on│
   │ to a filing passage;  │ │ team avg tenure vs    │ │ (Price..EV, P/E x3,   │ │                  │ │ the OTHER side; the │
   │ ONE "big thing" chart │ │ the pool average      │ │ leverage, 5y growth,  │ │                  │ │ JUDGMENT over two   │
   │ from THESIS_DRIVER    │ │                       │ │ Avg/Median/Min/Max) + │ │                  │ │ four-tab packs;     │
   │                       │ │                       │ │ Scanner factor        │ │                  │ │ marked machine;     │
   │                       │ │                       │ │ quintiles             │ │                  │ │ nothing trades on it│
   └───────────┬───────────┘ └───────────┬───────────┘ └───────────┬───────────┘ └────────┬─────────┘ └──────────┬──────────┘
      filings/v1/{key}/        filings/v1 (officer        Scanner UniverseDataRow      derived/model_block/     posture/v1/{key}/{as_of}
      {accession}.analysis     role start, authority)     (ticker,name,mktVal,         model_block_<key>.json   .json  +  READ-ONLY
      .json -- Claude API      + Lusha contacts_          country,sector,industry      (Bloomberg DAPI,         s3://opal-data-etfs
      w/ citations, SCHEDULED  prospecting c-suite        Group, universe weights)     box-side, raw bytes      config/etf_universe.json
      batch over the UNION     (no contact data stored)   UNION model-block header     before derived)          gold/book, gold/holding,
      universe, never per view + IR-domain web search     scalars; lib/research/                                snapshots/snapshot_<date>
                               for the CEO                peers/engine.py = rungs 1-2                           .json (22:00Z daily, ~Z fabric)

2. The identity plane -- one key in, the same key everywhere (C-ONE-IDENTITY; resolves Z-S95)

   ranked row 'BABA US' (Bloomberg value) ──┐
   model artifact 'BABA_US_Equity'         ─┼──► crosswalk/v1 (versioned, explicit: canonical key, Bloomberg id, ──► ONE canonical security_key
   local association 'BA' | 'security-<16hex>'┘     display ticker, model/pack key, association aliases,               resolved ONCE at the route
                                                    identifier provenance; exchange + share class preserved;           boundary and passed through
                                                    UNRESOLVED stays unresolved, never guessed US)                     overlay|thesis|peers|model|
                                                                                                                      coverage|posture
   an OLD and a NEW link for the same article (article_key = publisher:article_id) count ONCE per security

3. The query plane -- how a PM reaches the payoff

    YOU (portal)
        │  "what does this company mean for us?"
        ▼
   ┌────────────────────────────┐  GET /api/scoped/amgt/security/{security_key}/overlay | thesis | peers | model | posture
   │ SecurityAnalysis page      │  (opal-amgt-scoped-api on HTTP API 7k3ed8px20, authorizer naqxlm; the adapter
   │ header + the tab you open  │   lib/research/api/scoped_amgt.py reads the pool, the metrics table, the ETF plane)
   └─────────────┬──────────────┘
                 ▼
   ANSWER on the page: header line "Posture: worse than <comparable> (held in <ETF>, same sector, size band)";
   Posture tab: {verdict: worse, comparable: <security_key>, basis: [three cited claims, each linked to the
   Thesis / Peers / Model evidence it rests on], as_of: <snapshot date>, marked: machine} -- a person accepts or
   rejects it on the page; the trade pipeline never reads it.

  The "Peers ↔ Posture" analogy is exact and deliberate:
  ┌──────────────────────────────────┬─────────────────────────────────────────────────────────────┐
  │  Peers tab                       │  Posture tab                                                │
  ├──────────────────────────────────┼─────────────────────────────────────────────────────────────┤
  │ the N most similar names on      │ the ONE most similar name on the OTHER side (an Opal        │
  │ ANY side, by the ranker          │ holding for a non-held subject; a non-held name for a       │
  │                                  │ held one), by the SAME ranker                               │
  │ renders multiples side by side   │ renders a judgment over two four-tab evidence packs         │
  │ answers "who is it like?"        │ answers "is it a better or a worse pick than the one we own?"│
  │ no verdict                       │ a verdict, marked machine, for a person to accept or reject │
  └──────────────────────────────────┴─────────────────────────────────────────────────────────────┘
```

Three stories. The **evidence story**: nothing on Thesis or Posture is a bare assertion, every sentence links to the
filing passage or the tab it rests on, so an analyst can dispute a line by reading what it cites. The **identity
story**: one crosswalk resolves a ranked click, a model artifact and a publication association to the same key, so
an empty panel means "not collected" and never "wrong key". The **boundary story**: the ETF plane is read and never
written, Posture is stored and never traded from, and the harvest's mechanism and cadence stay Andrew's.

---

## Appendix -- the AS-BUILT page at the round-10 drain (this seat's `/draw` of ~04:5xZ, before Andrew's page words)

Kept verbatim so the round-11 cut can read the delta: three tabs (Thesis / Peers / Coverage) with the Model tab cut,
the coverage reader on the DynamoDB articles table, no identity crosswalk, no filings analyzer, no Posture.

Every name below is measured from the tree at HEAD, the drain ref, and the live plane tonight. Nothing is invented.

```
SECURITY ANALYSIS (AMGT_RESAPP, D5) -- one page, three stores, four producers, one adapter

1. The data plane -- how the figures, the rankings and the articles are produced

   SOURCES OF TRUTH          PRODUCERS (where they run)        VERSIONED STORES                SERVING ENGINE
   ────────────────          ──────────────────────────        ────────────────                ──────────────
  ┌───────────────┐  DAPI   ┌──────────────────────────┐ raw bytes THEN derived ┌─────────────────────────┐
  │ Bloomberg     │────────►│ AMGT-s-1 model-block job │───────────────────────►│ S3 opal-data-harvest    │
  │ Terminal      │ loopback│ (this box, box-side)     │  per security_key      │  versioning Enabled     │
  │ (this box)    │         └──────────────────────────┘  never overwrite       │  derived/model_block/   │
  │               │  DAPI   ┌──────────────────────────┐                        │   model_block_<key>.json│
  │               │────────►│ price_axis_pull.py       │─── PRICE#<date> rows ─┐│  packs/<key>/status.json│
  │               │ 30-day  │ (box-side, per day)      │   TOP_N ranked        ││  53 objects tonight     │
  │               │ returns └──────────────────────────┘                       │└─────────────────────────┘
  └───────────────┘                                                            │
        ▲  on-demand pull                                                      │
        │  ReceiveMessage / DeleteMessage                                      ▼
  ┌─────┴──────────────────┐  SendMessage   ┌────────────────────┐   ┌─────────────────────────────────────┐
  │ pull_consumer.py       │◄───────────────│ SQS                │   │ DynamoDB opal-harvest-security-     │
  │ (box-side, bounded     │ (ticker,       │ opal-research-     │   │  metrics  HASH axis_date RANGE ticker│
  │  pull+derive <=120 s)  │  security_key, │ pull-requests      │   │  GSI axis-rank-index (rank_sort)     │
  └────────────────────────┘  requested_at) └─────────▲──────────┘   │  partitions written today:           │
                                                      │              │   PRICE#<d>  TRENDING_CHATTER#<d>    │
                              POST /api/private/      │              │   BREAKOUT_CHATTER#<d>  (TOP_N=10)   │
                              research/pull  ┌────────┴──────────┐   │  + firm-scoped star markers          │
                                             │ Lambda            │   └──────────────▲──────────────────────┘
                                             │ harvest_enqueue   │                  │ batch_writer, one
                                             └───────────────────┘                  │ axis_date per day
  ┌───────────────┐ HTTP, paid  ┌──────────────────────────┐              ┌─────────┴─────────────────────┐
  │ Publishers    │ sessions,   │ lib/opal_data_harvest    │              │ Lambda amgt-resapp-chatter-axis│
  │ SA / FT /     │────────────►│ worker.py (this box;     │              │ EventBridge Scheduler          │
  │ Bloomberg /   │ 5 articles  │ Windows task 'Opal Data  │              │ amgt-resapp-chatter-axis-daily │
  │ WSJ / Barron's│ per security│ Harvest - Local          │              │ 30-day window over             │
  │ (5 pubs)      │ = validation│ Publications', DISABLED  │              │ ticker_date_index; re-pointed  │
  └───────────────┘ target only │ after one-shot test)     │              │ at the harvest tables ri-2     │
                                └────────────┬─────────────┘              └─────────▲─────────────────────┘
                                             │ articles: upload mechanism            │ Query per ticker,
                                             │ + cadence RESERVED TO ANDREW           │ published_at window
                                             ▼ (outbox, readback, stable key: his call)│
                                ┌───────────────────────────────────────────────────┴───┐
                                │ DynamoDB opal-harvest-articles                        │
                                │  HASH security_key RANGE published_at                 │
                                │  GSI platform_date_index, GSI ticker_date_index       │
                                └───────────────────────────────────────────────────────┘
                                                              │ Query / GetItem / BatchGetItem  (reads)
                                                              │ PutItem / DeleteItem on star / unstar (writes)
                                                              ▼
                       ┌──────────────────────────────────────────────────────────────────────┐
                       │ Lambda opal-amgt-scoped-api  = lib/research/api/scoped_amgt.py       │
                       │  read_rankings   Query GSI axis-rank-index, axis_date=:ad, presorted │
                       │  read_point      GetItem(axis_date, ticker)                          │
                       │  read_rank_series BatchGetItem, one point per axis_date in window    │
                       │  read_model_block  S3 derived/model_block/model_block_<key>.json     │
                       │  read_security_overlay / read_thesis_bundle  (header + FY figures)   │
                       │  read_peer_set   read_coverage_set (Query opal-harvest-articles)     │
                       │  read_starred / set_starred  (per firm)   refresh: NO queue carrier  │
                       │  env HARVEST_METRICS_TABLE, HARVEST_ARTICLES_TABLE from the resources│
                       │  DEPLOYED tonight (ri-4 drained @50064d78f5, 19 to add / 0 / 0)      │
                       └──────────────────────────────────────────────────────────────────────┘

2. The query plane -- how a PM reaches a ranked name and its pack

    YOU (browser, portal JWT)
        │  "which covered names are moving or being talked about right now, and show me one"
        ▼
   ┌────────────────────────────────────────────────────────────────────────────────────────┐
   │ /security-analysis            /security-analysis/:securityKey     (App.tsx, lazy route) │
   │ ⚠ exists ONLY on refs/drains/rg-2-portal @a845a8be (26 files); the live DEV/PROD        │
   │   checkout at e85f6eb84f carries 0 of them -- PORTAL FROZEN: COMMIT YES / PROMOTE NO    │
   │ ┌─────────────────────────────── header ────────────────────────────────────────────┐   │
   │ │ ticker search          PrintExportAction (Print is an export action, not a tab)   │   │
   │ ├────────────────────────────── LEAD PANEL ─────────────────────────────────────────┤   │
   │ │ movement  [ Trending | Breakout ]   x   subject [ Price | Chatter ]  -> ONE axis   │   │
   │ │ view      [ List | Chart ]                                                        │   │
   │ │  RankedList.tsx  (rank, ticker, score; click-through)  RankedChart.tsx (series)   │   │
   │ │  SecurityOverlay.tsx (header figures + identity_status)  StarredList.tsx (firm)   │   │
   │ │  empty vs ERROR now rendered apart (ri-1, drained @672bca64fe)                    │   │
   │ ├──────────────── tabs ─────────────────────────────────────────────────────────────┤   │
   │ │ ThesisTab  (model block: ~20 line items x 10 FY + ~25 header scalars; Model tab   │   │
   │ │            CUT and rehomed here + overlay)   PeersTab   CoverageTab (articles)    │   │
   │ │ every figure: ProvenanceLine (source, basis, vintage)  CheckFaceBadge (pass/fail)│   │
   │ └───────────────────────────────────────────────────────────────────────────────────┘   │
   └────────────────────────────────────────┬───────────────────────────────────────────────┘
                                            │ hooks/useLeadPanelApi.ts (React Query):
                                            │ useLeadPanelRankings(movement, subject)
                                            │ useRankTimeSeries  useSecurityOverlay  useThesisBundle
                                            │ usePeerSet  useCoverageSet  useStarredList / useSetStarred
                                            ▼
   ┌────────────────────────────────────────────────────────────────────────────────────────┐
   │ HTTP API 7k3ed8px20 (opal-portal-data-proxy-api)  -- authorizer naqxlm, portal JWT     │
   │ 85 routes before tonight + the 11 mounted by scoped-amgt-api.tf (0 collisions):        │
   │  GET  /api/scoped/amgt/lead-panel/rankings/{movement}/{subject}                        │
   │  GET  /api/scoped/amgt/lead-panel/timeseries/{movement}/{subject}                      │
   │  GET  /api/scoped/amgt/watchlist   POST .../watchlist/star   POST .../watchlist/unstar  │
   │  GET  /api/scoped/amgt/security/{security_key}/overlay | thesis | peers | coverage | print │
   │  POST /api/scoped/amgt/refresh                                                         │
   │ firm scoped by the edge's claims; every route CUSTOM auth, none NONE                   │
   └────────────────────────────────────────┬───────────────────────────────────────────────┘
                                            │ AWS_PROXY integration, 29 s ceiling
                                            ▼
                     opal-amgt-scoped-api  ──reads──►  metrics table / articles table / S3 model block
                                            │
                                            ▼
   ANSWER back on the page: "TRENDING x CHATTER, 2026-09-15: rank 00001 BABA US Equity, score 100,
   30-day window; click -> /security-analysis/BABA_US_Equity: Thesis figures with source Bloomberg,
   basis <field>, as of <vintage>, CheckFace PASS; Coverage: 5 admitted items ranked by recency"
   -- TODAY the rankings read shows the seed rows only; the first populated read waits on the
      repointed producer's next fire and the exercise cell ri-3 (in flight), which is the whole
      point of round 10.

  The "ranking is a row, never a render" model is exact and deliberate:
  ┌──────────────────────────┬──────────────────────────────────────────────────────────────┐
  │  the page                │  the pipeline                                                │
  ├──────────────────────────┼──────────────────────────────────────────────────────────────┤
  │ Trending x Chatter click │ one partition TRENDING_CHATTER#<date>, written daily by the  │
  │                          │ chatter-axis Lambda, read back presorted by rank_sort        │
  │ Trending x Price click   │ PRICE#<date>, written box-side from Bloomberg 30-day returns │
  │ a name in the list       │ one item (axis_date, ticker) + its point reads over the window│
  │ the Thesis figures       │ one JSON object under derived/model_block/, raw bytes before  │
  │                          │ derivation, versions accumulate                               │
  │ the Coverage tab         │ a Query on opal-harvest-articles by security_key + date       │
  │ a Star                   │ a firm-keyed marker row; triggers NO harvest                  │
  │ an uncovered ticker      │ POST /api/private/research/pull -> SQS -> the terminal box    │
  │ "the daily job wrote     │ a settled request ERROR, now rendered apart from EMPTY (ri-1) │
  │  no row"                 │                                                              │
  └──────────────────────────┴──────────────────────────────────────────────────────────────┘
```

Three stories live in this diagram. The **freshness story** is that nothing on the page is computed at render time: every ranking is a dated partition and every figure a versioned object, so "what did the page show on the 12th" is a key, not a guess. The **provenance story** is that the model block lands raw before derived and each figure carries its source, basis and vintage to the ProvenanceLine, which is what lets an analyst answer a challenge by pointing at the screen. The **failure story** is tonight's: the page was empty for two independent reasons, a producer failing daily on a deleted table and an API that was never mounted, and the boundary fix means a failed read now looks different from an empty day. What you can ask now that you could not this morning is "is the panel empty because there is nothing, or because something broke", and get a truthful answer from the page itself.
