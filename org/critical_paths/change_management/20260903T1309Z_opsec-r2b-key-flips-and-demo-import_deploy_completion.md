# Deploy Completion Record
**Date opened:** 2026-09-03T13:09:37.482066+00:00
**Status:** OPEN
**Deploy:** NFRA_OPSEC202609.TO-OP-S-16-17-8R2 -- address table onto the project key (in place) + opal-partner-demo terraform import; the BUCKET limb is HELD NOT ATTEMPTED per issuer ruling 19793 on row Z-S37
**Authored by:** 0.7.0_AE_CloudOps~S
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | dynamodb.tf flip + demo import declaration committed under 0.7.0_AE_CloudOps~S | commit hash |  | OPEN |
| L2 | activation | safe-apply of the table flip (0 add, 1 change, 0 destroy) -- ROLLBACK: revert kms_key_arn to absent, an in-place UpdateTable back to the AWS-managed key | apply output |  | OPEN |
| L3 | verify | opal-suspicious-addresses SSEType KMS with KMSMasterKeyArn = the PROJECT key; TableId b4af2a9e + CreationDateTime IDENTICAL before/after (the replace control); PITR/DP/stream/GSI unchanged | pasted reads |  | OPEN |
| L4 | activation | terraform import of opal-partner-demo under the tick-2 bar (plan captured BEFORE any settings change: 0 add / 0 destroy / no forces-replacement / DP unchanged-or-true) -- ROLLBACK: terraform state rm, which returns the table to unmanaged and changes nothing live | import + plan output |  | OPEN |
| L5 | verify | demo table in-place diffs are EXACTLY the two expected (SSE AWS-owned -> AWS-managed KMS, PITR OFF -> ON); DP never true->false; the three real firm tables ABSENT from the plan; TableId 99ddc090 identical | pasted reads |  | OPEN |
| L6 | verify | both modules re-plan 0-diff after the last apply; push state MEASURED | plan + ls-remote |  | OPEN |

## Log

- 20260903T130937Z OPENED by 0.7.0_AE_CloudOps~S with 6 leg(s)
