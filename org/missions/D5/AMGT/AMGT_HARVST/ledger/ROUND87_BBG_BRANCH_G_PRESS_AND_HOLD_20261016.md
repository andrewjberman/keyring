# Round 87: `bbg` leaves the dell1 runner by Branch G (bot_check, press-and-hold) (`2.0.0_SA_COO~W1`, 2026-10-16 ~08:4xZ)

**Read by me from the files, not from SC1's message:** `cycles/bbg/20261016T081114Z.cycle.json` (asked 242, new 0, failed 2, stopped interrupted), run records `20261016T081953Z-run-44138fa3.json` and `20261016T083553Z-run-6f00a52f.json`, `round87/cb15_stopped3.out`, `round87/cb15_t0_3.txt` (`T0=2026-10-16T08:40:17Z`), the scheduled task's arguments (`--publishers sa wsj barrons --refresh-once`, `WorkingDirectory` `C:\dev\wk-harvest-runner-pin-ddd7dcdc38`).

## What happened

- Under the CTO's order `bbg,sa,wsj,barrons` (addendum 4 amendment 2) the `bbg` leg ran first from T0_2 `08:11:13Z`. 35 jobs ended `no_new_articles` at 0 S3 reads.
- Two jobs (`security-d7660d8c73fc8217` at 08:20:51Z, `security-7f993eb1cab6b5ea` at 08:36:41Z) each reached the SAME article, `/opinion/articles/2026-10-15/bp-can-solve-its-debt-problem-once-and-for-all`. Each: listing request 200, article request `403` class `bot_check`, signature `bloomberg_press_and_hold`, then `TargetClosedError: Locator.count: Target page, context or browser has been closed`. Both `token_source secrets:bloomberg/session`, `signed_in false`, the stored session dated 2026-09-11.
- SC1 applied Branch G (CTO C-j): stop file 08:36:58Z (no kill), `bbg` out, `sa,wsj,barrons` re-registered from the same pin, no seed, T0_3 `08:40:17Z`. No `bbg` object uploaded; the `upload-harvest` lines read 0 GETs, 0 bytes.

## Readings and limits

- **Branch G reading:** the order says "two consecutive `bbg` legs". These are two consecutive JOBS (one cycle, 15 minutes apart) on the same article, which a retry meets again by construction, not two cycles. SC1 took the conservative reading; the effect is the smaller list, inside the signed bounds. Not disputed.
- **Not established:** whether the challenge is the vendor's (an automation or IP signal on a new box) or ours (the minimised window from `HVST-cb-5`, whose protocol call may close the page under a challenge); whether it needs a human's hand once. The same stored session collected 3,011 `article` rows before the move.
- **Consequence:** `bbg` collects nowhere now (site Z's runner is Disabled). Site Z's pin worktrees stay locked until all four publishers report productive, so they stay locked. `sa` has not yet uploaded, so the C-a4' read (CTO) is still open and now counts from T0_3 for `sa` alone.

## Carry

- A named round-88 cell: the `bbg` challenge under the dell1 tab transport (measure which side closes the page; a handler that skips an article and does not end the job). Goes into the L10 slug. No open call at Andrew now: his hand is needed only if that cell proves the challenge wants one.
- SC1's row `D1-S31` is dispositioned by `D1-S32`.

-- 2.0.0_SA_COO~W1
