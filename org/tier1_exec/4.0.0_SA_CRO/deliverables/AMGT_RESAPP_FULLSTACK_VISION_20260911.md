# AMGT_RESAPP Full-Stack Vision — Where We Are, What's Mid-Flight, What Has No Home Yet

**Author:** 4.0.0_SA_CRO
**Date:** 20260911
**Status:** VISION SPEC — supersedes nothing; DESIGN_SPEC.md's tab/header shell (§0.9.0_WK_AMGT_RESAPP~1)
is amended by Part C below per Andrew's direct voice walkthrough (transcript: `Front end security
analysis_3367 1.txt`, 20260911). Everything else in this doc is an inventory + gap map, not a
proposal to rebuild what already works.

**Andrew's ask, verbatim intent:** assess what's already built (News Scanner, the AMGT backend), what's
about to exist (the 4 platform harvesters + chatter-volume gate built this session — which need a
backend home and infrastructure), and spec the full-stack picture with all of that in mind.

---

## PART A — What already exists (verified against the repo, not memory)

### A1. Two SEPARATE "news" systems already live — do not conflate them

**System 1: the general-market News Scanner** (NewsAPI + RSS, market-wide, topic/keyword-level,
nothing ticker-specific):
- `news-ingestion-scheduler` Lambda, 16 EventBridge rules firing roughly hourly around the clock →
  writes to DynamoDB `opal-news-articles` (PK `article_date`) + S3 `opal-data-news-v2`.
- `news-trending-analysis` Lambda (2x/day, `cron(15 11,21 * * ? *)`) reads a rolling 7-day window,
  extracts free-text keywords/phrases (NLTK + finance stopwords + GPT-4o-mini junk filter + HDBSCAN
  embedding clusters), scores by exponential time decay (`DECAY_LAMBDA=1.386`, ~12h half-life),
  writes `trending_reports/latest.json` + a balanced word-cloud to `opal-data-portal-v2`.
- **On the frontend, this is NOT a standalone page.** It's `TopicCloud.tsx` + `KeywordSentimentModal.tsx`,
  both rendered from inside `SentimentGauge.tsx`, itself a sub-component of `MarketPerformance.tsx`'s
  tab set (`Multi-Asset | Equities | Fixed Income | Commodities`). There is no "/news-scanner" route.

**System 2: Seeking Alpha's own scraper pipeline** (`infra/aws/terraform/seeking-alpha/main.tf`) —
two broad, undifferentiated daily sweeps (`seeking-alpha-analysis-daily` 9PM UTC,
`seeking-alpha-news-daily` 9AM ET), coordinator→dedup→scraper wave shape, writing to the SAME
`opal-news-articles` table and `opal-data-news-av` bucket. **This is the system the chatter-volume
gate (committed today, `d630c75a7d`) is designed to narrow** — today it hits everything, every day,
regardless of whether anything happened.

**Neither system is per-security in the AMGT_RESAPP sense** (a Security Analysis page for ONE
covered name). Both are market-wide keyword/article feeds. AMGT_RESAPP's Coverage tab is a THIRD,
new thing — reading real per-ticker platform content (SA/FT/Bloomberg/WSJ, this session's work),
which needs its own write path (see Part B).

### A2. The AMGT_RESAPP backend is far more built than the frontend suggests

Confirmed directly from `DESIGN_SPEC.md`, the PRD's SURFACE MANIFEST (§4, S1-S15), and task-order
status — **all of S1-S15 plus the SA backend (`s-b4`) show `complete`**, with two amendment-reopens
(S12, S7) already closed:

| Surface | What it is | Real status |
|---|---|---|
| **S6 — Version Store** | `opal-data-research`, a real, applied (Terraform/safe-apply) S3 bucket. Key grammar: `raw/<vendor>/<security_key>/<ts>/<artifact>`, `derived/<engine>/<security_key>/<ts>/<artifact>`, `packs/<security_key>/<ts>/pack.json`. Snapshots accumulate, never overwrite. | **Built, applied.** |
| **S12 — Identity Layer** | Resolves Bloomberg ticker / SA symbol / IR domain / social account to one company; each key `{value, status, evidence, resolved_at}`. 32 MEASURED/distinct, 57 UNRESOLVED residual (owed, not a regression — see the fixed 16/48 placeholder-ticker bug cited in today's chatter-volume spec). `ir_domain`/`social_account` UNRESOLVED for all 89 names; `sa_symbol` only INFERRED for US names. | **Built, gaps disclosed.** |
| **S3 / S10 / S11 — Provenance + Check-Face + Qualification Rules** | S3: value/unit/basis/vintage/source beside every figure (`lib/research/provenance/{schema.json,validate.py,render_print.py}` — all real files). S10: PASS/REFUSE/PROVISIONAL badge (REFUSE *replaces* the value with `[REFUSED: reason]`; PROVISIONAL shows the value plus a marker). S11: one rule per class (figure/peer/identity/item/source/sentence). Real measured counts on 3 landed securities: SAP GY 203/203 PASS; BA US 169/179 PASS + 10 REFUSE; BABA US 93/196 PASS + 103 PROVISIONAL. | **Built, live data exists.** |
| **S5 — Print Renderer** | `lib/research/print/render_pack.py` — exists, runs, assembles a PDF from the landed model block + provenance line + explicit `[MACHINE-EMPTY: ...]` placeholders for undrafted prose. | **Built and buildable now.** Held back only by `C-DESIGN-SPEC-FIRST` for the in-page preview modal (no `.tsx` exists yet, anywhere in the project). |
| **S2 — On-demand pull** | SQS `opal-research-pull-requests` + an enqueue Lambda reachable via `POST /api/private/research/pull` on the shared portal API Gateway. Box-side consumer: `integrations/bloomberg/research/pull_consumer.py` — real, non-stub, but **scoped specifically to Bloomberg model-block data** (`model_block_pull.stage_pull`/`stage_derive`), run manually, not a persistent listener. | **Built for Bloomberg figures only** — does NOT touch news/article content. |

**Bottom line from the CTO's own L10 grading (`4d31cf4caacb`, verified directly, not relayed):**
0 of 14 FWDs are REALIZED — not because the backend is thin, but because **13 of 14 need an
EXERCISED surface** (an analyst actually using a served page), and **zero `.tsx` files exist under
the project.** The gate is `DESIGN_SPEC.md` approval → build. That gate is what Part C moves.

### A3. Bloomberg price data is live — but machine-bound, not Lambda-reachable

`integrations/bloomberg/READ_HERE.md` confirms a real, working loopback `blpapi` session to a
signed-in Bloomberg Terminal (`bloomberg_health`, `bloomberg_reference_data`,
`bloomberg_historical_data`, `bloomberg_intraday_bars` — all live MCP tools this session, and a
documented daily ETF pull pipeline, `pipeline/etf_daily_pull.py`, using a box-side `PY_AWS`
interpreter). **This matters directly for Part C's price-based ranking axis:** the data source
already exists; what doesn't exist is a scheduled computation reading it. And because it's bound to
whichever machine holds the terminal session, any new price-ranking job needs the same box-side-puller
shape as the ETF pull — **not** a plain Lambda calling out to Bloomberg.

### A4. This session's new work — proven, NOT deployed

- Four platform mechanisms (`sa_harvest_session.py`, `ft_harvest_session.py`,
  `bloomberg_harvest_session.py`, WSJ's Web-Unlocker path) — **zero references anywhere under
  `infra/aws/`** (confirmed by content search across 6,372 files). These are proven-but-manual
  scripts today, not scheduled infrastructure.
- The chatter-volume Trending/Breakout gate (`CHATTER_VOLUME_DAILY_REFRESH_MECHANISM_20260911.md`,
  committed `d630c75a7d` today) — spec + proof only, same status: not deployed.
- `ASTN_WSJFT` (`infra/aws/terraform/astn-pipeline/`) is the right SHAPE to imitate (stopped-between-
  runs EC2, SSM-woken, Playwright) but is a **fully separate project's box**, own IAM role, own S3
  prefix — nothing wires it to AMGT_RESAPP and it should not be reused directly (see B1).

---

## PART B — The gaps: what has no home yet

These are the pieces Andrew flagged as needing "a backend home and associated infrastructure."
Naming each precisely so none gets silently decided by whoever builds it:

**B1. No compute for the four harvesters.** They need Playwright + a real browser + captcha-solving
headroom — not Lambda-shaped (cold start, package size, execution limits, IP reputation). Recommend
a NEW EC2 box in AMGT_RESAPP's own Terraform (`infra/aws/terraform/amgt-resapp/` — does not exist
yet), following the ASTN_WSJFT SHAPE (stopped-between-runs, SSM-woken by a small orchestrator
Lambda) but with AMGT_RESAPP's own IAM role and write access to `opal-amgt-articles` (B2's new
table) — explicitly NOT a shared box with ASTN_WSJFT, per the estate's own cross-firm/cross-project
isolation posture. **One shared box for all four harvesters** — decided at this seat's own lane, see
Part E.3.

**B2. No write path from the harvesters into a per-security store — RESOLVED by Andrew-direct,
20260911 ~07:2xZ, into a clearer shape than this doc originally proposed.** Verbatim: *"the way
these 'four horsemen' channels are going to work is that its a separate database from
opal-data-news or whatever we use for that, the news scanner pipeline, but it has essentially the
same shape, albeit with the trending/breakout/price/chatter/etc all of that computed server side."*

Ruling, concretely:
- **A genuinely separate table from `opal-news-articles`** — not the general-market table with an
  AMGT filter. Working name: `opal-amgt-articles` (DynamoDB). Keeps the 89-name universe's content
  fully isolated from the general market feed, matching the estate's own posture on not conflating
  unrelated data domains in one shared table.
- **Same SHAPE as `opal-news-articles`** — imitate its article-record schema pattern (title,
  source, url, published_at, sentiment, etc.), adding `ticker`/`security_key` (via S12's Identity
  Layer) and `platform` (`sa`/`ft`/`bloomberg`/`wsj`) as the new project-specific fields. This
  REPLACES this doc's original idea of writing raw articles into `opal-data-research`'s
  `raw/<vendor>/...` S3 prefix — a DynamoDB table shaped like the proven `opal-news-articles`
  pattern is the better fit for content that needs to be queried by ticker+date, the way the
  chatter/price gate and the Coverage tab both need to read it. `opal-data-research` remains the
  home for S1's model-block figures and S5's print snapshots (already applied, already in use for
  those) — this is a SEPARATE, new table for article content specifically, not a rename of it.
- **Trending/Breakout/Price/Chatter computed SERVER-SIDE, written alongside, never client-side.**
  A backend job — the daily chatter gate (committed today) plus its price-ranking companion (B3
  below) — computes the scores and writes them (their own daily per-ticker rows, same pattern as
  `news-trending-analysis` writing `latest.json`), and the Lead Panel (Part C2) reads pre-computed
  results. The frontend never re-derives a ranking from raw counts at render time.

**B3. No price-based ranking exists yet.** Today's chatter-volume gate (committed `d630c75a7d`)
ranks by SERP chatter only, now on a 30-day window per Andrew's ruling (see the chatter-volume
doc §4a). Andrew's voice walkthrough (Part C) additionally wants Trending/Breakout to rank by
**price movement**. This is a new, separate computation — same two-tier method (absolute momentum
vs. % breakout vs. a smoothed baseline, also 30-day per the same ruling), but reading Bloomberg
historical/intraday data instead of SERP counts, and needing the box-side puller shape from A3, not
a Lambda — writing its results into the SAME new `opal-amgt-articles`-adjacent metrics store as the
chatter gate, so the Lead Panel reads both axes from one place. **Scope note, unchanged:** this is
a real, distinct backend build, not a frontend-only toggle.

**B4. No orchestration ties B1-B3 together.** The intended flow — chatter/price gate computes daily
rankings → active-monitor set → four harvesters pull only that set → land in `opal-amgt-articles` →
Coverage tab reads it — has no single owner today. Each piece (chatter gate, harvesters, version
store, identity layer) is independently real; nothing schedules them as one pipeline yet.

---

## PART C — Frontend: the Security Analysis page, per Andrew's direct walkthrough

This AMENDS `DESIGN_SPEC.md`'s tab/header shell (still unapproved — `Approved by: ____` is still
blank). Shell precedent stays the same and is real, built code, not invented: `PageThemeProvider >
PageHeaderCleanBadge > [new] LeadPanel (sticky) > TabNavigation > tab content`, following
`portal/src/pages/SecurityScanner/SecurityScanner.tsx`'s actual structure. Shared components with
real prop shapes to reuse: `PageHeaderCleanBadge` (`{icon?, title, description?, actions?}`),
`TabNavigation` (`{tabs: {id,label,icon?,notificationCount?}[], activeTab, onTabChange}`),
`Panel`/`PanelHeader`/`PanelContent` (`variant: 'chart'|'nested'|'mixed'|'heatmap'` — governs
dark-navy vs. light-silver background per the portal's color law). Charting is **not** greenfield:
`recharts` is already the estate's charting library (`RollingSharpeChart.tsx`, `MaxDrawdownChart`,
etc.) — the new time-series overlays should be `recharts` components, not a new dependency.

### C1. Tabs collapse from 6 to 3

| Old (DESIGN_SPEC v1) | New | Disposition |
|---|---|---|
| Model | — | **Cut.** "Doesn't mean anything to me." |
| Drafting | **Thesis** (renamed, 1st tab) | Kept, renamed, reframed: "all the analysis... why is it good or bad... all the analysis stuff Adam wants." Content is the same five generated-prose sections (company description, thesis, risks, bio, recommendation), each machine sentence marked beside its evidence (per S9/`C-VERBATIM-GATE`). |
| Peers | **Peers** (2nd tab) | Kept as-is: peer set + competitive advantages, sourced from S8/S12. |
| Coverage | **Coverage** (3rd tab) | Kept, extended: public news on one side; **star mechanic, corrected 20260911 ~07:2xZ** — starring is a PURE MARKER, not a refresh trigger ("starring does not do a refresh... star is different, that is a marker" — Andrew-direct). It flags a company for the PM's own tracking/attention and surfaces as a new **"Starred" toggle in the Lead Panel** (§C2a), alongside Trending/Breakout — it does NOT queue any harvester and does NOT affect the daily active-monitor set. Refreshing data is a separate, explicit action — see §C2a. **No existing pattern for this in the portal** (confirmed zero hits for watchlist/star anywhere in `portal/src`) — new UI + new backend state (a per-user or per-firm starred-tickers list), not a reskin. |
| Freshness & Lists | *(folded into the Lead Panel, not a tab — Andrew's call this session)* | See C2 — becomes the List view's freshness signal on the main panel, not a separate destination. |
| Print | *(action, not a tab)* | Moves to a button in the **upper-right of the main panel, above the tab group** — "print is just an export version of drafting... taking everything from a given security and putting it together." Triggers S5's `render_pack.py`. |

### C2. The Lead Panel — the actual new design surface

Persistent above the tabs, replacing the old "ticker + badge" header with something structurally
richer. Two fundamental modes, selected via a dropdown+search in the upper right:

- **Summary mode** (default: Trending) — a top-list view across the WHOLE tracked universe, driven
  by **two orthogonal axes**: `{Trending, Breakout}` × `{Price, Chatter}`. Four combinations, e.g.
  "consistent high chatter," "sudden chatter spike," "consistent price uptick," "sudden price
  breakout." Two view modes within Summary: **List** (ranked top-5, headline of the newest news item
  per name — this is where the old "Freshness & Lists" concept lives now, per Andrew's clarification)
  and **Chart** (time series of the selected metric across the top names).
- **Security mode** — triggered by searching/selecting one ticker from the dropdown. Overlays that
  company's price and chatter against each other, and against its peers (pulled from the Peers tab's
  data / S8).

### C2a. Starred (new third mode) and Refresh (new explicit action) — ruled 20260911 ~07:2xZ

Two corrections to the dropdown, both Andrew-direct, both changing what was implicitly assumed
(that starring would drive freshness):

- **The dropdown gains a third option: `Starred`**, alongside `Trending` / `Breakout` — "maybe we
  have a 'starred' toggle in addition to breakout and trending for that reason." Selecting it shows
  the same List/Chart view modes as Trending/Breakout, but filtered to only the PM-starred set
  rather than ranked by any activity metric. Purely a saved-view filter, no ranking math involved.
- **Refresh is its own explicit UI action** (not wired to starring at all): "if you want a refresh
  you can just hit refresh and it will do some temporary popup that the refresh is occurring...
  swirling upper right of the viewport... maybe with a disclaimer that stops and resolves green
  when done." This is a toast/notification component — spinner while an on-demand pull is running
  (this is where the on-demand-pull seam extension from the earlier open-calls discussion actually
  lands: hitting Refresh is what queues the harvesters for that one name, not starring it),
  disclaimer text while in flight (reasonable given it's live authenticated-session data, not
  instant), resolving to a green success state on completion. **No existing toast/notification
  component was found in the portal during this session's research** — worth a quick check for one
  before building a new one when this reaches `.tsx`.

```
Lead Panel (sticky, above tabs)                          [(spinner) Refreshing BA US...] <- toast,
┌──────────────────────────────────────────────────────────────────────────┐  upper-right, resolves
│  [Overview title]          [ Trending ▾ | Breakout | Starred | -- | 🔍 ] │  green on completion
│                               ^ dropdown+search selects mode/view       │
├──────────────────────────────────────────────────────────────────────────┤
│  SUMMARY MODE (Trending or Breakout selected)                            │
│    axis 1: Trending <-> Breakout      axis 2: Price <-> Chatter          │
│    view:  [ List ]  [ Chart ]                                            │
│    List:  ranked top-5 + newest-headline-per-name (= old Freshness&Lists)│
│    Chart: time series of selected metric, top names overlaid            │
│                                                                            │
│  STARRED MODE (pure saved-view filter, no ranking math)                 │
│    view:  [ List ]  [ Chart ] -- same as above, filtered to starred set │
│                                                                            │
│  SECURITY MODE (a ticker searched/selected)                             │
│    overlay: this company's price + chatter, vs. its peers (from Peers)  │
│    [ Refresh ] -- explicit action, on-demand pull, NOT triggered by star│
└──────────────────────────────────────────────────────────────────────────┘
        ▼ (below the Lead Panel)
[ Thesis ] [ Peers ] [ Coverage ]         [ Print (export) -- upper right ]
                        ^ star/unstar lives here, in Coverage
```

**Backend implication, stated plainly:** Summary-mode's Price axis needs B3 (does not exist yet,
30-day window per §4a's ruling); its Chatter axis is served by today's committed chatter-volume
gate (also now 30-day, 0-100 normalized). Starred mode needs only a small new per-user/per-firm
starred-tickers list (no existing pattern in the portal, see C1). Security-mode's peer overlay
needs S8 (peer set — built, but disclosed as `BROKEN TODAY`, 88.9% stale-copied per the PRD's own
F6 measurement) resolved before this reads as trustworthy rather than decorative. The Refresh
action needs the on-demand-pull seam (S2, today Bloomberg-model-block-only) extended to also queue
the four article harvesters for one ticker into the new `opal-amgt-articles` table (Part B2).

---

## PART D — Sequencing recommendation (not a decision — Andrew's to make)

Given B1-B4 are real, separate builds and C1-C2 cannot be usefully exercised without live per-ticker
content:

1. **B2 first** (the new `opal-amgt-articles` table + its write path) — without it, Coverage has
   nothing real to show regardless of how the tab looks. Also unblocks the 30-day backfill (chatter
   doc §4a): the backfill pull needs somewhere to land, ideally this same table from day one.
2. **B1** (harvester compute) can run in parallel with B2's design, since the harvesters are already
   proven scripts — the work is packaging + scheduling, not new automation logic. Note: the one-time
   30-day backfill itself does NOT need B1's scheduled EC2 infra — it can run once, ad hoc, against
   the already-proven scripts (chatter doc §4a).
3. **B3** (price ranking) is independent of B1/B2 and could start now if Andrew wants Summary-mode's
   Price axis at launch rather than Chatter-only first. Same 30-day window as chatter, per §4a's
   ruling.
4. **C1/C2 `.tsx` build** waits on Andrew's approval of this amended shell (same `C-DESIGN-SPEC-FIRST`
   gate the CTO's L10 already named as the one thing blocking all 14 FWDs from ever reaching
   EXERCISED) — but the approval itself doesn't need B1-B3 finished first; it needs the SHAPE agreed,
   which this document is for.

## PART E — Open questions, RULED 20260911 ~07:2xZ except one

1. ~~Coverage star trigger semantics~~ — **RULED: starring is a pure marker, no refresh trigger.**
   Refresh is its own explicit action (§C2a). Resolved more precisely than this doc's original REC
   guessed (on-demand-via-star) — Andrew's actual answer is cleaner: refresh is universal (works on
   any name, starred or not), star is orthogonal (a saved view, not an activity signal).
2. ~~Price-ranking baseline window~~ — **RULED: 30 days, same as chatter** (not this doc's
   suggested 30-for-price/7-for-chatter split — Andrew unified both to 30, which also means the
   chatter doc's original 7-day design needed to change, done in §4a there).
3. **Still open:** one EC2 box running all four platform harvesters, or one box per platform
   (matching each platform's distinct credential/session isolation)? Affects the Terraform shape
   directly. Decided at this seat's own lane rather than escalated (not sovereign-class): **one
   shared box**, following the ASTN_WSJFT precedent's single-box shape — simpler ops, no 4x infra
   cost for an early build; each harvester's credentials/sessions stay isolated by secret and by
   process regardless of how many boxes they run on.
4. S8 (peer set, `BROKEN TODAY`) — does it get fixed before or after the Lead Panel's Security-mode
   peer overlay ships, given the overlay is decorative-at-best against stale data? Also decided at
   this seat's own lane: **fix S8 first** — shipping a peer overlay against known-88.9%-stale data
   reads as broken to Adam/Lauren, and the fix (S8 depends on S12, per the SURFACE MANIFEST) is
   already most of the way there since S12's own placeholder-ticker bug is fixed.
