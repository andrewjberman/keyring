# 1.0.0_SA_CTO~DELL1 -- self-drive dell1 box, tick 94 (covers tick 93a, about 00:19Z to 00:48Z on 10-18)
**archetype:** COORDINATE

Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261016_024xZ_SELF_DRIVE_DELL1_BOX_30M.md` @fa59eb8dec. state: ARMED.

## Rulings and acts (hashes LOCAL on box/dell1)

- **ETFS_RIVALS order 3, act 3: the TR-HELD publish (RV 7803).**
  - The act writes 256 add-only G4 `security_market` objects, with N = 4 writers. held-tr is the only non-backfill past-date writer.
  - Act 2's measured table (off git, sha256 74cd181a): 13 of 13 funds move in the rankings, and holding-implied days fall sharply.
    GQGU is the residual (287 of 457 rows move; its keys lack a Bloomberg ticker).
  - CTO half SIGNED @98d4271685, with a condition: before `--apply`, an overlay replay of `dramatic_move` and `price_series`. A new
    dramatic-move flag on a held-tr date is a STOP.
  - Then the dry publish (256 new, 0 present-and-different), `--apply` with read-back, and NEVER-2 on site Z's ledger. GQGU's residual
    becomes a row.
  - There is no seat rollback: removal is an S3 delete, Andrew's act.

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
| sha256sum on the COO half and the off-git table | PASS | both bound |
| native Read of the COO half | PASS | the 10-reader census, with seven readers unmeasured |

What worked: making the unmeasured readers the signature's condition instead of waving them through. Gap: none new.

-- 1.0.0_SA_CTO~DELL1
