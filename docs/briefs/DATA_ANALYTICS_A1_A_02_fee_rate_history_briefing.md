# A_02 — fee_rate_history — DATA_ANALYTICS layer briefing

**Script:** `data/black_diamond/scripts/gold/A_02.fee_rate_history.py`
**Output:** `gold/dimensions/fee_rate_history.parquet`
**Layer / order:** Group A (dimensions); catalog line 81. Reads silver/fees/ (+ silver/allocations/ for cross-val).
**Essential status (Andrew's framework):** ESSENTIAL — feeds D_00 / D_00c / D_02 (fee-revenue attribution) → ADVI portal fee surfaces. Pairs with A_01: A_01 = WHO+SPLITS, A_02 = the FEE (fee_bps + schedule).
**Author/project:** 0.4.0_DS_ClientPlatform / ADVI_GLDOPS (2026-04-06).
**Briefing by:** 0.4.0_DS_ClientPlatform, 2026-06-24 (Andrew-direct A1 layer-walk). Source-grounded (file:line) + deployed-verified.

---

## 1. What it does

Builds a **per-account SCD Type 2 fee-rate history** from `silver/fees/` (BD `Fees_OpalCapital_Daily`). Detects when `fee_bps` or `fee_schedule` changes for an account → closes the prior period, opens a new one. One row per account per fee-rate period. Cross-validates the current rate against `silver/allocations/` (basis_points_1) for the overlap period (2026-01-16+) and logs disagreements as data-quality flags (L325-388).

Deliberately separate from A_01 (L9-12): different source (fees vs transactions), different change cadence (renegotiation vs reassignment), independent backfill.

## 2. Architecture / data flow

1. **Column resolution** (L88-111): BD fee reports use varying column names; `COLUMN_CANDIDATES` maps `Basis Points`/`basis_points`/**`basis_points_1`**/`BasisPoints` → canonical `fee_bps` (first-match-wins), etc.
2. **Load** silver/fees (parallel, 64 workers), resolve columns, normalize fee_bps→numeric, is_billable→bool (L118-191).
3. **Vectorized SCD build** (`build_fee_rate_history`, L264-318): dedup to one row per (account, day); hash the `[fee_bps, fee_schedule]` tuple; open a record on account-change OR state-change; `end_date` = next effective − 1 day; `is_current` = last.
4. **Cross-validate** vs latest allocation (L325-388) — log mismatches > 0.5bps.
5. **Save** + advance the incremental watermark sidecar.

## 3. Recompute posture — HEALTHY (already incremental; the model A_01 follows)

- **Catalog = `A_02|...|--upload --incremental`** (line 81) — A_02 **already runs incremental** nightly. NOT a full-recompute offender.
- Incremental design (L415-585) is elegant: **the fee_rate_history output IS the compressed change-point stream**, so it reconstructs change-point events from the existing history (`reconstruct_fee_events`) ∪ a fresh read of only the new + 14-day-recent window, re-feeds the SAME builder → identical SCD. Guards → full fallback: cold-start, restatement (etag fingerprint), vanished file, **back-dated row in a window file** (L559-569).
- **Shadow-parity PROVEN then flipped + shadow retired** — the correct lifecycle: scorecards identical=True / 0 mismatches / 10,782 rows for 06-12..06-15, then flipped to `--incremental` and the shadow stopped (no longer needed). **This is exactly the lifecycle the A_01 flip completes.**
- The full-rebuild it avoids: **1,890 silver/fees files (2020-03-06 .. present)**. Graceful, logged fallback to full on cold-start/restatement (not silent).
- Group-A context: A_00 + A_02 both incremental; A_01 was the lone straggler (overlooked) — now being flipped to match.

## 4. Tech debt

- **DEAD CODE (~65 lines):** `build_fee_history_for_account` (L198-241) + `_make_fee_record` (L244-261) — a per-account `iterrows` SCD builder, **never called** (only ref is its own def; superseded by the vectorized `build_fee_rate_history`). Drop in A2.
- **BD-denormalization resolved at gold:** `COLUMN_CANDIDATES` maps the dup-suffixed `basis_points_1` (the BD denormalization debt — duplicate-suffixed col-pairs) → `fee_bps`. A reasonable robustness layer, but the de-dup-suffixing belongs in **silver**.

## 5. Bullshit / overfit
- None egregious. The column-candidate resolver is defensive (BD's inconsistent naming), not overfit. No hardcoded single-entity hacks (unlike A_01's `Olivia Shin`).

## 6. What's GOOD (keep)
- **No legacy dual-write** — cleaner than A_00/A_01 (writes only the canonical key, L395-412).
- **Already-incremental** with the change-point-as-cache design + the back-dated-row guard — well-engineered, proven, and on the correct flip-then-retire-shadow lifecycle.
- **Cross-validation** vs allocations is a genuine data-quality control (catches fee disagreements between the fees report and allocations).

## 7. Actions

| When | Action | Owner |
|---|---|---|
| A2 | DELETE dead code `build_fee_history_for_account` + `_make_fee_record` (~65 lines) | DS |
| A2 | Move the `basis_points_1` de-dup-suffix resolution to silver (the BD-denorm cleanup) | DS (+ silver/AE) |
| — | Recompute: NO action — already incremental + proven | — |

## 8. Status
- **Essential** (Group-D closure). **Recompute HEALTHY** (already incremental — the model A_01 follows). Cleaner than A_00/A_01 (no dual-write, no overfit hacks). Only real debt = the dead per-account builder + the silver-belongs denorm resolver.
