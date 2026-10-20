# Deploy Completion Record
**Date opened:** 2026-10-20T07:17:40.704244+00:00
**Status:** OPEN
**Deploy:** NFRA_OPLGTW OG-ms-2 Phase B: add Schwab master 08403355 to ALYSSA's grant only (scope.masters and scope.accounts[08403355]); database-only, no deploy, no delete; Andrew's grant untouched; batch15 ledger CLOSED 20261020T070552Z
**Authored by:** 0.7.0_AE_CloudOps~NFRA1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| release-live | verify | the live marker equals batch15 13917ef993 and the deployed MASTERS lists the new master | proof: W/ms2_pb/step1_before.json and pre.json |  | OPEN |
| alyssa-write | verify | Alyssa's candidate activated through ops/schwab_entitlement_admin.py activate under opal-gateway-access-admin, approver Andrew Berman | proof: the ACTIVATED line in W/MS2_WRITE.md |  | OPEN |
| read-back | verify | strongly consistent live read plus decide() of the DEPLOYED tree on her live grant admits the four read tools and refuses schwab_prepare_download | proof: W/MS2_AFTER.json and W/MS2_READBACK_DECIDE.json |  | OPEN |

## Log

- 20261020T071740Z OPENED by 0.7.0_AE_CloudOps~NFRA1 with 3 leg(s)
