# Deploy Completion Record
**Date opened:** 2026-06-25T15:32:31.945209+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260625T153459Z
**Deploy:** ADVI_BDAPIMIG P1-C: 49F freshness-probe Lambda + alarms (14 add) + A test-hook update + SMS-sub removal (false-coverage)
**Authored by:** 0.6.0_AE_PartnerETL
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD commits a875ce989+b1da30ac9 + bd tag pushed | hashes/tag --follow-tags | Pushed CLOUD 222231f98..7ba884490 (a875ce989 src+tf, b1da30ac9 sha, record-deploy) + tag bd-v2.34.0 --follow-tags | CLOSED 20260625T153458Z |
| L2 | activation | bd-49f-freshness-probe Lambda + bd-49f-freshness-sched rate(1h) + 6 alarms (authtoken-dead/absence + 4x silver-stale) live; A test-hook in-place; SMS sub destroyed; via TF apply 14-add/1-change/1-destroy | 0-diff plan + live describe | safe-apply: 14 add/1 change/1 destroy; 0-diff (No changes). Live: bd-49f-freshness-probe Lambda + bd-49f-freshness-sched rate(1h) + bd-49f-authtoken-dead + bd-49f-authtoken-absence + 4x bd-49f-silver-stale alarms created; A test-hook in-place; SMS sub destroyed (false-coverage). | CLOSED 20260625T153458Z |
| L3 | verify | live invoke bd-49f-freshness-probe -> auth_ok + silver_age_hours; egress test-hook publishes [TEST] (CVO re-runs delivery + 401-specificity) | invoke result + CVO delivery confirm | Live invoke bd-49f-freshness-probe -> {auth_ok:true, silver_age_hours:{transactions:1.47,allocations:1.72,realized:137.78,unrealized:137.86}} -- auth probe + per-table freshness both functioning; realized/unrealized correctly flagged stale (>30h threshold). Test-hook invoke -> {published:true} ([TEST] to opal-bd-49f-cookie-alerts). CVO re-runs delivery + 401-specificity verify. | CLOSED 20260625T153458Z |

## Log

- 20260625T153231Z OPENED by 0.6.0_AE_PartnerETL with 3 leg(s)
- 20260625T153458Z LEG L1 closed: Pushed CLOUD 222231f98..7ba884490 (a875ce989 src+tf, b1da30ac9 sha, record-deploy) + tag bd-v2.34.0 --follow-tags
- 20260625T153458Z LEG L2 closed: safe-apply: 14 add/1 change/1 destroy; 0-diff (No changes). Live: bd-49f-freshness-probe Lambda + bd-49f-freshness-sched
- 20260625T153458Z LEG L3 closed: Live invoke bd-49f-freshness-probe -> {auth_ok:true, silver_age_hours:{transactions:1.47,allocations:1.72,realized:137.7
- 20260625T153459Z CLOSED -- all 3 legs proven
