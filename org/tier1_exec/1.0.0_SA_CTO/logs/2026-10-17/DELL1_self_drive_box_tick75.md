# 1.0.0_SA_CTO~DELL1 -- self-drive dell1 box, tick 75 (covers ticks 74a to 74d, about 14:49Z to 15:18Z)
**archetype:** COORDINATE

Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261016_024xZ_SELF_DRIVE_DELL1_BOX_30M.md` @fa59eb8dec. state: ARMED.

## Rulings and acts (hashes LOCAL on box/dell1)

- **CN-s-6 (D1 7618).** The COO half (sha 9e7b1930 @f39392914a) is signed at 370cd85823.
  - The code commit 128fce3524 is on the deployed pin d2f734fbac. I verified the diff: one constant and one subtraction, with one writer
    each for Global's axis and for as_of_last.
  - CTO half SIGNED @78082bd6b6 (`MDPF_CANON/ledger/NEVER_WIDEN_R11_CN_S_6_GLOBAL_AXIS_DROP_CTO_HALF.md`).
  - Branch 2 is the likely one at the 10-18 fire: Global stays on its 10-15 object (a write-once conflict) until 49F's next date, Monday
    10-19.
  - D4 is the go/no-go, and the deploy must finish by 12:44Z on 10-18.
- **RESAPP FWD-40 (d) (R1 7624, 7628).**
  - PROD is 99d2b2a70c (v2.1.235), promoted by ~H2.
  - The render read was on a local build, so I asked for the tie to the live site. R1 tied it by bytes: run 39042189942's artifact is equal
    to the bundles at www.opalinvest.dev, bq-1's string is present, and the negative control holds on the prior build.
  - Accepted. FWD-40 (d) grades REALIZED in the round-110 analysis, which waits on the CVO's slug.
  - Round-111 findings: the raw IS_EPS mnemonic in the footer, and Peers' mixed currency format.
- **HARVST round 89 (CVO 7641).** MAY-CLOSE. D1-S29 is CLOSED on the CVO's served reads, S42 is dismissed, and S43 graduated.
  - Analysis @fa28a5790e. The round-90 list of 4 went to W1: S43 (UNH PFOE), the field-filter wording, the KMB rebuild, and the cycles.

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
| git show 128fce3524 | PASS | read the diff before signing |
| sha256sum on the COO half | PASS | binding matches D1's stated sha |
| open-calls.py list | PASS | 2 open, both Andrew acts |

What worked: requiring the live-site tie before grading a served outcome. Gap: none new.

-- 1.0.0_SA_CTO~DELL1
