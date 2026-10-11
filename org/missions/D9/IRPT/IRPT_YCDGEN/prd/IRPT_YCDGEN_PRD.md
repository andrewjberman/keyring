# IRPT_YCDGEN -- the Analysis report generated in house, Opal-branded, with no YCharts call

```json
{
 "project": "IRPT_YCDGEN",
 "directive": "D9",
 "fabric": "dell2",
 "prd_version": "v0.10",
 "step": 4,
 "brief_ref": "docs/briefs/irpt-ycharts-inhouse-generation-feasibility-20261005.md@69141b561e",
 "endpoint_outcomes": ["FWD-1", "FWD-3", "FWD-4", "FWD-5", "FWD-6", "FWD-7", "FWD-8", "FWD-9", "FWD-10", "FWD-11", "FWD-12", "FWD-13", "FWD-14", "FWD-15", "FWD-16", "FWD-17", "FWD-18", "FWD-19", "FWD-20", "FWD-21", "FWD-22", "FWD-23"],
 "status": "RATIFIED"
}
```

Author: `1.0.0_SA_CTO`. D9 / IRPT / laptop. v0.2 of 2026-10-05 replaces v0.1 (@ec37b10ed2 lineage; v0.1's text is in git).
v0.3 (same day) corrects C-CLASSIFY to the table as `2.0.0_SA_COO~M` measured it and points C-REPORT at its design; the ENDPOINT
section is unchanged from v0.2 @4635d40c62.
v0.4 answers `3.0.0_SA_CVO`'s refusal of the v0.2 half (review @3bd1104913): the history line is out of the ENDPOINT block, FWD-16's
ACCEPT carries only Andrew's words, and C-PRICES names its bucket, its universe address and the carrier of the cross-firm rule.
v0.5 takes pricing out of the first version on Andrew's word of 20:50Z (C-V1; the ENDPOINT section is unchanged from v0.4).
v0.6 (clock read 21:31Z) adds the sector pages' scheme to C-CLASSIFY on Andrew's ~21:3xZ word; the ENDPOINT section is unchanged.

**Why v0.2.** Andrew turned the project from "Opal's script on YCharts' data endpoints" to "the report made entirely in Opal's
cloud". Inputs:
- Brief (parent): `docs/briefs/irpt-ycharts-inhouse-generation-feasibility-20261005.md` @69141b561e (`4.0.0_SA_CRO`).
- Brief (addendum): `docs/briefs/irpt-ycharts-inhouse-generation-yfinance-probe-20261005.md` @8e50ace95c (`4.0.0_SA_CRO`).
- Base brief, carried through v0.1: `docs/briefs/irpt-ycharts-direct-generation-opal-branded-brief-20261003.md` @45f673c2ea.
- Andrew's words: `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261005_195xZ_YCDGEN_FIVE_RECS_APPROVED_EXPLORE_YFINANCE.md`
  (five recommendations approved; yfinance for now) and
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261005_202xZ_YCDGEN_INHOUSE_ENDPOINT_THREE_CALLS_ANSWERED_CLASSIFICATION_THROUGH_CANONICAL_TABLE.md`
  (the endpoint's three calls).
- Endpoint: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_FORWARD_IRPT_YCDGEN_INHOUSE_GENERATION_20261005.md` @0bb26ab898,
  confirmed by the second record. FWD-15 was added from his answer to call 2, and FWD-16 from his word of ~20:4xZ
  (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261005_204xZ_YCDGEN_TYPO_AND_SWAP_AI_PIPELINE_CLASSIFY_IN_ETFCLASSIFIER_SHAPE.md`).
  The DONE WHEN lines of FWD-15 and FWD-16 are this seat's wording of his words; he confirmed them at 20:50Z
  (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261005_2050Z_YCDGEN_V1_NO_PRICING_SEAT_COO_Y_DONE_WHEN_CONFIRMED_COO_D_CAN_RIDE.md`).

## ENDPOINT (step 2, /endpoint --forward)

```
  FWD-1  Andrew submits one real Cottonwood portfolio for an Overview and opens an Opal-made
         report in the same sitting, with nothing asked of YCharts
         DONE WHEN  EXERCISED -- one live run, ending in Andrew opening the report
         ACCEPT     Andrew, signed in as himself, submits a real Cottonwood portfolio the way he does
                    today and opens an Opal-branded Overview without coming back to it later. Every
                    figure was worked out by Opal from data Opal already keeps. Nothing was asked of
                    YCharts during the run. A figure Opal cannot work out says so on the page, with the
                    reason. A step that used a saved example fails the outcome
         SOURCE     parent brief section 6, stage 1; addendum section 6; Andrew, call 1

  FWD-3  For each of the three report types, an analyst can point at anything on a YCharts-made
         report and say where it came from
         DONE WHEN  EXERCISED -- an analyst has traced one element of each type
         ACCEPT     for an Overview, a Comparison and a Multi report, every number, table and chart on the
                    page is either tied to a named YCharts answer, or listed plainly as something YCharts
                    works out only inside its own report builder. Nothing on the page is left unaccounted for
         SOURCE     base brief O2; parent brief section 3

  FWD-4  An analyst can make the Comparison and Multi reports too, Opal-branded, with Opal's own
         script
         DONE WHEN  EXERCISED -- one of each made and opened
         ACCEPT     for the same portfolio and comparisons, Opal's script makes a Comparison and a Multi
                    report in Opal's branding without YCharts' report builder. Anything YCharts works out
                    only inside its builder is rebuilt from data Opal holds, or left out with a note saying
                    so. It is never imitated
         SOURCE     base brief O3; parent brief section 6, stage 4

  FWD-5  The Opal-made report and the data behind it are found in Opal's own store, private to the
         client's firm
         DONE WHEN  EXERCISED -- an analyst has found one by its request
         ACCEPT     given a request, an analyst finds its report and the client's own holdings behind
                    it in the client firm's private area. Nobody at another firm can reach them
         SOURCE     base brief O4; parent brief section 4

  FWD-6  A report run is something Andrew waits for at his desk, and every run shows where its time
         went
         DONE WHEN  EXERCISED -- Andrew has waited for one, and its timing record has been read
         ACCEPT     Andrew asks for a report and has it in the same sitting. The run's record shows how
                    long each stage took: reading the holdings, working out the figures, and making the
                    pages
         SOURCE     parent brief section 1 item 4, and section 9

  FWD-7  For the same inputs, an analyst sees which figures on the YCharts report and the Opal report
         agree, and why any differ
         DONE WHEN  EXERCISED -- once for each of the three report types
         ACCEPT     for one report of each type, an analyst lists every figure that matches and every one
                    that differs, each difference with its reason: different dates, a different way of
                    calculating, or something only YCharts works out. It is a one-time check of the new
                    script, not a comparison that keeps running
         SOURCE     base brief O6; parent brief section 6, stage 6

  FWD-8  Opal keeps the market and fund data the report needs for every security a live client
         holds, refreshed on a schedule, so a report never waits on an outside source
         DONE WHEN  EXERCISED -- a scheduled refresh has run, and a report has been made from what it left
         ACCEPT     for each security in a live client portfolio, Opal has its price history as far back
                    as the report's longest period (or as long as the security has existed), and a
                    description of it: for a stock its sector, country and size; for a fund what it
                    holds, what it costs and when it started. Each carries the date it was true. A
                    security Opal has never seen is fetched once, when a client's file first names it.
                    A report made at any hour reads only what Opal already has
         SOURCE     parent brief section 5; addendum sections 3 and 5

  FWD-9  For any figure on an Opal-made report, an analyst can see how it was worked out, from what
         data, and how old that data was
         DONE WHEN  EXERCISED -- an analyst has picked one figure and followed it back
         ACCEPT     an analyst picks any figure and finds the method in words, the holdings it covered
                    and the date of each input. A figure that covers too little of the portfolio, or
                    rests on an input that has gone stale, is printed as not available with the reason,
                    never as a number
         SOURCE     parent brief section 7; RULINGS batch 267

  FWD-10 Returns on the report count dividends
         DONE WHEN  EXERCISED -- one dividend-paying holding checked by hand
         ACCEPT     for one holding that pays dividends, the one-year return on the report equals the
                    price change plus the dividends paid, worked out by hand from the same dates
         SOURCE     parent brief G1; addendum section 5

  FWD-11 Everyone who uses the Analysis tab gets the Opal-made report, and Opal stops calling
         YCharts for it
         DONE WHEN  EXERCISED -- an advisor other than Andrew has submitted a portfolio and opened one
         ACCEPT     after the one-time side-by-side of each report type, and on Andrew's word, an
                    advisor who submits a portfolio gets the Opal-made report. No step signs in to
                    YCharts or waits on it. The old way is switched off in the same change, not left
                    running beside the new one
         SOURCE     parent brief section 6, stage 6, and section 4

  FWD-12 An analyst can run the same portfolio again as another report type, or against another
         comparison, without a fresh wait
         DONE WHEN  EXERCISED -- a second run of one portfolio, timed against the first
         ACCEPT     having made one report for a portfolio, an analyst asks for a second with a
                    different comparison or type and gets it at least as quickly as the first, with no
                    limit on how many they ask for
         SOURCE     parent brief section 1 item 5

  FWD-13 The sector and bond-quality pages show what the client's funds actually hold
         DONE WHEN  EXERCISED -- one fund-heavy portfolio's sector page read against its funds
         ACCEPT     for a portfolio mostly in funds, the sector page adds up each fund's own mix by the
                    fund's share of the portfolio, not one label per fund. Where a fund's mix is not
                    known, as with countries today, the page says so
         SOURCE     parent brief section 1 item 3; addendum sections 3 and 4

  FWD-14 Opal records each day, from Bloomberg, how the funds its clients hold are spread across
         sectors and countries, so a report as of a past date can be made later
         DONE WHEN  EXERCISED -- two days recorded, and the first day's figures read back on the second
         ACCEPT     for the funds live clients hold, each day's spread is kept under its date and is
                    still there the next day
         SOURCE     parent brief section 5; Andrew's card 2 (approved, not started: Bloomberg quota)

  FWD-15 Every security on an Opal-made report takes its name and its classes from Opal's one
         classification table, and a security the table does not know gets a row there
         DONE WHEN  EXERCISED -- a report made for a portfolio holding one security the table did not know
         ACCEPT     each holding on the report shows the clean, properly capitalized name and the asset
                    class and sub asset class that Opal's own table gives it. For a security the table
                    had never seen, a row now exists there, tidied up, and the report used that row. No
                    outside source's own labels are printed in place of Opal's
         SOURCE     Andrew, call 2 (2026-10-05 ~20:2xZ)

  FWD-16 When a client's file names a security Opal cannot place, Opal suggests the security that
         was probably meant, or a comparable one to stand in for it
         DONE WHEN  EXERCISED -- one file with a mistyped ticker and one with a security Opal has no
                    data for, each taken through to a report
         ACCEPT     a mistyped ticker gets a suggested correction that is a real security. A security
                    Opal has no data for gets suggested stand-ins of the same kind, taken first from
                    the funds Opal's own table already knows for stocks, bonds, commodities and the
                    rest. Whatever is accepted has a row in Opal's table, in the
                    same shape as every other security there
         SOURCE     Andrew, 2026-10-05 ~20:4xZ ("typo" check 1 and "swap" check 2)

  FWD-17 When Opal suggests what a flagged ticker probably meant, the advisor can tell from the suggestion
         alone whether it is right
         DONE WHEN  EXERCISED -- one file with a mistyped ticker, the suggestion read on the page by an advisor
         ACCEPT     beside the suggested ticker the advisor sees the security's full name, what kind of
                    security it is, and a short reason it was suggested, and can judge it without opening
                    another site or tool
         SOURCE     check/swap brief O1, R1; Andrew-direct 2026-10-07 ~08:0xZ

  FWD-18 An advisor clears every flagged row of a file quickly
         DONE WHEN  EXERCISED -- one file with three or more flagged rows cleared on the page
         ACCEPT     accepting one suggestion is a single action that takes effect straight away, and
                    one action accepts every corrected-ticker suggestion on the file at once; a
                    stand-in for a different security is always accepted one at a time; nothing is
                    accepted unless the advisor chose it
         SOURCE     check/swap brief O2, O4, R2

  FWD-19 An advisor picks a stand-in for a fund Opal cannot price from a short list, instead of
         recalling a ticker
         DONE WHEN  EXERCISED -- one file with an unpriceable fund, a stand-in picked from the list
         ACCEPT     where no stand-in is suggested, the advisor can search by name or ticker among the
                    funds Opal already knows, and sees each fund's name and kind before picking it
         SOURCE     check/swap brief O3, R5

  FWD-20 Someone reading the report can tell a corrected typo from a stand-in
         DONE WHEN  EXERCISED -- one report read that carries one of each
         ACCEPT     the page and the report say "ticker corrected" for a fixed typo and "stand-in" for
                    a substitute security, and never call a typo fix a stand-in
         SOURCE     check/swap brief O5, R6, R9

  FWD-21 An advisor whose ticker matches several securities picks the one they meant
         DONE WHEN  EXERCISED -- one file with an ambiguous ticker taken through to a report
         ACCEPT     the advisor is shown the possible matches by name and picks one on the page,
                    without editing the file
         SOURCE     check/swap brief O6, R4

  FWD-22 When the check could not run, the advisor is told so plainly and is not told their file
         is wrong
         DONE WHEN  EXERCISED -- one upload where the check is made to fail, read on the page
         ACCEPT     the page says in plain words that the check did not run and that nothing is
                    wrong with the file, and offers to try again; it never shows a raw code
         SOURCE     check/swap brief O7, R3

  FWD-23 There is one place, not two, where an advisor substitutes a security
         DONE WHEN  APPLIED -- the second place is routed into the first or removed
         ACCEPT     every substitution an advisor makes goes through the same suggested and checked
                    path; no screen offers a free-text box that bypasses the checks
         SOURCE     check/swap brief Part VIII, R12
```

## PROVENANCE (outside the ratified section)

- v0.1 to v0.2: FWD-1, FWD-5 and FWD-6 amended in place; FWD-2 retired, its number vacant; FWD-3, FWD-4 and FWD-7 unchanged;
  FWD-8 to FWD-15 added. Ids are permanent.
- Andrew settled: the thread is submitted on the Analysis tab of the development build under his sign-in (call 1); classification
  passes through the canonical table (call 2); FWD-2 is dropped (call 3); Opal's own method, Overview first, no Bloomberg
  query-language purchase, a standing word for pulls scoped to live client holdings, and yfinance for now (the five cards).
- The standing of v0.1's work: the three element maps, the research layout module and its statistics, the keeper and the kept
  YCharts answers all stay. v0.2 changes where the figures come from, not what the page is.
- C-CLASSIFY's reading of the sector pages (Yahoo's sector names there only; names, asset class and sub asset class from the
  table) was confirmed by Andrew at 21:49Z (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261005_2149Z_FIVE_CALLS_ALL_OF_BD_SECURITIES_SIX_ASSET_CLASSES_INDUSTRY_GROUP_ONTO_TABLE.md`, call 4).
- v0.9 (`1.0.0_SA_CTO~DELL2`, 2026-10-07, under NFRA_CTLPLN ADDENDUM v0.12 C-ROLES): FWD-17 to FWD-23 added from the L2 run
  on `docs/briefs/irpt-check-swap-ai-autosuggest-ux-brief-20261007.md` @c16f0f8ddd (`4.0.0_SA_CRO~DELL2`, on Andrew-direct ~08:0xZ,
  record @1ea0796be2: "AI functionalities for autosuggesting swaps of unrecognized securities and associated frontend ops").
  FWD-1 to FWD-16 are unchanged. The seven are emitted by this seat and are NOT YET CONFIRMED by Andrew; the ratified-text half
  re-opens on the ENDPOINT change. Y-5 packet 2 (the web-search swap) is superseded by S32 (msg 120).
- v0.10 (`1.0.0_SA_CTO~DELL2`, 2026-10-07 ~13:4xZ): FWD-18 AMENDED IN PLACE (id unchanged). Bulk accept is narrowed to corrected-ticker
  (typo) suggestions; a stand-in is never bulk-accepted, because it changes what the report measures. Source: the CRO brief section
  4.3b @f9386e5865, E7 ("the case for friction in AI UX: why accept all is the wrong pattern"), found under Andrew's word of ~13:3xZ
  (web search only). Still not confirmed by Andrew. The brief's R13 (remember an accepted correction per firm) is NOT added: whether a
  firm-scoped memory is wanted is a product call left for Andrew.
- A word of his that amends an FWD becomes an addendum under the next unused id (FWD-16), or an in-place amendment. It is never
  a cell's choice.

## CONTRACTS

| Contract | Direction / owner | Binding agreement |
|---|---|---|
| C-SCOPE: in-house generation, one producer per request | Andrew's direction; the standing veto on shadow pipelines | This project builds the Analysis report's generation inside Opal's cloud. Any one request has exactly ONE producer. Until FWD-11, the Opal producer serves only the principals of C-SWITCH; every other request is served by the YCharts path, unchanged. No code path runs both producers on one request, and nothing compares them on a schedule (C-COMPARE is one-time). At FWD-11 the YCharts producer is removed in the same release that opens the Opal producer to everyone. |
| C-SWITCH: who gets the Opal producer before FWD-11 | this project; the served path's owner applies it | Selection is made on the server from the signed-in principal, against one short allow list that starts with Andrew's sign-in only. A client-sent flag never selects the producer. The list changes only on Andrew's word. FWD-11 deletes the list and the branch together. |
| C-ENDPOINTS | RETIRED in v0.2 | v0.1 named YCharts' data endpoints as the source of figures. No figure in an Opal-made report comes from a YCharts call. |
| C-VENDOR: which outside sources, and when | Andrew's cards 1, 2 and 5; his yfinance word | **Yahoo (through yfinance):** allowed for the securities in live client portfolios only. It is called by the scheduled refresh and by the one first-seen fetch (C-MART), never while a report is being made. **Bloomberg:** scheduled batches on the Terminal seat only, `integrations/bloomberg/READ_HERE.md` read first; FWD-14's capture is approved and waits on quota; no cell starts it on a day the quota is spent. **SEC filings:** inside card 1; no cell uses them until a round-N analysis names one. **YCharts:** no call in an in-house run. `2.0.0_SA_COO~Y`'s existing egress word stands for FWD-7 only. A source not named here needs Andrew's word. |
| C-V1: no pricing in the first version | Andrew, 2026-10-05 20:50Z ("let's avoid pricing for the v1") | The first version is the breakdowns: holdings, names and classes, allocation by the table's labels, and the fund look-through pages as their data arrives. Everything that needs a price history is OUT of the first version: returns, risk statistics, the benchmark and risk-free comparisons, FWD-10, FWD-12's timing of price-based re-runs, and the price-history clause of FWD-8. Those elements print as not available with the reason `NOT_IN_THIS_VERSION`. The C-PRICES table, the benchmark read and the risk-free read are NOT built, and no cell is cut for them, until Andrew asks for the price-based pages. Holding weights come from the dollar amounts in the accepted file, never from a price. |
| C-MART: the security data Opal keeps | this project (new tables); the existing Yahoo price pull (extended) | Per security: (1) a daily price history (C-PRICES; deferred by C-V1); (2) a reference snapshot (for a stock: sector, industry, country, market value and the ratios Yahoo serves; for a fund: asset mix, costs, yield, size, start date); (3) a fund look-through (sector weights, credit-quality weights, bond averages, top holdings). Every row carries its as-of date and its fetch date. The universe is the union of securities in live client portfolios; it carries tickers only, never a firm, an account or a weight. A security first named by an upload is fetched once, then joins the schedule. Snapshot fields have no history at the source, so history accrues from the first capture. |
| C-PRICES: the report's price history, in the shared market-data home | this project (new table); CLAUDE.md section 5 (no other firm's bucket) | **DEFERRED by C-V1: specified, not built.** The existing Yahoo price table is `s3://opal-data-bd/silver/historical_prices.parquet` (parent brief M1). `opal-data-bd` is 49financial's firm bucket, so a report for any other firm may NOT read it: that is a cross-firm reference by bucket. The report therefore reads ONE new table, builder output printed at L4: `address('marketdata','global','silver','security_total_return_prices','date=2026-10-05',object='prices.parquet')` -> `s3://opal-data-assets/marketdata/global/silver/security_total_return_prices/date=2026-10-05/prices.parquet`, with the close, the dividend-adjusted close and the dividends as separate named columns, written by the C-MART refresh. **The universe** is `address('marketdata','global','silver','security_universe','date=2026-10-05',object='universe.parquet')` -> `s3://opal-data-assets/marketdata/global/silver/security_universe/date=2026-10-05/universe.parquet`: bare tickers and first-seen dates, no firm, account or weight. **The carrier of the cross-firm rule:** a ticker reaches the universe only when a firm's OWN step pushes it (the upload's resolution, or that firm's own holdings job); no global job reads a firm bucket to build it, and no firm-scoped job reads another firm's bucket. `.tools/ds-precommit-check.py`'s foreign-bucket limb grades the refresh and the producer like any pipeline tree. The `opal-data-bd` table is not read, not modified and not extended by this project; folding that pull into the shared home is its own migration (R19), never a rider here. |
| C-STORE: addresses from the builder | CLAUDE.md rule 30; X10 | **Where each object lands (corrected at v0.7 and v0.8):** `run.json` is written to the FIRM bucket through the research role (`opal-data-cottonwood`, table `ycharts_runs`, the generic builder's address below). The report PDF and the Opal document are RETAINED artifacts, written to the reporting policy's registered destination, never through the generic builder: `opal_naming.reporting_destination('cottonwood','YCHARTS_OPAL_REPORT', <ART>, <digest>, policy_revision='irpt-ycdgen-research-v1')` -> `('opal-data-irpt', 'irpt/cottonwood/state/ycharts_opal_reports/<ART>/<digest>.pdf')` (READ 02:23Z 2026-10-06), the same bucket-and-firm-prefix shape as every `irpt-x10-v1` family; firm separation there is the key prefix plus IAM. The generic-builder addresses below, which name the firm bucket, were v0.1's and do not describe where the producer writes: `address('irpt','cottonwood','state','ycharts_runs','request=<REQ>',object='run.json')` and `address('irpt','cottonwood','state','ycharts_opal_reports','request=<REQ>',object='overview.pdf')` (X10 row `irpt-ycdgen-research`). Renaming them is not this revision. **New, builder output printed at L4 (2026-10-05 ~20:4xZ), beside C-PRICES' two:** `address('marketdata','global','silver','security_reference','date=2026-10-05',object='reference.parquet')` -> `s3://opal-data-assets/marketdata/global/silver/security_reference/date=2026-10-05/reference.parquet`; `address('marketdata','global','silver','fund_lookthrough','date=2026-10-05',object='lookthrough.parquet')` -> `s3://opal-data-assets/marketdata/global/silver/fund_lookthrough/date=2026-10-05/lookthrough.parquet`. `opal-data-assets` is a shared bucket: these tables hold public market data only (C-MART's universe rule). **Raw Yahoo answers:** `address('yahoo', ...)` is REFUSED today ("source 'yahoo' is not a systems.json key", READ at L4). Round 1 adds the `yahoo` vendor row to `infra/logic/registry/systems.json`; the order that writes raw answers prints the builder's output after the row lands. No address is typed by hand. |
| C-REGISTER: registry rows before writes | this project, round 1 | (1) the `yahoo` vendor row in `systems.json`; (2) the X10 families for each new `marketdata` table a round writes (first version: `security_reference`, `fund_lookthrough` and `security_universe`), in the grammar of the sibling families. Each lands before any object is written under it. Resource names are `name()` output printed in the order: `name('marketdata','global','security-reference-refresh','lambda')` -> `marketdata-global-security-reference-refresh-lambda` (READ at L4). The schedule's name is printed by its order; `name(..., 'schedule')` is refused, and the kind is a cadence. |
| C-SCHEDULE: production refresh is scheduled | law (CLAUDE.md section 5) | The reference and look-through refresh runs on its own daily schedule, on the trading-day frontier of `lib/trading_calendar.py`. An ad hoc run is QA and is never the acceptance of FWD-8. |
| C-CLASSIFY: one classification table | Andrew, call 2; the table is MDPF_SECCLASS's | Every name, asset class, sub asset class and sector the report prints FOR A SECURITY is read from `etf-classifications` through its one client (`infra/aws/lambda/v2_portal/_shared/etf_classifications_dynamodb.py`). A security the table does not hold gets a row added by the table's own classifier mechanism, cleaned and properly capitalized; Yahoo's labels are an INPUT to that row and are never printed in its place. This project adds no second writer to the table: it asks for the row through MDPF_SECCLASS's mechanism, and until the row exists the holding prints as not yet classified. **The table as measured by `2.0.0_SA_COO~M`** (`org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/ETF_CLASSIFICATIONS_VOCABULARY_AND_UNKNOWN_ROW_PATH_20261005.md` @73a3c60af8; 3,493 rows): `asset_class` has 6 values; the GICS sector names ARE the equity `sub_asset_class` values, with no separate sector field; the legacy `sector` attribute (179 rows) is a different grain and is NOT read by this project. So a stock's sector on the report is its `sub_asset_class` where that is a GICS name, and a fund's sector weights are keyed to those same ten names plus Real Estate. **An unknown security gets a row today** only through the scheduled plan and one conditional put, from a direct match in an existing source; a security with no direct match gets no row and is listed UNRESOLVED; no model is called. A model verdict fits the row shape only as `classified_by model` with its confidence fields, landed from a reviewed set (13 rows). Andrew's AI classifier is put in service by MDPF_SECCLASS PRD FWD-11, and this project consumes the row it writes. **The sector pages, while Yahoo is the source (Andrew, ~21:3xZ at the research seat's terminal, `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261005_213xZ_THREE_RECS_APPROVED_AND_CIK_QUESTION.md`, card 2: "Yahoo's scheme for now, stated on the page; switch to GICS when the canonical table is the sector source for the report"):** a page that adds up sector weights, a fund's look-through mix included, prints Yahoo's sector names and says so on the page. This is the one place a source's own labels are printed, because the table has no sector field yet and a fund's sector weights arrive keyed to those names. A security's NAME, asset class and sub asset class still come from the table alone. The pages switch to the table's sector field when MDPF_SECCLASS FWD-12 has landed it. |
| C-RESOLVE: the typo check and the swap check | Andrew, ~20:4xZ; the intake gate is IRPT_BCKEND's | The upload's two advisory checks exist: `check` (a likely ticker for a row not found) and `swap` (a stand-in), in `intake/upload_suggestions.py` and `intake/resolution_kimi.py`, on an AI model, advisory until the person accepts. Today both are VERIFIED against YCharts (`intake/security_resolution.py` reads its `securities_info`), and `swap` refuses pending vendor QA. In house: (1) a suggestion is verified against Opal's own data, that is, the security exists in C-MART or is fetched once as first-seen; (2) a swap's candidates come FIRST from `etf-classifications` rows of the same asset class and sub asset class, ETFs before other kinds (Andrew's recommendation), and only then from the model's own proposal; (3) the security given, and the security accepted, are each classified in the table's row shape through C-CLASSIFY; (4) nothing is substituted until the person accepts, as today. Which model runs the advice is not decided here; the existing advisory is the starting point. |
| C-METHOD: Opal's own method, stated | Andrew's card 3 | (The return, benchmark and risk-free lines apply when C-V1 lifts.) Total return (C-PRICES' adjusted close, or close plus dividends). Benchmark: the S&P 500 total return series Opal holds. Opal-defined market-value buckets, for the stock sleeve. No style box. Top holdings of a fund are the ten the source serves, and the page says ten. Each method is printed in words on the page it governs. **Risk-free rate:** the Bloomberg 3-month yield Opal already receives each morning (no new call). The FRED object is not used while row `IRPT_YCDGEN-S9` is open. |
| C-COVERAGE: print or "not available" | RULINGS batch 267; decomposition contract 3.5 | A figure that aggregates across holdings prints only when the holdings with an answer are at least 0.95 of the portfolio by weight; otherwise `NOT_AVAILABLE` with `COVERAGE_BELOW_0.95`. A per-holding figure prints for the holdings Opal has. An input older than its own declared age limit fails the figure with `STALE_INPUT` and its date; it never prints. Two states only: a value, or not available with the reason. |
| C-RUN: the run record | this project | `run.json` per request holds: the request (portfolio, type, comparisons, window); each input read with its as-of date; one entry per report element with `method`, `inputs`, `coverage`, `status`, `reason`; and stage timings on three clocks: reading (holdings and data), computing, rendering. No time target is typed; FWD-6's bar is Andrew's own sitting. |
| C-REPORT: the page's contract | IRPT_BCKEND owns `AnalysisReport`; this seat amends it | `AnalysisReport` v1 requires `vendor_artifact` and `effective_inputs.read_back`, which describe a vendor PDF. The Opal producer needs a form without them, on the precedent of `PerformanceReport`'s `provider: OPAL_ENGINE`. The design is `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_DESIGN_ANALYSISREPORT_OPAL_PRODUCER_FORM_20261005.md`: `AnalysisReport` v2 with a `provider` discriminator, where the Opal form carries `opal_artifact`, `inputs_as_of`, per-section `status`, `method` and `coverage`, and `computation_validation`. The contract's source of record is IRPT_BCKEND's PRD CONTRACTS table; this seat lands the row there at that project's next round boundary, before the thread's page hop is cut. |
| C-BRAND: Opal's branding | this project; the export path's assets | Unchanged from v0.1: the approved brand asset set by revision; no YCharts logo, layout imitation or wording. |
| C-BUILDERONLY: never imitated | FWD-4; base brief PART III item 5 | Unchanged from v0.1, and now the rule for every element: rebuilt from data Opal holds with its method stated, or left out with a line saying it is not available. Nothing is approximated to look like YCharts' figure. |
| C-KEEP, C-SESSION | v0.1; not used by an in-house run | The kept YCharts answers stay where they are. An in-house run opens no YCharts session and takes no lease. |
| C-SECRET, C-FIRM | law | Unchanged from v0.1. Client holdings, run records and reports live only in the client firm's bucket. The shared market-data tables carry no client fact. Git holds no client figure. |
| C-COMPARE: one-time, per type | FWD-7; the standing veto on parity comparators | For one report of each type, against a RETAINED YCharts PDF of the same inputs. Each figure is `MATCH` or `DIFFER`, each DIFFER with one reason from `AS_OF`, `CONVENTION` or `BUILDER_ONLY`. Once per type; nothing schedules or repeats it. Where no retained PDF matches the inputs, one served run by `2.0.0_SA_COO~Y` supplies it. |
| C-MORATORIUM: no alerts | law | No alarm, SNS, SES send, freshness checker or monitor. A stale input fails the figure on the page (C-COVERAGE); a failed refresh is a row and a run record. |
| C-DELIVERY: the page opens the report | FWD-1; Andrew, call 1 | The report opens from the Analysis tab's own status and section view. v0.1's printed signed link is withdrawn. |

## 1. The arc

**Start.** The Analysis tab's reports are made by YCharts: a resident worker signs in, uploads the holdings, holds 900 seconds
for the vendor's firewall, and downloads a PDF that Opal re-reads figure by figure. Rounds 1 to 5 of this project built the
element maps of all three report types, a research layout with its statistics, and a store of kept answers.

**End.**
- An advisor submits a portfolio on the Analysis tab and gets a report Opal made from data Opal keeps.
- That data is refreshed on a schedule for every security live clients hold, and every figure says how it was made and from
  what date.
- Every security's name and classes come from the one classification table.
- A one-time check per type has said which figures agree with YCharts and why any differ, and the YCharts calls have stopped.

## 2. THREAD -- FWD-1, one Cottonwood Overview end to end

1. **Submit.** Andrew, signed in as himself on the development build of the Analysis tab against the real backend, submits the
   reference Cottonwood portfolio for an Overview. Intake, acceptance and the job row are unchanged.
2. **Select.** The server reads his principal against the allow list and gives the request to the Opal producer (C-SWITCH).
3. **Read.** The producer reads the accepted holdings from the firm's store and resolves each to a security.
4. **Classify.** Each security's name and classes are read from the classification table (C-CLASSIFY).
5. **Data.** The producer reads what the first version's pages need from Opal's store: the fund look-through and reference
   rows that exist for the portfolio's securities (C-MART). Nothing is fetched from outside during the run.
6. **Compute.** Weights from the accepted dollar amounts; allocation by asset class and sub asset class; the look-through
   pages under the coverage rule (C-COVERAGE). Price-based elements are marked not in this version (C-V1).
7. **Render and record.** An Opal-branded Overview, and `run.json` with the trace and the three clocks (C-BRAND, C-RUN).
8. **Open.** The status reads ready in the Opal form of the report contract (C-REPORT), and Andrew opens it on the page.

Round 1 builds only this thread: cover, holdings with the table's names and classes, and allocation by asset class and sub
asset class. A row Opal cannot yet compute says so with the reason. The cells are the COO's to cut at L5, over these hops. What
round 1 needs that does not exist yet: the Opal form of C-REPORT and the C-SWITCH branch.

## 3. ENRICHMENT BACKLOG (ordered, one line each)

1. The scheduled refresh of reference and look-through data for the client-holdings universe, with the first-seen fetch (FWD-8).
2. The trace followed back by an analyst (FWD-9).
3. A security the table did not know, through the table's own mechanism, onto a report (FWD-15).
3a. The typo and swap checks verified against Opal's data, with swaps drawn first from the table's ETFs (FWD-16).
3b. The check/swap page made easy to use (FWD-17 to FWD-23). FWD-22, FWD-18 and FWD-17 come first: they work on today's
    check and need no new data. FWD-19 reuses the fund list the page already loads. FWD-21 and FWD-20 come next. FWD-23 is
    a product cut decided in the cell (route the second box into the checked path, or remove it).
4. Sector and bond-quality pages from fund look-through, after MDPF_SECCLASS states the sector vocabulary (FWD-13).
5. DEFERRED by C-V1, on Andrew's word only: the price table, returns and risk, dividends (FWD-10), long windows.
6. Comparison and Multi (FWD-4), then a timed second run of one portfolio (FWD-12).
7. The timing read (FWD-6) and the firm-private read (FWD-5).
8. The analyst's trace of one element of each YCharts type (FWD-3).
9. The one-time side-by-side per type (FWD-7), then the release and the removal of the YCharts producer on Andrew's word (FWD-11).
10. The daily Bloomberg fund capture, on a day with quota (FWD-14).

## 4. Engines (one row per engine)

| Engine | Serving shape | Role here | Deploy mechanics |
|---|---|---|---|
| the Opal producer (`infra/aws/lambda/investor-reporting/ycharts/research/`: `layout_overview.py`, `held_data.py`, the runner) | today an on-demand research run; in v0.2 the producer the generation worker calls for C-SWITCH principals | reads, classifies, computes, renders, records | the existing resident host and renderer; no new compute class (parent brief section 4, INHERITED) |
| the served generation worker and queue `irpt-generation` (IRPT_BCKEND) | the resident worker | carries the C-SWITCH branch | IRPT_BCKEND's release path, under a never-widen half |
| the reference and look-through refresh (NEW) | a scheduled daily job | C-MART tables | names and addresses from the builders (C-STORE, C-REGISTER) |
| the classification table and its classifier (`etf-classifications`; MDPF_SECCLASS) | one table, one client | C-CLASSIFY | MDPF_SECCLASS; consumed |
| the Bloomberg morning pull (the Terminal seat) | scheduled batches | the risk-free series (held); FWD-14's capture | `integrations/bloomberg/READ_HERE.md` first |
| the export path's brand assets (`export/bundle.py`) | the approved asset set by revision | C-BRAND | IRPT_BCKEND; read only |

## 5. WORKSTREAMS AND OWNERS

- **One workstream, issued by `2.0.0_SA_COO~Y`.** That lane is not seated at this writing; seating it is Andrew's word.
- **Write surface:** `ycharts/research/` and its tests; the C-MART refresh job and its tables; the registry rows of
  C-REGISTER; `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/`.
- **Written through another owner's release, as a named cell with its half:** the C-SWITCH branch in the served worker
  (IRPT_BCKEND).
- **Not written here:** `etf-classifications` (MDPF_SECCLASS, `2.0.0_SA_COO~M`); the `AnalysisReport` contract file (this
  seat); the session and lease modules; the export path.
- **L4-R:** the ENDPOINT changed, so `3.0.0_SA_CVO` re-signs the ratified-text half. The CRO wrote both briefs, so the brief
  half is accepted by authorship (proportionate sign-off).

## 6. Rulings closed at L4 (no decide-first question enters L5)

1. One producer per request; the Opal producer serves only the allow list until FWD-11; the list is server-side (C-SWITCH).
2. Nothing is fetched from an outside source while a report is being made (C-VENDOR, C-MART).
3. The report's price history is one new table at the shared market-data address; the 49financial-bucket price table is not read
   and not changed (C-PRICES).
4. New market-data tables live at the `marketdata` / `global` builder addresses; raw Yahoo answers wait for the `yahoo` registry
   row (C-STORE, C-REGISTER).
5. A security's printed name and classes come from the classification table only; this project never writes that table
   (C-CLASSIFY).
6. Opal's own method, stated on the page; no style box; the risk-free rate is the Bloomberg series already received (C-METHOD).
7. A value or "not available with the reason"; the 0.95 weight floor binds every aggregate (C-COVERAGE; batch 267).
8. The run and report tables keep v0.1's names (C-STORE).
9. The side-by-side is one-time per type and precedes the release; the release removes the YCharts producer (C-COMPARE, FWD-11).
10. FWD-14 does not start on a day the Bloomberg quota is spent, and no round waits for it.
10a. The first version carries no price-based content and builds no price table (C-V1).
11. Any new capability is a PRD addendum under the next unused FWD id.

## 7. SURFACE MANIFEST (step 4 -> step 5)

`claim`: `measured` = read at L4 by this seat (2026-10-05 ~20:3xZ to ~20:4xZ); `held` = taken from the briefs (`4.0.0_SA_CRO`'s
measurements, not re-read); `unmeasured` = new. v0.1's rows S01 to S12 are in git; S02, S04 and S09's maps are built, and S03
and S05 are not used by an in-house run.

| id | outcome_ref | surface | claim | evidence | lane | verb | depends_on | bound |
|---|---|---|---|---|---|---|---|---|
| S13 | FWD-1, FWD-11 | the C-SWITCH branch in the served generation worker | unmeasured | C-SWITCH | ~Y, through IRPT_BCKEND's release | wire | S20 | server-side; never-widen half |
| S14 | FWD-1 | the Opal producer reading accepted holdings from the firm's store | held (handoff; 99 holdings read by the CRO) | parent brief section 2 | ~Y | wire | -- | no saved example |
| S15 | FWD-1, FWD-15 | the classification read through the one client | measured (client's record shape carries `asset_class`, `sub_asset_class`, `sector`, `name`) | client file header | ~Y | consume | -- | no second writer |
| S16 | FWD-10 (DEFERRED by C-V1; `security_universe` alone moves to S22) | `security_total_return_prices` and `security_universe` at the `marketdata`/`global` builder addresses | measured (addresses printed); coverage held (addendum: 98 of 99 on yfinance) | C-PRICES | ~Y | wire | S21 | no firm bucket read; tickers only |
| S17 | DEFERRED by C-V1 | the S&P 500 total return series and the Bloomberg 3-month yield | held (INHERITED in the brief) | parent brief G3, G4 | ~Y | measure, then consume | -- | row S9: no FRED |
| S18 | FWD-1, FWD-9 | the computed trace and coverage rule in `layout_overview.py` | held (methods exist; floor per batch 267) | parent brief section 3 | ~Y | wire | S22 | two states only |
| S19 | FWD-1, FWD-6 | `run.json` v2 with inputs' dates and three clocks | unmeasured | C-RUN | ~Y | wire | S18 | no client figure in git |
| S20 | FWD-1, FWD-11 | the Opal form of `AnalysisReport` | measured as absent by the brief's contract note; not re-read | C-REPORT | this seat | amend | -- | lands before S13 |
| S21 | FWD-8 | registry rows: `yahoo` in `systems.json`; X10 families for the tables a round writes | measured (`address('yahoo',...)` refused; `marketdata`/`global` addresses printed) | C-STORE | ~Y | wire | -- | before any write |
| S22 | FWD-8, FWD-13 | the scheduled refresh writing `security_reference` and `fund_lookthrough` | unmeasured; yfinance coverage held (addendum section 3) | C-MART | ~Y | wire | S21 | universe carries tickers only |
| S23 | FWD-8 | the first-seen fetch at upload resolution | unmeasured | C-MART | ~Y | wire | S22 | once per security |
| S24 | FWD-15 | a row requested through MDPF_SECCLASS's classifier for an unknown security | unmeasured | C-CLASSIFY | ~Y asks; ~M's mechanism writes | consume | S15 | no second writer |
| S25 | FWD-13 | sector and credit-quality pages from look-through | unmeasured | C-CLASSIFY (vocabulary owed by MDPF_SECCLASS) | ~Y | wire | S22 | "not available" for countries |
| S26 | FWD-4, FWD-12 | Comparison and Multi through the Opal producer; a timed second run | held (maps READY) | round-5 grade | ~Y | wire | S18 | same store |
| S27 | FWD-7 | the one-time side-by-side record per type | unmeasured | C-COMPARE | ~Y | measure | S26 | once per type |
| S28 | FWD-11 | the release: allow list and YCharts producer removed together | unmeasured | C-SCOPE | ~Y, on Andrew's word | wire | S27 | one change |
| S29 | FWD-14 | the daily Bloomberg fund-allocation capture | held (proven on ETFs; untested on mutual funds) | parent brief G6 | ~Y | wire | quota | READ_HERE first |
| S30 | FWD-1..FWD-16 | the journey test across the thread, reading served artifacts | unmeasured | the ACCEPT lines | verification | verify | S19 | reads the store |
| S31 | FWD-16 | the check gate's verification moved from YCharts' `securities_info` to Opal's data | measured (file headers: `upload_suggestions.py:1-10`, `security_resolution.py:1-22`) | C-RESOLVE | ~Y, through IRPT_BCKEND's release | wire | S22, S23 | advisory until accepted |
| S32 | FWD-16 | swap candidates from `etf-classifications` by asset class and sub asset class, ETFs first | measured (`resolution_kimi.py:1-22`: swap refuses today) | C-RESOLVE | ~Y | wire | S15, S31 | the table first, the model second |
| S33 | FWD-17 | the verified suggestion keeps the security's name, kind and the model's reason (`intake/upload_suggestions.py`; the provider row requires `security_name`, `security_resolution.py:44-49`) and the review card shows them (`tabs/analysis/ProspectComposer.tsx`) | measured (brief Part VIII 8.1) | check/swap brief R1 | ~G2 (intake), page lane | wire | S31 | no numeric confidence until calibrated |
| S34 | FWD-18 | one-action accept and accept-all on the review card; the re-post already takes 1-20 corrections (`prospect.ts:74`) | measured (brief 4.4) | R2 | page lane | wire | -- | explicit choice only |
| S35 | FWD-19 | a typeahead over the `etf-classifications` list the page already fetches (`comparisonCatalogue.ts`; pattern `TradeSubmission/components/TickerAutocompleteInput.tsx`) | measured (brief 4.3) | R5 | page lane | wire | -- | no new route |
| S36 | FWD-20 | the correction records its origin (corrected vs stand-in) on the wire and in the disclosure; the check returns a kind (`resolution_kimi.py`) | unmeasured (wire owned by the P lineage) | R6, R9 | ~G2 + P lineage | amend | S33 | wording on page and report |
| S37 | FWD-21 | an AMBIGUOUS finding carries the provider's candidates and the select action the resolver computes (`portfolio.py:444`) | measured (brief 4.2 step 5d) | R4 | ~G2, page lane | wire | -- | -- |
| S38 | FWD-22 | words and a retry action for `TICKER_CHECK_UNAVAILABLE` (`uploads.py:40-53`) | measured (brief 4.2 step 5e) | R3 | ~G2, page lane | amend | -- | locked copy test |
| S39 | FWD-23 | the free-text substitution box in `tabs/analysis/InputReview.tsx` (mounted at `AnalysisTab.tsx:418`) routed or removed | measured (brief Part VIII 8.2) | R12 | page lane | amend | S34 | one path |

MECE check: every one of the 22 live outcomes has a row (FWD-3 and FWD-5 ride S26/S30 and v0.1's built maps and S10).

## 8. BRIEF COVERAGE -- content carried, not just cited

| Brief heading | Carried content | Consuming sections / surfaces |
|---|---|---|
| Parent 1 (verdict) | nothing is YCharts-only; prices cover 96 of 99; fund look-through is the build; the wait disappears; re-runs are free | ENDPOINT FWD-1, FWD-8, FWD-12, FWD-13; arc |
| Parent 2 (measurements) | M1 prices; M4 unlabelled kinds; M6 stale risk-free; M7 element classes | S16, S15, S17; C-METHOD |
| Parent 3 (element classes) | 25 percent ready, 17 percent on held data, 58 percent on a reference mart | C-MART; backlog 1, 4 |
| Parent 4 (process; contract note) | which steps go; `AnalysisReport` assumes a vendor PDF | section 2; C-REPORT; S20 |
| Parent 5 (gaps G1-G11) | G1 C-PRICES; G2 backlog 5; G3 and G4 C-METHOD; G5 to G7 C-MART; G8 to G11 partly served by Yahoo, the rest "not available" | C-PRICES, C-MART, C-METHOD, C-COVERAGE |
| Parent 6 (sequence) | the thread, then enrichment; the one-time acceptance | sections 2 and 3 |
| Parent 7 (risks) | mixed price series; coverage elsewhere; stale inputs; contract change on a served page | FWD-10; C-COVERAGE; C-REPORT; C-SCOPE |
| Parent 8 (five decisions) | all approved by Andrew | C-METHOD, C-VENDOR; ruling 6.10 |
| Parent 9 (not claimed) | run time unmeasured; no figure compared; one portfolio | FWD-6; FWD-7; S-row claims marked `held` |
| Addendum 3 (what Yahoo returns) | adjusted close and dividends; stock reference; fund mix, sectors, costs, credit quality, top ten | C-MART; C-METHOD |
| Addendum 3 (sector names) | Yahoo's names match YCharts' scheme | superseded by Andrew's call 2: C-CLASSIFY |
| Addendum 4 (what Yahoo lacks) | fund countries; top 25; maturity buckets; style box; loads; history of snapshots | C-COVERAGE ("not available"); C-METHOD; FWD-14 |
| Addendum 5 (conditions) | unofficial reader; fetch on a schedule; source's own as-of date; one portfolio; fix the price columns first | C-VENDOR; C-SCHEDULE; C-MART; C-PRICES |
| Check/swap brief (2026-10-07, Parts I, IV, VIII) | O1-O7 and R1-R12; packet 2 superseded by S32; external patterns not researched (egress) | ENDPOINT FWD-17 to FWD-23; backlog 3b; S33-S39 |
