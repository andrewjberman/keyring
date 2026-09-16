# Andrew-direct 2026-09-15 ~18:3xZ, at the `1.0.0_SA_CTO~W` terminal: the Model tab's universal score is DIVERGENCE (model NTM FCF against consensus, in analyst-dispersion units), with the Peers valuation model sent again beside it -- verbatim

**Recorded by:** `1.0.0_SA_CTO~W`. **Channel:** direct message in this Claude Code session, arriving mid-turn while this seat ran the
Peers score and the Robustness coverage on Bloomberg; exact arrival timestamp unavailable (after the 18:26:44Z clock read and the peer
record's commit @`947b9793a1`). **Project:** AMGT_RESAPP. **Descends from:** the per-tab principle (@`4eef3ae75a`), the Robustness
model (@`260402c006`, follow-on @`3f9481ea12`) and the Peers model (@`947b9793a1`).

## Verbatim, entire (one fenced block so the layout, the blank separator lines and the repeated heading survive byte for byte)

```text
Then the below paste provides the "Peers" Valuation score and the "Model" "Divergence" score: What this produces
A single signed number per name: how cheap or expensive it sits against its own ranked peer set, in peer-set standard deviations. Negative means expensive, positive means cheap.
Everything is yield-form, following the house convention — it keeps the sign correct through zero for unprofitable names, and averaging yields is equivalent to harmonic-mean averaging of the corresponding multiples, which is the right operation for comparables. Six measures, equal weight, no sleeve tilt. Two of them are EV-denominated to neutralize the leverage effect that would otherwise make indebted peers screen cheap on every equity-level yield.
Two nested rankings: the z-score is computed inside the peer set, and only then is the result percentile-ranked across the universe. The inner step asks whether the name is cheap relative to who it should be compared to; the outer step asks how unusual that degree of cheapness is.
 
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
 
What this produces
A single signed number per name: how far your model's free cash flow sits above or below consensus, normalized by how much dispersion there is among analysts. Positive means your model is more optimistic than the street.
This is deliberately not implied upside. Upside is a valuation level, and the peers tab already owns valuation — ranking both would double-count price and collapse the two axes into one. What the model tab contributes that nothing else can is a disagreement: a residual between your forecast and the consensus forecast, which has no mechanical relationship to where the multiple sits.
Normalizing by analyst dispersion rather than by a fixed percentage is what makes it comparable across names. Being 10% above consensus on a name where estimates span a wide range is unremarkable; being 10% above on a tightly-clustered name is a real disagreement. Dispersion is the denominator that separates them.
FCF is the forecast line rather than EPS because it's the output your model already produces deterministically, it's harder to manage than earnings, and it's consistent with the FCF-based constraint in robustness.
Two guards matter more here than elsewhere. If your model drivers auto-populate from consensus, D collapses toward zero and the factor measures nothing — so the seeding of those drivers has to be at least partly independent, and the distribution of D across the universe should be checked for exactly that degeneracy before you trust it. And estimate counts below four make dispersion meaningless.
 
INPUTS
  F_model     model NTM free cash flow          your model output
  F_cons      consensus NTM free cash flow      median across analysts
  s_cons      sd of analyst NTM FCF estimates
  N_est       count of contributing analysts
  R_ntm       NTM revenue, consensus

CORE
  D = ( F_model − F_cons ) / s_cons
      sign: positive = model above street

DISPERSION FLOOR
  s_floor = ψ · |F_cons|
            ψ = sector 20th pctile of ( s_cons / |F_cons| )
  s_cons  ← max( s_cons , s_floor )

DEGENERATE-CONSENSUS GUARD
  |F_cons| < 0.01 · R_ntm     use  s_cons ← max( s_cons , 0.01 · R_ntm )
                              consensus FCF near zero; percent-form
                              dispersion is unstable

COMPANION  (reported, not ranked)
  U = ( implied value / price ) − 1        model upside
  Δ = ( F_model − F_cons ) / |F_cons|      raw percent disagreement

GUARDS
  N_est < 4                   suppress D
  F_model missing             suppress D
  s_cons = 0 after floor      suppress D
  winsorize D at universe p1 / p99

CROSS-SECTIONAL
  P = pctile_rank( D | sector )
  R = residual of P on prior factors in orthogonalization order

DEGENERACY CHECK  (pre-deployment, universe-wide)
  sd( D ) across universe < 0.25     drivers likely seeded from consensus;
                                     factor is not measuring disagreement
```

## Read narrowly

- **RULED -- THE MODEL TAB'S SCORE:** D = (F_model − F_cons) / s_cons on NTM free cash flow, positive when the house model is above the
  street; the dispersion floor ψ (sector 20th percentile of s_cons/|F_cons|); the degenerate-consensus guard at 1% of NTM revenue; D
  suppressed below 4 estimates, without a model figure, or at zero dispersion after the floor; D winsorized at universe p1/p99; P a sector
  percentile, R the orthogonal residual.
- **RULED -- WHAT D IS NOT:** implied upside. U (model upside) and Δ (raw percent disagreement) are REPORTED COMPANIONS and are never
  ranked, so price and valuation stay with the Peers tab alone.
- **A CONDITION ON THE MODEL, RULED:** the model's drivers must be seeded at least partly independently of consensus, and the universe
  distribution of D is checked BEFORE deployment -- sd(D) below 0.25 across the universe means the factor is not measuring disagreement.
  This binds the model-block producer, not only the page.
- **THE PEERS MODEL, SENT AGAIN:** the Peers half of this paste is the model recorded @`947b9793a1`; this seat's byte comparison of the
  two texts is printed in the commit that lands this record. Nothing in it is read as a change unless that comparison shows one.
- **NOT RULED HERE:** the consensus source (Bloomberg's estimate fields are measured before a cut relies on them); how an NTM F_model is
  built from a model that today produces fiscal-year blocks; "implied value" for U; the orthogonalization order across the four scores;
  the "| sector" percentile beside the ~17:5xZ pool word, the one open question already carried for Robustness and Peers.
- **WHERE IT LANDS:** the round-11 L10 addendum as candidate 16, the Model tab's metric definition, beside candidates 13-15. The
  specification is frozen mid-round.

## Broadcast

One message to `2.0.0_SA_COO~W`, `3.0.0_SA_CVO~W`, `4.0.0_SA_CRO~W` and `0.0.0_AB_MSTR~Z`. Push state: LOCAL.
