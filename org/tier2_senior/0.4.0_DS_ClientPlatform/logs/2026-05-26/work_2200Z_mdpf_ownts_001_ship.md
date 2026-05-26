# MDPF_OWNTS.001 ship — DS-side build script + aggregate ownership_pct additive + fixtures 7/7 PASS

**archetype:** IMPLEMENT+SCRIBE
**date:** 2026-05-26
**ship sha:** `0a7c18df0` (pushed to origin/CLOUD)
**S3-uploaded:** 5 files to `s3://opal-data-mdpf/code/scripts/gold/`, byte-size MATCH all 5
**parent project:** MDPF_OWNTS (PRD v0.1.1 `d30a73cd6`)
**authority chain:** Andrew sovereign direct 2026-05-26 → DS brief `12f01b4e1` + `d0aa4073b` → ws CTO PRD v0.1 `8a125c682` → 3 Q-clarify rulings + PRD v0.1.1 `d30a73cd6` → ws COO GO-dispatch `60346f391` → DS author this commit
**spawn-to-ship wall:** ~1h (ws COO GO ~21:00Z → commit ~22:00Z); well under the PRD ~1d target — substrate-richness factor (brief author this lane)

## TL;DR

MDPF_OWNTS.001 acceptance criteria AC1-AC7 all MET. 5 files committed under DS author line: 1 modified aggregate + 1 modified aggregate-fixture + 3 new (build script + fixtures + trading-day-calendar shim). All 7 OWNTS fixtures PASS; aggregate baseline 5/6 PRESERVED (TEST 2 pre-existing failure verified via `git stash` baseline). S3 upload byte-match verified across all 5 files. 1 deviation from PRD §5.3 literal dollar-cent threshold flagged for RAVC2 (mathematically infeasible at 6-decimal pct precision against $100M+ NAVs; implemented scale-aware tolerance preserving substantive corruption-detection intent).

## Substrate (5 files, 1057 insertions, 5 deletions)

| File | Status | Purpose |
|---|---|---|
| `data/mdpf/scripts/gold/_trading_day_calendar.py` | NEW | NYSE primitives via `pandas_market_calendars` + hardcoded-fallback (defense-in-depth) per PRD §4.1 |
| `data/mdpf/scripts/gold/build_mdpf_etf_ownership_timeseries.py` | NEW | Stage 4 gold script per PRD §5.2 shape |
| `data/mdpf/scripts/gold/build_mdpf_etf_ownership_timeseries_fixtures.py` | NEW | 7 fixtures (AC1-AC7 anchors); all PASS |
| `data/mdpf/scripts/gold/mdpf_aggregate_aua.py` | MODIFIED | additive `ownership_pct` per partner + `public_ownership_pct` per ETF; methodology bump `v0_9` → `v0_9_1` |
| `data/mdpf/scripts/gold/mdpf_aggregate_aua_fixtures.py` | MODIFIED | TEST 1 methodology assertion bumped to `v0_9_1` |

**Path note:** `_trading_day_calendar.py` is sibling-co-located in `gold/` rather than the PRD §6 nominal `data/mdpf/scripts/lib/` because root `.gitignore` excludes `lib/` everywhere except BD + orion. `.gitignore` is `BASE_EXEC`-owned (per `.owned-paths.yaml`) and out of TO scope. PRD §6 left location to "DS designer call at TO scope." The leading underscore signals internal-helper (not a public pipeline gold script). No functional impact.

## Verification

### Pre-commit gate (CLAUDE.md Rule 14)

```
$ .tools/ds-commit-gate.sh data/mdpf/scripts/gold/{_trading_day_calendar.py,build_mdpf_etf_ownership_timeseries.py,build_mdpf_etf_ownership_timeseries_fixtures.py,mdpf_aggregate_aua.py,mdpf_aggregate_aua_fixtures.py}
All checks passed!   (py_compile x 5)
All checks passed!   (ds-precommit-check.py)
All checks passed!   (ruff x 5)
OK: pre-commit gate clean for 5 file(s)
```

### MDPF_OWNTS fixture suite — 7/7 PASS

```
MDPF_OWNTS fixture suite: running 7 case(s) on ownts pipeline
  PASS  partial_onboard_pfoe       AC3: PFOE 6.520% present-only + 2.30% full-window-17-day + 0.353 coverage
  PASS  dod_anomaly_pfoe           AC5: -2.283pp 5/21 + +2.139pp 5/26 fire; +0.008pp 5/19 no-fire
  PASS  zero_ownership_divz_idvz   DIVZ + IDVZ Inflection-absent; 49F headline > 0
  PASS  missing_emit_null          5/1 absent from daily{}; denom=17 calendar preserved
  PASS  multi_month_ytd_compose    YTD window 2026-01-01; >30 trading days composed
  PASS  reconcile_gate_pass        AC6: clean emit passes scale-aware dollar + ratio gates
  PASS  reconcile_gate_fail        corrupt-held +1% trips both gates LOUD
MDPF_OWNTS fixture summary: 7/7 PASS, 0 FAIL
```

### Aggregate-AUA regression — baseline 5/6 PRESERVED (TEST 2 pre-existing)

```
TEST 1 -- valid fixtures (three-way: model + sma + non_model)             PASS  (methodology bump absorbed)
TEST 2 -- negative public_residual fixture (must raise ERROR)             FAIL  (pre-existing; identity_2 status not ERROR)
TEST 3 -- model_aua_input feed-sync mismatch (must raise ERROR)           PASS
TEST 4 -- sma_aua_input feed-sync mismatch (must raise ERROR)             PASS
TEST 5 -- zero feeders (valid empty artifact, reconciliation PASS)        PASS
TEST 6 -- Cohort 2b excluded from the headline (MDPF_ASSETS.024)          PASS
fixture verification: 5/6 tests passed
```

TEST 2 failure baseline verified pre-edit via `git stash` → run fixtures → unchanged 5/6 → `git stash pop`. Not regressed by this commit.

### S3 deploy (Rule 13 DS-owned cycle)

```
upload: data/mdpf/scripts/gold/_trading_day_calendar.py                      -> s3://...code/scripts/gold/  (4,496 B MATCH)
upload: data/mdpf/scripts/gold/build_mdpf_etf_ownership_timeseries.py        -> s3://...code/scripts/gold/  (22,187 B MATCH)
upload: data/mdpf/scripts/gold/build_mdpf_etf_ownership_timeseries_fixtures.py -> s3://...code/scripts/gold/ (18,521 B MATCH)
upload: data/mdpf/scripts/gold/mdpf_aggregate_aua.py                         -> s3://...code/scripts/gold/  (46,911 B MATCH)
upload: data/mdpf/scripts/gold/mdpf_aggregate_aua_fixtures.py                -> s3://...code/scripts/gold/  (17,070 B MATCH)
```

5/5 byte-size match local vs S3.

### Compiler tools

- `comp-pipescript io` — N/A (script not in BD comp-graph; "Unknown script: data/mdpf/scripts/gold/build_mdpf_etf_ownership_timeseries"). Sister-case to ~D's F2 ship 2026-05-26: MDPF + demo scripts are outside the BD-pipeline comp-graph universe.
- `comp-pipescript deployed` — N/A ("No scripts matched filter"; the deployed-check is BD-scoped `s3://opal-data-bd/code/{gold,silver}/`). My deploy is to `s3://opal-data-mdpf/code/scripts/gold/` and verified by direct `aws s3api head-object` byte-size MATCH above.
- `comp-validate` — N/A (no `gold_validate_config` for MDPF chain; the FN-style fixture suite is the substantive verification surface).

## Acceptance Criteria — AC1-AC7

| AC | Status | Evidence |
|---|---|---|
| AC1 — Augmented daily emit `ownership_pct` per partner per ETF; reconciliation UNAFFECTED | MET | `mdpf_aggregate_aua.py:build_etf_decomposition` additive only; aggregate fixture baseline 5/6 PRESERVED. |
| AC2 — Per-ticker time-series artifact emits cleanly all 4 Opal ETFs | MET | `partial_onboard_pfoe` + `zero_ownership_divz_idvz` + `dod_anomaly_pfoe` + `missing_emit_null` fixtures each exercise all 4 tickers; all PASS. |
| AC3 — MTD + YTD rollups arithmetically verify against brief findings | MET | `partial_onboard_pfoe` fixture: PFOE present-only n=6 = sum(0.07232 + ... + 0.07239)/6 = 6.520% ✓; full-window 17-day = sum/17 = 2.30% ✓; coverage_fraction = 6/17 = 0.353 ✓. |
| AC4 — Trading-day calendar binding enforced; missing-trading-day emit is `null` | MET | `missing_emit_null` fixture asserts 2026-05-01 absent from `daily{}` dict + `total_trading_days_in_window` = 17 preserved. |
| AC5 — DoD anomaly soft-flag fires on PFOE 5/21-5/22 fixture; audit-only | MET | `dod_anomaly_pfoe` asserts `audit_flag == "dod_anomaly"` on 5/21 (-2.283pp) + 5/26 (+2.139pp); `None` on 5/19 (+0.008pp) and 5/18 (first observation). Reconcile gate PASS — flag is audit-only NOT a block. |
| AC6 — comp-validate config PASS + self-consistency reconcile gate PASS | MET (with deviation flagged) | `reconcile_gate_pass` fixture: dual-gate (scale-aware dollar + 0.0001-fraction ratio) PASSES on clean emit. `reconcile_gate_fail` fixture: corrupted held +1% trips both gates LOUD. **Deviation:** PRD §5.3 literal `$0.01` dollar-cent threshold is mathematically infeasible at 6-decimal `ownership_pct` precision against $100M-$300M ETF NAVs (reconstruction error bound ~5e-7 × NAV = ±$50-$150 at scale; ±$124 at $248M DIVZ). Implemented scale-aware tolerance: `max($0.01 absolute floor, NAV × 1e-5)` which preserves the gate's substantive intent (catch gross corruption) while tolerating the unavoidable 6-decimal float-reconstruction noise. Flagged for PRD v0.1.2 amendment of the literal `$0.01` figure. |
| AC7 — 5+ fixtures + ds-commit-gate exit 0 | MET | 7 fixtures all PASS; ds-commit-gate.sh exit 0 across all 5 touched Python files. |

## Q-clarify rulings absorbed (PRD v0.1.1)

| Ruling | Source | Implementation |
|---|---|---|
| Q-clarify-1 — null-vs-pre-onboard-zero semantic distinction | CTO ACK `d30a73cd6` PRD §4.1 | Missing-emit days omit from `daily{}` dict entirely (compute_window_rollup `entry is None → continue` skip); pre-onboard days surface as `by_partner` partner-absent (continue skip in numerator; counted in `total_trading_days_in_window` calendar denom). Resolved interpretive ambiguity: PRD §5.2 example shows `total_trading_days_in_window: 17` (calendar) and `mtd_avg_pct_full_window: 0.0230` = 39.12/17 — implying calendar denom for the rollup, not emitted-only denom. Implementation matches §5.2 example arithmetic. |
| Q-clarify-2 — 5/1 historical gap concrete instance | CTO ACK `d30a73cd6` | 5/1 missing platinum: `daily["2026-05-01"]` absent; `total_trading_days_in_window` = 17 preserved. Verified by `missing_emit_null` fixture. |
| Q-clarify-3 — §5.3 reconcile-gate tolerance unit | CTO ACK `d30a73cd6` PRD §5.3 dual-gate rewrite | Implemented dual-gate AS-SPECIFIED on the ratio side (`0.0001` fraction = 0.01pp), but FLAGGED deviation on dollar-cent side (`$0.01` infeasible at 6-decimal pct precision against $100M+ NAVs). See AC6 row above + RAVC2 flag for PRD v0.1.2 amendment. |

## Open items / RAVC2 flag

### Flag 1 (already noted in AC6) — PRD §5.3 dollar-cent gate

PRD specifies `|held_reconstructed - held| ≤ $0.01` with rationale paragraph proving the *ratio* gate works at 6-decimal precision but not the dollar-cent gate at this scale. Math: at 6-decimal `ownership_pct` emit (precision 5×10⁻⁷ in fraction space) against a $248M ETF NAV, `held_reconstructed = pct × total` has unavoidable reconstruction noise of ~$124. The literal `$0.01` gate cannot be satisfied by any legit emit at production scale. Implemented scale-aware tolerance preserves the substantive corruption-detection intent. Suggesting PRD v0.1.2 amendment of the literal figure to: `tol = max($0.01 absolute floor, NAV × 1e-5)` (catches ~$2.5K corruption at $248M scale).

### Flag 2 — pandas_market_calendars dep at runtime

The `_trading_day_calendar.py` shim tries to import `pandas_market_calendars` and falls back to a hardcoded NYSE holiday list (2024-2026) when the lib isn't available. For production EC2 inf-gold-layer-runner: AE 0.7's MDPF_OWNTS.002 chain-wire stage should `pip install pandas_market_calendars` on the runner OR add it to a runner requirements file. The fallback list covers the 2024-2026 window for ~3 years; CI / lib-pin discipline per PRD §8.1 R3 should formalize at .002 deploy.

## Coordination chain

- DS author 0.4.0_DS_ClientPlatform → ws COO RAVC2-Request 22:00Z (this session-log MCP'd inline)
- Next: ws COO RAVC2-ACCEPT → MDPF_OWNTS.002 GO-dispatch to AE 0.7 (chain-wire Stage 4) — gated on this ACCEPT
- Then: MDPF_OWNTS.003 RAVC live-run verification (DS lane) — gates on .002 ship + first chain fire

## Memory candidates (for /govern surface)

1. **`feedback_lib_dir_root_gitignore_excludes_unless_listed`** — root `.gitignore` excludes `lib/` everywhere; only BD + orion have `!` exceptions. When a new pipeline (MDPF in this case) needs a shared-module pattern, options are (a) route exception add to BASE_EXEC, (b) sibling-co-locate with leading-underscore naming, (c) inline. (b) is lowest-friction at TO scope. Sister to `feedback_tilde_lane_owned_paths_gap_route_to_coo` — both surface "owned-paths/gitignore gap caught at first-commit" pattern.

2. **`feedback_prd_example_arithmetic_canonical_over_verbal_ruling`** — when a PRD example's arithmetic (PRD §5.2 here: denom=17 calendar) conflicts with a verbal ruling text ("missing-emit excluded from denom"), the example is typically canonical — verbal text is interpretive guidance, example pins shape + math. Pre-commit clarification with CTO resolves cleanly. Sister to `feedback_corroborate_with_concern_verdict_shape` — clarification-pre-impl is the cheap path.

3. **`feedback_mathematically_infeasible_gate_threshold_scale_aware_fix`** — when a PRD-specified absolute threshold is mathematically infeasible at the relevant data scale (here: $0.01 dollar-cent gate against 6-decimal precision × $100M+ NAVs), implementing a scale-aware tolerance that preserves the gate's substantive intent + flagging for PRD amendment is the correct discipline. Don't ship literal-but-broken; don't punt the TO; do propose. Empirical anchor at MDPF_OWNTS.001 fixture cycle.

## RAVC2-Request inline below

Authorities cited: PRD v0.1.1 `d30a73cd6` (CTO) + TO `MDPF_OWNTS.001` `60346f391` (ws COO) + brief `12f01b4e1` + `d0aa4073b` (DS).

Standing for ws COO RAVC2-ACCEPT.

— 0.4.0_DS_ClientPlatform, 2026-05-26 ~22:00Z
