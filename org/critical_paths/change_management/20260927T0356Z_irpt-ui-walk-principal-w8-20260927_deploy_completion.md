# Deploy Completion Record
**Date opened:** 2026-09-27T03:56:50.003132+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260927T045416Z
**Deploy:** Window 8: INF's ONE Orion read (plan 7f64b166) + optional W8-2 on Andrew's word (packet e2462004; CTO @c42d47163d, CRO @1dbf46c36b)
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| C1 | activation | K1 + K1-CRED | W8-3 pins re-read; pre-read + censuses; put + read-back | W8-3 pins re-read equal (generate G/TqLPdL, adapter Ll6t4VPa + spent plan 01209afb, resident fe64236bbb-rb); pre-read 03:58Z K1 ABSENT, email-index 0, K1-CRED ABSENT; users 51 digest 76cbe66b..; SELECTION# 47; REPORT# 49F 19 / COT 0 / INF 0; INF PERFORMANCE_USE 1 (01209afb); chain census W8_CHAIN_CENSUS_BEFORE; 03:58:32Z K1 USER#usr_irptuiwalk_1790481488 put, read-back digest 62b8207d.. EQUAL; cap 05:58Z | CLOSED 20260927T035856Z |
| K1C | verify | K1-CRED deleted after the logins | ParameterNotFound | ~D logged in 04:01:32Z; ~Y has no Andrew word for W8-2 (101780), so no ~Y login; K1-CRED /irpt/ui-walk-principal/1790481488/password deleted 04:0xZ -> ParameterNotFound. A later ~Y login (W8-2 on Andrew's word) takes ONE fresh credential, minted and deleted, named here. | CLOSED 20260927T040236Z |
| D1 | verify | K1 delete after every job terminal | failing read + ~D reload | every job the window started is terminal (W8-2 REQ-a8e81b8e ATTENTION VENDOR_READ_BACK_REFUSED, per ~Y 101791; K11/K12 Performance reads are synchronous, no job); queues irpt-intake/generation/export 0/0 (generation-dlq 1 = window 6's known REQ-3a1b73a8 message, amendment 2); ~Y done (101791 'the principal can go'), ~D done (K12 101807, browser closed per 101811); 04:46:35Z walk_principal.py --kind=uiwalk delete 1790481488: K1 consistent GetItem no Item (VERIFIED); K1-CRED ParameterNotFound (already deleted 04:02:36Z), so the refused-login arm is not runnable; cap cron fc00ad2e cancelled. | CLOSED 20260927T045415Z |
| A1 | verify | route audit + write trace | 0 outside classes; keys traced; users == baseline; no auth after last exp | Routes: ~Y LIVE_CHAIN_1203_20260927_W8.json = 1 POST /auth/login + 1 POST /analysis/inputs + 1 POST /analysis; ~D w8-20260927.har (770 entries, sha256 8681959b487505b9.. re-hashed equal; leak check password/jwt/bearer false) = login 1, refresh 9, resolve 6, selections 14, 12 Performance GETs (INF pre-check 2, K11 2+2 reopen, COT pre-check 2, K12 2+2 reopen); /export 0, /analysis(by D) 0, /auth/admin 0 -> 0 outside the classes. Write trace (W8_CHAIN_CENSUS_BEFORE 03:58:24Z / AFTER 04:48:46Z; keys only): cottonwood irpt-requests 60->78, +18 = W8-2 K4/K5 (UPLOAD#/NORMALIZATION#/INPUT#, ARTIFACT#+RETENTION# original_holdings c4634b7e + normalized c71cdf3c + composition b2210b08, analysis#REQ-a8e81b8e) + K12 (PERFORMANCE_USE#22f0a988, ARTIFACT#/RETENTION#(+PROMOTION) ART-36a64d88 source evidence, RETENTION# a5cae16d, REPORT#RPT-b683f188, PERFORMANCE_ACCEPTED#2231da28); irpt-jobs/cottonwood 2->3 (+REQ-a8e81b8e); objects +1 original_holdings +1 normalized +1 composition; nothing gone. REPORT# (UI_WALK_W8_CENSUS_AFTER): 49F 19->19, COT 0->1 (RPT-b683f188, K12's HAR), INF 0->1 (RPT-df47a1fc, K11's HAR); INF PERFORMANCE_USE 1->2 (+7f64b166). SELECTION# 47->48: +sel_66e6034c, minted by cot_one_use_plan.py's served selections POST (line 83) after the before-census, the same id K12 read. Users 51->51, digest 76cbe66b.. equal. Auth: opalinvest-auth-handler, opal-portal-authorizer, opal-portal-rest-authorizer = 0 events naming irpt-uiwalk-1790481488 after 04:46:36Z, BUT the positive control over the window's life (03:58Z-) also reads 0: the auth handler logs method+path only (e.g. 04:01:25.931Z 'POST /auth/login'), so a by-name read cannot see this principal -- NOT discriminating (W7's same line was equally blind). The standing proof is K1 absent (consistent GetItem, VERIFIED). | CLOSED 20260927T045416Z |

## Log

- 20260927T035650Z OPENED by 2.0.0_SA_COO~P with 4 leg(s)
- 20260927T035856Z LEG C1 closed: W8-3 pins re-read equal (generate G/TqLPdL, adapter Ll6t4VPa + spent plan 01209afb, resident fe64236bbb-rb); pre-read 03
- 20260927T040236Z LEG K1C closed: ~D logged in 04:01:32Z; ~Y has no Andrew word for W8-2 (101780), so no ~Y login; K1-CRED /irpt/ui-walk-principal/1790481
- 20260927T045415Z LEG D1 closed: every job the window started is terminal (W8-2 REQ-a8e81b8e ATTENTION VENDOR_READ_BACK_REFUSED, per ~Y 101791; K11/K12 P
- 20260927T045416Z LEG A1 closed: Routes: ~Y LIVE_CHAIN_1203_20260927_W8.json = 1 POST /auth/login + 1 POST /analysis/inputs + 1 POST /analysis; ~D w8-202
- 20260927T045416Z CLOSED -- all 4 legs proven
