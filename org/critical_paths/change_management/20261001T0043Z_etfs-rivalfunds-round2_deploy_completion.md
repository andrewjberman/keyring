# Deploy Completion Record
**Date opened:** 2026-10-01T00:43:58.436130+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261001T044936Z
**Deploy:** ETFS_RIVALS round-2 live join (RIV-d-3): etfs-rivalfunds in-place deploy, G0, G3 + Bloomberg capture import, vehicle leg enabled, fire, read
**Authored by:** 0.9.0_WK_ETFS_RIVALS~5
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 8.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | safe-apply infra/aws/terraform/etfs-rivalfunds (5 Lambdas source_code_hash in place, 5 role policies widened, 2 new marker rules + targets + permissions; no destroy) | apply output: Apply complete, 0 destroyed, plan in-place or create-only | safe-apply etfs-rivalfunds (HALT_ACK=1, saved plan, 2026-10-01T01:08Z): Apply complete! Resources: 6 added, 9 changed, 0 destroyed. Plan = 5 aws_lambda_function in place (source_code_hash), 4 aws_iam_role_policy in place, 2 event rules + 2 targets + 2 permissions create-only; code pin 96ba9a72ab; naming-plan-gate PASS 29 graded; tag-authz and tombstone gates clean | CLOSED 20261001T011100Z |
| L2 | activation | G0 map_version 1 (home funds home_producer) + G3 import of dividends.json (G3 BEFORE any G5, row W3-S13) + key-4 served delta re-run WITH the imported G3 (CTO condition) before G5 writes | G0 object + G3 marker + key4_with_g3.json read | G0 map_version 1 landed (request a4ad74d5-58da-4558-8d27-4784e8bb0dfd, map-1.parquet 13 rows, IDVZ and PFOE home_producer); G3 import landed (actions-20260930-95af6e3d1a1c.parquet 4823 rows, marker import-r2-g3); key4_served_delta.py --with-g3 PASS before any G5 write: G1 0 of 325 fund-dates differ, only gold_version; G5 837=837 added 0 removed 0 every class 0 incl other, only corporate_actions_applied/dividends_applied/inference_version | CLOSED 20261001T023210Z |
| L3 | s3-prefix | opal-data-etfs bloomberg/etfs/bronze/holdings/ 937 imported captures (501 IDVZ-group + 436 PFOE-group), raw + sidecar each, 9 date-ordered batches | S3 object counts by prefix + fetch_bloomberg markers | bloomberg/etfs/bronze/holdings/: 937 raw + 937 sidecars (d-3.AC1: 'bloomberg bronze: 937 raw, 937 sidecars'); import batches 00-08, fetch_bloomberg markers 9 (import-r2-07 and import-r2-08 landed 2026-10-01 04:14Z and 04:20Z); counts in d3_live.json s3_prefixes | CLOSED 20261001T044909Z |
| L4 | activation | marker-driven build-bloomberg-silver, G1, G2 (+ replay), G5, G6 and the grouped page via rivalfunds Lambdas | Lambda request ids + S3 object counts by prefix | marker-driven chain for batches 07 and 08 on the live code (apply 04:10Z, 0 added 5 changed 0 destroyed): build_bloomberg_silver markers import-r2-07 04:16:06Z, import-r2-08 04:20:54Z; canonical, trade_schedule, build_flow_reconciliation markers followed; G2 full-history replay request ece72210-033a-4089-9541-1d67653f52bd (501 objects); page republished request 97a8dc31-b6d5-46a4-926d-d568ca064643 (revision 20261001T043113Z, grouped). prefix counts: G1 827, G2 501, G5 825, G6 501, page 16, bloomberg silver 3610 (d3_live.json) | CLOSED 20261001T044909Z |
| L5 | git | scheduled_daily_pull.cmd the ONE enabling line inside :rivalfunds_bbg_leg; b-1.AC3 still PASS | commit hash + b-1.AC3 PASS | commit 878746ee3e (scheduled_daily_pull.cmd +1/-0: set "RIVALFUNDS_BBG_LEG=1" at the head of the leg gate); b-1.AC3 RESULT: PASS 0 failures after it | CLOSED 20261001T044909Z |
| L6 | verify | d-3.AC1 AC2 AC3 PASS against the served bucket; Terminal state recorded (never a sign-in attempt) | AC RESULT lines | d-3.AC1 RESULT: PASS 0 failures; d-3.AC2 RESULT: PASS 0 failures; d-3.AC3 RESULT: PASS 0 failures (run 2026-10-01 ~04:4xZ after the enabling line and d3_live.json). Terminal state: NOT re-read this session (order bars any Bloomberg request and sign-in); last read ok=false at 2026-09-30 20:08 ET (gate 4 in d3_live.json); the first live 08:03 fetch waits on Andrew's sign-in | CLOSED 20261001T044909Z |

## Log

- 20261001T004358Z OPENED by 0.9.0_WK_ETFS_RIVALS~5 with 6 leg(s)
- 20261001T011100Z LEG L1 closed: safe-apply etfs-rivalfunds (HALT_ACK=1, saved plan, 2026-10-01T01:08Z): Apply complete! Resources: 6 added, 9 changed, 0
- 20261001T023210Z LEG L2 closed: G0 map_version 1 landed (request a4ad74d5-58da-4558-8d27-4784e8bb0dfd, map-1.parquet 13 rows, IDVZ and PFOE home_produce
- 20261001T044909Z LEG L3 closed: bloomberg/etfs/bronze/holdings/: 937 raw + 937 sidecars (d-3.AC1: 'bloomberg bronze: 937 raw, 937 sidecars'); import bat
- 20261001T044909Z LEG L4 closed: marker-driven chain for batches 07 and 08 on the live code (apply 04:10Z, 0 added 5 changed 0 destroyed): build_bloomber
- 20261001T044909Z LEG L5 closed: commit 878746ee3e (scheduled_daily_pull.cmd +1/-0: set "RIVALFUNDS_BBG_LEG=1" at the head of the leg gate); b-1.AC3 RESU
- 20261001T044909Z LEG L6 closed: d-3.AC1 RESULT: PASS 0 failures; d-3.AC2 RESULT: PASS 0 failures; d-3.AC3 RESULT: PASS 0 failures (run 2026-10-01 ~04:4x
- 20261001T044936Z CLOSED -- all 6 legs proven
