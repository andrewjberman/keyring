# Deploy Completion Record
**Date opened:** 2026-10-20T18:55:23.839994+00:00
**Status:** OPEN
**Deploy:** IRPT_ANLREQ TO-RUN-COMMENTARY-E2E-7C: staff filing through the PROD portal page after the status grant, the route, the sections and the saved Opal report PDF
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A | verify | mint the synthetic staff user with a non-empty name and the private login | mint ok name, A2 prefilled-by-page, L token private-file ok |  | OPEN |
| B | verify | browser leg B1 form read, B2 one filing, B3 Open report | B1 B2 B3 lines recorded |  | OPEN |
| P | verify | poll P1 to P5 and the P7 package reads | hops green or the first red named |  | OPEN |
| R | verify | route read, sections read and the saved PDF (R, R2, R3) | route, sections and R3 lines |  | OPEN |
| D | verify | delete only the recorded keys, each read back ABSENT, residue listed with VersionIds, and the private token file | deleted n of m, token_file=absent |  | OPEN |

## Log

- 20261020T185523Z OPENED by 0.7.0_AE_CloudOps~IB2 with 5 leg(s)
