# ETFS_AVGCAP W1 -- AC#2: Inflection May-partial + June-MTD averages + 2 grounded data-quality findings

**Project:** ETFS_AVGCAP.W1 (DS). **Engine:** `data/etfs/scripts/gold/avgcap_monthly_average.py` (AC#1, commit 116c84ed7).
**Inputs:** the AE-backfilled Inflection daily series `opal-data-etfs/daily/inflection/{date}.json`, 40/40 days 2026-05-15..06-23 (0 skipped, comp-freshness PASS).
**Author:** 0.4.0_DS_ClientPlatform, 2026-06-25. **Status:** numbers produced + source-grounded; **HOLDING the `opal-data-etfs/monthly/` serve pending CVO verification + the inf-gold price-staleness resolution (below).**

---

## 1. AC#2 numbers (calendar-day carry-forward per D1; partial-labeled per D2)

### May 2026 -- PARTIAL (in-clock window 05-15..05-31, 17 calendar days; Inflection clock D3=05-15)
| ETF | monthly avg ownership value | source_as_of<= |
|---|---|---|
| DIVZ | $4,711.41 | 2026-05-15 |
| IDVZ | $5,805.88 | 2026-05-15 |
| PFDE | $14,557,204.00 | 2026-05-15 |
| PFOE | $9,718,599.17 | 2026-05-15 |
| **Inflection total** | **$24,286,320.46** | |

### June 2026 -- MTD PARTIAL (window 06-01..06-23, 23 calendar days; `--as-of 2026-06-23` = last slice)
| ETF | monthly avg ownership value | source_as_of<= |
|---|---|---|
| DIVZ | $26,551,089.71 | 2026-06-01 |
| IDVZ | $20,824,042.61 | 2026-06-01 |
| PFDE | $18,159,833.18 | 2026-06-01 |
| PFOE | $10,671,422.17 | 2026-06-01 |
| **Inflection total** | **$76,206,387.67** | |

The May total (~$24M) and June-MTD total (~$76M) differ ~3.1x. This is **not** a methodology artifact -- it is the real source level, driven by the 06-03 step below. The 06-23 single-day total ($82.22M) is the latest level; June-MTD ($76.2M) is lower because it blends the pre-step 06-01/06-02 (~$23.5M) with the post-step days.

## 2. Finding A -- the 06-03 regime step: STATE source-confirmed; MECHANISM unverified

**State (source-confirmed, `opal-data-inf/gold/holdings/{date}.parquet`):**
- DIVZ and IDVZ are **entirely absent** from inf-gold holdings before 06-03 (0 rows on 05-30 and 06-02), then appear on 06-03 with `price_source=transaction_observed` (DIVZ 454 rows / $27.96M, IDVZ 454 rows / $22.13M).
- 06-03 is a **broad file expansion**: file rows 12,496 (06-02) -> 13,155 (06-03); PFDE units 532,822 -> 649,818 (+117K); total all-holdings MV $350.9M -> $377.6M.

So in May, Inflection's Opal-ETF ownership is essentially **PFDE + PFOE only** (~$24M); DIVZ/IDVZ are ~$0. The ~$5K May DIVZ/IDVZ averages come from a single 05-15 sliver ($11K/$14K) then $0 for the rest of the window.

**Mechanism (HYPOTHESIS -- NOT grounded, NOT to be called proof):** the 06-03 jump is either (a) a genuine Inflection allocation/ramp into DIVZ/IDVZ on/around 06-03, or (b) an inf-gold source-coverage expansion (positions held earlier but not captured until 06-03). inf-gold alone cannot disambiguate -- `transaction_observed` on 06-03 is consistent with EITHER a real buy or a first-capture. **Resolution path:** the Eclipse model-data cross-reference the PRD already scopes for Inflection (which Eclipse models hold the Opal ETFs -> which accounts -> expected vs actual) + an inf-source check. Routed to the inf-pipeline owner via COO.

**AC#2 treatment:** the numbers are reported faithfully + partial-labeled; the May reading is annotated "DIVZ/IDVZ effectively absent in-source pre-06-03" so the ~$5K values are not misread as a bug.

## 3. Finding B -- the 06-17..06-22 ETF price freeze: REAL inf-gold staleness (SOURCE-CONFIRMED)

**This is source-confirmed, not benign** (`opal-data-inf/gold/holdings/`):
- The 4 Opal-ETF **prices are frozen identical** across 06-17 / 06-18 / 06-22: DIVZ=37.3201, IDVZ=34.58, PFDE=27.6847, PFOE=22.9827 -- the same to 4 decimals for 3+ days.
- **The smoking gun is `price_source`:** 06-17 = `transaction_observed`; 06-18 and 06-22 = `linear_interpolation` carrying the 06-17 price **flat** (not interpolating toward a later observation). The fresh price feed for these tickers stopped after 06-17.
- Meanwhile the holdings file is **fresh, not carried**: file rows 13,227 (06-17) -> 13,237 (06-18/22); total all-holdings MV moves ($378.77M -> $379.36M); units drift into 06-23. So only the **ETF prices** are stale, not the file (this is why the etfs daily total is identical to the cent across those days while source ETags differ -- AE's observation, now mechanism-grounded).
- 06-23 partially breaks it (units move; price still 37.3201 = still carried).

**Classification:** a REAL upstream inf-gold ETF-PRICE staleness over 06-18..(>=)06-22, beyond AVGCAP's scope -- it affects **anything consuming inf-gold ETF prices in that window** (not just this metric). **Routed to the inf-pipeline owner via COO** (COO directive 133522Z: resolve, don't just note).

**AC#2 treatment (Rule 17 discipline):** AVGCAP **averages the served daily values faithfully and does NOT fabricate a de-frozen price** -- correcting the price is an upstream fix, not a metric decision. Sensitivity: the 5-6 frozen days (06-18..06-22) sit at ~$82.14M, close to the live 06-16 ($83.26M) and 06-23 ($82.22M) levels, so their over-weighting nudges the June-MTD mean by well under 1% -- the headline ($76.2M) is not materially distorted by the freeze (the bigger driver is the 06-03 step). Once inf-gold re-prices the window, re-run the engine (no code change) for the corrected June number.

## 4. Disposition / asks
- **CVO:** verify the May + June-MTD numbers (re-derive from the daily series) + the two findings' grounding. This is the close-gate (same as AC#1/#3).
- **COO -> inf-pipeline owner:** route Finding B (real inf-gold ETF-price staleness 06-18..06-22, `price_source` evidence) as a data-quality finding with cross-window blast radius; and Finding A's mechanism question (ramp vs coverage) for the Eclipse/inf-source resolution.
- **Serve hold:** NOT uploading `opal-data-etfs/monthly/2026-05.json` / `2026-06.json` until CVO verifies + Finding B is dispositioned (never-widen: a served partial carrying a known upstream freeze needs the cert first). Engine + numbers ready to serve on GO.
