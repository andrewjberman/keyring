# THE HARVEST BACKFILL PLAN -- social, SERP, and the four premium publications

`4.0.0_SA_CRO~Z`, 2026-09-11 ~23:0xZ. Written on Andrew's instruction to spec the chatter/SERP
backfill, *"put a lot of thought into this, do some testing locally as you write it to assess
feasibility."* Every number below is MEASURED on this device unless a line says MODEL-PRIOR.
**No vendor API was called to write this** -- see §8.

---

## 0. THE HEADLINE, BEFORE THE PLAN

⛔ **THE BINDING CONSTRAINT IS IDENTITY, NOT ACCESS.** We are authenticated for three of the four
publications right now. What we do not have is anything to look **up**.

```
THE UNIVERSE (89 covered names) -- identity-layer resolution, measured
  bloomberg_ticker    34 MEASURED   55 UNRESOLVED
  sa_symbol           10 INFERRED   79 UNRESOLVED     <- INFERRED, not MEASURED
  social_account       0            89 UNRESOLVED     <- ZERO. no handles at all.
  ir_domain            0            89 UNRESOLVED
```

**A social/X backfill addresses 0 of 89 names today. An SA backfill addresses 10.** No API tier, feed
strategy or proxy budget changes that: you cannot pull a company's X feed without knowing its
account, and you cannot query SA by symbol without the symbol.

⭐ **AND THE FIX IS CHEAP AND LOCAL.** The resolver already exists --
`lib/research/identity/resolver.py:39` declares `IDENTITY_KEYS = ("bloomberg_ticker", "sa_symbol",
"ir_domain", "social_account")` and `lib/research/lists/build_lists.py:137` already has
`build_social_accounts()`. **The slots and the code exist; the values were never populated.**
Resolution is desk work against names we already hold -- no scraping, no vendor call, no captcha.

**So the plan is: RESOLVE FIRST, then backfill against resolved identifiers.** Doing it the other way
builds a careful low-and-slow harvester that can address 11% of the universe on SA and none of it on
social.

---

## 1. WHAT WE ARE ALREADY AUTHENTICATED FOR (Andrew's explicit question)

Measured in Secrets Manager on this device, by NAME and LastChangedDate only -- **no secret value was
read, printed or logged**:

| publication | session | parked |
|---|---|---|
| Seeking Alpha | `seeking-alpha/session` | 2026-09-10 22:13 |
| FT | `astn/ft/session` (+ `astn/ft/credentials`) | 2026-09-10 23:47 |
| Bloomberg.com | `bloomberg/session` | 2026-09-11 01:13 |
| **WSJ** | **NONE** | -- consistent with its Web-Unlocker route |
| Google (SERP) | `google-cse-config` -- `google_api_key` + `google_cse_id`, andrew@fideles.capital | 2025-12-23 |
| Google OAuth | `google/officialmadeaux/*`, `google/andrew-goldengate/*` | 2026-09-10 |

⚠ **PARKED IS NOT VALID.** A `LastChangedDate` proves when a bundle was written, not that it still
authenticates. Step 1 of any run is a cheap liveness probe per publication, and the SA module already
has the discriminator for it (§3).

---

## 2. THE FOUR PUBLICATIONS ARE NOT ONE PROBLEM

⛔ **THEY DIVIDE INTO THREE MECHANISMS, AND ONLY ONE IS BUILT.**

| publication | mechanism | state |
|---|---|---|
| **Seeking Alpha** | authenticated **REST/JSON** + residential proxy | **BUILT AND MEASURED** -- `integrations/seekingalpha/rest_fetch.py` |
| **FT** | browser session harvester (`ft_harvest_session.py`) | session parked; no ETL |
| **Bloomberg.com** | browser session harvester, **Google OAuth** sign-in, same PerimeterX wall as SA | session parked; no ETL |
| **WSJ** | Bright Data **Web Unlocker** (no session) | route named, not built |

⭐ **Bloomberg.com is NOT the Bloomberg Terminal.** `bloomberg_harvest_session.py` is a web session
harvester "ported almost wholesale from `sa_harvest_session.py`" that signs in via Google OAuth and
hits the same PerimeterX Press-and-Hold wall. The Terminal is a separate operation (fundamentals /
model block) and is not part of harvesting.

---

## 3. SA IS THE TEMPLATE, AND BACKFILL THERE IS A PARAMETER SWEEP -- NOT NEW CAPABILITY

This is the most important engineering finding. **The backfill levers are already in the URLs and are
pinned to their minimums.** From `rest_fetch.py:330-356`, verbatim:

```
/api/v3/symbols/{t}/analysis?filter[until]=0&filter[related]=false&id={t}
   &include=author,primaryTickers,sentiments&lang=en&page[number]=1&page[size]={limit}

/api/v3/symbols/{t}/news?filter[since]=0&filter[until]=0&id={t}
   &include=author,primaryTickers,sentiments&page[size]={limit}
```

with `limit = config["articles_per_ticker"]` = **2**, `pace_seconds` = **2.0**,
`max_tickers_per_run` = **3**.

| lever | today | backfill use |
|---|---|---|
| `page[number]` | **hardcoded 1** on analysis | sweep 1..N -- this is the depth dial |
| `page[size]` | 2 | raise to a sane page (config, not code) |
| `filter[since]` / `filter[until]` | **0 / 0** on news (epoch, unbounded) | set `since` = Jan 1 epoch -- **server-side date bounding** |

⛔ **ASYMMETRY, MEASURED:** the **news** endpoint takes `filter[since]`/`filter[until]` but the URL
carries **no `page[number]`**; the **analysis** endpoint takes `page[number]` but carries **no
`filter[since]`**. So: news backfills by DATE WINDOW, analysis backfills by PAGE WALK with
client-side date cutoff. ⚠ Both are JSON:API and probably accept the other parameter -- **that is a
MODEL-PRIOR guess and is the first thing to test.**

**Cost model:** listings are cheap and return ids; each article BODY is one call to
`/api/v3/articles/{id}`. **Article bodies dominate the budget**, so depth is priced per article, not
per ticker.

---

## 4. THE RE-AUTH LOOP ANDREW ANTICIPATED IS ALREADY A WRITTEN CONTRACT

He asked for a plan covering *"authenticate, beat captcha, run REST API, and repeat multiple times."*
`rest_fetch.py`'s docstring already specifies exactly that cycle, measured:

1. **The jar must carry browser-minted PerimeterX cookies AND the identity cookie.** Identity alone
   returns **403**.
2. **Every request must carry a per-ticker `Referer`.** Without it the API answers **200 with a
   near-empty body** -- a SILENT failure, caught by `detectors.empty_body`.
3. **Egress must use the residential proxy.** The native/datacenter IP is PerimeterX-blocked after
   **roughly ten calls**.
4. **A 403 with the challenge marker is the RE-HARVEST signal**, never an auth failure. On it the run
   **STOPS**; the ETL never re-harvests, never signs in, never launches a browser.
5. **GET only.** The residential proxy refuses every POST (`policy_20130`).

⭐ **THE SEPARATION IS THE DESIGN AND THE BACKFILL MUST KEEP IT:** a **harvester** (browser, Kimi-VL
screen classification, `press_and_hold_lib.py` for the wall) mints a session and parks it; an **ETL**
rides the parked session and never authenticates. The loop is therefore:

```
   park session (browser, human-ish, slow)
        |
        v
   ETL rides it  --->  403 + challenge marker  --->  STOP, re-park, RESUME FROM CURSOR
        |
        v
   exhausted window -> advance cursor -> repeat
```

⛔ **THE RESUME CURSOR IS THE WHOLE BACKFILL DESIGN.** A backfill that cannot resume mid-window turns
every cookie expiry into a restart. `rest_fetch.py` already carries `--state-dir` with
`save_state(request_log, sa_ids)` -- **that is the seed of the cursor and it should be the unit of
work**: per (ticker, endpoint, page/window), durable, so a re-harvest costs one page and not one
ticker.

---

## 5. SERP: THE OFFICIAL API PATH, AND WHY ANDREW'S "10 PAGES" IS EXACTLY RIGHT

`google-cse-config` holds a **Google Custom Search JSON API** key and engine id. That is an official,
paid, ToS-clean API -- **not scraping, and not Bright Data.**

⚠ **MODEL-PRIOR, NOT MEASURED -- verify before committing the plan** (I did not call the API, §8):
CSE returns **10 results per request** and caps a single query at roughly **100 results (10 pages)**;
it supports **`dateRestrict`** (e.g. `d30`) and **`sort=date`**; the free tier is ~100 queries/day
with paid tiers beyond.

⭐ **His instinct maps exactly onto the real ceiling: "10 pages" IS the cap, and "last 30 days" IS
`dateRestrict=d30`.** Which means the backfill mechanic for SERP is forced and simple:

⛔ **WINDOW-SLICING.** One query against Jan 1 -> today returns at most ~100 results no matter what.
So slice the window and re-query: **per-month (8 slices) or per-week (~36 slices) per name**, each
capped at 100. Depth then costs queries, and queries are quota, and quota is money -- a knob we can
price exactly once the real limits are confirmed.

**Per-name SERP budget (MODEL-PRIOR arithmetic, to be re-priced after §8):**
`89 names x 8 monthly slices x up to 10 pages = up to 7,120 requests` for a Jan-1 sweep at monthly
granularity. At weekly granularity it is ~32,000. **This is the number that decides monthly vs weekly,
and it should be decided on price, not taste.**

---

## 6. SOCIAL / X

**Blocked at step zero: 0 of 89 handles.** No X integration exists in the estate (`comp-find --band
DEF` over `twitter|x\.com|social_account|cashtag` -> 3 hits, all identity-layer slots, no client).

So X is **net-new build** *and* **net-new identity**, which puts it last. Two honest routes once
handles exist, and the choice is Andrew's because both spend money or risk:

- **Official X API** -- ToS-clean, priced per tier, historical depth is the expensive part.
- **SERP-as-proxy** -- use the CSE path with `site:x.com "<handle>"` window-slicing. No new vendor, no
  new auth, and it reuses §5 exactly. **Much weaker signal** (it finds indexed pages, not the feed)
  but it is nearly free given we are building §5 anyway.

⭐ **RECOMMENDATION: do not build an X client yet.** Resolve handles, then run the SERP-as-proxy
variant for a month, then decide whether the signal justifies an API tier. That defers the only
irreversible spend until there is evidence.

---

## 7. THE PLAN, IN ORDER, WITH THE REASON EACH STEP PRECEDES THE NEXT

| # | step | why it is here and not later | vendor egress? |
|---|---|---|---|
| 1 | **Resolve identity** -- `sa_symbol` to MEASURED for 89, `social_account` for 89, `ir_domain` where it exists | everything downstream is keyed on these; 0 and 10 of 89 today | **NO** |
| 2 | **Liveness-probe the three parked sessions**, one cheap call each | "parked" is not "valid"; a dead session turns a backfill into a captcha loop | yes, 3 calls |
| 3 | **Make the cursor durable** -- per (ticker, endpoint, window), resumable | without it every cookie expiry restarts a ticker | NO |
| 4 | **SA backfill**: sweep `page[number]`, set `filter[since]`, raise `page[size]` off config | the only publication whose route is already built and measured | yes, paced |
| 5 | **SERP backfill** via CSE window-slicing | independent of publication auth; can run in parallel with 4 | yes, quota'd |
| 6 | **FT + Bloomberg.com ETLs**, on the SA template | sessions exist; only the ETL is missing. Port, do not invent | yes, paced |
| 7 | **WSJ** via Web Unlocker | no session; different mechanism; most likely to need a new vendor word | yes |
| 8 | **X** -- decide API vs SERP-proxy on evidence from 5 | defers the only irreversible spend | tbd |

**PACING, and it should be boring on purpose:** keep `pace_seconds >= 2.0`, keep
`max_tickers_per_run` small, run the local box's sweeps sequentially rather than in parallel, and
treat the re-harvest signal as a **stop**, never a retry. The estate's own measurement is that a
datacenter IP dies after ~10 calls; the residential proxy is what buys the runway, and nothing about
going faster improves the outcome.

---

## 8. WHAT I DID NOT DO, AND THE ONE CALL THAT NEEDS ANDREW

⛔ **NO VENDOR API WAS CALLED TO WRITE THIS.** Every finding above comes from the repo, Secrets
Manager metadata, the identity-layer JSON and the live AWS plane. That is deliberate:
`C-VENDOR-WORD-HARVESTERS` grants the per-use word for SA/FT/Bloomberg/WSJ **"effective when the
harvester box is stood up and ready to run -- NOT before"**, and Andrew has since said backfill runs
on **site-Z**, not the EC2 box.

⚠ **SO THE TIME-SCOPE CLAUSE NO LONGER MATCHES THE TOPOLOGY, AND THAT IS A CALL, NOT AN INFERENCE.**
Does the word cover a LOCAL backfill on site-Z, given its clock was written against a box that is now
not where this runs? **I am not reading it either way.** Steps 2 and 4-7 all need it settled.

**Also his, not mine:**
- **Google CSE quota tier and spend ceiling** -- §5's arithmetic is unpriced until the tier is known.
- **Bright Data Web Unlocker for WSJ** -- already the WSJ route, but extending it to the three session
  publications if PerimeterX proves hostile would be a NEW per-use vendor question.
- **X API tier**, if §6 evidence justifies it.

---

## 9. WHAT THIS UNBLOCKS, SO THE VALUE IS LEGIBLE

`lib/research/metrics/chatter_axis.py` is **built, scheduled and live** -- and it ranks by COUNTING
articles per ticker out of the harvest article store, which currently holds **0 rows**. It runs
cleanly and scores every ticker zero.

⭐ **THE CHATTER AXIS IS NOT WAITING ON CODE. IT IS WAITING ON THIS BACKFILL.** Every row this plan
lands is a row that axis can rank, and the Lead Panel reads those pre-computed rows directly.
