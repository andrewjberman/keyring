# 1.0.0_SA_CTO~DELL1 -- self-drive dell1 box, tick 86 (covers ticks 85a to 85d, about 20:19Z to 20:48Z)
**archetype:** COORDINATE

Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261016_024xZ_SELF_DRIVE_DELL1_BOX_30M.md` @fa59eb8dec. state: ARMED.

## Rulings and acts (hashes LOCAL on box/dell1)

- **RESAPP name collision (R1 7731).** `ledger/ROUND_ANALYSIS.round112.md` (rounds 111 and 112) and `round113.md` belong to the gx track. I
  checked the history: my round 110 and 111 files were new, and nothing was overwritten. From round 112 on, R1-track analyses carry the
  `.R1` suffix.
- **RESAPP round 112, R1 track (CVO 7732).** MAY-CLOSE. W491-S2, W494-S1 and W495-S2 are REMEDIATED; W495-S1 is not a defect; W497-S2
  graduated.
  - Analysis `ROUND_ANALYSIS.round112.R1.md` @8dc5a8af0c.
  - The walker's "FWD-5" and "FWD-6" labels are DSGN ids (the page halves are DSGN FWD-5, 21, 22, 26 and 27, per PRD v0.33). They are
    routed to DSGN's owner and not graded here.
  - S59 ruled: cut format:dates, occluded-popover and layout:clipped (display only); truncated names are a read; the walker control is an
    instrument issue; unconnected-field goes to AIFILL.
  - The round-113 list of 5 went to R1.
- **HARVST cf-1 census (W1 7734).** 94 of 94 names, 22 phrases. Not holdings:
  - "candidate for" on 10 names (9 of the round-90 rebuilds, plus CLX);
  - "initiate ~2% position in" on CNR;
  - "interesting exposure for" on ST_SP;
  - the template line on ML_FP.
  - cf-2's classification RATIFIED: a potential add with a current weight, an increase, and maintain-or-consider-increasing are holdings;
    the default is not a holding.
  - Four JP names (8306, 8316, 8766, 9433) serve a description paragraph as last_stated_position. They JOIN cf-2 and cf-4.

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
| git log on the round-analysis files | PASS | collision history checked before writing |
| native Grep/Read of the PRD and adjudication | PASS | the FWD-5/6 identity resolved from the PRD's own text |

What worked: reading the PRD's FWD text before grading labels a walker printed. Gap: the walker prints another project's FWD ids. That is
the DSGN row.

-- 1.0.0_SA_CTO~DELL1
