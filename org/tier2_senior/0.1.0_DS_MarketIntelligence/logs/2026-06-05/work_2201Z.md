# Work — FIND_DUALBIZ scaled to 315 firms + WHOIS-age scoring + staged-architecture formalization (2026-06-05)

**archetype:** IMPLEMENT
**secondary_archetypes:** DIAGNOSE, DESIGN

Andrew-direct live engagement, turn-by-turn. Continued FIND_DUALBIZ from the DDG-SERP-proven state through Bright Data SERP scaling, qualification-signal addition, and formal project elevation.

## BD SERP zone correction (cost incident — Andrew-stopped)

First two BD sweeps (v1=34, v2=259 candidates) wrongly routed Google SERP fetches through the `one_shotter` web-unlocker zone. Andrew stopped the v2 run mid-execution: "you should absolutely not fucking do that, stop any crawling that method immediately." Root cause: the unlocker zone bills premium residential-proxy bandwidth PER FETCH — crawling a search engine through it blows through API credits. Andrew provided the correct path: a DEDICATED SERP zone `serp_opal` (secret `find-dualbiz/bright-data/serp`, shares the find-insure API key), priced per query, returns STRUCTURED JSON (`organic[].link` — no HTML parse needed).

- Saved zone config to Secrets Manager `find-dualbiz/bright-data/serp`.
- Rewrote `serp_brightdata()`: serp_opal zone, JSON parse (dropped `_parse_google()` HTML scraper).
- Banked fabric memory `feedback_serp_use_dedicated_serp_zone_not_unlocker` + MEMORY.md pointer.

## Scale + qualification signal

- Expanded providers: added CreativeOne Wealth / IMPACT Wealth / Simplicity Wealth / North Star / Equita to provider-seeds + tamp-seeds; +string variants in serp.py.
- serp_opal sweep (9 providers, 3 pages) → 184 new candidates → pipeline 315 firms / **156 disclosure-present** (Andrew's 100 target cleared).
- WHOIS domain-age scoring added (`_util.get_domain_age` + `domain_age_score`, python-whois): older = better, 0-30 bucket. Wired into gold + as serving sort tiebreaker (element 4).
- Parallelized bronze (ThreadPoolExecutor 20 workers) + WHOIS (8 workers) — bronze ~10min→~30s. Andrew asked "can we parallelize / what's the bottleneck" → sequential curl was the wall.
- CSV export (246 clean rows, ranked, domain-age cols) → Andrew's desktop. Opened top-20 + full-37 in Chrome for Andrew review.

## Ranking schema (explained to Andrew, codified)

5-key tuple sort: (0) priority_rank+penalty [tier band + independence penalty, asc], (1) -insurance_density, (2) -security_density, (3) -dualbiz_score, (4) -domain_age_score. Element 0 gates (acquired_megacap +20 sinks below all independents); 1-2 = Andrew's insurance-then-security directive; 3-4 finer tiebreakers.

## Formalization (Andrew elevate)

Andrew (AskUserQuestion): enrichment scope = **WHOIS + FINRA + AUM**; persistence = **register as formal project now**.
- Authored staged-architecture doc-of-record `docs/architecture/FIND_DUALBIZ.md` (v0.1): S0-S7 stage contracts, two-loop design (gated SERP recall vs free evaluation, joined by persistent candidate registry S2), scoring/ranking schema, S6 WHOIS+FINRA+AUM qualification design (reuses FIND_INSURE brokercheck_client.py; flagged producing-vs-integrated ADV-AUM nuance), open decisions.
- Routed registry formalization to COO (their closure-authorship lane per LD-0162) with the 2-step JSON+REGISTRY edits + CTO-PRD routing — did NOT edit REGISTRY/JSON myself (owned-paths + DS-no-commit discipline).
- Answered COO [SYNC] (stale-summary); updated broker summary.

## Compiler Tools

| Tool | Result |
|------|--------|
| `.tools/ds-commit-gate.sh` (serp/harvest/pipeline/_util/discover) | All checks passed (each edit) |
| `serp.py --engine brightdata --independent-only --pages 3` (serp_opal) | 184 candidates, structured JSON, no rate-limit |
| `pipeline.py --deep` (parallelized) | 315 firms / 156 present; bronze 301/315 ok (16 playwright) |

## State / Next (evaluation-loop build, my lane, no blockers)

1. S2 `registry.py` — replace the `glob(serp-harvested-*.json)` hack (still mixing wrong-zone v1/v2 results) with canonical `candidates.json` + dedup/provenance.
2. S6 `enrich.py` — pull WHOIS out of gold; wire FINRA BrokerCheck (CRD/rep-count/Series-license) + SEC ADV AUM.
3. One canonical noise filter (collapse harvest.py denylist + CSV NOISE set).
Awaiting Andrew steer on build order (FINRA+AUM enricher first vs registry/filter cleanup first). COO formalizing project registry.
