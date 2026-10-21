# Deploy Completion Record
**Date opened:** 2026-10-21T17:32:10.845187+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261021T174412Z
**Deploy:** NFRA_SCHWABBF 0840 key function and puller
**Authored by:** 0.7.0_AE_CloudOps~NFRA1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L7 | activation | data/black_diamond/scripts/bronze/_monolith_bronze.py to its code home (the pre-push gate deploys it) | head-object ETag equals the repo file md5 | Deployed by safe_deploy_core.deploy_file (the pre-push gate's own function and key; the push itself deployed nothing) to s3://opal-data-bd/code/bronze/_monolith_bronze.py, status MATCH. Repo index blob md5 e59c68a31c8fc4e8dde82f57898fbff0 (15458 bytes, worktree identical, 0 CRs); head-object ETag e59c68a31c8fc4e8dde82f57898fbff0, ContentLength 15458, new VersionId jalNRmtiRcEu655VIh2sRGACkDAMZlTI. BEFORE (rollback anchor): ETag 89470f2fc70983111783a564766b7068, 4455 bytes, VersionId taU21QjAn1gScz8Otc9neFIw_4bLcbWg (2026-07-17); redeploy that version to roll back. Origin box/laptop 60341826d01 contains e2fea02fad, c9de8f372d and 35d1bfbd82b. Evidence: org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.7.0_AE_CloudOps~NFRA1/r5/step3_keyfn_before.txt, step3_keyfn_deploy.txt, step3_remote_head_ancestor.txt | CLOSED 20261021T174223Z |
| L8 | activation | infra/aws/ec2/canonical-schwab-si2/sdd-daily-pull.ps1 to s3://opal-data-assets/code/canonical-schwab-si2/sdd-daily-pull.ps1 | head-object ETag equals the repo file md5 | PRE-CHECK: repo file infra/aws/ec2/canonical-schwab-si2/sdd-daily-pull.ps1 line 305 reads the pipe form ($all = @($planItems \| ForEach-Object { $_ })); e2fea02fad is an ancestor of HEAD; index blob equals HEAD blob; md5 4555d652dda8ce569ec09bdee4f5e5fe, 51314 bytes. BEFORE (rollback anchor): ETag e49aea76a8c634c9d49e6a7cccc51bdf, 35853 bytes, SSE AES256, VersionId SMhvvWAbVOEv86DILTR.mBvF3uLSa0CP (2026-10-09); copy that version back to the same key to roll back. Uploaded with aws s3 cp --sse AES256 (cp rc=0 not taken as the oracle). AFTER head-object: ETag 4555d652dda8ce569ec09bdee4f5e5fe == repo md5, ContentLength 51314, SSE AES256, VersionId va6AYiIWWEtm2HUKANz6YpyDYkgT2T1w. Pickup is as the precedent entry L4: every scheduled pull re-fetches this object, so nothing else was changed (no rule, task or box touched). Evidence: r5/step4_puller_before.txt, r5/step4_puller_after.txt under org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.7.0_AE_CloudOps~NFRA1/ | CLOSED 20261021T174351Z |

## Log

- 20261021T173210Z OPENED by 0.7.0_AE_CloudOps~NFRA1 with 2 leg(s)
- 20261021T174223Z LEG L7 closed: Deployed by safe_deploy_core.deploy_file (the pre-push gate's own function and key; the push itself deployed nothing) to
- 20261021T174351Z LEG L8 closed: PRE-CHECK: repo file infra/aws/ec2/canonical-schwab-si2/sdd-daily-pull.ps1 line 305 reads the pipe form ($all = @($planI
- 20261021T174412Z CLOSED -- all 2 legs proven
