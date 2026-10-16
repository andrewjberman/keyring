# CTO ruling -- OPAL_BBGTML: fix the 07:00 sign-in tonight (R8), do not only wait for the trace, 2026-10-15 ~20:0xZ

By: `1.0.0_SA_CTO~Z`. On Andrew-direct, Teams 2026-10-15T18:00:40Z, relayed verbatim by `0.0.3_BG_BBGTerminal` (msg 34555):
**"send this log to CTO and have them fix it."** Log:
`org/tier0_utility/0.0.3_BG_BBGTerminal/logs/2026-10-15/investigation_cron_signin_failure_two_signatures_one_binary_update.md`.

## What the log establishes

- It is not Python. The cron pins the `cma` interpreter, and `bbg_credentials.py` imports only the standard library.
- There are two signatures, in sequence, after `wintrv.exe` was replaced on 10-06 at 04:04Z.
  - **A, glyph calibration** (10-06, 10-08): fixed. But the fixture was never re-derived against the new build.
  - **B, focus at submit** (10-11, 10-13, 10-15): still live. The fill verifies (9/9, OCR 100%), then 3 fixed foreground
    re-asserts fail and the script aborts at zero Bloomberg attempts.
- The contention is TRANSIENT. At 14:3xZ the foreground was the login window itself. The prime suspect is the updated
  `wintrv.exe` spawning a second window during the fill-to-submit gap.
- R7's foreground trace landed at 14:30Z, so tomorrow's fire names the window that takes focus.

## Ruling

A fix that waits for the window to be named is a wait. Andrew asked for a fix. **COO~ZB cuts R8 now, and it lands
tonight, before the 2026-10-16 07:00 ET fire.** Executor: `0.7.0_AE_CloudOps~ZS`, the owner of R3 and R7.

1. **Settle until the foreground is stable, then submit.**
   - Replace the fixed 3-try re-assert with a bounded loop:
     - poll the foreground every 250 ms for up to 90 s;
     - re-assert the login window when it is lost;
     - submit only once the login window (`BLOOMBERG: Login`, the `bplus64` process) has held the foreground for 2 s in a
       row.
   - If it never settles, abort exactly as today: at ZERO attempts, with R7's trace line.
   - This works whichever window takes focus transiently, because it waits the transient out.
2. **Re-derive signature A's glyph fixture against the current build**, in place of a widened tolerance band, so that a real
   mis-fill still fails verification.
3. **Unchanged:** the zero-attempt guard, the sign-in ledger and budget, the 07:30 backstop, and R7's trace.
4. **Proof:**
   - **Tonight:** the loop's logic is exercised offline with `-ForceDown -DrySubmit` and a planted focus thief. Both arms
     are shown: the thief releases within 90 s, so it settles and submits; the thief holds, so it aborts at 0 attempts.
     Nothing touches the live Terminal while it is signed in and serving.
   - **The real proof** is the 2026-10-16 07:00 ET fire: a clean unattended sign-in, or an abort with the trace naming
     the window, cut from on the same morning.
5. **Change management:** on this box an edit is a deploy, because the task runs the working tree. So R8 carries a NEVER-2
   ledger entry and lands after market close. It must not touch Positioning pipeline or ETFS view operations (Andrew
   2026-10-14).

## Addendum 2026-10-16 ~02:3xZ -- item 2 (re-derived glyph fixture) DEFERRED past the 11:00Z fire

Asked by `0.0.3_BG_BBGTerminal` (msg 34648). Measured on box/sitez @0faeb93352: item 1 landed in `bbg_signin.ps1`, but item 2 did not;
`bbg_verify.ps1` is unchanged since @0387041915.

- **Ruling: item 2 does NOT land before the 2026-10-16 11:00Z (07:00 ET) fire.** Signature A passes on the current band, so nothing
  blocks the fire. Leaving `bbg_verify.ps1` unchanged also means the fire grades ONE change, the settle loop, against signature B.
- **Widening the band is REFUSED.** Moving `$uLo` to len-2 would re-admit the 08-20 battery's border-artifact mutant, which measures
  10. Only a re-derived fixture closes item 2.
- **Parked:** item 2 is the next R-cell, cut by `2.0.0_SA_COO~ZB` after the 11:00Z fire is graded. That seat is not seated; its
  re-seat is MSTR~Z's to raise with Andrew.

## Addendum 2026-10-16 ~11:0xZ -- item 4's "tonight" offline proof was not executable; the harness becomes the next R-cell

Found by `0.0.3_BG_BBGTerminal` (msg 34930; findings
`org/tier0_utility/0.0.3_BG_BBGTerminal/deliverables/R8_OFFLINE_PROOF_NOT_EXECUTABLE_WHILE_SIGNED_IN_20261016.md`), corroborating
CloudOps~ZS's 10-14 note. Item 4's offline proof cannot run as written:
- `-ForceDown -DrySubmit` does not synthesize a Login window, so the fill gate (`bbg_fallback.ps1:108/:114`) exits 2 before
  submit, and it writes a false escalation line on the way.
- No planted-thief harness exists in either script.
- This seat ruled a proof whose premise it had not read.

- **2026-10-16 (DAPI up before the 11:00Z fire):** the fire is the organic negative arm (no GUI phase). The R7 `-TraceTest` run is
  recorded as the day's deliberate act; it proves the trace, not the loop.
- **The settle loop's live grade** moves to the next DAPI-down morning.
- **Next R-cell, for `2.0.0_SA_COO~ZB`** (with the parked item 2 glyph fixture): a harness that drives the settle-loop function
  against a mocked foreground source, with no Terminal and no Login window. Both arms: the thief releases inside 90 s and it
  submits; the thief holds and it aborts at 0 attempts. That makes the loop provable on demand.
