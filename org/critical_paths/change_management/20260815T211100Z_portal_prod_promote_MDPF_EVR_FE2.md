# DEPLOY-COMPLETION LEDGER — portal DEV -> PROD promote (MDPF_EVR.FE-2 + OPAL_INVPHL follow-on)

**Opened:** 2026-08-15T211100Z
**Owner:** 0.4.0_DT_ClientPlatform (DT lane, `/prod-deploy`)
**Status:** CLOSED 2026-08-15T~2140Z -- ALL LEGS LANDED, NOTHING STRANDED. PROD live and verified at portal-v2.1.162 (449a6a0e); CI run 31909060242 success (1 of 1 workflows on the sha); served ModelPortfolios chunk carries the FE-2 marker; AC-P3 rendered read done + mutant/console controls. No audited override used at any leg.
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
| 5 | push `origin PROD` -> CI deploy + tag | ✅ **DONE** — DT push DENIED by never-rules-gate GATE 5 (LD-0367/0368 integrator-only); override NOT used; handed to MSTR 211559Z, **MSTR pushed 2118Z** after re-deriving parity/payload/base; remote read-back `origin/PROD = 449a6a0e`; CI `Deploy to Production` run 31909060242 `conclusion: success` (1 of 1 on the sha, enumerated by headSha); tag `portal-v2.1.162` peels to 449a6a0e |
| 6 | workspace gitlink bump (DT commits) + push `origin CLOUD` (MSTR) | ✅ **NO-OP BY STATE** — gitlink already `e8b1fb07` (MSTR integrate @04d25a3533) == DEV HEAD == promoted payload head; `git diff HEAD -- portal` = 0 lines, an explicit bump would be an empty commit. Traceability (PROD 449a6a0e / tag / run) carried by this ledger + the proof-of-spec instance; the commit landing them is DT's, MSTR pushes CLOUD as integrator |
| 7 | worktree teardown + confirm main tree on DEV | ✅ **DONE** — `worktree remove` failed 'Filename too long' (documented Windows class; `.runtmp/portal-promote-20260815T211038Z` persists, gitignored + inert), `worktree prune` OK, `worktree list` no longer shows it; main tree **DEV** @e8b1fb07; cwd workspace root |

## Rollback

`git push origin fbbb9b39a0ce4103eaaf8cdf3f84581d3f244448:PROD` (integrator) — the merge is a
single `--no-ff` commit on top of the base; CI re-deploys whatever lands on PROD.

## AC-P3 — the rendered read, and what it can and cannot say

PNG `portal/.frontend-dev/screenshots/mdpf_evr_fe2_PROD_v2.1.162_global_REAL.png` (1440x2346): deployed PROD bundle
(`--origin https://opalinvest.dev`) + the SERVED Global platinum artifacts as fixtures. READ: Global (All); both AUA
charts with no band / no dash / no Interpolated legend entry; REFAREAS 0 x3. The 2 reconstructed dates (2026-05-20,
2026-08-05) render ordinary.

**Premise correction (source-confirmed):** the pixel read is NON-DISCRIMINATING at Global. A MUTANT fixture relabelling
both dates `interpolated_estimate` renders pixel-identical (60/3,378,240 px = the animated status dot), because
`portal/src/pages/ModelPortfolios.tsx:884-889 @449a6a0e` empties `trendInterpolatedDates` at Global (Andrew-direct
2026-07-23 materiality ruling; same gate at `:882 @fbbb9b39`). Global never pixel-rendered estimate-class on either
build — the TO's "visually distinct, live" premise is false at source. **The discriminating exercise on the deployed
bundle is behavioral:** console capture -> REAL data 0 `reconstructed` warns (known member, ordinary); unknown-string
mutant `reconstructed_zzz` -> 1 warn `invalid Global point_class 'reconstructed_zzz' at index 386 -- treating as
interpolated_estimate`. Plus the served chunk `ModelPortfolios-gqyfc1FQ.js` carries `reconstructed(` x1 (absent at
v2.1.161) with positive control `interpolated_estimate` x13.

## Rollback (unchanged, integrator-executed)

`git push origin fbbb9b39a0ce4103eaaf8cdf3f84581d3f244448:PROD` — CI re-deploys whatever lands on PROD.
