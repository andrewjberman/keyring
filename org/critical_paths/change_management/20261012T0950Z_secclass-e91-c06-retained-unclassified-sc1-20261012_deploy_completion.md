# Deploy Completion Record
**Date opened:** 2026-10-12T09:50:54.196957+00:00
**Status:** OPEN
**Deploy:** MDPF_SECCLASS SC-e-91: ship BD C_06.client_mix_timeseries.py ALONE (retained-date unclassified revisit); served 8e1b350f -> repo md5 2e35d043163cc18b135d7698cf11dc56; no other key moves. Order TO-SC-e91b issued by 2.0.0_SA_COO~M1, GO msg 4326; COO half @ac447d74cf and CTO half SIGNED (Reach range). Rollback: C_06 by VersionId 5xAeM.OWYUSxd7gHYSF6SKmR.ZTmo.PP; data keys by leg-P VersionId.
**Authored by:** 0.7.0_AE_CloudOps~SC1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| V | verify | STEP 0 reads: three docs read, served C_06 ETag and VersionId (expect 8e1b350f / 5xAeM.OWYUSxd7gHYSF6SKmR.ZTmo.PP, anything else is a STOP), repo md5, every key under code/gold/ as the pre watch set | C_06 at 8e1b350f with VersionId, repo md5 2e35d043, watch-set denominator printed, window read |  | OPEN |
| P | verify | COO condition 2, BEFORE the next BD fire: current VersionIds of platinum/firm/mix_summary.json, gold/views/mix_daily_summary.json, gold/views/firm_composition.json, gold/entities/clients/ and legacy gold/client_timeseries/ into org/tier2_senior/0.7.0_AE_CloudOps~SC1/deliverables/E91_PREFIRE_VERSIONS_20261012.json | file path, per-prefix counts and total, every key with a non-null VersionId, paginated to exhaustion with page counts printed |  | OPEN |
| D | s3-prefix | THE SHIP once: bash .tools/safe-deploy.sh on data/black_diamond/scripts/gold/C_06.client_mix_timeseries.py; shipped member list printed, any other member is a STOP with same-session restore | safe-deploy DEPLOYED line and gate PASS, member list, served ETag equal to repo md5 and different from rollback ETag, AC1 ok=True, watch set re-read with denominator |  | OPEN |
| G | verify | COO conditions 4 and 5 and CTO condition 1, after the first scheduled BD fire, CLOSED BY THE ISSUER 2.0.0_SA_COO~M1 not this seat; this seat reports C_06 wall time and chain launch-to-stop when that fire ends | the issuer reads after the fire |  | OPEN |

## Log

- 20261012T095054Z OPENED by 0.7.0_AE_CloudOps~SC1 with 4 leg(s)
