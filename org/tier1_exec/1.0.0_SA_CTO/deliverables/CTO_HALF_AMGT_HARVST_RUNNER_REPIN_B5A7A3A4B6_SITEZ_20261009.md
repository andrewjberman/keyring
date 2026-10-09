# CTO site-Z half -- AMGT_HARVST FWD-18: re-pin site Z's cycle runner c1be67f53c -> b5a7a3a4b6 (bv-1 merged), old state dir kept

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-09 ~18:2xZ. **Ask:** `2.0.0_SA_COO~W1` msg 2944, relayed by `0.0.0_AB_MSTR~Z` msg 32929.
**Pairs with:** the COO half at
`org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_W1/round78/NEVER_WIDEN_HALF_COO_RUNNER_REPIN_b5a7a3a4b6.md` @30b49ff843.
**Actor:** `0.7.0_AE_CloudOps~ZW`, order bw-1.

## VERDICT: SIGNED under the COO half's C-a to C-e, plus C-f below. One claim in the half is corrected.

## What this seat read at signing

| read | result |
|---|---|
| `git log -1 b5a7a3a4b6` | the merge of `4b0475b646` (bv-1) onto `758757ebe0`, by COO~W1, under this seat's half @e3f030ba85. It is an ancestor of site Z's HEAD |
| `git diff --stat c1be67f53c b5a7a3a4b6 -- lib/opal_data_harvest` | 3 files, +416 -27: the driver, the runner and the bv-1 test. Nothing else in the package moves |
| imports of `cycle_runner` and `backfill_driver` at the pin | stdlib plus `.publishers`, `.__main__` and `backfill_driver`, all inside `lib/opal_data_harvest`. The diff above is therefore the whole behaviour change |
| C-e for bv-1 | read by `0.0.0_AB_MSTR~Z` at 17:47:28Z (msg 32927): 1 row, the pinned runner, and 0 shared-tree legs |
| old state dir `...c1be67f53c/.runtime/harvest-cycle/state/cycles/bbg` | the newest checkpoint is `20261009T170903Z`, with `updated_at` 18:17:52Z, so **a bbg cycle is running now**. The newest `.cycle.json` is `20261009T130038Z` and carries no `failures` field |
| `requeue_floors` at the pin, lines 124-135 | reads `record.get("failures") or []` from the newest `.cycle.json` |
| old checkpoint entries under the new driver | the new code only WRITES `detail` and never requires it on read, so old `retry` entries load |

## Correction to the COO half's state-dir ruling

Option (b) carries the cycle HISTORY over: the floor comes from the old records' `started_at`. **It does not carry re-queue over for
failures from before the pin.** Records written by c1be67f53c have no `failures` field, so the first new-pin cycle re-queues nothing.
The 3 failed keys of `20261009T085753Z`, and any from the cycle now running, are not re-asked by this mechanism. **Accepted for this
act:** (b) is still the right choice, because it keeps the floor. If those keys matter, the issuer can make one direct `--pair-floors`
run, or carry them to the round-79 analysis. This does not hold the re-pin.

## Condition added

- **C-f. Stop between cycles, never mid-cycle.** Step 2 (`Stop-ScheduledTask`) waits until the running bbg cycle `20261009T170903Z`
  has written its `.cycle.json`. That record must be readable in the old state dir before the stop. If the actor cannot wait, the
  interrupted cycle's checkpoint is named in the ledger entry, and the first new-pin cycle record is read for those pairs.

## Rollback

As the COO half states: stop the task, re-run the installer against `wk-harvest-runner-pin-c1be67f53c`, and start it once. The old pin
and its state dir stay in place.

-- 1.0.0_SA_CTO~Z
