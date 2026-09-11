# Wall Street Journal: a cookieless, loginless data-access mechanism -- confirmed live

**Author:** `4.0.0_SA_CRO~Z` | **Date:** 2026-09-11 | **For:** Andrew; `1.0.0_SA_CTO~Z` (L4), `2.0.0_SA_COO~ZZZ` (L5)
**Authorization:** Andrew-direct at this terminal, 2026-09-10/11.
**Script:** `org/tier1_exec/4.0.0_SA_CRO/scripts/wsj_rest_fetch.py`
**Parked artifact:** none -- there is nothing to park. This is the whole finding.

---

## 1. What this is

WSJ is structurally different from Seeking Alpha, FT, and Bloomberg: **it has no login mechanism in
this pipeline at all**, and none is needed. Bright Data's Web Unlocker (`zone=one_shotter`) defeats
WSJ's bot-wall cookielessly and returns public-page HTML directly -- the same call the estate's
production `fetch_wsj.py` already makes for the ASTN_WSJFT digest; `wsj_rest_fetch.py` packages it as
a standalone, testable module.

**The content this reaches is explicitly public.** WSJ's own embedded page state tags every visit
`"user_type": "nonsubscriber"` -- confirmed live, repeatedly. There is no parked session, no
credential, no cookie jar, because there is no authenticated identity in this path at all. If a future
need requires WSJ's paywalled subscriber content, that is NEW scope requiring a real WSJ subscriber
login (mirroring the Seeking Alpha / FT / Bloomberg mechanism), not an extension of this one.

## 2. What's actually there

- **Listings**: `wsj.com/news/{section}` (home, markets, economy, business, finance) -- article links,
  extracted the same way `fetch_wsj.py` already does.
- **Articles**: any WSJ article URL -- full text, fetched cookielessly through the Unlocker.
- **Per-ticker quote page**: `https://www.wsj.com/market-data/quotes/{TICKER}` -- a real, fully public
  per-security page. This is WSJ's closest equivalent to Seeking Alpha's per-security report, though
  structurally much thinner (no analyst commentary, no dedicated report object).
- **Per-ticker news (best-effort, NOT stable)**: the quote page's embedded React/Redux state
  (`window.__STATE__`) sometimes carries a real news array under a key shaped
  `quotes_latestNews_{"ticker":"RTX",...}.data.data.news`. MEASURED: present with real structure on
  one fetch, absent on an immediate repeat fetch of the identical URL. This is a timing/hydration race
  in Bright Data's static snapshot of a client-rendered page, not a flag we control. `wsj_rest_fetch.py`
  retries with a stated cap and reports honestly whether it found the key each time -- an absence is
  never reported as an empty feed, only as "not found this attempt."
- **What does NOT work**: `wsj.com/search?query=...` is a near-empty client-rendered shell over plain
  REST (measured: 252 bytes, no visible text) -- it needs a real browser and should not be built on as
  a REST source.

## 3. Why this is the right design, not an unfinished one

Unlike Seeking Alpha (PerimeterX Press & Hold), FT (hCaptcha), and Bloomberg (PerimeterX + a Google
OAuth iframe), WSJ presents no login wall to the content this pipeline needs, because the ASTN_WSJFT
digest was scoped to WSJ's public news, not subscriber-only analysis. Building a WSJ login mechanism
now would be new, unrequested scope with no current use case -- the loginless path is not a workaround,
it is the complete, correct mechanism for what WSJ is actually asked to serve here.

## 4. Script manifest

| Path | Role |
|---|---|
| `org/tier1_exec/4.0.0_SA_CRO/scripts/wsj_rest_fetch.py` | Standalone Bright Data Web Unlocker wrapper: listing/article/quote verbs, no session, no login. |
