# ETFS_POSITIONING L1-2 -- PRE-FIRE-1 WRAPPER-LOG BASELINE

**Captured** 2026-08-21 ~2011Z by `2.0.0_SA_COO~Z`, **before** the first countable fire (08/22 07:00).
**Why this exists:** after 08/24 the pre-existing directory state is unrecoverable from the directory
itself -- the 30-run prune will have consumed the oldest entries. A Monday certifier needs to know what
was already there in order to identify what is new **by exclusion** rather than by trusting a filename.

**Inventory anchor** (sha256 of the sorted name list): `9A64EBDD91979ACBCAECE0785040003C005ADB43270A70184161F92454E9F7E8`
**Denominator:** 30 files, window 2026-08-05 .. 2026-08-21.

## Finding 1 -- the weekend interactive-logon flag is DISCHARGED

`0.7.0_AE_CloudOps~Z` flagged that the task runs `LogonType=Interactive` and that weekend survival was
UNTESTED. **It was already tested, four times:** `20260808` (Sat), `20260809` (Sun), `20260815` (Sat),
`20260816` (Sun) each produced a 07:00 log. The flag was right to raise; the history answers it.

## Finding 2 -- TWO WEEKDAY 07:00 FIRES ARE MISSING

| date | dow | 07:00 log |
|---|---|---|
| 08-11 | Tue | **ABSENT** -- no runs at all that day |
| 08-13 | Thu | **ABSENT** -- but a 17:45:54 hand run exists, so the box was up |

**Not a pruning artifact.** Surviving files run continuously 08-05..08-21 and a 30-run prune removes
oldest-first; it cannot punch holes in the middle. `08-05` also lacks a 07:00 log and **is excluded** --
it sits on the retention boundary. Denominator **16**, not 17.

**Observed per-fire rate: 14/16.** L1-2 requires **three consecutive**.
No independence claim is made: **misses may cluster** (a box that is off is off for a span, and one
outage spanning Sat-Sun-Mon takes all three fires), which makes the joint tail *worse*, not better.

**Cause of either miss: UNDETERMINED.** Not diagnosed here and not inferred from this device's
freeze history.

## Bound

Measured: the full inventory (names, sizes, mtimes), day-by-day presence of a 07:00-stamped log, window
continuity, and the 08/13 hand run proving the box was up. NOT measured: why either fire is missing;
whether a log can be created then deleted; whether a fire could run while failing to write a log at all
-- that last would make this an **under**-count of fires, so it does not weaken the finding.

## Full inventory as of capture

| file | dow | size | class |
|---|---|---|---|
| `bbg_tplus1_20260805_082500.log` | Wed | 1,465 B | other |
| `bbg_tplus1_20260805_090020.log` | Wed | 2,778 B | other |
| `bbg_tplus1_20260806_070001.log` | Thu | 6,129 B | 07:00 fire |
| `bbg_tplus1_20260806_091456.log` | Thu | 4,799 B | other |
| `bbg_tplus1_20260806_091731.log` | Thu | 5,911 B | other |
| `bbg_tplus1_20260806_091953.log` | Thu | 5,993 B | other |
| `bbg_tplus1_20260806_111816.log` | Thu | 5,985 B | other |
| `bbg_tplus1_20260807_070001.log` | Fri | 4,635 B | 07:00 fire |
| `bbg_tplus1_20260808_070001.log` | Sat | 4,635 B | 07:00 fire |
| `bbg_tplus1_20260809_070001.log` | Sun | 9,751 B | 07:00 fire |
| `bbg_tplus1_20260810_070002.log` | Mon | 4,251 B | 07:00 fire |
| `bbg_tplus1_20260812_070000.log` | Wed | 8,112 B | 07:00 fire |
| `bbg_tplus1_20260813_174554.log` | Thu | 8,106 B | other |
| `bbg_tplus1_20260814_070001.log` | Fri | 12,565 B | 07:00 fire |
| `bbg_tplus1_20260814_114706.log` | Fri | 4,647 B | other |
| `bbg_tplus1_20260815_070001.log` | Sat | 13,919 B | 07:00 fire |
| `bbg_tplus1_20260816_070001.log` | Sun | 13,920 B | 07:00 fire |
| `bbg_tplus1_20260817_070001.log` | Mon | 13,920 B | 07:00 fire |
| `bbg_tplus1_20260817_134429.log` | Mon | 4,883 B | other |
| `bbg_tplus1_20260818_070001.log` | Tue | 4,883 B | 07:00 fire |
| `bbg_tplus1_20260818_135338.log` | Tue | 4,498 B | other |
| `bbg_tplus1_20260819_070001.log` | Wed | 3,481 B | 07:00 fire |
| `bbg_tplus1_20260819_084944.log` | Wed | 4,883 B | other |
| `bbg_tplus1_20260819_102143.log` | Wed | 4,498 B | other |
| `bbg_tplus1_20260820_070001.log` | Thu | 6,191 B | 07:00 fire |
| `bbg_tplus1_20260821_070001.log` | Fri | 4,984 B | 07:00 fire |
| `bbg_tplus1_20260821_105844.log` | Fri | 1,218 B | other |
| `bbg_tplus1_20260821_105845.log` | Fri | 738 B | other |
| `bbg_tplus1_20260821_105846.log` | Fri | 1,145 B | other |
| `bbg_tplus1_20260821_105847.log` | Fri | 1,625 B | other |
