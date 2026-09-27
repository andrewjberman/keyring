# Deploy Completion Record
**Date opened:** 2026-09-27T18:13:46.059552+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260927T192028Z
**Deploy:** IRPT_BCKEND-S158: cot BD session auto-login succeeds again (log-on-failure + named cause fix)
**Authored by:** 0.6.2_AE_PartnerETL~S
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | read the box's own /tmp/cot-session-autologin-*.log via SSM and name the cause per failed day | ssm:<command_id> + the deliverable JSON path | READ, and the result is an ABSENCE not a cause. ssm:a9742a7d-f5fe-45db-8f80-18bea2dde130 + ssm:0dc8e587-3222-4173-870b-0f9ed47dc99e + ssm:3aab9ee3-5dd9-4cfe-a532-288052637758 on i-0643a5bee8a8feabf. /tmp is tmpfs (findmnt -> tmpfs; df -h -> 3.9G/0 used); 0 files match /tmp/cot-session-autologin-*.log and 0 match /tmp/*.log. S3 session-fetch prefix: 12 objects, newest 20260916-113031 (the last Success), nothing for 09-24..09-27, with the 09-16 object as the positive control. Persistent SSM orchestration: 42 dirs, all 4 failed command ids present, stdout AND stderr empty in 4 of 4. Screenshot carrier ruled out (BD_DEBUG_SHOTS unset, grep -c -> 0). Per-day cause UNMEASURABLE; recorded as IRPT_BCKEND-S164; deliverable org/tier2_senior/0.6.2_AE_PartnerETL/deliverables/IRPT_BCKEND_S158_CAUSE_20260927.json | CLOSED 20260927T192002Z |
| L2 | git | ssm.tf step uploads the log on failure (exit code captured without set -e aborting first) committed on CLOUD | commit hash + push state | CLOUD de68b15717 (author 0.6.2_AE_PartnerETL~S), 3 files changed; msg-verify MATCH len=2961; push state measured below at send time | CLOSED 20260927T183936Z |
| L3 | activation | safe-apply of aws_ssm_document.cot_bd_session_fetch so the LIVE document carries the log-on-failure step | aws ssm get-document read of the live Content | safe-apply 0 added/1 changed/0 destroyed (tagauthz PASSED, tombstone CLEAN); LIVE read-back aws ssm get-document opal-cot-bd-session-fetch -> DefaultVersion=5 LatestVersion=5 Active; runCommand line 7 './run-bd-auto-login.sh > $LOG_FILE 2>&1 \|\| EXIT_CODE=$?', line 8 'tail -25 $LOG_FILE \|\| true', line 10 'exit $EXIT_CODE' -- AC2 met on the live plane | CLOSED 20260927T183937Z |
| L4 | ec2-baked-asset | the named cause fixed inside the grant and S3->box deployed to /opt/bd-cot-auto-login | SSM cat/md5 of the RUNNING path | VACATED -- NO ACT TAKEN, NOTHING LANDED ON THE BOX. This leg presupposed a named cause; the reproduction through the trigger Lambda SUCCEEDED (ssm:cf7fdead-a0df-4024-b5a0-30d4974858db rc 0), so no cause was named and none was fixed. Deployed-bytes audit run anyway (rule 22a, md5 of the RUNNING path vs the build input): /opt/bd-cot-auto-login/run-bd-auto-login.sh md5 a10ac98ada74e0539b987cb30c8fd979 == repo a10ac98ada74e0539b987cb30c8fd979, so there was nothing to push even had a cause been found there. secret-ids.env and bd_49f_auto_login.js DIFFER from the repo and are recorded as IRPT_BCKEND-S165/S166 rather than changed -- both remedies sit outside this order's grant. | CLOSED 20260927T192003Z |
| L5 | verify | ONE Success of opal-cot-bd-session-fetch that moves blackdiamond/cot/session AWSCURRENT | ssm:<command_id> Success + the new AWSCURRENT version id/CreatedDate | ssm:cf7fdead-a0df-4024-b5a0-30d4974858db Status Success rc 0, ran 2026-09-27T18:40:53.956Z -> 18:42:27.956Z, fired via aws lambda invoke cot-bd-session-trigger {mode:session-refresh} (the document's own trigger, never a hand sign-in). AWSCURRENT MOVED: e9259045-d182-42e9-ac0c-e03c090c9d8c (2026-09-16T11:33:35.346Z, 11 days stale) -> 9da4e781-7f11-4cf0-b2dd-2980e56db1db (2026-09-27T18:42:27.771Z), written INSIDE the Success window so attributable to that run alone. Chain released: opal-cot-bronze-run ssm:590ed628 Success, opal-cot-silver-run ssm:907f9f8e Success, opal-cot-gold-run ssm:4fad5c7a Success rc 0. | CLOSED 20260927T192003Z |

## Log

- 20260927T181346Z OPENED by 0.6.2_AE_PartnerETL~S with 5 leg(s)
- 20260927T183936Z LEG L2 closed: CLOUD de68b15717 (author 0.6.2_AE_PartnerETL~S), 3 files changed; msg-verify MATCH len=2961; push state measured below a
- 20260927T183937Z LEG L3 closed: safe-apply 0 added/1 changed/0 destroyed (tagauthz PASSED, tombstone CLEAN); LIVE read-back aws ssm get-document opal-co
- 20260927T192002Z LEG L1 closed: READ, and the result is an ABSENCE not a cause. ssm:a9742a7d-f5fe-45db-8f80-18bea2dde130 + ssm:0dc8e587-3222-4173-870b-0
- 20260927T192003Z LEG L4 closed: VACATED -- NO ACT TAKEN, NOTHING LANDED ON THE BOX. This leg presupposed a named cause; the reproduction through the tri
- 20260927T192003Z LEG L5 closed: ssm:cf7fdead-a0df-4024-b5a0-30d4974858db Status Success rc 0, ran 2026-09-27T18:40:53.956Z -> 18:42:27.956Z, fired via a
- 20260927T192028Z CLOSED -- all 5 legs proven
