# Deploy Completion Record
**Date opened:** 2026-10-21T01:46:51.432256+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261021T015653Z
**Deploy:** IRPT_ANLREQ TO-RUN-FWD10-MULTICOMP-7G: one synthetic Multi-Comp filing (two Opal models) through the PROD page on the r34p resident, the PDF saved for the issuer outside the repository
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A | verify | mint the synthetic staff user with a non-empty name and the private login | A mint ok name, A2 prefilled-by-page, L token private-file ok | A mint ok name=E2E7G SYNTHETIC FILER, A2 prefilled-by-page, L token private-file ok (attempt 2, 01:48:58Z; attempt 1 at 01:47Z stopped at B1 on my parse error with nothing filed and its user deleted) | CLOSED 20261021T015653Z |
| B | verify | browser leg B1 form read, B2 one filing with two Opal models ticked, B3 Open report | B1 B2 B3 lines recorded | B1 form read (five Opal model labels incl. the two named); B2 comparables ticked=2 then ONE press: the page's holdings review REFUSED holdings_fwd10.csv at the upload step (Review required the file needs a correction), request variant=none comparison_keys=0, nothing filed, no ticket; STOP at B2 B2_REFUSED (row IRPT_ANLREQ-D2-S244); B3 NOT-RUN B2 | CLOSED 20261021T015653Z |
| P | verify | poll P1 to P5 and the P7 package reads | hops green or the first red named | P1 to P5 and P7 NOT-RUN B2: no request existed to poll | CLOSED 20261021T015653Z |
| R | verify | report PDF route, saved PDF, sections read (R, R3, R2) | route, R3 and sections lines | R R3 R2 NOT-RUN B2: no request, no PDF saved | CLOSED 20261021T015653Z |
| D | verify | delete only the recorded keys, each read back ABSENT, residue listed with VersionIds, and the private token file | deleted n of m, token_file=absent | 3 of 4 distinct keys ABSENT (upload row set and the synthetic user); 1 S3 state object stays, AccessDenied, key and VersionId in residue_7g.json (row IRPT_ANLREQ-D2-S244); token_file=absent; first delete 01:54:23Z after last read 01:49:22Z | CLOSED 20261021T015653Z |

## Log

- 20261021T014651Z OPENED by 0.7.0_AE_CloudOps~IB2 with 5 leg(s)
- 20261021T015653Z LEG A closed: A mint ok name=E2E7G SYNTHETIC FILER, A2 prefilled-by-page, L token private-file ok (attempt 2, 01:48:58Z; attempt 1 at 
- 20261021T015653Z LEG B closed: B1 form read (five Opal model labels incl. the two named); B2 comparables ticked=2 then ONE press: the page's holdings r
- 20261021T015653Z LEG P closed: P1 to P5 and P7 NOT-RUN B2: no request existed to poll
- 20261021T015653Z LEG R closed: R R3 R2 NOT-RUN B2: no request, no PDF saved
- 20261021T015653Z LEG D closed: 3 of 4 distinct keys ABSENT (upload row set and the synthetic user); 1 S3 state object stays, AccessDenied, key and Vers
- 20261021T015653Z CLOSED -- all 5 legs proven
