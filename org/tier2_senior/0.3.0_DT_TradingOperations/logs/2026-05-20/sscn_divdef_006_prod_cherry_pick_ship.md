# Session Log — SSCN_DIVDEF.006 PROD cherry-pick ship (8-commit SSCN-only promotion)

**Agent:** 0.3.0_DT_TradingOperations (DevOps Technician — Trading Operations)
**Date:** 2026-05-20
**Task Order:** SSCN_DIVDEF.006.dt-portal-dev-to-prod-push
**Project:** SSCN_DIVDEF (final ship — closes the project lifecycle)
**Status:** COMPLETE — 8 SSCN commits cherry-picked to portal/PROD, GHA deploy.yml green, opalinvest.dev smoke 25/25 + AC1-AC8 PASS

## Session Summary

Final PROD ship for SSCN_DIVDEF. Cherry-picked exactly the 8 SSCN commits from
origin/DEV onto portal/PROD (NOT a merge — origin/DEV carries 12 interleaved
non-SSCN ADVI/MDPF/TRSB commits). Pushed origin/PROD; GHA deploy.yml auto-deployed
to S3 `opalinvest-portal` + CloudFront `EVTSA9VEHNZVH`. opalinvest.dev smoke:
25/25 PASS on the SSCN smoke runner + dedicated AC5 universe sweep + AC6 Factor
Bank check — all 8 acceptance criteria satisfied.

## Startup

- Registered `0.3.0_DT_TradingOperations` (PID 34336); inbox-watch launched.
- Inbox: 2 COO messages — the "push cfdf9a5c" message superseded by the
  `GO: SSCN_DIVDEF.006` GO (CTO-gated 8-commit cherry-pick set).
- comp-graph context set to `SSCN_DIVDEF.006.dt-portal-dev-to-prod-push`.

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 0a | Phase 0 — `git push origin DEV` (portal) | origin/DEV d71ac15b..cfdf9a5c |
| 0b | Phase 0 — bump parent CLOUD `portal` gitlink to cfdf9a5c (safe-commit.sh, portal only) | commit `bf0d0d122`, 1 file; pushed origin/CLOUD 71049e936..bf0d0d122 |
| 0c | Phase 0 RAVC2 to COO | origin/DEV HEAD + CLOUD gitlink reported; COO VALIDATED |
| 1 | Phase 1 — `git checkout PROD` + `git pull origin PROD` | PROD baseline `4f8502e6`; all 8 SSCN SHAs confirmed on origin/DEV, none on PROD |
| 1b | `bun install` on PROD | 461 installs, no changes |
| 1c | comp-routes trace getUniverseScanner | route + edge JWT + API GW stable — PASS |
| 1d | comp-cache collisions | 4 collisions, all AdvisorIntelligence; ZERO scanner keys — PASS |
| 2a | CTO Gate Condition 2 — `git show --stat cfdf9a5c` | 1 file `.frontend-dev/runners/sscn_divdef_001_runner.mjs` +61; zero portal/src — PASS |
| 2b | Cherry-pick Run A `45ea7210^..b302f5cf` (3) | 9ef065f6 + 992b28f5 + c042408c — clean |
| 2c | Cherry-pick Run B `a844f0dd^..b05388dc` (2) | d5eb59ba + ad5d1324 — clean |
| 2d | Cherry-pick Run C `7ef0f4a6^..cfdf9a5c` (3) | 21fd2a12 + 28e27a51 + a7fd7655 — clean |
| 2e | AC1 verify — `git log origin/PROD..HEAD` | exactly 8 commits, ALL SSCN_DIVDEF, zero non-SSCN |
| 2f | `bun run typecheck` | exit 0 |
| 2g | `bun run build` | exit 0, built in 20.15s |
| 2h | `bun run lint` | exit 0; 11 problems (0 errors, 11 warnings) — all pre-existing AUA/Distribution react-hooks/no-explicit-any; ZERO SecurityScanner issue |
| 3 | Phase 3 — `git push origin PROD` | origin/PROD 4f8502e6..a7fd7655 (clean fast-forward; base re-verified == origin/PROD pre-push) |
| 3b | GHA deploy.yml run `26182828524` | SUCCESS — Build 1m33s + Deploy to S3+CloudFront 9s + Tag Deployment 12s, all 3 jobs green |
| 4 | Phase 4 — opalinvest.dev smoke | SSCN runner 25/25 PASS + AC5 universe sweep PASS + AC6 Factor Bank PASS |
| 9 | CloudFront invalidation | fired automatically by deploy.yml "Deploy to S3 + CloudFront" job (AC8) |

## Cherry-pick map (DEV SHA -> PROD SHA)

| SSCN TO | DEV SHA | PROD SHA |
|---------|---------|----------|
| .001 (DIVZ default preset) | 45ea7210 | 9ef065f6 |
| .001 (smoke constitution) | 2254437c | 992b28f5 |
| .005 (universe set 6->5) | b302f5cf | c042408c |
| .007 (layout revert) | a844f0dd | d5eb59ba |
| .008 (Presets dropdown) | b05388dc | ad5d1324 |
| .010 (Factor Bank Group relabel) | 7ef0f4a6 | 21fd2a12 |
| .011 (Equal Weight remainder spread) | d71ac15b | 28e27a51 |
| .011 (smoke runner Scenario 6) | cfdf9a5c | a7fd7655 |

Three contiguous DEV runs -> three range-picks; zero conflicts; result is exactly
8 SSCN commits, zero non-SSCN.

## Deployment Tags

| Pipeline | Tag | Commit | Note |
|----------|-----|--------|------|
| portal | `portal-v2.1.95` | a7fd7655 | created by deploy.yml "Tag Deployment" job on the PROD push |

## Verification

```
portal origin/PROD     = a7fd76558813584f81889af2af9f54e76f12741b
portal local PROD HEAD = a7fd76558813584f81889af2af9f54e76f12741b  (in sync)
portal PROD ahead of pre-push baseline 4f8502e6 = 8 commits, ALL SSCN_DIVDEF
GHA deploy.yml run     = 26182828524 SUCCESS (3/3 jobs green)
opalinvest.dev index   = Last-Modified Wed, 20 May 2026 18:46:50 GMT (fresh deploy)
```

### Acceptance Criteria Scorecard

| AC | Status | Evidence |
|----|--------|----------|
| AC1 | PASS | `git log origin/PROD..HEAD` = exactly 8 commits, all SSCN_DIVDEF, zero non-SSCN |
| AC2 | PASS | typecheck exit 0; build exit 0 (20.15s); lint exit 0, 11 pre-existing warnings, 0 errors, no new SecurityScanner issue |
| AC3 | PASS | opalinvest.dev: "Russell 1000" default; "13 factors" badge; Presets dropdown value "divz" on fresh load |
| AC4 | PASS | no preset-groups strip, no ranking-method control ("Non-sector neutral"/"Sector neutral" both absent); 13/13 number inputs at step=1, 0 at step=0.1 |
| AC5 | PASS | universe dropdown exactly 5 [sp500,r1000,rmidcap,sp400,msciusa] in v0.2 order, r1000 default, no legacy 6-set leak; universe-switch sweep — all 5 load 302 rows, 0 failed/4xx requests, 0 console errors |
| AC6 | PASS | Factor Bank tab: 18 master groups in the Group dropdown (size/efficiency/growth/management/solvency/profitability/quality/value/analyst/governance/crowding/insider/short/beta/volatility/liquidity/momentum/technical); Factor Bank tables use "Group" column header; no "systematic"/"yield" group values. See Observation below re: the separate scanner weights table. |
| AC7 | PASS | Equal Weight -> [8,7,7,8,7,7,8,8,8,8,8,8,8] = nine 8s + four 7s, sum 100, max-min=1 |
| AC8 | PASS | CloudFront invalidation fired by deploy.yml; opalinvest.dev serves the fresh build (Last-Modified 18:46:50Z); SSCN smoke runner 0 console errors across all 6 scenarios |

### Compiler-tool / GHA outputs

- comp-routes trace getUniverseScanner: `/api/general/security_scanner/latest/universes/{param}/scanner_data.json`, CF behavior `/api/general/*`, edge JWT YES, API GW YES — stable, unchanged by the 8 commits.
- comp-cache collisions: 4 shared keys, all AdvisorIntelligence (`advisor-book-view`, `advisor-intelligence`, `firm-leaderboard`, `partner-analytics`); ZERO SecurityScanner / scanner keys.
- GHA run 26182828524 non-fatal annotations: Node.js 20 deprecation warnings (future, cosmetic); a `/usr/bin/git exit 128` annotation in Build + Tag jobs (non-fatal — both jobs concluded green, `portal-v2.1.95` tag created successfully); GitHub Actions cache service 400 (transient, cache miss only).

## Observation — scanner weights table "Category" header (out of .006 scope, not a blocker)

AC6 ("no 'Category' user-facing label") is scoped to the Factor Bank tab, which is
fully compliant ("Group" column header, 18 groups, no systematic/yield). During
the AC6 probe a lone "Category" `<th>` was found on the SEPARATE scanner
selected-factors/weight-configuration table (headers: Category, Factor Name,
Summary, IC, Coverage, Relationship, Systematic, Weight) — `factorBankPanel: none`,
i.e. not inside the Factor Bank tab panel. It is faint (`text-white/40`) but
genuinely sighted-visible.

This header is NOT introduced by .006: it is unchanged by all 8 cherry-picked
commits, was present in the DEV build d71ac15b that Andrew smoke-approved, and
SSCN_DIVDEF.010's relabel was explicitly scoped to the Factor Bank tab (commit
"Factor Bank Group relabel", 2 files / 7 insertions). Flagged to COO/CTO as a
possible cosmetic follow-up; not an AC6 failure for this TO.

## Compiler Tools

| Tool | Result |
|------|--------|
| comp-routes trace getUniverseScanner | PASS — route + edge JWT + API GW stable; unchanged by the 8 SSCN commits |
| comp-cache collisions | PASS — 4 collisions all AdvisorIntelligence; zero scanner-key collision |

Phase-2 compiler mandate (`bun run typecheck` + `bun run build` on PROD post-cherry-pick): both exit 0.

## Current State

- portal/PROD = a7fd7655 (== origin/PROD); 8 SSCN commits cherry-picked, zero non-SSCN; tracked tree clean.
- opalinvest.dev live on the new build (Last-Modified 18:46:50Z); GHA deploy.yml `26182828524` green; tag `portal-v2.1.95`.
- All 8 acceptance criteria PASS. SSCN smoke runner 25/25; AC5 universe sweep + AC6 Factor Bank check PASS.
- Parent CLOUD `portal` gitlink synced to cfdf9a5c (commit bf0d0d122, origin/CLOUD).
- RAVC2 sent to 2.0.0_SA_COO + CC 1.0.0_SA_CTO.

## Next Steps

1. **[2.0.0_SA_COO]** On RAVC2 COMPLETE: execute the 3-step SSCN_DIVDEF project closure (JSON status + REGISTRY row move + PRD status note).
2. **[2.0.0_SA_COO / 1.0.0_SA_CTO]** Decide whether the scanner weights-table "Category" header (Observation above) warrants a cosmetic follow-up TO — out of .006 scope, pre-existing, in Andrew-approved DEV.
