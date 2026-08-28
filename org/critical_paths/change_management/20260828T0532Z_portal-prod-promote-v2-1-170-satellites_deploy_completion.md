# Deploy Completion Record
**Date opened:** 2026-08-28T05:32:49.256376+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260828T060153Z
**Deploy:** Portal DEV->PROD promote v2.1.170 -- Satellites end-to-end (Andrew smoke-tested + his 4 change items) and the D1 Asset Category Views panel. Merge d4a048fd, base/rollback 73afaccd, DEV pin 2858e7f5. Andrew-direct 2026-08-28 ~05:2xZ.
**Authored by:** 1.0.0_SA_CTO~Z
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 12.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| push-prod | git | origin/PROD | merge d4a048fd ON ORIGIN via ls-remote read (INTEGRATOR-ONLY push, 0.0.0_AB_MSTR~Z) | origin/PROD = d4a048fd5252833f6045e235d27fe8ee95b2799b (git rev-parse origin/PROD after fetch). Containment test, NOT hash equality: DEV 2858e7f5 is an ancestor of PROD; NEG CONTROL PROD is not an ancestor of DEV. Pushed 05:32:17Z by 0.0.0_AB_MSTR~Z under LD-0367. | CLOSED 20260828T055750Z |
| ci-deploy | activation | deploy.yml on PROD | gh run conclusion==success ENUMERATED BY headSha across ALL workflows, never the branch badge | gh run 33145060591 completed/success, re-read AFTER conclusion (0.0.0_AB_MSTR~Z, 13041). Upgraded from IMPLIED-by-tag-ordering to DIRECTLY OBSERVED at the served plane. NOT closed on a branch badge. | CLOSED 20260828T055750Z |
| tag | git | portal-v2.1.170 | git rev-parse <tag>^{commit} == PROD head -- PEELED, ls-remote shows the tag OBJECT sha and misreads as a double-merge | PEELED: git rev-parse portal-v2.1.170^{commit} = d4a048fd5252 == origin/PROD head. Raw ls-remote object sha is 0d55beb7978d (a DIFFERENT value that appears nowhere in the promote -- this is exactly the double-merge misread the peel exists to prevent). NEG CONTROL: portal-v2.1.169^{commit} = 73afaccd = the PROD base/rollback sha. | CLOSED 20260828T055750Z |
| served-bundle | verify | the served portal origin | route chunks actually SERVED are the new build -- DEPLOYED != RENDERED, and CloudFront invalidation is ASYNC | TWO INSTRUMENTS, TWO PLANES. (1) 0.0.0_AB_MSTR~Z, curl -sI on opalinvest.dev (alias read from the distribution's own Aliases): served index.html Last-Modified 05:34:02 GMT, main bundle 05:34:00 GMT, X-Cache: Miss from cloudfront -- edge went to ORIGIN, so not a stale cached copy. (2) 1.0.0_SA_CTO~Z, s3api head-object on the SITE bucket opalinvest-portal (default cache behavior target S3-opalinvest-portal, 1 of 7 origins): index.html LastModified 2026-08-28T05:34:02Z, assets/* 05:34:01Z. Objects written ~1m45s after the 05:32:17Z push. Response headers and object metadata are different planes -- corroboration, not repetition. | CLOSED 20260828T055750Z |
| ws-pointer | git | CLOUD workspace portal submodule pointer | pointer commit hash on origin/CLOUD (integrator push) | Pointer bump d3197e5b55 by 0.0.0_AB_MSTR~Z. VERIFIED BY 1.0.0_SA_CTO~Z ON THE ARTIFACT, NOT ON THE REPORT (that report said 5-of-5 while this leg still read OPEN with an empty proof field): merge-base --is-ancestor d3197e5b55 origin/SITEZ = YES; git ls-tree origin/SITEZ portal = 160000 commit 2858e7f5ff02ff3895ac2485843222063fb403b6, identical to portal actual HEAD. Pointer advanced 4ac152f8b93a -> 2858e7f5ff02 (was 34 commits behind). Records DEV per CLAUDE.md, not PROD. | CLOSED 20260828T060153Z |

## Log

- 20260828T053249Z OPENED by 1.0.0_SA_CTO~Z with 5 leg(s)
- 20260828T055750Z LEG push-prod closed: origin/PROD = d4a048fd5252833f6045e235d27fe8ee95b2799b (git rev-parse origin/PROD after fetch). Containment test, NOT ha
- 20260828T055750Z LEG tag closed: PEELED: git rev-parse portal-v2.1.170^{commit} = d4a048fd5252 == origin/PROD head. Raw ls-remote object sha is 0d55beb79
- 20260828T055750Z LEG ci-deploy closed: gh run 33145060591 completed/success, re-read AFTER conclusion (0.0.0_AB_MSTR~Z, 13041). Upgraded from IMPLIED-by-tag-or
- 20260828T055750Z LEG served-bundle closed: TWO INSTRUMENTS, TWO PLANES. (1) 0.0.0_AB_MSTR~Z, curl -sI on opalinvest.dev (alias read from the distribution's own Ali
- 20260828T060153Z LEG ws-pointer closed: Pointer bump d3197e5b55 by 0.0.0_AB_MSTR~Z. VERIFIED BY 1.0.0_SA_CTO~Z ON THE ARTIFACT, NOT ON THE REPORT (that report s
- 20260828T060153Z CLOSED -- all 5 legs proven
