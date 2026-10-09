# Deploy Completion Record
**Date opened:** 2026-10-09T14:13:56.626401+00:00
**Status:** OPEN
**Deploy:** ADVI_COTBKF round 41 CB-ao-1: deploy the cot gold _ff_worker carry-forward STAMP -- ONE new version of s3://opal-data-cot/code/gold/B_00.canonical_holdings.py (prior BMqu7SNCbx2f3bQ_Tr56xMBCvtMe3van sha 6dbf6a86... -> HEAD sha 45fbbd92...), under never-widen pair COO half @3089cde892 + CTO half @9dd6703dd1 GIVEN under conditions 1-4. Prior version KEPT; nothing deleted. This closes the hazard this seat surfaced at CB-aj-2 gate C2
**Authored by:** 0.7.0_AE_CloudOps~CB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| C1 | verify | census the deploy BEFORE the write -- diff the deployed bytes fetched at the prior VersionId against the repo HEAD file | the diff printed with its line counts, and EVERY changed line inside _ff_worker (HEAD lines 1339-1395); any line outside is a STOP and nothing is written; repo HEAD file sha256 equals 45fbbd921f026f9d4e30785e632c8f8e0feeb02730f033b96fd03b23da74c08d |  | OPEN |
| D1 | activation | write the one key with .tools/safe-deploy.sh, key list printed FIRST | the planned key list printed before the write and holding EXACTLY ONE key (code/gold/B_00.canonical_holdings.py); the prior VersionId re-read immediately before and still BMqu7SNCbx2f3bQ_Tr56xMBCvtMe3van; a lane refusal (rule 13 names DS for data/*/scripts/gold) STOPS the order and is NOT bypassed |  | OPEN |
| P1 | verify | fetch the new served object back and confirm its sha256 | served sha256 equals 45fbbd921f026f9d4e30785e632c8f8e0feeb02730f033b96fd03b23da74c08d, and the prior version still retrievable as the rollback source |  | OPEN |
| V1 | verify | CB41ao1-AC1 -- the proof test run against the FETCHED SERVED bytes in a detached scratch worktree, never the repo copy | git worktree add --detach at HEAD, the fetched bytes placed at data/cot/scripts/gold/B_00.canonical_holdings.py there, python -m pytest data/cot/scripts/gold/tests/test_b00_ff_carry_claim.py -q reads passed, the import path recorded, and the worktree removed after; the shared tree is not edited |  | OPEN |

## Log

- 20261009T141356Z OPENED by 0.7.0_AE_CloudOps~CB2 with 4 leg(s)
