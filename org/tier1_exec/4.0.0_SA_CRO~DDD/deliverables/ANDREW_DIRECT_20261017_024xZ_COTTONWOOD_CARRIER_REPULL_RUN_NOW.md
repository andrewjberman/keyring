# ANDREW-DIRECT 2026-10-17 ~02:4xZ -- run the Cottonwood carrier re-pull now, do not wait for the morning

**Author:** 4.0.0_SA_CRO~DDD. **Channel:** the 4.0.0_SA_CRO~DDD terminal on dell1, ~02:4xZ 2026-10-17 (~22:4x ET 10-16).
**Follows:** `ANDREW_DIRECT_20261017_015xZ_COTTONWOOD_530M_MDPF_AND_ADVI_CRO_EXECUTES.md`, findings ADDENDUM 3 runbook.

## VERBATIM

"do the run now, we dont need to wait until the morning"

## What it settles

- The runbook's step 1 waited on 2.0.0_SA_COO~C1's "fire read done" after the ~13:00Z R106 read (C1 msg 7162, condition 1).
  Andrew's word supersedes that timing: the carrier re-pull, the silver rebuild and the gold runs go now.
- Relayed to 1.0.0_SA_CTO~DELL1 and 2.0.0_SA_COO~C1. C1's other conditions still apply: touch no account_attributes
  partition and no A_00 code, and send the write and gold run times so C1 can snapshot.

## Addendum ~03:5xZ -- restate 10/15 on MDPF (Andrew-direct, AskUserQuestion answer, VERBATIM option chosen)

Question: "Model Portfolios won't overwrite an already-published date. To show $530.42M for 10/15 tonight I need to put S3
delete markers on Cottonwood's four 10/15 gold objects (prior versions stay recoverable) and rerun. OK to do that?"
Answer: "Yes, restate 10/15 (Recommended)". Scope: Cottonwood's four dated 10/15 keys under portal/gold/mdpf/cottonwood/
(category-views, aggregate-aua-timeseries, aum-metrics, account-distribution). Delete markers only; prior versions kept.
