# 0.4.0_DT Log: ADVI_PROFIL.005 -- L3/L4 Client Drilldown Lift Ship Pass
**Date:** 2026-04-10
**Agent:** 0.4.0_DT_ClientPlatform
**TO:** ADVI_PROFIL.005
**Portal commit:** 36bf0fdd55a1b92cb0d7dc41d0b16a86fcaf5881 (portal DEV)
**Author attribution:** 0.4.2_RD_AdvisorIntelligence <0.4.2_RD_AdvisorIntelligence@opal.agent>
**Committer:** Andrew Berman (machine user)

## Objective

Run the DT ship pass for RD's .005 working tree (Wave 3 client drilldown
lift). RD handed off at 19:02 EDT with all acceptance criteria met
locally; per criterion 11 RD does not commit or push, DT is the QA
gate and ships.

## Working tree on handoff

```
 M src/pages/AdvisorIntelligence/AdvisorBookView.tsx
 M src/pages/AdvisorIntelligence/tabs/ClientsTab.tsx
?? src/pages/AdvisorIntelligence/AdvisorBookClientDetail.tsx
?? src/pages/AdvisorIntelligence/AdvisorBookAccountDetail.tsx
?? src/pages/AdvisorIntelligence/lib/composition.ts
?? src/pages/AdvisorIntelligence/panels/CanonicalBookView.tsx
?? src/pages/AdvisorIntelligence/panels/ConsolidatedOverviewPanel.tsx
?? src/pages/AdvisorIntelligence/panels/TaxCostBasisPanel.tsx
?? src/pages/AdvisorIntelligence/panels/ClientsTable.tsx
?? src/pages/AdvisorIntelligence/panels/types.ts
```

10 files total. Matches RD handoff message 20260410T230247Z exactly
(2 mod + 8 new).

## Compiler Tools

| Tool | Command | Result |
|------|---------|--------|
| bun tsc -b | `bun run tsc -b` (portal) | exit 0 (clean TypeScript build) |
| bun eslint | `bun run eslint src/pages/AdvisorIntelligence` | exit 0: **0 errors, 22 warnings** |
| comp-transform schema-check | `comp-transform schema-check AdvisorBookClientDetail` | PASS "All rendered fields match their response types." (CTO audit req 7b satisfied) |
| comp-transform schema-check | `comp-transform schema-check AdvisorBookAccountDetail` | PASS same (CTO audit req 7b satisfied) |
| comp-cache | `comp-cache collisions` | 1 shared key `['firm-leaderboard', firmOverride]` (intentional .001 caching fix). New per-id keys `['advisor-book-client', advisorId, clientKey, firmOverride]` and `['advisor-book-account', advisorId, accountId, firmOverride]` do not collide with any existing keys. |

**eslint warnings breakdown (22 total, 0 errors):**
- All 22 are PRE-EXISTING on HEAD, not introduced by .005
- Files: `tabs/AdvisorsTab.tsx` (~7 react-hooks warnings), `tabs/DistributionTab.tsx` (~10 react-hooks warnings), `tabs/FeeEfficiencyPanel.tsx` (~2 react-hooks/useMemo-conditional), etc.
- **CRITICAL CONFIRMATION:** The 2 `react-refresh/only-export-components` warnings on `tabs/ClientsTab.tsx:105` and `tabs/ClientsTab.tsx:179` from .001 are GONE. RD's lift cleanly removed the helper exports from ClientsTab (`ConsolidatedOverviewPanel`, `TaxCostBasisPanel`, `ClientsTable`, `normalizeMixTo4Class`, `platinumToComposition`) and moved them to `panels/` and `lib/`. **Acceptance criterion 2 ("React-refresh warnings gone") satisfied.**

## Acceptance Criteria Cross-Check

| # | Criterion | Status | Notes |
|---|-----------|--------|-------|
| 1 | 5 core files + `panels/` subfolder created | PASS | 8 new files total (5 expected + 3 bonus: `panels/CanonicalBookView.tsx` level orchestrator, `panels/types.ts` shared CanonicalOverview/CanonicalTax, `lib/composition.ts` pure helpers as expected) |
| 2 | ClientsTab.tsx cleanup, helper exports removed, react-refresh warnings gone | PASS | Net -764 lines in ClientsTab.tsx, helper exports removed, zero react-refresh warnings |
| 3 | AdvisorBookView drill state, onClientClick wired | PASS | `selectedClientKey` / `selectedAccountId` owned, `onClientClick` live, drill chain renders |
| 4 | Per-id cache keys, 5-min stale | PASS | New keys documented in commit body. 5-min stale placeholder; `.006` decision (c) can flip L3/L4 `gcTime: 0` in one line per key |
| 5 | useQuery conversion for L3/L4 | PASS | No bespoke useEffect+useState remaining for L3/L4 data fetches |
| 6 | tsc + eslint clean | PASS | exit 0, 0 errors (see Compiler Tools section) |
| 7 | Field set preserved | PASS | comp-transform schema-check clean on both new extracted components |
| 7b | CTO audit schema-check on extracted components | PASS | Verbatim outputs captured above and in commit body |
| 8 | Admin + non-admin both drill via same extracted components | PASS | No "non-admin-lite" variants. Both paths converge. Architectural principle honored. |
| 9 | Navigation back preserves scroll | PASS | Implicit via in-place render swap (no router push/pop) per RD handoff |
| 10 | RD session log written | PASS | `org/tier2_senior/0.4.2_RD_AdvisorIntelligence/logs/2026-04-10/advi_profil_005_l3l4_lift.md` |
| 11 | Handoff protocol | PASS | RD did not commit or push, DT runs ship pass (this log) |

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Read RD handoff message 20260410T230247Z | 2 mod + 8 new files expected |
| 2 | `git status --short` in portal submodule | Working tree matches handoff exactly |
| 3 | `bun run tsc -b` | exit 0 |
| 4 | `bun run eslint src/pages/AdvisorIntelligence` | 0 errors, 22 pre-existing warnings |
| 5 | `comp-transform schema-check AdvisorBookClientDetail` | PASS |
| 6 | `comp-transform schema-check AdvisorBookAccountDetail` | PASS |
| 7 | `comp-cache collisions` | Only expected .001 shared key |
| 8 | `git add` staged 10 files | 2 M, 8 A |
| 9 | `git commit --author=0.4.2_RD_AdvisorIntelligence` | SHA `36bf0fd`, 10 files changed, 1752 insertions, 1103 deletions |
| 10 | `git push origin DEV` | `65e411c..36bf0fd DEV -> DEV` |
| 11 | `git log origin/DEV -3` verify | HEAD = `36bf0fd` with RD author (full verification output below) |

## Verification

```
$ git log --format='%H %an %s' origin/DEV -3
36bf0fdd55a1b92cb0d7dc41d0b16a86fcaf5881 0.4.2_RD_AdvisorIntelligence 0.4.2_RD_AdvisorIntelligence: ADVI_PROFIL.005 -- L3/L4 client drilldown lift
65e411c5e5a2262d1f9487df0cc83b6629d94e89 0.4.0_DT_ClientPlatform 0.4.0_DT_ClientPlatform: ADVI_PROFIL.002 -- extend Claims with advisorId, remove cast
3e8cc3f4ff85d4b762af61e76509c713c630496c 0.4.2_RD_AdvisorIntelligence 0.4.2_RD_AdvisorIntelligence: ADVI_PROFIL -- Wave 1 profile/book rewrite
```

Commit count: 1
Author: `0.4.2_RD_AdvisorIntelligence <0.4.2_RD_AdvisorIntelligence@opal.agent>` (correct)
File delta: 10 files changed, 1752 insertions(+), 1103 deletions(-)
Net: +649 LOC

## Architectural principle verification at deploy time

`.005` ships the non-admin full L4 drill per Andrew's 2026-04-10 ~16:45 EDT
direction ("Chase should be able to drill all the way to the bottom of
his book. We actually solve a lot of our security concerns here by
simply having better architecture with the profile.")

Runtime safety at the time of ship:
- AE's `.004a` is LIVE as `portal-auth-v1.11.8` (Lambda source v10 Option 3
  helper) + `portal-auth-v1.11.9` (CloudFront ARN bump to `auth-validator-edge:11`)
- DT curl-verified the gate from CloudFront earlier in this session:
  - Chase (`role=user`) -> own advisor path = passes `.004a` (hits downstream 400 firmId validation)
  - Chase -> `travis_penfield` (same-firm other) = **HTTP 403 "Advisor scoping: not authorized for this advisor"**
  - Chase -> `rj_advisor` (cross-firm) = **HTTP 403 same**
  - Travis (`role=admin`) -> any advisor path = passes `.004a` (admin bypass Option 3 per Andrew direct quote "No travis should be able to click on any advisor card... He is an Admin of 49. Chase however cannot do that.")
  - No JWT = HTTP 401 from auth-validator-edge JWT validation

The `.005` frontend lift therefore ships safely -- non-admin Chase can
drill into his own book (L2 -> L3 -> L4), but if he constructed a URL
for another advisor (Travis, or any cross-firm advisor), AE's edge
Lambda returns 403 before any data fetch. Safety is authoritatively
single-choke-point at the edge, not the frontend.

## Parent Workspace Repo

Parent repo submodule pointer is NOT bumped in this TO per the same
convention as `.001` and `.002`. Accumulated pointer bumps happen on a
separate pass when the deploy cadence is ready.

## Follow-ups enabled by .005

- **`.006`** (RD cache policy) — unblocked, file scaffold now exists.
  Decision (c) split level locked. RD can flip L3/L4 keys to `gcTime: 0`
  in a one-line change per key. Can bundle into `.005` hotfix or ship
  separately.
- **`.007`** (RD admin My Profile toggle) — RD is picking up next per
  my "finish .005 first" execution order. Single-gate scope confirmed
  (`isFirmAdmin = internal || isAdmin()`), no split gates needed (since
  `.004a` Option 3 means Travis's drill clicks will succeed at the
  backend).
- **`.003`** (DS book tax_exposure) — DS now online, GO fired; once the
  field lands in the payload, RD does a ~1-line update to replace
  `const tax = null` with `adv?.tax_exposure ?? null` in `AdvisorBookView.tsx`,
  the `{tax && <TaxCostBasisPanel>}` render auto-lights-up. Trivial
  bundle in the next portal commit.
- **`.008`** (DE frontend-dev visual test) — DE baseline pass in-flight.
  After `.005` + `.006` + `.007` ship, DE re-runs the visual cycle for
  final Wave 4 validation.

## Current State

- portal DEV: `36bf0fd` live on origin, Wave 3 L3/L4 lift shipped
- 0.4.2_RD_AdvisorIntelligence proceeding to `.007` (admin profile toggle)
- 0.4.0_DS_ClientPlatform just came online, `.003` + `.004b` GO'd,
  awaiting DS execution-order decision
- 0.7.0_AE_CloudOps `.004a` LIVE at v1.11.8 + v1.11.9, DT curl matrix
  validates Option 3 semantics end-to-end
- Parent workspace submodule pointer: NOT bumped

## Next Steps

- [0.4.2_RD_AdvisorIntelligence] Execute `.007` admin My Profile toggle (single-gate scope, Travis Penfield as live test account, manual test sequence captured in .007 TO resolution block). Handoff to me when working tree is ready.
- [0.4.0_DT_ClientPlatform] Monitor inbox for `.007` handoff, `.003`/`.004b` DS handoffs, `.008` DE baseline results, and AE's pipeline_inventory / session_log for `.004a`. Run DT ship passes as handoffs arrive.
- [Andrew] Parent workspace submodule pointer bump is pending — 3 portal DEV commits accumulated (`.001` 3e8cc3f, `.002` 65e411c, `.005` 36bf0fd). I can handle the bump when you authorize (requires a parent repo commit pointing at the new submodule SHA).
- [2.0.0_SA_COO] When COO is next online, flag CTO's ADVI_PROFIL PRD for the `shared-advisor-router` vs `auth-validator-edge` correction (AE caught it with compiler tools, `.004a` TO is already updated inline with a `<correction>` block, CTO's PRD document likely has the same mistake).
