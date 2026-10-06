# Deploy Completion Record
**Date opened:** 2026-10-05T19:43:09.436788+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261005T213558Z
**Deploy:** ETFS_RIVALS D12 Step B: flip RIVALFUNDS_LEG_D12 in leg_gates.json, deploy it, import the 189 local IDVZ/PFOE captures with rebuild_funds, census, one refresh republish
**Authored by:** 2.0.0_SA_COO~RV
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| F1 | activation | commit leg_gates.json RIVALFUNDS_LEG_D12 0 -> 1 (ENABLE, D13 stay 0) | commit hash + file read back at HEAD | commit 35c6b3a923: data/etfs/scripts/rivalfunds/leg_gates.json read at HEAD: ENABLE 0, D12 1, D13 0 | CLOSED 20261005T194433Z |
| N1 | activation | safe-apply the flip plan (0/5/0 code hashes) from C:/tmp/rv-r8 at the flip commit | apply output 0/5/0; before = round-9 live set | 19:45:10-19:46:53Z: HALT_ACK=1 bash .tools/safe-apply.sh -chdir=infra/aws/terraform/etfs-rivalfunds apply C:/tmp/rv_apply20.tfplan from C:/tmp/rv-r8 @35c6b3a923: Apply complete! Resources: 0 added, 5 changed, 0 destroyed; before = the round-9 live set (dMuSFoah, 2XaLTXHM, IHCy7pdV, g+Rb5Ip8, eGMhgbGj) | CLOSED 20261005T194727Z |
| N1v | verify | 5 live CodeSha256 equal the plan; package leg_gates.json D12 1 | get-function-configuration | 19:4xZ: 5/5 live CodeSha256 equal the plan (daily uEUmJ+ny, fetch 9Qn1CeZF, canonical 0BUVdGFS, silver RK3Hk+9t, publish 0GpPs6dP), all Successful; the staged package's leg_gates.json reads D12 1, ENABLE 0, D13 0 | CLOSED 20261005T194727Z |
| I1 | activation | collector import 189 local captures, date 2026-10-02, batch import-d12-idvz-pfoe, sink s3, rebuild_funds IDVZ/PFOE | status OK, 189 captures, marker carries rebuild_funds | 19:48:12-19:49:15Z: collector_bloomberg import on the terminal machine at CLOUD 35c6b3a923 (D12 on in-process): 189 local captures (bronze/holdings only), date 2026-10-02, batch import-d12-idvz-pfoe, sink s3: status OK, 189/189 OK, marker state/fetch_bloomberg/date=2026-10-02/import-d12-idvz-pfoe.json carries rebuild_funds [IDVZ, PFOE]; no Bloomberg request | CLOSED 20261005T194938Z |
| C1 | verify | the batch chain: canonical marker, coverage marker, trade-schedule marker for import-d12-idvz-pfoe | three markers present | the batch import-d12-idvz-pfoe: canonical marker 21:03:00Z after 5 passes (2 sync-equivalent + 3 async; cursor 96 -> 137 -> 174 -> 189 dates), coverage marker, trade-schedule marker status OK, 189 outputs, written_new 189, rows 9,837, held none (REPORT e3f76e49 738.6 s / 796 MB) | CLOSED 20261005T211143Z |
| K1 | verify | served census G1 + G5 per date vs the 19:1xZ snapshot (other funds), 09-30 IDVZ/PFOE source bloomberg | 0 other-fund deltas on pre-existing columns | 21:1xZ: served census vs the 19:1xZ snapshot (C:/tmp/r8measure/census_served.json): 189 report dates; G1 189 rebuilt, 0 dates with any other-fund delta, IDVZ/PFOE +12,798 rows, 0 dates not Bloomberg-sourced (09-30 included); G5 189 rebuilt, 0 other-fund deltas on every column the snapshot carries, IDVZ/PFOE +367 trade rows -- equals the mirror census | CLOSED 20261005T211602Z |
| P1 | activation | invoke only:[publish-page] 2026-10-05 batch rv-publish-1005d12 refresh_a1 true, retries off | response status | 21:16:02-21:17:54Z: invoke {only:[publish-page], date 2026-10-05, batch rv-publish-1005d12, refresh_a1 true}, AWS_MAX_ATTEMPTS=1: 200, no FunctionError, REPORT f717f0cb 107.5 s / 832 MB; status PARTIAL; AI SKIPPED_EXISTS; a1: buying_trend OK, input_census OK, holding_contribution FAILED (AccessDenied s3:ListBucket on gold/security_names -- row Z-S31; fixed forward ca39e20a20, its refresh under its own pair) | CLOSED 20261005T213557Z |
| P1v | verify | served page read back | IDVZ/PFOE latest report 10-02; batch named | 21:2xZ: served platinum/page/date=2026-10-05 read back: batch rv-publish-1005d12 published, 1,884,467 B, data-sec 1957, data-refused 0; funds_not_updated null (IDVZ no longer not-updated); IDVZ panel 'Latest report 2 Oct, BBG'; the IDVZ rankings still read the prior holding_contribution object (window from 2026-08-21) until the Z-S31 refresh | CLOSED 20261005T213558Z |

## Log

- 20261005T194309Z OPENED by 2.0.0_SA_COO~RV with 8 leg(s)
- 20261005T194433Z LEG F1 closed: commit 35c6b3a923: data/etfs/scripts/rivalfunds/leg_gates.json read at HEAD: ENABLE 0, D12 1, D13 0
- 20261005T194727Z LEG N1 closed: 19:45:10-19:46:53Z: HALT_ACK=1 bash .tools/safe-apply.sh -chdir=infra/aws/terraform/etfs-rivalfunds apply C:/tmp/rv_appl
- 20261005T194727Z LEG N1v closed: 19:4xZ: 5/5 live CodeSha256 equal the plan (daily uEUmJ+ny, fetch 9Qn1CeZF, canonical 0BUVdGFS, silver RK3Hk+9t, publish
- 20261005T194938Z LEG I1 closed: 19:48:12-19:49:15Z: collector_bloomberg import on the terminal machine at CLOUD 35c6b3a923 (D12 on in-process): 189 loca
- 20261005T211143Z LEG C1 closed: the batch import-d12-idvz-pfoe: canonical marker 21:03:00Z after 5 passes (2 sync-equivalent + 3 async; cursor 96 -> 137
- 20261005T211602Z LEG K1 closed: 21:1xZ: served census vs the 19:1xZ snapshot (C:/tmp/r8measure/census_served.json): 189 report dates; G1 189 rebuilt, 0 
- 20261005T213557Z LEG P1 closed: 21:16:02-21:17:54Z: invoke {only:[publish-page], date 2026-10-05, batch rv-publish-1005d12, refresh_a1 true}, AWS_MAX_AT
- 20261005T213558Z LEG P1v closed: 21:2xZ: served platinum/page/date=2026-10-05 read back: batch rv-publish-1005d12 published, 1,884,467 B, data-sec 1957, 
- 20261005T213558Z CLOSED -- all 8 legs proven
