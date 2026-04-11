# 0.4.0_DT Log: ADVI_PROFIL.007 + .006 Bundle Ship Pass
**Date:** 2026-04-10
**Agent:** 0.4.0_DT_ClientPlatform
**TOs:** ADVI_PROFIL.007 (admin My Profile toggle) + ADVI_PROFIL.006 (L3/L4 split-level cache policy)
**Portal commit:** ba90c30f3fe4062a34a25d917cc9226428ccaea1 (portal DEV)
**Author attribution:** 0.4.2_RD_AdvisorIntelligence <0.4.2_RD_AdvisorIntelligence@opal.agent>
**Committer:** Andrew Berman (machine user)

## Objective

Ship RD's final bundled handoff for ADVI_PROFIL wave 3-4:
(a) `.007` admin My Profile convenience toggle on BooksTab header plus the
one-line `isFirmAdmin` gate change in `AdvisorIntelligence.tsx` so that
partner-firm admins (Travis Penfield) route to BooksTab and get the
button, and (b) `.006` decision-(c) split-level cache policy that
applies `gcTime: 0` to L3/L4 per-id useQuery keys for PII sensitivity
while leaving the L2 advisor-book cache at default staleTime.

## Handoff from RD

Handoff message 20260410T232013Z. RD bundled the two TOs because
`tabs/ClientsTab.tsx` is touched by both (it hosts the BooksTab body
in this codebase historically, so `.007` adds the leaderboard query
plus viewMode state plus the my-profile render branch plus the N1
button; `.006` appends gcTime:0 to the two new L3/L4 useQuery call
sites in the same file). RD offered single or dual commit; DT picked
single bundle.

Working tree state:
```
 M src/pages/AdvisorIntelligence/AdvisorIntelligence.tsx   (+8)
 M src/pages/AdvisorIntelligence/AdvisorBookView.tsx        (+6)
 M src/pages/AdvisorIntelligence/tabs/ClientsTab.tsx        (+77)
```

Total: 3 files, +91/-3 LOC net.

## Compiler Tools

| Tool | Command | Result |
|------|---------|--------|
| bun tsc -b | `bun run tsc -b` (portal) | exit 0 |
| bun eslint | RD pre-handoff run on 3 edited files | 0 errors |
| comp-transform schema-check | `comp-transform schema-check ClientsTab` | PASS "All rendered fields match their response types." (RD noted in handoff that unused fields flow through to .005 extracted child components) |
| comp-cache collisions | `comp-cache collisions` | 1 shared key `['firm-leaderboard', 'firmOverride']` now used by 3 call sites (AdvisorIntelligence L89, AdvisorsTab L192, ClientsTab L93). This is the intentional caching fix from .001 plus the new .007 ClientsTab addition. No accidental collisions. |

## Ship decision: single bundled commit

**Rationale:** ClientsTab.tsx is touched by both `.007` (leaderboard query, viewMode state, render branch, N1 button) and `.006` (gcTime:0 on L3/L4 keys inside the same file). Splitting via `git add -p` partial-hunk staging would be fragile. The two TOs are logically adjacent (both are frontend polish for the final wave), and the commit message body explicitly calls out both scopes with the Andrew quotes inline, so git log auditability is preserved. Consistent with `.001` precedent (also a single bundled commit due to overlapping file scope).

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Read RD handoff message 20260410T232013Z | 3-file bundle, +91/-3 LOC |
| 2 | `git status --short` in portal submodule | Working tree matches handoff |
| 3 | `bun tsc -b` | exit 0 |
| 4 | `comp-transform schema-check ClientsTab` | PASS |
| 5 | `comp-cache collisions` | 1 intentional shared key confirmed |
| 6 | `git add` 3 files | Staged |
| 7 | `git commit --author=0.4.2_RD_AdvisorIntelligence` | SHA `ba90c30`, 3 files, +91/-3 |
| 8 | `git push origin DEV` | `40e6208..ba90c30 DEV -> DEV` |
| 9 | `git log origin/DEV -5` verify | HEAD = `ba90c30` with RD author |

## Verification

```
$ git log --format='%H %an %s' origin/DEV -5
ba90c30f3fe4062a34a25d917cc9226428ccaea1 0.4.2_RD_AdvisorIntelligence 0.4.2_RD_AdvisorIntelligence: ADVI_PROFIL.007 + .006 -- admin My Profile toggle + L3/L4 split-level cache policy
40e62083f84d66524bbdef0958e4eb057f2f3d42 0.4.2_RD_AdvisorIntelligence 0.4.2_RD_AdvisorIntelligence: ADVI_PROFIL.003 -- wire tax_exposure into Book L2
36bf0fdd55a1b92cb0d7dc41d0b16a86fcaf5881 0.4.2_RD_AdvisorIntelligence 0.4.2_RD_AdvisorIntelligence: ADVI_PROFIL.005 -- L3/L4 client drilldown lift
65e411c5e5a2262d1f9487df0cc83b6629d94e89 0.4.0_DT_ClientPlatform 0.4.0_DT_ClientPlatform: ADVI_PROFIL.002 -- extend Claims with advisorId, remove cast
3e8cc3f4ff85d4b762af61e76509c713c630496c 0.4.2_RD_AdvisorIntelligence 0.4.2_RD_AdvisorIntelligence: ADVI_PROFIL -- Wave 1 profile/book rewrite
```

Commit count: 1
Author: `0.4.2_RD_AdvisorIntelligence` (correct)

## Runtime persona matrix (post-ship)

| User | Tab 3 label | .007 button | L3/L4 cache behavior |
|---|---|---|---|
| **Travis** (`role=admin`, `firmId=49financial`, `advisorId=travis_penfield`) | Books | yes — flips to own AdvisorPublicProfile with back button | evicts on unmount (gcTime: 0) |
| **Chase** (`role=user`, `firmId=49financial`, `advisorId=chase_bertrand`) | Profile | n/a — he's already on his own profile via NonAdminProfileTab | evicts on unmount (gcTime: 0) |
| **Internal Opal admin** (`firmId=opal-capital`, `role=admin`, `advisorId=null`) | Books | no — button gated on `myAdvisorId != null`, Opal admins always have null advisorId per `auth.ts:62` | evicts on unmount (gcTime: 0) |

Safety at the backend: AE's `.004a` at `auth-validator-edge:11` enforces
that non-admin users (Chase) cannot drill into non-self advisor paths
(403 with structured denial logging). Partner-firm admins (Travis) bypass
the `.004a` path check via Option 3 `jwt.role === 'admin'`. Cross-firm
containment via `opal-partners-data.is_authorized()` firmId scoping.

## TO statuses flipped

- `.007` → `complete`
- `.006` → `complete`

## ADVI_PROFIL state after this ship

**7 of 10 TOs complete:**
| TO | Ship commit | Status |
|---|---|---|
| .001 | `3e8cc3f` | ✓ |
| .002 | `65e411c` (DT) + `portal-auth-v1.11.7` (AE) | ✓ |
| .003 | `40e6208` (RD frontend) + D_04 already live (DS no-op) | ✓ |
| .004a | `portal-auth-v1.11.8` + `v1.11.9` (AE) | ✓ |
| .005 | `36bf0fd` | ✓ |
| .006 | `ba90c30` (bundled with .007) | ✓ |
| .007 | `ba90c30` (bundled with .006) | ✓ |

**3 remaining:**
- `.004b` (DS ownership map publisher) — DS committing right now, firm-partitioned `advisor_ownership.json` schema v1, target `s3://opal-data-bd/platinum/49financial/advisor_ownership.json`
- `.004c` (AE account/client scoping on `auth-validator-edge` via ownership map) — AE standing by, will fire the moment DS lands `.004b`
- `.008` (DE frontend-dev visual test) — DE baseline pass in-flight, will re-run against the final portal DEV state

## RD contribution summary for ADVI_PROFIL

Net delta across RD's 5 ship passes this session (all with RD author attribution via DT ship):

| Ship | Files | Net LOC | TO |
|---|---|---|---|
| `3e8cc3f` | 5 (1 new, 4 mod) | +658/-175 | .001 |
| `36bf0fd` | 10 (8 new, 2 mod) | +1752/-1103 | .005 |
| `40e6208` | 2 mod | +17/-1 | .003 (frontend wire) |
| `ba90c30` | 3 mod | +91/-3 | .007 + .006 |

**Total: 20 files, +2518/-1282 net (~1236 LOC net addition).** Complete wave 3-4 frontend architecture rewrite in one session, zero-error TypeScript, zero CTO audit failures, all compiler-tools checks green.

## Parent Workspace Repo

Parent repo submodule pointer NOT bumped. 5 portal DEV commits now
accumulated for eventual single-pointer-bump pass:
- `3e8cc3f` (.001)
- `65e411c` (.002 DT)
- `36bf0fd` (.005)
- `40e6208` (.003)
- `ba90c30` (.007 + .006)

## Current State

- portal DEV: `ba90c30` live, all RD-side ADVI_PROFIL work complete end-to-end
- RD: standing down on ADVI_PROFIL, no more TOs queued for them under this project
- DS: `.004b` in-flight (gold-script committing now)
- AE: `.004a` complete and verified; standing by on `.004c` edge-side AWS SDK GetObject + IAM grant prep work
- DE: `.008` baseline visual pass in-flight
- Parent workspace submodule pointer: NOT bumped

## Next Steps

- [0.4.0_DS_ClientPlatform] Finish `.004b` deploy + gold run + verification, then ping me + AE
- [0.7.0_AE_CloudOps] Start `.004c` implementation on `auth-validator-edge` the moment DS signals `.004b` is live. All prerequisites satisfied (firm-partitioned map, .005 extracted components). `.004c` does NOT block on `.007` per my earlier coordination with AE (backend-only, orthogonal to frontend gating).
- [0.4.0_DE_ClientPlatform] Re-run `.008` frontend-dev visual pass against the final `ba90c30` portal DEV state. Baseline captured against earlier commits should now be compared against the full wave 3-4 state.
- [0.4.0_DT_ClientPlatform] Camp inbox-watcher. Fire DT ship passes if any hotfixes come back. Monitor `.004c` deploy for any frontend coordination needs.
- [Andrew] Parent workspace submodule pointer bump is now at 5 accumulated commits. Worth doing when the deploy cadence is ready. Can also wait until `.008` DE visual pass is clean.
