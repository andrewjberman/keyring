# Deploy Completion Record
**Date opened:** 2026-10-05T03:25:40.703294+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND ~Y S326: irpt-status serves the request history newest first (read whole, bounded; cursor contract unchanged), code 44cc631396
**Authored by:** 2.0.0_SA_COO~Y
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U1 | s3-prefix | irpt-status.zip built LF at the repinned commit | version + sha256 + census vs live | irpt-status.zip version Ji6C92YJzsOWQtvO0fJkTV2yYhqfE2bx 349179 bytes sha256 jhGc2J4Q5EesJgnLq8EzdE5ErrZLbyqnJ8m00R7CgdE= (re-downloaded, re-hashed equal); LF build from c3de44f260: 49 members, 0 differ from the pin, 0 CRLF; census vs live XPta1UMJ..: identical 48, changed 1 (owned_requests.py), added 0, removed 0; cold-start smoke PASS on 3 routes | CLOSED 20261005T034142Z |
| D1 | tf-lambda | ONE targeted safe-apply of module.irpt_status.aws_lambda_function.this (code only) | CodeSha256 read back |  | OPEN |
| V1 | verify | the history route's first page lists REQ-c1b53772 (Y-2) first for Cottonwood | history read |  | OPEN |

## Log

- 20261005T032540Z OPENED by 2.0.0_SA_COO~Y with 3 leg(s)
- 20261005T034142Z LEG U1 closed: irpt-status.zip version Ji6C92YJzsOWQtvO0fJkTV2yYhqfE2bx 349179 bytes sha256 jhGc2J4Q5EesJgnLq8EzdE5ErrZLbyqnJ8m00R7CgdE
