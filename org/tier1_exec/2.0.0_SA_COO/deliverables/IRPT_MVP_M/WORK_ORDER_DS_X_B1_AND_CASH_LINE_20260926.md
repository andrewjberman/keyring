# Work order: the gold readers admit `structured`, `commodities` and the BD cash line -- for 0.4.0_DS_ClientPlatform~X

- **Issued by:** `2.0.0_SA_COO~M`, 2026-09-26 ~23:5xZ.
- **Authority:** CTO msg 101573, widened by 101578. Not a DSGN round; lease IRPT_BCKEND~M (FAST).
- **Seat:** `0.4.0_DS_ClientPlatform~X`, already seated on IRPT_BCKEND (IB-rtc-2/6/8/9, IB-rtd-3, all complete).
- **Signed halves:**
  - ETF tags: CTO @f4db9245bd; `NEVER_WIDEN_HALF_REQUEST_ETF_TAGS_WIN_20260926.md`, Part B step B1.
  - COT cash line: CTO and CRO, on 9e3f568d42 + 0deac23f1e; `NEVER_WIDEN_HALF_REQUEST_COT_CASH_LINE_20260926.md`.
  - Both files are in `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/`.
- **Reader census:** `ETF_TAGS_READER_CENSUS_20260926.md`, in the same directory.

## Identity and worktree

- Every Bash call starts `export OPAL_AGENT_SERIAL=0.4.0_DS_ClientPlatform~X;`.
- Worktree: `git worktree add ../ajb_ds_x_b1 -b ds-x-b1-cashline CLOUD`. Edit and commit only there.
- Commit with `bash .tools/safe-commit.sh --author "0.4.0_DS_ClientPlatform~X <0.4.0_DS_ClientPlatform~X@opal.agent>" -F <msgfile> -- <paths>`.
  Write `<msgfile>` with the Write tool.
- Never push, merge to CLOUD, or rebase. `2.0.0_SA_COO~M` drains the branch.
  - A CLOUD commit to a COT gold script deploys on the next push (S141). So COT paths merge only after Monday
    2026-09-28's first COT run reads back clean (ledger cot-cash-admission-m-20260925 R1).
- Deliverables: `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.4.0_DS_ClientPlatform~X/`.
- Surprise rows: `org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md`, id
  `IRPT_BCKEND-D-S<k>`. Append, then keep working.

## Paths (your whole write surface)

Each firm's tree is edited on its own. BD and COT are never mirrored.

| # | Path | Act |
|---|---|---|
| 1 | `data/assets/scripts/gold/runners_49f/a07_dim_asset_classification.py` `classify` (:220) | BD cash line: ticker `CASH` AND asset name exactly `CASH` (whitespace-collapsed, upper) gives `cash`, checked FIRST. Pathward (CASH / PATHWARD FINANCIAL INC COM) stays equity. |
| 2 | `data/cot/scripts/gold/runners_cot/d08_cot_mix_summary.py` (:51-54; cash folds into fixed_income at :49) | Takes the cash line through a07. Admit `structured` and `commodities` as their own buckets. |
| 3 | `data/assets/scripts/gold/runners_49f/d06_firm_mix_summary.py` CLASS_ORDER (:46), SystemExit (:96-98) | Admit `structured` and `commodities`. |
| 4 | `data/black_diamond/scripts/gold/C_06.client_mix_timeseries.py` MIX (:179) | Admit both. |
| 5 | `data/black_diamond/scripts/gold/D_03.composition_artifacts.py` `_ASSET_CLASS_LABELS` (:101-107) | Admit both, with labels. |
| 6 | `data/black_diamond/scripts/gold/D_04.client_portal_summary.py` firm composition (:457-464) | Admit both. |
| 7 | `data/black_diamond/scripts/gold/lib/mix_views.py` MIX (:19) | Admit both. |
| 8 | `data/cot/scripts/gold/lib/mix_views.py` MIX (:19) | Admit both. |

- **Not yours:** COT `C_06`, `D_03` and `D_04`. `2.0.0_SA_COO~M` does them on branch `irpt-m-cot-cash-line`, which
  already carries those files.
- **Item 9, only if the CTO rules it** (asked in the seating message): d06 and d08 also admit `other`. Both raise on
  any class outside their list. The COT-new Part 2 write puts `other` on 26 COT keys, so Part 2 waits for this.

## Criteria (each proven by its invocation)

1. **Admission.** For each path 2-8, a test feeds one `structured` and one `commodities` row. Each must land in its own
   bucket: none raises, none drops, and pct sums to 1.0 within 0.001. Run:
   `py -3.12 -m pytest <the tests you add> -q` (rc 0).
2. **Cash line.** A test on a07 `classify`: CASH/CASH gives `cash`, CASH/PATHWARD FINANCIAL INC COM gives `equity`,
   FCASH/CASH is unchanged.
3. **Served delta, measured before any deploy.** Run d08 (and d06) on the served 2026-09-22 inputs, before and after.
   Print per class `$` and pct, and the count of scopes over 100% (the bar is 0). Record it in your deliverables as
   `D08_D06_CASH_LINE_DELTA_20260926.json`.
   - Negative cash-line rows exist (26, -$6,802,732.49). Apply C_06's positive-rows rule (`market_value > 0`) where the
     reader would otherwise drop a class while keeping it in the total.
4. `bash .tools/commit-gate.sh` is clean on every touched `.py`.

## Deploy

- DS rule 13, `.tools/safe-deploy.sh`, one ledger entry per act (`python .tools/deploy_ledger.py open ...`).
- **Admission-only code (items 3-8):** QA-deploy is yours once criteria 1 and 4 pass. It moves no served value,
  because no `structured` or `commodities` value exists in bd-securities until B2.
- **The cash-line rule (items 1 and 2):** deploys WITH the COT cash-line act, after Monday's R1, on `2.0.0_SA_COO~M`'s
  word. At the read-back, d08's value is printed beside C_06's (CRO 101595).
- **No value writes:** no bd-securities or etf-classifications write, and no PROD.

## Report

- One final message to `2.0.0_SA_COO~M`: the branch head, each criterion's output path, and the ledger slugs.
- No status messages.
