# NFRA_COMPLEARN — Macro-Project Brief

**Author:** 0.0.0_AB_MSTR (Tier-0, MSTR)
**Date:** 2026-06-30
**Authority:** Andrew-direct (MSTR session 2026-06-30, live design) + this commission ledgered LD-0225.
**Issued to:** 1.0.0_SA_CTO — for PRD authoring + arch-gate + TO decomposition.
**Status:** Commissioned. CTO stands up the macro-project under its own PRD/arch-gate.

> One-line: reclaim the dormant COMP_LEARNS runtime (`comp-learns-run` / `comp-learns-status`)
> as a **fabric-native, self-learning loop over our own tool-use** — Trino federates agent
> behavior x the cloud estate x git/local heat into one activity tracker, and a scheduled ratchet
> learns **which comp-tools we need most + when, and how to optimize the existing set.**

---

## 1. The problem — we build comp-tools by anecdote, not evidence

We have ~38 comp-tools and a strong doctrine (Rule 21: *"a repeat override for one intent = a
coverage gap -> build the tool"*). But that doctrine is a **manual reflex** — an agent notices it hit
raw grep twice, mentions it in a session log, maybe a tool gets built. We have **no systematic,
evidence-grounded view of**:

- which tools are used most, by whom (role), when (session-phase / time), against what (which estate
  region / firm / pipeline layer);
- where agents **fall back to raw grep/aws** (the rail escapes) — i.e. where a tool is MISSING;
- which tools **underperform** (error, get immediately re-run, return UNVERIFIABLE, dead-end);
- which **archetype clusters** (EXPLORE/DIAGNOSE) cost the most tool-invocations per outcome (the
  COST-leverage question — MSTR stimulus-scan signal class 6, "tooling R&D's highest-leverage target
  is COST not BUGS").

The signal to answer all of this **already exists** — it is just scattered across three logs and
never joined to the estate it operates on. NFRA_COMPLEARN closes that loop.

## 2. The thesis — the fabric studies its own cognition layer

COMP_LEARNS (2026-04, CL fabric, now paused/torn-down per LD-0222) was a measurement substrate for
frontier-model evals: *does a compiler-harness help a model on an external target codebase?* It built
a **ratchet** (iterate -> score -> mutate -> compare-to-champion -> KEEP/DISCARD -> scorecard +
champion + experiment_log) and two entry points — `comp-learns-run` (tick one iteration) and
`comp-learns-status` (observability, Operational-Mandate req #8). Those two `.tools/` shims are now
dead (they point at the decommissioned legacy `comp.framework.{run,status}`; the framework lived in
the CL fabric).

**The reframe (Andrew-direct):** invert the target. The codebase under study becomes **the fabric
itself**; the "models" are our **agents**; the "intervention" is the **comp-tool suite**; and the
ratchet's *champion* stops being a compiler version and becomes the **comp-tool inventory + routing
configuration** (which tools exist, what comp-which routes where, what the HUD nudges, what should be
built/merged/retired). The reclaimed `comp-learns-run`/`comp-learns-status` become the runner +
observability for THIS loop.

## 3. The three-plane federation — Behavior is the missing catalog

Three data planes exist; today only two are federated.

| Plane | Source (live today) | Catalog |
|---|---|---|
| **Estate** | `graph_nodes/edges` (Nessie/Iceberg) — cloud + dependency graph | `iceberg` (LIVE in Trino) |
| **Change** | `code_heat` parquet `{repo,path,heat,head_sha,computed_at}` — git/local write-history | `code_heat` (LIVE in Trino) |
| **Behavior** | **the missing plane** — what agents actually DO | **`tool_activity` (NEW)** |

The Behavior plane is extracted from three existing streams:
- **`org/compiler-tools-log.md`** — `DATE | AGENT | TO_ID | TOOL | COMMAND | RESULT` (the attributed
  tool-use ledger; see Section 6 — the seed corpus).
- **`org/mcp/agent_telemetry/*.jsonl`** — `{ts, agent, tool, kind, session_id}` (the PostToolUse hook
  stream; ALL tools, not just comp; 63 agent files).
- **`org/mcp/comp-which-rail.log`** — `{ts, action, tool, term, matches, files, scanned, path}` — the
  **rail-escape / on-rails-primitive** log = the single richest coverage-gap signal (a `RUN-GREP` with
  no rich-tool hit on a hot path is a tool-demand event).

Land `tool_activity` as an Iceberg/Parquet table in the same warehouse bucket as `code_heat`, bound as
a third Trino catalog. **This single catalog is the whole symbiosis** — once it exists, Trino joins
Behavior x Estate x Change.

## 4. Trino — the join substrate (the activity tracker)

The `globgrph-trino` federation already joins Estate x Change on `(repo,path)`. Adding `tool_activity`
lets Trino answer questions **no single stream can**:

- *"When agents touch hot cot-pipeline files (`code_heat` hot AND `graph_nodes.firm=cot`), which tools
  do they reach for, in what sequence, and where do they fall back to raw grep?"* -> per-context
  tool-demand profile.
- *"Which estate regions have high write-heat but low tool-coverage (many `comp-which-rail` escapes,
  few rich hits)?"* -> **the coverage-gap map = the build-next queue** (Rule 21, automated).
- *"Which archetype clusters cost the most tool-invocations per outcome?"* -> the COST-leverage map.

JOIN keys: `(repo,path)` Behavior<->Change; `target_path -> graph_nodes` Behavior<->Estate;
`firm`/`layer` derived dimensions. This federated view IS "the activity tracker between cloud estate /
git / local directory and daily agent behavior."

## 5. The reclaimed loop — comp-learns-run / comp-learns-status redefined

- **`comp-learns-run`** = tick one iteration of the **toolset-learning** loop. Pull the federated
  activity window from Trino -> compute the scorecard (coverage, cost, hit-rate, gap-set) -> propose
  ONE mutation to the toolset (a new comp-which routing rule, a spec for a missing tool, a merge of two
  redundant tools, a deprecation) -> compare to the reigning champion config -> ratchet KEEP/DISCARD ->
  write `scorecard.json` + `champion.json` + an `experiment_log` row + a ranked
  **build/optimize/retire WORKLIST**.
- **`comp-learns-status`** = what has the loop learned? Current iteration + the live Trino-derived
  dashboard: top demanded-but-missing tools (gap map), top optimize candidates (tools that
  error/re-run/return UNVERIFIABLE), the champion routing config, plateau state. The
  Operational-Mandate-#8 observability surface, repurposed. Reads SERVED state (Section 7); does not
  recompute.

The ratchet machinery (iterate/score/mutate/champion/experiment_log) is reused; only the SCORER and
the MUTATION SPACE change (from compiler-quality -> toolset coverage/cost/value).

## 5a. The routing rules ARE part of the champion + a worked example (Andrew-direct 2026-06-30)

**Scope clarification the PRD must carry:** NFRA_COMPLEARN's mutation space is NOT just "build / merge /
retire tools" — it **includes the comp-which curated routing rules**. A large share of discovery
friction is **Mode-1 routing misses** (a tool EXISTS, the router doesn't connect the agent's phrasing
to it), not missing tools. So the comp-which RULES map is a first-class **champion-config surface** the
loop proposes mutations to — `comp-learns-run` should emit routing-rule changes, not only tool-build
specs.

**LD-0226 is the canonical worked example — a hand-run iteration of exactly this loop**, done
2026-06-30 ahead of the build. The LD-0224 discovery audit found served-content-motion questions had no
route (`header_metrics` raw-grepped 5x in 14d; "no comp-tool reads served content" named 2x), and MSTR
wired a comp-xray curated rule + surfaced comp-freshness's `artifact` mode. **That manual fix IS one
`comp-learns-run` iteration's output**; the loop should propose such routing-rule mutations
automatically, scored: *did the new rule reduce the rail-escape / primitive-fallback rate for that
intent?* Fold LD-0226 into the PRD as the reference iteration + the seed of the routing-rule mutation
space.

**Empirical design input (from the LD-0224 audit — carry into the scorer):** discovery is **AMBIENT,
not invoked** — in the 14d to 2026-06-30 agents *typed* `comp-which` 3 times, but the PreToolUse HUD
fired it **639 times** (ROUTE -> rich tool), against 590 primitive-fallbacks (RUN-GREP/RUN-GLOB) + 158
DENY + 32 rail-checked overrides. So fabric fluency is a function of the **routing rules + the HUD**,
not whether agents remember to ask — and the `comp-which-rail.log` action mix is the primary
routing-quality signal the scorer reads.

## 6. Seed corpus — cold-start from 3 months of history (Andrew refinement #1)

The loop does NOT start cold. We have a deep historical corpus to **backfill** the Behavior plane:
- **`org/compiler-tools-log.md`: 8,600 structured rows spanning 2026-04-09 -> 2026-06-30** (~3 months),
  already in `DATE|AGENT|TO|TOOL|COMMAND|RESULT` form — a direct Phase-0 backfill into `tool_activity`.
- **1,469 session-log markdown files carry a `## Compiler Tools` section** (SESSION_LOG_STANDARD
  mandates it: table of tools run + **what worked / what failed / any gap found**). This is the
  qualitative layer — the agent-annotated "gap found" lines are the **highest-value training signal**
  for the gap map, and no automated stream captures them.

Phase 0 therefore includes a **one-time historical ETL** (the rolling log -> structured rows; the
session-log `## Compiler Tools` sections -> parsed gap/failure annotations) so the loop has dense
signal from iteration 1, not forward-only accumulation.

## 7. The loop must be ALIVE — scheduled, autonomous (Andrew refinement #2)

The self-learning loop **must not be gated on ad-hoc inquiry**. It runs on a **scheduled cadence**,
independent of any agent session:

- A **scheduled infrastructure job** (EventBridge -> in-VPC Fargate/Lambda running `comp-learns-run`)
  on a daily/nightly cadence — the same pattern as the nightly gold runs, NOT an agent self-tick.
  **This is deliberately a server-side pipeline job, which sidesteps the LD-0175 zero-launch-crons
  convention entirely** (that governs agent session loops; this is infra scheduling, Andrew-mandated).
- Each scheduled tick: refresh `tool_activity` from the day's logs -> run one ratchet iteration ->
  write `scorecard.json` + the build/optimize/retire **worklist** to a SERVED S3 surface.
- `comp-learns-status` (and an MSTR/CTO dashboard) reads that served state. The fresh worklist feeds
  the normal commission path (CTO triages -> tool builds/retirements).
- New tool-use keeps flowing into the logs -> the next scheduled tick re-scores -> the loop is
  **self-sustaining and alive**, closing the feedback loop without a human pressing run.

## 8. Design principles (carry into the PRD)

1. **Score on VALUE, not usage (the COMP_LEARNS "benchmark honesty is non-negotiable" lesson, reused).**
   Optimizing invocation-count Goodharts into more invocations, not more value. Anchor the score on
   OUTCOMES: rail-escapes prevented, diagnose-chains shortened, real drift/bugs caught,
   UNVERIFIABLE-rate reduced, cost-per-archetype-outcome lowered.
2. **Advisory, not auto-mutating.** The loop emits a WORKLIST; CTO ratifies tool builds/retirements.
   Mirrors NFRA_DEBTSCAN never-auto-delete + comp-heat advisory-only. The champion config is a
   recommendation, never a self-rewriting toolset.
3. **Read-only over the estate; vintage-stamped.** `tool_activity` is a derived snapshot like
   `code_heat` (computed_at column); the loop never mutates source logs.
4. **Attribution-correct.** Reuse the race-free per-session SERIAL/TO_ID resolution (the cross-attrib
   bug `comp_log_auto` already fixed) so role/TO/firm dimensions are trustworthy.

## 9. Relationship to NFRA_COMPDRIFT (LD-0221)

Sibling on the **same Trino substrate.** comp-drift owns the Estate->Change propagation-parity
topology; NFRA_COMPLEARN adds the **Behavior plane** and points the federation at **toolset cognition**
instead of data parity. They SHARE the Trino plumbing — land `tool_activity` as a shared catalog asset,
do not duplicate the federation. CTO should sequence the two so the Trino-catalog work is done once.

## 10. Lane / governance / build path

- **MSTR** (this brief + LD-0225) scopes + commissions; does not author the PRD.
- **CTO** (`1.0.0_SA_CTO`) — PRD + arch-gate + TO decomposition + macro-project stand-up
  (`org/projects/NFRA_COMPLEARN.json` + REGISTRY row). Owns the scorer design + mutation-space + the
  Goodhart-honesty gate (the load-bearing design risk).
- **AE** (`0.8.0_AE_CloudComp` — the Trino/federation + compdiff owner; `0.7.0_AE_CloudOps` — the
  EventBridge/Fargate scheduled-job infra) — builds `tool_activity` ETL + catalog bind + the scheduled
  runner.
- **CVO** (`3.0.0_SA_CVO`) — verifies the scorer honesty + the gap-map against ground truth (does a
  flagged "gap" reproduce as a real raw-grep escape on a hot path?).

## 11. Suggested phasing (CTO refines)

- **Phase 0 — Behavior catalog + seed backfill.** ETL the three logs + the 3-month historical corpus
  into the `tool_activity` Iceberg table; bind as a Trino catalog. (The real first cost: agent_telemetry
  has legacy `tool:"?"` rows; compiler-tools-log is markdown — a clean normalizing ETL.)
- **Phase 1 — Federated views + `comp-learns-status` dashboard.** Trino join views (Behavior x Estate x
  Change) + the read-only status surface. **Immediately useful** — the first real view of tool
  demand/gaps/cost, even before any loop.
- **Phase 2 — Scorer + `comp-learns-run` single iteration.** Reclaim the ratchet; value-anchored score;
  emit the worklist.
- **Phase 3 — Scheduled autonomous loop.** EventBridge->Fargate nightly tick; served worklist; close the
  feedback loop to the CTO commission path.

Phases 0-1 stand alone in value; Phases 2-3 are the self-learning payoff.

## 12. Asks to CTO

1. Author the NFRA_COMPLEARN PRD + arch-gate; stand up the macro-project (JSON + REGISTRY).
2. Decide the `tool_activity` schema + the JOIN-key model to Estate/Change (coordinate with the
   NFRA_COMPDRIFT Trino-catalog work — do it once).
3. Own the **scorer + mutation-space design + the Goodhart-honesty gate** (the load-bearing risk).
4. Specify the scheduled-job home (EventBridge->Fargate/Lambda) + the served worklist surface +
   `comp-learns-status` read path.
5. Decommission-vs-reclaim call on the two dead shims: confirm `comp-learns-run`/`comp-learns-status`
   are RECLAIMED to this loop (not removed), with the legacy `comp.framework.*` pointer replaced.
6. Sequence Phases vs the live ADVI_BREAKS P0 (this is NOT P0 — it's strategic infra; phase it behind
   the firefight unless you judge otherwise).
