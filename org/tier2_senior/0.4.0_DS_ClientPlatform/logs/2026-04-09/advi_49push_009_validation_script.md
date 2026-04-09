# Session Log -- ADVI_49PUSH.009 Platinum Consistency Validation Script
**Agent:** 0.4.0_DS_ClientPlatform~C
**Date:** 2026-04-09
**Project:** ADVI_49PUSH
**Status:** Complete -- committed 999cfa59, pushed to CLOUD.

---

## Summary

Finalized `validate_platinum_consistency.py`. The script was initially written by ~B; ~C added the leaderboard AUA cross-check and period_start_aua presence check to cover the .037 and .042 work from this session.

---

## What the Script Does

13 checks across 4 tiers:

**Tier 1 -- Firm-level:**
- T1a: Advisor AUA sum vs firm headline (semantic check, 0.80-1.50x ratio)
- T1b: Firm client_count > 0
- T1c: Leaderboard data found
- T1d: Leaderboard entry count matches advisor summary count
- T1d-2 (NEW): Leaderboard `total_aua` = advisor summary `total_aua` (verifies .037 tagged_aua fix)
- T1d-3 (NEW): `period_start_aua` present in all leaderboard entries (verifies .042 field)
- T1e: partner_analytics donut total vs firm AUA (SKIP if absent)

**Tier 2 -- Advisor-to-client:**
- T2f: Each advisor's total_aua = sum of their clients' total_aua
- T2g: Each advisor's client_count matches client files found

**Tier 3 -- Client-to-account (100-client sample):**
- T3i: Each client total_aua = sum of account AUA
- T3j: >90% of account summary files exist

**Tier 4 -- Timeseries sanity (20-client sample):**
- T4k: mix_timeseries latest date within 7d of summary data_as_of
- T4l: concentration.json has top_holdings

**Usage:**
```
python validate_platinum_consistency.py             # human output
python validate_platinum_consistency.py --json      # machine JSON
python validate_platinum_consistency.py --bucket X  # override bucket
```

**Exit codes:** 0=all pass, 1=failures, 2=platinum/ not found (pre-deploy)

---

## Design Notes

- T1a uses ratio check (not dollar match) because advisor book AUA (tagged, any-role) legitimately differs from firm headline AUA (unique accounts, no splits). The ratio 0.80-1.50 catches gross errors while allowing the expected semantic difference.
- T2f at advisor level uses the dollar tolerance ($1) which is appropriate since advisor books aggregate from the same client-level AUA. A mismatch here indicates orphan accounts or stale data.
- T3 and T4 sample rather than read all files (performance: ~600 clients * account files would be thousands of S3 reads at full scale).

---

## Files Modified

| File | Change |
|------|--------|
| `data/black_diamond/scripts/gold/validate_platinum_consistency.py` | Added T1d-2, T1d-3 checks; updated author attribution |

---

## Commit

| Step | Result |
|------|--------|
| Commit SHA | `999cfa59` |
| Push | origin/CLOUD up to date |

---

## Next Steps

[AE 0.6.0] Run `python validate_platinum_consistency.py` after D_04 chain re-run to verify gold run output.
