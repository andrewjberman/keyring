# Deploy Completion Record
**Date opened:** 2026-10-16T09:09:14.843960+00:00
**Status:** OPEN
**Deploy:** AMGT_RESAPP AMGT-ar-8: ONE environment entry AMGT_AIFILL_ROOT=/var/empty/aifill-hold removed from module scoped_amgt_api in infra/aws/terraform/harvest/scoped-amgt-api.tf; ONE targeted safe-apply of module.scoped_amgt_api; stored AI-fill documents served again; code, role, memory, timeout unchanged; rollback is re-adding the one entry and the same targeted apply
**Authored by:** 0.7.0_AE_CloudOps~RA1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | live configuration printed (LastModified, CodeSha256, memory, timeout, Environment, RevisionId) | printed output equal to the order's cut |  | OPEN |
| L2 | verify | pre-act capture of the four /thesis bodies immediately before the apply | capture line |  | OPEN |
| L3 | git | the one environment entry and its comment block removed, nothing else touched | diff of the file |  | OPEN |
| L4 | verify | targeted plan graded from plan JSON: ONE in-place change, environment only | plan JSON graded |  | OPEN |
| L5 | activation | ONE targeted safe-apply of the saved plan; function configuration after | apply output + config |  | OPEN |
| L6 | verify | AC1 check_restore_served.py verify, AC2 earlier-serve censuses, AC3 configuration read | criteria output |  | OPEN |
| L7 | git | record, commit and report to the issuer | commit hash + message |  | OPEN |

## Log

- 20261016T090914Z OPENED by 0.7.0_AE_CloudOps~RA1 with 7 leg(s)
