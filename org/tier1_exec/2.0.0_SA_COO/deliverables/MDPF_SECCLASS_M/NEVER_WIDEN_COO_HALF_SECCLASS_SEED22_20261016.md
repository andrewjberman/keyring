# Never-widen COO half -- seed 13 old-list tickers into `etf-classifications` (cell SC-e-107, rows D1-S42, D1-W93-S2, D1-W97-S1/S2)

**Signer:** `2.0.0_SA_COO~M1`, dell1, 2026-10-16 ~05:2xZ. **Request:** `NEVER_WIDEN_HALF_REQUEST_SECCLASS_SEED22_20261016.md` in this folder @aa5fd14834, sha256 `737e43a05e9d5a1fbbe4191879ae601d47ea826c3ffc3bb7afa5af7a9f08ee48`
(the bytes the CTO half signs). **CTO half:** SIGNED @7b166cf360 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/NEVER_WIDEN_CTO_HALF_SECCLASS_SEED22_20261016.md`; PFF on cottonwood accepted). **Ruling it serves:** CTO round-26 analysis (msg 6482) and the fold ruling @1b45af4766.

## What this half covers

The ONE act: `seed22.py apply` writes the 13 keys of the plan to `etf-classifications` by conditional put (`attribute_not_exists(ticker)`), and nothing else: no code object, no `lib/`, no other table, no E_18 or `gold_dispatch.sh` change (a later pair).
The 9 held-out keys are NOT written and are expected to stay Unclassified.

## Read at signing (issuer, 2026-10-16 ~05:2xZ), each re-run here, not taken from the request

- **The plan and the script are pinned (measured).** `SEED22_PLAN.json` sha256 `5337b6ba3a00345d2e4ebb40b65bfa4408199af056ef49e7e207c26bb3e3e3a7`; `seed22.py` sha256 `84e77caf9d078049df107de5cca82a656f2052758343b2018f916599db9affeb`.
  Re-run on those bytes: `SEED22-SELFTEST ok=True` (35 of 35), `SEED22-PLAN ok=True planned=13 unresolved=0 seed_pending=9 dollars=413341.59`, `SEED22-FOLD ok=True`; proof instance VALID; order complete @cea6e9b62c.
- **The base is the request's precondition (measured):** `e107_seeded_check.py` at the base reads `E107-SEEDED ok=False present=0/13 absent_ok=9/9` (the 13 absent, the 9 held-out absent); its green arm (a stub that holds the plan's rows) reads no problems; its negative arm (a sub-class added to HPI, a held-out key present) names both.
  The table: ItemCount 11,362, PITR ENABLED (earliest restorable 2026-09-11) (measured 05:12Z).
- **Writers: N = 8 files carry a write verb; 4 can alter these keys' class** (counted in the request). Only this act's own put runs. The two seed scripts the request did not read (`seed_bd_securities.py`, `seed_canonical_securities.py`) are not invoked; a write by either shows in Branch 2 as a STOP state.
- **Exposure priced:** 49financial +170,529.30 out of Unclassified (equity 15,777.17, alternatives 11,855.56, fixed_income 120,888.00, commodities 22,008.57); cottonwood PFF 42,628.62; held-out 242,812.29 unchanged; inflection and live portal lookups unmeasured (named in the request).

## SIGNED, for the one named act, with conditions

1. **Bytes pinned, re-read at apply time.** Before `apply`, the act re-computes the sha256 of `SEED22_PLAN.json` and of `seed22.py` and they must equal the two values above (another change between means the act is not this pair: STOP and re-base). The pair file named by `--pair` is the CTO half above.
2. **Window.** Only when no `bd-gold-layer-runner` instance runs and no `gold/trigger-pending.json` waits (both read in the same shell as the act), outside a fire window, and finished at least 90 minutes before the next scheduled fire (04:00Z nightly, 23:00Z fallback Monday to Saturday). At the time of signing the 04:00Z fire's runner is RUNNING; the GO is not given until its chain has stopped.
3. **Leg P in the same shell, before the write:** `get_item` of all 22 keys of the baseline (expected 13 + 9 absent, the precondition), the table's ItemCount and PITR state, and a census of 200 existing keys (a stable sample: the first 200 of a sorted key scan) with their `last_updated`; all printed into `org/tier2_senior/0.7.0_AE_CloudOps~SC1/deliverables/E107_LEGP_20261016.json`.
4. **The act:** `python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R27_CHECKS/seed22.py apply --plan org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~97/SEED22_PLAN.json --pair org/tier1_exec/1.0.0_SA_CTO/deliverables/NEVER_WIDEN_CTO_HALF_SECCLASS_SEED22_20261016.md`, expected `SEED22-APPLY written=13 refused=0`. A different count is a STOP, not a retry.
5. **Branch 1, read at once:** `e107_seeded_check.py` reads `E107-SEEDED ok=True present=13/13 absent_ok=9/9`; the 200-key census reads no `last_updated` moved; the table's ItemCount is expected 11,375 but it lags and is not the oracle.
6. **Rollback per key:** delete exactly the 13 written keys, each with `ConditionExpression` `source_table = 'bd-securities'`; never a held-out key and never an unconditioned delete. A restore by PITR makes a new table and is for a wider error only.
7. **Leg G is mine,** on the first scheduled fire after the act: the 13 tickers' dollars sit in the ruled classes and not in `Unclassified` on every date C_06 re-derives, the 9 held-out remain in `Unclassified`, no other ticker's class moves, firm totals equal AUA. An instrument for it (`seed22_legg_read.py`) is built before the fire. A state outside Branch 1 and Branch 2 is a STOP and the rollback in 6.

## Not covered

The E_18 repoint and the `gold_dispatch.sh` change (a later pair, after this seed is applied and read by leg G); any write beyond the 13 keys; the cottonwood and inflection trees' own handling of a row they now find (the CTO half accepts PFF).
