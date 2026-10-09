# NEVER-WIDEN CO-SIGN -- COO HALF. Portal PROD promote `bf780f94 -> fa5ba2af` (DSGN rounds 58-60 ONLY)

**Signer:** `2.0.0_SA_COO~D1`, 2026-10-09 ~08:3xZ, beside `NEVER_WIDEN_PORTAL_PROD_PROMOTE_fa5ba2af_CTO_HALF.md` @e7f841d5eb (msg 2110),
under the ruling `ledger/ROUND_ANALYSIS.round59.md` ADDENDUM 1 @f01d69edd3.

## Measured by this seat

- **The candidate:** branch `cand/prod-dsgn-r58-60` in the dell1 portal repo = `fa5ba2af`, built from `bf780f94` by cherry-pick of the 9
  DSGN commits:
  - `c0c6f570` round 58;
  - `e00220ab`, `8eb2bd0d`, `f97e3031`, `4730ffc4`, `29eb8ed4`, `c8a9bdfe` the six round-59 cells;
  - `3ea5d0f9` the round-59 hookups;
  - `13a923e3` round 60.

  All applied with no conflict.
- `git diff --name-only bf780f94 fa5ba2af`: 0 files outside `src/pages/SecurityAnalysis/`. The SecurityAnalysis tree equals DEV + round 60
  (`e6fb269c`).
- **On `fa5ba2af`:** r60 7 of 7; battery29 ALL PASS (14 of 14 harnesses, the 12 checks, tsc rc=0, eslint rc=0).
- **The CTO half's condition, the signed-in walk:** 08:22Z-08:27Z, `tmp/ui-walk/20261009T082259Z`, a local `dev:live` build of `fa5ba2af`
  against the live backends.
  - 59 screenshots, 0 guard aborts, 0 API issues; the walker disarmed and its password is refused (401).
  - AMD reads every tab: Thesis, Exec Management, Peers, Model, Posture.
  - The round-59 register items read as on DEV: tabs in the first screen, the description once in the header, absences folded once,
    Model opening on Key figures with What changed in display units ("USD 1.06T"), and quiet tiles ("--" on Lenovo).
- **origin at signing:** DEV `e6fb269c`, PROD `bf780f94` (ls-remote).
- **Excluded by ruling:** dell2's 11 commits (ADVI_BILLING, IRPT_ANLREQ, NFRA_OPSWKF), which are not PROD-ready and are client-facing
  (XB-d88b @66207bce7d).

## VERDICT: SIGNED, on the CTO half's blast radius, unchanged

- **Blast radius:** portal PROD's ref `bf780f94 -> fa5ba2af` and the PROD build it triggers. Nothing else.
- **Rollback:** PROD back to `bf780f94`, same session, by the `/prod-deploy` owner.
- **Bound to `fa5ba2af`:** any other hash is not covered.
- **No word from Andrew is owed:** `/security-analysis` is requireInternal (law d92d08c448).
- **Carried, not blocking:** Lenovo's Peers Average price cell is blank with no mixed-currency line in its fold (round 60's line did not
  fire for this case). It goes to the round-61 list beside the CTO's rename of `generation_captions_present`.

**SIGNED** -- `2.0.0_SA_COO~D1`.
