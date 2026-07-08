# Deploy Completion Record
**Date opened:** 2026-07-08T17:31:35.168714+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260708T182328Z
**Deploy:** NFRA_WEBSITE W1: EC2+EIP+SG+IAM+S3 (15 res) + OLS/PHP8/MariaDB-local/WP stack + Patricia WP-admin
**Authored by:** 0.7.0_AE_CloudOps~A
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD TF ec1148124 + stack scripts 156a97ff2 pushed | both hashes on CLOUD | TF ec1148124 + stack scripts 156a97ff2 both on CLOUD (push up-to-date) | CLOSED 20260708T174203Z |
| L2 | verify | 15 website resources applied via safe-apply + 0-diff re-plan | apply summary 15/0/0 + 0-diff | safe-apply(HALTGT): 15 added/0 changed/0 destroyed; re-plan = No changes (0-diff). Outputs: instance i-0152e3fe2599fa630, EIP 18.208.18.213, sg-062bbb40a6c92509c, role opal-website-wp-role | CLOSED 20260708T174204Z |
| L3 | ec2-baked-asset | stack scripts staged s3 ec2/website/ + installed on box | SSM md5/cat of running scripts | Stack scripts staged s3://opal-website-backups/code/website/ (5 .sh); SSM install SUCCESS d46bd5c5: OLS+LSPHP8.2+MariaDB11.8+WP installed, wp core install ok, ols1clk 4/4 smoke passed, docroot /usr/local/lsws/wordpress, least-priv DB opal_wp confirmed, localhost / + /wp-login.php = 200 | CLOSED 20260708T180901Z |
| L4 | verify | WP serves + live SG NO 0.0.0.0/0:22 + SSM reaches box exercised | describe-SG + SSM invocation + curl | EXERCISED (Rule 22a): public http://18.208.18.213/ = 200 OK server:LiteSpeed (WP live via SG-80); /wp-login.php = 200; live describe-security-groups = only 80+443 from 0.0.0.0/0, ZERO port-22 rules; SSM RunCommand executes on box (Ping Online, multiple commands Success) = SSM Session Manager reaches box with no SSH | CLOSED 20260708T180934Z |
| L5 | verify | Patricia WP-admin created WP-only + one-time reset link | wp user get + delivery block | WP-admin 'patricia' <patricia@thewhitelabelcreative.com> created as administrator (SSM cmd, WP-only, no AWS on the WP account); idempotent. Reset-link generation + ALL delivery HELD per Andrew-direct 2026-07-08 (do not send yet). Separately: Andrew-direct scoped AWS IAM for Patricia now built (iam_patricia.tf, apply held for scope-GO). | CLOSED 20260708T182328Z |
| L6 | verify | EC2_MANIFEST opal-website-wp registered + infra/website inventory filled | manifest entry + table | EC2_MANIFEST opal-website-wp registered (i-0152e3fe2599fa630, commit 1eba880d3); infra/website README resource-inventory filled with live ids (instance/EIP/SG/role/bucket) | CLOSED 20260708T182328Z |

## Log

- 20260708T173135Z OPENED by 0.7.0_AE_CloudOps~A with 6 leg(s)
- 20260708T174203Z LEG L1 closed: TF ec1148124 + stack scripts 156a97ff2 both on CLOUD (push up-to-date)
- 20260708T174204Z LEG L2 closed: safe-apply(HALTGT): 15 added/0 changed/0 destroyed; re-plan = No changes (0-diff). Outputs: instance i-0152e3fe2599fa630
- 20260708T180901Z LEG L3 closed: Stack scripts staged s3://opal-website-backups/code/website/ (5 .sh); SSM install SUCCESS d46bd5c5: OLS+LSPHP8.2+MariaDB
- 20260708T180934Z LEG L4 closed: EXERCISED (Rule 22a): public http://18.208.18.213/ = 200 OK server:LiteSpeed (WP live via SG-80); /wp-login.php = 200; l
- 20260708T182328Z LEG L5 closed: WP-admin 'patricia' <patricia@thewhitelabelcreative.com> created as administrator (SSM cmd, WP-only, no AWS on the WP ac
- 20260708T182328Z LEG L6 closed: EC2_MANIFEST opal-website-wp registered (i-0152e3fe2599fa630, commit 1eba880d3); infra/website README resource-inventory
- 20260708T182328Z CLOSED -- all 6 legs proven
