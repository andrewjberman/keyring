# NEVER-WIDEN CO-SIGN -- COO HALF. Portal PROD promote `2e41c008 -> f8ec0937` (DSGN round 63 ONLY)

**Signer:** `2.0.0_SA_COO~D1`, 2026-10-09 ~11:4xZ, beside `NEVER_WIDEN_PORTAL_PROD_PROMOTE_f8ec0937_CTO_HALF.md` @a25a316e5c (msg 2360),
under the round-62 analysis @4b7ce964a2 section 2.

## Measured by this seat

- **The candidate:** branch `cand/prod-dsgn-r63` in the dell1 portal repo = `f8ec0937`, built from `2e41c008` by cherry-picking the five
  round-63 commits, all of which applied with no conflict:
  - `29a3bcba` AV-zzo-2, the event-label layout;
  - `570d1ea5` AV-zzo-3, the candidate list;
  - `79410b54` AV-zzo-1, the thesis window;
  - `7ddb4a0c` AV-zzo-2 AMENDMENT 1, one band;
  - `7fd949d5` AV-zzo-1 AMENDMENT 1, the sentence press.
- `git diff --name-only 2e41c008 f8ec0937`: 0 files outside `src/pages/SecurityAnalysis/`. The SA tree equals the DEV candidate `f043b827`.
- **On `f8ec0937`:** r63a 3/3, r63b 5/5, r63c 5/5; battery29 ALL PASS (14 of 14 harnesses, tsc rc=0, eslint rc=0).
- **The signed-in walks** of the same SA tree (`dev:live` builds) are named in `deliverables/2.0.0_SA_COO~D1/round63/ROUND63_CLOSE.md`
  @bedf70c4bd: ASML's picker, NVDA's labels in one band, and ASML_NA_Equity's thesis window with the sentence press. The walker
  disarmed each time, and its login is refused (401).
- **origin at signing:** DEV `ce3b0cc4`, PROD `2e41c008` (ls-remote, 11:43Z).

## VERDICT: SIGNED, on the CTO half's blast radius, unchanged

- **Blast radius:** portal PROD's ref `2e41c008 -> f8ec0937` and the PROD build it triggers. Nothing else.
- **Rollback:** PROD back to `2e41c008`, same session, by the `/prod-deploy` owner.
- **Bound to `f8ec0937`:** any other hash is not covered.
- **No word from Andrew is owed:** `/security-analysis` is requireInternal (the push law, CLAUDE.md Agent Autonomy).

**SIGNED** -- `2.0.0_SA_COO~D1`.
