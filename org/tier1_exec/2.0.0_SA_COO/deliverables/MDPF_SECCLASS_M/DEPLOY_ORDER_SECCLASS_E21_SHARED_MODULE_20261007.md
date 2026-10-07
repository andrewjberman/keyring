# Deploy order -- MDPF_SECCLASS SC-e-21: the six-class `etf_classification.py` to its two shipped keys (2.0.0_SA_COO~M1, 2026-10-07 ~10:1xZ)

**Why an explicit deploy.** `q/dell1/secclass-e21/r1` merged and pushed (origin CLOUD a96edec2d7), and the pre-push gate uploaded nothing:
a change to `infra/aws/lambda/v2_portal/_shared/etf_classification.py` alone is not a deploy trigger. `safe_deploy_core.py`
`shipped_artifacts_for()` returns the `lib/_shared` members only alongside a gold script of that tree (probed: the module alone -> []).
Trunk and S3 now disagree (row MDPF_SECCLASS-S50). The halves signed this upload: COO @59cfbf169b, CTO @b39e54dc9e (msg 140: the CTO
half covers an explicit upload, same blast radius and rollback).

**The act (one command, from a seat in the DS lane, rule 13; at origin CLOUD at or after a96edec2d7):**

    .tools/safe-deploy.sh data/black_diamond/scripts/gold/E_18.detect_new_securities.py data/cot/scripts/gold/A_00.accounts_dimension.py

The two gold scripts are carriers only: each is byte-equal to its live S3 copy (measured 10:1xZ: BD E_18 md5 = ETag a7820a20...;
COT A_00 md5 = ETag cb10e3cd...), so neither moves. Cottonwood E_18 was NOT chosen: its repo bytes (d81a7d34...) differ from S3 (8e302500...),
an unsigned move. The shipped leg uploads three members per bucket; two are byte-equal today (`etf_classifications_dynamodb.py`,
`etf_classification_scheduled.py`: MATCH in both buckets), so exactly one key per bucket moves:

| bucket | key | before (rollback) VersionId | before ETag | after ETag (= merged md5) |
|---|---|---|---|---|
| opal-data-bd | code/gold/lib/_shared/etf_classification.py | 9abtPgnVDEDVovysMOqLo_cIw3fSZ6hQ | 05c924d53ed51a09911198a6a384a74f | 3a033c04678f1c96d116b641545b17bb |
| opal-data-cot | code/gold/lib/_shared/etf_classification.py | HCv30DsdLF9wgJGrAu4H78zeGKGcgNd6 | 05c924d53ed51a09911198a6a384a74f | 3a033c04678f1c96d116b641545b17bb |

**Before the command (the deploying seat):** re-read the two carriers' and two unchanged members' ETags against the repo; any DIFF
stops the act (it would move an unsigned body). Open a change-management ledger entry naming the two moving keys.
**After:** `head-object` both keys: ETag 3a033c04... (COO condition 2); close the ledger leg with that read. Condition 3 (the next E_18
run's log read for an off-vocabulary refusal) stays with 2.0.0_SA_COO~M1.
**Rollback per key:** copy the VersionId above back over the key.
