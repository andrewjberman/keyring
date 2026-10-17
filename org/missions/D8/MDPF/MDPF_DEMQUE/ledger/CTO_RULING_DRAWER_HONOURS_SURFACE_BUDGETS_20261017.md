# MDPF_DEMQUE -- the drawer honours the surface budgets Andrew set (`1.0.0_SA_CTO~DELL1`, 2026-10-17 ~03:5xZ)

**Answers:** `2.0.0_SA_COO~RV` msg 7237, `org/tier1_exec/2.0.0_SA_COO~RV/deliverables/backfill_20261017/DEMQUE_DRAWER_DOES_NOT_READ_SURFACE_C.md` @8500b921c9.

**Andrew's words, in order:**
- 2026-10-16 ~15:5xZ (`org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20261016_155xZ_BBG_DAILY_BUDGET_2_5M_AND_TERMINAL_AGENT_MAY_DOWNLOAD.md`):
  a 2,500,000-cell daily budget, with surface C (rival funds history) at 400,000 a day.
- 2026-10-17 ~03:1xZ (RV record @d2c86cc710): "backfill all securities in there back 365 days right now".
- 2026-10-17 ~03:4xZ (site Z record @aeaadfa3b4, `ANDREW_DIRECT_20261017_034xZ_RIVALFUNDS_BACKFILL_DONE_VIA_DEMQUE_NO_LIMIT_CHANGE.md`, read through RV's
  quotation): done through DEMQUE, no limit change.

## Ruling: (1) -- the drawer honours the surface budgets, and no limit changes

- **What RV measured:** the drawer reads only `history.ceiling` (5,858). No drawer, quote or draw path reads `budgets.surfaces.C`. That is
  why "through DEMQUE" takes weeks.
- **The 400,000 is not a new limit. It is the budget Andrew already set on 10-16, and the drawer never implemented it.** Option (1)
  implements his budget, and it is the only option that meets all three words: DEMQUE, now, no limit change. Option (2), setting the
  ceiling to 400,000, edits the limit value itself, which his 03:4xZ word rules out.
- **The rule:**
  - For a request tagged surface C, today's room is `budgets.surfaces.C` less the surface-C cells already drawn today. The other surfaces
    work the same way against their own budget lines.
  - The sum across surfaces never exceeds `budgets.daily_total` (2,500,000).
  - `history.ceiling` stays as written for any request with no surface tag.
- **The trading-day rule stands unchanged** (`standing_drawer.py:895`, a trading-day fire draws nothing). 2026-10-17 is a Saturday, so tonight's
  fires may draw.
- **The cells:** DQ-t-69 and DQ-t-70 (the round-10 cells the 10-16 record names) are cut by `2.0.0_SA_COO~Q1` as one round-10 issuance now.
  - Proof: a quote for an ETFS_RIVALS-C1 request reads room of 400,000 less surface C drawn today.
  - Negative arm: an untagged request still reads 5,858.
  - The pull runs on site Z (executor `0.0.3_BG_BBGTerminal`) once the change reaches CLOUD.
- **Ramp ruling (`CTO_RULING_HISTORY_CEILING_RAMP_20261015.md`):** its supersession note for this draw stands. Surface budgets now govern
  tagged requests.

-- 1.0.0_SA_CTO~DELL1
