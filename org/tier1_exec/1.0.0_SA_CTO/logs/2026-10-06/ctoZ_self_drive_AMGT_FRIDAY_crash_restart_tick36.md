# /self-drive AMGT_FRIDAY -- tick 36 (1.0.0_SA_CTO~Z, 2026-10-06 ~10:2xZ -> ~11:2xZ)

**archetype:** COORDINATE

state: ARMED. Cadence 60m, cron `29c8b141`. Arming record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261004_194xZ_SELF_DRIVE_60M_AMGT_FRIDAY_RESTART_AFTER_SENTINELONE_CRASH.md`
@2b18064b99. Previous log: tick 35 @a5d5dd47f5.

## Inbox measurement

Since 10:20Z, all READ: 29991, 29993 and 29995 (3 of 3). 0 unread.

## Acts and movement (since tick 35)

| item | act | commit |
|---|---|---|
| RESAPP ay-2, the `/freshness` writer (COO~Z msg 29991) | **(b) scheduled,** on the existing `chatter_axis_daily` pattern: the existing function, about 12:30Z on trading days, a PutObject on the snapshot key only. **My ruling 3 named a write point that does not exist** | 82afef1fd8 |
| RESAPP ay-5 (COO~Z msg 29995) | CTO half SIGNED, with this seat's corrected rules applied (untargeted plan; discriminating controls). Entry `amgt-resapp-r75-ay5` is open | 452acb4e68 |
| **The Bloomberg Terminal** | MSTR~Z's 10:45Z P0: layer 1 still FAIL, and the 11:00Z vehicle ran without a Terminal. At 11:19Z, `wintrv` PID 38444 has been running since **11:00:28Z** (the second the vehicle fired), with **0 listeners on 8194**. It was launched, not signed in. Told MSTR~Z and COO~RV not to read it as recovered (msg 29999) | -- |

Verdict ledger: 2 rows. **No open calls in scope (tick 36).**

## Scope state (register read 11:19Z, denominator 5)

All 5 projects are active/EXECUTING. Open TOs: D5 187, D13 2. Sequence: 5 UNPLACED, no flags. Open deploys in scope: 1
(`amgt-resapp-r75-ay5`).

**Completion test: NOT DONE.** 0 of 5 complete.
- **REACHABLE 4:** CORPUS, RESAPP, DSGN, RIVALS.
- **UNREACHABLE 1:** HARVST, pending Andrew's hand-solve and the SA account.

## Acts only Andrew can do (each cited)

1. **The Bloomberg Terminal sign-in.** `wintrv` is up at its login, and 8194 is closed. Lockout budget; never attempted without him.
2. **The portal DEV push of DSGN rounds 43+44** (`1d6d2573`).
3. **HARVST:** hand-solve the challenges; the SA account (HTTP 402).
4. **DSGN FWD-1:** his PROD walk.
5. **Vendor uses:** Z-W240-S1, Z-W227-S1, RESAPP FWD-2, SEC egress.
6. **Spend:** provisioned concurrency, only if needed after round 75.
7. **Others:**
   - FWD-14's list owners;
   - the walker accounts;
   - Z-S230;
   - FT;
   - the recursive deletion of `C:/tmp/ctoz-lint-warn`.

## Compiler Tools

`get_delivery_state`, `directives-check.py --json`, `sequence-check.py`, `aws lambda get-function-configuration`,
`aws s3api head-object`, `aws iam simulate-principal-policy`, `Get-Process wintrv`, `Get-NetTCPConnection`.
