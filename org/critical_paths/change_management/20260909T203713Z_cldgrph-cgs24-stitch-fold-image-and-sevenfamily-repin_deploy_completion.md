# NEVER-2 deploy ledger -- CG-s-24 stitch-fold image act + the seven-family digest re-pin

**Status:** CLOSED
**Opened (UTC):** 2026-09-09T20:37:13Z
**Owner:** `0.9.0_WK_NFRA_CLDGRPH~2` (spine-v3 L7 worker of `2.0.0_SA_COO~A`)
**Order:** `NFRA_CLDGRPH.TO-CG-F-4` (cell CG-s-24, PRD row S24; R13, R17), deliverable step 2
**Branch / HEAD at open:** `wk-cldgrph-6-2` @ `27e4ac36de776c8da06df4179b8343f62c63392b` (LOCAL, never pushed)

## THE ACT

1. Build + push a new `opal-globgrph-derive-runner` image from this HEAD
   (`infra/aws/globgrph/build-derive-image.sh --go` -> CodeBuild `globgrph-derive-build`).
   It carries the CG-s-24 stitch fold, the five CTO-gated `NODE_TYPE_LAYER` entries
   (GO 20260909T2015Z, CVO re-sign C-S40 @`e7db04572e`) and the `vocabulary=stitch-v1`
   stamp.
2. Move `local.globgrph_image_digest` (`infra/aws/terraform/globgrph/serving.tf:22`)
   to the new digest.
3. `bash .tools/safe-apply.sh -chdir=infra/aws/terraform/globgrph apply ... -target=<the
   address set censused from the plan>` -- the TARGETED set only, never an unscoped apply.
4. Read all seven task definitions live and confirm the new digest and no `:latest`.

## EVERY TASK FAMILY THAT PULLS THE TAG THIS ACT MOVES -- ALL SEVEN, BY THEIR TRUE NAMES

R13's obligation. **The names matter and are stated as measured**: the task order's cut
enumerated four of these without the `globgrph-` prefix, and those four do not resolve --
`describe-task-definition` raises `ClientException: Unable to describe task definition`
rather than returning a negative, so a sweep on the cut's names can print a clean
"0 of 7" having read only 3 (row `NFRA_CLDGRPH-W2-S49`, issuer amendment 20:1xZ).

| # | family (TRUE ACTIVE name) | revision BEFORE | image BEFORE | launcher |
|---|---|---|---|---|
| 1 | `globgrph-derive-runner` | 7 | `@sha256:1b89853f…` | EventBridge rule `opal-globgrph-derive-runner-nightly` |
| 2 | `globgrph-projection-worker` | 4 | `@sha256:1b89853f…` | EventBridge Pipe `opal-globgrph-projection-worker` |
| 3 | `globgrph-serving` | 2 | `@sha256:1b89853f…` | ECS service `aws_ecs_service.globgrph_serving` (always-on) |
| 4 | `globgrph-comp-learns-producer` | 2 | `@sha256:1b89853f…` | EventBridge rule `opal-globgrph-comp-learns-producer-nightly`, cron(0 4 * * ? *) |
| 5 | `globgrph-cse-producer` | 2 | `@sha256:1b89853f…` | EventBridge Scheduler `globgrph-cse-producer-nightly`, cron(30 3 * * ? *) |
| 6 | `globgrph-fedobs-producer` | 2 | `@sha256:1b89853f…` | EventBridge rule `opal-globgrph-fedobs-producer-nightly`, cron(30 4 * * ? *) |
| 7 | `globgrph-resource-summaries-producer` | 2 | `@sha256:1b89853f…` | **NONE declared** -- hand-run `ecs run-task` (row W1-S28) |

All seven read `local.globgrph_image_digest`, so **one edit moves all seven**:
`serving.tf:125`, `projection.tf:231`, `item2a.tf:361`,
`resource_summaries_producer.tf:158`, and the comp-learns / cse / fedobs task
definitions through the same local (censused with `comp-find 'globgrph_image_digest'`).

**NOT in this population, and named rather than omitted:** `globgrph-nessie` and
`globgrph-trino` run other images and reference no `opal-globgrph-derive-runner` tag,
so this act has nothing to move for them. That is 9 ACTIVE families in the account, 7
of which pull this tag.

**The ECR `:latest` tag WILL move with the push** (before: `sha256:1b89853f…`, pushed
2026-09-04T08:03:52Z, tags `latest` + `20260904-080337`). Nothing pulls it: all seven
families are pinned BY DIGEST, which is exactly why R13 exists. Stated here rather than
left to be inferred.

## PRE-STATE, measured (`.scratch/f4/f4_prestate.json`, 2026-09-09T20:3xZ)

    all seven          revision 7/4/2/2/2/2/2, all @sha256:1b89853fe44133f10a60dc2b3e7b463c0d3b68b827a2ddff249bf427ecde2778
    families on :latest    0 of 7
    distinct digests       1
    ECR :latest            sha256:1b89853f... pushed 2026-09-04T08:03:52Z
    projection pointer     projection/2026-09-09T20:04:09.034708+00:00/
    stitch marker          producer=stitch-codebuild built_at=2026-09-09T19:55:00Z
                           git_sha de590a7d02 artifact_sha256 918d825f...

## ROLLBACK

The prior digest `sha256:1b89853fe44133f10a60dc2b3e7b463c0d3b68b827a2ddff249bf427ecde2778`
is recorded above and remains in ECR (it is tagged `20260904-080337`, an immutable
timestamp tag, not only `latest`). Rolling back = restore that literal in
`serving.tf:22` and re-run the same targeted apply. No image is deleted by this act.

## WHAT THIS ENTRY DOES **NOT** DO

No unscoped `terraform apply`; no `aws lambda update-function-code`; no rule disabled;
no alarm, monitor or notifier; no local Kuzu store; the stitch STORE untouched (S26's).
`.tools/terraform.exe` is PRESENT in this worktree (91,104,424 B) and is the binary
used -- never the PATH `terraform`, which re-pins remote state.

---

## CLOSE

**Status at close:** CLOSED
**Closed (UTC):** 2026-09-09T20:58:00Z


**THE ACT COMPLETED, measured on the LIVE plane after the apply returned rc 0.**

    ECR :latest   sha256:1b89853f...  ->  sha256:478d0a43742b2ed5a44631c6352b5713c5ba22f015d82a673cfb93428a9dae20
                  pushed 2026-09-09T20:39:50Z, tags [20260909-203936, latest], 131,531,350 B
                  CodeBuild globgrph-derive-build:f8abbe55-c611-4317-8df7-2edf15908de3, SUCCEEDED
                  source commit 27e4ac36de776c8da06df4179b8343f62c63392b

    describe-task-definition, all seven by their TRUE names (f4_families_after.json):
      globgrph-derive-runner                 rev 7 -> 8
      globgrph-projection-worker             rev 4 -> 5
      globgrph-serving                       rev 2 -> 3
      globgrph-comp-learns-producer          rev 2 -> 3
      globgrph-cse-producer                  rev 2 -> 3
      globgrph-fedobs-producer               rev 2 -> 3
      globgrph-resource-summaries-producer   rev 2 -> 3
      ON_NEW_DIGEST = 7 of 7          ON_LATEST = 0 of 7

**THE APPLY WAS TARGETED, AND THE TARGET SET WAS CENSUSED FROM A PLAN, NOT GUESSED.**
An unscoped plan was run FIRST (read-only, never applied) and its address census read
**22** addresses: the 18 this act owns plus **4 foreign**, left exactly as found --

    aws_glue_partition.tool_activity["rolling_log"]          (update in place)
    aws_glue_partition.tool_activity["rolling_log_summary"]  (update in place)
    aws_glue_partition.tool_activity["routing"]              (create)
    aws_sns_topic_subscription.critical_surface_alerts_email (create)

The SNS subscription is an alert destination and the C3 moratorium forbids this order to
land one, so an unscoped apply here would have created a notifier nobody asked for. That
is the whole reason the plan census precedes the apply.

**THE 18 ADDRESSES APPLIED** (7 task definitions + 4 schedule/target launchers + the
projection pipe + the serving service + 5 launcher-role policies). Scoping to the seven
task definitions alone would have left every launcher pointing at the OLD revision --
the E-2 record's own lesson, and the reason this set is 18 rather than 7:

    aws_ecs_task_definition.derive_runner                    aws_cloudwatch_event_target.derive_runner_nightly
    aws_ecs_task_definition.projection_worker                aws_cloudwatch_event_target.comp_learns_producer_nightly
    aws_ecs_task_definition.globgrph_serving                 aws_cloudwatch_event_target.fedobs_producer_nightly
    aws_ecs_task_definition.comp_learns_producer             aws_scheduler_schedule.cse_producer_nightly
    aws_ecs_task_definition.cse_producer                     aws_pipes_pipe.projection_worker
    aws_ecs_task_definition.fedobs_producer                  aws_ecs_service.globgrph_serving
    aws_ecs_task_definition.resource_summaries_producer      aws_iam_role_policy.derive_runner_events_ecs
                                                             aws_iam_role_policy.comp_learns_producer_events_ecs
                                                             aws_iam_role_policy.cse_producer_scheduler_ecs
                                                             aws_iam_role_policy.fedobs_producer_events_ecs
                                                             aws_iam_role_policy.projection_pipe

    targeted plan (pre)   Plan: 7 to add, 11 to change, 7 to destroy.   18 addresses, 0 foreign
    apply                 Apply complete! Resources: 7 added, 11 changed, 7 destroyed.   rc 0
    targeted plan (post)  No changes. Your infrastructure matches the configuration.
    unscoped plan (pre, NEVER applied)  Plan: 9 to add, 13 to change, 7 to destroy.  22 addresses

**THE TASK ORDER SAYS "the TEN-address set".** That was E-2's ten, for an act that moved
FOUR families. This act moves SEVEN, so the set is 18 -- read off the plan rather than
carried over from the earlier record. Row `NFRA_CLDGRPH-W2-S52`.

**NOT HALF-LANDED.** The post-apply targeted plan reads "No changes", all seven families
read the new digest live, and the ECS service and the pipe were updated in the same apply
as the task definitions they reference, so no launcher is left on a stale revision.

`.tools/terraform.exe` (91,104,424 B) was the binary for init, both plans and the apply --
never the PATH `terraform`. The halt-gate blocked the first apply attempt with IDENTITY
UNRESOLVED and was satisfied the way it instructs, by naming this worker's own principal
in the gitignored `org/mcp/sessions/<session>.serial`; it was never overridden. Row
`NFRA_CLDGRPH-W2-S53`.
