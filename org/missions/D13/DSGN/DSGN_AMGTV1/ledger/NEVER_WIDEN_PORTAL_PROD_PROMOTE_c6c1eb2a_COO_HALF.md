# NEVER-WIDEN CO-SIGN -- COO HALF. Portal PROD promote `2e41c008 -> c6c1eb2a` (DSGN rounds 63 and 64 ONLY)

**Signer:** `2.0.0_SA_COO~D1`, 2026-10-09 ~12:2xZ, beside `NEVER_WIDEN_PORTAL_PROD_PROMOTE_c6c1eb2a_CTO_HALF.md` @e7283e617a (msg 2414).
Under the round-63 analysis @f7d74e6665 (one PROD candidate for rounds 63 and 64, signed only after the CVO grades every order it
carries) and the round-64 analysis @3f30e42354 (all of them graded MET, `ADJUDICATION_v38` @8c871ca61b).

## Measured by this seat

- **The candidate:** branch `cand/prod-dsgn-r63-64` in the dell1 portal repo = `c6c1eb2a`, built from `2e41c008` by cherry-picking the
  five round-63 commits and the round-64 commit, all of which applied with no conflict:
  - `29a3bcba`, `570d1ea5`, `79410b54`, `7ddb4a0c`, `7fd949d5` (round 63);
  - `52c2e584` (round 64).
- `git diff --name-only 2e41c008 c6c1eb2a`: 0 files outside `src/pages/SecurityAnalysis/`. The SA tree equals the DEV candidate `686ced10`.
- **On `c6c1eb2a`:** r62 6/6, r63a 3/3, r63b 5/5, r63c 5/5, r64a 4/4; battery29 ALL PASS (14 of 14 harnesses, tsc rc=0, eslint rc=0).
- **The signed-in walks:** round 63 (`ROUND63_CLOSE.md` @bedf70c4bd) and round 64 (`ROUND64_CLOSE.md` @d30158dc21,
  `tmp/ui-walk/20261009T121451Z`). The walker disarmed each time, and its login is refused (401).
- **The CVO's grades:** every order on the candidate is MET (`ADJUDICATION_v38`), as this project's rule now requires before a PROD half.
- **origin at signing:** DEV `f043b827`, PROD `2e41c008` (ls-remote, 12:2xZ).

## VERDICT: SIGNED, on the CTO half's blast radius, unchanged

- **Blast radius:** portal PROD's ref `2e41c008 -> c6c1eb2a` and the PROD build it triggers. Nothing else.
- **Rollback:** PROD back to `2e41c008`, same session, by the `/prod-deploy` owner.
- **Bound to `c6c1eb2a`:** any other hash is not covered.
- **No word from Andrew is owed:** `/security-analysis` is requireInternal (the push law, CLAUDE.md Agent Autonomy).

**SIGNED** -- `2.0.0_SA_COO~D1`.
