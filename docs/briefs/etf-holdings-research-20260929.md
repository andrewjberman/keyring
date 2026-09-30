# Rival funds: daily holdings, canonical shape, served research page

L1 BRIEF | NEW | Author: 4.0.0_SA_CRO~Z | September 29, 2026 | **Revision 2, September 29 ~23:5x ET**, folding Andrew's rulings on the 14-item gap pass (verbatim in the linked `ANDREW_DIRECT.md`)

Andrew's direction is a lightweight research product, **rivalfunds**, over six rival active ETFs: WCMG, GQGU, TSEL, BASG, ETFT and PCLG. Collect every fund's disclosed holdings daily, backfill up to two years (bounded by each ETF's own history), coalesce every source shape into one Opal-defined master table, compute change and performance tables from it, and serve a daily research page with chart views and AI analyses at `mcp.opalinvest.dev/rivalfunds`, archived by day. Less frequent disclosures are acceptable where daily history does not exist; they stay identifiable as such.

**Recommendation:** issuer-first daily collection for all six under a new, separate pipeline, `etfs-rivalfunds-daily`, fired at **7:00 AM ET**. Bloomberg's existing **8:03 AM ET** morning run is the fallback for funds Bloomberg carries, and the supplier of backfill and enrichment (prices, total returns, GICS, benchmarks). The backfill runs ad hoc from the outset through BOTH channels: issuer archives for GQGU and BASG, Bloomberg Excel BQL for WCMG, TSEL, ETFT and PCLG. Each stage hands the next a batch-complete marker; a daily schedule backstops every hop. OpenAI writes the analyses from computed tables. Everything, bronze through platinum, lives in `opal-data-etfs`.

Supporting design: [table, prompt, naming and serving specification](../../org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/AMGT_RECONN_SOURCES_20260929/GOLD_TABLES_AND_PROMPTS.md). Direct instructions and source evidence are linked in the references.

## PART I — THE OUTCOME TERRITORY

### O1 — Andrew opens one ETF's day on the served page and traces a change to its source

**Candidate thread first:** Andrew opens `mcp.opalinvest.dev/rivalfunds`, selects BASG, and reads the latest genuinely dated holdings report against the prior one: the change tables as charts, and an evidence-linked AI account of what changed and what cannot be inferred. He can trace a highlighted holding back through the canonical table and typed silver to the issuer's raw bytes. The page he reads is the day's archived served file, and `/rivalfunds/archive` lists every published day. This is one real use over real holdings, ending in Andrew's observed research result; it crosses every hop in PART V once. The broader research window is the available history up to two years.

### O2 — Andrew obtains the best available history without mistaking stale snapshots for daily disclosure

Andrew can inspect coverage for every confirmed ticker, retrieve its available history within the requested window, and distinguish daily, weekly, quarterly, missing and carried-forward observations. He sees legal inception, first source availability, requested date, actual report date and gaps separately. Predecessor mutual-fund history is not silently counted as ETF history. See supporting specification S1 and S3.

### O3 — Andrew receives fresh holdings each day without manual downloads, with Bloomberg spent only where needed

The issuer collection fires at 7:00 AM ET from AWS and captures each fund independently. At 8:03 AM ET the Bloomberg morning run reads the coverage record and requests only funds still uncovered that Bloomberg actually carries; a satisfied fund records a skip. GQGU has no Bloomberg fallback, and the page says so on a GQGU miss. Fund failures and unrelated morning-run failures remain distinguishable. See S1 and S2.

### O4 — Andrew compares any fund or source through one rich Canonical Shape

Bronze and silver keep each channel's own shape, one per source. Gold's `canonical_shape` is the accrual table that coalesces every shape into one Opal-defined master shape: every disclosed position with quantities, weights, values, identifiers, cash, instrument details, Opal asset/subasset classes and GICS hierarchy, with provenance and dates. Unknown fields stay unknown; a raw field survives even before it has a canonical column. See S2-S4.

### O5 — Andrew distinguishes portfolio tilts and likely trading from mechanical changes

Andrew can examine additions, exits, increases, reductions, concentration, sector/industry deltas and peer overlap. He can distinguish changes potentially explained by market prices, FX, fund share issuance/redemption, corporate actions, source changes or reporting gaps from residual activity consistent with manager trading. He chooses actual observation intervals rather than receive invented daily transactions. See S5.

### O6 — Andrew evaluates where a manager's positioning and observable decisions helped or hurt

Andrew can inspect top-ten and bottom-ten holdings by security return and by estimated portfolio contribution, with starting/ending weights and coverage. He can evaluate observed additions/reductions over subsequent windows against an explicit comparison, including exited holdings. Missing prices or incomplete exposure history reduce what can be concluded rather than disappear from the denominator. See S5 and S6.

### O7 — Andrew uses AI to form and revisit evidence-based hypotheses about manager behavior

Andrew can ask how a manager is tilting, what repeatable behavior the disclosed changes suggest, where past choices helped or hurt, and what direction could follow if that behavior continues. The response cites versioned table rows, separates observation from inference, offers alternatives and states what would invalidate each forecast. Saved hypotheses are later graded against new holdings without hindsight rewriting. See S7.

### O8 — An Opal researcher can reproduce and extend the research without changing its meaning

An Opal researcher can rebuild outputs from preserved raw observations, inspect source selection and corrections, and add a ticker or feed through the same schema, classification and LGIC naming rules. A rerun preserves evidence and does not duplicate positions or silently replace historical vintages. See S2-S7.

## PART II — WHERE THE BOUNDARY SITS

This product owns the six-fund universe, source-selection policy, historical coverage, raw/typed/canonical holdings, derived research tables, analysis prompt contracts, the served page and its daily archive. It owns the new issuer collector and the scoped Bloomberg holdings leg added to the existing morning vehicle.

**It is a separate pipeline from `etfs-netassets-daily`** (Andrew, item 1). That Lambda serves a different purpose (DIVZ/IDVZ/PFDE/PFOE AUM and holdings) and keeps its own schedule, homes and contracts. Nothing here extends, migrates or reads it; the shared FilePoint platform is a coincidence of vendor, not a shared pipeline.

It relies on **OPAL_BBGTML** for the established Bloomberg morning vehicle and local authenticated environment; **LGIC_NAMING / LGIC_ENFORCE / LGIC_CANON** for naming, placement and builders; the **research identity layer** (`lib/research/identity/`, built for AMGT) for security resolution; the **opal-gateway** for the authenticated route; and **ETFS_POSITIONING** for its established asset-class, subasset-class and GICS vocabulary. **AMGT_RESAPP** may consume the tables. A full research application, transaction execution, fund replication, a guaranteed prediction model and migration of existing ETF products are outside this brief.

The distinction between *securities held inside an ETF* and *clients holding ETF shares* is explicit. The client-ownership products already in `opal-data-etfs` are untouched.

## PART III — THE QUALITATIVE BAR

- Andrew can substantiate a claimed portfolio change by opening the underlying observations, and sees when the evidence permits only an interval-level inference.
- A stale Bloomberg answer cannot masquerade as a fresh disclosure or create a false no-trade day. A changed source basis cannot silently become a trade.
- **Nothing publishes past a failed guardrail** (Andrew, item 10). The pre-publish checks in S9 run before the served file is written; a failed check publishes a page that states what failed, or publishes nothing, never a quietly wrong page.
- Andrew can compare funds without learning six source formats, while still knowing which source supplied each material figure.
- Cash, derivatives and unidentified positions are visible rather than dropped to make totals look clean.
- A top/bottom table says what it ranks, its window and denominator. An AI explanation cites computed results and does not manufacture returns or manager intent.
- Daily holdings land when enrichment is unavailable; research requiring those fields visibly remains incomplete.
- Every S3 address and resource name is LGIC builder output and grades CONFORMANT.

## PART IV — THE SUBSTRATE: measured findings

### IV.1 — Full issuer holdings are accessible for all six funds (locally)

A repeat local HTTP/parser check at **2026-09-29 21:38:52–21:39:04 UTC** returned WCMG 49 rows, GQGU 39, BASG 35, TSEL 29, ETFT 29 and PCLG 29; weight totals were consistent with source rounding. TSEL's full-holdings page then stated September 29 while WCMG and ETFT still stated September 28. PCLG's file carries an execution timestamp, which must not automatically become a holdings date.

The files expose different semantics: GQGU/BASG share dated FilePoint patterns with fund filtering; TSEL's CSV lacks an internal date; ETFT's download link supplies only a top-ten slice while its page embeds the full portfolio. These need per-source adapters. **None of the six has been fetched from AWS**; that is the first test (Andrew, item 11). Publication times are unmeasured; a few days of observation settle them (item 12).

### IV.2 — Historical coverage has been counted, not inferred from request success

The completed census at **2026-09-29 approximately 20:39–20:48 UTC**, ending September 28:

| Fund | Backfill route | First report in tested route | Fresh report dates / trading dates in span |
|---|---|---|---|
| WCMG | Bloomberg Excel BQL | 2026-04-23 | 91 / 109 |
| GQGU | Issuer archive (no Bloomberg holdings) | 2025-07-14 | 305 / 305 |
| TSEL | Bloomberg Excel BQL | 2024-12-31 | 394 / 436 |
| BASG | Issuer archive | 2025-06-13 | 324 / 324 |
| ETFT | Bloomberg Excel BQL | 2025-12-02 | 206 / 206 |
| PCLG | Bloomberg Excel BQL | 2025-10-16 | 225 / 238 |

Bloomberg fills uncovered dates with older reports: TSEL's longest stale interval is 37 trading dates, PCLG's 12. No daily issuer archive has been established for WCMG/TSEL/ETFT/PCLG. Source start dates are not fund inception. The [full census](../../org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/AMGT_RECONN_SOURCES_20260929/DAILY_COVERAGE_CENSUS.md) carries the method.

### IV.3 — The working Bloomberg channel is installed Excel BQL, on a logged-in Terminal

Full historical holdings were exercised through Excel's `BQL.Query` with `holdings(...,dates=...)`, preserving `REPORT_DATE`. Raw `//blp/bqlsvc` remained unauthorized. Date-range queries failed; single-date queries worked, including multi-fund queries. The morning run (`integrations/bloomberg/pipeline/scheduled_daily_pull.cmd`, 8:03 AM ET) runs in the logged-in user's context and does nothing if no one is logged in, so the fallback is available only on days the Terminal is up. Unattended Excel, process cleanup and isolation from the other morning legs still need validation.

### IV.4 — Relevant substrate exists

`lib/trading_calendar.py` is the shared calendar. `lib/research/identity/` is the security identity layer AMGT built: one canonical key `<ROOT>_<CC>_Equity`, a versioned crosswalk, identifiers never guessed as US, alias collisions recorded as UNRESOLVED, every cell carrying MEASURED / INFERRED / UNRESOLVED, and `add_security` registering a new name with one Bloomberg reference-data call, raw response landed first. That is the resolution pattern to reuse for about 200 holdings, many non-US (Andrew, item 13). `data/etfs/scripts/gold/etf_positioning_gold.py` carries the established asset-class, subasset-class and GICS vocabulary.

The /daily-sprint cloud run is the serving precedent: a scheduled container Lambda (`infra/aws/lambda/daily_sprint_generator/`) authors with an OpenAI call, renders through the repo's renderer, publishes by day to S3 with read-back, and the gateway's `sprint_view.py` serves `/sprint`, `/sprint/<day>` and `/sprint/archive` (a delimiter listing of day prefixes) behind Entra sign-in and a roster. Its pages live at `s3://opal-data-portal-v2/daily-reports/<DAY>/`. This product copies the pattern with its archive in `opal-data-etfs` instead (Andrew, item 4).

`opal-data-etfs` has no S3 event notification configured (read 2026-09-30 ~03:2x UTC), so a new marker trigger overwrites nothing.

### IV.5 — The placement fix is LANDED in the LGIC registry

The tier home rule (`infra/logic/registry/tiers.json`) routed a PRODUCT-tenancy scope's bronze and silver to `opal-data-assets`; that is why `address('issuer-site','etfs','bronze',...)` returned `opal-data-assets`. The fix Andrew recalled was already in the registry: the **GENERAL tenancy** (`1675a8f631`, R4 narrowed 2026-09-18) homes every tier, platinum included, in the scope's own bucket; `harvest` and `transcripts` use it.

A separate `rivalfunds` scope pointing at `opal-data-etfs` was refused by the validator (a scope's bucket must be `opal-data-{scope}`). On Andrew's word (*"we can use etfs scope"*) the registry change is two edits, validated with 0 refusals: **the `etfs` scope moves to GENERAL tenancy**, and **a new system key `rivalfunds`** becomes the source of the product's derived tiers (`etfs/etfs/` is refused, and `etfs/global/` platinum homes in `opal-data-portal-v2`). R4's no-automatic-migration clause holds: existing `etfs/global/` addresses do not move, and all 12 generated registry targets are content-identical before and after (only their registry-hash stamps differ). From the live builder with the landed registry:

| Tier | Builder address |
|---|---|
| Issuer bronze / silver | `s3://opal-data-etfs/issuer-site/etfs/{bronze,silver}/holdings/date=...` |
| Bloomberg bronze / silver | `s3://opal-data-etfs/bloomberg/etfs/{bronze,silver}/holdings/date=...` |
| Gold | `s3://opal-data-etfs/rivalfunds/etfs/gold/<table>/date=...` |
| Platinum (served, by day) | `s3://opal-data-etfs/rivalfunds/etfs/platinum/page/date=...` |

All nine proposed keys graded CONFORMANT (September 30 ~04:1x UTC). `etfs-rivalfunds-daily` graded CONFORMANT as EVENT_RULE and SCHEDULE; `etfs-rivalfunds-daily-lambda`, `rivalfunds-etfs-build-canonical-shape-lambda` and `rivalfunds-etfs-publish-page-lambda` as LAMBDA.

## PART V — WHAT MUST BE TRUE: THE NON-NEGOTIABLE HOPS

Andrew named these explicitly so no hop is left unowned (item 8). They are requirements, not a sequence or a work allocation; round 1 crosses each once for BASG (O1), later rounds widen to all six.

- **H1 — Homes.** The registry change is landed (IV.5); every address and name is builder output. Bronze and silver keep one shape per channel and source; gold is the one master shape.
- **H2 — Backfill through both channels, ad hoc, from the outset** (item 7). Issuer archives for GQGU and BASG; Bloomberg Excel BQL for WCMG, TSEL, ETFT and PCLG; raw responses land in bronze with requested and report dates. A backfill is QA-class data landing, not production evidence.
- **H3 — Bronze to silver.** Silver is typed, deduplicated Parquet, every source column and row kept, fired by the bronze batch-complete marker. It also processes bronze that landed before it existed (the H2 backfill), by replay.
- **H4 — Silver to gold.** `canonical_shape` coalesces every silver shape; the S5 tables derive from it. Prices, total returns, GICS and benchmarks come from Bloomberg (item 13), resolved through the identity layer.
- **H5 — Gold to served page.** A publisher renders the day's page (charts plus OpenAI analyses from computed tables), writes it to the platinum day prefix with read-back, and the gateway serves `/rivalfunds`, `/rivalfunds/<day>` and `/rivalfunds/archive`.
- **H6 — Daily run.** `etfs-rivalfunds-daily` fires the issuer collector at 7:00 AM ET from AWS; the 8:03 AM ET Bloomberg leg covers funds still uncovered that Bloomberg carries; the chain runs through the page. Scheduled, never success-of-upstream alone.
- **H7 — Pre-publish guardrails** (item 10). The S9 checks run before H5 writes the served file.

**Trigger design, proposed for Andrew's review (item 3), detailed in S9:** each stage writes a batch-complete marker when its batch is whole, and the next stage fires on that marker (silver stays event-triggered, per R10). A daily scheduled sweep after the Bloomberg window runs any stage whose input marker has no matching output marker, then publishes the day's page. Every stage is idempotent on its batch id. The schedule makes the page arrive every trading day even when an event is lost, and it is the acceptance run.

Other things that must be true: each source has an exercised date extractor, complete-portfolio check and retry policy, and runs from AWS; the Bloomberg leg initializes its add-ins, handles asynchronous completion, cleans up its own Excel, and isolates its status from the other morning legs; identity, classification, prices, FX and corporate actions expose their date basis and coverage.

## PART VI — STATUS — NOT OUTCOME-BEARING

As measured on September 29, 2026: local issuer and Bloomberg captures exist; historical coverage is counted through September 28; local issuer fetch/parse completed at 21:38:52–21:39:04 UTC. The registry change (etfs GENERAL, system key rivalfunds) is committed locally; its generated targets are content-identical and were not re-stamped. Nothing has been built, scheduled or deployed; no issuer has been fetched from AWS; no page exists. Exact probe timestamps and hashes are under `.runtime/amgt-reconn-brief-20260929/` (device-local).

## PART VII — WHAT THIS BRIEF DOES NOT CLAIM

The research does not establish issuer publication times, AWS reachability of the six endpoints, Bloomberg quota cost, or reliable unattended Excel operation. Cross-source equivalence is incomplete: same-date comparisons found a WCMG quantity discrepancy with equal market value, broad BASG quantity differences, and cash representation differences. These are unresolved qualifications, not certified trades. Position-level reconciliation, historical GICS coverage, performance attribution, predictive validity and prompt quality remain untested. Backfilled holdings received today do not prove when a historical investor could have known them.

## References for the next consumer

- **BRIEF PATH:** `docs/briefs/etf-holdings-research-20260929.md` (revision 2)
- **PROJECT:** `ETFS_RIVALS` (named by Andrew 2026-09-30; not yet registered, L3 is the CTO's); product token `rivalfunds`, pipeline `etfs-rivalfunds-daily`, route `/rivalfunds`.
- **EXISTING PRD:** NONE.
- **SIBLING PROJECTS:** OPAL_BBGTML, LGIC_NAMING, LGIC_ENFORCE, LGIC_CANON, ETFS_POSITIONING, AMGT_RESAPP, AMGT_HARVST (identity layer). ETFS_INGEST / `etfs-netassets-daily` is a separate pipeline, named here only so no one conflates them.
- **PRIOR ART:** [supporting specification](../../org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/AMGT_RECONN_SOURCES_20260929/GOLD_TABLES_AND_PROMPTS.md); [Bloomberg access evidence](../../org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/AMGT_RECONN_SOURCES_20260929/BBG_EXCEL_ACCESS_VERIFIED.md); [daily census](../../org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/AMGT_RECONN_SOURCES_20260929/DAILY_COVERAGE_CENSUS.md); [Andrew-direct record](../../org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/AMGT_RECONN_SOURCES_20260929/ANDREW_DIRECT.md); /daily-sprint serving: `infra/aws/lambda/daily_sprint_generator/`, `infra/aws/ec2/opal-gateway/app/sprint_view.py`, `daily_reports/scripts/publish_daily_report.py`, `infra/aws/terraform/opal-gateway/daily-reports-iam.tf`; identity: `lib/research/identity/crosswalk.py`, `add_security.py`.
- **NAMING AUTHORITY:** `org/standards/NAMING_SCHEMA.json`; `infra/logic/registry/{systems,scopes,tiers}.json`; `lib/opal_naming.py`.
- **PLACEMENT AUTHORITY:** `infra/logic/02_DOCTRINE.md` R4 (narrowed 2026-09-18) and the GENERAL tenancy in `tiers.json`; Andrew's September 29 reaffirmations in `ANDREW_DIRECT.md`.
- **AUTHORIZATIONS ON RECORD:** OpenAI for the analyses (Andrew, item 4). Bloomberg for backfill and enrichment (items 7, 13); each pull remains subject to Andrew's per-use vendor word.
