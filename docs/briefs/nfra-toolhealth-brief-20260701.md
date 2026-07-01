# NFRA_TOOLHEALTH — Brief (MSTR charter → CTO PRD)

**Assess from real agentOps whether comp-tools are used CONSISTENTLY + CORRECTLY, as a queryable, closed learning loop.**

- **Type:** project (candidate `NFRA_TOOLHEALTH`; CTO names/scopes) — an observability + learning-loop layer; extends NFRA_COMPLEARN.
- **Origin:** Andrew-direct 2026-07-01 (discussion w/ MSTR). Verbatim intent: *"now that we have the comp-tools fairly hammered in, how can we assess from real-life agentOps that they are being used consistently and correctly? Is that being tracked with a mechanism that is easily queryable for an effective learning loop?"*
- **Author:** 0.0.0_AB_MSTR (scope) | **Issued to:** 1.0.0_SA_CTO (PRD + decomposition)
- **Ledger:** LD-0239 (`andrew_instruction`; S2; reversible) | **Status:** brief → CTO PRD.

## The premise + the grounded starting point (real, live — verified 2026-07-01)

We have the raw telemetry; we lack a fused, closed loop. Four live streams already exist:
- `org/compiler-tools-log.md` (12.4k lines, live) — every comp-tool run (tool/result/TO/agent) → **VOLUME**.
- `org/mcp/comp-which-rail.log` (3.3k lines, live) — rail route-vs-run + every `# rail-checked` override → **CONSISTENCY** (comp-tool vs raw-grep/aws bypass rate).
- `org/mcp/comproute-routing.jsonl` (622 lines) — the router's tool pick per query → **CORRECT ROUTING**.
- `org/mcp/agent_telemetry/*.jsonl` (69 files) — PostToolUse work stream, archetype-tagged → **SHAPE/COST**.
- These federate into Trino as the `tool_activity` catalog (COMPLEARN P0–P1); `org/modules/graph/comp_learns_score.py` = the value-anchored scorer (scores VALUE not usage; 241 inversions caught).

## What to build — the "comp-tool health" fused view + the closed loop

**Objective.** A single, queryable **per-tool health view** fusing the three axes, and closing the loop so the signal drives action:
1. **USED** — from `compiler-tools-log` (frequency, recency, by whom).
2. **RAIL-PREFERRED-OVER-RAW (consistency)** — from `comp-which-rail.log` (chosen vs. bypassed to raw grep/aws; every override is already logged).
3. **EFFECTIVE (correctness)** — is running the tool actually *reaching the answer*? This is what **NFRA_COMPPROOF** measures (blind-run: 5/6). Fold COMPPROOF in as the **recurring effectiveness probe** per tool/class.

**The output per tool → an action:** used+effective (KEEP) · used-but-ineffective (FIX) · effective-but-ignored (PROMOTE/surface) · dead (RETIRE).

**Close the loop (the load-bearing part).** Today the loop is `ACCUMULATES-BUT-INERT` (COMPLEARN D1): data collected + queryable, but not autonomously consumed-and-improved (needs the 2-stage close — DRV default-router flip [DONE] + affinity `w_h` activation [data-accruing]). This project's job is to make the fused health view **drive** the retire/fix/promote decisions, not just display them.

## Scope / boundaries
- IN: the fused per-tool health query (over the existing Trino `tool_activity` + rail-log + routing.jsonl + a COMPPROOF effectiveness feed); the action-classification rubric; the close-the-loop wiring into COMPLEARN's consume side.
- Extends COMPLEARN (don't rebuild the telemetry — REUSE it); uses COMPPROOF as the recurring effectiveness probe (don't re-invent blind-run).
- OUT: new telemetry collection (the streams exist); MSTR editing code (charter-through-Tier-1).
- Grounding: the health view grounds on the live logs/Trino, not assumed.

## CTO handoff
CTO owns the PRD, whether this is a COMPLEARN workstream or its own project, arch-gates, lanes (DE/AE-graph + CVO for the effectiveness-probe honesty). Push back on operational grounds. The high-value acceptance criterion: one query answers "which comp-tools are used, correctly-routed-to, AND actually effective — and which are ignored/misrouted/dead," and the loop acts on it.
