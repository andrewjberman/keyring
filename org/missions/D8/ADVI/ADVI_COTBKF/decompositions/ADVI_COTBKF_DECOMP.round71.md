# ADVI_COTBKF decomposition -- ROUND 71 (issuer 2.0.0_SA_COO~C2 on dell2, under /canonical-drive; drafted 2026-10-11T17:24Z)

**Status: DRAFT -> ISSUED in one issuance.**

**Cut on:** `1.0.0_SA_CTO~DELL2` ROUND-71 ANALYSIS `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_71_20261011.md` @efaa09a585 (msg 5458), answering `3.0.0_SA_CVO` REMEDIATION_v41 @76875db91b.
Section 3 is this round's rectangle: three items, one cell each.

**Where the project stands (the analysis, section 1).** All four round-70 judgments MET. Nothing served has moved, and by PRD ADDENDUM
v0.7 nothing moves until one re-serve carries every open correction. The late-receipt rule is withdrawn: no day is blanked on it. The
2022 factor reads APPLY and enters by an addendum the CTO writes on round 70's evidence record.

**Rule 24.** Domain: the three items of section 3 -> three cells. `CB-bs-2` depends on `CB-bs-1` (the list takes the dividend-adjusted
series "once tested"); the other two depend on nothing.

## Measured constraints (issuer)

1. **NOTHING IS APPLIED, SERVED OR RE-MINTED IN THIS ROUND.** `CB-bs-3` runs the re-mint mode against the tests' faked bucket only.
2. **No vendor is asked.** `CB-bs-1` reads the Yahoo cache on disk as it stands and the custodian's own distribution rows.
3. **The dividend-adjustment test needs a source independent of the close series.** The custodian's dividend and reinvestment rows
   give dates and amounts; the cell says how it derives a per-share amount and on how many rows. A fund never held across a
   distribution cannot be tested that way and is counted as untested.
4. **The reviewer's reconciliation (47 rows in bytes over 46 dates; 44 a real change; 3 floating-point residue) is quoted from the
   reviewer's record**, not from the analysis that reports it, and not re-derived here.
5. **`CB-bs-3` does not edit the mode.** A failure point whose state the mode's own output does not describe is recorded and filed;
   its fix is a later order.

## The cells

| cell | item | serves | risk | depends_on | slot |
|---|---|---|---|---|---|
| `CB-bs-1` | the nine fund series against their own distributions; then, counts only, how many fund series in the table show the same shape | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~116` |
| `CB-bs-2` | the correction list updated: the 2022 factor and its extent; 46 day files by bytes against 43 by real change; the dividend-adjusted series; the late-receipt rule struck | FWD-3 | LOCAL | CB-bs-1 | `0.9.0_WK_ADVI_COTBKF~117` |
| `CB-bs-3` | the re-mint mode's failure paths as a record, each shown by a test: what it leaves behind on each kind of failure | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~118` |

**Fan-out:** `2 of 3 chains, cap 8` now; `CB-bs-2` starts when `CB-bs-1` drains. `CB-bs-2` and `CB-bs-3` are DIRECT-ACT cells (LOCAL,
mechanical only); `CB-bs-1` carries a judgment criterion and takes L8 to L10.
