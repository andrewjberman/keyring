# Deploy Completion Record
**Date opened:** 2026-06-17T18:21:21.256768+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260617T182522Z
**Deploy:** NFRA_GRAPHS.D8-FP surface-scan Option-A: derive image rebuild (membership scan) + baseline re-sign (AWS-backend membership, replaces portal-inclusive)
**Authored by:** 0.7.0_AE_CloudOps <0.7.0_AE_CloudOps@opal.agent>
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| image-rebuild | activation | opal-globgrph-derive-runner:latest | CodeBuild SUCCEEDED + resolvedSourceVersion == uploaded zip version (image carries derive_runner membership scan) | CodeBuild globgrph-derive-build 20bc2e7a SUCCEEDED; build-source object byte-matches the fresh re-zip (68316B, in-zip membership-change confirmed); ECR opal-globgrph-derive-runner:latest freshly pushed (digest 0e7863c7). resolvedSrc=null expected (unversioned build-source, not stale-tell). Live scan behavior verifies on the 06-18 nightly log (mode=aws-backend-membership; scan runs only in full nightly, no ad-hoc). | CLOSED 20260617T182445Z |
| baseline-resign | s3-prefix | critical-surface-baseline.json | re-signed d8fp membership baseline uploaded (32 members/6 surface-firm) + legacy backed up | re-signed via resign_surface_baseline.py -> s3://opal-313476888478-globgrph/critical-surface-baseline.json. Verified on S3: schema=d8fp-aws-backend-membership-v1, 6 surface-firm / 32 members, F6-anchored (nessie_commit_hash). Legacy portal-inclusive baseline backed up to .legacy-pre-d8fp. Matches the AC3-tested + dry-run set. | CLOSED 20260617T182314Z |

## Log

- 20260617T182121Z OPENED by 0.7.0_AE_CloudOps <0.7.0_AE_CloudOps@opal.agent> with 2 leg(s)
- 20260617T182314Z LEG baseline-resign closed: re-signed via resign_surface_baseline.py -> s3://opal-313476888478-globgrph/critical-surface-baseline.json. Verified on 
- 20260617T182445Z LEG image-rebuild closed: CodeBuild globgrph-derive-build 20bc2e7a SUCCEEDED; build-source object byte-matches the fresh re-zip (68316B, in-zip me
- 20260617T182522Z CLOSED -- all 2 legs proven
