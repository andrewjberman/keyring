# Portal DEV->PROD Promote — v2.1.124 (PMTRDX.001 fileParser hardening)

**archetype:** DEPLOY

**Agent:** 0.4.0_DT_ClientPlatform
**Date:** 2026-06-17
**Trigger:** COO promote GO (Andrew-direct; PMTRDX.001 fileParser defensive hardening, 0.3.0_DE authored, COO-accepted 9/9 exercise-validated)
**Skill:** /prod-deploy

## Current State

Portal LIVE on PROD at **v2.1.124** (`90054baa`), CI-verified green. Second clean promote this session (after v2.1.123). Freeze released (COO-dispatched, so freeze was already active — no re-declare); main `portal/` tree confirmed back on DEV; workspace submodule pointer bumped + pushed on CLOUD.

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 0 | Confirm GO current (COO-dispatched freeze active) | GO `d725f7f3`, freeze active, no re-declare needed |
| 1 | **Delta-review BEFORE promote** (COO-mandated) | CLEAN — `origin/PROD..DEV` = EXACTLY 1 commit `d725f7f3`; no unready/WIP passengers |
| 2 | Push `d725f7f3` -> origin/DEV | `378fd8ff..d725f7f3` clean fast-forward; VALGATE D-1 PASS |
| 3 | Typecheck (tsc -b --noEmit) | 0 errors (local + pre-push gate) |
| 4 | Re-assert local PROD = origin/PROD | `e055d049` |
| 5 | Ephemeral worktree + bun install + `--no-ff` merge | worktree on PROD; bun 420 pkgs OK; merge `90054baa`; **PARITY GATE EMPTY** |
| 6 | Push PROD -> CI deploy.yml | `e055d049..90054baa`; pre-push tsc PASS; CI run 27706907113 |
| 7 | CI verify (gh run view --json) | **conclusion=success** (build + deploy + tag) |
| 8 | Tag verify (peel annotated tag) | `portal-v2.1.124^{commit}` == `90054baa` == origin/PROD head |
| 9 | Workspace pointer bump (safe-commit --only) | CLOUD `62409586f`; gitlink `378fd8ff`->`d725f7f3`; pushed (HALT_ACK=1) |
| 10 | Worktree teardown + flip-back | physical remove "Filename too long" (inert, gitignored); `worktree prune` cleaned tracking; main tree on DEV |
| 11 | RAVC2 report to COO + freeze release | reported landed + CI-verified |

## Deployment Tags

| Pipeline | Tag | Commit |
|---|---|---|
| portal | `portal-v2.1.124` | `90054baa` (peeled-verified) |

## Verification

```
CI run 27706907113: completed / success / "merge DEV->PROD: v2.1.124 — PMTRDX.001 fileParser unit guard ..."
portal-v2.1.124 peeled->commit: 90054baa5293f28d15f55ad72c134d53f7db9e8a
origin/PROD head:               90054baa5293f28d15f55ad72c134d53f7db9e8a   (match)
parity gate (git diff origin/DEV HEAD): EMPTY
workspace gitlink on origin/CLOUD: d725f7f32aeff9eb1e4deff2eea9ddd5015a5ada
main portal tree branch: DEV
```

## Shipped (1 commit)

- `d725f7f3` 0.3.0_DE_TradingOperations: fix(TradeSubmission/PMTRDX.001) fileParser unit guard — `assertFractionBasis` throws loud on percent-number uploads (>150%) instead of silently rendering x100 (e.g. 555%); `parseWeight` rejects un-normalized percent-numbers.

File: `src/pages/TradeSubmission/services/fileParser.ts` (+55 / -8).

## Compiler Tools

No comp-* tools run. Rationale: pure portal git promote (single-commit DEV->PROD merge-forward + CI deploy) of DE-authored, DE-validated frontend code — no data-pipeline/Lambda/infra/IAM surface for DT to check. The frontend-change compiler checks (comp-transform/comp-routes) are the AUTHOR's (DE) Phase-1 mandate, not the DT promoter's. Promote correctness gates — VALGATE D-1, pre-push `tsc -b --noEmit`, `--no-ff` parity gate, CI deploy.yml, peeled-tag verify, COO-mandated delta-review — all passed.

## Next Steps

- [2.0.0_SA_COO] RAVC2 reported; COO reports landed to Andrew (waiting on PROD landing). No close-trigger flagged for PMTRDX.001 by COO (DE owns the project-close decision).
- DT idle/available, event-driven, Monitor armed (task bobkodid4). Two clean promotes shipped this session (v2.1.123, v2.1.124).
