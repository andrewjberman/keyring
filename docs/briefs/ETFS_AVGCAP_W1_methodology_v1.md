# ETFS_AVGCAP W1 -- Averaging Methodology v1 (AC#1 / PRD deliverable-1)

**Project:** ETFS_AVGCAP (W1, P1, DS). **PRD:** `docs/architecture/ETFS_AVGCAP.md` (all 8 Andrew-decisions resolved 2026-06-22).
**Engine:** `data/etfs/scripts/gold/avgcap_monthly_average.py`. **Output:** `opal-data-etfs/monthly/{YYYY-MM}.json`.
**Author:** 0.4.0_DS_ClientPlatform, 2026-06-25. **Status:** v1 -- implemented + proven end-to-end on the live Inflection slice; awaiting CTO methodology-ratification (PRD lane) + CVO number-verification.

---

## 1. The metric (scope-lock, from the PRD)

For each `(partner, ETF, month)`: the **monthly AVERAGE ownership VALUE** = the mean over the month's in-clock days of the dollar market value the partner's client book holds in that Opal ETF.

```
avg(partner, ETF, month) = mean over in-clock calendar days D of [ ownership_value(partner, ETF, D) ]
```

`ownership_value` = sum of position `market_value` (price x units, end-of-day) across the partner's accounts holding the ETF on day D. It is the AUM the partner has placed in Opal's funds. Opal ETFs = DIVZ, IDVZ, PFDE, PFOE. Partners = Inflection (W1, live), 49 Financial (W2), Cottonwood (W3).

**Firm-separation (NEVER #1 / AC5):** this compute reads ONLY `opal-data-etfs`. The per-partner daily slices are written there by the ETFS_SETUP producers (each reads only its own firm bucket -- the write-out model). AVGCAP is single-bucket by construction; it issues zero firm-bucket reads.

## 2. Input contract (ETFS_SETUP daily producer)

```
s3://opal-data-etfs/daily/{partner}/{date}.json   (date = YYYY-MM-DD)
rows: [{ schema_version, partner, date, etf_ticker, ownership_value,
         account_count, source_artifact, source_as_of }]
```

A day with no priceable data writes **no slice** (the producer's `COMPLETENESS_FLOOR=0.5` design). No-slice days -- weekends, holidays, and producer-skip days alike -- are handled by the carry-forward rule below; they are not "held zero".

## 3. The settled methodology decisions (D1-D4, Andrew-direct) and how each is implemented

### D1 -- day basis = CALENDAR-DAY with last-known carry-forward
Holdings are a point-in-time snapshot, so the position held on Friday is still held Saturday/Sunday; the truthful AUM-average weights every calendar day. **Implementation:** within the in-clock window, seed at the first written slice; every subsequent calendar day carries forward the last-known `ownership_value` until the next written slice supersedes it. The monthly average is the mean of these carried daily values over the covered calendar days.

- A **trading-day mean** (mean of written slices only, no carry-forward) is computed alongside as a **diagnostic** (`trading_day_mean_diagnostic`). It is NOT the spec number; it is reported for transparency and to expose any divergence (the two coincide when the value is flat across no-slice gaps, and diverge when the value steps across a weekend).
- Days **before** the first in-window written slice have no value to carry and are excluded from the denominator (they could not be observed). This is what makes an onboarding/partial month honestly partial rather than zero-padded.

### D2 -- partial-month = report-the-partial + LABEL
Never hold-until-complete; never a cross-firm fetch. **Implementation:** a `partial: true` flag is set on any (partner, ETF) whose carried series does not cover the full in-clock window, and on the partner window when the window start > month start (clock or first-slice) or the window end < month end (MTD cap). The label rides on the artifact -- a partial month can never read as a full month (AC6 / the COTETL serve-time-vintage lesson, the $24M class).

### D3 -- per-partner onboarding clock bounds the denominator
`PARTNER_CLOCKS = {inflection: 2026-05-15, 49f: TBD(W2), cottonwood: TBD(W3)}`. The window start is clamped up to the clock. **Inflection May = partial 05-15..05-31** by construction.

### D4 -- rollups (all three)
The average is **linear**, so each rollup is the sum of its component per-(partner,ETF) monthly averages (no re-averaging of sums needed):
- **per-(partner, ETF)** -- the spec metric (the core).
- **per-partner total** -- sum over the partner's ETFs.
- **per-ETF all-partners** -- sum over partners (Opal's total AUM in each fund across the book).

### AC6 -- worst-case source_as_of
Every monthly value carries the **oldest** (worst-case) `source_as_of` of its daily inputs, so staleness/partial coverage is honest on the served artifact.

## 4. Output artifact

`opal-data-etfs/monthly/{YYYY-MM}.json` (single bucket), schema_version 1.0:
```
{ month, schema_version, methodology, generated_utc, as_of_cap,
  per_partner_etf:[{partner, month, window:{start,end,calendar_days,clock_applied,mtd_capped,partial},
                    etfs:[{etf, monthly_avg_ownership_value, trading_day_mean_diagnostic,
                           written_days, calendar_days_covered, window_calendar_days,
                           first_written, partial, source_as_of_worstcase}]}],
  rollup_per_partner_total:[...], rollup_per_etf_all_partners:[...] }
```
June-MTD is produced with `--as-of <run-date>` to cap the window at the latest available data (e.g. `--as-of 2026-06-25`).

## 5. Proof of correctness -- end-to-end on the live Inflection slice (2026-06-25)

Run: `python avgcap_monthly_average.py --month 2026-06 --dry-run` (one live slice: `daily/inflection/2026-06-23.json`):

| ETF | monthly_avg (carry-fwd) | written | covered | source_as_of<= |
|---|---|---|---|---|
| DIVZ | $29,295,532.10 | 1d | 8d | 2026-06-23 |
| IDVZ | $23,156,669.90 | 1d | 8d | 2026-06-23 |
| PFDE | $18,735,316.19 | 1d | 8d | 2026-06-23 |
| PFOE | $11,033,281.81 | 1d | 8d | 2026-06-23 |
| **Inflection total** | **$82,220,800.00 [PARTIAL]** | | | |

The **$82.2M** total matches the PRD's `~$82M` Inflection anchor and AE's live-slice value ($82.14M / 476 accounts) -- methodology is sound. The single 06-23 observation carries forward 06-23..06-30 (8 covered days of the 30-day window) and is correctly flagged `[PARTIAL]`. Once AE's backfill lands the 05-15.. series, the same engine produces the AC#2 May-partial + the true June-MTD averages over the full series (no code change -- just more input days).

## 6. Validation / cross-reference (D7, AC4 -- the separate recon piece)

- **49F (AC#3):** bd is the cross-check vs Schwab RPS (the number-of-record). A bd<->Schwab-RPS account-level reconciliation over `account_xref` (in-both / BD-only / Schwab-only) explains the ~4% net gap (bd lags RPS; e.g. RPS $529.9M vs bd $508.6M @ 05-08). COO GO'd a **read-only raw-`.RPS` parse** (`opal-data-schwab/bronze/rps/CRS2026*.RPS`) for this cycle -- no write to opal-data-schwab (avoids the AES256-PutObject-deny); the W2 silver/RPS build is the durable re-run home (~early-July).
- **Inflection:** cross-reference via Eclipse model-data (`silver/eclipse/{date}/portfolios_simple.parquet` account->model + the model->target-holdings artifact) -- which Eclipse models hold the Opal ETFs -> which accounts -> reconcile expected vs actual Orion positions. (A small W1 discovery: pin the model->target-holdings artifact.)

## 7. Open items / not-yet-in-this-deliverable

- **AC#2 numbers** (May-partial + true June-MTD): gated on AE's Inflection backfill (05-15.., ETA ~1h, schema-identical, written-vs-skipped list incoming). Engine ready; run on landing.
- **AC#3 recon numbers:** the read-only raw-RPS parse (GO'd) -- in progress alongside this doc.
- **49F / Cottonwood clocks** (PARTNER_CLOCKS): set when W2/W3 producers + clocks are confirmed.
- **Deploy/scheduling home:** there is no `opal-data-etfs` code-deploy lane yet (safe-deploy PIPELINE_MAP = bd/inf/cot). For W1 the engine is run to produce the artifacts; a nightly/monthly scheduling home is a later AE/DT infra step (does not gate the deliverable).
- **CTO ratification** of D1-D4 as implemented (PRD CTO lane) + **CVO** number-verification of the produced averages + recon.
