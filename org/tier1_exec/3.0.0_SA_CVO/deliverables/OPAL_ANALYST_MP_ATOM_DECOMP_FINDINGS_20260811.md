# OPAL_ANALYST W0 — Model Portfolios atom_decomp: FINDINGS + SEMANTIC PASS

**Run:** `portal-page-portfolios__20260811T1640Z` · **Author:** `3.0.0_SA_CVO~Z` ·
**Certifier:** `1.0.0_SA_CTO~Z` (pending)
**Rectangle:** 16 entities × 10 fields = 160 cells — **158 MEASURED, 2 NOT_MEASURABLE, 0 validator violations**
**Status: `OPEN`. DRY is NOT established and is NOT claimed** (see §5).
**Charter + domain bar (fixed before measurement):** `OPAL_ANALYST_MP_ATOM_DECOMP_CHARTER_20260811.md`
**Method read (CTO~Z's ask):** `workflows/atom_decomposition/runs/portal-page-portfolios/20260811T1640Z/METHOD_READ.md`

> **What this run is:** Andrew delegated the semantics he would have written and ordered this seat
> to run atom_decomp on Model Portfolios itself *"so that we validate every little thing."* The MP
> census (@0c1dae3da) was **input**, never evidence: every factual cell was re-grounded on the live
> artifact or at source. **That re-grounding contradicted four census claims and found one live
> user-facing defect.**

---

## §1 — The ten findings

Ordered by consequence. Every one is source- or live-grounded; each names its instrument.

### 🔴 F-1 — A LIVE DEFECT: the Data Refresh page's "View Portfolios" button goes to Market Overview

`portal/src/pages/DataRefresh/components/PipelineProgress.tsx:432` renders
`<Link to="/model-portfolios">View Portfolios</Link>`. **That route does not exist.** The route is
`/portfolios` (`App.tsx:408`), and `App.tsx:470` is `<Route path="*" element={<Navigate to="/market" replace />} />`.

So the button labelled **View Portfolios** silently delivers **Market Overview** — no 404, no error,
and the sibling button directly above it goes to `/market` on purpose. **A user clicking either
button lands in the same place, and nothing tells them the second one failed.**

Blast radius is bounded and stated: `/data-refresh` is `requireAdmin`, so admin users only.
**Not fixed by this run** — CVO~Z authors no portal code; routed to CTO~Z for a one-line assignment.

*How it was found: the census records the page as `/model-portfolios`. Checking that string at
source found the route absent, and the same string live in a component.*

### 🔴 F-2 — An entire prefix is missing from the census denominator: `json/portfolios/**`

The census declares the MP vertical as **482 keys**. Live enumeration measured **487**.

`json/portfolios/**` — 5 keys, all MP-vertical by name and content (`aum-metrics.json`,
`account-distribution.json`, `aum-timeseries.json`, plus `49financial/` and `inflection/` siblings),
frozen 2026-05-29 → 2026-07-27 — **is absent from the census entirely.** It is a *third* legacy MDPF
tree beside `json/mdpf/**` and `platinum/mdpf/archive/**`.

**It was not found by re-counting.** A recount would have agreed with the census forever. It
surfaced by following a *consumer* edge (F-3) into a prefix nobody had named — Rule 7's frontier
expansion doing exactly its job, and the answer to the charter's own §6 question 1.

*Instrument: `aws s3 ls --recursive`, CLI auto-paginated, counted client-side (never `--query
length()`, never `--no-paginate`).*

### 🔴 F-3 — A live accessor points at a key that does not exist, and the census's explanation is wrong

`getNonModelAssets` (`portal/src/api/portal-proxy.ts:410-418`) is **live, uncommented code** whose
fetch targets `/api/general/portfolios/non_model_assets.json`. **That key does not exist**
(`aws s3 ls` → rc=1; positive control on `json/portfolios/aum-metrics.json` → rc=0, run as a
**separate invocation**).

The census says *"portal-proxy.ts:414 fetch is commented out."* At source, `:414` is a commented-out
**private-endpoint variant**; the live fetch at `:417` is active and mispointed. **Right verdict
(the artifact is unconsumed), wrong mechanism** — and the mechanism is what a future engineer acts on.

**Not a live bug today** — zero callers, so it never fires. It is a **loaded gun**: anyone restoring
the non-model panel wires up a function that fetches a missing key, and CloudFront error rules can
return HTML for a missing JSON key, so the failure would present as a **parse error, not a 404**.

### 🟠 F-4 — Two artifacts are frozen behind a `state: live` census row

`json/benchmarks/_smartx_model_daily.json` and `_smartx_model_monthly.json` were last written
**2026-06-01** (`as_of_date` 2026-05-29). Their four prefix-siblings were rewritten **2026-08-11**.
The census records both as `state: live`.

**Trading-calendar resolution applied first, per CLAUDE.md NEVER#1:** 71 calendar days, ~50 trading
days. This is not a weekend, not a holiday, not a T-1 frontier. It is a freeze.

Producer, source-confirmed: `data/smartx/scripts/pull_smartx_model_monthly_performance.py`
(`OUT_KEY` :98, `OUT_KEY_DAILY` :99) — **an operator-run script with an `--upload` flag, not a
scheduled Lambda.** Its vintage advances only when someone runs it, and nobody has since June 1.

**The freeze is invisible to every instrument pointed at this prefix:** nothing renders these, so no
user sees a stale number; the siblings refresh daily, so a *prefix-level* freshness read passes.
**A frozen key beside fresh siblings under one prefix is the shape a per-prefix check cannot see.**

**Disposition is `NOT_MEASURABLE` and deliberately left open** — two readings fit equally and have
**opposite** remedies: (a) the SmartX cross-check was retired in favour of the Yang design series →
decommission; (b) an operator step silently stopped → **restore**. The discriminator: a retirement
leaves a ruling, an omission leaves nothing. **Nothing is deleted** (Rule 9).

### 🟠 F-5 — The vintage-field zoo is at least 8 forms wide, not the 3 the registry design records

PRD §8.2 records the measured set as `{data_as_of, _provenance.source_vintages/as_of_last, as_of}`.
**Measured across MP alone this cycle:**

| form | artifact | grain |
|---|---|---|
| `_provenance.source_vintages.{k}` | platinum aum-metrics, account-distribution, non-model-assets | date |
| `as_of_last` | aggregate-aua-timeseries | date |
| `data_as_of` | 4 benchmark artifacts + peers | date / **month** |
| `as_of` | yang volatility | date |
| `as_of_date` | `_smartx_model_daily` | date |
| **`as_of_month`** | `_smartx_model_monthly` | month |
| **`value_date` + `assignment_date`** | cottonwood account-units | date (**two of them** — F-6) |
| `latest.date` (nested) | non-model-assets | date |

The v0.2 design already accepts a **dotted path** for `vintage_field`, which was the right call and
absorbs all of these unchanged. **What needs correcting is the recorded count** — a design
validated against 3 variants and deployed against 8 is validated against a denominator it does not
have.

### 🟠 F-6 — One artifact carries two semantically distinct as-of dates, four days apart

`platinum/mdpf/cottonwood/account-units.json` carries **`value_date` = 2026-08-07** (the as-of of
the unit values — **this is THE vintage**) and **`assignment_date` = 2026-08-11** (when model
assignments were applied), plus `generated_at` as a third date.

**Quoting `assignment_date` as the data date overstates freshness by four days.** This is the
sharpest vintage trap in the vertical, on the only artifact scoped to a single partner.

### 🟡 F-7 — The panel's displayed date is not the date of every number in the panel

The Portfolio Analytics panel renders **aum-metrics** (donut) and **account-distribution**
(histogram) side by side under **one footer date**. Measured today: aum-metrics data date
**2026-08-10**, account-distribution **2026-08-11**, and the footer stamps `as_of_last` from the
*aggregate timeseries* (**2026-08-10**) per the ~0345Z stamp law (`ModelPortfolios.tsx:1634-1645`).

**This is not a defect** — the stamp law is a deliberate Andrew-era ruling and its source comment
documents the off-by-one it fixed. **It is a semantic the Analyst must hold:** the date shown under
the histogram is not the histogram's vintage. Answers cite the artifact's own field, never the panel.

### 🟡 F-8 — The census field table omits the most-asked field on the vertical's first artifact

`aum-metrics.json` has **9 live top-level keys**. The census row enumerates **2** (`_provenance`,
`by_model`) and omits `total`, `last_updated`, `dates`, `period`, `scope`, `meta`,
`non_model_assets_detail`.

**`total` is the scope-wide AUM figure** — the single most probable question against this artifact
is not in its census row. Same class on `model_portfolio_benchmarks.json`: `etf_compositions`,
`index_compositions`, `model_names`, `model_source_note`, `source` are live and uncensused, and the
composition maps are exactly what answers *"what IS the benchmark"* — a question the census row
cannot currently support.

### 🟡 F-9 — The census denominator is a snapshot of a partly-unbounded set, stated as a fixed number

`platinum/mdpf/_manifests/` was **6 keys** at census time and is **10** now — it **grows on every
publish run** (4 runs on 2026-08-11 vs 1/day on 08-07…08-10).

So the fixed **482** will disagree with every honest future recount, forever, for a reason that is
not drift. **The fix is to declare the family unbounded, not to re-count it.**

### 🟢 F-10 — A NON-FINDING, recorded on purpose: `peer_performance` is healthy

`data_as_of` **2026-07-31**, object age 8 days. On a flat-hours instrument this reads as staleness.
Scored against its own cadence it is **correct**: the producer (`yang-generate-peer-performance`)
runs **only when a peer Excel is in the upload manifest** — month-end by construction, so a
month-old date is the normal healthy state.

This is CLAUDE.md NEVER#1 arriving inside the MP vertical. **It is recorded because a domain bar
that only ever produces findings is not a bar** — and because the next fourteen pages will each
contain one of these.

---

## §2 — The semantic pass (Andrew's 6 questions, answered in his stead)

All 16 items carry Q1–Q6 as MEASURED cells in `rectangle.final.json`, with evidence per cell and
provenance `CVO-DELEGATED` — **never "Andrew said"**. Serve verdicts:

**Machine-counted off `rectangle.final.json`, not tallied by hand — 3 SERVE / 6 SERVE-WITH-CAVEAT / 7 DENY = 16.**

| verdict | count | items |
|---|---|---|
| **SERVE** | 3 | aum-metrics · aggregate-aua-timeseries · etf_returns |
| **SERVE-WITH-CAVEAT** | 6 | account-distribution *(quote its own vintage, not the panel's)* · model_portfolio_timeseries + model_portfolio_benchmarks *(**model-DESIGN returns, never a client's realized return** — this caveat is not optional)* · peer_performance *(month grain)* · **+ the 2 riders below, which are SERVE-WITH-CAVEAT verdicts awaiting a widening confirm** |
| **DENY** | 7 | both `_smartx` *(frozen)* · non-model-assets *(superseded, 3 days older than the live source)* · `_manifests` *(publish times, not data dates)* · archive *(Andrew's 2026-08-06 exclusion)* · json/mdpf legacy *(superseded)* · yang volatility *(7 months stale, and its live successor has a near-identical filename)* |
| **of which RIDE TO ANDREW** | 2 | benchmark_returns · account-units — **§3** |

> *An earlier draft of this table put SERVE-WITH-CAVEAT at 4 by listing the two riders as a
> separate verdict class rather than as a subset of it. Caught by machine-counting the rectangle
> during the cycle-3 sweep. The riders are a **routing** state, not a verdict — so they are shown
> as a subset here, and the four rows no longer sum to more than sixteen.*

**Dispositions:** 9 keep-as-is · 1 consolidate (non-model-assets) · 2 decommission **candidates**
(json/mdpf legacy — teardown already parked; yang volatility + its uninvoked producer Lambda) ·
2 NOT_MEASURABLE (the `_smartx` pair) · 1 keep-frozen (archive) · **1 promote candidate**:
`benchmark_returns` is written daily by a live producer, consumed by nobody, and carries the only
plain-language benchmark definitions in the vertical — *the reflex on a zero-caller artifact is to
cut it; here the right move is to use it.*

---

## §3 — ⚠ TWO ITEMS RIDE TO ANDREW — one confirm, no work is held on it

**Widening the serving surface is Andrew-only by design** (PRD §4.4; the §8.2 capital-markets
precedent rode an *already-approved* row to him as a one-line confirm). My delegation covers
**semantics**, not **widening** — reading it wider would erase an existing control. So I answered
Q4 for all 16, and these two carry `CVO-RECOMMENDED — RIDES TO ANDREW`:

1. **`json/benchmarks/benchmark_returns.json`** — in the approved benchmarks channel and refreshed
   daily, but **rendered nowhere**. Serving it puts a figure in front of a user that appears
   nowhere in the portal. **Rec: SERVE for benchmark-composition questions** (its unique value),
   caveated as not-displayed.
2. **`platinum/mdpf/cottonwood/account-units.json`** — in the approved mdpf-platinum channel and
   current, but it is **per-account, single-partner** data with no visual site. **Rec:
   SERVE-WITH-CAVEAT** (Cottonwood-only; quote `value_date`, never `assignment_date`).

**Every DENY above needs no word** — a denial narrows and is fully inside the delegation.
**This is not a gate**: nothing is held on the answer, and W1 is unaffected.

**Why the split exists at all — the charter's Rule 24(iv) self-check:** my own field axis **fails
the state-coherence postulate**, and I named which values do not move. "CVO authors the semantics"
delivers Planes A and B entirely and **structurally cannot** deliver Plane C's widening subset. A
plan reading *"CVO~Z provides the semantics"* silently covers nine tenths of its own axis.

---

## §4 — Andrew's own words, and what changes for the Analyst

He said the semantics would be *"fairly obvious."* Mostly they were. **The three that were not**,
and that a reasonable person would have got wrong:

1. **`model_portfolio_timeseries` / `model_portfolio_benchmarks` are model-DESIGN returns**
   (`series_note`, the artifact's own text) — **not any client's realized return.** An Analyst
   answering *"how did the portfolio do"* from these, unqualified, gives a materially misleading
   answer to a wealth-management client. This caveat is load-bearing.
2. **`etf_returns` and its three benchmark siblings come from different pipeline branches**
   (model-PKL-only vs both-PKLs). A day when only the model PKL lands leaves `etf_returns`
   **fresher than its siblings** — a divergence the page cannot show and the Analyst must check
   per artifact, never per channel.
3. **`aggregate-aua-timeseries` carries `partner_custody_total` as 448 nulls at global scope** —
   present-but-empty. Key existence is not data availability (Rule 13).

**Registry impact (`DATA_CATALOG` v0.2):** all four fields §8.2 declares it will consume —
`semantics:`, `census_ref:`, `vintage_field:`, `vintage_grain:` — are produced by this run for all
16 items. **Two corrections land with them:** `census_ref` must point at **`/portfolios`**, not the
nonexistent `/model-portfolios` (F-1) — *otherwise the Analyst's visual-coordinate citation sends a
team member to a route that redirects to the wrong page* — and the vintage-variant set is 8, not 3
(F-5).

---

## §5 — Honest limits of this run

- **DRY is not established.** Cycle 2 changed two statuses and re-grounded three cells; a
  zero-change cycle 3 is owed. `run.json` status is `OPEN` and says why. **Declaring DRY here would
  be a count target wearing a convergence label.**
- **Cycle 1 produced 160/160 MEASURED — and that was itself the smell.** Re-reading it against the
  domain bar found two cells whose *value* was "unresolved" while their *status* said MEASURED — a
  hole wearing a measured label, invisible to the one instrument whose job is seeing holes. Both
  were self-caught, not certifier-caught. The cycle-1 → cycle-2 delta is the most honest signal in
  this run.
- **Single-author population.** Rule 14(c)'s fan-out is prohibited by `org/XXX.md`'s agent ban;
  every cell has one author, so the whole independence burden sits on the certification pass
  (METHOD_READ M-1).
- **⛔ `rectangle.final.json` contains one deliberately planted false cell** (Rule 14(e), sealed at
  plant time in `MUTANT_SEALED.md`, committed with the rectangle). **It must not be consumed as
  SSOT.** A `c3` correction patch is owed the moment the verdict is written; the consumable artifact
  is `rectangle.final.certified.json`.
- **Instrument limits, disclosed:** `comp-routes` is DESIRED-plane only and was never allowed to
  carry a verdict alone; `comp-estate`'s freshness claims are snapshot-vintage and **were stale**
  against my live reads (it reported 2026-06-15 for a file rewritten 2026-08-11) — it was used for
  topology only; every ABSENT verdict carries a positive control run as a separate invocation.
- **Not in scope:** no portal code was changed, no key deleted, no allowlist widened, no gate
  created. F-1's fix is CTO~Z's to route.

---

## §6 — What I recommend next (recommendations, not dispatches)

| # | item | owner |
|---|---|---|
| 1 | **F-1 one-line fix**: `PipelineProgress.tsx:432` `/model-portfolios` → `/portfolios` | CTO~Z to route |
| 2 | Certification pass + the `c3` mutant-correction patch | CTO~Z, then me |
| 3 | Route the four census corrections (F-1, F-3 mechanism, F-4 state, F-8 fields) back to the census owner | 0.5.0_AE_OpalETL~Z |
| 4 | `json/portfolios/**` (F-2): census it, then dispose — a third legacy tree nobody was tracking | 0.5.0 / CTO~Z |
| 5 | Resolve the `_smartx` owned unknown before anyone proposes a disposition | 0.5.0 |
| 6 | Six METHOD_READ fixes into SKILL.md **before W1**, so 0.5.0 does not hit them fourteen times | CTO~Z (method owner) |
| 7 | The two Plane-C confirms (§3) | Andrew, one line |
