# self-drive cluster_open_calls -- tick 38 (2026-10-13 22:5xZ)

state: ARMED   cadence: 60m   cron: 6ca5a587   ticks covered: 38

## Measurements this tick

- cluster list (read 22:55Z): boxes=4 read=4 absent=none; open=20 (fork 2, act 13, approval 5), closed=137.
- dell1 0 open: eb2a closed on XA-17f5.
- dell2 adds FIVE client-facing approval rows (the DEVPLN route is live on dell2):
  - `8500` `cand/dell2/anlreq-90-held-submit`, `7b45` `anlreq-88-advisory-fee` and `fde0` `anlreq-87-model-order`: the three
    re-registered ANLREQ merges, under the four-commit waiver;
  - `cffa` and `3635` `cand/dell2/irpt-ytd-from-first-day-and-wider-export-modal`, the SAME branch registered twice. This is the
    IRPT_DASHBD smoke fixes from Andrew's ~18:1xZ smoke, and it is FWD-1's first organic client-facing case.
- site Z: new act `232a` (name one asset manager to run the FWD-21 harvest test call from their own Claude).
- The laptop list carries the new HELD fork `3d7e` (the CLAUDE.md DEV-route law edit).

## Calls this tick

- No fork for this seat to rule. `87a2` and `3d7e` are HELD for Andrew.
- The five dell2 approvals are client-facing, so each is ANDREW's to approve (C-CLASS; a CTO close reads `valid=no`). They are
  listed for him, never ruled here.
- The duplicate `cffa`/`3635` is relayed to dell2 to close one.

## Acts and approvals only Andrew can give

- **site Z 763e + 6c9f: the Bloomberg sign-in before 07:00 ET 10-14, and the R2/R3 hold yes/no by 10:30Z.**
- dell2 approvals: 8500, 7b45, fde0, cffa (=3635).
- dell2 f61b (the PROD execution id), e260.
- site Z 21d9, 232a, 2da6, 21c5, f0d2, 8ed7, a519.
- laptop 44eb, e435.
