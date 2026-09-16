# Andrew-direct 2026-09-15 ~18:2xZ, at the `1.0.0_SA_CTO~W` terminal: the Peers tab's universal score -- peer-relative valuation, verbatim

**Recorded by:** `1.0.0_SA_CTO~W`. **Channel:** direct message in this Claude Code session, arriving mid-turn while this seat measured the
Bloomberg sourcing for Robustness and the Mgmt tab; exact arrival timestamp unavailable (the surrounding clock read is 18:26:44Z).
**Project:** AMGT_RESAPP. **Descends from:** the one-standardized-metric-per-tab principle (record
`ANDREW_DIRECT_20260915_174xZ_ONE_STANDARDIZED_METRIC_PER_TAB_ABSOLUTE_AND_POOL_PERCENTILE.md` @`4eef3ae75a`) and the Robustness model
(record `ANDREW_DIRECT_20260915_181xZ_THESIS_RISK_TAB_SCORE_IS_ROBUSTNESS_FACTOR_MODEL.md` @`260402c006`, follow-on @`3f9481ea12`).

## Verbatim, entire (layout preserved)

> below is a summary on how we should process the "peer" score: What this produces
> A single signed number per name: how cheap or expensive it sits against its own ranked peer set, in peer-set standard deviations. Negative means expensive, positive means cheap.
> Everything is yield-form, following the house convention — it keeps the sign correct through zero for unprofitable names, and averaging yields is equivalent to harmonic-mean averaging of the corresponding multiples, which is the right operation for comparables. Six measures, equal weight, no sleeve tilt. Two of them are EV-denominated to neutralize the leverage effect that would otherwise make indebted peers screen cheap on every equity-level yield.
> Two nested rankings: the z-score is computed inside the peer set, and only then is the result percentile-ranked across the universe. The inner step asks whether the name is cheap relative to who it should be compared to; the outer step asks how unusual that degree of cheapness is.

```
Plain Text
MEASURES (m = 1…6, all yield-form, all NTM where estimates exist)
  m   y_m                                   denominator
  1   FCF / market cap                      equity
  2   NTM earnings / price                  equity
  3   (dividends + buybacks) / market cap    equity
  4   EBITDA / EV                            enterprise
  5   sales / EV                             enterprise
  6   NTM EPS growth / NTM P/E               equity   [inverse PEG]
  all y_m: higher = cheaper

PEER SET
  K = ranked peers from similarity function,  require |K| ≥ 8
  subject excluded from K

PER MEASURE m
  1.  winsorize y_m over K at p5 / p95
  2.  μ_m = median( y_m | K )
      σ_m =     sd( y_m | K )
  3.  z_m = ( y_m,subject − μ_m ) / σ_m

AGGREGATE
  V = ( 1/|M| ) · Σ_{m ∈ M} z_m
      M = measures available for both subject and ≥6 peers
      require |M| ≥ 3

GUARDS
  σ_m = 0 or |K_m| < 6        drop m from M
  |M| < 3                     suppress V; show raw table only
  |K| < 8                     suppress V; show raw table only
  EBITDA ≤ 0                  drop m = 4
  NTM EPS growth ≤ 0          drop m = 6

CROSS-SECTIONAL
  P = pctile_rank( V | sector )
  R = residual of P on prior factors in orthogonalization order
```

## Read narrowly

- **RULED:** the Peers tab's universal score is V, a peer-relative valuation z-score averaged over six yield-form measures at equal weight;
  it is the tab's standardized metric under the per-tab principle (the absolute figure V; the relative figure P).
- **RULED -- THE PEER SET:** K is the ranked peer set from the similarity function (R-1's served peers on this page), subject excluded, at
  least 8 members; below 8, or below 3 usable measures, V is suppressed and the raw table shown alone.
- **RULED -- THE TWO RANKINGS:** the z-score is taken inside the peer set; only the result is percentile-ranked, and that percentile is
  written `| sector`. This seat does not reconcile it with the ~17:5xZ pool word (the analyzed companies); the same question stands open on
  the Robustness model and goes to the addendum as one question for both.
- **NOT RULED HERE:** the data source for the six measures (the ~18:2xZ "all from Bloomberg" word named the Robustness score, and this
  seat does not widen it silently -- Bloomberg is measured first because it is the house source and R-1's CSC columns already carry
  Bloomberg codes); the orthogonalization order; which of V, P and R the page displays; the winsorization when K is small (p5/p95 over
  8-12 members moves at most the single extreme member).
- **WHERE IT LANDS:** the round-11 L10 addendum, beside candidate 13 (C-TAB-METRIC) and candidate 14 (Robustness), as candidate 15 --
  the Peers tab's metric definition. The specification is frozen mid-round.

## Broadcast

One message to `2.0.0_SA_COO~W`, `3.0.0_SA_CVO~W`, `4.0.0_SA_CRO~W` and `0.0.0_AB_MSTR~Z`. Push state: LOCAL.
