# Deploy Completion Record
**Date opened:** 2026-10-03T21:21:51.839030+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261004T022953Z
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
| D1 | tf-lambda | ONE targeted safe-apply of module.irpt_ycharts_generate.aws_lambda_function.this | CodeSha256 read back; cold-start smoke live | safe-apply ~22:11Z of the fresh targeted plan Y5V/plan_d1_y5v.txt (code only; s3_object_version w2yfewe.. -> YImF8vih.., source_code_hash fD2R6OFr.. -> jKsI7pZW..): Modifications complete after 9s, Apply complete 0/1/0; read back 22:11:30Z CodeSha256 jKsI7pZWzjaTub83yRvk1tass0oiVZkp9jmvr1v9ezQ=, 512 MB, 900 s, Successful; the deployed bytes (get-function Code.Location) hash the same; cold-start smoke PASS on 3 routes on the deployed bytes (Y5V/D1_READBACK_Y5V_20261003.txt). Before-read 22:02Z clean (Y5V/BEFORE_READ_Y5V_20261003.txt). CTO half batch 233 @c880214d5e on blob 7d815d61db. | CLOSED 20261003T221232Z |
| D2 | activation | resident install via SSM (root <pin>-st19) | running root, member digests, unit active, queue 0/0 | 22:12:32Z head-object of the script key printed BHSM0RkX_qwSdbWs163_N4jbBgSuFoY9 (8685 bytes); Y5V/install_fetch_and_run.sh over SSM (host sha256 check against f940529d.., install rc=0, package SHA256SUMS OK 251 members): running root /opt/irpt-resident/a163441fb0-st19, unit active since 22:13:37Z, NRestarts 0, tracebacks_30s 0; installed portfolio.py 1e5c24176baa8960 and enforce.py f5681952cb0901f4 equal git show a163441fb0; host library 857d90b8.. unchanged; queue 0/0 (Y5V/INSTALL_OUTPUT_Y5V_20261003.txt). Rollback root a6f6e7165e-st18 kept on the host. | CLOSED 20261003T221519Z |
| V1 | verify | Aproxy from the page (2.0.0_SA_COO~D) | row 100 value TIMXX; SGOV named; NORMALIZED with the correction disclosed; READY Overview | Y-5 V1 READY: Aproxy from the page (2.0.0_SA_COO~D, msgs 104878 + terminal read): upload UP-e82d7ddeef69f0c2 NEEDS_CORRECTION 02:10:14Z with row 100 TICKER_DATA_NOT_ENTITLED (the page drew the proxy box from the finding's value), SGOV named, NORMALIZED 02:10:55Z; REQ-a618aa83407689bc95193a01 RECEIVED 02:11:08Z; resident: RESOLVE_FUNDS gated=1, upload reconciled and bound at cents (no STEP_REFUSED), portfolio created, READ_BACK_RELEASE 02:11:18Z; CERTIFYING 02:27:04Z; READY 02:28:20Z report RPT-ffe600359a7b8c7f116426b9fc9133dd certification_sha256 7b9401569216e0bca97907934d23478ebf11739b4816baa289a98824c5ded28b (IRPT_MVP_Y/Y5V/V1/REQ-a618aa83_terminal_wait.txt) | CLOSED 20261004T022953Z |

## Log

- 20261003T212151Z OPENED by 2.0.0_SA_COO~Y with 5 leg(s)
- 20261003T214643Z LEG U1 closed: irpt-ycharts-generate.zip version YImF8vih8CBtZqEM7XksUccMJ63UayVz (21:42:20Z, 591597 bytes) read back sha256 jKsI7pZWzj
- 20261003T215253Z LEG U2 closed: both keys 404 before; tar irpt-resident-a163441fb0-st19.tar.gz version IJG0WnOfzvavTqPiurIYncWYL1ISXEfr 791835 bytes sha
- 20261003T221232Z LEG D1 closed: safe-apply ~22:11Z of the fresh targeted plan Y5V/plan_d1_y5v.txt (code only; s3_object_version w2yfewe.. -> YImF8vih..,
- 20261003T221519Z LEG D2 closed: 22:12:32Z head-object of the script key printed BHSM0RkX_qwSdbWs163_N4jbBgSuFoY9 (8685 bytes); Y5V/install_fetch_and_run
- 20261004T022953Z LEG V1 closed: Y-5 V1 READY: Aproxy from the page (2.0.0_SA_COO~D, msgs 104878 + terminal read): upload UP-e82d7ddeef69f0c2 NEEDS_CORRE
- 20261004T022953Z CLOSED -- all 5 legs proven
