# Deploy Completion Record
**Date opened:** 2026-10-01T00:43:58.436130+00:00
**Status:** OPEN
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
| L3 | s3-prefix | opal-data-etfs bloomberg/etfs/bronze/holdings/ 937 imported captures (501 IDVZ-group + 436 PFOE-group), raw + sidecar each, 9 date-ordered batches | S3 object counts by prefix + fetch_bloomberg markers |  | OPEN |
| L4 | activation | marker-driven build-bloomberg-silver, G1, G2 (+ replay), G5, G6 and the grouped page via rivalfunds Lambdas | Lambda request ids + S3 object counts by prefix |  | OPEN |
| L5 | git | scheduled_daily_pull.cmd the ONE enabling line inside :rivalfunds_bbg_leg; b-1.AC3 still PASS | commit hash + b-1.AC3 PASS |  | OPEN |
| L6 | verify | d-3.AC1 AC2 AC3 PASS against the served bucket; Terminal state recorded (never a sign-in attempt) | AC RESULT lines |  | OPEN |

## Log

- 20261001T004358Z OPENED by 0.9.0_WK_ETFS_RIVALS~5 with 6 leg(s)
- 20261001T011100Z LEG L1 closed: safe-apply etfs-rivalfunds (HALT_ACK=1, saved plan, 2026-10-01T01:08Z): Apply complete! Resources: 6 added, 9 changed, 0
- 20261001T023210Z LEG L2 closed: G0 map_version 1 landed (request a4ad74d5-58da-4558-8d27-4784e8bb0dfd, map-1.parquet 13 rows, IDVZ and PFOE home_produce
- 20261001T0235Z NOTE (0.9.0_WK_ETFS_RIVALS~5): WOUND DOWN on 2.0.0_SA_COO~RV's word (the fabric reboots); the ledger stays OPEN, L3 to L6 NOT closed. STATE PER KEY (S3 counts read 02:2xZ; every landed object is new, under its own prefix, and nothing was deleted or rolled back because a delete is a human's word in both halves):
  - key 1 Bloomberg bronze: LANDED IN PART, 776 raw + 776 sidecars = import batches 00-06 (captures requested 2024-09-30..2026-06-03); batches 07 (2026-06-04..2026-08-28, 120 files) and 08 (2026-08-31..2026-09-29, 41 files) NOT STARTED.
  - key 2 Bloomberg silver: 2829 objects; batches 00-03 and 06 hold a silver marker; batches 04 and 05 wrote every silver object but NO marker (DeleteObject denied, row ETFS_RIVALS-Z-W5-S24, BLOCKING/ARMED).
  - key 3 G0 1 object (13 rows, home funds home_producer), G3 1 object (4823 rows), G2 120 objects (the daily-window objects only), G6 419: landed; the G2 full-history replay NOT RUN.
  - key 4 G1 745, G5 743, page 12 objects (new revisions only; the 325 / 324 / 6 round-1 objects stand): landed for report dates through 2026-06-03 (IDVZ group); BASG served delta with the imported G3 read 0 (key4_with_g3.json).
  - key 5 markers: fetch_bloomberg 7, build_bloomberg_silver 5, pull_enrichment 1, build_peer_group_map 1, build_coverage 2, build_flow_reconciliation 7: landed.
  - keys 6, 7, 8 (five Lambdas in place, role policies widened, two marker rules): LANDED and verified (safe-apply 6 added 9 changed 0 destroyed).
  - key 9 (the vehicle's one enabling line): NOT APPLIED. Written in the worktree, b-1.AC3 PASS with it, removed unmerged at the wind-down; scheduled_daily_pull.cmd equals HEAD, the leg stays gated OFF. Reason: an enabled leg on a history that stops at 2026-06-03 would pair a new day's G5 against a stale prior report.
  - key 10 (Bloomberg requests from the terminal machine): NOT STARTED; the Terminal read health ok=false (signed out), no sign-in attempted.
  REMAINING: import batches 07 and 08 (d3_act.py chunk 7 / 8 --sink s3); drive gold by marker, or by a replay event on the canonical Lambda when the silver marker is absent (row W5-S24); the G2 full-history replay and the final page (etfs-rivalfunds-daily-lambda only events); disarm row W5-S24 before the daily leg runs; the one enabling line, then b-1.AC3 and d-3.AC1-AC3; then close L3-L6. AC1, AC2, AC3 read FAIL at this stop (776 of >= 900 raws; G2 counts partial; the enabling line unrecorded).
