# W5 LIFT CONSTRAINTS — the CVO~Z rulings that bind `DATA_CATALOG` v0.2

**Author:** `3.0.0_SA_CVO~Z` · opened 2026-08-11 ~1910Z · **cumulative, extended per page, rows never deleted**
**Authority:** Andrew-direct 2026-08-11 ~1020Z (delegated semantics) + PRD §9.3 (the semantics pen) — the same delegation that produces the semantic cells produces the constraints on how they may be consumed.
**Coverage:** W0 `/portfolios` + W1 pages 1–4 (`/cma`, `/positioning`, `/attribution`, `/factor-tilts`). **Two pages outstanding** (`/valuations`, `/correlations`), then W2–W4.

> **WHY THIS FILE EXISTS.** Every ruling below is currently buried in the certification of the page
> that produced it. W5 would have to re-mine five files to find them, discover them by hitting them,
> or ship without them — and the third is the likely one, because a constraint nobody knows about
> looks exactly like an absence of constraints. **This is the same records-colocation logic CTO~Z
> applied to the vintage-role register**: the register belongs where the run is READ, and so do the
> rulings. Nobody asked for this file; it is owed by the pen that wrote the rulings.
>
> ⚠ **IT IS A REGISTER, NOT A GATE.** It blocks nothing. It is the list W5 should be able to check
> itself against, and its failure mode is being out of date — so it carries its coverage line above,
> and I re-read prior pages when I extend it rather than appending blind.

---

## L-1 — Rows key on the FULL KEY PATH. Never a basename.
**Binding.** Origin: `/positioning` R3, widened at `/attribution` R3, third instance at `/factor-tilts`.

`json/portfolios/aum-metrics.json` and `platinum/mdpf/{scope}/aum-metrics.json` **share a basename and
are different artifacts** — different tree, producer, vintage and field set. A basename-keyed row
silently merges them, and **the Analyst would answer Model Portfolios questions from a legacy artifact
last written 2026-07-23.**

- Both rows carry an **explicit mutual disambiguation note** naming the other.
- **One artifact = ONE row**, regardless of how many pages render it. Page coordinates are a **LIST on
  that row**, never N rows. *Measured: `json/portfolios/aum-metrics.json` appears on THREE pages
  (`pos.03`, `att.03`, `ft.04`) with a different role on each — reported summary, AGG weighting input,
  scale context. Without this, one key acquires three semantic rows and an Analyst can get three
  answers for one object.*

## L-2 — The row carries the ACCESSOR SET as a list.
**Binding.** Origin: `/factor-tilts` R2 / K9.

One artifact is reached by `getAUMMetrics` from `@/api/endpoints/aum` on `/factor-tilts` and by
`getAUMSummary` from `@/api/portal-proxy` on `/positioning` and `/attribution`. **One artifact, two
accessors, two modules.** A per-page consumer count summed across pages **double-counts it** — and
under M5 a consumer count is what authorises or forbids a decommission.

*Latent hazard, recorded and correctly NOT scored: two paths to one artifact can diverge in caching,
auth or error handling without either page's authors noticing.*

## L-3 — ⛔ NEVER fall back to the footer for vintage. Some artifacts carry no vintage field at all.
**Binding, and this is the one that would reproduce a live defect inside the Analyst.**
Origin: the vintage-role register, W5-constraint half, bound in the PRD.

`json/portfolios/aum-metrics.json` has **no `data_as_of` field**; its vintage is `period`. A catalog
keyed on a uniform vintage field name finds nothing, and the natural fallback — read the displayed
date — **imports the display-vintage defect straight into the answering layer.**

- `vintage_field` is **per artifact** and accepts a **dotted path**.
- An artifact with no vintage field gets its vintage field named explicitly, or the row is incomplete.
- **The footer is never a vintage source.** 13 measured members across 5 pages say so.

## L-4 — The measured vintage-field variant set is at least EIGHT forms, not three.
**Correction to a recorded figure.** Origin: W0 F-5.

PRD §8.2 records `{data_as_of, _provenance.source_vintages/as_of_last, as_of}`. Measured across the
MP vertical alone: `_provenance.source_vintages.{k}` · `as_of_last` · `data_as_of` · `as_of` ·
`as_of_date` · **`as_of_month`** · **`value_date` + `assignment_date` (two, meaning different things,
four days apart)** · `latest.date` (nested) · and `period` with no `data_as_of` at all.

The dotted-path design absorbs all of these unchanged — **the design is right and the recorded count
is wrong.** A design validated against 3 variants and deployed against 8+ is validated against a
denominator it does not have.

## L-5 — `census_ref` points at `/portfolios`. The route `/model-portfolios` DOES NOT EXIST.
**Binding.** Origin: W0 F-1.

The MP census recorded the page as `/model-portfolios`; the real route is `/portfolios`
(`App.tsx:408`), and `App.tsx:470`'s catch-all silently redirects to `/market`. **A `census_ref`
carrying the wrong route does not fail — it sends a team member somewhere plausible and wrong.**

*The same string is also live in a component (`PipelineProgress.tsx:432`), which is the routed
frontend defect. The catalog must not inherit it.*

## L-6 — Consumer counts on `/cma` and `/positioning` are ACCESSOR-GRAIN. Re-derive before any decommission.
**Binding, and it is a flag against my own signed certifications.** Origin: K8, filed at `/attribution`,
bound in PRD §9.6.

K8 (*a consumer count is per CALL SITE, not per accessor*) arrived at page 3. My `/cma` and
`/positioning` certifications accepted **accessor-grain** counts. I did not re-open those runs — but
an accessor-level count **averages a load-bearing call site with a payload-discarding one into a number
true of neither**, and under M5 that number authorises deletion.

**No decommission may be proposed from a `/cma` or `/positioning` consumer count without a per-call-site
re-derivation.** *(Measured specimen: one accessor, load-bearing at `Attribution.tsx` and discarding a
~7.8KB payload at `SelectionTab.tsx` — a fetch whose only effect is `setIsLoading(false)`.)*

## L-7 — Semantics provenance is `CVO-DELEGATED` with a date. Never "Andrew said".
**Binding.** Origin: PRD §9.3 + every semantics payload.

Andrew's own recorded verbatim semantics, where they exist, **outrank a delegated one and are marked as
his.** Everything I authored carries evidence class DECISION with the delegation record as locator.

## L-8 — Serve verdicts travel WITH their caveats. Several caveats are load-bearing, not decoration.
**Binding.** Origin: all five pages.

A verdict lifted without its caveat is a different verdict. The ones that change an answer's truth:

| artifact | caveat that must travel |
|---|---|
| `model_portfolio_timeseries` / `_benchmarks` | **model-DESIGN returns, never a client's realized return** |
| `json/capital-markets/assumptions.json` | **forward-looking ASSUMPTIONS, not realized returns** |
| `json/capital-markets/views.json` | quote 2026-01-09 — and **the screen shows 2026-12-31, so the Analyst must contradict it** |
| `platinum/mdpf/cottonwood/account-units.json` | quote `value_date`, **never `assignment_date`** (4 days apart, different meanings) |
| `json/portfolios/aum-metrics.json` | **never answer a Model-Portfolios AUM question from it** (L-1) |
| factor-tilt tiers | **a tilt is a relative position** — not a holding, not a return |

## L-9 — TWO MP rows hold pending Andrew. The other fourteen lift immediately.
**Not a defect; a routing state.** Origin: W0 §3.

`json/benchmarks/benchmark_returns.json` and `platinum/mdpf/cottonwood/account-units.json` carry
`SERVE-WITH-CAVEAT — CVO-RECOMMENDED, RIDES TO ANDREW`, because answering them SERVE would **widen** the
serving surface, and widening is Andrew-only by design (PRD §4.4). **Nothing is held on it and it is
not a gate** — W5 lifts 14 of 16 MP rows now and holds 2 for a one-line confirm.

## L-10 — The vintage-role register lifts mechanically. Do not re-mine the rectangles.
**Binding.** Origin: CTO~Z direction 182858Z, PRD §9.9 item 5.

13 measured members across 5 pages, cumulative, in the latest certification. It carries the delta
convention, the four agreement sub-shapes, and the members whose absence would otherwise be invisible
(the coincidental and correlated-but-unwired agreements — nothing looks wrong at the site of them).

---

## What five pages of measurement have SETTLED, for whoever designs the answering layer

**The displayed vintage is not bound to the artifact it describes.** That is the whole class, and it is
now the only surviving framing — five pages eliminated the others by measurement, not by argument:

- **Not staleness.** On `/factor-tilts` the same footer key is *simultaneously* correct for three
  artifacts and wrong for a fourth by nineteen days.
- **Not a footer bug.** `ft.04` is mis-presented **with no footer at all** — through the page-level date
  registration.
- **Not direction-dependent.** I recorded an overstatement asymmetry across seven members; CTO~Z bound
  it as a design input; `att.01` falsified it at member nine by running **ten days behind**. *Struck,
  with the falsification beside it. It was mine, and a remedy scoped to "stop showing stale dates"
  would miss it entirely.*

**Consequence for W5:** every served answer states the vintage **from the artifact's own field**, names
that field, and never inherits a page-level or panel-level date. Where the artifact has no vintage
field, the row says so explicitly (L-3).

---

*Extended at each certification. Coverage line at the top is authoritative — if it does not name a
page, this file does not cover it.*
