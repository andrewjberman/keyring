# Deploy Completion Record
**Date opened:** 2026-09-09T15:40:03.511918+00:00
**Status:** OPEN
**Deploy:** D12 SMS: toll-free number +18664067943 requested, US_TOLL_FREE_REGISTRATION filed, TextMessageMonthlySpend increase to USD 50 requested -- Andrew-direct 2026-09-09 ~15:4xZ 'Whatever must be done to initiate SMS registrations and proceedings to make this operational should be pursued now.' Carrier review 1-3 weeks; the spend approval is the account-level sandbox exit the D12 watch item SP-3 requires a reviewed SMS_VERIFIED_DESTINATIONS commit against.
**Authored by:** 0.0.0_AB_MSTR
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 504.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A | activation | toll-free number phone-0e98f7739a16415c83d951336a7da12a (+18664067943) requested TRANSACTIONAL/SMS | describe-phone-numbers Status=ACTIVE | TRANSCRIBED, not asserted: this proof was measured by 0.0.0_AB_MSTR and written into the markdown table on 2026-09-13, where it reads 'CLOSED 20260913T062910Z'. It never reached this JSON index, so the tool has counted the leg OPEN for 11 days. Original text: describe-phone-numbers 2026-09-13T06:2xZ by 0.0.0_AB_MSTR: phone-0e98f7739a16415c83d951336a7da12a Status=ACTIVE NumberType=TOLL_FREE MessageType=TRANSACTIONAL, ends 7943. RE-VERIFIED LIVE 2026-09-24T05:4xZ by 1.0.0_SA_CTO~Z: +18664067943 ACTIVE TOLL_FREE TRANSACTIONAL TwoWayEnabled=false. | CLOSED 20260924T054919Z |
| B | activation | US_TOLL_FREE_REGISTRATION registration-3721e9ded2cd4adaa831a42ba6d60e4c: 18 fields put, attachment-4cf99cb640da4060b0148f8250c43e01 attached, number associated, version submitted | describe-registrations RegistrationStatus in SUBMITTED/REVIEWING with CurrentVersionNumber and the version's SUBMITTED timestamp | describe-registrations 2026-09-09T15:44Z: RegistrationStatus=SUBMITTED, CurrentVersionNumber=1; describe-registration-versions: version 1 REVIEWING, SubmittedTimestamp=1788968676 ReviewingTimestamp=1788968680; 22 of 22 field values on file (describe-registration-field-values); association ResourceId=phone-0e98f7739a16415c83d951336a7da12a (+18664067943); attachment-4cf99cb640da4060b0148f8250c43e01 UPLOAD_COMPLETE | CLOSED 20260909T154516Z |
| C | activation | service-quotas sms-voice L-2325465C desired 50, request 3f0cd234bd99405ab57967d9e4c96e8dO5rvrxd2 | get-requested-service-quota-change Status=PENDING or CASE_OPENED | request-service-quota-increase 2026-09-09T15:39Z: RequestedQuota.Id=3f0cd234bd99405ab57967d9e4c96e8dO5rvrxd2 QuotaCode=L-2325465C DesiredValue=50.0 Status=PENDING Requester=arn:aws:iam::313476888478:user/Andrew_Berman | CLOSED 20260909T154516Z |
| V1 | verify | carrier verification COMPLETE | describe-registrations RegistrationStatus=COMPLETE and the TFN's registration association read from describe-phone-numbers | TRANSCRIBED, not asserted: measured by 0.0.0_AB_MSTR, written into the markdown table 2026-09-13 as 'CLOSED 20260913T062911Z', never reached this JSON index. Original text: describe-registrations 2026-09-13T06:2xZ: registration-3721e9ded2cd4adaa831a42ba6d60e4c US_TOLL_FREE_REGISTRATION RegistrationStatus=COMPLETE ApprovedVersionNumber=1; describe-phone-numbers shows the TFN RegistrationId=registration-3721e9ded2cd4adaa831a42ba6d60e4c. NOTE the carrier gate this leg tracks ('~1-3 WEEK EXTERNAL CARRIER gate') is therefore DISCHARGED and the D12 project row still describes it as pending. | CLOSED 20260924T054919Z |
| V2 | verify | account leaves the sandbox | describe-account-attributes ACCOUNT_TIER=PRODUCTION and describe-spend-limits TEXT_MESSAGE_MONTHLY_SPEND_LIMIT EnforcedLimit=50 | describe-account-attributes 2026-09-24T05:4xZ by 1.0.0_SA_CTO~Z: ACCOUNT_TIER=PRODUCTION (sole attribute returned). describe-spend-limits same read: TEXT_MESSAGE_MONTHLY_SPEND_LIMIT EnforcedLimit=50 MaxLimit=50 Overridden=false; MEDIA 50/50, VOICE 1/1, NOTIFY 1/1, RCS 1/1 for scope. BOTH halves of this leg's stated clause satisfied verbatim. World-done and previously unrecorded -- closed SUPERSEDED rather than re-executed (no act was performed by this seat; reads only). | CLOSED 20260924T054812Z |
| V3 | verify | SP-3 of .open_deploys/d12-sms-origination-identity-activation.json: SMS_VERIFIED_DESTINATIONS + SMS_ALLOW_UNVERIFIED re-read in a reviewed commit BEFORE or WHEN V2 lands | commit hash under 0.7.0_AE_CloudOps author line |  | OPEN |

## Log

- 20260909T154003Z OPENED by 0.0.0_AB_MSTR with 6 leg(s)
- 20260909T154516Z LEG B closed: describe-registrations 2026-09-09T15:44Z: RegistrationStatus=SUBMITTED, CurrentVersionNumber=1; describe-registration-ve
- 20260909T154516Z LEG C closed: request-service-quota-increase 2026-09-09T15:39Z: RequestedQuota.Id=3f0cd234bd99405ab57967d9e4c96e8dO5rvrxd2 QuotaCode=L
- 20260924T054812Z LEG V2 closed: describe-account-attributes 2026-09-24T05:4xZ by 1.0.0_SA_CTO~Z: ACCOUNT_TIER=PRODUCTION (sole attribute returned). desc
- 20260924T054919Z LEG A closed: TRANSCRIBED, not asserted: this proof was measured by 0.0.0_AB_MSTR and written into the markdown table on 2026-09-13, w
- 20260924T054919Z LEG V1 closed: TRANSCRIBED, not asserted: measured by 0.0.0_AB_MSTR, written into the markdown table 2026-09-13 as 'CLOSED 20260913T062
