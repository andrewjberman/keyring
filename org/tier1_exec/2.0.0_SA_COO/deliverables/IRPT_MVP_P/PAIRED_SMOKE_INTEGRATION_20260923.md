# IRPT paired integration for Andrew's visual smoke

Owner: 2.0.0_SA_COO~P. Authority: completion CONTRACT v1.2 and exact CTO inbox notice 20260923T042532Z. Andrew-direct relayed verbatim in that notice, received in this Codex user inbox-event turn on 2026-09-23 at approximately 00:25 Eastern:

> is the most recent portal design promoted? do we need a /prod-deploy to assess? Need to make sure everything is merged from any relevant worktrees for IRPT in both Portal and ajb_workspace repos so I can visually smoke/test now

CTO assigns P paired integration/build, M/Y exact dependencies and patch order. Preserve active work; no unilateral shared merge/push. The request is for a concrete smoke candidate; build/source inclusion and visual inspection do not establish live backend or full E2E acceptance.

## Measured source inventory, 00:26 Eastern

| Repository/worktree | Branch | HEAD | Tracked dirt |
| --- | --- | --- | --- |
| ajb_workspace | CLOUD | 683c36c27785f905a42255b9b27f9fc85fe4e885 | Unrelated shared files and portal gitlink; do not sweep |
| ajb_workspace/portal | DEV | 8e6e2e38cc299c4415d42b0fe627edc50ec35e1b | None; untracked local artifacts |
| irpt-mvp-p-20260922 | irpt-mvp-p-20260922 | d91b2bdd10fe05a0e241ccbfb8f6d7f1b35a872c | None |
| irpt-mvp-p-portal-20260922 | irpt-mvp-p-portal-20260922 | 7411ada3356d1e0c8a69d6eb7b0b41f91396d336 | None; untracked .runtime/ |
| ajb_irpt_m | codex/irpt-m-completion | 8e2ba7830352b2a34c97ec96984d043654cab340 | None |
| ajb_irpt_m_portal | codex/irpt-m-ui | d4fca0e5692730e9f79c3fa013159ffa63ba5b6b | None; untracked .runtime/ |
| irpt-mvp-y-20260922 | irpt-mvp-y-20260922 | cdbd4de74d86c03463eed8068e57c41e0bf8abc1 | None; two .tools commit-message scratch files |
| irpt-mvp-y-portal-20260922 | irpt-mvp-y-portal-20260922 | 7a5b24e705f79d5df872f9a443b6a552e9de62b9 | None |

All listed desktop worktree paths are under C:/Users/AndrewBerman/Desktop/. P has no outstanding code edit; Y042724 explicitly reports no active code/commit/server writer and stable pins. M writer/patch-order confirmation requested. Do not conflate presence of a worktree with an active writer.

Latest reviewed P pair is d91b2/7411, review c5c3393b1f. Y reports latest backend consumer review64c5bc59a3 on exactcdbd and UI race closure1ebdadd0d4 on exact7a5. M confirmation is pending. Original B/F round holds and runtime/full-product limits are not silently lifted.

## Concrete integration work

Created isolated portal branch/worktree `irpt-smoke-p-portal-20260923` from Y7a5. Isolated backend branch/worktree `irpt-smoke-p-backend-20260923` is being created from Ycdbd. These existing integrated Y snapshots include P changes; blindly replaying all P/M commits would duplicate already-consumed patches. Check exact source content and owner handoffs before adding missing completed work.

Shared portal DEV is still F8e6, so it does not contain the current P/Y UI integration. This is a measured source fact, not a measurement of the deployed site's bytes. Build and targeted consumer verification are pending. No promotion/deployment claim is made.

## Current hazards and next proof

Preserve unrelated shared-root dirt and all scratch/untracked content. Do not use a bulk add, broad reset or shared checkout. Verify B/F final accepted source is represented, compare M/Y owned surfaces and route/schema/package inputs, build the exact portal tree, and provide a candidate-specific smoke procedure. Missing backend runtime routes, provider access, actual accepted data and render/export prerequisites remain separate from whether the latest UI can be visually inspected.
