# ETF holdings research: canonical holdings, manager activity and analysis

L1 BRIEF | NEW | Author: 4.0.0_SA_CRO~Z | September 29, 2026

Andrew's direction is a lightweight research foundation for WCMG, GQGU, TSEL, BASG, ETFT and PCLG. Preserve as much disclosed holdings information as possible, standardize it once, and use reproducible tables to study the managers. The history target is up to two years, bounded by each ETF's own available history. Less frequent disclosures are acceptable when daily history is unavailable; they must remain identifiable as such.

**Recommendation:** issuer-first daily holdings for all six; issuer archive backfill for GQGU and BASG; Bloomberg Excel BQL backfill for WCMG, TSEL, ETFT and PCLG. Add a selective Bloomberg script to the existing morning run, skipping holdings requests already satisfied by fresh, complete issuer data. A daily issuer Lambda is feasible from the public feed shapes exercised locally, but its AWS execution remains untested. Characteristics and enrichment must not block holdings collection.

Supporting design: [table, prompt and naming specification](../../org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/AMGT_RECONN_SOURCES_20260929/GOLD_TABLES_AND_PROMPTS.md). Direct instructions and source evidence are linked in the references.

## PART I — THE OUTCOME TERRITORY

### O1 — Andrew reviews one ETF's changes through one complete research journey

**Candidate thread first:** Andrew selects BASG and its latest two genuinely dated holdings reports, opens the standardized holdings and change tables, and reads a short evidence-linked account of what changed and what cannot be inferred. He can trace a highlighted holding back through typed data to the issuer's raw record. The initial consumer entry can be a research query or a small generated research report; a dashboard is not required. The broader research window is the available ETF history up to two years.

This is one real use over real holdings, ending in Andrew's observed research result. A QA output is sufficient for that candidate thread; production scheduling belongs to the wider capability below.

### O2 — Andrew obtains the best available history without mistaking stale snapshots for daily disclosure

Andrew can inspect coverage for every confirmed ticker, retrieve its available history within the requested window, and distinguish daily, weekly, quarterly, missing and carried-forward observations. He sees legal inception, first source availability, requested date, actual report date and gaps separately. Predecessor mutual-fund history is not silently counted as ETF history. See supporting specification S1 and S3.

### O3 — Andrew receives fresh holdings each day with Bloomberg requests limited to demonstrated needs

Andrew can rely on scheduled issuer collection and the existing Bloomberg morning vehicle without manually downloading portfolios. The issuer Lambda captures each fund independently; the Bloomberg script checks coverage and handles eligible backfill, missing holdings or separately requested enrichment. A satisfied issuer day produces a recorded Bloomberg skip. An issuer delay remains pending through the configured collection/retry window rather than immediately spending a Bloomberg request. Fund failures and unrelated morning-run failures remain distinguishable. See S1 and S2.

### O4 — Andrew compares any fund or source through one rich Canonical Shape

Andrew can query every disclosed position through an Opal-defined, denormalized base table regardless of issuer or Bloomberg channel. He has available quantities, weights, values, identifiers, cash, instrument details, Opal asset/subasset classes and GICS hierarchy fields together, with the provenance and dates needed to interpret them. Unknown fields remain unknown; richer future data can be added without losing raw source information. Bronze originals, typed silver Parquet and gold Parquet live in `opal-data-etfs` under LGIC source-first names. See S2–S4.

### O5 — Andrew distinguishes portfolio tilts and likely trading from mechanical changes

Andrew can examine additions, exits, increases, reductions, concentration, sector/industry deltas and peer overlap. He can distinguish changes potentially explained by market prices, FX, fund share issuance/redemption, corporate actions, source changes or reporting gaps from residual activity consistent with manager trading. He can inspect uncertainty and choose actual observation intervals rather than receive invented daily transactions. See S5.

### O6 — Andrew evaluates where a manager's positioning and observable decisions helped or hurt

Andrew can inspect top-ten and bottom-ten holdings by security return and by estimated portfolio contribution, together with starting/ending weights and coverage. He can evaluate observed additions/reductions over subsequent measured windows against an explicit comparison, including exited holdings. Contribution, counterfactual decision evaluation and actual fund performance stay distinguishable. Missing prices or incomplete exposure history reduce what can be concluded rather than disappear from the denominator. See S5 and S6.

### O7 — Andrew uses AI to form and revisit evidence-based hypotheses about manager behavior

Andrew can ask how a manager is tilting, what repeatable behavior the disclosed changes suggest, where past choices appear to have helped or hurt, and what portfolio direction could follow if that behavior continues. The response cites versioned table rows, distinguishes observation from inference, offers alternative explanations and states what would invalidate each forecast. Saved hypotheses can later be compared with new holdings without hindsight rewriting. See S7.

### O8 — An Opal researcher can reproduce and extend the research without changing its meaning

An Opal researcher can rebuild outputs from preserved raw observations, inspect source selection and corrections, and add a ticker or feed through the same schema, classification and LGIC naming rules. A rerun preserves evidence and does not duplicate positions or silently replace historical vintages. The researcher can tell whether a result uses today's best reconstruction or information actually available at an earlier time. See S2–S7.

## PART II — WHERE THE BOUNDARY SITS

This product owns the six-fund research universe, source-selection policy, historical coverage, raw/typed/canonical holdings, derived research tables, analysis prompt contracts and evidence-linked research outputs. It owns the new issuer collection capability and the scoped Bloomberg holdings addition to the existing morning vehicle. These are outcome boundaries, not a work allocation or implementation sequence.

It relies on **ETFS_POSITIONING / ETFS_INGEST** for reusable holdings and classification conventions; **OPAL_BBGTML** for the established Bloomberg morning vehicle and local authenticated environment; **LGIC_NAMING / LGIC_ENFORCE / LGIC_CANON** for naming, placement and canonical builders; and the established security identity and price/reference-data substrate. Existing ETF positioning and partner ETF-ownership outputs have separate consumers and are not implicitly migrated or widened.

**AMGT_RESAPP** may consume the resulting research tables. **AMGT_CORPUS / AMGT_HARVST** are potential later context sources for manager commentary and explanations; they are not prerequisites for this holdings-led thread. A full research application, transaction execution, fund replication, a guaranteed prediction model, and migration of existing four-fund products are outside this brief.

The distinction between *securities held inside an ETF* and *clients holding ETF shares* is explicit. Existing ETF ownership aggregation in the same bucket is prior art for storage, not a substitute for composition data.

## PART III — THE QUALITATIVE BAR

- Andrew can substantiate a claimed portfolio change by opening the underlying observations, and see when the evidence permits only an interval-level inference.
- A stale Bloomberg answer cannot masquerade as a fresh issuer disclosure or create a false no-trade day. A changed source basis cannot silently become a trade.
- Andrew can compare funds without learning six source formats, while still knowing which source supplied each material figure.
- A raw field survives collection even if Opal has not yet assigned it a canonical column. Cash, derivatives and unidentified positions are visible rather than dropped to make totals look clean.
- A top/bottom table says what it ranks, its window and denominator. An AI explanation cites those computed results and does not manufacture returns or manager intent.
- Daily holdings can land when optional GICS, beta, prices or other enrichment is unavailable. Research requiring those fields visibly remains incomplete.
- A researcher can derive proposed resource and storage names from LGIC's actual registry and grammar; the bucket placement follows Andrew's explicit direction and the placement metadata agrees with it before production writes.

## PART IV — THE SUBSTRATE: measured findings

### IV.1 — Full issuer holdings are accessible for all six funds

Earlier September 29 captures obtained complete current issuer portfolios. A repeat local HTTP/parser check at **2026-09-29 21:38:52–21:39:04 UTC** returned WCMG 49 rows, GQGU 39, BASG 35, TSEL 29, ETFT 29 and PCLG 29; reported weight totals were consistent with source rounding. TSEL's accompanying full-holdings page now states September 29, while WCMG and ETFT still state September 28. GQGU/BASG requests explicitly targeted September 28; PCLG's file carries a September 28 execution timestamp, which must not automatically become a certified holdings date.

The files expose different semantics. GQGU/BASG share dated FilePoint patterns with fund filtering; TSEL's CSV lacks an internal date; ETFT's download link supplies only a top-ten slice while its page embeds the full portfolio. These require source adapters, not one blind CSV downloader. Source details and links are in S1.

### IV.2 — Historical coverage has been counted, not inferred from request success

The completed census at **2026-09-29 approximately 20:39–20:48 UTC**, ending September 28, found:

| Fund | Recommended history route | First report in tested route | Fresh report dates / trading dates in span |
|---|---|---|---|
| WCMG | Bloomberg Excel BQL | 2026-04-23 | 91 / 109 |
| GQGU | Issuer archive | 2025-07-14 | 305 / 305 |
| TSEL | Bloomberg Excel BQL | 2024-12-31 | 394 / 436 |
| BASG | Issuer archive | 2025-06-13 | 324 / 324 |
| ETFT | Bloomberg Excel BQL | 2025-12-02 | 206 / 206 |
| PCLG | Bloomberg Excel BQL | 2025-10-16 | 225 / 238 |

Bloomberg fills uncovered dates with older reports. TSEL's longest observed stale interval is 37 trading dates and PCLG's is 12. No daily issuer archive has been established for WCMG/TSEL/ETFT/PCLG. No unavailable days are promised. Source start dates are not synonymous with fund inception. The [full census](../../org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/AMGT_RECONN_SOURCES_20260929/DAILY_COVERAGE_CENSUS.md) carries the reproducible method and exceptions.

### IV.3 — The working Bloomberg channel is installed Excel BQL

Full historical holdings were exercised through Excel's `BQL.Query` with `holdings(...,dates=...)`, preserving `REPORT_DATE`. Raw `//blp/bqlsvc` remained unauthorized even when Excel worked. This supports reusing the working Windows route; it does not support assuming the raw Python BQL service now works. GQGU returned no Bloomberg holdings in the completed census. Date-range queries failed; individual dated queries worked, including multi-fund queries.

The existing morning wrapper already has independently handled ETF legs. It is reusable orchestration, but existing code's broad claims about no backfill do not describe the newly exercised Excel route. Headless unattended Excel operation under the scheduled identity, process cleanup and source fallback still need production validation.

### IV.4 — Relevant producers exist, with different universes and legacy paths

Read September 29: `integrations/bloomberg/pipeline/etf_constituents_pull.py` targets DIVZ/IDVZ/PFDE/PFOE; `data/etfs/scripts/gold/etf_positioning_gold.py` already builds holdings/book Parquet and uses established asset-class, subasset-class and GICS industry-group semantics. `lib/trading_calendar.py` provides the shared trading calendar. `lib/research/identity/` supplies existing security identity machinery whose fit must be checked before creating a parallel resolver.

The live `opal-data-etfs` root listing at **approximately 21:35 UTC** contains `bbg/`, `bbg-testpull/`, `silver/`, `gold/`, `daily/`, `platinum/`, `config/` and `snapshots/`. That is evidence of existing substrate, not evidence that the new LGIC layout is deployed.

The deployed `etfs-netassets-daily` Lambda was read without invocation at **21:39:04 UTC**. Its code contains requests/retry handling, raw capture and TrueShares/Pathfinder collection. Its handler writes data, so it was not used as a read-only issuer probe. Existing cloud collection is prior art; these six sources have not been exercised from Lambda by this research.

### IV.5 — LGIC supplies the names; research belongs in its product bucket

`org/standards/NAMING_SCHEMA.json` v1.12, `infra/logic/registry/` and `lib/opal_naming.py` are the naming authorities. The existing registry includes `issuer-site`, `bloomberg` and `etfs`; six new vendor tokens are unnecessary. Source identity inside the data still records the actual issuer and endpoint.

The proposed source-first keys and Lambda/schedule examples in S2 graded CONFORMANT through the canonical grader at **approximately 21:39 UTC**. However, `address('issuer-site','etfs','bronze',...)` and its silver counterpart currently return `opal-data-assets`; the canonical gold address returns `opal-data-etfs/etfs/global/gold/...`.

The governing rule already places this research in `opal-data-etfs`: `infra/logic/02_DOCTRINE.md` R4 confines the shared `opal-data-assets` route to client/partner custodial information and homes outside research, public information and other general/product data in their own scope's bucket, including bronze and silver. Andrew reaffirmed that distinction on September 29, citing `opal-data-harvest` and `opal-data-transcript` as examples. The ETF composition researched here is outside research, not a client's custodial holdings.

All three layers therefore belong in `opal-data-etfs` under the existing policy; this is not a new exception or an open bucket-placement decision. The measured builder result above exposes placement metadata that has not caught up for this research use. Its correction is implementation alignment with R4, preserving LGIC's source-first grammar. R4 also states that existing addresses do not move automatically; this new research layout does not authorize migration of unrelated existing data or reclassification of the bucket's client-ownership products.

## PART V — WHAT MUST BE TRUE, WITHOUT SCOPING IT NOW

- Canonical LGIC placement metadata must reflect R4's existing distinction: client/partner custodial assets use `opal-data-assets`; this outside ETF research uses `opal-data-etfs` at every requested tier. Correcting the affected research placement is implementation work, not a policy exception requiring another decision. Key and resource names use the existing registry and builders; existing consumers retain their contracts.
- Each source must have an exercised date extractor, complete-portfolio check, publication/retry policy and compatible unattended network access. Lambda egress/parser behavior must be checked with real responses before calling it operational.
- The Windows Bloomberg script needs the installed add-ins, authenticated user context, asynchronous completion handling and ownership-safe Excel cleanup. The morning integration must isolate its status from other legs.
- Reusable identity, Opal classification vocabulary, GICS reference data, prices/total returns, FX and corporate actions must expose their date basis and coverage. Fund share counts and net assets are needed where analysis claims to adjust for creations/redemptions. Their absence constrains analysis, not raw ingestion.
- Source selection, corrected vintages, date semantics, unit conventions, allowable nulls and performance definitions must be closed in the subsequent schema/PRD. S3–S7 provide concrete proposals for that decision.
- The analysis runner must be able to retrieve bounded, versioned evidence and preserve prompt/model/input versions. AI is a consumer of computed tables, not their numeric authority.

## PART VI — STATUS — NOT OUTCOME-BEARING

As measured on September 29, 2026: local issuer and Bloomberg research captures exist; historical coverage counts are measured through September 28; repeated issuer fetching and parsing completed at 21:38:52–21:39:04 UTC; the deployed collector's bytes and configuration were read at 21:39:04 UTC; naming examples and placement behavior were exercised at approximately 21:39 UTC. Exact local probe timestamps, payload hashes and Lambda code hash are preserved under `.runtime/amgt-reconn-brief-20260929/`.

This brief and the accompanying specification are design deliverables. No new production collector, schedule, table, resource rename or placement-registry mutation was performed for this brief. The current skill invocation does not dispatch work or create an endpoint/PRD.

## PART VII — WHAT THIS BRIEF DOES NOT CLAIM

The research does not establish a source publication SLA, complete historical issuer archives for every fund, AWS accessibility for these six endpoints, measured Bloomberg billing savings, or reliable unattended Excel operation. It does establish public local retrieval and the historical coverage stated above. Bloomberg request avoidance is the recommended design; an exact quota saving is not quantified.

Cross-source equivalence is incomplete: earlier same-date comparisons found a WCMG quantity discrepancy with equal market value, broad BASG equity quantity differences, and cash representation differences. These are unresolved measurement qualifications, not certified trades or corporate-action explanations. Full position-level reconciliation, historical GICS coverage, performance attribution, predictive validity and prompt output quality remain untested.

Backfilled holdings received today do not prove when a historical investor could have known them. Historical analysis must disclose this availability limitation. A live-data candidate thread and eventual daily operations are desired outcomes, not status claims in this brief.

## References for the next consumer

- **BRIEF PATH:** `docs/briefs/etf-holdings-research-20260929.md`
- **PROJECT:** NONE-YET; new research capability, with existing substrate reused.
- **EXISTING PRD:** NONE for this six-fund research product.
- **SIBLING PROJECTS:** ETFS_POSITIONING, ETFS_INGEST, OPAL_BBGTML, LGIC_NAMING, LGIC_ENFORCE, LGIC_CANON, AMGT_RESAPP; potential later AMGT_CORPUS / AMGT_HARVST context.
- **PRIOR ART:** files and live measurements in IV.1–IV.5; [supporting specification](../../org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/AMGT_RECONN_SOURCES_20260929/GOLD_TABLES_AND_PROMPTS.md); [Bloomberg access evidence](../../org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/AMGT_RECONN_SOURCES_20260929/BBG_EXCEL_ACCESS_VERIFIED.md); [daily census](../../org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/AMGT_RECONN_SOURCES_20260929/DAILY_COVERAGE_CENSUS.md); [Andrew-direct record](../../org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/AMGT_RECONN_SOURCES_20260929/ANDREW_DIRECT.md).
- **NAMING AUTHORITY:** `org/standards/NAMING_SCHEMA.json`; `infra/logic/registry/{systems,scopes,tiers}.json`; `lib/opal_naming.py`; `org/missions/D14/LGIC/LGIC_NAMING/prd/LGIC_NAMING_PRD.md`.
- **PLACEMENT AUTHORITY:** `infra/logic/02_DOCTRINE.md` R4, narrowed September 18 and reaffirmed by Andrew September 29; the verbatim reaffirmation is in `ANDREW_DIRECT.md` linked above. R4 was checked against the local doctrine at approximately 2026-09-30 00:59 UTC.
- **MEASURED AT:** each status claim carries its UTC clock in IV and VI; timestamps marked approximately are bounded research-session observations, not server timestamps.
