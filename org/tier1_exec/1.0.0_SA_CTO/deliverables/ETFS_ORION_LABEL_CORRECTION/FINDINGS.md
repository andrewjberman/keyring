# ETFS Orion label correction — memorialized figures

**Author:** `1.0.0_SA_CTO` · **Date:** 2026-08-02 · **Andrew-direct:** *"Ok let's makes sure that we
have these final numbers memorialized somewhere."*
**Spec:** `docs/architecture/ETFS_ORION_LABEL_NORMALIZATION.md` @`8f0e32a642`

> ⚠ **THESE ARE MEASUREMENTS, NOT AN AUTHORIZATION.** Nothing here has been restated, no partner has
> been notified, and no rebate figure has been changed. **A restatement is Andrew's call.**

---

## 1. The defect

Orion returns the latest **settled** close (the prior trading day) and stamps `asOfDate` with the
**run date**. The gold/portal chain corrects for this via `orion_normalize_as_of`; **the ETFS rebate
chain does not** (call count: 0). So inflection's published daily series is labelled one NYSE trading
day forward.

**Mechanism note:** the sealed docstring attributes this to a *pre-open* pull at 09:00 ET. The
positions puller now fires **09:37 ET, post-open** (`cron(37 13)`), moved by Andrew-direct
`b2f61bed83` (2026-07-01) *"to avoid pulling before Orion settles prior-day close."* The operative
mechanism is therefore **the pull targets the prior settled close by design** — not pre-open timing.

## 2. Oracle test — passed, and it discriminates

| published | → true settled | outcome |
|---|---|---|
| 07-18 **and** 07-20 | both → 07-17 | values identical → collapse CORRECT |
| 07-25, 07-26, 07-27 | all → 07-24 | values identical → CORRECT |
| control 07-14 / 07-16 | → 07-13 / 07-15 | **different** → genuinely different books |

## 3. THE FIGURES — inflection, July 2026

Like-for-like: **22 trading-day observations on each basis, zero gaps.**

| ticker | published avg | true-settled avg | delta | % |
|---|---|---|---|---|
| DIVZ | 17,213,181.28 | 17,372,480.95 | +159,299.67 | 0.925% |
| IDVZ | 13,303,299.68 | 13,425,779.03 | +122,479.35 | 0.921% |
| PFDE | 10,855,741.97 | 10,949,981.15 | +94,239.18 | 0.868% |
| PFOE | 6,236,133.97 | 6,284,178.68 | +48,044.71 | 0.770% |
| **TOTAL** | **47,608,356.91** | **48,032,419.82** | **+424,062.91** | **0.891%** |

**Inflection's July basis is UNDERSTATED by $424,062.91 (0.891%).**

**Month boundary:** re-labelled, the July file spans **2026-06-30 → 2026-07-30** — it carries one
**June** settled day and omits true **07-31** (which lands in the August file). The understatement
direction follows from a rising series.

⚠ **BASIS, NOT PAYMENT.** Assumes a simple mean over trading-day observations. **Confirm the actual
ETFS_AVGCAP aggregation before quoting any dollar figure to a partner.**

## 4. ⛔ The larger defect — three partners, one file, two date bases

Schwab and Black Diamond feeds carry **accurate settled-date labels and must not be normalized.**
Only Orion forward-labels. So a single monthly rebate file has **inflection on T-1 while 49financial
and cottonwood are on T** — the partners are **not comparable in the artifact that decides what each
is paid.** This is the defect to fix regardless of what is decided about the offset.

## 5. One residual normalization does NOT explain

```
true 2026-07-13 (Mon) and true 2026-07-15 (Wed)
  IDENTICAL ETF vector: 17,221,032.09 / 13,502,102.90 / 11,079,105.25 / 6,300,737.41
```
Two different settled trading days, identical to the cent. **Andrew-direct: "holdings should be a raw
fact."** Open; do not let a green normalization imply it was resolved.

## 6. Artifacts

| file | what |
|---|---|
| `opaletfs_inflection_202607_CORRECTED_true_settled.csv` | the corrected daily series on TRUE settled dates, with the published date(s) each was derived from |
| `opaletfs_inflection_202607_published_vs_corrected.csv` | the per-ticker comparison in §3 |

## 7. Provenance

Published values read from the live `s3://opal-data-etfs/daily/inflection/*.json` slices; normalization
via the estate's shared `_orion_vendor_asof.orion_normalize_as_of`; trading days via
`lib/trading_calendar.py` (22 for July 2026 — 07-03 closed, Independence Day observed).
**Not recomputed from source parquet** — these are the figures as actually published, re-dated.
