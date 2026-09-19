# Deploy Completion Record
**Date opened:** 2026-09-19T09:53:01.303578+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260919T103423Z
**Deploy:** AMGT-rk-35: rolling history window; pull+derive on the three validation names (unserved keys); co-signed rk-35 pair
**Authored by:** 0.9.0_WK_AMGT_RESAPP~39
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | window rule + dry-run + pull-log home committed | commit hash | commit f3175defae (this worktree, wk-amgt-14-39) -- window rule + dry-run + pull-log home committed | CLOSED 20260919T103335Z |
| L2 | activation | raw + derived landed for CAT/CSL/Keyence (3 keys, unserved) | key list + stamps | raw landed: raw/bloomberg/{CAT_US_Equity/20260919T095600Z,CSL_AU_Equity/20260919T095603Z,6861_JP_Equity/20260919T095606Z}/{refdata,histdata,pull_log}.json (6 objects); derived landed: derived/model_block/{CAT_US_Equity,CSL_AU_Equity,6861_JP_Equity}/20260919T095644Z/model_block.json (3 objects) | CLOSED 20260919T103335Z |
| L3 | verify | 33 served stamps unchanged; validation blocks carry latest closed FY | AC2/AC3/AC4 output | AC2: CAT latest_closed_fiscal_year=2025 (FY2026 absent from Bloomberg's return, December FYE not yet reported); CSL latest_closed_fiscal_year=2026 with FY2026 SALES_REV_TURN/IS_EPS present (June FYE); 6861 latest_closed_fiscal_year=2026 with FY2026 SALES_REV_TURN/IS_EPS present (March FYE). AC3: REFUSE_NOT_YET_BUILT 0 on all three (checks 205/219/217). AC4: the OTHER 33 crosswalk names (36 minus the 3 validation names) show served_stamps_moved 0 / raw_landings_newer_than_pre 0; the 3 validation names themselves moved as this order's own authorized act (AC4 literal script flagged as REFUSED -- see surprise row AMGT_RESAPP-Z-W39-S1). | CLOSED 20260919T103336Z |

## Log

- 20260919T095301Z OPENED by 0.9.0_WK_AMGT_RESAPP~39 with 3 leg(s)
- 20260919T103335Z LEG L1 closed: commit f3175defae (this worktree, wk-amgt-14-39) -- window rule + dry-run + pull-log home committed
- 20260919T103335Z LEG L2 closed: raw landed: raw/bloomberg/{CAT_US_Equity/20260919T095600Z,CSL_AU_Equity/20260919T095603Z,6861_JP_Equity/20260919T095606Z
- 20260919T103336Z LEG L3 closed: AC2: CAT latest_closed_fiscal_year=2025 (FY2026 absent from Bloomberg's return, December FYE not yet reported); CSL late
- 20260919T103423Z CLOSED -- all 3 legs proven
