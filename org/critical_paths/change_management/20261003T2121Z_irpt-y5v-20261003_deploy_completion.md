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
| U1 | s3-prefix | irpt-ycharts-generate.zip at the merged pin, built from an autocrlf=false checkout | read back by version, sha equal; members byte-equal to git show; census vs live fD2R6OFr; cold-start smoke |  | OPEN |
| U2 | s3-prefix | irpt-resident-<pin>-st19.tar.gz and its install script | both keys 404 before, read back by version; gate G1-G5 |  | OPEN |
| D1 | tf-lambda | ONE targeted safe-apply of module.irpt_ycharts_generate.aws_lambda_function.this | CodeSha256 read back; cold-start smoke live |  | OPEN |
| D2 | activation | resident install via SSM (root <pin>-st19) | running root, member digests, unit active, queue 0/0 |  | OPEN |
| V1 | verify | Aproxy from the page (2.0.0_SA_COO~D) | row 100 value TIMXX; SGOV named; NORMALIZED with the correction disclosed; READY Overview |  | OPEN |

## Log

- 20261003T212151Z OPENED by 2.0.0_SA_COO~Y with 5 leg(s)
