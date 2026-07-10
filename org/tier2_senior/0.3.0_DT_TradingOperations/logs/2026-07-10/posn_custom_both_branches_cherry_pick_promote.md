# POSN_CUSTOM -- both-branches POSN-only cherry-pick promote (passenger f2053740 excluded)
**archetype:** DEPLOY

**Agent:** 0.3.0_DT_TradingOperations
**Date:** 2026-07-10
**Project:** POSN_CUSTOM | **TO:** POSN_CUSTOM.001/.002 (RD 0.2.1_RD_Positioning build)
**Dispatched by:** 2.0.0_SA_COO~C (FINAL GO, consolidated) | **Arch-gate:** 1.0.0_SA_CTO~C (PASS on 662e56ec) | **Mechanic:** CTO~C both-branches cherry-pick

## Current State

POSN_CUSTOM (Positioning custom model-blend + auto-select-CSM-when-Custom, POSN_CUSTOM.001/.002) is LIVE
on PROD (opalinvest.dev) AND on origin/DEV, tag `portal-v2.1.135`, CI SUCCESS. The passenger commit
`f2053740` (CTO~B's inflection advisor-allowlist "add Noel Soderblom") was EXCLUDED per CTO~C's ruling
(client-facing, not DEV-verified, gated on the gold pipeline emitting noel_soderblom) and Andrew's "POSN
only, no inflection." Executed as CTO~C's blessed both-branches cherry-pick: rebuild the 2 POSN commits
onto a clean origin/DEV base and push to BOTH origin branches, leaving f2053740 on NEITHER.

**Passenger structure:** on the local main tree the 2 POSN commits (573b41ad, 662e56ec) were STACKED ON
TOP of f2053740 (linear f2053740 <- 573b41ad <- 662e56ec), so a straight merge would have dragged
f2053740 to origin. The cherry-pick-onto-clean-base mechanic reconstructs POSN with f2053740 excluded
from the ancestry entirely.

**Instruction flurry (resolved to a stable end-state):** COO~C sent GO -> REFINE -> CLARIFY -> FINAL GO
(consolidated, supersedes all) -> PLAN APPROVED + gitlink pre-confirm -> gitlink confirm. I held on each
until the latest bound, ACK'd, and executed the consolidated FINAL GO + the pre-confirmed gitlink
resolution. No PROD push occurred before the GO; the mechanic changed from "cherry-pick onto PROD" to
"both-branches" before I pushed anything (I pre-staged reversibly and verified locally first).

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 0 | Open deploy-completion ledger (NEVER#5, 5 legs) | ledger `20260710T2235Z_posn-custom-promote` |
| 1 | Ephemeral worktree off origin/DEV (7db8f6b5 clean, NO f2053740) | `posn-dev-20260710T223830Z` detached |
| 1 | Cherry-pick BY HASH 573b41ad then 662e56ec | `3e24968d`+`c6dd7b9b`; clean, no conflict, no rebase |
| 1 | Local hard-check | files = Positioning/* only; inflection path ABSENT; f2053740 NOT ancestor |
| 2 (L1) | push origin/DEV (POSN-only) | `7db8f6b5..c6dd7b9b`; VALGATE D-1 PASS; DEV CI `29128393805` SUCCESS |
| 3 | re-assert local PROD + worktree off PROD + `bun install` | `posn-prod-20260710T224119Z`; 420 pkgs exit 0 |
| 3 | merge --no-ff origin/DEV (POSN-only) | merge `d882b24f`; 5 files Positioning/* only |
| 3 | PARITY GATE `git diff origin/DEV HEAD` | EMPTY (0 bytes) |
| 3 | typecheck (tsc -b --noEmit) on merged state | exit 0 |
| 3 (L2) | push origin/PROD | `5337b815..d882b24f`; VALGATE D-1 + PROD tsc PASS |
| 4 (L3) | CI deploy verify (`gh run view --json`) | run `29128552568` conclusion=SUCCESS |
| 4 (L3) | tag peel-verify | `portal-v2.1.135^{commit}=d882b24f == origin/PROD` (MATCH) |
| 5 (L4) | HARD both-branch f2053740-absence verify | ancestry + CONTENT absent on origin/DEV AND origin/PROD |
| 6 (L5) | CLOUD gitlink bump -> origin/DEV HEAD | `2f380afbc`; gitlink `7db8f6b5 -> c6dd7b9b` via cacheinfo (mechanic b) |
| 7 | teardown both worktrees + main-tree check | both unregistered; main tree on DEV; pwd = workspace root |
| 8 | close ledger + report | ledger CLOSED (5 legs); RAVC report to COO~C (freeze released) + CTO~C |

## Deployment Tags

| Pipeline | Tag | Commit |
|---|---|---|
| portal (PROD) | `portal-v2.1.135` | `d882b24f3382b40d64db6d8e9eb0ca3241d27745` (peeled) |

## Verification

```
origin/DEV  = c6dd7b9b (POSN-only: 3e24968d + c6dd7b9b, base 7db8f6b5)
origin/PROD = d882b24f (merge --no-ff origin/DEV; parity git diff origin/DEV HEAD = 0 bytes)
TAG:  git rev-parse portal-v2.1.135^{commit} = d882b24f == origin/PROD head  (MATCH; tag obj 30633a42)
CI:   PROD deploy 29128552568 conclusion=success; DEV validate 29128393805 success
f2053740 ABSENT -- BOTH branches, BOTH ways:
  ancestry: merge-base --is-ancestor f2053740 origin/DEV -> NO;  origin/PROD -> NO
  content:  origin/DEV:inflection/layout.ts and origin/PROD:inflection/layout.ts -- "Soderblom" ABSENT
promoted diff = src/pages/Positioning/* ONLY (5 files), ZERO AdvisorIntelligence/inflection
GITLINK: parent CLOUD portal gitlink = c6dd7b9b (== origin/DEV HEAD, on-origin, f2053740-free); commit 2f380afbc
MAIN TREE: git -C portal branch --show-current = DEV; HEAD f046b6a9 (CTO~B local stack f2053740+POSN+revert, preserved)
LEDGER: deploy_ledger.py -- CLOSED, all 5 legs proven
```

## Compiler Tools

| Phase | Tool + command | Result | Disposition |
|---|---|---|---|
| deploy contract | `.tools/deploy_ledger.py open/close-leg/close --slug posn-custom-promote` | 5 legs, each closed with live proof, ledger CLOSED | NEVER#5 satisfied |

DT gold/infra comp-tool minimums (`comp-pipescript io`/`comp-iam`/`comp-routes`) N/A: FE-only portal promote
(no gold script, no boto3, no CloudFront/Lambda@Edge change). Change surface = Positioning/* React
components, covered by the RD's build-time rails. `comp-surface-check` auto-ran on the gitlink commit
(portal path -> parent-scoped gitlink, no critical surface). The load-bearing verification here was the
git-level both-branch f2053740-absence hard-check (ancestry + content), run explicitly per CTO~C's must-check.

## Notes / gotchas banked

- **Both-branches cherry-pick w/ retained-local passenger:** because f2053740 was stacked UNDER the POSN
  commits and had to stay OFF origin, the mechanic was: worktree off origin/DEV (clean base, no f2053740),
  cherry-pick POSN by hash (creates new SHAs 3e24968d/c6dd7b9b with clean ancestry), push origin/DEV, then
  merge that POSN-only origin/DEV into PROD. Result: POSN on both origin branches, f2053740 on neither.
- **Gitlink under divergence:** origin/DEV (POSN-only c6dd7b9b) diverged from the local main-tree DEV
  (f046b6a9, holding f2053740+POSN+revert). `safe-commit -- portal` records the main-tree checkout, which
  would put an off-origin, f2053740-tainted SHA in the parent. Resolution (COO~C-confirmed): `git
  update-index --cacheinfo 160000,<origin/DEV-sha>,portal` + a scoped bare commit -- records the gitlink to
  the on-origin POSN-only HEAD WITHOUT touching the main tree (zero Rule-19 strand risk; main tree never
  moved). Parent `git status` will now show `portal` modified (checkout f046b6a9 vs gitlink c6dd7b9b) -- an
  expected, benign consequence of CTO~B's f2053740 stack being retained locally.
- **Windows long-path:** WT-PROD `worktree remove --force` hit "Filename too long" on node_modules but
  UNREGISTERED the worktree (list shows only the main DEV tree); physical `.runtmp` dir persists (gitignored,
  inert). WT-DEV removed cleanly.

## Next Steps

1. **[2.0.0_SA_COO~C]** Owns the served-PROD-artifact verify (opalinvest.dev Positioning custom model-blend
   + CSM auto-default on Custom) + Andrew smoke. RAVC-close POSN_CUSTOM.001/.002 (left pending -- not self-flipped).
2. **[1.0.0_SA_CTO~C / CTO~B]** f2053740 (inflection advisor-allowlist) remains on the local main-tree DEV
   (f046b6a9), NOT on origin -- available for CTO~B's own gated inflection promote once the gold pipeline
   emits noel_soderblom + it is DEV-verified. NOT lost.
3. **[DT]** Rollback path if served verify surfaces a problem: origin/PROD base 5337b8159 (portal-v2.1.134).
4. DT lane IDLE, reachable via the persistent inbox Monitor (task `bg7hw2p7h`). Both today's promotes
   (SSCN_PFOE v2.1.134, POSN_CUSTOM v2.1.135) landed + verified.
