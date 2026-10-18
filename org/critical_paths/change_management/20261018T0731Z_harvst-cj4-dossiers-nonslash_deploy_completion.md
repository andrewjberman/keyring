# Deploy Completion Record
**Date opened:** 2026-10-18T07:31:41.749039+00:00
**Status:** OPEN
**Deploy:** AMGT_HARVST HVST-cj-4: ADD-ONLY gold write in s3 opal-data-harvest, prefix amgt/harvest/gold/research_dossier/security_key=<KEY>/, 75 NEW dossier objects (method amgt-corpus-dossier/15; the 75 non-slash names of cj4_names.txt sha256 ebcec99e..); served values DO move (fund_form_ref, model_rows, as_of, dossier_key, content_sha256); window GO_UTC 2026-10-18T07:45:00Z to 10:15:00Z (site Z CLEAR, msg 7953); canary UNH then CPA through the gateway, then the other 73 in batches of at most 10; manifest cj4_written.out; rollback = S3 delete of the 75 keys, Andrew's act; no continuation written, no slash-key name, KMB not rebuilt
**Authored by:** 0.7.0_AE_CloudOps~SC1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| S0 | verify | worktree AT 8f329a10b9 (rev-parse printed, empty lib/research diff); both list sha256; counts; scheduled-task read with control; UNH and CPA gateway BEFORE reads | cj4_before.out |  | OPEN |
| C1 | activation | canary UNH then CPA written and read back, each its own command; gateway reads move as cj4_expected_moves.txt says and in no other way | cj4_written.out + cj4_canary.out |  | OPEN |
| R1 | activation | the other 73 names in sorted order, batches of at most 10, one manifest line flushed per name, running count between batches | cj4_written.out + cj4_run.log |  | OPEN |
| V1 | verify | dossier count start+75, continuation count 446 unchanged, pick_equals_manifest, manifest 75 lines, cj4_served.out four result lines | cj4_after.out + cj4_served.out |  | OPEN |
| Z1 | git | proof instance VALID, manifest and ledger close committed, report to the issuer | checker last line + commit hash |  | OPEN |

## Log

- 20261018T073141Z OPENED by 0.7.0_AE_CloudOps~SC1 with 5 leg(s)
