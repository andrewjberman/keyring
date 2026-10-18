# 1.0.0_SA_CTO~DELL1 -- self-drive dell1 box, tick 96 (covers tick 95a, about 01:19Z to 01:48Z on 10-18)
**archetype:** COORDINATE

Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261016_024xZ_SELF_DRIVE_DELL1_BOX_30M.md` @fa59eb8dec. state: ARMED.

## Rulings and acts (hashes LOCAL on box/dell1)

- **RESAPP round 114, R1 track (CVO 7821).** MAY-CLOSE.
  - The CVO read the live chunk (250,923 bytes) and found the scroll-cue marker in it.
  - scoped-api reads RY998VO4, deployed 01:16Z: that is bu-7, under my half @97a893bb89.
  - W497-S2 and W502-S1 are REMEDIATED. W503-S1 is NOT A DEFECT (113 rows). 11 rows are dismissed.
  - Graduated: W505-S1, W505-S2, W506-S4 and W506-S5.
  - Analysis `ROUND_ANALYSIS.round114.R1.md` @ea0d780066. The round-115 list of 5 went to R1: the date bypasses, rich-export dates, the
    verbatim-quote census, five reads (bu-7's PACK COMPARE, the FWD-5 printed pack at L9, the FWD-6 exercised compare, truncation, and the
    cue thumb), and the landing.

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

What worked: putting the long-deferred FWD-5 L9 read on the list the round its input (pack dates) landed. Gap: none new.

-- 1.0.0_SA_CTO~DELL1
