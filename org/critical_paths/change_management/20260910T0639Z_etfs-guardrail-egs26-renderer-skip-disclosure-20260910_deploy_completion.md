# Deploy Completion Record
**Date opened:** 2026-09-10T06:39:20.314423+00:00
**Status:** OPEN
**Deploy:** EG-s-26 DEPLOY: aws s3 cp of render_month_end.py to the artifact prefix the box pulls by key at run time -- NOT Terraform, NOT a served report key. BLAST RADIUS, the ACT's and measured rather than predicted: EXACTLY ONE key, s3://opal-313476888478-lambda-artifacts/ec2/etfs-reports/render_month_end.py. Nothing else in that prefix is written and platinum/reports/ is not touched by this cell at all. WHO IT REACHES: the next renderer run on the reporter box, which pulls this key fresh on every fire -- the monthly cron and EG-s-21's one permitted driven run. The change is ADDITIVE and BACKWARD COMPATIBLE (new keys INSIDE the existing coverage_verdict.json forcing object, no new CLI flag, no changed flag, no changed decision), so an OLD orchestrator against these NEW bytes behaves exactly as before -- which matters because EG-s-27 is live on 0.9.0_WK_ETFS_GUARDRAIL~4 in parallel and its own deploy is gated on THIS artifact being served, verified by its hash and not by anyone's report. ROLLBACK, exact key-and-bytes, from TWO independent sources verified byte-equal BEFORE the copy: .tools/aws s3api copy-object --bucket opal-313476888478-lambda-artifacts --key ec2/etfs-reports/render_month_end.py --copy-source 'opal-313476888478-lambda-artifacts/ec2/etfs-reports/render_month_end.py?versionId=V1i.w8DNP2iqwsiiRYC7k40Neh90w3DH' ; or re-upload the git blob at HEAD~1. Both read 66880-class bytes at sha256 b08a646d5755f501f10b0b3c8d0512702c20b38e02263dc3b33a2f963d71020f, 66756 B. AUTHORITY: the L6 issuance at 676bb96933 names this act, this key and this rollback and is the COO half; the face rules the artifact prefix a CODE location and not served output, so the never-widen trigger does not fire -- the same standing as EG-s-25, already filed as row W5-S4.
**Authored by:** 0.9.0_WK_ETFS_GUARDRAIL~5
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | the PRIOR object and its rollback, proven BEFORE the copy | prior sha256 + VersionId recorded, and the rollback source cross-checked against an independent git blob |  | OPEN |
| L2 | verify | the copy landed at ec2/etfs-reports/render_month_end.py | served bytes sha256 EQUAL to the committed bytes, both printed, read back from the SERVED object |  | OPEN |
| L3 | verify | nothing else moved in the artifact prefix | full listing before and after with denominators; exactly one key changed |  | OPEN |
| L4 | verify | no send, no invoke, no served-report write | AWS/SES metrics zero, zero Lambda invokes, platinum/reports/ unchanged with its denominator |  | OPEN |
| L5 | verify | the verdict did not move ON BOTH LADDER BRANCHES | class counts and the verdict value identical old-bytes vs new for ladder=True AND ladder=False, denominators printed |  | OPEN |

## Log

- 20260910T063920Z OPENED by 0.9.0_WK_ETFS_GUARDRAIL~5 with 5 leg(s)
