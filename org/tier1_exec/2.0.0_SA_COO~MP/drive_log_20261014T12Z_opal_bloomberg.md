# Drive log -- 2.0.0_SA_COO~MP (sitez) -- 2026-10-14 04Z-12Z -- NFRA_MCPORTAL (state at the model-policy relaunch)

## State, for the relaunched session

| item | state |
|---|---|
| Live gateway | `43088464f5` (another project's release on top of MP-n-4's `b0c75d24f1`). NFRA_OPLGTW r30 is IN FLIGHT: ledger `nfra-oplgtw-gateway-release-r30`, opened 11:20Z by `0.7.0_AE_CloudOps~Z` |
| PC round 1 | MP-pc-1 to MP-pc-4 COMPLETE and drained (@94e904d9c1, @3d9226072f, @5db04160eb, @868fe133db). MP-pc-5 (release, `0.7.0_AE_CloudOps~MQ`) and MP-pc-6 (close run, slot ~24) STAGED |
| G-REL5 | waits on the gateway queue: r30, then the tier-admission fix, then OG-mg-1. The payload was pre-checked at 04:3xZ to apply clean on live 43088464f5 (re-read at the act) |
| MP-pc-5 GO, when the queue frees | worker commits 90ad6bfa00, 12d990e43d (pc-1); 33d0604810 (pc-2); mcportal `17dcbb2` (on origin DEV, pushed by 0.0.0_AB_MSTR~Z) |
| MP-pc-6 spawn | NEW model policy: worker/worker-light spawn with model "haiku", effort "high" (1.0.0_SA_CTO~Z msg 34034) |
| F2 (FWD-21 writes) | waits on NFRA_OPLGTW OG-cp-1 (C-PERSON reader). The record shape is aligned with ~O's draft @91264782ab (status, revision, tools/channels allow/deny, stopped) |
| GW round 1 | MP-z-6 (FWD-20 close run) staged on Andrew's sitting, call 21d9 |
| MP-c-2 (FWD-1) | staged on Andrew's sitting with Alyssa, call def4 (raised by 1.0.0_SA_CTO~Z; it supersedes my 3b41; close 3b41 once a ruling record exists to cite) |
| Calls at Andrew | 21d9, def4 (and 21c5, 8ed7, f0d2, covered by 21d9) -- all `act` rows |
| Loops | /canonical-drive NFRA_MCPORTAL cron at :23 (session-only, re-arm after relaunch per LIVE_ARMS @81ef5aa2db); inbox watcher |
| Worktrees | drained and left in place: C:/tmp/mp-pc-21, mp-pc-23 (gitlink drift blocks a plain remove), C:/tmp/mp-pc-20 (orphan from a killed provisioning), mp-pc-20b, mp-pc-22. ~MQ holds rollback trees mp-z5-rb, mp-n4-rb until the rounds close |

## Acts this window

- 04:3xZ: WHILE-BLOCKED pre-check that MP-pc-5's payload applies clean on live 43088464f5.
- 11:3xZ: answered 0.0.0_AB_MSTR~Z's GC ask (msg 34012): rel-nfra-mcportal-c17 was superseded, never deployed. Tagged and removed with mp-n1-rb and mp-n1-rb2 (msg 34014).
- 12:1xZ: /open-calls NFRA_MCPORTAL for Andrew. No fork; five act rows.
- Hourly ticks 04Z-11Z: WAIT records (unblock.py) on the gateway queue, empty count 0 throughout.
