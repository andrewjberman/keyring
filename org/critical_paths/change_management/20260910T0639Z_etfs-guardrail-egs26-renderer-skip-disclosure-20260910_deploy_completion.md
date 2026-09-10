# Deploy Completion Record
**Date opened:** 2026-09-10T06:39:20.314423+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260910T123237Z
**Deploy:** EG-s-26 DEPLOY: aws s3 cp of render_month_end.py to the artifact prefix the box pulls by key at run time -- NOT Terraform, NOT a served report key. BLAST RADIUS, the ACT's and measured rather than predicted: EXACTLY ONE key, s3://opal-313476888478-lambda-artifacts/ec2/etfs-reports/render_month_end.py. Nothing else in that prefix is written and platinum/reports/ is not touched by this cell at all. WHO IT REACHES: the next renderer run on the reporter box, which pulls this key fresh on every fire -- the monthly cron and EG-s-21's one permitted driven run. The change is ADDITIVE and BACKWARD COMPATIBLE (new keys INSIDE the existing coverage_verdict.json forcing object, no new CLI flag, no changed flag, no changed decision), so an OLD orchestrator against these NEW bytes behaves exactly as before -- which matters because EG-s-27 is live on 0.9.0_WK_ETFS_GUARDRAIL~4 in parallel and its own deploy is gated on THIS artifact being served, verified by its hash and not by anyone's report. ROLLBACK, exact key-and-bytes, from TWO independent sources verified byte-equal BEFORE the copy: .tools/aws s3api copy-object --bucket opal-313476888478-lambda-artifacts --key ec2/etfs-reports/render_month_end.py --copy-source 'opal-313476888478-lambda-artifacts/ec2/etfs-reports/render_month_end.py?versionId=V1i.w8DNP2iqwsiiRYC7k40Neh90w3DH' ; or re-upload the git blob at HEAD~1. Both read 66880-class bytes at sha256 b08a646d5755f501f10b0b3c8d0512702c20b38e02263dc3b33a2f963d71020f, 66756 B. AUTHORITY: the L6 issuance at 676bb96933 names this act, this key and this rollback and is the COO half; the face rules the artifact prefix a CODE location and not served output, so the never-widen trigger does not fire -- the same standing as EG-s-25, already filed as row W5-S4.
**Authored by:** 0.9.0_WK_ETFS_GUARDRAIL~5
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | the PRIOR object and its rollback, proven BEFORE the copy | prior sha256 + VersionId recorded, and the rollback source cross-checked against an independent git blob | PROVEN, and cross-verified from TWO INDEPENDENT SOURCES rather than one source twice. PRIOR OBJECT s3://opal-313476888478-lambda-artifacts/ec2/etfs-reports/render_month_end.py VersionId V1i.w8DNP2iqwsiiRYC7k40Neh90w3DH, 66756 B, LastModified 2026-09-10T05:19:37Z, sha256 b08a646d5755f501f10b0b3c8d0512702c20b38e02263dc3b33a2f963d71020f -- recorded in this entry and in egs26_deploy_evidence.json step 2 (HEAD the key BEFORE, argv verbatim, rc 0) BEFORE the copy at step 3. INDEPENDENT SECOND SOURCE: git blob 32ae4ede66:data/etfs/scripts/presentation/render_month_end.py reads the SAME 66756 B and the SAME sha256 -- a different instrument on a different plane, not the same command twice. ROLLBACK, exact restore, one command, no rebuild: .tools/aws s3api copy-object --bucket opal-313476888478-lambda-artifacts --key ec2/etfs-reports/render_month_end.py --copy-source 'opal-313476888478-lambda-artifacts/ec2/etfs-reports/render_month_end.py?versionId=V1i.w8DNP2iqwsiiRYC7k40Neh90w3DH'. THE ROLLBACK IS A REAL RESTORE AND NOT A NO-OP: the prior sha256 DIFFERS from the served sha256 (b08a646d... vs 9b9cdd9c...), printed as arm (f)'s negative control. Re-measured at the re-seat's own instrument, not carried forward from the dead session. Battery arm (f), egs26_battery_output.txt. | CLOSED 20260910T123224Z |
| L2 | verify | the copy landed at ec2/etfs-reports/render_month_end.py | served bytes sha256 EQUAL to the committed bytes, both printed, read back from the SERVED object | PROVEN BY READING THE SERVED OBJECT, and the entry's ORIGINAL verifier for this leg was WRONG and is disclosed rather than quietly replaced -- see row ETFS_GUARDRAIL-W5-S8. SERVED: fresh head-object + get-object at the re-seat return VersionId TkhI7NPt_hpJUaXYAlBnjZggJQDz.wBG, 69879 B, LastModified 2026-09-10T06:40:10Z, sha256 9b9cdd9c39cbe92bbcb94c9550eebcf924b0f18744b81c61c3f66cfe75237a76. COMMITTED: git blob 5b15b09834:data/etfs/scripts/presentation/render_month_end.py, 69879 B, sha256 9b9cdd9c39cbe92bbcb94c9550eebcf924b0f18744b81c61c3f66cfe75237a76. EQUAL, both sides printed. NEGATIVE CONTROL so the equality discriminates: the prior version reads 66756 B / b08a646d... and DIFFERS, so this is a measurement and not a tautology. THE ACT IS WORLD-DONE AND WAS NOT RE-EXECUTED: the copy landed 06:40:10Z, the device rebooted 06:43:35Z, and CLAUDE.md NEVER-2 rules that a world-done act closes SUPERSEDED because a re-execute of an overtaken promote is a REWIND. NO COPY WAS ISSUED BY THE RE-SEAT; every AWS call it made is a READ. The evidence file's own served_sha256/served_bytes/served_equals_committed fields are FALSE (the verifier hashed the previous cell's download at egs26_deploy.py:130) and are left in place under a `corrections` block, because deleting a wrong measurement deletes the evidence that the instrument can fail that way. Battery arm (f), egs26_battery_output.txt. | CLOSED 20260910T123224Z |
| L3 | verify | nothing else moved in the artifact prefix | full listing before and after with denominators; exactly one key changed | PROVEN WITH DENOMINATORS ON BOTH SIDES AND ACROSS THE CRASH WINDOW. DURING THE ACT: s3://opal-313476888478-lambda-artifacts/ec2/etfs-reports/ listed 7 key(s) before and 7 after; EXACTLY 1 of 7 changed, ec2/etfs-reports/render_month_end.py, 66756 B -> 69879 B. No key added, none removed. SINCE THE ACT, spanning the 06:43:35Z reboot to the grading read at 12:2xZ: 0 of 7 key(s) moved, compared by ETag AND Size. ZERO GUARD, because an empty listing and an untouched population are the same value and only one of them is evidence: both listings are asserted NON-EMPTY (7 now, 7 baseline) before any delta is graded -- an earlier draft of the battery pointed the reports listing at the wrong bucket and got 0 keys with rc 0, which would have read as 'nothing to move' instead of 'wrong object'. Battery arm (f), egs26_battery_output.txt. | CLOSED 20260910T123224Z |
| L4 | verify | no send, no invoke, no served-report write | AWS/SES metrics zero, zero Lambda invokes, platinum/reports/ unchanged with its denominator | PROVEN ON THREE AXES WITH TWO DIFFERENT INSTRUMENTS, and the SES claim is scoped BEFORE its number rather than after. (1) NO SERVED-REPORT WRITE: s3://opal-data-etfs/platinum/reports/ listed 36 key(s) at 06:40:03Z before the act and 36 NOW; delta across the act = 0 key(s); delta before-the-act -> now, which SPANS the act AND the whole crash window, = 0 of 36 key(s), compared by ETag and Size, listing asserted non-empty first. (2) NO SES SEND: the claim is TIME OVERLAP, not a whole-day zero -- a whole-day zero would be a false claim, since other seats send legitimate mail and grading this act on their traffic would convict it of their sends. Every SES datapoint of the UTC day is enumerated with its 5-minute bucket: Send buckets at 00:20Z (2.0), 01:20Z (2.0), 11:40Z (3.0), whole-day total 7.0; NONE overlaps the act window 06:39:20Z-06:40:19Z. Second read at a different grain: the server-side narrow query StartTime=06:39:00Z EndTime=06:41:00Z returns datapoints=0 sum=0, and the two agree. (3) NO LAMBDA INVOKE: AWS/Lambda Invocations over 06:39:00Z-06:41:00Z, DENOMINATOR BY SUBTRACTION and never by recall -- 203 function(s) exist in this account MINUS the 190 whose name carries neither 'etf' nor 'report' = 13 checked, all sum=0. SECOND INSTRUMENT ON A DIFFERENT AXIS, because CloudWatch measures what FIRED and this measures what was ISSUED: a census of the verbatim argv of all 11 recorded steps returns AWS services {cloudwatch, s3api} and 0 of 11 steps touching anything else -- no `aws lambda`, no `aws ses`, no `aws ssm`. RESIDUAL STATED: a function named with neither token could in principle have fired; the argv census is what bounds that, since a step that never called `aws lambda` cannot have invoked anything. Battery arm (f), egs26_battery_output.txt. | CLOSED 20260910T123224Z |
| L5 | verify | the verdict did not move ON BOTH LADDER BRANCHES | class counts and the verdict value identical old-bytes vs new for ladder=True AND ladder=False, denominators printed | PROVEN ON BOTH LADDER BRANCHES WITH THE BEFORE SIDE LOADED FROM THE DEPLOYED PRE BYTES, not from a description of them. BEFORE = the object that WAS served, VersionId V1i.w8DNP2iqwsiiRYC7k40Neh90w3DH (66756 B, sha256 b08a646d...), fetched from S3 by version id and imported as a module with subprocess.run poisoned across the load so the renderer's own `aws s3 cp` box-bootstrap could not fire silently -- it did not fire. AFTER = data/etfs/scripts/presentation/render_month_end.py in this worktree. DENOMINATOR: 2 scenario(s) x 2 ladder branch(es) x 7 quantity(ies) (verdict, holes, A, B, C, D, UNKNOWN) = 28 compared quantities, plus 4 producer-invoke counts. RESULT: 28 of 28 IDENTICAL and 4 of 4 invoke counts identical. COMPLETE month -> PUBLISH, holes 0, C 0 on both branches; 5 REMOVED -> REFUSE, holes 5, C 5 on both branches; rung-1 invokes 5 on ladder=True and 0 on ladder=False, the same in both modules, so the ladder took the same path either side of the change. NEGATIVE CONTROL ON THE COMPARATOR ITSELF, so 'identical' is a measurement and not a constant: the two scenarios DISAGREE with each other (complete -> PUBLISH, 5 removed -> REFUSE), which means the comparator can report a difference and chose not to. Additionally 25 of 25 tests pass in the renderer's own suite, data/etfs/scripts/presentation/tests/, rc 0. Battery arm (e), egs26_battery_output.txt. | CLOSED 20260910T123224Z |

## Log

- 20260910T063920Z OPENED by 0.9.0_WK_ETFS_GUARDRAIL~5 with 5 leg(s)
- 20260910T123224Z LEG L1 closed: PROVEN, and cross-verified from TWO INDEPENDENT SOURCES rather than one source twice. PRIOR OBJECT s3://opal-31347688847
- 20260910T123224Z LEG L2 closed: PROVEN BY READING THE SERVED OBJECT, and the entry's ORIGINAL verifier for this leg was WRONG and is disclosed rather th
- 20260910T123224Z LEG L3 closed: PROVEN WITH DENOMINATORS ON BOTH SIDES AND ACROSS THE CRASH WINDOW. DURING THE ACT: s3://opal-313476888478-lambda-artifa
- 20260910T123224Z LEG L4 closed: PROVEN ON THREE AXES WITH TWO DIFFERENT INSTRUMENTS, and the SES claim is scoped BEFORE its number rather than after. (1
- 20260910T123224Z LEG L5 closed: PROVEN ON BOTH LADDER BRANCHES WITH THE BEFORE SIDE LOADED FROM THE DEPLOYED PRE BYTES, not from a description of them. 
- 20260910T123237Z CLOSED -- all 5 legs proven

---

## CLOSING STANDING: SUPERSEDED, NOT RE-EXECUTED

**The act reached the world before this entry reached the record, and the entry was closed
against the ARTIFACT rather than re-run.**

| fact | value | measured how |
|---|---|---|
| entry opened | `2026-09-10T06:39:20Z` | this file's own `opened_at` |
| copy landed | `2026-09-10T06:40:10Z` | `head-object` `LastModified` on the key |
| device rebooted | `2026-09-10T06:43:35Z` | RMM agent at 06:35:24Z, then an OS upgrade |
| entry committed | `2026-09-10T12:0xZ`, commit `b92263aa50` | the commit that created this file in git |
| entry closed | `2026-09-10T12:32:37Z` | `deploy_ledger.py close`, log line above |

**WHAT HAPPENED.** The acting session put the new renderer bytes at 06:40:10Z -- 50 seconds after
this entry opened -- and was killed 3m25s later when the device rebooted twice. The entry, its
completion doc and the deploy evidence were left STAGED-but-uncommitted and UNTRACKED respectively,
so for 5h21m the world had moved and **nothing in the repo recorded it**. A re-seat on the same
worker slot, `0.9.0_WK_ETFS_GUARDRAIL~5`, committed the record at `b92263aa50` and closed the entry
here.

**WHY SUPERSEDED AND NOT RE-EXECUTED.** CLAUDE.md NEVER-2: *an entry a device left OPEN proves only
that THIS device saw no completion* -- so measure the ARTIFACT, and *world-done -> close SUPERSEDED,
never re-execute (a re-execute of an overtaken promote is a REWIND)*. The artifact was measured at
the re-seat's own instrument, not carried forward from the dead session's report:

```
SERVED    s3://opal-313476888478-lambda-artifacts/ec2/etfs-reports/render_month_end.py
          VersionId TkhI7NPt_hpJUaXYAlBnjZggJQDz.wBG   69879 B   LastModified 2026-09-10T06:40:10Z
          sha256    9b9cdd9c39cbe92bbcb94c9550eebcf924b0f18744b81c61c3f66cfe75237a76
COMMITTED git blob 5b15b09834:data/etfs/scripts/presentation/render_month_end.py
          69879 B   sha256 9b9cdd9c39cbe92bbcb94c9550eebcf924b0f18744b81c61c3f66cfe75237a76   EQUAL

NEGATIVE CONTROL, so the equality discriminates rather than passing vacuously:
PRIOR     VersionId V1i.w8DNP2iqwsiiRYC7k40Neh90w3DH   66756 B
          sha256    b08a646d5755f501f10b0b3c8d0512702c20b38e02263dc3b33a2f963d71020f
          and git blob 32ae4ede66:...render_month_end.py reads the SAME 66756 B / b08a646d...
          BOTH DIFFER from the served bytes.
```

**NO COPY, NO PUT AND NO INVOKE WAS ISSUED BY THE RE-SEAT.** Every AWS call it made is a read:
`head-object`, `get-object`, `list-objects-v2`, `get-metric-statistics`. The five legs above are
closed on those reads.

**THREE SURPRISE ROWS CARRY WHAT THIS ENTRY CANNOT.**
`ETFS_GUARDRAIL-W5-S8` -- the original verifier for leg L2 hashed the PREVIOUS cell's download
(`egs26_deploy.py:129` downloads to one path, `:130` reads another), so it wrote
`served_equals_committed: false` about an object it never read, with rc=0 on all 11 steps. The wrong
values are preserved in `egs26_deploy_evidence.json` under a `corrections` block rather than deleted.
`ETFS_GUARDRAIL-W5-S9` -- the acceptance clause that names its object as "currently served" stopped
naming the object carrying the absence, because this cell's own deploy replaced it.
`ETFS_GUARDRAIL-W5-S10` -- this entry could not be "closed BEFORE the grading reads" as its task
order requires, and the RED window alarm cannot see the interval between an act reaching the world
and its entry reaching the record.

**ROLLBACK REMAINS LIVE AND EXACT** (leg L1): restore VersionId
`V1i.w8DNP2iqwsiiRYC7k40Neh90w3DH` by `copy-object` on the same key, or re-upload git blob
`32ae4ede66:data/etfs/scripts/presentation/render_month_end.py`. Both restore 66756 B /
`b08a646d5755f501f10b0b3c8d0512702c20b38e02263dc3b33a2f963d71020f`.
