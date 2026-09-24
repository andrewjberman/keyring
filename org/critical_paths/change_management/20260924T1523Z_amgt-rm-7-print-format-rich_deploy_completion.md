# Deploy Completion Record
**Date opened:** 2026-09-24T15:23:52.786979+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260924T155826Z
**Deploy:** AMGT_RESAPP rm-7: opal-amgt-scoped-api serves GET .../print?format=rich, pdf default unchanged
**Authored by:** 0.7.0_AE_CloudOps~A
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | module.scoped_amgt_api.aws_lambda_function.this (opal-amgt-scoped-api) | CodeSha256 AFTER differs from BEFORE DEQQiCH+UoUMd7EZSQA5RTsILDY5+ubb9Y3gVLE5elU= | CodeSha256 moved DEQQiCH+UoUMd7EZSQA5RTsILDY5+ubb9Y3gVLE5elU= -> y5bJBQsP8Q7Lfudb5nwc5wEr72IcH53uS5cz2T8bn/w=, equal to the uploaded artifact metadata content-sha256 and to the locally computed sha. Artifact VersionId ZacA2Kn0CWoJqOFLvTPe2kzZ4x_ctTYe -> 9z.fsHGW7ZN2Qf2yU_rsnv0wiL7uKqRS, 807904 -> 844437 bytes. Plan was exactly 0 add 1 change 0 destroy, in-place, only s3_object_version source_code_hash last_modified, 28 attributes and 4 blocks unchanged, print-deps-layer untouched. Apply complete 0 added 1 changed 0 destroyed; replan reads No changes. | CLOSED 20260924T155739Z |
| L2 | verify | the default print path, GET /api/scoped/amgt/security/BA_US_Equity/print with no format | content-stream digest EQUAL to BEFORE 5f150ad66d00e76f5364058eda899723f0b1a9623af058ce558f974ac6c5d602, with CAT_US_Equity 7c017870dea741188c768a812637b10dd94b6d90ee1e10a7392a511c48d2025f DIFFERENT as the live negative control | DELTA=0 on the content-stream comparand per issuer amendment 3: BA_US_Equity no-format content digest 5f150ad66d00e76f5364058eda899723f0b1a9623af058ce558f974ac6c5d602 BEFORE and AFTER, EQUAL. Negative control live: CAT_US_Equity 7c017870dea741188c768a812637b10dd94b6d90ee1e10a7392a511c48d2025f, DIFFERENT, so equal was free to fail. Recorded beside it, and the reason the comparand was re-cut: raw EQUAL False and normalised EQUAL False on this same correct deploy, because rl-10 removed /CreationDate (present BEFORE True, AFTER False; 77862 -> 77828 bytes). Either of the two earlier comparands would have graded this deploy FAIL and triggered rollback. | CLOSED 20260924T155739Z |
| L3 | verify | the same route with format=rich and with format=xml | rich returns 200 text/markdown over 20 KB whose first line is a Markdown heading naming the security, and xml returns 400 | format=rich returns 200 text/markdown; charset=utf-8, 58549 bytes (> 20 KB), first line '# BOEING CO/THE [BA US Equity] Research Note' -- a Markdown heading naming the security. format=xml returns 400 application/json with body {refused: true, reason: unknown print format 'xml': use format=pdf or format=rich}. Direct invoke of the deployed function, same code path as the BEFORE reads. | CLOSED 20260924T155740Z |

## Log

- 20260924T152352Z OPENED by 0.7.0_AE_CloudOps~A with 3 leg(s)
- 20260924T155739Z LEG L1 closed: CodeSha256 moved DEQQiCH+UoUMd7EZSQA5RTsILDY5+ubb9Y3gVLE5elU= -> y5bJBQsP8Q7Lfudb5nwc5wEr72IcH53uS5cz2T8bn/w=, equal to 
- 20260924T155739Z LEG L2 closed: DELTA=0 on the content-stream comparand per issuer amendment 3: BA_US_Equity no-format content digest 5f150ad66d00e76f53
- 20260924T155740Z LEG L3 closed: format=rich returns 200 text/markdown; charset=utf-8, 58549 bytes (> 20 KB), first line '# BOEING CO/THE [BA US Equity] 
- 20260924T155826Z CLOSED -- all 3 legs proven
