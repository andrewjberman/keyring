# DEPLOY-COMPLETION LEDGER — portal DEV -> PROD promote (MDPF_EVR.FE-2 + OPAL_INVPHL follow-on)

**Opened:** 2026-08-15T211100Z
**Owner:** 0.4.0_DT_ClientPlatform (DT lane, `/prod-deploy`)
**Status:** OPEN — leg 4 done, leg 5 (PROD push) handed to integrator MSTR
**Authority:** Andrew-direct at the MSTR terminal 2026-08-15 ~2100Z, VERBATIM *"yes, do both"*
(MSTR 210435Z) — (b) spawn DT for the PROD promote; shipping his ruling *"yes they should render
as ordinary points"* (LD-0417). COO GO `MDPF_EVR.FE-2.PROMOTE` @13ed79bc40 (210723Z). TO:
`org/tier2_senior/0.4.0_DT_ClientPlatform/task_orders/MDPF_EVR.FE-2.PROMOTE.prod-promote-reconstructed-ordinary.md`

## Scope

| | |
|---|---|
| Promote | portal `DEV` -> `PROD` |
| Riders | **exactly 3 commits** (AC-P1 measured at Step 0, `git -C portal rev-list --count origin/PROD..origin/DEV` = 3): `684e67de` OPAL_INVPHL pillar copy served-overrides + per-field repo fallback (DT); `778ea780` MDPF_EVR.FE-2 `reconstructed` own render-enum member (DE); `e8b1fb07` FE-2 AC-8 per-firm date-aligned `point_class[]` read (DE). Author census = 2 (DT, DE). No served-key change. |
| PROD base | `fbbb9b39` = `portal-v2.1.161` (exact-match tag) |
| Typecheck | main tree `bun run typecheck` (`tsc -b --noEmit`) rc=0 |
| Untracked in main tree | 13 `??` items (stray telemetry / screenshots / .runtmp probes, June–Aug); NOT tracked, NOT in payload, cannot ride an origin/DEV merge. Surfaced to COO, not chased. |

## Legs (7) and their state

| # | Leg | State |
|---|---|---|
| 1 | push `origin DEV` | ✅ N/A — origin/DEV already at `e8b1fb07`, local DEV 0 ahead / 0 behind (DE's commits already integrated) |
| 2 | re-assert local PROD from origin | ✅ **DONE** — `update-ref` no-op, local PROD == origin/PROD `fbbb9b39` |
| 3 | ephemeral worktree + `bun install` | ✅ **DONE** — `.runtmp/portal-promote-20260815T211038Z`, 420 pkgs FOREGROUND rc=0, `node_modules/.bin/tsc` present |
| 4 | merge `DEV->PROD` `--no-ff` + parity gate | ✅ **DONE** — merge `449a6a0e` (parents `fbbb9b39` + `e8b1fb07`); **`git diff origin/DEV HEAD` = 0 lines**; message carries `Base fbbb9b39... Rollback: fbbb9b39...` |
| 5 | push `origin PROD` -> CI deploy + tag | ⏳ **HANDED TO MSTR** — DT push DENIED by never-rules-gate GATE 5 (LD-0367/0368 integrator-only); override NOT used (same reason as 08-11: a non-integrator push republishes the tree). Exact command in handoff msg. |
| 6 | workspace gitlink bump (DT commits) + push `origin CLOUD` (MSTR) | ⏳ pending leg 5 |
| 7 | worktree teardown + confirm main tree on DEV | ⏳ pending |

## Rollback

`git push origin fbbb9b39a0ce4103eaaf8cdf3f84581d3f244448:PROD` (integrator) — the merge is a
single `--no-ff` commit on top of the base; CI re-deploys whatever lands on PROD.
