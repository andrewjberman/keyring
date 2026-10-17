# Deploy Completion Record
**Date opened:** 2026-10-17T17:17:23.433987+00:00
**Status:** OPEN
**Deploy:** AMGT_HARVST HVST-ce-4: ADD-ONLY gold rebuild in s3 opal-data-harvest for the 31 names of ce4_securities.txt (sha256 7881772d..): amgt/harvest/gold/research-continuation/security_key=<KEY>/<sha16>.json and amgt/harvest/gold/research_dossier/security_key=<KEY>/as_of=<as_of>.<sha16>.json, at most 62 new keys, from a worktree at 344ea6a5fc; window 2026-10-17 17:20Z to 19:30Z; canary UNH then KMB read served first; manifest ce4_written.out; no S3 delete
**Authored by:** 0.7.0_AE_CloudOps~SC1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| S0 | verify | worktree at 344ea6a5fc; ce4_securities.txt sha256 equals 7881772d..; CPA control and UNH/KMB BEFORE reads | ce4_before.out |  | OPEN |
| B1 | verify | canary in-memory builds (continuation.build, dossier build) for UNH and KMB, Mexico-id scans 0 and 0, UNH PFOE line_only true | ce4_before.out |  | OPEN |
| C1 | activation | canary writes UNH then KMB (continuation then dossier) and both read SERVED | ce4_written.out + ce4_canary.out |  | OPEN |
| R1 | activation | the other 29 serially in file order, each built value equal to the ce2_census line, every put in ce4_written.out | ce4_written.out |  | OPEN |
| V1 | verify | served reads: UNH, KMB, first/middle/last of the other 29, control CPA equal to the step-0 reading; ce4_served.out ends SERVED_CANARY, SERVED_SAMPLE_AND_CONTROL, WRITTEN continuation=31 dossier=31 | ce4_served.out |  | OPEN |
| Z1 | git | proof instance VALID, ledger close and the manifest committed, report to the issuer | checker last line + commit hash |  | OPEN |

## Log

- 20261017T171723Z OPENED by 0.7.0_AE_CloudOps~SC1 with 6 leg(s)
