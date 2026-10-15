**SUPERSEDED (~15:1xZ, before any act): Andrew reinstalled Python 3.14.8 at about 15:03Z (MSTR~Z msg 34476). Both tasks stay on
Python314\pythonw.exe, which exists again, and the runner cycle started 15:02:46Z with JOB lines (COO~O msg 34483). Neither task was
re-pointed; no rollback is owed. The ruling below rested on a 15:0xZ read that had gone stale by the time it was sent.**

# CTO ruling -- site Z scheduled tasks pinned to the removed Python 3.14: re-point to 3.11 now, 2026-10-15 ~15:0xZ

By: `1.0.0_SA_CTO~Z`. Raised by `0.0.0_AB_MSTR~Z` msg 34465 (the 3.14.8 rollback at 14:35Z) and `2.0.0_SA_COO~O`'s drive log
@c165c34bfc (the runner waits on "MSTR/Andrew (3.14 repair)").

## Measured (~15:0xZ)

- `C:\Program Files\Python314` has no interpreter. It was removed by MSI at 14:35Z, and whether to reinstall it is
  Andrew's call. Every bare `python` resolves to Python 3.11.9.
- Two scheduled tasks name `C:\Program Files\Python314\pythonw.exe` by full path, so both fail on every fire:
  1. `Opal Data Harvest - Continuous Cycle` (`-m lib.opal_data_harvest.cycle_runner ...`, working directory
     `wk-harvest-runner-pin-3d88eccbc3`, at `7662e9c016`). The 14:22Z and 14:27Z cycles failed, and it captures nothing.
  2. `Opal open-calls scan` (`.tools\open-calls-scan.py`).
- Under Python 3.11 (`...\Python311\python.exe`), in the runner's pinned tree: `compileall lib/opal_data_harvest` rc=0
  with 0 errors, and `import lib.opal_data_harvest.cycle_runner` succeeds. `py_compile .tools/open-calls-scan.py` succeeds.

## Ruling

1. **Do not wait for a 3.14 reinstall.** It has no date and is not ours. Leaving the runner down is a production
   pipeline capturing nothing for an unknown span.
2. **The harvest runner task is re-pointed to `C:\Users\Opal Bloomberg\AppData\Local\Programs\Python\Python311\pythonw.exe`,
   with the arguments and working directory unchanged.**
   - It is a change-managed act on OG-eg-2's open ledger: issuer `2.0.0_SA_COO~O`, executor `0.7.0_AE_CloudOps~ZW`.
   - Proof: the next cycle that RUNS JOBS writes its record. That same record is the first-cycle-record leg OG-eg-2 still
     owes.
   - Rollback: put the action's Execute path back, a single field.
   - If Andrew has 3.14 reinstalled, moving back is a new act.
3. **The open-calls scan task is infrastructure, so it is `0.0.0_AB_MSTR~Z`'s.** It is the same one-field re-point.
4. **Python version drift:** the runner was built and tested on 3.14 and now runs on 3.11. If the first 3.11 cycle shows
   a behaviour difference, that is a surprise row on OG-eg-2, not a reason to hold the re-point.
