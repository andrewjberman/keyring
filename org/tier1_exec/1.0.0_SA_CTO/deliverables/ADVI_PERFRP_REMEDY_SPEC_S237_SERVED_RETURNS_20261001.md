# ADVI_PERFRP -- remedy spec for the wrong 49 Financial returns on the advisor page (rows IRPT_BCKEND-S237, S239, W100-S2)

**Author:** `1.0.0_SA_CTO`, 2026-10-01 ~04:2xZ. **Status: SPEC ONLY. Nothing is cut and nothing is served.** The cell is cut by base
`2.0.0_SA_COO` (decision `CTO_DECISION_20261001_034xZ_S237_PERFRP_REMEDY_ROUTE.md` @8729d9792c) once Andrew lifts the D2 hold he
set by name (`org/ref/LIVE_ARMS.md`, Holds). On that word this file becomes the PRD addendum for the cell, unchanged.

## 1. The defect, in one paragraph

On 2025-01-09 the exchange was closed and the custodian still posted money. The retiring return engine (`c02`) reads one day's
flows per trading day, so every external flow dated 2025-01-09 is left out of the 2025-01-10 calculation while its value is in the
ending balance. A deposit reads as a gain and a withdrawal as a loss. `perfrp_emit_core.py` enumerates trading days, never loads
the 2025-01-09 partition, and links the bad day into every window that spans it.

## 2. What is measured

| fact | value | read by |
|---|---|---|
| the served object | `s3://opal-data-portal-v2/platinum/advi/49financial/perfrp_performance_account.json`, ONE version `E78kI4KB4KsZhdwsAFzfSvkI.kn5Snim`, 2026-09-01T03:16:07Z, 1,923,593 bytes | this seat, `list-object-versions`, 04:2xZ |
| served perfrp leaves at 49 Financial | 4, one version each: `perfrp_performance_account`, `perfrp_gainloss_account`, `perfrp_gainloss_relationship`, `perfrp_book_advisor` | same read |
| it is served | HTTP 200 three times (09-26, 09-28, 09-30), two clients, in 152,160 access-log lines | `2.0.0_SA_COO~P` @abc3f0991c |
| the leaf's population | 8,632 entries: 7,620 COMPUTED_PARTIAL, 997 NOT_COMPUTED_INPUTS_PRESENT, 15 NOT_COMPUTED_INPUTS_ABSENT | worker ~100, `S237_BLAST_RADIUS.json` |
| four accounts probed, since-inception | 0093614544 +69.81% vs +8.47%; 0063952925 +99.79% vs +4.54%; 0027256463 -83.34% vs +28.47%; 0036184450 -12.75% vs +28.06% (served vs counterfactual) | worker ~100, `perfrp_si_counterfactual.json` |
| accounts with a 2025-01-09 flow in `twr_daily` | 44 | row S237 (`0.4.0_DS_ClientPlatform~S`) |
| **is 2025-01-09 the only such day?** | **Yes at partition grain.** Window 2024-07-08..2026-09-01: 786 calendar days, 541 trading days, 245 non-trading days (21 of them weekdays). `flow_ledger` holds a partition on exactly 1 of the 245: 2025-01-09. `twr_daily` the same. Positive control: 2025-01-10 present in both. | this seat, 04:2xZ, partition listing minus `lib/trading_calendar.py` |

**Not measured:** flows whose ROW date is a closed day but which sit inside a trading day's partition (the listing sees partitions,
not rows); which of the 44 accounts carry a figure in the leaf (4 of 44 probed); whether `perfrp_book_advisor.json` and the two
gain/loss leaves take any input from the affected returns; who published the four leaves on 2026-09-01 and under which word (the
project record of 2026-08-31 says no perfrp key is served under the build-only cap).

## 3. The remedy, ruled

1. **The engine is not patched** (round-26 ruling 4 stands). `c02` is retired for Investor Reporting and is replaced for every firm
   by the dashboard project's `account_return_daily`; a second flow rule in `c02` would be a second path for a figure on its way out.
2. **The leaf stops carrying a figure it cannot support.** For every account with an external flow in the 2025-01-09 partition,
   every window that spans 2025-01-10 is emitted with NO return and the leaf's existing not-computed state, with the reason in the
   field the leaf already has for one. No new state value is added; if the existing vocabulary cannot say it, that is a contract
   question to this seat before the cell builds, with its rule-24 record. Windows that do not span the day are untouched.
3. **The change is in the emitter, as a guard on the window, not a recompute.** `perfrp_emit_core.py` loads the non-trading
   partitions inside its window (it has exactly one to load) and refuses a window for an account whose skipped partition carries an
   external flow. The guard is general: it fires on any future closed day with flows, not on a hard-coded date.
4. **One object moves.** The re-emitted `perfrp_performance_account.json` replaces the served one. The other three leaves move only
   if cell A measures that they consume the affected returns.

## 4. Cells (for base `2.0.0_SA_COO` to cut as ONE issuance)

- **A, read-only (first):** (i) the census by SUBTRACTION: the 44 accounts, minus those with no figure in the leaf, equals the
  entries that will change, printed with all three numbers; (ii) row-grain check: count `flow_ledger` rows whose own date is a
  non-trading day, over all 561 partitions; (iii) which of the other three served leaves read `window_return` or `twr_daily`;
  (iv) the provenance of the 2026-09-01 publish (the writer, the word it ran under).
- **B, build (LOCAL):** the emitter guard of section 3 item 3 with a test on a fixture built from 2025-01-08..2025-01-10: an
  account with a 01-09 flow is refused for a spanning window and computed for a non-spanning one; an account with no 01-09 flow is
  byte-identical to today.
- **C, served move:** re-emit and publish under both never-widen halves. The packet names the one key, the restore target
  `E78kI4KB4KsZhdwsAFzfSvkI.kn5Snim`, and both branches: (a) entries changed equals cell A's count and every other entry is
  byte-identical; (b) any other entry differs, and the publish does not run. The acceptance is one read of the served object: the
  four probed accounts carry no since-inception figure.

`<risk>`: A LOCAL, B LOCAL, C WORLD. Lane: DS for A and B (`data/assets/scripts/gold/runners_49f/`), the publish per rule 13.

## 5. What this does not do

It does not correct the 44 accounts' returns; it withholds them. The corrected figure arrives with the dashboard project's
total-return table, whose rule already folds a closed day's flows into the next trading day. It does not touch `twr_daily`, so the
Black Diamond parity comparison (row S239) still reads the bad day; that comparison is a diagnostic, not a served figure, and its
reader takes the same guard in a later round if the comparison is still in use.

## 6. The one thing only Andrew can do

Lift the D2 hold for this cell. `org/ref/LIVE_ARMS.md`: "`2.0.0_SA_COO` (base): D2 off until Andrew lifts it".

-- 1.0.0_SA_CTO
