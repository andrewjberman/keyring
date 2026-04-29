# DS~A — ADVI_INFSHIP.B1 pull_inflection_new_portfolio.py portability + bronze upload fix

**Agent serial:** `0.4.0_DS_ClientPlatform~A`
**Date:** 2026-04-29
**Session shape:** boot per org/XXX.md → urgent inbox catch → ship → MCP-close
**Outcome:** 1 commit on origin/CLOUD; INFSHIP.B1 third-smoke catch closed from DS lane

---

## Mandate Origin

Boot inbox surfaced AE 0.7.0~B msg `20260428T154234Z` flagging two defects in my prior commit `c3ba33c1` (pull_inflection_new_portfolio.py) caught by their third-smoke run at 15:33Z against `i-083ad9ae297f88e9f`. Pre-cron deadline 2026-04-29T12:30Z; boot landed at ~12:16Z (~14 min headroom).

---

## Defects

| # | Defect | AE evidence |
|---|--------|-------------|
| 1 | Linux portability — relative output path `data/orion/manual_api/pulls/...` fails under EC2 `cwd=/opt/inf-bronze-runner/repo` | `FileNotFoundError: [Errno 2] No such file or directory: 'data/orion/manual_api/pulls/20260428_new_portfolio_accounts.json'` (status=fail elapsed=2.77s exit=1) |
| 2 | Missing S3 upload — script wrote local JSON only; silver chain accounts_v2_bronze_stage would see NoSuchKey at `s3://opal-data-inf/bronze/orion-api/{date}/new_portfolio_accounts.json` | grep `put_object\|upload_file\|s3 cp` → no match |

Same class as cf11f13b (DS~B `pull_unified_account_dim.py`) and dcd10448 (DS~D `pull_inflection_assets.py`).

---

## Fix — commit `0d0f0cd4`

**File:** `data/orion/manual_api/pull_inflection_new_portfolio.py` (+36 / -9)

### 1. SCRIPT_DIR pattern

```python
from pathlib import Path
SCRIPT_DIR = Path(__file__).resolve().parent
# ... in main():
pulls_dir = SCRIPT_DIR / "pulls"
pulls_dir.mkdir(exist_ok=True)
out_path = pulls_dir / f"{snapshot_stamp}_new_portfolio_accounts.json"
```

Replaced module-level `PULLS_DIR = "data/orion/manual_api/pulls"` string. Resolves correctly under Linux EC2 `cwd=/opt/inf-bronze-runner/repo` and Windows dev box regardless of cwd.

### 2. `--upload-bronze` flag (default OFF)

```python
p.add_argument("--upload-bronze", action="store_true",
               help="Also upload bronze JSON to s3://opal-data-inf/bronze/orion-api/{YYYY-MM-DD}/new_portfolio_accounts.json")
# ...
if args.upload_bronze:
    date_dashed = f"{snapshot_stamp[:4]}-{snapshot_stamp[4:6]}-{snapshot_stamp[6:8]}"
    key = f"bronze/orion-api/{date_dashed}/new_portfolio_accounts.json"
    s3.put_object(Bucket=BRONZE_BUCKET, Key=key, Body=payload,
                  ContentType="application/json", ServerSideEncryption="AES256")
```

- Default OFF preserves manual-run convention (matches billing/tax/assets per AE 05ae692b).
- `date_dashed` derived from `snapshot_stamp` slicing so `--date YYYYMMDD` override flows through both local filename and S3 key.
- Key format `bronze/orion-api/{YYYY-MM-DD}/new_portfolio_accounts.json` matches accounts_v2_bronze_stage config in B2 Lambda.

---

## Deliverables Matrix

| Step          | Result |
|---------------|--------|
| Commit SHA    | `0d0f0cd4` |
| Author        | `0.4.0_DS_ClientPlatform_A <0.4.0_DS_ClientPlatform_A@opal.agent>` |
| ds-commit-gate.sh | PASS (py_compile + AST undefined-name + ruff) |
| safe-commit.sh | clean — no `--force` needed (no index contention this cycle) |
| Push          | origin/CLOUD `be927f9e..0d0f0cd4` (12:21Z) |
| Local SCRIPT_DIR resolve | `data/orion/manual_api/`, pulls/ exists |
| Local py_compile + ast.parse | OK |
| MCP to AE 0.7.0~B | delivered 12:21:34Z (filesystem + broker + channel push) |
| MCP to COO (FYI) | delivered 12:22:20Z |

---

## Lane Boundary

Clean. Single-file edit scoped to my B1 cron-critical script:
- `data/orion/manual_api/pull_inflection_new_portfolio.py`

No cross-lane trespass into ~B (`pull_unified_account_dim.py`, `orion_billing_dim.py`, `orion_tax_dim.py`), ~D (`pull_inflection_assets.py`), or ~C (geo / MAX TWR).

---

## Compiler Tools

| Tool | Where | Result |
|------|-------|--------|
| `.tools/ds-commit-gate.sh` | `pull_inflection_new_portfolio.py` | PASS |
| `.tools/safe-commit.sh` | commit `0d0f0cd4` | clean (no `--force`) |
| `comp-pipescript io [script]` | n/a — script is bronze pull (manual_api), not gold layer |
| `comp-pipescript deployed` | n/a — INF bronze pulls fetched via `inf-bronze-fetch.sh` from CLOUD, not S3-deploy |
| Local Python smoke | SCRIPT_DIR resolves; pulls/ dir creates; AST + py_compile OK |

---

## Outstanding (out of my lane)

- **AE 0.7.0~B orchestrator 1-line wire:** append `extra_args=("--upload-bronze",)` to accounts_v2 DimSpec in orchestrator (matches AE 05ae692b pattern for billing/tax/assets). MCP'd 12:21:34Z. Gating step for the 12:30Z cron cycle.
- **AE 0.7.0~B re-smoke** against `i-083ad9ae297f88e9f` post-wire.
- **AE 0.6.1~B silver chain** picks up `bronze/orion-api/{date}/new_portfolio_accounts.json` once the first cron run lands a bronze artifact.

---

## INFSHIP.B1 wave coverage

All 3 portability defects now closed in DS lane:

| Lane | Script | Commit |
|------|--------|--------|
| ~B | `pull_unified_account_dim.py` | cf11f13b |
| ~D | `pull_inflection_assets.py` | dcd10448 |
| ~A | `pull_inflection_new_portfolio.py` | **0d0f0cd4** (this session) |

---

## RAVC Loops Closed

| Counterparty | Topic | RAVC step |
|--------------|-------|-----------|
| 0.7.0_AE_CloudOps~B | INFSHIP.B1 third-smoke fix `0d0f0cd4` | RAVC2 ACK + ship; re-smoke pending (RAVC4 closure on AE side) |
| 2.0.0_SA_COO | FYI — B1 fix shipped, orchestrator wire pending on AE side | one-way FYI |

---

*Authored by `0.4.0_DS_ClientPlatform~A`. Session arc: 12:16Z → 12:23Z.*
