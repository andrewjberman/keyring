# Session Log — STAUDT Engine Accuracy + BFIX1+BFIX2

**Agent:** 0.4.0_DS_ClientPlatform~A
**Date:** 2026-04-20
**Session arc:** ad-hoc BD investigation -> engine_accuracy briefing -> BFIX1+BFIX2 dispatch -> Phase 0 scope correction -> Phase 1 ship -> CTO 3-question diagnostic probe

## Current state — standing by

- Commit `081223b5` (BFIX1+BFIX2 on B_00.canonical_holdings.py) shipped to origin/CLOUD
- CTO + COO pre-flag MCPs sent and ACKed
- CTO 3-question diagnostic probes complete, all GREEN
- Awaiting DT upload trigger (gated on FIX wave PROD deploy clearance + AE qa-runner availability)
- Heartbeat live

## What landed today

### FIX wave closes (~A's lane)

| Fix | Commit | DT validation | RAVC4 close MCP |
|---|---|---|---|
| FIX3A (D_02 L62+L1624 NNA prefix swap) | `43c3693a` | b5ad3829 PASS structural | 20260420T160534Z + re-confirm 20260420T183935Z |
| FIX7 (D_00b L791 RA-P5 guard-clause) | `e0550693` | b5ad3829 PASS firm ADV-AUA $1.651B | 20260420T183928Z + re-confirm 20260420T190342Z |
| FIX3B | (CANCELLED) | n/a — parquet verification proved aua_current IS in canonical/nna/ | n/a |
| INV4 | (DEFERRED) | OFC-NNA asymmetry lives in caller above L450, not D_00b internal | n/a |

### Ad-hoc BD investigation (off Andrew's "go investigate phantom holdings + Schwab RPS coverage" prompt)

Five-pass investigation produced four diagnostics + a CTO/COO briefing:
1. `phantom_buyhold_partition_2026-04-20.{md,json,parquet}` — Schwab-side gap profile, buy-and-hold-pre-lookback hypothesis test (only 15 accts / $461K — hypothesis disconfirmed at scale)
2. `engine_accuracy_2026-04-20.md` — topline reconciliation BD silver $1.697B vs gold canonical $1.649B = -$48M / -284bps
3. `engine_accuracy_drilldown_2026-04-20.md` — Schwab undershoot ($19.5M = ~96% cash deficit), non-Schwab overshoot (+$16M), 44 dropped Schwab accts
4. `BRIEFING_aua_engine_accuracy_2026-04-20.md` — CTO/COO-facing exec briefing with bug stack, recommended fixes, 50bps-target reframe

Critical reframe surfaced: portal flow path (NNA + GRO) implies $1.7B firm AUA matching BD silver, while snapshot path shows $1.65B. The $46M gap is entirely in the snapshot pipeline (B_00.canonical_holdings.py), not in flow calculations. Andrew validated via independent identity check ($1.45B EOP 2025 + $245M YTD NNA+GRO = $1.696B implied vs portal $1.65B).

### BFIX1 + BFIX2 — engine refinement bundle

- Commit: `081223b5` on origin/CLOUD
- Author: 0.4.0_DS_ClientPlatform~A
- Scope: B_00.canonical_holdings.py +102/-6 (single-file silver-layer patch)
- Authority: COO 20260420T184810Z (Path A + Direction 2 confirmed); Andrew chat ("Agreed go ahead")

**BFIX1 — bd_stale predicate Direction 2:**
- New helper `build_persistent_rps_accts(schwab_cache, n_assets=3, n_days=7)` builds set of accts with ≥3 distinct cusips across last 7 RPS days
- `reconcile_date()` accepts new `schwab_persistent_accts` param; when provided, `is_schwab_covered` uses the persistent set
- Falls back to legacy single-day predicate if param not passed (test-safe)
- Wired in `main()` to populate `_shared_02b['schwab_persistent_accts']`
- Recovery target: ~$6.6M MV across 25 real_units_in_cube accts (PCRA / AQR / Fidelity 401k / Schwab Trust Bank class)

**BFIX2 — additive bd_only re-injection:**
- New code path in `_worker_02b()` and `process_date()` immediately after `reconcile_date()`
- Detects accts in `bd_df` but absent from `holdings`, re-injects with `source='bd_only'`, `schwab_units=NaN`, `ticker=''`
- Belt-and-suspenders against the silent drop mechanism for newly-opened accts (Craig Smith Rollover IRA, Lyndon Cook Retirement Plan, Chad Marek PCRA, etc. — all opened in last week)
- Recovery target: ~$14.2M MV across 54 truly-non-mapped real_units accts

**Combined recovery: ~$20.8M of $48M gap. Closes -284bps -> ~-160bps. Does NOT hit 50bps target — remaining $32M lives upstream in A_03.positions_cube.py (BFIX4 follow-up).**

### Phase 0 mechanism note (the scope correction)

Per-account decomposition against positions_cube caught the original briefing's $38.6M attribution error:

| Pattern | Accts | $ MV | BFIX1 fix? |
|---|---:|---:|---|
| absent_from_cube | 69 | $23.7M | NO — upstream A_03 |
| fp_dust_in_cube | 17 | $8.3M | NO — upstream FIFO |
| real_units_in_cube | 25 | $6.6M | YES |

Same correction applied to BFIX2: 54 of 62 accts addressable, 8 absent from cube ($4.2M, mostly non-financial like Silverthorne Home / Austin Home).

### CTO 3-question diagnostic probes (interim window during Andrew's Group D run)

Per CTO 20260420T192447Z. All GREEN.

- **Q1 BFIX2 re-inject filter:** 92 accts re-inject (not 54), but composition is benign — 58 BFIX2-intended + 28 BFIX1-overlap (dissolves post-deploy) + 6 fp-dust (priced ~$0). No Bug 2 cash absorption. Evidence: `bfix2_reinject_filter_probe.md`.
- **Q2 bd_only downstream NaN handling:** Direct B_00 consumers (B_02/B_03/C_02) don't read ticker/schwab_units. No crash. Evidence: `bd_only_downstream_probe.md`.
- **Q3 BFIX1 outage boundary:** Persistent set 5,450 accts (134 fewer than single-day, correctly excludes bd_stale-overreach). Robust under 1-5 day dark, cliff at 7-day full dark — but current code has the SAME failure mode (L423-431 short-circuit). Real loss under 7d full outage: $200. No circuit-breaker needed. Evidence: `bfix1_outage_boundary_probe.md`.

CTO + COO MCPed with all three findings 20260420T193749Z + 20260420T193807Z.

## Files committed (this session)

Single commit `081223b5`:
- `data/black_diamond/scripts/gold/B_00.canonical_holdings.py` (+102/-6)
- `data/black_diamond/diagnostics/STAUDT/BFIX1/bfix1_phase0_mechanism_note.md`
- `data/black_diamond/diagnostics/STAUDT/BFIX1/bfix1_bfix2_phase1_evidence.md`
- `data/black_diamond/diagnostics/STAUDT/BRIEFING_aua_engine_accuracy_2026-04-20.md`
- `data/black_diamond/diagnostics/STAUDT/engine_accuracy_2026-04-20.md`
- `data/black_diamond/diagnostics/STAUDT/engine_accuracy_drilldown_2026-04-20.md`

Files written but not yet committed (CTO Q1+Q2+Q3 probes):
- `data/black_diamond/diagnostics/STAUDT/BFIX1/bfix2_reinject_filter_probe.md`
- `data/black_diamond/diagnostics/STAUDT/BFIX1/bd_only_downstream_probe.md`
- `data/black_diamond/diagnostics/STAUDT/BFIX1/bfix1_outage_boundary_probe.md`

Ad-hoc analysis files written to `data/black_diamond/diagnostics/STAUDT/` and the diagnostic script at `data/black_diamond/scripts/diagnostics/diag_phantom_buyhold_partition.py` (not committed yet — investigation script, not production).

## MCPs fired (key ones)

- 20260420T160534Z RAVC4 close FIX3A (initial)
- 20260420T183928Z RAVC4 close FIX7
- 20260420T183935Z RAVC4 re-close FIX3A (per COO nudge)
- 20260420T184006Z ACK BFIX1+BFIX2+BFIX3 dispatch
- 20260420T184536Z BFIX1+BFIX2 Phase 0 mechanism note + scope correction (path A vs B + Direction confirmation request)
- 20260420T190302Z Pre-flag COO on commit `081223b5`
- 20260420T190313Z Pre-flag CTO on commit `081223b5`
- 20260420T190342Z RAVC4 close FIX7 re-confirm (per COO push, original was missed)
- 20260420T193749Z CTO Q1+Q2+Q3 diagnostic probe results — all GREEN
- 20260420T193807Z COO FYI on Q1+Q2+Q3 results

## Open items / waiting on

1. **DT upload trigger for `081223b5`** — gated on FIX wave PROD deploy clearance (FIX1/FIX2/FIX6/FIX7) + AE qa-runner watchdog RCA resolution + AE-confirmed qa-runner availability. DT will MCP me when scheduling fires.

2. **qa-runner cycle** — likely full `--group ABCD` since B is silver-layer (downstream B_02/B_03/C_02 cascades through D-layer). DT/AE coordinate dispatch.

3. **Post-qa-runner RAVC4 close for BFIX1+BFIX2** — will include:
   - Per-account MV diff for re-inject cohort (target: 58 truly-non-mapped + 28 BFIX1-recovered = ~86 accts gain canonical positions)
   - Pricing rate ≥80% on re-inject cohort (Q2 spot-check ask)
   - Firm AUA gap close from -284bps to ~-160bps
   - comp-validate B_00 + canonical_holdings exit 0
   - BFIX4 TO proposal sketch (A_03 positions_cube — 69 absent + 17 fp_dust = $32M)
   - Coordination note for ~C: KPI sentinel enablement gate moves out by one TO (now after BFIX4, not BFIX1+2)

4. **BFIX3 (Schwab cash deficit investigation)** — queued P2 sequential after BFIX1+BFIX2 RAVC4 closes. Read-only investigation of why $18.8M Schwab-side cash drops out for 4,950 accts (Craig Smith / DONALD WAYNE CRABBE / Steve Jr & Mary Humphrey / etc.).

5. **BFIX4 TO proposal** (RAVC4 follow-up) — author scope sketch for A_03.positions_cube.py investigation. Target: 69 absent_from_cube ($23.7M) + 17 fp_dust_in_cube ($8.3M) + 8 BFIX2-side absent ($4.2M, mostly non-financial). Lane: likely ~A continuation given mental context.

## Notes for next session pickup

- The "Schwab-covered" predicate in B_00 L453 is **TODAY's RPS presence**, not mapping presence (briefing was wrong about this; corrected in Phase 0 mechanism note).
- The 62 BFIX2 dropped accounts are mostly newly-opened (≤7 days). The exact filter dropping them was NOT fully traced in Phase 0 — BFIX2's explicit re-inject is belt-and-suspenders. CTO flagged this for follow-up B_00 mini-PRD (post-STAUDT) to get a complete mechanism trace.
- `aua_residual` field in canonical_nna silently absorbs ~$50M YTD of snapshot drift. Andrew's identity check made this visible. After BFIX1+BFIX2+BFIX4 land, residual should shrink toward zero.
- Per-account decomposition against positions_cube is the gold-standard pattern for engine-accuracy attribution. Per CTO 20260420T184810Z: "bake into BFIX4 + future engine TOs."
- The ~$1B-and-up advisor leaderboard distribution post-FIX7 is sane (Travis $401M, Kyle $248M, Greg $107M, ...). Worth noting if asked about FIX7 effect.

## Status flags

- Inbox-watch.sh: running (relaunched after each spurious exit per Andrew mandate)
- Heartbeat: live (last 20260420T193807Z range)
- No active blockers on my side. Pure wait state.
