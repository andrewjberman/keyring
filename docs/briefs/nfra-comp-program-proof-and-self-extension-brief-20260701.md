# NFRA_COMP* — Program-Proof & Self-Extension Brief

**Does the shared-cognition substrate we built actually WORK on real problems — and can it grow itself?**

- **Type:** validation + bounded R&D charter (candidate macro name: `NFRA_COMPPROOF`; CTO decides macro-structure — may split a validation macro from a COMPLEARN self-extension sub)
- **Origin:** Andrew-direct 2026-07-01 (live session with MSTR, after the program-assessment + /draw). Verbatim intent:
  *"I want to spot check random /seams and processes and make sure it all actually works. Maybe you can write a
  brief for CTO to decompose which is basically like every nasty bug we ever had, maybe starting with ADVI_BREAKS
  and see if agents could solve it via graph traversal. also want to assess if the COMPROUTER actually works well.
  Also want to assess how COMPLEARNS actually learns on an autonomous basis; maybe would be cool to expand
  something here to assess if the tool could build its own comp-tools based on logged agent tool use over time."*
- **Author:** 0.0.0_AB_MSTR (scope + charter) | **Issued to:** 1.0.0_SA_CTO (PRD/decomposition + arch-gates)
- **Ledger:** LD-0234 (`directive_decomposition`, D-001 PHASE-2 + D-002; mandate_distance 1; S2; reversible)
- **Status:** brief -> CTO decompose. Do NOT preempt the live gate-lift wave; Workstreams B/C/D1 run concurrently on LIVE artifacts, A rides the wave-close.

---

## 0. The thesis — this is the PHASE-2 meta-test, pointed at the program itself

D-001 PHASE 2 says a mechanically-functional output that fails its holistic purpose is **not** a success — it is a
finding. We have built a large graph-substrate + comp-tool program (COMPUNIFY map, the four-peer FIRES/DECIDES/MAPS/
TRAINS contract, COMPDRIFT, the GLOBGRPH substrate, GRAPHDEPTH/GRAPHUNI coordinates). The single question that
governs whether any of it counts: **when a real problem walks in the door, does the substrate actually solve it —
and does the loop that is supposed to make it smarter actually make it smarter, on its own?**

Andrew's four asks are four facets of that one question, and they compose non-redundantly. The load-bearing spine is
**Workstream B — the incident-regression benchmark** ("every nasty bug we ever had"). B is simultaneously the
validation (does the graph solve real problems?), the COMPROUTE eval's intent-set (C), and the COMPLEARN
gap-feed / training corpus (D). A is the breadth sweep that keeps B honest. Build B first; C and D hang off it.

**Anti-drift self-consistency:** this validation harness must itself obey the program's own disjoint-verb, single-owner
discipline — it gets ONE home and ONE owner, not a scatter of one-off scripts. The thing that proves the anti-drift
program must not itself drift.

---

## Workstream A — Seam + process spot-check sweep (the breadth check)

**Objective.** Random-sample real `/seams` and end-to-end processes across the COMP* program AND the live estate,
and confirm they actually carry the right thing — grounded on the DEPLOYED/SERVED/LIVE artifact, never self-report
or the PRD `Status:` line. This is the "is the wave that says DONE actually done" check.

**Scope (IN).** (i) A randomized sample (not a hand-picked happy-path set) of seams across the three axes —
MECHANICAL (does the connection physically carry the flow), DECLARATIVE (does the record/name/status match
implementation reality), SEMANTIC (is the payload the correct content w/ validated quality). (ii) A sample of
whole processes (a scheduled pipeline tick, a comp-tool invocation chain, a served-artifact refresh) exercised
end-to-end. (iii) Special attention to the just-closed / closing wave (COMPUNIFY V1, COMPDIFF, the COMPDRIFT/
COMPLEARN/COMPROUTE hot lanes) — verify the certifications hold on the live artifact.

**Deliverable.** A spot-check ledger: per-target three-axis verdict + the knowledge-parity delta (believed vs true) +
residual unknowns. Every FAIL charted to a fix (not merely logged).

**Suggested owner (CTO decides).** CVO primary (`/seams` + verify-channel is CVO's discipline); COO~B coordinates
the sample scope over the COMP* surface.

---

## Workstream B — The incident-regression graph-solvability benchmark (THE SPINE)

**Objective.** Catalog the real nasty incidents this estate has actually suffered, and for each run the counterfactual:
**starting only from the symptom as it first appeared, could an agent reach the true root cause TODAY via graph
traversal + comp-tools?** Score coverage. Every miss is a coverage gap that feeds Workstream D.

**This is the COMP_LEARNS thesis pointed inward** — measure whether structured compiler/graph assistance changes
what an agent can solve on hard, real engineering failures. Reuse that program's measurement methodology where it fits.

**Scope (IN).**
1. **Build the corpus from the REAL record — do NOT invent incidents.** Mine: `git log -p CLAUDE.md` (every NEVER-rule
   cites an incident), the memory audit-discipline classes (Diagnostic-patterns/Verification-adjudication/
   Constraint-diagnosis), the NFRA_DEBTSCAN scan-family anchors (each anchored to a real incident), the program-origin
   briefs (COMPDIFF=frozen-but-fresh 3x 06-29; GCONTR=BMKAUD SmartX semantic-break 06-01; COMPRAIL=phantom-Deny +
   SNS-publish-not-delivers 06-18), the change-management ledger, and the RV records. **Start with ADVI_BREAKS** (the
   inf-AUA freeze / 49F / Cottonwood cluster) per Andrew.
2. **Per-incident schema:** `symptom_as_first_seen` | `true_root_cause` | `how_it_was_actually_found` (by-eye /
   manual-after-N-hours / which agent) | `graph_traversal_test` | `verdict` | `gap`.
3. **The test must be BLIND.** The solving agent is given ONLY the symptom + the comp-tools/graph — it must NOT know
   the answer (sharpest-test-binds; verifier != doer). A fresh spawned agent per incident is the clean design.
4. **Verdict per incident:** SOLVED (graph reaches root cause) / PARTIAL (narrows but does not close) / MISS (graph
   cannot — a coverage gap). Score the aggregate coverage %.
5. **Every MISS/PARTIAL becomes a filed charter** — a graph-enrichment or a new comp-tool (this is the roadmap
   generator, and the input to Workstream D).

**Deliverable.** (a) The incident catalog + per-incident blind-run results + aggregate coverage score; (b) a STANDING,
re-runnable harness (a regression suite — so "can the graph still solve the classic failures" becomes a repeatable
gate, not a one-time study); (c) the gap-charter list.

**Suggested owner (CTO decides).** CTO architects the harness; DS/AE build it; CVO scores the blind-runs (independent);
blind-solver agents spawned fresh (MSTR spawn-executor on COO request).

---

## Workstream C — Does COMPROUTE actually route well? (efficacy eval)

**Objective.** Empirically evaluate the DECIDES engine: given a real intent, does the posterior
(`score = query + surface_prior + history_affinity`, margin gate, PRIOR-not-FILTER) pick the tool an expert would use
/ the tool that actually solves it?

**Scope (IN).** (i) A labeled intent-set drawn from Workstream B's incidents + the LIVE `comp-which-rail.log` +
`agent_telemetry/*.jsonl`. (ii) Metrics: precision@1 and recall of the top pick vs the correct lens; margin-gate
calibration (does it abstain when it should?); cold-start behavior; and exercise of the two named failure modes in
the COMPROUTE PRD. (iii) A verdict: routes well / needs tuning / structurally short of its claim.

**Deliverable.** The eval harness + the scored report + a tuning charter if warranted. **CVO owns the honesty gate**
(the Goodhart guard — the eval must not be graded on data the router was fit on).

**Suggested owner (CTO decides).** COMPROUTE lane (AE `~E`, posterior owner) builds the eval; CVO honesty-gate.

---

## Workstream D — How does COMPLEARN actually learn, autonomously — and can it build its OWN tools?

**D1 — Autonomy audit (verify-channel, grounded).** Is the self-learning loop REAL, or a dead ratchet (it reclaimed
the dead `comp-learns-run/status` shims — the risk is it reclaimed the corpse too)? Ground against LIVE artifacts,
not the PRD: did the scheduled `EventBridge -> Fargate` refresh actually RUN; did it produce fresh `tool_activity`;
did `gap_heat` update; and did any of that **demonstrably change routing or agent behavior** on a subsequent cycle?
Verdict: learns / accumulates-but-inert / not-running — with the run-artifact evidence.

**D2 — The self-extending-toolchain spike (the R&D frontier Andrew flagged).** A BOUNDED, hypothesis-driven spike:
given the `tool_activity` corpus, can the loop **detect a recurring multi-tool SEQUENCE or a high-`gap_heat` intent
with no covering tool, and auto-PROPOSE (then eventually SCAFFOLD) a new comp-tool** for it? This is "a compiler that
writes compilers from its own usage."
- **Framed as a spike, not a build:** explicit hypothesis + kill criteria + time-box. The D-002 META guard binds — the
  test is whether it proposes tools that tie to REAL demand, not plausible-looking noise.
- **Proof-of-concept bar:** >=1 concrete auto-proposed comp-tool spec derived from real logged usage, as a demonstration
  — **proposed, not deployed.**
- **Hard boundary (see Boundaries):** NO auto-merge of machine-synthesized tools into the estate. A proposed tool is a
  candidate that enters the normal comp-dev review + CVO gate like any human-authored one.

**Suggested owner (CTO decides).** D1 = CVO (verify-channel on the live loop). D2 = a DE/DS spike under CTO. **Routing
flag for Andrew:** D2 IS the dormant COMP_LEARNS thesis (self-improving compiler apparatus) pointed inward at Opal's
own tool-use — it may warrant partial re-activation of the CL fabric (feature_clb), which is a **sovereign call
(CL re-activation, RV-0026 F-002)**. Surfaced as an option; not decided here.

---

## Cross-cutting boundaries (the leash)

- **Validation + bounded spike only.** This charter authorizes measurement and a proof-of-concept spike. It does NOT
  authorize deploying machine-synthesized tools, nor any S3 act (procurement/prod-mutation/destructive) — those
  surface separately.
- **No auto-merge of AI-written tools.** Any COMPLEARN-proposed tool goes through the standard comp-dev review + CVO
  gate before it is real. The loop proposes; humans+CVO ratify.
- **Ground on LIVE/served, never self-report or PRD `Status:`.** This is the PHASE-2 discipline; a "could-not-verify"
  is itself a finding.
- **Blind-solver discipline.** The B counterfactual agent must not know the answer, or it is not a test.
- **Do not invent incidents.** Mine the real record; a fabricated bug corrupts the benchmark.
- **Do not preempt the live wave.** B/C/D1 run concurrently on live artifacts; A rides the wave-close. GRAPHDEPTH keeps
  its foundational precedence.
- **Self-consistency.** The harness gets one owner + one home (anti-drift disjoint-verb discipline applies to the
  validator too).

## Sequencing

`B` first (it seeds C's intent-set and D's gap-feed). `A`, `C`, `D1` run concurrently on live artifacts. `D2` is gated
behind `D1` — confirm the loop learns AT ALL before extending it to synthesize. All four report into one program ledger.

## Acceptance criteria (machine-checkable-ish; CTO firms in decomposition)

- **A:** >=N seams + >=M processes spot-checked with per-axis verdicts grounded on live artifacts; 100% of FAILs charted.
- **B:** corpus of >=K real incidents on the 5-field schema; each blind-tested; an aggregate coverage score
  (SOLVED/PARTIAL/MISS %); 100% of MISS/PARTIAL -> a filed gap/tool charter; a standing re-runnable regression harness.
- **C:** COMPROUTE precision@1 + recall on a labeled set >=Y; margin-gate + cold-start + the 2 PRD failure modes
  characterized; CVO honesty-gate signed; an explicit routes-well/needs-tuning verdict.
- **D1:** autonomy verdict grounded on live run-artifacts (ran / refreshed / changed-behavior — yes/no + evidence).
- **D2:** spike report with a go/no-go on tool-synthesis feasibility + >=1 concrete auto-proposed comp-tool spec
  (proposed, not deployed) + kill-criteria assessment.

## CTO decomposition handoff

CTO owns: whether this is one macro (`NFRA_COMPPROOF`) or a validation macro + a COMPLEARN self-extension sub; the PRD;
the arch-gates; the TO decomposition + lane assignment (with COO), each TO carrying its `<compiler_tools_mandate>`,
`<cross_domain_coordination>`, and machine-checkable `<acceptance_criteria>`. Push back on any workstream on operational
grounds — MSTR sets the what + why + the leash; CTO informs the whether + how.
