# IRPT_BCKEND decomposition -- ROUND 12, WORKSTREAM ~PO (2026-10-19 ~14:5xZ, 2.0.0_SA_COO~N2, dell2)

**Cut on:** Orion pair (b) ADDENDUM 5, BOTH HALVES SIGNED (`deliverables/2.0.0_SA_COO~N2/ORION_PAIR_B_ADDENDUM_5_SCOPE_FEED_RAW_ONCE_AND_BACKFILL.md`, blob
`619dbf431bc578cf22bb59114f5e289d7f9c4c94`; COO half @5c163df336; CTO half @1855ec7d0b, `1.0.0_SA_CTO~DELL2` msg 10706, both proposals confirmed) and `TO-IB-pn-5`
merged (`d281b8b32c`, script blob `b3bcc5e55afd5ef91a25232dcddf7fd3a8969472`, sha256 `acfe390bda5af03e3c38330ece8f18d32a87f122594f593f855fc6d802eb21a3`).
The CTO half's conditions: the apply and the backfill run outside the weekday 11:30Z to 14:15Z band, never on Tuesday 2026-10-20, never alongside another
IB2 act; the smoke prints the run object's address and, if it came from the sidecar, shows its partition and object name equal the builder's; the
backfill prints peak memory and a failure is a STOP.

**Measured at the cut:** the live script object is the pn-4 object (sha256 `a92589d6...`, applied 2026-10-17, read clean at the 2026-10-18 11:33Z chain).
The feed's dispatch row and chain entries are live and this order does not touch the dispatch object. The next scheduled chains: Tue 2026-10-20 11:33Z
(the Inflection transaction day: the chain runs as scheduled; the apply never happens that day), then daily. A scheduled run after a weekend or holiday
covers several calendar days at once, so the first run of the new writer may write several day envelopes and still exactly one run object.
Not measured: the live dispatch object's hash now, the runner role's grants, the live notification filter, the household count today.

**Rectangle:** one cell.

| cell | item | outcome | risk | depends on |
|---|---|---|---|---|
| `IB-pn-7` | **Apply the raw-replies-once-per-run script.** To `0.7.0_AE_CloudOps~IB2`: gates, save the pn-4 script object, upload the new script (sha256 `acfe390b...`), the THREE-PART smoke over the live prefixes plus the run object's address (builder vs sidecar), NO dispatch change, read the first scheduled run from the STEP LOG (one run object, v2 envelopes without `responses`, silver in shape). | ADDENDUM 5 sections 1, 3 and 5 | WORLD | IB-pn-5 complete (done), the pair (signed) |

**Not in this cell:** the backfill run (a later order, `IB-pn-8`, which waits for this cell's first-run read to pass); the dispatch object; the B-IN adapter;
row `D2-W404-S9`'s fix.

**Chains:** A = IB-pn-7. M = 1. fanout: 1 of 1 chains, cap 4. The executor is a CloudOps seat (`0.7.0_AE_CloudOps~IB2`); one apply at a time per artifact
family. Close: this seat re-runs the three criteria of `checks/r12/pn7_cells.py` on the record at HEAD and closes the change-management entry.
