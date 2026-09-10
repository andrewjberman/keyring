# Deploy Completion Record
**Date opened:** 2026-09-10T03:40:42.281570+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260910T034857Z
**Deploy:** EG-s-19 THE CATCH-UP BRANCH DRIVEN: archive then DELETE one served slice (s3://opal-data-etfs/daily/cottonwood/2026-09-03.json) on ANDREW-DIRECT ~02:5xZ, then fire cot-etf-ownership-daily in the rule's own scheduled shape so its catch-up path finds and refills the hole itself. opal-data-etfs versioning is DISABLED (get-bucket-versioning empty, rc 0) so the DELETE IS FINAL and the ONLY way back is the archive copy named below. ROLLBACK: .tools/aws s3api copy-object --bucket opal-data-etfs --key daily/cottonwood/2026-09-03.json --copy-source opal-data-etfs/daily/_archive/cottonwood/2026-09-03.20260910T034042Z.json
**Authored by:** 0.9.0_WK_ETFS_GUARDRAIL~5
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | s3://opal-data-etfs/daily/_archive/cottonwood/2026-09-03.20260910T034042Z.json | archive copy exists and its sha256 EQUALS the source slice sha256, both printed | ARCHIVE VERIFIED BYTE-EQUAL. s3://opal-data-etfs/daily/_archive/cottonwood/2026-09-03.20260910T034042Z.json head-object rc 0, Size 1345, LastModified 2026-09-10T03:45:24.000Z, ETag 212d7da63d847fd3f25facd6a651b481. sha256 of the SOURCE slice bytes = 060188a6e76b2275538e9cb2de0244023600ccfaa713fa738d6f24e2eb757cc8 (1345 B); sha256 of the ARCHIVE bytes read BACK from S3 = 060188a6e76b2275538e9cb2de0244023600ccfaa713fa738d6f24e2eb757cc8 (1345 B); EQUAL. Copy made 03:45:22Z, verified 03:45:26Z, both BEFORE the delete at 03:45:26Z-03:45:28Z. | CLOSED 20260910T034821Z |
| L2 | verify | DELETE s3://opal-data-etfs/daily/cottonwood/2026-09-03.json | head-object 404 on the slice beside head-object 200 on the 2026-09-04 neighbour in the same call sequence | THE HOLE EXISTED. delete-object on s3://opal-data-etfs/daily/cottonwood/2026-09-03.json rc 0 at 2026-09-10T03:45:26Z (entry opened 03:40Z, so opened-at PRECEDES the delete). Then, in ONE call sequence: head-object on the deleted key rc 255 'An error occurred (404) when calling the HeadObject operation: Not Found' at 03:45:31Z, beside head-object on the 2026-09-04 neighbour rc 0 (200) at 03:45:34Z as the POSITIVE CONTROL. Bucket versioning DISABLED (get-bucket-versioning empty, rc 0) so the delete was final and the L1 archive was the only way back. | CLOSED 20260910T034822Z |
| L3 | verify | cot-etf-ownership-daily invoked in the rule's scheduled envelope shape, NO date key | StatusCode 200 + request id + 1 of 1 START RequestId in /aws/lambda/cot-etf-ownership-daily read BY TIME | FIRED IN THE RULE'S SHAPE. Payload = EventBridge default scheduled envelope (version/id/detail-type 'Scheduled Event'/source aws.events/account 313476888478/time/region us-east-1/resources [arn:aws:events:us-east-1:313476888478:rule/cot-etf-ownership-daily-schedule]/detail {}); NO 'date' key and NO 'probe' key, so the handler could not reach the explicit-date branch at lambda_function.py:304-308. Basis: list-targets-by-rule on cot-etf-ownership-daily-schedule returns 1 of 1 target with NO Input, InputPath or InputTransformer, so the rule delivers the default envelope. lambda invoke rc 0, StatusCode 200, ExecutedVersion LATEST, RequestId fdc655fd-08fd-4b1b-b58f-ad6199f9396e. Log group /aws/lambda/cot-etf-ownership-daily read BY TIME (filter-log-events 03:45:04Z-03:50:04Z) returns 6 events in 1 stream with 1 of 1 START RequestId, that same id. | CLOSED 20260910T034822Z |
| L4 | verify | the CATCH-UP branch found 2026-09-03 itself | CATCHUP: processed 2026-09-03 line in the log AND catchup_processed carrying the date in the response | THE BRANCH RAN AND FOUND THE DATE ITSELF -- the first observed exercise of this path in the estate. The log's own lines, /aws/lambda/cot-etf-ownership-daily read BY TIME: 03:45:37.943Z 'OK: wrote s3://opal-data-etfs/daily/cottonwood/2026-09-08.json (4 ETF slices, total_ownership=53641351.75, source_as_of=2026-09-08...)' = the MAIN path on the newest partition; 03:45:38.389Z 'OK: wrote s3://opal-data-etfs/daily/cottonwood/2026-09-03.json (4 ETF slices, total_ownership=53750650.53, source_as_of=2026-09-03...)'; 03:45:38.391Z 'CATCHUP: processed 2026-09-03 (status=ok)'. The invoke response: {status ok, date 2026-09-08, key daily/cottonwood/2026-09-08.json, slices 4, total_ownership 53641351.75, source_as_of 2026-09-08, catchup_processed [2026-09-03], catchup_failed [], catchup_skipped_unpriced []}. 2026-09-03 is carried by catchup_processed, NOT by the main path, whose date field is 2026-09-08. | CLOSED 20260910T034857Z |
| L5 | verify | slice restored and nothing else moved | head-object 200 with size+UTC, rows counted non-zero by a second reader, daily/ key counts equal before and after with denominators | SLICE BACK, NOTHING ELSE MOVED IN CONTENT. head-object on daily/cottonwood/2026-09-03.json rc 0 (200) at 03:45:39Z, Size 1345, LastModified 2026-09-10T03:45:39.000Z, ETag 212d7da63d847fd3f25facd6a651b481 -- restored on poll 1 of a bound of 30 polls over 15 minutes. Second independent reader (json.load): 4 rows, non-zero, one per universe ETF. Content vs the archive: sha256 060188a6e76b2275538e9cb2de0244023600ccfaa713fa738d6f24e2eb757cc8 on BOTH, 0 field-level differences over 4 tickers x 8 fields -- a byte-identical re-derivation, not merely a similar one. NOTHING ELSE: daily/cottonwood/ 62 keys before and 62 after (denominator printed both times); daily/ 273 -> 274, the ONE addition being the L1 archive this entry named before the act. Keys with CHANGED CONTENT under daily/: ZERO. Keys with a touched LastModified: 2 -- the hole itself, and daily/cottonwood/2026-09-08.json which the rule's own MAIN path re-processes by design (lambda_function.py:310-311), ETag 5da999e2fbfadfe302df35ef24407372 identical before and after, i.e. an idempotent byte-identical rewrite. See surprise row ETFS_GUARDRAIL-W5-S1. | CLOSED 20260910T034857Z |
| L6 | verify | ROLLBACK STATE | either NOT-NEEDED because L4+L5 are proven, or EXECUTED copy-object from the archive restoring the byte-identical original | ROLLBACK NOT NEEDED AND NOT RUN. The producer's own fire restored the slice within the bound (poll 1 of 30, 5 seconds after the invoke returned), and L5 proves the restored bytes are identical to the archived original, so the rollback path was never entered. The archive object is RETAINED at s3://opal-data-etfs/daily/_archive/cottonwood/2026-09-03.20260910T034042Z.json as the standing rollback; the rollback command remains: .tools/aws s3api copy-object --bucket opal-data-etfs --key daily/cottonwood/2026-09-03.json --copy-source opal-data-etfs/daily/_archive/cottonwood/2026-09-03.20260910T034042Z.json. EXACTLY ONE delete was performed under this order and no second delete of any kind was made. | CLOSED 20260910T034857Z |

## Log

- 20260910T034042Z OPENED by 0.9.0_WK_ETFS_GUARDRAIL~5 with 6 leg(s)
- 20260910T034821Z LEG L1 closed: ARCHIVE VERIFIED BYTE-EQUAL. s3://opal-data-etfs/daily/_archive/cottonwood/2026-09-03.20260910T034042Z.json head-object 
- 20260910T034822Z LEG L2 closed: THE HOLE EXISTED. delete-object on s3://opal-data-etfs/daily/cottonwood/2026-09-03.json rc 0 at 2026-09-10T03:45:26Z (en
- 20260910T034822Z LEG L3 closed: FIRED IN THE RULE'S SHAPE. Payload = EventBridge default scheduled envelope (version/id/detail-type 'Scheduled Event'/so
- 20260910T034857Z LEG L4 closed: THE BRANCH RAN AND FOUND THE DATE ITSELF -- the first observed exercise of this path in the estate. The log's own lines,
- 20260910T034857Z LEG L5 closed: SLICE BACK, NOTHING ELSE MOVED IN CONTENT. head-object on daily/cottonwood/2026-09-03.json rc 0 (200) at 03:45:39Z, Size
- 20260910T034857Z LEG L6 closed: ROLLBACK NOT NEEDED AND NOT RUN. The producer's own fire restored the slice within the bound (poll 1 of 30, 5 seconds af
- 20260910T034857Z CLOSED -- all 6 legs proven

---

## CARRIED DETAIL -- appended AFTER `close` (row `W1-S16`: the ledger re-renders this file from its sentinel on every call, so this block is appended LAST or not at all)

### THE AUTHORITY

ANDREW-DIRECT ~02:5xZ at the `1.0.0_SA_CTO` terminal, verbatim: *"Call 1, yeah try it but make sure no
test run hits aj's email, that is not appropriate."* Both halves bind. The DELETE of a served object is
approved by that word and by nothing else -- no seat may supply it. The standing constraint (no test run
hits aj@opalinvest.com) is proven below, not assumed. `etfs-reports-orchestrator` was NOT invoked under
this order in any mode.

### THE SLICE, THE ARCHIVE, THE ROLLBACK

| | value |
|---|---|
| slice deleted (EXACTLY ONE) | `s3://opal-data-etfs/daily/cottonwood/2026-09-03.json` |
| its size / UTC before the act | 1345 B / `2026-09-05T10:30:30.000Z` / ETag `212d7da63d847fd3f25facd6a651b481` |
| archive copy (THE ROLLBACK) | `s3://opal-data-etfs/daily/_archive/cottonwood/2026-09-03.20260910T034042Z.json` |
| sha256 of the SOURCE bytes | `060188a6e76b2275538e9cb2de0244023600ccfaa713fa738d6f24e2eb757cc8` (1345 B) |
| sha256 of the ARCHIVE bytes, read BACK from S3 | `060188a6e76b2275538e9cb2de0244023600ccfaa713fa738d6f24e2eb757cc8` (1345 B) -- EQUAL |
| sha256 of the RESTORED bytes, after the producer's own fire | `060188a6e76b2275538e9cb2de0244023600ccfaa713fa738d6f24e2eb757cc8` (1345 B) -- EQUAL to both |
| rollback command (archive RETAINED, standing) | `.tools/aws s3api copy-object --bucket opal-data-etfs --key daily/cottonwood/2026-09-03.json --copy-source opal-data-etfs/daily/_archive/cottonwood/2026-09-03.20260910T034042Z.json` |
| rollback state | NOT NEEDED, NOT RUN -- the producer restored the slice itself on poll 1 of a 30-poll / 15-minute bound |

`opal-data-etfs` versioning re-derived at this seat: `get-bucket-versioning` returns EMPTY at rc 0, i.e.
DISABLED. The delete was therefore FINAL and the archive above was the only way back. It was made, read
back and verified byte-equal BEFORE the delete, and the entry was OPEN at 03:40:42Z -- 4m44s before the
delete at 03:45:26Z.

### THE CHOICE OF DATE, MEASURED -- and it is a CHOICE, so the rejected dates are printed too

The estate's own calendar was enumerated at this seat rather than inherited from any hand-listed set (the
issuer's own enumeration of the non-trading days in this stretch was incomplete, and said so):
`lib/trading_calendar.py` `is_trading_day`, `calendar_source` = NYSE/pandas_market_calendars, 14 of 14 days
2026-08-28..2026-09-10 -- THREE non-trading days in the stretch, not two: `2026-09-05` (Sat), `2026-09-06`
(Sun), `2026-09-07` (Labor Day).

| date | (1) trading day | (2) slice present | (3) upstream partition / priced (the producer's OWN non-writing probe) | (4) NOT the newest priced partition | verdict |
|---|---|---|---|---|---|
| **2026-09-03** | **True** | **yes, 1345 B @ `2026-09-05T10:30:30.000Z`** | **`partition: true`, `priced: 11947`** | **yes -- newest is 2026-09-08** | **TAKEN** |
| 2026-09-08 | True | yes, 1345 B @ `2026-09-09T23:15:52.000Z` | `partition: true`, `priced: 12016` | **NO -- it IS the newest** | REJECTED: `_latest_partition()` returns it, so `_catchup_missing_dates(skip_date=...)` skips it at `lambda_function.py:268-269`. This is exactly the dead end `EG-s-17` closed on with `CATCHUP-BRANCH-NOT-EXERCISED`. |
| 2026-09-05 | **False** | no | `partition: false`, `priced: 0` | n/a | REJECTED: not a trading day, so its ABSENCE IS CORRECT and there is nothing to delete. |
| 2026-09-09 | True | no | `partition: false`, `priced: 0` | yes | REJECTED: upstream has not landed (the D+1 race, class D). The producer could NOT re-derive it, so a hole there would be damage, not a test. |
| 2026-09-04 | True | yes, 1345 B @ `2026-09-09T10:30:30.000Z` | `partition: true`, `priced: 12033` | yes | ELIGIBLE BUT NOT TAKEN -- kept intact as the 200 POSITIVE CONTROL beside the 404, and 2026-09-03 sits further from the newest partition, so the exclusion at (4) is unambiguous. |

The catch-up window the run actually used, re-derived: `_window_dates` starts at the PRIOR month's 1st only
while that month's report has NOT shipped. Measured at 03:4xZ: `s3://opal-data-etfs/platinum/reports/2026-08/etf_ownership.pdf`
head-object rc 0 (252393 B, `Thu, 10 Sep 2026 00:24:48 GMT`) -- SHIPPED, so the window started at
`2026-09-01` and ran through `today-1` = `2026-09-09` (UTC now was 2026-09-10T03:2xZ, NOT 09-09 local):
`['2026-09-01','2026-09-02','2026-09-03','2026-09-04','2026-09-08','2026-09-09']`, 6 dates. 2026-09-03 is
in the window on EITHER branch of the shipped test, so the choice is robust to it.

### WHAT THE FIRE PROVED

The catch-up branch has never once run in this estate. It ran here, and it found the date BY ITSELF:
`CATCHUP: processed 2026-09-03 (status=ok)` at 03:45:38.391Z, with `catchup_processed: ["2026-09-03"]` in
the response while the response's own `date` field reads `2026-09-08` -- so the recovery was on the CATCH-UP
path and not the main path. The restored slice is byte-identical to the archived original (sha256 equal,
0 field-level differences over 4 tickers x 8 fields).

### ANDREW'S ~02:5xZ CONSTRAINT, PROVEN ON THREE INDEPENDENT INSTRUMENTS

1. **The deployed bytes.** `get-function` -> the deployed package holds 1 of 1 file, `lambda_function.py`,
   sha256 `667c2c720268da03b215cf47b7520e3e2445d9a041715a40ed1bd7f423e63e1c`, byte-identical to the repo
   source at `infra/aws/lambda/cot-pipeline/cot-etf-ownership-daily/lambda_function.py`. Token census over
   those deployed bytes for `ses|sesv2|send_email|send_raw_email|sns`: **0 hits**. THIS PRODUCER HAS NO
   MAILER ON ANY PATH.
2. **The role.** `cot-etf-ownership-daily-role` carries 3 policies of 3 (managed `AWSLambdaBasicExecutionRole`
   = logs only; inline `cloudwatch-metrics` = `cloudwatch:PutMetricData`; inline `s3-etf-ownership` = 8 S3
   statements). **ZERO `ses:` actions.** It could not send if it tried.
3. **The window.** `AWS/SES` `Send`, `Delivery` and `Reputation.BounceRate`, Sum, period 300, over
   03:35:34Z-03:50:5xZ: **0 datapoints and Sum 0 on 3 of 3 metrics** -- zero SES sends of any kind, from any
   sender, in the run window.

`etfs-reports-orchestrator` -- the one component whose mailer reaches aj@ -- was not invoked, in any mode,
at any point under this order.
