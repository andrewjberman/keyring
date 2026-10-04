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
