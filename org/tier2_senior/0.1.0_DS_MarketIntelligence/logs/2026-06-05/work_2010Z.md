# Work — FIND_DUALBIZ SERP harvester (option a) proven; BD SERP fallback next (2026-06-05)

**archetype:** IMPLEMENT
**secondary_archetypes:** DIAGNOSE

Andrew-direct: try (a) Playwright/SERP pagination first; Bright Data SERP if needed.

## Built + proven: serp.py (DuckDuckGo SERP harvester)

`data/find/dualbiz/scripts/serp.py` — drives the DuckDuckGo HTML endpoint (browser-UA curl; no
Playwright needed for SERP), paginates (&s offset), unwraps uddg= result links, filters via the
harvest.py producing-firm filter, sweeps every provider's disclosure_search_strings. Bright Data SERP
documented as the `serp_brightdata()` fallback hook. ds-gate clean.

## Depth lift PROVEN (4/4 new firms scored present)

The first DDG query surfaced 4 NEW producing domains the page-1 WebSearch never returned -- ALL 4
scored as genuine independent dual-business targets:
- Envision Retirement Services (envisionrs.com) producing/present/188 (ins5 sec7) -- ranked #2 overall
- Clearpath Retirement (clearpathretirement.com) producing/present/157
- Mountain Star Financial (mountainstarfinancial.com) producing/present/129
- Stanley Retirement (stanleyretirement.com) producing/present/125

List: **15 -> 19 firms, 9 -> 13 present.** SERP pagination is the right recall unlock.

## The DDG limit -> Bright Data SERP is now "needed"

After the burst, DDG returned HTTP 202 + an "anomaly" (bot-detection) page -> free DDG works for a
handful of queries but rate-limits at volume. Bright Data SERP creds CONFIRMED present
(`brightdata-api-key` = 36-char Bearer token; `find-insure/bright-data/api-key`). FIND_INSURE already
calls `https://api.brightdata.com/request` (web-unlocker pattern) in crawl_web_bronze.py -> reuse that
exact pattern to fetch Google SERP HTML through the BD zone (defeats Google bot-blocking) and parse
result links. Same unwrapped-URL contract as ddg_search, so the harvest path is unchanged.

## Compiler Tools

| Tool | Result |
|------|--------|
| `.tools/ds-commit-gate.sh serp.py` | All checks passed |
| `python serp.py` (DDG sweep) | proven on 1st query (4 firms); rate-limited (202 anomaly) at volume |
| `python pipeline.py --deep` | 19 firms / 13 present; 4 SERP firms all present, independence-ranked |

## Next

Wire `serp_brightdata()` to the BD /request web-unlocker pattern (reuse FIND_INSURE key+zone) -> volume
SERP harvest without rate-limit -> sweep all providers -> roster depth at scale.
