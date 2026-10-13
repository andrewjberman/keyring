# Deploy Completion Record
**Date opened:** 2026-10-13T16:01:44.445985+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261013T160530Z
**Deploy:** IRPT_ANLREQ TO-SCRATCH-R21b: second live arm of the AR-y-229 fix (build-and-upload.sh at 25e92d4daa, blob eba6dc3da9): real run through a temp map, upload on investor-reporting/_ar222_scratch/ only; no function key, Lambda, Terraform or repository map moves
**Authored by:** 0.7.0_AE_CloudOps~AQ2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| S1 | verify | detached worktree at trunk head containing 25e92d4daa (same sparse cone, no .tools); script blob equals eba6dc3da9; BEFORE reads; temp map key read back; open-entry denominator | reads printed | worktree 876468fc1d detached at trunk head, contains 25e92d4daa (merge-base --is-ancestor true); script blob eba6dc3da97e9df525784382ee196077057140c6 equals the order; worktree made as in run 1 (sparse cone infra lib org/standards data/assets/scripts/gold/irpt_reporting; .tools absent: yes, so the shim WARN can reproduce); BEFORE: irpt-status.zip latest 2_5Slkao1AtJWcv9J0kJZvk7HHXP1hV0 of 64 versions, repository map irpt-status key investor-reporting/irpt-status.zip sha vlGh380Q.., CodeSha256 vlGh380Q..; temp map key read back investor-reporting/_ar222_scratch/ar222-20261013T160226.zip, worktree map still the real key. Denominator: 50 worktrees, 105 entries, 21 name the bucket or an investor-reporting path, 18 CLOSED on trunk; the 3 not closed (irpt-dashbd-thresholds-swap names a TF root only; healgap-r4-act-ht16 names a cot-pipeline key; secclass-e57e61 names an mdpf-secclass key) name no key under the artifact bucket's investor-reporting prefix. | CLOSED 20261013T160301Z |
| S2 | s3-prefix | real run of build-and-upload.sh investor-reporting irpt-status via BAU_SOURCE_MAP_OVERRIDE, no BUILD_ONLY, to the scratch key | exit code, SHA256 line, size, verify line | Real run, no BUILD_ONLY, through the temp map: exit_code=0, write VERIFIED size=363594 sha256 metadata match, temp map updated (scratch key + artifact_sha256 vlGh380Q..), SHA256 line vlGh380Q..; new object VersionId mtlPKxqyNGSRv0g2yPb0XM97pfHkf2Z0 under investor-reporting/_ar222_scratch/ar222-20261013T160226.zip. The shim WARN reproduced on stderr and did not enter the compare. SCRATCH2_RUN.txt | CLOSED 20261013T160527Z |
| S3 | verify | scratch object head-object size and content-sha256 equal the run; scratch prefix version count; real map row, irpt-status.zip latest and CodeSha256 unchanged | equalities printed | scratch head-object ContentLength 363594 and content-sha256 vlGh380Q.. equal the script's size and SHA256 line; 2 versions under _ar222_scratch/ (run 1 and this run); irpt-status.zip latest 2_5Slkao1.. (64 versions), REAL map row and CodeSha256 vlGh380Q.. all equal BEFORE. SCRATCH2_READBACK.txt | CLOSED 20261013T160527Z |

## Log

- 20261013T160144Z OPENED by 0.7.0_AE_CloudOps~AQ2 with 3 leg(s)
- 20261013T160301Z LEG S1 closed: worktree 876468fc1d detached at trunk head, contains 25e92d4daa (merge-base --is-ancestor true); script blob eba6dc3da97
- 20261013T160527Z LEG S2 closed: Real run, no BUILD_ONLY, through the temp map: exit_code=0, write VERIFIED size=363594 sha256 metadata match, temp map u
- 20261013T160527Z LEG S3 closed: scratch head-object ContentLength 363594 and content-sha256 vlGh380Q.. equal the script's size and SHA256 line; 2 versio
- 20261013T160530Z CLOSED -- all 3 legs proven
