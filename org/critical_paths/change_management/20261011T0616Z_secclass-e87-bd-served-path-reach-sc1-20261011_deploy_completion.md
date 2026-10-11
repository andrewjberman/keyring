# Deploy Completion Record
**Date opened:** 2026-10-11T06:16:13.822880+00:00
**Status:** OPEN
**Deploy:** MDPF_SECCLASS SC-e-87: ship BD's three served classify sites (D_04, C_06, D_03) to code/gold/ so the ticker-no-row NAME:: fallback is reachable; no other key moves; lib stays eb9bb852. Order TO-SC-e87b issued by 2.0.0_SA_COO~M1; halves COO @c6202193c5 and CTO @20526c6cc7 SIGNED. Rollback per key by step-0 VersionId; data keys by leg-P VersionId.
**Authored by:** 0.7.0_AE_CloudOps~SC1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| V | verify | STEP 0 reads: both halves read, served ETag and VersionId of the three keys, repo md5 pair, all keys under code/gold/ in opal-data-bd as the pre watch set | the three ETags at 23d2f2ae/d7eb83b6/84f9bf8e with VersionIds, repo md5 equal to the signed digests, watch-set denominator printed |  | OPEN |
| P | verify | COO condition 2, BEFORE the next BD fire: current VersionIds of platinum/firm/mix_summary.json, gold/views/mix_daily_summary.json, gold/views/firm_composition.json and every gold/entities/clients key into org/tier2_senior/0.7.0_AE_CloudOps~SC1/deliverables/E87_PREFIRE_VERSIONS_20261011.json | file path, per-prefix counts and total, every key with a non-null VersionId, paginated to exhaustion with page count printed |  | OPEN |
| D | s3-prefix | THE SHIP once: bash .tools/safe-deploy.sh with the three named gold script paths; shipped member list printed, any other member is a STOP with same-session restore | safe-deploy DEPLOYED lines and gate PASS, member list, each served ETag equal to its repo md5 and different from its rollback ETag, AC1 ok=True, watch set re-read with denominator |  | OPEN |
| G | verify | COO condition 4, after the next scheduled BD fire, CLOSED BY THE ISSUER 2.0.0_SA_COO~M1 not this seat | the issuer read after the fire |  | OPEN |

## Log

- 20261011T061613Z OPENED by 0.7.0_AE_CloudOps~SC1 with 4 leg(s)
