# Deploy Completion Record
**Date opened:** 2026-10-02T21:21:55.578005+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261002T233705Z
**Deploy:** st14 (row S279): the resident and irpt-ycharts-generate at f89fc8e731 -- a fund ticker no longer fails the whole upload
**Authored by:** 2.0.0_SA_COO~Y
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 12.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U1 | s3-prefix | irpt-ycharts-generate.zip new version at f89fc8e731 | read back by version, sha equal; census vs live E+FqSWwE | irpt-ycharts-generate.zip version y3LRNAoPvGmdWYZSNb5moyTiEDvo8055 (21:23:07Z, 582443 bytes) read back sha256 wjSX3zZoFu2EUintXwZVESW+ac8F+bdRHSWm+YfpmgA= equal; 113 members, staged rows all at f89fc8e731; census vs live E+FqSWwE: identical 99, eol_only 14, changed 13, added 1 (report_owner.py), removed 0 (ST14/census_irpt-ycharts-generate_st14.json); cold-start smoke PASS on 3 routes (ST14/ZIP_COLD_START_SMOKE_ST14_20261002.txt) | CLOSED 20261002T213059Z |
| U2 | s3-prefix | irpt-resident-f89fc8e731-st14.tar.gz and its install script | both keys 404 before, read back by version, sha equal | both keys 404 before; tar irpt-resident-f89fc8e731-st14.tar.gz version 4N3RhbITXo1u1zIsLkPbc0oYYWNCUVYE, 777996 bytes, sha256 4d317c00..; install script version 9GcYA4bLxx_gIvS_Vq4fYf0YX8mL.fVg, 8687 bytes, sha256 430d4172..; both read back by version equal; gate G1-G5 PASS (ST14/GATE_OUTPUT_ST14_20261002.txt) | CLOSED 20261002T213215Z |
| D1 | tf-lambda | ONE targeted safe-apply of module.irpt_ycharts_generate.aws_lambda_function.this | CodeSha256 read back equal to the built zip | safe-apply ~22:18Z of targeted plan ST14/plan_d1_st14.txt (1 change, code only): Modifications complete, Apply complete 0/1/0 (ST14/apply_d1_st14.txt); read back 22:19:30Z CodeSha256 wjSX3zZoFu2EUintXwZVESW+ac8F+bdRHSWm+YfpmgA=, 512 MB, 900 s, Successful; cold-start smoke PASS against the live configuration (ST14/D1_READBACK_20261002.txt). Same window as D2 (22:13Z). | CLOSED 20261002T222015Z |
| D2 | activation | resident install via SSM (root f89fc8e731-st14) | running root, member digests, unit active, queue 0/0 | 22:13Z via SSM (head-object printed 9GcYA4bL..; host fetched by key, sha256 430d4172.. verified; install rc=0): running root /opt/irpt-resident/f89fc8e731-st14; st14 digests equal the pin's blobs (security_resolution 7cee9b46b2958b08, portfolio 1500e601bf5ab62e, normalized_input b760f67e60f40e8f, resident_worker e3262b87b124eff2, IRPT_RESIDENT_RESOLVE_FUNDS present); st11/st12/st13 digests unchanged; host library 857d90b8.. unchanged; unit active since 22:13:00Z and polling; queue 0/0; nothing on 5901 (ST14/INSTALL_OUTPUT_ST14_20261002.txt) | CLOSED 20261002T221441Z |
| V1 | verify | Y-1 Case A first lookup on st14, spaced, solo gate | IRPT_RESIDENT_RESOLVE_FUNDS matched>=1, NORMALIZED with M:TIMXX; no WAF challenge | CLOSED per CTO rulings batch 192 (msg 104456): Case A run 3 from the page (23:24:44Z, UP-f0d8aead..): resident IRPT_RESIDENT_RESOLVE_FUNDS matched=1 refused=0 on ONE securities_info read, no WAF challenge, RESOLVE READY in ~2 s; 98 of 99 rows accepted; the one unusable row NAMED (row 100 TIMXX, TICKER_CHECK_UNAVAILABLE). S279 FIXED (S283 disarms). The packet's NORMALIZED-with-M:TIMXX criterion moved to Y-5 (TIMXX entitlement-gated, INFERRED, row S284). ST14/V1_CASE_A_RUN3/OUTCOME_V1_CASE_A_RUN3_20261002.md @40632158b9 | CLOSED 20261002T233705Z |

## Log

- 20261002T212155Z OPENED by 2.0.0_SA_COO~Y with 5 leg(s)
- 20261002T213059Z LEG U1 closed: irpt-ycharts-generate.zip version y3LRNAoPvGmdWYZSNb5moyTiEDvo8055 (21:23:07Z, 582443 bytes) read back sha256 wjSX3zZoFu
- 20261002T213215Z LEG U2 closed: both keys 404 before; tar irpt-resident-f89fc8e731-st14.tar.gz version 4N3RhbITXo1u1zIsLkPbc0oYYWNCUVYE, 777996 bytes, s
- 20261002T221441Z LEG D2 closed: 22:13Z via SSM (head-object printed 9GcYA4bL..; host fetched by key, sha256 430d4172.. verified; install rc=0): running 
- 20261002T222015Z LEG D1 closed: safe-apply ~22:18Z of targeted plan ST14/plan_d1_st14.txt (1 change, code only): Modifications complete, Apply complete 
- 20261002T233705Z LEG V1 closed: CLOSED per CTO rulings batch 192 (msg 104456): Case A run 3 from the page (23:24:44Z, UP-f0d8aead..): resident IRPT_RESI
- 20261002T233705Z CLOSED -- all 5 legs proven
