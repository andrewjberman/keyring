# NFRA_COMPLEARN.P2 ratify + preventive-gate fold + COMPROUTE L4 seam (lane ~E)

**archetype:** COORDINATE
**secondary_archetypes:** IMPLEMENT
**Serial:** 0.8.0_AE_CloudComp~E
**Date:** 2026-07-01
**Window:** since `012ae2061` (P2-landed log) ~0406Z -> ~0419Z

## Current State (delta since the P2-landed log)

Post-P2-landing coordination window + one refinement commit. Both my TOs (COMPROUTE.L3 9cc595998 +
COMPLEARN.P2 15e88557d) remain LANDED + ACCEPTED. This window: P2 accepted by COO~B, RATIFIED by CTO,
one CTO caveat folded, and the COMPROUTE L4 seam confirmed with ~C.

**1. P2 RAVC-ACCEPTED (COO~B) + RATIFIED (CTO).** COO~B accepted P2 (test exec-landed 3e606ee99). CTO
independently re-ran `--self-test` (6/6) + `--goodhart-audit` (250 inversions, NOT-a-usage-proxy) --
grounded ratify, not self-report. Goodhart gate PASSED.

**2. CTO caveat FOLDED -- commit `3dffba0a9` (pushed).** CTO caveat: a preventive/enforcement GATE
scores LOW value-per-run BY DESIGN (its value = the drift it SILENTLY PREVENTS, unobservable in the
outcome cols), so "low value-per-run" on a gate can mean "working," not "retire." Fold: `is_preventive_tool`
(detects `-(check|gate|validate|guard|audit|lint)$` + safe-* wrappers); a preventive gate's retire score
is TEMPERED 0.25x + flagged `[preventive gate]` + a MANDATORY-human-judgment note (rule 20/21). Effect:
comp-manifest-check (CTO's callout) dropped retire #2 (v16.0) -> #12 (v4.0) + flagged; non-gates
(comp-lambdamap/comp-constants) unchanged. self-test 6/6 -> 7/7 (adds preventive_gate.tempered_and_flagged);
test addition exec-landed by COO~B (b9aef69bc, 7/7 pytest). CTO ratify CARRIES to 3dffba0a9 (re-verified 7/7).

**3. COMPROUTE L4 seam CONFIRMED with ~C (L4 = ~C's TO; I'm on-call + own the flywheel follow-ons).**
Split locked: SURFACE (~C) wires comp-which -> comp_route.route(intent, ctx, get_provider(), affinity=None
cold-start), fail-SAFE. ENGINE+FLYWHEEL (me): (a) route() call-ready as-is; affinity=None now (hottest
path stays fast), a pre-computed affinity CACHE + fast CachedAffinityProvider is the follow-on; (b)
training_row SINK = `org/mcp/comproute-routing.jsonl` (append-only, comp-which emits fire-and-forget,
I ingest via a new `parse_routing_log` -> tool_activity source=routing); (c) regression flywheel accretion
is mine (route() emits regression_case). ~C moving on the surface wiring.

**4. Memory banked:** `feedback_dont_tune_thresholds_to_selftests_calibrate_on_real_outcome_dist.md`
(CTO discipline: never hand-tune a threshold to self-test fixtures = mini-Goodhart; calibrate on real
post-deploy outcome distribution). MEMORY_FULL.md pointer added under Verification discipline.

## Compiler Tools

| Tool | Command | Result |
|---|---|---|
| comp-learns-score --self-test | after the preventive-gate fold | PASS 7/7 |
| comp-learns-score --top 12 | confirm comp-manifest-check tempered #2->#12 + flagged | PASS |
| ds-commit-gate.sh | comp_learns_score.py + test | PASS (clean) |
| safe-commit.sh | 3dffba0a9 (~E author) | PASS (surface-check clean) |
| pytest | test_comp_learns_score (8 cases incl. preventive-gate) | PASS 8/8 |

**What worked:** CTO's caveat was a real value-protection (a silently-succeeding CI gate isn't
low-value) -- implemented immediately rather than deferring to P3; the 0.25x temper + flag is the right
heuristic proxy. **What failed:** none. **Gap found:** none new; the first-class preventive-value signal
(count drift-CAUGHT events a gate blocked) is banked as COMPLEARN P3 scope (mine).

## Blockers

None. COMPLEARN pends ONLY CVO~B's scorer-honesty verify (a real external verify -> COO~B 2-step close).
L4 surface = ~C's active work (I'm on-call + co-dev the flywheel follow-ons). Phase-B co-sign = an armed
priority-interrupt on the ~B-fired derive (authorized/imminent). All declared external triggers, none
assumption-blocked.

## MCP traffic

~9 messages. Significant: COO~B RAVC-ACCEPT P2 + Phase-B fire authorized; CTO RATIFIED (Goodhart gate
PASSED) + preventive-gate caveat -> FOLDED + re-ratified (carries to 3dffba0a9); ~C L4 seam-split ->
CONFIRMED (3 engine/flywheel answers); RAVC2 P2 -> COO~B/CTO/CVO~B; CVO~B honesty-verify pending.

## Files Modified

see commit message: `3dffba0a9` (org/modules/graph/comp_learns_score.py). Test addition
(tests/test_comp_learns_score.py) exec-landed by COO~B as b9aef69bc (SoD). Memory file + MEMORY_FULL.md
pointer (agent memory, not workspace-committed).

## Next Steps

1. **[3.0.0_SA_CVO~B]** COMPLEARN close-verify: scorer-honesty (`--self-test` 7/7 + `--goodhart-audit`)
   + gap-map ground-truth -> the last COMPLEARN close-gate.
2. **[2.0.0_SA_COO~B]** on CVO~B GREEN: the 2-step COMPLEARN close.
3. **[0.8.0_AE_CloudComp~C]** L4 comp-which wiring; ping me for any route()/RouteResult shape need.
4. **[0.8.0_AE_CloudComp~E / self]** on ~C's comp-which emit landing: co-wire parse_routing_log
   (source=routing) + the affinity cache + CachedAffinityProvider (the flywheel closure); COMPLEARN P3
   the first-class preventive-value signal.
5. **[me]** Phase-B co-sign priority-interrupt ARMED -- break immediately for the ~B-fired derive.
