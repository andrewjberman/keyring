# Deploy Completion Record
**Date opened:** 2026-09-27T02:54:08.980851+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260927T032452Z
**Deploy:** Window 7: the Analysis chain second attempt (packet 3ab51a52 = fffdca65 + D1-D5; CTO @c226ade7a3, CRO @d9b4142aa6; Andrew 'yes to all three' @6039c2f680); principal kept until jobs terminal (120-min cap); K1-CRED deleted after the logins
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| C1 | activation | K1 + K1-CRED | served pins re-read (generate G/TqLPdL, resident fe64236bbb-xv); pre-read + censuses; put + read-back | served pins re-read at create (CTO condition): generate CodeSha256 G/TqLPdL.., resident active on /opt/irpt-resident/fe64236bbb-xv; pre-read 02:54Z K1 ABSENT, email-index 0, K1-CRED ABSENT; users 51 digest 76cbe66b..; SELECTION# 47; REPORT# 49F 19 / COT 0 / INF 0; chain census W7_CHAIN_CENSUS_BEFORE_20260927.json (cottonwood rows 50 incl. the window-6 residue, jobs 1, _opal 2, queue 0/0); 02:55:07Z K1 USER#usr_irptuiwalk_1790477665 put, read-back digest a9e5e1d2.. EQUAL; K1-CRED by NAME; cap 04:55Z | CLOSED 20260927T025525Z |
| K1C | verify | K1-CRED deleted after ~D and ~Y logins (CRO condition) | ParameterNotFound | CRO condition: ~D logged in 02:56:29Z (101724ish), ~Y logged in 02:58:17Z; 02:59:5xZ ssm delete-parameter /irpt/ui-walk-principal/1790477665/password -> get-parameter ParameterNotFound. The K1 row stays until every job is terminal (cap 04:55Z); a later login needs ONE fresh credential, minted and deleted, named here. | CLOSED 20260927T030017Z |
| V1 | verify | the chain outcome | K4 branch; K5 job terminal (READY + report id, or named refusal); K10; vendor calls named from the journal | K4 02:59:57Z -> UP-f20976ad.. NORMALIZED (input portfolio_65bfe6d9..); K5 03:00:01Z -> 200 QUEUED REQ-e2fc5dd5dc2e050cc82a57e4 -> TERMINAL 03:00:10Z ATTENTION {code: VENDOR_READ_BACK_REFUSED}: intents holdings_upload (03:00:05Z) + portfolio_create (03:00:07Z) claimed, checkpoint_upload ok, checkpoint_portfolio model_portfolio_id 2363504, then the 7-setting read-back refused -> no report, no PDF. YCharts calls: identity/template reads, ONE holdings_upload, ONE portfolio_create (both objects KEPT: upload + portfolio 2363504), the read-back; no session capture needed (fresh session fence 13). No re-POST. K10 (~D 101736): the page lists no request without a client scope and no live route serves a request list, so the terminal job is not visible in the page (a product gap, to the CTO). K11 (amendment 3): 3 INF reads refused unspent (the page clamps to as-of 09-22 vs the plan's 09-25); the arm disarmed 03:21:34Z (ledger irpt-performance-inf-one-use-3-20260927). | CLOSED 20260927T032451Z |
| D1 | verify | K1 delete after every job is terminal | failing read + CloudFront login refused + ~D reload /login | every job the window started is terminal (REQ-e2fc5dd5 ATTENTION at 03:00:10Z; the queue 0/0); ~Y and ~D done (~D's browser closed 03:17Z); 03:22:20Z K1 DeleteItem -> consistent GetItem no Item (VERIFIED); K1-CRED already deleted 02:59:5xZ (ParameterNotFound), so the refused-login arm is not runnable; cap cron b8f97630 cancelled | CLOSED 20260927T032451Z |
| A1 | verify | route audit + write-set trace | 0 outside the classes; keys traced to K4/K5/K9; users == baseline; no auth after last exp | Routes: ~Y LIVE_CHAIN_1203_20260927_W7.json = 1 /auth/login + 1 POST /analysis/inputs + 1 POST /analysis; ~D k10-w7-20260927.har (460 entries, sha 8da38fa2..) = login 1, refresh 5, resolve 3, selections 3, GETs; export/analysis(by D)/auth-admin 0 -> 0 outside the classes. Write trace (W7_CHAIN_CENSUS_BEFORE/AFTER): cottonwood irpt-requests +10 = K4 UPLOAD#/NORMALIZATION#/INPUT# + 2x ARTIFACT#/RETENTION# (original_holdings, normalized_portfolio) + K5 analysis#REQ-e2fc5dd5#1 + ARTIFACT#/RETENTION# (composition); irpt-jobs/cottonwood +1 (the K5 job); _opal +0 new keys; objects +1 original_holdings +1 normalized +1 composition, 0 vendor/extraction/report; nothing gone. REPORT# 49F 19->19, COT 0->0, INF 0->0 (the K11 reads refused unspent). SELECTION# 47->47. Users 51->51, digest 76cbe66b.. equal. Auth handler + authorizer: 0 events naming irpt-uiwalk-1790477665 after 03:22:21Z (read 03:24Z; re-read after the last exp at the next tick). | CLOSED 20260927T032451Z |

## Log

- 20260927T025408Z OPENED by 2.0.0_SA_COO~P with 5 leg(s)
- 20260927T025525Z LEG C1 closed: served pins re-read at create (CTO condition): generate CodeSha256 G/TqLPdL.., resident active on /opt/irpt-resident/fe6
- 20260927T030017Z LEG K1C closed: CRO condition: ~D logged in 02:56:29Z (101724ish), ~Y logged in 02:58:17Z; 02:59:5xZ ssm delete-parameter /irpt/ui-walk-
- 20260927T032451Z LEG V1 closed: K4 02:59:57Z -> UP-f20976ad.. NORMALIZED (input portfolio_65bfe6d9..); K5 03:00:01Z -> 200 QUEUED REQ-e2fc5dd5dc2e050cc8
- 20260927T032451Z LEG D1 closed: every job the window started is terminal (REQ-e2fc5dd5 ATTENTION at 03:00:10Z; the queue 0/0); ~Y and ~D done (~D's brow
- 20260927T032451Z LEG A1 closed: Routes: ~Y LIVE_CHAIN_1203_20260927_W7.json = 1 /auth/login + 1 POST /analysis/inputs + 1 POST /analysis; ~D k10-w7-2026
- 20260927T032452Z CLOSED -- all 5 legs proven
