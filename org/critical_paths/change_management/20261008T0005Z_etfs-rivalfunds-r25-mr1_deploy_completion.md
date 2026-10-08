# Deploy Completion Record
**Date opened:** 2026-10-08T00:05:30.570427+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261008T001417Z
**Deploy:** ETFS_RIVALS RIV-mr-1 alone (the marker read-out, render.py only): five rivalfunds Lambdas at content pin fd633ec4d2 (live f9f8334ef6 + commit 339ba875be), one republish of 2026-10-07 refresh_a1 false (halves: COO 888f6d1b61, CTO 86a90330bc; mr-1 J1 MET ADJUDICATION_v30)
**Authored by:** 2.0.0_SA_COO~RV
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | safe-apply of C:/tmp/rv_apply25mr.tfplan: 5 aws_lambda_function.stage in place | five live CodeSha256 equal the plan after-set, MemorySize 3008, 5 of 5 | safe-apply rc=0, Apply complete 0 added 5 changed 0 destroyed (halt gate: the same 76 automated ledger nudges, all from deploy_ledger.py). list-functions 00:1xZ: 5 of 5 at MemorySize 3008; CodeSha256 daily UHfCiT80, fetch OoXPTjMF, canonical 7KNOgjTc, silver 7SS2kS3b, publish DGtKYZj1 = the plan after-set | CLOSED 20261008T001048Z |
| L2 | verify | ONE republish etfs-rivalfunds-daily-lambda only publish-page date 2026-10-07 refresh_a1 false | return status OK plus REPORT Max Memory Used and Duration | invoke 00:10:48Z StatusCode 200, no FunctionError, status OK, batch rv-publish-1007r25mr, RequestId a150286d-57a2-4974-8b3c-c8ac33a88a43; REPORT Duration 73,525.34 ms of 900 s, Memory Size 3008 MB, Max Memory Used 557 MB; one attempt | CLOSED 20261008T001417Z |
| L3 | verify | served read: sizes against the prediction; 0 moved table rows (CTO C2: a moved row is a rollback); chart data identical; the same key classes as rounds 23 and 24 | the reads printed | round25/served_grade_2026-10-07.after_mr1.json: manifest not older than index, 13 chart objects; index 1,693,709 B, audit 1,255,777 B, charts 5,675,727 B, 5,894 markers, each equal to the prediction; 1 script block, one fetch target (this product chart route). CTO C2: no table object written (a1_produced: the three tables SKIPPED; the keys written since 00:09Z are 32: index, audit, manifest, 13 charts, 15 copies under revisions, one state record), so no table row moved; 13 of 13 chart objects carry data identical to the objects served before; audit page byte-equal | CLOSED 20261008T001417Z |

## Log

- 20261008T000530Z OPENED by 2.0.0_SA_COO~RV with 3 leg(s)
- 20261008T001048Z LEG L1 closed: safe-apply rc=0, Apply complete 0 added 5 changed 0 destroyed (halt gate: the same 76 automated ledger nudges, all from 
- 20261008T001417Z LEG L2 closed: invoke 00:10:48Z StatusCode 200, no FunctionError, status OK, batch rv-publish-1007r25mr, RequestId a150286d-57a2-4974-8
- 20261008T001417Z LEG L3 closed: round25/served_grade_2026-10-07.after_mr1.json: manifest not older than index, 13 chart objects; index 1,693,709 B, audi
- 20261008T001417Z CLOSED -- all 3 legs proven
