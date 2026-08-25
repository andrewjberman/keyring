# Deploy Completion Record
**Date opened:** 2026-08-25T04:15:16.648099+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260825T042043Z
**Deploy:** Andrew ask 1: per-security PERFORMANCE 0/8 -> 8/8 windows (e37c75ad44) -> etf-positioning-producer
**Authored by:** 0.7.0_AE_CloudOps~Z
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| etf-positioning-producer | tf-lambda | module.etf_positioning_producer.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served | APPLIED 04:19:59Z. CodeSha256 -> 631ELit6nuAD0+J3w9n9J12OqVWDMQxRGj1X+fCzg00=. Packages BOTH Andrew asks: e37c75ad44 (per-security performance) + 7ba77cba29 (sub-asset weight map) -- ask 2 landed 00:17:01 mid-deploy so the first build captured only ask 1 and its byte-check correctly FAILED; rebuilt to take both. ACCEPTANCE: downloaded sha256 == live CodeSha256 (IS the running artifact); deployed member etf_positioning_gold.py sha256 35d3a35f04d1db90... == the tree sha PINNED BEFORE APPLY, so the check is immune to the tree moving again. Real git-derived tokens _load_backfill_history + DAY_TO_DAY_TOT_RETURN_GROSS_DVDS present; positive control CASH_NAME_MARKERS present; negative control zzz_no_such_9999 absent. re-plan rc=0. NOTE: my first attempt asserted an INVENTED token (_perf_windows, count 0 in tree) -- both controls passed while the target was fabricated; byte-identity to a pinned sha needs no token guessing. | CLOSED 20260825T042043Z |

## Log

- 20260825T041516Z OPENED by 0.7.0_AE_CloudOps~Z with 1 leg(s)
- 20260825T042043Z LEG etf-positioning-producer closed: APPLIED 04:19:59Z. CodeSha256 -> 631ELit6nuAD0+J3w9n9J12OqVWDMQxRGj1X+fCzg00=. Packages BOTH Andrew asks: e37c75ad44 (pe
- 20260825T042043Z CLOSED -- all 1 legs proven
