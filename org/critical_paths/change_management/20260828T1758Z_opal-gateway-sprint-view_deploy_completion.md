# Deploy Completion Record
**Date opened:** 2026-08-28T17:58:26.086123+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260828T181844Z
**Deploy:** Daily Sprint web client: /sprint on opal-gateway (ALB Entra OIDC wall) + daily-reports S3 read grant + publisher -- Andrew-direct 2026-08-28, recs approved, build solo
**Authored by:** 1.0.0_SA_CTO~D
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD commit of app/sprint_view.py + server.py/config.py wiring + daily-reports-iam.tf + tests + publisher + skill/README | commit hash | 97b8103069 (infra lane, GIT_COMMIT_AUTHOR_OVERRIDE=CLOUD_OPS_OR_ETL audited; 5 files) + d19943c4c2 (publisher + skill + README; 3 files), both author 1.0.0_SA_CTO~D, on CLOUD; git log -2 read back. Push state at close: LOCAL (UNREAD) | CLOSED 20260828T181226Z |
| L2 | activation | safe-apply aws_iam_role_policy.gw_daily_reports_read (plan 1 add/0 change/0 destroy) | apply rc + 0-diff re-plan + simulate-principal-policy GetObject on the exact key (one resource per call) + negative control on a sibling prefix | safe-apply.sh apply rc=0 (SAFE_APPLY_TERRAFORM=winget tf 1.14.5, the state-compatible binary; .tools/terraform.exe 1.9.8 could not init the backend). aws_iam_role_policy.gw_daily_reports_read created id=opal-gateway-role:opal-gateway-daily-reports-read. Re-plan -detailed-exitcode rc=0 'No changes'. LIVE simulate-principal-policy, ONE resource per call: GetObject daily-reports/2026-08-27/Desktop_DAILY_REPORT_2026-08-27.html -> allowed; GetObject not-daily-reports/x.html -> implicitDeny; ListBucket ctx s3:prefix=daily-reports/ -> allowed; ctx s3:prefix=platinum/ -> implicitDeny | CLOSED 20260828T180956Z |
| L3 | ec2-baked-asset | opal-gateway code deploy via safe-ec2-deploy.sh (S3 artifact -> SSM pull -> systemd restart) | on-box: systemd active, /health 200, md5 of /opt/opal-gateway/app/sprint_view.py == repo bytes | safe-ec2-deploy.sh rc=0 18:14:20Z (jq resolved from .tools; manifest row committed separately under SHARED_CLOUD_OPS override). SSM 150f9ad2 read-only: md5 on-box == local for app/sprint_view.py f2195b70, server.py 9ba5c40f, config.py 8b63cced (3/3); systemd active, ActiveEnterTimestamp 18:14:08Z; on-box /health 200. Manifest commit a7924a32 = HEAD at tar time (two peer commits landed between mine and the deploy; 97b8103069 is its ancestor) | CLOSED 20260828T181751Z |
| L4 | verify | the wall + the route through the ALB | unauthenticated GET https://mcp.opalinvest.dev/sprint -> 302 to login.microsoftonline.com/<tenant>; on-box GET /sprint without x-amzn-oidc-data -> 401 (fail-closed); /health unchanged | THROUGH ALB unauth: GET /sprint, /sprint/2026-08-27, /sprint/archive -> 302 Location login.microsoftonline.com/6810043e-d171-4adc-9975-068b35e179da/oauth2/v2.0/authorize?client_id=53360468... (x3); negative control /.well-known/oauth-authorization-server -> 200 (bypass rule intact). ON-BOX no x-amzn-oidc-data: /sprint 401, /sprint/2026-08-27 401 (fail-closed), /sprintfoo 404 (precise predicate), /health 200 | CLOSED 20260828T181752Z |
| L5 | verify | first publish: 2026-08-27 pages served from the ruled prefix | publish_daily_report.py read-back MATCH x2 + gateway ListBucket sees the DAY prefix | publish_daily_report.py --date 2026-08-27: Desktop 39689 B etag MATCH, Mobile 37812 B etag MATCH (read-back). s3api list (laptop cred) shows both keys 18:12:42Z. INSTANCE ROLE (SSM): list-objects-v2 delimiter / -> CommonPrefixes daily-reports/2026-08-27/; head-object Mobile -> 37812, ETag 6bd54d69cd4a... == publisher md5. Sibling-prefix negative on-box UNREAD (CLI error's leading blank line ate head -1); that axis rests on L2's simulate implicitDeny | CLOSED 20260828T181752Z |

## Log

- 20260828T175826Z OPENED by 1.0.0_SA_CTO~D with 5 leg(s)
- 20260828T180956Z LEG L2 closed: safe-apply.sh apply rc=0 (SAFE_APPLY_TERRAFORM=winget tf 1.14.5, the state-compatible binary; .tools/terraform.exe 1.9.8
- 20260828T181226Z LEG L1 closed: 97b8103069 (infra lane, GIT_COMMIT_AUTHOR_OVERRIDE=CLOUD_OPS_OR_ETL audited; 5 files) + d19943c4c2 (publisher + skill + 
- 20260828T181751Z LEG L3 closed: safe-ec2-deploy.sh rc=0 18:14:20Z (jq resolved from .tools; manifest row committed separately under SHARED_CLOUD_OPS ove
- 20260828T181752Z LEG L4 closed: THROUGH ALB unauth: GET /sprint, /sprint/2026-08-27, /sprint/archive -> 302 Location login.microsoftonline.com/6810043e-
- 20260828T181752Z LEG L5 closed: publish_daily_report.py --date 2026-08-27: Desktop 39689 B etag MATCH, Mobile 37812 B etag MATCH (read-back). s3api list
- 20260828T181844Z CLOSED -- all 5 legs proven
