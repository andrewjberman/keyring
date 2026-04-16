# CTO Session 30 — COMP_LEARNS_ARCHITECTURE PRD shipment

**Agent:** 1.0.0_SA_CTO
**Date:** 2026-04-16
**Scope:** PRD authored for COMP_LEARNS six-concern structural-inference architecture + 9-TO decomposition (.011-.019) + handoff to COO

## Trigger

Andrew briefing 2026-04-16: advance COMP_LEARNS from pilot (monolithic per-target compiler + query-pass-rate fit) into production-grade structural inference (AST-first extraction, normalized graph IR, A/B downstream-LLM primary metric, bootstrap-vs-target formal discipline). Briefing distilled learnings from autoresearch-master.zip (loop discipline) + corporeal-dev.zip (graph semantics + keep/discard loop).

## Decisions locked in PRD

1. **Six concerns** as module boundaries: `parsers / ir / compiler_subtypes / graph_builder / bench / loop`. Each has a contract; each is independently testable and replaceable.
2. **IR is a normalized graph** with first-class condition nodes (not edge attributes). Controlled vocabulary for NodeKind + EdgeKind in `ir/kinds.py`.
3. **SubtypeRecord is the contract between extraction and graph building.** Records carry confidence (certain / ambiguous / heuristic). Heuristic is penalized in scoring — ratchet drives graduation to AST-backed.
4. **Primary objective function = augmented-minus-baseline LLM success, α-weighted with token_reduction.** Structural F1 is a lever, not the product surface.
5. **v0 narrow target = `httpx`, inaugural subtype = `imports`.** Minimal viable ratchet: one KEEP cycle + one DISCARD cycle demonstrated end-to-end.
6. **Bootstrap vs target table is binding.** Regex extraction allowed with `heuristic` flag, penalized in scoring, auto-pressure to graduate.
7. **Gold authoring is CTO-owned in v0** (TO .016), delegated later.
8. **A/B LLM = claude-sonnet-4-6** (consistent with thread infra), budget $50/target/cycle hard-capped.

## Task orders (for COO decomposition)

9 new TOs (.011-.019):

| TO | Title | Owner | Gates |
|---|---|---|---|
| .011 | Module skeleton + core contracts | ~A | — |
| .012 | Python parser (LibCST) | ~A | .011 |
| .013 | imports subtype v0 | ~B | .011 + .012 |
| .014 | Graph builder v0 | ~C | .011 + .013 |
| .015 | Bench scorecard + A/B | ~D | .011 + ADVI_49EXEC.003 anthropic-sdk-deps |
| .016 | httpx gold authoring | CTO | .011 |
| .017 | End-to-end v0 ratchet | ~C | .011-.016 |
| .018 | program.md v1.0 update | CTO | .011-.017 |
| .019 | Visualization CLI (optional) | any lane | .017 |

## Coordination with COO

COO shipped `.tools/operator` this session (accountability mechanism for project closure). I requested CIRCULAR_DEPS fork kind addition — COO ACKed and is adding this turn. After decomposition COO will run `operator COMP_LEARNS` to validate dep graph — .017 should show as BLOCKED until .011-.016 complete, anything else is a fork back to CTO.

## Blockers flagged

1. LibCST dependency policy (layer vs venv) — AE 0.7 at .012 Phase 1.
2. Anthropic SDK availability — gates .015 Phase 2; waiting on ADVI_49EXEC.003 (AE 0.6 in flight).
3. ~D capacity constraint — CN-P1b re-sequenced pending today; .015 may need reassignment if ~D doesn't free in time.

## Open questions asked of Andrew (in handoff briefing)

1. httpx vs dogfood-on-`comp/framework/` as inaugural target
2. imports vs io as inaugural subtype
3. 2-hour CTO burn on gold authoring (.016) — OK?
4. claude-sonnet-4-6 as A/B LLM
5. $50/target budget cap
6. ~D capacity for .015 vs reassignment

Silence = defaults per PRD.

## Commits

- `docs/architecture/COMP_LEARNS_ARCHITECTURE.md` (new, ~550 lines)
- `org/projects/COMP_LEARNS.json` (phase flipped Phase 1 → Phase 2 architectural expansion; prds[] extended; blocking rewritten)
- This session log

## Compiler Tools

| Tool | Command | Result |
|------|---------|--------|
| `comp-build` | `--rebuild` | Cache refresh, 0 changes to comp/ index (comp-* tools don't yet index comp/ at function level). Motivates TO .011 as bootstrap of next-gen tooling. |
| `comp-xref` | `comp/framework/compiler_contract.py` | 1 consumer (comp/framework/run.py). Confirms compiler_contract is existing authority; TO .011 evolves alongside, doesn't break. |
| `comp-blast` | `comp/framework/extractor_interface` | 0 external consumers. Safe to rename-and-evolve into `compiler_subtypes/base.py` in TO .011. |

All three pre-runs documented in §10 of the PRD.

## State at close

- PRD shipped, project JSON updated, this log written.
- Handoff briefing coming in chat to Andrew.
- COO standing by for the handoff + decomposition.

— 1.0.0_SA_CTO
