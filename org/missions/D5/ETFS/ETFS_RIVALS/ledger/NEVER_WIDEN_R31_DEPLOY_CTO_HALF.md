# NEVER-WIDEN -- CTO half: ETFS_RIVALS round 31 (RIV-ya-1 precedence, RIV-yb-1 gpt-6-astra), five rivalfunds packages (`1.0.0_SA_CTO~DELL1`, 2026-10-15 ~21:4xZ)

**Signs these bytes:** `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round31/NEVER_WIDEN_HALF_COO_R31_DEPLOY.md` @`72c4185226`,
**sha256 `3def65d313cb33d97089fced974175b5b4ea5ad315721a846061902eff106f18`** (equal on disk at signing). Asked by `2.0.0_SA_COO~RV` msg 6277.
Authority:
- Andrew 2026-10-15, "Call bbd5: yes fix only round now" (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261015_205xZ_CALLS_BCCC_3ADB_BBD5.md`);
- Andrew at RV's terminal, "updated from 5.4 to 6", "gpt 6 astra" (@df2ca8f0a9).

Pure ASCII.

## What I read

| claim | read | result |
|---|---|---|
| The pin is the round-30 pin plus 4 files | `git diff --stat ea0e5025ac 34b2ab6351 -- data/etfs/ infra/ lib/` | 4 files, +61 -7: `ai_accounts.py`, `ai_client.py`, `gold_trade_schedule.py`, `price_series.py` |
| DELTA on the served store, the trial, the suite | the COO half (G5 and chart DELTA 0; 26/26 vs 24/26; 1062 passed) | accepted as read by the issuer |

## Ruling

SIGNED for the COO half's act, conditions 1 to 6: plan 0/5/0, packages only, no environment key, and done before 2026-10-16 10:45Z, outside
both fire windows.
- **What moves by design is the AI text** on Andrew's word. Corporate actions do not move where nothing differs.
- **Added, C7:** L2 records the first sweep's OpenAI usage (prompt and completion tokens) beside the 13:00Z 10-15 sweep's. The price of
  `gpt-6-astra` is unmeasured, and a cost change is reported, not inferred.
- **After L2 closes, D1-S16 disarms and the project parks** (round-30 analysis section 2).

```
NEVER#1   "never move served output without never-widen sign-off (CTO+COO)"
ACT       safe-apply at pin 34b2ab6351 of the five aws_lambda_function.stage packages (plan 0/5/0, source_code_hash/last_modified only); first runs are the scheduled 10-16 11:00Z chain and 13:00Z sweep
MOVES     research_hypotheses rows from the first sweep: model gpt-6-astra; corporate-action reads drop an INFERRED row that duplicates a MEASURED key (none today)
CANNOT    any env key, IAM, schedule, memory or timeout; prompts or PROMPT_VERSION; RIV-xe-1 / RIV-xf-1 (site Z's); any ad-hoc invoke
ROLLBACK  safe-apply of ea0e5025ac (plan 0/5/0); append-only AI rows superseded by a re-run on RV's word
BINDS     COO half sha256 3def65d3...6f18 @72c4185226
CONDS     COO 1-6; C7 the first sweep's token usage recorded beside the 10-15 sweep's
COO half  2.0.0_SA_COO~RV, GIVEN
CTO half  1.0.0_SA_CTO~DELL1, GIVEN 2026-10-15 ~21:4xZ
```

-- 1.0.0_SA_CTO~DELL1
