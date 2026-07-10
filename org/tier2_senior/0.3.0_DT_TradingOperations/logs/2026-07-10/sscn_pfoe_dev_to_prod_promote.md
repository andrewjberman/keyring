# SSCN_PFOE.001 -- portal DEV->PROD promote (PFOE preset + DIVZ relabel)
**archetype:** DEPLOY

**Agent:** 0.3.0_DT_TradingOperations
**Date:** 2026-07-10
**Project:** SSCN_PFOE | **TO:** SSCN_PFOE.001 (RD 0.3.4_RD_SecurityScanner build)
**Dispatched by:** 2.0.0_SA_COO~C (PROMOTE GO 212326Z) | **Arch-gate:** 1.0.0_SA_CTO~C (PASS on 7db8f6b5)

## Current State

SSCN_PFOE.001 (Security Scanner PFOE 16-factor preset + DIVZ dropdown relabel, FE-only single-file
`portal/src/pages/SecurityScanner/constants.ts`) is LIVE on PROD (opalinvest.dev), tag `portal-v2.1.134`,
CI SUCCESS. Executed via `/prod-deploy` ephemeral-worktree form; the main portal tree never left DEV
(Rule 19). Deploy-completion ledger opened at start and CLOSED (all 4 legs proven).

**Gate sequence (all three green before the PROD push):**
- RD green build on DEV: RD committed 7db8f6b5 locally (tsc/eslint exit 0, comp-cache 0 mismatch,
  comp-transform clean). DE review WAIVED by Andrew ("bring on DT and get it deployed").
- COO weight-check: GREEN 16/16 vs Yang's Teams table (sum 100%), pre-cleared by COO~C.
- CTO~C arch-gate: PASS -- inspected the committed diff on 7db8f6b5, 1 file, spec-match verbatim, hash unchanged.
- Independent DT QA (belt-and-suspenders): single file constants.ts, PFOE_PRESET 16 entries summing to
  exactly 100 (Growth 42 / Quality 30 / Sentiment 10 / Valuation 8 / Momentum 10), DIVZ relabel
  'DIVZ -- Dividend' -> 'DIVZ' with id/universe/entries untouched, PresetGroup union + PRESET_GROUP_ORDER
  extended with Growth/Sentiment/Valuation. Matches the arch-gate verdict.

**HOLD->GO handling:** COO~C first sent a PRIME(HOLD PROD) (do not push until CTO~C glance clears), which
crossed my HOLD ack; COO~C then sent the PROMOTE GO + a REINFORCE (ephemeral worktree ONLY -- my own prior
logged main-tree-stuck-on-PROD defect) + a CLEARED confirm. Latest+most-restrictive: proceeded on the GO
with the ephemeral-worktree form, held no PROD push before the GO landed.

**Isolation:** the main portal tree carried POSN_CUSTOM lane WIP (Positioning + new customBlend.ts) dirty
throughout. It was NEVER touched -- the origin/DEV push carries only committed history (7db8f6b5), and the
ephemeral worktree (checked out from PROD, clean) isolated the merge + PROD-push tsc gate from it. Parity
gate `git diff origin/DEV HEAD` was EMPTY, confirming no passengers rode the promote.

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 0 | Open deploy-completion ledger (NEVER#5, at deploy-start) | `582896f16` -- ledger `20260710T2127Z_sscn-pfoe-promote`, 4 legs |
| 1a | push origin/DEV (VALGATE D-1) | `0109fecb..7db8f6b5 DEV->DEV`; D-1 PASS (no-op); DEV CI `29124821158` SUCCESS |
| 2 | typecheck (merged state, in worktree) | `tsc -b --noEmit` exit 0 |
| 3 | re-assert local PROD from origin | `update-ref refs/heads/PROD -> 86ebd471` (dry-run-pollution guard) |
| 4 | ephemeral worktree + `bun install` (FOREGROUND) | `portal-promote-20260710T212925Z` on PROD; 420 pkgs, exit 0 |
| 4 | merge --no-ff origin/DEV | merge SHA `5337b8159`; 1 file, 57 ins / 8 del |
| 4 | PARITY GATE `git diff origin/DEV HEAD` | EMPTY (0 bytes) -- promoted content == origin/DEV |
| 4 | push origin/PROD (VALGATE D-1 + PROD tsc) | `86ebd471..5337b815 PROD->PROD`; D-1 PASS + tsc PASS |
| 5 | CI deploy verify (`gh run view --json`, NOT watch) | run `29125030758` conclusion=SUCCESS status=completed |
| 5 | tag peel-verify | `portal-v2.1.134^{commit}=5337b8159 == origin/PROD head` (MATCH) |
| 6 | workspace submodule pointer bump on CLOUD | `8566967f6` gitlink `0109fecb -> 7db8f6b5`; pushed CLOUD |
| 7 | worktree teardown + flip-back check | PROD worktree unregistered; main tree on DEV; pwd = workspace root |
| 8 | close ledger + report | ledger CLOSED (4 legs); RAVC report to COO~C (freeze released) + CTO~C |

## Deployment Tags

| Pipeline | Tag | Commit |
|---|---|---|
| portal (PROD) | `portal-v2.1.134` | `5337b8159a7c4dd5192ff2e002d0afa7bc611309` (peeled) |

## Verification

```
CI:   gh run view 29125030758 --json conclusion,status
      -> {"conclusion":"success","status":"completed", "displayTitle":"merge DEV->PROD: v2.1.134 -- SSCN_PFOE ..."}
TAG:  git rev-parse portal-v2.1.134^{commit} = 5337b8159a7c4dd5192ff2e002d0afa7bc611309
      git rev-parse origin/PROD              = 5337b8159a7c4dd5192ff2e002d0afa7bc611309   (MATCH)
      (ls-remote tag OBJECT sha = 08555d1a; peeled ^{} = 5337b8159 -- annotated tag, distinguished per procedure)
PARITY: git diff origin/DEV HEAD = 0 bytes (clean single-file promote)
MAIN TREE: git -C portal branch --show-current = DEV (never left)
POINTER:  parent gitlink git ls-tree HEAD portal = 7db8f6b5 (bumped, pushed CLOUD 8566967f6)
LEDGER:   deploy_ledger.py -- CLOSED, all 4 legs proven
```

Note: `git worktree remove --force` hit the documented Windows "Filename too long" on node_modules --
it UNREGISTERED the PROD worktree (worktree list shows only the main DEV tree, PROD branch free for the
next promote) but the physical `.runtmp/portal-promote-20260710T212925Z` dir persists (gitignored, inert).

## Compiler Tools

| Phase | Tool + command | Result | Disposition |
|---|---|---|---|
| deploy contract | `.tools/deploy_ledger.py open/close-leg/close --slug sscn-pfoe-promote` | 4 legs opened at start, each closed with live proof, ledger CLOSED | NEVER#5 satisfied structurally |

DT gold/infra comp-tool minimums (`comp-pipescript io` / `comp-iam service` / `comp-routes behaviors`) are
N/A here: this is a FE-only portal promote -- no gold script deployed, no new boto3 call, no CloudFront /
Lambda@Edge change. The change surface was covered by the RD's mandated frontend rails at build time
(`comp-cache collisions` = 0 TYPE MISMATCH / no new scanner key; `comp-transform schema-check SecurityScanner`
= clean) and re-affirmed by CTO~C's arch-gate; my promote re-verified the same commit shipped verbatim
(empty parity gate). Core doc `deployment_map.xml` unchanged -- no new Lambda/EC2 resource or contract change.

## Next Steps

1. **[2.0.0_SA_COO~C]** Owns the served-PROD-artifact verify (opalinvest.dev SecurityScanner shows PFOE
   preset) + hands Andrew the final smoke. AC4 UI smoke: select PFOE -> 16 factors, totalWeight badge 100
   green, grid re-ranks; select DIVZ -> label reads "DIVZ", 13 factors, badge 100; default-on-load DIVZ.
   Then RAVC-close SSCN_PFOE.001 (left `pending` -- I did not self-flip).
2. **[Yang / COO~C]** Non-blocking flag carried forward: `eps_stability` (96.7% coverage pick) vs the
   exact-name analyst factor `eps_stable_est` -- one-line code swap if Yang prefers; does not gate.
3. **[DT]** Rollback path if the served verify surfaces a problem: base `86ebd471` (portal-v2.1.133).
4. DT lane IDLE, reachable via the persistent inbox Monitor (task `bg7hw2p7h`).
