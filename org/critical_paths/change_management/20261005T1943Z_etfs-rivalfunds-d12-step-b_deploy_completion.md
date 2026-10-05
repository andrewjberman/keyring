# Deploy Completion Record
**Date opened:** 2026-10-05T19:43:09.436788+00:00
**Status:** OPEN
**Deploy:** ETFS_RIVALS D12 Step B: flip RIVALFUNDS_LEG_D12 in leg_gates.json, deploy it, import the 189 local IDVZ/PFOE captures with rebuild_funds, census, one refresh republish
**Authored by:** 2.0.0_SA_COO~RV
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| F1 | activation | commit leg_gates.json RIVALFUNDS_LEG_D12 0 -> 1 (ENABLE, D13 stay 0) | commit hash + file read back at HEAD |  | OPEN |
| N1 | activation | safe-apply the flip plan (0/5/0 code hashes) from C:/tmp/rv-r8 at the flip commit | apply output 0/5/0; before = round-9 live set |  | OPEN |
| N1v | verify | 5 live CodeSha256 equal the plan; package leg_gates.json D12 1 | get-function-configuration |  | OPEN |
| I1 | activation | collector import 189 local captures, date 2026-10-02, batch import-d12-idvz-pfoe, sink s3, rebuild_funds IDVZ/PFOE | status OK, 189 captures, marker carries rebuild_funds |  | OPEN |
| C1 | verify | the batch chain: canonical marker, coverage marker, trade-schedule marker for import-d12-idvz-pfoe | three markers present |  | OPEN |
| K1 | verify | served census G1 + G5 per date vs the 19:1xZ snapshot (other funds), 09-30 IDVZ/PFOE source bloomberg | 0 other-fund deltas on pre-existing columns |  | OPEN |
| P1 | activation | invoke only:[publish-page] 2026-10-05 batch rv-publish-1005d12 refresh_a1 true, retries off | response status |  | OPEN |
| P1v | verify | served page read back | IDVZ/PFOE latest report 10-02; batch named |  | OPEN |

## Log

- 20261005T194309Z OPENED by 2.0.0_SA_COO~RV with 8 leg(s)
