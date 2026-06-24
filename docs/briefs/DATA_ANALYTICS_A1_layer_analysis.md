# DATA_ANALYTICS A1 — layer-by-layer analysis (chronological, source-grounded)

Walking the dispatched bd gold chain A_00→D_04 in execution order (Andrew-direct deep-dive). Per layer: what it does, tech debt, bullshit/overfit, recompute posture (full-vs-incremental). Source-grounded (file:line); deployed-aware.

---

## A_00 — accounts_dimension  (`A_00.accounts_dimension.py`)

**Function:** `gold/accounts_dimension_latest.parquet`, 1 row/account_id (names, relationship, tax_status, qualified_flag, advisors, location, open/first-seen dates, account_type/registration). PRIMARY = `silver/transactions/` (2020+, latest-row-per-account + min-trade-date); ENRICHMENT = `silver/allocations/` latest snapshot, left-join for 2 fields only (account_type, account_registration_type).

**Recompute posture:** HAS real `--incremental` (watermark `_last_txn_file_date`; reads only new txn files; merges into existing; does NOT re-read history — rel_first_seen recomputed from stored first_transaction_date). Catalog runs `--incremental`. GOOD — not a daily full.
- 🚩 **Silent-fallback-to-FULL trap** (L623-624, L727-728): if dimension missing OR no watermark → `--incremental` silently does a FULL all-history rebuild (every txn file 2020+, 128 threads), no loud signal. A watermark-less/old-code dimension = silent nightly full. FIX: fail-loud (or auto-watermark) instead of silent full.

**Bullshit / overfit:**
- **L461 `replace('Olivia Shin','Liv Shin')`** — hardcoded single-person name fix in the gold transform. 49F-overfit; belongs in a silver alias/data-quality table.
- **L249-283 advisor carry-forward** — complex gold band-aid re-deriving last-non-blank advisor per account because BD blanks advisor on cash/dividend/fee txns. Should be a SILVER cleanup, not re-run in gold each build.
- L459 `replace('No Architect Value Assigned','Unassigned')` — magic-string BD-ism (minor).

**Tech debt:**
- **L601-605 LEGACY dual-write** every run ("during migration") — migration leftover; writes the artifact twice nightly. Confirm migration done → drop.
- **L555 vs L658 `data_as_of_date` dtype split** — full writes a `date` object, incremental writes a `str`. Same column, path-dependent dtype = latent downstream bug.
- L589-592 blanket object→string coercion at save — workaround for pyarrow type-inference (client_zip mixed types); papers over upstream dtype mess.

**Verdict:** essential (A_00 → all B/C/D → portal). Structurally sound + genuinely incremental. A2/A3 actions: kill the silent-full-fallback (fail-loud), move the name-fix + advisor-carry-forward to silver, drop the legacy dual-write, fix the date/str dtype split.

---

## A_01 — advisor_assignments  (`A_01.advisor_assignments.py`)

**Function:** `gold/dimensions/advisor_assignments_history.parquet` -- SCD Type 2 tracking the 5 advisory roles (architect/implementor/consultant/local_ops/additional_advisor) + their fee-split %s + house_split per account OVER TIME. Scans silver/transactions chronologically; opens a new SCD record when the advisor/split tuple changes. Baseline-supplements accounts with no txns from A_00.

**Recompute posture -- THE finding (full when proven-incremental exists):**
- 🚩🚩 **A_01 runs a FULL rebuild EVERY NIGHT** -- catalog = `--upload` (NO `--incremental`), confirmed LOCAL **and** DEPLOYED. Reads **1,815** txn files (2020-2026) to rebuild the entire **15,292-row** SCD history nightly, though nothing pre-2026 changes.
- A complete, sophisticated **incremental path EXISTS** (L468-749: daily-state-grain cache `ADVISOR_ASSIGNMENTS_DAILY_STATE` + 14-day re-read window + etag restatement-detection + cold-start fallback) and it is **shadow-parity PROVEN byte-identical** (identical=True, 0 cell_mismatches, 15292==15292) for **5+ consecutive nights (06-20..06-24; 13 scorecards)**.
- The code's OWN flip-gate ("full stays default until shadow parity is proven over clean nights and the dispatch is flipped", L469-471) is **MET** -- but the **flip never happened**.
- WORSE: A_01 is in `GLDINC_SHADOW_SET` -> the incremental ALSO runs nightly as a shadow (to prove parity). So the nightly pays for BOTH a full production build AND a shadow build. **Flipping captures the savings AND retires the now-redundant shadow.**
- **ACTION (highest-ROI change so far): flip catalog A_01 -> `--upload --incremental`** (proven; 14-day-window+cache vs 1,815-file full). DT/AE dispatch-lane change; cite the 5-night parity.

**Bullshit / overfit:**
- L271-330 `_normalize_multi_role_splits`: **row-by-row Python loop** (`for idx in history.index: ... .at[idx]`) over 15,292 records x 5 role-pairs -- slow, vectorizable. The RULE is legit (Andrew-approved 2026-04-09); the IMPLEMENTATION is the debt.
- L96 `SPLIT_NULL_PATTERNS` includes **"no 49 house split % value assigned"** -- 49F-overfit hardcoded string. The NULL_VALUES/SPLIT_NULL_PATTERNS BD-sentinel cleanups belong in SILVER.

**Tech debt:**
- **STALE DOCSTRING** (L18-21, L26-29): advertises outputs "fee_bps, fee_schedule from silver/allocations" -- but L834 says fee economics moved to A_02 ("01 tracks WHO+SPLITS; 01b tracks the FEE"). Header lists outputs it no longer produces.
- Hardcoded stale count "1,764 daily files" (L27) -- actual 1,815 (drifts).
- **LEGACY dual-write** (L770-774) -- same migration leftover as A_00.
- ~280 lines of incremental+shadow machinery maintained but the production benefit (the flip) uncaptured.

**Positive (not debt -- good engineering):** the ADHC_GLDINC deterministic-ordering oracle-fix (provenance `_file_date`/`_intra_pos` + total-order dedup, L182-189/238-246) fixed a real night-to-night SCD-survivor nondeterminism; the load-completeness guard (retry-then-fail-LOUD, L207-234) prevents silent incomplete builds. A_01 is well-engineered -- the debt is the un-flipped incremental + the silver-belongs cleanups.

**Verdict:** essential (A_01 -> D_00c/D_02 -> portal). Highest-ROI fix in the chain so far = flip to `--incremental` (proven). A2/A3: flip incremental + retire shadow; vectorize multi-role norm; move sentinels to silver; fix the stale docstring; drop legacy dual-write.

---
*(B_00, B_01, ... appended as the walk continues.)*
