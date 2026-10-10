# Deploy Completion Record
**Date opened:** 2026-10-10T23:00:22.588125+00:00
**Status:** OPEN
**Deploy:** NFRA_MCPORTAL MP-r-2: the CP2 gateway release (overlap, gitstate, calls + the A5 load remedy) on live base d3c31e972e
**Authored by:** 0.7.0_AE_CloudOps~MP
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

**PRE-ACT RECORD (the full census, times, rollback proof and tool surface -- AMENDMENT 4; this entry carries only this pointer because `deploy_ledger.py` regenerates the entry and drops appended prose, rows Z-S24/Z-S25):** `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.7.0_AE_CloudOps~MP/MP-r-2_PRE_ACT_RECORD.md` on branch `rel-nfra-mcportal-cp2-v2`

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | bundle build: mcportal bc37107 dashboard built by deploy-to-ec2.sh from the manifest pin | build log + bun pre-check 77 of 77 |  | OPEN |
| L2 | s3-prefix | release build + upload to s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway | head-object len/ETag/git-ref on the versioned key AND -latest |  | OPEN |
| L3 | ec2-baked-asset | SSM pull + restart on i-07dccb1615503ac99 | SSM md5 of the RUNNING /opt/opal-gateway/app files equals the release bytes |  | OPEN |
| L4 | verify | post-act reads: /health 200, four routes 401/403 with no identity, tool surface difference EMPTY, manifest record | the read-backs, each independent of the deploy rc |  | OPEN |

## Log

- 20261010T230022Z OPENED by 0.7.0_AE_CloudOps~MP with 4 leg(s)
