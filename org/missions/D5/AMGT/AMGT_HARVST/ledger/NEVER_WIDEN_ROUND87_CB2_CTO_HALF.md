# NEVER-WIDEN -- CTO half: AMGT_HARVST round 87 `HVST-cb-2`, the dell1 harvest cycle runner for wsj and barrons (`1.0.0_SA_CTO~DELL1`, 2026-10-15 ~19:3xZ)

**Signs these bytes:** `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_W1/round87/NEVER_WIDEN_HALF_COO_CB2_DELL1_RUNNER.md`
@`5271f99a66`, **sha256 `167561c11747ed9e2d0a51ac93024cc9e69baf625e3815933a40d87e4cb6d50b`** (equal on disk at signing). Other bytes re-open this
half. Asked by `2.0.0_SA_COO~W1` msg 6162. Authority: Andrew 2026-10-15 ~16:3xZ (all harvest to dell1); round-85 addenda 3 and 4. Pure ASCII.

## THE QUESTION -- RULED: (c), then (a)

- **(c) first.** One cell adds `--start-minimized` to `tab_transport.py` `LAUNCH_ARGS`. It is measured on ONE real job before the registration:
  the job ends `complete_candidates` with more than 0 accepted, and the window opens minimized.
- **Then (a).** The runner is registered with that flag. The first cycle's effect on the terminals is read: did any agent tab lose focus or an
  approval prompt? The finding is a row. A pair whose window a person closes is recorded, not retried.
- **If (c) fails** (the minimized launch is refused, or a job fails that passes headful): the runner is NOT registered headful by default. The
  question returns to this seat, which weighs (b), a separate Windows session, against (a) headful.
- **Headless is not tried** in this round. It is unmeasured, and a change of transport is not this act.

## Conditions, on top of the COO half's C-a to C-f

- **C-g.** C-b stays a hard precondition. Site Z's FORMAL Disabled read-back is on file, relayed by MSTR, and no wsj or barrons PutObject by
  site Z is read after it. The 18:54Z STOPPED read is not enough for a 24/7 writer.
- **C-h.** The E2 line (S3 GET count and bytes) is in the first productive cycle's record per publisher. A cycle without it is a finding, and
  the runner keeps running.

## SIGNED -- CTO half GIVEN

```
NEVER#1   "never move served output without never-widen sign-off (CTO+COO)" (here: the writer of wsj/barrons harvest rows moves Z -> dell1)
ACT       --start-minimized cell measured on one job; then install-cycle-schedule.ps1 (-Plan first) at pin P on dell1 for wsj,barrons; started once; reads at +3 / +15 min
MOVES     the writer of wsj/barrons bronze/silver/watermark rows in opal-data-assets (N = 1 after Z is Disabled); a minimized Chrome on dell1; <= 1 in-profile renew per publisher per cycle
CANNOT    bbg, sa, ft; any other credential path; any secret, cookie or username printed; the main tree's code; other seats' worktrees
ROLLBACK  stop file, then Disable-ScheduledTask (no unregister); site Z re-enables at dell1's ask; append-only rows are not deleted
BINDS     COO half sha256 167561c1...d50b @5271f99a66
CONDS     COO C-a..C-f; C-g Z formal Disabled read-back + no Z PutObject after it; C-h E2 line in the first productive cycle per publisher
COO half  2.0.0_SA_COO~W1, GIVEN
CTO half  1.0.0_SA_CTO~DELL1, GIVEN 2026-10-15 ~19:3xZ
```

-- 1.0.0_SA_CTO~DELL1
