# /self-drive AMGT_FRIDAY -- tick 37 (1.0.0_SA_CTO~Z, 2026-10-06 ~11:2xZ -> ~12:2xZ)

**archetype:** COORDINATE

state: ARMED. Cadence 60m, cron `29c8b141`. Arming record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261004_194xZ_SELF_DRIVE_60M_AMGT_FRIDAY_RESTART_AFTER_SENTINELONE_CRASH.md`
@2b18064b99. Previous log: tick 36 @468405caea.

## Inbox measurement

Since 11:20Z, all READ: 30001, 30004, 30005 and 30009 (4 of 4). 0 unread.

## Acts and movement (since tick 36)

| item | state | commit |
|---|---|---|
| **The 10-06 vehicle** (MSTR~Z msg 30001) | The sign-in fallback launched `wintrv` at 11:00:28Z. The fill failed verification and aborted before submit: **0 login attempts**. The DAPI precondition FAILED and the pull was not attempted. The rivalfunds leg exited 93. One cause | -- |
| **My correction** (MSTR~Z msg 30005) | I had told COO~RV to leave RIV-e-1 retrying because "it proceeds on sign-in". False: `ExecutionTimeLimit PT30M` killed the vehicle at 11:30:01Z, so names and D12 never ran. Recovery is MSTR~Z's re-run after the sign-in | b555e81836 |
| ETFS_RIVALS round-12 cell | `enrichment_bloomberg` bounds its retries with a distinct exit. COO~RV measured (msg 30009) that it saves no Bloomberg stage on a Terminal-down day; its value is a clean exit (RC 95) and log pruning | b555e81836 |
| Row OPAL_BBGTML-Z-S1 (MSTR~Z msg 30004) | Plaintext username in 15 of 31 vehicle logs (`bbg_verify.ps1:192-193`); the value is not reproduced. The fix is Andrew's (no-modify zone) | a0089a9bf3 |
| ETFS_RIVALS 10-06 page | Published 11:05Z: holding_contribution OK, refused 0, the replay's `-v02` inputs served. No G4 was written (the 10-02 restore is still newest) | (COO~RV) |
| RESAPP ay-5 | Deployed `D29LJCXh`. AE~A stopped on a c59 environment-crossing check (row Z-S359), ruled (a) by COO~Z @bf909b6665. The round-75 walk is running | (COO~Z / AE~A) |

Verdict ledger: 1 row. **No open calls in scope (tick 37).**

## Scope state (register read 12:19Z, denominator 5)

All 5 projects are active/EXECUTING. Open TOs: D5 187, D13 2. Sequence: 5 UNPLACED, no flags. Open deploys in scope: 1
(`amgt-resapp-r75-ay5`).

**Completion test: NOT DONE.** 0 of 5 complete.
- **REACHABLE 4:** CORPUS, RESAPP, DSGN, RIVALS.
- **UNREACHABLE 1:** HARVST, pending Andrew's hand-solve and the SA account.

## Acts only Andrew can do (each cited)

1. **The Bloomberg Terminal sign-in.** `wintrv` sits at its login with 0 listeners on 8194. Lockout budget; never attempted without him.
   The CORPUS 13:00Z fire and today's vehicle re-run wait on it.
2. **OPAL_BBGTML-Z-S1:** the plaintext username in the vehicle logs. `integrations/bloomberg/` is under his no-modify order.
3. **The portal DEV push of DSGN rounds 43+44** (`1d6d2573`).
4. **HARVST:** hand-solve the challenges; the SA account (HTTP 402).
5. **DSGN FWD-1:** his PROD walk.
6. **Vendor uses:** Z-W240-S1, Z-W227-S1, RESAPP FWD-2, SEC egress.
7. **Spend:** provisioned concurrency, only if needed after round 75.
8. **Others:**
   - FWD-14's list owners;
   - the walker accounts;
   - Z-S230;
   - FT;
   - the recursive deletion of `C:/tmp/ctoz-lint-warn`.

## Compiler Tools

`get_delivery_state`, `directives-check.py --json`, `sequence-check.py`, `Get-Process wintrv`, `Get-NetTCPConnection`, `git log`.
