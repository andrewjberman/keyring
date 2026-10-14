# /self-drive dell1 box open calls -- tick 10 (`1.0.0_SA_CTO~DELL1`, 2026-10-14 ~04:58Z)

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261013_203xZ_SELF_DRIVE_DELL1_BOX_OPEN_CALLS.md` @bcd3be8ec3.
**Ticks covered:** 10. The 04:43Z fire ran late, at ~04:58Z, because the seat was mid-turn. **state: ARMED**

## Measured

- **Box list:** `open-calls.py list`: rows=69, **open=0** (boxes=1 read=1, absent none).
- **Inbox:** 0 unread. msgs 5410, 5412, 5418, 5423 and 5425 were acted on and acked.

## Rulings since tick 9 (all in-lane, none listed for Andrew)

| call | asked by | ruling | record |
|---|---|---|---|
| 14 daily-tier names fail the Yahoo identity lock: a looser rule? | `2.0.0_SA_COO~Q1` msg 5410 | **No looser rule.** The names leave Yahoo and are priced by Bloomberg, surface B, depth c, on the V2 windows. BRKB is a symbol-form fix | msg 5411 |
| Draw the 14-name quote (7,685 cells, finish 10-18)? Hold the first wired Yahoo night? | `~Q1` msg 5418 | **Quote APPROVED** (queue only, non-trading days, behind B1). **Tonight runs**, not held | msg to `~Q1` 04:32Z |
| FWD-41 five-name read NOT MET (C-S143: 4 of 5 names carry unsupported claims) | `3.0.0_SA_CVO` msg 5423 | **NOT REALIZED.** The AI-fill blocks come off PROD under a never-widen pair; the fc-4 proof is re-seated; round 106 is the grounding pass; the ceiling is 150 USD | `AMGT_RESAPP/ledger/CTO_RULING_FWD41_FIVE_NAME_READ_NOT_MET_20261014.md` @906952cec1 |
| Round 105 slug (`~R1`, bl-1..bl-3) | `3.0.0_SA_CVO` msg 5425 | **FWD-40 REALIZED.** Round 106 for `~R1` takes W418-S2, W418-S3 and W419-S3. The hold condition: a held block renders its prior reason | `AMGT_RESAPP/ledger/ROUND_ANALYSIS.round105.md` @e8960ac7dd |

## Owed by this seat (each waits on a carrier, not on a decision)

- The `~R2` hold pair: sign on receipt.
- The round-105 AIFILL analysis: when the slug lands after fc-4 is re-seated.
- Analyses on the FIRMBKTS r7, CANON r6, BDPRCE r3, DEMQUE r9, HARVST r85, RIVALS r29 and SECCLASS r24 slugs.

## Completion test

Box-scope loop: there is no register DONE. The loop runs until Andrew's stand-down. **NOT DONE.**

## ACTS ONLY ANDREW CAN DO (cited)

- **Sign-in at the dell1 console after the NFRA_CTLPLN restarts**, Wed 2026-10-14 ~14:45Z and ~15:15Z (10:45 and 11:15 ET): his login (`/self-drive` Step 1, "his login or MFA code").
- **One session from his own work Claude through the gateway** for NFRA_OPLGTW FWD-21: his identity and login.

## Compiler Tools

`open-calls.py list`, inbox read, `safe-commit.sh`, `git ls-remote`.

-- 1.0.0_SA_CTO~DELL1
