# 1.0.0_SA_CTO~DELL1 -- self-drive dell1 box, tick 97 (covers tick 96a, about 01:49Z to 02:18Z on 10-18)
**archetype:** COORDINATE

Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261016_024xZ_SELF_DRIVE_DELL1_BOX_30M.md` @fa59eb8dec. state: ARMED.

## Rulings and acts (hashes LOCAL on box/dell1)

- **MDPF_SECCLASS round 28 (CVO 7828).** MAY-CLOSE over 22 orders.
  - S48 is DISARMED and REMEDIATED: the served 10-02 delta (+407,720) equals the input checker (+407,720.32).
  - S45 is REMEDIATED.
  - Nothing widened: the 00:24Z version moved only 10-08 to 10-15.
  - S42 stays armed until E_18's own fire line is read. W100-S3 (LCFYX) and S52 (the April table) graduated.
  - The 00:24Z version has no 10-16 row, and the cause is not read.
  - Analysis @09bb31491e. The round-29 list of 6 went to M1: reads first (E_18's fire line, the 10-16 gap against the trading-calendar
    frontier), then LCFYX, S52, the repoint followed by FWD-12, D_03 and C_06 if not landed, and the S48 14-date reconcile. One served
    change per fire.

## Completion test

NOT DONE. This is the standing box drive, which ends on Andrew's word.

## Acts only Andrew can do (each with its citation)

1. ADVI_COTBOOKS: confirm the 6 DONE WHEN lines (row 0cf5). Canonical loop L2.
2. SOC2_MSLOGS round 2: run the 8-day re-derive with his MFA session (row 89c9). The access group holds Andrew_Berman alone (TO-R2-r2 :29).
3. SOC2_MSLOGS FWD-1: his read of the enriched block, through the same MFA door.
4. EWS delivery channel. Nothing sends until he names one.
5. FWD-10's portal source line to PROD, a client-facing push (CLAUDE.md PUSHES).
6. Restart dell2's box manager session at the dell2 machine (row e1ee). No remote spawn path exists from dell1.

## Compiler Tools

| tool | result | note |
|---|---|---|
| open-calls.py list | PASS | 3 open, all Andrew items |

What worked: putting the read before the writes in round 29. Gap: none new.

-- 1.0.0_SA_CTO~DELL1
