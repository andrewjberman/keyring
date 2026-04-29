# DS~B — ADVI_INFLV2.002 NMEC/NMNC Lifecycle Emission: D_04 total.* + D_00c Leaderboard

**Agent serial:** `0.4.0_DS_ClientPlatform~B`
**Date:** 2026-04-29
**Session shape:** post-compaction loop session → INFLV2.002 Task 1 audit → Tasks 2-4 code execution
**Outcome:** 2 commits on origin/CLOUD; S3 MATCH both scripts; RAVC-PENDING-VALIDATION sent to COO + AE

---

## Mandate Origin

GO from `2.0.0_SA_COO` (20260429T131850Z) on ADVI_INFLV2.002:

> "Andrew directive to get all lanes active on Inflection. You're up on INFLV2.002."

Task 1 (read-only audit) started immediately. Tasks 2-4 (code) held on INFGRD.003 chain gate initially, then COO issued GO-NOW (20260429T161000Z) to execute before chain signal.

---

## Deliverables Matrix

| # | Item | Commit | S3 MATCH | Status |
|---|------|--------|----------|--------|
| 1 | INF_D_04 total.* NMEC split (Task 1 audit → Task 2 code) | `7bd1cf9be` | `7ee52d585e30a8c35dc49ffafb68cec0` | SHIPPED; pending INFGRD.003 validation |
| 2 | INF_D_00c leaderboard lifecycle_aua per advisor + firm (Task 3 code) | `d8467140f` | `325d2a6bb14e1e4c097a7e6cb2a071c3` | SHIPPED; pending INFGRD.003 validation |
| 3 | IWM book.json RAVC4-CLOSE | n/a (response to DE ACK) | — | CLOSED |
| 4 | INFLV2.005 Concentration Risk — dropped (DS~A shipped INF_D_07 `ffd4484b3`) | n/a | — | DROPPED (correct call) |

---

## Section-by-Section

### §1 — Task 1: Lifecycle Emission Audit (INF_D_04 post 7ecc140a)

**Audit findings:**

| Artifact | Slot | Status |
|---|---|---|
| header_metrics.json | radial_12m (NMNC/NMEC/Existing) | POPULATED ✓ (7ecc140a via `_build_radial_12m` → `_compute_hh_lifecycle`) |
| partner_analytics_*.json | views.aua.donut.segments | POPULATED ✓ (7ecc140a via `_build_aua_view` → `_compute_hh_lifecycle`) |
| header_metrics.json | total.new_client_aua / existing (2-segment) | GAP — NMEC collapsed into existing_client_aua; no nmec_aua field in total.* |
| timeseries_overview.json | NNA per period | POPULATED ✓; sign convention confirmed: net_nna positive = net money in (matches BD/49F) |
| leaderboard.json | NMEC/NMNC per entry | GAP — lives in INF_D_00c; `_compute_new_clients_per_advisor` has count only, no lifecycle AUA |

Gaps confirmed by COO in RAVC ACK (20260429T135144Z). Both assigned to Task 2 scope.

**RAVC Task 1 to COO:** `20260429T131850Z` — accepted.

---

### §2 — Task 2: INF_D_04 total.* NMEC Split: `7bd1cf9be`

**Root cause of gap:** `build_header_metrics()` lines 964-988 used a 2-segment `first_trade_date >= cutoff` heuristic directly, bypassing `_compute_hh_lifecycle()`. This collapsed NMEC HHs into `existing_client_aua` without surfacing their "new money" portion separately.

**Fix:**

Replaced lines 964-988 with `_compute_hh_lifecycle(window_days=365, accounts_v2_dim=accounts_v2_dim)` call:

```python
# NMNC/NMEC/Existing split via _compute_hh_lifecycle() (12-month window).
nmnc_aua = nmec_aua = existing_aua = 0.0
nmnc_count = nmec_count = existing_count = 0
try:
    hh_lc = _compute_hh_lifecycle(accounts_dim, holdings, nna, data_as_of,
                                   window_days=365, accounts_v2_dim=accounts_v2_dim)
    if not hh_lc.empty:
        nmnc_rows = hh_lc[hh_lc['lifecycle'] == 'nmnc']
        nmec_rows  = hh_lc[hh_lc['lifecycle'] == 'nmec']
        existing_rows = hh_lc[hh_lc['lifecycle'] == 'existing']
        total_hh_aua = float(hh_lc['aua'].sum())
        nmnc_aua = float(nmnc_rows['aua'].sum())
        nmec_aua = float(nmec_rows['window_inflows'].sum())
        existing_aua = max(0.0, total_hh_aua - nmnc_aua - nmec_aua)
        nmnc_count  = int(len(nmnc_rows))
        nmec_count  = int(len(nmec_rows))
        existing_count = int(len(existing_rows))
except Exception as e:
    log(f'WARN: NMNC/NMEC lifecycle split failed: {e}')
```

Added `nmec_aua` + `nmec_count` to `header_total` dict. Updated `new_client_pct` denominator to `nmnc + nmec + existing`.

**Pre-commit gate:** PASS. **Commit:** `7bd1cf9be`. **S3 MATCH:** `7ee52d58...`.

---

### §3 — Task 3: INF_D_00c Leaderboard lifecycle_aua: `d8467140f`

**Root cause of gap:** `compute_leaderboard_entries()` had `_compute_new_clients_per_advisor()` (count only, old first_trade_date heuristic) but no lifecycle AUA breakdown. Each entry dict had no `lifecycle_aua` field.

**Approach:** Copy (not import — both scripts run standalone on EC2) `_hh_inception_from_accounts_v2()` + `_compute_hh_lifecycle()` from D_04 into D_00c with attribution comment.

**Changes:**
1. Two helper functions inserted before `compute_leaderboard_entries()` (lines 513ff in new file)
2. Per-advisor account_id sets built from `account_team` groupby after `new_clients_by_adv`
3. Inside advisor loop: filter holdings/nna/accounts_dim to per-advisor account_ids; call `_compute_hh_lifecycle()`; inject `lifecycle_aua: {nmnc, nmec, existing}` into entry dict
4. Before firm entry: compute firm-level lifecycle on full holdings; inject `lifecycle_aua: {nmnc, nmec, existing}` into firm entry dict

**accounts_v2_dim:** Not loaded in D_00c — calls default to `accounts_v2_dim=None`, so lifecycle falls back to `first_trade_date` from `accounts_dim`. Acceptable for initial ship; will upgrade when D_00c gains v2 loading.

**Pre-commit gate:** PASS. **Commit:** `d8467140f` (+151 lines). **S3 MATCH:** `325d2a6b...`.

---

### §4 — IWM book.json RAVC4-CLOSE

DE (`0.4.0_DE_ClientPlatform`) sent ACK at `20260429T142254Z` on prior session's `4bf137520` (IWM book.json, $86.19M / 297 HH / 801 accts). All 3 IWM drill artifacts confirmed live:
- `top_holdings.json` (prior session)
- `composition.json` (DS~D `2b568b08`)
- `book.json` (`4bf137520`)

Visual cycle still gated on DT push of portal/DEV `1511d0b` (INFLV2.007 InflectionInsightsPanel). RAVC4-CLOSE sent `20260429T142415Z`. Loop fully closed on DS~B side.

---

### §5 — INFLV2.005 Collision Avoidance

COO assigned INFLV2.005 Concentration Risk to DS~B. Detected DS~A had already shipped `INF_D_07.concentration_risk.py` (`ffd4484b3`) with RAVC4 to COO + AE at 13:45Z. Immediately flagged to COO and dropped the assignment (`20260429T135100Z`). COO ACK confirmed correct call — no duplicate work.

---

## Compiler Tools

| Tool | Run count | Notes |
|------|-----------|-------|
| `.tools/ds-commit-gate.sh` | 1 run (both files, single invocation) | Both PASS — py_compile + AST undefined-name + ruff |
| `.tools/safe-commit.sh` | 2 commits (`7bd1cf9be`, `d8467140f`) | Both NORMAL pathspec; single-file scope |
| `aws s3 cp` + ETag verify | 2 (D_04 + D_00c to s3://opal-data-inf/code/gold/) | Both MATCH: `7ee52d58...`, `325d2a6b...` |
| `git push` | 1 push covering both commits | CLOUD `cbc4f2713 → d8467140f` |

---

## RAVC Loops

| Counterparty | Topic | Status |
|---|---|---|
| 2.0.0_SA_COO | Task 1 audit | CLOSED (20260429T131850Z sent; ACK received) |
| 2.0.0_SA_COO | Tasks 2-4 RAVC-PENDING-VALIDATION | SENT (20260429T152102Z); awaiting INFGRD.003 chain + re-smoke |
| 0.6.1_AE_PartnerETL | INFLV2.002 D_04+D_00c shipped; signal request for chain | SENT (20260429T152108Z) |
| 0.4.0_DE_ClientPlatform | IWM book.json B4 drill artifacts confirmed | CLOSED (20260429T142415Z) |

---

## Lane Boundary

Clean. Edits scoped to:
- `data/orion/scripts/gold/INF_D_04.client_portal_summary.py` (lifecycle block replacement + 2 new fields in header_total)
- `data/orion/scripts/gold/INF_D_00c.portal_leaderboard.py` (2 helpers + per-advisor + firm lifecycle injection)

No cross-lane trespass. Did not touch: INF_D_02 (B lane prior session), INF_I_D03 (DS~D lane), INF_D_07 (DS~A lane), silver/orchestrator (AE scope).

---

## Outstanding (out of lane / pending validation)

- **INFGRD.003 chain** (AE 0.6.1 in progress): once chain completes, re-smoke D_04 `header_metrics.total.nmec_aua` + D_00c `leaderboard.lifecycle_aua` against post-filter $191M / 4-advisor platinum data.
- **INFLV2.009 chain rerun** (AE scope): triggered by COO after INFLV2.002 RAVC closes.
- **DT portal/DEV push** (`1511d0b`, INFLV2.007): visual cycle for IWM L2 drill — DT lane.
- **accounts_v2_dim in D_00c**: lifecycle falls back to first_trade_date until D_00c gains v2 dim loading. Acceptable; flag for future upgrade.

---

## Numbers Reference

- 2 gold scripts modified: INF_D_04 (24 lines net change), INF_D_00c (+151 lines)
- 2 commits, 2 S3 uploads, 2 ETag MATCH verifications
- 0 FORCE-BYPASS commits (all clean single-file pathspec)
- INFLV2.002 Task 1 audit: 3 gaps identified → 2 actioned (this session), 1 already covered (radial_12m ✓)

---

*Authored by `0.4.0_DS_ClientPlatform~B`. Session arc: 20260429T131850Z → 20260429T163000Z (~90 min active wall clock across loop ticks). 2 commits + audit + collision avoidance + 4 RAVC loops.*
