# ADVI_COTBKF decomposition -- ROUND 74 (issuer 2.0.0_SA_COO~C2 on dell2, under /canonical-drive; drafted 2026-10-11T20:25Z)

**Status: DRAFT -> ISSUED in one issuance.**

**Cut on:** `1.0.0_SA_CTO~DELL2` ROUND-74 ANALYSIS `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_74_20261011.md` @42390144c0 (msg 5758), answering `3.0.0_SA_CVO` REMEDIATION_v44 @edbfc928ca.
Section 3 is this round's rectangle: five items, one cell each.

**Where the project stands (the analysis, section 1).** Nothing served has moved. Both round-73 criteria MET. The defect's floor is 19
fund series (21 by the validated-close instrument); three reaches stand on three different sets and none is a return error. "The size
in returns is still not measured." **Ruled:** the date convention belongs to the VALIDATION, not to the price: a fund is valued on a
day at its unadjusted close for that day, and no family rule enters the build's pricing. The re-mint mode's rows are closed; the real
bucket's handling of the write condition is a line of the re-serve's pair. **One fetch is permitted, once,** for the 27 held series.

**Rule 24.** Domain: the five items of section 3 -> five cells. `CB-bv-3` depends on `CB-bv-2` (it touches the validated funds only);
`CB-bv-5` (the list) depends on the other four.

## Measured constraints (issuer)

1. **NOTHING IS APPLIED, SERVED OR RE-MINTED.** Cell 3 builds two local copies and reads the bucket at the pin; it writes nowhere
   but a worktree scratch.
2. **The fetch (cell 4) is the 27 held tickers, once each, from the source the cache already uses; not Bloomberg; the 94 unheld are
   not fetched.** ISSUER RULING inside this decomposition: the files land in a NEW folder beside the cache
   (`C:/dev/ajb_workspace/.scratch/advi_cotbkf/yahoo_census_fetch_r74/`), not in the cache folder. The served table was reproduced at its pin against that folder as it stands, and a pinned
   re-build must still find it unchanged; the cell prints the folder's file count before and after. The project's own local data
   area holds both.
3. **None of the 27 has a reinvestment row** (round 73), so the custodian's price cannot validate a fetched close. Every reading of
   cell 4 says so, and cell 3 does not use them.
4. **Cell 3's baseline must equal the served returns before any variant number is read.** Its check's expected line carries
   `baseline_differing=0`. The variant is made through the as-traded basis's own substitution, pointed at a copied census file;
   if the chain cannot take a copy without a code edit, the cell stops and says which constant binds it.
5. **The either-date validation rule (cell 2) is wider than round 73's best-single-date rule.** The cell counts the dates on which
   the adjusted close matches too and lists any fund validated only on such dates.
6. **The list cell runs LAST,** as in round 73.
7. **Still owed by the CTO, not a cell:** the fund-basis rule as a PRD addendum (after cell 3's table); the 2022 factor's addendum.

## The cells

| cell | item | serves | risk | depends_on | slot |
|---|---|---|---|---|---|
| `CB-bv-1` | the date convention by fund family, rule first; per family or not established | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~127` |
| `CB-bv-2` | the validation rule written first (the row's own date or the trading day before; a stated share and minimum); validated, refuted, unreadable over 270 | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~128` |
| `CB-bv-3` | the first return number: for the validated funds, account-days whose daily return changes on the unadjusted close, in three bands; built on a copy at the pin | FWD-3 | LOCAL | CB-bv-2 | `0.9.0_WK_ADVI_COTBKF~129` |
| `CB-bv-4` | the one permitted fetch: the 27 held series, each asked once, into a new folder | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~130` |
| `CB-bv-5` | the correction list brought current with cells 1 to 4 | FWD-3 | LOCAL | CB-bv-1, CB-bv-2, CB-bv-3, CB-bv-4 | `0.9.0_WK_ADVI_COTBKF~131` |

**Fan-out:** `3 of 5 chains, cap 8` now; `CB-bv-3` starts when `CB-bv-2` drains; `CB-bv-5` when the other four have. `CB-bv-4` and
`CB-bv-5` are DIRECT-ACT cells (LOCAL, mechanical only); the other three carry a judgment criterion and take L8 to L10.
