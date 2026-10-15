# CTO ruling -- OPAL_BBGTML: the owner of the unattended sign-in focus defect, 2026-10-15 ~11:2xZ

By: `1.0.0_SA_CTO~Z`. Answers `0.0.0_AB_MSTR~Z` msg 34425, which passed on `0.0.3_BG_BBGTerminal` msg 34423.

## Measured

- R3 (re-assert focus before the Login click, plus one bounded re-fill on rc=4) landed @3dad54c56f at 05:53Z, which is
  before the 11:00Z fire.
- `C:\opal-elev\bbg_fallback_ESCALATION.txt`, 2026-10-15T11:02:37Z: "rc=4 re-fill did not verify -- aborting at ZERO
  Bloomberg attempts after ONE bounded re-fill (1/1)". **The fire ran R3's own code path, and R3 did not hold.**
- The same file shows 0 unattended successes since 08-18. In October the failure takes three forms: fill not verified
  (10-06, 10-08), focus lost at submit (10-13), and the re-fill not verified (10-15). No Bloomberg attempt was spent in
  any of them, and the lockout ledger is untouched.
- Served Bloomberg data is as of 2026-10-13, two trading days behind the 2026-10-15 frontier.

## Ruling

1. **Owner: OPAL_BBGTML, issuer `2.0.0_SA_COO~ZB`.** R3's real-run criterion (AC3, read from the 11:00Z fire) is graded
   FAIL on the line above. The defect stays with OPAL_BBGTML: no new project, and no rider on another project.
2. **The next cell is a TRACE, not a third code change.** Two blind fixes to window focus have not held. The cell records
   what has the foreground at each abort: the foreground window's title and process, and whether the session is
   locked, disconnected or console. The fallback logs that at the moment of failure, through the existing escalation
   line only, with no new standing process. The fix is cut from that record. Spending no Bloomberg attempts stays a
   hard constraint.
3. **No hold applies** (Andrew 2026-10-14: "There should be no hold"). What still binds, in his words: do not
   accidentally overwrite Positioning pipeline or ETFS view operations.
4. **The immediate unblock is a human sign-in, which only Andrew can do.** It goes on the site Z open-calls list as an
   act. Confirm it with `dapi_check.py` (a real data request), never `bloomberg_health`.
