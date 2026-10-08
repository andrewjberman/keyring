# Deploy Completion Record
**Date opened:** 2026-10-08T03:12:34.303649+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261008T113749Z
**Deploy:** MDPF_SECCLASS SC-e-68: the canonical CASH row fixed_income/Ultra Short Duration -> cash/Cash (one conditional update on etf-classifications)
**Authored by:** 2.0.0_SA_COO~M1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | cash_row_write.py --write --snapshot (one update_item on CASH, conditional on classified_by legacy and the current class) | WROTE line + post-read of the three attributes | WROTE 1 of 1, condition failures 0, at ~03:12:5xZ; pre-write dry run CASH-ROW-DRY-RUN write=1 current=fixed_income/Ultra Short Duration classified_by=legacy puts=0; snapshot CASH_ROW_SNAPSHOT_20261008.json taken 03:12:55Z first. POST-READ (ConsistentRead): exactly three attributes moved -- asset_class fixed_income->cash, sub_asset_class Ultra Short Duration->Cash, updated_by seed-etf-constituents...->mdpf-secclass-cash-row-r12; classified_by legacy, last_updated, management_style, name 'Cash & Cash Equivalents', ticker all equal the snapshot (CTO condition 2). Rollback: cash_row_write.py --rollback <snapshot> --write | CLOSED 20261008T031318Z |
| L2 | verify | first BD-family gold run after the write: Cottonwood mix total unchanged with CASH in cash (CTO condition 3; a laptop seat reads the cottonwood bucket) | the run id and the mix read | graded by 2.0.0_SA_COO~M1 on dell1 under CTO half amendment 3 @555db9c729 with R12_CHECKS/e68_cottonwood_grade.py @fb1f8e00a6 at 2026-10-08T11:37Z: E68-GRADE verdict=PASS. (a) opal-data-cot platinum/firm/mix_summary.json rebuilt 2026-10-08T11:36:44Z VersionId PpccM9D04LALkcC0bJF6hIVAPUQjBw8s data_as_of 2026-10-07 (prior eH1ZuCUJ..., 10-07T11:39:50Z); (b) 221 of 226 client compositions rebuilt after 03:12:55Z, 208 list key CASH, 0 non-cash, CASH market value 2,989,603.24 all in cash; (c) mix market values sum 566,255,064.72 = composition.total_market_value 566,255,064.72. Control on the pre-write bytes read NOT-YET at 11:36:43Z. Row MDPF_SECCLASS-D1-S6 records that COT already served CASH as cash before the write. | CLOSED 20261008T113749Z |

## Log

- 20261008T031234Z OPENED by 2.0.0_SA_COO~M1 with 2 leg(s)
- 20261008T031318Z LEG L1 closed: WROTE 1 of 1, condition failures 0, at ~03:12:5xZ; pre-write dry run CASH-ROW-DRY-RUN write=1 current=fixed_income/Ultra
- 20261008T031318Z HELD-SOVEREIGN-GATED gate=external/the first BD-family gold run after 03:12Z: Cottonwood's mix total unchanged with
- 20261008T051538Z HELD-SOVEREIGN-GATED gate=external/the first Cottonwood mix rebuild after 03:12:55Z: cot-bd-session-trigger on i-06
- 20261008T113748Z HOLD RELEASED -> OPEN
- 20261008T113749Z LEG L2 closed: graded by 2.0.0_SA_COO~M1 on dell1 under CTO half amendment 3 @555db9c729 with R12_CHECKS/e68_cottonwood_grade.py @fb1f8
- 20261008T113749Z CLOSED -- all 2 legs proven
