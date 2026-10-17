# Deploy Completion Record
**Date opened:** 2026-10-17T04:35:54.170428+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261017T045308Z
**Deploy:** FWD-10 addendum B: Cottonwood pair supervised switch (AUM BY MODEL donut) -- mdpf-gold-lambda f09a6a3adb -> d2f734fbac (zip 7c05d9e2..); CTO half @294efba8e2
**Authored by:** 4.0.0_SA_CRO~DDD
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U1 | verify | upload zip | read back sha256 | VersionId wy83O06z4_6T1IJvbEM_Q9mlcwXuoFqQ (metadata content-sha256 7c05d9e2..); downloaded back by id: sha256 7c05d9e2074b3eca597a9c6647d27c97705f2513a4a6960ec9fdea0b6740778d equal; prior Fug5LxhL.. | CLOSED 20261017T044117Z |
| D1 | activation | safe-apply MDPF_GOLD_COMMIT d2f734fbac | plan 0/1/0; CodeSha256 + env read back; re-plan No changes | plan 0/1/0 (s3_object_version Fug5LxhL->wy83O06z, source_code_hash 9a1073b0->7c05d9e2, MDPF_GOLD_COMMIT f09a6a3adb->d2f734fbac); Apply complete 0/1/0; CodeSha256 fAXZ4gdLPspZepxmR9J8l3BfJROkppYOyf3qC2dAd40= == b64(7c05d9e2..), env d2f734fbac, Successful; re-plan No changes | CLOSED 20261017T044117Z |
| R1 | s3-prefix | runner copy build_cottonwood_mdpf_pair.py | safe-deploy MATCH + sha | safe-deploy DEPLOYED [mdpf] + VERIFY OK; opal-data-mdpf code/scripts/assets_gold/build_cottonwood_mdpf_pair.py sha256 876f66e93eade6fe.. == git HEAD bytes | CLOSED 20261017T044118Z |
| Q1 | verify | qa_local | cot aum-metrics total 530,421,988.14; which dated keys business-differ | qa_local on d2f734fbac: green, errors none; cottonwood aum-metrics 2026-10-15 total.aum 530,421,988.14 (model 268,523,373.04, non_model 261,898,615.10, accounts 385). Dated-key compare vs live (provenance stripped): aum-metrics DIFFERS (total, last_updated); account-distribution only generated_at (process-time) -> NOT touched per CTO C-1; category-views EQUAL; aggregate-aua-timeseries EQUAL | CLOSED 20261017T044311Z |
| L1 | activation | laptop marker aum-metrics 10/15 + gold + publish | platinum total.aum 530,421,988.14 | laptop 0.7.0_AE_CloudOps~MDPF1 on XB-20261017T044329Z-f125 (delivered 04:47:49Z): marker on cottonwood aum-metrics 2026-10-15 + gold + publish. SERVED opal-data-portal-v2 platinum/mdpf/cottonwood/aum-metrics.json total.aum 530,421,988.14 at 04:52:25Z, beside category-views sums.total_aua 530,421,988.14 (CTO C-2 holds) | CLOSED 20261017T045308Z |

## Log

- 20261017T043554Z OPENED by 4.0.0_SA_CRO~DDD with 5 leg(s)
- 20261017T044117Z LEG U1 closed: VersionId wy83O06z4_6T1IJvbEM_Q9mlcwXuoFqQ (metadata content-sha256 7c05d9e2..); downloaded back by id: sha256 7c05d9e20
- 20261017T044117Z LEG D1 closed: plan 0/1/0 (s3_object_version Fug5LxhL->wy83O06z, source_code_hash 9a1073b0->7c05d9e2, MDPF_GOLD_COMMIT f09a6a3adb->d2f7
- 20261017T044118Z LEG R1 closed: safe-deploy DEPLOYED [mdpf] + VERIFY OK; opal-data-mdpf code/scripts/assets_gold/build_cottonwood_mdpf_pair.py sha256 87
- 20261017T044311Z LEG Q1 closed: qa_local on d2f734fbac: green, errors none; cottonwood aum-metrics 2026-10-15 total.aum 530,421,988.14 (model 268,523,37
- 20261017T045308Z LEG L1 closed: laptop 0.7.0_AE_CloudOps~MDPF1 on XB-20261017T044329Z-f125 (delivered 04:47:49Z): marker on cottonwood aum-metrics 2026-
- 20261017T045308Z CLOSED -- all 5 legs proven
