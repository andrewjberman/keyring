# CVO Exercise-Cert — TOOLHEALTH TH-C clause A (close-the-loop dispatch layer): PASS

**Date:** 2026-07-07T06:30Z
**Agent:** 3.0.0_SA_CVO
**Built:** comp_tool_health_gate.py (49dbc84dc + 4f71ccaf2). Converts each non-KEEP TH-B verdict -> a TYPED ADVISORY commission (FIX->fix-TO / RETIRE->deprecation-candidate / PROMOTE->concrete comp_route surface_prior proposal), advisory-only zero auto-mutation, each carrying the 3-axis HEALTH GROUNDING (CTO ratifies on evidence not label). Imports th.health() UN-FORKED.
**Scope (CTO):** clause A = DRV-INDEPENDENT (the DISPATCH layer -- verdict DRIVES the commission); certifiable now. Clause B (live-routing behavior-delta) gates on the (b) tail-corpus -- follows.
**Verdict:** PASS -- clause A close-the-loop CLOSES at the dispatch layer.

## Exercise (the load-bearing differential, on a LIVE tool -- NOT the self-test)
Pulled live th.health() = 52 tools (FIX 3 / RETIRE 4 / KEEP 45). Chose the LIVE KEEP tool comp-pipescript (real verdict=KEEP), ran the SAME live row through commission_for in both health states:
- HEALTHY (verdict=KEEP)  -> commission = **None**  (the null path the differential pivots on -- a healthy tool drives NO commission)
- FAILING (same live row, verdict flipped FIX) -> **action = "fix-commission"**:
    proposed_to.kind = "fix-TO", ratifier = "1.0.0_SA_CTO", auto_mutates = **False** (advisory, no auto-mutation)
    grounding carried from the LIVE row: used.events = 3092, rail.state = "chosen", effective = "pending (TH-A)"
=> DIFFERENTIAL on the SAME live tool: KEEP->None, FIX->fix-commission, advisory-only. The verdict DRIVES the action at the dispatch layer.

## Why this is the close-the-loop (not just a display)
Pre-TH-C: TH-B computes a verdict but DRIVES NOTHING (a display). TH-C clause A: a non-KEEP verdict now EMITS a typed, grounded, CTO-ratifiable advisory commission; a KEEP emits nothing. The before(display)->after(a commission a human can act on) IS the close-the-loop, proven by the healthy->NONE / failing->fix-commission differential on real live data.

## Honest notes (do not block clause A)
- Commissions carry `pending_effective=True` (grounding effective="pending TH-A") -> provisional until the recurring EFFECTIVE probe (TH-A) confirms. An honest flag; does NOT affect the dispatch-layer differential (verdict->commission logic is deterministic). TH-A effective-probe is a separate limb.
- ADVISORY by construction (auto_mutates=False, names a CTO ratifier) -> zero auto-mutation risk; the human gate is intact (mirrors NFRA_DEBTSCAN never-auto-delete).

## Verdict
TH-C clause A = PASS. Close-the-loop closes at the dispatch layer (verdict DRIVES a typed advisory commission; KEEP drives none), exercised on live comp-pipescript. Clause B (routing behavior-delta) follows on the tail-corpus. 2nd NFRA+SCTY-DRIVE completion cert.
