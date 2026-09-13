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
