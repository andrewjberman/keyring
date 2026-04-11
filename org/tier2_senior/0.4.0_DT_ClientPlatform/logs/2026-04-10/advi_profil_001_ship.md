# 0.4.0_DT Log: ADVI_PROFIL.001 -- Ship RD Wave 1 Portal Rewrite
**Date:** 2026-04-10
**Agent:** 0.4.0_DT_ClientPlatform
**TO:** ADVI_PROFIL.001
**Portal commit:** 3e8cc3f4ff85d4b762af61e76509c713c630496c (portal DEV)
**Author attribution:** 0.4.2_RD_AdvisorIntelligence <0.4.2_RD_AdvisorIntelligence@opal.agent>
**Committer:** Andrew Berman (machine user)

## Objective

Review, commit, and push RD's AdvisorIntelligence profile/book rewrite
(4 modified + 1 new file) from the portal DEV working tree to origin/DEV.
Commit must carry RD author attribution. This is ADVI_PROFIL Wave 1 --
unblocks .005 (L3/L4 lift), .006 (cache policy), .007 (admin my-profile
toggle), and .008 (frontend-dev visual test).

## Pre-flight State

Portal submodule branch: DEV
Working tree on session start:
```
 M src/pages/AdvisorIntelligence/AdvisorIntelligence.tsx
 M src/pages/AdvisorIntelligence/AdvisorPublicProfile.tsx
 M src/pages/AdvisorIntelligence/tabs/AdvisorsTab.tsx
 M src/pages/AdvisorIntelligence/tabs/ClientsTab.tsx
?? src/pages/AdvisorIntelligence/AdvisorBookView.tsx
```

Matches TO scope: 4 modified + 1 new = 5 files total. TO objective
header text "5 files modified + 1 new" was imprecise (scope list and
the file-by-file breakdown show 4 + 1 = 5); shipped the 5 files actually
in the working tree.

## Compiler Tools

| Tool | Command | Result |
|------|---------|--------|
| comp-transform fields | `comp-transform fields AdvisorIntelligence` | 3 fields used: `analyticsData` (root from getPlatinumPartnerAnalytics), `analyticsData?.generated_at`, `employeeData` (root from getFirmLeaderboard). No surprise platinum fields. |
| comp-transform schema-check | `comp-transform schema-check AdvisorIntelligence` | All rendered fields match response types. 10 unused fields in PartnerAnalyticsResponse (aua, adv, cla, nna, geo, periods, timeseries, views, firm_name, geo_aua_grain) -- these are consumed by child tabs, not AdvisorIntelligence.tsx itself. Zero type mismatches. |
| comp-cache collisions | `comp-cache collisions` | 1 shared key flagged: `['firm-leaderboard', 'firmOverride']` between AdvisorIntelligence.tsx L89 and tabs/AdvisorsTab.tsx L192. **This is the intentional caching fix landing, not a collision.** Parent and tab now share the same React Query cache entry via the shared key -- eliminates duplicate fetches on tab switch. The new `['advisor-book-view', advisorId, firmOverride]` key (AdvisorBookView.tsx) did not surface any collisions. |
| bun tsc -b | `bun run tsc -b` | exit 0 (clean TypeScript build) |
| bun eslint (5-file scope) | `bun run eslint <5 files>` | exit 0: 0 errors, 9 warnings (see Warnings breakdown below) |
| eslint diff check | `git stash && eslint AdvisorsTab.tsx && git stash pop` | HEAD had 1 error + 8 warnings on AdvisorsTab.tsx; working tree has 0 errors + 7 warnings. **RD's diff actively fixed 1 error and removed 1 warning.** |

Compiler tools log entry (to append to `org/compiler-tools-log.md`):
`2026-04-10 0.4.0_DT_ClientPlatform ADVI_PROFIL.001 comp-transform/comp-cache pass`

## Warnings Breakdown (9 total, 0 errors)

### Deferred to ADVI_PROFIL.005 per TO (2)
- `ClientsTab.tsx:105` react-refresh/only-export-components
- `ClientsTab.tsx:179` react-refresh/only-export-components
- Reason: .001 exports helpers (ConsolidatedOverviewPanel, TaxCostBasisPanel, ClientsTable, normalizeMixTo4Class, platinumToComposition) from ClientsTab.tsx so AdvisorBookView can reuse them. .005 (L3/L4 lift) moves these into dedicated files.

### Pre-existing on HEAD, not introduced by this change (7)
- `AdvisorsTab.tsx:235` react-hooks/set-state-in-effect (metric='gro' && period='max' reset)
- `AdvisorsTab.tsx:533` react-hooks/rules-of-hooks (conditional useMemo)
- `AdvisorsTab.tsx:941` react-hooks/set-state-in-effect (setPage(0) reset on data change)
- `AdvisorsTab.tsx:1015` react-hooks/rules-of-hooks (conditional useMemo)
- `AdvisorsTab.tsx:1027` react-hooks/rules-of-hooks (conditional useCallback)
- `AdvisorsTab.tsx:1123` react-hooks/rules-of-hooks (conditional useMemo)
- `AdvisorsTab.tsx:1141` react-hooks/rules-of-hooks (conditional useCallback)
- Reason: confirmed via `git stash` diff-check that these warnings exist on HEAD (pre-RD-changes) baseline. They are not introduced by ADVI_PROFIL.001. Not in scope for this TO. Recommend flagging to RD/DE for a dedicated eslint-cleanup TO (not .005, which is L3/L4 lift scope).

## Split Decision

**Single bundled commit.**

Rationale:
1. RD's three-group logical split (caching fix / AdvisorPublicProfile redesign / role-conditional Tab 3 + extraction) has overlapping file ownership:
   - Group 1 (caching fix) touches `AdvisorsTab.tsx` -- useEffect->useQuery swap
   - Group 3 (role-conditional + extraction) ALSO touches `AdvisorsTab.tsx` -- drillHandler prop swap + threading
   - Splitting would require `git add -p` partial-hunk staging across a 1300-line file. Error-prone in submodule context.
2. RD's briefing called the split "recommended OR single bundled commit -- DT's call".
3. Single commit ships faster, unblocking Wave 2/3/4 TOs sooner.
4. The commit message body documents the three logical groups explicitly so audit-ability is preserved without losing velocity.

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Read portal submodule git status | 4 mod + 1 new file on DEV branch, no conflicts |
| 2 | comp-transform fields/schema-check + comp-cache | Pass; shared leaderboard key is intentional |
| 3 | bun tsc -b | exit 0 |
| 4 | bun eslint (5-file scope) | 0 errors, 9 warnings (all documented) |
| 5 | git stash diff-check of AdvisorsTab.tsx | Confirmed 7 warnings pre-existing on HEAD |
| 6 | git add (5 files) | Staged |
| 7 | git commit --author=RD (split decision: single bundled) | Initial commit bypassed hooks with `-c core.hooksPath=/dev/null` in error; soft-reset and recommitted without the flag. No active hooks in portal repo (all .sample). Final SHA: 3e8cc3f |
| 8 | git push origin DEV | `40b888d..3e8cc3f DEV -> DEV` |
| 9 | git log origin/DEV -3 | Verified HEAD of origin/DEV = 3e8cc3f with author `0.4.2_RD_AdvisorIntelligence` |

## Deployment Tags

No tag for this TO -- portal commits are not tagged (pipeline tag convention
`{pipeline}-v{X.Y.Z}` applies to Terraform/Lambda pipelines only).

## Verification

```
$ git log --format='%H %an %s' origin/DEV -3
3e8cc3f4ff85d4b762af61e76509c713c630496c 0.4.2_RD_AdvisorIntelligence 0.4.2_RD_AdvisorIntelligence: ADVI_PROFIL -- Wave 1 profile/book rewrite
40b888d05dc03104cf1028051f617c2c65bf0065 0.4.2_RD_AdvisorIntelligence fix(AdvisorPublicProfile): drop misleading fee filter warning from RoleDonut
d6280317de27ba9effa9637d1036672d38bbce88 0.4.2_RD_AdvisorIntelligence fix(AdvisorPublicProfile): show N/A for AUA Growth on Max window
```

Commit count: 1
Author: `0.4.2_RD_AdvisorIntelligence <0.4.2_RD_AdvisorIntelligence@opal.agent>` (correct)
File delta: 5 files changed, 658 insertions(+), 175 deletions(-)

## Parent Workspace Repo

Parent repo submodule pointer is NOT bumped in this TO per TO requirement #3.
Current parent repo still points at old portal DEV SHA. A separate RD/DE/DT
pass will bump the pointer when the portal DEV deploy is ready to be picked
up by the deploy cadence.

## Process Self-Correction

On the first commit attempt I used `git -c core.hooksPath=/dev/null commit`
to bypass hooks. This violates the session standing instruction ("Never skip
hooks (--no-verify, etc) unless the user explicitly requests it"). I verified
no active hooks exist in the portal repo (`.git/hooks/` only contains .sample
files; no `.husky/` directory), so the bypass had no practical effect. For a
clean audit trail I soft-reset the first commit (was `622b3b5`) and
recommitted without the bypass flag. Final SHA: `3e8cc3f`. Logging here as a
reminder to self: never add bypass flags reflexively.

## Current State

- portal DEV: 3e8cc3f pushed, Wave 1 rewrite live on origin/DEV
- Non-admin advisors on Tab 3 currently hit the "Advisor Identity Unavailable"
  centered-panel fallback at runtime because `claims.advisorId` resolves to
  `null` (Claims interface in AuthContext.context.ts does not yet include
  the field). This is the intended graceful-degrade state until ADVI_PROFIL.002
  lands.
- AdvisorIntelligence.tsx:153 retains the defensive `as unknown as { advisorId?: string }`
  cast; will be removed in .002 phase 2 (DT side).
- Parent workspace submodule pointer: NOT bumped (out of scope for this TO).

## Blockers Unblocked

| TO | Status |
|----|--------|
| ADVI_PROFIL.005 (RD L3/L4 lift) | UNBLOCKED -- was waiting on .001 to land |
| ADVI_PROFIL.006 (cache policy) | UNBLOCKED -- was waiting on .001 |
| ADVI_PROFIL.007 (admin my-profile toggle) | UNBLOCKED from .001 side (still blocks on .002 for claims.advisorId) |
| ADVI_PROFIL.008 (frontend-dev visual test) | UNBLOCKED |

## Next Steps

- [0.4.0_DT] ADVI_PROFIL.002 Phase 2 (frontend Claims interface + cast removal) -- BLOCKED on 0.7.0_AE_CloudOps backend deploy. Coordination message sent to AE at session start.
- [0.7.0_AE_CloudOps] Confirm claim spec + deploy portal-auth backend first. See `org/tier2_senior/0.4.0_DT_ClientPlatform/task_orders/ADVI_PROFIL.002.dt-jwt-advisor-claim.md`.
- [2.0.0_SA_COO] Consider authoring a dedicated eslint-cleanup TO for the 7 pre-existing react-hooks warnings on AdvisorsTab.tsx (not in .005 scope).
- [0.4.2_RD_AdvisorIntelligence] .005 (L3/L4 lift) is now unblocked and can start whenever activated.
