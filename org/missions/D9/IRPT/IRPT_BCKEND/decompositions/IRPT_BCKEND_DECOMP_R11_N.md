# IRPT_BCKEND decomposition -- ROUND 11, WORKSTREAM ~PO (2026-10-19 ~14:1xZ, 2.0.0_SA_COO~N2, dell2)

**Cut on:** the CTO ruling `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/1.0.0_SA_CTO~DELL2/RULING_IB_PN5_BRONZE_ENVELOPE_FIX_WRITER_FIRST_20261019.md`
(@2f780e14a6): "IB2's two read-only reads (note section 'What would settle it') may run now. They do not wait on the fix." ADDENDUM 5 must
carry the roster's earliest start date and the day count N, and the measured size of the first scheduled run's bronze object.

**Measured at the cut:** TO-IB-pn-4 is complete (@c9cef038ef): the first scheduled chain (2026-10-18 11:33Z) wrote exactly two feed keys under
`orion/inflection/` and the 2026-10-19 chain skipped both as existing (IB2 msg 10676). The script limits `--from-date` to
`MAX_FROM_DAYS_BACK = 4000` days before the pull date (line 57), so N above 4000 would refuse a backfill run: the read states whether N is within it.
Not measured: N, the household count now, the size of either object.

**Rectangle:** one cell.

| cell | item | outcome | risk | depends on |
|---|---|---|---|---|
| `IB-pn-6` | **Two read-only reads for ADDENDUM 5.** To `0.7.0_AE_CloudOps~IB2`: (1) the earliest account start date over the feed's universe, the first scheduled run's day, N, the household and account counts, the null-start-date count, and whether N is within 4000; (2) the stored size, key count and version count of the first run's bronze and silver objects. Counts, dates and bytes only, in a record. | CTO ruling @2f780e14a6 | WORLD (read only) | none |

**Not in this cell:** any write; the ADDENDUM 5 pair; the apply of the new script; the backfill; row `D2-W404-S9`'s fix.

**Chains:** A = IB-pn-6. M = 1. fanout: 1 of 1 chains, cap 4. The executor is a CloudOps seat (`0.7.0_AE_CloudOps~IB2`). Close: this seat re-runs the three
criteria of `checks/r11/pn6_cells.py` on the record at HEAD.
