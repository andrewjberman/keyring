# Never-widen CTO half -- IRPT_DASHBD FWD-8: the split Black Diamond pull (DB-b-45)

Signer `1.0.0_SA_CTO~DELL2`, 2026-10-08 ~00:0xZ. **Pair:**
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/NEVER_WIDEN_PAIR_BD_SPLIT_PULL.md` @20669fcec6 (COO half SIGNED). The
halves are dell2's (laptop CTO ruling 106630, MSTR msg 1145).

## SIGNED, for exactly this act

- **The run:** one `bd_split_pull.py run --go`, at the pin the GO names (dell2 CLOUD at or after @35a0fc34d4), by laptop
  `0.7.0_AE_CloudOps~I`. At most one `sweep --go` of its FAILED set.
- **The vendor reads:** Black Diamond `performancePeriod`, READ only, under the runner's refusals:
  - 2,299 calls and 4,598 ranges;
  - `aggregate_rps` 2;
  - `failed_cap` 105;
  - abort on 3 consecutive failures or any unexpected 4xx.
- **The writes:** ONLY new objects under the builder-output prefix
  `s3://opal-data-assets/blackdiamond/49financial/bronze/reporting_performance/pull=split20261007/`. The runner refuses an existing
  key. No other prefix, firm, table, grant or schedule.

## Read at signing

- **Andrew's word:** the record @5ef6d33141, a commit by `0.0.0_AB_MSTR~DELL2` titled "... IRPT_DASHBD FWD-8 BD pull YES". It carries
  his per-use vendor word for exactly this one pull (CLAUDE.md: no vendor call without his per-use word). The laptop seat reads the
  record itself before step 1 (ruling 106630 (3)).
- **Writers of the named property:** 1 (the runner's landing), on one path.
- **Both branches** of the outcome (tie within 0.35 pp, or not) and **both run outcomes** (landed, or aborted by rule) are named in
  the pair, read from the round-19 analysis.

## Conditions

1. **Rollback is an S3 DELETE of the new keys**, and an S3 delete needs Andrew's word (CLAUDE.md, Agent Autonomy). The pair's "under
   the issuer's word" is not enough: a rollback that needs deletion goes to Andrew with the key list first.
2. **This is the first and only use of the word** (the dell2 abort @e39ea3dcca made 0 calls). A second run is a new word.

-- 1.0.0_SA_CTO~DELL2
