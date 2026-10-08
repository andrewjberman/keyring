# Never-widen half: MDPF_HEALGAP round 2, drain act 3 -- an induced PARTIAL day and its same-day repair (FWD-2, FWD-3), 2026-10-10

**Author:** `2.0.0_SA_COO~G1` (dell1), 2026-10-08 ~16:4xZ. **For:** `1.0.0_SA_CTO~DELL1`, who owes the CTO half.
**Status:** COO half SIGNED; CTO half owed. The terms come from ruling R2-4 (`R2_DRAIN_PLAN.md` @1fdab25b2b).
- **Vendor calls:** covered by Andrew's standing word for this runner's same-day re-run (ACT 1 approval).
- **Day:** 2026-10-10, because act 1's leg L4 needs a normal 2026-10-09 06:00Z fire.
- **Precondition:** act 1 L4 reads branch A at 2026-10-09 06:00Z, or this act does not start.

## The act, in order

1. **2026-10-09, evening (~20:00Z):** set the induce on the daily rule's target.
   - Rule `cot-rebalancer-runner-daily`, one target `cot-rebalancer-runner-daily` (live input `{"mode":"pull"}`, read 16:4xZ).
   - Input changes from `{"mode":"pull"}` to `{"mode":"pull","induce":"drop-feed:rebalancer_accounts"}` (`events:PutTargets`).
   - Read the input back with `list-targets-by-rule`.
   - This is a Terraform-managed input. The drift lasts about 10 h and is reverted in step 3.
2. **2026-10-10, 06:00-06:04Z:** the first attempt and its 2 async retries fire. On each attempt the runner:
   - pulls and lands `rebalancer_models` and `rebalancer_model_detail`, and skips `rebalancer_accounts`;
   - writes `meta/2026-10-10-result.json` with `verdict PARTIAL` and accounts `missing`;
   - writes no stamp, then raises `PartialDay`, so `on_success` (silver) does not fire.

   That makes 3 vendor pulls of two feeds each, within the 900 s event age. **FWD-2's exercise:** read the result object.
3. **~06:05Z:** restore the daily input to `{"mode":"pull"}` (`PutTargets`) and read it back. `terraform plan` on the rule
   then reads no changes.
4. **~06:06Z:** run `repair.py --date 2026-10-10`.
   - The dry run prints `MANIFEST date=2026-10-10 feeds=rebalancer_accounts keys=...`.
   - Before `--execute`, read the key sets of the two present feeds.
   - Then `repair.py --date 2026-10-10 --execute` invokes the runner asynchronously with `force=true`. This is one vendor pull,
     and per R2-2 it re-lands all three feeds with the same day's state.
   - The runner writes the result `COMPLETE` and the stamp, returns, and `on_success` fires silver.
   - **FWD-3's exercise:** the result reads `COMPLETE`, accounts has `healed_at` `null` live (R2-1), and the two present feeds'
     key sets after the repair are compared with the sets before. Any difference beyond LastModified is reported.
5. **07:00Z:** the satellites producer reads `rebalancer_models` and `rebalancer_model_detail`. Both landed at step 2, so it
   writes `as_of 2026-10-10`. Read it back.
6. **~11:3xZ:** the re-attempt target finds the stamp and SKIPs. The 13:30Z floor and the 13:50Z reader read normally.

## Writers counted

| property | writers | notes |
|---|---|---|
| the daily target's input | 2 | Terraform, and this act's `PutTargets`. Terraform is not applied on this root during the window: the act is announced to `0.0.0_AB_MSTR~DELL1` before step 1. |
| the day's bronze | 1 | the runner |
| the result | 1 | the runner |
| the stamp | 1 | the runner |
| silver for the day | 1 trigger | `on_success` of a successful runner invoke |

## Both branches, read from each producer's own rule

- **(A) The repair lands by about 06:1xZ.**
  - The day's silver builds about 6 h earlier than its 13:30Z floor, from the repaired bronze.
  - Satellites writes on time.
  - Served delta 0: the same day's state is served at the same served times.
- **(B) The repair fails (vendor error or session lapse).**
  - The day stays PARTIAL and silver is withheld.
  - At about 11:3xZ the re-attempt target fires with the input restored, pulls all three feeds, and stamps the day. That is
    FWD-1's path, unchanged.
  - If it also fails, the 13:30Z floor serves the prior day, exactly as on any failed day before this project.
  - The induce never outlives step 3, because step 3 runs whatever step 4 does.
- **(C) The step-3 restore fails.** Tomorrow's 06:00Z fire would induce again. The act therefore reads the input back at
  step 3, and if the restore did not take, it re-applies `terraform apply -target` to the rule's target the same hour. The
  ledger leg stays open until the read-back reads `{"mode":"pull"}`.

## Armed items (CTO round-1 analysis 2.2)

- No timer and no OS task is armed for this act. Step 1 is a hand act on 2026-10-09; steps 2-6 are read and acted from this
  seat at the times named.
- If the seat is not live at 2026-10-10 06:05Z, the induce stays in place. In that case the open ledger leg and
  `0.0.0_AB_MSTR~DELL1` (told at step 1) own the restore by 2026-10-10 12:00Z.

## Rollback

| what | rollback |
|---|---|
| input | `{"mode":"pull"}` via `PutTargets`, or `terraform apply -target=aws_cloudwatch_event_target.cot_rebalancer_runner_daily` |
| result object | none needed: inert |
| bronze | none needed: same-day state |
