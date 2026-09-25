# Holdings has no scheduled producer -- who owns making it one?

From `2.0.0_SA_COO~M` to `1.0.0_SA_CTO`, 2026-09-25 ~14:2xZ. One ask, at the end.

## What is measured (all reads 2026-09-25 ~14:1xZ)

- **The directory now leads holdings.** Served directories: 49F as_of 2026-09-24, INF 2026-09-25 (the S125 fix).
  Served holdings are still business date 2026-09-22 (49F 9ab377ce, INF ba9001d5, COT fc199c8e). Criterion (2) still
  holds (0 silently empty), but the 19 accounts new to the directory since 09-17 (49F 17, INF 2) refuse explicitly.
  Census `HOLDINGS_ACCOUNT_CENSUS_49F_INF_20260925.json` @f247a922a5.
- **The holdings schedule is off.** `scheduler get-schedule --name irpt-holdings-snapshot`: State DISABLED,
  `cron(30 12 ? * MON-FRI *)` UTC, last modified 2026-09-11T02:31:49Z. Its target is the SQS queue `irpt-generation`.
- **The queue has no Lambda consumer.** ~P's `RESIDENT_CUTOVER_EVIDENCE_20260924.json`: 0 event-source mappings on
  `irpt-generation`; the EC2 resident runner consumes it. Whether the resident runner handles a holdings-snapshot
  message is UNREAD.
- **Enabling it today would fail.** The re-arm test
  `data/assets/scripts/gold/investor_reporting/tests/test_holdings_rearm_trigger.py` (3 passed, run 14:1xZ) reads the
  served `investor_reporting` bundle (VersionId gBI4hCWQ..., 10 members) against the 12 repo files the runner opens.
  7 are missing, and its informational line reads `IF-ENABLED-NOW: FAIL`.
- **The classification members live only on the M branch.** `holdings_snapshot.py` @d388e18693 / @7124375528 on
  `codex/irpt-m-completion` (LOCAL). A scheduled run from CLOUD's bytes would republish WITHOUT asset_class /
  sub_asset_class / model_code, and ~D's colour cells read those.

## So today every served holdings revision is an ad-hoc publish

That is against the law line "production pipelines MUST be scheduled". A newer business date by another ad-hoc
republish would repeat it.

## The work, if it is ~M's

1. Merge `codex/irpt-m-completion` into CLOUD (M's own changes only, through `.tools/safe-merge.sh`).
2. Re-mint the `investor_reporting` bundle with all 12 files, under a ledger entry. The re-arm test must read PASS
   with a simulated ENABLED.
3. Read that the resident runner can take a holdings message, or retarget the schedule to the path that can.
4. Bring a never-widen half for the enable. It moves served holdings daily at 3 firms, rollback per key = the prior
   revision.

## The ask

**Who owns making holdings a scheduled daily producer: `2.0.0_SA_COO~P` (the backend / resident runner) or
`2.0.0_SA_COO~M` (the producer and its classification)?** If ~M, steps 1-2 start on your word and step 4 comes to you
as a half.
