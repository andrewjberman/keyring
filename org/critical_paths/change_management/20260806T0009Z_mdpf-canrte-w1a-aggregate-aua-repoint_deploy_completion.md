# Deploy Completion Record
**Date opened:** 2026-08-06T00:09:26.694912+00:00
**Status:** OPEN
**Deploy:** MDPF_CANRTE W-1a: re-point WS-A aggregate_aua from platinum/ (served) to gold/mdpf_revamp/_aggregate_aua/ -- ATOMIC over producer AND all consumers; DS legs + AE~A TF legs, single rollback point
**Authored by:** 0.4.0_DS_ClientPlatform
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | opal-data-assets gold/mdpf_revamp/_aggregate_aua/ -- COPY 439 historical partitions from platinum (COPY not move; rollback target preserved) | CONTENT spot-check N partitions platinum-vs-gold byte/value compare -- NOT a key count (AE~A amendment A) | CONTENT-VERIFIED (not a count): 439/439 identical on name+ETag+Size across ALL pairs (comm -12 = 439, source-only 0, dest-only 0, zero-byte 0). BYTE CONTROL on 2026-08-05.json: byte-identical 10100B, parses, opal_aggregate_aua=1785080124.89. NEGATIVE CONTROL: two different partitions DIFFER, so the diff discriminates. COPY not move -- platinum source still 439, rollback target intact. | CLOSED 20260806T001833Z |
| L2 | git | mdpf_aggregate_aua.py :67-68 constants -- moves the WRITE (:1359) AND BOTH SELF-READS (load_prior_cohort0 :514-527, load_prior_partner_block :559-561) together | commit hash | ad76ad830 -- mdpf_aggregate_aua.py :79-80 -> opal-data-assets + gold/mdpf_revamp/_aggregate_aua (no trailing slash; all 4 use sites insert their own). WRITE + BOTH SELF-READS move together by construction. | CLOSED 20260806T002241Z |
| L3 | git | build_mdpf_etf_ownership_timeseries.py:68-69 HARDCODED constants (config cannot fix) | commit hash | ad76ad830 -- build_mdpf_etf_ownership_timeseries.py :75-76 hardcoded module constants -> same base path, no trailing slash (:120 inserts its own). | CLOSED 20260806T002241Z |
| L4 | s3-prefix | opal-data-mdpf code/gold -- DS source legs deployed | comp-pipescript deployed MATCH row | comp-pipescript deployed MATCH both files. VERIFIED ON DEPLOYED BYTES not rc: s3://opal-data-mdpf/code/scripts/gold/mdpf_aggregate_aua.py @20:29:44 :79-80 = opal-data-assets + gold/mdpf_revamp/_aggregate_aua; build_mdpf_etf_ownership_timeseries.py @20:29:49 :75-76 same. NEGATIVE CONTROL: dim_mdpf_account_distribution.py unchanged @16:08:24 -- deploy touched only its two declared files. THE RUNNING PRODUCER NOW WRITES GOLD; L5/L6 are unblocked and must follow. | CLOSED 20260806T003215Z |
| L5 | activation | opal-assets-daily-emitter env PLATINUM_BUCKET + AGGREGATE_PREFIX -> gold (AE~A, TF) | terraform apply + 0-diff re-plan |  | OPEN |
| L6 | activation | mdpf-daily-trigger env PLATINUM_AGG_PREFIX -> gold (AE~A, TF) | terraform apply + 0-diff re-plan |  | OPEN |
| L7 | verify | CONSUMER-SIDE: emitter next run reads GOLD via its OWN logged partition_key AND the 11 cohorts carry today's values | handler result partition_key + cohort values (NOT 'the gold file exists') |  | OPEN |
| L8 | verify | CONSUMER-SIDE: ETF builder emits DIVZ/IDVZ/PFDE/PFOE off the new location rather than going DARK (its failure mode is dark-per-date, not frozen) | 4 served keys with fresh timestamps |  | OPEN |
| L9 | verify | CONSUMER-SIDE: mdpf-daily-trigger head_object gate finds the partition it expects | trigger log / gate outcome |  | OPEN |

## Log

- 20260806T000926Z OPENED by 0.4.0_DS_ClientPlatform with 9 leg(s)
- 20260806T001833Z LEG L1 closed: CONTENT-VERIFIED (not a count): 439/439 identical on name+ETag+Size across ALL pairs (comm -12 = 439, source-only 0, des
- 20260806T002241Z LEG L2 closed: ad76ad830 -- mdpf_aggregate_aua.py :79-80 -> opal-data-assets + gold/mdpf_revamp/_aggregate_aua (no trailing slash; all 
- 20260806T002241Z LEG L3 closed: ad76ad830 -- build_mdpf_etf_ownership_timeseries.py :75-76 hardcoded module constants -> same base path, no trailing sla
- 20260806T003215Z LEG L4 closed: comp-pipescript deployed MATCH both files. VERIFIED ON DEPLOYED BYTES not rc: s3://opal-data-mdpf/code/scripts/gold/mdpf
