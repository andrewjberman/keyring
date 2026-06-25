# DIVZ/IDVZ ETF-price "staleness" DX -- DISPOSITION: BENIGN CADENCE (no break, no fix)

**Agent:** 0.5.0_AE_OpalETL | **Date:** 2026-06-25 | **archetype:** DIAGNOSE
**Trigger:** COO GO (172219Z) -- CVO flagged DIVZ/IDVZ etf_net_assets @06-23 in the MDPF close-verify (Finding B). Break-vs-cadence, then fix-or-clear (Rule 22).
**Verify:** CVO (raised it). **Disposition:** CLEARED -- correct-as-is.

## Verdict

NOT a break. The DIVZ/IDVZ "@06-23 on 06-25" vintage is the **structural T+1 issuer-valuation lag of the TrueShares net-assets feed** -- consistent across all history, with daily-updating values. No producer failure, no fix. The CVO flag is correctly DISPOSITIONED as benign cadence.

## Grounding (Rule 22 -- source + content, no inference)

1. SYMPTOM (served): `s3://opal-data-portal-v2/platinum/mdpf/aggregate_aua/2026-06-25.json` `source_vintage.by_feeder.etf_net_assets` = {DIVZ: 06-23, IDVZ: 06-23, PFDE: 06-24, PFOE: 06-24}. A DIVZ/IDVZ-specific 1-day lag vs PFDE/PFOE.

2. FEEDER STAMPING (mechanism): `data/mdpf/scripts/gold/build_mdpf_wsd2_etf_netassets_feeder.py` selects the latest row per ticker by the `date` column (:129-131) and stamps the output `as_of_date` from that row's **`data_as_of`** field (:146 `"as_of_date": r.get("data_as_of")`; docstring :22, :117-119 -- "the as_of_date output column records the actual valuation date so any roll-forward is audit-visible").

3. SOURCE CADENCE (the root, `s3://opal-data-etfs/silver/netassets_daily.parquet`):
   - **DIVZ/IDVZ (source=`trueshares`, source_system=`etf_netassets_watch`):** `data_as_of` consistently = `date` - 1 trading day. Full recent history (date -> data_as_of): 06-16->06-15, 06-17->06-16, 06-23->06-22, 06-24->06-23 (lag=1 every weekday; lag 3-4 entries are Fri->Mon weekend gaps). The TrueShares issuer publishes the file on day D carrying its as_of valuation for D-1.
   - **PFDE/PFOE (source=`filepoint`):** `data_as_of == date` (lag 0) -- same-day valuation.
   - VALUES UPDATE DAILY (not frozen): DIVZ nav 37.23(06-22)->37.31(06-23)->37.70(06-24), net_assets 263.99M->264.54M->268.39M; IDVZ nav 34.41->34.37->34.20. The latest DIVZ/IDVZ draw (date=06-24) carries fresh values, stamped issuer-as_of 06-23.

4. BY DESIGN excluded from the freshness gate: the served `source_vintage.vintage_bearing_feeders = [model_aua_positions, non_model_aua]` -- `etf_net_assets` is NOT vintage-bearing; `overall: 2026-06-25, status: current`. The 1-day issuer lag is already tolerated/excluded from MDPF's freshness determination (CVO noted this: "excluded-from-overall + overall=current").

## Why CVO saw it / why it's benign

CVO's MDPF close-verify (16:23Z) surfaced DIVZ/IDVZ @06-23 and correctly flagged it as worth-a-look (not a defect call). Ground truth: TrueShares' T+1 issuer-as_of cadence makes the latest DIVZ/IDVZ valuation always read one day behind the draw date. Opal cannot make TrueShares strike a NAV faster; the data IS the latest available issuer valuation. PFDE/PFOE differ only because FilePoint values same-day.

## Disposition

- CLEAR -- correct-as-is, no change. The producer (`etf_netassets_watch`) is healthy (daily writes through 06-24; file mtime 06-24T22:00Z; 06-25 row lands 06-25 evening on the watch's ~22:00Z cadence).
- OPTIONAL non-urgent observability nicety (NOT a fix, flagging for the record): the served `source_vintage` stamps DIVZ/IDVZ at issuer `data_as_of` (06-23), which reads as "stale" to a verifier even though the draw is current (06-24, daily-updating). A future enhancement could surface both the draw-date and the issuer-as_of (or annotate the known TrueShares T+1 lag) so this 1-day issuer lag doesn't re-trigger a staleness flag. Low priority; the data is correct.

## Compiler Tools

| Tool | Call | Result |
|---|---|---|
| comp-which | route DIVZ/IDVZ price-source/freshness question | PASS (routed to comp-freshness/pipescript) |
| comp-freshness | artifact opal-data-etfs/silver/netassets_daily + mdpf feeder etf_net_assets | PASS (both file-fresh; symptom is data-vintage, not file age) |
| pipescript --resource | netassets_daily (producer) | MISS (ETFS netassets producer not in a pipescript thread -- gap) |
| comp-glob | locate ETFS netassets producer scripts | PARTIAL (found feeder + etfs/gold; the silver netassets producer is the etf_netassets_watch ingest, not in data/etfs/scripts) |

Gap: the ETFS silver netassets producer (`etf_netassets_watch`) is not registered in pipescript/comp-pipescript -- the DIVZ/IDVZ source lineage was grounded by reading the parquet's `source`/`source_system`/`data_as_of` columns directly. Worth a pipescript fill (alongside the MDPF-pipeline registration gap).
