# Deploy Completion Record
**Date opened:** 2026-09-25T23:03:11.864295+00:00
**Status:** HELD-SOVEREIGN-GATED -- gate: external / a canonical identity for the research folder 'AIA Group' (harvester_key security-a49e6fe67bebe3a9), which has none; the mint is an identity act outside this lane's <paths> and is a calls-not-picks decision reserved to 3.0.0_SA_CVO~Z / the issuer (held since 2026-09-25T23:47:58.414356+00:00)
**Deploy:** AMGT_RESAPP rr-3: the redeploy -- opal-amgt-scoped-api carries rr-2's Model Cases rule
**Authored by:** 0.7.0_AE_CloudOps~A
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | module.scoped_amgt_api.aws_lambda_function.this (opal-amgt-scoped-api) | CodeSha256 AFTER differs from BEFORE FOF+dRXoW1KFFzD0moLigsMB2LMmIjwhwURq7FkCzbw= and LastUpdateStatus=Successful (AC1); prior artifact VersionId ujFHMNbjbg6Yv3wFotVvfDPnF4reNQdO read at build and recorded as the rollback | AC1 exit=0. CodeSha256 moved FOF+dRXoW1KFFzD0moLigsMB2LMmIjwhwURq7FkCzbw= -> 982nlz5TEI32UQZSqFqbtVwu7/qgVLPn89tMF6kmYvo=, LastUpdateStatus=Successful, LastModified 2026-09-25T23:22:39Z. The deployed sha EQUALS the uploaded artifact metadata content-sha256 and the locally computed sha. Artifact VersionId ujFHMNbjbg6Yv3wFotVvfDPnF4reNQdO -> VgRYuqQ6UE3y8_4C6l1Rq8wWaXIf4j6K, 856314 -> 856864 bytes, ETag c69b4fc3c20a5633968e1391adca1c03; the prior version is preserved by bucket versioning and is the rollback the half names, read at build as the GO directed. Plan exactly 0 add 1 change 0 destroy, in-place, only s3_object_version + source_code_hash + last_modified, no second resource. 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed.' Replan reads 'No changes.' All three stop limbs were graded CLEAR before the apply and are enumerated in this entry -- limb 1 (1 of 7 changed files ships, exactly render_pack.py, with all 4 corpus files verified absent from the artifact), limb 2 (build_pack byte-identical, proven by a REPLACEMENT control because rq-2's control did not fire here), limb 3 (scoped_amgt.py untouched entirely). | CLOSED 20260925T232555Z |
| L2 | verify | the served /print?format=rich body across the LIVE research library with the CASES axis | AC2 served over N of N folders: OK N, NOT_OK 0, CAPTURE_FAILED 0, cases over N of N compared names at missing=0 extra=0, exit=0 |  | OPEN |

## Log

- 20260925T230311Z OPENED by 0.7.0_AE_CloudOps~A with 2 leg(s)
- 20260925T232555Z LEG L1 closed: AC1 exit=0. CodeSha256 moved FOF+dRXoW1KFFzD0moLigsMB2LMmIjwhwURq7FkCzbw= -> 982nlz5TEI32UQZSqFqbtVwu7/qgVLPn89tMF6kmYvo
- 20260925T234758Z HELD-SOVEREIGN-GATED gate=external/a canonical identity for the research folder 'AIA Group' (harvester_key security
