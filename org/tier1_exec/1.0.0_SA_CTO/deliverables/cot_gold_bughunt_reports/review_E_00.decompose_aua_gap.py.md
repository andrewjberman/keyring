# REVIEW -- E_00.decompose_aua_gap.py

- script: `data/cot/scripts/gold/E_00.decompose_aua_gap.py`
- verdict: **issues-found**
- runs_in_incremental: False
- findings: 2

## Finding 1 -- [medium/empty-null-handling/both]
- **Location:** `data/cot/scripts/gold/E_00.decompose_aua_gap.py:193`
- **Mechanism:** The AGGREGATE log line computes `total_gap/total_silver*100` with no zero-guard on total_silver. This is inconsistent with the script's OWN JSON output (line 452: `round(total_gap / total_silver, 6) if total_silver > 0 else 0`) and with the sibling validator C_04.validate_aua.py:153 (`(gap_abs / silver_aua) if silver_aua != 0 else 0.0`) -- both of which guard the identical divide, showing total_silver==0 is a known reachable state.
- **Failure scenario:** Run on a date where silver/allocations exists (so the existence checks pass) but account_market_value sums to $0 -- e.g. a corrupt/empty silver build for that date, or a date on which every account snapshot-zeroed. silver_acct sums to 0 -> total_silver=0.0 -> line 193 raises ZeroDivisionError -> caught by the top-level try/except (line 581) -> sys.exit(1). The diagnostic aborts before writing either aua_gap_decomposition_{date}.json or aua_gap_top_positions_{date}.json.
- **Proposed fix:** Guard the log ratio the same way as the JSON: `({(total_gap/total_silver*100) if total_silver else 0.0:+.3f}%)`.

## Finding 2 -- [low/empty-null-handling/both]
- **Location:** `data/cot/scripts/gold/E_00.decompose_aua_gap.py:228-231`
- **Mechanism:** The three tolerance-band log lines (within_1pct/5pct/10pct) each divide by `len(both)` with no zero-guard, whereas the mean/median lines a few lines above (208-209) ARE guarded `... if len(both) > 0 else 0`. `both` is the set of account_ids present in BOTH gold_acct and silver_acct after the outer merge at line 175.
- **Failure scenario:** Run on a date where the gold positions_cube and that day's silver/allocations share zero account_ids -- e.g. the cube is empty after ghost exclusion, or a mismatched-vintage/cross-date cube whose account set does not intersect the silver snapshot. The outer merge yields only gold-only + silver-only rows, so `both` is empty. total_silver is still >0 (from silver-only accounts) so line 193 passes, but `len(within_1pct)/len(both)*100` at line 228 raises ZeroDivisionError -> caught -> sys.exit(1).
- **Proposed fix:** Guard the band percentages on len(both), e.g. compute `denom = len(both) or 1` (or wrap the entire GROSS MODEL ERROR / tolerance-band block in `if len(both) > 0:` and emit a 'no matched accounts' line otherwise).
