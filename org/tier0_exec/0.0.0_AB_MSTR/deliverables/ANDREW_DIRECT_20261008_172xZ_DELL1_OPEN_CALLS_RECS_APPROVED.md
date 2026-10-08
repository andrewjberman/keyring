# Andrew-direct 2026-10-08 ~17:2xZ at the dell1 0.0.0_AB_MSTR~DELL1 terminal -- open-calls recs approved

**Verbatim:** "Recs approved."

It answers the /open-calls frame 0.0.0_AB_MSTR~DELL1 printed at ~17:2xZ (3 calls). Each ruling is that card's REC:

1. **CVO scratch branches** (3.0.0_SA_CVO msg 944, relayed by 1.0.0_SA_CTO~DELL1 msg 946): tag each tip as
   `archive/<branch>` first, then drop `cvo-secclass-r12-compile` and `cvo-secclass-r8-s50` and their worktrees
   `C:/dev/cvo_secclass_r12` and `C:/dev/cvo_secclass_s50`. Keep `cvo-secclass-r9-compile` and `C:/dev/cvo_secclass_r9`
   until the CVO confirms its 9 uncommitted files can be discarded. Measured before the act: commits not in CLOUD by
   patch (`git cherry`): r12 7 of 8, r9 7 of 7, s50 1 of 1. Uncommitted files: r12 0, r9 9, s50 0.
2. **Portal DEV -> PROD:** not yet. DEV is 44 commits ahead of PROD; 1.0.0_SA_CTO~DELL1 confirmed only MDPF_SECCLASS's 11
   (msg 1012). Routed to the laptop 0.0.0_AB_MSTR, which collects each project's CTO confirmation; then one /prod-deploy.
3. **SH-t-4:** yes. Re-land the `integrations/bloomberg/pipeline/etf_daily_pull.py` edit (reverted at ffef2f7c26; CTO
   half 2f1a7ff86c) AFTER the 2026-10-09 07:00 ET FWD-1 acceptance pull, not before (CTO msg 931). This lifts his
   2026-10-06 no-modify order for this one edit only.
