# /self-drive AMGT_FRIDAY -- tick 33 (1.0.0_SA_CTO~Z, 2026-10-06 ~07:2xZ -> ~08:2xZ)

**archetype:** COORDINATE

state: ARMED. Cadence 60m, cron `29c8b141`. Arming record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261004_194xZ_SELF_DRIVE_60M_AMGT_FRIDAY_RESTART_AFTER_SENTINELONE_CRASH.md`
@2b18064b99. Previous log: tick 32 @6f6e335c5d.

## Inbox measurement

Since 07:20Z, all READ: 29949, 29954, 29962 and 29963 (4 of 4). 0 unread.

## Acts (since tick 32)

| item | act | commit |
|---|---|---|
| **The Bloomberg Terminal is DOWN** (MSTR~Z msg 29954) | P0 fails at layer 1: no 8194 listener, `wintrv` absent, runbook steps 1-4 eliminated, and no sign-in attempted. The box slept 03:09-07:36Z after a power-plan switch to a duplicated plan with 600 s AC timeouts; MSTR~Z set all 3 plans to never. **PushNotification to Andrew** (terminal; mobile push inactive). **How today's fires read without a sign-in:** COO~X takes no Branch C on a Terminal failure; COO~RV relies on eg-1 refusing an all-error G4; CVO~RV grades one cause at 13:30Z | (msgs 29956-29958) |
| RESAPP ax-5 (COO~Z msg 29949) | AE~A stopped on a fifth changed file, condition 1 working. **Concurred** CHANGED 5 + ADDED 3 after a caller read. COO~Z's AMENDMENT 2 (route-count guard; graded on an UNTARGETED plan) is consistent with the half | 8ded0241cd |
| HARVST gold rebuild #7 (COO~H msg 29963) | CTO half SIGNED: (e) url-fill only, 1,746 ft/wsj rows, no host contacted | 0666944946 |

Verdict ledger: 3 rows. **No open calls in scope (tick 33).**

## Scope state (register read 08:18Z, denominator 5)

All 5 projects are active/EXECUTING. Open TOs: D5 181, D13 2. Sequence: 5 UNPLACED, no flags. **Open deploys in scope: 2**
(`amgt-resapp-r74-ax5`, `amgt-harvst-r49-av2-gold-rebuild7-ftwsj-url-20261006`). At 08:18Z `wintrv` is still absent, so the
Terminal is not yet signed in.

**Completion test: NOT DONE.** 0 of 5 complete; all 5 REACHABLE.

## Acts only Andrew can do (each cited)

1. **The Bloomberg Terminal sign-in, before 11:00Z** (07:00 ET). The ETFS_RIVALS vehicle and the CORPUS 13:00Z fire need it. Lockout
   budget: never attempted without him (CLAUDE.md, Bloomberg READ_HERE).
2. **The portal DEV push of DSGN rounds 43+44** (`1d6d2573`, approved @0c9b9db840).
3. **HARVST:**
   - Hand-solve the challenges (collection-run condition 3).
   - The Seeking Alpha account (HTTP 402).
4. **DSGN FWD-1:** his PROD walk.
5. **Vendor uses:** Z-W240-S1, Z-W227-S1, RESAPP FWD-2, SEC egress.
6. **Spend:** provisioned concurrency, only if needed after ax-5.
7. **Others:**
   - FWD-14's list owners;
   - the walker accounts;
   - Z-S230;
   - FT;
   - the recursive deletion of `C:/tmp/ctoz-lint-warn`.

## Compiler Tools

`get_delivery_state`, `directives-check.py --json`, `sequence-check.py`, `git grep` (callers at `da3c89dc54`), `Get-Process wintrv`,
PushNotification.
