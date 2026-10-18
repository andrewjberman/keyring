# Deploy Completion Record
**Date opened:** 2026-10-18T07:31:41.749039+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261018T093051Z
**Deploy:** AMGT_HARVST HVST-cj-4: ADD-ONLY gold write in s3 opal-data-harvest, prefix amgt/harvest/gold/research_dossier/security_key=<KEY>/, 75 NEW dossier objects (method amgt-corpus-dossier/15; the 75 non-slash names of cj4_names.txt sha256 ebcec99e..); served values DO move (fund_form_ref, model_rows, as_of, dossier_key, content_sha256); window GO_UTC 2026-10-18T07:45:00Z to 10:15:00Z (site Z CLEAR, msg 7953); canary UNH then CPA through the gateway, then the other 73 in batches of at most 10; manifest cj4_written.out; rollback = S3 delete of the 75 keys, Andrew's act; no continuation written, no slash-key name, KMB not rebuilt
**Authored by:** 0.7.0_AE_CloudOps~SC1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| S0 | verify | worktree AT 8f329a10b9 (rev-parse printed, empty lib/research diff); both list sha256; counts; scheduled-task read with control; UNH and CPA gateway BEFORE reads | cj4_before.out | PASS. cj4_before.out: worktree AT 8f329a10b9 (rev-parse printed, lib/research diff empty, field_map blob 3b2829c3 = the census pin), COO half sha256 35e368f3.. equals the CTO half's binding, cj4_names.txt ebcec99e.. 75 lines, cj4_expected_moves.txt ba4cd92e.. 75 lines, dossier objects 1479, continuation objects 446, 207 scheduled tasks read with control and none names a build, UNH and CPA gateway before reads, how a row with a value is counted | CLOSED 20261018T093050Z |
| C1 | activation | canary UNH then CPA written and read back, each its own command; gateway reads move as cj4_expected_moves.txt says and in no other way | cj4_written.out + cj4_canary.out | PASS. Canary UNH 07:49:11Z (fund_form_ref) and CPA 07:54:00Z (fund_form_ref, model_rows), each its own command, read back equal and +1; guard PASS; gateway after-reads moved only as cj4_expected_moves.txt says plus the pointers named (CPA model_rows at S3 level: the gateway cap omits it in both reads) (cj4_canary.out). Window GO_UTC 2026-10-18T07:45:00Z, end 10:15:00Z then 12:15:00Z by AMENDMENT 3 (W1 msg 7970); site Z CLEAR (msgs 7953, 7969) | CLOSED 20261018T093050Z |
| R1 | activation | the other 73 names in sorted order, batches of at most 10, one manifest line flushed per name, running count between batches | cj4_written.out + cj4_run.log | PASS. The other 73 written 07:55Z to 09:26:25Z in foreground python -u commands (2,3,2,2,2,2 names, then the AMENDMENT 2 memo driver 3,5x11,2); the bx-5 interval 08:41:34Z to 08:56:41Z is noted in cj4_run.log; manifest cj4_written.out 75 WROTE lines 75 distinct names 0 failure lines; cj4_run.log 75 READBACK equal=PASS, 75 COUNT plus_one=PASS, 75 pick_names_written_key=PASS, 75 model-block guard PASS (0 FAIL), 0 STOP | CLOSED 20261018T093051Z |
| V1 | verify | dossier count start+75, continuation count 446 unchanged, pick_equals_manifest, manifest 75 lines, cj4_served.out four result lines | cj4_after.out + cj4_served.out | PASS. cj4_after.out: dossier objects 1554 = 1479 + 75; continuation objects 446 unchanged; manifest 75 lines, names equal the list; 75 of 75 VersionIds equal a head read; pick_equals_manifest=75 of 75; cj4_served.out ends DOSSIERS_WRITTEN_AND_READ_BACK=PASS, CANARY_GATEWAY_MOVES_AS_NAMED=PASS, PICK_NAMES_MANIFEST_KEYS=PASS, COUNTS_AS_EXPECTED=PASS | CLOSED 20261018T093051Z |
| Z1 | git | proof instance VALID, manifest and ledger close committed, report to the issuer | checker last line + commit hash | PASS. proof instance VALID (rc=0); deliverables and manifest committed at a50b7a5b09 (LOCAL only; origin box/dell1 = 50ebdf435a; push is integrator-only). No continuation was written; the two slash-key names, KMB and the 17 other unchanged names were not rebuilt. | CLOSED 20261018T093051Z |

## Log

- 20261018T073141Z OPENED by 0.7.0_AE_CloudOps~SC1 with 5 leg(s)
- 20261018T093050Z LEG S0 closed: PASS. cj4_before.out: worktree AT 8f329a10b9 (rev-parse printed, lib/research diff empty, field_map blob 3b2829c3 = the 
- 20261018T093050Z LEG C1 closed: PASS. Canary UNH 07:49:11Z (fund_form_ref) and CPA 07:54:00Z (fund_form_ref, model_rows), each its own command, read bac
- 20261018T093051Z LEG R1 closed: PASS. The other 73 written 07:55Z to 09:26:25Z in foreground python -u commands (2,3,2,2,2,2 names, then the AMENDMENT 2
- 20261018T093051Z LEG V1 closed: PASS. cj4_after.out: dossier objects 1554 = 1479 + 75; continuation objects 446 unchanged; manifest 75 lines, names equa
- 20261018T093051Z LEG Z1 closed: PASS. proof instance VALID (rc=0); deliverables and manifest committed at a50b7a5b09 (LOCAL only; origin box/dell1 = 50e
- 20261018T093051Z CLOSED -- all 5 legs proven
