# 49F KILL-CLEAR ACCOUNTING -- the four-state grammar, grounded on verdict files (CVO canonical)

**3.0.0_SA_CVO 2026-08-11 ~1858Z · VALIDATE.** COO 185441Z ask: the true kill-clear count in the
four-state grammar with the denominator. **This file is the canonical count -- read IT, not a message
summary** (the 4-of-16 drift happened because "cleared" in my prose meant TECHNICAL-PARITY-CLEARED and
was read as BAR-DISCHARGED; the states below are each grounded on a committed verdict file).

## THE GRAMMAR (COO's, adopted)
- **BAR-CLEARED** = discharges Andrew's bar AS WRITTEN ("platinum outputs overlaid... field/quality
  parity, as validated by CVO") -- FULL field + quality + value overlay, no pending residual.
- **SCOPE-VALIDATED** = a REAL scope cleared (technical parity / computable core), with a NAMED residual
  (backfill window mass, or a cutover re-pin). Genuine quality; NOT a full discharge.
- **IN FLIGHT (WINDOW-GATED)** = not even the core clears yet; gated on the window backfill / emission.
- **NOT STARTED** = no CVO instance has reached me.

## THE COUNT: BAR-CLEARED = 0 of 16. (SCOPE-VALIDATED = 6; IN FLIGHT = 1; NOT STARTED at cert = 9.)
Denominator **16** = the 49F served-family roster (the header_metrics archetype "reused by the other 15
families"; exact roster is base DS's sweep scope).

| # | Surface | State | Grounding (verdict file) |
|---|---|---|---|
| 1 | header_metrics | **SCOPE-VALIDATED** (closest to BAR-CLEAR) | VALIDATED_49F_HEADER_METRICS: technical parity CLEAR; **gate 1 ($122.5M) DISCHARGED @745ca6d78f**; gate 2 = V2 window backfill running (fill-2). ONE landed compute from BAR-CLEARED. |
| 2 | fee_efficiency | **SCOPE-VALIDATED** | VALIDATED_49F_DASHBOARD_FEE_EFFICIENCY: computable CORE clears; window mass pending backfill |
| 3 | clients_tab | **SCOPE-VALIDATED** | VALIDATED_49F_FEE_EFFICIENCY_AMENDED_CLIENTS_TAB: technical parity clears; V8 residual named follow-on |
| 4 | client_detail | **SCOPE-VALIDATED** | VALIDATED_49F_CLIENT_DETAIL: value CHARACTERIZED vs sovereign band; V16/17/18 backfill + harness fan-out + cutover re-pin pending |
| 5 | mix_summary | **SCOPE-VALIDATED** | VALIDATED_49F_MIX_SUMMARY: P1-SCRIPTS; value rides the cot-bundle mix-basis band (dormant pre-cutover) |
| 6 | firm_leaderboard | **SCOPE-VALIDATED** | VALIDATED_49F_FIRM_LEADERBOARD: P1-SCRIPTS; window mass + serving port + V19 pinned divergence pending cutover |
| 7 | firm_dashboard | **IN FLIGHT (WINDOW-GATED)** | VALIDATED_49F_DASHBOARD_FEE_EFFICIENCY: "IN FLIGHT (WINDOW-GATED) is the CORRECT classification" -- NOT cleared (COO: stop carrying it as cleared) |
| 8 | firm_ownership_map (Unit-2) | **NOT STARTED** (at cert) | no CVO instance; ~A building |
| 9-16 | remaining families | **NOT STARTED** (at cert) | no CVO instance reached me; production-bound (fill-2 + emission) |

## WHAT ANDREW SHOULD HEAR (do not soften -- per COO)
- **Zero surfaces discharge the bar as written. Not one.** The "4 of 16 cleared" was a
  message-summary artifact; every verdict file states its scope precisely.
- **The work is real, not vapor:** six surfaces carry genuine technical/core parity with named,
  understood residuals, and three instrument defects were caught THIS sweep BY controls firing (the
  shadowed pin, the 0.5pp swallowed mutant, the cash class) -- the bar is discriminating, not decorative.
- **The path to the first BAR-CLEAR is short and human-free:** header_metrics needs only fill-2 to land;
  gate 1 is already Andrew-ruled. When fill-2 lands I re-grade the window monetary discrimination and,
  clean, header_metrics is the FIRST BAR-CLEARED surface.
- **The constraint is production, not validation:** my cert queue is drained; the remaining 9 are
  awaiting emission, not awaiting me.

## RE-GRADE DELTAS vs COO's prior report (the corrections)
- header_metrics gate 1: PENDING -> **DISCHARGED** (@745ca6d78f, ~1742Z).
- firm_dashboard: was carried CLEARED -> **IN FLIGHT (WINDOW-GATED)**, never cleared. Corrected.
- BAR-CLEARED total: reported 4 -> **0**. SCOPE-VALIDATED (real quality) = 6.

-- 3.0.0_SA_CVO
