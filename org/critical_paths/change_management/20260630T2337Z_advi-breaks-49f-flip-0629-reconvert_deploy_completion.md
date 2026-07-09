# Deploy Completion Record
**Date opened:** 2026-06-30T23:37:00.423476+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260701T021130Z
**Deploy:** ADVI_BREAKS 49F flip-tonight (Andrew GO 232230Z): transactions silver re-convert -> 06-29 -> A_03 positions_cube -> gold -> served un-freeze 06-26->06-29 to $1,831,666,360.06. Never-widen sign-off COMPLETE (Andrew+COO+CTO). Root: stale-silver (raw HAS 06-29, our silver lagged); fixed by force-reprocess (manifest filename-skip cleared).
**Authored by:** 0.4.0_DS_ClientPlatform~B
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | silver/transactions/2026-06-29 re-convert on fresh raw (DS ~B) | silver max trade_date==06-29 + ~316K rows | L1 CLEAN (l1_verify.py 0030Z, MY owner-RAVC): (i) raw 62,575 txn_ids ALL present in silver union, 0 missing; (ii) current_union_unique[>=01-27]=541,485 >= prior floor 538,178 (+3,307; 0.6.0 versioned baseline, NEVER#5 cross-check MATCH: 03-04=10,509, 02-27=20,259); (iii) max trade_date=06-29; (iv) silver/transactions/06-25=0 rows INVESTIGATED-BENIGN -- all 6,217 trade_date-06-25 txns present in union (06-27=6,150 + 06-29=67, 6,217/6,217), prior 06-25 partition also had 0 trade_date-06-25 rows (as-of export of older trades, fully redundant -> deduped empty); NOT loss. Merge 103 files 0 ERR. Benign cross-partition dup washes out at A_03 drop_duplicates keep=last (latest correction wins). Silver functionally correct for the flip. | CLOSED 20260701T003652Z |
| L2 | verify | A_03 positions_cube/2026-06-29 + gold-freshness + convergence gate (0.6.0_AE) | positions_cube/06-29 exists, built post-reconvert | A_03 positions_cube/2026-06-29 built 00:58:30 on the SETTLED silver (>00:30 re-convert); 0.6.0 L2-green. Verified present. | CLOSED 20260701T020320Z |
| L3 | verify | controlled gold run -> canonical/06-29 + cert/06-29 (0.7.0_AE) | canonical/holdings/06-29 + cert/06-29 written, gold ts > reconvert ts | 0.7.0 re-fired bd-gold-trigger (instance 00:45:14, one clean run); canonical/holdings/2026-06-29 written 01:00:38, cert/06-29 written 01:27 (certified 1,831,666,360.06 / gold_aua 1,733,726,603.64). Verified present. | CLOSED 20260701T020320Z |
| L4 | verify | served flip 5-tie + CK5/CK6 (DS ~B) | served as_of 06-29 + served.aua==cert/06-29 1,831,666,360.06 + gold_aua==holdings/06-29 to cent + penny-test 2bday | L4 FLIP-PASS (l6_verify.py 0201Z, my owner-RAVC): served flipped 06-26->06-29 @ 02:01:39; served.total.aua 1,831,666,360.06 == cert/06-29.certified_aua == silver/allocations[06-29] excl-mask replica, all to the CENT (d=+0.00); cert.gold_aua 1,733,726,603.64 == gold/canonical/holdings[06-29] mv-sum to the cent; gold-freshness PASS (holdings 01:00:38 + client_perf 01:27:32 built AFTER the settled-silver re-convert ~00:30); guard-floor + 2-bday penny-test PASS. 49F served-GREEN. | CLOSED 20260701T020320Z |
| L5 | verify | rollback-armed + 49F GREEN-vs-Orion cert (0.7.0 rollback + CVO) | 06-26 rollback confirmed armed pre-flip + served==Orion to cent | SUPERSEDED-COMPLETE via refire ledger advi-breaks-49f-flip-0629-refire (c914402cc, 5-tie CLOSED): served=cert=silver/allocations/06-29 sum=$1,831,666,360.06@06-29 penny-verified (0.6.0 bd-leg + 0.7.0 CDN 5-tie + L4 both-surface consistent). Author ~B reaped post-49F-complete; COO closing the stranded-on-reaped-lane leg. | CLOSED 20260701T021057Z |

## Log

- 20260630T233700Z OPENED by 0.4.0_DS_ClientPlatform~B with 5 leg(s)
- 20260701T003652Z LEG L1 closed: L1 CLEAN (l1_verify.py 0030Z, MY owner-RAVC): (i) raw 62,575 txn_ids ALL present in silver union, 0 missing; (ii) curren
- 20260701T020320Z LEG L2 closed: A_03 positions_cube/2026-06-29 built 00:58:30 on the SETTLED silver (>00:30 re-convert); 0.6.0 L2-green. Verified presen
- 20260701T020320Z LEG L3 closed: 0.7.0 re-fired bd-gold-trigger (instance 00:45:14, one clean run); canonical/holdings/2026-06-29 written 01:00:38, cert/
- 20260701T020320Z LEG L4 closed: L4 FLIP-PASS (l6_verify.py 0201Z, my owner-RAVC): served flipped 06-26->06-29 @ 02:01:39; served.total.aua 1,831,666,360
- 20260701T021057Z LEG L5 closed: SUPERSEDED-COMPLETE via refire ledger advi-breaks-49f-flip-0629-refire (c914402cc, 5-tie CLOSED): served=cert=silver/all
- 20260701T021130Z CLOSED -- all 5 legs proven
