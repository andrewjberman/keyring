# ANDREW-DIRECT 2026-08-24 ~21:5x-22:00Z -- PULL THE "AGG" VIEW FROM THREE PORTAL PAGES; BUILD A TOGGLE-PERSISTENCE PATTERN

**Received at:** `1.0.0_SA_CTO~X` terminal, 2026-08-24 (recorded 22:00:58Z)
**Channel:** direct, at this session's terminal
**Record duty:** CLAUDE.md / XXX.md "Andrew-direct instructions -- RECORD + BROADCAST, same turn"
**Broadcast:** COO + CVO + MSTR, same turn (CRO seats remain off-limits to this session per the 2026-08-24 ~19:36Z instruction)

---

## 1. THE INSTRUCTIONS, VERBATIM

Delivered across four messages in one exchange. Quoted exactly; the phrasing IS the ruling.

**(a) The concern that opened it:**

> "In essence, what my concern is here is that the "Agg" view is somehow tied to Opal's aggregate models
> somehow as opposed to the Advisor's aggregate Opal Model exposure, which would be a problem. The simple
> answer almost certainly is going to be just getting rid of "Agg" views in both "Positioning" and
> "Attribution" and "Factor Tilts" pages. Additionally, we should have some kind of short-term local cache
> where toggle state on "Positioning" is remembered within the user session."

**(b) The decision, after the measurement was reported:**

> "Yeah I had a feeling that was the case. I think the easier solution here is simply just pulling "Agg"
> toggle view from those three pages ("Positioning" "Attribution" and "Factor Tilts") nobody cares about
> this view and its more trouble than its worth."

**(c) The second deliverable, stated as a PATTERN and not a one-off:**

> "Also we want to get that subtle local/client-side browser cache mechanism with the toggles set up in
> Positioning (and define this mechanism as a pattern because we may want to implement it elsewhere in the
> Portal on key toggles)."

**(d) The routing instruction that produced the finding (same session, earlier):**

> "Try comp-trace comp-cache etc there should be some portal comp-tool solutions for this exact things"

and

> "See if any of those work, also check typscript main positioning page files and check to see if there is
> some client-side logic that isnt in the server for this as well."

---

## 2. WHAT WAS MEASURED (the finding his concern was tested against)

**His hypothesis was CORRECT.** Source-confirmed and exercised against live served artifacts.

### 2a. The mechanism -- SOURCE-CONFIRMED

`infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-positioning/lambda_function.py`
@ `69b867c4eb` (2026-08-18):

- `:1180 calculate_aggregated_holdings(model_holdings, aum_data, etf_lookup)`
- `:1193 total_aum = sum(aum_data.values())`
- `:1213 model_weight_in_agg = model_aum / total_aum`
- `:1218 contributed_weight = weight_in_model * model_weight_in_agg`

`aum_data` is loaded at `:1076 load_aum_data()`, `:1114-1125` -- from
`s3://opal-data-portal-v2/json/portfolios/aum-metrics.json`, field `by_model[].aum`.

### 2b. That artifact is FIRM-WIDE AND CROSS-PARTNER -- live read 2026-08-24

`s3://opal-data-portal-v2/json/portfolios/aum-metrics.json` (period 2026-07-22, quarterly anchors
q0=2026-06-30):

- `total.aum` = **$1,951,676,164.42**, `total.account_count` = **7,854**
- `meta.fee_basis_components` decomposes that total into **THREE PARTNER FIRMS**, summing EXACTLY to it:
  - `49financial` $1,689,302,889.53 (fee_scope `full`, basis schwab-rps)
  - `inflection`  $137,997,265.16  (fee_scope `model`, basis eclipse+orion)
  - `cottonwood`  $124,376,009.73  (fee_scope `model`, basis bd-rebalancer-models + bd-datamining-values)
- Token census over the whole artifact: `advisor` = **0**, `adviser` = 0, `rep_code` = 0, `household` = 0,
  `tenant` = 0, `account_id` = 0.

**There is no advisor dimension and no per-firm split in the weighting. There is one global number.**

### 2c. Exercised end-to-end against the SERVED positioning artifact

`s3://opal-data-portal-v2/json/positioning/positioning_data.json` (gzip-encoded, 8,133 bytes on the wire /
73,458 decompressed; `generated_at` 2026-08-22T11:06:02Z, `data_as_of` 2026-08-21 = Friday, i.e. correct
T-1 on a Monday -- NOT a staleness finding, NEVER#1 resolved before saying so):

`current_holdings.AGG.total_aum` = **$1,637,144,180.01**, 30 holdings, weights summing to exactly 1.0.
The per-model `aum` values carried in that artifact are byte-identical to `aum-metrics.json` `by_model`:

| model | aum in positioning_data.json | implied AGG weight |
|---|---|---|
| UST | 52,360,822.93 | 3.20% |
| ST | 129,227,888.01 | 7.89% |
| INT | 444,315,640.92 | 27.14% |
| LT | 804,605,507.26 | **49.15%** |
| ULT | 206,634,320.89 | 12.62% |

**So the "Aggregate" an advisor sees is Opal's own book, pooled across 49 Financial + Inflection +
Cottonwood.** Nearly half of every AGG weight is Long-Term Conservative because that is where Opal's
firm-wide dollars sit. An advisor whose entire book is Short-Term sees an "Aggregate" that is 49% LT and
3% ST. It is not their exposure and was never computed from it.

### 2d. Two further defects found in the same trace (recorded, NOT remediated)

1. **Silent denominator truncation.** `aum-metrics.json` `by_model` carries **7** models; the producer's
   `model_name_to_code` map (`:1090-1105`) covers only 5. `Opal Blend 5050 Int Ltc` ($32,065,435 / 155
   accounts) and `Opal Blend 5050 St Int` ($7,284,200 / 24 accounts) map to nothing and are dropped from
   both numerator and denominator. The survivors still normalise to exactly 1.0, so the truncation is
   invisible on screen -- a confident wrong number, not a gap. This is the hazard already documented at
   `portal/src/pages/Positioning/shared/bookSet.ts:36` and
   `portal/src/pages/Positioning/tabs/HoldingsTab.tsx:41-51`, now MEASURED live.
2. **THREE independent implementations of one concept**, two of them client-side and invisible to the
   server (this is the "client-side logic that isnt in the server" he asked me to look for):
   - **Positioning** -- renders the SERVED `current_holdings.AGG`. It ALSO carries a client-side
     AUM-weighted AGG builder (`HoldingsTab.tsx:53-60` `aggregateWeighting`, called at `:765` and `:885`)
     that is **unreachable dead code**: `selectedPeriod` is a `const 'Current'` at `:601` with no setter,
     and both call sites sit behind `selectedPeriod !== 'Current'`. `aumByModel` is fetched every mount
     (`:643-688`) and never used.
   - **Attribution** (`src/pages/Attribution/tabs/SelectionTab.tsx:53, 87, 128-129, 210-211`) -- computes
     AGG **client-side** from the same AUM map. Live.
   - **FactorTilts** (`src/pages/FactorTilts/constants.ts:178-339 computeAggregateMetrics`, wired at
     `FactorTilts.tsx:104-118`) -- computes AGG **client-side**, and AGG is the DEFAULT scope
     (`FactorTilts.tsx:56`).
3. **The client-side path reads the PUBLIC endpoint.** `getAUMSummary()`
   (`src/api/portal-proxy.ts:281-289`) is marked "DEMO MODE" and calls the general/unauthenticated
   `/api/general/portfolios/aum-metrics.json`, with the firm-scoped private endpoint
   (`/api/private/portfolios/aum-summary.json`) commented out. Firm-scoping was already switched off here.

---

## 3. WHAT THE INSTRUCTIONS AUTHORIZE

**AUTHORIZED, explicitly:**
- Remove the "Agg" toggle VIEW from **Positioning**, **Attribution**, **Factor Tilts** (his (b), naming all
  three pages).
- Build the client-side/browser toggle-state cache on **Positioning**, and **define it as a reusable
  pattern** for other key Portal toggles (his (c)).

**NOT AUTHORIZED BY THESE WORDS -- do not widen:**
- Removing or altering the PRODUCER's AGG block. He said pull the *toggle view*. `current_holdings.AGG`
  is served output; changing it is NEVER#3 territory and needs its own word. Leave the producer alone.
- Touching the **AGG ETF ticker** (iShares Core U.S. Aggregate Bond). It shares the string `AGG` and
  appears throughout benchmark composition (`lambda_function.py:157, 170, 596, 1009`, `BenchmarkHeatmap.tsx`,
  etc.). A string-matched removal would break benchmarks. The view-vs-ticker discrimination is
  load-bearing and must be made per call site, not by grep.
- Any other page's AGG (`TradeSubmission/tabs/HistoryTab.tsx`, `ModelPortfolios.tsx`, market-performance,
  Macroeconomics) -- he named three pages.

---

## 4. OPEN PROCESS QUESTION (surfaced, not self-adjudicated)

CLAUDE.md Rule 27 runs every new directive through register -> PRD -> COO atom-decomp -> TOs -> CVO
proof-of-spec. This arrived as a direct, scoped, two-part portal change at a CTO lane terminal. **I am not
manufacturing a gate on it** (the no-inferred-gates rule binds), and I am not deciding the pipeline
question myself. Recommendation stated to him: run it as one registered project with a short PRD, because
the toggle-persistence half is explicitly a REUSABLE PATTERN and patterns are exactly what the decomp
stage exists to pin. His call.

---

## 5. RECORD

- Finding + mechanism: this document.
- Instruments used: `comp-which` (routing), `comp-find` / `comp-find --name` (census, denominators
  printed), `comp-platinum page Positioning --firm bd`, `comp-trace`, live `aws s3 cp` reads of both
  served artifacts with the gzip encoding resolved.
- `comp-platinum page Positioning --firm bd` returned **"No fetches detected in this component"** -- a
  clean, well-formed, and MISLEADING zero: `Positioning.tsx` delegates every fetch to its panels and tabs.
  Recorded as a comp-tool coverage gap, not quoted as evidence of absence.
