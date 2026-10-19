# Deploy Completion Record
**Date opened:** 2026-10-19T14:31:56.658154+00:00
**Status:** OPEN
**Deploy:** AMGT_HARVST HVST-cn-7 stage 3: apply the RUN HALF of the standing dossier-refresh producer (11 resources: ECS cluster amgt-dossier-refresh-cluster, security group, task log group, task role + policy (s3:PutObject only under amgt/harvest/gold/research_dossier/, no Delete), execution role + attachment, task definition amgt-dossier-refresh-task by DIGEST sha256:ceac4ad0.., scheduler role + policy, the schedule DISABLED cron(0 10 ? * MON-FRI *) America/New_York) from worktree C:/tmp/cn7-build at 1dda9cc0a2; vars dossier_refresh_build_enabled=true dossier_refresh_run_enabled=true dossier_refresh_image_digest=sha256:ceac4ad030b3979611f605b0e01355a93a5336d2ca2e2cde7df0420b25381670; the schedule stays DISABLED until stage 5 (W1's separate message); nothing deleted
**Authored by:** 0.7.0_AE_CloudOps~SC1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| D1 | verify | full-root saved plan ends Plan: 11 to add, 0 to change, 0 to destroy and proposes nothing else (graded from JSON) | plan JSON denominator |  | OPEN |
| D2 | activation | safe-apply of the saved plan after get_delivery_state all READ; Apply complete 11 added | apply output |  | OPEN |
| D3 | verify | read back: task definition image is repo@digest (no tag), command --write --require-trading-day --manifest /tmp/dossier_refresh_manifest.txt; task role PutObject only under the dossier prefix and no s3:Delete*; schedule DISABLED cron(0 10 ? * MON-FRI *) America/New_York | describe outputs |  | OPEN |
| D4 | verify | plan after No changes; ledger closed and committed with cn7_s3.out | plan after + commit |  | OPEN |

## Log

- 20261019T143156Z OPENED by 0.7.0_AE_CloudOps~SC1 with 4 leg(s)
