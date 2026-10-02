# ETFS_RIVALS round 5 FAST A1 -- never-widen ADDENDUM 12, CTO half (a home-producer report's trace panel names its file)

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-02 ~14:1xZ. **COO half:**
`deliverables/2.0.0_SA_COO~RV/round5/NEVER_WIDEN_HALF_COO_FAST_A1_ADDENDUM12.md` @b66ec623ff (msg 28516), pin CLOUD 722f0db291.
**Extends** the A1 pair and addenda 1-11. Every gate, key and condition stands.

## What I read

- **The defect:** the served 10-02 page shows "source URL unavailable (bronze sidecar unreadable)" on PFOE's 26 trace rows. That is a
  read failure that never happened: a home-producer report has no bronze file by design, and its rows carry `source_channel` and
  `silver_uri`.
- **The scope:** this is round-5 analysis cell 6, done under the FAST lease, so round 6 drops the cell.
- **The plan is 0/5/0:** code hashes only. The package diff is `publish_page.py` (`_fund_files` carries the two columns) and
  `render.py` (`_source` names the home producer's file).
- **The served delta, measured** as an overlay over the served inputs:
  - 26 cells change to "Opal home producer file (<channel> <file>)";
  - 1 line changes, the G0 map date (data, as measured for addendum 11);
  - 0 other lines; no A1, AI or check-verdict change; 13 of 13.
- **The blast radius N1-N3:** the five Lambdas; ONE republish of 10-02 (1002f, no `refresh_a1`, no gold write); later runs. Both
  branches are covered.

## Conditions

1. The act-start gates hold. Served changes resumed on Andrew's 13:33Z word (@74e6e01a5b).
2. **The post-act read comes from the SERVED page:**
   - 0 "bronze sidecar unreadable" cells and 26 "Opal home producer file" cells;
   - every other line byte-equal to the measured overlay;
   - 13 of 13.
   HTTP status is never the grade.

**CTO HALF: SIGNED** for plan 0/5/0 at CLOUD 722f0db291, blast radius N1-N3, both branches.
