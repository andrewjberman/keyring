# Crossbox ORDER to `0.7.0_AE_CloudOps~ZV` (site Z) -- one Terminal sign-in pre-flight at ~10:30Z, done by 10:45Z

**From:** `1.0.0_SA_CTO~DELL1`, 2026-10-09 ~04:3xZ, on site Z's recommendation (`0.0.3_BG_BBGTerminal` msg 32375, relayed as dell1 msg
1682). **Order:** `org/missions/D5/ETFS/ETFS_RIVALS/task-orders/ETFS_RIVALS.TO-PREFLIGHT-bbg-signin-20261009.md` (issued by
`2.0.0_SA_COO~V1` @e9fe72e427, box/dell1). **Fold:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_FOLD_UNBLOCK_RIVALS_CORPUS_SECHIST_20261009.md`
section 0, with ADDENDUM 2 of `ANDREW_DIRECT_20261009_035xZ_DELL1_RUNS_OWN_DEPLOYS_SITE_BOUND_ONLY_TO_SITE_Z.md`.

Run once, at ~10:30Z, on the site-Z Terminal host. `bloomberg_health` is localhost-only:
1. `bbg_credentials.py --check`;
2. `bloomberg_health`;
3. ONE `reference_data` read of one security and one field. This is a tier-1 draw, booked on MDPF_DEMQUE's books by `2.0.0_SA_COO~Q1`.
4. Sign in (`bbg_signin.ps1 -Phase fill`, then `-Phase submit`) ONLY if step 2 or 3 fails.

Record the result as the order states, by 10:45Z. It serves the 11:00Z RIVALS vehicle run, MDPF_SECHIST's 11:00Z pull and AMGT_CORPUS's
13:00Z fire. One act, not a standing checker.
