# Deploy Completion Record
**Date opened:** 2026-10-20T16:58:31.567490+00:00
**Status:** CLOSED -- STOPPED AT R (the commentary-pdf route refused UNEXPECTED: irpt-status-role denied s3:GetObjectVersion on the retained PDF, row S231); B1, B2, P1 to P5, P7 COMPLETE, B3 and R2 read; seven synthetic state objects stay, AccessDenied (row IRPT_ANLREQ-D2-S232) -- closed 20261020T171113Z
**Deploy:** IRPT_ANLREQ TO-RUN-COMMENTARY-E2E-7B: staff filing through the PROD portal page with the Advisor pre-filled by the page (ADDENDUM 9 terms): form, filing, four package pointers, Open report, route, sections
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A | verify | mint the synthetic staff user with a non-empty name and the private login | mint ok name, A2 prefilled-by-page, L token private-file ok | A mint ok name=E2E7B SYNTHETIC FILER, A2 prefilled-by-page, L token private-file ok with the name claim equal to the synthetic name, 16:59:08Z to 16:59:11Z | CLOSED 20261020T171112Z |
| B | verify | browser leg B1 form read, B2 one filing, B3 Open report | B1 B2 B3 lines recorded | B1 advisor=required advisor_prefilled=yes labels=11 3 firms 5 models; B2 filed ok TCK-20261020-864bf125 REQ-c9ff59d956b590ce86fb1ccb at 16:59:41Z; B3 face=yes headings=1 (value=no is the script's fixed 12.5 marker; R2 value=13) | CLOSED 20261020T171112Z |
| P | verify | poll P1 to P5 and the P7 package reads | hops green or the first red named | P1 17:00:07Z, P2 and P3 17:01:11Z, P5 17:01:31Z, P4 outcome=ATTACHED 17:01:24Z; P7 PARTIAL at READY then COMPLETE 17:01:55Z with all four held | CLOSED 20261020T171113Z |
| R | verify | route read and sections read (R, R2) | route and sections lines | R REFUSED UNAVAILABLE,UNEXPECTED (irpt-status-role denied s3:GetObjectVersion on the retained PDF, row S231); R2 status 200 n_sections=100 value=13 builder_only_without_value=0 not_in_this_version=0 | CLOSED 20261020T171113Z |
| D | verify | delete only the recorded keys, each read back ABSENT, and the private token file | deleted n of m, token_file=absent | 14 of 21 distinct keys ABSENT (13 index rows and the user); 7 S3 state objects stay, AccessDenied (row S232); token file and folder ABSENT; first delete 17:02:13Z after last read 17:02:10Z | CLOSED 20261020T171113Z |

## Log

- 20261020T165831Z OPENED by 0.7.0_AE_CloudOps~IB2 with 5 leg(s)
- 20261020T171112Z LEG A closed: A mint ok name=E2E7B SYNTHETIC FILER, A2 prefilled-by-page, L token private-file ok with the name claim equal to the syn
- 20261020T171112Z LEG B closed: B1 advisor=required advisor_prefilled=yes labels=11 3 firms 5 models; B2 filed ok TCK-20261020-864bf125 REQ-c9ff59d956b5
- 20261020T171113Z LEG P closed: P1 17:00:07Z, P2 and P3 17:01:11Z, P5 17:01:31Z, P4 outcome=ATTACHED 17:01:24Z; P7 PARTIAL at READY then COMPLETE 17:01:
- 20261020T171113Z LEG R closed: R REFUSED UNAVAILABLE,UNEXPECTED (irpt-status-role denied s3:GetObjectVersion on the retained PDF, row S231); R2 status 
- 20261020T171113Z LEG D closed: 14 of 21 distinct keys ABSENT (13 index rows and the user); 7 S3 state objects stay, AccessDenied (row S232); token file
- 20261020T171113Z CLOSED -- all 5 legs proven
