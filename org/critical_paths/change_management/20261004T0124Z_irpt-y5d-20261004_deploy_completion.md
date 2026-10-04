# Deploy Completion Record
**Date opened:** 2026-10-04T01:24:47.369130+00:00
**Status:** OPEN
**Deploy:** Y-5 / S316: bind the upload at cents; a binding refusal is a named ATTENTION (generate Lambda + resident at one commit 3f29017cfc)
**Authored by:** 2.0.0_SA_COO~Y
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 12.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U1 | s3-prefix | irpt-ycharts-generate.zip at 3f29017cfc, built from an autocrlf=false checkout | read back by version, sha equal; members byte-equal to git show; census vs live FgZcBjJu; cold-start smoke | irpt-ycharts-generate.zip version w031eAfDs6mh.1ZOCaAks5bHDhKj8ajT (592791 bytes) read back sha256 uFTONal/RhfoETes4rqJ4xRjJV4d2/nv3OlwuR9AXCQ= ; LF build at 99dd031309 (row repinned to 3f29017cfc): 114 members, 0 differ from the pin, 0 CRLF; census vs live FgZcBjJu: identical 112, changed 2 (normalized_input.py, resident_worker.py), added 0, removed 0; cold-start smoke PASS on 3 routes (Y5D/) | CLOSED 20261004T013807Z |
| U2 | s3-prefix | irpt-resident-3f29017cfc-st21.tar.gz and its install script | both keys 404 before, read back by version; gate G1-G5 | both keys 404 before; tar irpt-resident-3f29017cfc-st21.tar.gz version Afk.fAfNkFDqQ6_ghVaHIYiUJZtwMyFj 793108 bytes sha256 40eaa8ee..; script resident_host_install_3f29017cfc-st21.sh version WjDopraRJ16d6CeXA7tgNjVzjyvB98Da 8685 bytes sha256 8c3a4fc1..; both read back equal; gate G1-G5 PASS, G5 vs running st20: changed 3 (normalized_input.py, resident_worker.py, resident_bindings.json), added 0, removed 0 (Y5D/) | CLOSED 20261004T013953Z |
| D1 | tf-lambda | ONE targeted safe-apply of module.irpt_ycharts_generate.aws_lambda_function.this | CodeSha256 read back; cold-start smoke on the deployed bytes | safe-apply ~01:5xZ of the fresh targeted plan Y5D/plan_d1_y5d.txt (code only; source_code_hash FgZcBjJu.. -> uFTONal..): Modifications complete after 10s, 0/1/0; read back 01:58:51Z CodeSha256 uFTONal/RhfoETes4rqJ4xRjJV4d2/nv3OlwuR9AXCQ=, 512 MB, 900 s, Successful; the deployed bytes hash the same; cold-start smoke PASS on 3 routes (Y5D/D1_READBACK_Y5D_20261004.txt). Before-read 01:47Z clean. CTO half batch 236 @e9c8c1d346 on blob dc23e50710. | CLOSED 20261004T020030Z |
| D2 | activation | resident install via SSM (root 3f29017cfc-st21) | running root, member digests, unit active, queue 0/0 | 02:00:30Z head-object of the script key printed WjDopraRJ16d6CeXA7tgNjVzjyvB98Da (8685 bytes); Y5D/install_fetch_and_run.sh over SSM (host sha256 check against 8c3a4fc1.., install rc=0, SHA256SUMS OK 251): running root /opt/irpt-resident/3f29017cfc-st21, unit active since 02:01:04Z, NRestarts 0, tracebacks_30s 0; normalized_input.py 1cbbcb47fcd34da7 and resident_worker.py 805bc24e1eb79368 equal git show 3f29017cfc; queue 0/0 (Y5D/INSTALL_OUTPUT_Y5D_20261004.txt). Rollback root 136ee09e9f-st20 kept. | CLOSED 20261004T020209Z |
| V1 | verify | Aproxy from the page (2.0.0_SA_COO~D) | the upload reconciles and binds; READY Overview |  | OPEN |

## Log

- 20261004T012447Z OPENED by 2.0.0_SA_COO~Y with 5 leg(s)
- 20261004T013807Z LEG U1 closed: irpt-ycharts-generate.zip version w031eAfDs6mh.1ZOCaAks5bHDhKj8ajT (592791 bytes) read back sha256 uFTONal/RhfoETes4rqJ4
- 20261004T013953Z LEG U2 closed: both keys 404 before; tar irpt-resident-3f29017cfc-st21.tar.gz version Afk.fAfNkFDqQ6_ghVaHIYiUJZtwMyFj 793108 bytes sha
- 20261004T020030Z LEG D1 closed: safe-apply ~01:5xZ of the fresh targeted plan Y5D/plan_d1_y5d.txt (code only; source_code_hash FgZcBjJu.. -> uFTONal..):
- 20261004T020209Z LEG D2 closed: 02:00:30Z head-object of the script key printed WjDopraRJ16d6CeXA7tgNjVzjyvB98Da (8685 bytes); Y5D/install_fetch_and_run
