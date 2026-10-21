# Deploy Completion Record
**Date opened:** 2026-10-21T09:06:31.630704+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261021T091342Z
**Deploy:** IRPT_ANLREQ TO-RUN-FWD10-MULTICOMP-7K: one synthetic Multi-Comp filing (two Opal models) through the PROD page on the r34s resident, the PDF saved for the issuer outside the repository, packager and audit outcomes by name
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A | verify | mint the synthetic staff user with a non-empty name and the private login | A mint ok name, A2 prefilled-by-page, L token private-file ok | A mint ok name=E2E7K SYNTHETIC FILER, A2 prefilled-by-page, L token private-file ok, 09:07:11Z to 09:07:15Z | CLOSED 20261021T091341Z |
| B | verify | browser leg B1 form read, B2 one filing with two Opal models ticked, B3 Open report | B1 B2 B3 lines recorded | B1 form read; B2 comparables ticked=2 variant=multicomp comparison_keys=2; filed ok TCK-20261021-097772c3 REQ-eef2992f2e0d5788e874a1da at 09:07:49Z (holdings fwd10_holdings_7k.csv sha256 a0edb28fd0ee accepted); B3 report face=yes headings=1 value=yes | CLOSED 20261021T091341Z |
| P | verify | poll P1 to P5 and the P7 package reads | hops green or the first red named | P1 09:08:15Z, P2 P3 P5 09:09:39Z, P4 outcome=ATTACHED 09:09:35Z; P7 PARTIAL at READY then COMPLETE 09:10:02Z with all four held | CLOSED 20261021T091342Z |
| R | verify | report PDF route, saved PDF, sections read, packager and audit outcomes (R, R3, R2, U) | route, R3, sections and U lines | R Multi-Comp report route /pdf passed: PDF 306057 bytes, 60 pages, sha256 2fc0ad5f8726, saved outside the repository (R3); R2 sections 200, 9 VALUE, compare_sections yes; U packager=ATTACHED audit=AUDIT_WRITTEN (one audit key, two versions, by name only) | CLOSED 20261021T091342Z |
| D | verify | delete only the recorded keys, each read back ABSENT, residue listed with VersionIds, and the private token file | deleted n of m, token_file=absent | 14 of 21 distinct recorded keys ABSENT (13 index rows and the user); 7 recorded S3 state objects stay, plus the audit object the resident wrote (one key, two versions), AccessDenied, keys and VersionIds in residue_7k.json (row IRPT_ANLREQ-D2-S254); token_file=absent; first delete 09:10:27Z after last read 09:10:24Z | CLOSED 20261021T091342Z |

## Log

- 20261021T090631Z OPENED by 0.7.0_AE_CloudOps~IB2 with 5 leg(s)
- 20261021T091341Z LEG A closed: A mint ok name=E2E7K SYNTHETIC FILER, A2 prefilled-by-page, L token private-file ok, 09:07:11Z to 09:07:15Z
- 20261021T091341Z LEG B closed: B1 form read; B2 comparables ticked=2 variant=multicomp comparison_keys=2; filed ok TCK-20261021-097772c3 REQ-eef2992f2e
- 20261021T091342Z LEG P closed: P1 09:08:15Z, P2 P3 P5 09:09:39Z, P4 outcome=ATTACHED 09:09:35Z; P7 PARTIAL at READY then COMPLETE 09:10:02Z with all fo
- 20261021T091342Z LEG R closed: R Multi-Comp report route /pdf passed: PDF 306057 bytes, 60 pages, sha256 2fc0ad5f8726, saved outside the repository (R3
- 20261021T091342Z LEG D closed: 14 of 21 distinct recorded keys ABSENT (13 index rows and the user); 7 recorded S3 state objects stay, plus the audit ob
- 20261021T091342Z CLOSED -- all 5 legs proven
