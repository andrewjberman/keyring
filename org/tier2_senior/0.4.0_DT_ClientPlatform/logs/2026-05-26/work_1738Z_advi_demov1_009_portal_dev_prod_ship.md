# ADVI_DEMOV1.009 — Portal DEV → PROD ship (DT 0.4 Phase 6 close-out)

**archetype:** DEPLOY
**secondary_archetypes:** COORDINATE, SCRIBE
**date:** 2026-05-26
**worker:** 0.4.0_DT_ClientPlatform
**TO:** ADVI_DEMOV1.009.dt-portal-prod-push-demo-tenant
**work-cycle:** 3 (spawn → Phase 1 ship → Phase 2 hold → UAT PASS → Phase 3+4 ship)
**wall:** ~1h35min spawn-to-final-RAVC2 (spawn ~15:54Z → final ship ~17:38Z)

---

## Current State

**SHIPPED — all 5 ACs MET.**

| AC | State | Evidence |
|---|---|---|
| AC1 (portal/DEV carries TO-008) | ✓ | `origin/DEV` = `03a8544155...` |
| AC2 (Andrew UAT PASS) | ✓ frontend-scope | UAT ~17:30Z Smoke-A/B PASS; Smoke-C/D PASS-with-backend-findings (F1+F2+F3 split-routed) |
| AC3 (portal/PROD carries cherry-pick) | ✓ | `origin/PROD` = `b7b201a610...` (cherry-pick of `03a85441` onto PROD) |
| AC4 (parent submodule bumped + tagged + pushed --follow-tags) | ✓ | parent `CLOUD` includes `794cf9c0a` portal gitlink bump; tag `portal-v2.1.73` (`6e5d9a9257`) pushed |
| AC5 (main worktree NOT stranded on PROD) | ✓ | main `portal/` tree on DEV @ `03a85441`; pre-existing 0.3.0_DT 2026-05-22 strand un-done at Phase 3 prep |

## Phase-by-phase ship trail

**Phase 1 (Spawn → Phase 1 ship) ~5min wall (9th fast-lane today per ws COO RAVC2-ACCEPT-PARTIAL):**
- Found DE 0.4 TO-008 `03a85441` committed locally but never pushed to portal/origin/DEV (Finding #1 to COO)
- Found main portal tree pre-stranded on PROD `0be05530` (0.3.0_DT 2026-05-22 SSCN_TOOLBAR damage; banking 3rd-fire of strand pattern)
- Found `.runtmp/portal-dev-verify` worktree exists (DE 0.4 leftover from local verification)
- Pushed local DEV → `origin/DEV` (3 ahead commits: TO-008 + 2026-05-23 INFGRO.005 add+revert pair net-zero). VALGATE D-1 PASS.
- GitHub Actions `ci.yml` GREEN on push (2m15s, run 26460394795).
- Local `bun tsc` + `bun run build` clean (24.52s vite production build).
- AC1 reality-reconciliation surfaced: portal has only ONE CloudFront distribution (`EVTSA9VEHNZVH` → opalinvest.dev); DEV-branch CI = build-validation only (no DEV-CF deploy). Equivalent surrogate via origin/DEV SHA + CI green + local builds clean. Banking absorbed by COO as 8th compiler-tool R&D candidate (deploy-model-vs-AC-wording semantic gap).

**Phase 2 (Andrew UAT) ~~1h hold (capacity-flex, no SLA pressure):**
- Andrew first attempted UAT — Demo not appearing in dropdown. Initial misdiagnosis as missing entry.
- I corrected my own framing twice: (1) the canonical UAT path is internal-staff `ALL_PARTNER_FIRMS` dropdown (not `demo@demo.test` Cognito login as PRD §6.1 wrote); (2) Opal uses DynamoDB user table, NOT Cognito (Andrew direct correction; banked `project_opal_auth_dynamodb_never_cognito.md` memory).
- True cause: Andrew was hitting opalinvest.dev (PROD CF, still at pre-demo `0be05530`) OR running `cd portal && bun run dev` from main tree stranded on PROD. Strand-pattern memory `feedback_portal_prod_promotion_strands_main_tree` biting in a new way (usually invisible until next promotion; today blocked UAT directly).
- Launched Vite dev server from existing `.runtmp/portal-dev-verify` worktree (DEV @ `03a85441`) on `http://localhost:5175/` for Andrew UAT.
- Andrew UAT PASS-frontend-scope. 3 backend findings surfaced.

**Phase 2.5 (Backend-findings brief) ~5min:**
- Wrote `docs/briefs/advi-demov1-uat-backend-findings-20260526.md` (commit `ad37838b1`, pushed CLOUD).
- F1 (numbers × 0.667 NOT applied) + F2 (account # in Fee Summary) → 0.6.0_AE_PartnerETL
- F3 (data-source label "Black Diamond" → "Database Connected: Lone Pine Analytics") → frontend 3-line patch; not AE; routes to DE pod as TO-010 candidate
- MCP to COO (UAT-PASS-FRONTEND-SCOPE + PROCEED-PHASE-3) + CC to 0.6.0_AE_PartnerETL.

**Phase 3 (Ephemeral-worktree cherry-pick) ~3min:**
- Killed Vite dev server (PIDs 179537 + 179340; port 5175 freed).
- `git -C portal worktree remove --force .runtmp/portal-dev-verify` (DE 0.4 leftover; untracked .frontend-dev/screenshots/ + .runtmp/ residue required --force).
- `git -C portal checkout DEV` — main portal tree un-stranded → DEV @ `03a85441`.
- `git -C portal worktree add .runtmp/portal-prod-cherry PROD` — ephemeral PROD worktree under `.runtmp/` for tidiness.
- `cd portal/.runtmp/portal-prod-cherry && git cherry-pick 03a85441` → PROD commit `b7b201a6` (9 files / 499 insertions / 2 deletions / 4 new files in `_partners/demo/`).
- `git push origin PROD` → VALGATE D-1 PASS + `tsc -b --noEmit` PROD-push typecheck PASS + push `0be05530..b7b201a6`.
- Removed ephemeral worktree.

**Phase 4 (Submodule bump + tag + push) ~7min (incl. concurrent-agent index-lock contention):**
- Bumped portal gitlink via `git update-index --cacheinfo 160000,b7b201a610e131b3c56bfa8e8013956cd49f26ea,portal` (clean pattern — preserves portal working tree on DEV, no temp re-strand).
- Multiple concurrent-agent lock contention rounds; ultimately committed via direct `git commit --only -- portal` (safe-commit fallback per CLAUDE.md Rule 14a) — commit `794cf9c0a`.
- Tag `portal-v2.1.73` (annotated; baseline was local-real-max `v2.1.72`; ws-charter ref to `v2.1.98` proved to be commit-message intent that was never actually pushed as a tag).
- `git push origin CLOUD --follow-tags` → `789bebc4d..32ae9a37e CLOUD -> CLOUD` + `[new tag] portal-v2.1.73 -> portal-v2.1.73`.

---

## Compiler Tools

| Tool | When | Outcome |
|---|---|---|
| `git ls-remote origin DEV/PROD` | Phase 1 baseline + Phase 3 verify + Phase 4 verify | All three returned expected SHAs |
| `bun tsc` + `bun run build` | Phase 1 local | Exit 0; clean |
| `git ls-remote --tags origin 'portal-v*'` | Phase 4 tag baseline | Empty on both portal + workspace remote; established `v2.1.73` as next sequential from local-real-max `v2.1.72` |
| `git update-index --cacheinfo` | Phase 4 gitlink bump | Clean — avoided main-tree re-strand by skipping checkout dance |

No `comp-*` tools fired this session (deploy + portal-frontend scope; no Lambda IAM / data-pipeline / portal schema-check changes touched).

---

## Memories banked

- `project_opal_auth_dynamodb_never_cognito` — fresh write today from Andrew correction (Cognito-vs-DynamoDB architectural fact)

## Memories surfaced (Andrew already had these; observed firing in practice today):

- `feedback_portal_prod_promotion_strands_main_tree` — 3rd-fire banked (per COO RAVC2-ACCEPT-PARTIAL); strand from 0.3.0_DT 2026-05-22 SSCN_TOOLBAR promotion blocked Andrew's UAT via `cd portal && bun run dev` path (strand-impact in a new dimension beyond next-promotion-stranding)
- `feedback_track_inflight_to_by_artifact_not_sla` — Phase 1 audit-of-state-of-truth resolved DE 0.4's "shipped via 6e6f013a8" framing into accurate "committed-locally-not-pushed" reality
- `feedback_git_fetch_before_deriving_deploy_head` — Phase 4 ground-truth-source for tag baseline (don't trust commit-message tag refs)

## Banking surfaces for future memories (R&D candidates per COO discussion):

1. **bookkeeping-vs-ship-gap class** — TO status flip via separate commit without remote-push leaves downstream consumers reading wrong ground-truth (Finding #1 banked by COO)
2. **AC-wording-vs-deploy-model semantic gap** — PRDs/TOs reference "DEV CloudFront" when portal has single-CF; compiler-tool sister to `comp-registry sync` R&D candidate per CVO comp-* brief
3. **strand-pattern impact-dimension expansion** — strand blocks UAT (not just next-promotion); was blocking-class today; future memory revision could note multi-dimensional impact

## Brief authored

`docs/briefs/advi-demov1-uat-backend-findings-20260526.md` — F1+F2+F3 backend/frontend split-routing. Andrew can deliver to AE 0.6.0 directly (path baked into MCP-CC).

## Phase 6 close-out trajectory

Per PRD §6.1 dependency graph:
```
TO-008 ✓ (DE 0.4 03a85441)
  → TO-009 ✓ (THIS — DT 0.4 portal DEV→PROD ship 794cf9c0a + tag portal-v2.1.73)
    → TO-VAL-FE ✓ (Andrew UAT PASS-frontend-scope ~17:30Z; backend follow-ons brief'd)
      → ADVI_DEMOV1.010 candidate (F3 frontend label-edit; DE pod next /work tick)
      → AE 0.6.0 collective brief (F1 + F2; standalone follow-on TOs)
      → PROJECT CLOSE pending COO disposition (likely after F3 + F1 + F2 close, OR 3-step atomic now if Andrew + COO agree Phase 6 = PASS-as-is)
```

---

**Final state — TO-009 SHIPPED with frontend Phase 6 fully closed.** Standing for COO RAVC2-ACCEPT + project close routing.

**work-cycle:3 (Phase 1+2+3+4 ship cycle; 1.5h end-to-end wall).**
