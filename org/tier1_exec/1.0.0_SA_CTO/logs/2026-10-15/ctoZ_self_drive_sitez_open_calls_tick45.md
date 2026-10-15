# /self-drive sitez open calls -- ticks 44-45 (17:52Z, 18:55Z 2026-10-15), `1.0.0_SA_CTO~Z`

Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261013_203xZ_SELF_DRIVE_60M_SITEZ_BOX_OPEN_CALLS.md`
@ce0ba39d90. Covers the span since tick 43 (@b0659b9974). **state: ARMED.**

## Measured

- `open-calls.py list`: rows 46, open 7, all person acts. Inbox: 0 unread.
- **Planned cells vs cut orders (NFRA_OPLGTW):** 0 gaps.
  - G2 `OG-cl-1..6` (cut @6fc29c2dbf; the adapter protocol amended A1 @9fa68ea4e6), `OG-gp-1` and `OG-gf-1`: 8 of 8
    pending, each with its worker worktree.
  - `OG-eg-3`, the site Z runner retirement: pending, reassigned from `~ZW` to `~Z` @167a5e9ecb.
- **Capacity:** `0.7.0_AE_CloudOps~ZW` is stopped at a weekly usage-limit dialog until Oct 18 (COO~O @167a5e9ecb; MSTR~Z
  msg 34523 declined a new seat). Told to Andrew at this terminal.

## Rulings and acts since tick 43

1. **G2 issuance read and accepted** (COO~O msg 34519, @6fc29c2dbf). Each of cl-1..6 states that client data never reads
   through `gateway-global-internal-reader-role`: 7 of 7 cl orders carry the line.
2. **NFRA_MCPINDEX MX-r-14, CTO never-widen half SIGNED @e5812ce7df** (COO~MI msg 34528).
   - Live base 06cfb6db64. Pins: catalog b97c59e6ac and discover 92ca8b57f7.
   - 24 own-firm rows: 23 for 49financial, 1 for inflection.
   - I re-ran f1.AC2: PASS, leaks 0.
   - The half is final on the ANNOUNCE.
3. **OPAL_BBGTML correction (COO~ZB msg 34518, row Z-S23 @eb80f77d65).** My ruling @701a4c705a stated "0 unattended
   successes since 08-18"; that figure came from the escalation file, which records failures only.
   - The sign-in ledger shows 19 unattended sign-ins from 08-23 to 10-04.
   - The break starts at the 10-06 Terminal self-update (build 3206.1.80.1).
   - The ruling stands: R7's trace is the next read, at the 2026-10-16 11:00Z pull.
4. **Andrew's question at this terminal: "the python cron script that runs the automated bbg pull".** Answered.
   - `OPAL_BBGTML_daily_pull` runs on the Anaconda `cma` env and Python311, never Python314, so the 14:02Z outage did not
     touch it.
   - The morning failure is the sign-in focus defect, which stays open.

## Moved without a call

- MCPORTAL MP-pe-2 complete @b006b05b90: the Gateway page groups tools by source.
- MCPINDEX MX-c-20 on A5 @d91a2df857.

## Acts only Andrew can do (each with its citation)

1. One MC Portal sitting, including one sign-in as Opal Bloomberg (21d9; covers 21c5, 8ed7, f0d2). Citation: his login and
   a human read.
2. One sitting with Alyssa (def4; 3b41 is a duplicate). Citation: his person act.
3. One Teams message from his account to Opal Bloomberg (a519). Citation: his own account.

## Completion test

NOT DONE: 7 open calls, every one a person act.
