# DS~B Session 1 — ADVI_TXNAMG.002 (TO-2) consumer migration

**Agent:** 0.4.0_DS_ClientPlatform~B
**Date:** 2026-05-15
**TO:** ADVI_TXNAMG.002.dsb-consumer-migration (from 2.0.0_SA_COO)
**Commit:** bcde73ada (pushed CLOUD; safe-deploy gate PASS)

## Objective

Migrate the two non-shielded silver/transactions consumers off the legacy
snake-case schema onto the canonical camelCase source-select so every consumer
reads the live full-history snapshot. Phase A = INF_D_05.activity_scan; Phase B
= INF_D_00.portal_aggregates verify-and-clean. Phase C (8-shielded confirmation)
held until COO signals TO-3 (amalgamating writer) has shipped.

## Empirical probe (pre-write)

`.runtmp/txnamg002_silver_probe.py` — read-only S3 schema probe of
`silver/transactions/`:

- 1,515 partitions. Canonical camelCase snapshot = `silver/transactions/2026-05-15.parquet`
  (mtime 2026-05-15T16:36:24Z, 32.7 MB, **1,299,335 rows**, `transDate` range
  2020-05-26 -> 2026-05-15, **0 NaT**). Carries `accountId/transDate/id/transTypeId/
  transAmount/navPrice/noUnits/assetId/ticker/productName/trans_type_desc`.
- The 4 newer-dated LEGACY partitions (2026-05-11..14) are snake-schema and
  **100% NaT `trans_date`** — exactly the writer-#3 null-trans_date partitions
  the TO describes (`dropna` would drop every row).
- INF_D_00's snake column check `{asset_id,nav_price,trans_type_id,units}` FAILS
  on a camelCase snapshot => **INF_D_00 currently takes the masked bronze fallback**
  (AC3 empirical answer). Bronze partition `2026-05-15.parquet` exists and is fresh.

## Phase A — INF_D_05.activity_scan.py

Replaced `_load_txn_partition` (snake-schema requirement, returned None on every
camelCase partition) + `load_all_transactions` (64-thread concat-all of ~1,515
partitions) with a single `load_all_transactions()` doing a **Path A.2
source-select**: mtime-sort descending, walk newest 5, load the first partition
carrying `REQUIRED_CANONICAL_COLS = {accountId, transDate, id}`, fail loud after
5 attempts. 1:1 cosmetic rename camelCase -> internal snake (Rule 17 sec 3.3).
Removed the now-unused `ThreadPoolExecutor/as_completed` import + `MAX_WORKERS`.

§7-Q1 RULED latest-snapshot (Andrew via CTO, f6a13a672) — confirms this read
model; concat-all rejected, superseded partitions inert.

**Local dry-run verification** (real prod S3): source-selected
`silver/transactions/2026-05-15.parquet`, 1,299,335 rows, 835 txn accounts,
trade_date 2020-05-26 -> 2026-05-15. `data_as_of = 2026-05-15` => windows
qtd/ytd/1y/max all anchored current. 4-window + legacy emit, 298 households each,
non-zero. **Recency gap closed in code** (was frozen 2026-05-08).

## Phase B — INF_D_00.portal_aggregates.py

`load_buy_lot_acquisitions_firm` migrated from `_newest()` + snake-schema check
+ masked bronze fallback to a Path A.2 canonical camelCase source-select.
Removed the dead bronze fallback and the now-unused `BRONZE_TRANSACTIONS_PREFIX`
constant — the silver-read path is now confirmed-live and unambiguous (AC3).

**Local verification** (`.runtmp/txnamg002_d00_probe.py`, importlib harness on
the real function): source-selected the canonical 2026-05-15 snapshot, returned
624,680 Buy rows / 826 accounts, trans_date 2020-05-26 -> 2026-05-15, all 8
normalized columns present.

## Phase C — HELD

8-shielded-consumer confirmation-run + AC6 (no concat-all reader remains) gated
on TO-3 ship. Awaiting COO signal.

**Finding flagged to COO:** `INF_D_02.load_buy_lot_acquisitions` (a SHIELDED
consumer, cost_basis path) carries the IDENTICAL stale snake-check + masked
bronze fallback as the INF_D_00 function fixed here. Not broken for AC4 (bronze
is fresh => non-zero output) and out of TO-2 scope, but it is a masked-fallback
twin worth a follow-up TO.

## Files Modified

| File | Change |
|------|--------|
| data/orion/scripts/gold/INF_D_05.activity_scan.py | `_load_txn_partition` + concat-all `load_all_transactions` -> single Path A.2 canonical camelCase source-select; removed ThreadPoolExecutor import + MAX_WORKERS |
| data/orion/scripts/gold/INF_D_00.portal_aggregates.py | `load_buy_lot_acquisitions_firm` -> Path A.2 canonical camelCase source-select; removed dead bronze fallback + unused BRONZE_TRANSACTIONS_PREFIX |

## Compiler Tools

| Tool | Result | Notes |
|------|--------|-------|
| `comp-pipescript io INF_D_05` | Resolved to `INF_D_05.client_top_holdings.py` (wrong twin) | `INF_D_05` prefix is ambiguous — two scripts share it (`INF_D_05`=client_top_holdings, `INF_D_05a`=activity_scan in the dispatch registry). comp-pipescript keyed the non-`a` ID. Gap noted; the io manifest for the file I edited was derived directly from the source instead. |
| `.tools/ds-commit-gate.sh` (both files) | PASS — "All checks passed!" x2 | py_compile + ds-precommit-check.py (AST undefined-name + `from __future__` Rule 15) + ruff --target-version py39 |
| `.tools/safe-commit.sh` | PASS — commit bcde73ada, scoped to the 2 gold scripts | --author 0.4.0_DS_ClientPlatform; modified TO file (COO scope) left untouched |
| `.tools/safe-deploy.sh` (pre-push hook) | PASS — both scripts DEPLOYED [inf] + verified | `data/orion/scripts/gold/*.py -> s3://opal-data-inf/code/gold/` |

**comp-pipescript io gap:** the `INF_D_05` ID disambiguation should prefer an
exact filename match or warn on prefix collision. Surfaced for the comp-tools
backlog.

## RAVC2

- **COO 2.0.0** — Phases A+B code-complete: migrated, gated, committed
  (bcde73ada), pushed CLOUD, S3-deployed (safe-deploy PASS), and verified by
  local dry-runs against real prod S3 (recency gap closed in code). AC2/AC3/AC5
  satisfied. AC1 (deployed `activity_scan_1y.json` artifact recency) needs a
  runner run — see Next Steps.
- **CTO 1.0.0** — CC on RAVC2.

## Next Steps

- `[AE 0.6.1]` Artifact-refresh run: the inf gold runner (i-0ed5afded2ebd4ed4)
  is stopped; the deployed `activity_scan_1y.json` is frozen at 07:08Z (06:00Z
  full chain, old code). Fire `--single INF_D_05a` (= `INF_D_05.activity_scan.py`)
  via the SSM-direct single-script runbook to refresh `platinum/firm/activity_scan_*.json`
  with the migrated code — closes AC1 at the artifact level. EC2 start/stop is
  AE-exclusive; DS cannot self-serve. Alternative: next daily full chain
  (2026-05-16 06:00Z) picks it up automatically.
- `[COO 2.0.0]` Phase C: signal when TO-3 (amalgamating writer) ships — DS~B
  resumes for the 8-shielded confirmation-run + AC6 assertion.
- `[COO 2.0.0]` Consider a follow-up TO for `INF_D_02.load_buy_lot_acquisitions`
  (masked-bronze-fallback twin, see Phase C finding).
