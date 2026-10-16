# Never-widen half request -- seed 13 old-list tickers into `etf-classifications` (cell SC-e-107, rows D1-S42, D1-W97-S1/S2, D1-W93-S2)

**Author:** `2.0.0_SA_COO~M1`, dell1, 2026-10-16 ~05:1xZ. **Cell:** `SC-e-107` (worker `0.9.0_WK_MDPF_SECCLASS~97`, plan merged @e6c7448985). **Ruling it serves:** CTO round-26 analysis (msg 6482) and the fold ruling
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_MDPF_SECCLASS_SEED22_FOLDS_20261016.md` @1b45af4766. Claim words: `measured` = read this session; `held` = cited from a record.

## What is changed (a data seed; the script is built and selftested, LOCAL on `box/dell1`, nothing written yet)

13 NEW keys in `etf-classifications` (us-east-1), written by `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R27_CHECKS/seed22.py apply --plan <SEED22_PLAN.json> --pair <this pair, signed>` through its own conditional put
(`ConditionExpression='attribute_not_exists(ticker)'`). The plan is `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~97/SEED22_PLAN.json` (13 planned, 9 seed_pending, 0 unresolved; `SEED22-PLAN ok=True`, `SEED22-FOLD ok=True`,
`SEED22-SELFTEST ok=True` 35 of 35; the fold map is `R27_CHECKS/seed22_fold_map_20261016.json`). Every row carries `source_table` = `bd-securities`, `source_last_updated` = the old row's own `last_updated`, `input`, `fold_rule`, `fold_note`, `source_asset_class`,
`source_sub_asset_class`. An old-list class that was set by an outside model (gpt-4o-mini or gpt-5.4-mini, `classified_by` on every old row, measured) is inherited, not re-derived; a later review of any row is a normal row change.

| ticker(s) | canonical class written | rule | dollars (10-09 lots) |
|---|---|---|---|
| AEMGX, CEMVX, FBCVX, FIADX | equity (EM, EM, US Large Cap, International): a direct canonical match from `plan_rows` | legacy-fork | 15,777.17 |
| CUBE, GLPI | alternatives / Real Estate | F1 | 11,855.56 |
| HPI, LCFYX, PFF, VRP, CPXIX | fixed_income, NO sub-class (attribute omitted) | F2 | 120,888.00 |
| EZET | commodities / Commodities | F4 | 18,856.67 |
| HODL | commodities / Commodities (OVERRIDES the old row's alternatives / Volatility: the name says bitcoin ETF) | F5 | 3,151.90 |
| **seeded total** | | | **170,529.30** |

**Held out, NOT written (expected to stay Unclassified; the pair names that as their expected outcome):** DODBX, BALCX, CIMAX (F2), KAMIX, FSNQX, HBLFX, JBAWX, TRRNX (F3), PCEF (F6): 9 tickers, **242,812.29**.

## The act (by a CloudOps lane, after both halves sign)

1. Open a change-management ledger before the act; close it at completion.
2. **Window:** only when no `bd-gold-layer-runner` instance is running, no `gold/trigger-pending.json` waits, outside a fire window, and with the act finished at least 90 minutes before the next scheduled fire (04:00Z nightly, 23:00Z fallback Monday to Saturday). Measured 2026-10-16T05:12Z: the 04:00Z fire's runner (`i-01003b035d2988dfb`) is RUNNING (launched 04:00:47Z); the act waits for its chain to stop.
3. Leg P before the write, in the same shell: `get_item` for the 13 keys (all absent, the precondition), the table's ItemCount (measured 11,362) and the PITR state (measured ENABLED, earliest restorable 2026-09-11), printed into a deliverable.
4. `seed22.py apply` refuses (exit 2, nothing written) when the pair file is absent, the plan's firm is not `49financial`, or any planned ticker already has a row; the conditional put makes a race a refusal, never an overwrite. It prints `SEED22-APPLY written=<n> refused=<m>`; expected `written=13 refused=0`.
5. Nothing else rides the act: no code object, no `lib/`, no other table, no E_18 or dispatch change (that is a LATER pair, after the seed is applied and read).

## Writers of the named property (counted; N printed)

The property: the existence and the `asset_class` / `sub_asset_class` of these 13 keys. Census (HEAD, `git grep` of the table name over `data/ infra/ lib/ scripts/ .tools/`, minus tests and docs): **87 files name the table; 8 code files carry a write verb** against it:
`seed_bd_securities.py`, `seed_canonical_securities.py` (data/black_diamond/scripts/classification), `mdpf-secclass/sector-writer/lambda_function.py`, `_shared/etf_classification_scheduled.py`, `yang_pipeline/label-legacy-classified-by.py`, `seed-etf-classifications.py`, `seed-etf-constituents.py`, `set-instrument-kind.py`.
**N = 8 writer files; 4 can create or alter these keys' class** (`etf_classification_scheduled.py` write, the E_18 route: a conditional put that never overwrites; `seed-etf-classifications.py`, read by the worker: a merge with a pre-read; `seed_canonical_securities.py` and `seed_bd_securities.py`, NOT read for this pair and NOT run by it) and 4 write other attributes (`sector`, `instrument_kind`, `classified_by`, constituents). The act writes only through its own conditional put; the other seven are not invoked.
**NOT measured:** whether any of the four seed scripts is scheduled; the COO half is not signed on a rule unread.

## Blast radius (priced per firm; the table is shared)

- **49financial (Black Diamond tree), D_04 and C_06 readers:** at their next run after the act, the 13 tickers' dollars (170,529.30 on the 10-09 lots; the run's own date differs by that day's prices) leave `Unclassified` for the classes above: equity +15,777.17, alternatives +11,855.56, fixed_income +120,888.00, commodities +22,008.57. The firm total and AUA do not move. The held-out 9 stay in `Unclassified`.
  The served `platinum/firm/mix_summary.json` `Unclassified` was 839,609.78 at data_as_of 2026-10-13 (measured at 03:0xZ).
- **cottonwood:** its canonical holdings of 2026-10-14 hold **one** of the 13, PFF, at 42,628.62 (measured); it moves to fixed_income on cottonwood's classifier at its next run. No other of the 22 is held there.
- **inflection:** no canonical holdings partition was found for it (measured), so no exposure is priced; **NOT measured:** live portal lookups by ticker and the other readers of the table (partners-data lambda etf_classifier, positioning), which read the new rows the moment they exist.
- **Not touched:** every existing key (11,362 keys, unchanged; 13 new keys are added), E_18, `gold_dispatch.sh`, any code object.

## Both branches of the expected outcome

- **Branch 1 (the act's own proof, needs no fire):** after `apply`: the 13 keys exist, each with exactly the ruled `asset_class` and `sub_asset_class` (absent where ruled none), the provenance attributes equal to the old row's `last_updated`; the 9 held-out keys are still absent; the table's ItemCount rises 11,362 -> 11,375 (ItemCount lags; the read is by `get_item` of the 22 keys); no existing key's `last_updated` moved (a sampled census of 200 plus the 22).
- **Branch 2 (the first scheduled fire after the act):** for each firm date C_06 re-derives, the 13 tickers' dollars sit in the ruled classes and not in `Unclassified`; the 9 held-out remain in `Unclassified`; no other ticker's class moves; firm totals equal AUA. A state outside both (a held-out key written, an existing key changed, a seeded ticker in `Unclassified` after the fire) is a STOP; the rollback below.

## Rollback per key

Delete the 13 keys by key (`delete_item`, `ConditionExpression` on `source_table = 'bd-securities'` so an unrelated row is never deleted), listed in the plan; PITR is ENABLED as a second path (a restore makes a new table, so it is for a wider error only). A delete restores behaviour at the next classifier run; it does not restate a served object a fire already wrote (a fire after the delete rewrites them).

## COO half: UNSIGNED

Left for `2.0.0_SA_COO~M1` (signed in the sibling file when the worker's instance is closed and the window is open).

## CTO half: UNSIGNED

Left for `1.0.0_SA_CTO`. Read: the named plan and map only; the 13 / 9 split against your ruling; both branches; the cottonwood price (PFF); the unmeasured readers; the rollback per key.
