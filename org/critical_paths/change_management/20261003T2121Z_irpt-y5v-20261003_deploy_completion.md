# Deploy Completion Record
**Date opened:** 2026-10-03T21:21:51.839030+00:00
**Status:** OPEN
**Deploy:** Y-5 finding value: a ticker finding carries the file's symbol (generate Lambda + resident at one commit)
**Authored by:** 2.0.0_SA_COO~Y
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 12.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U1 | s3-prefix | irpt-ycharts-generate.zip at the merged pin, built from an autocrlf=false checkout | read back by version, sha equal; members byte-equal to git show; census vs live fD2R6OFr; cold-start smoke | irpt-ycharts-generate.zip version YImF8vih8CBtZqEM7XksUccMJ63UayVz (21:42:20Z, 591597 bytes) read back sha256 jKsI7pZWzjaTub83yRvk1tass0oiVZkp9jmvr1v9ezQ= ; built from a core.autocrlf=false worktree at 095968d363 (row repinned to a163441fb0): 114 members, 0 differ from the pin, 0 CRLF; census vs live fD2R6OFr: identical 105, changed 9 (portfolio.py the fix; enforce.py, ExportBundle/ExportReceipt/OwnedAnalysisRequest schemas, opal_naming.py, reporting_policies.json, owned_requests.py, resident_worker.py), added 0, removed 0; cold-start smoke PASS on 3 routes (Y5V/) | CLOSED 20261003T214643Z |
| U2 | s3-prefix | irpt-resident-<pin>-st19.tar.gz and its install script | both keys 404 before, read back by version; gate G1-G5 | both keys 404 before; tar irpt-resident-a163441fb0-st19.tar.gz version IJG0WnOfzvavTqPiurIYncWYL1ISXEfr 791835 bytes sha256 1c5bfc10..; script resident_host_install_a163441fb0-st19.sh version BHSM0RkX_qwSdbWs163_N4jbBgSuFoY9 8685 bytes sha256 f940529d..; both read back equal; gate G1-G5 PASS, G5 vs running st18: changed 6 (portfolio.py the fix; enforce.py; ExportReceipt x2 and export-download response schemas; resident_bindings.json), added 0, removed 0 (Y5V/) | CLOSED 20261003T215253Z |
| D1 | tf-lambda | ONE targeted safe-apply of module.irpt_ycharts_generate.aws_lambda_function.this | CodeSha256 read back; cold-start smoke live |  | OPEN |
| D2 | activation | resident install via SSM (root <pin>-st19) | running root, member digests, unit active, queue 0/0 |  | OPEN |
| V1 | verify | Aproxy from the page (2.0.0_SA_COO~D) | row 100 value TIMXX; SGOV named; NORMALIZED with the correction disclosed; READY Overview |  | OPEN |

## Log

- 20261003T212151Z OPENED by 2.0.0_SA_COO~Y with 5 leg(s)
- 20261003T214643Z LEG U1 closed: irpt-ycharts-generate.zip version YImF8vih8CBtZqEM7XksUccMJ63UayVz (21:42:20Z, 591597 bytes) read back sha256 jKsI7pZWzj
- 20261003T215253Z LEG U2 closed: both keys 404 before; tar irpt-resident-a163441fb0-st19.tar.gz version IJG0WnOfzvavTqPiurIYncWYL1ISXEfr 791835 bytes sha
