# The rivalfunds daily pull files NON-US prices on a New York clock: 391 of 760 rows wrong on 2026-10-15

**archetype:** TRACE
**Recorded by:** `0.0.3_BG_BBGTerminal`, 2026-10-17 ~06:2xZ.
**Trigger:** Andrew, direct, in session: *"check out that lenovo price history for rivalfunds and get that
corrected properly"*. Lenovo was the entry point; the defect is universe-wide.

## The finding in one line

**The daily market pull captures `PX_LAST` once at ~11:00Z and files it under the NYSE T-1 date. That
timestamp is after the Asian close and during the European session, so only US names get a correct
close.**

## What is MEASURED, per class

Compared served `g4_rows` output against Bloomberg BDH `PX_LAST` for the same dates.

| class | mechanism | verdict |
|---|---|---|
| **US** (ADBE US) | 11:00Z precedes the US open, so PX_LAST is genuinely the prior close | **CORRECT**, 4 of 4 dates |
| **ASIA** (992 HK, 1 HK, 005380 KS) | Asia closed hours before 11:00Z, so PX_LAST is TODAY's close filed as yesterday's | **SHIFTED ONE TRADING DAY**, 12 of 12 date-checks |
| **EUROPE** (AAF/ADM LN, AI/AIR FP, ALV/BAS GR) | 11:00Z is mid-session in London/Paris/Frankfurt | **MATCHES NEITHER** the day's close nor the next day's |

The Asian shift is exact and repeatable -- every served value equals the NEXT trading day's close to the
cent. The European values are near-misses on both sides (BAS GR served 53.01 vs 52.48 and 52.97), which
is **consistent with an intraday snapshot recorded as a close**. That mechanism is INFERRED, not measured:
I did not capture an intraday series to prove it. The Asian mechanism IS measured.

### Lenovo, the case that opened it

| date | BDH truth | served `pull` | served `backfill` |
|---|---|---|---|
| 2026-09-29 | **35.48** | 34.54 | **35.48** correct |
| 2026-09-30 | 34.54 | -- | -- |
| 2026-10-13 | 31.10 | 30.40 | -- |
| 2026-10-14 | 30.40 | 25.98 | -- |
| 2026-10-15 | 25.98 | 28.06 | -- |
| 2026-10-16 | 28.06 | -- | **28.06** correct |

The served `pull` value on each date is the FOLLOWING date's true close. The `34.54` filed under 09-29 is
09-30's close. **The "28.06 on two consecutive days" that first looked like a stale carry-forward is not
stale at all**: 10-15's pull row holds 10-16's close, and 10-16's backfill row holds the true 10-16 close,
so the two agree for different reasons.

## Scale, with its denominator

Partition 2026-10-15, 760 merged rows:

| class | securities | priced by a `pull` row | status |
|---|---|---|---|
| ASIA | 248 | **170** | wrong (shifted), measured |
| US/CA | 236 | 188 | correct |
| OTHER (LN 53, FP 32, GR 29, NA 15, SW 14, BZ 14, SM 13, SJ 9, IM 9, NO 8, MM 7, DC 7, AB 6, ? 25) | 276 | **221** | wrong (neither close), measured on 6 of them |

**391 of 760 rows (51.4%) are priced by a writer that is wrong for that venue.** The 6 European names are a
sample, not a census: the 221 figure is the pull-priced OTHER population, and I verified 6 of it.

## What this does NOT explain, named deliberately

- **The 10 dates 992 HK is missing** (2025-10-29, 2025-12-26, 2026-02-17/18/19, 04-06/07, 05-01, 07-01,
  10-01) are ALL Hong Kong public holidays -- Chinese New Year, Ching Ming, Labour Day, SAR Establishment
  Day, National Day. **Correct behaviour. Not a defect and must not be "filled".**
- **The duplicate objects** on 2026-09-29 and 2026-10-02 are collapsed by `_g4_merge` to exactly one row
  per (security, date). Harmless. A 10-02 object even carries a null `px_close` and a second carries a
  duplicate revision; the merge resolves both to the correct 34.32.
- **Price LEVELS and currency are sound.** 28.06 HKD / 7.78 x 20 = 72.1 against the ADR's 70.11; the 20:1
  LNVGY ratio holds at both ends of the 251-date span. No scale or FX defect.

## The root is the one-calendar design, not a typo

`lib/trading_calendar.py` declares itself *"Shared NYSE trading-day calendar -- the ONE definition of
'trading day' ... for the whole estate"*. It holds no non-US exchange. A single-calendar frontier is
correct for a US-only book and silently wrong the moment the book holds Hong Kong, Seoul, London and
Paris. The pull inherits one capture time and one T-1, and no instrument-level venue clock exists to
contradict it.

## The correction, and why I did not make it

**Today's BDH backfill already wrote CORRECT values across 251 dates.** The right data is in the bucket.
But `drop_backfill` excludes `as_of_source == "backfill"` rows from the rankings by design (*"the dialog's
price curve reads them, the rankings never do"*), so **the rankings still read the shifted pull values and
ignore the correct backfill ones.**

Three separate acts, none of them mine to take alone:
1. **Code:** the daily pull needs a per-venue capture/attribution rule. Producer's owner.
2. **Served data:** superseding pull rows needs the never-widen pair; a delete needs Andrew.
3. **Policy:** whether the rankings should prefer a correct backfill close over a wrong pull close on a
   past date. That is a `drop_backfill` ruling, not a data fix.

## A correction I owe my own earlier escalation

I told `1.0.0_SA_CTO~Z` (35393) that my step-1 write "cost the 2026-09-29 rankings 650 price cells" and
framed it as a regression I caused. **The coverage number is right and the framing was wrong.** Those 650
cells were the SHIFTED values. Losing them removed incorrect prices; the merge now serves the correct
35.48 for Lenovo there. It is a coverage decrease, not a data-quality regression, and I had not yet
measured the values when I called it one.

## 7. CORRECTION (2026-10-17 ~06:5xZ): "US is correct" was WRONG, and the rule is about CAPTURE TIME

**Sections 1-6 above say US names are correct. That is true only for a run captured at ~11:00Z, and I
reached it unsoundly: every ADBE US row I checked was a `backfill` row, correct by construction, so I had
not tested a single US PULL row when I wrote it.**

Measured since, on US PULL rows against BDH:

| security | 2026-10-13 (captured 11:07:57Z) | 2026-10-14 (captured **14:35:28Z**) | 2026-10-15 (captured 11:09:18Z) |
|---|---|---|---|
| ABNB US | 165.58 **correct** | 169.59 vs true 167.06 **wrong** | 174.28 **correct** |
| ADP US | 275.90 **correct** | 288.50 vs true 280.32 **wrong** | 285.65 **correct** |
| ALNY US | 223.82 **correct** | 231.06 vs true 224.47 **wrong** | 234.03 **correct** |
| ACGL US | 96.85 **correct** | 100.24 vs true 97.60 **wrong** | 99.31 **correct** |
| ABX/TD/SHOP CN | **correct** | **wrong** (same pattern) | **correct** |

The capture instants come from the rows' own `revision` / `produced_at`: `20261014T110757Z`,
`20261015T143528Z`, `20261016T110918Z`. **The daily job's capture time DRIFTS between runs**, and the
14:35Z run lands mid-session in New York and Toronto.

### The corrected rule

**A snapshot row is correct if and only if the capture instant falls AFTER the venue's last close and
BEFORE its next open, on the date it is filed under.** There is no venue for which this holds
unconditionally, because the capture time is not fixed. At ~11:00Z: North America correct, Asia shifted
one trading day, Europe intraday. At 14:35Z: **North America intraday as well.**

### What this changes in the fix and the test

- The attribution MUST be computed from the ACTUAL capture timestamp against the venue's own calendar,
  never from an assumption about when the job runs. A per-venue map alone is insufficient if it assumes
  11:00Z.
- The acceptance test in section 4 MUST include a LATE-CAPTURE day (2026-10-14 is a measured example) and
  a US name. A test using only 11:00Z days and non-US names passes while the US defect stands, and a test
  using only US names on 11:00Z days passes while everything stands.
- Section 3's point 3 is reinforced, not weakened: no single capture instant is correct for all venues,
  and an unpinned capture time is not correct for ANY venue reliably.
