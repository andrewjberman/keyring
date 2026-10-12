# Deploy Completion Record
**Date opened:** 2026-10-12T12:38:13.171511+00:00
**Status:** OPEN
**Deploy:** NFRA_MCPORTAL MP-n-1 (PRD v0.6 C17 + AMENDMENT 1): the bounded gitstate read, released on live base d9f2ebded9
**Authored by:** 0.7.0_AE_CloudOps~MP
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

**PRE-ACT RECORD (the base-by-md5 read and its control, CTO-1's four terms, the rollback proof, the load samples and the census -- AMENDMENT 4: this entry carries only this pointer, because `deploy_ledger.py` regenerates the entry and drops appended prose, rows Z-S24/Z-S25):** `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.7.0_AE_CloudOps~MP/MP-n-1_PRE_ACT_RECORD.md` on branch `rel-nfra-mcportal-c17-v2`

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | release build + upload to s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway | head-object on the NEW versioned key AND on the rollback key opal-gateway-d9f2ebded9.tar.gz, which must still read ETag 18b56591a0201d43857c5adf3d955026 (COO condition C-1) |  | OPEN |
| L2 | ec2-baked-asset | SSM pull + restart on i-07dccb1615503ac99 | SSM md5 of the RUNNING /opt/opal-gateway/app files equals the release bytes, with a negative control against the base |  | OPEN |
| L3 | verify | served read-back: /health 200, gitstate 401/403 with no identity, the served cold read at or under 10 s with its body-fetch count, tool-surface difference empty | the read-backs, each independent of the deploy rc; graded by n1.AC3 |  | OPEN |
| L4 | git | manifest record on the release branch AND on box/sitez | deployed_commit/previous_deployed_commit/release_note, the box/sitez record written on top of its current EC2_MANIFEST per msg 33482 |  | OPEN |

## Log

- 20261012T123813Z OPENED by 0.7.0_AE_CloudOps~MP with 4 leg(s)
