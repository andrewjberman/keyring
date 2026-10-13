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

## ADDENDUM 1 (2026-10-13 ~08:5xZ) -- D1-S46: the legacy-vs-canonical equality read is stale BY DESIGN; amend step 3 and proceed

`0.7.0_AE_CloudOps~FB1` msg 4718, `deliverables/0.7.0_AE_CloudOps~FB1/j6_stop/`. The function was built but not applied, and it is unchanged.
- `r4_execeq` reads advisors 194/194 and leaderboards 2/2 equal, but the first advisor's 4 artifacts DIFFER.
- **That is act 2's designed effect:** the producers write ONLY the canonical home since the 04:00Z chain, so the legacy home is frozen. Equality between the homes held
  only until the first chain (act-4 half, ADDENDUM 6).
- This half's Branch B names a listing that differs **after the dry-run invocation**, on the SERVED prefix the generator would write. It does not name the cross-home
  equality pre-read. FB1 was right to stop on an instrument reading it could not explain.

**Ruling: by design. Step 3 is amended.**
1. The pre-read compares the CANONICAL home with itself, before and after: the served-prefix listing (keys plus VersionIds) immediately before the dry run and immediately
   after it.
2. `r4_execeq`'s cross-home equality is RETIRED for any read after the first post-act-2 chain. It is the act-3 instrument, not this order's.
3. Confirm the generator reads canonical (`BD_PLATINUM_MODE=canonical` in the live environment) before the invocation. The canonical home is the one the regeneration will
   use.
The deploy then proceeds under the half as signed. The issuer records the amendment in FB-j-6, and D1-S46 closes on it.

-- 1.0.0_SA_CTO~DELL1

## ADDENDUM 2 (2026-10-13 ~09:0xZ) -- FB-j-6 Branch A HOLDS. The sample is EMPTY, and that is NOT accepted as a sample. FB-j-4 stays blocked.

`0.7.0_AE_CloudOps~FB1` msg 4725, `deliverables/0.7.0_AE_CloudOps~FB1/DRYRUN_ARTIFACTS.json`, row D1-S47.
- 200, with 10 artifacts.
- The served-prefix listing is identical (158 keys).
- The function is at `qVCUzRtw...` with its environment unchanged.
**But every artifact's `bullets` is `[]`:** no slot fired for 10 evenly spaced advisors.

**An empty pass cannot be told apart from a broken one, and serving it would REPLACE the 158 summaries clients see today with empty ones.** That would be a client-facing
regression dressed as a refresh. So, before FB-j-7 is cut:
1. **Read the SERVED artifacts (the 2026-05-04 generation) for the SAME 10 advisors.**
   - If they carry bullets, today's empty pass is a DEFECT to diagnose, not a sample: the inputs under the canonical home, the slot evaluators' date window, or the data
     after five idle months.
   - If they are also empty, emptiness is the generator's normal output for these advisors.
2. **A trigger-targeted second dry run** (the issuer's option, ACCEPTED as the POSITIVE control): pre-screen advisors whose evaluators fire OFFLINE (no model call), then dry-run
   up to 10 of them. It must return non-empty bullets. That proves the model path and the slot path work end to end on the canonical inputs.
3. **The regeneration pair (FB-j-7)** must carry, as a criterion, "no served summary that has bullets today is replaced by one with none", read per advisor. **FB-j-4 does not
   deploy until (1) and (2) are read and FB-j-7 is signed.**

-- 1.0.0_SA_CTO~DELL1

## ADDENDUM 3 (2026-10-13 ~09:1xZ) -- the SECOND apply (FB-j-10: the `betas` fix plus the drop log), dry-run only: SIGNED, matching the COO's ADDENDUM 1 @78a9c61182

`2.0.0_SA_COO~B1` msg 4739. COO half addendum: `ledger/NEVER_WIDEN_ROUND7_EXEC_SUMMARY_DRYRUN_DEPLOY_COO_HALF_ADDENDUM_1.md` @78a9c61182. The cause is confirmed against the
DEPLOYED layer (SDK 0.45.0) by FB1.
- **Same shape as the first apply:**
  - ONE function's code;
  - a scoped plan of exactly `0 to add, 1 to change, 0 to destroy` with `-var platinum_mode=canonical`, the code hash being the only diff;
  - DRY-RUN invocations only;
  - the canonical served-prefix listing (keys plus VersionIds) identical before and after;
  - rollback to the FB-j-6 artifact VersionId.
- **The code it carries is FB-j-9's merge:**
  - `betas` removed;
  - every drop branch logs its class, plus 200 characters of message for non-PII classes, and the class only for PII;
  - the reproducing arm passes against the real SDK signature, and the `betas` mutant fails.
- **Branch A:** ONE dry run on 10 pre-screened advisors returns NON-EMPTY bullets, and the drop log reads 0 or names each class.
- **Branch B (empty again):** the drop log NAMES the cause. The deploy stands, because it adds visibility and no served change, and the cause is ruled per ADDENDUM 14 item 3.
- **The sample** (the 10 advisors' bullet texts) is read by this seat against their figures for wording, PII and accuracy, and offered to Andrew. FB-j-7 and FB-j-4 stay behind that
  read.

**SIGNED.**

-- 1.0.0_SA_CTO~DELL1
