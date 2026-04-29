# DS~D — ADVI_INFSHIP.B5 Transactions v2 — prompts[] fix + backfill

**Agent serial:** `0.4.0_DS_ClientPlatform~D`
**Date:** 2026-04-29
**Session shape:** TO dispatch from 0.6.1_AE_PartnerETL -> research -> build -> test -> backfill -> ship
**Outcome:** 1 commit on origin/CLOUD (79bf2afbc); backfills uploaded; orchestrator wired

---

## Mandate Origin

ADVI_INFSHIP.B5 TO from 0.6.1_AE_PartnerETL assigned to DS~D. `pull_inflection_transactions.py` (v1, AE 0.7.0~B) has never succeeded — transactions bronze missing from every bronze runner cycle.

AE diagnosis: original body used `parameters[]` format (HTTP 500). AE tested corrected `prompts[]` format and reported "header-only CSV (0 data rows)". AE concluded Custom Report 28198 is a UI-context report with no API-accessible data and proposed using Envision/ExcelReports API.

---

## Investigation Findings

### Envision API path (ruled out)

`data/orion/manual_api/probe_tax_txn.py` probe results (`20260428_tax_txn_probe.csv`): ALL Transaction.* and Trade.* paths return `{ERROR:X is not supported}`. Envision ExcelReports is aggregate-only — no transaction grouping exists per `additionalOptions` enumeration (13 categories, none Transaction-grain). Dead end per PATH_DISCOVERY.md.

### Custom Reports 28198 (correct endpoint)

Per `docs/architecture/INFLEC_API_ENDPOINTS_CATALOG.md` (DS~A v0.1, 2026-04-28): Custom Reports is the correct endpoint family for per-transaction grain. Report 28198 = "Homepage Daily Transactions - Rep" — Andrew's UI export source.

**v1 bug:** `parameters[{name, value}]` format causes HTTP 500.

**Correct format** (per Andrew HAR(4) / catalog §Custom Reports):
```json
{
  "runTo": {"source": "OnDemandUI"},
  "databaseIdList": [],
  "prompts": [
    {"id": 47115, "code": "@StartDate", ...},
    {"id": 47116, "code": "@EndDate", ...},
    {"id": 47117, "code": "@RepIDs", "defaultValue": "3,11,12"},
    {"id": 49130, "code": "@type", "defaultValue": "1,2,6,7,12,98,5,96,4,9,10,11,97,99"},
    {"id": 59602, "code": "@selectedType", "defaultValue": null}
  ],
  ...
}
```

**AE's "header-only" finding was incorrect.** With proper `prompts[]` format the endpoint returns real data. Independently verified against live API with current JWT.

---

## Fix — commit `79bf2afbc`

**Files:** `data/orion/manual_api/pull_inflection_transactions_v2.py` (+261) | `data/orion/scripts/bronze/orchestrator.py` (+432, first local copy)

### Script changes vs v1

| Change | v1 | v2 |
|---|---|---|
| Body format | `parameters[{name, value}]` — HTTP 500 | `prompts[{id, code, promptType, defaultValue}]` — 201 OK |
| Path portability | `PULLS_DIR = "data/orion/manual_api/pulls"` (relative) | `SCRIPT_DIR = Path(__file__).resolve().parent` |
| S3 flag | `--no-s3` (default: upload) | `--upload-bronze` (default OFF; matches billing/tax convention) |
| Data guard | None | `validate_csv_has_data()` — exit(4) on header-only CSV |
| Exit codes | 0-1 | 0 (ok) / 1 (JWT) / 2 (generate fail) / 3 (poll timeout) / 4 (header-only) / 5 (unexpected) |

### Orchestrator update

`data/orion/scripts/bronze/orchestrator.py` DimSpec updated:
```python
DimSpec("transactions", "data/orion/manual_api/pull_inflection_transactions_v2.py", extra_args=("--upload-bronze",))
```
Uploaded to `s3://opal-data-inf/code/bronze-runner/orchestrator.py`.

---

## Compiler Tools

| Tool | Input | Result |
|------|-------|--------|
| `.tools/ds-commit-gate.sh` | `pull_inflection_transactions_v2.py` | PASS (py_compile + AST + ruff) |
| `.tools/ds-commit-gate.sh` | `orchestrator.py` | PASS |
| `.tools/safe-commit.sh` | commit `79bf2afbc` | clean (no --force) |
| Live API test | Custom Reports 28198 Apr 1-29 window | 201 + 15,514 rows in ~2s |

---

## Deliverables Matrix

| Step | Result |
|------|--------|
| Commit SHA | `79bf2afbc` |
| Author | `0.4.0_DS_ClientPlatform_D` |
| Pre-commit gate | PASS |
| API validation (Apr 1-29) | 15,514 data rows, 7.3 MB |
| Backfill 2026-04-28 | 4,235 rows -> `s3://opal-data-inf/bronze/orion-api/2026-04-28/transactions.csv` |
| Backfill 2026-04-29 | 4,186 rows -> `s3://opal-data-inf/bronze/orion-api/2026-04-29/transactions.csv` |
| Orchestrator | Updated + S3 uploaded |
| MCP to AE 0.6.1 | RAVC2 delivered 15:02:47Z |

---

## Silver Side (no changes needed)

`data/orion/scripts/silver/convert_orion_to_silver.py` already normalizes the 29-col bronze TRN CSV schema (same columns as Andrew's manual UI exports). No silver builder changes required for API-sourced bronze at this schema.

---

## Outstanding (out of my lane)

- AE 0.6.1 re-smoke: inf-bronze-runner dispatch with v2 to confirm end-to-end
- Daily cron picks up v2 starting 2026-04-30 cycle

---

## RAVC Loops Closed

| Counterparty | Topic | RAVC step |
|---|---|---|
| 0.6.1_AE_PartnerETL | INFSHIP.B5 COMPLETE, backfills done, orchestrator wired | RAVC2 delivered |

---

*Authored by `0.4.0_DS_ClientPlatform~D`. Session arc: 15:48Z → 15:02Z.*
