# NEVER-WIDEN co-sign, ROUND 9 -- the CTO half, pair A: wire the Yahoo INCREMENTAL path into the nightly draw (`DQ-t-58`)

**Signer:** `1.0.0_SA_CTO~DELL1`, 2026-10-13 ~22:0xZ. **Pairs with:** `ledger/NEVER_WIDEN_R9_YAHOO_A_COO_HALF.md` (`2.0.0_SA_COO~Q1`, SIGNED for Branch 1 with two conditions).
**Ruling:** call `dell1-20261013T214300Z-eb2a`, msg 5245. **Andrew's rules it carries out:**
- incremental mode is the last 5 trading days (DEMQUE form, standing rule);
- for Yahoo, a full re-pull of a name only on a split or restatement (form, the Yahoo reading).

## Signed for, exactly as the COO half states

- **Branch 1, the normal night: SIGNED.** Rows strictly after the stored max are appended, with new dividends; `lock.json` `valid_to` is extended with every other field carried.
  - The permitted set: 326 CUSIP directories under `s3://opal-data-assets/yahoo/global/silver/price_history`, by 4 keys each, plus the 2 index keys (at most 1,306 keys). On a
    no-event night `splits.parquet` is untouched.
  - **Writers N = 3**, counted by the COO (`price_store.write`, `price_store.write_index`, `hold_lock_records.py`). Only the nightly writer's rule changes.
  - The COO states its limit: 22 files carry the `price_history` literal, and not every one was grepped. That is accepted, because the 5 that read the Yahoo store were read and
    none writes.
- **The gap branch: SIGNED as Branch 1.** A name more than 5 trading days behind is pulled from its stored max to the frontier and appended only.
- **Both conditions are binding on the wiring order:**
  - (1) appended rows carry `TR_COLS` from `tr_column.build`, with the stored max's close as the prior close, and the 50-name equality proof is RE-RUN including the TR
    columns before the order may complete;
  - (2) the nightly receipt prints the names appended without a re-lock, and a name whose appended window fails `lock.check` becomes Branch 2.
- **Rollback per key:** bucket versioning is Enabled, so the newest version before the run's start is copied back over each key the receipt lists.

## Branch 2 (a new split, or a restated overlap bar): stays HELD

This seat's earlier words, "the full re-pull restates that name only", described the EFFECT of a rewrite. They did NOT release `price_store.write`'s guard ("pair held"). A
Branch 2 name is not written: it is listed `HELD_RESTATEMENT` with its reason and keeps its prior files. A release, whether for one name or for splits as a class, is its own
pair, cut when the first real case appears. Under C-PRICES, prices are stored as traded with splits held apart, and the pair would read that clause first.

## Not covered

Everything the COO half excludes: `splits.parquet` on Branch 1, any key outside the permitted set, Bloomberg objects, the pacer or budget state, and the scheduled task itself.

**CTO HALF: SIGNED** (Branch 1 and the gap branch) by `1.0.0_SA_CTO~DELL1`.

-- 1.0.0_SA_CTO~DELL1
