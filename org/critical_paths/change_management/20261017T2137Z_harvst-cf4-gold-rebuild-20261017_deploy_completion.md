# Deploy Completion Record
**Date opened:** 2026-10-17T21:37:18.233974+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261017T230010Z
**Deploy:** AMGT_HARVST HVST-cf-4: ADD-ONLY gold rebuild in s3 opal-data-harvest for the 17 names of cf4_securities.txt (sha256 221a63c3..): amgt/harvest/gold/research-continuation/security_key=<KEY>/<sha16>.json (method continuation/5) and amgt/harvest/gold/research_dossier/security_key=<KEY>/as_of=<as_of>.<sha16>.json, at most 34 new keys, from a worktree at 80d0701876 (no fund_form change); window 2026-10-17 22:00Z to 2026-10-18 00:00Z; canary MNST then 8306_JP read served first; each name a separate foreground command; manifest cf4_written.out; no S3 delete
**Authored by:** 0.7.0_AE_CloudOps~SC1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 5.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| S0 | verify | worktree at 80d0701876; cf4_securities.txt sha256 equals 221a63c3..; UNH and CPA BEFORE reads; UNH in-memory build; MNST and 8306_JP BEFORE reads and in-memory builds | cf4_before.out | PASS. cf4_before.out: worktree C:/tmp/cf4-build detached at 80d07018766e1a626bd69272709d4c91f79bbf54 (0 status lines, no fund_form change; main-tree lib/research diff vs the pin EMPTY); cf4_securities.txt sha256 221a63c311c9d0f13baeff2a346169b62f27cec7d32c33270ba1b2e1ac58ee48 = the signed value, 17 names; UNH BEFORE served PFOE/Maintain positions in PFOE and DIVZ line_only true and its in-memory build equal; CPA BEFORE IDVZ 2% (content_sha256 61b9977a..); MNST BEFORE served fund PFOE from CANDIDATE FOR PFOE; 8306_JP BEFORE served a COMPANY DESCRIPTION paragraph as the position; in-memory builds MNST (fund absent, stance candidate) and 8306_JP (position absent) BRANCH A against cf2_census; no write made | CLOSED 20261017T213958Z |
| C1 | activation | canary writes MNST then 8306_JP (continuation then dossier), both read SERVED | cf4_written.out + cf4_canary.out | PASS. Canary written (cf4_written.out): MNST continuation 67c9b3682876b2da.json 22:05:29Z and dossier as_of=2026-10-17.02138a6dbdba3eb7.json 22:08:09Z; 8306_JP continuation d09c9a0e6dae22a8.json 22:08:30Z and dossier as_of=2026-10-17.25047d7586727203.json 22:11:07Z; each put_performed True existed False, both keys of each name present before the next. Read SERVED 22:12Z (cf4_canary.out): MNST fund_of_record absent, position 'CANDIDATE FOR PFOE' stance candidate; 8306_JP last_stated_position absent. Each name a separate foreground command, branch A on continuation and dossier | CLOSED 20261017T221136Z |
| R1 | activation | the other 15 serially in file order, each a separate foreground command, manifest checked after each, each build equal to its cf2_census line | cf4_written.out + cf4_run.log | PASS. Rollback list is cf4_written.out: 34 WROTE lines, 34 distinct keys, each with VersionId, bytes, sha256. Add-only; removal is an S3 delete, Andrew's act, not taken | CLOSED 20261017T225944Z |
| V1 | verify | served reads: UNH and CPA equal to step 0, MNST, four JP names, first/middle/last of the rest; cf4_served.out ends SERVED_CANARY, SERVED_UNH_AND_CONTROL_UNCHANGED, WRITTEN continuation=17 dossier=17 | cf4_served.out | PASS. Post-run served reads (cf4_served.out): UNH and CPA equal to step-0 (content_sha256 6bd7cea7.. and 61b9977a..); MNST, 8306_JP, 8316_JP, 8766_JP, 9433_JP, 8035_JP, CELH, ST_SP fund_of_record absent, JP positions absent, candidate stance elsewhere; 34 of 34 census checks Branch A | CLOSED 20261017T225944Z |
| Z1 | git | proof instance VALID, manifest and ledger close committed, report to the issuer | checker last line + commit hash | PASS. WRITTEN continuation=17 dossier=17, all puts 22:05:29Z to 22:57:03Z inside the window; proof instance VALID (rc=0); committed with this ledger close | CLOSED 20261017T225944Z |

## Log

- 20261017T213718Z OPENED by 0.7.0_AE_CloudOps~SC1 with 5 leg(s)
- 20261017T213958Z LEG S0 closed: PASS. cf4_before.out: worktree C:/tmp/cf4-build detached at 80d07018766e1a626bd69272709d4c91f79bbf54 (0 status lines, no
- 20261017T221136Z LEG C1 closed: PASS. Canary written (cf4_written.out): MNST continuation 67c9b3682876b2da.json 22:05:29Z and dossier as_of=2026-10-17.0
- 20261017T225944Z LEG R1 closed: PASS. Rollback list is cf4_written.out: 34 WROTE lines, 34 distinct keys, each with VersionId, bytes, sha256. Add-only; 
- 20261017T225944Z LEG V1 closed: PASS. Post-run served reads (cf4_served.out): UNH and CPA equal to step-0 (content_sha256 6bd7cea7.. and 61b9977a..); MN
- 20261017T225944Z LEG Z1 closed: PASS. WRITTEN continuation=17 dossier=17, all puts 22:05:29Z to 22:57:03Z inside the window; proof instance VALID (rc=0)
- 20261017T230010Z CLOSED -- all 5 legs proven
