# IRPT paired integration for Andrew's visual smoke

## Production publication verified, 2026-09-23 05:07Z

The earlier provisional Portal3e5 pin is superseded by `a538217980cdb5d15dc67cdcc98794baeb5e2517`: final typecheck caught a missing node env import in the test-only workspace override, repaired at a538 before any publication. Full `bun run typecheck`, full ESLint (0 errors/106 warnings), and `bun run build` then completed successfully on the repaired tree (Vite14.54s). Independent bounded review9d1575ac70 reproduced80 tests/377 assertions and preserved human page/print/nav restrictions.

MSTR published the full multi-author a538 candidate to DEV. Aligning the main DEV checkout through canonical safe-merge created metadata-only `3a298311dfab63928e7b912e0f62355ec8b7ce59`; its tree is byte-identical to a538. P published that sole P-authored commit with the skill's audited Andrew-direct annotation. DEV CI35820519811 completed success.

Canonical `/prod-deploy` sequence: fresh origin PROD base `f2ff7a0af2245cac624ff8a340d5d5e0b10e14aa`; derived ephemeral worktree `.runtmp/portal-promote-20260923T045952Z`; foreground Bun1.3.9 install377 packages completed116.62s; guarded no-ff merge; empty DEV/PROD tree diff; pre-push provenance, VALGATE and TypeScript passed; PROD push succeeded.

| Receipt | Exact value |
| --- | --- |
| DEV | `3a298311dfab63928e7b912e0f62355ec8b7ce59` |
| PROD | `e83ebbfe4f83228f42925b24f77f43e6b6d2a037` |
| Annotated release tag | `portal-v2.1.184`, peeled and equal to PROD |
| PROD workflow | `35820826235`, Deploy to Production, completed/success |
| Job results | Build Production Assets, Deploy to S3 + CloudFront, Tag Deployment: all success |
| Workflow enumeration | Exact PROD SHA has one returned workflow, success |
| Backend consolidation | MSTR merge `92982f4d46` preserves current CLOUD and cd8; remote CLOUD independently read at `3bb0bbdc8ea1c5687e41ceb4546b71356bb1906e` |
| Canonical gitlink commit | `b06c6cd8b6`, portal points to DEV3a298311; MSTR push requested |
| Main portal branch | DEV throughout |

Two inherited backend test failures were independently diagnosed by M/CVO as first-route-per-function fixture selection with a missing selection POST body, reproduced on original M8e2. This is separate from portal deployment; no production guard was weakened. Exact test-only repair f0aead3dcf is a post-freeze follow-up, excluded from this published candidate. No backend render/key/full-E2E hold is lifted. Andrew performs visual smoke.

## Superseding Andrew instruction and assembled publication pins, 2026-09-23 04:46Z

Andrew directly instructed this exact P session:

> i dont need all that, i can manage the visual smoke, i need the most completed version pushed to DEV and then DEV promoted to PROD in canonical form (/prod-deploy claude skill).

Visual-smoke work stopped. The canonical `.claude/skills/prod-deploy/SKILL.md` was read in full. MSTR was sent the multi-author DEV publication payload per Step 1a, and COO was notified of the DEV freeze. P will execute the ephemeral PROD promotion after the coordinated shared DEV push unless MSTR already owns that operation. No extra visual approval is requested.

- Portal immutable candidate: `3e5a6813f1f0194c8381083e6ed117db8f7197bd`, branch/worktree `irpt-smoke-p-portal-20260923`.
- Backend immutable candidate: `cd8d11825424e45fe82f1e78df0396904c0b9ae0`, branch/worktree `irpt-smoke-p-backend-20260923`.
- Portal includes Y `7a5b24e705f79d5df872f9a443b6a552e9de62b9` and remote DEV `b3d5f59b4534eb653105f9bedc9e178384111c9f` through merge `1193bed8`. M portal commits e2df1c04/e001b6d5/d4fca0e5 are all patch-equivalent in Y, independently reproduced by M/CTO/Y. No replay. SecurityAnalysis/MFA and admin/internal/Dev page, print and navigation restrictions retained; prior sanctioned print render delegate retained.
- Backend includes Y cdbd4de74, P d91b2bdd10, M 8e2ba78303 and B 2506c70874; X10 8909d8a77b merged at79c4d64a0c; F89 evidence4d967ed8279 merged atac69336529 and F90 evidence3fd911306d9 merged atcd8d118254. Append-only investigation rows preserved, canonical merge guards passed. Generated owned stamps exactly match the merged registry generator output. X10 remains PENDING_ENFORCEMENT.
- Portal full lint: zero errors,106 warnings. TypeScript and production build passed. The only lint repairs were equivalent ASCII-control checks and removal of invisible whitespace in a comment (5b805110). Test-only3e5a6813 adds explicit IRPT_WORKSPACE_ROOT to support isolated paired checkouts; default nested layout preserved.
- Portal focused checks:64 tests/290 assertions across13 files (admin gate, render delegate, retained selection, upload, dates, public status, owned history, composition);16 analysis/recipient tests/87 assertions across3 files. Mounted header and holdings race scripts both passed. Use IRPT_WORKSPACE_ROOT pointing to the backend candidate and IRPT_CONTRACTS_DIR pointing to its docs/contracts/investor-reporting/v1. Initial missing route-file failure without the latter was corrected by the existing generator configuration.
- Backend X10 placement60 tests passed; isolated Y composition/frozen-worker/canonical-profile36 tests passed. A combined pytest process had module-name contamination; isolated invocation resolved the two Y errors. Legacy guarded-entry tests retain two directory-selection positive-control failures (OBJECT_NOT_COVERED),97 pass; these are reported separately and do not establish runtime acceptance.
- Local preview5442 was started using VITE_IR_USE_FIXTURES=1, PID32536. Computer-use initialization failed; repository browser scripts ran instead. Full-page smoke did not produce a passing capture before Andrew superseded that work. Do not claim a verified preview or real generation/export.

Shared DEV publication, canonical PROD deployment/tag verification and CLOUD pointer receipt are pending below. Main portal remains DEV; unrelated shared dirt and untracked files are preserved. No backend runtime deployment or full E2E acceptance is asserted by the portal promotion.

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
