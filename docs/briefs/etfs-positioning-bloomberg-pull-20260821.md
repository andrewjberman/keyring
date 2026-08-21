# ETFS_POSITIONING -- the Bloomberg pull, delivered

**Author:** `0.0.0_AB_MSTR~Z` (site Z, Bloomberg terminal box) · **2026-08-21**
**Directive:** D4 (`ETFS_POSITIONING`) -- **LAPTOP-OWNED**; site Z executed ONE bounded pull.
**Spec:** `docs/architecture/ETFS_POSITIONING_BLOOMBERG_ASK.md` v2, Parts A/B/C.
**Parent PRD:** `docs/architecture/ETFS_POSITIONING_PRD.md` (s.4.3 shape, s.6.3a pull, s.6.3b grain).
**Artifacts:** `s3://opal-data-etfs/bbg-testpull/` (236 objects; `code/` carries all four producers).

---

## 0. WHAT WAS ASKED, AND THE ONE COURSE CORRECTION

The ask was a bounded re-run of Yang's model-Positioning Bloomberg pull against the ETF universe.
**My first pass ran the spec verbatim and produced the right data in the wrong shape** -- a snapshot
characteristics table plus a price/return history, with no `returns{}` block and no book assembly.

Andrew's correction: *"we want to get the data for this in as similar a shape as possible to how the
models data is procured for the 'positioning' page ... should have briefs and atom decomp and all
kinds of prior art on this already, it shouldnt be guesswork."*

**He was right and the prior art was decisive.** The served shape is recorded in PRD s.4.3, measured
off the live artifact, and carried in the certified atom-decomp rectangle
`workflows/atom_decomposition/runs/portal-page-positioning/20260811T1818Z/rectangle.final.certified.json`.
Reading it changed the deliverable from "the fields" to "the fields **in the B-form, with returns**".
**The residual work after reading the prior art was smaller than the work I had already done without
it** -- that is the whole lesson of this brief.

---

## 1. THE PULL

| | |
|---|---|
| transport | canonical LOCAL Bloomberg API -- `blpapi` via `integrations/bloomberg/mcp/blp_client.py`. **NOT the MCP tool** (Andrew-direct: *"you just hit bloomberg direct through canonical local api"*). |
| universe | **109** = 105 PFDE+PFOE constituents (supplied, not derived) + 4 fund tickers |
| window | **2020-12-31 -> 2026-08-20**, daily. Computed from `BDay(-1)` / `YearEnd(-6)`, never hardcoded, so a re-run shifts correctly. |
| history | 148,407 rows, 109/109 securities, median 1,415 rows/security |
| characteristics | 109 x 10 (snapshot) |
| fund daily series | 2,134 rows x 7, 4 funds |

---

## 2. THE DELIVERABLE -- `combined/etfs_positioning_books.json`

The four books in the served `current_holdings.<CODE>` shape: book `aum` + `returns{}` + weighted
`holdings[]`.

| book | AUM ($M) | holdings | weight sum | excluded |
|---|---|---|---|---|
| PFDE | 164.4 | 87 | 99.64% | 3 |
| PFOE | 90.3 | 22 | 97.66% | 2 |
| DIVZ | 307.3 | 0 | -- | book-level only |
| IDVZ | 198.7 | 0 | -- | book-level only |

**THE TIE-OUT.** PFDE 99.64 + 0.32 (FXFXX) + 0.03 (Cash&Other) + 0.00 (2602335D, zero-priced) =
**99.99**. PFOE 97.66 + 2.28 + 0.04 = **99.98**. Those are exactly the figures PRD s.3.1 records for
`silver/holdings`, reached here by an independent route -- **the join is confirmed by arithmetic, not
by having run.** The 5 excluded rows are NAMED in `excluded[]` per book; a silently dropped cash line
is how a weight sum quietly stops summing.

**Returns coverage:** `1D WTD MTD 1M QTD 1Q` = 109/109. `YTD`/`1Y` = **107/109** -- the two nulls are
PFDE and PFOE, listed ~160 trading days ago. **A window starting before a security existed is not a
return**; it would be a since-inception number wearing a `1Y` label. The producer refuses and emits
null. The refusal is the feature.

**The ours/Bloomberg split is preserved per field.** `weight` is ours
(`silver/holdings.weight_pct`); everything else on the row is Bloomberg. PRD 6.3a makes that
load-bearing and it is kept field-by-field rather than merged.

---

## 3. FINDINGS

**3.1 -- Bloomberg does NOT serve DIVZ/IDVZ constituent holdings, and it is not entitlement.**
Ten candidate mnemonics returned empty. With `fieldExceptions` surfaced (see 3.3), each named its
cause: `FUND_HOLDINGS`, `FUND_TOP_HOLDINGS`, `PORT_HOLDINGS` -> `BAD_FLD/INVALID_FIELD`, **identical
to a deliberately bogus control field** -- i.e. names that do not exist. `PORTFOLIO_MWEIGHT` and
`INDX_MEMBERS` -> `BAD_FLD/NOT_APPLICABLE_TO_REF_DATA`: real fields, wrong request type. **Zero
returned `NOT_AUTHORIZED`.** So the route forward, if ever wanted, is a different REQUEST TYPE, not a
different name. Combined with `TOTAL_NUMBER_OF_HOLDINGS_IN_PORT` returning 30/46 for DIVZ/IDVZ,
Bloomberg demonstrably holds portfolio data for these funds and will not serve constituents via
refdata.

**3.2 -- AUM IS available daily; most other characteristics are NOT.**
Measured per fund over the full window, with `PX_LAST` as a positive control in the same request:

| field | daily? |
|---|---|
| `px`, `aum`, `nav`, `yield`, `beta` | **YES** -- genuine series on all four funds |
| `te`, `fee`, `num_holdings`, `duration`, `credit` | **NO** -- 0 rows historically, all four funds |

DIVZ `aum` runs **2.50 -> 307.32 ($M)** across 1,399 dates / 1,253 distinct values.
⛔ **The load-bearing check is `distinct`, not row count.** A Bloomberg field can return a full column
of "history" that is today's value stamped on every date; a row count cannot tell that from a real
series. **So `fee` and `num_holdings` are permanently snapshot-only** -- if the page wants them as of
a past date, that must come from our own records.

**3.3 -- `blp_client.py` discarded the only field that explains an empty column.** Fixed
@`fe91e0a8eb`: `reference_data()` looped `if fd.hasElement(f)` and silently skipped, collapsing three
causes (bad name / wrong request type / not entitled) into one identical silence. `fieldExceptions`
is now surfaced under the reserved `__field_errors__` key, matching the existing `__error__`
convention. **This turned ten calls' worth of ambiguity into one definitive read.** Note the fix is
inert on the MCP path until that server restarts -- the direct/local path loads from disk and carries
it immediately.

**3.4 -- The grain change is real and is a category fact, not a defect.** PRD 6.3b predicted it and
the pull confirms it: `fee`/`aum`/`num_holdings` populate **4/109** (exactly the funds) and Bloomberg
returns `NOT_APPLICABLE_TO_REF_DATA` on **exactly 105** (exactly the constituents). 4 + 105 = 109 on
every axis. `aum` on a stock uses `CUR_MKT_CAP`; every row carries `aum_basis` so the two are never
silently mixed.

**3.5 -- Two smaller ones, flagged rather than smoothed.** `TRACKING_ERROR` exists for only IDVZ
(7.11) with **no field exception raised** on the other three -- Bloomberg simply has no value.
`GICS_SECTOR_NAME` is absent on the four funds **without** an exception, unlike the fund-only four
which all reported cleanly; the outcome is expected (an ETF has no single GICS sector) but arrives by
a different mechanism and that difference is unexplained.

---

## 4. NOT DONE, AND DELIBERATELY

**`asset_class` / `sub_asset_class` are NULL.** GICS across the 105 constituents gives **10 distinct
sectors** (Information Technology 29, Financials 18, Industrials 14, Consumer Discretionary 12,
Health Care 11, Communication Services 7, Consumer Staples 5, Utilities 4, Materials 3, Energy 2),
carried as `sub_asset_class_raw`. PRD s.4.4: the model `sub_asset_class` values are duration buckets
and cap tiers; on a stock the same axis is a GICS sector -- **a different grain on the same axis.**
Reusing the model enum would put two grains on one axis. **Minting the ETF vocabulary is a Rule-24
authoring act requiring the four-postulate test and it is not mine to do.** The raw value is carried
so whoever mints it works from measurement.

**`active` and `weight` on the B-form rows** are ours, not Bloomberg's; `weight` is joined in the
assembled books, `active` is not populated anywhere.

---

## 5. ARTIFACTS

```
s3://opal-data-etfs/bbg-testpull/
  README.md                                  contents + the traps, leads with the null-column gotchas
  code/etfs_positioning_pull.py              the 109 x 6y pull (Parts A/B/C)
  code/fund_daily_series.py                  fund-level daily; the distinct-vs-n test
  code/shape_to_positioning.py               -> B-form rows + returns{}
  code/assemble_books.py                     -> the four books + weight join + tie-out
  combined/etfs_positioning_books.json       *** THE DELIVERABLE -- start here ***
  combined/etfs_positioning_bform.json       109 B-form rows
  combined/etfs_positioning_characteristics.{pkl,csv}
  combined/etfs_positioning_history.{pkl,csv}      148,407 rows
  combined/etfs_positioning_fund_daily.{pkl,csv}   2,134 rows
  tickers/<TICKER>/                          109 folders: characteristics.csv, history.csv (+ fund_daily.csv on the 4 funds)
```

**Bucket note:** requested as `opal-data-efs`, which returns `NoSuchBucket`. Used `opal-data-etfs` --
the bucket the ask itself references for `silver/holdings` -- rather than create one off a typo.

---

## 6. BOUNDS

Every number here is from the site-Z terminal box on 2026-08-21 against a live Bloomberg session.
The pull is a **point-in-time read of a mutable surface**: re-running shifts the window forward by
construction. Nothing was applied, deployed, or served -- these are files in S3 and nothing consumes
them yet. The B-form and books are **shaped to** the served Positioning contract; they have **not**
been validated against a live portal renderer, and no claim is made that the page would render them.
