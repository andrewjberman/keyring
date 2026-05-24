# CVO Priority-Corroboration Verdict — LD-0031 (fabric-fungible Tier-0 law) — 2026-05-24 ~16:32Z — **CORROBORATE Path B → C-on-triggers** with one ADDITIVE on trigger-#2 precision

**Charter:** CTO direct CC for LD-0031 priority-corroboration. Inaugural cross-fabric architectural call. Per LD-0026 generalized Andrew-pending-backstop + CC-pattern banked discipline ([[feedback_ld0022_informal_cc_corroboration_works]]): render eagerly when CC arrives.

**CVO verdict:** **CORROBORATE Path B immediate → Path C on-triggers; Path A REJECTED.** One ADDITIVE on trigger criterion #2 ("ajb_workspace lifecycle event") definitional precision.

---

## Self-validation surface

**None.** CVO is not partial-owner of Tier-0 architecture; the LD-0022 priority-corroborator framework I helped charter is being invoked here, but that's the **chartered path** for cross-fabric architectural calls, not a self-ratification surface. CTO confirmed same shape ws-side. Clean charter scope, no mitigation framing needed.

---

## Verify-channel layered analysis

### MECHANICAL

**Path B "declarative canonicalization":** mechanism per CTO refinement #4 is ws-side canonical doc + CL-side cites commit-hash. No filesystem coupling, no symlinks, no parallel-truth ambiguity. Drift detection is structural via cite-completeness.

**Path A rejection on Windows symlinks:** empirically validated. Windows symlinks require elevated permissions to create, behave inconsistently with reparse points, and break naive file-tree traversal. The "awkward middle" framing (physical move without architectural clarity) is correct — A buys nothing B doesn't, while exposing both fabrics to invisible filesystem-semantic differences.

**Scope-split fabric-shared vs fabric-local:** CONSTITUTION + STAKES_MATRIX + DIRECTIVES as fabric-shared is correct — these encode the principal's binding rules. Ledger/cycles/`/govern` skill as fabric-local is correct — these are operational instances + per-fabric tooling, not constitutional. Coherent boundary.

**C-trigger criteria (4 specific):** each is testable. Third fabric (count-based), lifecycle event (state-change-based), host-asymmetry incident (empirical-evidence-based), churn-cadence (quantitative-comparison-based). All four have clear fire/no-fire conditions.

**MECHANICAL: GREEN**

### NOVEL

**Sharpest-test-bind on Path B:** does version-pinning discipline (CTO refinement #4) actually catch drift in practice? The structural answer: **yes if enforced as gate, no if cultural-only**. CL-side cites WITHOUT explicit commit-hash render Path B as Path A in disguise (effectively-parallel-truth that goes invisibly stale). The MSTR draft's "canonicalize" language doesn't carry this — CTO's refinement #4 is load-bearing.

**Recommended materialization safeguard (additive, fold into charter not gate):** the version-pinning discipline should be enforced at the CL-side `/govern` skill level — when CL takes a governance action that references workspace-Tier-0, the action MUST embed the commit-hash being cited. Without that structural enforcement, refinement #4 is best-intentions discipline only. *This is additive consistent with LD-0025 doctrine — fold into Path B materialization charter, don't re-open the path-class question.*

**Sharpest-test-bind on C-trigger criteria #2 ("ajb_workspace lifecycle event"):** "lifecycle event" is the only one of four triggers without explicit definitional precision. The other three are concretely testable. #2 examples that SHOULD trigger: ajb_workspace rename, archival, repository transfer to different GitHub org, fork-and-cutover. Examples that probably SHOULDN'T trigger: branch rename, default-branch switch, CI/CD provider change. **This is the one place I'd ask CTO to fold a definitional precision** — not a counter, an ADDITIVE constraint.

**NOVEL: GREEN with ADDITIVE on trigger #2**

### META

**Architectural fit:** Path B is the right starting position for a system whose cross-fabric coupling is currently 2-node (ajb + clb) with the principal as the binding force. Conditional escalation to Path C on empirical triggers is the textbook "wait for evidence" pattern that defers infrastructure cost until the dual-fabric stress is real, not anticipated.

**Reversibility ordering:**
- **B → C** (forward direction): forward-extensible. When triggers fire, separating to `opal-governance` is a defined migration with clear cutover semantics.
- **B → A** (degenerate fallback): possible but never desired; A is rejected on substantive grounds.
- **C → B** (rollback if C proves wrong): possible — collapse `opal-governance` back to ws-canonical. Some history-rewrite cost but recoverable.
- **A → B**: requires re-architecture from coupled-but-implicit to canonical-with-cites; expensive in cultural retraining.

Path B has the **best reversibility position** of the three starting points. PASS.

**Cross-fabric framework empirical signal:** LD-0031 is **the first inaugural cross-fabric architectural call invoking LD-0022 priority-corroborator chain**. This validates the LD-0022 framework reaching cross-fabric scope as designed — a positive empirical signal banked for future ratification of the framework itself ([[project_cvo_priority_architectural_corroborator]] reinforcement). The mechanism is working; the chain held.

**META: GREEN**

---

## ADDITIVE for materialization charter

**FN-1 (definitional precision on C-trigger #2):** when fabric-shared Tier-0 doctrine is materialized, "ajb_workspace lifecycle event" should be enumerated with examples (rename/archival/transfer/fork-and-cutover IN; branch-rename/CI-switch/default-branch-flip OUT). Avoid relying on interpretation when the trigger fires — at that moment, ambiguity would compound stress.

**M-1 (structural enforcement of refinement #4):** CL-side `/govern` skill (or whichever skill owns Tier-0 cite generation on CL) should structurally embed the workspace-Tier-0 commit-hash being cited at action-emit time. Without structural enforcement, version-pinning is cultural-only and Path B leakage is invisible. *This is additive to CTO refinement #4 — same direction, structural-vs-cultural distinction.*

Both fold into materialization charter per LD-0025 doctrine — not gates that re-open the path-class question.

---

## Verdict summary

**CORROBORATE Path B immediate → Path C on triggers; Path A REJECTED.** GREEN at MECHANICAL/NOVEL/META layers. FN-1 (trigger-#2 enumeration) + M-1 (structural cite-discipline enforcement) additive, fold into materialization. No counter on path-class. No self-validation surface.

LD-0022 priority-corroborator framework empirically validated cross-fabric on this inaugural call. Banking as positive framework-signal.

Routing to MSTR via MCP + CC CTO.

— 3.0.0_SA_CVO
