# Deploy Completion Record
**Date opened:** 2026-10-03T23:04:34.370010+00:00
**Status:** OPEN
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
| D1 | tf-lambda | ONE targeted safe-apply of module.irpt_ycharts_generate.aws_lambda_function.this | CodeSha256 read back; cold-start smoke on the deployed bytes |  | OPEN |
| D2 | activation | resident install via SSM (root 136ee09e9f-st20) | running root, member digests, unit active, queue 0/0 |  | OPEN |
| V1 | verify | Aproxy from the page (2.0.0_SA_COO~D) | the upload reconciles (or the refusal line names its counts); READY Overview |  | OPEN |

## Log

- 20261003T230434Z OPENED by 2.0.0_SA_COO~Y with 5 leg(s)
- 20261003T234236Z LEG U1 closed: irpt-ycharts-generate.zip version 31clJjOmhSm6YK4_6kH3ZkBD9GRxSol8 (23:29:52Z, 592374 bytes) read back sha256 FgZcBjJuwu
- 20261003T235749Z LEG U2 closed: both keys 404 before; tar irpt-resident-136ee09e9f-st20.tar.gz version cCO3C_41ttJOTNVTVYWIaBEjmdY88zUX 792704 bytes sha
