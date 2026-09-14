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

⛔ **CORRECTION 2026-09-12, SEE §10 -- THE PRECEDING PARAGRAPH IS WRONG AND THIS SEAT MEASURED IT
AFTERWARDS, NOT BEFORE.** Identity resolution is NOT vendor-free and its LOCAL yield is **ZERO NEW
VALUES**: the pass that exists has already run to its ceiling. Read §10 before acting on §0 or on
step 1 of §7. The rest of this brief stands.

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

---

## 10. CORRECTION (2026-09-12): §0's "CHEAP AND LOCAL" IS WRONG, AND THE FREE MOVE DOES NOT EXIST

⛔ **THIS SECTION CORRECTS THIS SEAT'S OWN HEADLINE RECOMMENDATION, WHICH WAS GIVEN TO ANDREW AS THE
ONE THING THAT NEEDED NO DECISION.** The words in §0 were *"Resolution is desk work against names we
already hold -- no scraping, no vendor call, no captcha"*, and §7 step 1 carries **vendor egress? NO**.
Both are false. What follows is measured; the original text is left standing above so the error is
legible rather than quietly removed.

### What the code's own bounds say -- and this was readable before the brief was written

`lib/research/identity/resolver.py`, module docstring, BOUNDS:

> *"ir_domain and social_account are UNRESOLVED at this cut, and the record says so plainly --
> **resolving them needs a SERP zone request and social lookups, each a vendor call this order does
> not carry the word for.**"*

So **two of the three keys named in step 1 are vendor-gated at the source**, stated by the module this
brief cited as evidence that the work was free. `sa_symbol` to MEASURED is likewise not local: the
numeric `sa_id` comes from the SA fetch path (AMGT-s-b4), also a vendor call. The module resolves
`sa_symbol` at most to INFERRED, and only from an already-MEASURED US ticker.

### The local yield, measured over the whole population rather than recalled

| key | state | NEW values obtainable with NO vendor call |
|---|---|---|
| `bloomberg_ticker` | 34 MEASURED / 55 UNRESOLVED | **0** -- local sources exhausted |
| `sa_symbol` | 10 INFERRED / 79 UNRESOLVED | **0** -- all 10 US-suffixed MEASURED tickers already inferred |
| `ir_domain` | 0 / 89 UNRESOLVED | **0** -- needs a SERP zone request |
| `social_account` | 0 / 89 UNRESOLVED | **0** -- needs social lookups |

`lib/research/identity/coverage_pass.py` **is** the "resolve locally" pass, it has already RUN (it is
what produced the 34, up from 32), and it names and checks three local sources, recording a null
contribution as a finding rather than a skip. Its residual, subtracted over the denominator rather
than listed forward:

    55 UNRESOLVED  =  40 with NO one-pager workbook on this device (PDF-only research material)
                   +  15 with a workbook whose only valid-shaped label hit is the shared
                         'AAPL US' template placeholder (or, for Rio Tinto, an
                         '#N/A Invalid Security' artifact)

There is no fourth local source. The gap is **data that is not on this device**, not work nobody did.

### The one large local lever left is ANDREW'S CALL AND IS ALREADY CARDED

`.../0.9.0_WK_AMGT_RESAPP~4/DESIGN_QUESTION_identity_fallback.md` -- marked **"Not coded. Not
exercised. Andrew's call, not this cell's."** The mechanism: read the trailing Bloomberg-shaped token
off a directory's own name (`Nestle NESN SW` -> `NESN SW`). Its own assessment: **up to 15 additional
INFERRED**, *"the single largest lever available on this identity layer, larger than every
workbook-read source combined -- it is just not a MEASURED lever."*
⚠ It reads **whoever named the directory's belief**, not the company's identity, and the document
records an OBSERVED failure mode in this corpus (`Nokia FH` yields the ambiguous `FH`). That is why it
is a call and not a default.

### Why the error happened, since the mechanism recurs

The brief read that `resolver.py` **declares** all four keys and that `build_social_accounts()`
**exists**, and concluded the values could be populated. **THE SLOTS EXISTING IS NOT THE VALUES BEING
OBTAINABLE** -- and the same file's BOUNDS said so, four lines from the line that was cited. This is
the night's recurring shape one more time: a DECLARATION read as a CAPABILITY, and a source quoted for
the half that supported the conclusion.
⭐ **The practical rule: when a module is cited as evidence that work is cheap, read its BOUNDS
section before quoting its API.** A module that knows what it cannot do usually says so.

### What this changes for the decision

**It does not slow anything down; it sharpens the ask.** §8's single call was *"does the vendor word
cover a local site-Z backfill"*. The corrected picture is that **every remaining step -- including the
identity step this brief offered as free -- sits behind that word or behind the design call above.**
There is no longer a "start here while deciding" item, and §7's ordering still holds: identity first,
because a backfill against 10 of 89 names is the more expensive mistake.

---

## 11. THE ANALYTICS HALF (Andrew-direct 2026-09-13 ~03:2xZ) -- WHAT THE BACKFILL MUST DELIVER FOR THE `*harvest` ANALYTICS TO MEAN ANYTHING

⛔ **ADDED BECAUSE HIS DIRECTION NAMES TWO THINGS AND §1-10 SPEC ONLY ONE.** Verbatim: *"the backfill
for the news in the opal-data-harvest and assocaited \*harvest analytics need to be figured out"*.
Sections 1-10 spec ACQUISITION. This section specs what the analytics REQUIRE of it -- read from the
producer's own constants, not proposed.

### The consumer's ratified constants, read at source

`lib/research/metrics/chatter_gate.py`: **`WINDOW_DAYS = 30`**, `TOP_N = 10`, `SCORE_MIN/MAX 0..100`.
`lib/research/metrics/chatter_axis.py` computes **TWO ranking products every run**:

| product | ranks by | what it needs from the store |
|---|---|---|
| `TRENDING_CHATTER#<as_of>` | absolute chatter volume **ON the as-of day** | that ONE day populated |
| `BREAKOUT_CHATTER#<as_of>` | percentage jump of that day **against the trailing baseline** | the as-of day **AND the 29 days before it** |

⛔ **AND BREAKOUT CARRIES A RATIFIED FLOOR: a minimum ABSOLUTE jump of 3 RAW MENTIONS.** The module's
own words: against an all-zero baseline *"no ticker gains the ratified minimum absolute jump (3 raw
mentions) ... so NO ticker"* ranks. **A perfect 30-day backfill that yields 1-2 mentions for a ticker
produces NOTHING for that ticker on the breakout axis.**

### ⭐ SO ANDREW'S OWN INSTRUCTION ALREADY MATCHED THE CODE, AND NOBODY HAD CONNECTED THEM

His original words for this brief were *"at least a month, preferably as far back as jan 1"*. Measured
against `WINDOW_DAYS = 30`:
- **"AT LEAST A MONTH" IS EXACTLY THE MINIMUM VIABLE BACKFILL** -- it is the smallest history that
  makes ONE day's BREAKOUT computable, because the baseline is the 29 days before the as-of day.
  One day short and breakout ranks on a truncated baseline; a month gives exactly one valid as-of day.
- **"PREFERABLY BACK TO JAN 1" IS WHAT MAKES THE AXIS RECOMPUTABLE FOR ANY PAST DATE.** With ~8 months
  of history the axis can be run for any historical `as_of_date`, so the ranking becomes a time series
  rather than a single snapshot -- and a wrong ranking today can be re-derived rather than re-harvested.
**His month/Jan-1 pair was not a rough preference. It is the minimum and the useful target of the
consumer's own ratified window, and the two land on the same numbers.**

### THE THREE THINGS THE BACKFILL MUST DELIVER, in acceptance terms

1. **DATE COVERAGE >= 30 CONSECUTIVE DAYS per ticker**, ending at the intended as-of date. Below that
   BREAKOUT is not merely weak, it is **uncomputable** -- the baseline does not exist.
2. **PER-TICKER DENSITY >= 3 MENTIONS on any day expected to rank.** Date range alone is insufficient:
   a sparse ticker with full date coverage still ranks nowhere. **Density is a separate axis from
   coverage and the brief's §7 pacing plan optimises only coverage.**
3. **`published_at` PRESENT AND CORRECT ON EVERY ROW.** The producer reads the window by
   `published_at` via the GSI and never reads an article body. **A row with a wrong or missing
   `published_at` is invisible to the axis no matter what else it carries** -- so a backfill that
   captures content but loses the date is worth nothing to this consumer.

### WHAT THIS CHANGES IN §7's PLAN, AND IT IS ONE LINE

§7 sequences acquisition by publication and paces by rate limit. **It should sequence by TICKER-WINDOW
COMPLETENESS instead**: a ticker with 30 unbroken days is worth more than three tickers with ten days
each, because the first produces a rankable signal and the second produces none. **Finish a ticker's
window before starting the next.** Same total calls, same pacing, different order, and the difference
is whether the analytics can run at all before the sweep completes.
⚠ NOT CHANGED: §0's identity finding still binds and is upstream of all of this. **A perfect backfill
against 10 resolvable SA symbols of 89 still feeds the axis 10 tickers.** Density and coverage are
requirements on names we can already identify; they do not substitute for the identity work.

### PRECONDITION, NAMED AS 22186 ASKS

**This section needs no harvester box and no vendor word.** It is read from the consumer's committed
constants and is executable as an acceptance spec the day acquisition begins. **The DESIGN is not
blocked; only the EXECUTION is**, and by exactly the items in §8 plus the box.

---

## 12. ANDREW'S RULINGS (2026-09-13 ~03:3xZ) FOLDED IN -- AND THE GRANTED ROUTE IS MEASURED DOWN

### What he cleared, verbatim-scoped

| his item | ruling | what it unblocks here |
|---|---|---|
| social data trigger | **GRANTED, on BRIGHT DATA SPECIFICALLY.** *"They can do that ... i was expecting that they would use bright data"* | `social_account` 0/89 |
| another provider | *"could be ok but need more details on who that is"* -- **a FRESH ASK naming the provider, not a granted one** | -- |
| drafting model | **`5.6-Sol`** | out of this brief's lane |
| terminal count | **89**, *"they do have egress for 89"* | the classification pass |
| the condition on it | *"be parsimonious about pulls until the shape and info is confirmed so we dont waste data quota on broken calls"* -- **A SEQUENCE, NOT A CAP** | §7 pacing |
| publications | **FT, WSJ, SA, BBG** -- "the four harvest publications" | §2's set, confirmed |
| ⭐ **SCOPE ADDITION he volunteered** | SERP to find these companies' **INVESTOR RELATIONS pages and any blogs on their own sites**; *"scraping that stuff is fine and in scope"* | **`ir_domain` 0/89, and a SOURCE this brief did not have** |

⛔ **WHAT HE DID NOT ANSWER AND THIS BRIEF DOES NOT INFER:** who OWNS the publisher list and the
company-to-social map. He gave the list's CONTENTS and named no owner. **A list with four correct
entries and no owner is exactly what FWD-14 exists to catch.**
⚠ **AND THE HARVESTER BOX IS STILL THE CLOCK ON THE FOUR-PUBLICATION PERMISSION.** These rulings do
not re-scope that, and this brief does not read them as doing so.

### ⛔ THE GRANTED ROUTE IS DOWN. MEASURED, TWO ARMS, ZERO QUOTA SPENT.

His words assume the capability is in hand: *"for which they should have the mcp and should be able to
figure it out."* Tested immediately, on the smallest possible probe, exactly as his parsimony
instruction directs:
```
mcp__brightdata__search_engine   "AstraZeneca investor relations official site"
   -> HTTP 400 dialing https://mcp.brightdata.com/sse?token=REDACTED
mcp__brightdata__scrape_as_markdown   https://www.astrazeneca.com/investor-relations.html
   -> HTTP 400 dialing https://mcp.brightdata.com/sse?token=REDACTED
```
**TWO DIFFERENT TOOLS, IDENTICAL FAILURE AT THE DIAL STAGE.** That isolates it to the TRANSPORT or the
TOKEN, not to a malformed query or one broken tool.
⭐ **AND THE FAILURE COST NOTHING, WHICH IS THE POINT OF HIS OWN INSTRUCTION.** The call never reached
the API, so no data quota was consumed. **"Be parsimonious until the shape is confirmed" earned its
keep on the first probe: a 1-call test found a broken route before an 89-name sweep could waste
anything on it.**
⚠ **NOT DIAGNOSED AND NOT THIS SEAT'S SURFACE:** whether the token is expired, the endpoint moved, or
the account is unprovisioned. Reported as a state, not a cause.

### THE ONE NARROW QUESTION THIS RAISES, WHICH IS HIS AND IS NOT ASSUMED

The estate holds an **official Google Custom Search API key and engine id** (`google-cse-config`) --
a DIFFERENT provider from Bright Data. His social-trigger grant names Bright Data and says another
provider needs *"more details on who that is"*; his SERP/IR-pages sentence names no provider at all.
⛔ **THOSE ARE TWO DIFFERENT SENTENCES AND THIS SEAT WILL NOT MERGE THEM.** Reading "use SERP" as
covering a provider he did not name would be exactly the widening the estate forbids.
**THE ASK, one line: does the IR-page/blog SERP work run on the Google CSE key the estate already
holds, or does it wait for Bright Data to be repaired?** Either answer unblocks it; the question is
which route is authorised, not whether the work is.

### What proceeds WITHOUT any further word, right now

- §11's acceptance requirements -- coverage >= 30 days, density >= 3 mentions, `published_at` correct
  -- are read from committed constants and need no vendor at all.
- §7's re-sequencing to TICKER-WINDOW COMPLETENESS is a plan change, not a call.
- The identity layer's `bloomberg_ticker` gap (55 of 89) is still gated on the **directory-name
  fallback**, which remains HIS unanswered design question and is the one lever needing no vendor.

---

## 13. THE IR-SEARCH ROUTE IS CONFIRMED WORKING -- ONE CALL -- AND THE PROBE FOUND A DEFECT THAT TOP-HIT SELECTION WOULD HAVE SHIPPED

**Authority:** Andrew-direct 2026-09-13 ~04:0xZ, card 4: run the investor-relations and blog search on
**the Google Custom Search key the estate already holds**, IR pages and company blogs, **SEARCH ONLY**,
and his prove-the-shape-first rule applies. **A per-use word for ONE provider for ONE purpose.**

### The shape, confirmed on a single call

```
secret   google-cse-config   keys: description, gmail_account, google_api_key, google_cse_id
route    GET https://www.googleapis.com/customsearch/v1?key=<...>&cx=<...>&q=<...>&num=5
probe    q = "AstraZeneca investor relations"
result   HTTP OK | totalResults 306,000 | 1 call spent
```
**QUOTA SPENT: ONE CALL.** Nothing further was run. His sequence -- prove the shape, then spend -- is
satisfied and the bulk pass has NOT begun.
⚠ No key or id value is recorded here or anywhere in this brief; the secret was read through a pipe
and never written to disk.

### ⛔ THE DEFECT THE PROBE FOUND, AND IT IS THE REASON TO PROBE

The five returned results were:
```
1. Investor relations - AstraZeneca        astrazeneca.com/investor-relations.html   <- correct
2. Joris Silon ... #investorrelations      linkedin.com/posts/...                    <- social noise
3. Results and presentations - AstraZeneca astrazeneca.com/investor-relations/...    <- correct
4. Kyntra Bio: Investor Overview           investor.kyntrabio.com/investor-overview  <- A DIFFERENT COMPANY
5. Events - AstraZeneca                    astrazeneca.com/investor-relations/events <- correct
```
>> **RESULT 4 IS ANOTHER COMPANY'S INVESTOR-RELATIONS PAGE, RETURNED INSIDE A QUERY THAT NAMED
   ASTRAZENECA.** On this query the top hit happens to be right, so a top-hit rule would have passed
   its own test and then silently assigned a WRONG IR DOMAIN to some other name in the 89. **The
   failure would not announce itself: a plausible IR domain for the wrong company looks exactly like
   a correct answer.** <<

### THE ACCEPTANCE CRITERION THIS FORCES, which is new

**AN `ir_domain` VALUE IS ACCEPTED ONLY IF THE RETURNED DOMAIN IS INDEPENDENTLY TIED TO THE SUBJECT
COMPANY -- NEVER BY RANK POSITION.** Concretely, at least one of:
- the registrable domain contains the company's own name token (`astrazeneca.com` for AstraZeneca); or
- two or more of the returned results share that same registrable domain (here THREE do, which is the
  signal that actually distinguishes AstraZeneca's domain from Kyntra Bio's single hit); or
- the domain matches a value already held for that company from another key.
**Where none holds, the value is UNRESOLVED, not a guess.** This is the same discipline the identity
layer already applies to `bloomberg_ticker`: a rule that cannot discriminate REFUSES rather than
returning its best candidate.
⭐ **AND THE MULTI-RESULT-AGREEMENT TEST IS THE STRONGEST OF THE THREE** and costs nothing extra --
it is already in the response that was paid for. One company's real IR presence produces several pages
on one domain; a wrong-company hit produces one.

### What is NOT yet done, stated so this does not read as finished

- **THE BULK PASS HAS NOT RUN.** 89 names, one call each, is the next act and it is deliberately not
  taken at 04:3xZ without the criterion above implemented and the results reviewed.
- **BLOGS are in his grant and are NOT probed.** Only the IR half has a confirmed shape; a company blog
  may need a different query form and that is unmeasured.
- **`social_account` IS UNAFFECTED AND STILL BLOCKED** -- it runs on Bright Data, whose stored key is
  measured STALE and whose rotation is the account owner's act.

---

## 14. THE BULK PASS HAS RUN: `ir_domain` GOES 0 OF 89 TO 79 OF 89 -- AND THE TEST s.13 LISTED FIRST IS THE ONE THAT NAMES THE WRONG COMPANY

**Authority:** unchanged -- Andrew-direct 2026-09-13 ~04:0xZ card 4, the Google Custom Search key,
IR and blog search, SEARCH ONLY. **No other provider was called and no result page was fetched.**
**Artifacts:** `deliverables/IDENTITY_IR_DOMAIN_PASS_20260913_Z.json` (89 records, each carrying its
own adjudication) and `scripts/ir_domain_bulk_pass.py` (the rule, runnable and auditable).

### The result, with its denominator

```
universe                         89
ir_domain INFERRED               79        <- was 0 of 89 at every prior cut
ir_domain UNRESOLVED             10
CALLS SPENT                      92   = 1 shape probe + 12 adversarial + 77 remainder
                                        + 1 raw diagnostic + 1 re-run after a repair
```
⚠ **THE STATUS IS `INFERRED`, NOT `MEASURED`, AND THE SCRIPT WAS CORRECTED TO SAY SO BEFORE THE
DELIVERABLE LANDED.** These values come from SEARCH METADATA -- result URLs and index titles. **No
page was read**, because card 4 is search-only. Promotion to MEASURED means fetching the page and
confirming it names the company; that is a scrape, and its route (Bright Data) is blocked on the key
rotation. **So the identity layer gains 79 rejectable values, not 79 confirmed ones**, and a consumer
can refuse them on the status field exactly as the rule intends.

### ⛔ THE FINDING: s.13 ORDERED THE TESTS (a), (b), (c) -- AND (a) IS THE ONE THAT PICKS A DIFFERENT COMPANY

s.13 asserted that multi-result agreement is "the strongest of the three". **That is now MEASURED,
and the measurement is far stronger than the claim was.** Across the 10 refusals:

| | test (a), the name token | test (b), multi-result agreement |
|---|---|---|
| named a DIFFERENT LISTED COMPANY | **8 of 10** | 0 of 10 |
| named a wrong entity inside the right group | 2 of 10 | 0 of 10 |
| named the correct domain | **0 of 10** | **7 of 10** (3 were genuine ties) |

Concretely, what test (a) elected: `mitsubishi-hc-capital.com` for Mitsubishi UFJ; `sumitomocorp.com`
for Sumitomo Mitsui; `taiwansemi.com` for TSMC; `tpgtelecom.com.au` for Singapore Telecom;
`globalterminals.com` for International Container Terminals; `walmart.com` for Walmart de Mexico;
`akerbp.com` for BP; `federatedhermes.com` for Hermes. **Every one is a real, separately listed
company whose name genuinely contains the token.**

>> **THE CONSEQUENCE, STATED PLAINLY: HAD THE THREE TESTS BEEN IMPLEMENTED AS A PRECEDENCE ORDER IN
   THE ORDER s.13 WRITES THEM, THIS PASS WOULD HAVE SHIPPED EIGHT WRONG COMPANIES' DOMAINS AND EACH
   WOULD HAVE LOOKED EXACTLY LIKE A CORRECT ANSWER.** The thing that caught all eight is not in
   s.13's list at all -- it is the **CONFLICT BRANCH**: when (a) and (b) disagree, take NEITHER.
   A criterion written as "at least one of" invites an OR; the value came from the AND. <<
⭐ The kyntrabio probe result that forced this criterion was a *rank* defect. **The real defect is not
rank -- it is that a company name is not a unique key**, and only corroboration across results
separates two companies that share one.

### The three corrections this pass made to the criterion, all disclosed rather than folded in

1. **NON-COMPANY DOMAINS ARE EXCLUDED BEFORE THE TESTS RUN.** s.13's test (b) says only "two or more
   results share that same registrable domain". Run literally, three LinkedIn hits elect
   `linkedin.com` -- with the agreement test firing exactly as specified. Aggregators, exchanges,
   social networks and news are removed first.
2. **PRESS-RELEASE WIRES joined that set after the first full pass.** A wire carries the company's own
   releases, so it clears the agreement test like a real IR site and is the most convincing wrong
   answer available. `newsfilecorp.com` reached n=2 on Telefonica Brazil, one result from election.
   ⭐ **The re-adjudication changed ZERO verdicts** -- re-run over the STORED results at zero call
   cost, with a replay control (re-deriving the original verdicts under the original set: 0 drift).
   So the result is stable against this repair, which is a measurement, not a hope.
3. **Test (c) CONTRIBUTED NOTHING AND THAT IS RECORDED AS A NULL, NOT A SKIP.** No company held a
   prior `ir_domain` from another key -- the layer was 0 of 89 -- so the branch was live and inert.

### ⛔ ONE DEFECT WAS IN THIS PASS'S OWN INSTRUMENT, AND THE CRITERION ABSORBED IT

`.bank.in` is the Reserve Bank of India's exclusive domain for Indian banks, so ICICI's registrable
domain is `icici.bank.in`. It was missing from the two-label-suffix set, so the extractor returned
`bank.in` -- **discarding the one label that names the company** -- and four results collapsed onto a
suffix. Test (b) duly elected it; test (a) named `icicibank.com`; **they disagreed and the pass
REFUSED.**
>> **AN EXTRACTOR DEFECT BECAME A REFUSAL INSTEAD OF A WRONG ANSWER.** That is what fail-closed buys,
   and it is worth more than the 1-in-89 it cost. Repaired; ICICI re-run on ONE call and now
   `icici.bank.in`, accepted by both tests agreeing. <<
⚠ **AND IT WAS FINDABLE ONLY BECAUSE IT PRODUCED A REFUSAL.** A suffix collapse that produced an
ACCEPT would have been silent. The accepted 79 were inspected by eye for that shape and none is a
bare suffix -- but that is an inspection, not a gate, and a full Public Suffix List is the real fix
if this layer ever becomes load-bearing.

### The zero-call dry run earned its own existence

The name rule strips trailing Bloomberg-shaped tokens off a folder name -- the exact complement of
the identity fallback rule that reads those same tokens as a ticker. **Printing all 89 derived
queries before spending anything found two folders where the stripped token WAS the identity:**
`Koninklijke KPN NA` -> "Koninklijke" (a Dutch honorific carried by Philips, Ahold and KLM alike) and
`Manila MER PER` -> "Manila" (a city). Both are recorded as named overrides with their reason.
**Two wrong queries caught for zero quota**, by inspecting a printed population rather than trusting
a rule that had already been validated 15-for-15 on a different question.

### THE 10 REFUSALS, WITH THE CANDIDATE ALREADY IN HAND

Converting any of these later costs **ZERO further calls** -- the candidate and its result count are
in the record's `adjudication` block.

| name | test (b) candidate | why it was refused |
|---|---|---|
| Mitsubishi UFJ Financial Group | `mufg.jp` (5 of 10) | (a) named Mitsubishi HC Capital |
| Sumitomo Mitsui Financial Group | `smfg.co.jp` (4) | (a) named Sumitomo Corporation |
| Taiwan Semiconductor Manufacturing | `tsmc.com` (7) | (a) named Taiwan Semiconductor Co |
| Walmart de Mexico | `walmex.mx` (5) | (a) named Walmart Inc, the US parent |
| Singapore Telecom | `singtel.com` (4) | (a) named TPG Telecom |
| International Container Terminals | `ictsi.com` (2) | (a) named Global Container Terminals |
| BNP Paribas | `invest.bnpparibas` (3) | the group's own estate is split across 7 domains |
| **BP** | tie `bp.com` 4 / `akerbp.com` 4 | **Aker BP is a separate listed company** |
| **Hermes** | tie `hermes.com` 3 / `federatedhermes.com` 3 | **two real companies share the name** |
| **Telefonica Brazil** | tie `telefonica.com` 2 / `telefonica.com.br` 2 | parent vs the Brazilian listco |

⭐ **THE LAST THREE ARE A DIFFERENT CLASS AND NO SEARCH HEURISTIC RESOLVES THEM.** A dead tie between
two genuinely existing companies is not a weakness of the rule -- it is the rule reporting that the
QUESTION is under-specified. **Each needs one line from whoever owns the holding**, and for Telefonica
Brazil the folder name itself ("Brazil", VIVT3) already contains the answer. **They are the only three
of the 89 that need a human.**

### What is STILL not done, so this does not read as finished

- ⛔ **BLOGS ARE IN CARD 4'S GRANT AND ARE STILL UNPROBED.** Only the IR half has a confirmed shape.
- ⛔ **`social_account` IS STILL 0 OF 89** -- Bright Data, blocked on a rotation that is the account
  owner's act. Nothing in this pass touches it.
- **`sa_symbol` is unmoved at 10 INFERRED / 79 UNRESOLVED** -- it needs the SA fetch path, not search.
- **The identity layer as a whole now reads:** `bloomberg_ticker` 34 MEASURED + 49 INFERRED = 83 of
  89; `ir_domain` 79 INFERRED of 89; `sa_symbol` 10 of 89; `social_account` 0 of 89.

---

## 15. THE BLOG HALF IS BUILT, PROVEN AND THEN STOPPED BY A QUOTA WALL -- AND THE WALL IS AN OPEN CALL, NOT A DEFECT

**Artifact:** `deliverables/IDENTITY_BLOG_ROOTS_PASS_20260913_Z.json`, marked **PARTIAL** in its own
`state` field. `scripts/ir_domain_bulk_pass.py --mode blog` carries the rule.

### ⭐ THE BLOG RULE IS STRICTER THAN THE IR RULE, AND THAT IS THE WHOLE POINT

By the time this runs the company's registrable domain is already held. So **test (c) -- dead on the
IR pass, recorded there as a measured null -- becomes the PRIMARY AND ONLY test:**
>> **A BLOG ROOT IS ACCEPTED ONLY IF ITS REGISTRABLE DOMAIN EQUALS THE HELD `ir_domain`. Everything
   else is discarded, whatever its rank.** That is not a heuristic. It is an identity constraint, and
   it makes the wrong-company failure mode -- the one that forced this entire criterion --
   **STRUCTURALLY IMPOSSIBLE here rather than merely unlikely.** <<
⚠ **THE PRICE IS RECALL, AND IT IS REAL:** a company whose newsroom lives on a SEPARATE domain
(Alibaba's is `alizila.com`, not `alibabagroup.com`) is refused. **The denominator is 79, not 89** --
a name with no `ir_domain` cannot have a blog resolved at all, and the pass drops those 10 rather than
paying for them.

### ⛔ THE FIRST BATCH OF 7 WAS SPENT ON A DEFECT, FOUND BY READING THE OUTPUT INSTEAD OF THE COUNT

The header line said *"ACCEPTED 4 of 7"*. The values under it were `www.asml.com/en`,
`www.astrazeneca.com/content` and `www.airliquide.com/group`. **The root extractor took the FIRST path
segment, which on a localized site is the LOCALE, not the blog.** Every one is a real URL prefix, so
nothing errored and nothing looked wrong. Repaired to take the prefix **up to and including the marker
segment**, and the marker test now reads a hyphenated segment as the words it is made of --
`press-releases` and `media-centre` are unmistakably editorial and failed an exact match, while a bare
substring test would accept `newsagents`. **Fixture: 7 of 7 including two negative controls.**
⭐ **AND THE SECOND-ORDER FIX MATTERS MORE THAN THE FIRST:** the blog branch stored only its OUTPUT,
so the repair could not be replayed and the 7 calls were lost. **The IR pass stored its result domains
and its equivalent repair cost ZERO calls.** The branch now stores `on_domain_links`. *Store the
INPUT to a rule you may have to fix, not just the rule's answer.*

### THE WALL, MEASURED

```
HTTP 429 from customsearch/v1 -- the daily query cap
104 calls today: 1 probe + 90 IR + 7 discarded blog + 5 blog + 1 diagnostic
partition, eligible 79:  ASKED 5 | INFERRED 3 | REFUSED 2 | NOT ASKED 74
```
⛔ **A REFUSAL AND A NEVER-ASKED ARE DIFFERENT FACTS AND THE ARTIFACT PARTITIONS THEM.** Collapsing
them would report 74 companies as having no blog when nothing was ever asked about them -- the
`0 hits across 0 files scanned` trap, on a vendor quota instead of a corpus.
⭐ **THE QUOTA WAS NOT WASTED.** It went on the IR pass, which is the prerequisite the blog rule cannot
run without, and which is COMPLETE at 79 of 89. Spending it in that order was the right sequence and
would be again.

>> **THE OPEN CALL, AND IT IS ANDREW'S BECAUSE IT IS A VENDOR SPEND CAP:** the `google-cse-config` key
   behaves as the Custom Search **free tier, 100 queries/day**. The blog half needs either
   **tomorrow's reset** (free, costs a day) or **billing enabled on that GCP project** (immediate).
   **No seat raises a vendor spend cap.** Nothing else is asked, and nothing else waits on it --
   the IR half is done and the resume command is recorded in the artifact's `blocker.resume`, with an
   `--exclude-done` limb so no name is ever paid for twice. <<

---

## 16. BRIGHT DATA WAS NEVER A CREDENTIAL FAULT. THE CONFIGURED ENDPOINT IS RETIRED -- FIXED, MEASURED, AND THE ROTATION THIS SEAT'S OWN DECISION TREE SENT TO ANDREW WAS THE WRONG ASK

**Authority:** Andrew-direct 2026-09-14 ~02:49Z, verbatim: *"i don't see why we are required to rotate
the bright data key, that is not relevant at this stage they have a working key"*, plus his standing
*"read the api docs and figure it out"* (~04:12Z). **He was right and the measurement now says so.**

### ⛔ THE DEFECT IN THE DIAGNOSIS IS THIS SEAT'S, NOT THE SEAT THAT RAN IT

This seat measured HTTP 400 at the DIAL STAGE for two tools and correctly named **two** candidates:
*"the transport OR the token"*. It then **authored the decision tree** that `0.0.0_AB_MSTR~Z` executed:

    configured == stored  ->  THE STORED KEY ITSELF IS STALE. Rotation, the account owner's act.
    configured != stored  ->  the DEVICE CONFIG is out of sync; resync from the secret.

>> **THAT TREE HAS NO TRANSPORT BRANCH. Both of its arms are inside the TOKEN candidate**, so whatever
   it returned, the answer was going to be about the token. The hash match proved the config and the
   secret **AGREE**; it never touched **VALIDITY**, and agreement was silently read as guilt. **A
   two-candidate diagnosis was collapsed to one by an instrument that could only ever see one.** <<
⚠ `0.0.0_AB_MSTR~Z` has taken this as its own inference. **It is not. The tree is this seat's**, and a
seat that runs another's tree faithfully is not the author of its blind spot. The cost was real: a
rotation request reached Andrew, and rotating a working key would have broken the one thing that worked.
⭐ **THE TRANSFERABLE FORM:** *when you name N candidates, the discriminator must be able to return
"not this one" for each of them. A test whose every branch lives inside candidate 1 cannot exonerate
candidate 2 -- and it will still print a confident verdict.* Rule 22's DISCRIMINATION axis at the
level of the HYPOTHESIS SET rather than the reading.

### THE MEASUREMENT, one JSON-RPC `initialize` POST, same token, three paths

```
/sse       (the configured endpoint)   HTTP 404   <- retired
/mcp       (streamable HTTP)           HTTP 200   full initialize result, capabilities, session id
/nope-xyz  (NEGATIVE CONTROL)          HTTP 404   <- so 404 means "no such endpoint",
                                                     and /sse is in that class
```
>> **THE SAME TOKEN THAT 404s ON `/sse` RETURNS HTTP 200 ON `/mcp`. THE KEY IS FINE. THE CONFIGURED
   TRANSPORT IS A RETIRED ENDPOINT.** Bright Data moved from SSE to streamable HTTP and the device
   config still named the old one. Proven end-to-end, not just at the handshake: `tools/list`
   returned 5 tools and a real `search_engine` call returned a 3.8 KB payload. <<

### THE FIX, AND WHAT IT DOES NOT DO

`~/.claude.json`, node `/mcpServers/brightdata`: `type: "sse"` -> `"http"`, and `/sse?token=` ->
`/mcp?token=`. **`type: "http"` was already the convention in that same file** -- two other servers
use it. Backed up first (`.claude.json.bak-brightdata-transport-<stamp>`), both anchors verified
UNIQUE before any write, the result parsed as JSON before being written, and the other three servers
confirmed untouched. **A json round-trip was deliberately refused: it would reformat a 68 KB config
that seven live sessions share, to fix two fields.**
⚠ **AND IT DOES NOT REPAIR A RUNNING SESSION.** Measured, not assumed: the MCP tool in this session
still dials the old URL after the edit, because a client reads that config at session start. **Every
seat gets the working binding at its NEXT session start**; until then the working route is the direct
JSON-RPC POST to `/mcp`, which this seat has exercised.

### ⛔ BUT BRIGHT DATA CANNOT SUBSTITUTE FOR THE CSE ON THE BLOG HALF, AND THIS IS THE PART TO READ

The obvious next move -- *the CSE quota is gone, so run the blog pass on Bright Data instead* -- **does
not work, and the reason is not a quota or a permission.** `search_engine` returns Google's SERP with
the links as **REDIRECT STUBS**:
```
{"link":"/goto?url=CAESVQHrOzAVgLcEzlW3FxG2QxlW5W6kjgGTGOuRgZpPrTieUGAQ...",
 "title":"Boeing Newsroom", "description":"News & Stories | Sep 13, 2026 ..."}
```
**THERE IS NO HOST IN THAT LINK.** The blog rule's entire safety is `registrable(link) == held_domain`
-- an identity constraint. **A stub has no registrable domain, so the only test the blog rule has
cannot run at all.** The titles are present and tempting; matching on a title instead would throw away
the exact property that makes s.15's rule safe, and s.14 is a 89-name demonstration of what happens
when a name is trusted as a key.
⛔ **SO THE BLOG HALF STAYS ON THE GOOGLE CSE AND STAYS BLOCKED ON ITS QUOTA.** Recorded here
explicitly so the next seat does not spend the discovery again. Neither weakening the rule to
title-matching, nor resolving ~740 redirect stubs by scraping them, is a trade worth making.
⭐ **AND THIS IS A PROPERTY OF THE TOOL, NOT A FAULT:** Bright Data's value was never SERP link
extraction. It is `scrape_as_markdown`, which returns actual page content -- which is what
`social_account` and the four publication backfills need, and what neither is blocked on any more.

### WHAT IS NOW UNBLOCKED, AND WHAT THE BLOCKER ACTUALLY WAS

| item | was reported blocked on | true state |
|---|---|---|
| `social_account`, 0 of 89 | "Bright Data key rotation, account owner's act" | **NOT BLOCKED.** The key works; the transport was wrong and is fixed |
| the 4 publication backfills | the same | **NOT BLOCKED** by credentials |
| the blog half, 74 not-asked | Google CSE daily quota | **STILL BLOCKED**, and Bright Data cannot substitute (above) |
⚠ **NOTHING HERE WIDENS ANY GRANT.** Andrew's Bright Data word covers this work and his card 4 covers
the Google key; the two stay separate, as they have all night.

---

## 17. SEEKING ALPHA IS READABLE WITHOUT A LOGIN, WITHOUT A CAPTCHA AND WITHOUT A BROWSER -- BUT THE PER-TICKER ACCESS THE ANALYTICS HALF NEEDS IS STILL UNPROVEN. AND EVERY FAILURE SHAPE HERE RETURNS `isError=False`

**This corrects s.3's premise.** s.3 said *"SA IS THE TEMPLATE, AND BACKFILL THERE IS A PARAMETER
SWEEP"* -- of the authenticated browser session. With the Bright Data transport repaired, the content
comes back over `scrape_as_markdown` with **no sign-in, no captcha solve, no screenshot, no
press-and-hold**. Measured end to end:

```
https://seekingalpha.com/news          28,510 bytes   47 raw links -> 25 DISTINCT article URLs
https://seekingalpha.com/news/<slug>   14,038 bytes   title, tickers, and 'Sep 13, 2026'
```
⭐ **THE ARTICLE PAGE CARRIES ITS DATE, which is s.11's third acceptance requirement** (`published_at`
correct), and it arrives on the LOGGED-OUT view -- the page even renders *"Create Free Account"*.
**If this holds at scale, the entire authenticated-harvest apparatus is unnecessary for SA content.**

### ⛔ BUT THE HALF THE ANALYTICS ACTUALLY NEEDS IS NOT PROVEN, AND SAYING SO IS THE POINT

s.11's acceptance is **>=30 consecutive days PER TICKER**. What was proven is the **market-wide front
page**, one day deep.
- `https://seekingalpha.com/symbol/ASML/news` -- **the per-ticker page -- returned 12,791 bytes of
  PURE NAVIGATION CHROME**: zero dates, zero article links, every link a relative nav entry. It is
  client-rendered and the scraper gets the pre-hydration shell.
- **Pagination / date-ranged access is unattempted.** 25 articles of one day is not 30 days of one
  ticker.
>> **SO: SA CONTENT IS REACHABLE. SA CONTENT *FOR A GIVEN TICKER OVER A GIVEN WINDOW* IS NOT YET
   REACHABLE BY ANY ROUTE THIS SEAT HAS PROVEN.** That is the gap the next step closes, and it is a
   narrower and more useful statement than either "SA works" or "SA is blocked". <<

### ⛔⛔ THE INSTRUMENT TRAP, AND IT IS THE MOST TRANSFERABLE THING IN THIS SECTION

**FOUR DIFFERENT OUTCOMES WERE OBSERVED. ALL FOUR RETURNED `isError=False`.**

| what actually happened | `isError` | body | what it looks like |
|---|---|---|---|
| transient failure on a good URL | **false** | **0 bytes** | identical to a dead host |
| NEGATIVE CONTROL: nonexistent host | **false** | **0 bytes** | -- |
| client-rendered page, shell only | **false** | 12,791 | **a solid success** |
| a JSON VALIDATION ERROR from the vendor | **false** | 438 | content |
| genuine content | **false** | 14,038 | a solid success |

⛔ **THE SUCCESS FLAG IS CONSTANT ACROSS EVERY OUTCOME, SO IT CARRIES NO INFORMATION. AND SIZE IS NOT
A PROXY: 12,791 BYTES OF NAVBAR OUTRANKS 438 BYTES OF ERROR AND BOTH OUTRANK THE EMPTY ONE.**
⚠ **THIS SEAT WAS ONE SENTENCE FROM TWO OPPOSITE WRONG CONCLUSIONS IN FIVE MINUTES.** The very first
probe returned 0 bytes and would have been reported as *"Bright Data cannot unlock Seeking Alpha"* --
a false negative that would have kept the whole backfill on the fragile browser route. A re-run of the
IDENTICAL URL returned 12,791 bytes. Then that 12,791 would have been reported as *"SA scrapes fine"*
-- a false positive, because it was entirely chrome.
>> **THE ONLY SOUND ORACLE IS A CONTENT ASSERTION: does the payload contain the FIELDS THE WORK NEEDS**
   -- here, article links and a date. Zero of each on the per-ticker page; 25 links on the listing; a
   date on the article. **Assert on the field, never on the flag and never on the length**, and
   **retry once before recording an absence**, because a transient and a dead host are byte-identical.

### One defect of this seat's own, kept because it produced a fifth shape
The first article fetch failed on **URL validation**: the extracted link carried TWO `#` fragments
(`...#scroll_comments#source=...`), which is not a valid URI. **The vendor returned that refusal as
438 bytes of successful CONTENT**, not as an error. Fix: strip from the first `#`. It also collapsed
47 raw links to **25 distinct articles** -- so the same bug was inflating the link count by 88%.

---

## 18. THE SA BACKFILL NEEDS NO VENDOR AT ALL -- and the constraint is NOT the window, it is DENSITY and IDENTITY. A SYMBOL THAT RESOLVES IS NOT A SYMBOL THAT IS RIGHT

**This supersedes s.17's route and most of s.3.** `seekingalpha.com/api/v3/symbols/<SYM>/news` is
**directly fetchable from this device**: HTTP 200, **342,550 bytes of CLEAN JSON, 50 records, 50
`publishOn` timestamps**, no login, no captcha, no browser, **and no vendor egress at all.**

### THE VENDOR PATH WAS STRICTLY WORSE, WHICH IS THE PART TO CARRY FORWARD

The same endpoint through Bright Data's `scrape_as_markdown` came back **234,727 bytes** -- SMALLER
than the direct 342,550 -- and **STRUCTURALLY UNPARSEABLE.** The markdown transform did two things:
```
1. escaped markdown metacharacters INSIDE the JSON    "data":\[{...}]      (2,009 of them)
2. REWROTE MARKDOWN LINK SYNTAX INSIDE JSON STRINGS, injecting bare quotes:
   "content":"\n\nASML ([ASML]("https://see...          <- the quote ends the JSON string
```
Unescaping fixes (1). **Nothing fixes (2)** -- the payload is not recoverable as JSON, only as regex
scrapings. **A MARKDOWN CONVERTER IS A LOSSY, CORRUPTING TRANSFORM FOR A JSON ENDPOINT, AND THE
RESULT STILL LOOKS LIKE JSON.** 235 KB of visibly-correct data that `json.loads` cannot read.
>> **THE RULE: BEFORE BUILDING ON A VENDOR, TEST WHETHER THE DIRECT FETCH WORKS. Here the vendor was
   not merely unnecessary -- it DEGRADED the payload**, and the degradation was invisible until a
   parser was pointed at it. <<

### THE MEASUREMENT, over a jurisdiction-spanning sample, with its negative control

```
symbol  http recs oldest      newest        note
ASML    200   50  2026-05-13  2026-09-08    US-listed ADR
ADBE    200   50  2026-06-15  2026-09-13    US
BA      200   50  2026-07-24  2026-09-12    US
NFLX    200   50  2026-06-16  2026-09-13    US
NESN    404    0  -           -             SWISS ROOT -- SA DOES NOT KNOW IT
NSRGY   200   50  2024-03-26  2026-09-10    the US ADR for the same company
ROG     200   50  2023-04-27  2026-07-28    <- RESOLVES. WRONG COMPANY. See below.
RHHBY   200   50  2026-02-07  2026-09-09    the real Roche
PBR     200   50  2026-02-04  2026-09-10    Petrobras US ADR
8035    404    0  -           -             JP NUMERIC ROOT -- SA DOES NOT KNOW IT
TOELY   200   21  2017-07-27  2026-07-30    Tokyo Electron ADR -- 21 ARTICLES IN 9 YEARS
ZZQQXX  404    0  -           -             NEGATIVE CONTROL -- fires
```

### FINDING 1 -- A SYMBOL THAT RESOLVES IS NOT A SYMBOL THAT IS RIGHT. THIRD INSTANCE TONIGHT.

`ROG` returns HTTP 200 with 50 clean records spanning three years. **It is ROGERS CORPORATION, not
Roche.** Verified by reading its own titles: *"Rogers forecasts Q3 revenue of $233M-$243M"*,
*"Rogers Non-GAAP EPS of $0.92 misses"*. The real Roche is `RHHBY`, whose titles name Roche.
>> **A 200 WITH FIFTY WELL-FORMED RECORDS IS NOT EVIDENCE OF THE RIGHT COMPANY**, and this would have
   landed three years of another firm's earnings news under Roche in the harvest estate. It is the
   same failure as s.14's `mitsubishi-hc-capital.com` and `taiwansemi.com`, on the SYMBOL axis
   instead of the DOMAIN axis. **A name is not a unique key; neither is a ticker root.** <<
**THE ACCEPTANCE RULE THIS FORCES:** an `sa_symbol` is accepted only when the returned articles' own
text ties them to the subject company -- the same corroboration discipline s.14 landed, and it is
**free**, because the titles arrive in the payload already paid for.

### FINDING 2 -- THE BACKFILL IS GATED ON THE IDENTITY LAYER, EXACTLY AS s.7 SEQUENCED IT

**The Bloomberg root does NOT work for non-US names.** `NESN` 404s, `8035` 404s; only the **US ADR
ticker** resolves (`NSRGY`, `TOELY`). And `sa_symbol` stands at **10 INFERRED of 89**, all ten of them
US names where the root happens to be the symbol.
>> **SO ~79 OF 89 NAMES HAVE NO KNOWN SA SYMBOL, AND THE ROOT WE HOLD IS THE WRONG KEY FOR THEM.**
   s.7's ordering -- identity first, because a backfill against 10 of 89 is the more expensive mistake
   -- is now measured rather than argued. <<

### FINDING 3 -- THE WINDOW IS SATISFIED. THE DENSITY IS THE REAL CONSTRAINT.

s.11 sets three bars. Against them:
- **`published_at` correct: SATISFIED.** Full ISO-8601 with offset, e.g. `2026-09-08T12:22:49-04:00`.
- **>=30-day window: SATISFIED BY ONE CALL, for every symbol that resolved.** The oldest record is
  older than the 30-day cut in 9 of 9 cases; spans ran 51 to 3,291 days.
  **AND s.11's OWN WORDING IS AMBIGUOUS, WHICH IS THIS SEAT'S DEFECT TO NAME:** *">=30 consecutive
  days per ticker"* can mean *the window SPANS 30 consecutive days* (satisfied) or *there is an
  article on each of 30 consecutive days* (**not satisfied by anything** -- ASML has 50 articles
  across 119 days, i.e. news on ~25% of days). **The first is the reading `WINDOW_DAYS = 30` supports
  and the one this section measures against.** Stated rather than silently chosen.
- **>=3 mentions in the window: NOT SATISFIED FOR THIN NAMES.** `TOELY` has **21 articles in NINE
  YEARS** -- about two a year. No harvest fixes that; **the coverage does not exist.**
>> **SO THE BINDING CONSTRAINT IS NOT THE HARVEST AND NOT THE WINDOW. It is that a thinly-covered ADR
   generates too little to clear the density bar, and s.11's re-sequencing of s.7 BY TICKER-WINDOW
   COMPLETENESS should be re-sequenced by DENSITY instead.** <<

### WHAT THIS CHANGES, PLAINLY

| was believed | measured |
|---|---|
| SA backfill needs an authenticated browser session (s.3) | it needs an unauthenticated GET |
| Bright Data is the route once the credential is fixed (s.16) | Bright Data is **worse** here than no vendor |
| the blocker is vendor access | the blockers are **`sa_symbol` identity** and **article density** |

**NOT DONE AND NOT CLAIMED:** no data was landed anywhere. **No S3 write, no DynamoDB write, no
pipeline run** -- landing harvest data is DS/COO lane at L6/L7, not L1's, and this section is the
route and its measured limits, not the harvest itself.

---

## 19. `sa_symbol` RESOLVES 17 OF 17 ASKED -- AND ONLY 8 OF THEM CLEAR THE DENSITY BAR. s.18's PREDICTION HOLDS: DENSITY, NOT ACCESS, IS THE BINDING CONSTRAINT

**Artifacts:** `scripts/sa_symbol_resolve_pass.py` and
`deliverables/IDENTITY_SA_SYMBOL_DENSITY_PASS_20260913_Z.json`, marked **PARTIAL** in its own `state`.
Free, direct, unauthenticated, **no vendor** -- 121 calls, no quota consumed anywhere.

### THE RULE, AND WHY IT RESOLVES IDENTITY AND DENSITY IN ONE SWEEP

The news call that corroborates a symbol is the same call that measures its density, so both come
from one read. A symbol is accepted only when **(a)** SA's own company name for it matches ours AND
**(b)** a returned article **title** names the company. Rank and relevance score are recorded and
**never decide** -- s.18's `ROG` is Rogers Corporation with 50 immaculate records.

### THE PARTITION, WHICH IS THE FIRST THING TO READ

```
universe                                  89
ASKED                                     17
NOT ASKED -- HTTP 403 from the vendor     72   <- NOT a finding about those names
RESOLVED of asked                         17
REFUSED ON EVIDENCE of asked               0
CLEARING THE DENSITY BAR                   8 of 17
```
⛔ **THE SEARCH ENDPOINT SERVED 17 QUERIES AND THEN RETURNED HTTP 403 FOR EVERY REMAINING NAME.** The
first run of this pass printed *"RESOLVED 17 of 89 / REFUSED 72 of 89"* -- **which reads as "Costco,
Netflix, Visa and Mastercard have no SA symbol".** They were never asked. The artifact now partitions
the two and every not-asked record says so in its own evidence field.
⚠ **AND THE GUARD THAT WOULD HAVE CAUGHT IT EXISTED -- IN THE OTHER SCRIPT.** `ir_domain_bulk_pass.py`
stops after 3 consecutive vendor failures. This pass was written later, without it, and spent **72
pointless calls recording absences it never asked about.** *A control does not travel between scripts
on its own; it has to be carried.* Added here now.
⭐ **The per-symbol NEWS endpoint was NOT rate-limited** -- only the name-to-symbol SEARCH was. **A
name whose symbol is already known can still be harvested**, so the 403 does not block the backfill,
only the resolution of the remaining 72.

### ⛔ TWO DEFECTS THE FIRST BATCH CAUGHT, BOTH MINE, AND ONE SHIPPED A WRONG COMPANY

**1. SA marks the matched substring with `<b>` IN EVERY FIELD, INCLUDING `name`.** A search for "ASML"
returned the symbol as `<b>ASML</b>`, so the news URL became `/symbols/%3Cb%3EASML%3C/b%3E/news` and
404'd. **It produced FALSE REFUSALS on precisely the EASIEST names** -- the ones where the query
matched the ticker itself. ASML and BNP Paribas both read UNRESOLVED for this reason alone.

**2. THE ACCEPTANCE RULE ACCEPTED A WRONG COMPANY, AND THE REASON IS THE ONE THIS PLAN KEEPS
RE-LEARNING.** `America Movil` was matched to **`LILA` -- Liberty Latin America Ltd.** -- on the token
`america`, and **48 of 50 returned titles "confirmed" it**, because test (b) uses THE SAME TOKENS as
test (a).
>> **TWO TESTS THAT SHARE A DEPENDENCY ARE ONE TEST.** s.14's criterion worked because its two tests
   were INDEPENDENT (a name token vs. multi-result domain agreement). Here both read one weak
   geographic word, so they failed together and the second one's agreement was worthless
   corroboration. **This is Rule 22's shared-dependency blindness, inside the acceptance rule, one
   section after this plan wrote about it.** <<
⚠ **AND THE CORRECT ANSWER WAS REJECTED FOR HAVING ACCENTS:** SA names it *"América Móvil, S.A.B. de
C.V."*, which the ASCII strip turned into `amricamvil`, matching none of our tokens. **The right
answer failed and the wrong one passed, in the same comparison.**
✅ **THE FIX IS NOT A LONGER STOPWORD LIST WRITTEN FROM RECALL** -- that is the Rule 24 trap. It is a
**SYMMETRIC measure derived from the two names themselves**: jaccard(our distinctive words, SA's
distinctive words) >= 0.5, plus accent folding and a containment escape for concatenated forms.
```
America Movil vs Liberty Latin America Ltd.        j = 0.25  REFUSED
America Movil vs America Movil, S.A.B. de C.V.     j = 1.0   ACCEPTED
Roche         vs Rogers Corporation                j = 0.0   REFUSED
Air Liquide   vs L'Air Liquide S.A.                j = 1.0   ACCEPTED
```
**Fixture: 9 of 9, including both failures that had shipped.**

### THE DENSITY MEASUREMENT -- and it is the reason this section matters

```
folder                         symbol  recs  in-30d  oldest       s.11 density bar
Adobe                          ADBE    50    26      2026-06-15   MET
Alibaba                        BABA    50    35      2026-07-20   MET
AstraZeneca                    AZN     50    12      2026-04-29   MET
Boeing                         BA      50    24      2026-07-24   MET
BP                             BP      50     5      2026-05-13   MET
Cadence                        CDNS    50     5      2025-09-06   MET
Celsius                        CELH    50     4      2025-06-04   MET
Clorox                         CLX     50     4      2025-05-04   MET
--------------------------------------------------------------------------------
ASML                           ASML    50     2      2026-05-13   NOT MET
British American Tobacco       BTI     50     2      2025-02-13   NOT MET
Air Liquide                    AIQUF   50     1      2020-09-02   NOT MET
America Movil                  AMX     50     1      2020-07-14   NOT MET
BNP Paribas                    BNPQF   50     1      2022-10-01   NOT MET
Canadian National Railway      CNI     50     1      2024-10-23   NOT MET
BB Seguridade                  BBSEY   17     1      2022-02-07   NOT MET
Bunzl                          BZLFF   18     1      2018-08-28   NOT MET
China Construction Bank        CICHY   25     0      2011-01-05   NOT MET
```
>> **THE 30-DAY WINDOW IS COVERED IN ALL SEVENTEEN -- every `oldest` predates the cut. THE WINDOW WAS
   NEVER THE PROBLEM. NINE OF SEVENTEEN SIMPLY DO NOT GENERATE THREE ARTICLES IN THIRTY DAYS.** <<
⭐ **AND THE MISSES CLUSTER, WHICH MAKES THIS ACTIONABLE RATHER THAN JUST DISAPPOINTING:** they are
overwhelmingly the **foreign-ordinary / unsponsored tickers** -- `AIQUF`, `BNPQF`, `BZLFF`, `BBSEY`,
`CICHY`. Those lines carry a trickle of coverage while the same company's **sponsored ADR** is where
the articles land.
⛔ **SO THIS PASS HAS A SELECTION DEFECT OF ITS OWN, NAMED RATHER THAN HIDDEN:** where several tickers
are the same company, it picks the one with the most **TOTAL** records. **It should pick the one with
the most records IN THE WINDOW**, which is the quantity the bar is actually about. Not re-run because
the search endpoint is currently 403; the fix is one comparison key and the resume command is in the
artifact.

### WHAT THIS SETTLES, AND THE ONE NUMBER NOT TO QUOTE YET

- **`sa_symbol` is resolvable for free and the Bloomberg root is not the key** -- SA's own search maps
  company NAME to symbol, and the rule corroborates on SA's company name plus its article titles.
- **The binding constraint is DENSITY**, exactly as s.18 predicted, and it is now measured: **8 of 17.**
- ⚠ **DO NOT EXTRAPOLATE 8/17 TO THE 89.** The 17 asked are alphabetically the first 17, not a sample
  drawn to represent the universe, and they skew toward names whose folder happens to sort early. The
  honest statement is *8 of the 17 measured*, and the remaining 72 need the 403 to lift.
- ⚠ **"REFUSED ON EVIDENCE: 0 of 17" IS NOT A CLEAN BILL FOR THE RULE.** The rule discriminates at the
  CANDIDATE level -- it rejected Liberty Latin America, Rogers, Sony and Xanadu Quantum by name -- but
  a 0% name-level refusal over 17 large caps means the rule has not yet been tested where it will
  actually bite: a name with NO SA listing at all.
---

## 20. `social_account` HAS A PROVEN ROUTE AND IT IS THE COMPANY'S OWN SITE, NOT SERP -- shape confirmed on 2 calls, and the bulk pass is DELIBERATELY NOT RUN

**Authority:** Andrew's Bright Data grant, unchanged. Shape proved on **two calls plus a negative
control**, per his prove-the-shape-first rule. **The bulk pass has NOT begun.**

### WHY NOT SERP, WHICH IS THE ROUTE THAT WOULD HAVE BEEN TRIED FIRST

s.16 measured that Bright Data's `search_engine` returns Google **redirect stubs with no host**. **A
social handle IS a URL**, so a stub carries none of the information the key needs. The blog half died
on exactly this; recording it here stops the same discovery being paid for a third time.

### THE ROUTE: READ THE COMPANY'S OWN SITE, USING THE `ir_domain` WE ALREADY HOLD

```
astrazeneca.com   body 13,056   5 platforms:  x/AstraZeneca  linkedin/company/astrazeneca
                                              facebook/AstraZeneca  instagram/astrazeneca
                                              youtube/user/astrazeneca
adobe.com         body  8,213   0 platforms  <- root page carries none
NEG CONTROL       body      0   0 platforms  <- fires
```
⭐ **AND THIS IS STRONGER EVIDENCE THAN ANY SEARCH RESULT COULD BE.** A handle linked FROM the
company's own domain is **published by the company about itself** -- the same domain-equality identity
constraint the blog rule uses, and immune to the wrong-company failure that has now bitten this plan
three times (s.14 domains, s.18 `ROG`, s.19 `LILA`).
⭐ **AND IT ADMITS A GENUINELY INDEPENDENT SECOND TEST, which is the lesson s.19 paid for:** signal one
is *the link was found on the company's own domain*; signal two is *the handle text carries the
company's name* (`x/AstraZeneca`). **Those two do not share a dependency** -- unlike s.19's pair, which
both read the same token set and failed together.

### ⛔ WHY THE BULK PASS IS NOT RUN TONIGHT, STATED AS A REASON AND NOT AS A HEDGE

**Adobe returned ZERO.** Its root page does not carry the links in the fetched markdown -- a
client-rendered footer, most likely. **So the rule as probed covers one of two, and a 79-call bulk
pass would bank that miss rate into an artifact.** The fix is a fallback page order (`/about`,
`/contact`, a social hub) and that is a DESIGN choice with a call-count multiplier attached -- 79 calls
becomes 160 to 240.
>> **PROVING A SHAPE ON THE EASY CASE AND THEN SPENDING THE BATCH IS THE MISTAKE THIS PLAN MADE IN
   s.17**, where 12,791 bytes of navigation chrome read as a working route. **Two of two would have
   justified the batch; one of two justifies designing the fallback first.** <<

### STATE OF THE FOUR IDENTITY KEYS

| key | state | what it is waiting on |
|---|---|---|
| `bloomberg_ticker` | 34 MEASURED + 49 INFERRED = **83 of 89** | nothing |
| `ir_domain` | **79 INFERRED of 89** | 10 refused; 3 of those need one human line |
| `sa_symbol` | **17 of 17 ASKED resolved**, 72 never asked | the SA search **HTTP 403** to lift |
| `social_account` | **0 of 89**, route PROVEN | a fallback-page rule, then one bulk pass |

⛔ **NOTHING IN THIS SECTION LANDED DATA.** No S3, no DynamoDB, no pipeline, no applied state, no
terraform. **The portal freeze is untouched.** Content fetched from the web was treated as DATA and no
instruction inside it was acted on.

---

## 21. `ir_domain` CLOSES AT 88 OF 89 AT ZERO CALL COST -- because test (c) was never running, and I had recorded that as a measured NULL

**No vendor call. No quota. Nine refusals closed from evidence already on disk.**

### ⛔ I MIS-READ MY OWN CRITERION'S THIRD TEST

s.14 reported: *"Test (c) CONTRIBUTED NOTHING AND THAT IS RECORDED AS A NULL, NOT A SKIP. No company
held a prior `ir_domain` from another key -- the layer was 0 of 89 -- so the branch was live and
inert."*
>> **THAT IS THE WRONG READING OF MY OWN TEST.** (c) says *"the domain matches a value already held
   for that company FROM ANOTHER KEY"* -- and I read "another key" as *another `ir_domain`*, which is
   not another key at all, it is the same key. **`bloomberg_ticker` IS another key, it was 83 of 89
   populated at the time, and it was never wired in.** <<
⭐ **THE REFUSALS WERE NEVER WRONG. The criterion simply had a test it was not running**, and I
recorded its silence as a measured null instead of asking what it was supposed to read.

### WHY THE BLOOMBERG ROOT IS EXACTLY THE RIGHT TIEBREAK, AND IT IS THE INVERSE OF TONIGHT'S LESSON

Every one of the ten refusals was a collision between two companies **sharing a NAME**. s.14, s.18 and
s.19 each landed the same finding from a different direction: **a company name is not a unique key**
(`mitsubishi-hc-capital.com`, `ROG`=Rogers, `LILA`=Liberty Latin America).
>> **BUT A BLOOMBERG ROOT *IS* A UNIQUE KEY, AND IT WAS IN THE FOLDER NAME THE WHOLE TIME.** Two firms
   can share "Hermes"; they cannot share `RMS FP`. <<

```
folder                         root     test (a) elected              excluded because        -> accepted
BP PLC                         BP       akerbp.com (Aker BP)          AKRBP NO != BP             bp.com
Hermes RMS                     RMS      federatedhermes.com (FHI US)  FHI US != RMS FP           hermes.com
Telefonica Brazil VIVT3 BZ     VIVT3    telefonica.com (TEF SM)       TEF SM != VIVT3 BZ         telefonica.com.br
Mitsubishi UFJ FG 8306 JP      8306     mitsubishi-hc-capital.com     8593 JP != 8306 JP         mufg.jp
Sumitomo Mitsui FG 8316 JP     8316     sumitomocorp.com              8053 JP != 8316 JP         smfg.co.jp
Taiwan Semiconductor TSM US    TSM      taiwansemi.com                a separate smaller firm    tsmc.com
Walmart de Mexico WALMEX MM    WALMEX   walmart.com (WMT US)          WMT US != WALMEX MM        walmex.mx
Singapore Telecom ST SP        ST       tpgtelecom.com.au (TPG AU)    TPG AU != ST SP            singtel.com
BNP Paribas BNP FP             BNP      bnpparibas-am.com             a SUBSIDIARY of BNP FP     invest.bnpparibas
```
⚠ **THIS IS NOT A WEAKENING OF THE CRITERION AND THE DIRECTION MATTERS.** Test (a)'s candidate is
**excluded ON EVIDENCE** -- a ticker that does not match -- not demoted on preference. Where test (a)
and test (b) disagreed, a third independent signal now adjudicates instead of both being discarded.
⚠ **AND BNP IS A DIFFERENT SHAPE FROM THE OTHER EIGHT, SAID RATHER THAN BLURRED:** its rival candidate
is a SUBSIDIARY of the same group, not a different company. The root picks the listed parent's own
investor site; it is the weakest of the nine and is marked as such here.

### THE ONE THAT STAYS REFUSED, AND WHY THAT IS THE HONEST ANSWER

**`International Container Terminals`** -- its folder carries **NO Bloomberg-shaped token at all**, so
test (c) has nothing to run on. `ictsi.com` is very likely correct (test (b), 2 results) but it would
be closed on a *different and weaker* basis than the other nine. **One refusal that is genuinely a
refusal is worth more than a clean 89 of 89.**

### THE LAYER NOW

| key | at session start | now |
|---|---|---|
| `bloomberg_ticker` | 34 MEASURED | **83 of 89** |
| `ir_domain` | **0 of 89** | **88 of 89** |
| `sa_symbol` | 10 INFERRED | 17 of 17 asked; the rest gated on a moving rate limit |
| `social_account` | 0 of 89 | 0, route proven, bulk pass gated on a fallback-page rule |

⚠ **ALL 88 ARE `INFERRED`, NOT `MEASURED`, AND NOTHING HERE CHANGES THAT.** No page was fetched to
confirm any company operates any domain; card 4 is search-only. Every value stays rejectable on its
status field.
⛔ **AND A RATE LIMIT THAT MOVES BETWEEN ENDPOINTS WAS MEASURED TONIGHT:** at 05:33Z the SA *search*
limit had LIFTED (HTTP 200) while the *news* limit had ENGAGED (HTTP 403) -- **the block migrated
between two endpoints of one host.** `sa_symbol_resolve_pass.py` now records a news-side refusal as
**NOT ASKED**, not as REFUSED-ON-EVIDENCE. The search side already had that guard and the news side
did not. **That is the third time in one session a control failed to travel to the sibling surface it
obviously applies to** -- the first was `ir_domain_bulk_pass.py`'s consecutive-failure stop, missing
from the pass written after it.

---

## 22. `social_account` LANDS AT 61 OF 88 AND 263 HANDLES -- the last 0-of-89 key is open, and the 27 misses are a DIAGNOSED instrument limit, not an absence

**Artifacts:** `scripts/social_account_pass.py`,
`deliverables/IDENTITY_SOCIAL_ACCOUNT_PASS_20260914_Z.json`. 115 Bright Data calls across two runs.
Read-only. **No data landed anywhere.**

```
universe                                89
with a held ir_domain                   88    <- the only names this method can read at all
RESOLVED                                61
  handles captured                     263
  facebook 52 | youtube 51 | linkedin 49 | instagram 46 | x 42 | tiktok 11 | weibo 1
no links, page arrived                  20    <- client-rendered footer
no payload, stable across two runs       7
```

### THE EVIDENCE MODEL, stated as what it is rather than dressed as two tests

**PRIMARY is STRUCTURAL:** the handle was linked **from the company's own domain** -- the `ir_domain`
already resolved for it. That is the collection method, true by construction, **and it is not claimed
as a discriminating test.** It is nonetheless the strongest identity tie available here, and immune to
the wrong-company failure that bit this plan three times tonight, because the company published it
about itself.
**The name check is a RECORDED FLAG, NEVER A GATE** -- and s.22's most useful result is why.

### ⭐ THE FLAG VINDICATED ITSELF BY BEING A FLAG. SEVEN RECORDS, FIVE OF THEM CORRECT.

Seven resolved records carried **no** handle containing a company token. Inspected rather than
counted:
```
BB Seguridade   BBSeguros, bb-seguros     CORRECT -- Banco do Brasil's insurance brand
Grupo Aero.     omaeropuertos             CORRECT -- the company IS OMA Aeropuertos
Manila          meralco, meralcoph        CORRECT -- Manila Electric IS Meralco
Schlumberger    slbglobal, WeAreSLBGlobal CORRECT -- the company rebranded to SLB
Haliburton      halliburton               CORRECT -- THE FOLDER misspells it with one 'l'
Celsius         2471716                   JUNK -- a bare platform ID
Telefonica BZ   playlist                  JUNK -- a YouTube /playlist URL
```
>> **HAD THE NAME CHECK BEEN A GATE, IT WOULD HAVE DISCARDED FIVE CORRECT ANSWERS TO CATCH TWO JUNK
   ONES.** A brand name is not the legal name; `Haliburton` failed only because OUR source has the
   typo. **A flag that is not a gate only pays if someone looks inside it, and this is what looking
   bought.** The two junk shapes are now filtered at the extractor. <<

### ⛔ THE RETRY RECOVERED ZERO, AND THE HYPOTHESIS IT TESTED WAS WRONG

Six major companies came back empty on the first run, and *retry once before recording an absence* is
banked estate discipline, so the guard went in. **Re-running all 27 recovered NONE.** The empty set is
**STABLE AND REPRODUCIBLE**, not transient.
⭐ **THE GUARD WAS STILL RIGHT TO ADD** -- it is what turned "probably a flake" into a trustworthy
negative. **A control that disproves your hypothesis has done its job, not failed at it.**

### ⛔ AND THE 20 "NO LINKS" LOOKED LIKE MY BUG. I TESTED THAT INSTEAD OF ASSUMING EITHER WAY.

Nike returned **33,141 bytes** and Boeing **25,332** with zero social links. Both companies plainly
run social accounts, so the obvious reading was an extractor defect.
```
searched both bodies for: twitter | x.com | instagram | facebook | youtube | linkedin
result: NOT ONE OF THOSE WORDS APPEARS ANYWHERE IN EITHER BODY, IN ANY FORM
```
>> **SO THE EXTRACTOR IS NOT AT FAULT AND THE PAGES DO NOT CARRY THE LINKS AT ALL.** Modern corporate
   footers are client-rendered and `scrape_as_markdown` returns pre-hydration content. First seen on
   Adobe in s.20, now confirmed on two more and stated as a **property of the tool**, not a mystery. <<
⚠ **NONE OF THE 27 IS EVIDENCE THAT A COMPANY PUBLISHES NO SOCIAL ACCOUNTS.** Every record says so in
its own field. Closing that gap needs a **rendered-DOM fetch**, which is a different capability from
the one in hand -- not more calls of the same kind.

### THE FOUR IDENTITY KEYS AT THE END OF THIS SESSION

| key | at session start | now |
|---|---|---|
| `bloomberg_ticker` | 34 MEASURED | **83 of 89** |
| `ir_domain` | **0 of 89** | **88 of 89** |
| `sa_symbol` | 10 INFERRED | 17 answered; 72 behind a burst-sensitive limiter |
| `social_account` | **0 of 89** | **61 of 88, 263 handles** |

⚠ **EVERY VALUE IN ALL FOUR IS `INFERRED`, NOT `MEASURED`.** No page was fetched to confirm a domain
is operated by its company; no social account page was visited; no ticker was confirmed against a
security master. **The layer gained rejectable values, not confirmed ones**, and every consumer can
still refuse on the status field -- which is the whole point of the rule.

---

## 23. THE SA LIMITER IS NOT BURST-SENSITIVE, IT IS ESCALATING -- AND RETRYING MADE IT WORSE. STOPPING IS THE CORRECT ACT

**A short section because the finding is operational and the right response is to stop.**

### THE OBSERVATIONS, IN ORDER, AT THREE TIMES

```
05:50Z   a 2-call manual probe          BOTH 200   -- search AND news open
05:55Z   resume at 0.25s spacing        403 after 4 names (6 calls)
06:08Z   resume at 8s spacing           403 on the FIRST name
```
⛔ **I READ THE 05:55Z FAILURE AS BURST SENSITIVITY AND SLOWED DOWN THIRTY-TWO-FOLD. IT DID NOT HELP
AND THE BLOCK GOT HARDER** -- from failing at call 6 to failing at call 1.
>> **SO THE MODEL IS NOT "TOO FAST"; IT IS A SUSTAINED, ESCALATING BLOCK WITH A COOLDOWN LONGER THAN
   THE ~13 MINUTES BETWEEN ATTEMPTS -- AND EACH ATTEMPT PLAUSIBLY EXTENDS IT.** <<
⭐ **THE CORRECT ACT IS THEREFORE TO STOP, NOT TO PACE.** This is the narrow case where the estate's
*"never wait, fire the ad-hoc"* rule does not apply: **the ad-hoc IS the thing degrading the
resource.** Naming that is the exception the rule asks for.
⚠ **AND IT CORRECTS s.19's WORDING**, which called this "a moving rate limit" as though it were
weather. It is a response to *this device's own request pattern*, and the pattern is mine.

### WHAT THIS DOES AND DOES NOT COST

- ⛔ **It costs the remaining 72 `sa_symbol` resolutions.** They stay NOT ASKED -- never REFUSED -- and
  every record says so in its own evidence field.
- ✅ **It costs the backfill NOTHING that is not already lost.** s.19 measured the binding constraint
  as **DENSITY, not identity**: only 8 of 17 resolved names clear `>=3` mentions in 30 days. **A name
  whose symbol we cannot resolve today is not the reason the backfill is not running.**
- ✅ **And the per-symbol NEWS endpoint is a different surface.** Any name whose symbol is ALREADY
  known stays harvestable; this block is on name-to-symbol SEARCH.

### THE GUARDS EARNED THEIR KEEP HERE, WHICH IS THE ONE CHEERFUL PART

Both runs cost **6 calls each** instead of 216. The consecutive-refusal stop fired at 3, the
`--exclude-done` limb meant no already-answered name was re-spent, and the NOT-ASKED partition kept
72 names out of the REFUSED column.
⭐ **AND THE TALLY FIX IS VISIBLE IN THE OUTPUT:** the second run printed `REFUSED 0 of 18` where the
first printed `REFUSED 1 of 18` for the identical data -- the print had been using a different formula
from the JSON and was booking a NOT-ASKED as a REFUSAL. **One formula now, and the corrected line is
the one a reader sees.**
