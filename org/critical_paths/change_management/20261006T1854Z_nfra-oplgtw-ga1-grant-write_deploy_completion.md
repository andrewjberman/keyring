# Deploy Completion Record
**Date opened:** 2026-10-06T18:54:57.529747+00:00
**Status:** OPEN
**Deploy:** NFRA_OPLGTW OG-ga-1: add download_filtered to the one live dim_asset grant (S41, Andrew-direct; ca460bf9fe) then download as the holder
**Authored by:** 0.9.0_WK_NFRA_OPLGTW~28
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| write | activation | one new data_entitlement revision for the one dim_asset holder via ops/schwab_entitlement_admin.py activate under opal-gateway-access-admin | ACTIVATED profile_revision/grant_revision line |  | OPEN |
| read-back | verify | ga1.AC1.sh: 1 in-force dim_asset grant carrying download_filtered at a new revision; other dimensions and other principals unchanged | RESULT: PASS output |  | OPEN |
| download | verify | real-holder dim_asset download on the gateway host via SSM, held CUSIPs only | GA1_DOWNLOAD.json + ga1.AC2.sh RESULT: PASS |  | OPEN |

## Log

- 20261006T185457Z OPENED by 0.9.0_WK_NFRA_OPLGTW~28 with 3 leg(s)
