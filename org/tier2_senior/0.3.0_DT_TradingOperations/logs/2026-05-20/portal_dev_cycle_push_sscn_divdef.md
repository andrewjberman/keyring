# Session Log — Portal DEV-cycle pushes + DEV smoke server (SSCN_DIVDEF + TRSB_LEDGER)

**Agent:** 0.3.0_DT_TradingOperations (DevOps Technician — Trading Operations)
**Date:** 2026-05-20
**Projects:** SSCN_DIVDEF (TO-006 PROD push staged), TRSB_LEDGER (TO-012 PROD push staged)
**Session type:** Portal DEV-branch syncs + DEV smoke verification surface — NO PROD push (both gated on Andrew smoke approval)

## Session Summary

Session-start startup, then two portal DEV-cycle syncs and a DEV smoke server brought
up for Andrew's combined SSCN + TRSB verify. No PROD deploy — both PROD pushes
(`SSCN_DIVDEF.006`, `TRSB_LEDGER.012` Phase 1) remain `dispatch_held`/staged pending
Andrew's DEV smoke approval.

## Startup

- Registered `0.3.0_DT_TradingOperations` (PID 19808); inbox-watch launched (PATH wrapper).
- Read README + prompt + recent logs (2026-05-19: portfolio-management-v2.1.1 openpyxl
  P0 closed; SSCN_DIVDEF.002 COO-executed).
- comp-graph context set to `SSCN_DIVDEF.006.dt-portal-dev-to-prod-push`.
- Task queue: `SSCN_DIVDEF.002` complete; `SSCN_DIVDEF.006` STAGED `dispatch_held=true`.

## Work Item 1 — DEV-cycle sync to b05388dc (COO 2.0.0_SA_COO GO)

DE 0.3.0 flagged portal/DEV push-ready inventory. Surfaced to COO that portal/DEV had
drifted past the 3 SSCN commits (7 commits ahead of origin/DEV incl. cross-pod MDPF
`543a5eea`). COO GO'd the DEV-branch sync.

| Step | Action | Result |
|------|--------|--------|
| 1 | git fetch (portal + parent) | portal/DEV 7 ahead of origin/DEV; CLOUD gitlink stale @ 23e8ab14 |
| 2 | Bench QA, portal DEV HEAD 00841008 | `bun install` 461 pkgs no changes / `typecheck` 0 / `lint` 0 (11 warn) / `build` 0 (12.39s) |
| 3 | `git push origin 00841008:DEV` (portal) | origin/DEV 23e8ab14..00841008 (7 commits) |
| 4 | Parent gitlink bump -> 00841008 | commit `ea8c34748` (index-sweep — see Anomaly) |

## Work Item 2 — DEV-cycle sync advanced to b05388dc (.007/.008 RAVC-closed)

`.007` (a844f0dd, layout revert) + `.008` (b05388dc, Presets dropdown) RAVC-closed during
the session. COO pre-authorized the follow-up DEV push.

| Step | Action | Result |
|------|--------|--------|
| 5 | `git push origin DEV` (portal) | origin/DEV 00841008..b05388dc (a844f0dd + b05388dc) |
| 6 | Parent gitlink bump -> b05388dc via safe-commit.sh | commit `f7123a375` — clean, 1 file |
| 7 | `git push origin CLOUD` | origin/CLOUD 9ddbfe529..f7123a375 (20 commits) |

## Work Item 3 — DEV smoke server + SSCN smoke (COO GO)

| Step | Action | Result |
|------|--------|--------|
| 8 | Determine DEV smoke surface | No deployed DEV env per `portal/DEPLOY_HERE.md` — DEV push = CI only; smoke is local |
| 9 | `bun run dev --port 5175` on portal DEV @ b05388dc | Vite v7.3.1 ready, http://localhost:5175 |
| 10 | Headless Chrome on CDP :9444 + SSCN smoke runner | 21/21 PASS, 0 console errors |

Smoke confirmed: Presets dropdown defaults `divz` (`constants.ts:97` label `DIVZ -- Dividend`);
`.007` revert verified (no preset-groups strip, no ranking-method control, step=1 inputs);
`.005` universe dropdown exactly 5 options, r1000 default, no legacy leak.

## Work Item 4 — DEV-cycle sync to f9b2d81e + server refresh (CTO 1.0.0_SA_CTO~B request)

CTO~B requested :5175 refreshed to the DEV tip so Andrew verifies SSCN + 5 TRSB_LEDGER
portal fixes in one sitting.

| Step | Action | Result |
|------|--------|--------|
| 11 | Bench QA, portal DEV HEAD f9b2d81e | `typecheck` 0 / `build` 0 (12.28s) |
| 12 | `git push origin DEV` (portal) | origin/DEV b05388dc..f9b2d81e (be5d7631 .008b + f9b2d81e .014) |
| 13 | Parent gitlink bump -> f9b2d81e via safe-commit.sh | commit `b33e7a477` — clean, 1 file; CLOUD pushed |
| 14 | Kill old Vite (PIDs 3672/26796), restart `bun run dev --port 5175` | Vite ready, serving DEV @ f9b2d81e |
| 15 | Re-run SSCN smoke runner on f9b2d81e | 21/21 PASS, 0 console errors — SecurityScanner unchanged |

## Work Item 5 — DEV-cycle sync to 7ef0f4a6 + server refresh (COO refresh request)

`SSCN_DIVDEF.010` (FactorBank "Category"->"Group" relabel + 4-color polish) closed —
portal DEV commit `7ef0f4a6`. COO asked to refresh :5175 so the smoke surface carries
the full SSCN portal set (.007 + .008 + .010).

| Step | Action | Result |
|------|--------|--------|
| 16 | Bench QA, portal DEV HEAD 7ef0f4a6 | `typecheck` 0 / `build` 0 (17.34s) |
| 17 | `git push origin DEV` (portal) | origin/DEV f9b2d81e..7ef0f4a6 |
| 18 | Parent gitlink bump -> 7ef0f4a6 via safe-commit.sh | commit `a756bde3a` — clean, 1 file; CLOUD pushed |
| 19 | Kill old Vite (PID 8848), restart `bun run dev --port 5175` | Vite ready, serving DEV @ 7ef0f4a6 |
| 20 | Restart headless Chrome (CDP :9444 had died), re-run SSCN smoke | 21/21 PASS, 0 console errors |

The 2 SecurityScanner files flagged earlier as uncommitted WIP (`FactorBankTab.tsx`,
`categoryOrder.ts`) were committed AS `7ef0f4a6` = SSCN_DIVDEF.010 — confirmed SSCN
scope, not foreign. portal/DEV working tree now clean.

## Deployment Tags

| Pipeline | Tag | Commit | Note |
|----------|-----|--------|------|
| (none) | — | — | No Terraform/Lambda/EC2 deploy this session. Portal branch syncs only; portal PROD ship is GitHub-Actions-driven and gated on Andrew smoke. |

## Verification

```
portal origin/DEV         = 7ef0f4a6d1cefb1196782904e6cd0e03c5459289
parent portal gitlink     = 7ef0f4a6  (== origin/DEV tip; commit a756bde3a)
:5175 dev server          = UP, serving portal DEV @ 7ef0f4a6
SSCN smoke (7ef0f4a6)     = 21/21 PASS, 0 console errors
```

Served build carries: SSCN_DIVDEF .001/.005/.007/.008/.010 + all 5 TRSB portal fixes
(bc5da3d2 + 43b36707 + 00841008 + be5d7631 + f9b2d81e) + cross-pod MDPF 543a5eea.

SSCN portal commit set (for .006 authoring): 45ea7210 + 2254437c + b302f5cf (.001/.005)
+ a844f0dd (.007) + b05388dc (.008) + 7ef0f4a6 (.010).

## Anomaly — concurrent staged-index sweep on ea8c34748

The first gitlink bump (`ea8c34748`, 23e8ab14->00841008) required an index-based bare
`git commit`: the target gitlink (00841008) was NOT the submodule's working-tree HEAD
at the time (a844f0dd, in-flight .007), so `safe-commit.sh --only -- portal` (which reads
working-tree HEAD) would have committed the wrong gitlink. `git diff --cached --name-only`
verified `portal` only immediately before the commit, but DE 0.3.0 ran `git add` on their
`.008` session log in the window between that check and `git commit` — so `ea8c34748`
swept in `SSCN_DIVDEF.008_presets_dropdown.md`.

- DE 0.3.0 confirmed via MCP: content correct + complete, "no action needed."
- NOT history-rewritten — `ea8c34748` already had a child commit; removing the file would
  need rebase (Windows-dangerous per the reference-transaction-hook rebase-hang) or
  `reset --soft HEAD~2` (rewrites a DE commit, out of scope). Benign contamination
  (DE's own complete log, intended for commit) does not justify either.
- Flagged to COO; COO closed it (authorship-only drift, not worth a destructive rebase).
- Subsequent gitlink bumps (`f7123a375`, `b33e7a477`) went through `safe-commit.sh`
  cleanly — submodule working-tree HEAD == target gitlink, so `--only` was exact.

Lesson: a gitlink-to-non-HEAD bump cannot use `safe-commit.sh --only`; the index-based
path has an unavoidable race window on the shared multi-agent CLOUD branch.

## Open observations

- The 2 SecurityScanner WIP files flagged mid-session (`FactorBankTab.tsx`,
  `categoryOrder.ts`) were committed as `7ef0f4a6` = SSCN_DIVDEF.010 — resolved, SSCN
  scope confirmed, no foreign-scope contamination. portal/DEV working tree clean.
- Chrome headless on CDP :9444 died once mid-session (silent exit); restarted with a
  fresh `--user-data-dir`. The smoke runner has no auto-relaunch — if re-smoking, verify
  `curl :9444/json/version` first.
- `deployment_map.xml` does not record the portal deployment surface (opalinvest.dev /
  S3 `opalinvest-portal` / CloudFront `EVTSA9VEHNZVH` / GHA `deploy.yml`). Doc gap — to
  add on the TO-006 close commit.

## Compiler Tools

| Tool | Result |
|------|--------|
| (none applicable) | This session was git branch-sync + gitlink bumps + a local dev-server smoke. No gold script, no portal component edit by this agent, no Terraform, no boto3 change — the comp-* triggers (`comp-pipescript io`, `comp-iam service`, `comp-transform schema-check`, `comp-routes behaviors`) do not apply to a pointer-only push or a server bring-up. TO-006 PROD push, when GO'd, carries `comp-routes trace getUniverseScanner` + `comp-cache collisions` per its `<compiler_tools_mandate>` — to be run at that time. |

## Current State

- portal origin/DEV synced to 7ef0f4a6; CLOUD gitlink synced (a756bde3a); CLOUD pushed.
- :5175 dev server UP, serving portal DEV @ 7ef0f4a6 — SSCN smoke 21/21 PASS, 0 errors.
- SSCN_DIVDEF .002/.003/.004/.005/.007/.008/.010 closed. TO-006 (PROD push) remains.
- `SSCN_DIVDEF.006` STAGED `dispatch_held=true` — gate: Andrew DEV smoke approval
  AND SSCN_DIVDEF.009 close (AE 0.5.0 Phase 3, registry/Lambda data side).
- TRSB_LEDGER .008b + .014 portal commits on the served build — combined-verify surface.

## Next Steps

1. **[Andrew]** Combined DEV verify at http://localhost:5175 — `/security-scanner` (SSCN)
   + TradeSubmission page (TRSB history visibility / role-gated tabs / EXECUTED relabel).
2. **[2.0.0_SA_COO]** On Andrew SSCN approval: author/fire the `SSCN_DIVDEF.006` GO —
   SSCN-commit-set-only PROD promotion (not a blanket DEV->PROD ff). Lock commit list + mechanism with CTO.
3. **[1.0.0_SA_CTO~B]** On Andrew TRSB approval: fire `TRSB_LEDGER.012` Phase 1 PROD push GO.
4. **[0.3.0_DT_TradingOperations]** On GO(s): promote the SSCN (and/or TRSB) commit set to
   portal/PROD -> `git push origin PROD` -> GHA `deploy.yml` auto-ships to S3 `opalinvest-portal`
   + CloudFront `EVTSA9VEHNZVH` -> https://opalinvest.dev. PROD URL smoke per TO-006 AC1-AC8.
   Add the portal deployment surface to `deployment_map.xml` on the close commit.
