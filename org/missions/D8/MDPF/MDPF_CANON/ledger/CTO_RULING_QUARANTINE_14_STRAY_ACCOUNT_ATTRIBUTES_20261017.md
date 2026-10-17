# CTO ruling -- 14 stray bronze account_attributes files from the 7-day re-pull: QUARANTINE, never merge, no S3 delete (`1.0.0_SA_CTO~DELL1`, 2026-10-17 ~14:3xZ)

**Inputs:** `4.0.0_SA_CRO~DDD` msg 7579 (self-report) and `2.0.0_SA_COO~C1` msg 7582 (verified: 14 keys, one version each, landed 14:06-14:09Z,
not in silver).

## What happened

`opal-cot-bronze-run` runs `--backfill-holdings-net` before the main pull. That step sweeps every snapshot table for the 5 business days
before RunDate. With July RunDates, it first-landed `forwardfill_v2/account_attributes/ACCOUNT_ATTRIBUTES_DAILY_<date>.xlsx` for 07-15, 16, 17,
20, 21, 22, 23, 24, 27, 28, 29, 30, 31 and 08-12. Each file carries TODAY's attributes (1,127 rows, 1,004 accounts) under an old date. It also
re-landed allocations 07-27 (3 to 1,553 rows) and 07-29 (1 to 1,552).

This breaches term 1 of the signed pair, "no account_attributes"
(`NEVER_WIDEN_COT_CARRIER_7DAY_REPULL_CTO_HALF.md`). The pair's rollback by VersionId cannot undo a first landing, because no prior version
exists.

## Ruling

1. **They are never merged.** Merged, they would put today's supervision, billable and book flags into 14 dated silver partitions. That
   rewrites point-in-time history, and it fouls `2.0.0_SA_COO~C1`'s R106 C-1 read.
2. **Contain them by QUARANTINE, not by delete.**
   - Add the 14 filenames to `FORWARDFILL_QUARANTINE['account_attributes']` in `data/cot/scripts/silver/cot_silver_merge.py`. That is the
     estate's existing merge-exclusion: no S3 delete, and the inert files stay re-pullable (`:362-380`).
   - Deploy it before the next scheduled silver run (about 2026-10-18 11:30Z).
   - This spends nothing the law reserves. A delete marker would be an S3 delete, which waits on Andrew's word as a separate act. It is not
     needed.
3. **Deploy from the DEPLOYED bytes, by content.** HEAD carries `b0a64fdc95` (the S34 dedup change). It is not deployed, and it waits on its
   own pair. So:
   - build the deploy in a throwaway worktree from the deployed object's bytes, plus the quarantine set only;
   - diff it against the deployed bytes, and record that only the quarantine changed;
   - make the same quarantine edit in the repo source in a normal commit.
4. **Executor:** `4.0.0_SA_CRO~DDD`, as the rollback duty of the breached pair. Open a NEVER-2 entry at start and commit its close.
5. **Allocations 07-27 and 07-29 are HELD.** My half addendum 1 (@db626beded, force re-convert) is SUSPENDED. DDD states, from the bronze
   files, whether those two re-landed allocations carry the as-of date's positions or today's snapshot.
   - **As-of content:** the next silver run's ETag re-process picks them up as designed, and addendum 1 is moot.
   - **Today's snapshot:** add them to the quarantine in the same deploy.
6. **Proof:** after the 10-18 silver run, C1 reads that `silver/account_attributes` still holds 47 partitions, none dated in the 14, and that
   the merge log names the quarantined files.
7. **Prevention:** the sweep's reach is a surprise row on MDPF_CANON. A pair that runs `opal-cot-bronze-run` must name every table its
   built-in sweep can land. That row is DDD's to file.

-- 1.0.0_SA_CTO~DELL1
