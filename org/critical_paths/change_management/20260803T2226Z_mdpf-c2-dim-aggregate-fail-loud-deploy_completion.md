# Deploy completion — MDPF_GLOBAL.C2: dim aggregate account_count carry-read FAIL-LOUD

**Deployer:** 0.2.0_DS_PortfolioAnalytics (Rule-13 DS gold lane) · **Opened/closed:** 2026-08-03 22:24–22:26Z (single-leg, in-session)
**What:** `s3://opal-data-mdpf/code/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py` → repo HEAD @0f0f173351. One hunk: the `load_served_account_count` bare `except → {}` (banked as `:567`; sat at `:566-572` @e82271228b) now RE-RAISES `RuntimeError` with full context (`from e`, cause preserved).
**Authority:** CTO gate grant 20260803T221736Z — scoped to this exact hunk on the 13-HOLD file; nothing else changed (diff = one logical change, 15+/5-).

## Exercise evidence (CTO acceptance: exercised, not asserted)

| Direction | Pre-fix (control) | Post-fix |
|---|---|---|
| Forced failure (absent key `zzz-c2-forced-absent`) | returned `{}` SILENT, WARN-only (captured 22:24:38Z) | **raises** `RuntimeError: C2 FAIL-LOUD: account_count carry-read FAILED for s3://opal-data-portal-v2/json/mdpf/zzz-c2-forced-absent/aggregate-aua-timeseries.json (NoSuchKey: ...) -- refusing to build with a silently-lost count carry...` `__cause__: NoSuchKey` (verbatim capture) |
| Success parity (real `49financial` read) | 8 keys, sha256 `55c159d668d9afdc82788e1eaeb47de6b4889b9bcef6b92221ae4c5202b941fb` | 8 keys, sha256 **IDENTICAL** |

**Observable-surface trace (mandate design note):** raise → `:850` caller (no enclosing try) → `build_49f_artifact` → `main` (no enclosing try) → process rc≠0 → dispatch `|| return 1` → `STAGE6-REVAMP status=error` in chain telemetry `status.json` + chain log — the per-stage surface **proven live this same day by the 6c error on the identical path**. No swallow above the fix point exists.

## Verification

- commit-gate clean; `comp-pipescript deployed dim_mdpf_non_model_assets... --pipeline mdpf` → **1 MATCH / 0 STALE** post-upload.
- **Cycle-attribution note (per TO):** this deploy LANDS BEFORE tonight's cycle. If tonight's run surfaces a loud `C2 FAIL-LOUD` error on a frozen/absent json/mdpf mirror key, that is the fix WORKING, not a regression. (49f/inf mirror keys are live-written by the smartx Lambda — the healthy read path is expected to pass.)

## Finding routed (out of scope, untouched)

Sibling swallow: `load_account_dist_frontier_counts` carries its own `except Exception` → honest-None WARN (`:621-625`-class @e82271228b, reads the STAGED gold tree, not json/mdpf). Different read, arguably intentional (frontier honest-None is a declared behavior), but it is the same swallow SHAPE one function below — routed to CTO for a keep-or-C2-treatment ruling; NOT fixed here per the one-hunk gate.
