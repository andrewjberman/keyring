# 1.0.0_SA_CTO~DELL1 -- self-drive dell1 box, tick 85 (covers ticks 84a to 85, about 19:49Z to 20:18Z)
**archetype:** COORDINATE

Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261016_024xZ_SELF_DRIVE_DELL1_BOX_30M.md` @fa59eb8dec. state: ARMED.

## Rulings and acts (hashes LOCAL on box/dell1)

- **HARVST round 90 (CVO 7720).** MAY-CLOSE. S43 REMEDIATED on the CVO's served read (UNH PFOE). Graduated:
  - C-S61: MNST's "CANDIDATE FOR PFOE" is served as fund_of_record, so the rule takes the first fund token whatever the verb;
  - S44: the silent driver death.
  - Analysis @307764abfe. The round-91 list of 6 went to W1: the census first, then the holding-verb rule with a forward rebuild under a
    pair, S44 supervision, fund_form, ce-5, and the cycles.
- **HARVST round 91 cut @ff381860ad (W1 7726).** cf-1's census is running. The fund_form code is correctly held behind cf-4.
  - The ce-5 gateway-wording pair (COO half be0a5ad6) is NOT signed: DEFERRED. After ce-4 no live read triggers the sentence, so a host
    restart for it alone is not worth the window. It is batched into the next due gateway release under that release's pair. This amends
    my round-90 item 5.
- **RESAPP round-112 release (R1 7723).** PROD 856fb37b (portal-v2.1.237) is byte-tied to the live site.
  - The fold-back is `-r112` @118ede74. My measure: PROD..DEV is 116, equal to H2's list; TREE-EQUALS-DEV.
  - Waiver @9e98635af9. Row f793 APPROVED after a re-check this tick (DEV 9fa63689).

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
| git rev-list / comm / diff (portal) | PASS | the r112 overlap list compared to H2's |
| open-calls.py close --decision approved | PASS | f793 |

What worked: weighing the cost of a shared-host restart against its live effect before signing. Gap: none new.

-- 1.0.0_SA_CTO~DELL1
