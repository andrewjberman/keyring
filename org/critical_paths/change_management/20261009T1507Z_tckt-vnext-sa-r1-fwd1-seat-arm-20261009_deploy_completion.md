# Deploy Completion Record
**Date opened:** 2026-10-09T15:07:32.232230+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261009T154842Z
**Deploy:** TCKT_VNEXT SA-r-1: ONE live FWD-1 journey as a synthetic test filer through CloudFront (pair v2.1, CTO half @85c6dc8fe7)
**Authored by:** 0.7.0_AE_CloudOps~TV2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| ROW | verify | opal-users-v2 | conditional put attribute_not_exists(PK) of USER#tckt-fwd1-testfiler-20261009@opal.invalid + read back present | conditional put accepted (attribute_not_exists(PK) held); ConsistentRead get-item read back present with userType={S:test-filer}, firmId={S:opal-capital}, allowedFirmIds={L:[{S:49financial}]} (type tag L), status={S:active} | CLOSED 20261009T152557Z |
| TOK | verify | opal/auth/jwt-private-key | CURRENT slot read into memory only, RS256, exp=iat+2h; never printed/stored/committed; first read reported after the run via MSTR~DELL2 | ONE RS256 token minted in-process from the CURRENT slot of opal/auth/jwt-private-key (bare PEM = current slot per lambda/lib/authkeys/jwtPublicKeys.mjs); iat 2026-10-09T15:40:57Z exp 17:40:57Z (iat+2h); held in memory only -- never printed, stored or committed; left to expire, not revoked. Key read reported after the fact to 0.0.0_AB_MSTR~DELL2 by secret name and run id. | CLOSED 20261009T154841Z |
| RUN | verify | CloudFront journey | one-firm proof BEFORE any hop (27 clamped routes x 49financial+cottonwood, ONE_FIRM sample, one data-refresh route; any cottonwood or data-refresh admit = STOP) then hops a-g recorded in R1_RUN/sa_r1_trace.json, status+artifact id only, NO client figures | One-firm proof ran BEFORE any hop (CTO half v2.1 condition 1). Measured over 27 clamped routes = 21 IRPT + 6 ticket-api: 22 of 22 EXERCISED arms refused cottonwood, 0 admits (all 21 IRPT returned public_reason_code FIRM_BINDING; GET /api/scoped/tickets list returned 8 tickets, distinct requester firms ['49financial'] only). 5 ticket-api arms recorded NOT_EXERCISED (their gate keys on the ticket's requester.firm and a synthetic id refuses at cur is None -- NOT-FOUND is indistinguishable from a clamp refusal, so counting it would be ABSENT read as EXERCISED-AGAINST). Instrument control: own-firm arms returned varied codes (NOT_FOUND/INVALID_INPUT/OBJECT_NOT_COVERED/None), NOT a uniform 401, so the clamp was genuinely reached. STOP MET: data-refresh GET /api/scoped/data-refresh/history admitted at HTTP 200 -> per step 4 no hop ran. Trace: R1_RUN/sa_r1_trace.json. Row TCKT_VNEXT-D2-S16 filed. | CLOSED 20261009T154841Z |
| CLN | verify | cleanup same session | row REMOVEd and read back absent; test ticket COMPLETED by the same principal; token left to expire | Cleanup in the same session: filer row deleted and ConsistentRead get-item read back ABSENT (True). No ticket was created (the STOP preceded hop (a)), so there was nothing to complete -- recorded as NO_TICKET_CREATED rather than as a pass. Token left to expire at 17:40:57Z; no IAM, code or route change was made. | CLOSED 20261009T154842Z |

## Log

- 20261009T150732Z OPENED by 0.7.0_AE_CloudOps~TV2 with 4 leg(s)
- 20261009T152557Z LEG ROW closed: conditional put accepted (attribute_not_exists(PK) held); ConsistentRead get-item read back present with userType={S:tes
- 20261009T154841Z LEG TOK closed: ONE RS256 token minted in-process from the CURRENT slot of opal/auth/jwt-private-key (bare PEM = current slot per lambda
- 20261009T154841Z LEG RUN closed: One-firm proof ran BEFORE any hop (CTO half v2.1 condition 1). Measured over 27 clamped routes = 21 IRPT + 6 ticket-api:
- 20261009T154842Z LEG CLN closed: Cleanup in the same session: filer row deleted and ConsistentRead get-item read back ABSENT (True). No ticket was create
- 20261009T154842Z CLOSED -- all 4 legs proven
