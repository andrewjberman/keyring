# Root cause -- 2026-10-05 "job was not acquired by Runner of type hosted" (portal deploy run 37368605578)

- **Answers:** the second half of Andrew-direct 2026-10-05 ~20:4xZ
  (`ANDREW_DIRECT_20261005_204xZ_FULL_PROD_DEPLOY_NOW_AND_ROOT_CAUSE_THE_RUNNER_FAILURE.md`): the cause is measured, not
  inferred, and lands as a record.
- **Egress:** githubstatus.com was read on Andrew's word 2026-10-06 ~18:3xZ ("go chekc github status history for that window").
- **Recorded by:** `2.0.0_SA_COO~D`.

## Cause: a GitHub-side incident, not Opal billing

GitHub incident `3q1yb5m7ltvb`, "Incident with Actions". Impact: Critical. Components: Actions, Pages. Read from
`https://www.githubstatus.com/api/v2/incidents.json` on 2026-10-06; shortlink https://stspg.io/c11dc9nb1zdq.

| UTC | GitHub update (verbatim) |
|---|---|
| 19:11:58 | "We are investigating reports of degraded performance for Actions" |
| 19:15:17 | "We're investigating an issue causing delays when assigning GitHub-hosted runners to Actions jobs." |
| 20:39:27 | "We're continuing to investigate job failures and delays affecting GitHub-hosted runner assignment." |
| 20:47:22 | "Actions is experiencing degraded availability. We are continuing to investigate." |
| 21:09:15 | "... some customers are also unable to access repository list, licensing and billing pages." |
| 21:32:31 | "We have applied mitigations to address GitHub Actions failures. Queued jobs are clearing." |
| 21:54:23 | "Actions is operating normally." |
| 22:49:42 | "This incident has been resolved." |

## Opal's failures fall inside the incident window

- **Deploy run 37368605578, attempt 1:** Build Production Assets was queued 20:15:29-20:30:31Z and then cancelled. This
  falls inside 19:11-21:54Z.
- **Attempt 2:** got a runner and deployed (~20:45Z). This is consistent with intermittent runner assignment during the
  incident.
- **Tag job, and DEV CI run 37374477632:** both were queued with no runner from ~21:12Z. They cleared after GitHub's
  21:32Z mitigation.

## What this settles

- The billing / spending-limit hypothesis is not supported. A spending cap does not clear itself on a re-run, and
  GitHub's own incident names the exact failure mode in the exact window. The billing-page check stays available as an
  optional confirmation, but nothing waits on it.
- The protection against a half-send is the `/prod-deploy` Step 5 no-runner rule: one re-run, then a revert-merge
  rollback and escalation (`ANDREW_DIRECT_20261006_181xZ_RECS_APPROVED_...` @51eb952230). Under that rule, this
  incident would have ended in attempt 2's success, or in a clean rollback. It would not have left a half-landed PROD.
