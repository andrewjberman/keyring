# Deploy Completion Record
**Date opened:** 2026-10-13T15:10:58.267458+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261013T151600Z
**Deploy:** IRPT_ANLREQ TO-SCRATCH-R21: live arm of the AR-y-222 fix (build-and-upload.sh at 9ffca59db9, blob 372c3240fb): real run through a temp map with the upload landing on investor-reporting/_ar222_scratch/ only; no function key, Lambda, Terraform or repository map moves
**Authored by:** 0.7.0_AE_CloudOps~AQ2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| S1 | verify | detached worktree at trunk head containing 9ffca59db9; script blob equals 372c3240fb; BEFORE reads of irpt-status key, repository map row and CodeSha256; temp map key read back; open-entry denominator | reads printed | worktree f970b40f11 detached at trunk head, contains 9ffca59db9 (merge-base --is-ancestor true); script blob 372c3240fb162fd2249a9613d92b12be2119db7d equals the order; BEFORE: irpt-status.zip latest 2_5Slkao1AtJWcv9J0kJZvk7HHXP1hV0 of 64 versions, repository map irpt-status artifact_s3_key investor-reporting/irpt-status.zip artifact_sha256 vlGh380Q.., CodeSha256 vlGh380Q..; temp map key read back investor-reporting/_ar222_scratch/ar222-20261013T151208.zip, worktree map still the real key. Denominator: 48 worktrees, 102 entries, 20 name the bucket or an investor-reporting path, 18 CLOSED on trunk; the 2 not closed (irpt-dashbd-thresholds-swap OPEN, names only the TF root investor-reporting/reporting-gold, upload leg closed; secclass-e57e61 HELD, mdpf-secclass key) name no key under the investor-reporting prefix of the artifact bucket. | CLOSED 20261013T151242Z |
| S2 | s3-prefix | real run of build-and-upload.sh investor-reporting irpt-status via BAU_SOURCE_MAP_OVERRIDE, no BUILD_ONLY, upload to the scratch key | exit code, SHA256 line, size, verify line | Real run, no BUILD_ONLY, through the temp map: exit_code=1, UPLOAD NOT VERIFIED. The object LANDED at the scratch key (VersionId RIwe3hOh..., 363594 bytes); the script's two scalar head-object reads returned the right values but each preceded by a .tools/aws shim WARN line (the worktree's sparse cone has no .tools), merged in by the script's 2>&1, so the compare failed. Temp map not updated. The fix is not proven on this CLI in this worktree. SCRATCH_RUN.txt | CLOSED 20261013T151514Z |
| S3 | verify | scratch object head-object size and content-sha256 equal the run; scratch prefix version count; real map row, irpt-status.zip latest and CodeSha256 unchanged | equalities printed | scratch head-object ContentLength 363594 and content-sha256 vlGh380Q.. equal the script's size and SHA256 line; 1 version under _ar222_scratch/; irpt-status.zip latest 2_5Slkao1.. (64 versions), real map row and CodeSha256 vlGh380Q.. all equal BEFORE. SCRATCH_READBACK.txt | CLOSED 20261013T151515Z |

## Log

- 20261013T151058Z OPENED by 0.7.0_AE_CloudOps~AQ2 with 3 leg(s)
- 20261013T151242Z LEG S1 closed: worktree f970b40f11 detached at trunk head, contains 9ffca59db9 (merge-base --is-ancestor true); script blob 372c3240fb1
- 20261013T151514Z LEG S2 closed: Real run, no BUILD_ONLY, through the temp map: exit_code=1, UPLOAD NOT VERIFIED. The object LANDED at the scratch key (V
- 20261013T151515Z LEG S3 closed: scratch head-object ContentLength 363594 and content-sha256 vlGh380Q.. equal the script's size and SHA256 line; 1 versio
- 20261013T151600Z CLOSED -- all 3 legs proven
