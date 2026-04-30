# Session Wrap — ADVI_HISTBF.001 Phase 0 (REST Discovery + Lookback Verification)

**Agent:** 0.4.0_DS_ClientPlatform_B
**Date:** 2026-04-30
**TO:** ADVI_HISTBF.001 Phase 0 continuation
**Prior log:** `histbf_phase0_probe.md` (same date)

---

## What Happened This Session (continuation)

### Pivot: PARTIAL → SUPPORTED Investigation

User directed: "explore all the partials to find strategies to get to SUPPORTED."

**Performance:** Annual window chunking proven empirically.
- 3 annual windows tested: 2020-2021 (13.7s), 2021-2022 (13.3s), 2022-2023 (19.7s) — all SUCCESS
- 5y+ timeout was a compute issue, not a data availability issue
- Reclassified: **SUPPORTED**

**Billing + Activity:** Exhaustive rep attribution investigation — 12+ API probe patterns.
- No historical rep assignment data exists in Orion API (architecturally current-state only)
- Endpoints probed: `/Representatives/Audit`, `/Representatives/History`, `/Clients/History`, `/Clients/{id}/RepresentativeHistory`, `/Reporting/History/Representatives`, `/Billing/Invoices`, `/Billing/Periods`, `/Billing/FeeSchedules`, `/Billing/History`
- All returned 404 or silently ignored date params
- `startDate` confirmed = original inception date, NOT rep transfer date
- Reclassified: **PATH-TO-SUPPORTED** (requires manual advisor transition table from Inflection)

Written: `docs/data/inflec_histbf_upgrade_paths.md` — committed `93e704001`

---

### Major Pivot: Dashboard HAR + Screenshot Analysis

User provided: 4 dashboard screenshots of client 449 (Thomas Henderson) + HAR file.

**Finding:** Orion dashboard backed by direct REST endpoints + SignalR WebSocket — not primarily Envision.

Direct probes on client 449 found:

**Transaction endpoint:** `GET /api/v1/Portfolio/Accounts/{id}/Transactions`
- No pagination limit (removing $top returns full 6,584 records for client, 3,454 for account 1063)
- Full history from 2020-06-04 across all accounts
- 22 transaction type codes decoded; key types for HISTBF:
  - `transTypeId=24` = Management Fee (144 records, -$169,249.46 total for client 449)
  - `transTypeId=110` = Fee Credit (reversal)
  - `transTypeId=8` = Client Contribution
  - `transTypeId=51` = Client Distribution

**Performance endpoint:** `GET /api/v1/Portfolio/Clients/{id}/Performance`
- 309 weekly TWR factors from 2020-06-04 to present
- Factor = weekly return multiplier; cumulative = prod(factor) - 1
- Full historical access confirmed

**Assets endpoint:** `GET /api/v1/Portfolio/Clients/{id}/Assets/{MM-DD-YYYY}`
- Already known SUPPORTED; reconfirmed MV $1.70M at 2020-06-04 through $4.70M at 2026-04-30

Written: `docs/data/inflec_histbf_transaction_endpoint_discovery.md` — committed `51ae1d972`

---

### Lookback Verification

User asked: "and do those items have full time series lookback?"

Verified per-account for client 449:

| Account | Count | Earliest | Latest | Fee txns |
|---------|-------|---------|--------|---------|
| 792 | 2,855 | 2020-06-04 | 2026-04-27 | 33 |
| 471 | 134 | 2020-12-30 | 2026-03-31 | 0 |
| 1063 | 3,454 | 2020-06-04 | 2026-04-15 | 95 |
| 951 | 123 | 2025-03-21 | 2026-04-09 | 10 |
| 1427 | 388 | 2025-11-21 | 2026-04-27 | 6 |
| Total | 6,584 | 2020-06-04 | | 144 |

**Key boundaries:**
- True Inflection origin: **2020-06-04** (2020-05-25 and 2020-05-26 assets return $0 MV)
- Late-opening accounts (951, 1427) have no pre-open data — not an API limitation, no data existed
- Total Inflection clients: **314** (revised from 294 Phase 0 estimate)
- Performance: 309 weekly factors from 2020-06-04, full lookback confirmed
- Verdict: **Full historical lookback confirmed** for all 3 HISTBF dims via REST transactions

---

## Final Phase 0 Classification

| Dim | Final Class | Method |
|-----|------------|--------|
| positions_mv | SUPPORTED | REST Assets endpoint |
| assets_v2 | SUPPORTED | REST Assets endpoint |
| accounts_v2 | CURRENT-ONLY | No historical state |
| household_rep_mapping | CURRENT-ONLY | No historical state |
| household | CURRENT-ONLY | Envision current-state only |
| billing (fees) | **SUPPORTED** | REST Transactions transTypeId=24,110 |
| activity (flows) | **SUPPORTED** | REST Transactions transTypeId=8,51 |
| performance (TWR) | **SUPPORTED** | REST Performance weekly factors |

**5 of 8 dims SUPPORTED. 3 CURRENT-ONLY (no path via any Orion API).**

---

## Commits This Session (continuation)

| Commit | Description |
|--------|-------------|
| `93e704001` | docs(ADVI_HISTBF.001): PARTIAL->SUPPORTED upgrade path investigation |
| `51ae1d972` | docs(ADVI_HISTBF.001): REST transaction endpoint discovery + revised classification |
| (this session wrap) | log(ADVI_HISTBF.001): session wrap REST discovery + lookback verification |

---

## Phase 1 Gates (unchanged)
1. JWTRES.001 ship (JWT refresh resilience before full backfill run)
2. CTO review of updated eligibility matrix
3. AE 0.6.1 Phase 1 scope decision (REST-only path, ~22K calls vs original 450K)
4. Inflection advisor transition table (for billing/activity rep attribution — Path 1 from upgrade_paths.md)

## RAVC4 Status
Sending to COO + cc AE 0.6.1 upon commit of this log.
