# Deploy Completion Record
**Date opened:** 2026-10-20T21:55:47.142185+00:00
**Status:** CLOSED -- RUN-DONE PASS (the Overview PDF route and the commentary route both answered PDFs; the Overview saved outside the repository); seven synthetic state objects stay, AccessDenied, both retained PDFs among them (row IRPT_ANLREQ-D2-S237, residue_7d.json) -- closed 20261020T220346Z
**Deploy:** IRPT_ANLREQ TO-RUN-COMMENTARY-E2E-7D: staff filing through the PROD portal page after r37, the Overview PDF saved for Andrew outside the repository, the commentary route read
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A | verify | mint the synthetic staff user with a non-empty name and the private login | mint ok name, A2 prefilled-by-page, L token private-file ok | A mint ok name=E2E7D SYNTHETIC FILER, A2 prefilled-by-page, L token private-file ok (name claim equals the synthetic name), 21:56:27Z to 21:56:32Z | CLOSED 20261020T220345Z |
| B | verify | browser leg B1 form read, B2 one filing, B3 Open report | B1 B2 B3 lines recorded | B1 advisor=required advisor_prefilled=yes labels=11 3 firms 5 models; B2 filed ok TCK-20261020-7d5b0bf1 REQ-bb8793fa8c8e2c9da8bc033d at 21:57:05Z; B3 face=yes headings=1 (value=no is the script's fixed 12.5 marker; R2 value=13) | CLOSED 20261020T220345Z |
| P | verify | poll P1 to P5 and the P7 package reads | hops green or the first red named | P1 21:57:30Z, P2 P3 21:58:54Z, P5 21:59:14Z, P4 outcome=ATTACHED 21:59:09Z; P7 PARTIAL at READY then COMPLETE 21:59:18Z with all four held | CLOSED 20261020T220346Z |
| R | verify | Overview route, saved PDF, commentary route and sections read (R, R3, R4, R2) | route, R3, R4 and sections lines | R Overview route /pdf passed: PDF 231470 bytes, 39 pages, sha256 22a754c7965a, saved outside the repository (R3); R4 commentary route passed: PDF 45182 bytes, 2 pages, sha256 dece2cfc56b9; R2 status 200 n_sections=100 value=13 builder_only_without_value=0 not_in_this_version=0 | CLOSED 20261020T220346Z |
| D | verify | delete only the recorded keys, each read back ABSENT, residue listed with VersionIds, and the private token file | deleted n of m, token_file=absent | 14 of 21 distinct keys ABSENT (13 index rows and the user); 7 S3 state objects stay (both retained PDFs among them), AccessDenied, keys and VersionIds in residue_7d.json (row S237); token file and folder ABSENT; first delete 21:59:38Z after last read 21:59:35Z | CLOSED 20261020T220346Z |

## Log

- 20261020T215547Z OPENED by 0.7.0_AE_CloudOps~IB2 with 5 leg(s)
- 20261020T220345Z LEG A closed: A mint ok name=E2E7D SYNTHETIC FILER, A2 prefilled-by-page, L token private-file ok (name claim equals the synthetic nam
- 20261020T220345Z LEG B closed: B1 advisor=required advisor_prefilled=yes labels=11 3 firms 5 models; B2 filed ok TCK-20261020-7d5b0bf1 REQ-bb8793fa8c8e
- 20261020T220346Z LEG P closed: P1 21:57:30Z, P2 P3 21:58:54Z, P5 21:59:14Z, P4 outcome=ATTACHED 21:59:09Z; P7 PARTIAL at READY then COMPLETE 21:59:18Z 
- 20261020T220346Z LEG R closed: R Overview route /pdf passed: PDF 231470 bytes, 39 pages, sha256 22a754c7965a, saved outside the repository (R3); R4 com
- 20261020T220346Z LEG D closed: 14 of 21 distinct keys ABSENT (13 index rows and the user); 7 S3 state objects stay (both retained PDFs among them), Acc
- 20261020T220346Z CLOSED -- all 5 legs proven
