# Deploy Completion Record
**Date opened:** 2026-10-21T04:13:38.054451+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261021T044943Z
**Deploy:** IRPT_ANLREQ TO-RUN-FWD10-MULTICOMP-7I: one synthetic Multi-Comp filing (two Opal models) through the PROD page on the r34q resident, the PDF saved for the issuer outside the repository, packager and audit outcomes by name
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A | verify | mint the synthetic staff user with a non-empty name and the private login | A mint ok name, A2 prefilled-by-page, L token private-file ok | A mint ok name=E2E7I SYNTHETIC FILER, A2 prefilled-by-page, L token private-file ok, 04:15:34Z to 04:15:39Z | CLOSED 20261021T044942Z |
| B | verify | browser leg B1 form read, B2 one filing with two Opal models ticked, B3 Open report | B1 B2 B3 lines recorded | B1 form read; B2 comparables ticked=2 variant=multicomp comparison_keys=2; filed ok TCK-20261021-26db6ce5 REQ-0240fbdbf8c59e703e9fa3f0 at 04:16:14Z (holdings fwd10_holdings_7i.csv sha256 3125b93613e2 accepted); B3 NOT-RUN P1 | CLOSED 20261021T044942Z |
| P | verify | poll P1 to P5 and the P7 package reads | hops green or the first red named | P1 first red: job never READY in the 1800 s budget; resident retained_for_retry class=RecipeRefused code=- at 04:16:15Z, 04:31:15Z, 04:46:16Z (no COMPOSITION-REFUSED: the r34q admission fix held); STOP at P1 NOT_READY_IN_BUDGET (row IRPT_ANLREQ-D2-S249) | CLOSED 20261021T044942Z |
| R | verify | report PDF route, saved PDF, sections read, packager and audit outcomes (R, R3, R2, U) | route, R3, sections and U lines | R R3 R2 NOT-RUN P1: no request reached READY, no PDF saved; U packager=NONE_LOGGED audit=AUDIT_NO_MARKER_FOUND (neither ran) | CLOSED 20261021T044943Z |
| D | verify | delete only the recorded keys, each read back ABSENT, residue listed with VersionIds, and the private token file | deleted n of m, token_file=absent | 10 of 13 distinct keys ABSENT (9 index rows and the user); 3 S3 state objects stay, AccessDenied, keys and VersionIds in residue_7i.json (row IRPT_ANLREQ-D2-S250); token_file=absent; first delete 04:46:35Z after last read 04:46:35Z; the irpt-generation message is left in flight, untouched | CLOSED 20261021T044943Z |

## Log

- 20261021T041338Z OPENED by 0.7.0_AE_CloudOps~IB2 with 5 leg(s)
- 20261021T044942Z LEG A closed: A mint ok name=E2E7I SYNTHETIC FILER, A2 prefilled-by-page, L token private-file ok, 04:15:34Z to 04:15:39Z
- 20261021T044942Z LEG B closed: B1 form read; B2 comparables ticked=2 variant=multicomp comparison_keys=2; filed ok TCK-20261021-26db6ce5 REQ-0240fbdbf8
- 20261021T044942Z LEG P closed: P1 first red: job never READY in the 1800 s budget; resident retained_for_retry class=RecipeRefused code=- at 04:16:15Z,
- 20261021T044943Z LEG R closed: R R3 R2 NOT-RUN P1: no request reached READY, no PDF saved; U packager=NONE_LOGGED audit=AUDIT_NO_MARKER_FOUND (neither 
- 20261021T044943Z LEG D closed: 10 of 13 distinct keys ABSENT (9 index rows and the user); 3 S3 state objects stay, AccessDenied, keys and VersionIds in
- 20261021T044943Z CLOSED -- all 5 legs proven
