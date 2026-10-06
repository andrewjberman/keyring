# Deploy Completion Record
**Date opened:** 2026-10-06T18:54:57.529747+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261006T190049Z
**Deploy:** NFRA_OPLGTW OG-ga-1: add download_filtered to the one live dim_asset grant (S41, Andrew-direct; ca460bf9fe) then download as the holder
**Authored by:** 0.9.0_WK_NFRA_OPLGTW~28
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| write | activation | one new data_entitlement revision for the one dim_asset holder via ops/schwab_entitlement_admin.py activate under opal-gateway-access-admin | ACTIVATED profile_revision/grant_revision line | ACTIVATED profile_revision=3 grant_revision=3 (activate under opal-gateway-access-admin, rc=0; scope change operations +download_filtered only; GA1_WRITE.md) | CLOSED 20261006T190039Z |
| read-back | verify | ga1.AC1.sh: 1 in-force dim_asset grant carrying download_filtered at a new revision; other dimensions and other principals unchanged | RESULT: PASS output | ga1.AC1.sh: in-force active dim_asset grants 1; of them carrying download_filtered 1; revision advanced True; other dimensions unchanged True; other principals unchanged True; RESULT: PASS exit=0 | CLOSED 20261006T190040Z |
| download | verify | real-holder dim_asset download on the gateway host via SSM, held CUSIPs only | GA1_DOWNLOAD.json + ga1.AC2.sh RESULT: PASS | ran: real-holder dim_asset download on i-07dccb1615503ac99 ssm dca27ce0 Success, dim_asset_download OK, GA1_DOWNLOAD.json written, digest in host output; ga1.AC2.sh RESULT: FAIL (unheld_returned 23 = blank-cusip rows, 0 non-blank unheld; row Z-W28-S1 BLOCKING); the grant write itself is complete and stays in force | CLOSED 20261006T190040Z |

## Log

- 20261006T185457Z OPENED by 0.9.0_WK_NFRA_OPLGTW~28 with 3 leg(s)
- 20261006T190039Z LEG write closed: ACTIVATED profile_revision=3 grant_revision=3 (activate under opal-gateway-access-admin, rc=0; scope change operations +
- 20261006T190040Z LEG read-back closed: ga1.AC1.sh: in-force active dim_asset grants 1; of them carrying download_filtered 1; revision advanced True; other dime
- 20261006T190040Z LEG download closed: ran: real-holder dim_asset download on i-07dccb1615503ac99 ssm dca27ce0 Success, dim_asset_download OK, GA1_DOWNLOAD.jso
- 20261006T190049Z CLOSED -- all 3 legs proven
