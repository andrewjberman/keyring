# D5-FIX DC-01..07 (7 dead modules) + ROUTE-01 — LANDED
**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE
**serial:** 0.4.0_DE_ClientPlatform
**window:** ~2034Z -> 2040Z 2026-06-12

## Summary

COO GO'd the next D5 fix batch on the ORPHAN-PM close. Removed 7 whole-file dead modules
(DC-01..07) + fixed ROUTE-01 (searchSecurities missing /general/ prefix). Both landed on portal
DEV, VALGATE PASS, no PROD. Standalone dead modules = clearer-cut than ORPHAN-PM, no product-confirm
needed (clean abandoned, no paused-WIP signal).

## Deployment sequence

1. Pulled clean DEV (HEAD==origin/DEV, behind 0, tree clean)
2. verify_modules.py: 7/7 = 0 path-inbound; symbol name-mentions in live files = independent
   duplicate definitions (shadows of live paths), confirmed by 0 import-specifier matches for all 7
3. ROUTE-01 edit: portfolio-optimization.ts:191 /api/trades/ -> /api/general/trades/
4. git rm 7 modules; tsc -b --force --noEmit EXIT 0 + vite build EXIT 0 (14.13s) [combined]
5. comp-routes behaviors: /api/general/trades/* -> APIGateway-portal (auth-gated) = real CF behavior
6. Commit dbcaa6de (7 deletions) + 73d2436a (ROUTE-01); push origin DEV
7. VALGATE D-1 PASS (no partner adapters); surface-check OK (8 files, no critical surface)

## Verification

| Check | Result |
|---|---|
| tsc -b --force --noEmit | EXIT 0 |
| vite build | EXIT 0 (14.13s) |
| comp-routes behaviors (ROUTE-01) | PASS (/api/general/trades/* real behavior) |
| VALGATE D-1 | PASS (no-op, no static partner adapters) |
| D8 surface-check | OK — 8 files, no critical surface |

## Compiler Tools

| Tool | Run | Result | Note |
|---|---|---|---|
| comp-routes behaviors | /api/general/trades/* | PASS | ROUTE-01 fixed path matches a real CF behavior (was unmatched -> SPA HTML) |

What worked: 0 import-specifier matches for all 7 module paths was the decisive ground-truth that
the symbol name-mentions (MODEL_NAMES, Topic, getSentimentColor) were independent duplicate
definitions in live files, not imports — these dead modules are SHADOWS of live paths. D8 note:
benchmarks.ts did NOT fire the surface-check despite being benchmark-adjacent, because the dead
shadow is not a registered critical surface (live benchmark surface = portal-proxy, untouched).

## Files Modified

portal DEV: dbcaa6de (7 deletions: benchmarks/market-update/endpoint-mapping/sentiment-backend/
client-axios/rsiCalculator/colorTokens), 73d2436a (portfolio-optimization.ts 1-line ROUTE-01).
See commit messages. No PROD promote.

## Blockers

None. DC-01..07 + ROUTE-01 closed pending COO/CVO RAVC accept.

## Current State

- portal DEV HEAD 73d2436a = origin/DEV. 7 dead modules gone; searchSecurities path corrected.
- D5 fix queue: ORPHAN-PM (closed) + DC-01..07 + ROUTE-01 all in.
- Remaining from the joint ledger: ORPHAN-AI (11 files) + ORPHAN-MISC (8 files) orphan clusters —
  same per-cluster product-confirm gate (CVO template), pending COO sequence.
- Rule 19: main tree on DEV, clean. Workspace submodule pointer NOT bumped (DEV-only).

## Next Steps

- [2.0.0_SA_COO] accept the DC+ROUTE RAVC2; sequence ORPHAN-AI / ORPHAN-MISC (per-cluster
  product-confirm gate) to DE when ready.
- [0.4.0_DE_ClientPlatform] standing by for ORPHAN-AI/MISC; banked: getPlatinumClientDetailStatic
  schema drift T1b (bundle next portal pass).
