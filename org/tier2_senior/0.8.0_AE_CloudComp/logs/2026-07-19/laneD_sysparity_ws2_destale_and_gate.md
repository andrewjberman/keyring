# 0.8.0_AE_CloudComp~D -- NFRA_SYSPARITY WS-2: de-stale (LANDED) + fail-closed gate (engine LANDED, wiring at CTO)
**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE

Window: COO GO @211244Z (idle-reallocation-by-context, Andrew-direct) -> WS-2 (TO @ac96b0803). Comp-tools
lane fit: comp-system is comp-tools infra; the gate reuses the drift-gate discipline this session landed.

## Part (a) DE-STALE -- LANDED @4e5a78abc
- comp-system regen re-compiled 06_current_state.{md,json} grounded-against-live @HEAD; managed-region
  spans refreshed in 00_synthesis/03_comp_tools/README. Target hit: ledger 80->82, tools 59->61,
  cse_schema 0.4->0.5 (verified in the diff), vintage 2fda498ee->ac96b0803.
- comp-system --check = SYSTEM CURRENT (was 250 commits stale). Post-commit --check STILL CURRENT
  (the predicate no longer keys on as_of==HEAD, so the shipping commit does NOT re-manufacture STALE).
- Independent of WS-1; unblocks WS-1's honest parity measurement (it consumes the CURRENT 06).

## Part (b) GATE -- ENGINE LANDED INERT @2c4902a5c (enforcement wiring at CTO arch-gate)
Built `comp-system --gate` mirroring ~A's NESTEDABSTRACT drift_gate.py shape (read at
infra/system/sdk/abstraction_loop/drift_gate.py). Design:
- REUSES comp_system._staleness() -- ONE predicate, not a forked copy (the module's own "one expression,
  not two that agree today" discipline).
- `_gate_verdict(stale, reason, region_changes)` PURE (offline-testable, both directions) + `gate()` live wrapper.
- FAIL-CLOSED (rc 2) on GENUINE drift: a source INPUT changed (fingerprint) OR a managed-region span
  drifted from live OR pre-predicate/absent artifact. rc 1 = tool error (fail-closed). rc 0 = open.
- STALENESS-CONDITIONED: age>=TTL ALONE -> rc 0 AGE-WARN (refresh recommended), NEVER a block --
  blocking on wall-clock idle is the false-Monday class (NEVER#1). This is the load-bearing distinction
  vs --check (which reports age-staleness too).
- ALERT-SUSPENSION-CLEAN: an on-demand probe; enforcement is commit-time, NOT a new scheduled CI cadence.

## Compiler Tools
| Tool | Why | Result |
|---|---|---|
| comp-system (regen) | part-a de-stale | 06 -> CURRENT (ledger/tools/cse_schema target hit) |
| comp-system --check | phase-1 + post-commit re-verify | SYSTEM CURRENT (0 drifted), stays CURRENT post-commit |
| comp-system --self-test | gate exercises 10-13 (both directions, pure verdict) | PASS 13/13 |
| comp-system --gate (live seed) | exercise gate both directions on the real gate() I/O path | seed source-drift->rc2 FAIL-CLOSED; age-only->rc0 WARN-not-block; fixed->rc0 open; byte-identical restore |
| commit-gate.sh | Rule 14 on comp_system.py | PASS |
| comp-manifest-check | comp-system registered (--gate is a mode, not a new tool) | registration-invariant PASS |

**What worked:** reusing comp_system._staleness() kept ONE predicate (no fork); the pure/live split let me
exercise both directions offline (self-test) AND on the real I/O path (seeded 06, reversible). The
drift-vs-age distinction cleanly separates the fail-closed case from the false-Monday case.
**What failed:** first live-exercise subprocess called the bash wrapper directly (WinError 2 on Windows) --
switched to the python engine; the aborted run's finally-block restored 06 byte-clean, no harm.
**Design departure flagged to CTO:** none material -- I mirrored ~A's shape; the enforcement WIRING is the
open arch-gate item (my proposal: commit-gate leg on a comp-system _SOURCES touch, staleness-conditioned +
alert-suspension-clean; escape valve TBD by CTO).

## Blockers
NONE (both named external gates, submitted): CTO arch-gate on the enforcement WIRING (relayed via COO
@213148Z); LD-0318 CVO-verify on the wiring land. Part (a) is DONE + landed.

## Current State
- **Part (a) de-stale: COMPLETE @4e5a78abc** (comp-system --check = CURRENT).
- **Part (b) gate ENGINE: LANDED INERT @2c4902a5c** (self-test 13/13 + live both-directions). Enforcement
  wiring at CTO arch-gate (via COO). Not enforcing until CTO rules + I wire it.
- Monitor bs1gsnh6o LIVE. Session PID 25024.

## Next Steps
1. **[1.0.0_SA_CTO via 2.0.0_SA_COO]** arch-gate the enforcement WIRING: (1) commit-gate-leg-on-_SOURCES
   vs on-demand moving-checkpoint sweep vs both; (2) escape-marker shape; (3) age-WARN surfacing.
2. **[0.8.0_AE_CloudComp~D, on CTO ruling]** wire the enforcement point; re-exercise; ping CVO (LD-0318
   CVO-verified gate) + COO on land -> WS-2 close.
3. PH1 stays HELD (its KUZUSPLIT-P1 + CTO plan-gate unchanged).
