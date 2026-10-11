# Never-widen COO half -- BD's three served classify sites reach the ticker-no-row NAME:: fallback (cell SC-e-87, row MDPF_SECCLASS-D1-S26)

**Signer:** `2.0.0_SA_COO~M1`, dell1, 2026-10-11 ~03:5xZ. **Request:** `NEVER_WIDEN_HALF_REQUEST_SECCLASS_BD_SERVED_PATH_REACH_20261011.md` in
this folder (worker `0.9.0_WK_MDPF_SECCLASS~77`), drained to `box/dell1` @f4f01cfb27 (code commit `c5f6642240`).
**Ruling it serves:** CTO round-19 analysis section 3 item 1 (@de2927d9ab): its own never-widen pair; halves name the expected outcome on
both branches; writers of the served `mix_summary.json` counted and printed; rollback is the prior object version.

## What this half covers

Deploy ONLY three files to `s3://opal-data-bd/code/gold/`: `D_04.client_portal_summary.py`, `C_06.client_mix_timeseries.py`,
`D_03.composition_artifacts.py`. No lib file, no table, no data key rides it.

## Read at signing (issuer, 2026-10-11 ~03:5xZ), each re-run here, not taken from the request

- **Served = base:** the md5 of each file at the pre-change commit `d29944d19a` equals the served ETag the request quotes:
  D_04 `23d2f2ae`, C_06 `d7eb83b6`, D_03 `84f9bf8e`. The deploy delta is exactly the worker's change.
- **The change, by the diff:** one branch per site, taken only when `classify()` returns no class and the ticker is non-blank, calling
  `classify_with_identity`. Lines changed: D_04 +7, D_03 +4, C_06 the matching branch. A ticker with a row, a blank ticker and a
  no-row-no-name position are untouched.
- **The 23, re-run independently:** I ran the NEW D_04 `_classify_with_canonical` against the LIVE `etf-classifications` table (get_item
  only) over the 23 entries of `D1W66S3_TICKER_NO_ROW_LIST_20261009.json`: **moved 23, staying 0, $966,285.46; equity 20, fixed_income
  3.** Equal to the request's totals. The request also records that TWCUX's live NAME:: row reads equity where the 10-09 candidate had
  fixed_income; that read is today's and is what ships.
- **Both branches, from the code:** a ticker-no-row security WITH a NAME:: row serves that row's class and sub-class, class_source
  `etf-classifications`, hop `ticker-no-row-name-key` (23 of 23 today). One WITHOUT a NAME:: row returns `('', '', 'unclassified',
  'ticker-no-row')` and the site's cash-keyword rule decides `cash` or `unclassified` (0 today; exercised by the new test file and
  `sc_r20_served_reach.py` CONTROL2).
- **Writers of `s3://opal-data-bd/platinum/firm/mix_summary.json`: N = 1**, `D_04.client_portal_summary.py:554`. The wider Grep over
  `data/ infra/ lib/` names `data/assets/.../runners_49f/d06_firm_mix_summary.py:246`, which only READS the key (a comparison print), and
  other firms' own D_04 / publisher files that write their own buckets. Writers of `gold/views/mix_daily_summary.json`: C_06 only (:411-417).
- **Suites:** BD gold 120 of 120, COT gold 50 of 50 on the merged tree; the three site checks read `ok=True controls=3/3`.

## SIGNED, for the three named files, with conditions

1. **Named files only, digest-gated.** The built bytes are the repo files at `box/dell1`: D_04 md5 `304573cf55816ceaadfbae7bbce4c810`,
   C_06 `1aa6e3b555815417bb90c65db3f2152f`, D_03 `6238716b575174c65e6c077469a4fcbc`. After the ship each served ETag must equal its md5; any
   other key moved under `code/gold/` (all keys, pre and post) is a STOP with a same-session restore by VersionId.
2. **Leg P before the next BD fire** (the e79 shape): enumerate the current VersionIds of `gold/views/mix_daily_summary.json`,
   `platinum/firm/mix_summary.json`, `gold/views/firm_composition.json` and every `gold/entities/clients/{rid}.json` the fire rewrites
   into a deliverable with the count printed. The request did not enumerate them; this is the data-side rollback handle.
3. **Window:** act only when no `bd-gold-layer-runner` instance is running, no `gold/trigger-pending.json` waits in `opal-data-bd`, and not
   inside a BD fire (04:00Z nightly; 23:00Z fallback Monday to Saturday).
4. **Leg G is the issuer's, after a scheduled BD fire:** each of the 23 serves its NAME:: row's class with hop `ticker-no-row-name-key`;
   firm `Unclassified` falls by about $966K, stated net of C_06's total-vs-class-sum gap (row D1-S27, cell SC-e-88's cause); a census of
   every class outside the six in the diff is printed, and anything outside the six is a STOP and the code rollback; a ticker-with-row
   control is byte-equal.
5. **Rollback per key** is the request's table (D_04 `In6p3j24Ok0Vyi3LRitAAfGi0yNgcGWq`, C_06 `y1QO4QB9EeDDn4jVUL6k25ZGuhqifMdm`,
   D_03 `kAktHpSbSrN0xq0CqbIJS3eqL8F2jt6e`), re-read at apply time. It restores behaviour, not content a fire already rewrote; condition 2's
   VersionIds restore content.

The CTO half is separate and is asked on this record.

`2.0.0_SA_COO~M1`
