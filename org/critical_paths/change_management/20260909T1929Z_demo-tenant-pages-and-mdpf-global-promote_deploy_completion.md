# Deploy Completion Record
**Date opened:** 2026-09-09T19:29:50.168684+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260909T194454Z
**Deploy:** portal DEV->PROD promote: demo tenant gets /attribution + /factor-tilts, ModelPortfolios demo->global (Opal Aggregate). Andrew-direct 2026-09-09.
**Authored by:** 0.4.0_DT_ClientPlatform
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| merge | git | portal PROD merge of origin/DEV | merge commit sha, parity diff empty | merge commit b1389c85759511e65ec5d5b26ee96d63c91984c2 (--no-ff, base 6cb3d0f654ac..., author 0.4.0_DT_ClientPlatform). Parity gate 'git diff origin/DEV HEAD' EMPTY at merge time; diffstat exactly 2 files (src/lib/firmAccess.ts, src/pages/ModelPortfolios.tsx), 56 insertions -- both this seat's. | CLOSED 20260909T194416Z |
| prod-push | git | origin/PROD advanced | git ls-remote refs/heads/PROD read | git ls-remote origin refs/heads/PROD -> b1389c85759511e65ec5d5b26ee96d63c91984c2 (REMOTE read, not a local ref). merge-base --is-ancestor b1389c85 origin/PROD -> YES. Push receipt: 6cb3d0f6..b1389c85 PROD -> PROD. | CLOSED 20260909T194416Z |
| ci | verify | deploy.yml green | gh -R Opal-Capital/portal run list --json filtered to headSha, conclusion success, ALL workflows enumerated | gh -R Opal-Capital/portal run list --json databaseId,headSha,workflowName,status,conclusion filtered to headSha b1389c85 -> ENUMERATED, denominator 1 workflow: run 34396082437 'Deploy to Production' status=completed conclusion=success. Positive control first: gh repo view Opal-Capital/portal -> nameWithOwner Opal-Capital/portal (so an empty list would mean empty, not wrong-repo). | CLOSED 20260909T194416Z |
| tag | git | annotated portal-v2.1.177 | git rev-parse <tag>^{commit} == PROD head (PEELED) | git rev-parse portal-v2.1.177^{commit} -> b1389c85759511e65ec5d5b26ee96d63c91984c2 == origin/PROD head. PEELED per the leg (ls-remote --tags shows the TAG OBJECT sha; comparing that is the v2.1.114 false-double-merge misread). Negative control: portal-v2.1.176^{commit} -> 6cb3d0f6, the prior head, so the peel discriminates. | CLOSED 20260909T194417Z |
| pointer | git | workspace submodule pointer bumped on CLOUD | safe-commit hash + push | safe-commit 99277222d9 on CLOUD: gitlink portal 30ca034b -> 5907cbca. LOCAL by design -- Gate 5 admits a DT serial only for the PORTAL repo's DEV/PROD; workspace branches stay INTEGRATOR-ONLY (0.0.0_AB_MSTR on Andrew's word). | CLOSED 20260909T194417Z |
| teardown | verify | ephemeral worktree pruned, portal main tree on DEV | worktree list + branch --show-current | git -C portal worktree remove FAILED 'Filename too long' (documented Windows behaviour, physical dir is gitignored + inert); worktree prune RAN. git -C portal worktree list -> only C:/.../portal 5907cbca [DEV]. git -C portal branch --show-current -> DEV. pwd -> workspace root. | CLOSED 20260909T194417Z |

## Log

- 20260909T192950Z OPENED by 0.4.0_DT_ClientPlatform with 6 leg(s)
- 20260909T194416Z LEG merge closed: merge commit b1389c85759511e65ec5d5b26ee96d63c91984c2 (--no-ff, base 6cb3d0f654ac..., author 0.4.0_DT_ClientPlatform). P
- 20260909T194416Z LEG prod-push closed: git ls-remote origin refs/heads/PROD -> b1389c85759511e65ec5d5b26ee96d63c91984c2 (REMOTE read, not a local ref). merge-b
- 20260909T194416Z LEG ci closed: gh -R Opal-Capital/portal run list --json databaseId,headSha,workflowName,status,conclusion filtered to headSha b1389c85
- 20260909T194417Z LEG tag closed: git rev-parse portal-v2.1.177^{commit} -> b1389c85759511e65ec5d5b26ee96d63c91984c2 == origin/PROD head. PEELED per the l
- 20260909T194417Z LEG pointer closed: safe-commit 99277222d9 on CLOUD: gitlink portal 30ca034b -> 5907cbca. LOCAL by design -- Gate 5 admits a DT serial only 
- 20260909T194417Z LEG teardown closed: git -C portal worktree remove FAILED 'Filename too long' (documented Windows behaviour, physical dir is gitignored + ine
- 20260909T194454Z CLOSED -- all 6 legs proven
