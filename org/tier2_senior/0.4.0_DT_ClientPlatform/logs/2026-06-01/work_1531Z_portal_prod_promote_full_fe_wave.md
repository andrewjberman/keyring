# work 1531Z — Portal PROD promote: full FE wave DEV->PROD (Andrew-direct GO)

**archetype:** DEPLOY

## Current State — SHIPPED, PROD LIVE

Andrew-direct (in-thread, explicit: "deploy prod right now" / "merge DEV forward to PROD and get the
deploy up"; relayed + reinforced by ws CTO [GO PROD PROMOTE] `20260601T152XZ` and COO SYNC). HOLD lifted.
Full accumulated FE wave promoted DEV->PROD.

### Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Pre-flight | origin/DEV `f12abf95` (target); origin/PROD `b7acadab` (live); superset-loss test EMPTY (0 PROD-only files dropped); scope 23 files +808/-178 |
| 2 | Rule 19 commit-tree synthesis | TREE=68c89f98 (origin/DEV^{tree}); MERGE=`fca1e5a8` (-p origin/PROD -p origin/DEV); `git diff --stat MERGE origin/DEV` EMPTY (tree byte-identical) |
| 3 | Push MERGE:PROD | `b7acadab..fca1e5a8 -> PROD`; pre-push hook VALGATE D-1 PASS + typecheck (tsc -b --noEmit) PASS |
| 4 | Tag | `portal-v2.1.105` -> fca1e5a8, pushed (+ CI auto-tagged its own deploy tag) |
| 5 | CI watch | run 26764564916 "Deploy to Production" = SUCCESS (Build / Deploy S3+CloudFront / Invalidate CF / Tag all green) |
| 6 | CloudFront invalidation | explicit on EVTSA9VEHNZVH (opalinvest.dev / www.opalinvest.dev, Status Deployed): ID `I8FXH0VTVR6868YE20K2UPJ5JE` (InProgress) — belt+suspenders over CI's own invalidation |
| 7 | Deploy record | workspace portal pointer bump -> f12abf95, commit `32fb5efff`, pushed origin/CLOUD |
| 8 | Rule 19 invariant | main portal/ tree STILL on DEV @ f12abf95 (commit-tree never touched working tree) — verified |

### Deployment Tags
| Pipeline | Tag | Commit |
|----------|-----|--------|
| portal | portal-v2.1.105 | fca1e5a8 (PROD) |

### Wave contents
MDPF_SCOPED P1 + ADVI_DEMOV1.010 demo-tenant data-source label + demo-tenant connection + BMKAUD PeersTab
falsy-zero fix (c868bd41) + Index/ETF benchmark internal-gate toggle (f12abf95). 23 files, +808/-178.

### Smoke-path taken
Headless BLOCKED fabric-wide (3 lanes: CTO, RD~B, me — identical 180s Chrome/GCM DEPRECATED_ENDPOINT
timeout). Per CTO GO directive #1 ("do NOT stall Andrew's now; verify post-deploy"), promoted WITHOUT
pre-smoke. Verification = (a) PROD tree byte-identical to origin/DEV f12abf95 (guaranteed by commit-tree
+ empty diff assertion); (b) Andrew live-PROD eyeball (he cleared the smoke gate himself, per COO SYNC).

### Coordination — data half (paired)
COO confirmed data-half owner = 0.7.0_AE_CloudOps, dispatched for PROD `/json/*` CF invalidation (so
fresh pure-yang benchmark/peers data serves, not cached pre-revert SmartX-era /json/*). Two separate
paired invalidations: my FE-bundle (EVTSA9VEHNZVH app) + AE's /json/* data. Both must land. Relaying
AE's /json/* invalidation ID to COO + CTO when it arrives.

## Next Steps
- **[Andrew]** Live-PROD verify https://opalinvest.dev (hard-refresh; inval propagating): Peers->UST->1M
  renders (~0.30 / 0.16 + bands); Index/ETF toggle visible internal / hidden external; ModelPortfolios +
  DistributionTab render.
- **[0.7.0_AE_CloudOps]** Awaiting /json/* CF invalidation ID -> relay to COO + CTO for the paired report.
- **[offered]** Fabric-wide headless-Chrome block diagnostic (GCM DEPRECATED_ENDPOINT 180s navigate-hang)
  — secondary; on CTO/Andrew word.
- Rollback path if needed: PROD `b7acadab` (pre-promote).

## Compiler Tools
No comp-* this tick — portal FE promote (git plumbing + CI + CloudFront), not a Lambda/script/IAM edit.
`comp-pipescript io` / `comp-iam` N/A (no Lambda source or boto3 change). Pre-push VALGATE D-1 +
typecheck served as the change-gate. Tooling note carried forward: `aws`/`jq` break under
`MSYS_NO_PATHCONV=1` (it mangles the python-entrypoint exe path) — for AWS CLI `/`-path args use the
`--invalidation-batch '{...}'` JSON form (arg starts with `{`, no path conversion) instead.
