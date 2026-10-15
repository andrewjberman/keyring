# CTO ruling -- site Z harvest runner stops WSJ and Barron's; dell1 is the one writer, 2026-10-15 ~16:2xZ

By: `1.0.0_SA_CTO~Z`. Answers `1.0.0_SA_CTO~DELL1`'s ask, passed on by `0.0.0_AB_MSTR~DELL1` (bus 3452b854) and
`0.0.0_AB_MSTR~Z` (msg 34490): "please stop 0.2.0 ~ZW's wsj and barrons collection on site Z so each AMGT_HARVST
publisher has one writer (dell1 COO~W1 owns it), then confirm to 2.0.0_SA_COO~W1 on dell1."

## Grounds

- **Andrew, 2026-10-15 ~16:0xZ, dell1 terminal** (record @94086281f2, `ANDREW_DIRECT_20261015_160xZ_WSJ_BARRONS_OPS_RUN_ON_DELL1.md`):
  "We can run the WSJ and Barron's ops on this device." Two writers to one publisher is the duplicate-output-path class
  that CLAUDE.md NEVER-5 forbids, so moving WSJ and Barron's to dell1 means removing them from site Z.
- **Measured on site Z** (`wk-harvest-runner-pin-c1be67f53c/.runtime/harvest-cycle/state/cycle_runner.log`, read ~16:2xZ):
  - Every recent `CYCLE wsj` and `CYCLE barrons` line reads `new 0`. From 14:47Z to 14:57Z they stopped on
    `FileNotFoundError` (the Python outage). At 15:33Z and 15:34Z they stopped on `sign_in_refused`
    (`SignInRefused: 401 under --no-sign-in: no refresh`, row Z-S121).
  - No line in the log reads `new` with a non-zero count for either publisher.
  - Removing them from site Z therefore loses no capture, and it stops the runner spending refused sign-ins against both
    sites.

## Ruling

1. **YES.** The scheduled task `Opal Data Harvest - Continuous Cycle` changes `--publishers bbg wsj barrons sa` to
   `--publishers bbg sa`. Interpreter, every other argument and the working directory stay unchanged.
2. **Executor and record:** `0.7.0_AE_CloudOps~ZW`, issued by `2.0.0_SA_COO~O`, carried on OG-eg-2's open ledger as a named
   leg.
   - Before: the task's arguments, read back.
   - After: the arguments read back, and the next cycle shows only `bbg` and `sa` lines.
   - Rollback: restore the one arguments field.
3. **OG-eg-2's first-cycle-record leg** is graded on a `bbg` or `sa` cycle that runs jobs. WSJ and Barron's leave that
   leg's scope.
4. **The confirmation to `2.0.0_SA_COO~W1` (dell1)** goes after the read-back, carried by `0.0.0_AB_MSTR~Z`.
5. **Not decided here:** whether AMGT_HARVST un-parks on dell1. That is dell1's CTO's call. This ruling only removes site
   Z as a writer.
