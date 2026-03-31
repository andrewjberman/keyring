# ADVI_PRICES.005 -- MBS Fix Silver Rebuild + 05e Validation -- 0.6.0_AE_PartnerETL

**Date:** 2026-03-27
**Start Time:** 11:30 PM ET (2026-03-26)
**End Time:** 11:40 PM ET (2026-03-26)
**Task Order:** ADVI_PRICES.005.ae-mbs-fix-gold-rerun.md

## Objective

Execute revised PRICES.005 scope (COO revision): silver rebuild + 05e validation only, NOT full gold rerun. Validate that the $107M MBS mispricing fix and T1 staleness cap reduce gold-vs-silver AUA gap to under 1%.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Receive GO from COO (3 messages) | GO + revised scope: silver rebuild + 05e only |
| 2 | Receive DT confirmation | e494e2be pushed to origin/CLOUD |
| 3 | Receive DS brief | MBS fix details (d39a3cdb) |
| 4 | git stash uncommitted GLDRST P3 changes | 14 files stashed |
| 5 | S3 sync silver scripts | 5 files uploaded to s3://opal-data-bd/code/silver/ |
| 6 | S3 sync gold scripts | 13 files uploaded to s3://opal-data-bd/code/gold/ |
| 7 | git stash pop | Uncommitted changes restored |
| 8 | S3 verify key files | 05e (21KB), inject (9KB), build_canonical (20KB) confirmed |
| 9 | SSM attempt 1 (`60dc587f`) | FAILED -- `set -o pipefail` not supported by /bin/sh |
| 10 | SSM Phase 1 (`b89e6de6`) | SUCCESS -- inject + build + 05e in sequence |
| 11 | **Discovery: inject before build is wrong order** | build_canonical_prices_v2 rebuilds from scratch, overwrites inject output |
| 12 | SSM Phase 2 (`65982b7d`) | SUCCESS -- re-inject AFTER build + re-run 05e |
| 13 | Messages delivered to COO + DS | Written to org/mcp/inbox/ (MCP broker down) |

---

## 05e Results -- Three-Phase Comparison

| Phase | Gold AUA | Silver AUA | Gap | Gap % |
|-------|----------|------------|-----|-------|
| Prior (GLDRST.002 run) | $1,553,803,595 | $1,611,595,100 | $57,791,505 | 3.72% |
| Phase 1: T1 staleness cap only | $1,604,383,535 | $1,611,595,100 | $7,211,565 | 0.447% |
| Phase 2: T1 cap + MBS overrides | $1,608,867,040 | $1,611,595,100 | $2,728,060 | **0.169%** |

### Impact Decomposition

- **T1 staleness cap:** +$50.6M gold AUA (stale T1 prices demoted, Yahoo Finance fills in with current market prices)
- **MBS overrides:** +$4.5M gold AUA (two MBS tranches corrected from par to market value)
- **Net:** gold moves from $1.554B to $1.609B, closing $55M of the $57.8M gap

### MBS Override Verification

| Asset | Override Price | Rows | Confirmed |
|-------|--------------|------|-----------|
| WELLS FARGO MBS 2007-15 | $7.12/unit | 5,018 (2007-01-01 to 2026-03-25) | YES -- scoped_override source |
| BANC AMERICA FDG 2006-2 | $201.57/unit | 5,278 (2006-01-01 to 2026-03-25) | YES -- scoped_override source |

Neither MBS account appears in the worst offenders list. Fix validated.

### build_canonical_prices_v2 Summary

- 10,496,895 rows, 9,981 assets, 2020-06-30 to 2026-03-25
- Sources: linear_interpolation 81.6%, yahoo_finance 16.5%, transaction_observed 1.9%
- T1 outlier cap: 30 assets capped at median (>50x threshold)
- Notable caps: CHIPOTLE pre-split $3,239 -> $55.45, DODGE & COX INCOME X $40,412 -> $12.49
- Elapsed: 113s on c6i.16xlarge

### Remaining Gap Drivers (Top 5 by abs contribution)

| Asset | Source | Gold MV | Gap | Accounts |
|-------|--------|---------|-----|----------|
| PATHFINDER DISCIPLINED US EQUITY ETF | transaction_observed | $98.3M | -$8.5M | 4,905 |
| PATHFINDER FOCUSED OPPORTUNITIES ETF | transaction_observed | $91.6M | -$7.8M | 4,905 |
| ISHARES CORE MSCI EAFE ETF | transaction_observed | $106.2M | -$7.9M | 4,045 |
| STATE STREET SPDR S&P 500 ETF | transaction_observed | $64.7M | -$5.9M | 3,041 |
| OPAL INTERNATIONAL DIVIDEND INCOME ETF | transaction_observed | $116.0M | -$3.5M | 4,678 |

These are structural pricing divergences (our transaction_observed prices vs custodian mark-to-market). Not addressable by overrides.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Re-ordered inject after build | build_canonical_prices_v2 rebuilds from scratch. Running inject first wastes the override work. Correct order: build -> inject -> 05e. |
| Dropped `set -o pipefail` from SSM | SSM runs /bin/sh (dash), not bash. `pipefail` is a bash extension. Used `set -e` only. |
| Wrote inbox messages directly (bypassing MCP) | MCP broker has generator context manager bug. Wrote .md files directly to org/mcp/inbox/{agent}/. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `.tmp_ssm_params.json` | SSM parameters for Phase 1 | No -- temp file, gitignored |
| `.tmp_ssm_params2.json` | SSM parameters for Phase 2 | No -- temp file, gitignored |
| `org/mcp/inbox/2.0.0_SA_COO/...` | Results message | No -- local only |
| `org/mcp/inbox/0.4.0_DS_ClientPlatform/...` | Results message | No -- local only |

---

## Blockers

None.

---

## Current State

**Status:** COMPLETE
**Active branch:** `CLOUD`

ADVI_PRICES.005 silver rebuild + 05e validation finished. AUA gap reduced from 3.72% ($57.8M) to 0.169% ($2.7M) through two mechanisms: T1 staleness cap (365-day demotion of stale transaction prices, +$50.6M) and MBS scoped overrides (WELLS FARGO MBS $7.12, BANC AMERICA $201.57, +$4.5M). Canonical prices rebuilt (10.5M rows, 9,981 assets) and uploaded to s3://opal-data-bd/silver/prices/canonical_prices.parquet (92.3 MB). Results reported to COO and DS via inbox. MCP broker has a generator context manager bug preventing send_message -- messages written directly to inbox folders.

---

## Next Steps

1. **[2.0.0_SA_COO] Decide on full gold rerun** -- 05e validates the prices are correct, but gold artifacts (parquets, portal JSON) still reflect old prices. Full gold rerun needed to propagate.
2. **[0.4.0_DS_ClientPlatform] Fix inject/build ordering in documentation** -- build must run before inject, not after. DS message had the wrong order.
3. **[0.6.0_AE_PartnerETL] SSM lesson learned** -- always use `set -e` not `set -euo pipefail` in SSM commands (runs /bin/sh, not bash)
4. **[1.0.0_SA_CTO or 0.4.0_DS_ClientPlatform] MCP broker bug** -- `'generator' object does not support the context manager protocol` on register_agent, set_summary, send_message. Broker needs fix.

**Do NOT:**
- Run inject before build -- build overwrites the inject output
- Use `set -o pipefail` in SSM commands -- SSM runs /bin/sh (dash)
- Assume 05e gap improvement propagates to gold artifacts without a full gold rerun
