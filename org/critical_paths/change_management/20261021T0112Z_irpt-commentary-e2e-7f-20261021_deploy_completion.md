# Deploy Completion Record
**Date opened:** 2026-10-21T01:12:42.864056+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261021T011844Z
**Deploy:** IRPT_ANLREQ TO-RUN-COMMENTARY-E2E-7F: one synthetic Overview filing through the PROD page on the r34p resident, the Overview PDF saved for Andrew outside the repository, the commentary route read
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A | verify | mint the synthetic staff user with a non-empty name and the private login | A mint ok name, A2 prefilled-by-page, L token private-file ok | A mint ok name=E2E7F SYNTHETIC FILER, A2 prefilled-by-page, L token private-file ok, 01:13:17Z to 01:13:21Z | CLOSED 20261021T011843Z |
| B | verify | browser leg B1 form read, B2 one filing, B3 Open report | B1 B2 B3 lines recorded | B1 advisor=required advisor_prefilled=yes labels=11 3 firms 5 models; B2 filed ok TCK-20261021-bdecca98 REQ-6a4c277c240f901b864cbca7 at 01:13:53Z; B3 face=yes headings=1 value=yes | CLOSED 20261021T011843Z |
| P | verify | poll P1 to P5 and the P7 package reads | hops green or the first red named | P1 01:14:18Z, P2 P3 P5 01:15:22Z, P4 outcome=ATTACHED 01:15:16Z; P7 PARTIAL at READY then COMPLETE 01:16:06Z with all four held | CLOSED 20261021T011843Z |
| R | verify | Overview route, saved PDF, commentary route and sections read (R, R3, R4, R2) | route, R3, R4 and sections lines | R Overview route /pdf passed: PDF 262121 bytes, 42 pages, sha256 74d8b3e803c2, saved outside the repository (R3); R4 commentary route passed: PDF 39567 bytes, 2 pages, sha256 9026e1de3398; R2 status 200 n_sections 118 value 29 | CLOSED 20261021T011843Z |
| D | verify | delete only the recorded keys, each read back ABSENT, residue listed with VersionIds, and the private token file | deleted n of m, token_file=absent | 14 of 21 distinct keys ABSENT (13 index rows and the user); 7 S3 state objects stay (both retained PDFs among them), AccessDenied, keys and VersionIds in residue_7f.json (row IRPT_ANLREQ-D2-S241); token_file=absent | CLOSED 20261021T011844Z |

## Log

- 20261021T011242Z OPENED by 0.7.0_AE_CloudOps~IB2 with 5 leg(s)
- 20261021T011843Z LEG A closed: A mint ok name=E2E7F SYNTHETIC FILER, A2 prefilled-by-page, L token private-file ok, 01:13:17Z to 01:13:21Z
- 20261021T011843Z LEG B closed: B1 advisor=required advisor_prefilled=yes labels=11 3 firms 5 models; B2 filed ok TCK-20261021-bdecca98 REQ-6a4c277c240f
- 20261021T011843Z LEG P closed: P1 01:14:18Z, P2 P3 P5 01:15:22Z, P4 outcome=ATTACHED 01:15:16Z; P7 PARTIAL at READY then COMPLETE 01:16:06Z with all fo
- 20261021T011843Z LEG R closed: R Overview route /pdf passed: PDF 262121 bytes, 42 pages, sha256 74d8b3e803c2, saved outside the repository (R3); R4 com
- 20261021T011844Z LEG D closed: 14 of 21 distinct keys ABSENT (13 index rows and the user); 7 S3 state objects stay (both retained PDFs among them), Acc
- 20261021T011844Z CLOSED -- all 5 legs proven
