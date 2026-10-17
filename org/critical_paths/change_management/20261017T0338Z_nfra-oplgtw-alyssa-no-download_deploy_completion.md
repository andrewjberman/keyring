# Deploy Completion Record
**Date opened:** 2026-10-17T03:38:13.996323+00:00
**Status:** OPEN
**Deploy:** NFRA_OPLGTW OG-ap-35 Phase B: narrow one client's live Schwab grant by one key (remove download_filtered), ask sha256 224a80d88a52, halves CTO df73e21192 COO 4aea561614 CVO 03311f4476, GO msg 35330; the CTO ruling aed4469fa6 enforces Andrew's 2026-10-08 word
**Authored by:** 0.7.0_AE_CloudOps~NFRA1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| write | activation | ONE activate of ONE record through ops/schwab_entitlement_admin.py under opal-gateway-access-admin: her grant revision 4 to 5 with operations minus download_filtered, nothing else changed; her email_deny record re-put unchanged | proof: the ACTIVATED line (profile_revision 5 grant_revision 5), her grant and profile read back at revision 5, scope without operations hash equal to the before hash, the other two principals grant hashes equal, the email_deny hash before equal to after |  | OPEN |
| read-back | verify | through the INSTALLED code on the host: the entitlement decision for her principal refuses download_filtered and answers list; no call as her, no contact with her or her firm | proof: W/AG1_AFTER.json with download_refused true and other_operation_answers true |  | OPEN |

## Log

- 20261017T033813Z OPENED by 0.7.0_AE_CloudOps~NFRA1 with 2 leg(s)
