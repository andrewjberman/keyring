# Deploy Completion Record
**Date opened:** 2026-10-13T06:19:44.022290+00:00
**Status:** OPEN
**Deploy:** MDPF_SECCLASS SC-e-97: ship BD C_06.client_mix_timeseries.py and D_04.client_portal_summary.py TOGETHER (rolling re-derive of B_00's 15-date correction window); C_06 2e35d043 -> f847d8d105025ffbee94b1aa5092faf6, D_04 9d083669 -> 43a5d613ca9292329278573038f14158; gold_dispatch.sh and every other key unmoved. Order TO-SC-e97b by 2.0.0_SA_COO~M1, GO msg 4647, amendment 1 (leg P at BOTH destinations); COO half addenda 1-2 and CTO half addendum 2 SIGNED. Rollback: both code objects by step-0 VersionId (C_06 zjQmOYVVYTSGOWLFQ0P33vVeWkwp4_eT, D_04 ap.CyBT8aJijz5kWFsSNjEFU99itbXED); data keys by leg-P VersionId at their destination.
**Authored by:** 0.7.0_AE_CloudOps~SC1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| V | verify | STEP 0 reads: halves read, served C_06 / D_04 / gold_dispatch.sh ETag and VersionId (expect 2e35d043 zjQm..., 9d083669 ap.CyBT..., f568d11b; any other is a STOP), repo md5s, every key under code/gold/ as the pre watch set, a head-object of one canonical 49F key as read proof, window | the three code keys at their expected ETags, repo md5 f847d8d1 and 43a5d613, watch-set denominator printed, 49F read proof, runner stopped and trigger-pending absent |  | OPEN |
| P | verify | COO condition 3 and amendment 1, BEFORE the next BD fire: VersionIds at BOTH destinations derived with lib/platinum_dest.py (canonical opal-data-49financial advi/49financial/platinum/ entities clients and advisors, views mix_daily_summary and firm_composition, firm mix_summary, artifacts firm_mix_views and firm_mix_views_daily; legacy opal-data-bd gold/client_timeseries/ and gold/meta/client_timeseries_watermark.json) into org/tier2_senior/0.7.0_AE_CloudOps~SC1/deliverables/E97_PREFIRE_VERSIONS_20261012.json, plus the live bodies of mix_daily_summary, firm mix_summary and firm_mix_views beside it | file path, per-prefix page and key counts and total, every key with a non-null VersionId, paginated to exhaustion, bodies saved with the VersionId read |  | OPEN |
| D | s3-prefix | THE SHIP once under one window read: bash .tools/safe-deploy.sh on C_06 then on D_04, back to back, no fire between; each shipped member list printed, any member other than its one key is a STOP with same-session restore | both safe-deploy DEPLOYED lines and gate PASS, each served ETag equal to its repo md5 and different from its rollback ETag, gold_dispatch.sh unmoved, AC1 ok=True, watch set re-read with denominator |  | OPEN |
| G | verify | COO conditions 5, 6, 9, 10 and the CTO conditions, after the first scheduled BD fire that RUNS C_06, CLOSED BY THE ISSUER 2.0.0_SA_COO~M1 not this seat; this seat reports that fire's C_06 wall time, chain launch-to-stop and its C06-ROLLING-REDERIVE line | the issuer reads after the fire |  | OPEN |

## Log

- 20261013T061944Z OPENED by 0.7.0_AE_CloudOps~SC1 with 4 leg(s)
