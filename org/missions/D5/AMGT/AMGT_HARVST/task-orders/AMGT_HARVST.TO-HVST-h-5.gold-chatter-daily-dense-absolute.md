# AMGT_HARVST task order -- `HVST-h-5` -- H5: gold `chatter_daily`, one row per (security, UTC day), DENSE from 2026-01-01 with a zero row for an empty day, ABSOLUTE figures only, placed on the day by `published_utc` alone, rebuildable from silver

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-h-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~5</issued_to>
<issued_by>2.0.0_SA_COO~Y</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- 0 armed gates on any harvest surface (C1=23 C2=7 C3=12 C4=21 C5=334); a gold snapshot at a new prefix is not a deploy and nothing reads it yet.
comp-iam: RUN at L5 on the DESIRED plane only; the S3 write under amgt/harvest/gold/ is measured by AC4's own conditional PUT.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification, not a produced artifact.
</preflight>

**You are `0.9.0_WK_AMGT_HARVST~5`.** Work ONLY in the worktree whose absolute path is in your spawn prompt.
- **Your first act** prints `git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel`, and tests that `org/`,
  `.tools/`, every EXISTING path in section 3, and `lib/research/harvest/tests/test_publication_gold_mention.py` exist.
  - That last file is the predecessor's. If it is absent, STOP with a BLOCKING row.
- Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_HARVST~5;`.
- **NEVER RUN AN INSTALL. NEVER CALL A PUBLISHER.** AWS is allowed only as S3 reads of `opal-data-harvest`, and
  conditional writes under `amgt/harvest/gold/`.

## 1. THE CELL, inlined in full -- `HVST-h-5` (manifest row H5; outcomes FWD-5, FWD-7, FWD-9)

**The contract, verbatim** (PRD v0.2 @9102ccfe81, `C-HV-DAILY-DENSE`):
- The gold `chatter_daily` table has one row per (security, UTC day), at
  `s3://opal-data-harvest/amgt/harvest/gold/chatter_daily/date=2026-09-22` (builder output).
- The series is DENSE from **2026-01-01 for every security**, the backfill floor. An empty day is a zero row.
- It stores ABSOLUTE figures only:
  - `articles_total` and the tier counts;
  - `mention_score` (the sum of weights) and `mention_count_total`;
  - `publishers_distinct`;
  - `trailing_7d_sum` and `trailing_30d_sum`;
  - `baseline_30d_sum` and `baseline_30d_days` (fewer than 30 days flags a short baseline);
  - `cumulative_ytd`;
  - `first_published_utc` and `last_published_utc`;
  - `data_status` (`COMPLETE | PARTIAL | DENIED`), so a quiet day is never a broken read.
- `published_utc` is the only clock that places an article on a day.
- **Relative figures -- the breakout ratio, z-score and any 0-100 normalisation -- are computed at SERVE time**, never
  stored.

**And `C-HV-ABSOLUTE-ONLY`, `C-HV-GOLD-REBUILDABLE` and `C-HV-KEY`**, as the predecessor order quoted them: no stored
ratio, share, z-score or normalised score; a rebuild from the same silver gives identical rows; every row carries
`security_key` and, where the crosswalk holds one, `composite_figi`.

**The outcome bars this cell serves:**
- **FWD-9 (the gold half):** *"every day from 2026-01-01 has a row on the daily series"* for Lenovo.
- **FWD-5 and FWD-7:** this table is what the timeline and the chatter ranks read.

**THE STATE you start from** (read at your branch HEAD):
- `lib/research/harvest/publication_gold.py` (by `HVST-h-4`) holds `mention_rows`, `WEIGHTS`, `write_gold` and a
  `build-mention` CLI. The `article_security_mention` snapshot is in `opal-data-harvest` under
  `amgt/harvest/gold/article_security_mention/`.
- Each gold table's `date=` partition is the BUILD date, taken as a full snapshot. **Read the NEWEST `date=` and the
  newest part in it.**
- The retrieval spans per (security, publisher) are in silver `listing_hit` (`search_page`, `fetched_at`, and the hits'
  published dates) and in `HVST-h-10`'s `RUN_REPORT.md` (each publisher's status and stop reason).

**RULED -- what you build** (extending `publication_gold.py`, and never editing `HVST-h-4`'s functions' behaviour):
1. **`daily_rows(mention_rows, securities, start=date(2026,1,1), end=<as_of>, coverage=...)`** is PURE and returns
   exactly one row per (security, day) for every day from `start` through `end` inclusive:
   - `articles_total` counts distinct articles; the tier counts are `tier_a`..`tier_d`.
   - `mention_score` = the sum of `signal_weight`; `mention_count_total` = the sum of `mention_count`.
   - `publishers_distinct` counts distinct publishers.
   - `trailing_7d_sum` and `trailing_30d_sum` are the `mention_score` over the 7 and 30 days ENDING on the day,
     inclusive, floored at `start`.
   - `baseline_30d_sum` is the `mention_score` over the 30 days BEFORE the trailing-7 window. `baseline_30d_days` is
     how many of those days fall on or after `start`.
   - `cumulative_ytd` is the `mention_score` from January 1 of the day's year through the day.
   - `first_published_utc` and `last_published_utc` are None on a zero day.
   - `security_key`, and `composite_figi` where held.
   - `data_status`, per (security, day):
     - `COMPLETE`: every enabled publisher's retrieval span for that security covers the day;
     - `PARTIAL`: some do, but not all;
     - `DENIED`: none do.
     A publisher's span is from the oldest published date its listings reached for the security (or the bound it
     stopped at) through its fetch time. A publisher whose run status was not a success covers no day. `coverage` is
     that computed map.
2. **A CLI `build-daily --securities-json FILE --as-of YYYY-MM-DD`** reads the newest mention snapshot and silver
   `listing_hit`, writes a `chatter_daily` snapshot through `write_gold`, and prints
   `{"securities", "days", "rows", "rows_per_security", "key"}`.
3. **New test file `lib/research/harvest/tests/test_publication_gold_daily.py`.** Exactly ten arms:
   - `test_dense_zero_rows_for_empty_days`
   - `test_row_count_is_days_times_securities`
   - `test_published_utc_places_the_day` (an article fetched on a later day lands on its published day)
   - `test_offset_timestamp_lands_on_utc_day`
   - `test_trailing_sums_inclusive`
   - `test_baseline_short_at_start`
   - `test_cumulative_ytd`
   - `test_absolute_only_columns` (no column name contains ratio, share, pct, norm, z_ or zscore, and every numeric
     column is a count or a sum of weights)
   - `test_data_status_complete_partial_denied`
   - `test_rebuild_identical`

**What this cell does NOT change:**
- `HVST-h-4`'s functions, and the mention snapshot;
- silver;
- `store.py`;
- the chatter axis;
- any served object.

## 2. WHERE THIS CAME FROM
Round 1, decomposition v1.0 @9fbf337a74, chain A position 7 of 9. After `HVST-h-4`. `HVST-h-6` (events) and `HVST-h-7`
(the projection) read your table.

## 3. SURFACES -- what you may read and write

<paths>
lib/research/harvest/publication_gold.py
lib/research/harvest/tests/test_publication_gold_daily.py
lib/research/harvest/tests/test_publication_gold_mention.py
lib/research/harvest/store.py
lib/research/harvest/tests/test_store.py
lib/research/identity/crosswalk.py
lib/opal_data_harvest/silver_from_bronze.py
lib/opal_data_harvest/config.json
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~10/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~4/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~5/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-h-5.gold-chatter-daily-dense-absolute.md
</paths>

- **Only `publication_gold.py` and your new test file may change.** AC3 fails otherwise.
- Scratch goes in `<your worktree>/.scratch/hv5/`.
- **Committing:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_HARVST~5 <0.9.0_WK_AMGT_HARVST~5@opal.agent>" -F <msgfile> -- <paths>`.

## 4. BOUNDS
- **The code and tests come first**; the live build after.
- **Pure ASCII.** A refused PUT is a BLOCKING row.
- **Surprise rows:** `AMGT_HARVST-Z-W5-S<k>`, with `disarm_owner` `2.0.0_SA_COO~Y`.

## 5. PROOF OF SPEC (each invocation LITERAL; timeout 600)

Copy `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~4/securities.json` (`HVST-h-4`'s list: the five
pilots plus Lenovo) byte for byte to `.scratch/hv5/securities.json`. If it is absent, STOP with a BLOCKING row.

Write `.scratch/hv5/check.py`. It reads the snapshot key AC4 printed, and prints:
- `lenovo_rows <n> expected_days <d> first <date> last <date> missing_days <m>`;
- `rebuild_symmetric_difference <x>` (recomputing `daily_rows` from the same inputs, excluding only `run_stamp`);
- `banned_columns <list>`.

<proof_of_spec>
  <criterion id="AC0" cell_refs="HVST-h-5"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/harvest/tests/test_publication_gold_mention.py -q --color=no -p no:cacheprovider 2>&1 | tail -1</invocation><expect>BEFORE any edit: "12 passed" (the predecessor's bar)</expect></criterion>
  <criterion id="AC1" cell_refs="HVST-h-5"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/harvest/tests/test_publication_gold_daily.py -v --color=no -p no:cacheprovider 2>&1 | tail -14</invocation><expect>"10 passed" and no "failed" -- the ten arms named in section 1 item 3</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-h-5"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/harvest/tests/test_publication_gold_mention.py -q --color=no -p no:cacheprovider 2>&1 | tail -1</invocation><expect>"12 passed" and no "failed" -- HVST-h-4's behaviour unchanged</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-h-5"><invocation>cd "$(git rev-parse --show-toplevel)" && git diff --name-only "$(git merge-base HEAD SITEZ)" HEAD -- lib && git status --porcelain -- lib && echo "--- end"</invocation><expect>before "--- end", ONLY lib/research/harvest/publication_gold.py and lib/research/harvest/tests/test_publication_gold_daily.py, and nothing else under lib</expect></criterion>
  <criterion id="AC4" cell_refs="HVST-h-5"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m lib.research.harvest.publication_gold build-daily --securities-json .scratch/hv5/securities.json --as-of "$(date -u +%Y-%m-%d)"</invocation><expect>a JSON line whose rows equal securities times days, with a key beginning "amgt/harvest/gold/chatter_daily/date="</expect></criterion>
  <criterion id="AC5" cell_refs="HVST-h-5"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/hv5/check.py</invocation><expect>"missing_days 0" with first 2026-01-01 and lenovo_rows equal to expected_days; "rebuild_symmetric_difference 0"; "banned_columns []" -- dense from the floor, rebuildable, absolute only (FWD-9's gold half)</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR.** No judgment criterion.

## 6. WHEN YOU ARE DONE
1. Write the instance to
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~5/AMGT_HARVST.TO-HVST-h-5.gold-chatter-daily-dense-absolute.proof_of_spec.json`.
2. Grade it with `python .tools/proof-of-spec-check.py <instance> AC0,AC1,AC2,AC3,AC4,AC5`, which must return rc 0.
3. Flip only on all PASS.
4. Commit with `--only`.
5. Report once, with Lenovo's non-zero days and the `data_status` counts.

**MUTATION DISCIPLINE:** snapshot the working-tree bytes to `.scratch/hv5/` first. Never `git checkout --`, `stash` or
`git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6):**
1. **The baseline window is defined here:** the 30 days before the trailing-7 window, so a burst is never its own
   baseline. That is a working rule the PRD leaves open, and the CTO's round analysis may amend it.
2. **`data_status` is derived from retrieval coverage, never from a count.** A zero on a covered day is a real quiet day;
   a zero on an uncovered day reads PARTIAL or DENIED.

<status>pending</status>
<round>1</round>
<slot>~5</slot>
<fabric>site-z</fabric>
