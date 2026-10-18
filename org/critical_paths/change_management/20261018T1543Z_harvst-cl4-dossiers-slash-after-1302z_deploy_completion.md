# Deploy Completion Record
**Date opened:** 2026-10-18T15:43:51.575786+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261018T155839Z
**Deploy:** HVST-cl-4: 2 research_dossier objects (BP/_LN_Equity, NG/_LN_Equity) added again after the 13:02Z model blocks, add-only, encoded partitions; GO 15:23Z, start condition met 15:40Z (cl-2 ledger closed), window to 16:40Z (site Z cleared to 16:50Z); rollback = S3 delete of the 2 keys, not pre-approved
**Authored by:** 0.7.0_AE_CloudOps~SC1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 1.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| S0 | verify | before-state, pinned worktree, list hashes, counts, scheduled-task read, four-spelling gateway reads (read only) | cl4_before.out | PASS. cl4_before.out 15:49Z: worktree C:/tmp/cl4-build HEAD 4c7a60cabe with an empty lib/research diff; list sha256 1e857087.. and e81381b9.. (2 lines each); counts dossier 1556, continuation 446, BP partition 16, NG 15, raw spelling 0; 207 scheduled tasks read with the control, none builds a dossier/continuation/fund form and none runs in the window; plan-mode run: both names move model_rows only, guard PASS; four gateway before reads transcribed | CLOSED 20261018T155014Z |
| W1 | s3-prefix | amgt/harvest/gold/research_dossier/security_key=BP-SLASH-_LN_Equity/ | cl4_run_log.out: BP object written under the encoded partition, read back, +1 count, pick names it | PASS. cl4_run_log.out 15:51:21Z: BP/_LN_Equity written at amgt/harvest/gold/research_dossier/security_key=BP-SLASH-_LN_Equity/as_of=2026-10-18.b8aef145b89bc510.json (VersionId OGkQV40POrCtXe6zOClZVyrya7N5A1Vd, 265726 B), put_performed 1 existed 0, under the encoded partition and not under the raw spelling, moved=model_rows as listed, guard PASS, count 16->17, the gateway pick names the key, read-back equal | CLOSED 20261018T155144Z |
| W2 | s3-prefix | amgt/harvest/gold/research_dossier/security_key=NG-SLASH-_LN_Equity/ | cl4_run_log.out: NG object written under the encoded partition, read back, +1 count, pick names it | PASS. cl4_run_log.out 15:54:12Z: NG/_LN_Equity written at amgt/harvest/gold/research_dossier/security_key=NG-SLASH-_LN_Equity/as_of=2026-10-18.255bb27c74280fb6.json (VersionId anp6r4_4Ag5F5T.krxDa7lOQFtwgDfvB, 109733 B), put_performed 1 existed 0, encoded partition not the raw one, moved=model_rows as listed, guard PASS, count 15->16, the gateway pick names the key, read-back equal | CLOSED 20261018T155431Z |
| V1 | verify | canary and after reads through the gateway in all four spellings | cl4_canary.out and cl4_after.out | PASS. cl4_canary.out and cl4_after.out: the gateway reads of the four spellings after BP and after NG: only dossier_key, content_sha256, the dossier entry of source_keys, duplicates_dropped, denominator_note and model_rows move (BP by script, NG by reading), fund_form_ref and the rest equal; the new dossier_key for all four spellings; the pick names both manifest keys (2 of 2); dossier objects 1558, continuations 446, 0 under the raw spellings | CLOSED 20261018T155755Z |
| Z1 | verify | cl4_served.out, proof instance VALID, close committed with the manifest | cl4_served.out ends with the four lines | PASS. cl4_served.out ends DOSSIERS_WRITTEN_AND_READ_BACK=PASS, CANARY_GATEWAY_BOTH_SPELLINGS_MOVE_AS_NAMED=PASS, PICK_NAMES_MANIFEST_KEYS=PASS, COUNTS_AS_EXPECTED=PASS; proof instance AMGT_HARVST.TO-HVST-cl-4.2-slash-key-dossiers-are-rebuilt-add-only-after-the-1302z-model-blocks.proof_of_spec.json checker last line on the committed bytes at a98c3a7fad: VALID (rc=0). The ledger close is committed with the manifest cl4_written.out (2 lines, committed in a98c3a7fad). Plain: no continuation was written; no object under the raw spelling (0 and 0); the driver wrote only the two listed names, the table count moved +2 and the manifest holds 2 lines, but no per-partition census of the 75 non-slash names, KMB or the 17 other names was taken. NOT proven: the NG gateway comparison is by reading; the dossiers fall a day behind the daily 13:0xZ model block again (round-98 scheduled refresh). Rollback: an S3 delete of the two keys, not mine | CLOSED 20261018T155838Z |

## Log

- 20261018T154351Z OPENED by 0.7.0_AE_CloudOps~SC1 with 5 leg(s)
- 20261018T155014Z LEG S0 closed: PASS. cl4_before.out 15:49Z: worktree C:/tmp/cl4-build HEAD 4c7a60cabe with an empty lib/research diff; list sha256 1e85
- 20261018T155144Z LEG W1 closed: PASS. cl4_run_log.out 15:51:21Z: BP/_LN_Equity written at amgt/harvest/gold/research_dossier/security_key=BP-SLASH-_LN_E
- 20261018T155431Z LEG W2 closed: PASS. cl4_run_log.out 15:54:12Z: NG/_LN_Equity written at amgt/harvest/gold/research_dossier/security_key=NG-SLASH-_LN_E
- 20261018T155755Z LEG V1 closed: PASS. cl4_canary.out and cl4_after.out: the gateway reads of the four spellings after BP and after NG: only dossier_key,
- 20261018T155838Z LEG Z1 closed: PASS. cl4_served.out ends DOSSIERS_WRITTEN_AND_READ_BACK=PASS, CANARY_GATEWAY_BOTH_SPELLINGS_MOVE_AS_NAMED=PASS, PICK_NA
- 20261018T155839Z CLOSED -- all 5 legs proven
