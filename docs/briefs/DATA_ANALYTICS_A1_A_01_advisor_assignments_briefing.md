# A_01 — advisor_assignments — DATA_ANALYTICS layer briefing

**Script:** `data/black_diamond/scripts/gold/A_01.advisor_assignments.py`
**Output:** `gold/dimensions/advisor_assignments_history.parquet`
**Layer / order:** Group A (dimensions), runs after A_00 (reads it as baseline), in PHASE chain `CHAIN_CANONICAL` / GROUP_A.
**Essential status (Andrew's framework):** ESSENTIAL — feeds D_00c (portal_leaderboard) + D_02 (advisor_client_detail) → ADVI portal advisor/fee surfaces.
**Author/project:** 0.4.0_DS_ClientPlatform / ADVI_GLDOPS (2026-04-06).
**Briefing by:** 0.4.0_DS_ClientPlatform, 2026-06-24 (Andrew-direct A1 layer-walk). Source-grounded (file:line) + deployed-verified.

---

## 1. What it does

Builds a **SCD Type 2 (slowly-changing-dimension) history** of the advisory team + fee-split configuration for **every account over time**. For each account it scans `silver/transactions/` chronologically; whenever the tracked tuple changes between transactions it **closes the prior record** (`end_date`) and **opens a new one** (`effective_date`). One account therefore yields N records = N distinct advisor/split configurations it has had.

**Tracked fields (a change in ANY opens a new SCD record), L70-80:**
- 5 roles: `architect, implementor, consultant, local_ops, additional_advisor`
- 6 splits: the 5 role `_split_pct` + `house_split_pct`

**Sources:**
- PRIMARY: `silver/transactions/` (1,815 daily files, 2020-present) — the only source covering every account ever seen.
- BASELINE FALLBACK: `gold/dimensions/accounts_dimension_latest.parquet` (A_00) — supplements accounts that have no transactions (role names only, splits = 0), L386-415.

**Boundary (note for A_02):** A_01 tracks **WHO + SPLITS only**. Fee economics (`fee_bps`, `fee_schedule`) are owned by **A_02** (fee_rate_history) — L834-836. Downstream joins A_01 ⋈ A_02 on (account_id, date-range) for revenue attribution.

---

## 2. Architecture / data flow

1. **Load** transactions (parallel, 64 workers), keep only `account_id, trade_date, transaction_id` + tracked fields; tag each row with provenance `_file_date` + `_intra_pos` (L182-189).
2. **Dedup** on `transaction_id` via a total-order sort `(transaction_id, _file_date, _intra_pos)` keep=last (L238-246) — deterministic survivor.
3. **Normalize** roles (strip BD sentinels → '') + splits (BD string→float, sentinels→0), L127-147 / L346-353.
4. **Daily-state dedup** on `(account_id, trade_date)` total-order keep=last (L355-365) — one config per account-day.
5. **Change detection:** hash the tracked tuple, open a new record on account-change OR state-change (L370-382); `end_date` = next effective_date − 1 day; `is_current` = last record.
6. **Baseline supplement** for txn-less accounts (L386-415).
7. **Multi-role split normalization** (L271-330): if one person holds 2+ roles with split>0 on a record, average their splits across those roles (total share unchanged; stops role-rollup double-counting). Andrew-approved 2026-04-09.
8. **Save** + write the daily-state cache + watermark (both modes).

---

## 3. Recompute posture — THE headline finding

**A_01 runs a FULL rebuild EVERY NIGHT** — catalog `A_01|...|--upload` (NO `--incremental`), confirmed **local AND deployed**. Each night it reads **1,815 transaction files** (2020-2026) to reconstruct the entire **15,292-row** SCD from scratch, although nothing pre-2026 ever changes.

**A complete, sophisticated incremental path already exists** (L468-749):
- daily-state-grain cache `ADVISOR_ASSIGNMENTS_DAILY_STATE` + watermark + 14-day re-read window + etag-fingerprint restatement-detection + cold-start fallback.
- Correctness argument (L472-491): `(cache rows from files ≤ floor) ∪ (raw rows from window files > floor)` → the UNCHANGED builder → identical output, because the total-order dedup survivor can never be out-ranked by a cache loser.

**It is shadow-parity PROVEN** (run_shadow_parity, L690-749): `identical=True, 0 cell_mismatches, 15292==15292`, **5+ consecutive nights** (06-20..06-24; 13 scorecards at `gold/_parity/advisor_assignments/`).

**The code's OWN flip-gate** (L469-471): "Full-rebuild stays the dispatch default + authoritative *until shadow parity is proven over clean nights and the dispatch is flipped*." **The condition is MET — but the flip never happened.** Worse, A_01 is in `GLDINC_SHADOW_SET`, so the incremental ALSO runs nightly as a shadow — the pipeline pays for a full build **plus** a shadow build of the same thing.

**FIX (authored 2026-06-24, Andrew-direct; routed to 0.7.0_AE_CloudOps — gold_dispatch.sh is the CLOUD_OPS_OR_ETL lane):**
- 1-token change: bd catalog L80 `--upload` → `--upload --incremental`.
- SAFE NOW: the full runs already maintain the cache+watermark (main() `save_aa_state` both modes) → `--incremental` consumes them immediately; restatement/cold-start self-falls-back to full.
- Deploy: AE commit+push → `aws s3 cp` the .sh to `s3://opal-data-bd/code/gold/` (the EC2 pull-path; safe-deploy skips .sh) → verify → deploy-ledger.
- **Scope: bd ONLY.** cot A_01 + inf INF_A_01 are forks with **ZERO incremental code** (0 fn refs, 0 scorecards) — flag-flipping breaks them; they need the incremental **ported + shadow-proven first** (separate DS+AE TO).

---

## 4. Tech debt

- **Stale docstring** (L18-21, L26-29): advertises outputs `fee_bps`, `fee_schedule` from `silver/allocations` — but those moved to A_02 (L834). Header lists outputs it no longer produces.
- **Hardcoded stale count** "1,764 daily files" (L27) — actual 1,815.
- **Legacy dual-write** (L770-774): writes the artifact to a second `LEGACY` key on every run ("during migration") — confirm migration done → drop.
- ~280 lines of incremental + shadow machinery (L468-749) maintained but the production benefit (the flip) uncaptured until the flip lands.

## 5. Bullshit / overfit

- **49F-overfit sentinel** (L96): `SPLIT_NULL_PATTERNS` includes `"no 49 house split % value assigned"` — a firm-specific hardcoded string. The `NULL_VALUES`/`SPLIT_NULL_PATTERNS` BD-sentinel cleanups (L83-101) belong in **silver**, not re-applied in gold each build.
- **Row-by-row multi-role normalization** (L271-330): `for idx in history.index: ... history.at[idx, ...]` over 15,292 records × 5 role-pairs — O(rows) Python iteration, vectorizable. The RULE is legit (Andrew-approved); the IMPLEMENTATION is the debt.

## 6. What's GOOD (keep — not debt)

- **Deterministic-ordering oracle-fix** (ADHC_GLDINC, L182-189 / L238-246): provenance `_file_date`+`_intra_pos` + total-order dedup fixed a real night-to-night SCD-survivor nondeterminism (pre-fix 14,733-14,742 records on identical data). Solid.
- **Load-completeness guard** (L207-234): retry-with-backoff on transient S3 read failures, then **fail LOUD** rather than build from an incomplete load (a swallowed failed read = 192 missing rows / 18 shifted SCD keys, empirically). Exactly right.
- The incremental design itself is sound + proven — the only issue is it isn't wired into the dispatch.

## 7. Actions

| When | Action | Owner |
|---|---|---|
| NOW (routed) | Flip bd catalog A_01 → `--incremental` + deploy + ledger | 0.7.0_AE_CloudOps (DS deploy-verifies) |
| A2 | Move BD-sentinel cleanups (NULL_VALUES/SPLIT_NULL_PATTERNS, the "49 house" string) to SILVER; vectorize multi-role normalization; fix stale docstring; drop legacy dual-write | DS |
| A3 | Parameterize the SCD builder firm-agnostic (the engine is reusable across firms); port the incremental + shadow-prove to cot/inf so they can flip too | DS authors / AE deploys |
| Cleanup | Retire the GLDINC shadow for A_01 once the flip is live + stable | AE |

## 8. Status

- **Essential** (Group-D closure). Well-engineered core; the debt is the un-flipped incremental + silver-belongs cleanups.
- bd flip: ROUTED to 0.7.0_AE_CloudOps (Andrew-direct), ready-to-execute, awaiting AE commit+deploy → DS deploy-verify.
- cot/inf incremental port: FLAGGED (separate TO).
