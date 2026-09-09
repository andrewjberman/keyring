# Deploy Completion Record
**Date opened:** 2026-09-09T23:12:34.653323+00:00
**Status:** HELD-SOVEREIGN-GATED -- gate: external / ETFS_GUARDRAIL-W1-S11 -- the DEPLOYED render_month_end.py fails at module import on the reporter box (ModuleNotFoundError: _orion_vendor_asof, SSM command c935cadb-1e84-473a-a6ca-ab068f89f564 Failed rc=1); L3 (served objects) and L4 (SES send) cannot be proven until that renderer fix is deployed by the issuer 2.0.0_SA_COO's next cut. NO half-landing: 5 of 5 served objects are bit-identical to their pre-invoke state (ETags unchanged), so the rollback is a verified no-op and NOTHING was deleted. (held since 2026-09-09T23:33:08.706824+00:00)
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
| L3 | verify | served keys platinum/reports/2026-08/etf_ownership.pdf, .html, opaletfs_{49financial,cottonwood,inflection}_202608.csv | s3api LastModified (UTC) after the invoke + CSV last row begins '# coverage:' |  | OPEN |
| L4 | verify | SES report send to the JOINED recipients aj@opalinvest.com + andrew@opalinvest.com | SES MessageId(s) + Destinations in the orchestrator CloudWatch log for the run + CloudTrail SendRawEmail |  | OPEN |
| L5 | verify | reporter box i-070477bf35fc54409 stopped after the run | ec2 describe-instances State.Name=stopped | ec2 describe-instances --instance-ids i-070477bf35fc54409 -> State.Name=stopped (read 2026-09-09T23:25Z, and again by the S14-AC1 battery arm (g)). CloudTrail same-window: StartInstances 2026-09-09T23:14:48Z and StopInstances 2026-09-09T23:15:24Z, both Username=etfs-reports-orchestrator -- the finally-stop ran. No cost leak. | CLOSED 20260909T233249Z |

## Log

- 20260909T231234Z OPENED by 0.9.0_WK_ETFS_GUARDRAIL~1 with 5 leg(s)
- 20260909T233249Z LEG L1 closed: 5 of 5 prior served objects copied to s3://opal-data-etfs/platinum/reports/_archive/2026-08/20260909T230636Z/ (copy-obje
- 20260909T233249Z LEG L2 closed: aws lambda invoke --function-name etfs-reports-orchestrator --payload {"mode":"run"} (byte-equal to the live schedule's 
- 20260909T233249Z LEG L5 closed: ec2 describe-instances --instance-ids i-070477bf35fc54409 -> State.Name=stopped (read 2026-09-09T23:25Z, and again by th
- 20260909T233308Z HELD-SOVEREIGN-GATED gate=external/ETFS_GUARDRAIL-W1-S11 -- the DEPLOYED render_month_end.py fails at module import

## NEVER-2: never-widen sign-off (BOTH halves), the served keys, the archive and the rollback

**RE-APPENDED 2026-09-09T23:36Z AFTER THE LAST LEDGER MUTATION.** `.tools/deploy_ledger.py` REGENERATES
this whole file from the sentinel on every `close-leg`/`hold` (`_write_entry` -> `Path(...).write_text(`
`_render_entry(state))`, deploy_ledger.py:239,289-291), so a hand-added section written before those calls
is silently destroyed. Filed as surprise row ETFS_GUARDRAIL-W1-S16. No further ledger mutation is made
under this order; a future one MUST re-append this section.

**THIS IS A SERVED-OUTPUT MOVE.** The monthly orchestrator was invoked BY HAND with the schedule's own
payload; the run was to REWRITE the served August report keys. This entry was opened at
2026-09-09T23:12:34Z, BEFORE the invoke at 2026-09-09T23:14:43Z.

**OUTCOME: NOTHING LANDED.** The render failed on the box at module import
(`ModuleNotFoundError: No module named '_orion_vendor_asof'`, SSM command
c935cadb-1e84-473a-a6ca-ab068f89f564, ResponseCode 1), so no served object was rewritten: 5 of 5 keys
below still carry LastModified 2026-09-01T17:38:41/42Z and their pre-invoke ETags. The rollback is a
MEASURED no-op and was not executed. Legs L3/L4 are unprovable -> this entry is HELD-SOVEREIGN-GATED on
the named gate, not left OPEN.

**NEVER-WIDEN SIGN-OFF, BOTH HALVES**

- COO half: issuance commit `4155c85a1f` (`4155c85a1f56f0a5673d1183f17c69e16c1e3f81`) -- the ONE round-2
  issuance that created
  `org/missions/D8/ETFS/ETFS_GUARDRAIL/task-orders/ETFS_GUARDRAIL.TO-EG-s-14.the-august-re-render.md`
  (`git log -1 --format=%h -- <that file>` = `4155c85a1f`).
- CTO half: broker message id `94775` -- sign-off covering EXACTLY: the same orchestrator with
  `{"mode":"run"}`; writes to `platinum/reports/2026-08/` PDF/HTML/CSV; the prior objects archived
  before the run with sha256 pairs; rollback one copy-object back per key; NOTHING DELETED.

**SERVED KEYS THE RUN WOULD REWRITE** (bucket `opal-data-etfs`), 5 of 5 enumerated from S3 before the run:

- `platinum/reports/2026-08/etf_ownership.pdf`
- `platinum/reports/2026-08/etf_ownership.html`
- `platinum/reports/2026-08/opaletfs_49financial_202608.csv`
- `platinum/reports/2026-08/opaletfs_cottonwood_202608.csv`
- `platinum/reports/2026-08/opaletfs_inflection_202608.csv`

(A successful run would ALSO write `coverage_verdict.json` and, if unresolved days remained,
`coverage_unresolved.json` under the same month prefix -- NEW keys, not rewrites. Neither exists: the gate
never ran.)

**ARCHIVE** -- `get-bucket-versioning` on `opal-data-etfs` returned EMPTY (versioning NOT enabled), so the
archive is a `copy-object` of each prior object, verified byte-equal by sha256 on both sides:

| served key (prior) | prior sha256 | bytes | archive key | archive sha256 | byte-equal |
|---|---|---|---|---|---|
| `platinum/reports/2026-08/etf_ownership.html` | `e6b16ef24ae6e997e2b85b3d393d6c60b089b47a4c04e021866ef839c3b3eee5` | 62477 | `platinum/reports/_archive/2026-08/20260909T230636Z/etf_ownership.html` | `e6b16ef24ae6e997e2b85b3d393d6c60b089b47a4c04e021866ef839c3b3eee5` | YES |
| `platinum/reports/2026-08/etf_ownership.pdf` | `e85fe6c5028ac860bb245c968f5e6047b50fc1ea0b7b26f71b8854f9383192e8` | 273857 | `platinum/reports/_archive/2026-08/20260909T230636Z/etf_ownership.pdf` | `e85fe6c5028ac860bb245c968f5e6047b50fc1ea0b7b26f71b8854f9383192e8` | YES |
| `platinum/reports/2026-08/opaletfs_49financial_202608.csv` | `1fba75df7fe50e8b0287c96f2b6be36d9fa8d61ae2f5e0a4f59cbece3e35e3bc` | 1952 | `platinum/reports/_archive/2026-08/20260909T230636Z/opaletfs_49financial_202608.csv` | `1fba75df7fe50e8b0287c96f2b6be36d9fa8d61ae2f5e0a4f59cbece3e35e3bc` | YES |
| `platinum/reports/2026-08/opaletfs_cottonwood_202608.csv` | `98fb455c41a3958610a28bb9161ef9f111d012098f0f8862e3050babf6ebda6a` | 1828 | `platinum/reports/_archive/2026-08/20260909T230636Z/opaletfs_cottonwood_202608.csv` | `98fb455c41a3958610a28bb9161ef9f111d012098f0f8862e3050babf6ebda6a` | YES |
| `platinum/reports/2026-08/opaletfs_inflection_202608.csv` | `f19db318f79821c65144f2996cc2f670b4d47ffcda328c4054ceb666a8296221` | 1828 | `platinum/reports/_archive/2026-08/20260909T230636Z/opaletfs_inflection_202608.csv` | `f19db318f79821c65144f2996cc2f670b4d47ffcda328c4054ceb666a8296221` | YES |

Denominator: 5 of 5 prior objects archived; 5 of 5 byte-equal.

**ARCHIVE LOCATION -- A DEVIATION FROM THE ORDER'S LETTER, DISCLOSED.** The task order names
`platinum/reports/2026-08/_archive_<UTC>/<name>`. The orchestrator's `_month_csv_keys`
(`infra/aws/lambda/etfs-reports-orchestrator/lambda_function.py:265-274`) enumerates
`platinum/reports/2026-08/` WITHOUT a delimiter and attaches EVERY `.csv` under it to the report email --
so an archive inside the month prefix would have put 3 stale duplicate CSVs (same filenames) into the
delivered email to the two real inboxes, damaging the very served delivery this order exists to prove. The
archive therefore sits at `platinum/reports/_archive/2026-08/<UTC>/` -- same bucket, outside the month
prefix's enumeration, nothing deleted, sha256 pairs unchanged. Filed as surprise row
ETFS_GUARDRAIL-W1-S12.

**ROLLBACK** -- one `copy-object` back per key, from the archive to the served key; nothing is deleted.
NOT EXECUTED: measured unnecessary (0 of 5 served objects changed).

```
.tools/aws s3api copy-object --bucket opal-data-etfs \
  --key platinum/reports/2026-08/etf_ownership.html \
  --copy-source opal-data-etfs/platinum/reports/_archive/2026-08/20260909T230636Z/etf_ownership.html
.tools/aws s3api copy-object --bucket opal-data-etfs \
  --key platinum/reports/2026-08/etf_ownership.pdf \
  --copy-source opal-data-etfs/platinum/reports/_archive/2026-08/20260909T230636Z/etf_ownership.pdf
.tools/aws s3api copy-object --bucket opal-data-etfs \
  --key platinum/reports/2026-08/opaletfs_49financial_202608.csv \
  --copy-source opal-data-etfs/platinum/reports/_archive/2026-08/20260909T230636Z/opaletfs_49financial_202608.csv
.tools/aws s3api copy-object --bucket opal-data-etfs \
  --key platinum/reports/2026-08/opaletfs_cottonwood_202608.csv \
  --copy-source opal-data-etfs/platinum/reports/_archive/2026-08/20260909T230636Z/opaletfs_cottonwood_202608.csv
.tools/aws s3api copy-object --bucket opal-data-etfs \
  --key platinum/reports/2026-08/opaletfs_inflection_202608.csv \
  --copy-source opal-data-etfs/platinum/reports/_archive/2026-08/20260909T230636Z/opaletfs_inflection_202608.csv
```

After a rollback, re-read each served object and confirm its sha256 equals the prior sha256 in the table
above. `coverage_verdict.json` / `coverage_unresolved.json`, if a future run writes them, are NEW keys with
no prior version; rollback leaves them in place (NEVER-AUTO-DELETE -- an S3 delete needs a human's word).

**NOTHING IS DELETED BY THIS ENTRY OR ITS ROLLBACK.**

