# Deploy Completion Record
**Date opened:** 2026-09-12T08:33:41.578962+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260912T083939Z
**Deploy:** IRPT_BCKEND IB-rt-6: the DRIVEN PRODUCTION FIRE of irpt-directory-refresh for business date 2026-09-11 (three firms)
**Authored by:** 0.9.0_WK_IRPT_BCKEND~2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | invoke the deployed irpt-directory-refresh with business_date 2026-09-11 | StatusCode 200 and the three per-firm envelopes | aws lambda invoke irpt-directory-refresh, payload business_date=2026-09-11: StatusCode 200, ExecutedVersion $LATEST, Duration 1893 ms, no function error. Three per-firm envelopes returned, all REFRESH_FAILED/FAILED with manifest_read_error=AccessDenied. | CLOSED 20260912T083938Z |
| L2 | s3-prefix | the three firm buckets investor-reporting/directory/_refresh/2026-09-11/manifest.json | head-object on each, with the denominator | 0 of 3 manifests written, and that IS the verified end state: the fire raised on its FIRST read and returned before any write, so nothing landed in any of the three buckets and there is nothing to roll back. Denominator 3 of 3 firms, each with manifest_key=None and manifest_written=None. | CLOSED 20260912T083938Z |
| L3 | verify | each manifest reads build_dispatch SSM with a real command id, and each command id resolves through ssm get-command-invocation | the three command ids and their statuses | 0 of 3 SSM commands sent -- the dispatcher was never reached. ROOT CAUSE MEASURED WITH TWO INSTRUMENTS, not inferred: (1) the live run returns manifest_read_error=AccessDenied for all three firms; (2) simulate-principal-policy, SINGLE ARN and exact grain, says s3:GetObject on arn:aws:s3:::opal-data-bd/investor-reporting/directory/_refresh/2026-09-11/manifest.json is ALLOWED while s3:ListBucket on arn:aws:s3:::opal-data-bd is implicitDeny. S3 answers 403 rather than 404 for a MISSING key when the caller cannot list the bucket, so a genuine absence is indistinguishable from a denial -- and the classifier correctly refuses to call it absence. Fix carried in the next entry under this slug. | CLOSED 20260912T083938Z |

## Log

- 20260912T083341Z OPENED by 0.9.0_WK_IRPT_BCKEND~2 with 3 leg(s)
- 20260912T083938Z LEG L1 closed: aws lambda invoke irpt-directory-refresh, payload business_date=2026-09-11: StatusCode 200, ExecutedVersion $LATEST, Dur
- 20260912T083938Z LEG L2 closed: 0 of 3 manifests written, and that IS the verified end state: the fire raised on its FIRST read and returned before any 
- 20260912T083938Z LEG L3 closed: 0 of 3 SSM commands sent -- the dispatcher was never reached. ROOT CAUSE MEASURED WITH TWO INSTRUMENTS, not inferred: (1
- 20260912T083939Z CLOSED -- all 3 legs proven
