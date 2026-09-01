# ETFS partner-ownership tracking — STATE OF THE SYSTEM

**Author:** `4.0.0_SA_CRO` · **Date:** 2026-09-01 · **Andrew-direct** (verbatim): *"research the ETFS_CANON
and the state of our tracking methodology for partner ETFS ownership. I need to present a monthly report for
August and July for our CFO with the partner daily holdings and average holdings. Before doing so, as our
capabilities have improved substantially i think we need to get establish the state of this system."*

> **CLASS: MEASUREMENT + ASSESSMENT.** Nothing here changes a served artifact, re-renders a report, notifies
> a partner, or restates a figure. Every act below that would move data is listed as a PROPOSAL for Andrew's
> word (CRO proposes on the build side; §3 of the CRO README).

---

## 0. HEADLINE — four sentences

1. **The monthly report system is LIVE, SCHEDULED, and has already produced both months you asked for**:
   `platinum/reports/2026-07/` (rendered 2026-08-01T14:00:56Z) and `platinum/reports/2026-08/`
   (rendered **2026-09-01T14:02:21Z — today**), each an HTML + PDF + three per-partner daily CSVs.
2. **August is sound.** An independent recompute from the live daily slices reproduces the served August
   report to **$0.00 across all 12 partner×ETF cells**.
3. **July is STALE against its own source data by +$497,352.47 (+0.082%)** — a backfill of 8 daily slices
   landed **4h 10m AFTER** the July report was rendered, and the report has never been re-rendered.
4. **`ETFS_CANON` itself was never built** — its deferral condition fired, nobody picked it up, and the
   gold table its design gate ruled (`gold/ownership_daily/`) does not exist in the bucket.

---

## 1. WHAT ACTUALLY EXISTS TODAY (measured, not recalled)

**Bucket `opal-data-etfs` — 1,257 objects** (two list pages of 1000 + 257; `--query length()` returns the
PAGE count, so the single-number form would have said 1000. Rule 22a.)

| Layer | Key | State |
|---|---|---|
| **Daily slices** | `daily/{49financial,cottonwood,inflection}/{date}.json` | **LIVE.** 84 / 52 / 114 slices. Schema `{schema_version, partner, date, etf_ticker, ownership_value, account_count, source_artifact, source_as_of}` — carries its own provenance. |
| **Daily serving** | `platinum/etf_ownership_dashboard.json` | **LIVE, FRESH** — `generated_utc 2026-09-01T16:00:02Z`, grand total **$657,715,307.12** (point-in-time, not an average). |
| **Monthly report** | `platinum/reports/{YYYY-MM}/etf_ownership.{html,pdf}` + 3 CSVs | **LIVE, SCHEDULED** — fires on the 1st, ~14:00Z, for the prior month. 2026-05 … 2026-08 all present. |
| **Gold canonical daily** | `gold/ownership_daily/date={D}/` | ⛔ **DOES NOT EXIST.** `gold/` holds only `_manifests/`, `book/`, `holding/`. This is the ETFS_CANON build that was ruled but never dispatched. |
| **`monthly/` prefix** | — | ⛔ **DOES NOT EXIST.** The `monthly/2026-05.json` / `2026-06.json` artifacts named in the `ETFS_AVGCAP` registry are not in this bucket. The monthly product now lives under `platinum/reports/`. |

**Delivery:** an orchestrator Lambda (`etfs-reports-orchestrator`) starts a transient EC2 box that renders
and uploads under `platinum/reports/`, then emails the PDF + CSVs to `andrew@opalinvest.com` via SES.
IAM is scoped to `opal-data-etfs/platinum/reports/*` only — no firm bucket (NEVER#1 intact).

---

## 2. THE METHODOLOGY, STATED PLAINLY (this is what the CFO is actually being shown)

**The average is a 31-day CALENDAR-day mean with carry-forward — not a trading-day mean.**

Every served CSV carries all 31 calendar days. Non-trading days repeat the prior available value
(49F 07-03/04/05 are all identical to 07-02). Days with no slice are filled the same way.

**Verification that this reading is exact, not inferred:** recomputing August on this basis from the raw
slices reproduces the served report to **$0.00 in all 12 cells**. A wrong basis could not do that.

**It matters, and here is the size of it.** Trading-day-only vs calendar-day, same underlying data:

| Month | Partner | calendar-day (as served) | trading-day only | delta |
|---|---|---|---|---|
| 2026-07 | 49financial | 527,715,910.53 | 528,375,243.69 | +0.125% |
| 2026-07 | **cottonwood** | **31,186,887.06** | **33,783,112.93** | **+8.325%** |
| 2026-07 | inflection | 46,695,709.41 | 46,986,265.28 | +0.622% |
| 2026-08 | all three | 651,880,184.31 | 652,324,891.37 | +0.069% |

⚠ **Cottonwood July swings 8.3% on basis choice alone.** Cause: Cottonwood onboarded *during* July —
DIVZ runs $1.08M (07-01) → $3.30M (07-07) → $14.9M (07-14) → $18.5M (07-28). **A July average for
Cottonwood is a ramp artifact, not a run-rate**, on any basis. Its August average ($52.5M) is the first
clean full month. **This is the single most likely thing to mislead a CFO in the July column.**

---

## 3. THE THREE DEFECTS, RANKED

### 3.1 — JULY IS STALE AGAINST ITS OWN SOURCE (new finding, this session)

The July report rendered at **2026-08-01T14:00:56Z**. A backfill wrote **8 inflection July slices** at
**2026-08-01T18:10:48–18:11:04Z** — 4h 10m later: `07-01, 07-13, 07-14, 07-15, 07-20, 07-21, 07-22, 07-23`.
Cottonwood backfilled similarly. **The report was never re-rendered.**

The served CSV therefore carries 07-10's value flat across 07-13/14/15, while the live slices hold real,
distinct values for those days (DIVZ 17,301,411.87 / 17,221,032.09 / 17,184,824.86).

**Recompute from live slices, today, on the report's own methodology:**

| partner | served July avg | recomputed today | delta | % |
|---|---|---|---|---|
| 49financial | 527,715,910.53 | 527,715,910.53 | **0.00** | 0.000% |
| cottonwood | 31,186,887.06 | 31,242,755.15 | +55,868.09 | +0.179% |
| inflection | 46,695,709.41 | 47,137,193.79 | **+441,484.38** | **+0.945%** |
| **TOTAL** | **605,598,506.99** | **606,095,859.47** | **+497,352.47** | **+0.082%** |

**49financial reconciling to $0.00 is the positive control** — it proves the deltas are in the data, not in
my method. **August's whole-report $0.00 is the second control**: zero slices were written after the August
render, for any partner. *August does not have this problem; July does.*

### 3.2 — THE ORION T-1 LABEL DEFECT IS STILL UNFIXED

`docs/architecture/ETFS_ORION_LABEL_NORMALIZATION.md` + the 2026-08-02 CTO memo established that Orion
returns the prior settled close but stamps it with the **run date**, so inflection's series is labelled one
trading day forward. The portal chain corrects this via `orion_normalize_as_of`; **the ETFS chain does not.**

**Re-measured today: `orion_normalize_as_of` = 0 hits across 19 files in `data/etfs/`.** Thirty days on, the
call count is still zero. The August report rendered today carries the same defect.

⛔ **The consequence the memo calls the larger defect, and I agree: within one monthly file, inflection is on
T-1 while 49financial and cottonwood are on T. The three partners are not on the same date basis in the
artifact that compares them.**

⚠ **DO NOT ADD $424,063 AND $441,484.** The memo's $424,063 (published-vs-true-settled re-dating) and my
$441,484 (served-vs-live-slices staleness) are two different corrections on the same partner-month computed
on different bases; they overlap by an amount I have **not** measured. **Neither number is presentable as a
July inflection adjustment until one basis is chosen and the figure recomputed once.** The memo's own §3
carries this caveat; this is its confirmation, not its discovery.

### 3.3 — COTTONWOOD IS MISSING 5 AUGUST TRADING DAYS, AND THE ARTIFACT CANNOT SHOW IT

Against the NYSE calendar (`lib/trading_calendar.py`; July = 22 trading days, August = 21):

| Month | 49financial | cottonwood | inflection |
|---|---|---|---|
| 2026-07 | **22/22** | **22/22** | **22/22** |
| 2026-08 | **21/21** | ⚠ **16/21** | **21/21** |

Cottonwood missing: `08-04, 08-18, 08-20, 08-21, 08-31`.

⛔ **The carry-forward hides this.** The August Cottonwood CSV shows all 31 days and looks complete; the
missing days are silently filled with the prior value. **A reader cannot see the gap from the artifact.**
Measured effect on the August Cottonwood average is small (**+0.069%** vs trading-day basis) because the
book was flat across those days — but *that is luck, not a control.*

### 3.4 — ONE RESIDUAL NOBODY HAS EXPLAINED (carried forward, still open)

Two different settled trading days with an identical ETF vector to the cent
(17,221,032.09 / 13,502,102.90 / 11,079,105.25 / 6,300,737.41). Confirmed still present in the live slices
(published 07-14 and 07-16). Andrew's standing word: *"holdings should be a raw fact."* **Open. A green
normalization must not be read as having resolved it.**

---

## 4. ETFS_CANON — WHY THERE IS UNADDRESSED WORK

Your read this morning was right, and the register now says why.

- **2026-08-24** — you deferred it: *"We can revisit ETFS_CANON After INGEST is done."*
- The **design gate was RULED** the same day (`ctoZ_TO-D4a...20260824.md`): marquis = the AVGCAP average
  (confirmed); daily canonical form = **S3 gold parquet, NOT DynamoDB** (no new Lambda, no new IAM); one
  scheduled gold writer; full lookback; monthly = platinum JSON + deck, **internal only**.
- **ETFS_INGEST is now complete — the deferral condition fired, and nothing in the estate watches for that.**
  The row simply sat. It was closed by mistake at ~14:0xZ today and you corrected it ~14:1xZ.
- ⛔ **The registry's own `pipeline` field still describes the DynamoDB/fan-in architecture the design gate
  overruled.** Anyone reading the registry row today gets the superseded design.

**So: the design is ruled and current; the build was never dispatched; the record describing it is stale.**

---

## 5. WHAT I RECOMMEND BEFORE YOU PRESENT

Ranked. Items 1–2 are cheap and I can do them on your word; 3–4 are yours.

1. **Present August as the headline month; treat July as the ramp/partial month.** August is
   independently reconciled, complete for 49F and Inflection, and is Cottonwood's first clean full month.
2. **Re-render July** (`platinum/reports/2026-07/`) so the served artifact matches its own source data —
   +$497,352.47, +0.082%. This is a re-render of an internal artifact on data already in the bucket, not a
   restatement and not a partner-facing act. **PROPOSAL — needs your word.**
3. **Decide the date-basis question before any figure goes to a partner or into a rebate.** Inflection on
   T-1 beside two partners on T is the defect that actually matters. Fixing it is a code change to the
   ETFS chain (call `orion_normalize_as_of`), and it moves history.
4. **Say the basis out loud in the report.** "Monthly average = mean of daily ownership value over all 31
   calendar days, non-trading days carried forward." One line. Without it, the Cottonwood July number
   invites a wrong question.
5. **Add a coverage line per partner** ("21 of 21 trading days; 0 carried") so a gap like Cottonwood's five
   August days cannot hide behind carry-forward again.

---

## 6. THE NUMBERS, AS SERVED (what is in the artifacts today)

Monthly average ownership value, calendar-day basis, USD.

| Partner | July 2026 | August 2026 | Δ | Δ% |
|---|---|---|---|---|
| 49 Financial | 527,715,910.53 | 547,008,390.28 | +19,292,479.75 | +3.66% |
| Cottonwood | 31,186,887.06 | 52,488,748.61 | +21,301,861.55 | +68.30% *(onboarding ramp)* |
| Inflection | 46,695,709.41 | 52,383,045.42 | +5,687,336.01 | +12.18% |
| **TOTAL** | **605,598,506.99** | **651,880,184.31** | **+46,281,677.31** | **+7.64%** |

Per-ETF August averages (all partners): DIVZ 222,519,864.21 · IDVZ 185,260,189.04 ·
PFDE 158,241,665.40 · PFOE 85,858,465.66.

⚠ July inflection/cottonwood figures above are the **served** values and are the ones §3.1 shows to be
stale. The Cottonwood MoM +68.30% is an onboarding ramp, not growth.

---

## 7. PROVENANCE

All S3 state read live 2026-09-01 ~15:3x–16:0xZ via `.tools/aws` against `opal-data-etfs`. Trading days from
`lib/trading_calendar.py` (`calendar_source: NYSE/pandas_market_calendars`). Averages recomputed
independently from the raw `daily/{partner}/{date}.json` slices and cross-checked against the served CSVs —
**August reconciles at $0.00 in all 12 cells, and 49financial reconciles at $0.00 in both months; those are
the controls.** Slice-vs-CSV grain spot-checked at `daily/inflection/2026-07-16.json` (matches to the cent).
Census `orion_normalize_as_of -- data/etfs` = 0 hits over 19 files scanned (12 ephemeral-floor files excluded
and not covered by that zero). Registry rows read at `org/projects/ETFS_CANON.json` and `ETFS_AVGCAP.json`.

**NOT measured, and named so it is not assumed:** the overlap between the §3.2 and §3.1 inflection
corrections; whether the July backfill has a recurring cause; whether Cottonwood's five August gaps will
backfill; the `account_count` dimension (present in slices, absent from every served CSV).
