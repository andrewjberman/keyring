# Deploy Completion Record
**Date opened:** 2026-10-08T01:35:58.592724+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261008T113322Z
**Deploy:** ETFS_RIVALS rounds 25+26 readers (RIV-rg-1 narrowed by RIV-rg-2): five rivalfunds Lambdas at CLOUD 0576fb051f, one republish of 2026-10-07 refresh_a1 true; must move no served figure (halves: COO a4ce155438, CTO e081a672d4; rg-2 J1 MET ADJUDICATION_v33; C1 MET msg 31527)
**Authored by:** 2.0.0_SA_COO~RV
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 14.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | safe-apply of C:/tmp/rv_apply26.tfplan: 5 aws_lambda_function.stage in place | five live CodeSha256 equal the plan after-set, MemorySize 3008, 5 of 5 | safe-apply rc=0, Apply complete 0 added 5 changed 0 destroyed (halt gate: the same 76 automated ledger nudges, all from deploy_ledger.py). list-functions 01:4xZ: 5 of 5 at MemorySize 3008; CodeSha256 daily hwvMccck, fetch n7y+Lj2a, canonical uLmr4Ejy, silver 7KmpjwMV, publish 3ug0KrGK = the plan after-set | CLOSED 20261008T014132Z |
| L2 | verify | ONE republish etfs-rivalfunds-daily-lambda only publish-page date 2026-10-07 refresh_a1 true | return status OK plus REPORT Max Memory Used and Duration | invoke 01:41:32Z StatusCode 200, no FunctionError, status OK, batch rv-publish-1007r26, RequestId a88e29b3-0c30-4956-80a2-687c197b4477; REPORT Duration 131,690.30 ms of 900 s, Memory Size 3008 MB, Max Memory Used 967 MB; one attempt | CLOSED 20261008T015053Z |
| L3 | verify | served read: the three rebuilt tables row for row against the objects before them (one moved row is a rollback); chart data identical; sizes | the reads printed | round26/served_read_2026-10-07.after_r26.json: 0 moved table rows. holding_contribution and buying_trend were rebuilt by the new readers and wrote NO object (write_unique: an object of the same content sha exists; 3 objects before, 3 after). input_census wrote one new object: its price, gics and holdings rows (762, 762, 13) are identical as sets; 38 market_reading rows differ (readings that arrived after 17:46Z). The rendered page equalled the served bytes: no page object, revision copy or chart object written; index 1,693,709 B, 13 chart objects, sizes as predicted. Keys written under rivalfunds/etfs/ since 01:40Z: 2 (the census object and the state record) | CLOSED 20261008T015053Z |
| L4 | verify | first daily run on the shared reader, 2026-10-08 11:00Z (gold_canonical_shape and gold_trade_schedule) | status and REPORT lines; read with ledger etfs-rivalfunds-r22 L4 | 2026-10-08 scheduled run 11:00:33Z-11:06:19Z, REPORT lines read by 2.0.0_SA_COO~RV: fetch-holdings 1.0 s / 100 MB; build-silver 2.2 s / 236 MB; build-canonical-shape 156.6 s / 279 MB; publish-page 177.7 s / 1015 MB of 3008 MB; sum 337.5 s, under the 720 s line. Page date=2026-10-08 published 11:06:19Z: 13 funds in input, 11 updated (CGIC, SCHY held by report_date_freshness: the Terminal was signed out, vehicle exit 93/97), fund sections 1411 of 1411, 13 chart objects. First scheduled run of gold_canonical_shape and gold_trade_schedule on the shared reader (package pin 0576fb051f): holding_contribution 6066 rows, as_of 2026-10-07, g4_dates 5, refused {}. | CLOSED 20261008T113208Z |

## Log

- 20261008T013558Z OPENED by 2.0.0_SA_COO~RV with 4 leg(s)
- 20261008T014132Z LEG L1 closed: safe-apply rc=0, Apply complete 0 added 5 changed 0 destroyed (halt gate: the same 76 automated ledger nudges, all from 
- 20261008T015053Z LEG L2 closed: invoke 01:41:32Z StatusCode 200, no FunctionError, status OK, batch rv-publish-1007r26, RequestId a88e29b3-0c30-4956-80a
- 20261008T015053Z LEG L3 closed: round26/served_read_2026-10-07.after_r26.json: 0 moved table rows. holding_contribution and buying_trend were rebuilt by
- 20261008T113208Z LEG L4 closed: 2026-10-08 scheduled run 11:00:33Z-11:06:19Z, REPORT lines read by 2.0.0_SA_COO~RV: fetch-holdings 1.0 s / 100 MB; build
- 20261008T113322Z CLOSED -- all 4 legs proven
