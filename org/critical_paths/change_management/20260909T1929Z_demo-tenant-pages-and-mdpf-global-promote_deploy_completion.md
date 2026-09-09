# Deploy Completion Record
**Date opened:** 2026-09-09T19:29:50.168684+00:00
**Status:** OPEN
**Deploy:** portal DEV->PROD promote: demo tenant gets /attribution + /factor-tilts, ModelPortfolios demo->global (Opal Aggregate). Andrew-direct 2026-09-09.
**Authored by:** 0.4.0_DT_ClientPlatform
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| merge | git | portal PROD merge of origin/DEV | merge commit sha, parity diff empty |  | OPEN |
| prod-push | git | origin/PROD advanced | git ls-remote refs/heads/PROD read |  | OPEN |
| ci | verify | deploy.yml green | gh -R Opal-Capital/portal run list --json filtered to headSha, conclusion success, ALL workflows enumerated |  | OPEN |
| tag | git | annotated portal-v2.1.177 | git rev-parse <tag>^{commit} == PROD head (PEELED) |  | OPEN |
| pointer | git | workspace submodule pointer bumped on CLOUD | safe-commit hash + push |  | OPEN |
| teardown | verify | ephemeral worktree pruned, portal main tree on DEV | worktree list + branch --show-current |  | OPEN |

## Log

- 20260909T192950Z OPENED by 0.4.0_DT_ClientPlatform with 6 leg(s)
