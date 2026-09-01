# BRIEF — ETFS partner-ownership tracking: state, repairs, and what is still open

**Tags:** `ETFS` `ETFS_CANON` `ETFS_TRACKING` `ETFS_AVGCAP` `ETFS_SETUP` `PARTNER_OWNERSHIP`
`JULY_2026` `AUGUST_2026` `2026-07` `2026-08` `CFO_REPORT` `MONTHLY_AVERAGE` `DAILY_HOLDINGS`
`COTTONWOOD` `49FINANCIAL` `INFLECTION` `DIVZ` `IDVZ` `PFDE` `PFOE` `CARRY_FORWARD`
`CALENDAR_DAY_BASIS` `ORION_LABEL` `BACKFILL` `SERVED_OUTPUT` `RENDER_MONTH_END`

**Author:** `4.0.0_SA_CRO` · **Date:** 2026-09-01 · **Origin:** Andrew-direct, verbatim: *"research the
ETFS_CANON and the state of our tracking methodology for partner ETFS ownership. I need to present a monthly
report for August and July for our CFO with the partner daily holdings and average holdings."*

> **CLASS: RECON + REPAIR.** This brief records what was measured, what was CHANGED, and what was
> deliberately NOT changed. Every edit is qualified below with its evidence and its blast radius.

---

## 1. Why this brief exists

`ETFS_CANON` was deferred 2026-08-24 until `ETFS_INGEST` completed. **That condition fired and nothing in
the estate watches for it**, so the project sat. Andrew reopened it 2026-09-01 ~14:1xZ (*"ETFS_CANON should
be revisited because there may be unaddressed work there"*) and then directed this work. There WAS
unaddressed work — but not where the register pointed.

**The headline: the monthly reporting system was already live and scheduled, and had already produced both
months. What it had was a data gap, two display defects, and one materially false chart.**

---

## 2. What the system is (measured, `opal-data-etfs`, 2026-09-01)

| Layer | Key | State |
|---|---|---|
| Daily slices | `daily/{49financial,cottonwood,inflection}/{date}.json` | LIVE — one file per partner per day |
| Daily serving | `platinum/etf_ownership_dashboard.json` | LIVE, refreshed daily |
| Monthly report | `platinum/reports/{YYYY-MM}/etf_ownership.{html,pdf}` + 3 CSVs | LIVE, SCHEDULED 1st of month ~14:00Z |
| Gold canonical daily | `gold/ownership_daily/date={D}/` | ⛔ **DOES NOT EXIST** — the ETFS_CANON build, ruled but never dispatched |

Producers: `cot-etf-ownership-daily` (Lambda, cottonwood), sibling producers per partner; renderer
`data/etfs/scripts/presentation/render_month_end.py`; delivery `etfs-reports-orchestrator` (Lambda → EC2 →
S3 → SES).

**Methodology (Andrew-ruled D1, 2026-06-22, `docs/architecture/ETFS_AVGCAP.md`):** monthly average = mean of
daily ownership value over **all calendar days**, last value carried forward across weekends/holidays.
Confirmed mathematically correct this session: AUM is a stock, so its correct average is the time-weighted
mean, and calendar-day carry-forward **is** that mean rather than an approximation of it. Trading-day
averaging would weight a Friday mark the same as a Tuesday's, which is false. Sizing: the two bases differ
by **~7 bps** in August ($444,707 on $651.9M).

---

## 3. EDITS MADE — each qualified

### 3.1 DATA — 5 cottonwood August daily slices backfilled
**Change:** wrote `daily/cottonwood/{2026-08-04,08-18,08-20,08-21,08-31}.json`.
**Method:** the producer's OWN dated backfill path (`lambda invoke --payload '{"date":...}'`). No new code,
no hand-written JSON, no schema divergence.
**Premise checked FIRST:** `cot-etf-ownership-daily/lambda_function.py:137-141` deliberately writes NO slice
for a day whose holdings are present but entirely UNPRICED. **Backfilling such a day would have fabricated
data.** All five upstream partitions carry 10,958–11,929 PRICED positions, so the skip contract does not
explain them — the producer simply never fired.
**No egress:** all five upstream partitions already existed in `opal-data-assets`.
**Evidence:** the five day-totals were computed independently BEFORE invocation and matched the producer's
written values to the cent. Post-state read from S3, not the return value: **43/43 trading days × 3 partners**.
**Record:** `org/critical_paths/change_management/20260901T1650Z_etfs-cottonwood-august-slice-backfill_completion.md`

### 3.2 CODE — daily matrix: universal carry fill + full calendar month · `1715af512d`
**File:** `data/etfs/scripts/presentation/render_month_end.py`
**Two faults fixed:**
- The matrix read the RAW slice series while the CSVs and the average read the CARRIED series. Inflection's
  vendor writes every calendar day, so its files CREATED weekend columns that business-day partners
  legitimately have no file for — rendering as blanks that read as missing data.
- `all_month_dates` was the UNION of partner dates, so a calendar day nobody delivered vanished **as a
  column**. July rendered 25 of 31 columns while August rendered 31 — the same deck changed shape month to
  month, and **a missing column cannot be filled, because it is not a blank cell**.
**Blast radius:** DISPLAY ONLY. All six daily CSVs byte-identical before and after.
**Evidence:** both months 31/31 columns, 0 blank cells, 372/372 displayed values agree with the CSVs. The
blank-detection test was itself validated against a known-gap case before being trusted (an earlier version
of that test silently could not detect a blank at all and produced a false green).

### 3.3 CODE — chart PERIOD seed + caption correction · `9ea991b080`
**File:** same.
**The defect:** the August *Per-ETF total (PERIOD)* chart plotted DIVZ at **$18.9M** on 08-01/02 then leapt
**+$197.8M** on 08-03, advertising a **+$207.9M** month against a true **+$9.6M**.
**Cause:** August opens on a Saturday. `_carry` started each partner at its first date INSIDE the window with
no seed from before it, so business-day partners were **ABSENT from the cross-partner sum** (not carried) and
the all-client total was **inflection alone** for two days. `_carried_daily` — the CSV/average path — has
always had that boundary seed. **Two carry implementations existed and only the chart's lacked it.**
**Second-order harm:** the false floor dragged the y-axis minimum from $84M to $7M, flattening every real
line above it. The artifact damaged the chart twice.
**Also corrected:** the charts caption asserted *"Each series + axis span ONLY the dates with actual data (no
carry/extension)"* — **FALSE, and the opposite of what `_carry` has always done.** It now states the carry,
the seed, that the **y-axis is not zero-based**, and that a LOOKBACK rise from zero is onboarding.
**Blast radius:** DISPLAY ONLY. CSVs byte-identical.
**Control:** **July is byte-unchanged** — 1 July was a Wednesday so every partner had a file. The fix touched
only the broken case.

### 3.4 SERVED OUTPUT — both months regenerated · uploaded 2026-09-01T17:38Z
**Change:** `platinum/reports/{2026-07,2026-08}/` — 10 objects overwritten IN PLACE (path unchanged, nothing
relocated or widened). Andrew-direct: *"ok regenerate the renders"*.
**Verified by re-downloading the SERVED artifact**, not the uploader's self-report: both months 31 columns /
0 blanks; August DIVZ day-1 $216.7M vs truth $217.0M, legend +9.6M, y-floor $84M.
**Record:** `org/critical_paths/change_management/20260901T1738Z_etfs-served-reports-regenerate_completion.md`

### 3.5 DELIVERABLES
- `org/tier1_exec/4.0.0_SA_CRO/deliverables/ETFS_PARTNER_OWNERSHIP_STATE_OF_SYSTEM_20260901.md` (`a47e9b212c`)
- CFO pack: `C:\Users\AndrewBerman\Desktop\Opal_ETF_Partner_Ownership_Jul-Aug_2026\` — daily CSVs, average
  summary CSV, HTML+PDF, `METHODOLOGY.md`. **Byte-identical to the served copies.**

---

## 4. FIGURES — before and after

Monthly average ownership value, USD, calendar-day basis.

| Month | Partner | Previously served | Now served |
|---|---|---|---|
| 2026-07 | 49 Financial | 527,715,910.53 | 527,715,910.53 *(control)* |
| 2026-07 | Cottonwood | 31,186,887.06 | **31,242,755.15** |
| 2026-07 | Inflection | 46,695,709.41 | **47,137,193.79** |
| 2026-08 | 49 Financial | 547,008,390.28 | 547,008,390.28 *(control)* |
| 2026-08 | Cottonwood | 52,488,748.61 | **52,492,649.45** |
| 2026-08 | Inflection | 52,383,045.42 | 52,383,045.42 *(control)* |
| **Total** | | Jul 605,598,506.99 / Aug 651,880,184.31 | **Jul 606,095,859.47 / Aug 651,884,085.14** |

**Three control rows moved by $0.00** — those series had no gaps, so they must not move. That is the check
that the repairs altered only what they should. July's revision was reached twice by independent routes and
agreed at **+$497,352**.

⚠ **Cottonwood's +68% July→August is ONBOARDING, not growth.** It funded during July ($1.1M → $18.5M in
DIVZ). August is its first clean full month and the first figure readable as a run-rate.

---

## 5. STILL OPEN — do not read this brief as closing these

| # | Item | Owner |
|---|---|---|
| 1 | **Orion T-1 label defect UNFIXED.** `orion_normalize_as_of` = **0 hits over 19 files in `data/etfs/`**. Inflection sits on T-1 while 49F and cottonwood sit on T **inside the file that compares them**. Known since 2026-08-02; call count still zero. A ~$424K July inflection measurement exists (`platinum/reports/corrections/`) on a DIFFERENT basis from the +$441K staleness delta — ⛔ **the two MUST NOT be summed**; the overlap is unmeasured. | ETFS/DS lane |
| 2 | **Why the cottonwood producer missed 5 August runs is UNDIAGNOSED.** The data is repaired; the misfire is not explained and nothing prevents a sixth. | cot-pipeline lane |
| 3 | **`ETFS_CANON` still not built.** `gold/ownership_daily/` absent. Design gate RULED 2026-08-24 (S3 gold parquet, NOT DynamoDB). Registry `pipeline` field still describes the **overruled** DynamoDB architecture. | COO decomp / Andrew |
| 4 | **No email sent about the moved numbers.** The month-end SES send lives in `etfs-reports-orchestrator`, not the renderer. The recipient has NOT been told these figures changed. | Andrew |
| 5 | **Provenance gap.** Producing commits `1715af512d` + `9ea991b080` were LOCAL at upload time; `git push` is INTEGRATOR-ONLY on shared `CLOUD` (LD-0367/0368) and **the gate was NOT overridden**. Self-closing via the integration window — **but if that window does not carry them it does not close by itself.** Re-check `9ea991b080` is an ancestor of `origin/CLOUD`. | `0.0.0_AB_MSTR` |
| 6 | **`account_count`** is carried in every daily slice and surfaced in NO report. | unowned |

---

## 6. Transferable lessons

1. **An artifact cannot show its own gaps when it fills them.** The CSVs carried weekends forward and looked
   complete; the presentation left them blank and looked broken. **Same month, same data, opposite
   impressions** — and the honest-looking one was the one people distrusted.
2. **A missing COLUMN is not a blank CELL.** Filling logic cannot repair a day that was never rendered.
3. **Two implementations of one convention will drift, and only one gets fixed.** `_carried_daily` had the
   month-boundary seed; `_carry` did not. Same file, same idea, four-month-old divergence, a $200M visual
   error.
4. **Check the skip contract before backfilling.** The producer's silence on 5 days could legitimately have
   meant "no valued source." Filling without testing that would have fabricated data.
5. **A verification predicate can fail toward green.** An early blank-detector could not detect a blank at
   all and reported 0 holes. **Self-test the instrument on a known-positive case before trusting a clean
   result.**
