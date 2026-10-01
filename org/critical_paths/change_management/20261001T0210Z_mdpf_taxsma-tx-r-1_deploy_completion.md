# Deploy Completion Record
**Date opened:** 2026-10-01T02:10:40.180621+00:00
**Status:** OPEN
**Deploy:** MDPF_TAXSMA TX-r-1: backend release with Tax DISABLED and the rollout switch OFF -- functions mdpf-gold-lambda and opal-assets-mdpf-portal-publisher (each $LATEST only: 0 aliases, 0 published versions), packages built at e8994f23af
**Authored by:** 4.0.0_SA_CRO
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 14.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U1 | verify | both artifacts uploaded: s3://opal-data-assets/portal/gold/mdpf/_code/mdpf-gold-lambda.zip and s3://opal-313476888478-lambda-artifacts/opal-assets/opal-assets-mdpf-portal-publisher.zip | each downloaded back, sha256 equal to the built zip (gold ee12387e.., publisher a63f896a..), content-sha256 metadata carries the same hex; prior versions recorded for rollback |  | OPEN |
| P1 | verify | fresh saved plans of mdpf-pipeline and opal-assets | each plan changes only its one function (code + the commit pin; the publisher also gains TAXSMA_ROLLOUT_SWITCH=OFF) |  | OPEN |
| D1 | activation | safe-apply mdpf-pipeline (mdpf-gold-lambda) | deployed CodeSha256 equals the built zip; no Tax env var set; re-plan No changes |  | OPEN |
| D2 | activation | safe-apply opal-assets (opal-assets-mdpf-portal-publisher) | deployed CodeSha256 equals the built zip; TAXSMA_ROLLOUT_SWITCH=OFF on the applied plane; re-plan No changes |  | OPEN |
| V1 | verify | deployed qa_local invoke of mdpf-gold-lambda (dry run, zero S3 writes), before and after the apply | both green 16 of 16; every body difference a process-time path; Tax DISABLED |  | OPEN |
| V2 | verify | the next scheduled publisher run (13:50Z) | both served category-views keys content-equal to before on every field other than generation time (DELTA=0, comparison printed) |  | OPEN |

## Log

- 20261001T021040Z OPENED by 4.0.0_SA_CRO with 6 leg(s)
