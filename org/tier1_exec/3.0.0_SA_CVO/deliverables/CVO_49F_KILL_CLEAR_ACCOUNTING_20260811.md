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

## ⚖ DENOMINATOR CONVENTION (PINNED ~1956Z, COO 195302Z ask -- the frame must not shift by row)
**THE UNIT IS A SERVED PLATINUM KEY, never a family.** One emitter serving N served keys counts as N
units, because Andrew's bar validates each SERVED SURFACE ("platinum outputs overlaid with existing
platinum jsons") -- a served JSON is bar-cleared or it is not, per key. Consequence, reconciled to base's
by-KEY census (195302Z): the timeseries twins (firm_timeseries_chart / gold_timeseries_chart) are TWO
keys, clients_tab and clients_tab_slim are TWO keys, the partner-analytics trio is THREE keys (one
derivation, three served period frames). **THE TOTAL MOVES 16 -> 17** (the +1 is the timeseries twin,
previously counted as one -- the inconsistency COO caught; base's key census is the denominator source of
truth). I would rather 2 of 17 with a stable frame than 2 of 16 with a convention that shifts by row.

## THE COUNT: BAR-CLEARED = 3 of 17. (SCOPE-VALIDATED = 6; IN FLIGHT = 0; NOT STARTED at cert = 8.)
*(~2020Z: **fee_efficiency IN FLIGHT -> BAR-CLEARED (the THIRD)** -- base fixed both blockers with measurements: the AGGREGATE window control (d03 --verify-windows, the emitter home I accepted on client_detail) which I adversarially verified on MY OWN cell (qtd.advisors[20] +$6M -> PIN-VIOLATION qtd, a different cell than base tested; my first attempt was a VACUOUS mutant that never landed -- the echo-back caught it, Rule 22b); the 66 advisor-grain zero cells classified NO-ROWS via an independent C_00 ledger walk; the Unassigned double-count discharged (144-advisor refined universe). IN FLIGHT is now 0.)*

## ⚖ ZERO-CELL CONVENTION (PINNED ~2020Z, COO 201259Z + base proposal)
**"LEGITIMATELY ZERO" := NO-ROWS against the flow ledger** (the cell's underlying accounts have zero
external flow rows in that window, measured against the C_00 526-partition ledger -- an independent leg
BELOW the C_01 series the emitter reads, not self-comparison). Graders TARGET POPULATED cells; the
vacuity check (a mutant on a zero cell is vacuous) is the enforcement. **NONZERO-UNDERLYING is the real
finding class** (a cell reading zero while its ledger rows are nonzero) -- zero instances measured today;
the walk that finds one is written. Extends the SS 4.1 precondition-state rule: a zero-with-a-measured-
NO-ROWS-reason is a genuine absence; a zero-as-a-shrug is not, and only the ledger walk distinguishes them.
*(~2005Z: timeseries_overview @45672c14ec -> SCOPE-VALIDATED -- a no-pin family (index-misalignment makes leaf pins noise; discrimination via derivation-crossing build-time controls, cross-tie 38/38); cross-family tie 13,063,592.19 == d07 qtd verified against my own value.)*
*(⚠ LABEL CORRECTION ~1936Z: the dashboard/fee_efficiency states were SWAPPED in prior versions -- I propagated COO's mis-attribution without checking my OWN verdict file, which says (line 50) "dashboard is the second surface to CLEAR technical parity" and (line 43) the IN-FLIGHT verdict is FEE_EFFICIENCY's (its Unassigned double-count). Truth: **dashboard** was technical-clear -> now BAR-CLEARED; **fee_efficiency** was and remains IN FLIGHT. The count (7 SV / 1 IF pre-grade) was numerically right; the label of which surface was IN FLIGHT was wrong. Map-vs-territory, caught by reading the file.)*
*(Updated ~1936Z: **dashboard is BAR-CLEARED -- the SECOND** (same window-NNA calibration as header_metrics, reused by construction: windows non-zero + identical values, positive limb PASS, MY validator-planted mutant FAIL rc=1, pins transitively grounded via the shared served-NNA source). ⚠ **fee_efficiency FINDING (stays SCOPE-VALIDATED, NOT bar-cleared): its PER-ADVISOR window plane does NOT discriminate** -- my mutant on a LIVE nonzero cell (windows.max.advisors[0].nna, +$6M on 60.38M) was ABSORBED rc=0; base's mutant hit only the pinned FIRM-level windows. A blanket exemption over live per-advisor fields (SS 5a). Flagged to base: pin the per-advisor windows or determine band-absorption-vs-not-compared before bar-clear. Prior ~1922Z: header_metrics FIRST bar-clear.)*
Denominator **16** = the 49F served-family roster (the header_metrics archetype "reused by the other 15
families"; exact roster is base DS's sweep scope).

| # | Surface | State | Grounding (verdict file) |
|---|---|---|---|
| 1 | header_metrics | **⭐ BAR-CLEARED (FIRST)** | VALIDATED_49F_HEADER_METRICS ~1922Z: all planes clear incl. live windows; both gates discharged (gate 1 @745ca6d78f; gate 2 fill-2 + window discrimination DEMONSTRATED by a validator-planted mutant rc=1); pins independently grounded vs served bytes. Residual: re-pin-daily (by-design, stale-pin-fails-loud). |
| 2 | fee_efficiency | **⭐ BAR-CLEARED (THIRD)** | ~2020Z: base's AGGREGATE window control (d03 --verify-windows @9a157f02e5) adversarially verified on MY cell -- qtd.advisors[20] +$6M -> PIN-VIOLATION qtd (any single-advisor sum-mover fails; cancelling residual = deferred fan-out, the client_detail pattern). 66 zero cells all NO-ROWS (C_00 ledger walk). Unassigned double-count discharged. Core + windows clear; gate 1 rides ~1742Z. |
| 3 | clients_tab | **SCOPE-VALIDATED** | VALIDATED_49F_FEE_EFFICIENCY_AMENDED_CLIENTS_TAB: technical parity clears; V8 residual named follow-on |
| 4 | client_detail | **SCOPE-VALIDATED** | VALIDATED_49F_CLIENT_DETAIL: value CHARACTERIZED vs sovereign band; V16/17/18 backfill + harness fan-out + cutover re-pin pending |
| 5 | mix_summary | **SCOPE-VALIDATED** | VALIDATED_49F_MIX_SUMMARY: P1-SCRIPTS; value rides the cot-bundle mix-basis band (dormant pre-cutover) |
| 6 | firm_leaderboard | **SCOPE-VALIDATED** | VALIDATED_49F_FIRM_LEADERBOARD: P1-SCRIPTS; window mass + serving port + V19 pinned divergence pending cutover |
| 7 | firm_dashboard | **⭐ BAR-CLEARED (SECOND)** | ~1936Z: live windows verified, positive limb PASS, MY validator-planted mutant FAIL rc=1; same window-NNA calibration + served-NNA source as header_metrics (pins transitively grounded). Gate 1 (total.aua) rides ~1742Z. Was IN FLIGHT; now cleared. |
| 8 | firm_ownership_map (Unit-2) | **SCOPE-VALIDATED** | VALIDATED_49F_FIRM_OWNERSHIP_MAP @fe9ffd6f30: no monetary plane (mutant transposed to id-plane tamper guard, discriminating); cross-derivation id-set parity deferred to cutover re-pin |
| 9-16 | remaining families (8) | **NOT STARTED** (at cert) | no CVO instance reached me; production-bound (window-derivation build + emission) |

## WHAT ANDREW SHOULD HEAR (do not soften -- per COO)
- **The FIRST bar-clear has landed: header_metrics, 1 of 16.** The count was 0 at ~1858Z and is 1 at
  ~1922Z -- earned by base building the window derivation post-fill-2 and my adversarial grade (validator-
  planted window mutant FAILs; pins independently grounded against the served bytes to exact magnitude).
  The remaining 6 SCOPE-VALIDATED carry genuine technical/core parity with named residuals; 1 IN FLIGHT
  (dashboard); 8 awaiting emission.
- **The work is real, not vapor:** and the bar is discriminating -- FOUR instrument defects were caught
  THIS sweep BY controls firing (the shadowed pin, the 0.5pp swallowed mutant, the cash class, and base's
  own 0.5pp-vs-0.02pp window-tolerance self-catch). The first bar-clear passed BECAUSE a validator-planted
  mutant could fail and a pin was independently grounded, not because it looked clean.
- **The path for the rest is the same shape:** each window family needs base's shared window-derivation
  (runner_common.window_nna_sums, one derivation home) + a grade; the calibration header_metrics just
  established (pinned V5-NNA-REBASE divergence + validator mutant) carries to them.
- **The constraint is production, not validation:** my cert queue is drained; the remaining 8 are
  awaiting emission, not awaiting me.

## RE-GRADE DELTAS vs COO's prior report (the corrections)
- header_metrics gate 1: PENDING -> **DISCHARGED** (@745ca6d78f, ~1742Z).
- firm_dashboard: was carried CLEARED -> **IN FLIGHT (WINDOW-GATED)**, never cleared. Corrected.
- BAR-CLEARED total: reported 4 -> **0**. SCOPE-VALIDATED (real quality) = 6.

-- 3.0.0_SA_CVO
