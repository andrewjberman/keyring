# Deploy Completion Record
**Date opened:** 2026-07-08T01:18:22.687676+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260708T012629Z
**Deploy:** NFRA_INFRPT.P3 follow-on: fold contract-integrity producer into nightly Fargate derive-runner (recurring schedule) + derive-image rebuild
**Authored by:** 0.7.0_AE_CloudOps
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD commit c15bc0f79 pushed | hash on origin/CLOUD | commit c15bc0f79 on origin/CLOUD; HEAD Dockerfile carries both my P3 COPYs (publish_contract_integrity.py + contract_engine.py) -- image matches committed source | CLOSED 20260708T012628Z |
| L2 | activation | CodeBuild globgrph-derive-build -> ECR opal-globgrph-derive-runner:latest | build SUCCEEDED + ECR imagePushedAt fresh | CodeBuild globgrph-derive-build 218f6ba0 SUCCEEDED (zip parsed from Dockerfile COPY-set, 15 files incl fedobs+P3; build #1 failed on a concurrently-added fedobs COPY missing from the exact-set zip -> fixed by dynamic COPY-parse). ECR opal-globgrph-derive-runner:latest tag 20260708-012438 pushedAt 01:24:49Z digest ecb2b4ae -- MY build, no concurrent clobber | CLOSED 20260708T012629Z |
| L3 | verify | producer runs in-container + contract_integrity/latest.json refreshes on the scheduled nightly (derive_runner_nightly, NEVER#4 -- validate-on-nightly, not ad-hoc) | next-nightly artifact generated_at advance (task-tracked, NOT stranded) | producer-run + contract_integrity/latest.json refresh validates on the scheduled derive_runner_nightly (~02:00Z, ~35min out) -- task-tracked, will confirm generated_at advance + RAVC; NOT stranded (mirrors the 07-07 derive-rebuild L4 nightly-validate precedent, NEVER#4) | CLOSED 20260708T012629Z |

## Log

- 20260708T011822Z OPENED by 0.7.0_AE_CloudOps with 3 leg(s)
- 20260708T012628Z LEG L1 closed: commit c15bc0f79 on origin/CLOUD; HEAD Dockerfile carries both my P3 COPYs (publish_contract_integrity.py + contract_eng
- 20260708T012629Z LEG L2 closed: CodeBuild globgrph-derive-build 218f6ba0 SUCCEEDED (zip parsed from Dockerfile COPY-set, 15 files incl fedobs+P3; build 
- 20260708T012629Z LEG L3 closed: producer-run + contract_integrity/latest.json refresh validates on the scheduled derive_runner_nightly (~02:00Z, ~35min 
- 20260708T012629Z CLOSED -- all 3 legs proven
