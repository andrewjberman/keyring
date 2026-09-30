# Deploy Completion Record
**Date opened:** 2026-09-30T14:37:34.935239+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260930T161408Z
**Deploy:** Ship lib/silver_ids.py flat to code/silver/ and the fallback import; one real INF gold chain run
**Authored by:** 0.9.0_WK_IRPT_BCKEND~97
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U1 | verify | the two readings + collision census | readings deliverable written, every collision probe 404 | RESOLUTION_READINGS.json @2e5173d3b6: sync_layout, deployed_dispatch (sha equal to repo d6b00f6fdd75), sys_path_reading; 7 collision probes all HTTP 404 | CLOSED 20260930T144236Z |
| D1 | activation | code/silver/silver_ids.py + code/silver/_orion_api_silver_lib.py | sha256 of each S3 object equals the committed file | s3://opal-data-inf/code/silver/silver_ids.py sha256 d04e4920e606 == lib/silver_ids.py; s3://opal-data-inf/code/silver/_orion_api_silver_lib.py sha256 ed85e079a550 == committed file (aws s3 cp; safe-deploy HALT-GATE refused, recorded in readings) | CLOSED 20260930T145031Z |
| R1 | verify | one real full chain run | status.json newer run, SILVER_REPS ok, PULL_POSITIONS_DAILY ok, raw jsonl.gz for the run date | chain_full_20260930_145412: SILVER_REPS ok, PULL_POSITIONS_DAILY ok, bronze/positions/2026-09-30.jsonl.gz 2309545B at 2026-09-30T15:18:55Z; P26-1-AC2 PASS; chain later failed at INF_C_01 (NNA coverage guard, separate row W97-S3) | CLOSED 20260930T161408Z |

## Log

- 20260930T143734Z OPENED by 0.9.0_WK_IRPT_BCKEND~97 with 3 leg(s)
- 20260930T144236Z LEG U1 closed: RESOLUTION_READINGS.json @2e5173d3b6: sync_layout, deployed_dispatch (sha equal to repo d6b00f6fdd75), sys_path_reading;
- 20260930T145031Z LEG D1 closed: s3://opal-data-inf/code/silver/silver_ids.py sha256 d04e4920e606 == lib/silver_ids.py; s3://opal-data-inf/code/silver/_o
- 20260930T161408Z LEG R1 closed: chain_full_20260930_145412: SILVER_REPS ok, PULL_POSITIONS_DAILY ok, bronze/positions/2026-09-30.jsonl.gz 2309545B at 20
- 20260930T161408Z CLOSED -- all 3 legs proven
