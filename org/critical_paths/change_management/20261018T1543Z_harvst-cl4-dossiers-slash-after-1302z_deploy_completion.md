# Deploy Completion Record
**Date opened:** 2026-10-18T15:43:51.575786+00:00
**Status:** OPEN
**Deploy:** HVST-cl-4: 2 research_dossier objects (BP/_LN_Equity, NG/_LN_Equity) added again after the 13:02Z model blocks, add-only, encoded partitions; GO 15:23Z, start condition met 15:40Z (cl-2 ledger closed), window to 16:40Z (site Z cleared to 16:50Z); rollback = S3 delete of the 2 keys, not pre-approved
**Authored by:** 0.7.0_AE_CloudOps~SC1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 1.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| S0 | verify | before-state, pinned worktree, list hashes, counts, scheduled-task read, four-spelling gateway reads (read only) | cl4_before.out |  | OPEN |
| W1 | s3-prefix | amgt/harvest/gold/research_dossier/security_key=BP-SLASH-_LN_Equity/ | cl4_run_log.out: BP object written under the encoded partition, read back, +1 count, pick names it |  | OPEN |
| W2 | s3-prefix | amgt/harvest/gold/research_dossier/security_key=NG-SLASH-_LN_Equity/ | cl4_run_log.out: NG object written under the encoded partition, read back, +1 count, pick names it |  | OPEN |
| V1 | verify | canary and after reads through the gateway in all four spellings | cl4_canary.out and cl4_after.out |  | OPEN |
| Z1 | verify | cl4_served.out, proof instance VALID, close committed with the manifest | cl4_served.out ends with the four lines |  | OPEN |

## Log

- 20261018T154351Z OPENED by 0.7.0_AE_CloudOps~SC1 with 5 leg(s)
