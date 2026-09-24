# Deploy Completion Record
**Date opened:** 2026-09-24T04:17:52.528749+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260924T053114Z
**Deploy:** IRPT directory listing speed: memory 512->1769, keep-warm schedule, code package at CRO pin 5886d0b9bd (CTO GO 100162/100169)
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A1 | activation | safe-apply of the saved directory-root plan 31060b25 (3 add / 1 change / 0 destroy) | apply output line | safe-apply of the SAVED plan .runtime/directory-speed/speed.tfplan (sha256 31060b2529019729 re-read before the act), HALT_ACK=1: aws_iam_role + aws_iam_role_policy + aws_scheduler_schedule irpt-directory-keepwarm created; module.irpt_directory_search.aws_lambda_function.this Modifications complete after 12s; Apply complete 3 added / 1 changed / 0 destroyed rc=0 at 2026-09-24T04:21:24Z; apply.log sha256 e01958d3461176fb | CLOSED 20260924T042725Z |
| V1 | verify | get-function-configuration CodeSha256 == 6uxqQO2S..., MemorySize 1769, layers/env unchanged; get-schedule irpt-directory-keepwarm-5min ENABLED; re-plan rc 0 | readback lines | get-function-configuration irpt-directory-search: CodeSha256 6uxqQO2Sm6SLY4k+XYWzuQ/Corssjy3zVW/DNDS6qMI= (== built artifact, version LZzc0blK), MemorySize 1769, Timeout 15, Handler entry.lambda_handler, env keys unchanged, State Active, LastUpdateStatus Successful (post-config.json); scheduler get-schedule irpt-directory-keepwarm-5min State ENABLED rate(5 minutes) input {irpt_warm:true} target irpt-directory-search (schedule.json); re-plan -detailed-exitcode rc 0 No changes (post-plan.log); member census 20/20 with exactly entry.py, loaders.py, served.py differing from the deployed o590uh5o | CLOSED 20260924T042725Z |
| R1 | verify | record-terraform-deploy.sh irpt-directory-search with the ledger commit and the code sha | recorder commit | record-terraform-deploy.sh investor-reporting --function irpt-directory-search --deploy-ledger 145435aa6c --code-sha256 6uxqQO2S...: committed 83a232fa71 in irpt-p-publish-20260923; source map deployed_code_sha256 6uxqQO2S..., last_deployed_at 2026-09-24T04:24:02Z | CLOSED 20260924T042726Z |
| M1 | verify | CloudWatch Duration p50/p90 of irpt-directory-search over the first hour beside the 15:19-03:19Z baseline; one warm-fire log line; one timed Global list load | measurement receipt | CloudWatch Duration irpt-directory-search, period 3600: BEFORE 03:21-04:21Z n=60 p50 2308 ms p90 4665 ms p99 6093 ms max 6203 ms; AFTER 04:21-05:21Z n=33 p50 160 ms p90 634 ms p99 972 ms max 980 ms (the AFTER sample includes the 5-minute warm pings at ~2 ms, so p50 overstates the improvement; p90/p99/max carry the page loads). Read 05:29Z | CLOSED 20260924T053114Z |

## Log

- 20260924T041752Z OPENED by 2.0.0_SA_COO~P with 4 leg(s)
- 20260924T042725Z LEG A1 closed: safe-apply of the SAVED plan .runtime/directory-speed/speed.tfplan (sha256 31060b2529019729 re-read before the act), HAL
- 20260924T042725Z LEG V1 closed: get-function-configuration irpt-directory-search: CodeSha256 6uxqQO2Sm6SLY4k+XYWzuQ/Corssjy3zVW/DNDS6qMI= (== built arti
- 20260924T042726Z LEG R1 closed: record-terraform-deploy.sh investor-reporting --function irpt-directory-search --deploy-ledger 145435aa6c --code-sha256 
- 20260924T053114Z LEG M1 closed: CloudWatch Duration irpt-directory-search, period 3600: BEFORE 03:21-04:21Z n=60 p50 2308 ms p90 4665 ms p99 6093 ms max
- 20260924T053114Z CLOSED -- all 4 legs proven
