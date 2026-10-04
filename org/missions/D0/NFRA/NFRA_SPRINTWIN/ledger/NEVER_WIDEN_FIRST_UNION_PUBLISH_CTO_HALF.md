# NFRA_SPRINTWIN -- the first scheduled publish under the window + union: never-widen pair, CTO half

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-04 ~20:4xZ. **Request:** `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/NEVER_WIDEN_REQUEST_NFRA_SPRINTWIN_FIRST_UNION_PUBLISH_20261004.md`
@93151a0af8 (msg 29213). **COO half:** `2.0.0_SA_COO~H` (PRD v0.2 placement @1f344f57f4). **Candidate:** CLOUD @6c491b6e9d
(function @dc86c2b2cd).

## What I read

- **The producer's rule, from the candidate's own bytes** (`infra/aws/lambda/daily_sprint_generator/lambda_function.py`
  @6c491b6e9d, `cut_window` :435-475, `censuses` :293-311):
  - `end = min(census generated_at for the day + [limit])`, where limit is the run time on the day itself, else 16:10 ET of that day;
  - `start = prev.window_end`, or `end - 24h` with no watermark; capped at 7 days, and the uncovered span is stated;
  - a day with its own watermark reuses it.
  - Branches A (a census exists) and B (none) in the request match this rule as written.
- **The blast radius:** the keys of 2026-10-05. That is `Desktop_` and `Mobile_DAILY_REPORT_2026-10-05.html` (overwritten as today)
  plus a NEW `daily-reports/2026-10-05/watermark.json`, written last after both pages verify. QA runs write only
  `sprint/global/platinum/qa_page/` (`_home`).
- **The transition seam, measured:**
  - With no watermark, the first window starts 24h before the earliest Oct-5 census (about 19:55-20:02Z Oct 4).
  - The Oct-4 page (old image) counted only what was pushed by its fire. Origin CLOUD was `2205340103` (committed 19:29:38Z) and
    still read that at 20:1xZ.
  - `git rev-list --count --since=2026-10-04T19:55Z 2205340103` = **0**. So no commit lands in both pages: the seam's double count is
    empty in fact.
  - Unpushed Oct-4 work made before the window start is not reported by either page. That is the old regime's last loss, not a
    new one.
- **The rollback target is held:** ECR `daily-sprint-generator` holds 5 images, and `446603c3...` is the newest (tag `latest`).
  `get-function` ResolvedImageUri = `@sha256:446603c3b130...`. Under keep-last-5, the 5th new push evicts it.
- **Writers of the served pages: 2, rules read 2.**
  1. This function, under the new rule.
  2. A seat running `/daily-sprint` locally. Its step 7 publishes both pages to the same keys over its own window
     (`git log --all --since=<DAY>T00:00Z`, pushed refs).
  - **Writer 2's rule now differs from writer 1's.** A local publish of 2026-10-05 after the fire would replace the union page with
    a pushed-only day population, under a watermark that no longer describes it.

## Conditions

1. **Writer 2 is covered before the fire, by EITHER:**
   - (a) the C-WINDOW local half landing: `/daily-sprint` passes the day's served watermark pair, as the PRD requires; OR
   - (b) the builder relaying to `0.0.0_AB_MSTR` and `0.0.0_AB_MSTR~Z`, before 2026-10-05 19:30Z: "no local `/daily-sprint`
     publish of a day that carries a served watermark until the local half lands".
   - `stitch_daily_report.py` (edit in place, same population) is not affected.
2. **The rollback target stays held.** The builder pushes at most 4 new images before the fire. It re-reads `describe-images` for
   `446603c3` before the move and again before 19:30Z.
3. **No served invoke before both halves are signed.** Until then, only `{"qa": true}` runs.
4. The request's own clause stands: if either half is unsigned at 2026-10-05 19:30Z, the image rolls back to `446603c3` before the
   20:10Z fire.
5. One NEVER-2 entry covers the image move and the policy change (C-SERVED). It is opened before the move.

**CTO HALF: SIGNED** for the first scheduled publish under the window + union (2026-10-05 20:10Z), under conditions 1-5.

## ADDENDUM A -- the served re-run of 2026-10-04 (extension, 1.0.0_SA_CTO~Z, 2026-10-04 ~21:4xZ)

**Request:** the same file @55bb66278d, section ADDENDUM A (msg 29254). **Authority:** Andrew-direct ~21:3xZ, record
`org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_DIRECT_20261004_213xZ_OPEN_CALLS_ALL_RECS_APPROVED_RERUN_DAILY_SPRINT_ONCE_LAPTOP_ONBOARD.md`
@b7f2fb4dc7.

**What I read:**
- The three keys: the 10-03 seed watermark (NEW, written by the builder), the two 10-04 pages (overwritten) and the 10-04 watermark
  (NEW, written by the function last). The watermark keys now have 2 writers: the function, and the builder's one seed.
- The rule (`cut_window` @dc86c2b2cd): with no 10-04 watermark, prev = the seed, so start = 2026-10-03T22:16:00Z and end = the
  earliest 10-04 census. The 10-05 fire then starts at the 10-04 end, which is contiguous.
- **The seam, measured on site Z:** `git log --all --no-merges` with commit time in [2026-10-03T22:15:00Z, 22:16:00Z) = **0**. The
  neighbours are 22:14:27Z and 22:14:44Z (inside the 10-03 page) and 22:16:20Z (in the new window). Positive control: 40 commits in
  [22:00Z, 23:00Z).

**Conditions (the original 1-5 carry):**
- A1. The seed is written with read-back BEFORE the invoke. It is the only builder-written watermark.
- A2. At invoke time, the union (pushed refs plus every device census in the window) has 0 rows with commit time in
  [2026-10-03T22:15:00Z, 22:16:00Z). The laptop's refs are not visible from site Z. A non-zero is a STOP and a re-seed.
- A3. The QA trace and both device censuses come first, as the addendum orders. ONE served invoke of `{"date": "2026-10-04"}`, once.
- A4. **Both invoke-time branches are covered,** read from the same rule (`limit` in `cut_window`):
  - invoked before 2026-10-05T04:00Z (10-04 is still the New York day): end = the earliest 10-04 census, capped at the run;
  - invoked after it: end = min(the 10-04 censuses, 2026-10-04T20:10Z), and the rest falls contiguously into 10-05. This matches
    `2.0.0_SA_COO~H`'s extension @7fa231405f.
  - A 2026-10-03 invoke on the new image is not covered.

**CTO HALF: EXTENDED** to Addendum A under A1-A3 and the original conditions 1-5.
