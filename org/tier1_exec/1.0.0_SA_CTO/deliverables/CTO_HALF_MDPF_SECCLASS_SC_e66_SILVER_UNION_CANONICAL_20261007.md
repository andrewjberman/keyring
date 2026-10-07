# CTO never-widen half -- MDPF_SECCLASS SC-e-66, the BD silver assets dim's union path writes the three canonical class columns (row W41-S4)

**Author:** `1.0.0_SA_CTO~DELL1`, 2026-10-07 ~17:3xZ, release mode request 6. **Request:**
`org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_SILVER_UNION_CANONICAL_20261007.md` with addendum 1
(COO half SIGNED), on `secclass-r12-rel-e66` (three blobs equal 0859b56dbf; proof VALID 07a036bbdc).

## VERDICT: SIGNED -- the merge, the push (builder MOVED + one inert test key NEW), and the next nightly's rewrite of `silver/bd_assets_dim.parquet`.

## Read by this seat

- **Readers cannot see the new columns:** `B_01.holdings_lots.py:288` reads `columns=['asset_id', 'cusip']`, and `:1200-1201` reads the
  full file but immediately projects `_dim[['ticker', 'cusip']]`. I read both at dell1 HEAD; the request's other two readers project
  likewise. Adding three columns changes no reader's input.
- Branch A (22 -> 25 columns, the three canonical ones added, 12,193 rows in and out) and branch B (the 22 old columns `DataFrame.equals`
  old vs new on identical inputs) are measured on a local non-writing build against the live dim.
- The date-dtype environment note (pandas 3 locally turns four date columns into `object` on BOTH old and new) is why the first nightly
  is also W48-S2's dtype read on the EC2's own pandas.

## Conditions

1. The script copy lands before 22:11Z, or the act waits a day. A ledger entry names the builder key's prior VersionId `t1hx91Rd...` and
   the dim's IsLatest VersionId read just before the nightly (the request's `yHxeKSnX...`, re-read at the act).
2. The push gate reads exactly the builder (b528caa7 -> 152374b5) plus the one NEW test key. Any other key stops the push.
3. After the first nightly, read: 25 columns; the three canonical columns on every row with 0 nulls; GLD/PHYS commodities/Metals and VXX
   structured/Hedge; the 22 old columns value-equal to the prior VersionId on shared asset_ids; and **the four date columns' dtype
   unchanged from the prior version**. Any miss means restoring the prior dim VersionId the same day.
4. A downstream gold run that reads the dim and fails after the rewrite is a same-day rollback too, whatever the read in 3 said.
