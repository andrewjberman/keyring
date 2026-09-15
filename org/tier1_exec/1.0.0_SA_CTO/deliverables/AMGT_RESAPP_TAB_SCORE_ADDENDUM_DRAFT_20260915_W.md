# DRAFT -- the tab-score addendum text for AMGT_RESAPP's next PRD version (candidates 13-16 + FWD-20)

**Status: DRAFT, NOT THE PRD.** Written by `1.0.0_SA_CTO~W` at 2026-09-15 ~22:5xZ while round 11's slug is staged in
`3.0.0_SA_CVO~W`'s worktree and not yet committed. It edits nothing. The L10 answer merges this text with the slug's own rows once
that slug is read; the round-11 specification stays frozen until then, and this file is superseded by whatever the PRD version carries.
**Why it exists now:** every input it rests on is settled -- Andrew's four models, this lane's rulings (cards 1-18), and both CROs'
research -- so only the slug's rows are missing, and drafting the settled half now makes the L10 answer a merge rather than a write.

**Sources, all committed:** Andrew-direct records @`4eef3ae75a` (per-tab principle), @`260402c006` + @`3f9481ea12` (Robustness),
@`947b9793a1` (Peers V), @`287d2c2619` (Divergence D), @`a026de4004` (the five answers); this lane's measurement card
`AMGT_RESAPP_SUBSTRATE_MEASUREMENTS_20260915_W/TAB_SCORE_SOURCING_BLOOMBERG_LUSHA_MEASURED.md` and its instruments;
`4.0.0_SA_CRO~W` @`7bad309f20` (five-point findings) and @`ecfe46465e` (Lusha v3 reference); `4.0.0_SA_CRO~Z` @`910dc1bb7e` (Seeking
Alpha); adjudications @`1685652d6e` (cards 1-12), @`4be2f8be48` (15), @`ffa54cb4f0` (16), @`40dc1897f1` (18).

---

## C-TAB-METRIC -- one standardized metric per tab (candidate 13)

Every tab declares ONE headline metric, served as a record:

```
{metric_id, definition, unit, absolute, percentile, pool_n, pool_vintage, source, state: MEASURED | ABSENT, reason}
```

**The pool and the percentile (Andrew ~17:5xZ; card 6).** `percentile` ranks the company within the POOL OF ANALYZED COMPANIES in the
Security Analysis database -- companies deduplicated by company FIGI (card 9), eligible for that metric's version, at one `as_of` cut.
Below 5 eligible names the percentile is `ABSENT` with `pool too small (N)` and the absolute still renders. A second figure labelled
`sector` is served only where that sector holds at least 5 eligible names; the two are never mixed, and a global fallback is labelled.

**Store and history (Andrew ~17:5xZ).** `s3://opal-data-harvest`, append-only: one record per company per metric per analysis at
`metrics/v1/{metric_id}/{security_key}/{as_of}.json`, never overwritten; one dated pool snapshot per metric at
`metrics/v1/{metric_id}/_pool/{as_of}.json` carrying every analyzed company's latest value, its `n` and the percentile rule, so a
percentile is recomputable and auditable over time.

## The four tab metrics

| tab | metric_id | absolute | source, as ruled | state today |
|---|---|---|---|---|
| Exec Management | `exec_mgmt_tenure_avg_years` | average tenure of current executives in executive positions at the company | Bloomberg `EXECUTIVE_AVERAGE_TENURE` (card 1) | MEASURED, 33 of 33 pool names |
| Exec Management (companions) | `exec_company_tenure_avg_years`, `exec_role_tenure_avg_years` | time at the company in general; time in the current role | filings only -- proxy-statement biographies and the 10-K / 20-F officer section (cards 1, 15) | ABSENT with reason where the filing is silent; Lusha is NOT a source |
| Thesis / Risk | `robustness_S` | Andrew's six-constraint soft-min score (@`260402c006`) | every input from Bloomberg (@`3f9481ea12`) | ABSENT with reason where a name is ineligible (card 5) |
| Peers | `peers_V` | peer-relative valuation z over six yield-form measures (@`947b9793a1`) | Bloomberg, on the served R-1 peer set | MEASURED where the peer set is non-empty (10 of 33 today) |
| Model | `divergence_D` | (model NTM FCF - consensus NTM FCF) / analyst dispersion (@`287d2c2619`) | Bloomberg (card 16) | ABSENT until FWD-20 serves a house forecast (card 4) |

### Exec Management -- what each measure is, and is not

`EXECUTIVE_AVERAGE_TENURE` is time IN AN EXECUTIVE POSITION, not total time at the company; the two are separate metric ids and are
never substituted for one another (card 1). Bloomberg carries time at the company only for the CEO
(`TOTAL_TENURE_OF_CEO_COMPANY`, beside `CHIEF_EXECUTIVE_OFFICER_TENURE` for time in role), and no Bloomberg field carries a per-officer
join date -- the bulk officer list is names and titles. Lusha is not a source (card 15): its documented enrich request cannot exclude
emails and phones, and its documented response carries no employment dates; the one authorized call is not made. Each officer value
carries its source and date precision; an annual join year yields a tenure RANGE, never day precision.

### Thesis / Risk -- Robustness eligibility and inputs (card 5)

The model stands as Andrew gave it, parameters unchanged. Eligibility is computed ONLY by a windowed instrument: the latest 8 TTM
observations built from `FUND_PER=Q` quarters with the model's domain guards applied -- a count of matching dates anywhere in a
response is not eligibility. `x6` (largest customer share) is `SUPPLY_CHAIN_REVENUE_PERCENTAGE` at the latest observation only, earlier
observations ABSENT and never carried back. `x3` and `x4` use year-1 plus year-2 debt principal, LABELLED "debt principal due within 24
months", and only after the principal fields' documentation is reconciled. Where a name is ineligible the tab serves `ABSENT` with the
reason and the constraint count. A round-12 cell measures an annual-frequency variant and reports the eligible count; a parameter change
goes to Andrew only with that count in hand.

### Peers -- V, with the subject capped (Andrew's ruling + card 7)

Each measure is winsorized at the peers' p5/p95 AND THE SUBJECT IS CLAMPED TO THOSE BOUNDS before z (Andrew ~19:0xZ "Yeah sure").
Contract fixes: a missing dividend or buyback component makes measure 3 ABSENT, never zero; the EBITDA guard reads the same period as
the measure it guards; NTM EPS growth is its own input (forward EPS against trailing EPS, one currency and share basis), never derived
from a pair of P/E ratios. Members resolve by company FIGI to an exchange-coded Bloomberg security BEFORE any measure is read -- of 120
member rows requested by raw identifier, 3 resolved to a different company and 4 were invalid. A `BEST_*` field without
`BEST_FPERIOD_OVERRIDE=BF` is the next fiscal QUARTER; fundamentals are read in one currency (`EQY_FUND_CRNCY=USD`).

### Model -- Divergence, and what it waits on (cards 3, 4, 16)

`s_cons` is not carried by any source measured: Bloomberg has no FCF estimate spread or count, and Seeking Alpha carries no cash-flow
estimates at all. The proxy is `s_proxy = |F_cons| * sd(CFPS) / |mean(CFPS)|` at 1FY, ABSENT when the CFPS mean is near zero or fewer
than 4 estimates contribute; EPS dispersion in the same form where CFPS fails; the score record carries `dispersion_proxy: CFPS | EPS`
so a proxy change never reads as a changed view. Annual standard deviations are never summed into an NTM figure; period ends come from
`BEST_PERIOD_END_DATE`. Seeking Alpha's EPS high, low and analyst count are a SECOND INSTRUMENT printed beside Bloomberg's count for the
estimate-count guard and flagged on disagreement, never substituted (card 16). D is ABSENT with reason until FWD-20 serves.

## FWD-20 -- the house forecast Divergence needs (card 4)

**An analyst sees where the firm's own forecast disagrees with the street.**
DONE WHEN EXERCISED -- an analyst has read a Divergence figure whose model side came from the firm's own forecast.
ACCEPT: the pool carries, per analyzed company, a forecast of next-twelve-month free cash flow whose revenue, margin, cash-tax, capex
and working-capital drivers are seeded from dated filings and operating history, with every assumption stored beside its source and
timestamp; no driver is copied from a consensus feed; and before the score is shown, `sd(D)` across the universe is at least 0.25
(Andrew's degeneracy check), with the distribution recorded.
SOURCE: Andrew-direct ~18:3xZ @`287d2c2619`; the pool holds only reported fiscal-year history today (17 model-block objects, no forecast
line and no driver).

## Open questions this addendum does NOT close

1. **Promoting the Security Analysis page** (PORTAL FROZEN) and **activating recurring harvest collection** (mechanism and cadence
   reserved) are Andrew's, carried as cards since tick 1.
2. **Who exercises the outcomes that name a person** (FWD-5, FWD-7), and when -- asked of Andrew once the page is exercisable (card 12).
3. **Sector statistics for Robustness** need a calibration population broader than the analyzed pool; the pool ranks, the calibration
   set is named in the round-12 cell.
