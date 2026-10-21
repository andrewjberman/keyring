# Deploy Completion Record
**Date opened:** 2026-10-21T01:46:51.432256+00:00
**Status:** OPEN
**Deploy:** IRPT_ANLREQ TO-RUN-FWD10-MULTICOMP-7G: one synthetic Multi-Comp filing (two Opal models) through the PROD page on the r34p resident, the PDF saved for the issuer outside the repository
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A | verify | mint the synthetic staff user with a non-empty name and the private login | A mint ok name, A2 prefilled-by-page, L token private-file ok |  | OPEN |
| B | verify | browser leg B1 form read, B2 one filing with two Opal models ticked, B3 Open report | B1 B2 B3 lines recorded |  | OPEN |
| P | verify | poll P1 to P5 and the P7 package reads | hops green or the first red named |  | OPEN |
| R | verify | report PDF route, saved PDF, sections read (R, R3, R2) | route, R3 and sections lines |  | OPEN |
| D | verify | delete only the recorded keys, each read back ABSENT, residue listed with VersionIds, and the private token file | deleted n of m, token_file=absent |  | OPEN |

## Log

- 20261021T014651Z OPENED by 0.7.0_AE_CloudOps~IB2 with 5 leg(s)
