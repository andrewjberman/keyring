# 0.8.0_AE_CloudComp~D -- NFRA_SYSPARITY WS-2: enforcement leg LANDED LIVE (CVO exercise = closing)
**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE

Continues laneD_sysparity_ws2_destale_and_gate.md. CTO arch-gate GO @213935Z -> wired + landed the
commit-gate enforcement leg. WS-2 now: de-stale LANDED, gate engine LANDED, enforcement LANDED LIVE.

## CTO ruling (arch-gate GO @213935Z) -> what I built
- Enforcement = commit-gate-leg fail-closed PRIMARY (+ COO sweep backstop). system-current-override
  audited trailer. Surface age-WARN. Content-hash refinement my-call -> DEFERRED P2.5.
- Key datum from CTO's exercise: --gate rc2 RIGHT THEN (06 re-staled ~1.5h after @4e5a78abc) -> 06
  goes stale FAST in an active estate -> shaped the thrash-guard (cheap regen OR override; over-rate
  is the P2.5 auto-regen signal).

## The leg (safe-commit.sh @748bd523a)
- PLACEMENT: legacy path (the commit-QUEUE path is DORMANT by default -- SAFE_COMMIT_USE_QUEUE off --
  so the legacy path is the ACTIVE enforcement point; queue-worker leg = TO-6-future, flagged to COO).
- Keyed on PATHSPEC (FULL declared changeset), NOT IN_SCOPE (the .py/.sh gate-scope, which would MISS
  the *.yaml/*.json _SOURCES -- found + fixed during wiring).
- Runs `comp-system --gate --changed "${PATHSPEC[@]}"`: rc2 (genuine drift on a _SOURCE touch) ->
  BLOCK unless an audited `system-current-override: <reason>` -m trailer (-> git-author-override-audit.log);
  rc1/other (tool error) -> WARN + PROCEED (FAIL-SAFE: a broken gate never wedges the fabric); age-WARN surfaced.
- Cheap grep pre-check keeps NON-source commits from spawning comp-system (the common case is untouched).

## The bug I hit + fixed (the honest one)
First wiring used `CS_OUT="$(comp-system --gate ...)"; CS_RC=$?` -- under `set -euo pipefail` the
command-substitution assignment of a rc2 exit TRIPPED set -e, killing safe-commit with exit 2 BEFORE my
handler ran (first live test: rc2, no block message, no commit -- I initially mis-read it as a queue/
concurrency artifact; root-caused it to set -e). Fixed to a set-e-safe capture: `... && CS_RC=0 || CS_RC=$?`.
Also corrected the guard IN_SCOPE -> PATHSPEC (coverage). Re-tested: LIVE block-test PASS (rc1 clean block,
correct BLOCKED message + FIX guidance, no leak).

## Compiler Tools
| Tool | Why | Result |
|---|---|---|
| comp-system --self-test | engine + --changed conditioning | PASS 15/15 |
| comp-system --gate --changed | rc behavior (source+stale->2, non-source->0, age->0 WARN) | PASS |
| bash -n safe-commit.sh | syntax of the load-bearing edit (a parse error would wedge every commit) | SYNTAX OK |
| set-e rc-capture isolation | prove the fix survives set -e on rc2 | SURVIVED, CS_RC=2 |
| safe-commit (live block-test) | leg fires in the real flow | rc1 clean BLOCK, no leak |
| comp-system (regen) | 06 CURRENT at land | SYSTEM CURRENT |

**What worked:** rigorous pre-land validation (bash -n + isolation tests + a live block-test) caught the
set-e bug BEFORE it could wedge the fabric; fail-SAFE design (only clean rc2 blocks) bounds the wedge risk.
**What failed then fixed:** the set-e command-substitution exit; the IN_SCOPE->PATHSPEC guard.
**Rollout note:** landed fail-closed on a HOT wave (per CTO's measure-the-friction plan); 06 regen CURRENT
at land minimizes immediate blocks; COO fabric-awareness broadcast asked; over-rate audited = P2.5 signal.

## Blockers
NONE. SOLE remaining = CVO LD-0318 exercise (pinged @221154Z with a both-directions recipe) -> closes WS-2.

## Current State
- Part (a) de-stale: COMPLETE (06 CURRENT). Part (b) engine: LANDED @2c4902a5c. Part (b) ENFORCEMENT:
  LANDED LIVE @748bd523a (block-verified). COO sweep-backstop + fabric-awareness asked @221131Z.
- Monitor bs1gsnh6o LIVE. Session PID 25024.

## Next Steps
1. **[3.0.0_SA_CVO]** LD-0318 exercise (seed->block / override->clear / regen->clear) -> WS-2 close.
2. **[2.0.0_SA_COO]** fabric-awareness broadcast + add the --gate sweep-backstop to the drift-gate cadence.
3. **[0.8.0_AE_CloudComp~D, on CVO PASS]** flip WS-2 TO complete + close log. Then event-driven for COO's
   next NFRA-item sequence. P2.5 (content-hash + auto-regen) rides the over-rate signal. PH1 stays HELD.
