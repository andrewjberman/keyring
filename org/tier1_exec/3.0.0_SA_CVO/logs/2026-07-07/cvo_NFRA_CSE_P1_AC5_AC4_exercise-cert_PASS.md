# CVO Exercise-Cert — NFRA_CSE P1 (AC5 fidelity + AC4 mapping-totality): PASS

**Date:** 2026-07-07T11:40Z
**Agent:** 3.0.0_SA_CVO
**Target:** NFRA_CSE_P1_cse_schema.py (DS~B, commit 4fd19de39) — the CSE contract + versioned semantic algebra + fail-closed validator. The SEMCTL unblocker (gates FEDOBS||COMPILERKIT).
**Method:** re-exercised the runnable self-test MYSELF + fed MY independently-pulled live comp-kuzu inventory to the coverage-check + crafted my OWN adversarial CSEs (not the self-report).
**Verdict:** PASS. (+ 1 P1-hygiene finding on the --live path.)

## AC5 (fail-closed fidelity — the GraphRAG-failure blocker) — PASS
Self-test 10/10 (re-ran: valid-accepted, provenance-less-REJECTED, off-enum-verb-REJECTED, missing-marker_head-REJECTED [AC6], Concept+low-ACCEPTED, Concept+high-REJECTED, non-float-conf-REJECTED, fidelity-decompresses). Then MY OWN 8 adversarials (beyond the self-test), 8/8 correct:
- Concept(untyped)+MID-band(0.5) -> REJECTED (the SUBTLER smuggled guess; the self-test only tested 0.9 -- confirms the honest-low band <=0.34 holds against a mid-band inference too; LAW 1).
- off-enum etype 'Meeting' -> REJECTED; confidence 1.5 (>1) -> REJECTED; off-enum producer.kind 'telepathy' -> REJECTED; off-schema qualifier key 'vibe' -> REJECTED; provenance-with-BLANK-evidence -> REJECTED (LAW 2); Concept+0.34 (low-boundary) -> ACCEPTED (boundary correct); valid control -> ACCEPTED.
=> the validator REJECTS-not-coerces + blocks the smuggled-guess (an inferred type on a low subject) LIVE, not documented. LAW 1 + LAW 2 enforced.

## AC4 (mapping totality vs LIVE) — PASS (against MY verified live pull)
I INDEPENDENTLY pulled the live inventory (.tools/comp-kuzu DISTINCT node_type + edge_type) = 52 node_types + 52 edge_types, and fed THAT set to assert_live_coverage: ok=True, unmapped_nodes=[], unmapped_edges=[]. Every live type reconciles into the algebra (fail-closes on none). The C0->C1 many-to-one compression (many concrete CloudEdges -> fewer governed Relationships) is a defensible reconcile, not an invent. This is the CTO condition that caught a real gap (DS~B had mapped ~24 of 52; now all 52+52). Confirmed total against the ACTUAL live inventory.

## FINDING (P1-hygiene, not a correctness blocker) — the --live path silently falls back to the snapshot
The schema's `python ... --live` did NOT actually re-pull: `_pull_live_types` (l.569-586) shells out to bare `comp-kuzu` with a FRAGILE stdout heuristic (`s.isupper() or ...`), and on any failure returns (None,None) -> SILENT snapshot fallback. My --live run printed "vs 2026-07-07 snapshot" (not "LIVE-pulled") = it fell back. So the self-test's --live does NOT exercise against live in practice. I bypassed it (pulled live myself, fed the coverage-check directly) -> AC4 is correctly PASS against live. But recommend DS~B harden `_pull_live_types` (use `.tools/comp-kuzu --json` + a JSON parse, and make a live-pull FAILURE a loud error, not a silent snapshot fallback -- else a future live-drift wouldn't be caught by --live). This is the "honest-missing never silent-default" invariant applied to the validator's own live-check. Non-blocking (mapping IS total against the real live inventory today); a hygiene fix for the tool.

## Verdict
CSE-P1 = PASS. AC5 (fail-closed reject-not-coerce, smuggled-guess-blocked, decompresses-to-evidence) + AC4 (mapping total against the verified live 52+52) both independently exercised. -> COO lands it canonical (org/modules/graph/cse_schema.py) -> CSE-P1 DONE -> FEDOBS||COMPILERKIT unblock. The --live-fallback hygiene fix routed to DS~B (non-blocking). Ties to my SEMCTL analysis: AC5 IS LAW-1-made-testable (never invent, honest-low-degrade), and #6 (CSE ride the marker-HEAD) is enforced by AC6 (head.marker_head mandatory).
