# TASK ORDER (FENCED) -- NFRA_COMPPROOF.D2 (self-extending toolchain spike)

<issued_to>0.4.0_DE_ClientPlatform (spike lead) under 1.0.0_SA_CTO</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<status>FENCED / HELD -- gated behind D1-GREEN. Do NOT dispatch or start until TO-D1 (CVO~B autonomy audit) returns a LEARNS verdict. If D1 = accumulates-but-inert / not-running, D2 stays fenced (fix COMPLEARN first).</status>
<priority>BOUNDED R&D SPIKE -- sovereign implications; fenced. PRD SS2-D2/SS3-leash/SS6.</priority>
<date>2026-07-01</date>

## Context
COMPPROOF-D2: the qualitatively different, sovereign-adjacent workstream -- can COMPLEARN's loop, from the tool_activity corpus, DETECT a recurring multi-tool sequence / high-gap_heat uncovered intent and auto-PROPOSE a new comp-tool spec? This is a bounded, hypothesis-driven spike, NOT a program. FENCED behind D1: confirm the loop LEARNS AT ALL (D1-GREEN) before extending it to synthesize.

## Objective
A go/no-go on tool-synthesis: >= 1 concrete auto-proposed comp-tool spec DERIVED from real logged usage -- **PROPOSED, NOT DEPLOYED** -- with an explicit hypothesis + kill-criteria + time-box.

## Scope (LEASHED)
1. **Mine tool_activity** for a recurring multi-tool SEQUENCE or a high-gap_heat uncovered intent (real logged usage, not invented).
2. **Auto-PROPOSE a spec** for a new comp-tool that would cover it -- a SPEC, not an implementation. >= 1 concrete proposed spec.
3. **THE LEASH (binding, PRD SS3-5):** validation + bounded spike ONLY. NO auto-merge/auto-deploy of any machine-synthesized tool (normal comp-dev review + CVO gate if it ever proceeds). D2's CL-fabric re-activation (RV-0026 F-002) is a SOVEREIGN surface -- SURFACE it to Andrew/MSTR, do NOT self-authorize.
4. **Hypothesis + kill-criteria + time-box:** state the explicit hypothesis, the kill-criteria (what result kills the spike), and a time-box up front.

<compiler_tools_mandate>
  <phase id="1" when="gate-check (before any work)">
    <step><run>confirm TO-D1 returned LEARNS (the loop demonstrably changes behavior on live artifacts). If not GREEN, STOP -- D2 stays fenced.</run>
    <expect>D1-GREEN (learns) is the unfence condition.</expect>
    <if_mismatch>HALT. D2 does not start on an inert/dead loop -- that would synthesize on a foundation that doesn't learn.</if_mismatch></step>
  </phase>
  <phase id="2" when="spike">
    <step><run>mine tool_activity -> propose >= 1 spec; document hypothesis/kill-criteria/time-box; NO deploy; flag the sovereign CL-surface if implicated</run>
    <expect>>= 1 concrete auto-proposed spec (PROPOSED-NOT-DEPLOYED); leash respected; sovereign surface flagged not self-authorized.</expect>
    <if_mismatch>Any auto-deploy / self-authorized CL-reactivation = a leash violation (RED). Propose only.</if_mismatch></step>
  </phase>
</compiler_tools_mandate>

<cross_domain_coordination>
- 1.0.0_SA_CTO: spike lead-of-record (governs the bounded R&D).
- 3.0.0_SA_CVO~B (TO-D1): D1-GREEN is the unfence gate; CVO gates any downstream tool-dev.
- 0.0.0_AB_MSTR / Andrew: the RV-0026 CL-fabric re-activation is a SOVEREIGN surface -- surfaced, never self-authorized.
- 2.0.0_SA_COO~B: I dispatch D2 (unfence) ONLY on D1-GREEN.
</cross_domain_coordination>

<acceptance_criteria>
1. (Gate) started ONLY after D1-GREEN.
2. Spike report + go/no-go on tool-synthesis + >= 1 concrete auto-proposed spec (PROPOSED, NOT DEPLOYED) + kill-criteria assessment.
3. The sovereign CL-surface flag raised (not self-authorized) if CL-re-activation is implicated. RAVC CTO + COO~B.
</acceptance_criteria>

## Note
FENCED for a reason: synthesizing new tools on a loop that doesn't demonstrably learn is building on sand -- D1 first. And the leash is absolute: PROPOSE, never deploy; the CL-fabric surface is Andrew's call, not the spike's.
