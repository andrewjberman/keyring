# AMGT_RESAPP round 65 -- `AMGT-ao-2` never-widen pair, CTO half (the title-case redeploy at 9a8cbd2c97)

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-03 ~18:2xZ.
**COO half:** `deliverables/2.0.0_SA_COO~Z/round65/NEVER_WIDEN_HALF_COO_AO2.md` @2ec3428fb8 (msg 28933).
**Executor:** `0.7.0_AE_CloudOps~A`.
**Carries:** AMGT-ao-1 (drained @9f8f4ee4b6), this seat's round-64 ruling 1 (@504827836c).

## What I read

- **The act:** one upload plus one code-only `safe-apply` at 9a8cbd2c97. Memory stays 1769.
- **The base and rollback:** CodeSha256 `KQSA62c3...` and VersionId `.xFOZLD1X0znp_5COtZvp3UgWTBrw19p`. The base matches the round-64
  leg-2 close @9b94636a21.
- **Drift:** HEAD equals 9a8cbd2c97 on both packaged files (`git diff --stat` empty). Source diff since leg 2's 43711514cc: exactly
  `scoped_amgt.py` and `publication_gold.py` among packaged files (plus 2 test files), which agrees with CONTENT-DIFF 355 / 353 / 2 / 0 / 0.
- **`scoped_amgt.py`, ao-1, read:**
  - Only an ALL-CAPS name is re-cased; a mixed-case name is served unchanged.
  - 36 declared words stay upper: issuer initialisms and legal forms. Their source is named in `DISPLAY_NAME_ACRONYMS_SOURCE` (the
    r33 universe's company field plus the served names).
  - The legal forms Inc / Corp / Co / Ltd / SpA / Oyj take their conventional case.
  - 5 cut names (28-character width) take a full name, each with its estate source cited (r33 universe company field, or the
    classifications table `name`). No vendor call is made.
  - `test_display_name_case.py` + `test_model_block_names.py` were run by this seat: 22 passed.
- **`publication_gold.py`, COO~H's quarantine release (Andrew-direct ~17:3xZ), read by this seat with an AST census:**
  - The `QUARANTINED_PUBLISHERS` / `is_quarantined` / `GRADED_PUBLISHERS` readers sit in exactly 9 functions: `run_record_spans`,
    `publisher_coverage`, `daily_rows`, `_iter_all_listing_hits`, `_without_quarantined_jobs`, `build_daily`,
    `_iter_latest_articles`, `build_mention` and `build_event`. All 9 are builders.
  - The route-reached functions (`_day_of`, `_baseline`, `_latest_gold_snapshot_rows_cached`, `_event_id`) call none of them.
  - 0 hits for either symbol in `lib/research/api` or `timeline_api.py`.
  - **No served effect through this function**, as the half says.
- **Writers of the served property** (`display_name` on every route): 1, `_clean_display_name` in this function.

## Both branches (as the half states)

| check | if the act holds | if it does not |
|---|---|---|
| r65 c17 | 0 of 94 and 0 of 95 all-caps names; "Mitsubishi UFJ Financial Group" on both routes | ROLLBACK |
| r64 c12 | one name per security, unchanged | ROLLBACK |
| r64 c9, c10, c11, c13, c14 | unchanged YES | any move means ROLLBACK |
| covered keys' overlay, thesis, peers, timeline, collected/chatter | 200 | a non-200 means ROLLBACK |

## Conditions

1. **The build-time content diff equals the two files,** or STOP. The live base is re-read before the build.
2. **Post-act reads on the DEPLOYED function:** CodeSha256 off `KQSA62c3...`, memory 1769, and c17 printed with its denominators
   (all-caps count per route, plus the 5 cut names as served).
3. **No data-engineering operation** (collector, schedule, gold write) is in the act. That is Andrew's ~17:3xZ word, and the half's
   own STOP.
4. **NEVER-2:** one entry, opened before the upload and closed after the reads.

**CTO HALF: SIGNED** for ao-2: one upload plus one code-only `safe-apply` at 9a8cbd2c97 (or a descendant with an equal content
diff), memory unchanged at 1769, with the VersionId `.xFOZLD1X...` rollback.
