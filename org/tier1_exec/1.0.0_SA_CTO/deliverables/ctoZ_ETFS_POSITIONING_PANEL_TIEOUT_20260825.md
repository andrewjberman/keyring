# ETFS Positioning: why the two panels did not tie -- and which one was lying

**archetype:** DIAGNOSE
**Seat:** `1.0.0_SA_CTO~Z` | **Date:** 2026-08-25 | **Fix:** portal `a00e67cc` (LANDED LOCAL on portal DEV, rides the integration window)

## The ask

ANDREW-DIRECT 2026-08-25 at the CTO~Z terminal, VERBATIM (the operative clause):

> "in the 'Holdings Breakdown' it seems like we have every exact equity versus fixed income (usually one
> MMKT or UST cash-equivalent holding) and it adds to 100% within 2bps. However if you look at the
> 'Positioning Summary' at the top of the page, the numbers are different and they resolve 50bps or more
> from 100%, which does not make sense and needs to be investigated because all these numbers need to tie.
> I need you to investigate, figure out what needs to be fixed here, fix it, validate the fix, and have
> 0.2.0_DT_PortfolioAnalytics~Z to come in and run the /prod-deploy then smoke and validate those numbers."

## The finding INVERTS the natural reading

The reasonable prior -- the one in the ask, and the one I started with -- is that the bottom panel is
right (it foots to 100) and the top panel is broken (it does not). **It is the other way round.**

Both panels read the SAME artifact. The top renders it faithfully. The bottom was **editing it**.

`HoldingsTab.tsx:880-887` (@ `f67b3a48`) ran:

```
proportionalRound(attributionHoldings.map(h => h.weight), 100.00, 2)
```

and then summed the panel's asset-class subtotals from those **rewritten** weights (`:1251`). The target
was a hardcoded `100.00`. `PositioningSummary` renders the book-level `allocation` object unmodified.

**So the bottom panel footed to ~100% BY CONSTRUCTION. It could not have reported a book that does not
sum to 100 -- which is exactly the condition worth seeing.** That is the "instrument that could not have
said otherwise" class in `docs/doctrine/CONTROLS_OVER_CARE.md`, sitting on a client-facing page.

## Measurement -- the served artifact, not the types

`s3://opal-data-portal-v2/platinum/etfs/positioning_data.json`
`generated_at 2026-08-25T13:01:21Z` | `data_as_of 2026-08-24` | ETag `b3e1ad04fd15c6f560e1ae6bd97d8b60`

| book | `allocation` sum | holdings sum | artifact DIFF | panel disagreement (FI / EQ) |
|---|---|---|---|---|
| DIVZ | 99.80 | 99.80 | **0.0000** | 0.00 / -0.20 pp |
| IDVZ | 99.51 | 99.51 | **0.0000** | 0.00 / -0.38 pp |
| PFDE | 100.01 | 100.01 | **0.0000** | 0.00 / +0.01 pp |
| PFOE | 99.99 | 99.99 | **0.0000** | 0.00 / -0.01 pp |

**The artifact's two sources agree EXACTLY, every book.** The entire disagreement was manufactured at
render. Denominator: 4 of 4 books in the artifact, no sampling.

Two further properties of the plug, both worse than the tie-out itself:

1. **It rewrote client-facing security weights.** 39 of IDVZ's 44 rows and 20 of DIVZ's 29 displayed a
   weight that was not the reported weight (rendered SALXX 0.90 against a reported 0.89; JD 1.53 against
   1.52; and so on down the table).
2. **It was silently partial.** The distribution loop is bounded by `i < indices.length`, so a gap wider
   than the holding count can never close. IDVZ needed 54bp of plug against 44 rows and landed at 99.90
   while declaring a 100.00 target.

## Why the books do not sum to 100 -- upstream, and NOT fixed here

`s3://opal-data-etfs/silver/holdings/2026-08-24.parquet` sums to 99.80 / 99.51 / 100.01 / 99.99 for the
four books. `etf_positioning_gold.py` drops nothing -- it iterates every source row for the fund.

The discriminator is the **vendor**, and it is visible in the data:

| feed | books | residual line | book sums to |
|---|---|---|---|
| filepoint | PFDE, PFOE | emits `Cash&Other` (`is_cash=True`) | ~100.00 |
| trueshares | DIVZ, IDVZ | **none** -- cash sleeve is SALXX, a real MMKT security | 99.80 / 99.51 |

So DIVZ and IDVZ genuinely account for only 99.80% / 99.51% of NAV. The 20bp / 49bp residual is real
(uninvested cash, receivables/payables) and the Polen feed simply does not report it as a row.

**That is a PRODUCER question in the DS lane, and it is carded to Andrew rather than plugged.** Synthesising
a residual holding row is a client-facing data-product decision with a live basis question (weight-space
residual vs a NAV recompute -- the two disagree here: 99.815% by market value against 99.80% by reported
weight for DIVZ). It belongs in gold beside the vendor's own sentinel, never at the render.

**After this fix the page SHOWS the gap instead of smearing it across the equity holdings.** That is the
point, not a side effect.

## Validation

| rung | instrument | result |
|---|---|---|
| DESIRED | `tsc -b --noEmit` | rc=0 |
| DESIRED | `eslint HoldingsTab.tsx` | rc=0 |
| EXERCISED | `ui-smoke.mjs positioning --click ETFs --click "Expand Details" --click IDVZ`, fixtured with the REAL served bytes | BEFORE: summary FI `0.89` vs breakdown FIXED INCOME TOTAL `0.90`. AFTER: **both `0.89`**; equity rows return to reported weights |
| DATA | post-fix recomputation, both panels, all 4 books | tie at display precision, 4/4 |
| BLAST RADIUS | models family, every book x every period (UST/ST/INT/LT/ULT/AGG x current/qtd/ytd/1y/si) | already sums to **exactly 100.000000** -> the plug had nothing to redistribute -> **DELTA=0 for models** |

**The first render I took was the FAILURE state and I discarded it.** Both live legs return 401 without a
real bearer, so the unfixtured page renders "ETF positioning data could not be loaded" with both panels
empty -- a render that proves nothing while looking like a render. Fixturing the real served bytes exercises
the aggregation code, which is the thing under test.

## State

- Portal `a00e67cc` -- **LANDED LOCAL on portal DEV**, tree clean. My push is correctly BLOCKED by LD-0367
  (integrator-only); I did not override. Asked `0.0.0_AB_MSTR~Z` to push it in the integration window.
- `/prod-deploy` + smoke is `0.2.0_DT_PortfolioAnalytics~Z`'s per Andrew. **That seat is not live** (the
  fabric has been dark since ~09:08Z); spawn requested from MSTR~Z.
- **OPEN CARD AT ANDREW:** whether the DIVZ/IDVZ NAV residual gets an explicit producer-side cash row.
  My rec: **yes, in gold, weight-space residual, reusing the existing `Cash&Other` sentinel shape** -- but
  it changes what a client sees, so it is his call and DS's build, not mine to ship inside a render fix.
