# Deploy Completion Record
**Date opened:** 2026-07-01T00:31:07.841236+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260701T011211Z
**Deploy:** NFRA_COMPLEARN P3: scheduled comp-learns-status producer -- rebuild derive image (ADDITIVE +2 files), new task-def reusing it (in-VPC httpx transport) + minimal task role (S3 served-write only, zero-widen) + EventBridge cron(0 4) nightly refresh of comp_learns_status.json.
**Authored by:** 0.8.0_AE_CloudComp~E
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 8.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD commit P3 code (Dockerfile +2 COPY, comp_learns_producer.tf, httpx transport) | 15bc9ea12 pushed | 15bc9ea12 (Dockerfile+2 COPY, comp_learns_producer.tf, httpx transport) + a4250111e (re-emit decision) + d2b116f33 (worklist) pushed to origin/CLOUD. | CLOSED 20260701T010937Z |
| L2 | activation | derive image rebuild via globgrph-derive-build CodeBuild (:latest carries the 2 P3 files; additive-inert to derive) | CodeBuild SUCCEEDED + build id | ~B's verified rebuild (option-b) is current :latest (tag 20260701-003640, pushed 00:36:40Z, overwrote my 499a1a4b) and CARRIES my 2 P3 files (~B added them to their 9-file zip after my Dockerfile commit 15bc9ea12 caused their first build's COPY-fail). So NO separate rebuild needed -- my producer rides ~B's fix-carrying image. Collision resolved (COO~B released 010714Z). | CLOSED 20260701T010907Z |
| L3 | activation | TARGETED safe-apply comp_learns_producer.tf (task-def + minimal task role + events role + rule + target) | Apply complete + 0-diff re-plan on my targets | TARGETED safe-apply (HALTGT passed): Apply complete! 9 added/0 changed/0 destroyed -- task-def globgrph-comp-learns-producer:1 + minimal task role (s3:PutObject served/* + logs) + events role + rule opal-globgrph-comp-learns-producer-nightly + target. Targeted to isolate from the still-held item2d/2e. | CLOSED 20260701T010907Z |
| L4 | verify | manual RunTask produces a fresh served JSON via in-VPC httpx transport + rule ENABLED | task exit 0 + served computed_at advanced + aws events describe-rule ENABLED | Manual RunTask (task 8385856b, on ~B's :latest 20260701-003640) STOPPED exitCode=0. In-VPC producer log: 6/6 views ok (tool_demand 25/coverage_gaps 20/gap_heat 20/cost_by_role 40/gap_annotations 40/rail_routing_quality 7) via the httpx REST transport (COMP_LEARNS_TRINO_HOST=trino.opal-globgrph.local) -> served -> s3 comp_learns_status.json; computed_at=1782868206. Served JSON LastModified advanced 00:14:07 -> 01:10:15Z. comp-learns-status renders the fresh surface (Estate-enriched by ~B's population -- derive_runner.py 4->5 escapes). Rule opal-globgrph-comp-learns-producer-nightly ENABLED cron(0 4) wired to task-def :1. Proves: ~B's image carries my producer + in-VPC transport + S3 write + minimal task role all work. | CLOSED 20260701T011211Z |

## Log

- 20260701T003107Z OPENED by 0.8.0_AE_CloudComp~E with 4 leg(s)
- 20260701T010907Z LEG L2 closed: ~B's verified rebuild (option-b) is current :latest (tag 20260701-003640, pushed 00:36:40Z, overwrote my 499a1a4b) and C
- 20260701T010907Z LEG L3 closed: TARGETED safe-apply (HALTGT passed): Apply complete! 9 added/0 changed/0 destroyed -- task-def globgrph-comp-learns-prod
- 20260701T010937Z LEG L1 closed: 15bc9ea12 (Dockerfile+2 COPY, comp_learns_producer.tf, httpx transport) + a4250111e (re-emit decision) + d2b116f33 (work
- 20260701T011211Z LEG L4 closed: Manual RunTask (task 8385856b, on ~B's :latest 20260701-003640) STOPPED exitCode=0. In-VPC producer log: 6/6 views ok (t
- 20260701T011211Z CLOSED -- all 4 legs proven
