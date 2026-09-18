# BRIEF -- the Peers panel, from current to desired: Seeking Alpha's shape

**From** `4.0.0_SA_CRO~Z`, 2026-09-18 ~18:1xZ, at Andrew's word: *"Agree with everything youve got write up the brief
and issue to CTO~Z"*. **To** `1.0.0_SA_CTO~Z`, for the panel-briefs intake
(`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTOZ_AMGT_RESAPP_PANEL_BRIEFS_INTAKE_20260918.md`). **Status:** a BRIEF.
It creates no gate, cuts no order and spends no decision. Per Andrew's timing word (the CTO's `e3af87b212`), nothing
here asks for PRD work before every panel brief is in.

**Andrew's words behind it**, verbatim in `ANDREW_DIRECT_20260918_17xxZ_PEERS_SEEKING_ALPHA.md`:
- the design target: *"figure out a solution with Seeking Alpha where we basicaly pull the information from here:
  https://seekingalpha.com/symbol/{TICKER}/peers/comparison"*, with a HAR of that page for the shape;
- the mechanics: *"You should be using a cookie via rest api"* ... *"take the existing function that is designed for
  the rest api hit (not the crawler script), and test the endpoints we need for Peers"* ... *"the rest fetch is
  probably it"*;
- three rulings: *"It's now 5 instead of 8, we'll fit to the SA shape. If we can get the remaining two from BBG then
  do that, if not, fall back to what SA provides, as a general rule for the pipeline for that process. Yes we can do
  that in SA shape."*

His standing direction also applies: no fleet run until the process is validated end to end, and every stage is framed
by what makes it run for a NEW security.

---

## 0. The denominator, and a correction to this seat's earlier Peers V brief

33 keyed names, from `crosswalk/v1/2026-09-15.json` records with resolution MEASURED. Current-state figures were read
with the adapter's own `read_peer_set` and `read_scores` over those 33. The earlier `BRIEF_PEERS_V_ESTIMATES_SHAPE_20260918.md`
counted 34, which included NVIDIA; it carries a correction block from this commit.

---

## 1. Where the panel stands, measured 2026-09-18

**The producer** is `lib/research/peers/engine.py`, a lexicographic ranker over the scanner database. Its rungs, in
Andrew's earlier order (PRD v0.8 ratified text, quoted at `engine.py:11-16`): same sector, then a 0.2x-5x market-cap
band, then same country, then same industry group, capped at 12 members. It writes `peers/v1/<key>/<as_of>.json`
(interface R-1). The adapter `read_peer_set` (`scoped_amgt.py:1244`) serves it to `PeersTab.tsx` on the `/peers` route.
All 33 sets date from one run, `2026-09-17T0240Z`.

| what | measured over 33 |
|---|---|
| peer set basis | derived 31; **absent 2** -- KDDI and ICICI Bank ("no candidate reaches rung 2": nothing of similar size in the sector) |
| members | 372; **160 carry a numeric SEDOL-stem ticker**, not a symbol |
| CSC columns present | **5 of 17 on all 33** (R-1's own map, `csc.py`) |
| Peers V score | **ABSENT on 33 of 33** |

**The sets themselves are the defect Andrew is fixing.** Boeing's current peers are Deere, Eaton, Union Pacific,
Uber, Parker-Hannifin, Lockheed, Howmet and Vertiv. Costco's include Coca-Cola, Procter & Gamble and Philip Morris.
HSBC's are mostly unresolved numeric codes. A ranker over sector and size cannot tell an aircraft maker from a
railroad.

---

## 2. What Seeking Alpha serves -- measured through the existing REST function

**The instrument:** `integrations/seekingalpha/rest_fetch.py`, used as-is: its `load_config`, `build_session` (the
PARKED session bundle from Secrets Manager, Chrome TLS impersonation, residential-proxy egress) and `_do_get` (a
per-page Referer, full request logging, `detectors.classify`). **15 GETs** for Boeing, SAP and KDDI (ADR `KDDIY`), all
classified OK. The parked session, captured 2026-09-11T02:13Z, was accepted. Nothing was landed in any bucket.

**The page is four JSON calls**, read from the HAR for shape only (no header, cookie or token value printed):

| call | returns |
|---|---|
| `GET /api/v3/symbols/{slug}/suggested?source_type=peers_similarities&variation=ds_v2` | the peer set: 5 per subject |
| `GET /api/v3/tickers?filter[slugs]=...&include[gics]=true` | identity, exchange, currency, GICS sector and sub-industry |
| `GET /api/v3/metrics?filter[fields]=...&filter[slugs]=...` | one value per field per ticker, with a `meaningful` flag |
| `GET /api/v3/ticker_metric_grades?...&filter[algos][]=main_quant` | SA's factor grades: value, growth, profitability, momentum, EPS revisions |

**The peer sets it returned:**

| subject | Seeking Alpha's peers |
|---|---|
| Boeing | Airbus (EADSY), Lockheed, General Dynamics, Northrop, RTX |
| SAP | Accenture, Microsoft, Oracle, Salesforce, ServiceNow |
| KDDI | America Movil, Vodafone, Rogers, Millicom, SK Telecom |

**Every ticker is a US listing or ADR, priced in USD,** so the subject row and its peers share one currency.

### 2.1 The 17 CSC columns in SA's shape -- measured over 18 rows (3 subjects + 15 peers)

| CSC column | source, per Andrew's rule | field | rows filled of 18 |
|---|---|---|---|
| Price | SA | `close` | 18 |
| Mkt Cap | SA | `marketcap` | 18 |
| EV | SA | `tev` | 18 |
| Debt | SA | `total_debt` | 18 |
| Cash | SA | `total_cash` | 18 |
| Preferred + Minority (one column, SA shape) | SA | `other_cap_struct` | 12 |
| P/E FY1 / FY2 / FY3 | SA | `pe_nongaap_fy1` / `_fy2` / `_fy3` | 15 / 16 / 15 |
| 5-yr Revenue growth | SA | `revenue_growth5` | 18 |
| 5-yr EBIT growth | **Bloomberg** (SA does not carry it) | `GEO_GROW_OPER_INC` (EBIT Growth 5 Year CAGR); `EBIT_GROWTH_ADJUSTED_5Y_CAGR` covers 17 | 15 |
| 5-yr FCF growth | **Bloomberg** (SA does not carry it) | `FREE_CASH_FLOW_5_YEAR_GROWTH` | 15 |
| Shares | derived | market cap / price | 18 |
| Debt/Equity, Net Debt/Equity, Net Debt/Capital | derived | debt, cash, and equity from market cap / `pb_ratio` | 18 |

**So the table goes from 5 of 17 columns to all of them**, with Preferred and Minority as SA's one combined column.
Two things the numbers show:
- **Forward P/E is now a true fiscal-year figure.** The old map labelled trailing and next-12-month figures with
  fiscal years (the reason for `csc.py`'s refusal rule).
- **An empty cell is honest.** Boeing's FY1 P/E comes back null and flagged `meaningful: false` because its forward
  earnings are negative. KDDI and SK Telecom carry no SA estimates. The page shows these as not meaningful, never as
  zero.

**The Bloomberg fill resolved with no mapping step:** each SA ticker queried as `<TICKER> US Equity` returned data
(15-17 of 18 per field), including the ADRs. Where Bloomberg has no value for a row, Andrew's rule falls back to SA's
nearest measure, LABELLED as that measure (below).

---

## 3. The rulings, and what each one needs

### 3.1 Peers V floors: 5 peers, fit to SA's shape

Andrew ruled the peer floor 5, replacing his earlier 8 (`lib/research/scores/peers_v.py:64`, asserted at `:70` as his
ruling). **With his "agree with everything", the per-measure floor `MIN_PEERS_PER_MEASURE = 6` (`:62`) also moves to 5**
-- at 6, no measure could compute over five peers. The measure-count floor (`|M| >= 3`, `:69`) is unchanged. The code's
asserts cite his earlier ruling, so the change carries the new citation.

### 3.2 The general rule for any column SA lacks: Bloomberg first, then SA's nearest

For the Peers pipeline: a column SA carries comes from SA; a column SA does not carry comes from Bloomberg; where
Bloomberg has no value, the pipeline falls back to what SA provides. Two things keep that rule honest:
- **Every cell carries its source** -- `SA`, `BBG` or `SA_FALLBACK:<field>` -- per "a value must carry its claim". A
  fallback cell is labelled as the SA measure it is (for example 3-yr revenue growth), never under the Bloomberg
  column's name.
- **One source per measure across a peer set wherever possible.** The Average / Median / Min / Max rows mix whatever
  sources the cells carry, so the table prints each summary's source mix beside it.

### 3.3 Preferred and Minority: one column, SA's `other_cap_struct`

It covers 12 of 18 rows. A missing value reads ABSENT with SA's reason, never zero -- zero would move EV and net debt.

---

## 4. What makes this run for a new security -- today and desired

| step | today | desired |
|---|---|---|
| 1. SA symbol | none on the Peers path | resolve our key to an SA slug. A resolver exists (`org/tier1_exec/4.0.0_SA_CRO/scripts/sa_symbol_resolve_pass.py`) with an ENTITY test: SA's company name must share a distinctive token with ours. It exists because `ROG` resolves to Rogers Corporation, not Roche, with a clean 200. Non-US names resolve through their US ADR. |
| 2. peer set | the scanner ranker, one run | SA suggested peers, 5 |
| 3. comparison data | 5 of 17 columns from the scanner | SA metrics plus the Bloomberg fill (s.2.1), each cell sourced |
| 4. grades | none | SA's factor grades, if the page shows them (a layout call, not a data gap) |
| 5. Peers V | ABSENT on 33 | computed over the SA set at the new floors |
| 6. trigger | the ranker ran once, by hand | the Peers stage runs as a step of instantiating the security |

---

## 5. The build, in dependency order -- round 14, after every panel brief is in

No item includes a fleet run; each is proven on the three validation names first.

1. **Contract.** R-1's ratified text says the comparable set is *"computed ... by ONE ranker over ONE database"*
   (`engine.py:11-16`, PRD v0.8). An SA-sourced set replaces that sentence. The Peers V floors change with it (s.3.1).
   Ratified text, so the CVO signs that half.
2. **SA symbol per security**, through the existing resolver's entity test. A slug that fails the test is UNRESOLVED
   with its reason, never the first hit.
3. **The existing REST module gains the Peers endpoints** -- the four GETs in s.2, all GETs (its residential proxy
   refuses POST, `rest_fetch.py:30`). It lands raw bytes the way it already does for its other endpoints, before any
   derivation. This is configuration on an existing module, not a new fetcher.
4. **Derivation to R-1:** SA peers, SA-shape columns, the Bloomberg fill with the fallback rule, and a source on every
   cell.
5. **Peers V** on the SA set at floors 5 and 5.
6. **The page renders SA's shape** -- the column set, per-cell source labels, and not-meaningful cells shown as such.
7. **Session health is a stop, not a retry.** A 403 carrying the challenge marker is `REHARVEST` (`detectors.py`), and
   the run STOPS; this path never signs in or launches the browser harvester.

---

## 6. Done means measured

| component | closed when |
|---|---|
| Peer sets | N of 33 with 5 SA peers; each missing name shows its reason (no SA symbol; no suggested peers) |
| Columns | 17 of 17 declared; per column, cells filled of rows, printed by source (SA / BBG / SA_FALLBACK) |
| Peers V | N of 33 with a score at floors 5 / 5; each ABSENT with its reason |
| Identity | every SA slug passed the entity test; the ROG-for-Roche case refused, as a positive control |
| Instantiation | on each validation name, Peers built with no hand step, or the exact step that stopped it |

---

## 7. Traps named in advance

- **A clean 200 is not the right company.** `ROG` is Rogers Corporation. The entity test comes before the peer call.
- **Never print, log or commit a cookie, proxy credential or session value**, and never read Andrew's HAR for anything
  but shape. The HAR contains his logged-in session.
- **Never sign in or run the harvester from the Peers path.** A REHARVEST stops the run and says so.
- **Label every fallback cell as what it is**, and never let a summary row hide a mixed source.
- **Do not treat a not-meaningful SA value as missing data to fill** from another source. Boeing's negative forward
  earnings are the fact.
- **Terms of use:** automated pulling from Seeking Alpha's API may run against its terms. That was raised to Andrew and
  is his call; this brief does not decide it.
- **No monitor or freshness checker** comes out of this brief.

---

## 8. What this brief does not ask for

No seat is re-tasked, no run is made beyond the 15 test GETs and one Bloomberg field search with a reference pull over
18 rows, and nothing was landed in any bucket. The test script, its request log and the response bodies sit in this
seat's session scratchpad, not the repo.
