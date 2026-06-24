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

## A_02 — fee_rate_history  (`A_02.fee_rate_history.py`)  · full briefing: DATA_ANALYTICS_A1_A_02_fee_rate_history_briefing.md

**Function:** `gold/dimensions/fee_rate_history.parquet` -- per-account SCD Type 2 fee-rate (fee_bps + fee_schedule) history from silver/fees/; cross-validates vs silver/allocations. The FEE counterpart to A_01 (A_01=WHO+splits).

**Recompute posture: HEALTHY -- already incremental.** Catalog line 81 = `--upload --incremental`. A_02 was shadow-proven (06-12..06-15, identical/0-mismatch/10,782 rows) THEN flipped + shadow retired = the correct lifecycle (the model A_01's flip completes). Avoids a 1,890-file (2020-2026) full read; change-point-as-cache design + back-dated-row guard; graceful logged fallback to full. **Group-A: A_00 + A_02 incremental; A_01 was the lone straggler.**

**Tech debt:** DEAD CODE (~65 lines) -- `build_fee_history_for_account` (L198-241) + `_make_fee_record` (L244-261), a per-account iterrows builder NEVER called (superseded by the vectorized `build_fee_rate_history`). BD-denorm resolved at gold (`COLUMN_CANDIDATES` maps dup-suffixed `basis_points_1`) -- belongs in silver.

**Bullshit/overfit:** none egregious (no single-entity hacks; the column resolver is defensive).

**Good:** NO legacy dual-write (cleaner than A_00/A_01); cross-validation vs allocations is a real data-quality control; well-engineered incremental.

**Verdict:** essential (Group-D closure). Healthiest Group-A script so far. A2: delete the dead per-account builder; move the denorm resolver to silver. Recompute = no action (already incremental).

---

## A_03 — positions_cube  (`A_03.positions_cube.py`, 1,928 lines) ★ crux  · full briefing: DATA_ANALYTICS_A1_A_03_positions_cube_briefing.md

**Function:** `gold/positions_cube/YYYY-MM-DD.parquet` (2,361 partitions, 2020..present) -- daily holdings FIFO-reconstructed from silver/transactions/. The positions FACT -> B_00 -> all B/C/D -> portal.

**Recompute: FULL nightly + NOT justified (CORRECTED 2026-06-24, Andrew-challenged).** Catalog line 82 = `--upload`; rebuilds all 2,361 partitions (2020->present) nightly + writes every partition unconditionally. The `--incremental` is only a whole-run fingerprint SKIP-GATE (won't help -- INPUTS-CHANGED nightly), but that does NOT mean A_03 can't be incremental. GROUNDED refutation of the author's "history rewrites nightly": synthetic injection = 99.6% in 2024 (78,692 events, the 4/30/2024 rotation), pre-2024 = 13 events (0.0%) -> deep history (2020-2023, most partitions) is STABLE, rebuilt for nothing. RIGHT model (Andrew's): first-full -> ~7-14 day revision window + freeze deep history + **freeze the one-time 2024 injection (stop re-deriving it from today's snapshot nightly -- the bug-shaped artifact that rewrites 2024->present).** Two fixes: (A) windowed-incremental in the CURRENT design = real win NOW; (B) snapshot-native (cot model) = clean end-state (deletes FIFO+injection). I over-claimed "inherently full"; corrected.

**Bullshit/overfit -- WORST in Group A:** ~500 lines of synthetic injection (L359-866: phantom-sell closure, Schwab-RPS two-sided ground-truth, synthetic-buy back-solve for ~$177M vanished positions) repairing BD's incomplete feed -- ALL vanish under snapshot-native. + hardcoded NAME_ALIASES (OPAL/EVENTIDE->POLEN), _CASH/_PAR patterns (SHIELD/BUFFER/DELPHI), maturity-year regex-on-name, sentinel-date clamps. Belongs in silver security-master.

**Tech debt:** DEAD CODE (L254-262 unreachable ghost-suppression fragment after a return); 3 overlapping allocation loaders; 3 legacy dual-writes; rows/partitions stat mislabel (L1317).

**Good:** the fingerprint-gate + gate-evidence shadow (correct for an inherently-full fact); memory strategy; deterministic compute; careful txn taxonomy.

**Verdict:** essential. THE poster child for the DATA_ANALYTICS rebuild -- ~500 injection lines + inherent full-recompute, all because positions are FIFO-reconstructed from an incomplete feed. A3 = snapshot-native positions (architecture, not a flag). A2 = delete dead code/consolidate loaders/drop dual-writes/move overfit to silver.

---
*(B_00, B_01, ... appended as the walk continues.)*
