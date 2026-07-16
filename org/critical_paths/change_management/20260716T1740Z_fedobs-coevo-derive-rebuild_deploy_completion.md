# Deploy Completion Record
**Date opened:** 2026-07-16T17:40:24.627187+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260716T175750Z
**Deploy:** Rebuild derive-runner image so fedobs_observe.py picks up the coevolution OOM fix cca39dbe1 (source<>graph_head); ~Z routed, my standing rebuild lane; no TF change (task-def/schedule live)
**Authored by:** 0.7.0_AE_CloudOps
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | CodeBuild globgrph-derive-build from verified source zip (fedobs_observe.py w/ fix) -> ECR :latest new digest | build SUCCEEDED + new imageDigest | CodeBuild globgrph-derive-build:1adef157-f4be-48a9-a71a-75358438cfa7 SUCCEEDED; ECR opal-globgrph-derive-runner:latest new digest sha256:174ac79f408965b69c16ba868709ff90f961c45c29c76588ff69d78537a566c5 (pre-rebuild was sha256:94819df5). Source zip Dockerfile-COPY-derived (20 entries), fedobs/fedobs_observe.py present + verified carrying 'source <> graph_head' before zip. | CLOSED 20260716T175749Z |
| L2 | verify | read-only run-task exercise of fedobs producer on NEW :latest (per ~Z's method) -> exit 0, no OOM | task exit code + log | Read-only run-task on the NEW :latest (task 1a9503bffe0743f5a41ba9d6d894676b, globgrph-fedobs-producer:1, command-override python file-read): exit 0, stdout FIX_PRESENT -- the fix is baked in the RUNNING image (runtime confirmation, not build log). No producer run / no served-artifact write / no OOM path. Fix LOGIC already proven in-VPC by 0.8.0~Z (949 pairs, no OOM). Served-artifact verification is ~Z's on the first nightly. | CLOSED 20260716T175750Z |

## Log

- 20260716T174024Z OPENED by 0.7.0_AE_CloudOps with 2 leg(s)
- 20260716T175749Z LEG L1 closed: CodeBuild globgrph-derive-build:1adef157-f4be-48a9-a71a-75358438cfa7 SUCCEEDED; ECR opal-globgrph-derive-runner:latest n
- 20260716T175750Z LEG L2 closed: Read-only run-task on the NEW :latest (task 1a9503bffe0743f5a41ba9d6d894676b, globgrph-fedobs-producer:1, command-overri
- 20260716T175750Z CLOSED -- all 2 legs proven
