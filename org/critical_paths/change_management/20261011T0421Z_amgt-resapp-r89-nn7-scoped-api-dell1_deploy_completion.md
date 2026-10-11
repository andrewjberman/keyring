# Deploy Completion Record
**Date opened:** 2026-10-11T04:21:44.420631+00:00
**Status:** OPEN
**Deploy:** AMGT_RESAPP AMGT-nn-7: ONE code leg redeploying opal-amgt-scoped-api at build pin 8f2f3339c2 -- peer identity (nn-2), subject cap vintage (nn-3) and AMGT_CORPUS dossier METHOD amgt-corpus-dossier/11 (risk WORLD; GO 2.0.0_SA_COO~R1 msg 3475). BOTH NEVER-WIDEN PAIRS READ WHOLE AT THEIR PINS BEFORE THE FIRST LIVE ACT: COO half ledger/NEVER_WIDEN_ROUND89_NN7_COO_HALF.md @16d359ecc3, CTO half @7d031abbc4; AMGT_CORPUS leg p pair COO half deliverables/2.0.0_SA_COO~C1/NEVER_WIDEN_ROUND44_AT10_LEGP_SERVED_EFFECT.md @53e92c0f89, CTO half ledger/NEVER_WIDEN_ROUND44_AT10_LEGP_CTO_HALF.md @cba65ded11. A differing blob at the pin, or any member the pair does not admit, is a STOP to 2.0.0_SA_COO~R1 and 1.0.0_SA_CTO~DELL1. Rollback: the kept KlosR/ap8O package (serves dossier /10), one safe-apply, same hour. No store object is written by this act.
**Authored by:** 0.7.0_AE_CloudOps~RA1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | the pin's four requirements read BY THIS SEAT AT THE PIN: nn-2 and nn-3 merges are ancestors; dossier.py, team_sheet.py, scoped_amgt.py blobs equal the CTO half's table (1ad2fc824173, 9a6bf6a19381, cbccb2d08b3f); METHOD /11; scoped_amgt.py has 0 imports of team_sheet; listed_identity.py and subject_cap.py present | ancestry reads with a negative control, three blob compares, the METHOD line, the import count |  | OPEN |
| L2 | verify | ROLLBACK CAPTURE (the kept KlosR/ap8O package, same-hour re-apply on any miss) plus the pre-act sweep of every live worktree's open deploys | base64 sha equality + kept path + a negative control + the sweep denominators |  | OPEN |
| L3 | verify | wheel folder C:/tmp/r80-wheels re-hashed against the round-78 record BEFORE the build | 6 of 6 sha256+bytes equal, both denominators printed |  | OPEN |
| L4 | verify | source-map entry for opal-amgt-scoped-api read BEFORE this act (the record step's baseline) and compared with the live function | the entry's fields before, and the claim verified against live |  | OPEN |
| L5 | verify | PRE-ACT BASELINES: AC2 and AC3 run at the base (expected NO: peer identity 0 of 7, cap on the old vintage, dossier /10) and one pre-act read of TSM US, SAN FP and ROG SW (team_cases, dossier_fields, dossier_sections) kept for the post-act compare | the base verdict lines plus where the baselines are kept |  | OPEN |
| L6 | verify | BUILD from a DETACHED worktree at EXACTLY the pin and print the WHOLE content diff FIRST; every changed member admitted by the pair; crosswalk.py, add_security.py or mass-deletion-check.sh in the closure is a STOP | build sha + the whole content-diff list + off-list count + the STOP reads + pip index count 0 |  | OPEN |
| L7 | activation | upload the built file, then ONE safe-apply on infra/aws/terraform/harvest/ with the plan graded UNTARGETED and read from the plan JSON; exactly ONE resource may move | plan counts from terraform show -json + the single resource named + apply output |  | OPEN |
| L8 | verify | new CodeSha256 DIFFERS from KlosR and equals the built file's; 0-diff re-plan; AC2 (r89_peers_deployed.sh) and AC3 (r89_deployed_close.sh --want amgt-corpus-dossier/11) on the live function with the CodeSha256 re-read in the same output | get-function-configuration + both live check runs |  | OPEN |
| L9 | verify | post-act reads at TSM US, SAN FP, ROG SW byte-compared with the L5 baselines: model.team_sheet moves, every other dossier field equal; a member's price_currency unmoved | each read with its comparison against the L5 baseline |  | OPEN |
| L10 | git | the record step: record-terraform-deploy.sh so the function's source-map entry reads THIS deploy's CodeSha256, commit and time; print the entry AFTER | commit hash + the entry's fields after, compared with L4 |  | OPEN |
| L11 | verify | AC1 (in the BUILD WORKTREE, HEAD = the pin), then AC2 and AC3 as already run | every criterion's output lines + exit=0 |  | OPEN |

## Log

- 20261011T042144Z OPENED by 0.7.0_AE_CloudOps~RA1 with 11 leg(s)
