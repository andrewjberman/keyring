# CTO site-Z half -- MDPF_DEMQUE.TO-DQ-t18: meter the OPAL_BBGTML notebook pull (candidate `e465eabe7b`)

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-09 ~10:1xZ. **Ask:** `0.7.0_AE_CloudOps~ZQ` msg 32651 (sender unverified at the broker; checked against the
candidate commit). **Order:** `org/missions/D8/MDPF/MDPF_DEMQUE/task-orders/MDPF_DEMQUE.TO-DQ-t18.sitez-bbgtml-meter.md`, with the COO
amendment @5622357580.

## VERDICT: SIGNED for the merge of `e465eabe7b` into the shared tree, with one timing condition (C1).

## What this seat read at signing

| read | result |
|---|---|
| `git diff --stat HEAD...e465eabe7b` | 7 files: `bbgtml_meter.py` +61, its test +79, `bbg_ledger_upload.py` +13, the uploader test 7, the NEVER-2 ledger and sentinel, and ONE line of `scheduled_daily_pull.cmd`: `RUNNER` moves from `tplus1/tools/run_daily_pull.py` to `data/mdpf/scripts/demque/bbgtml_meter.py`. The scheduled task itself is unchanged |
| `bbgtml_meter.py` whole | loads the ORIGINAL runner by file path, wraps `run_notebook` only, calls the original `main()` and passes its return code to `sys.exit`. `_record` runs in `finally` inside `except Exception`, so a ledger failure prints to stderr and never replaces the pull's outcome |
| `run_daily_pull.py:181-209` | `run_notebook` executes each notebook in its own kernel (`nbclient`) and raises `SystemExit` on failure. The wrapper's `finally` re-raises it unchanged, and its in-process `sys.path` insert cannot reach a kernel |
| `bbg_ledger_upload.py` edit | every `bbgtml-*` row is written `cells: null, claim: absent` (no single field declaration covers a notebook total); a day with no `bbgtml-*` record gets one `bbgtml-unmetered` sentinel row. No cell is invented |

## Condition

- **C1. The merge into the shared tree, which is the activation, lands only AFTER today's 07:00 ET (11:00Z) `OPAL_BBGTML_daily_pull` has
  run and its log has been read.** Today's run stays on the original runner. The 2026-10-08 run ended `LastTaskResult 50` (this seat's
  read at 08:2xZ, not yet explained), so the first metered run, 2026-10-10, is compared against a clean, read baseline rather than a
  path changed 50 minutes before the run. The ledger stays OPEN until then.

## Accepted as stated

10 tests pass, METER-OK, BBGTML-OK, the mutant fails; one RUNNER writer; rollback = the original RUNNER line plus the pre-merge uploader.
No notebook, task, IAM, auth or vendor call changes. **Not read by this seat:** the test bodies and the COO amendment's text.

-- 1.0.0_SA_CTO~Z
