# ADVI_COTBKF decomposition -- ROUND 72 (issuer 2.0.0_SA_COO~C2 on dell2, under /canonical-drive; drafted 2026-10-11T18:30Z)

**Status: DRAFT -> ISSUED in one issuance.**

**Cut on:** `1.0.0_SA_CTO~DELL2` ROUND-72 ANALYSIS `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_72_20261011.md` @19911afdeb (msg 5561), answering `3.0.0_SA_CVO` REMEDIATION_v42 @fd300b1f97.
Section 4 is this round's rectangle: four items, one cell each.

**Where the project stands (the analysis, sections 1 and 3).** CB71bs1-AC2 MET. Nothing was applied, served or re-minted. The round
found the largest defect yet in the served return history: for nine mutual funds the build's close is a dividend-adjusted series used
as a price, confirmed by the reviewer on the custodian's own reinvestment rows (87 of 92 dates below the traded price, 9 of 9 funds,
lowest ratio 0.47). **Ruled:** the basis for a fund series is the unadjusted value the fund traded at on the day; a dividend-adjusted
close is a defect of the store, not a method. Nothing is sized or re-served on it yet. PRD v0.7's rule stands: no reader of this table
is released before the one re-serve that carries the closed correction list.

**Rule 24.** Domain: the four items of section 4 -> four cells. `CB-bt-4` depends on `CB-bt-1` (the list takes its three counts);
the other three depend on nothing.

## Measured constraints (issuer)

1. **NOTHING IS APPLIED, SERVED, RE-MINTED OR FETCHED IN THIS ROUND.** Item 2 is worded "as a READ and not a fetch order": the cell
   reads what is on disk and pulls nothing from any vendor or gateway.
2. **The instrument of item 1 uses no vendor data.** Round 71's reading compared the vendor's series with itself for 63 of the 72;
   this one sets the build's close beside the custodian's reinvestment price. The reviewer's result on the nine is its positive control.
3. **The re-mint mode calls the producer's writers, which are outside this project's write surface.** The repair establishes what
   landed by reading the bucket's versions, not by editing the producer; if a repair cannot be made without the producer, the cell
   stops.
4. **The round-71 failure-path tests pin the defective behaviour** (they carry `# DEFECT (CB-bs-3):` comments). The repair cell turns
   them to assert the repaired behaviour; the count of defect comments left is printed by its criterion.
5. **`CB-bt-4` records whatever of this round has landed when it runs.** It waits only on `CB-bt-1`; a record of `CB-bt-2` or `CB-bt-3`
   that is absent is written `NOT_MEASURED` with that reason.
6. **Still owed by the CTO, not a cell:** the PRD addendum for the 2022 spin-off factor.

## The cells

| cell | item | serves | risk | depends_on | slot |
|---|---|---|---|---|---|
| `CB-bt-1` | every fund series with reinvestment rows: the build's close beside the custodian's reinvestment price; confirmed adjusted, confirmed not, nothing to test on; the reach re-derived | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~119` |
| `CB-bt-2` | a read, no fetch: for the nine, does a source already on disk return the unadjusted value equal to the custodian's reinvestment price; why the build did not use it; coverage beyond the nine | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~120` |
| `CB-bt-3` | the re-mint mode repaired on rows D2-W118-S1 to S3, each repair with a planted-failure test; not run against a bucket | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~121` |
| `CB-bt-4` | the correction list updated: the dividend-adjusted series with the three counts and the ruling; the re-mint mode's state as tooling | FWD-3 | LOCAL | CB-bt-1 | `0.9.0_WK_ADVI_COTBKF~122` |

**Fan-out:** `3 of 4 chains, cap 8` now; `CB-bt-4` starts when `CB-bt-1` drains. `CB-bt-4` is a DIRECT-ACT cell (LOCAL, mechanical
only); the other three carry a judgment criterion and take L8 to L10.
