# Deploy Completion Record
**Date opened:** 2026-10-21T07:04:38.528050+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261021T071043Z
**Deploy:** IRPT_ANLREQ TO-RUN-FWD10-MULTICOMP-7J: one synthetic Multi-Comp filing (two Opal models) through the PROD page on the r34r resident, the PDF saved for the issuer outside the repository, packager and audit outcomes by name
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A | verify | mint the synthetic staff user with a non-empty name and the private login | A mint ok name, A2 prefilled-by-page, L token private-file ok | A mint ok name=E2E7J SYNTHETIC FILER, A2 prefilled-by-page, L token private-file ok, 07:05:15Z to 07:05:19Z | CLOSED 20261021T071042Z |
| B | verify | browser leg B1 form read, B2 one filing with two Opal models ticked, B3 Open report | B1 B2 B3 lines recorded | B1 form read; B2 comparables ticked=2 variant=multicomp comparison_keys=2; filed ok TCK-20261021-652d164a REQ-b231bf75ffd6f31471aa4b25 at 07:05:54Z (holdings fwd10_holdings_7j.csv sha256 e06adcd797a0 accepted); B3 report face=yes headings=1 value=yes | CLOSED 20261021T071042Z |
| P | verify | poll P1 to P5 and the P7 package reads | hops green or the first red named | P1 07:06:19Z, P2 P3 07:07:23Z, P5 07:07:43Z, P4 outcome=ATTACHED 07:07:40Z; P7 PARTIAL at READY then COMPLETE 07:08:07Z with all four held | CLOSED 20261021T071042Z |
| R | verify | report PDF route, saved PDF, sections read, packager and audit outcomes (R, R3, R2, U) | route, R3, sections and U lines | R Multi-Comp report route /pdf passed: PDF 308075 bytes, 60 pages, sha256 46bc9043237a, saved outside the repository (R3); R2 sections 200, 9 VALUE, compare_sections yes; U packager=ATTACHED audit=AUDIT_WRITTEN (one audit key, two versions, by name only) | CLOSED 20261021T071042Z |
| D | verify | delete only the recorded keys, each read back ABSENT, residue listed with VersionIds, and the private token file | deleted n of m, token_file=absent | 14 of 21 distinct recorded keys ABSENT (13 index rows and the user); 7 recorded S3 state objects stay, plus the audit object the resident wrote (one key, two versions), AccessDenied, keys and VersionIds in residue_7j.json (row IRPT_ANLREQ-D2-S251); token_file=absent; first delete 07:08:30Z after last read 07:08:27Z | CLOSED 20261021T071043Z |

## Log

- 20261021T070438Z OPENED by 0.7.0_AE_CloudOps~IB2 with 5 leg(s)
- 20261021T071042Z LEG A closed: A mint ok name=E2E7J SYNTHETIC FILER, A2 prefilled-by-page, L token private-file ok, 07:05:15Z to 07:05:19Z
- 20261021T071042Z LEG B closed: B1 form read; B2 comparables ticked=2 variant=multicomp comparison_keys=2; filed ok TCK-20261021-652d164a REQ-b231bf75ff
- 20261021T071042Z LEG P closed: P1 07:06:19Z, P2 P3 07:07:23Z, P5 07:07:43Z, P4 outcome=ATTACHED 07:07:40Z; P7 PARTIAL at READY then COMPLETE 07:08:07Z 
- 20261021T071042Z LEG R closed: R Multi-Comp report route /pdf passed: PDF 308075 bytes, 60 pages, sha256 46bc9043237a, saved outside the repository (R3
- 20261021T071043Z LEG D closed: 14 of 21 distinct recorded keys ABSENT (13 index rows and the user); 7 recorded S3 state objects stay, plus the audit ob
- 20261021T071043Z CLOSED -- all 5 legs proven
