# ETFS_RIVALS (rivalfunds) -- status (FULL; round 7 DEPLOYED 75ad1e4d2e and CLOSED; round 8 cut after the 2026-10-05 grades)

Seat `2.0.0_SA_COO~RV` (CLAUDE). Mode FULL on Andrew's word ("yes you can move to /canonical-drive for the remainder";
record `org/tier1_exec/2.0.0_SA_COO/deliverables/cooRV_ANDREW_DIRECT_20261002_141xZ_CANONICAL_DRIVE_MAX_PARALLEL_RELAYED.md`).
Goal (Andrew ~04:59Z): "i want mcp.opalinvest.dev/rivalfunds demoable Today".

Team:
- reviewer `3.0.0_SA_CVO~RV`: round-7 L8/L9 part A at caf8f6bf69; the drain-end packet was sent 00:08Z;
- open calls `4.0.0_SA_CRO~RV`: CALLs 1-14 ruled (CALL 14: LONG_COMP_NAME rides R-21).

As of 2026-10-03T00:5xZ.

## Pins

| What | Value |
|---|---|
| Deployed artifact pin | CLOUD **75ad1e4d2e** in the five rivalfunds Lambdas (round 7: sa-1, pv-1, cu-1, rd-1, nt-1, nm-2, cg-1, cs-1). The sweep schedule input carries `run_path: "scheduled"` |
| Deploy record | NEVER-2 `etfs-rivalfunds-round7` CLOSED 6/6 (65ebcbdd20). Pair: COO 76f548ce47 / CTO be6048931d. Post-act: `deliverables/2.0.0_SA_COO~RV/round7/postact_round7_deploy.json` |
| Served page 2026-10-02 | batch rv-publish-1002r7: 13/13 funds, 213 trades, AI 12/12, 1,886,555 B (cap 2,097,152). "Single trade" 58, UNRESOLVED 0, case-only name clashes 2 |
| Round 7 | 8/8 orders complete (issuance ce9f61d933; flips db36578751 + 2998d045a2); every worker worktree removed |
| I-1 (W4-S9) | DISARMED (30fb2b5079, row Z-S15); the continuation half is cu-1, now deployed |

## Round 7 CLOSED (CTO analysis 115645c4b4, on CVO slug 28841 @904caf2003)

The apply PASSES and rd-1's J1 PASSES. sa-1's J1 and ui-5 are NOT_EVALUATED until 10-05, by design.

## Next proof: Monday 2026-10-05, named readers (ROUND_ANALYSIS.round7.md ruling 2)

If a seat is not live at its time, its first live session reads before any other act.

1. **11:00Z (07:00 ET) and after 08:03 ET, `2.0.0_SA_COO~RV`:** the vehicle pull.
   - `get(id(), name())` gives names, not ticker forms.
   - G4 `security_name` is populated, with `__field_errors__` empty (CRO~RV CALL 14).
   - **A LONG_COMP_NAME field error -> revert `enrichment_bloomberg.py` in CLOUD the same session.**
2. **13:00Z (09:00 ET) sweep -> 13:30Z read.**
   - `2.0.0_SA_COO~RV` reads the evidence: the REPORT line, `gold/research_hypotheses/date=2026-10-05/` with run_path
     "scheduled", the attempt record, and the page manifest's `ai-` batch.
   - `3.0.0_SA_CVO~RV` grades sa-1's J1 and ui-5 on the SERVED 10-05 page.
   - "Nothing happened" is a FAIL that morning.
3. **Round 8: ONE issuance after those grades.** The enrichment list:
   - W1-S46's deadline-aware vendor timeout (a planted deadline still republishes);
   - the 3 money-market keys (DGCXX x2, IJGXX) in reader words;
   - what the 10-05 grades leave open;
   - the walk-register remainder.
   **PREPARED, not issued:** local branch `rv-prep8` @b483790280 (worktree /c/tmp/rv-fast) holds
   `deliverables/2.0.0_SA_COO~RV/round8/`:
   - DECOMP_DRAFT.md: 4 cells on 3 chains (dt-1; an-1 -> rw-1; rp-1), with 7 rulings;
   - register_r7.json: 33 items, 17 REALIZED / 8 PARTIAL / 6 NOT / 2 not-yet;
   - 7 checks, each base FAIL and fix PASS.
   The cut adds item 3, re-runs the checks at the then-current base, and issues once.
   Repairs batched into one cell: Z-S18 (rp-1). Z-S16 was dismissed by the CVO (C-S26) and Z-S17 is retracted (Z-S19).
   The G5 replay (D10) is NOT cut (draft ruling 4): its 6 cells roll off around 10-08, and a replay route would help for
   about 2 days.

## Issuer acts still owed

- **G5 replay (D10): ruled NOT owed** (round-8 draft ruling 4). A rebuild at the deployed code would clear the 6 n/a
  cells (measured locally at `C:/tmp/r7measure/g5pin/`). But no deployed route rebuilds G5, a local gold write is QA-only,
  and the cells roll off around 10-08. If Monday's grades raise it, a replay-route cell joins the repair chain.
- **I-2: PARKED pending Andrew's explicit directive.**
  - What it is: IDVZ/PFOE trend from inception (D12); ACWI/IWM benchmarks (D13, the v0.8 leg: +4 names on the same 1
    query, measured offline).
  - Andrew-direct ~17:3xZ 2026-10-03 (MSTR broadcast msg 28913; record
    `org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20261003_17xxZ_RELEASE_ALL_QUARANTINE_NO_DATA_OPS_CHANGES_WITHOUT_DIRECTIVE.md`):
    "it is inappropriate for agents to adjust our data engineering operations without my explicit directive ... We will
    discuss internally on how to proceed with further data collection after review."
  - Both acts are new data collection, so neither runs until his directive names them. Owner: 2.0.0_SA_COO~RV. Un-park
    condition: Andrew's explicit word on D12 and/or D13.
  - No ETFS_RIVALS quarantine exists to release: "quarantin" has 0 hits in the mission tree, the rivalfunds package, and
    3,996 rivalfunds/etfs S3 keys.

## Open findings (rows, owner named)

- Z-S16 is DISMISSED (CVO C-S26, ADJUDICATION_v7.Z). A skipped step omits `run_path` rather than misstating it; no stored
  value is wrong.
- Z-S17 is RETRACTED by Z-S19. The 0 -> 0 G5 exit row is ruled behaviour (CRO~RV CALL 12, ratified): G5 keeps the row and
  the page hides and counts it. Round 6's x-1.AC3 pins it. Nothing is owed.
- Z-S18 (COO~RV): the census's +2 missing prices are PFOE's ServiceNow and Workday. cg-1 re-keyed them to the rankings'
  key, and the holding-implied lookup still reads the books by the G1 key. The page is unaffected; next round.
- 795 snake_case tokens remain on the page: cited table names and guardrail codes, left out of rd-1 by the cut.
- IDVZ (I-4): the TrueShares layout changed on 10-01 (Andrew's or CRO~RV's call on the source policy).

## Limits

No product ID is PASS until `3.0.0_SA_CVO~RV` grades the served artifact. Workers never call a vendor, write S3 or deploy.
An agent-turn vendor call is excluded by the PRD's NEVER line (:891), even under a launch word (CRO~RV CALL 14).
