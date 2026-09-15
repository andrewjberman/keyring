# Andrew-direct 2026-09-15 ~18:1xZ, at the `1.0.0_SA_CTO~W` terminal: the Thesis/Risk tab's universal score is ROBUSTNESS -- the factor model, verbatim

**Recorded by:** `1.0.0_SA_CTO~W`. **Channel:** direct message in this Claude Code session; exact arrival timestamp unavailable
(after 18:04Z by the surrounding tool reads). **Project:** AMGT_RESAPP. **Descends from:** the one-standardized-metric-per-tab principle
(record `ANDREW_DIRECT_20260915_174xZ_ONE_STANDARDIZED_METRIC_PER_TAB_ABSOLUTE_AND_POOL_PERCENTILE.md` @`4eef3ae75a`).

## Verbatim, entire (the model's layout preserved)

> I want to show you something, i am building out factor models/methodologies that we can use for the universal "scores" per tab.
> For Thesis/Risk, it should be Robustness, i have the information here for the related model:

```
CONSTRAINTS (universal, n = 6)
 
  i   metric x_i                        s_i   g_i      t_i
  1   EBIT / interest expense           +1    ln       covenant, else 2.0
  2   net debt / EBITDA                 -1    ln       covenant, else sector ceiling
  3   (cash + revolver) / 24m obligs     +1    ln       1.0
  4   debt maturing ≤24m / total debt   -1    logit    0.25
  5   FCF / revenue  (TTM)              +1    identity 0.0
  6   largest customer / revenue        -1    logit    0.20
 
 
TRANSFORMS
 
  identity   g(x) = x
  ln         g(x) = ln(x)
  logit      g(p) = ln( p / (1-p) ),   p clamped to [0.005, 0.995]
 
 
PER CONSTRAINT i, PER NAME
 
  1.  x_i,q  for q = 1…8          8 TTM observations
  2.  u_i,q = g_i( x_i,q )        transform, then winsorize at sector p1/p99
  3.  σ_i   = max(  sd(u_i,1…8),  φ_i  )
              φ_i = sector 20th pctile of sd(u_i) across universe
  4.  h_i   = s_i · ( u_i,1 - g_i(t_i) ) / σ_i        u_i,1 = current
  5.  h̃_i   = λ_i · h_i
 
      λ:   i=1  1.0     i=2  1.0     i=3  0.9
           i=4  0.9     i=5  1.0     i=6  1.4
 
 
AGGREGATE
 
  S = -τ · ln(  (1/n) · Σ_i exp( -h̃_i / τ )  )
 
      n = count of constraints measured for this name
      τ = 0.5   (sweep 0.25 … ∞ in backtest; τ→∞ yields mean(h̃))
 
 
DOMAIN GUARDS
 
  EBITDA ≤ 0 or EBIT ≤ 0     drop i=1, i=2; decrement n
  net debt < 0               floor x_2 at 0.1
  x ≤ 0 on any ln metric     drop that i; decrement n
  n < 5                      flag; exclude from ranked factor
 
 
CROSS-SECTIONAL
 
  P = pctile_rank( S | sector )
  R = residual of P on prior factors in orthogonalization order
```

## Read narrowly

- **RULED:** the Thesis/Risk tab's universal score is ROBUSTNESS, computed by the model above; it is the tab's standardized metric
  under the per-tab principle (the absolute figure S; the relative figure a percentile).
- **SHOWN, NOT FINAL:** he is "building out" the models and shared this one to show it; τ is itself to be swept in a backtest. This
  record does not freeze any parameter, threshold or guard -- it carries the model as given so a cut can build from exact text.
- **NOT RULED HERE:** the other tabs' models; the orthogonalization order across factors; the reference population for the sector
  statistics (the winsorization bounds, φ_i, the sector ceiling) beside the ranking pool Andrew set at ~17:5xZ (the analyzed
  companies); which of P and R the page displays.
- **WHERE IT LANDS:** the round-11 L10 addendum, beside candidate 13 (C-TAB-METRIC), as the Thesis/Risk tab's metric definition; the
  specification is frozen mid-round.

## Broadcast

One message to `2.0.0_SA_COO~W`, `3.0.0_SA_CVO~W`, `4.0.0_SA_CRO~W` and `0.0.0_AB_MSTR~Z`. Push state: LOCAL.
