# OPAL_BBGTML -- register, ground, build all legs to the CTO enable gate
**archetype:** MIXED (IMPLEMENT + DEPLOY)

## Summary
Second sovereign-delegate project this session (basis: Andrew-direct ~15:4xZ, verbatim at
task_orders/ANDREW_DIRECT_20260715_bbgtml_alyssa_skills_scoping.md; code Andrew-set OPAL_BBGTML).
Three-leg Alyssa workflow: /bbg-pull (Yang's two notebooks on the terminal machine) -> leg-2
tripwire -> /bbg-send (m365 gateway tool through the /data-refresh portal channel with
upload/pipeline/display confirmation). Registered (8b7b53c95), PRD grounded+authored (b0c1f0f02),
built and exercised everything short of the CTO-gated enable flip, same session.

## What was grounded (kills the external dependency)
- Yang's "two python scripts" = two notebooks at SharePoint site 'Shared' -> OCIO Models/Dashboard/
  202511 Model Portfolio Exposure/src (folder OneDrive-syncs locally): market_indices_data_pull
  -> 'data YYYYMMDD v1.pkl' (84 return indices incl .UST/.ST/.INT/.LTC/.LTA + 81 macro + corr;
  idempotent-by-date); model_portfolio_regression_analysis -> 'model YYYYMMDD v1.pkl'.
- /data-refresh backend LIVE: opal-data-refresh-api (data-refresh-v2.2.0); routes ride the PORTAL
  FRONT DOOR (CF behavior /api/scoped/data-refresh/* -> APIGateway-portal + Lambda@Edge validator);
  Dev-or-empty userType gate at lambda_function.py:89-114; contracts pinned at :264/:357/:718.
- Gateway integration framework (fail-closed ENABLED_INTEGRATIONS; ycharts precedent) fits exactly.

## Built + exercised
| Piece | Evidence |
|---|---|
| B2 tripwire (bbg_pkl_tripwire.py) | POSITIVE: 17/17 PASS on the real 07-10 vintage. NEGATIVE x2 (key-drift mutant; missing files): FAIL loud, exit 1. Pins measured (8.5MB data/4 keys; 17.1MB model/13 keys; summary 25x10; 5 model index names incl Yang's 'Agressive' spelling) |
| B4 runner + skill | run_daily_pull.py (nbconvert in-place, cwd=src, chains tripwire, failure exit VERIFIED 1) + .bat (conda cma default, BBG_CONDA_ENV override) + BBG_DAILY_SKILL.md; DEPLOYED additively to the SharePoint project tools/ (syncs to Alyssa) |
| B1 surface | Exact diff packaged (gateway_diff_proposal/) -> CTO RULED option (a) 172813Z: merge-dark now, enable = his gate |
| B3 merge-dark | opal_portal integration in the gateway tree (5fd17deba, fix ca3ea5689); spec validator NONE errors; registry loads [opal_portal, ycharts]; ENABLED_INTEGRATIONS untouched = zero live tools; code NOT on the EC2 box (deploy rides the enable flip, one restart) |
| Credential chain | Secret opal/portal/svc-data-refresh (never printed; SM ARN ...-4QLOH6) + svc-bbgtml@opalinvest.com via canonical create_user_v2.py (opal-capital/internal/user, must_change=False, --no-ses; firm dict enforces @opalinvest.com, superseding DIFF.md's .dev suggestion) |
| IAM grant | opal-portal-iam.tf (ycharts pattern, exact ARN); commit-before-apply ca3ea5689 -> plan 1-add -> safe-apply -> 0-diff -> tag m365-mcp-gateway-v1.6.0; ledger 20260715T1815Z CLOSED 5/5 |
| 22a verify | APPLIED get-role-policy = exact ARN no-wildcard; POSITIVE simulate allowed (one --resource-arns); NEGATIVE control SEPARATE invocation (orion/jwt/current) implicitDeny |
| Pins 1-3 | EXERCISED LIVE: login 200+accessToken (svc cred passes the Dev-gate); status structured-404 via CF; upload-urls 200 {uploadId, urls dict, expiresIn} after files=[{name,size}] fix. Discovery: direct API GW host lands on the portal-data-proxy fallback router -- front door is the correct client path |
| Dark staging | Real 07-10 pair PUT into pending/24f508ff-96e0-48c4-b8d3-7d00b213c8ca/, ListObjectsV2-verified key+size+ETag, trigger NOT called (staged, not served). Honest substitution: the delegated-Graph download leg used the local synced bytes; exercised at first enabled dry_run |

## Boundaries held
Shape-(b) vendor posture (Bloomberg never leaves the terminal machine); gateway = shared infra
surfaced FIRST (CTO ruled before any edit); gateway never unpickles; NEVER#5 (confirmation reads
the real triggered run; dark exercise deliberately never triggered); secret value never
printed/logged (redacted in all outputs).

## Current State / Next
- Enable gate: CTO AM review (evidence message 180234Z) -> ENABLED_INTEGRATIONS flip + gateway
  EC2 deploy (one restart) -> first enabled dry_run (exercises the Graph leg) -> B5 full
  end-to-end on Alyssa's next real morning run -> close w/ COO CC.
- Alyssa-side: tools/ live in the project folder; her first guided /bbg-pull run confirms the
  conda env name + template path on her machine (PRD open-confirms).

## Blockers
None (the enable gate is sequenced, not blocked).

## Compiler Tools
| Tool | Purpose | Result |
|---|---|---|
| comp-grep (x8) | provisioning script hunt, data-refresh backend + CF behavior trace, gateway TF/IAM mapping | Found create_user_v2.py, the CF front-door behavior (:451), ycharts-iam precedent |
| comp-glob (x3) | user-script + gateway source location | users/scripts/create_user_v2.py; infra/aws/ec2/m365-mcp-gateway/ |
| comp-pulse diff (auto x6 commits) | pre-commit risk reflex | REFLEX CLEAN x6 |
| (in-band) | safe-commit surface-check, safe-apply HALTGT, TF plan/0-diff | All PASS |

Raw-aws calls were operational (secretsmanager create/get, s3 list, simulate) or rail-checked
with inline markers (Rule 22a live-primitive mandate: get-role-policy + simulate x2).
