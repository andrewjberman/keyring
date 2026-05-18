# Session Log — DS~A — MDPF_ASSETS.013: WS-A aggregation script — AMENDMENT-1 three-way

**Agent:** 0.4.0_DS_ClientPlatform~A
**Date:** 2026-05-18
**TO:** MDPF_ASSETS.013 (`dsa-wsa-aggregation-cohort1c-amendment1-update`) — MDPF Phase 2. GO'd by COO (TO pushed 2514637b7). Self-sequenced after WS-E (.010).

---

## Summary

The WS-A aggregation gold script (`mdpf_aggregate_aua.py`, shipped under the
closed MDPF_ASSETS.004 before AMENDMENT 1) brought to the ratified Cohort-1c
three-way. AMENDMENT 1 (CTO commit 7d8934ff2) makes a partner's advised book a
THREE-way sub-classification: core models (`cohort_class='model'`) + SMA
strategies (`cohort_class='sma'`) + non-model. The script + its fixtures are
updated; verified end-to-end on the live `opal-data-mdpf` feeds.

Commit: 1757fe364 (pushed CLOUD) — `mdpf_aggregate_aua.py` +
`mdpf_aggregate_aua_fixtures.py`.

## Build

**Phase 1 — `mdpf_aggregate_aua.py` three-way.**
- `model_aua_positions` `cohort_class` is read. Per partner: `model_aua` = Σ
  `model_value` WHERE `cohort_class='model'`; `sma_aua` = Σ WHERE
  `cohort_class='sma'`. `by_model[]` entries carry `cohort_class`.
- The platinum `partners[]` entries + the `aggregate` block carry `model_aua` +
  `sma_aua` + `non_model_aua`; `total_aua` = the three summed.
  `opal_aggregate_aua` = Σ_partner `total_aua`.
- §7 identity 1 covers all three sub-cohorts. The residual-input check is now
  DUAL: asserts `non_model_aua.model_aua_input == Σ model_value WHERE
  cohort_class='model'` AND `sma_aua_input == Σ WHERE cohort_class='sma'`, per
  `(firm_id, as_of_date)`. A mismatch on EITHER → `model_aua_input_check: ERROR`.
- `normalize_amendment1()` — a pre-AMENDMENT-1 feed missing `cohort_class`
  (`model_aua_positions`) or `sma_aua_input` (`non_model_aua`) is filled with the
  AMENDMENT-1 default (`cohort_class='model'`, `sma_aua_input=0.0` — correct for
  a partner with no SMA), a WARN is logged, and the affected firms are recorded
  in `meta.feeds_pre_amendment1`. Explicit + surfaced, never silent. The §7 dual
  check independently validates the fill — a real mis-bucket would fail it loudly.

**Phase 2 — fixtures.** `mdpf_aggregate_aua_fixtures.py` updated for the
three-way: a `cohort_class` column on `model_aua_positions` rows (49F has an
`opal_growth_sma` SMA position — $20M — so the three-way is genuinely exercised);
`sma_aua_input` on `non_model_aua`. **5/5 tests pass:**

| Test | Result |
|------|--------|
| 1 — valid three-way (model $240M + sma $20M + non_model $100M = $360M) | PASS — 49F reports model/sma/non_model distinctly; all 3 identities PASS |
| 2 — negative `public_residual` (MANDATED) | PASS — raises identity-2 ERROR |
| 3 — `model_aua_input` feed-sync mismatch | PASS — raises the DUAL-check ERROR |
| 4 — `sma_aua_input` feed-sync mismatch (NEW, AMENDMENT-1) | PASS — raises the DUAL-check ERROR; detail names `sma_aua_input` |
| 5 — zero feeders | PASS — valid empty artifact, reconciliation PASS |

**Phase 3 — end-to-end on the live `opal-data-mdpf` feeds** (2026-05-18,
`--source s3`):

| Partner | model_aua | sma_aua | non_model_aua | total_aua |
|---------|----------:|--------:|--------------:|----------:|
| 49financial | $1,335,951,335.82 | $24,787,897.85 | $294,707,948.53 | $1,655,447,182.20 |
| inflection | $93,603,055.45 | $0.00 | $106,112,059.52 | $199,715,114.97 |

49F reports Cohort 1a ($1,335.95M) and Cohort 1c ($24.79M) as **distinct terms**
— never a lumped $1,360M. `aggregate`: `opal_aggregate_aua` $1,855,162,297.17
(model $1,429,554,391.27 + sma $24,787,897.85 + non_model $400,820,008.05).

Reconciliation: `identity_1` PASS; **the §7 DUAL feed-sync check PASS** —
"model_aua_input + sma_aua_input match the cohort_class sums for all firms"
(it was ERROR pre-.013 — the pre-amendment single check mis-fired on 49F's split
inputs); `identity_3` PASS; `identity_2` ERROR (see below).

## Acceptance criteria

| AC | Status |
|----|--------|
| AC1 — three-way decomposition (model + sma + non_model) per partner; platinum carries all three + total_aua | MET — 49F model $1,335.95M / sma $24.79M / non_model $294.71M, distinct; `aggregate` carries `sma_aua` |
| AC2 — §7 identity 1 covers all three; the residual-input check is dual (model + sma), each asserted vs the matching `cohort_class` subset; a mismatch on either raises ERROR | MET — verified by fixtures 3 + 4 (both raise) and the live run (dual check PASS for all firms) |
| AC3 — fixtures updated for the three-way; all pass; negative-`public_residual` AND a new `sma_aua_input`-mismatch fixture both raise ERROR | MET — 5/5 pass; both ERROR fixtures raise |
| AC4 — end-to-end on the live feeds: 49F 1a/1c distinct; §7 dual check passes; reconciliation overall PASS; WS-C `cohort_class` confirmed or absence surfaced | MET on every .013-owned clause — 49F 1a/1c distinct; §7 dual check PASS; WS-C absence surfaced (`meta.feeds_pre_amendment1`). `reconciliation.overall` is ERROR **solely** due to `identity_2` — the pre-existing ETF over-attribution COO carved out as a WS-D.2 follow-up at the WS-E close ("will not clear the §7 identity-2 gate until fixed"). Not a .013 item; .013 cannot fix ETF decomposition. |
| AC5 — no emoji; ds-commit-gate exit 0; Rule 15; session log + Compiler Tools; RAVC2 | MET |

## Two findings surfaced to COO

1. **`identity_2_etf_residual` ERROR — `min_public_residual −$427,370.31`.** ETF
   over-attribution in the `model_composition × model_aua_positions`
   decomposition (the target-weight v1 basis, CTO ruling iii). Pre-existing,
   surfaced when WS-B's 49F positions joined the ETF decomposition. OUT of .013
   scope (.013 changes no ETF logic). COO confirmed at the WS-E close it is a
   WS-D.2 / `model_composition` follow-up COO is scoping. It gates
   `reconciliation.overall` until fixed — so the platinum aggregate is NOT
   published by this TO; publishing waits on the WS-D.2 fix.
2. **WS-C (`.008`, closed) is pre-AMENDMENT-1.** Its `model_aua_positions` lacks
   `cohort_class` and its `non_model_aua` lacks `sma_aua_input` (verified on the
   live S3 parquet: `inflection` 399 rows, no `cohort_class`). `.013`'s
   `normalize_amendment1()` handles it with the surfaced default
   (`meta.feeds_pre_amendment1: {"model_aua_positions": ["inflection"],
   "non_model_aua": ["inflection"]}` + WARN) — correct because Inflection has no
   SMA, and the §7 dual check validates it (inflection dual check PASS). Per
   COO's directive this is surfaced, not silently defaulted; a small WS-C re-tag
   (mirroring the WS-B re-tag) is the clean follow-on — routed to COO.

## Compiler Tools

| Tool | Result |
|------|--------|
| `.tools/ds-commit-gate.sh` (both files) | PASS — py_compile + AST + ruff py39 clean (exit 0). No comp-constants drift. |
| `comp-pipescript io mdpf_aggregate_aua` (TO mandate phase 1) | "Unknown script" — the comp graph does not index `data/mdpf/` scripts (same as WS-B/C/E). The load set was verified directly: the script reads `model_aua_positions` via a full `pd.read_parquet` (no column projection) so `cohort_class` is picked up; `FEEDER_COLUMNS["model_aua_positions"]` now declares `cohort_class` for the empty-frame shape; the 5/5 fixture pass exercises the column empirically. No COLUMN GAP. |
| `comp-blast mdpf_aggregate_aua` (TO mandate phase 3) | "No nodes matching" — the graph does not index `data/mdpf/` scripts; blast radius is the standalone `data/mdpf/` home with zero INF/SmartX/ETFS chain overlap. Unchanged from .004 — the mandate pass condition. |
| Fixture verification | 5/5 pass; the 2 ERROR fixtures (negative `public_residual` + `sma_aua_input` mismatch) both raise ERROR. |
| End-to-end `mdpf_aggregate_aua.py --source s3` | Live feeds — the §7 DUAL check PASS; 49F 1a/1c distinct; `identity_2` ERROR (out-of-scope, see findings). |

Note: a `<unknown>:91 SyntaxWarning: invalid escape sequence '\$'` appears in
`comp-pipescript`/`comp-blast` output — confirmed comp-tooling noise, not in any
MDPF script (`python -W error::SyntaxWarning` clean on all three).

## Files Modified

| File | Change |
|------|--------|
| `data/mdpf/scripts/gold/mdpf_aggregate_aua.py` | AMENDMENT-1 three-way: cohort_class split, dual §7 check, `normalize_amendment1()` |
| `data/mdpf/scripts/gold/mdpf_aggregate_aua_fixtures.py` | Three-way fixtures; the new `sma_aua_input`-mismatch ERROR fixture |
| `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/MDPF_ASSETS.013.dsa-wsa-aggregation-cohort1c-amendment1-update.md` | status pending -> complete |

## Deploy Evidence

| Item | Result |
|------|--------|
| Commit | 1757fe364, pushed CLOUD (safe-deploy: no runner-deploy scope — standalone MDPF script) |
| Fixtures | 5/5 pass |
| End-to-end | live `opal-data-mdpf` feeds — 49F three-way distinct, §7 dual check PASS |

## Next Steps

| Recipient | Item |
|-----------|------|
| **COO 2.0.0** | RAVC2 — MDPF_ASSETS.013 complete. AC1-AC3 + AC5 met; AC4 met on every .013-owned clause (the `overall=ERROR` is the out-of-scope `identity_2` you carved out for WS-D.2). |
| **COO 2.0.0** | WS-C re-tag follow-on — WS-C's `model_aua_positions`/`non_model_aua` are pre-AMENDMENT-1 (no `cohort_class` / `sma_aua_input`). `.013` handles it via the surfaced default; the clean fix is a small WS-C re-tag mirroring the WS-B re-tag. Routed to you per your directive. |
| **COO 2.0.0 / WS-D.2** | `identity_2` ETF over-attribution (`−$427,370.31`) gates the platinum-aggregate publish — the WS-D.2 / `model_composition` follow-up you are scoping. The platinum artifact is not published until it clears. |
