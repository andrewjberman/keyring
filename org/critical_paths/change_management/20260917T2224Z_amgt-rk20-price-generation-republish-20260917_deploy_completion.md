# Deploy Completion Record
**Date opened:** 2026-09-17T22:24:35.665406+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260917T223557Z
**Deploy:** AMGT-rk-20: price_axis_pull.py generation-contract wiring + one-time republish of the already-landed 2026-09-15 TRENDING_PRICE#/BREAKOUT_PRICE# rows into a _CURRENT generation. Not a Lambda deploy -- direct boto3 write via backfill_legacy_generation.republish_crossed_generation(). Co-signed CTO 533f216c74 / COO 6b7d4f2341, HALF 1.
**Authored by:** 0.9.0_WK_AMGT_RESAPP~27
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | opal-harvest-security-metrics TRENDING_PRICE#2026-09-15 + BREAKOUT_PRICE#2026-09-15 partitions and _CURRENT pointers | pre/post item counts + pointer state, read live via boto3 | PRE-ACT (live boto3 reads, 2026-09-17T22:2xZ): BREAKOUT_PRICE#2026-09-15 and TRENDING_PRICE#2026-09-15 both had 32 already-landed bare rows, no _CURRENT pointer at either (read_generation_pointer returned None both). Nearest pointer in window, BREAKOUT_PRICE#2026-09-10, state=EMPTY (not COMPLETE) -- correctly never used as a fallback per _find_latest_served_pointer's own rule. read_rankings('BREAKOUT','PRICE',None,20) BEFORE: as_of_date=2026-09-17, dated=False, ranking_status=ABSENT, row_count=0. EXECUTED: python -m lib.research.price.backfill_legacy_generation --republish-crossed --as-of-date 2026-09-15 (rc=0) -- OK: crossed republish [WRITE] as_of=2026-09-15 run_id=R20260917T222502Z rows_ranked=64 rows_written=64; axis=TRENDING_PRICE rows_written=32 state=COMPLETE pointer_written=True generation_id=20260917T222503Z-c35c454d1e4f; axis=BREAKOUT_PRICE rows_written=32 state=COMPLETE pointer_written=True generation_id=20260917T222505Z-45dc4b07af48; pointers_written=2 of 2. POST-ACT live reads: get_item on opal-harvest-security-metrics BREAKOUT_PRICE#2026-09-15/_CURRENT returns pointer_exists=True generation_id=20260917T222505Z-45dc4b07af48 state=COMPLETE (AC2 PASS exactly as specified). read_rankings('BREAKOUT','PRICE',None,20) AFTER: as_of_date=2026-09-15, dated=True (differs from the order's own AC1 <expect> of dated=false; row AMGT_RESAPP-Z-W27-S9 grounds why -- requested_as_of defaults to today 2026-09-17, served date 2026-09-15 differs, dated=true is this reader's own correct contract), ranking_status=SERVED, row_count=20. Discriminator: exactly the two named partitions (TRENDING_PRICE#2026-09-15, BREAKOUT_PRICE#2026-09-15) plus their two _CURRENT pointer items were touched -- no third partition, no relabel to today's date (as_of_date stayed 2026-09-15 throughout), no delete of legacy bare rows, no schedule/alarm/IAM/route change. Not a Terraform resource -- direct boto3 write via republish_crossed_generation(), per the CTO half's own read; no terraform plan/apply for this act. | CLOSED 20260917T223532Z |

## Log

- 20260917T222435Z OPENED by 0.9.0_WK_AMGT_RESAPP~27 with 1 leg(s)
- 20260917T223532Z LEG L1 closed: PRE-ACT (live boto3 reads, 2026-09-17T22:2xZ): BREAKOUT_PRICE#2026-09-15 and TRENDING_PRICE#2026-09-15 both had 32 alrea
- 20260917T223557Z CLOSED -- all 1 legs proven
