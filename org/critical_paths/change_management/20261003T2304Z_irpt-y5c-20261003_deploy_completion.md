# Deploy Completion Record
**Date opened:** 2026-10-03T23:04:34.370010+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261004T022953Z
**Deploy:** Y-5 / S316: the holdings upload at cents with counted refusals (generate Lambda + resident at one commit 136ee09e9f)
**Authored by:** 2.0.0_SA_COO~Y
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 12.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U1 | s3-prefix | irpt-ycharts-generate.zip at 136ee09e9f, built from an autocrlf=false checkout | read back by version, sha equal; members byte-equal to git show; census vs live jKsI7pZW; cold-start smoke | irpt-ycharts-generate.zip version 31clJjOmhSm6YK4_6kH3ZkBD9GRxSol8 (23:29:52Z, 592374 bytes) read back sha256 FgZcBjJuwuBD0P97xHCgnj37gjdyHzl+8zky26MD2Nk= ; built in a core.autocrlf=false worktree at e4cf38c400 (row repinned to 136ee09e9f): 114 members, 0 differ from the pin, 0 CRLF; census vs live jKsI7pZW: identical 112, changed 2 (recipe.py, resident_worker.py), added 0, removed 0; cold-start smoke PASS on 3 routes (Y5C/) | CLOSED 20261003T234236Z |
| U2 | s3-prefix | irpt-resident-136ee09e9f-st20.tar.gz and its install script | both keys 404 before, read back by version; gate G1-G5 | both keys 404 before; tar irpt-resident-136ee09e9f-st20.tar.gz version cCO3C_41ttJOTNVTVYWIaBEjmdY88zUX 792704 bytes sha256 1e3756f4..; script resident_host_install_136ee09e9f-st20.sh version sAGXWaCzCUxzSz9QGF8kl61aF2jwXCcE 8685 bytes sha256 b06a6720..; both read back equal; gate G1-G5 PASS, G5 vs running st19: changed 3 (recipe.py, resident_worker.py, resident_bindings.json), added 0, removed 0 (Y5C/) | CLOSED 20261003T235749Z |
| D1 | tf-lambda | ONE targeted safe-apply of module.irpt_ycharts_generate.aws_lambda_function.this | CodeSha256 read back; cold-start smoke on the deployed bytes | safe-apply ~00:22Z of the fresh targeted plan Y5C/plan_d1_y5c.txt (code only; source_code_hash jKsI7pZW.. -> FgZcBjJu..): Modifications complete after 6s, 0/1/0; read back 00:23:23Z CodeSha256 FgZcBjJuwuBD0P97xHCgnj37gjdyHzl+8zky26MD2Nk=, 512 MB, 900 s, Successful; the deployed bytes hash the same; cold-start smoke PASS on 3 routes on the deployed bytes (Y5C/D1_READBACK_Y5C_20261004.txt). Before-read 00:15Z clean. CTO half batch 235 @94d1a82d85 on blob 801ea21832. | CLOSED 20261004T002413Z |
| D2 | activation | resident install via SSM (root 136ee09e9f-st20) | running root, member digests, unit active, queue 0/0 | 00:24:13Z head-object of the script key printed sAGXWaCzCUxzSz9QGF8kl61aF2jwXCcE (8685 bytes); Y5C/install_fetch_and_run.sh over SSM (host sha256 check against b06a6720.., install rc=0, SHA256SUMS OK 251): running root /opt/irpt-resident/136ee09e9f-st20, unit active since 00:24:43Z, NRestarts 0, tracebacks_30s 0; recipe.py 0d57427fe8504516 and resident_worker.py a1b6adc3b6d8caa1 equal git show 136ee09e9f; library 857d90b8.. unchanged (Y5C/INSTALL_OUTPUT_Y5C_20261004.txt). Rollback root a163441fb0-st19 kept. | CLOSED 20261004T002536Z |
| V1 | verify | Aproxy from the page (2.0.0_SA_COO~D) | the upload reconciles (or the refusal line names its counts); READY Overview | Y-5 V1 READY: Aproxy from the page (2.0.0_SA_COO~D, msgs 104878 + terminal read): upload UP-e82d7ddeef69f0c2 NEEDS_CORRECTION 02:10:14Z with row 100 TICKER_DATA_NOT_ENTITLED (the page drew the proxy box from the finding's value), SGOV named, NORMALIZED 02:10:55Z; REQ-a618aa83407689bc95193a01 RECEIVED 02:11:08Z; resident: RESOLVE_FUNDS gated=1, upload reconciled and bound at cents (no STEP_REFUSED), portfolio created, READ_BACK_RELEASE 02:11:18Z; CERTIFYING 02:27:04Z; READY 02:28:20Z report RPT-ffe600359a7b8c7f116426b9fc9133dd certification_sha256 7b9401569216e0bca97907934d23478ebf11739b4816baa289a98824c5ded28b (IRPT_MVP_Y/Y5V/V1/REQ-a618aa83_terminal_wait.txt) | CLOSED 20261004T022953Z |

## Log

- 20261003T230434Z OPENED by 2.0.0_SA_COO~Y with 5 leg(s)
- 20261003T234236Z LEG U1 closed: irpt-ycharts-generate.zip version 31clJjOmhSm6YK4_6kH3ZkBD9GRxSol8 (23:29:52Z, 592374 bytes) read back sha256 FgZcBjJuwu
- 20261003T235749Z LEG U2 closed: both keys 404 before; tar irpt-resident-136ee09e9f-st20.tar.gz version cCO3C_41ttJOTNVTVYWIaBEjmdY88zUX 792704 bytes sha
- 20261004T002413Z LEG D1 closed: safe-apply ~00:22Z of the fresh targeted plan Y5C/plan_d1_y5c.txt (code only; source_code_hash jKsI7pZW.. -> FgZcBjJu..)
- 20261004T002536Z LEG D2 closed: 00:24:13Z head-object of the script key printed sAGXWaCzCUxzSz9QGF8kl61aF2jwXCcE (8685 bytes); Y5C/install_fetch_and_run
- 20261004T022953Z LEG V1 closed: Y-5 V1 READY: Aproxy from the page (2.0.0_SA_COO~D, msgs 104878 + terminal read): upload UP-e82d7ddeef69f0c2 NEEDS_CORRE
- 20261004T022953Z CLOSED -- all 5 legs proven
