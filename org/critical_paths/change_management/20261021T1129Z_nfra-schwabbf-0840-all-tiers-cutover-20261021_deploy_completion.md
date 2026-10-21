# Deploy Completion Record
**Date opened:** 2026-10-21T11:29:08.251869+00:00
**Status:** OPEN
**Deploy:** NFRA_SCHWABBF 0840 cutover on bronze, silver and state (master 08403355). Consumer families of the monolith Schwab bronze, from the live sweep of 2026-10-21 11:2xZ (245 Lambdas, 341 roles, 12 ECS families, 163 EventBridge rules read): (1) the silver converter Lambda opal-assets-silver-schwab, reading schwab/<master>/bronze for 08242234, 08335338, 08403355 on S3 events, role opal-assets-silver-schwab-role; (2) the scheduled reconciliation sweep rule opal-assets-silver-schwab-sweep-daily, ENABLED, cron 12:15Z daily, mode sweep, INSIDE the 12:00-20:00Z window (no deploy or copy before its fire has ended); (3) the Black Diamond Schwab converters, four scripts in the bd bronze script tree reading monolith bronze by master (purpose model_portfolios, master 08242234) through the shared bd helper, deployed standalone to the bd code home; (4) the Schwab pull rules canonical-schwab-si2-08242234, canonical-schwab-si2-08335338 and schwab-canonical-si2-08403355 (writers of bronze, fires 09:45, 10:15, 10:45, 21:45, 22:15, 22:45Z); (5) role opal-schwab-monolith-remap-role (write only, 08242234 and 08335338 bronze). Not bronze readers: 17 roles reading silver, meta or gold of the three masters (gateway, irpt, mdpf, bd-exporter, consolidation); 2 roles with object-read on the whole bucket by AWS-managed policy (opal-drift-producer-codebuild-role, opal-news-lambda-role); schwab-anonymizer (secrets only); ECS opal-clientops-ews-task (writes ews_store in the destination state prefix). Rows S8 and S9.
**Authored by:** 0.7.0_AE_CloudOps~NFRA1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 12.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | shared-infra: the 5 fence rows on the opal-data-49financial and opal-data-cottonwood bucket policies, applied EARLY by TO-BF-r2 under entry nfra-schwabbf-fence-rows-early-20261021 (CTO ruling msg 110046) | get-bucket-policy read shows the rows still present |  | OPEN |
| L2 | activation | [order kind tf-apply] opal-assets: schwab fence variant, firm read/write/state grants, firm event rules, converter package; starts only after the 12:15Z opal-assets-silver-schwab-sweep-daily fire has ended | policy reads, notification config, function config |  | OPEN |
| L3 | activation | [order kind tf-apply] canonical-schwab-ec2: box MonolithSchwabStateWrite | get-role-policy |  | OPEN |
| L4 | s3-prefix | [order kind s3-copy] state tier 6930 keys to opal-data-49financial | move tool verify rc 0 |  | OPEN |
| L5 | s3-prefix | [order kind s3-copy] silver tier 7581 keys | move tool verify rc 0 |  | OPEN |
| L6 | s3-prefix | [order kind s3-copy] bronze tier 6074 keys, converter events drained | move tool verify rc 0, DLQ 0 |  | OPEN |

## Log

- 20261021T112908Z OPENED by 0.7.0_AE_CloudOps~NFRA1 with 6 leg(s)
