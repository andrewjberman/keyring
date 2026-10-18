# Deploy Completion Record
**Date opened:** 2026-10-18T11:23:35.832612+00:00
**Status:** OPEN
**Deploy:** AMGT_HARVST HVST-cj-5: 2 research_dossier objects ADDED (BP/_LN_Equity then NG/_LN_Equity) under the ENCODED partitions security_key=BP-SLASH-_LN_Equity/ and NG-SLASH-_LN_Equity/ via dossier.write_one at 8f329a10b9; GO_UTC 11:15:00Z, window to 12:15:00Z; moves fund_form_ref (BP) and model_rows (both) only; no continuation written; rollback = S3 delete of the 2 keys (Andrew's act)
**Authored by:** 0.7.0_AE_CloudOps~SC1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 1.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| S0 | verify | before-state: worktree at 8f329a10b9 with empty lib/research diff; list sha256 and counts; dossier count 1554 and continuation 446; scheduled-task read with control; BEFORE gateway reads of the four spellings | cj5_before.out |  | OPEN |
| W1 | s3-prefix | BP canary: pre-write comparison and CTO model-block guard, dossier.write_one, key under security_key=BP-SLASH-_LN_Equity/, read-back, +1 count, manifest line; four-spelling canary reads | cj5_run.log + cj5_canary.out |  | OPEN |
| W2 | s3-prefix | NG/_LN_Equity: same guards and checks; both NG spellings read against their before reads | cj5_run.log + cj5_ng.out |  | OPEN |
| A1 | verify | after: dossier count = start + 2, continuation unchanged, gateway pick over a fresh listing of each encoded partition names the manifest key, manifest 2 lines | cj5_after.out |  | OPEN |
| Z1 | git | cj5_served.out four lines; proof instance VALID; deliverables committed; ledger close committed with the manifest; issuer told | checker last line + commit hashes |  | OPEN |

## Log

- 20261018T112335Z OPENED by 0.7.0_AE_CloudOps~SC1 with 5 leg(s)
