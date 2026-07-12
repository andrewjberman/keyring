# CVO~A -- PASSCRAFT: the FP-R0 (QUESTION-CLASS) ruling + rail mint + emitter fold; and catching CTO's two-rail-set conflation

**archetype:** VALIDATE
**secondary_archetypes:** IMPLEMENT, COORDINATE

**Window:** 2026-07-12T12:02Z (last log 994fd0b26) -> ~15:03Z. Andrew-direct dispatch (via MSTR->CTO 133357Z): CVO~A owns PASSCRAFT P2+R0+AC4 -- the open tail of the tool-check-generalization program. 3 commits (2 CVO + 1 CTO-authored hand-off). Workstream CLOSED (CTO 150310Z).

## Summary

Owned + closed the PASSCRAFT R0 workstream. GROUNDED the program first (found TO-1 recon + TO-2 emitter already BUILT+green by 0.8.0_AE_CloudComp -- not the "prose" greenfield the dispatch implied; my job was the CVO-owned pieces). RULED R0 IN (CTO arch-gate-ratified): classify the QUESTION before the CLAIM -- a DYNAMIC question answered from SOURCE is auto-INFERRED, never OBSERVED. Minted it as FP-R0 into a version-pinned CVO-owned front-pass rule set. Folded it into the ToolAudit emitter as a fail-closed consistency lint (anti-harness §0 held -- computes no verdict). Along the way CAUGHT CTO's own two-rail-set conflation (he authorized minting into the wrong set) and my R0 principle DECIDED the ToolAudit<->wire architecture (a hand-authored verdict is INFERRED, so it can't be the wire's effective source -> CTO decoupled them). The keystone is live (wire 995aee8a5, comp-freshness=FIX) with FP-R0 as its classification backbone.

## Work done

- **R0 RULING (TO-R0, the load-bearing CVO deliverable): R0 IN, a NEW rail upstream of FP-R1.** Source-grounded (NFRA_TOOLPASS @11af75d95): FP-R1 (CLASS) leaves the OBSERVED/INFERRED boundary to author judgment; a source read IS "a command+output line", so a dynamic-from-source passes FP-R1's letter while INFERRED in truth; tool-1's 4/10-wrong (all this class) proves R1-as-practiced didn't catch it; the doctrine (:89-90) holds it as "a candidate amendment routed to CVO, NOT self-landed" -- explicitly awaiting this ruling. Corroborated by EXERCISE (my comp-transform what-value-flowed + comp-whoread who-reads-at-runtime + CTO's own comp-transform false-UNUSED fix -- 3 design-independent). CTO independently re-grounded + ratified.
- **CAUGHT THE TWO-RAIL-SET COLLISION (grounding catch, before minting):** RAIL_SET_canonical_20260710 (R1-R7 = verification negative-controls) and NFRA_TOOLPASS "four rules" (R1-R4 = CLASS/FALSIFIER/BRANCH/CENSUS) are TWO different R-numbered sets. CTO's R0 reasoning cited the four-rules R1/R3 but authorized minting into RAIL_SET_canonical (whose R1=NEGATIVE, not CLASS). Surfaced it; CTO corrected the home (front-pass set) + affirmed it's the exact two-names-per-number drift the RAIL_SET's own :178 rule forbids.
- **MINTED the rail (eeaef157f):** org/tier1_exec/3.0.0_SA_CVO/deliverables/FRONTPASS_RULES_canonical_20260712.md -- FP-R0..FP-R4 version-pinned, the FP- prefix + a "two sets are DISTINCT" table as the durable collision fix, CTO's conflation+correction recorded on the artifact's face (R5-disclosure), the 5 dynamic-question types, the exercised minting bar, the CLAUDE.md Rule-22 tie, and the exercised-reach corollary (shared with CVO base's effective-axis).
- **CSE CONVERGENCE with CVO base (lead): converged then cleanly DECOUPLED.** My exercised-reach strengthener (effective=yes needs an EXERCISED oracle_run, never a source file:line) landed in the SHARED contract. Then CTO ruled (134939Z) the wire reads only CVO~B's exercised probe -- because a hand-authored ToolAudit effective is reading-confidence=INFERRED, which FP-R0 BARS from being the effective source. So the ToolAudit dropped effective/effective_evidence/verdict-enum (dead weight for a decoupled wire); FP-R0 DECIDED that architecture.
- **EMITTER FP-R0 FOLD (32141b332, CTO §0-gate PASS):** comp_passcraft.py + tests. question_class (STATIC|DYNAMIC, REQUIRED, fail-closed) + the FP-R0 consistency lint (DYNAMIC + class=OBSERVED + source-only evidence_ref -> REJECT). Anti-harness held: the lint appends to `errors` (a validation, same category as class-enum), computes NO verdict. Proven non-vacuous by source-neuter (disable the lint -> dynamic-from-source test flips RED). AC4 FUNCTIONAL upgrade closes the name-based gap in the old structural anti-harness check: a meta-test injects a verdict-DERIVING path (monkeypatch validate to auto-supply a missing verdict) -> the reject stops firing -> proving the anti-harness REJECT is real, not name-dependent.
- **DOC AMEND (e5e7d13b9, CTO-authored -- lane hand-off):** NFRA_TOOLPASS sec.2 amends-to-cite FRONTPASS_RULES_canonical (FP-R0 entry + canonical note + FP-Rn annotations + the disambiguation). owned-paths BLOCKED my CVO commit (docs/architecture/ = ANY_CTO lane); I did NOT --force, unstaged to keep the shared index clean, handed CTO the exact command; CTO landed it.

## Compiler Tools

| Tool | Run | Result | Note |
|---|---|---|---|
| comp-passcraft --self-test | exercised (before + after the fold) | PASS | 15->21 checks incl the 5 FP-R0 cases + AC4 non-vacuity |
| comp-passcraft (source-read + neuter) | recon/emit/validate grounded from source | n/a | grounded TO-1+TO-2 built-state; source-neutered the FP-R0 lint to prove non-vacuity |
| py_compile / ruff / commit-gate / safe-commit | every commit | PASS | all 3 commits clean (owned-paths correctly blocked the arch-doc CVO commit) |
| pytest test_passcraft_anti_harness.py | exercised | PASS | 17->22 (added FP-R0 tests + the AC4 functional neuter) |

- **What worked:** grounding-before-acting caught (a) the emitter wasn't greenfield, (b) CTO's two-set conflation, (c) the effective=INFERRED architecture decision. The neuter-audit discipline proved both the FP-R0 lint and the anti-harness reject non-vacuous.
- **What failed:** nothing shipped wrong; owned-paths blocked my arch-doc commit as designed (correct -- a lane boundary, not mine to bypass).
- **Gap found:** the CVO-publishes-canonical / doc-amends-to-match pattern is inherently a TWO-author hand-off (canonical rail set in org/ = CVO-lane; the citing doc in docs/architecture/ = ANY_CTO-lane). CTO affirmed + banked; worth documenting in the pattern so nobody assumes single-author.

## MCP traffic

~30 messages, all CTO + CVO-base coordination (no genuine human input -- the Andrew-direct dispatch arrived via MSTR->CTO). Significant: CTO's R0 arch-gate ratification (134429Z) + routing correction (my collision catch, 135144Z) + the effective-decouple ruling (134939Z) + the emitter §0-gate PASS (141005Z) + 2 substance/amend gates (135857Z, 145848Z); CVO base's CSE convergence v1-lock + supersede + reconcile (my strengthener into the shared contract).

## Blockers

None standing. One RESOLVED: owned-paths (BLOCK mode) rejected my CVO commit of the arch-doc amend (lane=ANY_CTO); handed to CTO who landed it under a CTO author (e5e7d13b9). Not an assumption-blocker -- evidence-cited (the hook's own VIOLATION line).

## Current State (handoff -- zero prior context)

- **PASSCRAFT/FP-R0 workstream CLOSED.** 3 commits: rail eeaef157f (CVO, org/tier1_exec/3.0.0_SA_CVO/deliverables/FRONTPASS_RULES_canonical_20260712.md) + emitter 32141b332 (CVO, org/modules/graph/comp_passcraft.py + tests/test_passcraft_anti_harness.py) + doc amend e5e7d13b9 (CTO, docs/architecture/NFRA_TOOLPASS.md sec.2). All on origin/CLOUD.
- **FP-R0 is LIVE-LOAD-BEARING:** the keystone wire (995aee8a5, comp_tool_health.classify_full) reads CVO~B's exercised probe for `effective`; comp-freshness=FIX by default; that verdict is trustworthy because of FP-R0's exercised-reach law (effective=yes needs an exercised run, never a source read).
- **The ToolAudit emitter** (comp_passcraft.py) now requires question_class + lints FP-R0; it feeds the assurance-plane annotation (a separate TOOLGRAPH consumer), NOT the wire (decoupled). If that consumer later wants `effective` on the ToolAudit, coordinate with the TOOLGRAPH TO-2 / assurance-plane owner (the effective field + CSE placement Qualifier.EFFECTIVE was drafted with CVO base but deferred).
- **CVO cron state:** ZERO. Inbox watcher live (Monitor b9jexby6b).

## Next Steps

- **[me/CVO~A]** PASSCRAFT R0 done. Free + reachable for CTO's next dispatch.
- **[owner: TOOLGRAPH TO-2 / assurance-plane annotation]** if the ToolAudit CSE should carry `effective`, coordinate the CSE placement (Qualifier.EFFECTIVE vs provenance, cse_schema 0.4->0.5) -- my dedicated-Qualifier lean is on record; the exercised-reach lint would land with it.
- **[1.0.0_SA_CTO]** optional: document the two-author hand-off in the doc-amends-to-match pattern (per the lane-seam CTO banked).

## Files Modified

See commit messages for per-file detail: eeaef157f (rail, CVO), 32141b332 (emitter+tests, CVO), e5e7d13b9 (NFRA_TOOLPASS sec.2 amend, CTO-authored via the lane hand-off).
