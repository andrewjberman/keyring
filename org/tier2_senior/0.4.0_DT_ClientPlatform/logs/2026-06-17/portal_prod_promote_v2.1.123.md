# Portal DEV->PROD Promote — v2.1.123

**archetype:** DEPLOY

**Agent:** 0.4.0_DT_ClientPlatform
**Date:** 2026-06-17
**Trigger:** Andrew-direct GO ("get portal tree deployed, follow protocol")
**Skill:** /prod-deploy (DT canonical procedure)

## Current State

Portal is LIVE on PROD at **v2.1.123** (`e055d049`), CI-verified green. Freeze window released; main `portal/` tree confirmed back on DEV; workspace submodule pointer bumped + pushed on CLOUD.

Identity note: launched under malformed serial `0.4.0_T_ClientPlatform` (broker rejected — not in org hierarchy; `_T_` matched no role pattern in `ajb.ps1`). Andrew clarified it was a registration typo for **`0.4.0_DT_ClientPlatform`**; re-registered correctly, no role self-assignment made. No ajb.ps1 fix needed (the UNRECOGNIZED default branch behaved as designed; this was a typo, not a mapping gap).

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 0 | Freeze declared to COO | COO ACK — HOLD clear (no portal-repo passengers from COO fabric) |
| 1 | Push local commit -> origin/DEV | `f3ceea7c..378fd8ff` clean fast-forward; VALGATE D-1 PASS |
| 2 | Typecheck (tsc -b --noEmit) | 0 errors (local + pre-push gate) |
| 3 | Re-assert local PROD = origin/PROD | `2d07297c` (dry-run-pollution guard) |
| 4 | Ephemeral worktree + bun install + `--no-ff` merge | worktree on PROD; bun install 420 pkgs OK; merge `e055d049`; **PARITY GATE EMPTY** (PROD tree == origin/DEV) |
| 5 | Push PROD -> CI deploy.yml | `2d07297c..e055d049`; pre-push tsc PASS; CI run 27698098374 |
| 5a | CI verify (gh run view --json, NOT watch) | **conclusion=success** (build + deploy-to-server + tag) |
| 5b | Tag verify (peel annotated tag) | `portal-v2.1.123^{commit}` == `e055d049` == origin/PROD head |
| 6 | Workspace pointer bump (safe-commit --only) | CLOUD `7df4d9cb6`; gitlink `0ac642ad`->`378fd8ff`; pushed (HALT_ACK=1 routine msg) |
| 7 | Worktree teardown + flip-back | physical remove hit "Filename too long" (inert, gitignored); `worktree prune` cleaned tracking; main tree on DEV |
| 8 | RAVC report to COO + freeze release | reported landed; YANG_SITTW auto-close-trigger fired |

## Deployment Tags

| Pipeline | Tag | Commit |
|---|---|---|
| portal | `portal-v2.1.123` | `e055d049` (peeled-verified) |

## Verification

```
CI run 27698098374: completed / success / "merge DEV->PROD: v2.1.123 ..."
portal-v2.1.123 peeled->commit: e055d04915d0b88393742b04f66d84770b991d47
origin/PROD head:               e055d04915d0b88393742b04f66d84770b991d47   (match)
parity gate (git diff origin/DEV HEAD): EMPTY
workspace gitlink on origin/CLOUD: 378fd8ff03d11d3ac0a48a400d43ee23d4ba87c6
main portal tree branch: DEV
```

## Shipped (9 commits, origin/PROD..origin/DEV + 1 local)

- `378fd8ff` lock white-label user patricia -> Demo + hide partner selector (Andrew-direct)
- `f3ceea7c` retire CausalityEngine FE page (06-16 teardown FE leg; backend deleted by 0.5.0_AE)
- `fbfdbe9d` YANG_SITTW.TO-1 REFINE — Global deep-tail Non-Model band reconcile
- `a344b2bd` types: declare TTW period key
- `8f564d42` land white-label patricia on Demo default
- `700ec9b4` YANG_SITTW.TO-3 — TTW period on MP Performance
- `a447712b` YANG_SITTW.TO-1 leg b — MP Global since-inception view
- `27299745` YANG_SITTW TO-2 — TTW period on Market Overview
- `0ac642ad` D5-FIX — remove 29 dead exported functions

Net: 28 files, +173 / -2312 (bulk = CausalityEngine page retirement + dead-code sweep).

## Compiler Tools

No comp-* tools run. Rationale: this was a pure portal git promote (DEV->PROD merge-forward + CI deploy), not a data-pipeline/Lambda/infra change — no gold-script IO, no schema/transform surface, no IAM/boto3 delta. The promote's own gates (VALGATE D-1 adapter-threading, pre-push `tsc -b --noEmit`, the `--no-ff` parity gate, CI deploy.yml, peeled-tag verification) are the relevant correctness checks and all passed. comp-transform/comp-routes would apply to a frontend *change* authored by DE/RD, not a DT promote of already-committed DEV work.

## Next Steps

- [2.0.0_SA_COO] Close YANG_SITTW (2-step atomic: JSON status->complete + REGISTRY row move) citing PROD `e055d049` / tag `portal-v2.1.123` / CI run 27698098374. (Reported; awaiting COO action.)
- [MSTR] No role-mapping fix required — `_T_` was a launch-time typo, not an ajb.ps1 gap; corrected to `0.4.0_DT_ClientPlatform` per Andrew.
- DT idle/available, event-driven, Monitor armed (task bobkodid4).
