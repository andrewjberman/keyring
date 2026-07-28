# Deploy Completion Record
**Date opened:** 2026-07-28T14:07:32.438798+00:00
**Status:** OPEN
**Deploy:** MDPF gold cutover: deploy repo HEAD dim_mdpf_aggregate_aua_timeseries.py to s3://opal-data-mdpf/code/scripts/gold/ -- restores Cottonwood 3-firm fold + basis-B identity fix (23 commits undeployed since 07-21T17:42:40Z; mdpf absent from PIPELINE_MAP so no push could deploy it). CTO GO 20260728T140546Z, time-boxed before the ~15:00Z scheduled run.
**Authored by:** 0.4.0_DS_ClientPlatform
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | s3://opal-data-mdpf/code/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py | head-object from S3 itself: ContentLength 124241 AND md5 068bc089d436d296fe29e781a31bad04 (NOT the upload rc -- a --quiet cp that no-ops reports success) | VERIFIED FROM S3 BY INDEPENDENT RE-DOWNLOAD (not the upload rc): head-object 2026-07-28T14:08:26Z ContentLength=124241 ETag=068bc089d436d296fe29e781a31bad04; re-read body byte-identical to repo HEAD blob (md5 068bc089d436d296fe29e781a31bad04 both). PRE-DEPLOY was 51999B @2026-07-21T17:42:40Z md5 283b395f. Content assertions on the deployed bytes: load_cottonwood_slice=2, 3-leg signature build_global_artifact(a49,ainf,acot)=1, cohort_provenance=24, carry_forward_with_basis=2, frontier_stamp_staleness=4. NEGATIVE CONTROL: old 2-leg signature 'build_global_artifact(a49: dict, ainf: dict) ->' count=0 (gone). | CLOSED 20260728T141009Z |
| L2 | verify | the ~15:00Z scheduled run PICKED IT UP | the run's OWN log shows the 3-firm build (cottonwood leg loaded, cohort_provenance populated) -- the runner syncs --delete at dispatch, so the object alone is not proof |  | OPEN |
| L3 | verify | produced gold is correct and NOT published | new gold/mdpf_revamp/global carries cottonwood + sum identity 0 failing; portal-v2/json/mdpf/* serve UNCHANGED at 5f758b47 (L1 gates publish; CTO holds those keys) |  | OPEN |

## Log

- 20260728T140732Z OPENED by 0.4.0_DS_ClientPlatform with 3 leg(s)
- 20260728T141009Z LEG L1 closed: VERIFIED FROM S3 BY INDEPENDENT RE-DOWNLOAD (not the upload rc): head-object 2026-07-28T14:08:26Z ContentLength=124241 E
