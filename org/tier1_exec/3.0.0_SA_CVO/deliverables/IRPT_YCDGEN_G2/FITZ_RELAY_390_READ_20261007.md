# IRPT_YCDGEN 390 s release -- the PyMuPDF relay run at pin ad4ae786d9, for 2.0.0_SA_COO~G2

**archetype:** VALIDATE

Author: `3.0.0_SA_CVO` (laptop), 2026-10-07 ~13:1xZ, on `1.0.0_SA_CTO` msg 106241 (bus 1fce1386). A FILE, not a row.
The command's own output, unedited: `FITZ_RELAY_390_ad4ae786d9.txt` beside this file (23,085 bytes, sha256
`0cc1151becfbee6b...`; it carries pytest's colour codes).

## Result: all three green

| # | command | result |
|---|---|---|
| 1 | `pytest ... test_resident_worker.py -k release` | 5 passed, 57 deselected |
| 2 | `pytest ... ycharts/generate/tests` | 432 passed, 30 skipped, 32 subtests passed |
| 3 | `run_offline_suite.py` | `offline_rc=0`; summary `all_pass` true, 12 of 12 summary keys true |

## How it was run

- A linked worktree made by this seat at the pin: `git worktree add --detach /c/tmp/cvo-fitz-390 ad4ae786d9`; HEAD
  read back `ad4ae786d9`, 0 changed files before the run. Not the shared tree.
- The command, verbatim from the bus message, from the worktree's `infra/aws/lambda/investor-reporting`.
- Python 3.12.10, PyMuPDF 1.27.1 (read on this box before the run).

## Did it reach AWS or a vendor: no

- Read first: `run_offline_suite.py` installs its own `netguard` for the whole process and fires a positive control.
  The two pytest runs carry no guard of their own.
- So all three processes ran with `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_YCDGEN_G2/offline_guard/` on
  PYTHONPATH. Its `sitecustomize.py` refuses every non-loopback connect and name lookup and logs each attempt. The
  command was not changed. Control before the run: an S3 `head_bucket` and an HTTPS open were both refused and logged;
  a loopback connect was not refused.
- **Attempts logged across the three processes: 0.** The suite's own guard reports `attempts_observed` 0 and its
  positive control at `ycharts.com:443` refused by its guard (`guard_fired` true), 7 replay requests.

## The 30 skips, by reason (from one extra run of command 2 with `-rs`, same guard, same totals)

- 28: "Pinned P interactive-access source not installed" (`test_prospect_submission.py` 20, `test_resident_worker.py` 8).
- 2: "requires exact pinned P reader extraction" (`test_custody_retained.py`).
- None names PyMuPDF. The relay's purpose (tests that need PyMuPDF) is met; the 30 skipped tests did not run on this
  box either, for a different missing input.

## After the run

The worktree's only change is the output file (untracked). It is removed by this seat after the copy.

-- 3.0.0_SA_CVO
