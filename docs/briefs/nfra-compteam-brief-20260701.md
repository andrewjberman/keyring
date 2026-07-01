# NFRA_COMPTEAM — Macro-Project Brief (MSTR charter → CTO PRD)

**Onboard the team to the MCP server + a deployment strategy: distribute working agents, and give them partitioned read-access to portal data.**

- **Type:** macro_project (`NFRA_COMPTEAM`) — productization / distribution of the comp-tool + agent-org stack.
- **Origin:** Andrew-direct 2026-07-01 (live session with MSTR). Verbatim intent:
  *"we need to now get the team onboarded to the MCP server and we need to implement a deployment strategy to
  this end. What I think it should be is using the agent_blueprint v1 folder on desktop, just updating that with
  all our new developments, claude.md, harness mechanics for comp-which and ranking system however we implemented
  it here, etc. (no git functions needed). That aspect is how they will have agents. Then there is the aspect of
  how to create partitioned read areas via kuzu/nessie/iceberg so that can get information. I think its really
  just a function of exploring TSGRAPH and figuring out the key portal surfaces so that they can cleanly pull any
  data displaying on the portal in obvious panel clusters."*
- **Author:** 0.0.0_AB_MSTR (scope + charter) | **Issued to:** 1.0.0_SA_CTO (PRD authoring + arch-gates + decomposition)
- **Ledger:** LD-0237 (`andrew_instruction`; S2; reversible)
- **Status:** brief → CTO PRD (`docs/architecture/NFRA_COMPTEAM_PRD.md`). Register the macro on PRD landing.

---

## The thesis

We have built the comp-tool + agent-org stack for ourselves. NFRA_COMPTEAM **packages it for the team** — two
distinct deliverables that together let a teammate stand up a working agent AND have it pull real portal data:

1. **How they get AGENTS** — a refreshed, self-contained distribution kit (the `agent_org_blueprint_v1` folder),
   updated with everything we've developed since it was last cut.
2. **How they get INFORMATION** — partitioned, scoped read-areas over the kuzu/nessie/iceberg graph substrate, so a
   teammate's agent can cleanly pull the data that's displayed on the portal, organized by the portal's own panel
   clusters.

---

## Component A — the agent distribution kit (refresh `agent_org_blueprint_v1`)

**Objective.** Update the existing kit on Desktop — `agent_org_blueprint_v1_src/` (+ `agent_org_blueprint_v1.zip`;
ship-source memory `reference_agent_org_blueprint_kit_source_and_ship`) — with all developments since it was last
cut, so a teammate can unzip it and have a working, current agent. **This is the "how they have agents" half.**

**Scope (IN) — refresh with our new developments:**
- **CLAUDE.md** — the current operating law (adapted for a fresh team — strip Opal-internal incident history that
  doesn't transfer; keep the rules + gates that make an agent behave).
- **comp-which RAIL harness mechanics** — the comp-which-first rail (NFRA_COMPRAIL) + the on-rails
  comp-grep/comp-glob primitives + the PreToolUse HUD nudge — how an agent is routed to the right tool.
- **The RANKING system, however we implemented it here** — the COMPROUTE posterior router (score = query +
  surface_prior + history_affinity), the COMPUNIFY coverage map (the prior), and the COMPLEARN learned signal — the
  DECIDES engine + its map. Package whatever of this transfers as a working router for a teammate.
- Any harness/hook/skill scaffolding the kit needs to be a runnable agent out of the box.
- **NO git functions needed** (Andrew-direct) — the distributed kit does NOT carry our git/deploy/safe-commit
  machinery. It is a READ/REASON agent kit, not a commit/deploy one. (Aligns with Component B: read-only.)

**Deliverable.** A refreshed, self-contained, versioned kit (a new `agent_org_blueprint_vN`) that a teammate unzips
→ registers to the MCP server → has a current, correctly-railed, correctly-routing agent, with NO git surface.

## Component B — partitioned read-areas over the graph (how they get information)

**Objective.** Create **partitioned, scoped read-areas** via kuzu / nessie / iceberg so a teammate's agent can pull
information — specifically, **the data displayed on the portal**, cleanly, organized by the portal's own panel
clusters. **This is the "how they get information" half.**

**Andrew's framing (the load-bearing insight):** this is *really* a function of **exploring TSGRAPH and figuring out
the key portal surfaces** — so that a teammate can cleanly pull *any data displaying on the portal*, organized in
**obvious panel clusters.**

**Scope (IN):**
- **Leverage NFRA_TSGRAPH** (the intra-TypeScript semantic graph; `org/modules/graph/tsgraph_spike/`) — it already
  models the portal at component/field grain AND the **PanelCluster** community-detection groupings (the `CLUSTERS` +
  `SHARES_SOURCE` edges, the bipartite component↔data-source graph). The "obvious panel clusters" Andrew wants ARE
  TSGRAPH's PanelCluster nodes. Use it to enumerate the key portal surfaces + their backing data sources.
- **Map each portal panel cluster → its served data source** (the SERVED_FROM fine-lineage: served-field → fetch →
  adapter → hook → prop → JSX-render, back to the gold/platinum artifact). This is what lets a teammate say "give me
  the data behind the X panel" and get a clean pull.
- **Partition the read-area** — scoped read-partitions on the kuzu/nessie/iceberg substrate so a teammate's agent
  reads ONLY its allowed slice (per-team / per-surface). This is a scoped-read design (multi-consumer read isolation
  over the shared graph) — coordinate with the SCTY program on the access-scoping model (this is a read partition,
  not a write path).

**Deliverable.** A partitioned read-access design + the portal-surface → data-source map (grounded in TSGRAPH), so a
teammate's kit-agent pulls portal-displayed data by panel cluster, read-only, within its partition.

---

## Constraints / boundaries (the leash)

- **Read-only + no-git distribution** — the kit carries NO git/deploy/commit functions (Andrew-direct); the read-areas
  are READ partitions, not write paths. A distributed agent cannot mutate our estate.
- **Scoped/partitioned access is a security surface** — the read-partitioning intersects SCTY (the onboarding-guardrails
  program). Coordinate the access-scoping model with SCTY; do not ship an unscoped read.
- **Strip non-transferable internals from the kit** — Opal-specific incident history / firm-internal specifics that
  don't generalize to a fresh team; keep the transferable rules + harness.
- **Grounding** — the portal-surface map is grounded against TSGRAPH + the live served artifacts, not assumed.

## CTO decomposition handoff

CTO owns: the PRD (`docs/architecture/NFRA_COMPTEAM_PRD.md`); whether this is one macro with two components (A: kit
refresh, B: partitioned read-areas) or a macro + sub; the arch-gates; the TO decomposition + lanes with COO (kit
refresh likely AE/DE; the TSGRAPH portal-surface map + read-partition design likely DE + AE-graph, with SCTY
coordination on scoping). Each TO carries its `<compiler_tools_mandate>`, `<cross_domain_coordination>` (TSGRAPH,
GLOBGRPH, SCTY are the obvious cross-domain touchpoints), and machine-checkable `<acceptance_criteria>`. Push back on
either component on operational grounds — MSTR sets the what + why + leash; CTO informs the whether + how.
