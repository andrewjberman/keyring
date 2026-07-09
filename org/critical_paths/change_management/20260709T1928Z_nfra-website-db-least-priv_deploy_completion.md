# Deploy Completion Record
**Date opened:** 2026-07-09T19:28:43.239767+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260709T192905Z
**Deploy:** NFRA_WEBSITE W1 req-2: enforce least-priv on WP DB user opal_wp (ALL PRIVILEGES ON *.* -> opal_wp.* only)
**Authored by:** 0.7.0_AE_CloudOps~A
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 8.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD commit: db-least-priv.sh + bootstrap-stack.sh regex-fix + harden.sh 3.5 + dispatch.sh | hash pushed | f05629cf5 pushed to CLOUD (db-least-priv.sh new + bootstrap-stack.sh:265-283 detect->assert + harden.sh 3.5 + dispatch.sh dbpriv step/allowlist) | CLOSED 20260709T192904Z |
| L2 | s3-prefix | scripts staged to s3://opal-website-backups/code/website/ | aws s3 ls db-least-priv.sh + updated dispatch.sh | s3://opal-website-backups/code/website/db-least-priv.sh (4068B) + dispatch.sh (2055B) staged 2026-07-09T19:21-22Z; aws s3 ls confirmed | CLOSED 20260709T192904Z |
| L3 | ec2-baked-asset | box pulls dispatch.sh + runs dbpriv step (S3->box, Rule 12); grant converged | SSM Success + POST grants USAGE ON *.* + ALL ON opal_wp.* | SSM d940719c i-0152e3fe2599fa630 Success: dispatch.sh dbpriv -> PRE=[ALL ON *.* + ALL ON opal_wp.*] POST=[USAGE ON *.* + ALL ON opal_wp.*]; script hard-verified no residual global priv | CLOSED 20260709T192904Z |
| L4 | verify | EXERCISED: WP reads/writes/DDLs its DB under the scoped grant + independent SHOW GRANTS shows no global priv | SSM exercise transcript | SSM 65432760 EXERCISED (Rule 22a): independent SHOW GRANTS=USAGE ON *.* + ALL ON opal_wp.*; wp option get siteurl=http://18.208.18.213 (read); option add/get/delete _ae_leastpriv_probe (write); mysql CREATE/DROP _ae_probe on opal_wp.* (DDL) all OK; site 200 home/wp-login/wp-json post-change | CLOSED 20260709T192905Z |

## Log

- 20260709T192843Z OPENED by 0.7.0_AE_CloudOps~A with 4 leg(s)
- 20260709T192904Z LEG L1 closed: f05629cf5 pushed to CLOUD (db-least-priv.sh new + bootstrap-stack.sh:265-283 detect->assert + harden.sh 3.5 + dispatch.s
- 20260709T192904Z LEG L2 closed: s3://opal-website-backups/code/website/db-least-priv.sh (4068B) + dispatch.sh (2055B) staged 2026-07-09T19:21-22Z; aws s
- 20260709T192904Z LEG L3 closed: SSM d940719c i-0152e3fe2599fa630 Success: dispatch.sh dbpriv -> PRE=[ALL ON *.* + ALL ON opal_wp.*] POST=[USAGE ON *.* +
- 20260709T192905Z LEG L4 closed: SSM 65432760 EXERCISED (Rule 22a): independent SHOW GRANTS=USAGE ON *.* + ALL ON opal_wp.*; wp option get siteurl=http:/
- 20260709T192905Z CLOSED -- all 4 legs proven
