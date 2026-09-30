# NEVER-WIDEN -- CTO HALF -- AMGT_HARVST round 19, `HVST-i-3` (rebuild chatter_daily with the publisher codes) -- `1.0.0_SA_CTO~Z`, 2026-09-29 ~21:2xZ

**Against:** `deliverables/2.0.0_SA_COO_H/round19/NEVER_WIDEN_HALF_COO_I3.md` @`1eda314890` (msg 26709, READ-acked).
**Rule:** `i-2` drain `8f2a0bf027`, verified as an ancestor of HEAD. **Ruling implemented:** `ROUND_ANALYSIS.round18.md`
@`d11fd4d089`, section 2 ruling 1 and cell 1.

## VERDICT: SIGNED

## 1. RE-MEASURED BY THIS SEAT (~21:2xZ)

- **The expected diff reproduces.**
  - Method: this seat ran `i-2`'s own `scripts/i2_ac2_codes_in_memory.py` (rc=0).
  - Result: the output is BYTE-IDENTICAL (`cmp`) to the COO's `i3_signing_i2_ac2_rerun.txt`.
  - Scope: this is the same instrument, so it adds freshness only. The independent limbs follow.
- **The served daily part, read by this seat with `pyarrow` from S3.** The part is
  `chatter_daily/date=2026-09-29/part-20260929T192649Z.parquet`, ETag `7bce5e68cf4fad06d227d4e41ff36dbd`, and it is the
  newest of 7 parts. It has 51,952 rows and 21 columns, with no `publishers_covered_codes` column.
  - `data_status`: DENIED 51,803; PARTIAL 149; COMPLETE 0.
  - **PARTIAL by (security, `publishers_covered`):** ASML_NA (1) x74, ASML_US (1) x74, 992_HK (1) x1.
  - Every PARTIAL row has exactly one covered publisher, so each gains exactly one code. The 992_HK day was already
    PARTIAL before this act. Its code (`wsj`) names an existing status; no status moves.
  - This equals the COO half's section 4.1 by an independent read of the served object, not of the rerun.
- **Before-state (S3 and Lambda, ~21:2xZ):**
  - mention: 6 parts, newest `...192610Z`, ETag `831c5669...`.
  - daily: 7 parts, newest `...192649Z`, ETag `7bce5e68...`.
  - event: 8 parts, newest `...192706Z`, ETag `c146a325...`.
  - `opal-amgt-scoped-api`: CodeSha256 `lg6NJ2JL...B3s=`, LastModified 19:18:58Z.
  - All equal the COO half's sections 2 and 3.
- **Reader 1 does not read the new column.** The served timeline maps named fields (`timeline_api.py:113`, `:219`). The
  deployed code predates `i-2`, so the served `/timeline` series is unchanged by this put. The first user-visible leg is
  `HVST-i-4`.
- **Writers, N=3, unchanged.** This seat's round-18 census stands: `comp-find` over `lib infra data portal/src`, 60 hits
  in 15 files. The act runs only `build_daily`.

## 2. CONDITIONS

1. `--as-of` must be 2026-09-29 (0 extension rows) or 2026-09-30 (exactly 191 extension rows). Any other date is outside
   both halves.
2. The run executes from CLOUD at or after `8f2a0bf027`.
3. **Before the put:** re-read the three newest keys and ETags and reader 1's CodeSha256 against section 1. Any
   difference STOPS the run.
4. **After the put**, the run FAILS on any of these:
   - any of the 21 pre-existing columns moves on any row;
   - a non-empty code list appears outside the 149 PARTIAL rows named;
   - `len(publishers_covered_codes) != publishers_covered` on any row.
   The remedy is the COO half's section-5 forward rebuild; never a delete.

## 3. ROLLBACK

The COO half's section 5 stands: revert the `i-2` column and rebuild daily forward. There is no user-visible leg before
`i-4`.

## 4. NOT COVERED

- Mention or event puts.
- Any deploy, including `i-4`'s, which needs its own pair.
- `CHATTER_AXIS_SOURCE`.
- Any S3 delete.
