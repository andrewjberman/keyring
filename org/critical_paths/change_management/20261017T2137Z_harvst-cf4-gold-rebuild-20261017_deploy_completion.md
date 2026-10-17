# Deploy Completion Record
**Date opened:** 2026-10-17T21:37:18.233974+00:00
**Status:** OPEN
**Deploy:** AMGT_HARVST HVST-cf-4: ADD-ONLY gold rebuild in s3 opal-data-harvest for the 17 names of cf4_securities.txt (sha256 221a63c3..): amgt/harvest/gold/research-continuation/security_key=<KEY>/<sha16>.json (method continuation/5) and amgt/harvest/gold/research_dossier/security_key=<KEY>/as_of=<as_of>.<sha16>.json, at most 34 new keys, from a worktree at 80d0701876 (no fund_form change); window 2026-10-17 22:00Z to 2026-10-18 00:00Z; canary MNST then 8306_JP read served first; each name a separate foreground command; manifest cf4_written.out; no S3 delete
**Authored by:** 0.7.0_AE_CloudOps~SC1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 5.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| S0 | verify | worktree at 80d0701876; cf4_securities.txt sha256 equals 221a63c3..; UNH and CPA BEFORE reads; UNH in-memory build; MNST and 8306_JP BEFORE reads and in-memory builds | cf4_before.out |  | OPEN |
| C1 | activation | canary writes MNST then 8306_JP (continuation then dossier), both read SERVED | cf4_written.out + cf4_canary.out |  | OPEN |
| R1 | activation | the other 15 serially in file order, each a separate foreground command, manifest checked after each, each build equal to its cf2_census line | cf4_written.out + cf4_run.log |  | OPEN |
| V1 | verify | served reads: UNH and CPA equal to step 0, MNST, four JP names, first/middle/last of the rest; cf4_served.out ends SERVED_CANARY, SERVED_UNH_AND_CONTROL_UNCHANGED, WRITTEN continuation=17 dossier=17 | cf4_served.out |  | OPEN |
| Z1 | git | proof instance VALID, manifest and ledger close committed, report to the issuer | checker last line + commit hash |  | OPEN |

## Log

- 20261017T213718Z OPENED by 0.7.0_AE_CloudOps~SC1 with 5 leg(s)
