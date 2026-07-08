# LOOP-CLOSE terminus/acceptance cert -- CONDITIONAL PASS (real-measure + gate-bites + reversible-inverse HELD; DEMOTED-CSE-emission is the ONE required fix)

**archetype:** VALIDATE
**secondary_archetypes:** DIAGNOSE
**Agent:** 3.0.0_SA_CVO | **Date:** 2026-07-08T15:3xZ
**From:** DS~B (152458Z) + COO~B (150857Z) + CTO ratify (commission CTO-PROMOTE-20260708T1521Z) | recognizer materialized ac7ed5086
**Grounding:** git spot-check of the co_session shas vs real portal commits + EXERCISED demote on the real ac7ed5086 artifact (not the fixture) + source-read of main()'s CSE handling. The terminus phantom-guard + inspectability bar.

## VERDICT: CONDITIONAL PASS. The substantive loop-close HOLDS (measure git-real, gate bites 1/7, reversibility exact-inverse proven, human-ratify gated). ONE required fix before full closure: the materialize/demote CLI must EMIT/PERSIST the MATERIALIZED/DEMOTED CSE (R4/AC5). The write-back is reversible+real+gated but NOT yet CSE-audit-trailed.

### (i) MEASURES ARE GIT-REAL (phantom-guard) -- PASS (+ signal-quality note)
CTO's expanded 6-sha sample, ALL git-verified to real portal commits where the claimed files co-changed: e502951536 {portal-proxy,ModelPortfolios} (benchmark toggle), fbfdbe9d75 {same} (YANG_SITTW refine, 2-file focused), ce0eb37123 {ClientsTab,DistributionTab} (007b sweep), 149622a0ac {portal-proxy,ModelPortfolios} (demo endpoints), 5557c3100a {same} (34-file restructure), 3e128b0223 {same} (15-file heatmap). Signal is REAL, not manufactured. Distribution skewed/sparse. HONEST NOTE (correcting DS~B's "all focused, not sweeps"): 3 of 6 are BROAD commits (34/15/6 files) incl. one literal unused-vars sweep -- the coupling signal includes broad-commit co-appearances (weaker than "focused"). NOT a phantom (acceptance = real-vs-manufactured, which passes); a signal-quality refinement for productionization (weight by commit breadth / exclude sweeps).

### (iii) GATE BITES ON REAL DATA -- PASS (1/7, tightened by the smell)
silent-display-fork promoted on its OWN independent 0.18 warrant; firm-conditional-display HELD (file-subsumed -> no independent co-evolution warrant, coupling neutralized to 0.0 -- my measure-provenance smell -> COO disposition -> CTO-affirmed); 5 others dropped. 1/7, not all 7. A real sparse signal leaves >=6 held -- gate bites hard. My smell made it MORE honest (prevented a double-count promotion of the system).

### (ii) REVERSIBILITY -- exact-inverse PROVEN, but DEMOTED-CSE-EMIT FAILS (the required fix)
- EXACT-INVERSE round-trip: PROVEN by exercise on the REAL ac7ed5086 artifact (not the fixture). PRE manifest = [recognizer:silent-display-fork] -> demote -> POST = [] (returns to pre-materialize state exactly). Reversibility MECHANISM works.
- DEMOTED CSE EMITS: FAILS. GROUNDED by exercise: demote-CSE lines in the trails = 0 BEFORE and 0 AFTER my demote. Source confirms: demote() constructs + RETURNS the cse (line 133) but main() (line 220-221) prints ONLY `reason` and DISCARDS the cse; --materialize prints its CSE to stdout only (line 215), never to a trail. So R4 ("every materialize/demote emits a CSE") + AC5 (inspectable CSE trail) are NOT met by the CLI: the R3 critical-surface manifest is mutated with NO durable CSE audit trail (only the manifest's own git history). REQUIRED FIX: main() APPENDS the returned cse to the lifecycle trail for BOTH --materialize and --demote. Well-scoped; then the terminus closes clean.

## What this means for the loop-close
The SEMCTL federated learning loop's SUBSTANTIVE close is real: observe (CSE) -> measure (git-real co-evolution) -> validate (gate bites, honest 1/7) -> promote (CTO human-ratify) -> materialize (reversible, exact-inverse proven). Honesty held at every gate (the phantom-guard caught the double-count smell; the measure is git-grounded not manufactured). The ONE gap is inspectability of the write-back: the materialize/demote events are not emitted as CSEs, so the governance plane can't audit them as CSEs (git history is a partial mitigation). This is a governance/auditability gap, not a correctness/safety one -- but R4/AC5 is an explicit invariant, so the terminus is CONDITIONAL until the CSE-emission lands.

## State + handoff
- Manifest currently EMPTY (I demoted silent-display-fork for the reversibility exercise). Pinged DS~B to RE-MATERIALIZE under CTO's commission (AC2: I cannot self-materialize) -> the ratified promotion stands. Will confirm the restored manifest.
- On (a) the CSE-emission fix + (b) the manifest re-materialized -> terminus closes clean (full PASS).

## Compiler Tools
- git -C portal show --name-only x6 (measure phantom-guard) + EXERCISED --demote on the real artifact + grep the CSE trails before/after (grounds the CSE-emit gap by exercise, not just by reading main()) + source-read main(). No comp-tool models a promotion-lifecycle CSE trail; the exercised run + git are the grounding.

-- 3.0.0_SA_CVO
