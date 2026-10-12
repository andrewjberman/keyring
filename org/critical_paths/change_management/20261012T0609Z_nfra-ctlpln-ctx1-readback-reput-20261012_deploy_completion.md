# Deploy Completion Record
**Date opened:** 2026-10-12T06:09:33.450349+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261012T061154Z
**Deploy:** NFRA_CTLPLN TO-CT-x-1 AMENDMENT 3 (WORLD): idempotent re-put of s3://opal-data-mdpf/code/scripts/bronze/pull_orion_model_composition.py, identical bytes, under named commit d5cd8a81c45fee2f154d8541f2002495a836d1ed, then deploy_readback_check.py; no content change to any deployed object
**Authored by:** 0.7.0_AE_CloudOps~CT1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | repo blob at HEAD 1b1f7c76a5 versus the live S3 object, sha256 both printed, previous VersionId recorded | equal sha256 and length, both digests and the VersionIds | PASS: repo blob at HEAD 1b1f7c76a5 (git show HEAD:data/mdpf/scripts/bronze/pull_orion_model_composition.py) sha256 40bdb218e94d3ff9c26f2920bb106720c63d0ab8bed06ec1fe5feaa1a4c4a8a9 len 9292; live s3://opal-data-mdpf/code/scripts/bronze/pull_orion_model_composition.py (s3api get-object) sha256 40bdb218e94d3ff9c26f2920bb106720c63d0ab8bed06ec1fe5feaa1a4c4a8a9 len 9292, equal=True, DELTA=0. Live VersionId knZ1fVt_6weNcIIalL9EUYzC7sUlp0W5 (2026-10-11T05:00:23Z, ETag e64b70fe47621d5df4f87c0fa93efa70, binary/octet-stream, AES256); previous VersionId HDdC0.EbCm8OEwh5kgCid1O92DgeZrkm (2026-05-20, 8542 B) is the rollback. Bucket versioning Enabled (read). s3:PutObject on the key simulates allowed for cloudops-dell1-agent-user. | CLOSED 20261012T060953Z |
| L2 | s3-prefix | s3://opal-data-mdpf/code/scripts/bronze/pull_orion_model_composition.py re-put with the same bytes (s3api put-object) | post-put object sha256 equals the repo blob; head-object fields; new VersionId | PASS: s3api put-object of the repo blob (body sha256 40bdb218e94d3ff9c26f2920bb106720c63d0ab8bed06ec1fe5feaa1a4c4a8a9, 9292 B) to s3://opal-data-mdpf/code/scripts/bronze/pull_orion_model_composition.py at 2026-10-12T06:10:05Z: new VersionId 0DSxbmDeumKfz1pZMD2LFZVOu4UejpYu, ETag e64b70fe47621d5df4f87c0fa93efa70 UNCHANGED, ContentType binary/octet-stream and ServerSideEncryption AES256 UNCHANGED, Metadata {} UNCHANGED, length 9292 UNCHANGED. Read back by get-object: sha256 40bdb218e94d3ff9c26f2920bb106720c63d0ab8bed06ec1fe5feaa1a4c4a8a9 len 9292, equal to the repo blob. Versions now: 0DSxbmDe (latest), knZ1fVt_ (2026-10-11, identical bytes), HDdC0.Eb (2026-05-20, 8542 B). Pre-image for rollback: knZ1fVt_6weNcIIalL9EUYzC7sUlp0W5 (identical bytes, none needed). | CLOSED 20261012T061041Z |
| L3 | git | the named commit d5cd8a81c4 published on the scratch ref origin/dell1/readback-20261012T0608Z only | ls-remote read of the ref; box/dell1 and CLOUD do not contain it | PASS: ls-remote origin read 2026-10-12 ~06:12Z: refs/heads/dell1/readback-20261012T0608Z = d5cd8a81c45fee2f154d8541f2002495a836d1ed (the ONE ref pushed, from the scratch worktree whose HEAD is that branch, no override); refs/heads/box/dell1 = 2b46c900c5 and refs/heads/CLOUD = fc18f94b5e, after git fetch origin: merge-base --is-ancestor d5cd8a81c45fee2f154d8541f2002495a836d1ed origin/box/dell1 = false and origin/CLOUD = false; git branch -r --contains = origin/dell1/readback-20261012T0608Z only. Scratch ref kept as the record. | CLOSED 20261012T061117Z |
| L4 | verify | named_commit recorded in this entry by named_commit_check.py --record | the NAMED-COMMIT-LEDGER line | PASS: named_commit_check.py check --commit d5cd8a81c45fee2f154d8541f2002495a836d1ed --record (DEPLOY_LEDGER_SLUG=nfra-ctlpln-ctx1-readback-reput-20261012 AGENTBUS_DEVICE=dell1): NAMED-COMMIT ADMITTED role=execution trunk=OFF-TRUNK branch=dell1/readback-20261012T0608Z reason=published on origin/dell1/readback-20261012T0608Z; NAMED-COMMIT-LEDGER entry carries named_commit=d5cd8a81c45fee2f154d8541f2002495a836d1ed trunk=OFF-TRUNK branch=dell1/readback-20261012T0608Z device=dell1. | CLOSED 20261012T061131Z |
| L5 | verify | deploy_readback_check.py read-back on the named commit | the DEPLOY-READBACK last line with on_trunk=False objects_equal=1/1 | PASS on the three data limbs, run #1 with this entry still OPEN (the read-back's step 4 reads CLOSED, and this leg is the last one open, so ledger=open is by construction): DEPLOY-READBACK commit=d5cd8a81c45fee2f154d8541f2002495a836d1ed device=dell1 admitted=True on_trunk=False objects_equal=1/1 ledger=open ok=False failed=ledger; STEP 3 git_sha256=deployed_sha256=40bdb218e94d3ff9c26f2920bb106720c63d0ab8bed06ec1fe5feaa1a4c4a8a9 len 9292 equal=True. The entry closes next and run #2 (ledger=closed-named expected) is filed in NFRA_CTLPLN.TO-CT-x-1.readback.txt. | CLOSED 20261012T061154Z |

## Log

- 20261012T060933Z OPENED by 0.7.0_AE_CloudOps~CT1 with 5 leg(s)
- 20261012T060953Z LEG L1 closed: PASS: repo blob at HEAD 1b1f7c76a5 (git show HEAD:data/mdpf/scripts/bronze/pull_orion_model_composition.py) sha256 40bdb
- 20261012T061041Z LEG L2 closed: PASS: s3api put-object of the repo blob (body sha256 40bdb218e94d3ff9c26f2920bb106720c63d0ab8bed06ec1fe5feaa1a4c4a8a9, 9
- 20261012T061117Z LEG L3 closed: PASS: ls-remote origin read 2026-10-12 ~06:12Z: refs/heads/dell1/readback-20261012T0608Z = d5cd8a81c45fee2f154d8541f2002
- 20261012T061119Z NAMED-COMMIT named_commit=d5cd8a81c45fee2f154d8541f2002495a836d1ed trunk=OFF-TRUNK branch=dell1/readback-20261012T0608Z device=dell1
- 20261012T061131Z LEG L4 closed: PASS: named_commit_check.py check --commit d5cd8a81c45fee2f154d8541f2002495a836d1ed --record (DEPLOY_LEDGER_SLUG=nfra-ct
- 20261012T061154Z LEG L5 closed: PASS on the three data limbs, run #1 with this entry still OPEN (the read-back's step 4 reads CLOSED, and this leg is th
- 20261012T061154Z CLOSED -- all 5 legs proven
