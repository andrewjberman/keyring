# Session Log — ADVI_INFLEC SCOPEFIX Advisor Chain

**Agent:** 0.6.1_AE_PartnerETL
**Date:** 2026-04-27
**Session period:** ~17:20–18:15 ET
**Triggered by:** COO dispatch — Andrew seeing blank advisor intelligence panels

---

## Summary

Full SCOPEFIX chain executed to fix blank Inflection advisor panels. Root cause:
`_apply_scopefix()` in `convert_orion_to_silver.py` was filtering out all
`rep_bucket='individual'` rows, silencing individual advisor accounts at the silver layer.
Six scripts patched (across 3 COO overrides), chain ran through multiple type-cascade
failures before completing cleanly.

Final result: 10 advisor books / 995 client details / 9 advisor compositions live on S3.

---

## Root Cause Chain

```
silver/transactions (SCOPEFIX filter firm-only)
  → A_00 accounts_dim (zero individual advisors)
  → C_07 account_team (zero advisor_key entries)
  → D_02 platinum/advisors/*/book.json (zero books)
  → I_D03 platinum/advisors/*/composition.json (zero compositions)
```

Prior D_02/I_D03 script-level fixes (~A lane and base DS) were patching symptoms.
SCOPEFIX in silver was the actual root cause.

---

## Execution Log

| Step | Script | SSM | Result | Notes |
|---|---|---|---|---|
| Silver rebuild | convert_orion_to_silver.py (f2dfee9a) | 41e99792 | PASS | 3,320,073 individual rows now flowing |
| A_00 | accounts_dimension (pre-patch) | 8ff7b0ae | PASS | 2,808 accounts |
| C_01 | canonical_nna | e3fbb0b4 | PASS | NNA partitions rebuilt |
| C_07 | advisor_attribution | 3859370d | FAIL | household_id 'unknown' ArrowInvalid (pyarrow double schema) |
| — | COO override f84c2df4 | — | — | A_00: pd.to_numeric(errors='coerce') on household_id |
| A_00 (re-run) | accounts_dimension (f84c2df4) | 63615c2f | PASS | 2,808 accounts, float64 household_id |
| C_07 (re-run) | advisor_attribution | 1ba57f83 | PASS | account_team 2,818 rows, 11 advisors |
| D_02 attempt 1 | advisor_client_detail (345d6e3c) | 94460566 | FAIL | int(hh_id) fails on float 1000.0 |
| — | COO override 0ac97913 | — | — | D_02 line 309: int(hh_id) → int(float(hh_id)) |
| D_02 attempt 2 | advisor_client_detail (0ac97913) | bff1ce7b | FAIL | int(float('unknown')) — C_07 fillna('unknown') reverts NaN |
| — | COO override 412e2378 | — | — | D_02 lines 309/430/445: 4-case guard (isna or =='unknown') |
| D_02 attempt 3 | advisor_client_detail (412e2378) | 2380300c | PASS | 10 books, 995 client details |
| I_D03 | composition_artifacts (9f98dc46) | b148313c | PASS | 9 compositions, 0 skipped |

---

## Type Cascade Incidents

### Incident 1: C_07 ArrowInvalid — household_id 'unknown' vs double
- Pre-fix silver had only firm placeholder accounts (household_id = integer strings)
- Post-SCOPEFIX silver includes individual advisor accounts with household_id = 'unknown'
- C_07 parquet schema had household_id typed as double — string 'unknown' rejected
- Fix: A_00 pd.to_numeric(errors='coerce') → NaN for non-numeric values

### Incident 2: D_02 int(hh_id) fails on float 1000.0
- A_00 pd.to_numeric converted '1000' → 1000.0 (float64)
- D_02 line 309: `int(hh_id)` called on float → Python int(float) works but int('1000.0') fails if serialized back to string
- Fix: `int(float(hh_id))`

### Incident 3: D_02 int(float('unknown')) fails
- C_07 _upload uses `df.fillna('unknown').astype(str)` — converts NaN back to 'unknown' string in account_team parquet
- D_02 reads account_team, pd.notna('unknown') = True, int(float('unknown')) → ValueError
- Fix: 4-case guard: `None if (pd.isna(hh_id) or str(hh_id) == 'unknown') else int(float(hh_id))`
- Applied at all 3 household_id cast locations in D_02 (lines 309, 430, 445)

---

## S3 State After Completion

platinum/advisors/ (excl. quarantine): 19 keys

9 named advisors × book.json (14:09Z):
  dan_sinnen, daria_zalewska, jeremy_keil, john_kurcz, keil_financial_partners,
  kevin_christensen, patrick_scanlan, peter_lee, tim_demuth

1 unknown/ × book.json (14:09Z):
  Unassigned accounts not in account_team — flagged to DS for PLACEHOLDER exclusion

9 named advisors × composition.json (14:11Z):
  All 9 named advisors

Client details: 995 households (vs 297 pre-SCOPEFIX — 3.3× increase)

---

## COO Overrides (CLASS-A)

| Commit | File | Fix |
|---|---|---|
| f84c2df4 | A_00.accounts_dimension.py | pd.to_numeric(household_id, errors='coerce') |
| 0ac97913 | D_02.advisor_client_detail.py | int(hh_id) → int(float(hh_id)) |
| 412e2378 | D_02.advisor_client_detail.py | 4-case household_id guard (isna + 'unknown' check) |

---

## Files Changed

| File | Action | Why |
|---|---|---|
| `infra/aws/ec2/EC2_MANIFEST.json` | dispatch_script updated | orion-gold-dispatch.sh key (session 1, commit 7b300f1e) |
| `org/tier2_senior/0.6.1_AE_PartnerETL/logs/2026-04-27/inf_rdvsds_dchain_rerun.md` | created | D-chain re-run log (session 1) |
| `org/tier2_senior/0.6.1_AE_PartnerETL/logs/2026-04-27/inf_scopefix_advisor_chain.md` | created | This file |

S3 uploads (AE-uploaded COO override scripts):
- s3://opal-data-inf/code/gold/A_00.accounts_dimension.py (f84c2df4 fix)
- s3://opal-data-inf/code/gold/D_02.advisor_client_detail.py (412e2378 fix)

---

## Outstanding Items (not AE scope)

1. unknown/ advisor key: DS to add to _PLACEHOLDER_KEYS exclusion in D_02
2. Schema fixes F1-F3 (leaderboard/partner_analytics/header_metrics): blocking RD re-validation — DT scope
3. RD portal smoke: in progress (real Andrew JWT, Option C auth)
4. Terraform fix for aws CLI -s shebang: long-term AMI fix (post-W5)

---

## Current State

- SCOPEFIX chain: COMPLETE
- Instance i-0ed5afded2ebd4ed4: stopped
- platinum/advisors/: 19 keys live on S3
- AE: idle-complete, standing by
