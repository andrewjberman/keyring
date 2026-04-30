# Session Log — DIAGFIX.012: employee_leaderboard joe_brandenbur g advisor_id fix

**Agent:** 0.4.0_DS_ClientPlatform
**Date:** 2026-04-30
**Session type:** Context-resumption continuation (Wave D)
**Session window:** ~19:44Z – 19:47Z

---

## Context at Resumption

Continued from prior session (session_histbf003_client_universe_fix.md). Wave D investigation
identified that the employee_leaderboard artifact was missing the `joe_brandenbur g` entry
(Joe Brandenburg, rep_id=6, ~$16.47M AUA). Portal layout.ts expects 4 allowedAdvisorKeys
including `joe_brandenbur g`; artifact had only 3 (peter_lee, patrick_scanlan,
inflection_wealth_management).

---

## Root Cause

`INF_C_07._apply_accounts_v2_advisor_key_override()` in
`data/orion/scripts/gold/INF_C_07.advisor_attribution.py`:

1. Converted `df['account_id']` to str (line 144) for the accounts_v2 lookup merge.
2. Applied the representative_name → advisor_key slug override correctly.
3. **Never restored the original dtype** before returning.

In `main()` at line 202:
```python
acct_team = latest[['account_id', 'total_aua']].merge(acct_dim, on='account_id', how='outer')
```
`latest` (account_performance.parquet) has `account_id: int64`.
`acct_dim` (after override) has `account_id: object` (str).
The outer merge produced NaN account_ids for all accounts, effectively discarding
the joe_brandenbur g advisor_key override. account_team reported 3 advisors; the
$16.1M attributed to Joe Brandenburg rolled silently into `inflection_wealth_management`.

---

## Fix

`data/orion/scripts/gold/INF_C_07.advisor_attribution.py` — commit `f5c4caae2`:

```python
# Before the str conversion, save original dtype
_orig_acct_id_dtype = df['account_id'].dtype
df['account_id'] = df['account_id'].astype(str).str.strip()
df = df.merge(lookup, on='account_id', how='left')
# ... override logic ...
df = df.drop(columns=['_key_override'])
# Restore original dtype so downstream merge with account_performance (int64) matches correctly.
try:
    df['account_id'] = pd.to_numeric(df['account_id'], errors='coerce').astype(_orig_acct_id_dtype)
except Exception:
    pass
```

---

## Validation

ds-commit-gate.sh: PASS (py_compile + AST scan + ruff)

INF_C_07 re-run (inf-gold-layer-runner, 19:44Z):
```
FLAG2: advisor_key override via accounts_v2 (snapshot_date=2026-04-29): 3 -> 4 unique advisors
account_team: 836 rows, 4 advisors
```

INF_D_00c re-run (19:45Z):
```
Account team: 836 rows, 4 advisors
QTD: 4 advisors, total_aua=$197,355,918
YTD: 4 advisors, total_aua=$197,355,918
MAX: 4 advisors, total_aua=$197,355,918
```

Artifact verification (s3://opal-data-inf/platinum/firm/leaderboard.json, generated 19:45Z):
- peter_lee: $160.6M
- patrick_scanlan: $20.3M
- **joe_brandenbur g: $16.1M** (RESTORED)
- inflection_wealth_management: $360K

All 4 allowedAdvisorKeys in portal layout.ts now present in artifact.

---

## Secondary Issue (Non-Blocking, DIAGFIX.013)

INF_D_00c lifecycle split produced WARNs for all advisors:
```
WARN: lifecycle split failed for joe_brandenbur g: You are trying to merge on int64 and object
columns for key 'account_id'. If you wish to proceed you should use pd.concat
```
Same dtype pattern exists in INF_D_00c's internal lifecycle (new_client vs existing_client)
merge path. NNA totals compute correctly (fallback path used); joe_brandenbur g shows
nna=0 for QTD rather than lifecycle-broken-down NNA. Flagged for DIAGFIX.013.

---

## Commits This Session

| Commit | Description |
|--------|-------------|
| `f5c4caae2` | fix(ADVI_INFLEC.DIAGFIX.012): restore account_id dtype after accounts_v2 override in INF_C_07 |

Pushed to `origin/CLOUD`.

---

## Open Items Carried Forward

| Item | Gate | Status |
|------|------|--------|
| DIAGFIX.013: INF_D_00c lifecycle split dtype fix | Not yet scoped | Follow-up |
| DE re-validation of leaderboard artifact | COO ack | Open |
| HISTBF.003 Phase 1 bronze execution | CTO+COO wave plan GO | ON HOLD |
| accounts_v2 silver re-run (Fidelity_LH) | Next scheduled window | Unblocked |
| Ghost household orphan account_id confirmation | Pre-Phase-1 | On hold |
| HISTBF.004 silver backfill | HISTBF.003 Phase 1 close | On hold |
