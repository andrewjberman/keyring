# work 1739Z — Portal DEV-delta SYNTHESIS promote DEV->PROD (COO [DRIVE] GO)

**archetype:** DEPLOY

## Current State — SHIPPED, PROD LIVE

Respawned (prior session ended after the full-FE-wave PROD promote, v2.1.105). `/watcher` self-healed
(was NOT REGISTERED + no watcher -> re-registered PID 3812 + launched tracked watcher). Read ws COO
`[DRIVE] GO` `20260601T170722Z`: Andrew PASSED the human visual smoke of the per-firm Daily AUA
(Global/49F/INF, briefing `4bb7a0ecc`) — the visual gate that held the promote is CLEARED. GO the
smoke-validated DEV delta since v2.1.105; EXCLUDE in-flight Macro/Inflection (ride next promote). COO GO
is my authority (spawn != dispatch). ACK'd COO + FYI CTO pre-exec; executed; reported DONE to both.

## Why a SYNTHESIS promote (not a full DEV->PROD)

DEV HEAD (998ff784) had moved 3 commits PAST the smoke-validated state. The `origin/PROD..origin/DEV`
delta was a clean linear 6-commit chain: the 3 smoke-validated commits are exactly the BOTTOM 3, the 3
in-flight EXCLUDED commits exactly the TOP 3. So the synthesis cut-point = tree @ `103f623a`.

| Promote? | Commit | Subject |
|----------|--------|---------|
| YES | 2eb4b450 | polish(ModelPortfolios): canonical FE model names (Benchmark Comparison + Return vs Volatility) |
| YES | 1b9e176c | revert(ModelPortfolios): remove firm-invariant disclaimer (Performance + Peers) |
| YES | 103f623a | feat(MDPF Cohort-1c): fold SMA into combined non-model on per-firm view  <- CUT POINT |
| NO (in-flight) | 39555946 | polish(MDPF): distinct colors for Inflection 50/50 blend |
| NO (in-flight) | b0a5a55a | fix(Macro): year-qualified (YYYY-MM) month-key lookup |
| NO (in-flight) | 998ff784 | fix(Macro): read producer's values_ym (YYYY-MM) field |

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Pre-flight | origin/PROD `fca1e5a8` (v2.1.105 + CI auto-tag v2.1.106); target tree `103f623a^{tree}`; net scope 2 files (ModelPortfolios.tsx + ReturnVolatilityScatter.tsx) +67/-44 = sum of the 3 commits (full capture); SUPERSET-LOSS test EMPTY (0 PROD-only files dropped) |
| 2 | Rule 19 commit-tree synthesis | TREE=`6aa4796a`; MERGE=`456d134e` (`commit-tree 103f623a^{tree} -p origin/PROD -p 103f623a`); `git diff --stat MERGE 103f623a` EMPTY (byte-identical to Andrew-validated cut) |
| 3 | HALTGT (manual) | inbox empty, no STOP-class message before the irreversible push |
| 4 | Push MERGE:PROD | `fca1e5a8..456d134e -> PROD`; portal pre-push VALGATE D-1 PASS (no api/endpoints changed) + typecheck `tsc -b --noEmit` PASS (working tree, incl. unrelated HoldingsTab.tsx WIP, type-clean) |
| 5 | Tag | `portal-v2.1.107` -> 456d134e, pushed (CI auto-tagged v2.1.108 same commit) |
| 6 | CI watch | run `26771239387` "Deploy to Production" = SUCCESS (Build / Deploy S3+CloudFront / Tag all green) |
| 7 | CF invalidation | explicit /* on EVTSA9VEHNZVH (opalinvest.dev/www, Deployed): `I1J61YOMSTXHG3EJBQVWHWA4H0` (InProgress) — belt+suspenders over CI's own invalidation |
| 8 | Rule 19 invariant | main portal/ tree STILL on DEV @ 998ff784 (commit-tree never touched the working tree); DEV HEAD unchanged; another lane's in-flight HoldingsTab.tsx WIP left untouched — verified |

## Deployment Tags
| Pipeline | Tag | Commit |
|----------|-----|--------|
| portal | portal-v2.1.107 (DT) + portal-v2.1.108 (CI auto) | 456d134e (PROD) |

## Verification

- PROD tree byte-identical to `103f623a` — the exact state Andrew visual-smoked on DEV-build. PROD now
  serves what was validated (commit-tree synthesis guarantees content, not just commit lineage).
- CI "Deploy to Production" 26771239387 SUCCESS (all 3 jobs).
- Rendered-pixel re-verify is human-only (headless-Chrome blocked fabric-wide); CloudFront portal fetch
  = 403 auth gate. Data/asset-layer evidence = CI Deploy-to-S3+CF SUCCESS + byte-identical tree.

## Next Steps
- **[next /work tick]** Confirm CF invalidation `I1J61YOMSTXHG3EJBQVWHWA4H0` reaches Completed.
- **[next promote]** In-flight Macro YYYY-MM (b0a5a55a/998ff784) + Inflection blend colors (39555946)
  ride the next DEV->PROD when ready/smoke-validated.
- Rollback path if needed: PROD `fca1e5a8` (v2.1.105/106).

## Compiler Tools
No comp-* this tick — portal FE promote (git plumbing + CI + CloudFront), not a Lambda/script/IAM edit.
Pre-push VALGATE D-1 + typecheck served as the change-gate. AWS CLI `/*` invalidation used the
`--invalidation-batch '{...}'` JSON form (arg starts with `{`) to dodge Git-Bash path mangling.
