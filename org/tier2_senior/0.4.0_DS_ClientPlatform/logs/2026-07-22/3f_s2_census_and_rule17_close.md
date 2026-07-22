# 0.4.0_DS_ClientPlatform — 3F-S2 silver census + Rule-17 audit — COMPLETE

**archetype:** VALIDATE
**secondary_archetypes:** TRACE, SCRIBE

**Window:** 2026-07-22 ~20:26Z (session start, MDPF_3FIRMS dispatch) → ~21:0xZ.
**TO:** `MDPF_3FIRMS.3F-S2` (GO 203250Z, sequence S2→S4→G8). **Deliverable:**
`deliverables/MDPF_3FIRMS_3F-S2_SILVER_CENSUS_20260722.md`.

## Summary

Full bronze-vs-silver completeness census on the six MDPF-feeding fact tables, denominators
enumerated at run time, per-table positive controls (6/6 PASS, separate `s3api` invocations) + a
planted-absence mutant control (PASS). **Verdict: 0 unexplained missing partitions on any table;
zero reprocesses fired.** Rule-17 audit across all four converter families: **violation list
EMPTY**; one strictness divergence itemized (SmartX `to_numeric(errors="coerce")` vs mirror-family
raise-on-drift) → 3F-S4 disposition. Nothing on the fillna/dropna escalation trigger.

Key numbers (vintage 20:26–20:55Z, repo @ `61365878d`): RPS 539/539 trading days (92-date head-gap
below the 2024-11-01 display floor = depth statement per Andrew @`0b06b5a14`; +1 vendor-delivered
mourning-day partition 2025-01-09) · SmartX 9/9 (initial silver-without-bronze flag was my
wrong-axis comparison vs `models_summary`; closed, independently converged with 0.5.0's 99-object
census) · Orion 2272/2272 bronze==silver, 5 calendar absences = the known 07-11..07-15 gap
(3F-B3 propagation tomorrow) · Eclipse 54/54 bronze==silver, **6 trading-day vendor-side absences
incl. NEW 2026-05-21** (not on the banked unfillable list; flagged to 0.6.2~A for 3F-B4) ·
BD-holdings 28/28 trading days (5 early weekend/Juneteenth extras) · rebalancer 2/2.

## Post-census finding (3F-S3/S4 joint thread, empirical)

**`blackdiamond/.../fact_holdings_s2` is the xlsx section-2 vendor Timestamps sheet (5 rows × 7
cols: Created / Template Name / Start Date / End Date / Date Range), NOT holdings.** The real
table is `fact_holdings` (16,762 × 24 @ 07-20, the verified $458M/913-account universe). PRD §1.2
naming `_s2` as the Cottonwood total_aua source is a PRD text defect — contrast Schwab, where
`fact_rps_s2` (7,086 × 39 @ 07-21) is the REAL account-balances section. `_s{N}` is mechanical
per-section; what section 2 IS differs per vendor. Landing the footer is CORRECT Rule-17 behavior
(never drop a sheet); naming it a source is not. Determination + evidence sent to 0.7.0 (joint
record); PRD amendment is CTO's.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `comp-freshness artifact` ×6 | each MDPF fact table | PASS ×6, **gap recorded** | all six on "No cadence config entry" flat-hours fallback — no `trading-day-frontier` basis on any MDPF leg; the Monday-false-alarm class. Routed to COO. No staleness raised off it (NEVER#1). |
| `comp-pipescript io` | schwab_conversion / mirror_conversion / rebalancer_conversion | **INSTRUMENT GAP** | registry resolves gold scripts only; silver converters unregistered → fell back to source reads per the mandate's own if_mismatch. Registry gap noted. |
| `comp-glob` | `*silver*` under data/assets/scripts | PASS | located the converter family |
| `comp-to` | 3F-S2 | PASS | race-free session TO context |
| trading-calendar resolve (lib/trading_calendar.py) | 6 legs | PASS + mutant control PASS | calendar source NYSE/hardcoded-fallback-2024-2027; planted 07-01 deletion detected |
| positive controls | `s3api list-objects-v2` ×6, separate invocations | 6/6 CONTROL-PASS | independent instrument confirms known-present partitions in census sets |

## MCP traffic

GO + scope-update from COO (203250Z, 204333Z) · ACKs to COO (202809Z, 203425Z) · convergence
exchange with 0.5.0 (3F-B2 SmartX axis) · 3F-S3 joint thread opened by 0.7.0 (204804Z) — reply
pending this commit.

## Next

3F-S4 (cross-firm schema parity — the coerce-vs-raise divergence + the `_s{N}` semantics land
there) → 3F-G8 on its narrowed gate. Exercised runner-role read (3F-S3 AC-4 behavioral leg) via
the Rule-12 S3→EC2 diagnostic path.
