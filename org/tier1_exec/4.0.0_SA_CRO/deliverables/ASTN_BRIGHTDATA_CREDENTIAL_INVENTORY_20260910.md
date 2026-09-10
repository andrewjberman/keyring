# ASTN / Bright Data -- what WSJ+FT actually used, and how many credentials this estate holds

**Author:** `4.0.0_SA_CRO~Z` | **Date:** 2026-09-10
**Question (Andrew, verbatim):** *"check out the ASTN macro key and the associated project and
resources, i want you to see what we were doing to get WSJ and FT info, were we using Bright Data
for that? I can update API key if so. Also, probably would make sense to keep using Bright Data for
SA as well with our residential proxy for all of the above."*

---

## THE SHORT ANSWER

**Yes, Bright Data -- for both, by two different mechanisms. And you almost certainly do NOT need to
update any API key, because a LIVE Bright Data account already exists with every zone required.**

## 1. WHAT ASTN IS

`ASTN` = the CEO-facing macro (tools for Austin). `ASTN_WSJFT` = a daily 3am-ET job pulling the top
~15-20 WSJ + FT stories, AI-summarising each into **verbatim-gated** cited bullets, emailed to
Austin via SES. PRD: `docs/architecture/ASTN_WSJFT_PRD.md` (85 lines, author `1.0.0_SA_CTO`).

## 2. THE TWO FETCH MECHANISMS -- both proven live 2026-06-24, per the PRD s2

- **WSJ = Bright Data Web Unlocker (`one_shotter`). Cookieless, no login** -- the Unlocker defeats
  the bot-wall on its own. ~7K chars of real article body per test.
- **FT = OUR OWN Playwright/Chromium + injected parked `FTSession` cookies, egressing through a
  Bright Data US sticky-session RESIDENTIAL PROXY.** Not the Unlocker, not the Scraping Browser.

**THE ELIMINATED PATHS ARE THE VALUABLE PART OF THAT R&D, and they transfer directly to any
authenticated source (SA included):**

| Path tried | Result |
|---|---|
| Bright Data Web Unlocker with custom cookies | **IGNORES them** -- uses its own managed session -> FT paywall. Cannot ride our auth. |
| Bright Data Scraping Browser | passes Cloudflare but **SANDBOXES cookie injection (0 of 49 attempts** via `Storage.setCookies` and `Network.setCookie`) -> cannot ride our auth. |
| Local headless browser | Cloudflare `403 "Just a moment..."` -- headless fingerprint flagged. |
| **our browser + residential IP + stealth fingerprint** | **WORKS.** Full cookie control, passes Cloudflare, not headless-detected. |

> **=> A COOKIELESS UNLOCKER CANNOT READ AUTHENTICATED CONTENT. This is measured, not theoretical,
> and it is the single most transferable fact in this record.**

## 3a. CORRECTION 2026-09-10, SAME DAY -- s3 BELOW UNDERCOUNTED. THERE ARE SIX.

> ⛔ **s3's "THREE DISTINCT SECRETS" IS WRONG AND IS LEFT STANDING BELOW SO THE ERROR IS LEGIBLE.**
> **How it happened:** s3 probed **three secret names I guessed at** from reading code, and reported
> the result as an inventory. **I never enumerated the secret list.** A check scoped to the members
> I already knew about could not see the members I did not -- and the enumeration changes the
> recommendation.
>
> **TRUE DENOMINATOR: 87 secrets in us-east-1; 6 are Bright Data.** (Counting trap hit and
> corrected en route, Rule 22a: `list-secrets --query 'length(SecretList)'` auto-paginated and
> returned PER-PAGE counts -- `10 10 10 10 10 10 10 10 7` -- so the count was re-derived client-side
> after draining `NextToken`.)

| Secret | Value fp | State |
|---|---|---|
| `brightdata-api-key` | `c4..0a` | **ALIVE** (200) |
| `find-insure/bright-data/api-key` | `c4..0a` -- **SAME VALUE** | **ALIVE** (200) |
| **`seeking-alpha/bright-data-api-key`** | `c5..18` -- distinct | **DEAD** (401) |
| `opal/external-apis` -> `bright_data_api_key` | `23..ad` -- distinct | **DEAD** (401) |
| `astn/brightdata/residential-proxy` | proxy user/pass | not API-testable (s3 correction) |
| `find-dualbiz/bright-data/serp` | `{api_key_secret, endpoint, zone}` | untested |
| `find-insure/bright-data/scraping-browser-creds` | `{wss_url}` | connection string |

## 3b. ANDREW-DIRECT 2026-09-10 -- THE ARCHITECTURE RULING THAT SETTLES THIS

> **VERBATIM:** *"there are only 3 types of Bright Data API, the one_shotter, the
> scraping_browser1, and the serp_opal. we do not need to make more that are target-specific, these
> are the three archetypes."*

**READ: ONE ACCOUNT CREDENTIAL, THREE ZONES BY PURPOSE. Target-specific Bright Data resources are
not to be minted.** The three archetypes are the whole API surface:

| Zone | Type | Use |
|---|---|---|
| `one_shotter` | unblocker | cookieless fetch of a bot-walled public page (WSJ; SA public pages) |
| `scraping_browser1` | browser_api | remote browser where a page needs real rendering |
| `serp_opal` | serp | search-engine results (the IR-page scan; the last-week web search) |

⚠ **`residential_proxy1` is NOT a fourth archetype and is NOT retired by this ruling.** It is a
PROXY, not an API you call -- our own browser egresses through it (the proven ASTN FT path, s2).
The ruling is about API types; do not read it as removing the proxy.

**THIS INVERTS THE s5(a)/(b) RECOMMENDATION AND THE CORRECTION IMMEDIATELY BELOW.** This seat
argued for issuing a SECOND key so SA and ASTN could rotate independently. **That is precisely the
target-specific proliferation the ruling forbids**, and the measured evidence backs the ruling
rather than the recommendation: **both target-specific keys are DEAD** (`seeking-alpha/...` and
`opal/external-apis`) while the **account-level key is ALIVE**, and `find-insure`'s only survives
because it is a COPY of the account key. A credential one pipeline uses is a credential nobody owns.

**THE REMEDY IS CONSOLIDATION, NOT ROTATION:**
1. Every consumer reads the ONE account credential (`brightdata-api-key`) and selects a ZONE.
2. `seeking-alpha/bright-data-api-key`, `opal/external-apis` -> `bright_data_api_key`, and
   `find-insure/bright-data/api-key` are **retired or become pointers** -- not re-keyed.
3. **Zone selection moves into the CALLER**, which is where it belongs: the SA scrapers already
   name `'zone': 'one_shotter'` inline, so the shape is already half-built.
4. **Nothing needs minting in the portal, so option (b) is withdrawn** and the reason for driving
   the portal at all has largely evaporated.

⚠ **TWO ZONES WERE AUTO-CREATED THIS SESSION AND THAT WAS MY DOING.** Registering the Bright Data
MCP server auto-provisioned `mcp_unlocker` and `mcp_browser` on the account (four zones before, six
after). They are the MCP's own managed zones, not archetypes, and I did not anticipate them --
recorded because under this ruling an unplanned zone appearing is exactly the thing to notice, and
whether they should persist is Andrew's call.

**SUPERSEDED BELOW:**

1. ~~**A DEDICATED SA KEY ALREADY EXISTS** -- `seeking-alpha/bright-data-api-key`, so the remedy is
   a rotation into an existing secret.~~ **WITHDRAWN by 3b:** that secret should not exist. The
   fact it already exists is the defect, not the solution.
2. **SA HAS TWO STALE KEYS IN TWO PLACES, AND THE LAMBDA READS THE WRONG ONE OF THE TWO.** It reads
   `opal/external-apis` -> `bright_data_api_key` (`23..ad`, dead) while a purpose-named
   `seeking-alpha/bright-data-api-key` (`c5..18`, also dead) sits beside it. **That is the actual
   mess** -- not one lapsed credential but a split identity where neither half works.
3. **THE COUPLING I WARNED ABOUT IN s5(a) ALREADY EXISTS.** `find-insure/bright-data/api-key` holds
   the SAME value as `brightdata-api-key`. ASTN and find-insure already share one credential, so a
   rotation of the live key breaks find-insure too. **Nobody is tracking that.**

**ZONE LIST GREW DURING THIS SESSION.** At the s4 reading the account carried four zones; after the
Bright Data MCP server was registered it carries six -- `mcp_unlocker` and `mcp_browser` were
**auto-provisioned by the MCP registration itself**. Recorded because a zone list is now a moving
object and any future reading of s4 must carry its own timestamp.

## 3. THE CREDENTIAL INVENTORY -- THREE DISTINCT SECRETS, NOT ONE  [SUPERSEDED BY 3a -- UNDERCOUNT]

Fingerprints differ, so these are genuinely different credentials -- **"update the API key" is not
one act.**

| Secret | Holds | Used by | State |
|---|---|---|---|
| `opal/external-apis` -> `bright_data_api_key` (len 36, `23..ad`) | API token | **SA scrapers** | **DEAD -- 401** |
| `brightdata-api-key` (len 36, `c4..0a`) | API token | **ASTN WSJ Unlocker** | **ALIVE -- HTTP 200** |
| `astn/brightdata/residential-proxy` | `{host, port, username, password, country=us}` | **ASTN FT proxy** | **UNTESTED -- see the correction below** |

> **CORRECTION, MY OWN INSTRUMENT ERROR, STATED RATHER THAN QUIETLY DROPPED:** my first probe sent
> the residential-proxy **password** as a Bearer token to the Bright Data API and reported `DEAD` on
> the 401 it got back. **That test is invalid** -- a proxy username/password is not an API token, and
> a 401 from that endpoint says nothing about whether the proxy works. Its true state is UNTESTED;
> testing it needs an actual proxied request. The evidence that it is probably fine is
> circumstantial but real: its username fingerprint ends `..y1` and the live account carries a zone
> named `residential_proxy1`.

## 4. THE LIVE ACCOUNT'S ACTIVE ZONES -- everything needed is already paid for

`GET /zone/get_active_zones` with `brightdata-api-key` -> **HTTP 200**:

```
one_shotter          type=unblocker      <- the EXACT zone the SA scrapers call
scraping_browser1    type=browser_api
serp_opal            type=serp           <- a SEARCH-ENGINE-RESULTS zone
residential_proxy1   type=res_rotating   <- the residential proxy
```

## 5. WHAT THIS MEANS -- three consequences, in order of value

**(a) THE SA REVIVAL IS PROBABLY A CONFIG CHANGE, NOT A PURCHASE.** The SA scrapers read
`opal/external-apis` -> `bright_data_api_key`, which is dead. The live `brightdata-api-key` carries
the very `one_shotter` zone those scrapers call. **Repointing the secret is a one-line change with
zero spend.** This should be tested before any subscription is bought or renewed.

**(b) `serp_opal` ALREADY ANSWERS CALL 4.** The ruling was *"We can do a scan for IR pages
associated with the 89 and enumerate from there"* -- a SERP zone is precisely the instrument for
that scan, and for the "web search filtered to the last week" leg. **It exists, it is active, and
nothing has to be procured.**

**(c) YOUR RESIDENTIAL-PROXY INSTINCT IS THE RIGHT ONE, AND ASTN'S R&D PROVES WHY -- with a
sharpening.** `opal/external-apis` also holds `seeking_alpha_email` and `seeking_alpha_password`.
So SA has **parked credentials that the current scrapers never use**, because `one_shotter` is
cookieless and provably cannot ride an authenticated session (s2). **The SA estate is therefore
using the wrong Bright Data product for authenticated SA content** -- it can reach public pages and
not paywalled ones. The ASTN FT pattern -- our browser + parked session + residential proxy -- is
the transferable one, and it is already built and proven in this estate.

> **One caveat on the zone type, flagged not resolved:** ASTN's proven FT combo used a **US
> STICKY-session** proxy (the code passes a `SESSION_ID`), and the live zone is typed
> `res_rotating`. Bright Data normally does sticky sessions on a rotating zone via a session token
> in the username, so this is very likely fine -- **but it is an inference, not a measurement**, and
> a session-riding fetch should be exercised before anything is designed on top of it.

## 6. OPEN / NOT MEASURED

1. **Is the ASTN pipeline itself still running?** Not checked. The SA estate turned out to be
   parked; ASTN's state is unestablished and should not be assumed live.
2. **Does repointing the SA scrapers at `brightdata-api-key` actually work?** The zone is present
   and the token authenticates; an end-to-end SA fetch has not been run.
3. **The residential proxy's true state** -- s3 correction.
4. `org/tier2_senior/2.0.0_SA_COO/deliverables/UNOWNED_CODE_ASTN_WSJFT_NEWS_SCANNER_20260819.md`
   exists and was **not read**. Its title suggests ASTN_WSJFT was flagged as UNOWNED CODE, which
   bears on who maintains any of this. Worth reading before work is scoped onto it.
