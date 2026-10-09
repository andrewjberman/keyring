# Deploy Completion Record
**Date opened:** 2026-10-09T15:04:18.251570+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261009T150806Z
**Deploy:** AMGT_RESAPP round 86 AMGT-kk-3: five stored drafts s3://opal-data-harvest/drafting/v1/<KEY>.json edited in place (company_description from the business item only; NU sentences 6/11/19 whole); no fetch, no model call, no delete; dell1
**Authored by:** 0.9.0_WK_AMGT_RESAPP~343
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | drafting/v1/ASML_NA_Equity.json prior VersionId AHblHQYsQKRuezgUjaX9aNuVzcqgpI6A (2026-10-09T09:39:49Z, 125612 bytes); ROLLBACK = re-put prior bytes, never a delete | new VersionId; before/after drafting/v1 listing; served /thesis dossier description still present; outside-section count >= 16 | ASML drafting repaired in place: company_description 5 -> 0 (4x Item 5, 1x Item 3.D removed); prior AHblHQYsQKRuezgUjaX9aNuVzcqgpI6A (125612 B, untouched, rollback = re-put its bytes); NEW V0isdrasNyU1Umncd8Cii4pp.MVGHgPc (122394 B, sha256 4743071c... read back). Served dossier description still served (1535 chars, What started as...), 0 description sentences, 16 outside (base 16). Listing 47 -> 52 versions, 1 added per key (listing_diff.txt). AC2 and AC3 YES on the live function. | CLOSED 20261009T150805Z |
| L2 | verify | drafting/v1/BABA_US_Equity.json prior VersionId 1qNTUIXdb4c7AxTjIL2jeWdIVpwMgmjY (2026-10-09T11:36:13Z, 115657 bytes); ROLLBACK = re-put prior bytes, never a delete | new VersionId; listing; served description present; outside-section count >= 19 | BABA: company_description 1 -> 0 (1x Item 5 removed); prior 1qNTUIXdb4c7AxTjIL2jeWdIVpwMgmjY (115657 B, rollback = re-put); NEW nzqUee7dvuZWBrJEzo_pb3OBssIroB6c (115010 B, sha256 618fede0... read back). Served dossier description still served (1945 chars); 19 outside (base 19). Listing diff: 1 version added for this key. AC2/AC3 YES. | CLOSED 20261009T150806Z |
| L3 | verify | drafting/v1/NU_US_Equity.json prior VersionId I.NWiDvQCJPaU6FLUMRycOhwkVGzWxUb (2026-10-09T13:19:01Z, 107028 bytes); ROLLBACK = re-put prior bytes, never a delete | AC1 YES before any write; new VersionId; listing; served description present; outside-section count >= 28 | NU: AC1 YES before any write (K1 28/28, K2 0 restated 0 glued, K3 28/28 verbatim, K4 28/28). company_description 10 -> 1 (8x Item 5, 1x Item 3.D removed; the Item 4.B sentence kept); sentences 6 (removed, Item 5), 11, 19 restored to the whole filing sentence; prior I.NWiDvQCJPaU6FLUMRycOhwkVGzWxUb (107028 B, rollback = re-put); NEW ms8LxPe84kA9x8qb4L4f74vtKnlO2HRQ (96726 B, sha256 055cea68... read back). Served dossier description was ABSENT before and is absent after (no change); 28 outside (base 28). AC2/AC3 YES. | CLOSED 20261009T150806Z |
| L4 | verify | drafting/v1/PBR_US_Equity.json prior VersionId udNXabeQDGrI2lWggAed7LQkh.HbopbJ (2026-10-09T11:43:47Z, 94411 bytes); ROLLBACK = re-put prior bytes, never a delete | new VersionId; listing; served description present; outside-section count >= 22 | PBR: company_description 4 -> 0 (4x Item 5 removed); prior udNXabeQDGrI2lWggAed7LQkh.HbopbJ (94411 B, rollback = re-put); NEW HOuHcN523UASWJFYVVDH9zdEmOXtTKLZ (91375 B, sha256 28ff779b... read back). Served dossier description still served (721 chars); 22 outside (base 22). AC2/AC3 YES. | CLOSED 20261009T150806Z |
| L5 | verify | drafting/v1/SAP_GY_Equity.json prior VersionId PN03Mcrkm.OvgvMjGD1Va1xp5WLYNNiw (2026-10-09T11:40:26Z, 110389 bytes); ROLLBACK = re-put prior bytes, never a delete | new VersionId; listing; served description present; outside-section count >= 13 | SAP: company_description 5 -> 0 (5x Item 5 removed); prior PN03Mcrkm.OvgvMjGD1Va1xp5WLYNNiw (110389 B, rollback = re-put); NEW ppUca4bJJDMbWrhpDu178JeH8W2DxYnK (106830 B, sha256 f425fa0a... read back). Served dossier description still served (2408 chars); 13 outside (base 13). AC2/AC3 YES. | CLOSED 20261009T150806Z |

## Log

- 20261009T150418Z OPENED by 0.9.0_WK_AMGT_RESAPP~343 with 5 leg(s)
- 20261009T150805Z LEG L1 closed: ASML drafting repaired in place: company_description 5 -> 0 (4x Item 5, 1x Item 3.D removed); prior AHblHQYsQKRuezgUjaX9
- 20261009T150806Z LEG L2 closed: BABA: company_description 1 -> 0 (1x Item 5 removed); prior 1qNTUIXdb4c7AxTjIL2jeWdIVpwMgmjY (115657 B, rollback = re-pu
- 20261009T150806Z LEG L3 closed: NU: AC1 YES before any write (K1 28/28, K2 0 restated 0 glued, K3 28/28 verbatim, K4 28/28). company_description 10 -> 1
- 20261009T150806Z LEG L4 closed: PBR: company_description 4 -> 0 (4x Item 5 removed); prior udNXabeQDGrI2lWggAed7LQkh.HbopbJ (94411 B, rollback = re-put)
- 20261009T150806Z LEG L5 closed: SAP: company_description 5 -> 0 (5x Item 5 removed); prior PN03Mcrkm.OvgvMjGD1Va1xp5WLYNNiw (110389 B, rollback = re-put
- 20261009T150806Z CLOSED -- all 5 legs proven
