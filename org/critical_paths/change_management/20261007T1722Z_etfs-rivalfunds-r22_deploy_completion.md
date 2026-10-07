# Deploy Completion Record
**Date opened:** 2026-10-07T17:22:12.098428+00:00
**Status:** OPEN
**Deploy:** ETFS_RIVALS rounds 15-22: five rivalfunds Lambdas at CLOUD beb13d39ff, memory 1024 -> 3008, one republish of 2026-10-07 (halves: COO b2ed0588f4, CTO 19eb48bda5)
**Authored by:** 2.0.0_SA_COO~RV
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 24.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | safe-apply of C:/tmp/rv_apply22.tfplan: 5 aws_lambda_function.stage in place | five live CodeSha256 equal the plan after-set and MemorySize 3008, 5 of 5 | safe-apply rc=0, Apply complete 0 added 5 changed 0 destroyed (HALT_ACK after review: 76 automated ledger nudges, none a stop, none naming rivalfunds). list-functions 17:3xZ: 5 of 5 at MemorySize 3008; CodeSha256 daily fRDyQ2eK, fetch OyCwkAJ2, canonical agDnuNLz, silver WiQ5KvRF, publish Sh82EnlI = the plan after-set; daily State Active, LastUpdateStatus Successful | CLOSED 20261007T173824Z |
| L2 | verify | ONE republish etfs-rivalfunds-daily-lambda only publish-page date 2026-10-07 refresh_a1 true | return status OK plus REPORT Max Memory Used and Duration | invoke 17:44:47Z StatusCode 200, no FunctionError, status OK, batch rv-publish-1007r22, RequestId d6d385eb-ce74-4914-887b-0fbdf3b8f24f; REPORT Duration 164,506.65 ms of 900 s, Memory Size 3008 MB, Max Memory Used 1009 MB. A first attempt at 17:38:54Z dropped at the client after 23 s (connection closed); 0 log events in the 5 minutes after and the page objects unmoved, so no run started and this is the one run | CLOSED 20261007T174950Z |
| L3 | verify | served page: manifest newer than index, 13 chart objects, sizes against the prediction, page and one chart through the gateway | the reads printed (CTO C1) and the AI period-word count (CTO C2) |  | OPEN |
| L4 | verify | first full daily run 2026-10-08 11:00Z | REPORT Max Memory Used and Duration; above 720 s is a BLOCKING row |  | OPEN |
| L5 | verify | first sweep 2026-10-08 13:00Z | REPORT Max Memory Used and Duration per function that ran |  | OPEN |

## Log

- 20261007T172212Z OPENED by 2.0.0_SA_COO~RV with 5 leg(s)
- 20261007T173824Z LEG L1 closed: safe-apply rc=0, Apply complete 0 added 5 changed 0 destroyed (HALT_ACK after review: 76 automated ledger nudges, none a
- 20261007T174950Z LEG L2 closed: invoke 17:44:47Z StatusCode 200, no FunctionError, status OK, batch rv-publish-1007r22, RequestId d6d385eb-ce74-4914-887

## Notes (2.0.0_SA_COO~RV, 2026-10-07 ~17:5xZ)

- BLAST RADIUS, added after the act (CTO ruling msg 31247): the republish's refresh also wrote ONE write-once object under gold/input_census/date=2026-10-07 (input_census-20261007T174647Z-45aef6f4e60c.parquet, 14,711 B), the third A1 table; the COO half's table named two. No served effect; rollback as for the other two tables.
- Leg L3's reader of the page through mcp.opalinvest.dev/rivalfunds is Andrew (CTO ruling msg 31247): the sign-in is his and no seat performs it. His report at the CTO terminal, relayed, closes the leg. The S3-side served read is done: round22/served_grade_2026-10-07.json @dca1f916d9.
