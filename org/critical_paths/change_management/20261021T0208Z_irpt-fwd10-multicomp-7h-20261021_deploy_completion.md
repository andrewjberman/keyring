# Deploy Completion Record
**Date opened:** 2026-10-21T02:08:59.006234+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261021T024504Z
**Deploy:** IRPT_ANLREQ TO-RUN-FWD10-MULTICOMP-7H: one synthetic Multi-Comp filing (two Opal models) with the corrected holdings file through the PROD page on the r34p resident, the PDF saved for the issuer outside the repository
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A | verify | mint the synthetic staff user with a non-empty name and the private login | A mint ok name, A2 prefilled-by-page, L token private-file ok | A mint ok name=E2E7H SYNTHETIC FILER, A2 prefilled-by-page, L token private-file ok, 02:10:29Z to 02:10:34Z | CLOSED 20261021T024504Z |
| B | verify | browser leg B1 form read, B2 one filing with two Opal models ticked, B3 Open report | B1 B2 B3 lines recorded | B1 form read; B2 comparables ticked=2 variant=multicomp comparison_keys=2; filed ok TCK-20261021-c553ca50 REQ-e90c581652f6c90d3e33af23 at 02:11:10Z (the corrected holdings file sha256 1c20745eff0e accepted by the page); B3 NOT-RUN P1 | CLOSED 20261021T024504Z |
| P | verify | poll P1 to P5 and the P7 package reads | hops green or the first red named | P1 first red: job never READY in the 1800 s budget; resident COMPOSITION-REFUSED step=3 SubmissionRefused, retained_for_retry code=CLOSED_COMPOSITION_REQUIRED at 02:11:11Z, 02:26:11Z, 02:41:12Z; STOP at P1 NOT_READY_IN_BUDGET (row IRPT_ANLREQ-D2-S245) | CLOSED 20261021T024504Z |
| R | verify | report PDF route, saved PDF, sections read (R, R3, R2) | route, R3 and sections lines | R R3 R2 NOT-RUN P1: no request reached READY, no PDF saved | CLOSED 20261021T024504Z |
| D | verify | delete only the recorded keys, each read back ABSENT, residue listed with VersionIds, and the private token file | deleted n of m, token_file=absent | 10 of 13 distinct keys ABSENT (9 index rows and the user); 3 S3 state objects stay, AccessDenied, keys and VersionIds in residue_7h.json (row IRPT_ANLREQ-D2-S246); token_file=absent; first delete 02:41:21Z after last read 02:41:21Z; the irpt-generation message is left in flight, untouched | CLOSED 20261021T024504Z |

## Log

- 20261021T020859Z OPENED by 0.7.0_AE_CloudOps~IB2 with 5 leg(s)
- 20261021T024504Z LEG A closed: A mint ok name=E2E7H SYNTHETIC FILER, A2 prefilled-by-page, L token private-file ok, 02:10:29Z to 02:10:34Z
- 20261021T024504Z LEG B closed: B1 form read; B2 comparables ticked=2 variant=multicomp comparison_keys=2; filed ok TCK-20261021-c553ca50 REQ-e90c581652
- 20261021T024504Z LEG P closed: P1 first red: job never READY in the 1800 s budget; resident COMPOSITION-REFUSED step=3 SubmissionRefused, retained_for_
- 20261021T024504Z LEG R closed: R R3 R2 NOT-RUN P1: no request reached READY, no PDF saved
- 20261021T024504Z LEG D closed: 10 of 13 distinct keys ABSENT (9 index rows and the user); 3 S3 state objects stay, AccessDenied, keys and VersionIds in
- 20261021T024504Z CLOSED -- all 5 legs proven
