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
| **A_02** fee_rate_history | SCD-2; reconstruct change-points from existing history + read only new+window fee files, re-run same builder | LOW — append-natured, immutable closed periods; **probe-verified: 0 forward-dated + 0 back-dated-beyond-14d rows in all 1,881 fee files** | **1 (DONE, parity proven)** |
| **A_01** advisor_assignments | **DAILY-STATE-GRAIN cache** (load_flows preflt pattern), NOT the A_02 trick: (a) output is mutated post-detection (multi-role split averaging) so it can't reconstruct; (b) **probe: 38% of recent txn files carry rows back-dated >14d (worst -519d)** — a change-point cache would fall back nearly every night. Full (account,date) grain + per-row file provenance absorbs back-dated insertions exactly; eviction-by-provenance handles in-window restatement | MED — known residual: cross-boundary txn_id re-post with changed trade_date (shadow-detected) | 2 |
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

## 4b. Measured data-shape probes (2026-06-11) — design inputs, not assumptions

One-off read-only probes of source-file date integrity (trade_date vs file date),
run locally before finalizing each design:

| Source | Files | Forward-dated (trade>file) | Back-dated >14d | Consequence |
|---|---|---|---|---|
| silver/fees/ | 1,881 | **0** | **0** | A_02 change-point reconstruction + 14d window valid as designed |
| silver/transactions/ | 1,808 | 1 (2026-01-30, +3d) | **39 files, worst -519d; 26/68 (38%) of files since 2026-03** | A_01 change-point cache UNVIABLE (fallback ~every night) → daily-state-grain cache design |

Implication for later scripts: **A_03 and B_01 read silver/transactions too** —
their incremental designs inherit the back-dated reality and need grain-level
caches or equivalent, not naive date-partition skipping.

Also fixed from this analysis: A_02 BACK-DATED ROW GUARD (deployed c8ed91949) —
any window-file row with trade_date <= window_floor → full-rebuild fallback
(A_00/load_flows "historical backfill → full scan" class). My original 1/3/10-day
shadows passed because no back-dated fee rows existed — the guard makes it
structural rather than empirical-luck.

## 4c. Pre-existing full-path nondeterminism (documented, NOT fixed — never-widen)

A_01's full path concats files in thread-completion order; cross-file ties at the
same (account_id, trade_date) resolve keep='last' = non-deterministic survivor
when the colliding rows differ. Pre-existing behavior; per the GLDINC Option-A
doctrine (cache must match oracle; do NOT redesign shared dedup semantics) the
incremental mirrors the same code and any shadow diff isolated to this class is
a DATA finding to escalate, not a code bug to "fix" by changing survivor logic.

## 4d. A_01 status: BLOCKED-EXTERNAL on oracle stabilization (CTO-ruled fix-oracle-first)

The A_01 offline shadow FAILED parity (61 keys) and root-caused to a PRE-EXISTING
defect in the full path itself: **the A_01 oracle is non-deterministic** —
cross-file (account_id, trade_date) ties (back-dated rows colliding with
original same-day rows) resolve by `drop_duplicates keep='last'` over
thread-completion-order concat. Evidence: consecutive full builds of identical
data produced 14,733/14,735/14,740/14,742 records (10-36 key wobble per pair);
served advisor_assignments_history (→ C_08/D_00c/D_02) flips attribution keys
night-to-night with no data change. The incremental's diff is the SYSTEMATIC
variant (union order forces window-row wins vs the oracle's random winner) —
byte-parity against a random tie-winner is unachievable by construction.

**CTO ruling (2026-06-11 211102Z): fix-oracle-first APPROVED.** DS implements a
deterministic tiebreak as its own reviewed gold-lane change (sort on
(account_id, trade_date, _file_date, intra-file position) before dedup —
removes the completion-order dependency entirely), changed-keys delta
documented (never-widen-conscious). Then A_01 incremental re-proves parity
against the stabilized oracle and resumes. Diagnostic artifacts:
/tmp/a01_diag_{full1,full2,incr}.parquet.

**Oracle-fix ENGINEERED + PROVEN (AE, 2026-06-11 ~2146Z; DS split option-1,
handed off for DS review/commit/deploy):**
- Fix: _file_date + _intra_pos provenance in _load_one; total-order sort
  before BOTH dedups (txn_id and (account_id, trade_date)); survivor =
  "latest file, last row" everywhere. Plus a LOAD-COMPLETENESS GUARD: a
  failed file read now raises instead of WARN-and-continue.
- Determinism proof: 4/4 complete-load builds BYTE-IDENTICAL (14,847 rows,
  0 sym_diff, 0 cell mismatches). Pre-fix code never matched twice.
- SECOND pre-existing defect caught live during the proof: one transient S3
  read failure silently dropped a file (192 raw rows) and shifted 18 SCD keys
  — the swallowed-exception load path made even a deterministic oracle
  non-reproducible. Hence the guard (failure-path-only change).
- Changed-keys delta: 122 keys / 60 accounts vs the pre-fix sample;
  account-level containment within the enumerated 79-key tie-population =
  TRUE. txn_id sort is load-bearing (32,277 cross-file txn_ids dataset-wide —
  the earlier 3-pair disjointness probe undersampled).
- A_02 confirmed needing no equivalent fix (no cross-file ties in fees).

## 4e. B_02 canonical_lots — design (third pattern: PER-DATE INPUT FINGERPRINT)

Empirical S3-version evidence (etag comparison across nightly rebuilds):
- `lots_realized/{old-date}`: re-uploaded EVERY run, byte-identical content
  (same etag 6 consecutive runs) — recompute + write waste, plus 2 identical
  S3 noncurrent versions/day of version bloat.
- `lots_unrealized/{old-date}`: writes STOP ~7 days after the date (inputs age
  out → empty → no write) — already self-limiting.
- BUT naive date-skipping is WRONG and sealed-dates would freeze out late
  postings: bd_realized is one all-dates file re-read nightly; a late-posted
  realized row at an old trade_date legitimately CHANGES that date's output.

Design: per-date INPUT fingerprints in `gold/meta/canonical_lots_watermark.json`:
hash(bd_realized rows per trade_date), hash(canonical_prices rows per date),
etags of per-date Schwab ULN/ULT/RLD + silver alloc files. Recompute EXACTLY
{dates whose any input-fingerprint changed} ∪ {new holdings dates}; skip the
rest (no recompute, no rewrite). Reference-data hash (mappings/cusip-bridge/
closure_map) change → full fallback. MORE faithful than B_00 sealing (late
postings propagate); kills both the recompute and the version bloat.
Semantic note for DS: skipped dates stop getting fresh LastModified stamps —
anything monitoring old-partition freshness must key on content, not mtime.

## 4g. Late-session corrections (2026-06-11 evening, measured > assumed)

**A_03 + B_01: pattern #4 (WHOLE-RUN INPUT-FINGERPRINT GATE) — both hybrid
designs in §3 are RETIRED.** S3-version evidence:
- A_03: old partitions change EVERY data-night (retroactive reconciliation is
  load-bearing; per-date narrowing would mean reimplementing it) BUT
  no-input-change runs are byte-identical → gate the whole 563s run on one
  2,520-component input digest.
- B_01: history is APPEND-ONLY (old partitions never rewritten); reruns
  byte-identical incl. a midnight-straddling pair (snapshot_date anchors to
  the latest alloc partition, not wall clock) → gate the whole 731s FIFO
  replay (2,658-component digest). The "lot-state + daily revaluation" hybrid
  was unnecessary.
Combined: ~1,294s of the ~1,734s no-change-night waste.

**CLASS-N census (the A_01 defect as a class):** DS's proactive scan found the
dedup signature in 10 more scripts; my assembly-pattern census + CTO's
independent code-read CONVERGED: the discriminator is the CONCAT ASSEMBLY —
index-slot (dfs[i]=result; deterministic): A_00, A_03, B_01,
build_canonical_prices_v2, E_02/03/04/09/10. Completion-order append
(nondeterministic): **A_04 only** (+E_13 unverified, diagnostic). CTO class
ruling 230339Z: fix A_04 (A_01 remedy verbatim); index-slot ratified as the
convention for new parallel loads; ds-precommit AST-rule candidate routed to
COO. A_03's hold/un-hold round-trip took ~15 min and validated the
fix-oracle-first sequencing.

**A_04 (7/7): ORACLE-FIX ONLY; KEEP-FULL recommendation for the conversion.**
The 90-day window anchors to max(trade_date) (input-driven, fine), but
created_date/updated_date are now()-stamped — every run drifts those bytes by
design, so a gate needs a timestamp-semantics ruling… for a 31s script. Not
worth the review surface. The CLASS-N oracle-fix (provenance + total-order +
index-slot assembly) is mandatory regardless and shipped with materiality +
determinism + delta proofs.

## 5. Rollout discipline

1. AE converts script N (additive) + offline `--shadow` parity proof.
2. RAVC2 per-script → COO + DS.
3. DS deploys the additive path (full stays authoritative — zero live risk).
4. Nightly `--shadow` accumulates clean-night parity evidence.
5. Andrew nod → flip dispatch `INCREMENTAL_CAPABLE` (separate commit).
6. Verify the next nightly's watermark-gated runtime drop + unchanged output.

No cutover without (clean-night shadow evidence + Andrew nod). Multi-day,
one-by-one, per Andrew's directive.
