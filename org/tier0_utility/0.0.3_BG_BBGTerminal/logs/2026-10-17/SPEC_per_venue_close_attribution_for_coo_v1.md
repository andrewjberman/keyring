# SPEC for `2.0.0_SA_COO~V1`: file each close under its own venue's trading date

**From:** `0.0.3_BG_BBGTerminal` (site Z). **Routed by:** `1.0.0_SA_CTO~Z` msg 35402 -- the per-venue fix
belongs to ETFS_RIVALS, not to this seat. Rulings `ETFS_RIVALS-Z-S84` @3103085b97, `S85` @05cfab9b91.
**Authority:** Andrew, direct to this seat, *"check out that lenovo price history for rivalfunds and get
that corrected properly"*. CTO~Z: *"fix whatever is inside your lane ... hand your measured spec to
COO~V1."* The producer is outside my lane, so this is the handoff, not a request for permission.

## 1. THE DEFECT, measured

The daily market pull captures `PX_LAST` once at ~11:00Z and files it under the **NYSE** T-1 date.
`PX_LAST` is a point-in-time snapshot, so what it means depends entirely on where the instrument trades
at 11:00Z.

| venue class | state at 11:00Z | what gets stored | verdict |
|---|---|---|---|
| US | market not yet open | the genuine prior close | **correct** |
| ASIA | closed hours earlier, same day | **TODAY's close under YESTERDAY's date** | shifted exactly one trading day |
| EUROPE | mid-session | an **intraday** price as if it were a close | matches no close |

Evidence, served `hc.g4_rows` vs Bloomberg BDH `PX_LAST`:
- ADBE US: correct 4 of 4 dates.
- 992 HK, 1 HK, 005380 KS: shifted 12 of 12 date-checks, each served value equal to the NEXT trading
  day's close TO THE CENT. An exact equality across three exchanges is a mechanism, not noise.
- AAF/ADM LN, AI/AIR FP, ALV/BAS GR: match neither the day's close nor the next day's (BAS GR served
  53.01 against a true 52.48 and 52.97). **Intraday-as-close is INFERRED here, not measured** -- I did
  not capture an intraday series. Treat the Asian mechanism as established and the European as a strong
  hypothesis needing one intraday capture to confirm.

Scale, partition 2026-10-15, denominator 760 merged rows: **391 priced by a wrong-for-venue writer**
(170 ASIA measured; 221 other pull-priced, 6 of them verified). ASIA 248 securities / US-CA 236 / OTHER
276, where OTHER is LN 53, FP 32, GR 29, NA 15, SW 14, BZ 14, SM 13, SJ 9, IM 9, NO 8, MM 7, DC 7, AB 6,
unparsed 25.

## 2. ROOT CAUSE

`lib/trading_calendar.py` declares itself *"Shared NYSE trading-day calendar -- the ONE definition of
'trading day' / 'expected priced frontier' / 'trading days behind' for the whole estate"* and holds no
non-US exchange. One calendar is correct for a US-only book and silently wrong once the book holds Hong
Kong, Seoul, London and Paris. Nothing in the pull can contradict it, because no instrument-level venue
clock exists.

**This is why it reads as healthy:** every row carries `claim: MEASURED` and a real vendor timestamp. The
value IS measured. Only its DATE is wrong, and no field in the schema can express that.

## 3. THE FIX SHAPE (CTO~Z's words, with the detail I measured)

1. **File each close under its own venue's trading date.** The pull needs a venue -> calendar/timezone
   map, keyed off the Bloomberg exchange code (the second token of the ticker). The attribution date is
   the last COMPLETED session of THAT venue as at capture time, never NYSE T-1.
2. **Re-source the history from BDH.** `historical_data` returns a close already bound to its own
   session date, so it is immune to this defect by construction -- which is exactly why today's backfill
   rows are correct where the pull rows are not.
3. **Do not fix this by moving the capture time.** No single UTC instant is simultaneously after the
   Asian close and after the European close and before the US open. A one-shot capture cannot be correct
   for all three; the attribution must be per venue, or the pull must be per venue.

## 4. ACCEPTANCE TEST, reusable as written

For a sample spanning all three classes, assert `served px_close == BDH PX_LAST` for the SAME date:

```
hc.g4_rows(sink, day) -> px_close for <security>
bloomberg_historical_data([<security>], ["PX_LAST"], day, day)
```

The sample must include at least one US, one Asian and one European name, because a US-only sample passes
today. Add a NEGATIVE CONTROL: assert the served value does NOT equal the next trading day's close --
without it, a test that merely finds "a plausible price" passes against the shifted data.

## 5. WHAT MUST NOT BE "FIXED" -- each of these looked like a defect and is not

- **The 10 dates 992 HK is missing** (2025-10-29, 2025-12-26, 2026-02-17/18/19, 2026-04-06/07,
  2026-05-01, 2026-07-01, 2026-10-01) are ALL Hong Kong public holidays. Correct absences. Filling them
  would invent trading days. Note this is also the trap the NYSE-only calendar sets: a freshness checker
  on that calendar flags 992 HK stale on every HK holiday.
- **Duplicate objects** on 2026-09-29 and 2026-10-02 are collapsed by `_g4_merge` to exactly one row per
  (security, date); one 10-02 object carries a null `px_close` and another a duplicate revision, and the
  merge still resolves to the correct 34.32. No de-duplication work is owed.
- **Price levels and FX are sound.** 28.06 HKD / 7.78 x 20 = 72.1 against the ADR's 70.11; the 20:1
  LNVGY ratio holds at both ends of the 251-date span.
- **2026-09-29 served data:** CTO~Z ruled no corrective timed object and no delete (S85). Do not restore
  the 650 ranking cells that partition lost -- they held the SHIFTED values.

## 6. THE OPEN POLICY QUESTION, which is not a data fix

Today's BDH backfill wrote correct closes across 251 dates, so **the right data is already in the
bucket.** But `drop_backfill` excludes `as_of_source == "backfill"` from the rankings by design (*"the
dialog's price curve reads them, the rankings never do"*). So the rankings still read the wrong pull
values and ignore the correct backfill ones. Whether a correct backfill close should outrank a wrong pull
close on a PAST date is a `drop_backfill` ruling for ETFS_RIVALS, and S85 declined the naive read-side
version of it. Flagging it as owed, not proposing it.

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
