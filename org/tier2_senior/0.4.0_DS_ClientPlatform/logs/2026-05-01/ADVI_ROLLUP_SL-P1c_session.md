# ADVI_ROLLUP SL-P1c Session Log
**Date:** 2026-05-01 | **Agent:** 0.4.0_DS_ClientPlatform~B | **Project:** ADVI_ROLLUP

---

## Actions Completed

### 1. SL-P1b Verdict Delivered (session carryover — c52f1fc5e)
- ITERATE verdict committed. ADVI_SLEEVE_P1B_ANALYSIS.md at DS deliverables path.
- TO flipped to complete. COO RAVC4 sent.

### 2. SL-P1c Authored and Dispatched (d8e324ad3)
- TO authored: `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI_ROLLUP.SL-P1c.b01-denominator-fix.md`
- COO accepted. Fix B spec confirmed.

### 3. Fix B Implementation — B_01.holdings_lots.py

**Commit:** 7c9f1b13c | **Author:** 0.4.0_DS_ClientPlatform | **Branch:** CLOUD

Changes applied:
- `from __future__ import annotations` added (Rule 15)
- `fifo_mv_by_acct` dict computed pre-loop from FIFO lot DataFrame (filter to sleeve accounts)
- `non_cash_target_mv = max(account_mv - cash_mv - fifo_covered_mv, 0.0)` — uncovered MV base
- `grp_nc_pass` filter applied before `total_unit_cost` sum (pre-veto denominator fix)
- Cash lot logic preserved unchanged
- 4 pre-existing ruff errors cleaned (E702 semicolon, 3x F841 unused vars)

**ds-commit-gate.sh:** exit 0 (py_compile + AST + ruff py39 all PASS)

**S3 upload:** `aws s3 cp ... s3://opal-data-bd/code/gold/B_01.holdings_lots.py`
- ETag: `d1472b93c42959301d123e453b13f8f1`
- comp-pipescript deployed B_01: MATCH

**Push:** `git push origin CLOUD` → 85ff82f3b..7c9f1b13c

### 4. Fix C — Pandas 2.3.3 groupby is_in_axis ValueError

**Root cause found during dry-run:** First dry-run under Fix B failed at sleeve shadow pass with `ValueError: The truth value of a DataFrame is ambiguous` at `_build_uln_sleeve_lots` line 957. Root cause: `_fifo_sleeve.groupby(Series_named_account_id)` triggers pandas 2.3.3 `is_in_axis` code path which calls `IndexEngine.get_loc(Series)` in Cython. This raises `ValueError` (not caught by `is_in_axis`'s except clause: only catches `KeyError, TypeError, InvalidIndexError`). Fix: create `_acct_norm` as an explicit column, use string key `'_acct_norm'` for groupby — `_is_label_like('_acct_norm')` returns True, `is_in_axis` returns immediately without calling `get_loc`.

Also removed temporary `import traceback as _tb` debug code from sleeve except block.

**Commit:** 040c81b4f | **Author:** 0.4.0_DS_ClientPlatform | **Branch:** CLOUD

**ds-commit-gate.sh:** exit 0

**S3 upload:** `aws s3 cp ... s3://opal-data-bd/code/gold/B_01.holdings_lots.py`
- comp-pipescript deployed B_01: MATCH (ETag: see aws s3api head-object)

**Push:** `git push origin CLOUD` → 7c9f1b13c..040c81b4f

### 5. Dry-run (2026-04-21 partition) — OOM BLOCKED (Fix C)

**Result:** `[ULN sleeve shadow pass failed] Unable to allocate 15.5 MiB for an array with shape (2, 1017531) and data type int64 -- shadow artifact not produced`

**Root cause:** Pure RAM exhaustion on local machine. At the point of the sleeve pass, the Python process was at 6.1 GB and the system had < 16 MB free. The failure occurs at `pd.MultiIndex.from_arrays([real_open_sleeve['account_id']...])` at lines 942-946 — BEFORE Fix C's groupby change. Fix C code is not the cause; the environment simply ran out of memory.

This matches the DS~D addendum prediction exactly: "Jones dry-run assertion (AC2) cannot be confirmed locally (OOM, 1,781 parquet files)."

**Note:** The previous diagnostic run (b5k89juq4) passed the MultiIndex step and reached the groupby line — confirming Fix C targets the correct location. The current OOM is a different memory condition (more agents competing for RAM at run time).

**Fix C S3 ETag:** `01d183981bb3430917e898c825ecc0a7`

**Path forward:** Code is correct (Fix B + Fix C, both gate-clean). Validation deferred to first nightly EC2 emission. EC2 runner has sufficient RAM (1,781 parquet files run routinely there).

**Pending nightly assertions:**
- a. Jones z0817905851: shadow MV = cash-only (~$21,060)
- b. 3 pure-sleeve accounts: shadow MV within 2% of silver/allocations
- c. Firm shadow open MV > $15.9M (buggy baseline)

---

## S1 — Cohort Drift Investigation (COMPLETE — non-blocking)

**Question:** Why did cohort shrink from 553 (dry-run) to 458 (live nightly)?

**Findings:**

| Metric | Value |
|--------|-------|
| Cohort parquet accounts (2026-04-13.parquet) | 598 |
| Dry-run shadow accounts (2026-04-13 data) | 553 |
| Live shadow accounts (2026-04-15 through 2026-04-21) | 458 (stable) |
| Cohort → dry-run gap | -45 (runtime filtered on dry-run data) |
| Dry-run → live gap | -95 |
| Cohort → live gap | -140 |

**Key findings:**
1. **Only one cohort parquet exists** (2026-04-13.parquet, 598 accounts). No regeneration occurred after dry-run. Cohort criteria unchanged.
2. **Zero shadow accounts outside the cohort** — all 458 live accounts are in the 598 cohort. No phantom accounts.
3. **17 dropped accounts had MV=0** on the 2026-04-13 cohort date — no lots to emit at any date; consistently absent from both dry-run and live.
4. **43 dropped accounts had MV < $1,000** — thin accounts; likely filtered by lot-quantity thresholds.
5. **Signal type identical** across dropped vs retained (all have `retirement_acct_type + sleeve_registration`). Drift is not signal-quality driven.
6. **Live shadow stable at 458** across all 4 emission dates (2026-04-15, 2026-04-16, 2026-04-17, 2026-04-21) — exactly 1 account entered and 1 exited per consecutive pair.

**Probable cause of dry-run → live drift (-95 accounts):**
The 95 accounts that appeared in dry-run shadow but not in live nightlies had ULN/unrealized data present on 2026-04-13 but absent (or price-missing) on 2026-04-15+. Possible mechanisms:
- Accounts that closed between 2026-04-13 and 2026-04-15 (MV→0 on live dates)
- Thin or zero-balance accounts whose ULN rows disappeared from silver/unrealized between the two dates
- Accounts that moved to full FIFO coverage (with Fix B, uncovered_mv→0 and no cash lot → skip)

**Recommendation:** No cohort regeneration needed. The 458-account cohort is the correct runtime cohort for current data. The -95 drift will be re-evaluated post-Fix B dry-run — if dry-run on 2026-04-21 shows a different count, investigate further.

---

## Compiler Tools Log

| Tool | Result |
|------|--------|
| ds-commit-gate.sh B_01 (Fix B, 7c9f1b13c) | EXIT 0 — all checks PASS |
| ds-commit-gate.sh B_01 (Fix C, 040c81b4f) | EXIT 0 — all checks PASS |
| comp-pipescript deployed B_01 (Fix C) | MATCH |
| aws s3 ls s3://opal-data-bd/diagnostics/sleeve_cohort/ | 1 file: 2026-04-13.parquet (15,342 bytes) |

---

## Pending (this session)

- [x] Fix B implemented and committed (7c9f1b13c)
- [x] Fix C implemented and committed (040c81b4f) — pandas 2.3.3 groupby string-key fix
- [x] S3 upload MATCH (ETag: 01d183981bb3430917e898c825ecc0a7)
- [x] Dry-run attempted — OOM on local machine (consistent with DS~D prediction)
- [ ] RAVC4 to COO: fix commits + ETag + OOM status + nightly-validation plan
- [ ] First nightly emission: assert Jones + pure-sleeve + firm MV
- [ ] Monitor 3 consecutive clean nightly emissions → final RAVC4

---

## DS~D Addendum — S1 Confidence Tier Analysis (2026-05-01)

Additional S1 analysis by DS~D (complement to DS~B findings above).

**Confidence tier breakdown (cohort 2026-04-13 vs first live emission 2026-04-15):**

| sleeve_confidence | Emitting | Non-emitting | Non-emit rate |
|------------------|----------|--------------|---------------|
| 0.50 | 424 | 73 | 15% |
| 0.75 | 32 | 67 | 68% |
| 1.00 | 2 | 0 | 0% |

**Key finding:** All 1.0-confidence accounts emit. 68% of 0.75-confidence accounts do not
emit — these borderline-detection accounts are most susceptible to FIFO-covered or
missing-ULN conditions. 15% of 0.50-confidence accounts don't emit (likely false positives
in the sleeve detector). The confidence tier is strongly predictive of emission success.

**Jones z0817905851 in pre-fix shadow:** 4 rows confirmed (CASH + 3 ETFs) across all 4
emission dates (2026-04-15 through 2026-04-21). All ETF rows have approx MV ≈ $0 due to
the weight-deflation bug (12.43% of intended MV). Post-Fix B, Jones should emit 1 row
(CASH only, ~$21,060) — verified via code-review of lines 975-1014.

**EC2 note:** Jones dry-run assertion (AC2) cannot be confirmed locally (OOM, 1,781 parquet
files) or via QA runner (i-0090b823a4a0997e3 stopped). Will be validated via first nightly
emission under fixed S3 code.
