# Chatter-Volume Gated Daily News Refresh — Spec + Proof

**Author:** 4.0.0_SA_CRO
**Date:** 20260911
**Status:** SPEC + PROOF (pre-build; no infrastructure stood up yet)
**Owed to:** Andrew, per direct request 2026-09-11 — "find some low impact mechanism to
assess whether any of these tickers have new news every day... spec it out/prove it"

---

## 0. The discrepancy this spec resolves instead of guessing past

Andrew's request cited "98 securities" as coming from the email that initiated
AMGT_RESAPP. I checked Andrew's actual mailbox directly (`mcp__opal-gateway__search_email`,
identity `Andrew@opalinvest.com`) rather than assume. The real kickoff email —
**"Claude automation," Adam Muller (Adam@opalinvest.com), 2026-09-10T13:18:06Z, the only
AMGT_RESAPP-relevant email in the mailbox** — contains no ticker count whatsoever. It
describes automating five report SECTIONS (financial model, company description,
investment thesis, risks, management bio) using the Copa and SAP packs as formatting
examples. No universe size, no ticker list.

So "98" does not exist as a source-of-truth number anywhere I can find — confirmed twice
independently this session (once against the mailbox directly, once by a second research
pass re-deriving it from the repo without being told the first result). What DOES exist:

- **`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~3/universe.json`**
  — the real security-universe file, denominator **89 folders**. Schema per entry:
  `{folder, one_pager_files, bloomberg_ticker: {value, status: MEASURED|INFERRED|UNRESOLVED}}`.
  Current partition: 32 MEASURED / 0 INFERRED / 57 UNRESOLVED.
  ⚠ **Known defect, already flagged as a surprise row, already fixed in a sibling
  script:** 16 of the 48 raw "MEASURED" entries share the placeholder string "AAPL US" —
  a join bug. `.../~1/select_securities.py:8-13` already implements the fix (drop any
  ticker value that recurs across >1 folder before trusting it as MEASURED). **This
  mechanism's universe loader must apply the same dedup rule** — feeding the raw,
  unfixed 48 "MEASURED" tickers into the daily SERP loop would silently double- (or
  16x-) count "AAPL US" as if it were 16 different real tickers.
- A **separate 63-name materiality queue** — a different list, for a different purpose,
  out of scope for this mechanism.

**This spec is written to be universe-size-agnostic** — nothing below hardcodes 98, 89,
or 63. The mechanism takes "the AMGT_RESAPP tracked universe" (post-dedup) as an input
list, whatever its final signed count turns out to be. Recommend Andrew confirm the
89-folder / post-dedup count before the universe list is frozen for L4; that
confirmation is not a blocker to building or proving the mechanism itself.

---

## 1. The problem restated precisely

Four platforms now have proven login/data-access mechanisms: Seeking Alpha, FT,
Bloomberg, WSJ. Each is expensive to hit — a real authenticated session, a captcha
solve, or at minimum a Bright Data Web Unlocker call — and each is rate-sensitive
(anti-bot detection, session staleness, ToS exposure). Running all four against every
tracked security every day is:
- **Wasteful** — most days, most tickers have no material news.
- **Riskier** — more daily hits per platform per credential raises detection/ban surface
  for no informational gain on quiet days.
- **Not what a portfolio manager needs** — a PM wants FRESH DATA on what's actually
  moving or being talked about, not a stale, uniform sweep.

The fix: gate the expensive per-platform pull behind a cheap, frequent signal that
answers "is anything happening on this ticker today" BEFORE spending a platform call on
it — and use that signal to also answer "how much has NEWS ATTENTION shifted," so the
same signal drives two rankings, not just a threshold.

---

## 2. This is not a new PRD surface — it's an unbuilt one that already exists

AMGT_RESAPP's own PRD already names this exact concept: **S13 / FWD-11, "THE SOCIAL
FEED."** This mechanism is the build-out of that surface, not new scope invented here.
[Reference this in the round-2 L4 fold `1.0.0_SA_CTO~Z` is authoring — see §8.]

**A sibling, complementary surface already has a full (not-yet-triggered) design under
the same task order:** `AMGT-s-13` (`lib/research/social/`) — a per-POST social
discussion feed built on Bright Data's **Datasets API**, a different product from the
SERP/Web-Unlocker mechanism this spec uses. That surface is correctly gated behind
Andrew's explicit per-use word under the standing vendor-egress moratorium — **that
gate is specific to the Datasets API product**, not to SERP/Web-Unlocker, which is
already proven and in live use elsewhere in this estate (`serp.py`, the WSJ mechanism).
This spec's mechanism needs no new vendor-egress approval; `AMGT-s-13`'s does, separately,
whenever that surface is built.

---

## 3. What already exists in the estate that this reuses (not reinvents)

### 3.1 The cheap SERP primitive — `data/find/dualbiz/scripts/serp.py`

Already built, already in production for a different purpose (disclosure-string
discovery for FIND_DUALBIZ). Three directly-reusable functions:

- `ddg_search(query, max_pages=2, per_sleep=1.2)` — DuckDuckGo HTML endpoint
  (`https://html.duckduckgo.com/html/?q=...`), plain browser-UA `requests` call. **Zero
  vendor cost.** This is the PRIMARY path for the chatter-volume signal.
- `serp_brightdata(query, max_pages=2, per_sleep=0.5)` — Bright Data `serp_opal` zone
  (structured JSON via `organic[].link`, NOT the `one_shotter` Web Unlocker zone used
  elsewhere in the estate — a different Bright Data product). Documented FALLBACK for
  when DDG rate-limits or returns degraded results.
  - Secrets: `find-dualbiz/bright-data/serp` (zone config), `find-insure/bright-data/api-key`
    (shared BD API key) — note these are DIFFERENT secret names than
    `brightdata-api-key` used by the WSJ/one_shotter path elsewhere in the news
    mechanisms. Worth a one-line confirmation with whoever owns FIND_DUALBIZ that
    reusing these secrets cross-project is fine, or mint an AMGT_RESAPP-scoped copy —
    minor, not a blocker.
- `serp_search(query, engine="ddg"|"brightdata", max_pages=2)` — engine-agnostic
  dispatcher. **This is the function the daily chatter job calls directly.**

`harvest_query()` / `sweep_discovery()` / `sweep_provider_strings()` in the same file
are domain-specific to FIND_DUALBIZ's use case and are NOT reused — only the three
primitives above. Confirmed: only `data/find/dualbiz/`'s own scripts currently call
`serp_search`/`ddg_search`/`serp_brightdata` (no cron or Lambda wrapper schedules
`serp.py` today — it's invoked ad hoc within FIND_DUALBIZ). This mechanism would be the
first SCHEDULED consumer of these primitives, not a second copy of an existing job.

### 3.2 The rolling-window + decay pattern — `infra/aws/lambda/news_trending_analysis/lambda_function.py`

Read in full this session (1,667 lines). **Important distinction to get right:** this
Lambda is NOT a per-ticker chatter-volume counter, and is not directly reusable as the
new mechanism's engine. What it actually does:
- Reads `opal-news-articles` (DynamoDB, PK=`article_date`) over a rolling `DAYS_BACK=7`
  window.
- Extracts free-text KEYWORDS/PHRASES from already-ingested article titles+summaries
  (NLTK + finance stopwords, GPT-4o-mini junk filtering, HDBSCAN embedding clusters).
- Scores each keyword/cluster by **exponential time decay**
  (`DECAY_LAMBDA=1.386`, ~12h half-life — NOT the 14-day/λ=0.05 figure carried over from
  an earlier summary in this session; the deployed value in the file today is 1.386,
  cited at `lambda_function.py:76`).
- Writes `trending_reports/latest.json` to S3 + a balanced (bullish/neutral/bearish)
  keyword list for the portal word cloud.
- Triggered 2x/day (`cron(15 11,21 * * ? *)`, i.e. ~7:15 AM / 5:15 PM ET) by
  `infra/aws/terraform/news-pipeline/eventbridge.tf:161-165`, itself fed by a 21-rule
  NewsAPI+RSS ingestion schedule (`news-ingestion-scheduler`, 16 rules) running roughly
  every 1-2 hours around the clock into `opal-news-articles`.

**What we take from it:** the ARCHITECTURAL PATTERN (rolling N-day window read,
exponential decay so older activity fades gracefully rather than falling off a cliff,
S3 latest.json + dated archive, async chain-invoke to the next stage) — not the code
itself. The new mechanism needs a per-TICKER SERP hit-count time series, which is a
different, simpler, and much cheaper input than full article text; it does not need
GPT junk-filtering, embedding clustering, or FinBERT sentiment, because it isn't trying
to summarize a topic — it's trying to produce one number per ticker per day.

### 3.3 The existing SA scraper's wave pattern — `infra/aws/terraform/seeking-alpha/main.tf`

Confirms the estate already has a proven coordinator → dedup → scraper wave shape for
pacing platform hits (`analysis-coordinator` → `analysis-listing-parser` →
`analysis-dedup` → `analysis-scraper`, with `TRIGGER_WAVE_SIZE`/`TRIGGER_WAVE_DELAY`
env vars already used for exactly this kind of self-throttling). **This also confirms
the problem is live today, not hypothetical:** both existing SA pipelines
(`seeking-alpha-analysis-daily` at 9 PM UTC and `seeking-alpha-news-daily` at 9 AM ET)
currently run as broad, undifferentiated sweeps — there is no per-ticker gate today.
The new mechanism's job is to sit in FRONT of a Bloomberg/FT/WSJ/SA equivalent of this
same wave shape and narrow the input list before the wave starts.

### 3.4 Confirmed gap — no existing per-ticker chatter-volume store

No DynamoDB table or S3 prefix currently holds a rolling per-ticker SERP-hit-count
time series. `opal-news-articles` stores full ingested articles, keyed by date, not raw
search-hit counts — a different grain entirely. This mechanism needs a new, small table
(§5).

---

## 4. Proof #1 — the SERP signal is real and differentiable (with a live query-construction lesson)

Tested live against Bright Data's MCP `search_engine`/`search_engine_batch` tools this
session (after a genuine MCP connection outage was resolved by Andrew reconnecting it —
confirmed via repeated identical `HTTP 400` failures across three different tool calls
before the reconnect, and clean structured JSON after).

**The lesson, proven by a direct side-by-side retest:** ticker + casual name produces
unusable results; ticker + proper legal-name suffix does not.

| Query | Organic results |
|---|---|
| `RTX Raytheon stock news` | **0** — "RTX" collides with NVIDIA's GeForce RTX product line; "Raytheon" alone as a modifier isn't enough to disambiguate |
| `RTX Corporation stock news` | **9**, all on-topic |
| `"RTX Corporation" stock news` (quoted) | **9**, all on-topic |

**Consequence for the design:** the per-ticker query template MUST use the security's
full legal name, not a nickname or bare ticker+sector guess. This is why §5 specifies a
`legal_name` field as required, not optional, on the universe input — a query built
from ticker alone will silently under-count exactly the tickers most prone to name
collisions (RTX/GameStop-adjacent tickers, single-word common-noun-colliding names,
etc.), which would corrupt the ranking rather than just fail loudly.

---

## 5. The mechanism

### 5.1 Two-tier ranking, computed once per SERP cycle

Proven via `org/tier1_exec/4.0.0_SA_CRO/scripts/chatter_ranking_poc.py` (synthetic
7-day dataset, 8 tickers) — re-run directly against the committed copy of the script;
this is the actual console output, not a projection:

```
TRENDING (top absolute volume today):
  NVDA: 9
  GME: 9
  AAPL: 7

BREAKOUT (top % jump vs 6-day baseline, min absolute jump >= 3):
  GME: +362% (today=9, baseline=1.17)

ACTIVE MONITOR SET (union, gets daily platform refresh): ['AAPL', 'GME', 'NVDA'] -- 3 of 8 tickers
Noise check: SLEEPY/SMALLCO (near-zero baseline, tiny blips) excluded from breakout: True
```

Note RTX (`[4,3,4,5,4,4,5]`) does NOT appear in Breakout even though its today-value (5)
is its 7-day high: `abs_jump = 5 - 4.0 = 1.0`, below `MIN_ABSOLUTE_JUMP=3` — correctly
read as "consistently active" (already captured if it ever cracks Trending), not
"breaking out."

**Trending** = highest absolute chatter volume TODAY. Rewards mega-caps that are
*consistently* in the news (NVDA in the synthetic set: `[9,8,9,10,9,8,9]` — always
loud, always relevant).

**Breakout** = highest PERCENTAGE jump vs. the trailing 6-day baseline (today excluded
from its own baseline average). Rewards tickers going from quiet to loud (GME:
`[1,1,1,1,1,2,9]` — a real spike). Two noise guards, both load-bearing and both proven
in the POC:

1. **`BASELINE_SMOOTHING = 1.0`** (Laplace-style) — added to the baseline denominator
   before computing percentage jump. Without it, a ticker with a true zero baseline
   (`[0,0,0,0,0,0,1]`) produces a divide-by-zero / undefined-infinite percentage. With
   smoothing, it produces a finite, comparably-small percentage that a real spike still
   beats.
2. **`MIN_ABSOLUTE_JUMP = 3`** — a candidate must gain at least this many raw mentions
   today, not just a big percentage. Without this guard, SLEEPY's `0 -> 1` jump reads as
   "infinite percent" and would falsely dominate Breakout over GME's real `1 -> 9`
   spike. Confirmed in the POC output: **SLEEPY and SMALLCO are correctly excluded.**

**Union, not intersection:** the daily-refresh set is `TOP_N Trending ∪ TOP_N Breakout`
(TOP_N=3 in the POC; a real value TBD with Andrew, see §7 open question). A name can
win both lists; the union just narrows how many DISTINCT tickers get the expensive
per-platform pull. In the 8-ticker POC this took 8 → 3. At real universe scale (say the
~89-name AMGT_RESAPP set), with TOP_N=10 each, the theoretical worst case is 20 tickers
(no overlap) and the realistic case is fewer, since a Breakout winner is very often
already a Trending winner by the day the platforms actually need to be hit.

### 5.2 Where the raw daily number comes from — the SERP fetch

One `serp_search(f'"{legal_name}" {ticker} stock news', engine="ddg")` call per ticker
per day (DDG primary, Bright Data `serp_brightdata` fallback per §3.1). The chatter
number is the **organic result count** returned by that one call — no scraping of the
result pages themselves, no article text, just a count. This is the cheapest possible
signal: one HTTP GET per ticker per day, run once (not per-platform — see §6, this is
shared across all four downstream platform machines).

At an ~89-name universe: 89 DDG calls/day, well within the `per_sleep=1.2` pacing
already coded into `serp.py`'s `ddg_search` (≈2 minutes total wall-clock for the whole
universe, run once, not per-platform).

### 5.3 New DynamoDB table — `opal-ticker-chatter-daily`

No existing table holds this (confirmed, §3.4). Minimal schema:

| Field | Type | Notes |
|---|---|---|
| `ticker` (PK) | String | e.g. `NVDA` |
| `date` (SK) | String (`YYYY-MM-DD`) | one row per ticker per day |
| `chatter_count` | Number | raw SERP organic-result count for that day |
| `source_engine` | String | `ddg` or `brightdata` — which path served this day's number (Rule-22-style provenance; lets a later analysis distinguish a real zero from a fallback-path anomaly) |
| `query_used` | String | the exact query string sent — audit trail for the query-construction lesson in §4 |

7-day rolling reads use `Query` on `ticker` with a `date BETWEEN` condition — same
access pattern shape as `news_trending_analysis`'s date-partition reads, just keyed by
ticker instead of by global date, because the consumer here needs a per-ticker series,
not a global one.

### 5.4 Legal-name source for query construction — confirmed, no clean field exists

Checked directly: there is **no dedicated `legal_name`/`company_name` field** anywhere
in AMGT_RESAPP, and no broader ticker→legal-name security master exists elsewhere in
the repo (checked ETF/positioning data, `data/etf_dashboards/`, `data/yang/` — no hits).
The only human-readable name is the **folder string itself** in `universe.json` (e.g.
`"Boeing BA"`, `"Kimberly Clark KMB"`, `"Alibaba BABA"`) — folder name minus the ticker
suffix is a workable proxy for the legal name used in §4's query template. Not a clean
structured field, but sufficient: it already carries the exact distinguishing word
(`"Boeing"`, `"Kimberly Clark"`) that the RTX lesson in §4 showed is the difference
between 0 and 9 results. Recommend the universe loader parse `folder` into
`{ticker, name_hint}` once at load time rather than adding a new manual field — this
avoids a second place for the two to drift apart.

---

## 6. Concurrency and pacing across the four platforms

Andrew's framing: "all three [sic — four] can be getting hit at the same time by the
respective machines since they're on different platforms," each at "1 request every 1m
or 2m." This is confirmed correct and requires no new orchestration complexity:

```
                    ┌─────────────────────────────┐
                    │  ONE daily chatter-volume    │
                    │  job (§5.1-5.3): SERP every  │
                    │  tracked ticker, rank, write │
                    │  ACTIVE MONITOR SET to S3    │
                    └──────────────┬───────────────┘
                                   │  active_monitor_set.json
                                   │  (Trending ∪ Breakout tickers)
              ┌────────────────────┼────────────────────┬────────────────────┐
              ▼                    ▼                    ▼                    ▼
     Seeking Alpha machine   FT machine          Bloomberg machine     WSJ machine
     (sa_harvest_session.py) (ft_harvest_...)    (bloomberg_harvest_..)(wsj_rest_fetch.py)
     1 req / 1-2 min,        1 req / 1-2 min,    1 req / 1-2 min,      1 req / 1-2 min,
     ONLY the active set     ONLY the active set ONLY the active set   ONLY the active set
```

Each platform machine is already independent (separate credentials, separate sessions,
separate secrets) — nothing about running them concurrently is new. The ONLY new
coordination point is that all four now read the SAME `active_monitor_set.json` (or
equivalent DynamoDB flag) instead of each independently deciding "what's my ticker
list today," so a ticker that isn't Trending or Breakout gets skipped by all four
platforms uniformly, not just some of them.

This mirrors the existing SA coordinator→dedup→scraper wave shape (§3.3) — the new
piece is simply that the "coordinator" step's input list is now the chatter-volume
gate's output instead of "every listing page found today."

---

## 7. Open questions for Andrew before this becomes an L4 line item

1. **TOP_N per ranking** — the POC used 3 for an 8-ticker toy set. At real universe
   scale, is 10 (per Andrew's own "top 10 movers" framing) the right per-list number,
   or should Trending and Breakout have different N?
2. **Universe size** — confirm ~89 vs. some other final count before the tracked-ticker
   list is frozen (§0). Not a blocker to building the mechanism.
3. **What happens to a ticker that's neither Trending nor Breakout for N consecutive
   days** — does it ever get a "just in case" refresh (e.g. once a week regardless), or
   does staying off both lists mean staying unrefreshed indefinitely? Not specified by
   Andrew's original framing; worth a one-line ruling so it's not silently decided by
   whoever builds it.
4. **`find-dualbiz`-scoped secrets reuse** (§3.1) — fine to reuse, or mint an
   AMGT_RESAPP-scoped Bright Data SERP secret to keep the two projects' egress
   attributable separately?

---

## 8. Where this lands

Per `1.0.0_SA_CTO~Z`'s message (msg-id 21202, 20260911T053536Z): the SA/FT/Bloomberg/
WSJ mechanisms are already queued for the AMGT_RESAPP round-2 L4 amendment. This
chatter-volume gate is the piece that decides WHEN those four mechanisms fire per
ticker — recommend it folds into the same round-2 amendment, against PRD surface
S13/FWD-11 ("THE SOCIAL FEED"), rather than opening a separate PRD line.
