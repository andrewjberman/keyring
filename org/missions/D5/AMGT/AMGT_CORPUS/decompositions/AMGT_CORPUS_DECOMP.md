# AMGT_CORPUS -- L5 decomposition v34.0 -- ROUND 34 (FWD-22 + FWD-20's V3 set + earnings dates + long name: ONE daily scripted pull)

**Issuer:** `2.0.0_SA_COO~X`, 2026-10-03 ~21:xxZ.

**Source:**
- `1.0.0_SA_CTO~Z` round-33 analysis `ledger/ROUND_ANALYSIS.round33.md` @`e55e3b5152` s.2: "The first word that lands is cut as
  round 34 the same tick: FWD-22 is a scripted, deterministic producer on the terminal box, with the A.4 limits binding; if the
  word covers V3 and the earnings fields, they ride the same producer from its first run."
- The word: Andrew-direct 2026-10-03 ~20:3xZ, verbatim "yes to all recommendations", record
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261003_20xxZ_YES_TO_ALL_SEVEN_OPEN_CALL_RECS.md` @`9fe6e6f111`,
  card 3: "CORPUS: a daily Bloomberg re-pull with earnings dates, the V3 fields and a long-name field -- yes, one daily pull for all
  of it ... this record is the per-use vendor word". Relay: `1.0.0_SA_CTO~Z` msg 29002 (READ-acked).
- PRD v0.7 `C-NO-VENDOR-CALL` (B.2): on that word, the Model-block pull of every name with a block may recur on a schedule, from a
  SCRIPTED DETERMINISTIC PRODUCER on the terminal box; A.4 limits 1 (an agent turn is not a producer) and 2 bind.
- Round 33's decomposition is kept as `AMGT_CORPUS_DECOMP.round33.md`. Base: CLOUD `6527a03cc1`.

## 0. What this round IS

| # | item | cell | path | risk |
|---|---|---|---|---|
| 1 | The producer: a `refresh` stage that re-pulls every registered name WITH a block, the V3 set + the long name + the earnings dates in its request, and the scheduled entry running it after `admit` | `CRPS-aj-1` | worker `0.9.0_WK_AMGT_CORPUS~1` | LOCAL |
| 2 | The served act: re-pin `amgt-induction-daily` to the merged commit, fire its own trigger on demand, rebuild the unit map for the new mnemonics, re-derive, verify every block's as_of | `CRPS-aj-2` | the issuer's paired act after aj-1 drains | WORLD |

One chain, `aj-1 -> aj-2` (aj-2 runs the code aj-1 lands). Write sets are disjoint:
- aj-1: `integrations/bloomberg/research/model_block_pull.py`, one new test file beside it, `lib/research/corpus/induction_scheduled.py`;
- aj-2: the Scheduled Task's pinned checkout, `field_map.json`, the served blocks, the ledger entry.

## 1. The cells

**CRPS-aj-1 (the producer).** Serves FWD-22 and FWD-20; supplies RESAPP FWD-37's earnings dates (fold ruling 8 @`82d1cb21e2`).
- **The V3 set, measured at the cut:** `python -m lib.research.corpus.typecast --read-latest` (workbooks_read 158, with_mnemonics
  120, mnemonic_core 96) minus the producer's HEADER+HIST+FORECAST union at the base (66 fields, 46 of the core) = 50, less
  `BEST_FPERIOD_OVERRIDE` (an override parameter, already the forecast request's override) = **49**. This is the brief's "96 core,
  46 pulled, 49 real gaps" (`docs/briefs/amgt-security-analysis-friday-demo-brief-20261001.md` IV.1), reproduced.
- **Placement:** `BEST_CPS` -> FORECAST_FIELDS; `SHORT_NAME`, `COUNTRY_FULL_NAME`, `AVG_DAILY_VALUE_TRADED_3M`,
  `CRNCY_ADJ_MKT_CAP` -> HEADER_FIELDS; the other 44 -> HIST_FIELDS (yearly, as the team's BDH template calls them). The long
  name `LONG_COMP_NAME` and the earnings dates `EXPECTED_REPORT_DT` (next) and `ERN_ANN_DT_AND_PER` (history, a BULK field) ->
  HEADER_FIELDS. Every addition is APPENDED; no base member moves.
- **A field Bloomberg refuses is a refusal, never a guess:** the existing `__field_errors__` -> `unresolved` path carries it with
  Bloomberg's own text. A wrong request type surfaces on the first scripted run and is the next round's repair.
- **refresh:** population = registered names that HAVE a `derived/model_block/<key>/` object; skip a name whose latest block was
  derived today (UTC), counted `already_current`; batches of at most 3; unreachable DAPI -> REFUSED rc 4.
- **The scheduled entry** runs `refresh` after `admit` and announces `induction_scheduled step model_block_refresh rc <n>`.
- Checks (the issuer's files, `deliverables/2.0.0_SA_COO~X/checks/round34/`), at the base: `aj1_check.py` build 0/5, control
  3/3; `aj1_refresh_dry.sh` FAIL (no stage); `aj1_sched_dry.sh` FAIL (no step line) -- all as expected.

**CRPS-aj-2 (the issuer's paired served act).** After aj-1 drains to CLOUD:
1. The never-widen pair: COO half signed here, CTO half owed by `1.0.0_SA_CTO~Z`. The blast radius is the Scheduled Task's pin, one
   new raw stamp and one new derived stamp per name (write-once keys), and `field_map.json`'s new entries. Rollback per key: re-pin
   to `33c1d096a343`; the reader serves the prior stamp.
2. One NEVER-2 entry, slug `amgt-corpus-r34-aj2`, sentinel committed after each leg close.
3. Legs: `schedule_induction.ps1 -Plan -Commit <merge>` -> `-Register -Commit <merge>` -> fire the task's own trigger on demand
   (`schtasks /run /tn amgt-induction-daily`) -> read the run log (`refresh population ... pulled <K> bloomberg_calls <c>`) ->
   rebuild the unit map for the new mnemonics through `build_unit_map.py` (dry run first, the moved entries printed) -> re-derive
   -> verify: every block's latest stamp is the run's UTC date, denominator printed; the field errors of the new mnemonics
   censused.
4. FWD-22's acceptance is the NEXT scheduled fire (13:00Z), read the day after.

## 2. Found at the cut (rows, not cells)

- `AMGT_CORPUS-Z-S84` (OBSERVATION): in `--mode dry-run` the scheduled entry's admit step reads rc 1 at the base --
  `induction_run`'s dry run poisons `boto3.client`, and admit's S3 read trips it. The fire path is not poisoned. `aj1_sched_dry.sh`
  grades the refresh step's placement, not its dry-run rc.

## 3. Coverage

| cell | order | slot |
|---|---|---|
| CRPS-aj-1 | `AMGT_CORPUS.TO-CRPS-aj-1.daily-refresh-producer.md` | `~1` |
| CRPS-aj-2 | the issuer's paired act (no order) | -- |
