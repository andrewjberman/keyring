# DS~D Session 2 — ADVI_TXNAMG.003 Amalgamating Writer

**Agent:** `0.4.0_DS_ClientPlatform~D`
**Date:** 2026-05-15
**TO:** `ADVI_TXNAMG.003.dsd-amalgamating-writer` (COO-issued; dispatch_held released on TO-1 RAVC2 validation)
**Status:** COMPLETE — code shipped + S3-deployed + verified + locally validated. RAVC2 to COO + CC CTO + AE 0.7.0.

## Current State

TO-3 of `ADVI_TXNAMG` — the core deliverable. `convert_transactions_to_silver.py` is now the
single canonical amalgamating writer of `silver/transactions/{date}.parquet`: the REST
full-history spine LEFT-JOINed with the 11 Custom-Report-unique columns by transaction id.
Committed `10de8e67f`, pushed CLOUD, S3-deployed to `opal-data-inf`, SHA-verified MATCH.

## What I Did

Extended `data/orion/scripts/silver/convert_transactions_to_silver.py` per the COO-validated
TO-1 contract (brief `docs/briefs/txnamg-001-join-key-column-audit-20260515.md`):

- **New `_load_custom_report_enrichment(s3)`** — reads the accumulated Custom-Report bronze
  (`bronze/orion-api/*/transactions.csv`, 1,509 files) via a 24-worker ThreadPoolExecutor,
  strips CSV header whitespace, parses + type-coerces the 11 carried columns, dedups on `id`
  (keep most recent CSV), returns the join frame. Schema-stable empty frame on a missing
  enrichment source — never fails the chain (PRD §4.1 error case).
- **`build_silver`** gains a `cr_enrichment` parameter + a `df.merge(cr_enrichment, on="id",
  how="left")` — the same Rule-17 JOIN-enrichment class as the existing rep_id join. Joined
  columns populated on Custom-Report-overlap rows, NULL elsewhere (no business fillna/dropna/
  row-filtering). UNION extension point left open per COO directive (closed-account rows).
- **11 carried columns** (camelCase, matching the REST spine): `accountLname`,
  `activityCategory`, `downloadSymbol`, `createdDate`, `createdBy`, `editedDate`, `editedBy`,
  `repName`, `currentAccountValue`, `currentCashValue`, `managedAccount`. The other 18 CR
  columns are aliases of existing REST columns (not joined); `fkTradeStatus` not carried
  (encoding variant of REST `status`, no CTO override).
- Pinned the Custom Report 28198 datetime format (`%m/%d/%Y %I:%M:%S %p`) — verified
  era-stable 2020/2022/2024/2026.

## Validation — local, against production S3 (`txnamg003_validate.py`)

The exact committed code, run against the exact production S3 inputs:

| Check | Result |
|---|---|
| AC5 row count preserved | PASS — silver 1,299,335 == bronze 1,299,335 (left join) |
| AC1 column count = REST + 6 + 11 | PASS — 48 cols |
| AC1 all 11 carry columns present + `id` unique | PASS — no fan-out |
| AC3 NULL-elsewhere (non-overlap rows all 11 cols NULL) | PASS — 151,276 rows NULL |
| AC3 populated-on-overlap (`repName` non-null on overlap) | PASS — 1,148,059 rows (88.36%) |
| AC3 join value fidelity (silver == Custom-Report source) | PASS |
| AC2 2021 txn (id=390362) carries all 11 join columns | PASS — repName=Peter Lee, createdDate=2021-01-13, currentAccountValue=851437.78 |
| AC2 2023 txn (id=572441) carries all 11 join columns | PASS — repName=Peter Lee, createdDate=2023-01-11, currentAccountValue=95873.08 |
| AC4 sparsity preserved (no fillna of joined cols) | PASS |

## Deploy cycle (CLAUDE.md Rule 13)

- Commit `10de8e67f` (author `0.4.0_DS_ClientPlatform~D`).
- `git push origin CLOUD` — pre-push hook fired `safe-deploy.sh`: `DEPLOYED [inf]
  convert_transactions_to_silver.py`, gate PASS, S3 cp + SHA verify MATCH on `opal-data-inf`.

## Deploy wave + AC5 artifact-level closure (2026-05-15, with AE 0.7.0)

The TO-3/TO-4 same-wave deploy was choreographed with AE 0.7.0 per the PRD §3 sequencing
invariant and executed:

- **Step 1 — TO-4 (AE 0.7.0):** `inf-api-txn` Lambda trimmed (writer #3's silver-write
  removed, sentinel body revised to "txn bronze done"), terraform-apply 0-diff, tag
  `inf-pipeline-v1.7.61`, live CodeSha verified. Writer #3's silver-write is gone first —
  eliminates the clobber race entirely.
- **Step 2 — chain-run (AE 0.7.0):** `inf-gold-trigger` `{"mode":"full"}` → plain
  `--chain full` on `inf-gold-layer-runner` (production). Dispatched 17:57Z, completed
  18:55Z exit 0 (`gold/meta/pipeline-complete.json` written — dispatch.sh writes it only
  on `chain_exit==0`). `INF_API_SILVER_TXN` (this writer) ran ~10min in.

**AC5 — artifact-level validation (`txnamg003_artifact_validate.py`):** ran against the
materialized `s3://opal-data-inf/silver/transactions/2026-05-15.parquet` (36.8 MB, LM
18:07:20Z) — **ALL PASS:**

| Check | Result |
|---|---|
| AC1 column count == 48 | PASS — 31 REST + 6 meta + 11 CR, all present |
| AC1 `id` unique (no fan-out) | PASS |
| AC5 row count preserved vs REST spine | PASS — silver 1,299,493 == `bronze/transactions/2026-05-15.parquet` 1,299,493 |
| AC3 enrichment present | PASS — 1,148,059/1,299,493 rows (88.35%) carry `repName` |
| AC3 NULL-elsewhere | PASS — 151,434 non-overlap rows have all 11 carry cols NULL |
| AC4 sparsity preserved (no fillna) | PASS |
| AC2 2021 txn id=390362 carries all 11 join columns | PASS — repName=Peter Lee, createdDate=2021-01-13, currentAccountValue=851437.78 |
| AC2 2023 txn id=572441 carries all 11 join columns | PASS — repName=Peter Lee, createdDate=2023-01-11, currentAccountValue=95873.08 |

The full `--chain full` ran the D-tier end-to-end at exit 0 — TO-2's migrated `INF_D_05`
consumer read the amalgamated camelCase silver without error (chain-exit-0 evidence).

**TO-3 COMPLETE — all AC1-6 PASS, artifact materialized + validated.** `silver/transactions/`
now has exactly one writer (the gold chain). AE 0.7.0 sends the TO-4 RAVC2 on this PASS.

## Compiler Tools

| Tool | Run | Result |
|---|---|---|
| `comp-pipescript io convert_transactions_to_silver.py` | Phase 1 | S3-DYNAMIC reads only; "no s3_layout constants detected" — the documented coverage gap (PRD §5.2): comp graph does not model this script's S3 IO. Manual review is the sanctioned basis. |
| `.tools/ds-commit-gate.sh` | Phase 2 | PASS — py_compile + ds-precommit-check (Rule-17, `coerce_silver_ids` present, `from __future__` first) + ruff py39 all clean. |
| `.tools/safe-deploy.sh` (via pre-push hook) | Phase 3 | PASS — `DEPLOYED [inf]`, S3 cp + SHA verify MATCH on `opal-data-inf`. |
| `comp-pipescript deployed` | Phase 3 | Default target is `opal-data-bd`; orion silver maps to `opal-data-inf` — safe-deploy's internal comp-pipescript confirm covered the verify (gate PASS). |

## Next Steps

| Recipient | Item |
|-----------|------|
| **COO 2.0.0** | RAVC2 — AC1-6: code shipped + S3-deployed + MATCH + locally validated against prod S3 (AC1-5 substantively proven; AC6 PASS). RAVC2 receipt releases TO-4 dispatch_held. |
| **CTO 1.0.0** | CC on RAVC2. The §4.1 left-join-vs-UNION amendment question (closed-account rows, ~2.7% of CR ids absent from the REST spine) — the writer is structured so a UNION is a clean additive `pd.concat` if ruled. |
| **AE 0.7.0** | CC + sequencing coordination — TO-4 (inf-api-txn Lambda silver-write removal) lands before/same-wave as TO-3 per PRD §3. The live chain-run (INF runner start) is the coordinated deploy wave. |
| **DS~D (self)** | TO-6 (INFINC.006 resume) is gated on TO-3 + TO-4 shipping — held. /loop watchdog standby. |
