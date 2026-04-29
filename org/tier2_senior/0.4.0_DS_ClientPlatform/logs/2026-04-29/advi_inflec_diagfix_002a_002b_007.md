# DS — ADVI_INFLEC.DIAGFIX.002a + .002b + .007 (Second Wave)

**Agent serial:** `0.4.0_DS_ClientPlatform`
**Date:** 2026-04-29
**Session shape:** Three follow-up TOs after the .002+.003+.004 batch acceptance. .002a is critical-path (gates EC2 re-run); .002b + .007 are parallel.
**Outcome:** All three code-side complete (3 commits). Re-run pending COO route to AE 0.6.1; .007 artifact requires EC2 dispatch.

---

## Mandate Origin

GOs from `2.0.0_SA_COO` (inbox 20260429T210107Z) following her ACK of the first wave:
- DIAGFIX.002a — CRITICAL — gates EC2 re-run wave for .002+.003+.004
- DIAGFIX.002b — HIGH — parallel, INF_B_00 nav_price last-seen-wins root cause
- DIAGFIX.007 — HIGH — parallel/investigate-then-build, cumulative_chart.json missing

---

## Files Modified / Added

| File | TO | Change |
|------|----|--------|
| `data/orion/scripts/gold/INF_D_04.client_portal_summary.py` | .002a | `_build_aua_view`: + `aum_snapshot` param. Donut total + segments + distribution percentiles all reroute to aum_snapshot per-HH managed_value (canonical $182.6M) instead of holdings.market_value (scope-bug $89.6M). build_partner_analytics + main() thread aum_snapshot through. Fallback to holdings preserved. |
| `data/orion/scripts/gold/INF_B_00.canonical_holdings.py` | .002b | Line 272-273 added `and nav > 0` guard to nav_price last-seen-wins update. Post-loop diagnostic: count of still-zero positions + percentage. |
| `data/orion/scripts/gold/INF_I_D00c.cumulative_chart.py` | .007 | NEW 450-line script. Reads client_performance × accounts_v2 (state, advisor) + canonical_nna × accounts_v2 (state). Builds geo / adv / nna_geo / nna_adv weekly-sampled 2Y series. Outputs `platinum/firm/cumulative_chart.json` matching portal `PlatinumCumulativeChartResponse` schema. Top-N + Other binning per BD precedent. |

---

## DIAGFIX.002a — Critical Path Detail

**Problem:** `partner_analytics_quarterly.json views.aua.donut.total` = $89.6M from holdings.market_value sum (scope bug from INF_B_00 nav_price=0 issue, fixed in DIAGFIX.002b). Should be $182.6M canonical.

**Fix:** Switch the AUA *value* source for `views.aua.*` from holdings to `silver/aum_snapshot`'s `managed_value` per-HH (already used by `build_dashboard` for the canonical headline). Lifecycle classification (NMNC / NMEC / Existing) still uses holdings + nna for *when* the HH started — that's a temporal classification unaffected by the scope mismatch.

**Decision noted in RAVC:** segment HH counts now drawn from intersection with aum_snapshot's 274-HH managed set (vs the 307-HH holdings set). COO approved: "274 HH count for donut segments is APPROVED. Managed-only is correct and consistent with $182.6M total."

**Distribution percentiles:** DIAGFIX.004 Fix C had previously moved this from hard-coded zeros to holdings groupby quantiles. .002a supersedes — now uses aum_snapshot.managed_value Series directly for quantiles. Per-HH median (p50) expected to be $300K-$700K range across 274 HHs.

---

## DIAGFIX.002b — Root Cause Detail

**Problem:** 40.2% of `gold/holdings/*.parquet` rows have `market_value=$0` due to nav_price=0. Affects 85.2% of accounts. Source: AE 0.6.1 DIAGFIX.001 RAVC (Option D).

**Mechanism:** INF_B_00 reconstructs position snapshots from TRN feed using "last seen wins" for nav_price. Many TRN rows are non-trade events (advisory fee, journal, income distribution) carrying nav_price=0. Last seen wins overwrote the last valid nav with 0 whenever the most recent transaction was a non-trade.

**Fix:** Guard the update at line 272-273: change `if nav is not None:` to `if nav is not None and nav > 0:`. Post-loop diagnostic logs still-zero count + percentage; expect <5% post-fix vs 40.2% baseline.

**Verification (post-EC2 re-run):** holdings.market_value.sum() expected to rise significantly from $89.6M baseline. May not reach $182.6M (TRN reconstruction coverage), but should close most of the gap. Escalation per TO: COO notified if post-fix sum < $130M.

---

## DIAGFIX.007 — Investigation + Build

**Investigation finding:** BD's `cumulative_chart.json` IS produced (4.4MB at `s3://opal-data-bd/platinum/firm/cumulative_chart.json`) by `D_04.build_cumulative_chart()`. BD's builder reads from BD's `gold/artifacts/timeseries_chart.json` (which has cohort-distribution schema: geo/adv/ofc views with categories+data per cohort over time).

**Inflection's `timeseries_chart.json` has a DIFFERENT schema:** built by INF_I_D00b, it's a windowed-AUA/NNA structure (3M/6M/1Y/2Y/3Y/MAX windows with daily series), NOT cohort-distribution. So porting BD's `build_cumulative_chart()` directly does not work.

**Solution:** New script `INF_I_D00c.cumulative_chart.py` (450 LOC) computes the cohort timeseries from source data directly:
- `client_performance × accounts_v2` (state, advisor_key) → `geo` + `adv` views
- `canonical_nna × accounts_v2` (state) → `nna_geo` + `nna_adv`
- Weekly downsample to ~104 points across 2Y window
- Top-N + Other binning (8 states, 9 advisors)
- Output schema matches `types.ts PlatinumCumulativeChartResponse`

**Verdict against TO criteria:** VERDICT A — data exists, script written, gate passes. Acceptance criterion #1 (artifact at S3) PENDING EC2 dispatch (`orion-gold-dispatch.sh --single INF_I_D00c` or include in re-run wave). nna_geo / nna_adv data points beyond 2021Q1 will be 0 until DIAGFIX.003 INF_C_01 backfill lands; this is documented in the RAVC.

**Not emitted in V1:**
- `ofc` / `nna_ofc` (Inflection has no office cohort)
- `geo_drill` / `adv_drill` / `nna_*_drill` (additive in follow-on; portal makes them optional)

---

## Pre-commit Gate

```
.tools/ds-commit-gate.sh INF_D_04.client_portal_summary.py        → All checks passed!
.tools/ds-commit-gate.sh INF_B_00.canonical_holdings.py           → All checks passed!
.tools/ds-commit-gate.sh INF_I_D00c.cumulative_chart.py           → All checks passed!
```

py_compile + AST undefined-name scan + ruff exit 0 for all three.

---

## Compiler Tools

| Phase | Tool | Result | Notes |
|-------|------|--------|-------|
| 1 — before write (.002a) | `comp-pipescript io INF_D_04` | SKIPPED — registry gap | Same as prior INF wave |
| 1 — before write (.002b) | `comp-pipescript io INF_B_00` | SKIPPED — registry gap | Confirmed pattern manually via grep |
| 1 — before write (.007) | `comp-pipescript io INF_I_D00b/D00c` | N/A | New script; no precedent in graph |
| 2 — before commit | `.tools/ds-commit-gate.sh <each .py>` | PASS | All 3 files exit 0 |
| 3 — after S3 upload | `comp-pipescript deployed <script>` | SKIPPED — registry gap | MD5 ETag MATCH used as substitute |

Pattern: registry coverage gap remains the standing limitation for INF/Orion scripts. Documented across INFGRD.006 + DIAGFIX.002+003+004+002a+002b+007. Recommend a comp-pipescript graph extension TO if not already in CTO/COO queue.

---

## Deploy Cycle

| TO | Commit SHA | S3 ETag (MD5) |
|----|-----------|---------------|
| .002a | `aa030d272` | `02834680f0c7809df3e86a3d449bf54f` |
| .002b | `127fe2a17` | `62b2aa49ba65479e1dfeb74b0006ba4b` |
| .007 | `6e68732d3` | `84a5bfc043c4561a04a15f3ce9a3502c` |

All pushed to CLOUD. All MD5 = ETag verified MATCH.

---

## Acceptance Criteria Status

### .002a
| # | Criterion | Status |
|---|-----------|--------|
| 1 | Code-side: aum_snapshot canonical in views.aua | DONE |
| 2 | Gate exit 0 + S3 MATCH | DONE |
| 3 | RAVC | DONE |
| post | After re-run: views.aua.donut.total = ~$182.6M; segments sum to ~$182.6M; distribution.p50 non-zero | PENDING EC2 |

### .002b
| # | Criterion | Status |
|---|-----------|--------|
| 1 | After re-run: market_value.sum() > $130M; <5% nav=0 | PENDING EC2 |
| 2 | Gate exit 0 + S3 MATCH | DONE |
| 3 | RAVC | DONE |

### .007
| # | Criterion | Status |
|---|-----------|--------|
| 1 | cumulative_chart.json non-empty at platinum/firm/ | PENDING EC2 dispatch (--single INF_I_D00c) |
| 2 | OR VERDICT C | N/A — data is available, build proceeded |
| 3 | Gate exit 0 + S3 MATCH for script | DONE |
| 4 | RAVC | DONE |

---

## Next Steps

- [AE 0.6.1] Re-run wave dispatch (per COO GO 20260429T211013Z): INF_C_01 backfill (full range) + INF_B_00 + standard chain → INF_I_D00 + INF_D_07 + INF_I_D00c
- [DS / NEXT] Standby for re-run completion verdict
- [DS / NEXT] DIAGFIX.008 (asset mix build) — start AFTER re-run wave per COO priority directive. Use ETFClassifier in regex-fallback ONLY (no bd-* DDB calls) per Andrew's directive.

---

*Authored by `0.4.0_DS_ClientPlatform`. Session arc: ~50 min for 3 follow-up TOs. 3 commits, 3 S3 uploads, 2 RAVCs (002a + 002b/007 combined).*
