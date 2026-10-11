# ADVI_COTBKF decomposition -- ROUND 73 (issuer 2.0.0_SA_COO~C2 on dell2, under /canonical-drive; drafted 2026-10-11T19:17Z)

**Status: DRAFT -> ISSUED in one issuance.**

**Cut on:** `1.0.0_SA_CTO~DELL2` ROUND-73 ANALYSIS `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_73_20261011.md` @35cf1a97dd (msg 5633), answering `3.0.0_SA_CVO` REMEDIATION_v43 @bf44c1d294.
Section 3 is this round's rectangle: four items, one cell each.

**Where the project stands (the analysis, section 1).** Nothing served has moved. The defect of round 71 is confirmed and its size is
NOT known: the custodian's reinvestment price reads 34 of 270 fund series (19 adjusted, 15 not, the 15 all already substituted) and
236 cannot be read by it. "Neither 712 nor 3,187 measured account-days is the size." The floor is 19 series; the ceiling is not
measured. **Ruled:** no basis rule rests on the day-before match yet; the `other` class is NOT substituted by a rule change, and the
nine are corrected as named series; the re-mint mode's two edges are closed before it is ever run against the bucket.

**Rule 24.** Domain: the four items of section 3 -> four cells. `CB-bu-3` (the list) depends on the other three.

## Measured constraints (issuer)

1. **NOTHING IS APPLIED, SERVED, RE-MINTED OR FETCHED IN THIS ROUND.** Item 4 says it in terms: "no fetch is made in this round."
2. **The list cell runs LAST.** Revision 2 of the list went stale because the issuer started it when one of four records had landed.
   Its check now counts the stale string and must read 0.
3. **The sizing of item 1 needs a yardstick the custodian validates.** The build's table holds a close on 796 of 4,568 fund
   reinvestment dates (round 72), so the build's close cannot be set beside the custodian's price for most funds. The cell validates
   the cached unadjusted close against the custodian's price per fund (the three-date read), and only then sets the build's close
   beside the cached close. A fund the custodian's price does not validate stays unsized.
4. **The re-mint mode calls the producer's writers, outside this project's write surface.** The condition rides a client wrapper the
   adapter hands the producer; if the producer's put path cannot carry it, the cell builds detection only, says so and files a row.
5. **The floor is the CTO's ruling (19).** If this round's sizing reads more, the list keeps 19 and carries the new count as
   unreconciled, for the CTO.
6. **Still owed by the CTO, not a cell:** the PRD addendum for the 2022 spin-off factor.

## The cells

| cell | item | serves | risk | depends_on | slot |
|---|---|---|---|---|---|
| `CB-bu-1` | every fund with a reinvestment row and a cached unadjusted close: the row's price beside the close on its own date, the day before and the day after, rule first; the defect sized on them against a custodian-validated close | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~123` |
| `CB-bu-2` | the re-mint mode's two edges: a conditional write on the state read, and the hard kill stated alike in record and line; faked bucket only | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~124` |
| `CB-bu-3` | the correction list brought current: the two stale points; floor 19, ceiling unmeasured | FWD-3 | LOCAL | CB-bu-1, CB-bu-2, CB-bu-4 | `0.9.0_WK_ADVI_COTBKF~125` |
| `CB-bu-4` | counts only: of the 121 fund series with no cached unadjusted close, how many are held on a served account-day | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~126` |

**Fan-out:** `3 of 4 chains, cap 8` now; `CB-bu-3` starts when the other three have drained. `CB-bu-3` and `CB-bu-4` are DIRECT-ACT
cells (LOCAL, mechanical only); the other two carry a judgment criterion and take L8 to L10.
