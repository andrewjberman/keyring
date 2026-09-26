# Deploy Completion Record
**Date opened:** 2026-09-26T03:21:35.082351+00:00
**Status:** HELD-SOVEREIGN-GATED -- gate: external / leg R1 reads COT C_06's first scheduled run after the write and BD C_06's next run; both run on trading days (held since 2026-09-26T03:26:16.450830+00:00)
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
