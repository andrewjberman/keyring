# AMGT_RESAPP -- Security Analysis: the research pack, automated

**L1 BRIEF | `4.0.0_SA_CRO~Z` | 2026-09-10 | MODE: NEW (greenfield)**
**Directive:** D5 Alternative Research. **Project:** AMGT_RESAPP (D5's first registered project).
**Origin:** Adam Muller (Head of Asset Management) -> Andrew, 2026-09-10T13:18:06Z, "Claude
automation": automate *a simple financial model, a company description including segments, the
investment thesis, the risks, a bio of key management usually the CEO* -- and *"we want it to print
cleanly."*

> **Consumer:** `/endpoint --forward` at L2 (`1.0.0_SA_CTO`). Every outcome below is numbered and
> separately headed so it can be cited. Parts II-VII bound and support Part I; only Part I is
> outcome-bearing.

---

# PART I -- THE OUTCOME TERRITORY

## O1 -- An analyst gets a first-draft pack for a covered name without opening Excel or a terminal
Today the pack is assembled by hand: a FactSet/CapIQ/Bloomberg-driven Excel one-pager, pasted into a
Word template, then written around. O1 is met when an analyst opens the Security Analysis page for a
name in coverage and the model block, company description and segment breakdown are already there.

## O2 -- An analyst pulls a pack for a name that is NOT in coverage, by typing a ticker
Adam's team covers a fixed list today. O2 is met when an analyst types a ticker the firm has never
covered, and gets the same assembled pack -- with the page honest about the fact that it is being
fetched now rather than served from a snapshot.

## O3 -- An analyst can defend every number on the page in an IC meeting
O3 is met when each figure carries, visibly, where it came from, on what definition, and as of when
-- so that a challenge in a meeting is answered from the page rather than from memory.

## O4 -- An analyst reads what has been said about the name recently without leaving the page
O4 is met when the page surfaces recent coverage of the security -- news, Seeking Alpha, and recent
web mentions from the company's own IR channel and trusted publications -- ranked by recency and
frequency of mention, each item linking out.

## O5 -- An analyst hands Adam a printed pack that looks like the ones already circulating
Adam's acceptance test is *"we want it to print cleanly."* O5 is met when the page produces a
PDF preview in a modal, downloadable, whose output Adam would forward without reformatting.

## O6 -- An analyst returns to a name and can see what changed since last time
O6 is met when a previously-researched name shows its prior snapshots, and refreshing produces a new
one rather than overwriting -- so an analyst can say what moved, not merely what is true now.

## O7 -- Adam can see which covered names have current research and which have gone stale
O7 is met when the coverage universe is visible in one place, each name showing when it was last
refreshed, so the gap between "covered" and "current" is legible without opening folders.

## O8 -- An analyst gets a peer comparison that is actually about this company
Measured today: **48 of 54 one-pagers carry a peer set belonging to a different company.** O8 is met
when the comparison block on the page is about the security on the page -- and when it is not
derivable, says so rather than showing someone else's comps.

## O9 -- An analyst sees the AI-drafted prose as drafted, and edits from it
Per Andrew's ruling, the AI drafts Adam's five limbs first and summarises the evidence second. O9 is
met when generated prose is visibly marked as generated, sits beside the evidence it was drawn from,
and is a starting point an analyst edits rather than a finished claim.

---

# PART II -- WHERE THE BOUNDARY SITS

**THIS PROJECT OWNS:** the Security Analysis portal page and its design spec; the versioned pack
object and its store in `opal-data-research`; the assembly path that fills it (market/fundamental
data, evidence, AI drafting); and the print renderer that emits Adam's artifact.

**IT RELIES ON, AND DOES NOT OWN:**

| Relied on | Owner / home |
|---|---|
| Bloomberg terminal + DAPI on this device | `0.0.3_BG_BBGTerminal`; `integrations/bloomberg/` |
| The Bright Data account and its three zone archetypes | estate-wide; ruled by Andrew 2026-09-10 |
| The residential proxy + Kimi vision authenticator pattern | **ASTN_WSJFT** and **ADVI_BDAPIMIG.P1** |
| Portal shell, auth, panel primitives, tab navigation | the portal estate; `SecurityScanner` precedent |
| The research corpus in SharePoint (89 names, template, packs) | Adam's team -- **read-only to us** |

**NAMED SIBLINGS, and how this differs from each:**
- **ASTN_WSJFT** -- CEO news digest. Shares the residential proxy and the session-riding pattern;
  different consumer, different output. **No shared code is assumed, only a shared pattern.**
- **ADVI_BDAPIMIG.P1** (`bd-49f-auto-login`) -- the Kimi vision authenticator. **Source of the
  pattern if SA needs authenticated access.** Not a dependency if public pages suffice.
- **The Seeking Alpha scraper estate** (7 Lambdas) -- an **ARCHIVE PRODUCER for a parked estate**,
  not this project's fetch path. Andrew ruled the design is a symbol-page one-shot.
- **D5's existing alt-research corpus** (research-call transcripts + the 63-name materiality queue)
  -- the same directive, a **different function**. AMGT_RESAPP does not consume or replace it.
- ⚠ **`OPAL_KIMIPIPELINE` is NOT a sibling.** Name collision only. Different program entirely.

**EXPLICITLY NOT OWNED HERE:** the missing `aws_lambda_function` declarations on the seven SA
Lambdas (an `AE_CloudOps` estate defect, surfaced separately); the FactSet and CapIQ subscriptions;
and Adam's editorial judgment -- **the analyst-specific sections are the value of a pack and this
project drafts toward them, it does not replace them.**

---

# PART III -- THE QUALITATIVE BAR

*No numbers are invented here. Each bar names who, what, and what it displaces.*

1. **An analyst opens a covered name and does not open Excel.** The model block is populated with
   figures they would otherwise have pulled by hand through three separate add-ins.
2. **A figure survives a challenge in an IC meeting from the page alone.** Asked "where is that
   from, and as of when," the analyst points at the screen rather than reconstructing it.
3. **Adam forwards the printed output without reformatting it.** The displacement test: it replaces
   the Word document he circulates today, not merely a screenshot of a dashboard.
4. **The comparison block is about the company on the page.** Today it usually is not; an analyst
   who has learned to distrust it stops distrusting it.
5. **An analyst refreshing a name can state what changed.** Not "here is the current state" but
   "revenue guidance moved and here is the prior snapshot that says so."
6. **A machine-drafted paragraph is never mistaken for a firm view.** An analyst can tell at a
   glance which sentences they must own before the pack leaves the building.

---

# PART IV -- THE SUBSTRATE: findings, each with what was measured

**F1 -- The corpus, the template and the model already exist and are consistent.** 89 name folders
in a SharePoint library that syncs to this device; a blank `NEW Research Pack Template` whose four
blocks (`[PASTE EXCEL OUTPUT]` / RECOMMENDATION+COMPANY DESCRIPTION / THESIS|RISKS / bio) are
reproduced in the filled packs -- provenance confirmed by a misspelling (`CONSDIERATIONS`) shared
between template and pack.

**F2 -- The model is mechanical and small; the cost is field mapping, not volume.** ~20 line items
x 10 years plus ~25 header scalars. Measured payload for one security's full 10-year history:
**180 data points, ~3.4 KB, one call.** Projected full 89-name rebuild ~17,400 data points,
~300 KB. **The binding constraint is UNIQUE SECURITIES TOUCHED, not volume** -- an undeduped peer
block would add up to ~1,000 more.

**F3 -- Bloomberg serves the model, with two named exceptions.** 32 of 35 line items mapped on
`SAP GY Equity`. Raw items reconcile to FactSet within +/-1 (Revenue, FCF). `EBITDA_ADJUSTED` lands
~1% off where plain `EBITDA` was 7-10% off. **No Bloomberg mnemonic reproduces FactSet's recurring
EPS across 8 tested** -- FactSet's normalization is proprietary. **RULED by Andrew 2026-09-10: adopt
Bloomberg's definitions and state the basis beside the number.**

**F4 -- Bloomberg's units are inconsistent across its own field families.** `CUR_MKT_CAP` absolute
while `NET_DEBT`/`CURR_ENTP_VAL` are millions; `EQY_SH_OUT_REAL` absolute while
`IS_SH_FOR_DILUTED_EPS` is millions; margins are percents where the source workbook holds decimals;
`CAPITAL_EXPEND`'s sign is inverted. **A mnemonic-only mapping is silently wrong by 100x in some
cells and 1e6 in others.**

**F5 -- Price and fundamentals land on different dates in one response.** Measured 4 of 10 years
split (14 rows for 10 fiscal years). **Joining on the date string silently drops 40% of that name's
price history.** Fiscal year is the join key.

**F6 -- The peer block is broken across the corpus.** Full population of 54 one-pagers: **48
(88.9%) carry a stale telecom peer set** copied from a KPN workbook onto ASML, AstraZeneca, BP,
Boeing, Costco, Hermes and 42 others. **4 (7.4%) carry a genuine, unmistakably hand-chosen set**
(Imperial Brands vs Japan Tobacco; Lenovo vs Asus/Acer). Peer selection is analyst judgment -- and
it is exercised 7.4% of the time.

**F7 -- The landed SA corpus is not a usable news source.** 10,245 objects; article dates stop at
**2026-04**; **0 of 200 sampled articles carry a populated ticker**; both DynamoDB tables are
partitioned by date, not ticker. **It is an archive, not a feed.**

**F8 -- A cookieless unlocker cannot read authenticated content.** Measured on FT: the Web Unlocker
ignores custom cookies; the Scraping Browser sandboxes cookie injection (0 of 49). The working
combination is **our own browser + a residential IP + a real fingerprint**, riding a parked session.

**F9 -- The estate already holds a proven session-harvesting authenticator.**
`bd_49f_auto_login.js`: Kimi vision classifies the screen to one token and localizes elements to
click; the OTP is pulled from email via Graph; the fresh session is parked in Secrets Manager. Its
hardening (health guard, DOM fallback, "a hang is not a throw") is paid-for and should be inherited.

**F10 -- The portal has the page skeleton and the process precedent.** `SecurityScanner` provides
`ScannerHeaderPanel`, `tabs/` on shared `useTabNavigation`, `utils/asOf.ts`, and a 560-line
`DESIGN_SPEC.md` gated *"no .tsx files written until approved."* Market Overview (`/market` ->
`MarketPerformance`) provides `SentimentPanel`, `SentimentGauge`, `KeywordSentimentModal`.

**F11 -- The SERP path for IR pages works, with a trap.** `serp_opal` returned 10 correct organic
results for one name. **The `link` field is an obfuscated Google redirect; `display_link` carries
the real domain.** An enumerator built on the obvious field stores unresolvable URLs and looks like
it worked.

---

# PART V -- WHAT MUST BE TRUE (named, deliberately NOT sequenced)

- **The desktop/cloud seam is crossed somehow.** The portal runs in AWS; Bloomberg DAPI is
  `127.0.0.1:8194` on this device only. Any design must say how a browser request reaches it.
- **The Bloomberg session's state is visible to the user.** Sign-out is the most common failure and
  costs a 2-attempt budget to repair; a page that fails silently against it reads as broken.
- **`opal-data-research` exists** (measured absent on the live plane) and every vendor response
  lands there on first pull -- **a correctness requirement, not an optimisation**, because
  Bloomberg's derived fields have no backfill.
- **A ticker identity layer exists.** The Bloomberg ticker, the SA symbol and the IR-page identity
  are three different keys, and the coverage universe is heavily ex-US.
- **Zone selection lives in the caller** -- one account credential, three archetypes.
- **A decision on paywalled sources.** If SA analysis behind a login is in scope, the F9
  authenticator pattern and `seeking-alpha/credentials` are the route; if public pages suffice,
  neither is needed.
- **The design spec is approved before .tsx is written**, per the F10 precedent.

---

# PART VI -- STATUS TODAY ⛔ **NOT OUTCOME-BEARING**

*Every line measured 2026-09-10; status ages, outcomes do not.*

- Nothing is built. No page, no route, no bucket, no pack object.
- D5 placement moved to this device on Andrew's word today; the register act is routed to
  `0.0.0_AB_MSTR~Z` and **not yet applied**. D5's member set read empty at time of writing.
- Bloomberg terminal: `ok: true`, `//blp/refdata`, no sign-in spent.
- Bright Data: one live account credential; `one_shotter`, `scraping_browser1`, `serp_opal`,
  `residential_proxy1` active. Two per-target key secrets measured dead.
- The SA estate: 7 Lambdas Active but **undeclared in Terraform**; both daily rules DISABLED; both
  EC2 scrapers stopped.
- `seeking-alpha/credentials` created today and tagged.

---

# PART VII -- WHAT THIS BRIEF DOES NOT CLAIM

- **The field map was measured on ONE security** (`SAP GY Equity`). The unit conventions in F4 are
  the most likely thing to differ on a US name, an ADR or a financial. Nothing here establishes
  they generalise.
- **Whether the stale peer set (F6) reaches the PRINTED packs is UNVERIFIED.** The docx pastes Excel
  output as an image; which image is the comparison was not traced. **Nobody should conclude packs
  shipped wrong on the strength of this brief.**
- **Whether SA's login is captcha-gated is unknown**, so whether F9's vision layer is needed at all
  is unknown.
- **The IR scan was proven on one name, not at scale.** How many of the 89 resolve to a genuine IR
  domain rather than an aggregator is unmeasured, and the ex-US names are the risk.
- **The RSS/NewsAPI news scanner's liveness was not established.** Its README is ~10 months stale
  and cites a path from the other device.
- **CapIQ's `IQ_*` line items were never mapped** -- only FactSet's, and only via cached workbook
  values read with `data_only=True`.
- **No decomposition, no sequencing, no task orders.** That is L5 and it is not this seat's.

---

```
  BRIEF PATH        docs/briefs/amgt-resapp-security-analysis-20260910.md
  PROJECT           AMGT_RESAPP  (named by Andrew 2026-09-10; register act routed, NOT yet applied)
  DIRECTIVE         D5 Alternative Research
  EXISTING PRD      NONE for AMGT_RESAPP.  D5's directive PRD: docs/architecture/D5_ALT_RESEARCH_PRD.md
  SIBLING PROJECTS  ASTN_WSJFT · ADVI_BDAPIMIG.P1 · the SA scraper estate · D5 alt-research corpus
                    (NOT OPAL_KIMIPIPELINE -- name collision only)
  PRIOR ART         SecurityScanner page skeleton + DESIGN_SPEC precedent · MarketPerformance
                    sentiment/news components · bd_49f_auto_login.js Kimi authenticator ·
                    ASTN_WSJFT residential-proxy session-riding · Bright Data 3 zone archetypes
  SUPPORTING        org/tier1_exec/4.0.0_SA_CRO/deliverables/AMGT_RESAPP_{PRE_BRIEF_NOTES,
                    BLOOMBERG_FIELD_MAP,SA_ONESHOT_PROBE,SA_CORPUS_STALENESS,DATA_CONTRACT_DRAFT,
                    KIMI_AUTHENTICATOR_PATTERN,LAMBDAS_PEERS_IRSCAN}_20260910.md
                    ANDREW_DIRECT_20260910_AMGT_RESAPP_FIVE_CALLS_RULED.md
  MEASURED AT       2026-09-10, 13:30Z-16:00Z (all Part VI claims and all Part IV findings)
```
