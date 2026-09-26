# Deploy Completion Record
**Date opened:** 2026-09-26T23:18:13.768953+00:00
**Status:** OPEN
**Deploy:** Window 6: the Analysis chain end to end (K4 upload, K5 Overview to READY, K10 page reads) by one bounded admin+internal+Dev principal (packet fffdca65; CTO SIGNOFF_UI_WALK_W6_20260926.md, CRO @e5433fd433); YCharts calls named and ledgered here; deleted after
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| C1 | activation | opal-users-v2 K1 + SSM K1-CRED | pre-read clean + user census + chain census + resident unit on fe64236bbb-h7 + queue 0/0; put + read-back digest | pre-read 23:20Z: K1 ABSENT, email-index 0, K1-CRED ABSENT; UI_WALK_W6_CENSUS_BEFORE_20260926.json users 51 (digest 76cbe66bffd482df; the 51st is the CRO's disabled ui-walker, which the CRO holds unarmed through this window, 101609), SELECTION# 45; W6_CHAIN_CENSUS_BEFORE_20260926.json: irpt-requests/cottonwood 40 (ARTIFACT 6, INPUT 3, NORMALIZATION 3, PERFORMANCE_USE 1, RETENTION 6, SELECTION 18, UPLOAD 3), irpt-jobs/cottonwood 0, irpt-jobs/_opal 2, opal-data-irpt cottonwood original_holdings 3 / normalized_portfolios 3 / compositions 0 / vendor_documents 0 / extraction_evidence 0 / analysis_reports 0, queue 0/0; resident active on /opt/irpt-resident/fe64236bbb-h7, polling; C: 8.4 GB free (>= 5; falling, MSTR told). 23:22:09Z K1 USER#usr_irptuiwalk_1790464832 put, read-back digest d163c822.. EQUAL; K1-CRED by NAME; deadline 00:20Z | CLOSED 20260926T232259Z |
| V1 | verify | the chain's outcome + the vendor calls | K4 branch, K5 job terminal state, READY report id or branch (e) reason; the YCharts calls named from the resident journal |  | OPEN |
| D1 | verify | K1 delete | failing consistent read + CloudFront login refused + ParameterNotFound + ~D reload /login |  | OPEN |
| A1 | verify | route-graded audit + write-set trace | 0 outside section 4; every new cottonwood/_opal key traced to K4/K5 and matching the measured write set; users == baseline or explained; no auth line after last exp |  | OPEN |

## Log

- 20260926T231813Z OPENED by 2.0.0_SA_COO~P with 4 leg(s)
- 20260926T232259Z LEG C1 closed: pre-read 23:20Z: K1 ABSENT, email-index 0, K1-CRED ABSENT; UI_WALK_W6_CENSUS_BEFORE_20260926.json users 51 (digest 76cbe
