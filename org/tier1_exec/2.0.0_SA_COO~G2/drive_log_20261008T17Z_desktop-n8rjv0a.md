# /canonical-drive IRPT_YCDGEN -- 2.0.0_SA_COO~G2 on dell2, 2026-10-08 ~06:4xZ-17:3xZ (dell2 reboot 16:38Z; reseat)

## Reconstructed gap (06:4xZ to the 16:38Z reboot; no tick log was committed for it)
Evidence only, from the broker ledger, the shared tree and the worktrees:
- 10:40Z sent msg 1245 to 1.0.0_SA_CTO~DELL2: u-6 premise measured false (worker HEAD df5280bce5: AC1 PASS, AC2 FAIL, AC3 FAIL; v1 is sha-pinned, v2 is the served contract). Ruled YES at msg 1250 (11:23Z, read 13:01Z): recut on v2.
- 13:01Z read 1254/1258 (release 1 LIVE 10:06Z, CodeSha256 ZspX0qD2..., after-read 4 PASS) and 1260 (measure and close ledger irpt-ycdgen-r6-branch-b2-20261006).
- 13:50Z ledger closed by the tool (leg F1 SUPERSEDED per msg 1260), left UNCOMMITTED in the shared tree at the reboot.
- 1305 (Andrew "HAVE DELL2 RETRY", 14:08Z) and 1307 (CTO ruling: ~G2 runs the F1 retry, five conditions) were OFFER-EXHAUSTED -- never read before the reboot.

## Reseat ~17:0xZ (Andrew-direct 165xZ record, 0.0.0_AB_MSTR~DELL2 deliverables)
- /watcher: registered (was NOT REGISTERED); Monitor armed, script pid 11760; inbox empty; ledger 113 rows since 10-07, 111 READ + 2 OFFER-EXHAUSTED (1305, 1307) opened and acked.
- LIVE_ARMS: my /canonical-drive IRPT_YCDGEN row (CHOSEN) is live. Drive lease: none (FULL).
- Committed the ledger close @7ff70823b3 (shared tree; push state LOCAL, origin CLOUD a92d59d74f by ls-remote).
- u-6 RECUT on ruling 1250 @b95f3c25e8 (branch wk-IRPT_YCDGEN-6, C:/dev/wk-ycdgen-u6): the generator reads AnalysisReport from `_contracts/AnalysisReport.v2.schema.json`; v1 byte-frozen; AC2 body compare with header excluded. Gate limb: none graded it. Worker 0.9.0_WK_IRPT_YCDGEN~6 re-spawned on the recut face.
- F1 retry (msgs 1305/1307): mapping the deployed portal route, the authorizer and a Cottonwood-allowed principal before the run. Risk WORLD (a real submit). Result goes to 0.0.0_AB_MSTR~DELL2 either way.

## Next
1. F1 retry per CTO_RULING_IRPT_YCDGEN_FWD1_DELL2_RETRY_20261008.md conditions 1-5; PASS -> FWD-1 seat-driven arm REALIZED + release 1 after-read 5; else one surprise row.
2. Drain u-6 on its report; then the round-6 drain.

## Compiler Tools
- comp-find / comp-which: not used this window (reads were exact files named by messages and commits).
- Rail: one raw recursive grep was refused by the HUD; re-run with the native Grep tool.
