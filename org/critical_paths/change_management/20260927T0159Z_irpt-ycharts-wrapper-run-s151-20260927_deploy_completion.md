# Deploy Completion Record
**Date opened:** 2026-09-27T01:59:56.671790+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260927T020538Z
**Deploy:** S151: ONE run of the YCharts session-capture wrapper on i-0167fd745ad906a66 to measure receive 1's failure cause (Andrew-direct via CTO 101694, record @60ffa353f1); no vendor write, no retry
**Authored by:** 2.0.0_SA_COO~Y
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 1.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| R1 | verify | one run of /opt/investor-reporting-ycharts/run-ycharts-session.sh (task probe) as ec2-user on i-0167fd745ad906a66 | rc + the runner receipt (ok/failure_class or authenticated), scrubbed; runner lease _opal/ycharts-session fence before 12 and after; ycharts/session/current version before 02e53a44 and after; queue 0/0 before and after; 0 vendor writes | ONE run, SSM 29cacb70 02:02:13-02:02:25Z: WRAPPER_RC=0; receipt ok=true task=probe result authenticated=true reason=OK http 200; steps CH-SIGNIN_FORM -> CH-AUTHENTICATED; runner lease _opal/ycharts-session fence 12 -> 13, released (expires 0); ycharts/session/current 02e53a44 (fence 11) -> d38f6941 AWSCURRENT (fence 13, captured 02:02:23Z), 02e53a44 now AWSPREVIOUS; queue irpt-generation 0/0 before and after; 0 vendor writes (probe task only); resident env HOME=/home/ec2-user PATH includes /usr/bin (same as this run): receive-1's failure not reproduced | CLOSED 20260927T020538Z |

## Log

- 20260927T015956Z OPENED by 2.0.0_SA_COO~Y with 1 leg(s)
- 20260927T020538Z LEG R1 closed: ONE run, SSM 29cacb70 02:02:13-02:02:25Z: WRAPPER_RC=0; receipt ok=true task=probe result authenticated=true reason=OK h
- 20260927T020538Z CLOSED -- all 1 legs proven
