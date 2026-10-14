# Deploy Completion Record
**Date opened:** 2026-10-14T11:29:20.884648+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261014T114741Z
**Deploy:** COMM_ASSIST r18 CA-j-10: four-hour ingress mark (ingress_mark.py + tenant.py) onto module.ldo_001, CODE ONLY, pinned build afa8752f44 -- functions teams-global-chat-assist-handler-lambda and teams-global-chat-assist-ingress-lambda (us-east-1)
**Authored by:** 0.7.0_AE_CloudOps~CA
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | teams-global-chat-assist-handler-lambda code: new CodeSha256 equal to the built package replacing nX67q2k05fh77lG2gBLsNlp6HLAZeELPq85CJpWCVhA=; env unchanged | get-function-configuration CodeSha256 + LastModified + env key names | live get-function-configuration teams-global-chat-assist-handler-lambda: CodeSha256 /amW90t7TNsAAcx8Ap0t/eD7Jgk1HAOXJHCv8t8Mkho= (was nX67q2k05fh77lG2gBLsNlp6HLAZeELPq85CJpWCVhA=), LastModified 2026-10-14T11:35:35Z, CodeSize 295126, env keys 15 unchanged, mode record -- equals the zip built at pin afa8752f44; saved r18c/AFTER_handler_config.json | CLOSED 20261014T113700Z |
| L2 | activation | teams-global-chat-assist-ingress-lambda code: new CodeSha256 equal to the built package replacing nX67q...; env unchanged | get-function-configuration CodeSha256 + LastModified + env key names | live get-function-configuration teams-global-chat-assist-ingress-lambda: CodeSha256 /amW90t7TNsAAcx8Ap0t/eD7Jgk1HAOXJHCv8t8Mkho= (was nX67q...), LastModified 2026-10-14T11:35:41Z, CodeSize 295126, env keys 15 unchanged, mode record -- equals the zip built at pin afa8752f44; saved r18c/AFTER_ingress_config.json | CLOSED 20261014T113700Z |
| L3 | verify | CAj10-AC2 check_j10_live.py PASS plus a targeted re-plan of module.ldo_001 reading no changes | check output + plan tail | CAj10-AC2 check_j10_live.py RESULT: PASS (one new package on both; served zip hash equals CodeSha256 at 295126 B; 6 files equal the pin; INGRESS_MARK_MODE=record and other keys as recorded; secret has a current version, value not read; both roles may read it by simulation; served code round-trips a mark, refuses a tampered one, bounds a mark at 4h with edge_ok and edge_stale, holds marks by age, parses the modes). Targeted re-plan -detailed-exitcode rc=0 'No changes' -- saved r18c/CAj10_REPLAN_AFTER.txt | CLOSED 20261014T113700Z |
| L4 | verify | ingress logs show ingress_poll and mail_poll within 10 minutes of the apply and no mark-secret error | log-line counts (no message content, secret value never read) | log read 2026-10-14T11:47:21Z, 11m40s after the apply: ingress 11 ingress_poll (last 11:46:18Z), 2 mail_poll (last 11:46:21Z, failed=0 refused=0 sent=0), 0 Traceback/ERROR, 0 AccessDenied and 0 ingress-mark lines; handler log group 0 lines (no text arrived); counts only, saved r18c/CAj10_L4_log_read.txt | CLOSED 20261014T114741Z |

## Log

- 20261014T112920Z OPENED by 0.7.0_AE_CloudOps~CA with 4 leg(s)
- 20261014T113700Z LEG L1 closed: live get-function-configuration teams-global-chat-assist-handler-lambda: CodeSha256 /amW90t7TNsAAcx8Ap0t/eD7Jgk1HAOXJHCv
- 20261014T113700Z LEG L2 closed: live get-function-configuration teams-global-chat-assist-ingress-lambda: CodeSha256 /amW90t7TNsAAcx8Ap0t/eD7Jgk1HAOXJHCv
- 20261014T113700Z LEG L3 closed: CAj10-AC2 check_j10_live.py RESULT: PASS (one new package on both; served zip hash equals CodeSha256 at 295126 B; 6 file
- 20261014T114741Z LEG L4 closed: log read 2026-10-14T11:47:21Z, 11m40s after the apply: ingress 11 ingress_poll (last 11:46:18Z), 2 mail_poll (last 11:46
- 20261014T114741Z CLOSED -- all 4 legs proven
