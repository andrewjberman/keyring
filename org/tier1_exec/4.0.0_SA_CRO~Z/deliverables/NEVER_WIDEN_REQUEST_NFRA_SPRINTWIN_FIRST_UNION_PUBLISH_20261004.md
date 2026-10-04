# Never-widen request -- NFRA_SPRINTWIN: the first scheduled daily-sprint publish under the window + union

**Author:** `4.0.0_SA_CRO~Z`, NFRA_SPRINTWIN's solo builder (Andrew-direct ~18:4xZ 2026-10-04,
`org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/ANDREW_DIRECT_20261004_184xZ_NFRA_SPRINTWIN_CRO_Z_BUILDS_SOLO.md`). This file is the
request; it signs nothing. **Halves owed** (PRD v0.2 seats line and C-SERVED): CTO half `1.0.0_SA_CTO~Z`; COO half `2.0.0_SA_COO~H`.
**Candidate:** CLOUD @6c491b6e9d (function @dc86c2b2cd, census scripts @493b50dde5, chart labels @608559d4fe). NOT deployed. The
deployed function runs image `sha256:446603c3b130...` (ResolvedImageUri read 2026-10-04 ~20:3xZ).

## The act

One image move on `daily-sprint-generator` (build from committed bytes, push `:latest`, `safe-apply -replace` of the function),
plus the role policy's three new grants (plan: 0 add, 1 change, 0 destroy). The tag has ONE consumer, this function. The first
SERVED effect is the next scheduled fire, 2026-10-05 20:10Z (4:10 PM ET), unless a manual `{"date": ...}` invoke runs first.

## Writers of the served property, counted

- Pages `daily-reports/<day>/{Desktop,Mobile}_DAILY_REPORT_<day>.html`: TWO writers. (1) This function, through
  `publish_daily_report.py`, on its schedule and on a manual `{"date": D}` invoke. (2) A seat running `/daily-sprint` locally
  with the same publisher. This act changes writer (1) only; writer (2)'s rule is unchanged.
- `daily-reports/<day>/watermark.json`: ONE writer, this function, NEW. Written last, after both pages verified.
- `{"qa": true}` writes ONLY `s3://opal-data-portal-v2/sprint/global/platinum/qa_page/date=<D>/` (pages, report JSON, its own
  watermark). It never touches `daily-reports/`. Rule: `lambda_function.py` `_home()` and `publish_qa()` @dc86c2b2cd.

## The blast radius, per the producer's rule (`cut_window` + `censuses` @dc86c2b2cd)

The keys of 2026-10-05: its two pages (overwritten as today) and one new watermark. Nothing else in the bucket.
- **Branch A, at least one device census dated 2026-10-05 exists.** window_end = the earliest such `generated_at` (never later
  than the run). window_start = run's window_end minus 24 h (no served watermark exists yet). The population = pushed history
  in [start, end) UNION every device census row in that window not already pushed, by sha. The page gains unpushed commits;
  its source line names each reporting device, its census time and the unpushed count, and names a missing device.
- **Branch B, no device census for the day.** window_end = the run time; window_start = 24 h earlier; the population is pushed
  history only (today's population, over a 24-hour window instead of 00:00 ET to now); the source line names both devices
  as not reporting.
- Both branches: the area chart's 48 bins run from the window start; the hour labels read from it (@608559d4fe).
- A dated manual re-run of a day that has a watermark reuses it; of a day that has none, it caps window_end at 16:10 ET of
  that day. That is the manual path's reachable state, covered here.

## Rollback, per key

- Pages: re-point the function to `sha256:446603c3...` (kept by keep-last-5) with `safe-apply -replace`, then invoke
  `{"date": "2026-10-05"}`; the old image re-publishes both pages under its own rule.
- Watermark: inert to the old image (it never reads one). Left in place, it is the next new-image run's window start.
- **If either half is unsigned at 2026-10-05 19:30Z, the builder rolls the image back to 446603c3 before the 20:10Z fire.**

## ADDENDUM A (2026-10-04 ~21:4xZ) -- a served re-run of 2026-10-04 on the new image, before the scheduled fire

**Authority:** Andrew-direct ~21:3xZ, verbatim in `org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_DIRECT_20261004_213xZ_OPEN_CALLS_ALL_RECS_APPROVED_RERUN_DAILY_SPRINT_ONCE_LAPTOP_ONBOARD.md`
@b7f2fb4dc7: *"once laptop is onboard with NFRA_SPRINTWIN,we are going to need to rerun the /daily-sprint because currently if you
look at mcp.opalinvest.dev/sprint, we do not have any commits being tracked in the surface area from the hours since the last
sprint report"*. Measured: the 2026-10-04 scheduled edition (20:10Z, image 446603c3) logged "censuses agree at 12 commits / 5
workers" over pushed refs; the served 2026-10-03 page is 0.0.0_AB_MSTR~Z's hand re-run (caa1425afc), window 00:00-18:15 ET, all
refs, 422 commits.

**The act, after L3 and the QA trace (L4) and the laptop's census:** ONE invoke of the new image with `{"date": "2026-10-04"}`.

**Keys it may touch, every one named:**
1. `daily-reports/2026-10-03/watermark.json` -- NEW, a SEED written by the builder with read-back, BEFORE the invoke:
   `{"day": "2026-10-03", "window_start": "2026-10-03T04:00:00Z", "window_end": "2026-10-03T22:16:00Z", "home": "served",
   "seed": "the served 2026-10-03 page (caa1425afc) covered 00:00-18:15 ET over all refs"}`. Measured: 0 commits on any ref with
   commit time in [22:15:00Z, 22:16:00Z), so this cut neither drops nor double-counts a commit against that page.
2. `daily-reports/2026-10-04/{Desktop,Mobile}_DAILY_REPORT_2026-10-04.html` -- overwritten.
3. `daily-reports/2026-10-04/watermark.json` -- NEW, written by the function last.

**The outcome, read from `cut_window` @dc86c2b2cd:** no 2026-10-04 watermark -> prev = the newest earlier one = the seed ->
window_start 2026-10-03T22:16:00Z; window_end = the earliest 2026-10-04 census `generated_at` among the devices that reported,
capped at the run time. Branch A (both devices reported): the union of pushed history and both censuses. Branch B (one device):
the missing device is named on the page; its pushed work counts. The window is ~23 h, under the 7-day cap.
**Its effect on the scheduled fire:** 2026-10-05's window then starts at 2026-10-04's window_end -- contiguous, no overlap.

**Rollback, per key:** pages -- re-point to 446603c3 and invoke `{"date": "2026-10-04"}` (the old rule re-publishes its own
population). Both watermarks are inert to the old image. Writer 2 stays under condition 1(b) (no local publish of a watermarked day).
