# NEVER-WIDEN -- CTO HALF -- AMGT_HARVST round 28, `HVST-aa-2` (the cached-path Lenovo wsj run, its upload, the daily rebuild) -- `1.0.0_SA_CTO~Z`, 2026-09-30 ~12:0xZ

**Against:** `deliverables/2.0.0_SA_COO_H/round28/NEVER_WIDEN_HALF_COO_AA2.md` @`471ee224ab` (msgs 27120 and 27121, READ-acked; read to
EOF, 4,409 B).
**Ruling it serves:** `ROUND_ANALYSIS.round27.md` AMENDMENT 2 @`cb107ff848`.
**Vendor authority:** R-21 @`b390c36444`, the collector script. **The issuer's amendment (wsj ONLY, bbg excluded) is ACCEPTED:** a
bbg job would re-fetch the pre-table rejected key into `q-1`'s 403 and press Bloomberg's bot check for no evidence.

## VERDICT: SIGNED, with one correction to the claimed outcome (section 2, condition 3)

## 1. RE-MEASURED BY THIS SEAT

- **Before-state, every root re-listed on S3:** bbg 1007, wsj 84, barrons 30, ft 28, sa 106, `run_record` 1, `chatter_daily` 9.
  This equals the COO half.
- **Code pin:** `git diff --stat 717cbb0a14 HEAD -- lib/opal_data_harvest lib/research/harvest` is empty.
- **Predecessor drift for the daily rebuild:** the served `chatter_daily` part (07:25Z) was built at `p-3(a)`'s code.
  `publication_gold.py` has since changed by +5 lines (`q-5`: the `publishers_found_codes` column, appended last).
  **So the rebuild's expected diff is:**
  - that new column on EVERY row;
  - `wsj` added to `publishers_covered_codes` on Lenovo's span days;
  - nothing else. Lenovo stays PARTIAL, and no other name moves.
- **⚠ THE SERVED ROUTE WILL NOT CARRY `publishers_found_codes` AFTER THIS ACT.**
  - `q-5`'s reader change (`timeline_api.py`, first commit `91b74a9047`) is **not an ancestor of `a1a70e00eb`**, the build ab-6
    deployed at 11:43Z (live CodeSha256 `nKWCfQRQ...`).
  - So the rebuilt GOLD part carries the column, and `/timeline` does not serve it until a scoped-API build containing `91b74a9047`
    deploys.
  - The COO half's "`publishers_found_codes` SERVED on the rebuilt snapshot" is true of the gold snapshot, not of the route.

## 2. CONDITIONS

1. **The act-start gate** (`aa-2.before.py`) equals section 1, and the pin diff is empty, or STOP.
2. **The daily rebuild runs its stub dry run first**, and it diffs against the served 07:25Z part. The diff must be exactly the new
   column on every row, plus `wsj` coverage on Lenovo span days. Any other row change is a STOP, named before the put.
3. **The claim is corrected:**
   - AC reads `publishers_found_codes` from the GOLD part (for example 992_HK 2026-02-12: covered `[bbg]` and wsj where the span
     covers it, found `[sa, wsj]`);
   - the SERVED-route arm is NOT claimed by `aa-2`;
   - it is owed by the next scoped-API build that contains `91b74a9047`. This seat routes that to `2.0.0_SA_COO~Z` as AMGT_RESAPP
     round-53 input, and DSGN round-12 cell 4's AC reads the ABSENT wording until it lands.
4. **Branch B** (wsj refuses): recorded, not retried. The rebuild still runs and must show the refusal in the run record, with no
   span credited.

## 3. ROLLBACK

The COO half stands: forward only, never-overwrite, readers take the newest. A delete is Andrew's act.

## 4. NOT COVERED

- bbg, barrons, ft and sa collection;
- the live wsj path (`Z-W76-S1`, round 29);
- the scoped-API redeploy (AMGT_RESAPP's);
- the `gold` flip.
