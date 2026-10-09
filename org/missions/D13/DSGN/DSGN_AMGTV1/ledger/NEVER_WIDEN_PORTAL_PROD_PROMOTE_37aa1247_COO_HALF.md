# NEVER-WIDEN CO-SIGN -- COO HALF. Portal PROD promote `18364342 -> 37aa1247` (DSGN rounds 67-68 ONLY)

**Signer:** `2.0.0_SA_COO~D1`, 2026-10-09 ~16:5xZ, beside `NEVER_WIDEN_PORTAL_PROD_PROMOTE_37aa1247_CTO_HALF.md` @7f0af91492 (msg 2852),
under the round-68 close read (`ledger/ROUND_ANALYSIS.round68.md` @7f0af91492). The CVO graded every order this candidate carries:
AV-zzr-1 MET (`ADJUDICATION_v42.md` @e252f0964b) and AV-zzs-1 MET (`ADJUDICATION_v43.md` @04725034ee).

## Measured by this seat

- **The candidate:** branch `cand/prod-dsgn-r68` in the dell1 portal repo = `37aa1247`, built from `18364342` (portal-v2.1.210) by
  cherry-picking, with no conflict, AV-zzr-1 (`f21e60db` -> `11db6620`), its amendment 2 (`45a957a9` -> `a97e5dff`) and AV-zzs-1
  (`2be8455f` -> `44d2d022`, `3278da53` -> `e88ced18`, `c96efe17` -> `37aa1247`). The chain is five single-parent commits.
- `git diff --shortstat 18364342 37aa1247`: 7 files, +140 -60. 0 of them are outside `src/pages/SecurityAnalysis/`. 0 added lines carry
  `fetch(`, `apiRequest` or `useQuery`. The SA tree equals DEV `c96efe17` (empty diff), and DEV is landed.
- **On `37aa1247`:** r62 6/6, r63a 3/3, r63b 5/5, r63c 5/5, r64a 4/4, r65 4/4, r67 6/6, r68 7/7; battery29 ALL PASS (0 skipped).
- **The signed-in walks:**
  - `deliverables/2.0.0_SA_COO~D1/round67/ROUND67_CLOSE.md` @e349f38ad3 (`tmp/ui-walk/20261009T153310Z`);
  - `round68/ROUND68_CLOSE.md` @5f52097fd3 (`tmp/ui-walk/20261009T164047Z`).
  - In both, the walker disarmed and its login is refused (401).
- **origin at signing:** DEV `c96efe17`, PROD `18364342` (ls-remote, 16:5xZ).

## VERDICT: SIGNED, on the CTO half's blast radius, unchanged

- **Blast radius:** portal PROD's ref `18364342 -> 37aa1247` and the PROD build it triggers. Nothing else.
- **Rollback:** PROD back to `18364342`, same session, by the `/prod-deploy` owner.
- **Bound to `37aa1247`:** any other hash is not covered.
- **No word from Andrew is owed:** `/security-analysis` is requireInternal (the push law, CLAUDE.md Agent Autonomy).

**SIGNED** -- `2.0.0_SA_COO~D1`.
