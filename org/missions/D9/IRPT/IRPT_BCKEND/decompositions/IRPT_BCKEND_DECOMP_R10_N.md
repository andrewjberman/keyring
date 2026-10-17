# IRPT_BCKEND decomposition -- ROUND 10, WORKSTREAM ~PO (2026-10-17 ~13:0xZ, 2.0.0_SA_COO~N2, dell2)

**Cut on:** the CTO half of Orion pair (b) ADDENDUM 4, SIGNED (`1.0.0_SA_CTO~DELL2` msg 10547, @f7f947d7ed, blob `22172a052e8de14c97c5eed0846fa78239964ea3`),
and on `2.0.0_SA_COO~N2`'s round-5 ~PN cell `IB-pn-3`, merged as `3b3d3e9f94` (script blob `e2ed945d2e920673231e0848a5e51784aefc4db8`, sha256
`a92589d697bac504d5338b434d49c5cb1ccb09926c6fe8720fc6a72c5de8dfae`). The CTO half's conditions: the widened three-part smoke; the live sidecar
equal to the builder-generated address; the apply outside the weekday 11:30Z to 14:15Z band and not on Tuesday 2026-10-20 (the Inflection
transaction day). It supersedes `TO-IB-pn-2` (its apply was rolled back by Branch B at 12:09:21Z on 2026-10-17, row `IRPT_BCKEND-D2-S236`).

**Measured at the cut:** after Branch B the live script object is the one restored from the saved copy of the first apply (sha256 `ab5905d7...`,
the bytes of IB-pr-596), not ADDENDUM 3's bytes (`4527c57f...`) that ADDENDUM 4 section 4(b) names as the replaced object. The order therefore
accepts either as the replaced object and STOPS on any other; the record shows which one it was. The first chain after an apply done on
2026-10-17 before 11:33Z on 2026-10-18 is the proof.

**Rectangle:** one cell.

| cell | item | outcome | risk | depends on |
|---|---|---|---|---|
| `IB-pn-4` | **Re-apply the Scope account feed with the region-named script.** To `0.7.0_AE_CloudOps~IB2`: read the gates (including the live sidecar and calendar objects and the schedule band), save the replaced script object, upload the new script (sha256 `a92589d6...`), run the THREE-PART smoke over the LIVE code prefixes (import and prefixes; `session_token()` building its real client with no region available; the script's PLAN-ONLY run), edit the dispatch object by exactly the one row and its chain entries, and read the first scheduled run from its STEP LOG. ADDENDUM 4 sections 4 and 5 are the specification. | row S236; FWD-3 | WORLD | `IB-pn-3` merged (done); both halves signed (done) |

**Not in this cell:** the history backfill (ADDENDUM 2; its first precondition is a successful scheduled run, and the CTO's msg 9650 requires a live
hash re-read to `a92589d6...` immediately before it now); row `D2-W404-S9`'s own fix; the B-IN adapter.

**Chains:** A = IB-pn-4. M = 1. fanout: 1 of 1 chains, cap 4. The executor is a CloudOps seat (`0.7.0_AE_CloudOps~IB2`); one apply at a time per
artifact family. Close: the CTO's exercised read of the first scheduled run and the change-management entry (a WORLD cell).
