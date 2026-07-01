# NFRA_COMPROUTE — The Router as a First-Class Project (Brief)

**Author:** 0.0.0_AB_MSTR (Tier-0, MSTR)
**Date:** 2026-07-01
**Authority:** Andrew-direct (MSTR session 2026-07-01): "let's get serious, where is the generalizable systems alpha here — we should have an NFRA project devoted to the more comprehensive approach we discussed an hour ago." Elevates the LD-0231 / COMPLEARN §4a router fold to a standalone project. Commission ledgered LD-0232.
**Issued to:** 1.0.0_SA_CTO — author the NFRA_COMPROUTE PRD + arch-gate + stand up the project. COO~B coordinates.
**Relationship:** ELEVATES LD-0231 (the §4a posterior fold). The §4a spec is CORRECT and PRESERVED — re-homed from COMPLEARN into this project. Nothing built is wasted.

> One-line: the fabric's **intent -> capability router** — its single highest-frequency cognitive
> junction — becomes a first-class, self-improving, surface-aware **posterior decision engine**, not a
> curated-rule patch and not a COMPLEARN tenant. comp-which is its surface; COMPRAIL fires it;
> COMPUNIFY feeds it the prior; COMPLEARN trains it. The engine generalizes past comp-tools to ANY
> intent->capability match — up to routing WORK to the right agent/lane.

---

## 1. The gap — the true router has no home

comp-which is the router's **surface**, not the router. The routing DECISION today is scattered across
three places, owned by no one:
- the curated `RULES` inside `.tools/comp-which`,
- the fuzzy backstop in `graph-call-manifest.yaml`,
- (as of LD-0231, an hour ago) a **§4a tenant inside NFRA_COMPLEARN**.

No NFRA project OWNS the decision engine. That homelessness is the gap. The DE's comp-drift / comp-cluster
curated fixes (LD-0231 #1 live, #2 pending) are correct but **O(1) one-offs** — patches to specific
mis-routes. The generalizable alpha is the ENGINE, and it needs a first-class home.

**MSTR correction owned:** LD-0231 framed the router as "a delta to COMPLEARN, not a new project" to
avoid project proliferation. That optimized for fewer-projects over correct-decomposition. The router is
a DISTINCT capability (the decision layer) — a peer to the map (COMPUNIFY) and the learning loop
(COMPLEARN), not a tenant of either. Elevating it is the LESS-drift choice: one clear owner instead of a
§4a sub-feature.

## 2. The systems alpha — why a PROJECT, not a fold

**Routing is the fabric's attention-allocation problem.** Every agent, constantly — the PreToolUse HUD
fires the router **ambiently ~639x / 14d** (agents type it explicitly only 3x, LD-0224) — must decide
"which capability do I reach for RIGHT NOW, given what I'm trying to do and where I am." Today that
decision is **context-blind and non-learning** (agent memory / a static curated rule / a fuzzy string
match). The alpha is turning it into a **learned, context-conditioned POSTERIOR that improves from the
fabric's own behavior.** Four leverage properties a curated rule can never have:

1. **Highest-frequency cognitive junction.** Every agent, every session, ~639x/14d ambiently. A small
   routing-accuracy gain COMPOUNDS across the whole fabric — leverage no single tool has.
2. **Generalizes beyond comp-tools.** The same engine (`prior x likelihood x learned + margin`) routes
   ANY intent -> capability: comp-tools today, but also **skills, MCP tools, docs/PRDs**, and ultimately
   **which AGENT / LANE a TO belongs to.** It is the fabric's intent->capability matcher, not a comp-tool
   feature.
3. **Self-improving flywheel.** It reads COMPLEARN's `tool_activity`; every margin-gate disambiguation is
   a labeled example -> more use -> better routing -> more use. **O(compounding)** vs the O(1), decaying,
   hand-authored curated rule.
4. **Context-as-prior.** Role, working-set, session-trajectory as priors — situational-awareness ->
   capability selection. The fabric develops a **shared, improving sense of where to look.**

That is a cognitive substrate, not a tool feature. It earns its own project.

## 3. The engine — re-homed from LD-0231 §4a (preserved, not re-derived)

The posterior spec authored in COMPLEARN §4a (CTO, c15aad2d9) is CORRECT and is re-homed here verbatim:
```
score(tool | intent) = w_q * query_match(tool, intent)
                     + w_s * surface_prior(tool.surface, ctx)      # ctx = {role, working-set, trajectory}
                     + w_h * history_affinity(tool, role, ctx)     # from COMPLEARN tool_activity
```
- **Margin gate:** (s1 - s2) >= epsilon -> route confident; < epsilon -> surface BOTH with their
  coverage-map `concern` + grain, never silent-argmax.
- **PRIOR-not-FILTER:** surface_prior is additive (a boost, never a hard filter) -> cross-surface tools
  stay reachable.
- **Cold-start-safe:** empty affinity -> score = query + prior, degrades to today + prior + margin (still
  an upgrade); the learned term accretes.
- **Value-anchored (Goodhart-honest):** history_affinity weighted by OUTCOME (rail-escape-reduction),
  never usage-count. CVO verifies.
Full spec + the two-failure-mode design validation: LD-0231 + NFRA_COMPLEARN §4a (to be moved to the
NFRA_COMPROUTE PRD).

## 4. Clean architecture — four peers, no meta-drift

| Project | Owns | The question it answers |
|---|---|---|
| **NFRA_COMPRAIL** / TOOLHUD | the reflex + HUD + gate that FIRES the router | **WHEN** to route + enforce |
| **NFRA_COMPROUTE** (new) | the posterior decision engine — **the true router** | **HOW** to route |
| **NFRA_COMPUNIFY** | the one-home capability map (the prior source) | **WHAT** exists to route to |
| **NFRA_COMPLEARN** | `tool_activity` + the affinity training signal | **LEARN** to route better |

COMPROUTE **consumes** COMPUNIFY (the prior) + COMPLEARN (the learned term) and is **fired** by
COMPRAIL/TOOLHUD. comp-which is COMPROUTE's first CLI surface. This is **orthogonal decomposition of a
distinct capability**, not the redundant-parallel-structure meta-drift COMPUNIFY guards against (two
gates / two maps). The four verbs are disjoint: fire / decide / map / learn.

## 5. Relationship to LD-0231 / COMPLEARN §4a — elevation, not waste

- The §4a posterior spec is **re-homed** from COMPLEARN into the NFRA_COMPROUTE PRD (it is the router's
  core spec; it was in the wrong container).
- **COMPLEARN's role narrows cleanly** to the **training-signal provider**: it owns `tool_activity` + the
  affinity table + the tool build/optimize/retire ratchet, and it FEEDS COMPROUTE the learned term. It no
  longer "contains" the router.
- The DE's LD-0231 curated fixes (comp-drift live @ 9fe941ef8; comp-cluster pending the engine-home
  ruling) become **COMPROUTE's cold-start priors** — the O(1) patches sit UNDER the O(compounding)
  engine, exactly where they belong.
- The authoring-vs-landing ruling (LD-0231 §9, CTO-ruled: lane-portable read-side + governor
  registration) applies directly — COMPROUTE's engine is read-side cognition, lane-portable by the same
  ruling.

## 6. The generalization roadmap — the alpha realized in stages (CTO scopes phasing)

- **Stage 1 — comp-tool posterior (near-term, off the live substrate).** comp-which becomes the posterior
  router (the §4a engine): surface-prior + margin off the live COMPUNIFY map + rail-log; learned affinity
  off ~E's live `tool_activity`. This is the immediate, shippable payoff.
- **Stage 2 — cross-capability.** Extend the intent->capability matcher beyond comp-tools to **skills +
  MCP tools + docs/PRDs** (route "how do I X" to the right skill/doc, not only the right comp-tool). Same
  engine, a broader capability-map.
- **Stage 3 — routing WORK (the highest-value generalization).** Route a TO / intent to the right
  **AGENT / LANE** — the same posterior over the ORG capability-map (who owns what). **Dispatch becomes
  learned, not hand-mapped.** This is where the router stops being a comp-tool convenience and becomes
  fabric-organizational alpha.

The engine must be built **capability-map-agnostic** from Stage 1 so Stages 2-3 are a new map + new
training data, NOT a re-architecture.

## 7. Asks to CTO

1. **Author the NFRA_COMPROUTE PRD** + arch-gate; stand up the project (`org/projects/NFRA_COMPROUTE.json`
   + REGISTRY row).
2. **Re-home the LD-0231 §4a posterior spec** from the COMPLEARN PRD into COMPROUTE; **narrow COMPLEARN
   §4a** to "provides the training signal (tool_activity + affinity) to COMPROUTE."
3. **Own the engine design** — the posterior + margin gate + the **generalization interface**
   (intent->capability, capability-map-agnostic so it extends to skills/MCP/docs/agents without a
   re-architecture).
4. **The four-way separation** (COMPRAIL fires / COMPROUTE decides / COMPUNIFY maps / COMPLEARN trains) as
   the explicit anti-meta-drift contract in the PRD.
5. **Sequence:** Stage 1 (comp-tool posterior) near-term off the live substrate; Stages 2-3 (cross-
   capability, agent/lane routing) as the roadmap — the engine capability-map-agnostic from day one.

## 8. Lane / governance

- **MSTR** (this brief + LD-0232, elevating LD-0231) scopes + commissions; does not author the PRD.
- **CTO** (`1.0.0_SA_CTO`) authors the NFRA_COMPROUTE PRD + arch-gate + project stand-up; owns the engine
  + generalization-interface design.
- **COO~B** (`2.0.0_SA_COO~B`) coordinates — already on the comp-program; sequences COMPROUTE against the
  live substrate (Stage 1 off ~E's tool_activity) + the DE's comp-cluster reshape.
- **CVO** (`3.0.0_SA_CVO`) — Goodhart-honesty + routing-quality ground-truth (does a disambiguation
  actually reduce the mis-route rate).
- **~C** (`0.8.0_AE_CloudComp~C`, COMPUNIFY governor) — the role->surface prior map hook.
- **~E** (`0.8.0_AE_CloudComp~E`, COMPLEARN) — the `tool_activity` + affinity training signal COMPROUTE
  consumes.
- **DE** (`0.4.0_DE_ClientPlatform`) — comp-which as COMPROUTE's first surface; the curated fixes are its
  cold-start priors.
