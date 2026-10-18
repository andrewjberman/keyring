# Deploy Completion Record
**Date opened:** 2026-10-18T02:36:23.052220+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261018T032212Z
**Deploy:** AMGT_HARVST HVST-cf-5: ADD-ONLY gold write in s3 opal-data-harvest, prefix amgt/harvest/gold/research-fund-form/, two NEW fund-form objects of method_version 2: fund=pfoe (33 reports, canary) then fund=idvz (82 reports), written one per foreground command; window 2026-10-18 02:45Z-04:30Z (site Z cleared, msg 7847); manifest cf5_written.out; rollback = S3 delete of the 2 keys, Andrew's act; C-6 (no dossier/continuation write_one) stays in force for DIVZ builds after the close
**Authored by:** 0.7.0_AE_CloudOps~SC1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| S0 | verify | worktree at 04be089e13 (empty lib/research diff); in-memory builds PFOE 33 and IDVZ 82; stored v1 forms listed; scheduled-task read with control; substrate view of UNH and CPA before; gateway BEFORE reads | cf5_before.out | PASS (with one stated difference). cf5_before.out: worktree 04be089e13, empty lib/research diff; builds PFOE 33 and IDVZ 82 equal the census (115 / 232); stored v1 forms listed (9); scheduled-task read with control (207 tasks, control found, 0 fund_form tasks); CPA substrate before = stale v1 current False; UNH substrate before reads absent (continuation /3 picked), differing from the order's expectation and reported to the issuer 02:39Z; gateway BEFORE reads of UNH and CPA printed; no compare, no write, no etfs_compare_peers | CLOSED 20261018T024140Z |
| C1 | activation | canary PFOE (33 reports) written and read back equal=PASS | cf5_written.out + cf5_run.log | PASS. Canary PFOE written 02:45:48Z (cf5_written.out): fund=pfoe/57cee6de8b2cd85e.json 33 reports 2050641 B VersionId eTDIHeR0QURzZtiYNy2.YPzHJoe2qLFg put_performed True existed False; READBACK fund=PFOE reports=33 equal=PASS; issuer told 02:45:56Z; window 02:45Z-04:30Z (site Z CLEAR, msg 7847) | CLOSED 20261018T025539Z |
| R1 | activation | IDVZ (82 reports) written and read back equal=PASS, manifest WRITTEN forms=2 reports=115 | cf5_written.out + cf5_run.log | PASS. IDVZ written 02:46:39Z: fund=idvz/65a5baab3afd06f0.json 82 reports 379207 B VersionId r3IA6.bhHGZ87xQXR56xLZKXUHXXtWPN put_performed True existed False; READBACK fund=IDVZ reports=82 equal=PASS; manifest closes WRITTEN forms=2 reports=115; one foreground python -u command each, manifest read after each | CLOSED 20261018T025539Z |
| V1 | verify | read_latest IDVZ and PFOE return the new objects, DIVZ raises LookupError; substrate current True method_version 2 for UNH and CPA; in-memory dossier.build equals stored except fund_form_ref; gateway reads equal; cf5_served.out four result lines | cf5_served.out | PASS. cf5_served.out (02:47Z-03:20Z): read_latest IDVZ and PFOE return the new v2 objects, DIVZ raises LookupError (expected); substrate._pick_stored returns the new objects current True; CPA member new, current True, v2; UNH member absent before and after (printed, not graded, AMENDMENT 2); dossier preview: first reading FAIL kept as history, AMENDMENT 3 controlled comparison PASS (CPA arms A and B differ only in fund_form_ref, new names the v2 IDVZ object; UNH identical); gateway reads of UNH and CPA equal before and after; ends FORMS_WRITTEN_AND_READ_BACK=PASS, READ_LATEST_AND_SUBSTRATE_CURRENT=PASS, DOSSIER_PREVIEW_ONLY_FUND_FORM_REF_DIFFERS=PASS, GATEWAY_READS_UNCHANGED=PASS | CLOSED 20261018T032212Z |
| Z1 | git | proof instance VALID, manifest and ledger close committed, C-6 for DIVZ stated in the close, report to the issuer | checker last line + commit hash | PASS. proof instance VALID (rc=0) at the cf-5 commit b0e8b6ea60; manifest committed with it; ledger close committed next. C-6 STAYS IN FORCE FOR DIVZ BUILDS after this close (CTO half condition 2): DIVZ still resolves to the stale version-1 form fund=divz/e19a2eb0a66b84a2.json (read_latest DIVZ raises LookupError); no dossier or continuation write_one that reads DIVZ's form until the round-93 cell lands. Also named: a UNH dossier/continuation rebuild today would serve fund_of_record absent (continuation-pick finding). Push state LOCAL (ls-remote origin box/dell1 = 88aa5c5c0e; push is integrator-only) | CLOSED 20261018T032212Z |

## Log

- 20261018T023623Z OPENED by 0.7.0_AE_CloudOps~SC1 with 5 leg(s)
- 20261018T024140Z LEG S0 closed: PASS (with one stated difference). cf5_before.out: worktree 04be089e13, empty lib/research diff; builds PFOE 33 and IDVZ
- 20261018T025539Z LEG C1 closed: PASS. Canary PFOE written 02:45:48Z (cf5_written.out): fund=pfoe/57cee6de8b2cd85e.json 33 reports 2050641 B VersionId eT
- 20261018T025539Z LEG R1 closed: PASS. IDVZ written 02:46:39Z: fund=idvz/65a5baab3afd06f0.json 82 reports 379207 B VersionId r3IA6.bhHGZ87xQXR56xLZKXUHXX
- 20261018T032212Z LEG V1 closed: PASS. cf5_served.out (02:47Z-03:20Z): read_latest IDVZ and PFOE return the new v2 objects, DIVZ raises LookupError (expe
- 20261018T032212Z LEG Z1 closed: PASS. proof instance VALID (rc=0) at the cf-5 commit b0e8b6ea60; manifest committed with it; ledger close committed next
- 20261018T032212Z CLOSED -- all 5 legs proven
