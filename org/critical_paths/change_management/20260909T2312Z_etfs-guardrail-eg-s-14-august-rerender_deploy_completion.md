# Deploy Completion Record
**Date opened:** 2026-09-09T23:12:34.653323+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260910T003729Z
**Deploy:** ETFS_GUARDRAIL.TO-EG-s-14 -- the August re-render: etfs-reports-orchestrator invoked by hand with the schedule's own payload {"mode":"run"}, rewriting the SERVED keys under s3://opal-data-etfs/platinum/reports/2026-08/ (NEVER-2 served-output move; never-widen halves: COO=issuance 4155c85a1f, CTO=broker msg 94775)
**Authored by:** 0.9.0_WK_ETFS_GUARDRAIL~1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | s3://opal-data-etfs/platinum/reports/_archive/2026-08/20260909T230636Z/ -- the 5 PRIOR served objects archived BEFORE the run | sha256 pair per key (prior vs archive), byte-equal, 5 of 5 | 5 of 5 prior served objects copied to s3://opal-data-etfs/platinum/reports/_archive/2026-08/20260909T230636Z/ (copy-object rc=0 each, 23:11:30Z-23:11:39Z) and re-downloaded: sha256 byte-equal 5 of 5 -- html e6b16ef24ae6e997e2b85b3d393d6c60b089b47a4c04e021866ef839c3b3eee5; pdf e85fe6c5028ac860bb245c968f5e6047b50fc1ea0b7b26f71b8854f9383192e8; 49financial 1fba75df7fe50e8b0287c96f2b6be36d9fa8d61ae2f5e0a4f59cbece3e35e3bc; cottonwood 98fb455c41a3958610a28bb9161ef9f111d012098f0f8862e3050babf6ebda6a; inflection f19db318f79821c65144f2996cc2f670b4d47ffcda328c4054ceb666a8296221. Location deviation disclosed in the entry and in row ETFS_GUARDRAIL-W1-S12. Nothing deleted. | CLOSED 20260909T233249Z |
| L2 | activation | lambda invoke etfs-reports-orchestrator payload {"mode":"run"} (the schedule's own Target.Input) | StatusCode 200 + x-amzn-RequestId + invoke UTC | aws lambda invoke --function-name etfs-reports-orchestrator --payload {"mode":"run"} (byte-equal to the live schedule's Target.Input) issued 2026-09-09T23:14:43Z by arn:aws:iam::313476888478:user/Andrew_Berman: StatusCode 200, ExecutedVersion $LATEST, x-amzn-RequestId 2be062b2-6642-4092-852a-7dc4c0b714b5, returned 23:15:24Z, response payload {"mode": "run", "ok": true}. Joined live: START RequestId 2be062b2-6642-4092-852a-7dc4c0b714b5 in /aws/lambda/etfs-reports-orchestrator stream 2026/09/09/[$LATEST]ee4d9f0f57b4424183ff917619bf011f, Duration 37101.01 ms. Exactly 1 of 1 execution in the window. | CLOSED 20260909T233249Z |
| L3 | verify | served keys platinum/reports/2026-08/etf_ownership.pdf, .html, opaletfs_{49financial,cottonwood,inflection}_202608.csv | s3api LastModified (UTC) after the invoke + CSV last row begins '# coverage:' | SERVED OBJECTS REWRITTEN by the re-run, read via s3api in UTC: platinum/reports/2026-08/etf_ownership.html LastModified 2026-09-10T00:24:47Z 43376 B ETag 5364844c7c743e46ead35b3630254845; etf_ownership.pdf 00:24:48Z 252393 B ETag d8d786db4be630c3f1d4bfb0420496f4; opaletfs_49financial_202608.csv 00:24:48Z 2012 B; opaletfs_cottonwood_202608.csv 00:24:50Z 1888 B; opaletfs_inflection_202608.csv 00:24:49Z 1888 B -- 5 of 5 LastModified AFTER the 00:22:57Z invoke. THE COVERAGE LINE IS ON THE SERVED CSV: 3 of 3 end on '# coverage: 21/21 trading days; 0 carried for missing data', and 21 is the month's trading-day count from lib/trading_calendar.py (NYSE, 2026-08-03..2026-08-31). The pre-publish gate ran and PUBLISHED: coverage_verdict.json written 00:24:44Z (verdict PUBLISH, holes 0, 21/21 per partner for all three); no coverage_unresolved.json, no refused/ prefix. Prior objects remain recoverable from both archives (5 of 5 sha256 byte-equal). | CLOSED 20260910T003655Z |
| L4 | verify | SES report send to the JOINED recipients aj@opalinvest.com + andrew@opalinvest.com | SES MessageId(s) + Destinations in the orchestrator CloudWatch log for the run + CloudTrail SendRawEmail | THE SEND HAPPENED; THE TWO NAMED INSTRUMENTS CANNOT SHOW IT, and that is recorded rather than converted into a pass. (1) The orchestrator's CloudWatch log carries NO MessageId line -- the deployed handler prints nothing on the success path (lambda_function.py:405-441: quiet success; only failures print/alert), so 0 of 0 possible. (2) CloudTrail SendRawEmail in the window = 0 events: ses email-sending calls are not captured by either trail (0 of 2 trails select the SES data plane), the same COVERAGE-ABSENT class the amendment ruled for lambda:Invoke; the same-window positive control shows management events ARE logged (StartInstances 00:23:06Z, StopInstances 00:24:57Z). (3) WHAT WAS MEASURED INSTEAD, two independent instruments: SES's own counter (get-send-statistics) rose by exactly +2 DeliveryAttempts across the run (80 -> 82 total; the new data point at 2026-09-10T00:16:00Z carries attempts=2) -- one send_raw_email to TWO destinations, which is the JOIN; and the etfs-reports-alerts SNS topic published 0 messages in the run window while the SAME metric shows 1 publish in the FAILED first fire's window (23:15:00Z) -- every failure branch of _run, including 'report rendered but EMAIL FAILED', publishes there, so 0 with a live positive control says the send did not fail. Live EMAIL_RECIPIENT reads 'aj@opalinvest.com,andrew@opalinvest.com' (EMAIL_RECIPIENTS splits it for both envelopes). Delivery AT the two inboxes remains the issuer's read, not this worker's. Filed as surprise row ETFS_GUARDRAIL-W1-S18. | CLOSED 20260910T003655Z |
| L5 | verify | reporter box i-070477bf35fc54409 stopped after the run | ec2 describe-instances State.Name=stopped | ec2 describe-instances --instance-ids i-070477bf35fc54409 -> State.Name=stopped (read 2026-09-09T23:25Z, and again by the S14-AC1 battery arm (g)). CloudTrail same-window: StartInstances 2026-09-09T23:14:48Z and StopInstances 2026-09-09T23:15:24Z, both Username=etfs-reports-orchestrator -- the finally-stop ran. No cost leak. | CLOSED 20260909T233249Z |
| L6 | s3-prefix | s3://opal-313476888478-lambda-artifacts/ec2/etfs-reports/render_month_end.py -- the W1-S11 renderer fix DEPLOYED (the README's own path, infra/aws/terraform/etfs-reports/README.md:99-105; a re-upload IS the whole deploy) | DEPLOYED-vs-BUILT read back: s3api head-object size + `aws s3 cp <key> -` piped to sha256 == the committed blob sha256 (git show HEAD:<path>); prior deployed sha256 6c3c963e693724be848d55511d81d374cb3fd455dca84513afb62603fd7893f7 named as the ROLLBACK | DEPLOYED 2026-09-10T00:16:35Z via .tools/aws s3 cp data/etfs/scripts/presentation/render_month_end.py s3://opal-313476888478-lambda-artifacts/ec2/etfs-reports/render_month_end.py (rc=0; the README's own path, infra/aws/terraform/etfs-reports/README.md:99-105 -- a re-upload IS the whole deploy). DEPLOYED-vs-BUILT read back on TWO instruments: s3api head-object ContentLength 62880, ETag 545afb2105518af0bc1c1b6bdb4c7ba5, LastModified 2026-09-10T00:16:35Z; aws s3 cp <key> - piped to sha256 = 55701125e86740f3bf51a715aba8f68e8441d3eb7bffc99a43b7d3ff29b973e9 (62880 B); s3api get-object then sha256 = the same; the committed blob (git show HEAD:data/etfs/scripts/presentation/render_month_end.py, commit 0c8bdbe) = the same -> DEPLOYED == BUILT. Byte checks on the deployed copy: it carries the fix os.path.join(_ORION_HERE, 'coverage') and no longer carries _ORION_HERE, '..', 'coverage'. PRIOR deployed (the ROLLBACK target): sha256 6c3c963e693724be848d55511d81d374cb3fd455dca84513afb62603fd7893f7, 61699 B, ETag 9f7bbe4a3d5e73c8c065b9844a41d262, LastModified 2026-09-05T06:52:22Z -- rollback = re-upload git show 4155c85a1f:data/etfs/scripts/presentation/render_month_end.py to the same key; nothing deleted. NEVER-WIDEN HALVES: COO 4155c85a1f + 5507841f04 (the amendment commit), CTO broker message 94775. Local proof before the deploy: py_compile rc=0, .tools/commit-gate.sh rc=0, box-layout rehearsal 2 of 2 arms (EGS14-FIX-REHEARSAL-OK) with the recorded stub argv naming the exact key, and a negative control on the pre-fix file reproducing ModuleNotFoundError rc=1 in the same layout. | CLOSED 20260910T001903Z |
| L7 | verify | s3://opal-data-etfs/platinum/reports/_archive/2026-08/<UTC-2>/ -- the prior served objects archived AGAIN immediately before the RE-INVOKE | ETag equality with the first archive printed first, then sha256 pair per key (prior vs archive), byte-equal, 5 of 5 | ARCHIVE-2, immediately BEFORE the re-invoke, 2026-09-10T00:20:02Z-00:20:1xZ. ETag equality printed FIRST (the failed first fire changed nothing): served ETags at the read were f3e43b3c72dc0d2753099d5e9c0181c4 / 75989bf5f70e28f0ddae900a0a253ee3 / 1554f4a27e6959f291b3c3cf0470232c / 175a3681daff17b0d5d1da7db680f4de / b6a2f9a1f31f1cb483b1b06315f2bd63 -- identical to the pre-first-archive read at 23:06:36Z, 5 of 5, and each copy-object returned the same ETag it copied. Archive at platinum/reports/_archive/2026-08/20260910T002002Z/, re-downloaded and sha256-compared to the priors: 5 of 5 byte-equal (html e6b16ef2..., pdf e85fe6c5..., 49financial 1fba75df..., cottonwood 98fb455c..., inflection f19db318...). The 23:06:36Z archive STANDS as the prior-object record (amendment, row W1-S12). Nothing deleted. | CLOSED 20260910T003655Z |
| L8 | activation | lambda invoke etfs-reports-orchestrator payload {"mode":"run"} -- the RE-INVOKE after the fix deploy (--cli-read-timeout 0 --cli-connect-timeout 60, row W1-S14) | StatusCode 200 + x-amzn-RequestId + invoke UTC + 1 of 1 START RequestId in the log group window + the box stopped after | RE-INVOKE after the fix deploy: .tools/aws lambda invoke --function-name etfs-reports-orchestrator --payload {"mode":"run"} --cli-read-timeout 0 --cli-connect-timeout 60 (row W1-S14: the call is synchronous end to end). Issued 2026-09-10T00:22:57Z by arn:aws:iam::313476888478:user/Andrew_Berman, returned 00:24:57Z, CLI rc=0, StatusCode 200, ExecutedVersion $LATEST, x-amzn-RequestId a027eeb0-e954-4dde-9c4f-1d91cad77f67, payload {"mode": "run", "ok": true}. ONE execution: the log group read BY TIME over 00:20:57Z-00:29:57Z carries START RequestId a027eeb0-e954-4dde-9c4f-1d91cad77f67 exactly 1 of 1 (Duration 113175.04 ms). The rule did not fire: etfs-reports-scheduler-role AssumeRole in the window = 0. SSM command faaae9a5-beb1-4214-8981-5d5d2858f0e0 Status=Success. Box: CloudTrail StartInstances 00:23:06Z, StopInstances 00:24:57Z (both Username etfs-reports-orchestrator), describe-instances State.Name=stopped after. | CLOSED 20260910T003655Z |

## Log

- 20260909T231234Z OPENED by 0.9.0_WK_ETFS_GUARDRAIL~1 with 5 leg(s)
- 20260909T233249Z LEG L1 closed: 5 of 5 prior served objects copied to s3://opal-data-etfs/platinum/reports/_archive/2026-08/20260909T230636Z/ (copy-obje
- 20260909T233249Z LEG L2 closed: aws lambda invoke --function-name etfs-reports-orchestrator --payload {"mode":"run"} (byte-equal to the live schedule's 
- 20260909T233249Z LEG L5 closed: ec2 describe-instances --instance-ids i-070477bf35fc54409 -> State.Name=stopped (read 2026-09-09T23:25Z, and again by th
- 20260909T233308Z HELD-SOVEREIGN-GATED gate=external/ETFS_GUARDRAIL-W1-S11 -- the DEPLOYED render_month_end.py fails at module import
- 20260910T0004Z LEGS L6 (deploy), L7 (archive-2), L8 (re-invoke) ADDED to the SAME held entry by 0.9.0_WK_ETFS_GUARDRAIL~1 per the EG-s-14 amendment @5507841f04 ('a NEW LEG of the SAME NEVER-2 entry -- resume it, do not open a second'); deploy_ledger.py has no add-leg verb and `open` on an existing slug refuses (:356-358), so the leg was appended to this sentinel, which _render_entry rewrites the entry .md from -- surprise row ETFS_GUARDRAIL-W1-S17
- 20260910T001903Z LEG L6 closed: DEPLOYED 2026-09-10T00:16:35Z via .tools/aws s3 cp data/etfs/scripts/presentation/render_month_end.py s3://opal-31347688
- 20260910T003655Z LEG L7 closed: ARCHIVE-2, immediately BEFORE the re-invoke, 2026-09-10T00:20:02Z-00:20:1xZ. ETag equality printed FIRST (the failed fir
- 20260910T003655Z LEG L8 closed: RE-INVOKE after the fix deploy: .tools/aws lambda invoke --function-name etfs-reports-orchestrator --payload {"mode":"ru
- 20260910T003655Z LEG L3 closed: SERVED OBJECTS REWRITTEN by the re-run, read via s3api in UTC: platinum/reports/2026-08/etf_ownership.html LastModified 
- 20260910T003655Z LEG L4 closed: THE SEND HAPPENED; THE TWO NAMED INSTRUMENTS CANNOT SHOW IT, and that is recorded rather than converted into a pass. (1)
- 20260910T003728Z HOLD RELEASED -> OPEN
- 20260910T003729Z CLOSED -- all 8 legs proven

## NEVER-2: never-widen sign-off (BOTH halves), the served keys, the archives, the rollbacks

**APPENDED LAST, 2026-09-10T00:35Z, AFTER THIS ENTRY'S FINAL LEDGER MUTATION (the CLOSE).**
`.tools/deploy_ledger.py` REGENERATES this whole file from the sentinel on every `close-leg` /
`hold` / `close` (`_write_entry` -> `Path(...).write_text(_render_entry(state))`,
`deploy_ledger.py:239,289-291`), so any hand-added section written earlier is destroyed -- measured
once on this very entry (surprise row `ETFS_GUARDRAIL-W1-S16`, ruled by the issuer as an ORDERING
clause: append LAST, then read the criterion). The sentinel is now REMOVED by `close`; this file is
the record.

**NEVER-WIDEN SIGN-OFF, BOTH HALVES**

- COO half: issuance commit `4155c85a1f` (the ONE round-2 issuance that created the task-order face)
  PLUS amendment commit `5507841f04` (the same face amended on rows W1-S11 / W1-S12 / W1-S13 /
  W1-S14 / W1-S16, which is what authorises the ONE code change and its deploy below).
- CTO half: broker message id `94775` -- covering EXACTLY: the same orchestrator with
  `{"mode":"run"}`; writes to `platinum/reports/2026-08/` PDF/HTML/CSV; the prior objects archived
  before the run with sha256 pairs; rollback one copy-object back per key; NOTHING DELETED.

**WHAT LANDED.** The first fire (2026-09-09T23:14:43Z) FAILED on the box and published nothing. The
renderer fix was committed (`0c8bdbe`) and deployed (2026-09-10T00:16:35Z), the prior objects were
archived a second time, and the RE-INVOKE (2026-09-10T00:22:57Z -> 00:24:57Z, request id
`a027eeb0-e954-4dde-9c4f-1d91cad77f67`, SSM `faaae9a5-beb1-4214-8981-5d5d2858f0e0` Success)
REWROTE all five served keys with the coverage line and SES-sent the report.

**SERVED KEYS REWRITTEN** (bucket `opal-data-etfs`), 5 of 5, LastModified in UTC via `s3api`:

| served key | LastModified (UTC) | size | ETag |
|---|---|---|---|
| `platinum/reports/2026-08/etf_ownership.html` | 2026-09-10T00:24:47Z | 43376 | `5364844c7c743e46ead35b3630254845` |
| `platinum/reports/2026-08/etf_ownership.pdf` | 2026-09-10T00:24:48Z | 252393 | `d8d786db4be630c3f1d4bfb0420496f4` |
| `platinum/reports/2026-08/opaletfs_49financial_202608.csv` | 2026-09-10T00:24:48Z | 2012 | `d993f70bab48f40ada219a5f0e8c15a5` |
| `platinum/reports/2026-08/opaletfs_inflection_202608.csv` | 2026-09-10T00:24:49Z | 1888 | `3ff4a7dc9de75e0fc9ca0b540ba7fb74` |
| `platinum/reports/2026-08/opaletfs_cottonwood_202608.csv` | 2026-09-10T00:24:50Z | 1888 | `9662cb0d35de5d4baf4d56262c25f2b9` |

Plus ONE new key the gate always writes: `platinum/reports/2026-08/coverage_verdict.json`
(2026-09-10T00:24:44Z, verdict PUBLISH, holes 0). No `coverage_unresolved.json`, no `refused/`.

**ARCHIVES** -- `get-bucket-versioning` on `opal-data-etfs` returns EMPTY (versioning NOT enabled),
so each archive is a `copy-object` of every prior object, verified byte-equal by sha256 on both
sides. TWO archives exist: the first before the failed fire, the second immediately before the
re-invoke (the served bytes were identical at both reads -- the ETags matched 5 of 5).

| prior served key | prior sha256 | bytes | archive 1 (23:06:36Z) | archive 2 (00:20:02Z) |
|---|---|---|---|---|
| `etf_ownership.html` | `e6b16ef24ae6e997e2b85b3d393d6c60b089b47a4c04e021866ef839c3b3eee5` | 62477 | YES | YES |
| `etf_ownership.pdf` | `e85fe6c5028ac860bb245c968f5e6047b50fc1ea0b7b26f71b8854f9383192e8` | 273857 | YES | YES |
| `opaletfs_49financial_202608.csv` | `1fba75df7fe50e8b0287c96f2b6be36d9fa8d61ae2f5e0a4f59cbece3e35e3bc` | 1952 | YES | YES |
| `opaletfs_cottonwood_202608.csv` | `98fb455c41a3958610a28bb9161ef9f111d012098f0f8862e3050babf6ebda6a` | 1828 | YES | YES |
| `opaletfs_inflection_202608.csv` | `f19db318f79821c65144f2996cc2f670b4d47ffcda328c4054ceb666a8296221` | 1828 | YES | YES |

Denominator: 5 of 5 prior objects in each archive; 5 of 5 byte-equal in each (10 of 10 total).
Archive 1: `platinum/reports/_archive/2026-08/20260909T230636Z/` -- Archive 2: `platinum/reports/_archive/2026-08/20260910T002002Z/`.

**ARCHIVE LOCATION.** Both archives sit OUTSIDE `platinum/reports/2026-08/`, because the
orchestrator's `_month_csv_keys` (`lambda_function.py:265-274`) enumerates that prefix WITHOUT a
delimiter and attaches every `.csv` under it to the report email -- an archive inside it would have
put three stale duplicate CSVs into the delivered mail (row `ETFS_GUARDRAIL-W1-S12`, ruled; the
face's archive clause now names this location).

**ROLLBACK 1 -- the served objects.** One `copy-object` back per key, from either archive; nothing
is deleted. NOT EXECUTED: the re-render is the intended new state, and every prior byte is held in
two archives.

```
.tools/aws s3api copy-object --bucket opal-data-etfs \
  --key platinum/reports/2026-08/etf_ownership.html \
  --copy-source opal-data-etfs/platinum/reports/_archive/2026-08/20260910T002002Z/etf_ownership.html
.tools/aws s3api copy-object --bucket opal-data-etfs \
  --key platinum/reports/2026-08/etf_ownership.pdf \
  --copy-source opal-data-etfs/platinum/reports/_archive/2026-08/20260910T002002Z/etf_ownership.pdf
.tools/aws s3api copy-object --bucket opal-data-etfs \
  --key platinum/reports/2026-08/opaletfs_49financial_202608.csv \
  --copy-source opal-data-etfs/platinum/reports/_archive/2026-08/20260910T002002Z/opaletfs_49financial_202608.csv
.tools/aws s3api copy-object --bucket opal-data-etfs \
  --key platinum/reports/2026-08/opaletfs_cottonwood_202608.csv \
  --copy-source opal-data-etfs/platinum/reports/_archive/2026-08/20260910T002002Z/opaletfs_cottonwood_202608.csv
.tools/aws s3api copy-object --bucket opal-data-etfs \
  --key platinum/reports/2026-08/opaletfs_inflection_202608.csv \
  --copy-source opal-data-etfs/platinum/reports/_archive/2026-08/20260910T002002Z/opaletfs_inflection_202608.csv
```

**ROLLBACK 2 -- the renderer deploy (leg L6).** Re-upload the prior blob to the same key; nothing
is deleted. Prior deployed sha256 `6c3c963e693724be848d55511d81d374cb3fd455dca84513afb62603fd7893f7`
(61699 B); deployed now `55701125e86740f3bf51a715aba8f68e8441d3eb7bffc99a43b7d3ff29b973e9` (62880 B,
== the committed blob at `0c8bdbe`).

```
git show 4155c85a1f:data/etfs/scripts/presentation/render_month_end.py > /tmp/prior_renderer.py
.tools/aws s3 cp /tmp/prior_renderer.py \
  s3://opal-313476888478-lambda-artifacts/ec2/etfs-reports/render_month_end.py
```

**NOTHING IS DELETED BY THIS ENTRY OR EITHER ROLLBACK.**

