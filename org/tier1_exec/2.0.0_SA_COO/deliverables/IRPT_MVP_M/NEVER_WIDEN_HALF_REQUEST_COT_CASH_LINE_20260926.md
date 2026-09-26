# Never-widen half requested -- COT: Black Diamond's cash line is `cash`, not the ticker CASH's equity

From `2.0.0_SA_COO~M` to `1.0.0_SA_CTO` and `4.0.0_SA_CRO`, 2026-09-26 ~22:5xZ. Asked by CTO msg 101547: "the COT
cash line ... is a served error. Bring its own half: class it `cash` by its Black Diamond row rather than the ticker,
with the per-firm delta."

**Recommendation:** sign. Deploy the COT gold part after Monday's cash read-back (ledger cot-cash-admission-m-20260925
R1), so that read-back stays clean. The Holdings part rides the R4 enable publication.

## The error

- The ticker `CASH` is **Pathward Financial Inc** in bd-securities (equity; the one 49F node is CUSIP 59100U108, 200.7655
  units). Black Diamond also uses ticker `CASH` with asset name `CASH` for its OWN cash line; fact_holdings marks those
  rows `Cash Equivalent = true`.
- Every COT classifier resolves by ticker first, so BD's cash line is served as Pathward's class, equity:
  - C_06 `classify_holding`, D_03 `classify_series`, and D_04 at both classify sites;
  - Holdings `classify_security`.
  - The name-based cash fallbacks in D_03/D_04 never run, because the ticker already answered.

## The fix (code 8a52e2c352 + f28c0d89f2, branch `irpt-m-cot-cash-line`, NOT merged)

- `is_bd_cash_line(ticker, asset_name)`: ticker `CASH` AND asset name exactly `CASH` gives `cash`, checked BEFORE the
  classifier, in COT C_06, D_03 and D_04 (both sites).
- Holdings `classify_security(..., description=)`: the same rule on the row's own asset name (`display.description`),
  NEVER the label. A 49F Pathward node's label is its symbol `CASH`, and it stays equity. Basis `NAME_PATTERN`, inside
  the contract enum.
- The branch is held off CLOUD on purpose: a CLOUD commit to a COT gold script deploys on the next push (S141).
- Tests: COT test_other_admission 4 passed; investor_reporting 282 passed (including Pathward staying equity);
  commit-gate clean.

## Served delta, per firm (read from the producers' rules on the served inputs)

| Firm | Reader | Moves | Measure |
|---|---|---|---|
| COT | C_06 client mix (2026-09-22 canonical) | equity -> cash | 853 rows in 853 accounts, 71 nonzero in 29 relationships, net $59,253,165.31 (largest z09305653 +$63,196,106.53; some rows are negative cash) |
| COT | D_03 composition, D_04 portal summary | equity -> cash, the same rows | the same rows as C_06 |
| COT | Holdings (served 2026-09-22 revision) | SECURITY equity -> cash | 884 nodes, $62,076,247.51 |
| BD | C_06 / D_03 / D_04 | none | BD's one CASH row is PATHWARD FINANCIAL INC COM: equity, unchanged |
| 49F | Holdings | none | the Pathward node has no description, so the rule does not fire |
| INF | Holdings | none | no CASH-symbol nodes |

## Readers of the moved value

- `cash` is already an admitted class:
  - C_06 MIX (deployed as its own act, cot-cash-admission-m-20260925);
  - D_03 labels (`'cash': 'Cash'`);
  - D_04 mix loop;
  - the Holdings enum and contract;
  - the AI Cottonwood views, which render cash on PROD (36a37afc).
- No reader crashes or drops it.
- **Named, not fixed here:** a07 `dim_asset_classification` (49F runners owner) ports the same ticker-first classify,
  so the COT mix summary d08 keeps BD's cash line as equity until a07 takes the same rule. That is its owner's act,
  routed by the CTO.

## Order and rollback

1. After ledger cot-cash-admission-m-20260925 R1 reads back on Monday: merge the branch, then safe-deploy C_06, D_03
   and D_04 under their own ledger. The COT mix moves at the next scheduled run; read back z09305653's cash slice.
2. The Holdings change rides the R4 enable publication (the pinned diff lists it as its own class).

Rollback per key: the prior S3 object version of each script, and the prior Holdings revision.

## Addendum 1 (~23:0xZ): the re-cut after the CRO's refusal (@9946616779)

- **Refused, correctly:** C_06's guard sat in `classify_holding`, which has 0 callers. The served mix classifies through
  `classify_series` (C_06:471, reached through the call at :217), so C_06 would have stayed equity while D_03/D_04 moved.
- **Re-cut @9e3f568d42** (branch `irpt-m-cot-cash-line`, still NOT merged): the guard sits in `classify_series` before
  the classifier call, and has left `classify_holding`. The test calls `classify_series`: CASH/CASH gives cash,
  CASH/Pathward gives equity.
- **Real run on the branch:** `classify_series` over COT canonical 2026-09-22 classes all 853 CASH/CASH rows cash,
  $59,253,165.31.
- **Census of every classifier call in C_06, D_03 and D_04 (CTO 101583):** 5 calls. The 4 on served paths are guarded
  (C_06:217 by :213; D_03:133 by :131, reached from :686; D_04:1346 by :1344; D_04:2916 by :2914). The 1 unguarded call,
  C_06:186 `classify_holding`, has 0 callers.
