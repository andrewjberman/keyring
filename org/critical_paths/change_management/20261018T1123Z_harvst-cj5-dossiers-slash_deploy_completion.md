# Deploy Completion Record
**Date opened:** 2026-10-18T11:23:35.832612+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261018T114046Z
**Deploy:** AMGT_HARVST HVST-cj-5: 2 research_dossier objects ADDED (BP/_LN_Equity then NG/_LN_Equity) under the ENCODED partitions security_key=BP-SLASH-_LN_Equity/ and NG-SLASH-_LN_Equity/ via dossier.write_one at 8f329a10b9; GO_UTC 11:15:00Z, window to 12:15:00Z; moves fund_form_ref (BP) and model_rows (both) only; no continuation written; rollback = S3 delete of the 2 keys (Andrew's act)
**Authored by:** 0.7.0_AE_CloudOps~SC1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 1.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| S0 | verify | before-state: worktree at 8f329a10b9 with empty lib/research diff; list sha256 and counts; dossier count 1554 and continuation 446; scheduled-task read with control; BEFORE gateway reads of the four spellings | cj5_before.out | PASS. cj5_before.out: pair verified (COO half sha256 1e2728c9.. = the CTO half's binding; CTO half signed 93f7352b2e), worktree C:/tmp/cj5-build HEAD 8f329a10b9 with a 0-byte lib/research diff and 0 status lines; list sha256 1e857087.. and 726cbde1.. (2 lines each); counts dossier 1554 and continuation 446; encoded partitions 15 (BP) and 14 (NG) objects, 0 under the raw spelling; scheduled tasks 207 read, control found, 0 name dossier/continuation/fund_form/corpus; BEFORE gateway reads of the four spellings recorded; plan mode: BP moved fund_form_ref,model_rows and NG model_rows (= list), guards PASS | CLOSED 20261018T113713Z |
| W1 | s3-prefix | BP canary: pre-write comparison and CTO model-block guard, dossier.write_one, key under security_key=BP-SLASH-_LN_Equity/, read-back, +1 count, manifest line; four-spelling canary reads | cj5_run.log + cj5_canary.out | PASS. BP/_LN_Equity written 2026-10-18T11:30:25Z (GO_UTC 11:15:00Z): key .../security_key=BP-SLASH-_LN_Equity/as_of=2026-10-18.2d0238f7570cff0e.json VersionId vzO7hgbtnhFAw4NLfXC.cLwZiiR6vSa0 265712 B put_performed 1 existed 0, under the encoded partition, none under raw; guard PASS (91 valued rows both, stamp later); read-back PASS; partition 15 to 16; pick names the key. Canary cj5_canary.out: BP raw and encoded gateway reads identical, new dossier_key in both, only the named values moved | CLOSED 20261018T113713Z |
| W2 | s3-prefix | NG/_LN_Equity: same guards and checks; both NG spellings read against their before reads | cj5_run.log + cj5_ng.out | PASS. NG/_LN_Equity written 11:34:16Z: key .../security_key=NG-SLASH-_LN_Equity/as_of=2026-10-18.1af6506669c49a8a.json VersionId ohYYtWyEDpyXppB1TlgcPxNnC8xl6wBC 109719 B put_performed 1 existed 0, encoded partition; guard PASS (64 valued rows both); read-back PASS; partition 14 to 15; pick names the key; both NG spellings return the new dossier_key, only model_rows and the pointers moved (compared by reading, stated in cj5_canary.out) | CLOSED 20261018T113713Z |
| A1 | verify | after: dossier count = start + 2, continuation unchanged, gateway pick over a fresh listing of each encoded partition names the manifest key, manifest 2 lines | cj5_after.out | PASS. cj5_after.out 11:34:58Z: dossier objects 1556 (1554+2), continuation 446 unchanged, manifest 2 lines, pick_equals_manifest=2 of 2, objects under the raw spelling 0 and 0; cj5_served.out ends DOSSIERS_WRITTEN_AND_READ_BACK=PASS, CANARY_GATEWAY_BOTH_SPELLINGS_MOVE_AS_NAMED=PASS, PICK_NAMES_MANIFEST_KEYS=PASS, COUNTS_AS_EXPECTED=PASS | CLOSED 20261018T113713Z |
| Z1 | git | cj5_served.out four lines; proof instance VALID; deliverables committed; ledger close committed with the manifest; issuer told | checker last line + commit hashes | PASS. cj5_served.out written with the four PASS lines; proof instance named exactly AMGT_HARVST.TO-HVST-cj-5.2-slash-key-dossiers-are-rebuilt-add-only.proof_of_spec.json, checker last line on the committed bytes at f7576dfed8: VALID (rc=0). HISTORY, plainly: the instance was INVALID (rc=1) when first read at c9facabbb6 and again at f6edb920b5, because its doc rows were pinned PENDING-THIS-COMMIT although cj5_served.out was carried earlier by 4aa32e3e71 and cj5_before.out, cj5_written.out and cj5_canary.out by c9facabbb6 (CCX class); only those rows' commit_or_etag moved, no criterion, evidence or grade moved; deliverables committed at 4aa32e3e71 (cj5_served.out) and c9facabbb6 (the rest; LOCAL, origin box/dell1 4aa32e3e71, push is integrator-only); the issuer told at the BP canary (11:32:57Z) and told of cj5_served.out below | CLOSED 20261018T114046Z |

## Log

- 20261018T112335Z OPENED by 0.7.0_AE_CloudOps~SC1 with 5 leg(s)
- 20261018T113713Z LEG S0 closed: PASS. cj5_before.out: pair verified (COO half sha256 1e2728c9.. = the CTO half's binding; CTO half signed 93f7352b2e), w
- 20261018T113713Z LEG W1 closed: PASS. BP/_LN_Equity written 2026-10-18T11:30:25Z (GO_UTC 11:15:00Z): key .../security_key=BP-SLASH-_LN_Equity/as_of=2026
- 20261018T113713Z LEG W2 closed: PASS. NG/_LN_Equity written 11:34:16Z: key .../security_key=NG-SLASH-_LN_Equity/as_of=2026-10-18.1af6506669c49a8a.json V
- 20261018T113713Z LEG A1 closed: PASS. cj5_after.out 11:34:58Z: dossier objects 1556 (1554+2), continuation 446 unchanged, manifest 2 lines, pick_equals_
- 20261018T114046Z LEG Z1 closed: PASS. cj5_served.out written with the four PASS lines; proof instance named exactly AMGT_HARVST.TO-HVST-cj-5.2-slash-key
- 20261018T114046Z CLOSED -- all 5 legs proven
