# Deploy Completion Record
**Date opened:** 2026-09-25T23:03:11.864295+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260926T002707Z
**Deploy:** AMGT_RESAPP rr-3: the redeploy -- opal-amgt-scoped-api carries rr-2's Model Cases rule
**Authored by:** 0.7.0_AE_CloudOps~A
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | module.scoped_amgt_api.aws_lambda_function.this (opal-amgt-scoped-api) | CodeSha256 AFTER differs from BEFORE FOF+dRXoW1KFFzD0moLigsMB2LMmIjwhwURq7FkCzbw= and LastUpdateStatus=Successful (AC1); prior artifact VersionId ujFHMNbjbg6Yv3wFotVvfDPnF4reNQdO read at build and recorded as the rollback | AC1 exit=0. CodeSha256 moved FOF+dRXoW1KFFzD0moLigsMB2LMmIjwhwURq7FkCzbw= -> 982nlz5TEI32UQZSqFqbtVwu7/qgVLPn89tMF6kmYvo=, LastUpdateStatus=Successful, LastModified 2026-09-25T23:22:39Z. The deployed sha EQUALS the uploaded artifact metadata content-sha256 and the locally computed sha. Artifact VersionId ujFHMNbjbg6Yv3wFotVvfDPnF4reNQdO -> VgRYuqQ6UE3y8_4C6l1Rq8wWaXIf4j6K, 856314 -> 856864 bytes, ETag c69b4fc3c20a5633968e1391adca1c03; the prior version is preserved by bucket versioning and is the rollback the half names, read at build as the GO directed. Plan exactly 0 add 1 change 0 destroy, in-place, only s3_object_version + source_code_hash + last_modified, no second resource. 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed.' Replan reads 'No changes.' All three stop limbs were graded CLEAR before the apply and are enumerated in this entry -- limb 1 (1 of 7 changed files ships, exactly render_pack.py, with all 4 corpus files verified absent from the artifact), limb 2 (build_pack byte-identical, proven by a REPLACEMENT control because rq-2's control did not fire here), limb 3 (scoped_amgt.py untouched entirely). | CLOSED 20260925T232555Z |
| L2 | verify | the served /print?format=rich body across the LIVE research library with the CASES axis | AC2 served over N of N folders: OK N, NOT_OK 0, CAPTURE_FAILED 0, cases over N of N compared names at missing=0 extra=0, exit=0 | AC2 exit=0 under amendment 1 @a2072789f1 (population PINNED): 'population: PINNED .../population_at_cut.txt, 94 folders'; 'served over 94 of 94 folders: OK 94, NOT_OK 0, CAPTURE_FAILED 0'; 'cases over 94 of 94 compared names: page=282 rich=282 same=282 missing=0 extra=0'. The exit is the script's own rc ('exit $rc'), not a wrapper's or a pipe's. THE PINNED FILE WAS CHECKED BEFORE THE RUN rather than trusted: 96 lines = 2 comment lines + 94 entries, 0 duplicates, and 'AIA Group' absent -- consistent with the expected 94. WHAT THIS RUN DID AND DID NOT CHANGE, STATED PLAINLY: the cases figures are IDENTICAL to the failing run (page=282 rich=282 same=282 missing=0 extra=0 in both). The 94 folders that pass here are the same 94 that read OK before; the only difference is that the 95th, 'AIA Group', is no longer in the population. So amendment 1 corrected the CRITERION'S DENOMINATOR and changed nothing on the served plane, and this leg's pass adds no served evidence beyond what the first run already produced -- it removes a member that could not be measured at all. The served-plane evidence for this act is therefore the 282/282 cases axis, which held in both runs, plus OK 94 / NOT_OK 0. AIA Group is carried to round 44 as new scope with no identity minted this round (the issuer's row Z-S285, and this lane's Z-S284 recording the drift). | CLOSED 20260926T002533Z |

## Log

- 20260925T230311Z OPENED by 0.7.0_AE_CloudOps~A with 2 leg(s)
- 20260925T232555Z LEG L1 closed: AC1 exit=0. CodeSha256 moved FOF+dRXoW1KFFzD0moLigsMB2LMmIjwhwURq7FkCzbw= -> 982nlz5TEI32UQZSqFqbtVwu7/qgVLPn89tMF6kmYvo
- 20260925T234758Z HELD-SOVEREIGN-GATED gate=external/a canonical identity for the research folder 'AIA Group' (harvester_key security
- 20260926T001419Z HOLD RELEASED -> OPEN
- 20260926T002533Z LEG L2 closed: AC2 exit=0 under amendment 1 @a2072789f1 (population PINNED): 'population: PINNED .../population_at_cut.txt, 94 folders'
- 20260926T002707Z CLOSED -- all 2 legs proven
