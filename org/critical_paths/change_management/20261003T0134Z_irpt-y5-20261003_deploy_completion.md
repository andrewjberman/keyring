# Deploy Completion Record
**Date opened:** 2026-10-03T01:34:45.012103+00:00
**Status:** OPEN
**Deploy:** Y-5 packet 1: the resident (st15 -> st16) and irpt-ycharts-generate at 34088050e0 -- user-named proxy corrections; gated rows named
**Authored by:** 2.0.0_SA_COO~Y
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 24.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U1 | s3-prefix | irpt-ycharts-generate.zip at 34088050e0 from an autocrlf=false checkout | read back by version, sha equal; every member byte-equal to git show (S286); census vs live VZvhvWRM; cold-start smoke | irpt-ycharts-generate.zip version oew.wOPKuZQKvi30OCFECa5x7Dk_9MOL (01:37:42Z, 586808 bytes) read back sha256 aug0YyWcP6wwRwwnkyWYH+GBfT8gN9irrmEMCz/Vvj8= ; built from a core.autocrlf=false checkout: 113 members, 0 differ from git show 34088050e0, 0 CRLF (S286 remedied); census vs live VZvhvWRM: identical 109, eol_only 14 (live's CRLF copies), changed 4 (AnalysisUploadRequest contract, portfolio.py, uploads.py, report.pdf EOL), added 0, removed 0; cold-start smoke PASS on 3 routes (Y5/) | CLOSED 20261003T014113Z |
| U2 | s3-prefix | irpt-resident-34088050e0-st16.tar.gz and its install script | both keys 404 before, read back by version; gate G1-G5 | both keys 404 before; tar irpt-resident-34088050e0-st16.tar.gz version eB6EYhL7W5R9SWNmwtOnDZnkFhL1kcCA 784084 bytes sha256 4d231519..; script version cBX09ViGMXenXFxtK8Cd6goAVXjFEZeo 8683 bytes sha256 ee864bf3..; both read back equal; gate G1-G5 PASS, G5 vs running st15: changed 5 (Y-5's four + bindings), added 0, removed 0 | CLOSED 20261003T014331Z |
| D1 | tf-lambda | ONE targeted safe-apply of module.irpt_ycharts_generate.aws_lambda_function.this | CodeSha256 read back | safe-apply ~02:06Z of targeted plan Y5/plan_d1_y5.txt (code only): Modifications complete, Apply complete 0/1/0; read back 02:07:19Z CodeSha256 aug0YyWcP6wwRwwnkyWYH+GBfT8gN9irrmEMCz/Vvj8=, 512 MB, 900 s, Successful; cold-start smoke PASS live (Y5/D1_READBACK_20261003.txt). Same window as D2 (02:03Z). The served generate bundle now carries LF members (S286). | CLOSED 20261003T020834Z |
| D2 | activation | resident install via SSM (root 34088050e0-st16) | running root, member digests, unit active, queue 0/0 | 02:03Z via SSM (head-object printed cBX09ViG..; host fetched by key, sha256 ee864bf3.. verified; install rc=0): running root /opt/irpt-resident/34088050e0-st16; st16 digests equal the pin's blobs (portfolio d81c071e2ba3213e, uploads 253bc7ec44d0de36, status cb3b2ea620f83090); unit active since 02:03:31Z; queue 0/0 (Y5/INSTALL_OUTPUT_Y5_20261003.txt). Before-read 02:01Z clean (CTO half batch 198). | CLOSED 20261003T020512Z |
| V1 | verify | after option A: Case A with TIMXX -> SGOV from the page (Y-5), solo gate | gated row named with words; corrected re-post NORMALIZED with SGOV; READY Overview |  | OPEN |

## Log

- 20261003T013445Z OPENED by 2.0.0_SA_COO~Y with 5 leg(s)
- 20261003T014113Z LEG U1 closed: irpt-ycharts-generate.zip version oew.wOPKuZQKvi30OCFECa5x7Dk_9MOL (01:37:42Z, 586808 bytes) read back sha256 aug0YyWcP6
- 20261003T014331Z LEG U2 closed: both keys 404 before; tar irpt-resident-34088050e0-st16.tar.gz version eB6EYhL7W5R9SWNmwtOnDZnkFhL1kcCA 784084 bytes sha
- 20261003T020512Z LEG D2 closed: 02:03Z via SSM (head-object printed cBX09ViG..; host fetched by key, sha256 ee864bf3.. verified; install rc=0): running 
- 20261003T020834Z LEG D1 closed: safe-apply ~02:06Z of targeted plan Y5/plan_d1_y5.txt (code only): Modifications complete, Apply complete 0/1/0; read ba
- 20261003T070424Z HELD-SOVEREIGN-GATED gate=sovereign/Andrew option A: the attended YCharts sign-in that replaces the EVICTED session 
- 20261003T163630Z HOLD RELEASED -> OPEN
