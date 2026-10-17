# 1.0.0_SA_CTO~DELL1 -- self-drive dell1 box, tick 84 (covers ticks 83a and 83b, about 19:19Z to 19:48Z)
**archetype:** COORDINATE

Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261016_024xZ_SELF_DRIVE_DELL1_BOX_30M.md` @fa59eb8dec. state: ARMED.

## Rulings and acts (hashes LOCAL on box/dell1)

- **HARVST ce-4 done (W1 7712).** 62 of 62 add-only gold writes ran 17:22Z to 19:27Z, all inside the signed half @eae892eec0.
  - My read of `ce4_written.out`: 31 distinct continuation keys and 31 distinct dossier keys.
  - SC1's driver process died silently at about 18:45Z, after NOW_US_Equity's continuation. W1 ruled a guarded resume.
  - The manifest shows NOW's continuation as EXISTED-NOT-REWRITTEN, with the same VersionId: no retried write, so the half was not
    widened. The resume is accepted.
  - The driver death goes in as a surprise row on AMGT_HARVST.
- **RESAPP round 112 approvals (R1 7715), Security Analysis, opal-internal:**
  - row 48c7, bs-1 @618a39dd5f: a harness and census fixture only, approved for DEV only and kept out of the promote;
  - row 32d8, bs-2 @937f15a01d: one price-currency helper for the header and Peers, approved for DEV and PROD.
  - Addendum 4 @b8837e499e. The padded-currency edge is carried to round 113.

## Completion test

NOT DONE. This is the standing box drive, which ends on Andrew's word.

## Acts only Andrew can do (each with its citation)

1. ADVI_COTBOOKS: confirm the 6 DONE WHEN lines (row 0cf5). Canonical loop L2.
2. SOC2_MSLOGS round 2: run the 8-day re-derive with his MFA session (row 89c9). The access group holds Andrew_Berman alone (TO-R2-r2 :29).
3. SOC2_MSLOGS FWD-1: his read of the enriched block, through the same MFA door.
4. EWS delivery channel. Nothing sends until he names one.
5. FWD-10's portal source line to PROD, a client-facing push (CLAUDE.md PUSHES).

## Compiler Tools

| tool | result | note |
|---|---|---|
| grep / sort / uniq over ce4_written.out | PASS | distinct keys and the duplicate-line check |
| git show --stat (portal) | PASS | bs-1 and bs-2 file sets on 932cea99 |

What worked: reading the write manifest by key, not by line count. Gap: a long nohup driver can die silently. That is the surprise row
requested.

-- 1.0.0_SA_CTO~DELL1
