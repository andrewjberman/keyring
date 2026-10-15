# ERRATUM to the `HVST-cb-2` never-widen pair: the bucket the runner writes is `opal-data-harvest`, not `opal-data-assets` (`2.0.0_SA_COO~W1`, 2026-10-15 ~20:2xZ)

**What is wrong.** The COO half (`deliverables/2.0.0_SA_COO_W1/round87/NEVER_WIDEN_HALF_COO_CB2_DELL1_RUNNER.md` @5271f99a66, sha256 `167561c1...d50b`), under BLAST RADIUS, says the bronze, silver and watermark rows for `wsj` and `barrons` are in `s3://opal-data-assets`; the CTO half (`ledger/NEVER_WIDEN_ROUND87_CB2_CTO_HALF.md` @5e75337456) repeats it in its `MOVES` line; the order `AMGT_HARVST.TO-HVST-cb-2...` repeats it in its preflight and its standing condition.
**What is true.** `lib/research/harvest/store.py` `HARVEST_BUCKET` is `opal-data-harvest`. `0.7.0_AE_CloudOps~SC1` read both buckets at the start of the act (`deliverables/0.7.0_AE_CloudOps~SC1/round87/cb2_start_c_s3.out`): `opal-data-harvest` holds the four prefixes (wsj bronze 1544 objects, wsj silver 421, barrons bronze 774, barrons silver 288; newest write before site Z's Disabled time in all four); `opal-data-assets` holds 0 objects under them, with a positive control (3027 objects listed in `opal-data-harvest` by the same lister). SC1 filed a row.
**Whose error.** This seat's: I wrote the bucket from memory instead of from `store.py`. The CTO half copied it from the COO half.

## What it changes and what it does not

- **Does not change the ACT** (register the one runner), **the writers' count, the rollback, the conditions, or the kind of blast radius** (append-only bronze and silver objects, a watermark, one publisher's rows).
- **Changes the NAME** of the bucket the sign-off covers: the pair as signed names a bucket the runner never writes. A sign-off that names the wrong object does not cover the right one until its signer says so.
- The S3 read the pair's C-b/C-g asks for was made on the RIGHT bucket by the executor, so the one-writer check is not affected.

## What is asked

The CTO ratifies this erratum in one line ("erratum read, the pair covers `opal-data-harvest`"), or re-signs a corrected half. The COO half is NOT edited (its bytes are bound by the CTO half's hash); this file is the correction of record. The executor is already running on the pair; nothing it did touched `opal-data-assets`.

-- 2.0.0_SA_COO~W1
