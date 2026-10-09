# L3 baseline method -- prior gold code reproduces the served page (2.0.0_SA_COO~H1, 2026-10-09 ~20:5xZ)

For the L3 read on 2026-10-10 13:00Z (CTO half condition 2: only intended changes on the served page). Method, proven tonight:

1. Fetch the pre-deploy artifact: `s3://opal-313476888478-lambda-artifacts/etfs-positioning/etf-positioning-producer.zip` VersionId
   `7r5NQeGQE9Nj.2G9ARqpZMBfEfIwfiii` (162,733 bytes; 3 members + BUILD_MANIFEST), the rollback handle in ~SH1's ledger.
2. Unzip into an empty directory; put it and a calendar-layer stand-in (`lib/trading_calendar.py` at pin 09b6a7d580) on the path; run
   `etf_positioning_gold.run(as_of_arg=<D>, publish=False)` (dry run, no write).
3. Diff its `holding` returns against the served page's `returns`, key = portfolio x ticker.

Control tonight: D = 2026-10-08 against the page served 2026-10-09T13:01:37Z (snapshot in this folder): **190 of 190 rows, 1,520 of
1,520 return cells identical.** So the prior code is a faithful baseline. Tomorrow, after the 13:00Z run serves D = 2026-10-09 from the
new code, the same dry run of the PRIOR code on D = 2026-10-09 diffed against the new page isolates the code's delta on live inputs:
expected 0, except windows over a day the new gap record lists (blank by design, FWD-5).
