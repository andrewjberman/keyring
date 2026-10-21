# Deploy Completion Record
**Date opened:** 2026-10-20T23:34:52.803769+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261020T234450Z
**Deploy:** IRPT_ANLREQ TO-RUN-COMMENTARY-E2E-7E: one synthetic Overview filing through the PROD page on the r34o resident, the Overview PDF saved for Andrew outside the repository, the commentary route read
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A | verify | mint the synthetic staff user with a non-empty name and the private login | A mint ok name, A2 prefilled-by-page, L token private-file ok | A mint ok name=E2E7E SYNTHETIC FILER, A2 prefilled-by-page, L token private-file ok, 23:35:27Z to 23:35:31Z | CLOSED 20261020T234416Z |
| B | verify | browser leg B1 form read, B2 one filing, B3 Open report | B1 B2 B3 lines recorded | B1 advisor=required advisor_prefilled=yes labels=11 3 firms 5 models; B2 filed ok TCK-20261020-7a6d600b REQ-719a4d55ff1992f3724978d9 at 23:36:01Z; B3 NOT-RUN P4 (the run stopped before the report was opened) | CLOSED 20261020T234416Z |
| P | verify | poll P1 to P5 and the P7 package reads | hops green or the first red named | P1 P2 P3 green; P4 first red at 23:37:00Z: packager outcome=ATTACHED_WITHOUT_COMMENTARY 23:36:18Z then retained_for_retry class=RetentionRefused code=-; P5 and P7 final NOT-RUN; STOP at P4 code=RETAINED_FOR_RETRY (row IRPT_ANLREQ-D2-S239) | CLOSED 20261020T234416Z |
| R | verify | Overview route, saved PDF, commentary route and sections read (R, R3, R4, R2) | route, R3, R4 and sections lines | R R2 R3 R4 NOT-RUN P4: the run stopped at P4, no route read, no PDF saved for Andrew from this run | CLOSED 20261020T234416Z |
| D | verify | delete only the recorded keys, each read back ABSENT, residue listed with VersionIds, and the private token file | deleted n of m, token_file=absent | 13 of 19 distinct keys ABSENT (12 index rows and the user); 6 S3 state objects stay, AccessDenied, keys and VersionIds in residue_7e.json (row IRPT_ANLREQ-D2-S240); token_file=absent; first delete 23:37:14Z after last read 23:37:10Z | CLOSED 20261020T234416Z |

## Log

- 20261020T233452Z OPENED by 0.7.0_AE_CloudOps~IB2 with 5 leg(s)
- 20261020T234416Z LEG A closed: A mint ok name=E2E7E SYNTHETIC FILER, A2 prefilled-by-page, L token private-file ok, 23:35:27Z to 23:35:31Z
- 20261020T234416Z LEG B closed: B1 advisor=required advisor_prefilled=yes labels=11 3 firms 5 models; B2 filed ok TCK-20261020-7a6d600b REQ-719a4d55ff19
- 20261020T234416Z LEG P closed: P1 P2 P3 green; P4 first red at 23:37:00Z: packager outcome=ATTACHED_WITHOUT_COMMENTARY 23:36:18Z then retained_for_retr
- 20261020T234416Z LEG R closed: R R2 R3 R4 NOT-RUN P4: the run stopped at P4, no route read, no PDF saved for Andrew from this run
- 20261020T234416Z LEG D closed: 13 of 19 distinct keys ABSENT (12 index rows and the user); 6 S3 state objects stay, AccessDenied, keys and VersionIds i
- 20261020T234450Z CLOSED -- all 5 legs proven
