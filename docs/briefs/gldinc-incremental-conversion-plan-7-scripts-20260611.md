# GLDINC Incremental-Conversion Plan — 7 BD Gold Full-Recompute Scripts

**Project:** ADHC_GLDINC (incremental workstream)
**Author:** 0.6.0_AE_PartnerETL
**Date:** 2026-06-11
**Authorization:** Andrew direct (sovereign) — "fix all of them ... make sure your logic in doing so does not break the outputs, so be careful and go one by one."
**Routed to:** COO + DS (0.4.0_DS_ClientPlatform, gold-script deploy owner per Rule 13)

---

## 1. Origin

Andrew-requested nightly telemetry diagnosis of the BD gold c6i.16xlarge runner
(see session log 2026-06-11) found: the watermark-gated scripts (A_00, B_00,
B_01b, C_06) correctly no-op on no-new-data nights, but **7 scripts run a FULL
recompute every run regardless of input change**. Because BD source data lands
~once/day (~18:00Z), the second daily run (04:00Z) is largely redundant for
these 7 — they recompute byte-identical outputs. Measured wall time on the
2026-06-11 04:00Z run (no new data vs the 22:00Z run):

| Script | wall_s | Group | Output |
|---|---:|---|---|
| B_01 holdings_lots | 731 | B | FIFO lot snapshot |
| A_03 positions_cube | 563 | A | per-day cumulative positions |
| B_02 canonical_lots | 191 | B | per-date open/closed tax lots |
| B_03 account_gains | 141 | B | account gains |
| A_01 advisor_assignments | 52 | A | SCD-2 advisor/split history |
| A_04 client_dimension | 31 | A | household snapshot dimension |
| A_02 fee_rate_history | 25 | A | SCD-2 fee history |

~1,734s (~29 min) of redundant c6i.16xlarge recompute on a no-new-data night.

## 2. Method — structural no-break guarantee

Every conversion is **ADDITIVE**:
- A new `--incremental` code path + a **cold-start → full-rebuild fallback**.
- The existing full-rebuild path is **untouched** and stays the dispatch
  default + the authoritative output.
- Therefore the **code change alone cannot change live outputs.**

**Validation = shadow parity, no manufactured runs:**
- A `--shadow` self-check builds the full oracle + a simulated-incremental and
  asserts byte-identity. Runnable offline (reads S3, not the c6i runner) AND on
  the scheduled nightly (GLDINC P1 pattern).
- Accumulate clean nights, get Andrew's nod, **then** flip the dispatch
  `INCREMENTAL_CAPABLE` list. Cutover is a **separate gated step**, never bundled
  with the additive code change.

**Restatement safety:** each watermark carries a per-partition fingerprint
(etag). If a historical source file changes/vanishes, the incremental path falls
back to full rebuild. A recent re-read window (mirroring B_00 `--force-recent-days
14`) absorbs late restatements inside the window.

**DS coordination (Rule 13):** AE does the engineering + this plan; DS owns the
commit → S3 → dispatch deploy cycle for `data/black_diamond/scripts/gold/*.py`.
Each script's deploy is sequenced with DS (live on the 9-RED shadow-set bundle).

## 3. Safety classification — they are NOT uniform

The careful finding: **3 of the 7 have fields that change daily even with no new
data**, where a naive watermark-skip would freeze the output (= a break). These
get hybrid designs and go LAST.

| Script | Incremental shape | Risk | Order |
|---|---|---|---|
| **A_02** fee_rate_history | SCD-2; reconstruct change-points from existing history + read only new+window fee files, re-run same builder | LOW — append-natured, immutable closed periods | **1 (DONE, parity proven)** |
| **A_01** advisor_assignments | SCD-2 from transactions (same pattern as A_02) + latest-allocation fee snapshot leg | LOW-MED | 2 |
| **B_02** canonical_lots | per-date transform (BD provides lots, identity source); process only new dates | MED | 3 |
| **B_03** account_gains | TBD — read structure; watch price/time-dependent fields | MED | 4 |
| **A_03** positions_cube | forward cumulative by date BUT reconciles vs LATEST Schwab RPS / unrealized / realized — latest-snapshot passes can retroactively touch historical partitions | **HIGH** — needs forward-incremental + bounded re-reconciliation window | 5 |
| **B_01** holdings_lots | FIFO lot snapshot; persist open-lot state + apply new txns FIFO, BUT price/market_value/accrued_gain/holding_period MUST recompute daily | **HIGH** — hybrid lot-state-incremental + daily revaluation; naive skip = stale prices = broken output | 6 |
| **A_04** client_dimension | snapshot agg with "active in last 90 days" **sliding window** that changes daily with no new data | MED, LOW VALUE (31s) — either keep full or split: incremental new-household detection + always-recompute window fields | 7 (decide; flag if value < risk) |

## 4. Script 1: A_02 fee_rate_history — DONE, parity PROVEN

**Cost:** `load_fee_files()` reads all 1,881 silver/fees files every run; the SCD
build is vectorized/fast. Incremental reads only new+window files.

**Provably-identical trick:** the `fee_rate_history` output *is* the compressed
change-point stream (each SCD record = the date a fee state began). Reconstruct
those change-points + a fresh read of the new+14-day-window files, re-run the
**unchanged** `build_fee_rate_history()` → identical SCD. Closed historical
periods are immutable; restatement is fingerprint-guarded.

**Changes (additive):**
- `lib/s3_layout.py`: `FEE_RATE_HISTORY_WATERMARK = gold/meta/fee_rate_history_watermark.json`
- `A_02.fee_rate_history.py`: `--incremental` path (watermark + restatement
  fallback + reconstruct-change-points merge), `--shadow` parity proof,
  `load_fee_files(keys=None)` (default = identical full behavior). Full path
  untouched; now also writes the watermark sidecar (separate key, output identical).
  (+ Rule 15 `from __future__ import annotations` + 3 pre-existing lint fixes.)

**Parity proof (offline `--shadow`, local read of S3, no c6i run):**

| simulated gap | files read (vs 1,881) | identical | sym_diff | cell_mismatches |
|---|---|---|---|---|
| 1 day | 15 | **True** | 0 | 0 |
| 3 days | 17 | **True** | 0 | 0 |
| 10 days | 24 | **True** | 0 | 0 |

10,773 records both paths, 0 row-count delta. **Output is byte-identical.**

**Status:** additive code passes `ds-commit-gate` (py_compile + precommit +
ruff). Pending: DS deploy-cycle coordination → land additive path → nightly
`--shadow` clean-night accumulation → Andrew nod → flip `INCREMENTAL_CAPABLE`.

## 5. Rollout discipline

1. AE converts script N (additive) + offline `--shadow` parity proof.
2. RAVC2 per-script → COO + DS.
3. DS deploys the additive path (full stays authoritative — zero live risk).
4. Nightly `--shadow` accumulates clean-night parity evidence.
5. Andrew nod → flip dispatch `INCREMENTAL_CAPABLE` (separate commit).
6. Verify the next nightly's watermark-gated runtime drop + unchanged output.

No cutover without (clean-night shadow evidence + Andrew nod). Multi-day,
one-by-one, per Andrew's directive.
