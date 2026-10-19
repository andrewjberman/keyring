# 1.0.0_SA_CTO~Z -- /self-drive 30m sitez open calls, ticks 164-165 (2026-10-19 08:58Z to 09:57Z)

**archetype:** COORDINATE

Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261016_024xZ_SELF_DRIVE_30M_SITEZ_BOX_OPEN_CALLS.md` @b155c4c03a.
Session cron e6b088c9. **state: ARMED**

## Bloomberg Terminal: signed in on attempt 1 of 2

- **09:0xZ (msg 35924): HELD at verify, 0 attempts spent.** Two stale dialogs, about 9 hours old, covered the login fields:
  - a "FREEZE TRIPWIRE" citing a 19:58 scan;
  - a PowerShell "guard page" error from the commit exhaustion.
- **RULED:**
  - keep the screenshot and the dialog text;
  - close with close, cancel or OK only, never the tripwire's action button, no bugcheck;
  - re-fill, verify, attempt 1, with the bounds unchanged.
- **09:19:42Z (msg 35926): SIGNED IN on attempt 1. Attempt 2 is unspent.**
  - `bloomberg_health` ok:true, plus real data on both channels: reference AAPL PX_LAST 343.46 and 3 history rows.
  - **The 11:00Z constituents capture is protected.**
  - Eight tripwire dialogs, not one, were closed by WM_CLOSE, none by its action. 0 have returned.
  - `bplus64` is 26 processes, 3,108 MB in total, the largest 311 MB. That is a healthy fresh Terminal: per-process size is the
    discriminator, against last night's 10 processes at about 3.7 GB each.
- Andrew was push-notified that no sign-in is needed.

## Correction: round-45 amendment A2 @cc6b4f8f3f

- A1 was wrong on G-C and G-E. I acted on `WALKTHROUGH_PROTOCOL.md` section 1 without checking the later rulings.
  - **G-C was RETIRED** by 1.0.0_SA_CTO~O ruling 28152, on Andrew-direct 2026-09-30 (OG-g-1 status).
  - **The pilot identity is already verified** (OG-g-2 complete, `IDENTITY_PILOT.json`).
- A1 item 4 is withdrawn. Items 1-3 stand. Sent to 2.0.0_SA_COO~O, together with the protocol edit to drop G-C.
- **Open-calls:**
  - the corrected act `sitez-20261019T093315Z-2ac2` (the walkthrough sitting only) was added;
  - `a485` is SUPERSEDED by `2ac2`, but cannot be closed alone: the tool refuses a CROSS-BOX act close, and `--decision withdrawn`
    applies to approval rows only. It stays open, marked superseded here and in A2.
- **Lesson:** read the status tag of the order behind a protocol's precondition before relaying the precondition as an act.

## Box state

- Commit free 26,546 MB (09:57Z), a slow drift after the Terminal's relaunch; 8 claude.exe alive.

## Open calls

- 0 forks.
- 6 open `act` rows, which only Andrew can do:
  - f0d2: sign in once as Opal Bloomberg in the MP-v-2 Edge;
  - 8ed7: one /control-plane and /open-calls run;
  - def4: the Alyssa sitting, postponed by Andrew;
  - 5b35: the asset manager's harvest call (FWD-21);
  - 2ac2: the Schwab pilot walkthrough (FWD-1 to 8);
  - a485: superseded by 2ac2.

## Compiler Tools

| tool | used for | result |
|---|---|---|
| grep (OG-g-1, OG-g-2 status tags) | G-C and G-E state | G-C retired 09-30; pilot identity verified |
| open-calls.py close / add | act rows | 2ac2 added; a485 close refused (cross-box act) |
