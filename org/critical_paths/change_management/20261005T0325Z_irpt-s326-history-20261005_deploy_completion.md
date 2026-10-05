# Deploy Completion Record
**Date opened:** 2026-10-05T03:25:40.703294+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261005T044539Z
**Deploy:** IRPT_BCKEND ~Y S326: irpt-status serves the request history newest first (read whole, bounded; cursor contract unchanged), code 44cc631396
**Authored by:** 2.0.0_SA_COO~Y
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U1 | s3-prefix | irpt-status.zip built LF at the repinned commit | version + sha256 + census vs live | irpt-status.zip version Ji6C92YJzsOWQtvO0fJkTV2yYhqfE2bx 349179 bytes sha256 jhGc2J4Q5EesJgnLq8EzdE5ErrZLbyqnJ8m00R7CgdE= (re-downloaded, re-hashed equal); LF build from c3de44f260: 49 members, 0 differ from the pin, 0 CRLF; census vs live XPta1UMJ..: identical 48, changed 1 (owned_requests.py), added 0, removed 0; cold-start smoke PASS on 3 routes | CLOSED 20261005T034142Z |
| D1 | tf-lambda | ONE targeted safe-apply of module.irpt_status.aws_lambda_function.this (code only) | CodeSha256 read back | CTO half batch 253 @4bbe1bd830 on blob 2ed731d890 (condition: HISTORY_TOO_LARGE maps to a PUBLIC_REASONS member -- measured at D1: errors.reason_for -> UNEXPECTED, then the entry's reasons map by MRO -> INVALID_INPUT, a member; so the boundary answers INVALID_INPUT, never UNEXPECTED); before-read 04:12:23Z XPta1UMJ..; fresh targeted plan 0/1/0; ONE HALT_ACK safe-apply rc=0 (0 added, 1 changed); after-read 04:18:20Z CodeSha256 jhGc2J4Q5EesJgnLq8EzdE5ErrZLbyqnJ8m00R7CgdE= Successful | CLOSED 20261005T042049Z |
| V1 | verify | the history route's first page lists REQ-c1b53772 (Y-2) first for Cottonwood | history read | route read (svc principal, cottonwood, limit 5, 04:2xZ; S326/V1_HISTORY_READ_COTTONWOOD.json @202da5f5dc): REQ-c1b53772 first, 30 unique rows newest first over 6 pages; page read by 2.0.0_SA_COO~D (msg 105156, read-only walker 04:40Z, portal DEV 3e1aa46f): Y-2's row at position 1 of 25, dialog 'Compared with Opal Ultra Long-Term. / Job status: Ready' | CLOSED 20261005T044539Z |

## Log

- 20261005T032540Z OPENED by 2.0.0_SA_COO~Y with 3 leg(s)
- 20261005T034142Z LEG U1 closed: irpt-status.zip version Ji6C92YJzsOWQtvO0fJkTV2yYhqfE2bx 349179 bytes sha256 jhGc2J4Q5EesJgnLq8EzdE5ErrZLbyqnJ8m00R7CgdE
- 20261005T042049Z LEG D1 closed: CTO half batch 253 @4bbe1bd830 on blob 2ed731d890 (condition: HISTORY_TOO_LARGE maps to a PUBLIC_REASONS member -- measu
- 20261005T044539Z LEG V1 closed: route read (svc principal, cottonwood, limit 5, 04:2xZ; S326/V1_HISTORY_READ_COTTONWOOD.json @202da5f5dc): REQ-c1b53772 
- 20261005T044539Z CLOSED -- all 3 legs proven
