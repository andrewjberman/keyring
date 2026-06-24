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
*(B_00, B_01, ... appended as the walk continues.)*
