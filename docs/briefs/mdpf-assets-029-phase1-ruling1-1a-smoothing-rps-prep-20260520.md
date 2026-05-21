# MDPF_ASSETS.029 Phase 1 — RULING #1 (1a smoothing) + RPS-side prep

**Agent:** 0.4.0_DS_ClientPlatform~B
**Date:** 2026-05-20
**TO:** MDPF_ASSETS.029 Phase 1 (GO'd, ab6d2a87c)
**Scope:** the seam-independent work CTO~B authorized while the RPS-vs-crosswalk
seam is with Andrew (CTO~B walked back the HYBRID on the Andrew-directive flag).
**Routed to:** 1.0.0_SA_CTO~B (direct) + 2.0.0_SA_COO~B (separate send)
**Non-mutating:** all reads; scratch outputs only; no S3 write, no commit of data.

---

## TL;DR

- **RULING #1 (1a anomaly) executed.** 05-15/05-18/05-19 1a interpolated;
  12-25 carry-forward is **moot** (no 12-25 partition exists). The two
  borderline dates BOTH corroborated as **real — keep, do not smooth**:
  2026-01-14 is a concentrated inflow, 2026-04-02 is a market move.
- **Date-alignment reconciled** (CTO~B's 98-vs-97 item): characterized fully.
- **RPS-side prep done** — RPS Schwab-whole gathered for all 97 dates.
- **97-sweep stays hard-stopped** pending Andrew's seam ruling.

---

## RULING #1 — 1a-series anomaly smoothing

### Corroboration of the two borderline moves (by_model decomposition)

CTO~B asked for one independent signal per borderline date. Used the
`aum-timeseries.json` `by_model` decomposition: a real rate/market move on a
duration-laddered fixed-income book is **duration-ordered** (Long-Term moves
most, Ultra-Short least); a flow is **concentrated**; an artifact is a uniform
step.

**2026-01-13 → 01-14 (+3.6% aggregate) — REAL (inflow). KEEP.**

| model | move |
|-------|------|
| Ultra Short-Term | **+17.16%** ($62.8M → $73.5M, +$10.8M) |
| Short-Term | +0.81% |
| Intermediate | +1.29% |
| Long-Term Conservative | +4.30% |
| Long-Term Aggressive | +1.71% |

Not a market move — a market/rate move would be duration-ordered (Ultra-Short
least). The +17% is **concentrated in the Ultra-Short model** = a ~$10.8M
inflow/allocation into the cash-like model. CTO~B's criteria count "a known
inflow" as corroborated-real. **Keep — real AUA.**

**2026-03-31 → 04-02 (+3.2% aggregate) — REAL (market). KEEP.**

| model | move |
|-------|------|
| Ultra Short-Term | +0.42% |
| Short-Term | +2.70% |
| Intermediate | +2.99% |
| Long-Term Conservative | +3.74% |
| Long-Term Aggressive | +2.71% |

Cleanly **duration-ordered** — Ultra-Short moves least, Long-Term Conservative
most, mid-duration models in between. That is the signature of a real rate
move (over 2 calendar days — 04-01 has no partition). **Keep — real market.**

### Smoothing applied

| date | adjustment | raw 1a | adjusted 1a | marker |
|------|-----------|--------|-------------|--------|
| 2026-05-15 | interpolated_anomaly | $1,443.82M | $1,344.44M | `_1a_adjustment` + `_1a_raw` |
| 2026-05-18 | interpolated_anomaly | $1,434.02M | $1,347.34M | `_1a_adjustment` + `_1a_raw` |
| 2026-05-19 | interpolated_anomaly | $1,426.52M | $1,348.31M | `_1a_adjustment` + `_1a_raw` |

Linear interpolation between the 05-14 anchor ($1,343.5M) and the 05-20 anchor
($1,349.3M) — 05-20 is the .028 partition, untouched. The spike’s round-trip
signature (+7.5% out, −5.4% back to trend in 5 days) + the correlated
`silver/transactions` 79→1.3M-row event = data artifact, per CTO~B.

**2025-12-25 carry-forward is MOOT** — there is no `aggregate_aua/2025-12-25.json`
partition (12-25 is a market holiday; the partition set skips it). The 1a
series carries a 12-25 point but the sweep writes no 12-25 partition, so
nothing to carry-forward into. Noted; no action.

**Marker convention:** every adjusted value carries `_1a_adjustment`
(`interpolated_anomaly` | `holiday_carryforward`) **and** `_1a_raw` (the
pre-adjustment value) in the partition — estimation visible in the artifact,
never silent, per CTO~B's mandatory-marking rule.

Net: the smoothing touches **3 partition-dates** (05-15/18/19). 01-14 and
04-02 kept as real. A small, fully-justified, fully-marked adjustment set.

## Date-alignment reconciliation (CTO~B's 98-vs-97 item)

The 1a series has 98 points in 2025-12-23..2026-05-19; there are 97
`aggregate_aua` partitions. Not a clean off-by-one — a 6-vs-5 set difference:

- **6 1a-dates with NO partition:** 2025-12-24, 12-25, 12-30, 12-31,
  2026-01-01, 01-02 — year-end holidays/closures. The 1a series carries them;
  the partition set (correctly) does not. No partition to write — ignore them
  in the sweep.
- **5 partitions with NO 1a-point:** 2025-12-27 (Saturday), 2026-01-26, 01-28,
  02-05, 04-03. The sweep must roll-forward 1a from the nearest prior 1a date
  for these. **Note:** 01-26 / 01-28 / 02-05 are the *same three dates* whose
  `silver/allocations` partitions carry a schema variance (flagged in the
  calibration brief) — these three dates are doubly-irregular and warrant
  explicit handling/verification in the sweep.

## RPS-side prep

RPS Schwab-whole = `sum(market_value)` over `schwab/silver/rps/date=.../`,
gathered for all 97 partition dates. Range $1,321.70M (2025-12-23) →
$1,612.08M. **7 dates roll-forwarded** (no exact RPS partition): 2025-12-27,
2026-01-19, 02-16, 04-03, 04-30, and **05-18 + 05-19 both sourced from 05-15**
(RPS's latest partition is 2026-05-15 — a 4-day lag past the 05-19 span end).
Series saved to scratch; ready to feed the sweep under whichever basis Andrew
rules.

## Status

**97-sweep hard-stopped** pending Andrew's RPS-vs-crosswalk seam ruling
(CTO~B is carrying the options to him). The seam-independent prep is done:
the 1a series is cleaned + marked, the RPS series is gathered, the
date-alignment is characterized. On Andrew's ruling + CTO~B's relay, the sweep
can proceed immediately. All crosswalk/`silver/allocations` operations remain
held per CTO~B's walk-back.
