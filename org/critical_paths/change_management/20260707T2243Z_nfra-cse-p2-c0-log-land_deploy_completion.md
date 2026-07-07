# Deploy Completion Record
**Date opened:** 2026-07-07T22:43:58.392276+00:00
**Status:** OPEN
**Deploy:** NFRA_CSE.P2 req#1: land the append-only C0 CSE event log (globgrph.cse) on the existing Nessie store -- image rebuild (COPY-only add) + ecs run-task command-override (no new IAM/TF); one-marker C0/C1 consistency
**Authored by:** 0.5.0_AE_OpalETL
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD commit cse_store.py + derive_runner marker tuple + Dockerfile COPY | hashes pushed origin/CLOUD |  | OPEN |
| L2 | activation | CodeBuild globgrph-derive-build rebuild -> ECR opal-globgrph-derive-runner:latest (bakes cse_store/cse_schema/comp_ladder) | build SUCCEEDED + new :latest digest |  | OPEN |
| L3 | activation | ecs run-task command-override python /app/cse_store.py --ensure -> create globgrph.cse table | warehouse/globgrph/cse_* table dir present live |  | OPEN |
| L4 | verify | ecs run-task --ingest real code-producer CSEs + 4-table marker stamp | cse rows queryable live + _branch_head.main.json carries cse snapshot |  | OPEN |

## Log

- 20260707T224358Z OPENED by 0.5.0_AE_OpalETL with 4 leg(s)
