# Deploy Completion Record
**Date opened:** 2026-10-17T03:22:49.428276+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261017T042538Z
**Deploy:** FWD-10 (b) Cottonwood carrier re-pull as-of 2026-10-15 (Andrew-direct ~02:4xZ 'do the run now'; CTO half @48c6253f60)
**Authored by:** 4.0.0_SA_CRO~DDD
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| B1 | verify | bronze holdings+allocations re-land as-of 10/15 | carrier values non-null; supervised ~530.42M | SSM 4ec0fe1e (holdings, 03:23Z) + 5f00c984 (allocations, 03:25Z), RunDate 2026-10-16 -> as-of 2026-10-15. Holdings 1,631,221 B (was 1,619,743), nzf 0.650 (was 0.633). READ GATE: re-landed holdings collapsed by Account Supervised = Supervised 530,421,988.14 (BD Dashboard 530,421,988.14, to the cent), Unsupervised 33,137,909.52, all 563,559,897.67 (BD 563,559,898). Allocations 364,670 B (was 342,439). | CLOSED 20261017T032543Z |
| S1 | activation | opal-data-cot silver run + MDPF mirror re-convert | silver 10/15 totals read back; no account_attributes partition written | ADVI silver (opal-data-cot): scoped SSM AWS-RunShellScript dd6fc7f6 03:27Z, cot_silver_merge --table holdings/--table allocations --date 2026-10-15 only (no account_attributes, no --finalize; CTO C-1): RE-LAND reprocessed, holdings 21,510 rows supervised 530,370,482.38. MDPF mirror: opal-assets-ingest-mirror {firm:cot} 03:29Z written 2 verified 2; event path did not re-convert (convert_bd skips existing partitions unless force), so the vendored converter run_event(force=True) 03:34Z run 20261017T033409Z-ca0bb33d converted both; fact_holdings 10/15 supervised 530,421,988.14 (= BD to the cent). | CLOSED 20261017T033500Z |
| G1 | activation | ADVI gold chain | account_performance 10/15 supervised read back | ADVI gold chain opal-cot-gold-run 4040b2a6 03:35:03Z->03:38:33Z Success; account_performance rewritten 03:36:51Z; platinum/firm/header_metrics.json 03:38:30Z total.aua 530,370,482.38, 864 accounts, 225 clients, data_as_of 2026-10-15 | CLOSED 20261017T042538Z |
| M1 | activation | mdpf-gold-lambda production run + publisher | Global + cot model/SMA equal before/after; cot total read | dell1 production run 03:37Z green but all dated 10/15 keys A8-CONFLICT (no write); Global dated keys unchanged (C-2 narrowed to Global by CTO 7248: held). Restatement on Andrew-direct via laptop 0.7.0_AE_CloudOps~MDPF1 (XB-20261017T040845Z-8c16, CTO half @c403b0df70): 4 Cottonwood 10/15 delete markers + gold rerun -> category-views 2026-10-15 rewritten 04:19:13Z total_aua 530,421,988.14; publisher -> opal-data-portal-v2 platinum 04:24Z | CLOSED 20261017T042538Z |
| V1 | verify | served 10/15 Cottonwood total on MDPF and ADVI | served artifacts read | SERVED reads: MDPF opal-data-portal-v2 platinum/mdpf/cottonwood/category-views.json as_of 2026-10-15 sums.total_aua 530,421,988.14 (BD Dashboard Supervised 530,421,988.14) and aggregate-aua-timeseries latest 530,421,988.14, both 04:24Z; ADVI opal-data-cot platinum/firm/header_metrics.json total.aua 530,370,482.38 (-51,505.76 = ADVI silver account+asset_name dedup) | CLOSED 20261017T042538Z |

## Log

- 20261017T032249Z OPENED by 4.0.0_SA_CRO~DDD with 5 leg(s)
- 20261017T032543Z LEG B1 closed: SSM 4ec0fe1e (holdings, 03:23Z) + 5f00c984 (allocations, 03:25Z), RunDate 2026-10-16 -> as-of 2026-10-15. Holdings 1,631
- 20261017T033500Z LEG S1 closed: ADVI silver (opal-data-cot): scoped SSM AWS-RunShellScript dd6fc7f6 03:27Z, cot_silver_merge --table holdings/--table al
- 20261017T042538Z LEG G1 closed: ADVI gold chain opal-cot-gold-run 4040b2a6 03:35:03Z->03:38:33Z Success; account_performance rewritten 03:36:51Z; platin
- 20261017T042538Z LEG M1 closed: dell1 production run 03:37Z green but all dated 10/15 keys A8-CONFLICT (no write); Global dated keys unchanged (C-2 narr
- 20261017T042538Z LEG V1 closed: SERVED reads: MDPF opal-data-portal-v2 platinum/mdpf/cottonwood/category-views.json as_of 2026-10-15 sums.total_aua 530,
- 20261017T042538Z CLOSED -- all 5 legs proven
