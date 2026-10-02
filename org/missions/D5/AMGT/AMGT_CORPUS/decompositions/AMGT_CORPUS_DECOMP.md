# AMGT_CORPUS -- L5 decomposition v32.0 -- ROUND 32 (the round-31 carried list: two LOCAL direct acts and one paired SERVED act)

**Issuer:** `2.0.0_SA_COO~X`, 2026-10-02 ~15:0xZ.

**Source:**
- `1.0.0_SA_CTO~Z` RULED msg 28540 (READ-acked 14:49Z). Ruling 1: round-31 ruling 1's "until after Friday" ended with the demo,
  so cut round 32 this tick: (1) Z-S74, LOCAL; (2) the BEST_DIV_YLD label DECIMAL -> PERCENT, SERVED, which brings its
  never-widen half to this seat. FWD-20 and FWD-22 stay on Andrew's word. Ruling 2: Z-W4-S6's Peers lookup is RESAPP's
  (2.0.0_SA_COO~Z, round 63/64); there is no CORPUS path grant.
- The rectangle is round-31 analysis `ledger/ROUND_ANALYSIS.round31.md` @`85df450e8d` s.3, less the two items held on Andrew's
  word.
- Round 31's decomposition is kept as `AMGT_CORPUS_DECOMP.round31.md`. Base: CLOUD `1c50edaa81`.

## 0. What this round IS

| # | item | cell | path | risk |
|---|---|---|---|---|
| 1 | Z-S74: the provenance validator and print renderer read `UNRESOLVED-ON-` and `ZERO-DOMINATED` unit/sign texts as NOT measured | `CRPS-ah-1` | **DIRECT ACT** | LOCAL |
| 2 | BEST_DIV_YLD under 0.3 is decided by the same-name identity `BEST_DPS / PX_LAST x 100`, not by magnitude | `CRPS-ah-2` | **DIRECT ACT** | LOCAL |
| 3 | The map rebuild carrying ah-2, and ONE re-derive of each block whose BEST_DIV_YLD unit moves (dry run first) | `CRPS-ah-3` | the issuer's paired act after ah-2 | SERVED |

Chains: `ah-1` (alone) and `ah-2 -> ah-3` (ah-3 consumes ah-2's map). Write sets are disjoint:
- ah-1: `lib/research/provenance/`;
- ah-2: `integrations/bloomberg/research/build_unit_map.py` and its test;
- ah-3: `field_map.json`, the served blocks and the dossiers.

## 1. The cells

**CRPS-ah-1 (Z-S74).**
- The defect: `lib/research/provenance/validate.py:32` (`derive_unit_status`), `:39` (`derive_sign_status`) and
  `render_print.py:208` / `:289` mark a unit unmeasured only when it is empty or starts with the retired pointer `SEE
  field_map.json`.
- Measured over the 100 served blocks (37,746 figures), read 14:5xZ: 11 units (10 `ZERO-DOMINATED: ...`, 1
  `UNRESOLVED-ON-...`) and 11 signs (`UNRESOLVED-ON-...`) read MEASURED.
- After the act, all four predicates read those prefixes as not measured. The 37,735 other units stay MEASURED.
- Check: `checks/round32/ah1_check.py`. At base: build 0/4, control 5/5 (as expected). The act must reach build 4/4, control 5/5.
- Off the served path: `scoped_amgt.py` imports only the overlay functions from `render_print`, per the round-27 pair.

**CRPS-ah-2 (the BEST_DIV_YLD label).**
- The defect: `build_unit_map.classify_unit`'s percent family labels any |value| < 0.3 `DECIMAL (differs from CRO's PERCENT
  reading on SAP)`. Measured: 12 BEST_DIV_YLD figures on BA, GOOGL, HEI and PWR, against 270 PERCENT. Z-S76 showed BA's values
  ARE percent: 0.005 / 196.8 x 100 reproduces them.
- The rule, BEST_DIV_YLD only, |value| < 0.3:
  - The same name's 1FY `BEST_DPS` and `PX_LAST` decide, on a same-currency read (`CRNCY == EQY_FUND_CRNCY`, both stated).
  - `|v| ~= DPS / PX x 100` within `RECONCILE_TOLERANCE` -> PERCENT. `|v| ~= DPS / PX` -> DECIMAL (the existing label).
  - Anything else -> UNRESOLVED with the cause named.
  - An exact zero stays with `unit_from_basis_zero`. |value| >= 0.3 is unchanged. No other mnemonic moves.
- Check: `checks/round32/ah2_check.py`. At base: build 0/4, control 4/4 (as expected). The act must reach build 4/4, control 4/4,
  with the build_unit_map test files green.

**CRPS-ah-3 (the paired SERVED act).** After ah-2 lands:
1. A serializing dry run over every served key: a TEMP map plus `stage_derive` with a write-capturing client, printing every
   moved map entry and every (from, to) transition.
2. The COO half, signed here, and the CTO half, owed by `1.0.0_SA_CTO~Z`.
3. One NEVER-2 entry, slug `amgt-corpus-r32-ah3`, with the sentinel committed after every leg close.
4. Legs: gate -> map -> blocks -> dossiers -> verify.

The expected reach is 4 blocks (BA, GOOGL, HEI and PWR) and 0 value moves. The dry run, never this line, is the number signed.

## 2. Found at the cut (rows, not cells)

- **The same magnitude rule labels 92 served figures DECIMAL across 8 percent-family mnemonics.**
  - BEST_DIV_YLD (12) is this round's item.
  - The others are outside the CTO's ruling: EQY_DVD_YLD_IND (16, on GOOGL, HEI, MELI and PWR), RETURN_ON_INV_CAPITAL (20),
    RETURN_ON_ASSET, RETURN_COM_EQY, RETURN_ON_TANGIBLE_ASSETS and OPER_MARGIN (10 each), and SI_PERCENT_EQUITY_FLOAT (4).
  - Filed as a row for the round-32 analysis; nothing is cut for them here.
- **Z-W4-S6:** routed to RESAPP by ruling 2 (row Z-S79 carries the measurement).

## 5. Close

- `fanout: 0 worker chains of 2, cap 3, reason: ah-1 and ah-2 are each one LOCAL cell under the size floor (the issuer's direct acts); ah-3 is the issuer's paired act and spawns no worker.`
- `checks: ah1 base: build FAIL 0/4 + control PASS 5/5 as expected; ah2 base: build FAIL 0/4 + control PASS 4/4 as expected.`
- **Real run:**
  - ah-1: its census over the 100 served blocks (the 11 + 11 move to UNRESOLVED; the other 37,735 units stay MEASURED).
  - ah-3: the served blocks re-read, and BA's Model tab on 5174.
- The L8 packet then goes to `3.0.0_SA_CVO~Z`.
