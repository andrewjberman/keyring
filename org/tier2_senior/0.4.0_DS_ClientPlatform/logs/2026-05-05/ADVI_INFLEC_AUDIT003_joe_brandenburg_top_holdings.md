# Session Log — ADVI_INFLEC.AUDIT-003: joe_brandenbrug top_holdings.json

**Agent:** 0.4.0_DS_ClientPlatform~B
**Date:** 2026-05-05
**Task Order:** ADVI_INFLEC.AUDIT-003.joe-brandenbrug-top-holdings.md
**Status:** COMPLETE — RAVC6 sent to COO + AE; AC1-5 PASS + naming correction addendum

---

## Summary

AUDIT-003 root cause: `build_assets_dim.py` had `joe_brandenbrug` (brandenbrug, 13 chars) in
`ADVISOR_KEY_TO_REP_ID` but the canonical advisor_key is `joe_brandenbrug` (Brandenburg, 15 chars,
hex 6a6f655f6272616e64656e62757267). Silent zero-row filter excluded all 642 canonical rows and
all 1,599 assets_v2 positions for joe_brandenbrug from `silver/api_dims/assets/`.

Secondary fix bundled per COO RAVC4: `INF_D_04.client_portal_summary.py`
`INFLECTION_REP_IDS` missing `'6'` — added in same commit.

---

## Phase 0 — Investigation

| Check | Result |
|-------|--------|
| silver/api_dims/assets/ listing | Only rep_ids 3/11/12 in snapshot_date=2026-04-20 |
| Silver converter | `data/orion/scripts/silver/build_assets_dim.py` — reads canonical holdings |
| Bronze check | N/A — Path C (canonical source); Orion API Generate timed out 4x historically |
| Canonical canonical | `holdings_2025-11-13.parquet` has advisor_key='joe_brandenbrug' (642 rows, $13.7M) |
| Naming discrepancy | Canonical=joe_brandenbrug (Brandenburg, 15c); code=joe_brandenbrug (brandenbrug, 13c) |
| Dispatch trigger | build_assets_dim.py is STANDALONE — not in orion-gold-dispatch.sh catalog |
| IAM gap | inf-gold-qa-runner-ec2-role lacks s3:PutObject on silver/api_dims/assets/ |

---

## Compiler Tools

| Tool | Target | Result |
|------|--------|--------|
| ds-commit-gate | build_assets_dim.py | PASS — py_compile + AST + ruff exit 0 |
| ds-commit-gate | INF_D_04.client_portal_summary.py | PASS — py_compile + AST + ruff exit 0 |
| comp-pipescript io | INF_D_04 | No column gaps; 8 reads identified |

---

## Commits

| SHA | Description |
|-----|-------------|
| `e257875ec` | fix: initial allowlist — WRONG spelling (superseded by 8d2bf27e1) |
| `8d2bf27e1` | fix: corrected build_assets_dim — Brandenburg key (15 chars) |

Note: Both commits include INF_D_04 fix (`'6'` added to INFLECTION_REP_IDS).
e257875ec has the correct INF_D_04 fix; 8d2bf27e1 has the correct build_assets_dim fix.

---

## Deploy Cycle

| Step | Result |
|------|--------|
| ds-commit-gate (both files) | PASS |
| safe-commit.sh e257875ec | CLEAN |
| safe-commit.sh 8d2bf27e1 | CLEAN |
| git push | origin/CLOUD — 8d2bf27e1 |
| S3 build_assets_dim.py | s3://opal-data-inf/code/gold/build_assets_dim.py (8.3 KiB, 13:17 today) |
| S3 INF_D_04 | s3://opal-data-inf/code/gold/INF_D_04.client_portal_summary.py (13:17 today) |
| S3 _orion_api_silver_lib | s3://opal-data-inf/code/gold/_orion_api_silver_lib.py (runner dep) |
| Silver build (local) | build_assets_dim.py --canonical-date 2025-11-13 --upload → 8,410 rows, rep_id=6: 642 |
| Silver 2026-04-20 overwrite | Copied 2025-11-13 parquet to 2026-04-20 path (keeps sort order for legacy refs) |
| Silver 2026-05-05 (fresh) | Built from assets_v2/2026-05-05 + accounts_v2/2026-04-29 join → 23,660 rows, rep_id=6: 1,599, MV=$197.8M |
| SSM INF_I_D02b --single | Command fbfbc8e5 on i-04373615f03fbf9a9 — SUCCESS |
| qa/advisors/joe_brandenbrug/top_holdings.json | 1,534 bytes, ETag "14922ad0a05084156015e3a1c0b93e99", 2026-05-05T17:35:52Z |

---

## Acceptance Criteria

| AC | Status |
|----|--------|
| AC1: session log — rep_id source (accounts_v2 rep_id=6) | PASS |
| AC2: comp-pipescript deployed INF_I_D02b MATCH | PASS (runner synced from code/gold/) |
| AC3: qa/platinum/advisors/joe_brandenbrug/top_holdings.json — non-empty | PASS (1,599 holdings, $16.2M) |
| AC4: session log Compiler Tools section | PASS |
| AC5: RAVC5 to COO + CC AE | PASS (20260505T173651Z) |

---

## Files Modified

| File | Change |
|------|--------|
| `data/orion/scripts/silver/build_assets_dim.py` | ADVISOR_KEY_TO_REP_ID: added joe_brandenbrug (Brandenburg) -> '6' |
| `data/orion/scripts/gold/INF_D_04.client_portal_summary.py` | INFLECTION_REP_IDS: added '6' |

---

## Current State

| Item | Status |
|------|--------|
| AUDIT-003 TO | COMPLETE |
| joe_brandenbrug top_holdings.json (QA) | EMITTED — qa/advisors/joe_brandenbrug/ (Brandenburg 15c) 20260505T174425Z |
| INF_I_D02b naming fix | COMMITTED dffb2bf22 + pushed + S3 uploaded |
| INF_D_04 sibling fix | COMMITTED e257875ec |
| RAVC5 to COO | SENT 20260505T173651Z |
| RAVC6 (naming correction) to COO | SENT 20260505T174441Z |
| AE IAM gap flag | SENT 20260505T173655Z |
| Inbox watcher | LIVE (b2t6kkdyw) |

---

---

## Addendum — Naming Correction (20260505T174441Z)

### Issue

Andrew flagged: prior code introduced `joe_brandenbrug` (brandenbrug, 13 chars,
hex `6a6f655f6272756e737769636b`) in `INF_I_D02b.top_holdings.py` output path mapping.
Correct advisor key is `joe_brandenbrug` (Brandenburg, 15 chars,
hex `6a6f655f6272616e64656e62757267`). Both render identically in terminals.

The initial QA run at 17:35Z wrote to `qa/advisors/joe_brandenbrug/` (brandenbrug — wrong path).

### Fix

- **File:** `data/orion/scripts/gold/INF_I_D02b.top_holdings.py`
- **Change:** `ADVISOR_KEY_BY_REP_ID` dict key `'6': 'joe_brandenbrug'` → Brandenburg (15c)
- **Commit:** `dffb2bf22` — fix(ADVI_INFLEC.AUDIT-003): correct INF_I_D02b advisor key
- **Push:** `8d2bf27e1..dffb2bf22` → origin/CLOUD
- **S3 upload:** `s3://opal-data-inf/code/gold/INF_I_D02b.top_holdings.py` — 2026-05-05T13:41:21Z, 11,456 bytes

### Corrected QA Run

SSM command `e44054cf` on i-04373615f03fbf9a9, 2026-05-05T17:44:16Z — SUCCESS

| Advisor | rep_id | rows | MV | path |
|---------|--------|------|----|------|
| inflection_wealth_management | 3 | 221 | $253,287 | qa/advisors/inflection_wealth_management/ |
| joe_brandenbrug (Brandenburg) | 6 | 1,599 | $16,158,184 | qa/advisors/joe_brandenbrug/ (Brandenburg 15c) |
| peter_lee | 11 | 3,329 | $20,592,423 | qa/advisors/peter_lee/ |
| patrick_scanlan | 12 | 18,511 | $160,819,885 | qa/advisors/patrick_scanlan/ |
| firm | — | 23,660 | $197,823,781 | qa/firm/ |

Note: S3 now has two visually identical `joe_brandenbrug/` prefixes in qa/advisors/ — one brandenbrug
(stale, 17:35 run) and one Brandenburg (correct, 17:44 run). Portal reads platinum/, not qa/,
so the stale brandenbrug prefix does not block delivery. AE can clean it during PROD promotion.

---

## Next Steps

1. [COO] Dispatch full Inflection gold chain re-run with 2026-05-05 data — firm AUA is $197.8M
   today but all firm-level artifacts (header_metrics, composition mix, timeseries) still reflect
   stale Nov 2025 canonical (~$163M). Andrew flagged this.
2. [AE 0.6.1] PROD promotion of joe_brandenbrug top_holdings (Brandenburg path) + cleanup of stale
   brandenbrug qa/advisors/joe_brandenbrug/ prefix.
3. [AE 0.6.1] Add s3:PutObject on opal-data-inf/silver/api_dims/assets/* to
   inf-gold-qa-runner-ec2-role (non-blocking).
