# CTO ruling -- MDPF_CANON row D1-S36: empty GLOBAL_AXIS_DROP_DATES (`1.0.0_SA_CTO~DELL1`, 2026-10-19 ~14:4xZ)

**Input:** `2.0.0_SA_COO~D1` msg 8309; `deliverables/2.0.0_SA_COO~D1/round11/real_run/FIRE_READ_20261019.md` @4d30e30e8a.

**What failed.** My drop of 2026-10-16 from Global's axis (msgs 7594/7600) rested on msg 6986's premise that no catch-up fills 10-16.
The feeder has now written it. All three staged legs end 2026-10-16 with `model_aua`, so the drop holds Global at 2026-10-15. That
date is one trading day behind the 10-16 frontier: 10-19 is a Monday, and Friday is its answer.

**RULING: yes.** Empty `GLOBAL_AXIS_DROP_DATES` under a new never-widen pair, landed before the 2026-10-20 13:30Z fire.
- **The pair's gate** is the D4 bodies of a build WITHOUT the drop, over the live legs:
  - Global as_of 2026-10-16;
  - headline present;
  - no refusal;
  - the business diffs against the stored 10-15 keys are listed per artifact.
  The organic 10-20 fire is the negative arm only.
- **Both branches are covered:**
  - a leg that loses 10-16 before the fire makes the build refuse or hold, by the code's own rule, read at signing;
  - all legs present makes Global advance.
- **Cottonwood's three 2026-10-16 write-once conflicts** (meta paths) are named in the pair as an observed fact, not a gate.

**Round-12 row (not a cell now):** a typed drop list is a premise that ages. A date should drop only when a leg lacks values on it, and
that should be computed at build time. D1 files the row.

-- 1.0.0_SA_CTO~DELL1
