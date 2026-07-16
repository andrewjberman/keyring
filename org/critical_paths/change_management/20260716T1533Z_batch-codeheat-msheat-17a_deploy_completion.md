# Deploy Completion Record
**Date opened:** 2026-07-16T15:33:21.473016+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260716T161346Z
**Deploy:** Batch (3 groups, CTO 152408Z): codeheat env revert (TO-2 ruling 033933Z) + ms_heat freshness twin consequences (37d8d9dfe/528c430bc) + 17a monolith parquet-under-bronze deny (first bucket policy)
**Authored by:** 0.7.0_AE_CloudOps
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD commit: item2a env delete + monolith.tf bucket policy + EOL renormalize riders | hash pushed | d89cc4fc9 on origin/CLOUD (contains-verified); tags globgrph-v0.1.18 + opal-assets-v0.25.0 pushed --follow-tags; single work-package push per COO 155206Z discipline | CLOSED 20260716T161342Z |
| L2 | activation | globgrph targeted apply: derive task-def revision (env deleted) + freshness_stale[ms_heat] alarm + freshness_alarm_read policy + freshness_alarm lambda env | plan diff + apply + 0-diff | globgrph targeted apply 2/4/1 (task-def replace = ECS revision swap 5->6; BOTH ARN-pinned dependents included after dependency census: event target + events-role RunTask policy) -> targeted re-plan 'No changes'. APPLIED reads: rev 6 env list WITHOUT GLOBGRPH_CODEHEAT_ENABLED; alarm opal-globgrph-freshness-stale-ms_heat_snap_last_append EXISTS State=OK (born healthy, heartbeat live); event target TaskDefinitionArn ...:6 (no stranded revision) | CLOSED 20260716T161342Z |
| L3 | activation | opal-assets targeted apply: aws_s3_bucket_policy.monolith (pure add, first policy) | plan 1/0/0 + apply + 0-diff | opal-assets targeted apply 1/0/0 (pure add, first bucket policy; pre-read NoSuchBucketPolicy) -> re-plan 'No changes' | CLOSED 20260716T161344Z |
| L4 | verify | live reads: task-def env ABSENT + alarm exists + get-bucket-policy present + deny exercised where safe | APPLIED-truth citations | DENY EXERCISED: put-object _gate_test/inflection/bronze/probe.parquet -> AccessDenied 'explicit deny in a resource-based policy' (no residue); ISOLATED POSITIVE CONTROL: same-path probe.json -> landed (ETag cc725c85) -> deleted. get-bucket-policy renders both Resource patterns. Twin first-fire 15:45:52Z read + explained fabric-wide (adjudicated-hole exact-token semantics; COO/CTO/~B notified 160730Z) | CLOSED 20260716T161345Z |

## Log

- 20260716T153321Z OPENED by 0.7.0_AE_CloudOps with 4 leg(s)
- 20260716T161342Z LEG L1 closed: d89cc4fc9 on origin/CLOUD (contains-verified); tags globgrph-v0.1.18 + opal-assets-v0.25.0 pushed --follow-tags; single 
- 20260716T161342Z LEG L2 closed: globgrph targeted apply 2/4/1 (task-def replace = ECS revision swap 5->6; BOTH ARN-pinned dependents included after depe
- 20260716T161344Z LEG L3 closed: opal-assets targeted apply 1/0/0 (pure add, first bucket policy; pre-read NoSuchBucketPolicy) -> re-plan 'No changes'
- 20260716T161345Z LEG L4 closed: DENY EXERCISED: put-object _gate_test/inflection/bronze/probe.parquet -> AccessDenied 'explicit deny in a resource-based
- 20260716T161346Z CLOSED -- all 4 legs proven
