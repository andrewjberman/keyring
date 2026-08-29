# Deploy Completion Record
**Date opened:** 2026-08-25T18:52:21.840732+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260825T185547Z
**Deploy:** ETFS_POSITIONING: one calendar-free coverage rule replaces the fixed-income exception -- Andrew-direct 2026-08-25
**Authored by:** 1.0.0_SA_CTO~Z
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | SITEZ d50aeb9310 | hash (rides integration) | SITEZ d50aeb9310, commit-gate clean, msg-verify MATCH. LANDED LOCAL -- push is integrator-only. | CLOSED 20260825T185547Z |
| L2 | s3-prefix | lambda-artifacts producer zip | uploaded sha + content-sha256 metadata | PUT etf-positioning-producer.zip VersionId VG8a9Mrr6WQJ3Zpe_1gQx0NnwSPjCE_0, 40073 B, 3 members, content-sha256=pQ76SKsrmmY9RrQi4piSVwEHytutdxCBDQBh5K/XHNY=. Deterministic rebuild identical. | CLOSED 20260825T185547Z |
| L3 | activation | module.etf_positioning_producer TF apply | 0-destroy + 0-diff replan + CodeSha256 == uploaded | safe-apply 0 add / 1 change / 0 destroy. Re-plan -detailed-exitcode rc=0 (captured before any pipe) = No changes. | CLOSED 20260825T185547Z |
| L4 | verify | deployed bytes carry the new rule and NOT the old exception | package download + token controls | Downloaded package sha256 b64 == live CodeSha256 == uploaded (pQ76SKs...), so it IS the running artifact. TOKEN CONTROLS 4/4: 'START COVERAGE' and 'if first > start' PRESENT; 'trading_days_between(start, as_of)' ABSENT (the calendar dependency is gone from this function); negative control absent. The single remaining 'lenient' occurrence is line 638, INSIDE THE DOCSTRING explaining what was replaced -- read the hit, not the count. | CLOSED 20260825T185547Z |
| L5 | activation | ad-hoc republish | invoke rc + manifest | Ad-hoc republish under Andrew's standing authorization: StatusCode=200, FunctionError=null. Served generated_at 2026-08-25T18:54:34Z. | CLOSED 20260825T185547Z |
| L6 | verify | served: 184/189 full 8/8, 0 lost, equity controls unmoved | live S3 read | BEFORE/AFTER over all 189 rows x 8 windows (1512 cells): 1496 unchanged, 16 GAINED, 0 LOST, 0 CHANGED. ICT +6 -> 8/8 (1Y 103.0754), MER +6 -> 8/8, RBGLD +2 -> 8/8, AZN +1 and TTE +1 (neither was on any list -- the general rule found them). EQUITY CONTROLS byte-identical: MSFT, ASML, NVDA. SERVED: 184 of 189 rows full 8/8, ZERO partial; the 5 blanks are the 4 CASH bookkeeping lines and the TPG CVR (Bloomberg returned 0 rows over 13 months -- genuinely untraded, left null). SPEC REGRESSION CLEAN: canonical CASH 4/4, DIVZ/IDVZ 100.00, PFDE 100.01, PFOE 99.99 raw truth preserved. | CLOSED 20260825T185547Z |

## Log

- 20260825T185221Z OPENED by 1.0.0_SA_CTO~Z with 6 leg(s)
- 20260825T185547Z LEG L1 closed: SITEZ d50aeb9310, commit-gate clean, msg-verify MATCH. LANDED LOCAL -- push is integrator-only.
- 20260825T185547Z LEG L2 closed: PUT etf-positioning-producer.zip VersionId VG8a9Mrr6WQJ3Zpe_1gQx0NnwSPjCE_0, 40073 B, 3 members, content-sha256=pQ76SKsr
- 20260825T185547Z LEG L3 closed: safe-apply 0 add / 1 change / 0 destroy. Re-plan -detailed-exitcode rc=0 (captured before any pipe) = No changes.
- 20260825T185547Z LEG L4 closed: Downloaded package sha256 b64 == live CodeSha256 == uploaded (pQ76SKs...), so it IS the running artifact. TOKEN CONTROLS
- 20260825T185547Z LEG L5 closed: Ad-hoc republish under Andrew's standing authorization: StatusCode=200, FunctionError=null. Served generated_at 2026-08-
- 20260825T185547Z LEG L6 closed: BEFORE/AFTER over all 189 rows x 8 windows (1512 cells): 1496 unchanged, 16 GAINED, 0 LOST, 0 CHANGED. ICT +6 -> 8/8 (1Y
- 20260825T185547Z CLOSED -- all 6 legs proven
