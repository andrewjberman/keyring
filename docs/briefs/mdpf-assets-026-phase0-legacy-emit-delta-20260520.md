# MDPF_ASSETS.026 Phase 0 -- legacy-emit v0.8 delta quantification

**Author:** 0.4.0_DS_ClientPlatform~B | **Date:** 2026-05-20
**For:** 1.0.0_SA_CTO~B (gates the now-vs-WS-F decision to Andrew) | CC 2.0.0_SA_COO~B
**Non-mutating:** no commit, no S3 deploy, no live-artifact change. Analysis only.

## Question

How much does the LIVE Model Portfolios page headline (`enterprise_total` in
`s3://opal-data-portal-v2/json/portfolios/non_model_assets.json`) move when
`build_legacy_compat_emit.py` is brought to the v0.8 taxonomy?

## Method

The delta was quantified analytically + component-decomposed, then
cross-checked to the cent against the live artifact (the live
`enterprise_total` is reproduced exactly from its components -- see below). The
legacy emit formula (build_legacy_compat_emit.py L592-631):

  enterprise_total = total_49f + inf_2a + cohort_0
  total_49f        = broader_custody            (the 3-term 1a+1c+1b collapses)
  non_model_aum    = broader_custody - 1a       (emitted; SMA-INCLUSIVE)

## FINDING 1 -- the TO's "SMA double-count" premise is WRONG (component = $0)

The .026 TO estimated component (i) "SMA double-count removal (~$25M)" from
L499-503 (`new_1b = broader_custody - 1a - sma_aua`). But `new_1b` is NOT the
emitted figure -- it only feeds `total_49f` (which round-trips to
`broader_custody`). The EMITTED `non_model_aum` is `nm_total = enterprise_total
- model_aum_total - cohort_0` = `broader_custody - 1a`, which is **already
SMA-INCLUSIVE**. There is no SMA double-count and no SMA-exclusive 1b in the
live legacy artifact. **Component (i) = $0.** The ~$25M estimate does not apply
to the legacy emitter.

## FINDING 2 -- the real components: 1b basis (+) and Cohort 0 removal (-)

The live legacy `enterprise_total` INCLUDES Cohort 0 (`etf_public_residual`);
the v0.8 headline (1a+1b+2a) EXCLUDES it (audit-only per .024). And the legacy
1b basis is `broader_custody` (the CEO-direct 2026-05-19 "all-49-minus-liab"
scope) vs v0.8's `certified_aua` (the full BD book).

  v0.8 enterprise headline = certified_aua + inf_2a   (= 1a + 1b_v08 + 2a)
  live  enterprise_total   = broader_custody + inf_2a + cohort_0
  delta = (certified_aua - broader_custody) - cohort_0

## Quantified delta -- two recent dates

### 2026-05-18 (RPS-coverage date -- Cohort 0 nonzero)
| | Value |
|---|---|
| 49F 1a | $1,340,415,278.02 |
| Inflection 2a | $93,603,055.45 |
| broader_custody (49F, legacy basis) | $1,799,587,556.09 |
| certified_aua (49F, v0.8 full BD book) | $1,812,084,304.28 |
| Cohort 0 (etf_public_residual) | $91,328,983.13 |
| **live enterprise_total** | **$1,984,519,594.67** |
| **v0.8 enterprise_total** | **$1,905,687,359.73** |
| **DELTA** | **-$78,832,234.94** |

Component breakdown of the -$78.83M:
- (i) SMA double-count: **$0.00** (Finding 1)
- (ii) 1b basis broader_custody -> certified_aua: **+$12,496,748.19**
- (iii) Cohort 0 removed from headline: **-$91,328,983.13**
- residual: $0.00

### 2026-05-15 (pre-RPS-coverage -- Cohort 0 = $0)
| | Value |
|---|---|
| broader_custody | $1,799,587,556.09 |
| certified_aua | $1,804,819,715.69 |
| Cohort 0 | $0.00 |
| **live enterprise_total** | **$1,894,134,015.63** |
| **v0.8 enterprise_total** | **$1,899,366,175.23** |
| **DELTA** | **+$5,232,159.60** |

Component breakdown of the +$5.23M:
- (i) SMA: $0.00  (ii) 1b basis: +$5,232,159.60  (iii) Cohort 0: $0.00

## Interpretation for the Andrew decision

The page-headline delta is **not a fixed number** -- it is dominated by the
Cohort-0-removal component, which is $0 on pre-RPS-coverage dates and ~-$91M
once RPS coverage starts (2026-05-18 onward):
- Recent / current dates (2026-05-18+): the page headline DROPS ~$79M
  (-$91M Cohort 0 removal, partially offset by +$12.5M basis correction).
- Historical / pre-RPS dates: the page barely moves (~+$5M, basis only).

The dominant driver is therefore a CORRECTNESS fix that v0.8/.024 already
ruled: Cohort 0 belongs in audit fields, not the headline. The 1b basis change
is small (+$12.5M -- broader_custody was already a broad scope post the 5/19
CEO pivot, so the gap to the full BD book is minor).

Cross-check: the v0.8 legacy `enterprise_total` for 2026-05-18
($1,905,687,359.73) reconciles to-the-cent against the v0.8 platinum
`opal_aggregate_aua` (1a+1b+2a = $1,905,687,359.73) -- so the .026 Stage-1 AC3
(legacy == platinum to the cent) is achievable.

## Phase 0 status

AC0 satisfied. Stage 1 (the actual build_legacy_compat_emit.py change) remains
DISPATCH_HELD on Andrew sign-off -- it moves the live CEO-visible page headline
~-$79M on current dates.
