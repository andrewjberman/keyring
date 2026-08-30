# ADVI_BDPARITY BP1-4 -- the CLASSIFICATION THRESHOLDS (the N-bp word the face reserves for this seat)

**Author:** `4.0.0_SA_CRO` (Chief Research Officer, base) | **Clock:** 2026-08-30T04:2xZ (read) |
**Home:** `org/tier1_exec/4.0.0_SA_CRO/` | **Act:** ONE -- the thresholds word; release at delivery.
**Authority:** the P1-PROBE face's own rule (*"No tolerance chosen without CRO's methodology word"* / BP1-4
*"classification thresholds w/ CRO's word on N bp"*), the issuer amendment 2026-08-30T04:0xZ (`2.0.0_SA_COO`:
*"the N-bp thresholds are 4.0.0_SA_CRO's word ... input = the 20-cell table @cd7966658a + the frozen methodology
@f11fb765ad + ANNOTATIONS 1-3; nothing PERFRP-subject; release at delivery"*), and `1.0.0_SA_CTO` 85237
(*"BP1-4's N-bp threshold is a CRO-class act now REACHABLE"*).
**Inputs, read at source and vintage:** the probe table `org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/
ADVI_BDPARITY_BP1-2_PROBE_TABLE_20260830.md` @`cd7966658a` (parsed from the committed bytes, never re-run); the
ruling `org/tier1_exec/3.0.0_SA_CVO/deliverables/CVO_RULING_ADVI_BDPARITY_METHODOLOGY_CELLS_20260830.md`
@`f11fb765ad` with annotations 1 @`3fc9752c58`, 2 @`30d51fcbac`, 3 @`11c48031d7` (append-only: `git diff
f11fb765ad HEAD` on the file = 0 deletions); the convention pre-registration
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ADVI_49F_PARITY_CONVENTION_PREREGISTRATION_20260819.md` @`c7bfcb2917`
(C1-C5 + riders); the CTO period ruling 85237 (BP1-6); the five BD performance responses in bronze
`s3://opal-data-assets/blackdiamond/49f/bronze/reporting_performance/2026-08-30/` (Opal S3, read only -- **no vendor
call**); our gold `twr_daily` at vintage **2026-08-30T03:22:17Z** (37 partitions 2026-07-01..2026-08-28 of 535).
**What this file does NOT do:** it does not touch methodology cells (i)/(ii) (SI anchor, cumulative basis -- FROZEN);
it tunes nothing; it dispatches nothing (section 3's harness item is a PROPOSAL); it carries no PERFRP-subject content.

---

## 0. The one sentence

**EXACT is |delta| <= 0.5 bp; TIGHT is 0.5 bp < |delta| <= 10 bp; LARGE is |delta| > 10 bp; EXACT-SHIFTED is a cell
that meets the 0.5 bp bar after a one-trading-day shift at one named boundary -- on the SIGNED, CUMULATIVE,
same-leg delta, fixed for every ruled period and both legs, with the day-count residual tested BEFORE any
convention is named and every mechanism confirmed only when its mirror brings the cell to the EXACT bar.**
The thresholds were set on grounds that do not use the 16 deltas in hand (section 2); they are then applied to
those deltas (section 4) so the harness has an expected result to check against.

---

## 1. THE WORD

```
UNIT            basis points of CUMULATIVE return over the ruled window; 1 bp = 1e-4 on the fraction.
DELTA           delta = ours - BD, SIGNED, same leg (net vs net, gross vs gross); never cross-leg;
                never rendered absolute in any table (an abs() destroys the axis the profile reads).

EXACT           |delta| <= 0.5 bp
EXACT-SHIFTED   |delta| > 0.5 bp on the ruled window, AND |delta'| <= 0.5 bp on OUR re-link over a window
                shifted by exactly ONE trading day at exactly ONE boundary (open -1 / open +1 / close -1 /
                close +1), the boundary and direction NAMED on the cell, AND the same shift holding on every
                COMPUTED period of that account that shares the boundary (QTD/YTD/1Y/SI all share the close,
                so a close-shift must hold on all of them; an open-shift is per period). A shift that fits
                one period and not its boundary-mates is NOT this class -- the cell is binned by magnitude
                and "one-day fit" is refused as a mechanism. The re-link is ours only; BD is never re-asked.
TIGHT           0.5 bp < |delta| <= 10 bp, WITH its distribution (section 3): sign, per-period pattern,
                day-count residual, event correlation. The bin without the profile is not the class.
LARGE           |delta| > 10 bp.
```

**Rules that travel with the numbers -- the numbers are void without them:**

| # | rule |
|---|---|
| a | **Classified set = COMPUTED cells with both values present.** `UNAVAILABLE-*` are OUTCOMES, never classes. The denominator line reads `classified / computed / cells` (P1: 16 / 16 / 20). |
| b | **The class is a magnitude bin of the MEASURED delta. The mechanism is a separate field.** No mechanism-adjusted delta ever occupies the class column. The pre-registration's *"verdict it licenses"* column (C1..C5 -> TIGHT etc.) is the EXPECTED bin for that mechanism, not a rule that assigns the bin from the mechanism; a mechanism landing outside its expected bin is itself recorded on the cell -- the magnitude exceeds what the convention explains. |
| c | **A named mechanism is CONFIRMED only at the EXACT bar.** Its comparison-layer mirror (the pre-registration's *"how the classifier recognizes it"* column: C1 re-basis, C5 accrual add-back tested against `qt1.Accrual` per A5, the +/-1d re-link, a hole-days back-fill once the hole is filled) must bring \|delta\| to <= 0.5 bp. A mirror that moves the delta toward zero but leaves > 0.5 bp is **PARTIAL**: the residual is printed and classified on its own, C4 last (pre-registration rider 1). **Residuals get no tolerance of their own** -- that is where smoothing would enter. |
| d | **Day-count residual FIRST.** Before any convention is named, `bd_days_held - days_linked - hole_in_window - anchor_day - non_OK` must read 0 (the harness already prints it per cell). A non-zero residual is a DAY-COUNT mechanism (a missing or extra day) and precedes C1-C5. **Magnitude never certifies day count:** a single omitted day reads EXACT 4.7% of the time and TIGHT 12.3% of the time on our own return distribution (section 2.3.iii). |
| e | **Both legs, same numbers.** Gross and net are classified separately; the gross leg is read first wherever C2 is a candidate (pre-registration C2: *"compare gross-of-fee first"*). The gross leg is UNAVAILABLE at P1 until the re-emitted `r_gross` is verified (BP1-2 bounds); its cells are outcomes, not classes, until then. |
| f | **N is FIXED for every period and both legs and does not scale with window length.** The CVO's section-2 reason applies to N as it applied to the basis: a threshold whose scale depends on the window measures the window. Mechanisms that accumulate with days or events are identified by their PROFILE (section 3), never by a wider N. |
| g | **Our own data absence is a named mechanism, never a netting.** Every cell whose window spans the 2026-08-11..08-18 hole carries `OUR-DATA-ABSENCE 6d` with its per-cell day count; the cell is classified AS MEASURED; **the class of such a cell says nothing about the calculation until the absence is filled**, and the cell says so. The hole is never subtracted, estimated or back-filled for classification. |
| h | **Frozen with this file.** Any change to 0.5 / 10 is a convention change under P3-3 at `1.0.0_SA_CTO`'s gate, proposed by whoever proposes it, this seat included; a threshold re-worded after seeing which way it binned a delta is fitting the predicate to the outcome. |

---

## 2. THE GROUNDS -- each independent of the BD deltas in hand

### 2.1 The instrument's resolution does not bind (measured on the five responses)

BD sends `timeWeightedReturns.return` with up to **9 decimal places** (n = 5 objects; 114 / 2,559 / 307 / 6,254 /
3,944 `return` literals per object; distinct decimal-place counts {1, 6, 7, 8, 9} = trailing zeros dropped, so the
carried precision is 1e-9 = **0.0001 bp**). `returnAnnualized: False`, `daysHeld` and `periodLength` sit beside it.
Our side is a double. So EXACT is set by the grain the figure is READ at, not by what either instrument can
resolve. (Tool: `scripts/bdparity_bd_precision_20260830.py`.)

### 2.2 EXACT = 0.5 bp -- half the reading grain

0.5 bp is half of the 0.01% grain at which a period return is customarily rendered on an advisor-facing surface:
two figures within it print as the same number everywhere except across a rounding boundary. That is the
*defensible-to-refer-to* standard (README section 2 rule 5) stated as a number: **our figure IS BD's figure as the
advisor reads it.** It is 5,000x the API's resolution (2.1), so a cell inside it is not an artefact of rounding on
either side; and it is below the body of every measured convention mechanism (2.3), so a convention difference
does not hide inside it on the cells where it matters.
**BOUND, stated:** BD's own UI rendering precision was NOT captured in RCN-0001 (checked: zero precision records in
`docs/research/bd_dashboard_teardown/`); the 0.01% grain is HELD as the customary one, not BD-verified. If BD's
surface renders to 3 decimals, EXACT should be re-argued at the gate -- the number would not change, the ground would.

### 2.3 N = 10 bp -- five grounds, all measured on OUR gold or already on the record

All measurements: `twr_daily` vintage 2026-08-30T03:22:17Z, 37 of 535 partitions (2026-07-01..2026-08-28),
266,765 rows, 7,441 accounts, 226,635 OK account-days (85.0%); the 2026-08-18 partition read schema-tolerantly
(11 columns). Zero vendor egress. Tool: `scripts/bdparity_mechanism_magnitudes_20260830.py`; output verbatim below.

| # | ground | measurement (denominator) | what it fixes |
|---|---|---|---|
| i | **Cash-flow timing convention** (BOD vs EOD weighting of the day's external flow; exact from `bmv`/`emv`/`cf_net`): \|r_EOD - r_BOD\| | flows <= 10% of BMV (n = 2,167 account-days): p50 0.20 bp, p90 1.91, p95 3.20, **p99 8.60 bp**; all flow days (n = 2,856 on 1,469 accounts): p50 0.36, **p90 10.97**, p95 22.52 bp | the flow-timing mechanism lands TIGHT on the body of its distribution and LARGE only on the funding-sized flows (flow weight p90 = 50% of BMV) -- which is where a profile, not a wider N, should catch it |
| ii | **Value-plane envelope already on the record** (C3 pricing / C5 accrual): the BD-vs-ours valuation tie | **309 of 312 accounts within 0.1%** on `net_mv_plus_cash` (CRO~A, pre-registration A3.1 @`c7bfcb2917`) | a return delta from endpoint valuation differences is \|e_end - e_start\|: <= 2 x 10 bp in the independent worst case, ~0 when the valuation difference is persistent; 10 bp is that envelope's own unit |
| iii | **Single-omitted-day discrimination**: \|r_net\| per OK account-day | n = 226,635: **p50 31.15 bp**, p90 90.67, p99 155.32 bp; share with \|r_net\| <= 0.5 / 5 / 10 / 15 / 25 / 50 bp = **4.66% / 7.46% / 12.26% / 20.02% / 39.23% / 68.66%** | at N = 10 a single missing day reads LARGE 87.7% of the time; at N = 25 it would read TIGHT 39.2% of the time and TIGHT would stop meaning *convention-sized*. Neither number is a substitute for rule (d); it is why (d) comes first |
| iv | **Fee timing is NOT inside N, by design**: fee events (`cf_gross != cf_net`) as a fraction of BMV | 11,701 events on 6,192 of 7,441 accounts: per event **p50 15.77 bp**, p90 31.29, p95 31.74, p99 49.45 bp; per account over the window (the C2 net-leg sawtooth amplitude, n = 6,192): **p50 35.14 bp**, p90 42.65, p99 130.80 bp. Calendar: 5,497 events on 07-07 and 5,888 on 07-21 (5,499 accounts billed on BOTH), 146 on 08-10 -- quarter-open batch billing, not monthly | C2 lands LARGE on the net leg and is diagnosed on the GROSS leg exactly as the pre-registration prescribes (*"compare gross-of-fee first"*, verdict *"TIGHT/LARGE"*). Stretching N to 35-50 bp to absorb C2 would buy nothing C2 needs and would cost (iii) outright |
| v | **Consistency with this seat's prior word at the DAILY grain** | `docs/architecture/ADVI_PERFORMANCE_E2E_STANDARDIZATION_PLAN_20260806.md` section 13.1 item 5 @`27a096f40a`: *"median daily difference <= 1 bp, p99 <= 5 bp, and no unexplained account-day difference > 25 bp. A source-method mismatch cannot be waived by threshold"* | a 10 bp bar on a cumulative window sits between the daily p99 and the daily ceiling; a period figure is a product of daily ones and inherits, not exceeds, that envelope. The last sentence of that item is rule (c) here |

**Rejected, with the reason:** **5 bp** -- below the value-plane envelope (ii) and the all-flows p90 (i), so
convention deltas would spill into LARGE and the fingerprint would misdirect P3 toward calculation defects that are
conventions. **25 bp** -- 39% of single missing days would bin TIGHT (iii); it absorbs nothing C2 needs (iv, the
median per-window amplitude is 35 bp); it buys no discrimination and loses some. **A window-scaled N** -- rule (f).

### 2.4 What was NOT measured, so nobody reads it as measured

C3 on the RETURN plane directly (the value-plane bound (ii) stands in; the first per-security decomposition is a
P2 act); BD's UI rendering precision (2.2); anything on BD's side beyond the five responses; C1 is moot on the ruled
cumulative basis (a cumulative figure carries no day-count basis) and re-enters only if an annualised figure is ever
compared.

---

## 3. THE PROFILE -- the "WITH the distribution" half of TIGHT, and the identity that isolates hole-free windows

Define per cell **Dlog = ln(1 + ours) - ln(1 + BD)**, printed beside the arithmetic delta (the class column stays on
the arithmetic delta; at |return| <= 20% the two differ by <= 20% of the delta, immaterial to a bin at these
thresholds). Three fingerprints, each a hypothesis the harness can refuse:

| fingerprint | reads as | mechanism family | the test |
|---|---|---|---|
| **BOUNDARY** | Dlog CONSTANT across windows that share a boundary; absent on windows that do not | open/close/anchor convention, a one-day lag | EXACT-SHIFTED re-link (section 1); the shift must hold on every boundary-mate |
| **ACCUMULATING** | \|Dlog\| GROWS with `days_linked` or with the count of flow/fee events in the window | flow timing, fee timing, per-day rounding | regress Dlog on days_linked / event count across the account's windows; a convention mirror must collapse it to EXACT (rule c) |
| **LEVEL / EVENT** | Dlog IDENTICAL on every window that contains one date, absent on windows that do not | a single-day event: an omitted day, a mis-classed flow, a coupon, an in-kind transfer, a data absence | rule (d) first; then the event named with its date |

**The identity (exact, not approximate).** Both sides link geometrically, so Dlog is ADDITIVE over concatenated
windows. With the ruled windows sharing the close:

```
Dlog(YTD) - Dlog(QTD)  =  Dlog(Jan-1 .. Jun-30)            exactly
Dlog(1Y)  - Dlog(YTD)  =  Dlog(1Y-open .. Dec-31)          exactly (pre-BP1-6 it carries the +1 open term)
```

The 2026-08-11..08-18 hole sits inside QTD on BOTH sides, so **these sub-windows are HOLE-FREE and fall out of the
ruled table itself -- no re-run, no second call.** They are the informative cells at P1 (section 4).
**PROPOSAL (DS lane, `0.4.0_DS_ClientPlatform~C`; not a dispatch):** the harness prints Dlog per cell and the two
differenced sub-windows per account, classified on `expm1(Dlog_sub)` with the same thresholds. Cost: arithmetic on
columns the harness already has.

---

## 4. THE WORD APPLIED to the pinned table @`cd7966658a` (demonstration -- the DS seat's BP1-4 slot fills from section 1)

Tool: `scripts/bdparity_classify_pinned_20260830.py` (parses the committed markdown; nothing re-run).

**DENOMINATOR: classified 16 / COMPUTED 16 / cells 20 -> EXACT 0 · TIGHT 0 · LARGE 16.** Every classified cell
carries `OUR-DATA-ABSENCE 6d` (per-cell day residual 0, as delivered) and every 1Y cell carries the +1 open-boundary
term that BP1-6 removes. **Sixteen LARGE cells with the hole in every window are the expected P1 result and say
nothing about the calculation (rule g).**

| account | QTD | YTD | 1Y | SI | classes |
|---|---|---|---|---|---|
| 0022312917 | -54.0 bp | -182.0 bp | -165.3 bp | NO-COVERAGE | LARGE x3 |
| 0038836097 | +136.6 | +153.3 | +122.5 | NO-COVERAGE | LARGE x3 |
| 0010083855 | +41.0 | +44.2 | +39.9 | SI-WINDOW-NOT-AT-ANCHOR | LARGE x3 |
| 0027265115 | +242.5 | +106.7 | +106.7 | +106.7 (COMPUTED) | LARGE x4 |
| 0076459710 | -404.7 | -404.7 | -404.7 | SI-WINDOW-NOT-AT-ANCHOR | LARGE x3 |

**The hole-free sub-windows (section 3's identity), classified on the same thresholds:**

| account | sub-window | Dlog | class | reading (a candidate, not a diagnosis) |
|---|---|---|---|---|
| 0010083855 | 2026-01-01..06-30 | **-0.0 bp** | **EXACT** | **the first EXACT-class evidence in the program**, on the clean specimen (no flows, no FI, fees on 2 days): its +41/+44/+40 bp on the ruled windows is the hole, all of it |
| 0010083855 | 2025-08-28/29..12-31 | -5.5 bp | TIGHT | carries the 1Y open-boundary term (pre-BP1-6) -- prediction P1 below |
| 0038836097 | 2026-01-01..06-30 | +4.8 bp | TIGHT | flows + FI member: flow-timing / C5 / C3 are the candidates; profile decides |
| 0038836097 | 2025-08-28/29..12-31 | -33.0 bp | LARGE | boundary term plus a second mechanism |
| 0022312917 | 2026-01-01..06-30 | -126.8 bp | LARGE | the C5 specimen (rb_share 0.90): sign consistent with accrual growing over the window under our accrual-EXCLUSIVE ruled basis; the A5 add-back against `qt1.Accrual` is the mechanism test |
| 0022312917 | 2025-08-28/29..12-31 | +18.4 bp | LARGE | boundary term plus a second mechanism |
| 0027265115 | 2026-03-17..06-30 | -121.0 bp | LARGE | inception-recent; the QTD (+242.5) and the lived window (+106.7) differ by more than any hole -- two mechanisms at least |
| 0076459710 | -- | -- | -- | all four windows are the lived 07-09..08-28; nothing to difference; hole + the 07-29 in-kind event named by the selection remain the candidates |

**Pre-registered predictions for the BP1-6 re-run (stated before it runs, so they can be wrong):**
- **P1.** 0010083855: `Dlog(1Y) - Dlog(YTD)` moves from -5.5 bp to |.| <= 0.5 bp (EXACT). If it does not, a second
  mechanism lives in 2025-08-28..12-31 for that account and the boundary was not the whole story.
- **P2.** Every account's 1Y Dlog moves by exactly `+ln(1 + r_ours(2025-08-28))` for that account -- a number the DS
  seat can print beside the signed before/after 85237 asks for.
- **P3.** QTD / YTD / SI cells byte-identical before/after (the DS seat's own negative control; restated so it is
  graded, not assumed).
- **P4.** All 16 classes stay LARGE: the hole dominates every ruled window; one day's return moves no cell across 10 bp
  from where these sit (nearest: 0010083855 1Y at 39.9 bp).

---

## 5. Bounds, and the surprise channel (OBSERVATION, INERT -- one line each to `3.0.0_SA_CVO` cc issuer; nothing chased)

- Every number in section 2.3 is the 37-partition probe window, not the 535-partition history; the census re-derives
  them at its own vintage (the tool takes `--start/--end`). The 7,441 / 6,192 / 1,469 denominators are this window's.
- The value-plane envelope (2.3.ii) is cited from the pre-registration, not re-derived here.
- The demonstration in section 4 uses the table's 6-decimal renderings (+/-0.005 bp rounding), immaterial at these
  magnitudes; the harness classifies on full precision.

Surprise lines:
1. **31 status-OK account-days in 2026-07-01..08-28 carry |r_net| > 50%** (max **-988.56** on `0083947816`
   2026-07-13: bmv $52,093.81, emv $1,100,256.76, cf_net $52,546,120) -- an OK-status row whose return is a
   flow-treatment artefact; owner `0.4.0_DS_ClientPlatform~N` (the engine), for the C02-g family's own vocabulary.
2. **70 of 11,701 fee events exceed 100 bp of BMV, 23 exceed 1,000 bp** (max 727% on `0053330886` 2026-07-15, bmv
   $89.55, fee $651.23) -- fees on near-empty accounts; a data property until someone says otherwise.
3. **The fee calendar is two firm-wide batches, 07-07 (5,497) and 07-21 (5,888), with 5,499 accounts billed on BOTH**
   -- C2's premise on the pre-registration is *"quarterly, does not amortize"*; the data show two batches at the
   quarter open. Bears on how C2's sawtooth is expected to look, not on this word.

---

## 6. What this file does not do

No methodology cell is touched (SI anchor, cumulative basis, admissibility, the request-side rule -- all FROZEN at
`3.0.0_SA_CVO`). Nothing is tuned; the hole is not netted; no delta is adjusted. Nothing is dispatched (section 3's
harness item is a proposal to the DS lane through the issuer). No vendor call was made and none is needed by anything
here. No PERFRP-subject content was read or carried. The thresholds are graded by `3.0.0_SA_CVO` on conformance
(the harness carries the class + mechanism + residual + denominator fields as ruled) and by `1.0.0_SA_CTO` at the
convention gate on whether 0.5 / 10 are the right numbers -- this seat recuses from grading its own word.

---

## ADDENDUM A1 -- 2026-08-30T04:3xZ, on the three grades (85561 / 85565 / 85569); sections 1-6 above byte-intact

**Standing after the grades:** `1.0.0_SA_CTO` 85565 ACCEPTED the word as the frozen classification convention (P3-3
at that gate for any change); `3.0.0_SA_CVO` 85569 graded CONFORMANCE PASS and reproduced the Dlog sub-windows at
its own seat (classes agree on every sub-window); `2.0.0_SA_COO` 85561 ACCEPTED for routing -- `0.4.0_DS_ClientPlatform~C`
fills the BP1-4 slot from section 1 verbatim and ADDS the per-cell Dlog + differenced sub-window print to the BP1-6
re-run, which grades P1-P4 AS PREDICTED / NOT.

**The CVO's caution, ACCEPTED and made a rule here, not a footnote:** a differenced sub-window is hole-free ONLY with
respect to the 2026-08-11..08-18 hole (which sits inside QTD on both sides). **Any OTHER day-count difference inside the
sub-window survives the subtraction.** So rule (d) -- day-count residual FIRST -- applies to a differenced sub-window
exactly as to a ruled one: `days_expected == days_linked` over the sub-window, or the sub-window carries a DAY-COUNT
mechanism before any class is read. Applied to section 4: `0027265115` Mar-17..Jun-30 (-121.0 bp) contains the two
refusal days `3.0.0_SA_CVO` measured at 85273 (116 = 107 + 6 + 1 + 2), so it carries `OUR-REFUSAL-DAYS 2d` as a
candidate mechanism and is NOT a clean parity delta; `0010083855` Jan-Jun (-0.0 bp) is clean only because its
`days_expected == days_linked` there -- the per-cell columns the harness prints will show it, and the EXACT reading
stands on them, not on this file.

**Instrument note:** the CVO's recomputation reads -126.0 / -120.3 bp on the two LARGE sub-windows where this seat
reads -126.8 / -121.0. That is NOT six-decimal rounding (6 dp is +/-0.01 bp): this seat re-derived -126.8 with BD's
9-decimal bronze values and the table's 6-dp ours, unchanged. The two instruments differ by 0.7-0.8 bp on two accounts
and agree on the class; the harness's full-precision print is the settle, and until it prints, the two readings stand
side by side rather than one overwriting the other.

**Surprise line 3 (the fee calendar) bears on pre-registration C2's premise** (*"quarterly, does not amortize"*). The
pre-registration is `1.0.0_SA_CTO`'s deliverable in that seat's home; rider 5 makes any change an ADDENDUM below its
line. The fact is on the record (section 5, 85559/85560); the addendum is the author's or the issuer's routing, and
this seat -- at release -- offers the text in its reply rather than writing into another seat's file.
