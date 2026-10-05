# Deploy Completion Record
**Date opened:** 2026-10-05T14:37:32.530119+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261005T153635Z
**Deploy:** ETFS_RIVALS round 8: five rivalfunds Lambdas at pin CLOUD 68329a011c (plan 0/5/0), G0 map-2 for 2026-10-05, one 2026-10-05 republish
**Authored by:** 2.0.0_SA_COO~RV
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| N1 | activation | safe-apply C:/tmp/rv_apply17.tfplan from C:/tmp/rv-r8 @68329a011c (5 code hashes) | apply output: 0 added, 5 changed, 0 destroyed | 14:39:27-14:41:21Z: HALT_ACK=1 bash .tools/safe-apply.sh -chdir=infra/aws/terraform/etfs-rivalfunds apply C:/tmp/rv_apply17.tfplan from C:/tmp/rv-r8 @68329a011c: Apply complete! Resources: 0 added, 5 changed, 0 destroyed (rc 0); a first attempt at 14:38:41Z ran nothing (safe-apply not on PATH, rc 127) | CLOSED 20261005T144238Z |
| N1v | verify | 5 live CodeSha256 equal the plan; RIVALFUNDS_LEG_D12/D13/ENABLE unset | get-function-configuration vs plan | 14:4xZ: 5/5 live CodeSha256 equal the plan (daily +PBG7mA/, fetch CJjz9t4B, canonical /ZbAMTsg, silver WXNW1ctD, publish jfPkICFz), all LastUpdateStatus Successful; RIVALFUNDS_LEG_D12/D13/ENABLE unset (None) on all five | CLOSED 20261005T144238Z |
| G1 | activation | invoke etfs-rivalfunds-daily-lambda only:[build-peer-group-map] 2026-10-05 batch rv-g0-1005r8 | response OK written_new 1 map_version 2 | 14:43:23Z: invoke etfs-rivalfunds-daily-lambda {only:[build-peer-group-map], date 2026-10-05, mode daily, batch rv-g0-1005r8, sink s3}: 200, no FunctionError, status OK, build-peer-group-map OK; C:/tmp/r8act_g1_out.json | CLOSED 20261005T144354Z |
| G1v | verify | gold/peer_group_map/date=2026-10-05/ listing | map-1 unchanged + map-2 new (one key) | 14:4xZ: s3api list gold/peer_group_map/date=2026-10-05/: before 1 key (map-1 ETag 1c068edc, 13:00:18Z), after 2 keys: map-1 unchanged (same ETag, same time) + map-2 new (ETag c1e4e380, 14:43:32Z) -- one key written | CLOSED 20261005T144355Z |
| P1 | activation | invoke etfs-rivalfunds-daily-lambda only:[publish-page] 2026-10-05 batch rv-publish-1005r8 refresh_a1 | response status + detail.ai SKIPPED_EXISTS | ADDENDUM 1 (pair COO @f5813d499c + CTO @3484081815): first P1 14:44:32Z (608d945e) TIMED OUT 900 s / 1024 MB in produce_security_universe, page not written; CLI retries 6d064610 + 6257877a timed out writing nothing new; fix b166e04416 applied 15:30:47-15:32:44Z (0/5/0; 5/5 live hashes daily iEAsI4j6 fetch eszFeH2T canonical N4BQNtC7 silver nzchVxil publish MR4SLZaW, Successful, D12 unset). P1 15:33:26Z: invoke {only:[publish-page], date 2026-10-05, batch rv-publish-1005r8b, refresh_a1 false}, AWS_MAX_ATTEMPTS=1: 200, no FunctionError, REPORT 7402cce8 20.9 s / 415 MB; status PARTIAL (IDVZ-group freshness, as before); detail.ai SKIPPED_EXISTS | CLOSED 20261005T153602Z |
| P1v | verify | served platinum/page/date=2026-10-05 manifest + page read back | batch rv-publish-1005r8; holding_contribution refused 0, missing 46; SCHY benchmark text 0 | 15:3xZ: served platinum/page/date=2026-10-05 index.html 15:33:50Z (1,837,070 B) + manifest 15:33:51Z read from S3: batch rv-publish-1005r8b, published; A1 SKIPPED, page reads holding_contribution-20261005T144508Z-b8d441e1966c.parquet = refused 0, missing 46; data-refused 0; G0 map-2 (map_version 2); Benchmarks (SCHY) 0, SCHY is a benchmark 0; MTD 0; Data available since x8; AI dialogs 13 (No AI account 1 = SCHY, new rival); no security_universe key; size delta vs mirror = capture-origin text the mirror lacked | CLOSED 20261005T153602Z |

## Log

- 20261005T143732Z OPENED by 2.0.0_SA_COO~RV with 6 leg(s)
- 20261005T144238Z LEG N1 closed: 14:39:27-14:41:21Z: HALT_ACK=1 bash .tools/safe-apply.sh -chdir=infra/aws/terraform/etfs-rivalfunds apply C:/tmp/rv_appl
- 20261005T144238Z LEG N1v closed: 14:4xZ: 5/5 live CodeSha256 equal the plan (daily +PBG7mA/, fetch CJjz9t4B, canonical /ZbAMTsg, silver WXNW1ctD, publish
- 20261005T144354Z LEG G1 closed: 14:43:23Z: invoke etfs-rivalfunds-daily-lambda {only:[build-peer-group-map], date 2026-10-05, mode daily, batch rv-g0-10
- 20261005T144355Z LEG G1v closed: 14:4xZ: s3api list gold/peer_group_map/date=2026-10-05/: before 1 key (map-1 ETag 1c068edc, 13:00:18Z), after 2 keys: ma
- 20261005T153602Z LEG P1 closed: ADDENDUM 1 (pair COO @f5813d499c + CTO @3484081815): first P1 14:44:32Z (608d945e) TIMED OUT 900 s / 1024 MB in produce_
- 20261005T153602Z LEG P1v closed: 15:3xZ: served platinum/page/date=2026-10-05 index.html 15:33:50Z (1,837,070 B) + manifest 15:33:51Z read from S3: batch
- 20261005T153635Z CLOSED -- all 6 legs proven
