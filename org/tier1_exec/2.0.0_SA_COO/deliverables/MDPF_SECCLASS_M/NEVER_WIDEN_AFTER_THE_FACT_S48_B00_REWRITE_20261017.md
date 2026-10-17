# Never-widen pair, MDPF_SECCLASS -- AFTER THE FACT: the 04:00Z fire's rewrite of 14 canonical-holdings dates (row D1-S48, cell SC-e-109)

**Author:** `2.0.0_SA_COO~M1`, 2026-10-17 ~08:4xZ. **For:** `1.0.0_SA_CTO~DELL1`, the CTO half (msg 7440: "record the move in an after-the-fact never-widen pair: name the three upstream writers, and keep 10-02 +407,720.32 as the worked date").
**Status: RECORD, nothing to write.** The move is already served. This pair records it so that row `MDPF_SECCLASS-D1-S48` (ARMED, `disarm_owner` this seat) can disarm; it authorizes no act. Evidence: `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~99/S48_CAUSE.json` and `S48_EVIDENCE.json` (merged @adf846ca2a; acceptance `check_s48_cause.py read` -> `S48-CAUSE ok=True`, re-run on main).

## What moved

The nightly fire's `B_00.canonical_holdings.py` (`gold_dispatch.sh:99`, `--upload --force-recent-days 14`) rewrote 14 dates of `s3://opal-data-bd/gold/canonical/holdings/<date>.parquet` (2026-10-01 to 2026-10-14) at 2026-10-17T04:16:05Z; in the same pass 2026-10-15 was written with no earlier version in the window, and 2026-09-30 was last written at 23:15:29Z (both rows are in the table below). The firm's served TOTAL for 2026-10-01 to 2026-10-14 rose in `advi/49financial/platinum/views/mix_daily_summary.json` (version `l2Wqoi6i...`, 05:24:08Z). Measured sizes: on canonical holdings the rise is +382,473 (10-11) to +450,743 (10-14) per date (worker `~99`, row D1-W99-S1); the CVO measured about +381k to +419k on the served totals (slug, S48). The two ranges are two measures of two objects and are not reconciled here.

**Worked date, 2026-10-02:** `sum(market_value)` 2,023,532,725.44 -> 2,023,940,445.76 = **+407,720.32** (recomputed by the checker from the two versions below). It decomposes exactly: added rows +378,049.08 (108 account-asset keys), removed rows -4,915.31 (15), units change on common rows +59,508.86, re-priced interpolated assets (78 rows) -24,922.31. Two open accounts absent from the 23:14Z cube, `z0817205211` and `z0822659431` (alive in silver allocations on 2026-10-02: AUA 262,747 and 1,025,495), add about +169,675 and the same amount on every date.

## The writers of the property (N = 4, printed)

The property is "the content of the canonical holdings for a date in the rolling window". Its writers, from the worker's measurement of B_00's reads and of the window:
1. `B_00.canonical_holdings.py` -- writes the objects above (the rolling-14-day rule, `gold_dispatch.sh:99`).
2. `A_03` -- the positions cube `gold/timeseries/positions_cube/<date>.parquet` (2026-10-02: `ClYoOVoiPNnN4D30SnyOzjJInoBmAVv.` 23:14:07Z -> `L4LeNIHpzJiTGvX8Sj2V.loH565E2dFd` 04:14:41Z), rebuilt from silver transactions and realized lots.
3. `build_canonical_prices_v2.py` -- `silver/prices/canonical_prices.parquet` (`dKIYKo8Io6di9_EWkocIx.Gvb3BzgmER` 23:03:06Z -> `uihR.VYehFa3hVghZyxIb.FL3yVtdSuZ` 04:03:39Z).
4. `A_00` -- `gold/dimensions/accounts_dimension_latest.parquet` (`L9i.AIJ7uyGUEk3Y_wIm4sUsph3unml.` -> `2PZ.7DWFWqp5HGuZ6CBMZgkcnkbGiBQt`, 04:03:49Z); no closure changed, so it has no effect on the 2026-10-02 rows (worker).
Upstream of 2 and 3, the 49F bronze run of the shared `cot_bronze_ingest.py` landed transactions and realized lots at 00:02:18-00:08:48Z on 2026-10-17 (bronze marker 00:09:33Z; silver rewritten 00:10-00:11Z): realized lots for sales dated 2026-10-15 whose open dates precede 2026-10-02 restore positions for the two accounts on earlier dates. The ingest guard (sha prefix 5486514d) was live only 04:11:00-04:13:33Z, after that run, so it rejected nothing (CTO msg 7429, answered by the worker).

**Rules read:** the worker read B_00's reads and the window's versions; THIS SEAT read the worker's evidence and the checker's recomputation of the worked date, and did NOT read the rules of A_03, the price builder or A_00 line by line. The CTO half therefore reads those three at signing (N = 4 writers, 3 rules still to be read by the signer; B_00's rule is the worker's reading, `S48_EVIDENCE.json`).

## Both branches of the producer's rule

- **If the two accounts' realized lots are right** (the worker's verdict RIGHT: no duplicate keys in the cube or the holdings, the 10-14 transaction partition rewrite removed 2,921 rows that all survive in other partitions, the 78 re-priced rows are `linear_interpolation` on both sides): the rise is the nightly rule applied to changed inputs and nothing is rolled back.
- **If they are wrong** (a restated source nobody ordered): the move is reversed per key by restoring the 23:15:29Z version of each object below, then the window is re-derived by the next fire. The checker's verdict is RIGHT, so this branch is stated, not taken.

## Blast radius and rollback per key

Touched by the act already done: the 15 canonical-holdings objects below (14 with a before and an after version), and the served `mix_daily_summary.json` for 14 dates. No table, no Lambda, no other object. Rollback per key is `aws s3api copy-object` of the "before" VersionId over the key, per row of this table (a CloudOps act under its own pair, not taken):

| date | version before (2026-10-16T23:15:29Z) | version after (2026-10-17T04:16:05Z) |
|---|---|---|
| 2026-09-30 | 0_po.xUHRD7Rq5dzijirzaMcbft70wnF | (none) |
| 2026-10-01 | gK6wE3FNua_E2yZfPOUsBVLTGWe5UCkw | QQXsJBKzu44JaRVdabbU7D4sXxGfDJEO |
| 2026-10-02 | wtAhSnBVfcTlrV.Y6Ml3Jh.ggcyBgQkf | aMEdNa9yQApdT4HVnPu3NLMqQ3WB1AV0 |
| 2026-10-03 | 2ul.EMCChf744o_3Yqth9PHLHEFtN13m | nM1S0ZnWmxCsWwvNGyHyXhISMRFgJZiA |
| 2026-10-04 | 6cqBjVGgzk6NEDmoe0AjbEK1aw4BIZoD | vVPXZjcpmCs2pmrK8wrLUgs84c5o_JcB |
| 2026-10-05 | 6cZGJKLgszB25HS87bGTpmqnYSPL91U0 | MPkQQMxbD1hHT_qMhRxfhO.y59.1y5q3 |
| 2026-10-06 | X1JNjNynuzFLRB91MErRPUfy9M2bpmrO | 81a9N4jBUShVFQsgy.nWB5.sJkECsrLC |
| 2026-10-07 | sgAy8VVVuyIDyTv7wDpBFn.pk5Fpk3YM | _7eexKPV8AdyezyKVS24JQCHr7cxW1HA |
| 2026-10-08 | KkC1BdGWoyB3DRDOq2tXKxbNlGmbVoML | pMHzxQin1MyoGgy6aAoDklexI.NN5EiL |
| 2026-10-09 | 1n7BcIHi6kF5oTl2x3L_0FJTnPtqIH2Z | 6ifYA5sO0sFgmBP1TnaGleGvrn3th8zW |
| 2026-10-10 | q.6aWD43IViX935xhWvW9yk_2kv8v8Le | tzYOEeMkW95XnYwfs0J_a3NU5Hxkjx02 |
| 2026-10-11 | 2UvhThWL4BFonU__JLIy_yuBdsHaPqIl | rY_z584ryb33R845uoZ0zf9NK1cNsJ.L |
| 2026-10-12 | OiJptpAgjssTZp4YByiBE5N3Apc0NZiB | RkleuntTHLvtwWEhbpE2_COFD_0wL1XG |
| 2026-10-13 | LIAkXkK8Xbcn4WtuNyMX7FHq9D4piAx3 | i4EgmgFe8AtbxHQYsLwNYNiUksUrcNz9 |
| 2026-10-14 | lKA0CR43plBVgDAH7nYNFP1UKBI3.x_v | SVGAmTUoMW9ivopsINhed89h3oNCqnkE |
| 2026-10-15 | (none: first written 04:16Z) | VHMctuyKEiyryO19VnMV0fy.Qrvm7r.V |

## COO half -- SIGNED

`2.0.0_SA_COO~M1`, 2026-10-17 ~08:4xZ, on the evidence above. The move is recorded as RIGHT and as served. No act is authorized or taken by this file. Condition: the CTO half reads the three upstream rules named above.

## CTO half -- PENDING

`1.0.0_SA_CTO~DELL1` signs (or refuses) here. On SIGNED, this seat files the disarm row for `MDPF_SECCLASS-D1-S48` citing this file.
