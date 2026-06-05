# Work — FIND_DUALBIZ roster harvester + web-search saturation finding (2026-06-05)

**archetype:** DIAGNOSE
**secondary_archetypes:** IMPLEMENT

Andrew-direct: build + run the directory-roster harvester to deepen the list.

## Built: harvest.py (disclosure-search-result -> producing-firm domains)

`data/find/dualbiz/scripts/harvest.py` — takes a batch of search-result URLs, filters out
directories/aggregators/regulators/socials/press/data-brokers (DIRECTORY_DENYLIST) + provider-own
RIA domains (PROVIDER_OWN), dedups against the existing roster, emits clean producing-firm candidates.
ds-gate clean.

## Two empirical findings (both negative-but-important)

1. **Advisor directories are a DEAD-END for domains.** getwarmer / seniorfinanceadvisor /
   smartadvisormatch enumerate IAR NAMES but carry NO outbound links to the producing firms' websites
   (probed getwarmer firm-advisors page = only logo.dev; getwarmer individual advisor page = ZERO
   external links). So "parse directory roster pages" yields names, not scrapeable domains. The
   name->domain resolution gap kills the directory vector.

2. **Plain consumer web-search disclosure harvesting has SATURATED.** Ran 4 provider disclosure-string
   query variants (Alphastar x2, AE Wealth, Gradient); harvest.py: 16 URLs -> **0 new** producing
   candidates (all were directories/provider-own/already-known). The WebSearch tool returns only page-1
   (~10 results); after ~a dozen firms per provider, page-1 returns only known firms + directories.

## The actual depth unlock (for Andrew's call)

The long tail of producing firms lives on **search-result pages 2-N**, which the page-1 consumer search
can't reach. Three options:
- **(a) Playwright-driven SERP pagination (no key, free):** drive Bing/DuckDuckGo result pages 1-5 via
  the headless-Edge fetcher we already wired; feed URLs to harvest.py. Fragile (ToS-gray, layout drift)
  but zero cost. Buildable now.
- **(b) Paid search API (Bing Web Search / SerpAPI):** robust pagination, ~$ per 1k queries, needs a key.
- **(c) Accept the ~15-firm validated set as the PoC** and pivot to qualification (FINRA license + AUM
  enrich, per the existing FINRA BrokerCheck client) for IR handoff.

Recommendation: (a) as the next free experiment; escalate to (b) if depth justifies the spend. The
fingerprint + scorer + ranking + escape-valve are all proven; the only remaining bottleneck is search
RECALL (result-page reach), not scrape or scoring.

## Compiler Tools

| Tool | Result |
|------|--------|
| `.tools/ds-commit-gate.sh harvest.py` | All checks passed |
| `python harvest.py --urls ... --tamp ...` | runs; 16 urls -> 0 new (saturation confirmed; filter+dedup correct) |
| getwarmer advisor-page link probe | 0 external links (directory dead-end confirmed) |

## State

Pipeline complete + proven end-to-end: 15 firms / 9 present, independence-ranked. Harvester built.
Search recall is the sole remaining lever -> options (a)/(b)/(c) above pending Andrew.
