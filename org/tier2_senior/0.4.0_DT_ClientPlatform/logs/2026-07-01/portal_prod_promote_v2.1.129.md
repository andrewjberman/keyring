# Portal DEV->PROD Promote — v2.1.129

**archetype:** DEPLOY

**Serial:** 0.4.0_DT_ClientPlatform
**Window:** session start 2026-07-01 ~1333Z -> ~1347Z (single task: portal promote, Andrew-direct)

## Summary

TO opened as "Push portal DEV 90322ba0 to opalinvest.dev (DEV-ONLY)". On inspection, portal
`ci.yml` (DEV trigger) only Lints/TypeChecks/Builds + uploads artifacts — it does NOT publish to
any server (only `deploy.yml` on PROD does S3-sync + CloudFront-invalidate + tag). Surfaced this;
**Andrew confirmed** DEV pushes do not reach a server and directed `/prod-deploy` instead (with a
2nd promote expected ~3h once more pre-promote work lands). Ran the canonical DT promote: pushed
90322ba0 to origin/DEV first (CI-validated), then promoted origin/PROD..origin/DEV (3 commits) to
production as **v2.1.129**. Clean run; CI green; tag peel-verified; main tree confirmed back on DEV.

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 0 | /watcher self-heal | was NOT REGISTERED -> registered LIVE (PID 38540); persistent Monitor armed (bkrgsgipa); inbox empty |
| 0 | DEV push of 90322ba0 (pre-promote) | `07d5887f..90322ba0 DEV->DEV`; VALGATE D-1 PASS; CI 28521455051 (ci.yml) validate-only |
| 0 | Andrew correction + /prod-deploy GO | DEV != server-deploy confirmed; promote authorized |
| 0 | FREEZE declared to COO | COO ACK: noted + ENFORCING, relayed DE to hold portal/DEV |
| 1 | Portal tree state | on DEV, tracked-clean, local DEV == origin/DEV |
| 2 | `bun run typecheck` (tsc -b --noEmit) | EXIT 0 |
| 3 | Re-assert local PROD from origin | PROD = origin/PROD = 5c9e5784 |
| 4 | Ephemeral worktree add PROD + bun install | worktree `.runtmp/portal-promote-20260701T133809Z`; bun install 420 pkgs 141s EXIT 0 |
| 4 | `git merge --no-ff origin/DEV` | merge SHA `eb049b7e` (ort strategy, 7 files) |
| 4 | Parity gate `git diff origin/DEV HEAD` | EMPTY (PROD tree == DEV tree) |
| 4 | `git push origin PROD` | `5c9e5784..eb049b7e PROD->PROD`; VALGATE D-1 PASS + tsc gate PASS |
| 5 | CI verify (gh run view --json) | run 28521963790 "Deploy to Production" conclusion=**success** |
| 5 | Tag peel-verify | `portal-v2.1.129^{commit}` = eb049b7e == origin/PROD head (MATCH) |
| 6 | Workspace pointer bump | `7c5c2e09f` -> portal 90322ba0; pushed CLOUD `72088fca1..7c5c2e09f` |
| 7 | Worktree teardown | `--force` de-registered (physical delete failed long-path, residue inert); list shows main DEV tree only |
| 7 | Main tree check | on DEV @ 90322ba0 (Rule 19 held); cwd = workspace root |
| 8 | RAVC to COO | FREEZE RELEASED + promote complete + CI-green PROD reported |

## Deployment Tags

| Pipeline | Tag | Commit |
|---|---|---|
| portal | portal-v2.1.129 | eb049b7e (peel-verified == origin/PROD head) |

## Commits promoted (origin/PROD..origin/DEV)

| Hash | Summary |
|---|---|
| 90322ba0 | fix(AdvisorIntelligence) 49F Advisors tab blank at period boundary + rename Executive Summary -> Summary (CVO-verified GREEN) |
| 07d5887f | feat(cottonwood/COTMVP-B) firm-level Clients roster section (advisor-independent) — Andrew-direct |
| ad97d915 | refactor(INFREF) repoint PartnerAnalytics headline AUA tile _fresh -> canonical getHeaderMetrics().total.aua + remove dead fn/type |

## Files Modified (by the merge)

src/api/endpoints/advisor-intelligence.ts (-43); src/pages/AdvisorIntelligence/_partners/cottonwood/CottonwoodClientsSection.tsx (new +122); .../cottonwood/index.tsx; .../_shared/AdvisorPublicProfile.tsx; .../_shared/components/AdvisorAnalytics.tsx; .../_shared/components/PartnerAnalytics.tsx; .../_shared/tabs/AdvisorsTab.tsx

## Verification (actual output)

- CI run **28521963790**: `{"conclusion":"success","status":"completed","headSha":"eb049b7e..."}`
- Tag **portal-v2.1.129** peeled: `git rev-parse portal-v2.1.129^{commit}` = eb049b7e ==
  `origin/PROD` head eb049b7e (MATCH).
- Parity: `git diff origin/DEV HEAD` EMPTY (no unverified passenger drift).
- Main tree `git -C portal branch --show-current` = DEV.
- Workspace gitlink -> portal 90322ba0, CLOUD 7c5c2e09f pushed.

## Compiler Tools

| Tool | Why | Result |
|---|---|---|
| comp-surface-check | Auto-run by safe-commit.sh on the portal pointer-bump commit (critical-surface gate) | PASS (1 changed file touches no critical surface) |

No comp-* tool deliberately invoked beyond the auto-gate: this is a pure DEV->PROD git promote (DT
lane) with no estate search/inspection/IAM/data-path change in scope. The promote's own gates
(VALGATE D-1, tsc, CI deploy.yml, parity diff, tag-peel) are the verification surface; the
safe-commit surface-check auto-logged above covered the pointer-bump's critical-surface check.

## Current State

Portal **LIVE on PROD at v2.1.129** (`eb049b7e`), CI run 28521963790 success, tag portal-v2.1.129
peel-verified. 49F Advisors period-boundary fix + Summary rename + COTMVP-B firm Clients roster +
INFREF AUA-tile canonical repoint all shipped. Main `portal/` tree back on DEV (`90322ba0`).
Workspace gitlink bumped to DEV HEAD 90322ba0 (`7c5c2e09f`, pushed CLOUD). Freeze window RELEASED
to COO. Ephemeral worktree de-registered; physical `.runtmp/portal-promote-20260701T133809Z`
residue persists (Windows long-path, gitignored, inert). Rollback SHA = 5c9e5784 (prev v2.1.128),
encoded in the merge message.

## Next Steps

- [Andrew/CVO] Live-render / visual QA of the 49F Advisors tab on the served PROD site (their call per the TO).
- [2.0.0_SA_COO] FREEZE RELEASED reported; portal/DEV pushes may resume.
- [DT] 2nd promote expected ~3h once more pre-promote work lands — will re-open a freeze window then. DT idle/available, event-driven; Monitor armed (bkrgsgipa).
