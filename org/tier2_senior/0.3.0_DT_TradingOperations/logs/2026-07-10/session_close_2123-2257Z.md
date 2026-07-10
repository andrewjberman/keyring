# Session close 2123-2257Z -- two portal DEV->PROD promotes (SSCN_PFOE + POSN_CUSTOM)
**archetype:** DEPLOY
**secondary_archetypes:** COORDINATE

**Agent:** 0.3.0_DT_TradingOperations
**Date:** 2026-07-10
**Window:** ~2123Z (session start / watcher arm) -> 2257Z (this close)
**Detailed per-promote logs (the deep record; this is the session wrapper):**
- `sscn_pfoe_dev_to_prod_promote.md`
- `posn_custom_both_branches_cherry_pick_promote.md`

## Current State

Launched fresh, ran `/watcher` (Monitor `bg7hw2p7h` armed, registered PID 18552) + `org/XXX.md` startup,
then executed TWO portal promotes dispatched by 2.0.0_SA_COO~C. Both LIVE, CI-verified, ledgers CLOSED.
Main portal tree on DEV throughout (Rule 19); no strands (`deploy_ledger.py check` = no stranded/open of mine).

**Promote 1 -- SSCN_PFOE -> portal-v2.1.134** (standard ephemeral-worktree merge). PFOE 16-factor Security
Scanner preset + DIVZ relabel, single-file `constants.ts`. origin/PROD merge `5337b8159`; CI `29125030758`
SUCCESS; parity EMPTY; gitlink bumped to 7db8f6b5 (`8566967f6`). All 3 gates green before push (RD green
build + COO weight 16/16 + CTO~C arch-gate PASS).

**Promote 2 -- POSN_CUSTOM -> portal-v2.1.135** (CTO~C both-branches POSN-only cherry-pick; passenger
`f2053740` inflection-allowlist EXCLUDED per CTO~C ruling + Andrew "POSN only, no inflection"). Cherry-picked
573b41ad+662e56ec by hash off clean origin/DEV(7db8f6b5) -> origin/DEV `c6dd7b9b`; merge --no-ff ->
origin/PROD `d882b24f` (parity EMPTY); CI `29128552568` SUCCESS. **f2053740 verified ABSENT on BOTH origin
branches -- ancestry AND content** (Soderblom allowlist add absent from inflection/layout.ts on both).
Promoted diff = Positioning/* only. CLOUD gitlink -> `c6dd7b9b` (origin/DEV HEAD) via `update-index
--cacheinfo` (`2f380afbc`) so the main tree never moved -- it stays on DEV at `f046b6a9`, preserving CTO~B's
local f2053740+revert stack (not lost, available for CTO~B's gated inflection promote later).

**Coordination:** COO~C's POSN dispatch arrived as a 6-message flurry (GO -> REFINE -> CLARIFY -> FINAL GO
consolidated -> plan/gitlink pre-confirm -> gitlink confirm). Held on each until the latest bound; pre-staged
reversibly; executed only the settled FINAL GO. One genuine ambiguity (gitlink target under DEV/PROD
divergence) surfaced to COO~C rather than improvised -- COO~C called it "a sharp, correct catch" and
pre-confirmed the resolution (gitlink == origin/DEV HEAD).

## Compiler Tools

| Tool | Result | Note |
|---|---|---|
| `.tools/deploy_ledger.py` (open/close-leg/close x2 promotes) | PASS | 4+5 legs, each closed with live proof; both ledgers CLOSED; NEVER#5 satisfied |
| `comp-surface-check` (auto in safe-commit x4) | PASS | ledger + pointer + 2 log commits; portal gitlink = parent-scoped, no critical surface |

DT gold/infra comp minimums (`comp-pipescript io`/`comp-iam`/`comp-routes`) N/A both promotes: FE-only portal
(no gold script, no boto3, no CloudFront/Lambda@Edge). The load-bearing verifications were git-level: SSCN
parity-empty; POSN both-branch f2053740-absence (ancestry + content) per CTO~C's must-check. **What worked:**
the ephemeral-worktree form + `cacheinfo` gitlink mechanic kept the main tree on DEV with zero strand risk;
the deploy ledger structurally gated each leg. **Gap found:** none new -- the Windows long-path
`worktree remove` failure is known/benign (unregisters, physical dir persists gitignored).

## Blockers

None. Both promotes landed clean. Residual (owner-tracked, not a blocker): COO~C owns the served-artifact
verifies + Andrew smoke; f2053740 held local for CTO~B's gated inflection promote.

## Next Steps

1. **[2.0.0_SA_COO~C]** Served-PROD-artifact verify both (opalinvest.dev: SecurityScanner PFOE preset; Positioning
   custom model-blend + CSM auto-default) + Andrew smoke; RAVC-close SSCN_PFOE.001 and POSN_CUSTOM.001/.002
   (left pending -- not self-flipped).
2. **[1.0.0_SA_CTO~C / CTO~B]** f2053740 remains on local main-tree DEV (`f046b6a9`), NOT on origin -- CTO~B's
   gated inflection promote when the gold pipeline emits noel_soderblom + DEV-verified.
3. **[DT]** Rollback bases if a served verify fails: SSCN `86ebd471` (v2.1.133 base) / POSN `5337b8159` (v2.1.134).
4. DT lane IDLE, reachable via Monitor `bg7hw2p7h`.

## Files Modified

See commit messages: `582896f16`, `8566967f6`, `8ace8f946`, `2f380afbc`, `e33056b58` (ledger opens + 2 pointer
bumps + 2 per-promote logs). This session-close log + compiler-tools-log line committed here.
