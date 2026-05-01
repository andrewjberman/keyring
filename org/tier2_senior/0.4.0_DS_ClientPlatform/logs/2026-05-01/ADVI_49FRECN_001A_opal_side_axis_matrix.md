# Session Log — ADVI_49FRECN.001A — Opal-Side Axis Matrix

**Agent:** 0.4.0_DS_ClientPlatform~A
**Date:** 2026-05-01
**Task Order:** ADVI_49FRECN.001A — Phase 0 Slice A: Opal-Side Reference Snapshot + Per-Axis Matrix Shell
**Status:** COMPLETE

---

## Summary

Executed Phase 0 Slice A of the 49Financial reconciliation investigation. Extracted Opal-side reference numbers from gold and silver artifacts at reference date 2026-04-29, built all three axis matrices (per-advisor, per-account-type, per-custodian), saved the account-id flat list, and appended Slice A section to the shared report stub.

Key finding: Andrew confirmed during session that BD Silver/Allocations is the true active account source at 6,611. Our gold-processed count is 6,032. The 579-account gap is DS~B's investigation scope.

---

## Compiler Tools

| Tool | Script | Result |
|------|--------|--------|
| comp-pipescript io | D_00.portal_aggregates.py | OK — 18 reads, 5 writes; no COLUMN GAPS |
| comp-pipescript io | D_02.advisor_client_detail.py | OK — 17 reads, 4 writes; no COLUMN GAPS |
| comp-pipescript io | A_00.accounts_dimension.py | OK — 1 read, 1 write; no COLUMN GAPS |

All three comp-pipescript io runs completed before reading any gold script. No COLUMN GAPS surfaced.

---

## Artifacts Read

| Artifact | S3 Key | Notes |
|---------|--------|-------|
| header_metrics.json | gold/artifacts/summary/header_metrics.json | Firm totals, by_architect top-10 (truncated) |
| account_performance.parquet | gold/timeseries/account_performance.parquet | 6,030,059 rows total; filtered to date=2026-04-29 (6,032 rows) |
| accounts_dimension_latest.parquet | gold/dimensions/accounts_dimension_latest.parquet | 10,120 rows; 9,750 active; joined for account_type |
| silver/allocations/2026-04-29.parquet | silver/allocations/2026-04-29.parquet | 6,611 rows — BD truth source |

---

## Key Findings

### Account Count Reconciliation

```
BD Silver/Allocations (2026-04-29):  6,611  $1,730.79M  (BD truth per Andrew)
Gold account_performance (2026-04-29): 6,032  $1,659.48M
Portal header_metrics:               6,025  $1,657.87M
49F display:                         6,611  ~$1,717-1,720M implied
```

- 579-account gap between silver and gold (DS~B scope: bronze→silver→gold trace)
- 7-account gap between account_performance and header_metrics (D_00 filtering — likely AUA=0 exclusion)
- AUA gap: silver $1,730.79M vs gold $1,659.48M = $71.31M (includes negative-balance accounts in silver)

### Per-Account-Type (Gold, 2026-04-29, top 5 by AUA)

| Type | Accounts | AUA |
|------|---------|-----|
| IRA | 2,066 | $528.18M |
| Brokerage | 1,304 | $407.91M |
| Joint | 569 | $200.83M |
| Trust | 169 | $200.15M |
| RothIRA | 1,068 | $59.84M |

### Per-Advisor (Gold, 2026-04-29, top 5 by AUA)

| Advisor | Accounts | AUA |
|---------|---------|-----|
| 49F House | 2,681 | $537.30M |
| Travis Penfield | 197 | $317.44M |
| Kyle Sims | 294 | $102.54M |
| Greg Rosner | 245 | $71.99M |
| Hunter Lloyd | 133 | $70.23M |

CAVEAT: "49F House" (2,681 accounts) is a firm-level pool — 49F likely attributes these to individual advisors.

### Custodian Finding

No explicit custodian field in gold OR silver/allocations. Inferred from rep_code + account number format:
- Schwab dominant: rep_code 8242234 = 6,023/6,611 (91.1%) + 8-digit account number format confirms
- No RepCode: 542 accounts (8.2%)
- Other codes: 46 accounts

---

## Deliverables Produced

| Item | Path |
|------|------|
| Reconciliation report (Slice A) | docs/architecture/49F_RECONCILIATION_2026-05-01.md |
| Account-id flat list | tmp/49frecn/opal_accounts_2026-04-29.parquet |
| TO status flipped | open -> pending (ADVI_49FRECN.001A) |

---

## Files Modified

| File | Change |
|------|--------|
| docs/architecture/49F_RECONCILIATION_2026-05-01.md | Created — Slice A section with 3 axis matrices + firm totals + caveats |
| org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI_49FRECN.001A.ds-a-opal-side-axis-matrix.md | Status: open -> pending |
| org/tier2_senior/0.4.0_DS_ClientPlatform/logs/2026-05-01/ADVI_49FRECN_001A_opal_side_axis_matrix.md | This log |

Note: tmp/49frecn/opal_accounts_2026-04-29.parquet is NOT committed (tmp/ is gitignored). DS~B should request via MCP message for the file path.

---

## Next Steps

[DS~B] Receive RAVC4 with: commit ref, parquet path (tmp/49frecn/opal_accounts_2026-04-29.parquet), link to Slice A section in docs/architecture/49F_RECONCILIATION_2026-05-01.md. Use account-id list for set-diff against 49F's 6,611.

[DS~B] Investigate the 579-account gap: silver/allocations 6,611 → gold 6,032. Andrew confirmed silver/allocations is the truth source.

[DS~B] Resolve "49F House" attribution (2,681 accounts): request 49F per-advisor mapping.

[DS~C] Receives note: per-account-type silver vocabulary confirmed same as gold. Silver `account_category` field (Retirement/Investment/Trust/Corporate/Other) may be more useful than `account_type` for 49F comparison.
