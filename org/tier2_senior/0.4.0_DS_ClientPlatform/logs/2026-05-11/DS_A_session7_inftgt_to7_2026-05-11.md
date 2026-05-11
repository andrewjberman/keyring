# DS~A Session 7 — ADVI_INFTGT.TO-7 — Concentration Risk Wire-Up
**Date:** 2026-05-11  
**Agent:** 0.4.0_DS_ClientPlatform~A  
**TO:** ADVI_INFTGT.TO-7

## TL;DR

`concentration_risk.json` was `[]` (2 bytes) because `INF_D_07.load_latest_holdings()` always took the alphabetically-latest holdings partition (`keys[-1]`), which was `2026-05-08.parquet` — a file with **all-null market_values** (9,348 rows, 0 priced). The `dropna(subset=['market_value'])` eliminated every row, producing an empty artifact.

**Fix:** Scan backwards from latest (last 10 partitions), log each candidate, pick the first with at least 1 priced row. `2026-05-05.parquet` (9,326/9,330 rows priced) wins. Also added `.copy()` after `dropna` to suppress `SettingWithCopyWarning` from chained assignment.

**Result:** 294 HH rows | 37,730 bytes | 15 diversified / 194 moderate / 85 concentrated.

---

## Root Cause Investigation

### comp-pipescript io INF_D_07

```
READS (1):
  silver/accounts_dim/latest.parquet [HARDCODED]
WRITES: (none detected)
```

Confirmed: no holdings source registered. The script reads holdings dynamically via S3 list-objects (not a hardcoded path), so comp-pipescript doesn't see it in the manifest.

### S3 probe — holdings pricing coverage

| Partition | Rows | Priced | All-null? |
|---|---|---|---|
| 2026-05-08.parquet | 9,348 | 0 | YES |
| 2026-05-07.parquet | 9,351 | 0 | YES |
| 2026-05-06.parquet | 9,339 | 0 | YES |
| 2026-05-05.parquet | 9,330 | 9,326 | no |
| 2026-05-04.parquet | 9,315 | 9,311 | no |

Pricing gap: `canonical_prices` enrichment hasn't run for the 4 most recent holding dates. The fix uses the latest priced partition rather than the latest date.

### Join verification (pre-fix)

- Accounts dim: 835 accounts / 307 households
- Holdings 2026-05-04: 782 unique accounts, after join 99.5% match rate → 294 households

---

## Files Modified

| File | Change |
|------|--------|
| `data/orion/scripts/gold/INF_D_07.concentration_risk.py` | `load_latest_holdings()`: scan backwards for latest priced partition (last 10); `.copy()` after dropna |
| `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI_INFTGT.TO-7.ds-concentration-risk-wire-up.md` | Task order authored + marked complete |

---

## Compiler Tools

| Tool | Result |
|---|---|
| `comp-pipescript io INF_D_07` | Reads: silver/accounts_dim only (holdings dynamic) |
| `.tools/ds-commit-gate.sh` | PASS (py_compile + AST + ruff) |
| Manual MD5 verify (local vs S3) | ae4cadcc93ad2103694c7841d7a5d94b == ae4cadcc93ad2103694c7841d7a5d94b MATCH |
| Dry-run rc | 0 |
| Upload rc | 0 |

---

## Deploy Evidence

| Step | Result |
|---|---|
| Commit SHA | `1bbc22a8f` |
| Author | `0.4.0_DS_ClientPlatform~A` |
| Push | `origin/CLOUD` up to date |
| S3 code upload | `s3://opal-data-inf/code/gold/INF_D_07.concentration_risk.py` MATCH |
| Artifact upload | `s3://opal-data-inf/platinum/firm/concentration_risk.json` 37,730 bytes |
| Artifact row count | 294 households |
| Sample validation | HH 463: $4.4M aua, 20.8% top1 (LLY), tier=moderate |

---

## Output Summary

```
294 households | diversified=15 | moderate=194 | concentrated=85
Holdings source: gold/holdings/2026-05-05.parquet (latest priced partition)
```

---

## Cross-pod Notes

- The 4-day pricing gap (2026-05-05..08 unpriced) is a known state — canonical_prices enrichment
  for INF hasn't run for those dates. The backwards-scan is the correct steady-state fix; the
  artifact will self-update to later dates as pricing catches up.
- Flagged to COO in RAVC2: pricing gap depth (4 days) should be monitored; if it grows > 10 days,
  the 10-partition scan window may need extending.
