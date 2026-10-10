# ANDREW-DIRECT 2026-10-10 ~23:xxZ -- model policy by role (start point; to be assessed), plus the CTO's implementation and test proposal

**Channel:** Claude Code terminal, laptop, to 1.0.0_SA_CTO.

**Verbatim:**

> We can lift the hold but I think we need to do two things first. 1. WE need to have a new policy around what workers are
> what model. CTO/CVO/CRO are all Opus. MSTR and COO are all Sonnet, spawned subagent workers need to be haiku. High effort
> default in all cases, and the 5.5 models in each case. I want to assess whether this actually works in practice, but we
> need to start somewhere. Let's discuss how to get this implemented and tested across the system.

**Status:** DECIDED and IMPLEMENTED as `MP-20261010` (`org/ref/MODEL_POLICY.json`) on Andrew's answers below. The
dell1/dell2 hold stays until Andrew lifts it.

**Andrew's answers (same terminal, the next message), VERBATIM:**

> The premise is that worker agents are just being told what to do and have strict deliverables that they just adhere to,
> i.e. proof of spec, so they shouldnt need reasoning, they are told exactly what to do. Sonnet agents need some degree of
> reasoning to coordinate and field issues. Opus agents need high degree of reasoning because they are doing
> architecture/governance/validation. Yeah also to your point regarding tier2/3 seats, those are always going to be sonnet
> 5.5 at high effort. on call 2, yes out of scope for now. on call 3, yes laptop goes first, and also Dell1. WE can compare
> and contrast with sitez and Dell2. The second item was the rollout/testing.

**What the answers settle:**
- Tier-2/3 seats are always Sonnet 5.5 at high.
- Codex seats are out of scope for now.
- TREATMENT arm = laptop + dell1. CONTROL arm = sitez + dell2, which keep their pre-policy defaults so the two arms can be
  compared.
- The "second thing first" is this rollout and testing.

**Not named by him, so unchanged:** the BG seat `0.0.3_BG_BBGTerminal` and any other 0.0.N utility seat keep their
pre-policy pins.

**How it is built (MP-20261010):**
- Launchers: `.tools/model-policy.ps1` reads the policy; `.tools/ajb.ps1` and `.tools/spawn-agent.ps1` both use it.
- Workers: on a treatment device the dispatch skill spawns workers with `model: "haiku"` and `effort: "high"`. The worker
  frontmatter stays as it is for the control arm.
- Measurement: `.tools/model-census.py`.

## The policy as given

| Role | Serial shape | Model | Effort |
|---|---|---|---|
| CTO, CVO, CRO | 1.0.0 / 3.0.0 / 4.0.0 (+ ~lanes) | claude-opus-5-5 | high |
| MSTR, COO | 0.0.0 / 2.0.0 (+ ~lanes) | claude-sonnet-5-5 | high |
| spawned subagent workers | `worker`, `worker-light` agent types | claude-haiku-5-5 | high |

## What runs today (measured 2026-10-10 on the laptop)

- **Seat sessions** launch through `.tools/ajb.ps1`; `.tools/spawn-agent.ps1` wraps it.
  - Tier 1 and MSTR get NO flag, so they fall to each box's `~/.claude/settings.json`. On the laptop that is `"model": "opus"` at
    `effortLevel xhigh`.
  - Tier 2 and Tier 3 are DERIVED to `claude-opus-5` at `xhigh` (Andrew-direct 2026-08-24 and 08-26), in TWO places:
    `ajb.ps1:313-320` and `spawn-agent.ps1:63-66`. spawn-agent fills `-Model` first, so its copy is the one that wins for
    spawned seats.
  - The BG seat is pinned to `claude-opus-5` at `high` (`ajb.ps1:292`).
- **Subagent workers:** `.claude/agents/worker.md` reads `model: sonnet`, `effort: high`; `worker-light.md` reads
  `sonnet`, `medium`. The file says the value is per-fabric and a merge must not pick one side. The dispatch skill forbids a
  `model` argument at spawn.
- **Measurement instrument (exists, no build):** every Claude Code transcript records `"model"` on each assistant message,
  sessions in `~/.claude/projects/<proj>/<session>.jsonl` and subagents in `.../<session>/subagents/*.jsonl`.
  `org/mcp/sessions/<session>.serial` maps a session to its serial. Joining the two gives MEASURED model per serial and per
  worker, with no self-report.
- **Sampled now:** this CTO session runs `claude-opus-5-5`. Two recent laptop subagent transcripts ran `claude-opus-5-5`.
  Their agent type was not read, so this shows only that file policy and running model must be measured, not assumed.

## Proposed implementation (one change set, one owner, all four boxes through CLOUD)

1. **ONE role table, ONE place.**
   - Replace the per-serial table and the tier rule in `ajb.ps1` with a role map derived from the serial (base triple):
     1/3/4.0.0 -> opus-5-5; 0.0.0 and 2.0.0 -> sonnet-5-5; effort high for all.
   - DELETE spawn-agent's duplicate tier-default, so spawned and hand-launched seats read the same table. An explicit
     `-Model`/`-Effort` still wins.
2. **Workers.** Set `worker.md` and `worker-light.md` to `model: claude-haiku-5-5`, `effort: high`. That retires the
   per-fabric note: one value on every box. With effort at high for both, worker-light differs only in its name and the
   trial it was cut for; fold it into `worker` or keep it as an alias.
3. **Hand-launched sessions.** A session Andrew opens with bare `claude` skips `ajb.ps1` and reads the box's
   `~/.claude/settings.json`. Two options:
   - (a) set each box's default to sonnet-5-5 high and launch Tier 1 by `ajb`;
   - (b) leave settings alone and have the transcript census below flag any mismatch.
   Recommend (b): no per-box hand edit to drift.
4. **Records that this supersedes, edited in the same commit:**
   - Andrew-direct 2026-08-24/08-26 (Tier 2/3 Opus 5 xhigh);
   - 2026-09-16 and 2026-10-08 (workers Sonnet);
   - the worker agent descriptions ("RUNS SONNET 5.5");
   - dispatch SKILL.md:84 and :253.

## Proposed test (mechanical first, then "does it work in practice")

- **T1 MECHANICAL, day 0.** Launch one seat per role through the real path on one box (CTO, CVO, CRO, COO, MSTR lane), and have
  the COO spawn one `worker`. Read `"model"` from each transcript, not from the session's own claim. Pass when 6/6 match the
  table. A negative arm: one seat launched with an explicit `-Model` override must read the override.
- **T2 CENSUS, every box.** One small read-only script (`.tools/model-census.py`) joins `org/mcp/sessions/*.serial` to the
  transcripts and prints, per box:
  - serial, role, model expected, model measured, and a MISMATCH row;
  - the denominator: sessions read, and sessions with no serial file.
  It is run by MSTR at /govern, and it is not a monitor.
- **T3 PRACTICE, one week.** Compare Haiku-worker rounds with the prior Sonnet-worker rounds of a similar size, on numbers the
  fabric already keeps:
  - minutes per task order;
  - check defects per order at the COO drain;
  - CVO L9 REWORK rate;
  - surprise rows per order.
  Then compare Sonnet-COO rounds with Opus-COO rounds on rounds-to-close and refused issuances. Name a revert trigger up front,
  e.g. a defect rate 1.5x baseline over two rounds, which returns that role to its previous model.

## Questions for Andrew (each changes what gets built)

1. **Tier-2/3 seats** (AE CloudOps appliers, DS, DE, RD) and the BG seat are separate sessions, not subagents. Today they run
   Opus 5 at xhigh. Your rule does not name them. Recommendation: Sonnet 5.5 high, the same as COO.
2. **Haiku on WORLD-risk cells.** A worker cell that touches live AWS is a high cost-of-being-wrong act. Recommendation: keep
   Haiku for every worker as stated, and route a cell the worker cannot do to a re-cut (the existing rule), never a quiet
   model upgrade. Applies are already done by Tier-2 CloudOps seats, not workers.
3. **Codex seats** are out of scope unless you say otherwise.
4. **Rollout:** all four boxes at once when the hold lifts, or the laptop first (T1 here, then the others)? Recommendation:
   the laptop first, the same evening.
