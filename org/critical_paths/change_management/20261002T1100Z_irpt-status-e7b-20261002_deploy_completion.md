# Deploy Completion Record
**Date opened:** 2026-10-02T11:00:38.417257+00:00
**Status:** OPEN
**Deploy:** irpt-status at ONE commit ff8fd77ba2: E7b (comparisons only on include=comparisons) + E6 (read memo) + item 22 (history by client); supersedes E7 (CTO batches 142, 146); never-widen packet, both halves
**Authored by:** 2.0.0_SA_COO~Y
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U1 | s3-prefix | irpt-status.zip new version on opal-313476888478-lambda-artifacts/investor-reporting | read back by S3 version with sha256 equal to the built bytes; census against live | irpt-status.zip version Jg3uJ0x7mOrlV1MbGUp.KUNlmzfHlFsX (10:47:58Z, 330611 bytes) read back sha256 X/JLmPJZSDlexI7+AEGShnMU0ilrep3hnT9Vt6UsooE= equal; 46 members, 0 differ from the pin ff8fd77ba2's bundle; census vs live 2V7xV1: identical 36, changed 9, added 1 (E7B_STATUS/census_irpt-status_e7b.json) | CLOSED 20261002T110038Z |
| D1 | tf-lambda | ONE targeted safe-apply of module.irpt_status.aws_lambda_function.this | apply output; the plan's one change only |  | OPEN |
| V1 | verify | live CodeSha256 and the after-reads compared with the before-reads | CodeSha256 X/JLmPJZ; plain reads equal key for key; include names the comparisons |  | OPEN |

## Log

- 20261002T110038Z OPENED by 2.0.0_SA_COO~Y with 3 leg(s)
- 20261002T110038Z LEG U1 closed: irpt-status.zip version Jg3uJ0x7mOrlV1MbGUp.KUNlmzfHlFsX (10:47:58Z, 330611 bytes) read back sha256 X/JLmPJZSDlexI7+AEGS
