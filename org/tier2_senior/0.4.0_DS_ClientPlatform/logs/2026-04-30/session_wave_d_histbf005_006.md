# Session Log — Wave D + HISTBF.005/006 Wave A bronze pull scripts
## Agent: 0.4.0_DS_ClientPlatform~D | Date: 2026-04-30

---

## TOs / Scope This Session

1. **Wave D**: employee_leaderboard advisor_id fix (INF_D_00c)
2. **INF_D_02 S3 deploy**: line 604 fix confirmed deployed (MATCH)
3. **HISTBF.005 Wave A**: pull_inflection_transactions_rest.py
4. **HISTBF.006 Wave A**: pull_inflection_performance_rest.py
5. **294 vs 314 client gap investigation**

---

## Wave D — employee_leaderboard advisor_id fix

### Root Cause
`INF_D_00c.portal_leaderboard.py` line 689 computed `all_advisors` from
`set(aua_by_adv) | set(nna_by_adv)`. Holdings parquet (gold/canonical/holdings_*.parquet)
carries `joe_bradford` (67 accounts, $16.1M, rep_bucket='individual') as a 4th advisor key.
But `gold/views/account_team.parquet` (authoritative INF_C_07 output) maps those same 67
accounts to `inflection_wealth_management`.

### Fix
Commit `8afd5c384`:
- Restrict `all_advisors` to account_team individual advisors (authoritative set)
- Re-route orphan AUA (joe_bradford $16.1M) to `firm_aua` so totals balance

### Verification
- INF_D_00c --upload run: 3 advisors in all 3 windows
  - QTD/YTD/MAX: ['peter_lee', 'patrick_scanlan', 'inflection_wealth_management']
- Matches allowedAdvisorKeys exactly
- total_aua=$197,355,918 (unchanged — firm entry absorbs $16.47M)
- firm entry: peter_lee=$160.6M, patrick_scanlan=$20.3M, IWM=$16.47M
- gold/artifacts/employee_leaderboard.json + platinum/firm/leaderboard.json updated
- S3 MATCH: 9ef404f34060c037d199dd5c59b2970d

---

## INF_D_02 S3 Deploy Fix

Commit `5d0a95218` (line 604 dtype fix) was on CLOUD but S3 was stale (MD5 mismatch).
Uploaded and confirmed MATCH. Dry-run clean: 3 advisors, no ValueError.

---

## HISTBF.005 — pull_inflection_transactions_rest.py

### Changes from prior version
- Output path: single parquet → per-account JSON at
  `bronze/orion-api-v2/transactions/{account_id}/data.json`
- 404 handling: now treated as success (empty JSON written)
- Resume: per-account JSON existence check
- Project attribution: HISTBF.003 → HISTBF.005

### Key facts
- Endpoint: GET /api/v1/Portfolio/Accounts/{accountId}/Transactions
- Universe: accounts_v2 silver (~590 accounts)
- Rate limiter dim_name="transactions"
- Assert fresh JWT at startup

**Commit:** e778fee0c  
**S3 MATCH:** code/bronze/pull_inflection_transactions_rest.py — MATCH

---

## HISTBF.006 — pull_inflection_performance_rest.py

### Changes from prior version
- Output path: single parquet → per-client JSON at
  `bronze/orion-api-v2/performance/{client_id}/data.json`
- Stores full raw Orion JSON (not pre-parsed detail rows)
- Resume: per-client JSON existence check
- Project attribution: HISTBF.003 → HISTBF.006
- HARD LIMIT comment added: no date window params

### Key facts
- Endpoint: GET /api/v1/Portfolio/Clients/{clientId}/Performance
- Universe: household_rep_mapping (313 clients)
- Rate limiter dim_name="performance"
- 404 = SKIP (success, log INFO)
- HARD LIMIT: no date window params — inception-to-date only

**Commit:** e778fee0c  
**S3 MATCH:** code/bronze/pull_inflection_performance_rest.py — MATCH

---

## 294 vs 314 Client Gap Investigation

| Source | household_ids | Notes |
|--------|--------------|-------|
| accounts_v2 (2026-04-29) | 294 | Missing 19 households |
| household_rep_mapping (2026-04-29) | 313 | Authoritative (includes Fidelity_LH + ghost HH) |
| COO-cited gold chain | 314 | 1 more than hrm; likely snapshot drift |

**Finding:** 19 households are in household_rep_mapping but not accounts_v2. These are
ghost/Fidelity_LH households that exist in Orion but don't appear in NewPortfolio accounts.

**Recommendation:** HISTBF.003 full backfill MUST use household_rep_mapping (313) as universe,
matching pull_inflection_assets_v2.py current behavior. NOT accounts_v2.

**RAVC to COO sent.** HISTBF.003 full backfill held pending GO.

---

## MCPs Sent

1. COO: Wave D COMPLETE (leaderboard advisor_ids corrected) + INF_D_02 MATCH
2. AE 0.6.1: HISTBF.005 + HISTBF.006 MATCH — chain reg gate signal
3. COO: RAVC4 HISTBF.005 + HISTBF.006 + client gap findings

---

## Pending

- HISTBF.003 full backfill: awaiting GO from COO after client gap source confirmed
- Wave B EC2 dispatch: AE-owned (after chain reg update)
- DS~B: convert_transactions_to_silver.py + convert_performance_to_silver.py
- ORNREN.003: on hold, no GO
