# ADVI_COTBKF -- L9 grade of CB38al1-AC2 on the SERVED Cottonwood account_return_daily mint

**Grader:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T07:51:03Z. Row ADVI_COTBKF-D2-S97.
**Input:** `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_MINT_ARD_COTTONWOOD_DRAIN_END_20261011.md @850013eb11 (msg 4420)`. This seat read the served objects itself; no client figure or account id is written here.

| limb of CB38al1-AC2 | verdict | this seat's read of the served bytes |
|---|---|---|
| every row's method claim is truthful (never the custodian method) | **MET** | Method row 3's served manifest: `method_version` 3, positions-based value basis, flow convention END, 5 thresholds and the tie-out each claimed `absent`; the word custodian appears nowhere. Three day manifests (2013-04-03, 2018-07-09, 2026-06-22): `method_version` 3, the C-METHOD formula, `positions_x_as_traded_close`, `net_of_fees`, `as_traded`; no custodian text. Two day files (465 rows): every row carries `method_version` 3; `return_basis` is TWR on the 28 measured rows and NOT_MEASURABLE on the 437 blank ones |
| the two exceptions read as blanks with reasons, never zeros | **MET** | In the two day files, 437 of 437 blank rows carry a null return and 0 carry a zero. The served reasons sidecar hashes `589f72cc...`, equal to the manifest, and holds 1,584,413 rows: the two exceptions read 988 `HELD_SOURCE_UNDER_REVIEW` and 110 `REGRESSED_UNDER_AS_TRADED`, the counts the manifest states |
| the producer is unedited | **MET** | The build's worker has 0 commits on `account_return_daily.py`; the adapter imports it |

**Verdict: CB38al1-AC2 MET.**

This seat also recomputed the content hash of one served day with the adapter's own `content_hash`: it equals the manifest's.

## Three things a reader of this table should know

1. **94 of every 100 rows are blank.** 1,584,413 of 1,691,729 account-days carry no return, 1,558,187 of them for an unpriced holding.
   The table is truthful and mostly empty. Whether it is useful to its first reader (IRPT_DASHBD's hop for FWD-12) is that reader's
   test; the packet claims no outcome REALIZED, which is right.
2. **The manifest's `sha256` and `bytes` are the local build file's, not the served object's.** On the 2 days sampled the served
   file's hash and size differ (the mint rewrites each file through the producer). Only `content_sha256` describes what is served.
   A consumer that checks a download against `sha256` will refuse a good file.
3. **Method row 3 states `income_basis: cash_when_received` with no limit.** It is true of every measured row today, because none
   holds a bond (round 57). The served row does not say so; the limit lives in the pair.

## Not read by this seat

The object count under the three prefixes and the object versions (the applier's). 2 of 3,325 day files and 3 of 3,325 day
manifests were read; the issuer's verify line covers all 3,325 by content hash.
