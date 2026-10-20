# Deploy Completion Record
**Date opened:** 2026-10-20T18:55:23.839994+00:00
**Status:** CLOSED -- STOPPED AT R (the commentary-pdf route refused INVALID_INPUT: COMMENTARY_PDF_BINDING in the irpt-status log, row S233; the 7b IAM denial is gone); B1, B2, P1 to P5, P7 COMPLETE, B3 and R2 read; no PDF saved; seven synthetic state objects stay, AccessDenied (row IRPT_ANLREQ-D2-S234, residue_7c.json) -- closed 20261020T190421Z
**Deploy:** IRPT_ANLREQ TO-RUN-COMMENTARY-E2E-7C: staff filing through the PROD portal page after the status grant, the route, the sections and the saved Opal report PDF
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A | verify | mint the synthetic staff user with a non-empty name and the private login | mint ok name, A2 prefilled-by-page, L token private-file ok | A mint ok name=E2E7C SYNTHETIC FILER, A2 prefilled-by-page, L token private-file ok (name claim equals the synthetic name), 18:56:07Z to 18:56:11Z | CLOSED 20261020T190420Z |
| B | verify | browser leg B1 form read, B2 one filing, B3 Open report | B1 B2 B3 lines recorded | B1 advisor=required advisor_prefilled=yes labels=11 3 firms 5 models; B2 filed ok TCK-20261020-85182d16 REQ-1eb7e112fd97eaebddf1a3f6 at 18:57:03Z; B3 face=yes headings=1 (value=no is the script's fixed 12.5 marker; R2 value=13) | CLOSED 20261020T190420Z |
| P | verify | poll P1 to P5 and the P7 package reads | hops green or the first red named | P1 18:57:28Z, P2 P3 P5 18:58:32Z, P4 outcome=ATTACHED 18:58:25Z; P7 PARTIAL at READY then COMPLETE 18:59:16Z with all four held | CLOSED 20261020T190420Z |
| R | verify | route read, sections read and the saved PDF (R, R2, R3) | route, sections and R3 lines | R REFUSED UNAVAILABLE,INVALID_INPUT (the 7b AccessDenied is gone; irpt-status log: RequestReadRefused COMMENTARY_PDF_BINDING, row S233); R2 status 200 n_sections=100 value=13 builder_only_without_value=0 not_in_this_version=0; R3 NOT-RUN R, no PDF saved | CLOSED 20261020T190420Z |
| D | verify | delete only the recorded keys, each read back ABSENT, residue listed with VersionIds, and the private token file | deleted n of m, token_file=absent | 14 of 21 distinct keys ABSENT (13 index rows and the user); 7 S3 state objects stay, AccessDenied, keys and VersionIds in residue_7c.json (row S234); token file and folder ABSENT; first delete 18:59:35Z after last read 18:59:31Z | CLOSED 20261020T190421Z |

## Log

- 20261020T185523Z OPENED by 0.7.0_AE_CloudOps~IB2 with 5 leg(s)
- 20261020T190420Z LEG A closed: A mint ok name=E2E7C SYNTHETIC FILER, A2 prefilled-by-page, L token private-file ok (name claim equals the synthetic nam
- 20261020T190420Z LEG B closed: B1 advisor=required advisor_prefilled=yes labels=11 3 firms 5 models; B2 filed ok TCK-20261020-85182d16 REQ-1eb7e112fd97
- 20261020T190420Z LEG P closed: P1 18:57:28Z, P2 P3 P5 18:58:32Z, P4 outcome=ATTACHED 18:58:25Z; P7 PARTIAL at READY then COMPLETE 18:59:16Z with all fo
- 20261020T190420Z LEG R closed: R REFUSED UNAVAILABLE,INVALID_INPUT (the 7b AccessDenied is gone; irpt-status log: RequestReadRefused COMMENTARY_PDF_BIN
- 20261020T190421Z LEG D closed: 14 of 21 distinct keys ABSENT (13 index rows and the user); 7 S3 state objects stay, AccessDenied, keys and VersionIds i
- 20261020T190421Z CLOSED -- all 5 legs proven
