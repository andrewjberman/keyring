# Deploy Completion Record
**Date opened:** 2026-10-21T14:41:41.181572+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261021T144947Z
**Deploy:** IRPT_ANLREQ TO-RUN-FWD10-MULTICOMP-7M: one synthetic Multi-Comp (two Opal models plus typed ETF VNQ) through the PROD page on the r34t resident, PDF saved for the issuer outside the repository
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A | verify | mint the synthetic staff user (name prefilled) and login | A mint ok, A2, L token ok | A mint ok name, A2 prefilled-by-page, L token private-file ok (14:43:28Z to 14:43:33Z) | CLOSED 20261021T144947Z |
| B | verify | browser leg B1 form read, B2 one filing with two Opal models ticked and VNQ typed, B3 Open report | B1 B2 B3 lines recorded | B1 form read; B2 comparables ticked=2 other_etfs=1 variant=multicomp comparison_keys=3; filed ok TCK-20261021-09410391 REQ-e3cb830253d6642241024e32 at 14:44:10Z; B3 face yes | CLOSED 20261021T144947Z |
| P | verify | poll P1 to P5 and the P7 package reads | hops green or the first red named | P1 14:44:35Z, P2 P3 P5 14:46:20Z, P4 outcome=ATTACHED 14:46:23Z; P7 COMPLETE with all four held | CLOSED 20261021T144947Z |
| R | verify | report PDF route, saved PDF, sections read, packager and audit outcomes | route, R3, sections and U lines | route /pdf 309963 bytes 60 pages sha256 db369fa6f8c5 saved outside repo; sections 9 VALUE with compare; packager ATTACHED audit AUDIT_WRITTEN | CLOSED 20261021T144947Z |
| D | verify | delete only the recorded keys, residue listed with VersionIds, the private token file | deleted n of m | 14 of 22 recorded keys ABSENT; 8 S3 objects (9 versions) AccessDenied listed in residue_7m.json, row IRPT_ANLREQ-D2-S257; token file absent | CLOSED 20261021T144947Z |

## Log

- 20261021T144141Z OPENED by 0.7.0_AE_CloudOps~IB2 with 5 leg(s)
- 20261021T144947Z LEG A closed: A mint ok name, A2 prefilled-by-page, L token private-file ok (14:43:28Z to 14:43:33Z)
- 20261021T144947Z LEG B closed: B1 form read; B2 comparables ticked=2 other_etfs=1 variant=multicomp comparison_keys=3; filed ok TCK-20261021-09410391 R
- 20261021T144947Z LEG P closed: P1 14:44:35Z, P2 P3 P5 14:46:20Z, P4 outcome=ATTACHED 14:46:23Z; P7 COMPLETE with all four held
- 20261021T144947Z LEG R closed: route /pdf 309963 bytes 60 pages sha256 db369fa6f8c5 saved outside repo; sections 9 VALUE with compare; packager ATTACHE
- 20261021T144947Z LEG D closed: 14 of 22 recorded keys ABSENT; 8 S3 objects (9 versions) AccessDenied listed in residue_7m.json, row IRPT_ANLREQ-D2-S257
- 20261021T144947Z CLOSED -- all 5 legs proven
