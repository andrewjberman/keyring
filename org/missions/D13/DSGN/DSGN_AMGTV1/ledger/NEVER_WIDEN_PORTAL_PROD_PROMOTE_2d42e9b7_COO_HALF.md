# NEVER-WIDEN CO-SIGN -- COO HALF. Portal PROD promote `f73f9ab0 -> 2d42e9b7` (DSGN_AMGTV1 FWD-1's PROD walk)

**Signer:** `2.0.0_SA_COO~D1`, 2026-10-09 ~05:3xZ, beside `NEVER_WIDEN_PORTAL_PROD_PROMOTE_2d42e9b7_CTO_HALF.md` @b44ccdfe2c (msg 1769).

## Measured at signing (`git ls-remote` + `git log f73f9ab0..2d42e9b7` in the dell1 portal repo, ~05:3xZ)

- origin DEV = `2d42e9b733`, origin PROD = `f73f9ab0eb`. The set is 25 commits and 40 files (+1417 -156), matching the CTO half's
  measured set.
- **DSGN_AMGTV1, 8 commits (this half covers them):**
  - `2d42e9b7`, `19a172da`: round 57, AV-zzi-2 and AV-zzi-1. CTO-approved @e8b9029fba; walked signed-in on DEV 04:18Z.
  - `0008ddd3`, `9067c5a5`: round 56, AV-zzh-1. Approved msg 1458; walked 02:24Z.
  - `8d2a08a9`: round 55, AV-zzg-1. Approved msg 1319; walked 01:50Z.
  - `84e13d0f`, `be3c3547`, `2b8cbe4c`: round 53. Approved by `1.0.0_SA_CTO~Z` (msgs 32088/32089) and on DEV per the CTO~Z hand-over.
  Every changed file is under `src/pages/SecurityAnalysis/` or `src/pages/Freshness/`, and both routes are internal.
- **AMGT_CORPUS, 9 commits (this half covers them, as the CTO half assigns):** `21719e17`, `88184ca2`, `4af1297f`, `c243dc2b`,
  `636ce634`, `5a526eba`, `de6fc425` and the two DEV merges `0498827c`, `1cbc56a7`. This is CORPUS round 40's portal candidate. Its
  amendment `5a526eba` cites the CTO review of `636ce634`. It is on DEV and touches SecurityAnalysis presentation files (SecurityOverlay,
  ThesisTab, ModelTab, reasonWords). This seat did not walk CORPUS's outcomes separately: the 04:18Z and 05:12Z walks of DEV exercised
  the same pages with those commits present, and found no break that traces to them.
- The other 8 commits (IRPT_BCKEND, IRPT_YCDGEN, TCKT_VNEXT) rest on the laptop CTO's XB-bf16 answer, not on this half.

## VERDICT: SIGNED, on the CTO half's blast radius and its four conditions, unchanged

- **Blast radius:** portal PROD's ref `f73f9ab0 -> 2d42e9b7` and the PROD build it triggers. Nothing else.
- **Rollback:** PROD back to `f73f9ab0`, same session, by the `/prod-deploy` owner.
- **Bound to `2d42e9b7`:** if DEV reads anything else at the promote, this half does not cover the difference.
- **After the promote:** this seat runs one signed-in read of `/security-analysis` for AMD on PROD's build path, if the walker can reach it;
  otherwise the read is the `/prod-deploy` owner's. FWD-1's walk is then Andrew's act.

**SIGNED** -- `2.0.0_SA_COO~D1`.
