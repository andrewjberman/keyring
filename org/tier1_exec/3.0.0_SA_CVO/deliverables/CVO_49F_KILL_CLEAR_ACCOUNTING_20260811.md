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

## THE COUNT: BAR-CLEARED = 8 of 17. (SCOPE-VALIDATED = 9; IN FLIGHT = 0; NOT-YET-GRADED = 0.) ⭐ ALL 17 KEYS GRADED.
*(~2145Z: **advisor_nna_canonical @58a8411dad -> SCOPE-VALIDATED (the 17th and last key graded)** -- gzip instrument-support gate CLEARED (positive limb read a real 4,277,840-field diff off the gzip legacy side, not a silent empty). Firm plane discriminates: my mutant firm.QTD.nna +$50M -> FAIL. BUT a FINDING on the per-advisor plane (base flagged it, I confirmed + grounded the mechanism): my mutant on ONE advisor's QTD.nna +$50M (Abby Horton, real value -$128,100) -> ABSORBED PASS. And UNLIKE fee_efficiency, a firm-total pin CANNOT catch it -- the attribution is NONADDITIVE (I verified: firm QTD nna 7.43M != sum of 146 advisors 24.64M, delta $17.2M from multi-advisor double-count), so there is NO additive-identity backstop. The per-advisor NNA is product content advisors SEE. NOT bar-clear until base's offered top-N per-advisor window pins land -- accepted. clause(a) grounded complete; clause(b) 8 bar-cleared + 9 scope-validated, this the last.)*
*(~2140Z: **partner_analytics TRIO -> 3x BAR-CLEARED** (quarterly/monthly/annual) -- ~B sent the QA root; I graded ALL THREE adversarially: each positive limb PASS rc=0 + MY OWN mutant (views.aua.current.metrics.aua +$5M, echo-back landed 1789058516.82->1794058516.82) -> FAIL rc=1 through the V32 pin (which I verified == V19). Ran from --report-dir scratch per base's banked fit-clobber hazard. cla finding (NMNC/NMEC cohorts) disclosed+dispositioned. 16 of 17 keys BAR/SCOPE-graded; only advisor_nna_canonical (d14) ungraded, gated on its gzip baseline read.)*
*(~2135Z: **partner_analytics TRIO @e7de551719 -> 3x SCOPE-VALIDATED** (quarterly/monthly/annual, one emitter d13) -- structural VALID, 6 rows PASS incl. a DERIVATION-CROSSING cross-tie (account data-sums == C_01 manifest-sums, 12/12 cent-exact); V32 corroboration +10,519,155.99 == V19 VERIFIED against my held firm_leaderboard value; cla FINDING disclosed (the family serves NMNC/NMEC cohorts, NOT A_07 classification -- the alias-set layer-finding's sibling, measured-before-build + disposition approved); determinism stable x2 (caught real nondeterminism). BAR-CLEAR pends ~B/base's QA root for MY OWN adversarial pin-mutant -- validated on structure + cross-checks I could do, not on ~B's reported PIN-MUTANT. Only advisor_nna_canonical (d14) now ungraded.)*
*(~2115Z: **cumulative_chart @9853de4b84 -> SCOPE-VALIDATED** -- no-pin family (fit certifies SHAPE only), BUT I adversarially exercised its additive SUM IDENTITY DIRECTLY on the payload (not the build-time flags): adv-decomposition == geo-decomposition 109/109 to the cent (the additive dividend the nonadditive families cannot have), and my mutant (Travis Penfield +$6M on 2025-06-27) BREAKS it by exactly $6M. fit shape PASS (172,990 fields, FAIL 0); cross-tie #3 285,114,023.14 present (the cum-NET series, distinct from the 1,789,058,516.82 total AUA I hold). Leaf value-parity deferred to cutover (index-misalignment). 13 of 17 keys graded.)*
*(~2110Z: **timeseries_chart TWINS @4faf0dd4e2 -> 2x SCOPE-VALIDATED** (firm_timeseries_chart + gold_timeseries_chart) -- I independently hashed both payloads: BYTE-IDENTICAL (platinum==gold==3715c6d64dca), so the truncation rule is vacuous at 761<1,091 days and grading one grades both. No-pin family (V27 daily index-misalignment, fit certifies SHAPE only, the timeseries_overview precedent); discrimination via derivation-crossing cross-ties 525/525 REFUSES + 761/761 additive identities. Cross-tie #4 285,114,023.14 verified against my d07-held value. Census-path finding disclosed (the d00 sampler cap hid the 2 largest artifacts through 5 vintages; frozen from live bytes @76d225de9b).)*
*(~2040Z: **clients_tab_slim -> BAR-CLEARED (the FIFTH)** -- headline is the dashboard subset BY CONSTRUCTION (values identical to the dashboard I bar-cleared), counts V24-pinned at my grounded 852/1,241, total_aua D5-pinned; my mutant total_aua +$1M -> FAIL rc=1 (echo-back landed); no window domain (zero-cell convention vacuously satisfied). ⚠ INSTRUMENT NOTE: my FIRST grade attempt reported a false rc=1 READ-FAILURE from a cygwin-path artifact in an inline python -c -- I almost logged "baseline not readable" (the nna_canonical class), but ls showed the file present and a clean re-grade PASSED. A read-failure must be PROVEN real before it is reported as absence -- it bit me on a path artifact, exactly the blind spot I flagged for the gzip baseline.)*
*(~2025Z: **firm_leaderboard -> BAR-CLEARED (the FOURTH)** -- adversarial mutant on windows.QTD.summary.total_nna +$6M (echo-back confirmed landed 13.06M->19.06M) -> FAIL rc=1; positive limb PASS; PLUS ~A's cross-derivation control (account-grain data-sums vs manifest-grain sums, REFUSES on a cent -- the d08 gap-class solved) guards the per-account plane STRONGER than a pin. Cross-family ties (QTD 13.06M, MAX 285.11M) match my held values. V19 +$10.5M summary.total_aua is a pre-declared band.)*
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
Denominator **17** (PINNED above, served-KEY). ⚡ **CLAUSE (a) -- ALL CODE PROVEN TO COMPILE: COMPLETE,
GROUNDED ~2130Z.** All 14 emitters d01-d14 + the a07 dim EXIST in data/assets/scripts/gold/runners_49f/
and `python -m py_compile d*.py a07*.py` returns rc=0 -- every one of the 17 served keys has a built,
compiling emitter (d01-d11 = 11 singleton keys; d12 = the 2 twins; d13 = the 3-key partner trio; d14 =
nna_canonical). This is source-grounded, NOT the arithmetic coincidence -- I ran the compile sweep.
**FULL 17-KEY ROSTER (rebuilt ~2130Z -- the prior 8-row + "remaining (8)" table was stale and
self-contradicted the count line; COO 212649Z caught it):**

| # | Key | Emitter | State | Grounding |
|---|---|---|---|---|
| 1 | header_metrics | d01 | **⭐ BAR-CLEARED** | validator-planted window mutant FAIL; pins grounded vs served bytes |
| 2 | dashboard | d02 | **⭐ BAR-CLEARED** | same window-NNA calibration; my mutant FAIL |
| 3 | fee_efficiency | d03 | **⭐ BAR-CLEARED** | aggregate window control (d03 --verify-windows) verified on MY cell -> PIN-VIOLATION; zero cells NO-ROWS; Unassigned discharged |
| 4 | firm_leaderboard | d07 | **⭐ BAR-CLEARED** | my mutant QTD.summary.total_nna FAIL; ~A cross-derivation control (account vs manifest) |
| 5 | clients_tab_slim | d11 | **⭐ BAR-CLEARED** | dashboard subset by construction; my total_aua mutant FAIL through D5 |
| 6 | clients_tab | d04 | SCOPE-VALIDATED | technical parity clears; V8 residual named |
| 7 | client_detail | d05 | SCOPE-VALIDATED | value characterized vs sovereign band; harness fan-out + cutover pending |
| 8 | mix_summary | d06 | SCOPE-VALIDATED | value rides the cot-bundle mix-basis band (dormant pre-cutover) |
| 9 | ownership_map | d08 | SCOPE-VALIDATED | no monetary plane; id-plane tamper guard discriminates; cross-derivation deferred to cutover |
| 10 | timeseries_overview | d09 | SCOPE-VALIDATED | no-pin (index-misalignment); derivation-crossing cross-tie 38/38; cross-tie verified vs my value |
| 11 | cumulative_chart | d10 | SCOPE-VALIDATED | additive identity 109/109 to the cent + my mutant breaks it; no-pin, cutover-deferred leaf parity |
| 12 | firm_timeseries_chart | d12 | SCOPE-VALIDATED | twin, byte-identical (I hashed both); no-pin; derivation-crossing cross-ties 525/525 |
| 13 | gold_timeseries_chart | d12 | SCOPE-VALIDATED | twin of #12, same bytes -- graded together by measured identity |
| 14 | partner_analytics quarterly | d13 | **⭐ BAR-CLEARED** | positive PASS + MY mutant (aua +$5M) FAIL rc=1 through the V32 pin (==V19 verified); cross-tie 12/12 cent-exact |
| 15 | partner_analytics monthly | d13 | **⭐ BAR-CLEARED** | positive PASS + MY mutant FAIL rc=1; monthly m3=Sunday calendar-grammar catch disclosed |
| 16 | partner_analytics annual | d13 | **⭐ BAR-CLEARED** | positive PASS + MY mutant FAIL rc=1; annual V33 zero-skeleton y3 by declaration |
| 17 | advisor_nna_canonical | d14 | SCOPE-VALIDATED (tooth built, too SHALLOW) | gzip gate CLEARED; firm pin fires; base built 90 top-10 per-advisor pins @7e154395e8 -- my Travis-Penfield YTD +$40M -> FAIL (pins work). BUT top-10 covers only 53.3% of the book; #11 Patrick Mundlin ($15.1M) is material and ABSORBS. RECOMMEND a MATERIALITY FLOOR not top-N: pin |MAX nna| >= $1M = 76 advisors / 96.4% (the <$1M tail is a genuine immaterial residual). Bar-clear on the widened floor. |

**Reconciliation:** 8 BAR-CLEARED + 9 SCOPE-VALIDATED + 0 NOT-YET-GRADED = 17. ⭐ ALL 17 KEYS GRADED. The 4 remaining are no
longer "NOT STARTED / no emitter" -- their emitters BUILT and COMPILE (clause a done); what remains is
instance delivery + my adversarial grade. "NOT STARTED at cert" in the count line means not-yet-CVO-graded,
NOT no-emitter -- the count line and this table now agree.

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
