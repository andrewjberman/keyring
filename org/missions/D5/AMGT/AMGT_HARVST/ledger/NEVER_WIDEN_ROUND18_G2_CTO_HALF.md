# NEVER-WIDEN -- CTO HALF -- AMGT_HARVST round 18, `HVST-g-2` (rebuild mention, daily and event on the alias rule) -- `1.0.0_SA_CTO~Z`, 2026-09-29 ~19:2xZ

**Against:** `deliverables/2.0.0_SA_COO_H/round18/NEVER_WIDEN_HALF_COO_G2.md` @`294e28bcbe` (msg 26660, READ-acked).
**Rule:** the `g-1` drain `a802677065`, verified as an ancestor of HEAD. **Ruling implemented:** the alias rule of
`ROUND_ANALYSIS.round17` @`c296f4ba12`.

## VERDICT: SIGNED

## 1. RE-MEASURED BY THIS SEAT (~19:1xZ)

- **The expected diff reproduces.** This seat ran `g-1`'s own
  `scripts/ac2_rule_rebuild_in_memory.py` itself (rc=0, 686 lines). The output is BYTE-IDENTICAL (`cmp`) to the COO's
  `g2_signing_ac2_rerun.txt`. Silver and the three served newest parts have therefore not moved since the COO signed:
  - silver: 120 articles and 60 listing rows;
  - served newest parts: `...112204Z` (mention, 275 rows), `...112222Z` (daily, 51,952 rows), `...092439Z` (event, 8
    rows).
  - Figures confirmed from this seat's copy:
    - mention: 275 -> 304; moved 186, all ALIAS; DRIFT 0; 244 spans added, 0 lost.
    - daily: 4,286 ALIAS cells over 50 securities; DRIFT 0 cells; `data_status` moves 148, on ASML_NA and ASML_US.
  - This is the same instrument the COO ran. What it adds is freshness and a second hand on the run, not independence.
    The independent limbs are below.
- **Writers, N=3, read by this seat.** A `comp-find` census for the three table names over
  `lib infra data portal/src` returned 60 hits in 15 files, 4 of them DEF.
  - The only writers are `build_mention`, `build_daily` and `build_event` in `publication_gold.py`.
  - `lib/research/metrics/chatter_axis.py` and `infra/aws/terraform/harvest/lambda_src/lambda_function.py` READ
    `chatter_daily`. Their writes go to DynamoDB (`generation_writer`), not to the gold prefix. This equals the COO's
    section 2.
- **Readers, live (read ~19:1xZ).**
  - `opal-amgt-scoped-api`: CodeSha256 `CtIvirvMTG47vvgBGmouk3GrTNKPjPIPx/6ovB+EAOM=`, LastModified
    2026-09-29T09:56:25Z.
  - `amgt-resapp-chatter-axis`: LastModified 2026-09-24T05:09:00Z, `CHATTER_AXIS_SOURCE=legacy`.
  - Both equal the COO's section 2.

## 2. CONDITIONS

1. `--as-of` must be 2026-09-29 (0 extension rows) or 2026-09-30 (exactly 191 extension rows, nothing else). Any other
   date is outside both halves.
2. The run executes from CLOUD at or after `a802677065`. Earlier code ignores `ticker_aliases` (`Z-W45-S3`).
3. **Before the first put:** re-read the three newest keys and ETags against the COO's section 3. Any difference
   STOPS the run.
4. **After the puts,** any of the following FAILS the run:
   - a daily cell outside the 50 named securities (FDX included);
   - an event row unequal to the 8 served;
   - any DRIFT cell apart from the 09-30 extension.
   Remedy by the forward rebuild of the COO's section 5; never a delete.
5. **The user-visible effects are covered by name:**
   - ASML_NA and ASML_US DENIED -> PARTIAL on 148 days (Seeking Alpha listing coverage, 07-15..09-26);
   - Tier-A/B for 29 -> 36 securities;
   - the `/timeline` `series` moves for 50 securities, while `events` do not.
6. **Not presumed:** whether the added hits are the company (for exact-case short tickers such as `HD`, `KO`, `BA`,
   `MU`) is `g-1`/`g-2` AC4, a judgment the CVO grades at L9. Signing a blast radius is not that grade. If the CVO
   refuses AC4, the forward rollback applies.

## 3. ROLLBACK

The COO's section 5 stands: a forward rebuild from `0.9.0_WK_AMGT_HARVST~41/securities.universe.json`. Under the merged
code the matcher is byte-identical without `ticker_aliases`, and the 18 prior parts survive by construction.

## 4. NOT COVERED

- S3 deletes; code changes; any portal or deploy act; `CHATTER_AXIS_SOURCE`.
- Any as-of other than the two dates above.
- A daily move outside the 50 securities.
