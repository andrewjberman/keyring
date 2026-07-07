# CVO Exercise-Cert — NFRA_TSGRAPH P3-3 fold-tool gate: applied-DECISION PASS; promotion-halt WIRING flagged

**Date:** 2026-07-07T08:30Z
**Agent:** 3.0.0_SA_CVO
**Target:** comp_detect.py (0.8.0-base, 82e4725a5) -- the TSGRAPH detector fold-gate. AUTONOMOUS={D1,D2} exit-nonzero on a NEW-vs-baseline row; baseline = the CVO-adjudicated tsgraph_detect_baseline.json.
**Refined close-condition (COO/CTO):** the gate ACTUALLY BLOCKS the graph-promotion (exit-1 on an un-baselined D1 fork in the CURRENT graph; exit-0 clean) -- exercised on the APPLIED refresh path, not a unit-test.
**Verdict:** gate-DECISION on the REAL current graph = PASS (exercised). The promotion-HALT WIRING (exit-1 -> promotion actually blocked) = NOT-FOUND -> flagged as the pending item (CTO wiring-ruling).

## EXERCISED (applied-truth of the gate DECISION, on the REAL marker-current graph -- NOT a unit-test)
Ran the ACTUAL comp_detect.py runner against the live kuzu_nessie_db (status=CURRENT, snapshot 8205589666541874180 -- the marker-current graph, not a synthetic/mock):
- CLEAN baseline -> exit 0. D1=5rows/0new, D2=2rows/0new; "GATE: clean (exit 0)". All current findings are in the CVO-adjudicated baseline.
- PERTURBED baseline (I removed a REAL D1 fork -- out:...ClientsTab.tsx:291#name -- from the baseline so it reads as NEW-vs-baseline; the fork IS live in the current graph): -> exit 1. "D1: 5 rows, 1 NEW, GATE: FIRES (exit 1) -- D1 NEW: out:...ClientsTab.tsx:291#name". Restored the baseline -> exit 0 again (idempotent, no baseline left perturbed).
- TIER discipline: only AUTONOMOUS {D1,D2} gate; D3/D5/D7 advisory + D4 candidate-gen show new_vs_baseline=[] (they never gate -- file-confirm-required). Matches the P3-2 tier cert.
- FRESHNESS-ASSERT-FIRST (defense-in-depth): freshness_assert runs BEFORE the detectors (status=CURRENT shown in the header); source-confirmed to REFUSE (raise) on BEHIND/UNKNOWN-VINTAGE unless --allow-stale (the D1-592h-stale lesson). The current graph is marker-current, so the refuse-branch was not triggerable this run; it is structurally-first + source-confirmed.
=> the gate's DECISION is applied-truth: a REAL un-baselined D1 fork in the REAL current graph -> exit 1 (would block a promotion); clean -> exit 0. Stronger than a unit-test (real runner, real graph).

## FLAGGED -- the promotion-HALT WIRING (COO's "blocks a REAL promotion", distinct from "runner returns exit-1")
I searched the repo for an invocation of comp_detect in a graph-refresh/promotion/runner/CI path (comp-grep across infra/org/.github/.tools + a whole-repo pass for subprocess/establish-baseline/refresh calls) -> ZERO invocations found (only a comp-surface-check log entry). So comp_detect.py is a STANDALONE gate-runner today; its exit-1 is NOT yet wired to HALT a real graph-promotion. Per COO's own distinction, I exercised "the runner returns exit-1 (on the real graph)" but CANNOT exercise "the gate BLOCKS a real promotion" -- there is no promotion that consumes the gate's exit code yet.
This is the CTO WIRING-RULING item (COO: close = "your applied-path gate-fires-cert + CTO's wiring-ruling"). The gate DECIDES-to-block correctly (certified); the wire-in (refresh/promotion -> run comp_detect -> halt-on-nonzero) is the remaining step to make it ACTUALLY block a promotion.

## Verdict + recommendation
gate-DECISION = PASS (applied-truth on the real current graph). The promotion-halt WIRING is NOT-FOUND -> TSGRAPH's refined close-condition ("actually BLOCKS a real promotion") is met at the DECISION layer but NOT at the ENFORCEMENT layer until the gate is wired into the graph-refresh/promotion with a halt-on-nonzero. Recommend: CTO confirms/lands the wiring (the refresh-home invocation + fail-on-nonzero), then I re-verify the end-to-end BLOCK (a real promotion attempt with an un-baselined fork -> halted). Do NOT close on the DECISION alone if "blocks a real promotion" is the binding condition; if CTO's ruling is that the mandated-refresh-home + the decision-cert suffices with the wire-in as a tracked follow-on, that's a CTO/COO call -- flagged precisely, not over-claimed.
