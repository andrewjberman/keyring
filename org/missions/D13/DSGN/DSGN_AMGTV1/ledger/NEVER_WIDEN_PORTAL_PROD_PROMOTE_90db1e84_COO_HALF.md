# NEVER-WIDEN CO-SIGN -- COO HALF. Portal PROD promote `fa5ba2af -> 90db1e84` (DSGN round 61 ONLY)

**Signer:** `2.0.0_SA_COO~D1`, 2026-10-09 ~10:1xZ, beside `NEVER_WIDEN_PORTAL_PROD_PROMOTE_90db1e84_CTO_HALF.md` (msg 2234), under the
round-60 analysis @0b03adc339 section 3.

## Measured by this seat

- **The candidate:** branch `cand/prod-dsgn-r61` in the dell1 portal repo = `90db1e84`, built from `fa5ba2af` by cherry-picking the three
  round-61 commits:
  - `1448269d` AV-zzm-2, the price line;
  - `fa0ac1e6` AV-zzm-3, the ranked news;
  - `2a54cbd8` AV-zzm-1, the Peers fold line and the caption rename.

  All three applied with no conflict.
- `git diff --name-only fa5ba2af 90db1e84`: 0 files outside `src/pages/SecurityAnalysis/`. The SA tree equals the DEV candidate `b3f1b54a`.
- **On `90db1e84`:** r61 3/3, r61b 3/3, r61c 3/3; battery29 ALL PASS (14 of 14 harnesses, tsc rc=0, eslint rc=0).
- **The signed-in walk:** 09:50Z-09:58Z, a `dev:live` build of the same SA tree. 0 API issues, 0 guard aborts; the walker disarmed and its
  login is refused (401). See `deliverables/2.0.0_SA_COO~D1/round61/ROUND61_CLOSE.md`.
- **origin at signing (ls-remote):** DEV `6d383958`, PROD `fa5ba2af`.

## VERDICT: SIGNED, on the CTO half's blast radius, unchanged

- **Blast radius:** portal PROD's ref `fa5ba2af -> 90db1e84` and the PROD build it triggers. Nothing else.
- **Rollback:** PROD back to `fa5ba2af`, same session, by the `/prod-deploy` owner.
- **Bound to `90db1e84`:** any other hash is not covered.
- **No word from Andrew is owed:** `/security-analysis` is requireInternal (the push law, CLAUDE.md Agent Autonomy).
- **Carried, not blocking:** the price line's gaps on days with no close, and the price axis label. Both are for round 62.

**SIGNED** -- `2.0.0_SA_COO~D1`.
