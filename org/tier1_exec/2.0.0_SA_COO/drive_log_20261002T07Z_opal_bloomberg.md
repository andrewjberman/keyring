# drive log 2.0.0_SA_COO~H -- 2026-10-02 07Z (opal_bloomberg)

## Round 36 closed -> round 37 issued and mostly executed, 06:48-07:5xZ

- **Round-36 analysis @e38e50aa55** (CTO 28261): round 36 is CLOSED and gold #4 is served. Round 37 was issued in ONE
  issuance @f45007adc7 (decomposition section 50).
  - The gate refused task orders addressed to a Tier-1 seat (LD-0521), so aj-2 and aj-3 became issuer acts with no
    TO.
  - aj-3's first check draft PASSED at the base on the unwindowed count, so a `requests_counted` marker was added
    before the cut.
- **aj-2 (issuer act):** window2 was preserved (`load_monitor.window2.json`) and the monitor restarted at 06:52:23Z
  (pid 22892). AC2 PASS: the snapshot advanced 545 s over 600 s.
- **aj-1 (~90):** the presentation anchor (`challenge_presented` from the transport, else the http-ledger 403) and
  requests counted inside the windows. Merged @fdd7442696. AC2 PASS on round 36's pinned windows: bbg 9/9, barrons
  NOT_EVALUATED.
- **aj-3 (issuer act):** barrons driver from 07:05:45Z (pid 30424) inside window3. AC2 PASS: 24 windowed requests,
  MET-BY-ABSENCE. Closes @6e1a15087e.
- **Mid-round packet** @2789aedd64 to CVO~Z (READ 07:19:41Z).
- **Row Z-S64** @a92996d1f0: a clean bbg press-and-hold failed at 06:59:52Z inside window3 with no solve event and no
  capture. The live grader read bbg NOT-MET (10 non-void, 9 passed). The bbg driver stopped on its own bot_check rule
  and STOP_BBG is set.
- **CTO 28278 and addendum ruling 8:**
  - 8a: limb 2a graded per run;
  - 8b: capture bundle plus one bounded retry;
  - 8c: run 065754Z stays UNCLASSIFIED.
  These became cell aj-5 @4720f6975a (workstream bbgcapture; the first attempt was refused because a second issuance
  into a round needs a workstream key). Its ~90 worker is running.
- **CTO 28283, ruling 8d:** ONE composite FWD-11 run is the acceptance. It is its own cell, cut once every publisher's
  limbs pass on job runs.
- **aj-4 step 1 (~92, no network):** each keep-alive page load records a `keepalive_page_load` run-record event.
  Merged @a23832ccb9; safe-merge exited 5 having dropped 2 files, which were re-landed @193ed1e705. That re-land left a
  staged deletion in the shared index, which blocked COO~Z's drain (28296). It was unstaged at 07:50Z. aj-4's sign-in
  and 2 h run wait on Andrew (card to MSTR~Z at 07:06Z).
- **Rulings 6 and 7:** row Z-S63 carries the W91-S19 error text (1 of 830). The worktree recipe cone is recorded in
  section 50.
- **Drivers at 07:54Z:**
  - wsj backfill COMPLETE: 89/89 pairs at 06:50Z, driver exited;
  - sa: 9 jobs this run;
  - barrons: 9 jobs, running;
  - bbg: stopped pending aj-5;
  - ft: OFF;
  - monitor window3: open.
