# ADVI_FIRMBKTS `FB-l-5` -- the issuer's independent read of the first moved trigger's first floor day (`2.0.0_SA_COO~B1`, 2026-10-16 ~16:5xZ)

**Claim under test:** `0.7.0_AE_CloudOps~FB1` msg 6892: `FB-l-5` complete, the 13:30Z fire published (22 of 23 named keys with new VersionIds, 0 outside), the 16:30Z catch-up halted with zero writes, AC1 PASS, ledger closed; record `dc05178afa`, close `b8b775464537d677055c171cf7294551f6c03b3a` (on this box's `box/dell1`, which is this seat's own branch). FB1 flagged one anomaly itself: the `platinum/` version count fell from 79,959 to 77,338 with no write, read as lifecycle expiry. Read from the committed record and the live account.

| read | instrument | result |
|---|---|---|
| AC1 on the committed record | this seat's `r8_checks.py move`, record pulled with `git show b8b775464537:<path>` | `MOVE: OK trigger=inf-portal-publisher`, rc 0 (grades shape only) |
| the publisher writes where the record says | `lambda get-function-configuration` | `OUTPUT_BUCKET` = `INPUT_BUCKET` = `opal-data-inf`; function last modified 2026-10-14 14:09Z (the FB-m-2 deploy) |
| the old trigger is gone | `get-bucket-notification-configuration` on `opal-data-inf` | ONE lambda entry: `silver/_silver_complete/` + `.json` to `inf-silver-aggregator`; no `gold/meta/` entry |
| the new trigger is live | `scheduler get-schedule` x2 | `advi-inf-publish-daily` ENABLED `cron(30 13 * * ? *)`, `advi-inf-publish-catchup-daily` ENABLED `cron(30 16 * * ? *)`; both `Input {}`, dead-letter queue `advi-inf-publish-dlq`, retry 1, flexible window OFF |
| invocations today | `logs filter-log-events` on the publisher, `START RequestId` | exactly two: 13:30:28Z and 16:30:12Z; none after the 12:56:43Z marker |
| the guard's verdicts | same, `READINESS` | 13:30Z `READINESS OK` (`frontier-after-served`); 16:30Z `READINESS HALT` (`not-after-served`, served=2026-10-16) |
| writes, with a positive control | `list-object-versions --prefix platinum/`, every version and delete marker dated today, partitioned by time | 22 versions at 13:30-13:35Z (the control: the record's 22 of 23 keys, all under `platinum/firm/snapshots/` and `platinum/advisors/`); 0 from 13:35Z to 16:30Z; **0 at or after 16:30Z**; 0 delete markers (76 empty pages of `None`, which also shows the listing covered the whole history); latest version today 13:31:13Z |
| the version-count fall | `get-bucket-lifecycle-configuration` | rule `expire-noncurrent-versions-14d` Enabled, no prefix filter, 14 days: it expires noncurrent versions bucket-wide, so a falling count with no new version is that rule |
| ledger | the record and `FB-l-5`'s completion commit | `ledger_closed` true; the order status is `complete` |

**The zero-writes claim holds on a direct measure,** not on the counts: no version or delete marker under `platinum/` has a `LastModified` at or after 13:35Z. The count comparison alone could not have shown that, as FB1 said.

## What this read does NOT establish (named)

- Not re-read: the 23rd named key (`top_holdings.json`, written by the gold chain) and the CloudFront invalidation; the advisor publisher's `COMPLETE: 5 published, 0 errors` line and the 32 advisor objects before and after (FB1's own counts); the completion series (11 trading-day completions, 30 min margin) beyond the two days' markers.
- The 14-day lifecycle explains the direction and the cause of the fall; it does not by itself prove the size, 2,621 versions, which was not recomputed.
- The 16:30Z halt exercised one arm of the guard on one day. A gold day that finishes after 16:30Z publishes the next day at 13:30Z (stated in the signed addendum, not guarded).
- Whether the CTO reads the record's `early_fire_statement` as meeting condition C4 is the CTO's read, not this one.

## State after

`FB-l-5` is terminal (complete) with its record verified. With it, the eight round-8 orders are complete (`proof_ok=8` after the instance-name copies in `deliverables/2.0.0_SA_COO~B1/round8/PROOF_INSTANCE_NAME_COPIES.md`); `round-close-check --round 8` reads MAY-CLOSE.
