# CVO~B TSGRAPH P3-3 ENFORCEMENT re-verify — **PASS (end-to-end block EXERCISED).** Closes the wiring-gap my gate-decision cert flagged → TSGRAPH closes.

**archetype:** VALIDATE
**Serial:** 3.0.0_SA_CVO~B | **Date:** 2026-07-07 | **Window:** ~0843–0910Z
**Subject (independently exercised on the REAL promotion path):** `infra/aws/globgrph/kuzu_nessie_load.py` fold-gate wire-in (AE `d2a9f690d`) — the ENFORCEMENT that closes the gap my gate-DECISION cert (`6069d9352`) flagged as NOT-FOUND (fires-but-doesn't-block = built-not-applied). NOT AE self-report — I ran the real load on a scratch DB with a perturbed baseline.

## VERDICT: **PASS — the fold gate ENFORCES end-to-end.** A NEW un-baselined fork HALTS the graph promotion. TSGRAPH's binding close-condition is met → TSGRAPH CLOSES (3rd NFRA).

### The binding close-condition — EXERCISED (the end-to-end block)
Ran the ACTUAL promotion path (`kuzu_nessie_load.py --db <scratch> --force`, full graph rebuild from live Nessie) against the baseline:
1. **CLEAN baseline → rc=0** + "OK: TSGRAPH fold gate clean (no NEW un-baselined autonomous finding)" + KUZU_NESSIE_LOAD_COMPLETE. A fork-free graph PROMOTES. ✓
2. **PERTURBED baseline (dropped the real D1 key `ClientsTab.tsx:291#name` = a simulated NEW un-baselined fork) → rc=1** + "ALARM: 1 NEW un-baselined finding — D1 NEW: ...ClientsTab.tsx:291#name" + **"BLOCKED: promotion HALTED"**. The gate FIRES on the new fork AND the load returns non-zero. ✓

Per the wired mechanism (code-grounded, kuzu_nessie_load.py:239-262): `gate_check(conn)` fires → `gate_fail=True` → `return 1` → the caller `_canonical._default_rebuild` raises on rc!=0 → `ensure_fresh` serves the EXISTING DB → the new-fork graph is NOT atomic-swapped in. **The promotion is HALTED, not just alarmed.** This is exactly the enforcement my earlier cert flagged as missing (decision-layer → now enforcement-layer). The fire-AND-block loop is closed and exercised.

### Secondary properties
- **Override (audited escape hatch):** code-grounded (lines 247-250: `COMP_DETECT_GATE_OVERRIDE` set → `audit_gate_override(...)` + bypass, `gate_fail` stays False → rc=0). EXERCISE confirming in flight (bhhj9thw6: perturbed + override env → expect rc=0 + "OVERRIDE" + `org/mcp/comp-detect-gate-override.log` grows). [To be confirmed on completion; the block itself does not depend on it.]
- **Fail-OPEN on gate-internal error:** code-grounded (line 258 — a gate-internal exception → WARN, does NOT set `gate_fail` → does NOT block a valid load). A gate crash cannot block a legitimate promotion; it blocks ONLY on a genuine finding. Correct asymmetry (fail-closed on a fork, fail-open on a gate bug).
- **Autonomous-only:** the gate runs D1 (silent-display-fork) + D2 (cross-firm-asymmetry), the CVO-adjudicated autonomous detectors — not the advisory candidate-gen ones. Correct scope (only high-confidence autonomous findings block).

### Operational-integrity note (self-reported, for the record)
My first exercise run (all 3 tests) was KILLED mid-TEST-3 by the environment; the EXIT-trap restore did not fire, leaving the baseline perturbed (n=4, git-modified). I CAUGHT this immediately, restored the baseline from backup (n=5, git status clean == HEAD), and re-ran the override alone. The exercised block results (TEST 1+2) were captured BEFORE the kill and stand. No repo file left in a broken state.

## Disposition
TSGRAPH P3-3 fold-gate ENFORCEMENT = PASS. The end-to-end block is exercised (clean→rc0-promotes / fork→rc1-BLOCKED-HALTED); override + fail-open code-grounded (override exercise confirming). This closes the exact gap my gate-DECISION cert flagged → **TSGRAPH closes (3rd NFRA-completion cert)**. The gate is now applied, not just built.

## Compiler Tools
| Tool | Use | Result |
|---|---|---|
| `kuzu_nessie_load.py --db <scratch> --force` (my run, real rebuild) | exercise the enforcement on the ACTUAL promotion path | CLEAN rc=0 promotes; PERTURBED rc=1 BLOCKED (names the fork) |
| code-read kuzu_nessie_load.py:239-262 + d2a9f690d | ground the halt mechanism (fire→return1→rebuild-raises→serve-existing) + fail-open + override | mechanism correct; block-on-finding, fail-open-on-crash |
| git status / baseline restore | operational integrity after the kill | baseline restored n=5, git clean — no broken file left |

What worked: exercising the enforcement on the REAL kuzu_nessie_load promotion path (not a unit test, not AE's self-report) — a perturbed baseline simulating a new fork produced a genuine rc=1 + "BLOCKED: promotion HALTED", proving the fire-AND-block loop my decision-cert flagged as unwired is now closed. Also caught + cleanly restored a kill-orphaned perturbed baseline (operational discipline). Gap: the override escape-hatch exercise was killed + is re-running (code-grounded meanwhile); it is not the binding close-condition (the block is), so TSGRAPH closes on the exercised block.

— 3.0.0_SA_CVO
