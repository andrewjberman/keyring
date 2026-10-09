# Deploy Completion Record
**Date opened:** 2026-09-26T03:21:35.082351+00:00
**Status:** HELD-SOVEREIGN-GATED -- gate: external / OWNER 2.0.0_SA_COO~M1. RE-MEASURED 2026-10-09 ~07:5xZ after FWD-15 (TO-AI-e49 COMPLETE 10-08): of the 941 Part-1 written keys (receipt BD_SECURITIES_COT_NEW_P1_RECEIPT_20260926.json), 925 present in etf-classifications, 16 absent (was 66 absent on 10-08: BD 8 + COT 58). Of the 16: 5 are e49 FINAL refusals (E49_FINAL_REFUSALS_ALL/V3, E49_TWICE_REFUSED_FINAL; terminal by ruling); 11 were never in e49's planned set (E49_AI_SNAPSHOT keys) -- outside FWD-15's firm-held-unplaced scope: ETHA, NAME::AST INVESTMENT GRADE BOND PORTFOLIO, NAME::AXA MODERATE ALLOCATION, NAME::BENEFIT FIXED RATE OPTION, NAME::CALAMOS STRATEGIC TOTAL RETURN COM SH BEN INT, NAME::GRAYSCALE ETHEREUM STAKING MINI ETF, NAME::JOHN HANCOCK LIFE INSURANCE CO 5 06 15 2028, NAME::MFS MULTIMARKET INCOME TR SH BEN INT, NAME::MORGAN STANLEY 6 25 08 09 2026, NAME::PATRIOT BK N A 4 5 2026, NAME::PRUDENTIAL ANNUITY. Closes on a ruling for the 11 (not held -> CLOSED_UNREMEDIATED NOT_A_DEFECT, or a placement cell) at the next round analysis. No rollback (S188). (held since 2026-10-09T07:51:21.197402+00:00)
**Deploy:** bd-securities COT-new write Part 1: 941 conditional PutItem (CTO @ab4a2e41bb; sha c96398886f143f54)
**Authored by:** 2.0.0_SA_COO~M
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 96.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A07 | verify | a07 dim_asset_classification dry build with the new items (CTO precondition) | per-firm delta 49F/INF/COT count and dollars; 0 moves outside the written keys | measure_a07_delta_cot_new.py --part all (dry, no upload; A07_DELTA_COT_NEW_20260926.json): 123 of the union's keys change; 49F 10 keys $56,952.06 (8 equity->fixed_income, 2 equity->alternatives: ARKB CGMU ESIIX ETHA JCBUX JSOSX LBNYX PZA SHYD WOBDX); INF 8 keys $0.00 (positions at 0 shares; incl. FDIC91232 = Leader Bank IRA -> other, a Part-2 key); COT 122 keys $62,603,923.90; changed NOT via a written key: 0 -> no stop | CLOSED 20260926T032135Z |
| W1 | verify | bd-securities 941 conditional PutItem classified_run=irpt-m-cot-new-20260926 | receipt: written 941, condition refusals 0, read-back 941, loader 941 | receipt BD_SECURITIES_COT_NEW_P1_RECEIPT_20260926.json: census sha c96398886f143f54 941 keys 0 present; wrote 941 of 941; 0 condition refusals; read-back 941 (class + classified_run); fresh loader 935 of 941 -- 6 NAME:: keys (HOTCHKIS WILEY HY, MFS CHARTER INCOME, NEOS 1-3M T-BILL ETF, NUVEEN AMT-FREE MUN, NUVEEN CA HY MUNI, PIMCO HIGH INCOME) resolve by name to a same-name ticker sibling (HWHZX MCR CSHI NUW NCHRX PHK, fixed_income), so COT serves fixed_income for all 6 ($604,373 at 09-22; BD 0 rows). Versus the half: +$149,663 equity->fixed_income (NEOS) and $1,025 fixed_income instead of alternatives (HOTCHKIS) -- reported to the CTO | CLOSED 20260926T032551Z |
| R1 | verify | COT C_06 first scheduled run after the write (Mon 2026-09-28) and BD C_06 next run | COT mix moves equity->fixed_income/alternatives per the half; BD 652 accounts per the half |  | OPEN |

## Log

- 20260926T032135Z OPENED by 2.0.0_SA_COO~M with 3 leg(s)
- 20260926T032135Z LEG A07 closed: measure_a07_delta_cot_new.py --part all (dry, no upload; A07_DELTA_COT_NEW_20260926.json): 123 of the union's keys chang
- 20260926T032551Z LEG W1 closed: receipt BD_SECURITIES_COT_NEW_P1_RECEIPT_20260926.json: census sha c96398886f143f54 941 keys 0 present; wrote 941 of 941
- 20260926T032616Z HELD-SOVEREIGN-GATED gate=external/leg R1 reads COT C_06's first scheduled run after the write and BD C_06's next r
- 20260929T002333Z HELD-SOVEREIGN-GATED gate=external/CTO ruling S188 (msg 102504): R1 stays OPEN, no rollback; COT half waits on the 
- 20260930T190520Z HELD-SOVEREIGN-GATED gate=external/CTO ruling S188 (msg 102504): R1 stays OPEN, no rollback; COT half waits on the 
- 20261008T065132Z HELD-SOVEREIGN-GATED gate=external/OWNER 2.0.0_SA_COO~M1 (dell1; laptop ~M closed, laptop CTO msg 106788 via MSTR m
- 20261008T065635Z HELD-SOVEREIGN-GATED gate=external/OWNER 2.0.0_SA_COO~M1. R1 COT half MEASURED 2026-10-08T06:5xZ against etf-classi
- 20261008T072825Z HELD-SOVEREIGN-GATED gate=external/OWNER 2.0.0_SA_COO~M1. R1 measured 2026-10-08 against etf-classifications (the t
- 20261009T075120Z HOLD RELEASED -> OPEN
- 20261009T075121Z HELD-SOVEREIGN-GATED gate=external/OWNER 2.0.0_SA_COO~M1. RE-MEASURED 2026-10-09 ~07:5xZ after FWD-15 (TO-AI-e49 CO
