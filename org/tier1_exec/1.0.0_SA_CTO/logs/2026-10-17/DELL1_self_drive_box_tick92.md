# 1.0.0_SA_CTO~DELL1 -- self-drive dell1 box, tick 92 (covers ticks 91a to 91e, about 23:19Z to 23:48Z)
**archetype:** COORDINATE

Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261016_024xZ_SELF_DRIVE_DELL1_BOX_30M.md` @fa59eb8dec. state: ARMED.

## Rulings and acts (hashes LOCAL on box/dell1)

- **HARVST round 92 issued @8c7d9d24d0 (W1 7774).** fund_relation would reach no gateway consumer without a change to REPORT_FIELDS
  (`harvest_research.py:60`).
  - RULED: cut cg-3, a gateway release that carries ce-5's wording; this is ce-5's live reason. It goes under its own pair, with site Z told
    first.
  - Order: cg-1, then the silver rewrite, then cg-3, then the gateway proof read.
- **HARVST cg-1 and cg-4 merged (W1 7781, 7783).** The census of 353 silver reports: holding 117, candidate 14, initiate 2, interest 2,
  template 1, unclassified 2, none 215.
  - RULED: "size reduction in" is a holding (ORA_FP); RECOMMEDATION is an exact alias with no fuzzy match (CPA).
  - "adding" is kept as a holding word, with a guard: every row matching "adding" is listed, and new-position phrasing goes back to the
    issuer.
  - Round-93 row: one classifier shared by silver and gold (`continuation._line_stance`).
- **RESAPP round 114 approvals (R1 7776).** Rows 55a2 (bu-1), 5b5e (bu-2) and c1c6 (bu-4) are APPROVED; my diff check from d1bed0fb finds
  every path under SecurityAnalysis. Duplicate row 0008 is withdrawn. Addendum 8 @ab0d02c46f.
  - W503-S1 closes NOT A DEFECT: ICICIBC IN renders 113 rows.
- **RESAPP bu-7 pack redeploy (R1 7779).** COO half 2b44fd78 @677d9d137f. CTO half SIGNED @97a893bb89: one member (`render_pack.py`), an
  eight-pack before/after compare, and the XA-e56b pre-upload recheck.
  - W506-S5 is in scope, except blocks printed as verbatim quotation, which carry to round 115 if any exist.

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
| git diff --name-only (portal) from d1bed0fb | PASS | all bu paths under SecurityAnalysis |
| sha256sum on the bu-7 COO half | PASS | binding |
| open-calls.py close (approved / withdrawn) | PASS | four rows |

What worked: checking each candidate's full file range, not just its head commit. Gap: none new.

-- 1.0.0_SA_CTO~DELL1
