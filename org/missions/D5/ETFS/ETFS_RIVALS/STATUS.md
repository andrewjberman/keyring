# ETFS_RIVALS (rivalfunds) -- status (FULL; round 7 DEPLOYED 2026-10-02 ~23:57Z; L8/L9 at the CVO)

Seat `2.0.0_SA_COO~RV` (CLAUDE). Mode FULL on Andrew's word ("yes you can move to /canonical-drive for the remainder";
record `org/tier1_exec/2.0.0_SA_COO/deliverables/cooRV_ANDREW_DIRECT_20261002_141xZ_CANONICAL_DRIVE_MAX_PARALLEL_RELAYED.md`).
Goal (Andrew ~04:59Z): "i want mcp.opalinvest.dev/rivalfunds demoable Today".

Team:
- reviewer `3.0.0_SA_CVO~RV`: round-7 L8/L9 part A at caf8f6bf69; the drain-end packet was sent 00:08Z;
- open calls `4.0.0_SA_CRO~RV`: CALLs 1-14 ruled (CALL 14: LONG_COMP_NAME rides R-21).

As of 2026-10-03T00:2xZ.

## Pins

| What | Value |
|---|---|
| Deployed artifact pin | CLOUD **75ad1e4d2e** in the five rivalfunds Lambdas (round 7: sa-1, pv-1, cu-1, rd-1, nt-1, nm-2, cg-1, cs-1). The sweep schedule input carries `run_path: "scheduled"` |
| Deploy record | NEVER-2 `etfs-rivalfunds-round7` CLOSED 6/6 (65ebcbdd20). Pair: COO 76f548ce47 / CTO be6048931d. Post-act: `deliverables/2.0.0_SA_COO~RV/round7/postact_round7_deploy.json` |
| Served page 2026-10-02 | batch rv-publish-1002r7: 13/13 funds, 213 trades, AI 12/12, 1,886,555 B (cap 2,097,152). "Single trade" 58, UNRESOLVED 0, case-only name clashes 2 |
| Round 7 | 8/8 orders complete (issuance ce9f61d933; flips db36578751 + 2998d045a2); every worker worktree removed |
| I-1 (W4-S9) | DISARMED (30fb2b5079, row Z-S15); the continuation half is cu-1, now deployed |

## Next proof

1. **L9:** 3.0.0_SA_CVO~RV grades rd-1's J1 on rv-publish-1002r7 and sa-1's J1 on the 10-05 sweep. The L10 slug then goes to
   the CTO.
2. **2026-10-05 07:00 / 08:03 ET:** the vehicle's `get(id(), name())` and LONG_COMP_NAME (G4 `security_name`). The proof is
   `security_name` populated with `__field_errors__` empty (CRO~RV CALL 14). Names then reach the holdings Security cells,
   which show tickers today.
3. **2026-10-05 09:00 ET (the acceptance):** the sweep stamps "scheduled", continues any open cursor, runs ONE account for page
   day 10-05 and republishes under an `ai-` batch.

## Issuer acts still owed

- **G5 replay (D10):** a rebuild at the deployed code clears the page's 6 n/a cells (the 09-30 trims-to-zero become exits
  priced from the prior valuation). Measured locally at `C:/tmp/r7measure/g5pin/`. It needs its own pair.
- **I-2:** IDVZ/PFOE trend from inception (D12); ACWI/IWM benchmarks (D13, the v0.8 leg).

## Open findings (rows, owner named)

- Z-S16 (COO~RV): a skipped AI step reports no `run_path`. One line in `run_ai_step`; next round.
- Z-S17 (COO~RV): G5 writes a phantom zero-share exit one report after every full sale (stored, hidden on the page); next
  round, in `gold_trade_schedule.py`.
- Census prices missing 42 -> 44 at round 7: measured, cause not shown (CTO binding: J1 names it).
- 795 snake_case tokens remain on the page: cited table names and guardrail codes, left out of rd-1 by the cut.
- IDVZ (I-4): the TrueShares layout changed on 10-01 (Andrew's or CRO~RV's call on the source policy).

## Limits

No product ID is PASS until `3.0.0_SA_CVO~RV` grades the served artifact. Workers never call a vendor, write S3 or deploy.
An agent-turn vendor call is excluded by the PRD's NEVER line (:891), even under a launch word (CRO~RV CALL 14).
