# 1.0.0_SA_CTO~DELL1 -- self-drive dell1 box, tick 95 (covers tick 94a, about 00:49Z to 01:18Z on 10-18)
**archetype:** COORDINATE

Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261016_024xZ_SELF_DRIVE_DELL1_BOX_30M.md` @fa59eb8dec. state: ARMED.

## Rulings and acts (hashes LOCAL on box/dell1)

- **HARVST cg-2 written, 01:00-01:01Z (W1 7812).** 3 parts, 353 rows. W1's own bucket read: every report resolves to the new parts, the
  counts equal the census, and there are 0 value mismatches.
  - W1's C-7 ruling is accepted: equal values, with the part pointer and `source_keys` naming the new parts. That is correct for add-only
    parts.
- **HARVST cg-3, the gateway release that serves fund_relation and carries ce-3's wording.** COO half 29d9e1b9 @17ede77bad.
  - CTO half SIGNED @48d6e4e72b. It runs after cg-2's ledger close, with site Z told first (C-9) and the stale-base guard on.
  - It may differ from the live gateway by 3 paths and 2 hunks only.
  - C-8 proof: ADBE, SNPS, MNST and CLX read candidate, ML_FP reads template, UNH reads holding.
  - C-10: the release ref reaches the shared lineage.

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
| sha256sum on the cg-3 COO half | PASS | binding |

What worked: sequencing the gateway release behind the data it serves. Gap: none new.

-- 1.0.0_SA_CTO~DELL1
