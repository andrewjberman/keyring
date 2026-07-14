# Deploy Completion Record
**Date opened:** 2026-07-14T17:48:13.766944+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260714T180207Z
**Deploy:** NFRA_WEBSITE TO-2 PHASE A: staging cutover new.opalinvest.com (blog_public=0, WP re-key off raw IP, HTTP-01 cert, stage-wire+verify). Public apex/www/email UNTOUCHED.
**Authored by:** 0.7.0_AE_CloudOps~A
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | repo->S3 script parity (9/9 ETag MATCH incl rewritten tls-cutover.sh) | done this session | aws s3 sync + per-file ETag-vs-md5 verify: 9/9 MATCH (tls-cutover.sh a165a0119f98eacc6963441c5a1d59e7 @ repo 127da60f3, clean tree) | CLOSED 20260714T174921Z |
| L2 | verify | A2 blog_public=0 staging hygiene via SSM | wp option get re-read | SSM ba1eaf33: option update + re-read -> blog_public=0 | CLOSED 20260714T175023Z |
| L3 | verify | fresh DB+content backup immediately pre-re-key via SSM | S3 object listed | SSM 8787060c: backup run complete 2026-07-14_175030Z; S3-listed opal_wp_2026-07-14_175030Z.sql.gz 1922029B | CLOSED 20260714T175204Z |
| L4 | verify | A3 wp search-replace http://18.208.18.213 -> https://new.opalinvest.com (dry-run count, live, residual-IP assert 0) | counts | SSM 4f89830a: dry-run 943 -> live 943 replacements; residual-IP dry-run count=0; siteurl+home re-read https://new.opalinvest.com | CLOSED 20260714T175426Z |
| L5 | verify | A4 tls-cutover.sh stage-issue HTTP-01 cert | x509 subject+dates | SSM 6c093f10: certbot HTTP-01 issued; x509 subject CN=new.opalinvest.com issuer LE/YE1 notAfter Oct 12 2026 (after cbd19923d IMDSv2 fix) | CLOSED 20260714T180026Z |
| L6 | verify | A5 tls-cutover.sh stage-wire + on-box strict verify | strict_verify output | SSM 8829e56e: wired+reloaded; positive control 200; box-pinned strict target 200; trusted LE cert CN=new.opalinvest.com | CLOSED 20260714T180134Z |
| L7 | verify | EXTERNAL strict HTTPS fetch of https://new.opalinvest.com/ via public DNS from off-box | curl 200 + trusted chain | off-box strict curl via public DNS: 200 from 18.208.18.213, title 'Opal Capital \| Investment Platform for Independent Advisors' -- real site, trusted chain, no -k | CLOSED 20260714T180207Z |

## Log

- 20260714T174813Z OPENED by 0.7.0_AE_CloudOps~A with 7 leg(s)
- 20260714T174921Z LEG L1 closed: aws s3 sync + per-file ETag-vs-md5 verify: 9/9 MATCH (tls-cutover.sh a165a0119f98eacc6963441c5a1d59e7 @ repo 127da60f3, 
- 20260714T175023Z LEG L2 closed: SSM ba1eaf33: option update + re-read -> blog_public=0
- 20260714T175204Z LEG L3 closed: SSM 8787060c: backup run complete 2026-07-14_175030Z; S3-listed opal_wp_2026-07-14_175030Z.sql.gz 1922029B
- 20260714T175426Z LEG L4 closed: SSM 4f89830a: dry-run 943 -> live 943 replacements; residual-IP dry-run count=0; siteurl+home re-read https://new.opalin
- 20260714T180026Z LEG L5 closed: SSM 6c093f10: certbot HTTP-01 issued; x509 subject CN=new.opalinvest.com issuer LE/YE1 notAfter Oct 12 2026 (after cbd19
- 20260714T180134Z LEG L6 closed: SSM 8829e56e: wired+reloaded; positive control 200; box-pinned strict target 200; trusted LE cert CN=new.opalinvest.com
- 20260714T180207Z LEG L7 closed: off-box strict curl via public DNS: 200 from 18.208.18.213, title 'Opal Capital | Investment Platform for Independent Ad
- 20260714T180207Z CLOSED -- all 7 legs proven
