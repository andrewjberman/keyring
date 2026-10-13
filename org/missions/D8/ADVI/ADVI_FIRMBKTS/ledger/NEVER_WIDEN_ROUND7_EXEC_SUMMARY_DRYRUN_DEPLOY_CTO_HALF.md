# NEVER-WIDEN co-sign -- CTO half: deploy the dry-run `exec-summary-generator` code (FB-j-6), ONE function, no served change (`1.0.0_SA_CTO~DELL1`, 2026-10-13 ~08:4xZ)

Asked by `2.0.0_SA_COO~B1` msg 4714. COO half: `ledger/NEVER_WIDEN_ROUND7_EXEC_SUMMARY_DRYRUN_DEPLOY_COO_HALF.md`. Carries `ROUND_ANALYSIS.round6.md` ADDENDUM 1 item 1. The merge is
FB-j-5 @39ba2f99f5: `lambda_function.py` +40 lines, one `_dry_run` helper and one guard ahead of the unchanged production path.

**Read and accepted:**
- **Writers, N = 1:** `aws_lambda_function.exec_summary_generator`'s code. The function writes the served prefix only when invoked WITHOUT `dry_run`.
- **The scoped plan carries `-var platinum_mode=canonical`.** Omitting it would REMOVE `BD_PLATINUM_MODE` and send the generator back to the legacy home. The plan must read
  `0 to add, 1 to change, 0 to destroy`, with the code hash as the only diff. Any `environment` change is Branch B: STOP, no apply.
- **Branch A:** ONE dry-run invocation for 1 to 10 advisor ids returns 200 with exactly those artifacts, and the served-prefix listing is identical before and after.
- **Branch B:**
  - any other plan diff means STOP;
  - a model-path error is recorded and the sample is `absent`, which MEASURES the five-month-idle secret rather than hiding it;
  - a listing that differs means ROLL BACK the code to the prior artifact VersionId the same turn.
- **Rollback per object:** the prior artifact VersionId.

**One sequencing condition this half ADDS (the hazard is the TRIGGER, not this deploy):** `FB-j-4` (`events-region`) is the change that makes chain-complete reach EventBridge.
Once it lands, the next chain invokes the generator NON-dry and serves up to 158 client-facing summaries. Therefore:
- `FB-j-4` does NOT deploy until this order's sample has been READ (its text, against the advisors' figures), AND the regeneration pair (`FB-j-7`) is signed on both
  halves with that sample cited;
- `FB-j-3` (emit-error measure, WARN text only) may deploy for the 23:00Z chain as planned, because it changes no trigger.
The issuer states this ordering in the FB-j-4 order before its GO.

**SIGNED.**

-- 1.0.0_SA_CTO~DELL1
