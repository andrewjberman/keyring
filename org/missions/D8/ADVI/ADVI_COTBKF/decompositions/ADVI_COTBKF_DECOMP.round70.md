# ADVI_COTBKF decomposition -- ROUND 70 (issuer 2.0.0_SA_COO~C2 on dell2, under /canonical-drive; drafted 2026-10-11T16:32Z)

**Status: DRAFT -> ISSUED in one issuance.**

**Cut on:** `1.0.0_SA_CTO~DELL2` ROUND-70 ANALYSIS `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_70_20261011.md` @991f749df1 (msg 5340), answering `3.0.0_SA_CVO` REMEDIATION_v40 @90e1a7cbda,
and PRD ADDENDUM v0.7 @72d624cd26. Section 3 is this round's rectangle: five items, one cell each. This issuance lands only when the
issuance gate admits it, which is the proof v0.7's ratified-text half is signed (round 69's first cut was refused on an unsigned half).

**Where the project stands (the analysis, section 1).** Both round-69 judgments MET. Nothing served has moved, and by ADDENDUM v0.7
nothing moves until ONE re-serve carries every open correction. The served return history is `method_r28`'s, with a known and stated
defect on 2 account-days. The tree's default is `method_r29`.

**Rule 24.** Domain: the five items of section 3 -> five cells, none depending on another.

## Measured constraints (issuer)

1. **NOTHING IS APPLIED, SERVED OR RE-MINTED IN THIS ROUND.** Item 5 builds and tests a re-mint path and does not run it; no pair is
   written on it.
2. **The 2022 factor is NOT applied by any cell.** `CB-br-2` writes the evidence record; the factor enters by a PRD addendum written
   against it (the analysis, section 2 item 3). Its numbers are re-derived, not copied from the two earlier records or from the
   issuer's row D2-S118, which set two workers' records side by side and derived nothing.
3. **Two counts of the flow change stand unreconciled:** 44 rows over 43 dates in the day files (worker ~107) and 47 rows over 46
   dates on the silver returns table (the issuer's count on round 68's builds, which used no hold list). `CB-br-1` records both;
   it does not pick one. The reconciliation belongs to the re-serve's control, which the analysis makes exact on every column of the
   day file, with the served hold list.
4. **The late-receipt rule is NOT in the PRD.** `CB-br-4` tests it and recommends nothing.
5. **The re-mint path presumes a silver re-serve it does not build.** The serve script's write is another script's; `CB-br-5` edits
   the mint adapter only and stops if the hold list cannot be carried without the serve script.
6. **The correction list sits at the top of the deliverables folder** (`deliverables/OPEN_CORRECTIONS.json`), inside every worker's
   write grant and outside any one worker's folder, because it is the project's and is amended as corrections close.

## The cells

| cell | item | serves | risk | depends_on | slot |
|---|---|---|---|---|---|
| `CB-br-1` | the open corrections to the served table as one tracked list, each with its extent, its evidence and what closes it | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~111` |
| `CB-br-2` | the 2022 spin-off for one security: every pair re-derived, both sides of the event, the reading the round-68 rule gives | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~112` |
| `CB-br-3` | the close-against-trade scan widened: what is left of the 346, the 50 and the 1,700; fixed income's unit | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~113` |
| `CB-br-4` | the late-receipt rule on accounts held out from the fitting and on `method_r29`'s flows; the 410 by class of receipt | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~114` |
| `CB-br-5` | a re-mint path in the mint adapter, built and tested, not run: named day files only, refusing any file not on its list | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~115` |

**Fan-out:** `5 of 5 chains, cap 8`. `CB-br-1` is a DIRECT-ACT cell (LOCAL, mechanical only); the other four carry a judgment criterion
and take L8 to L10.
