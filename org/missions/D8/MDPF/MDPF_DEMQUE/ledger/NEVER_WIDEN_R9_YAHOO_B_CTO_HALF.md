# NEVER-WIDEN co-sign, ROUND 9 -- the CTO half, pair B: label Yahoo-sourced client prices UNVERIFIED until the porting test passes (`DQ-t-59`)

**Signer:** `1.0.0_SA_CTO~DELL1`, 2026-10-13 ~22:1xZ. **Pairs with:** `ledger/NEVER_WIDEN_R9_YAHOO_B_COO_HALF.md` (`2.0.0_SA_COO~Q1`, SIGNED).
**Andrew's rule it carries out:** Yahoo-sourced client prices already stored read UNVERIFIED until their security passes the porting test (2026-10-13, the DEMQUE form,
"Surface B").

## Signed for, exactly as the COO half states

- **One new index column, `porting_verdict`**: UNVERIFIED (default) | PASS | FAIL | UNTESTABLE. It goes on `index/index.parquet` and `index/index.csv` only, **2 keys**. No
  `cusip=` key moves.
- **The column, not `claim`, is the right shape.** Putting the label in `claim` would mint a value-enum member without its TAXONOMY LAW record. The COO's choice is correct.
- **Writers N = 1** (`price_store.write_index`). There is no new writer.
- **All three branches as stated:**
  - no verdicts file: every row reads UNVERIFIED, the true state today;
  - a verdicts file: each name reads its verdict, a missing row reads UNVERIFIED;
  - unreadable or malformed: every row reads UNVERIFIED and says why. It fails closed, so a PASS is never written on a read that did not complete.
- **Rollback:** the newest S3 version of each of the 2 keys before the run's start.

## The gap the COO names, carried as the next cell (not a condition of this pair)

The label lives on the store's index, but the figures Andrew's rule is about are DOWNSTREAM:
- `commonwealth_price_need.py` carries `demque_claim` and ignores the new column;
- `land_cot.py` does not read the index at all.

So a Cottonwood valuation built from a Yahoo price does not yet say UNVERIFIED. **Next cell, owned by the consumer:** ADVI_COTBKF (dell2, `2.0.0_SA_COO~C2`) carries
`porting_verdict` through `commonwealth_price_need` and the lander into every client figure that uses the price, under its own pair. Routed cross-box through MSTR. Until it
lands, the index column is true and the downstream figures are named as unlabelled.

**CTO HALF: SIGNED** by `1.0.0_SA_CTO~DELL1`.

-- 1.0.0_SA_CTO~DELL1
