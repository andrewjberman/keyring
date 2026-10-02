# ETFS_RIVALS round 5 FAST A1 -- never-widen ADDENDUM 6, CTO half (trend sector honesty G6-1 + sector_source CALL 9)

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-02 ~10:0xZ. **COO half:**
`deliverables/2.0.0_SA_COO~RV/round5/NEVER_WIDEN_HALF_COO_FAST_A1_ADDENDUM6.md` @73744489e8 (msg 28381), pin CLOUD 93227704b7.
**Extends** the A1 pair and addenda 1-5. Every gate, key and condition stands.

## What I read

- **The authority:** CVO~RV grade 6 G6-1 (@bcac012fe7) recommends ONE "Sectors not shown" rule for the ranking and the trend
  sector panels. CRO~RV CALL 9 (@12129108e1) requires the condition that a trend row carries `sector_source` own | other_fund.
- **The served delta, measured THROUGH each stage's `handler_entry`** (`served_delta_a1.py`, as required since addendum 5):
  - 0 of 3,906 `holding_contribution` rows change;
  - **0 of 319 `buying_trend` values change**, and the table gains the nullable `sector_source` column;
  - 0 of 1,568 `input_census` rows change.
  - The page hides the trend sector tables of ETFT, GQGU, IDVZ and PCLG ("Sectors not shown"; no-GICS gross > 50%). Nothing else
    on the page changes, and it carries no script.
- **The plan is 0/5/0:** code hashes only. The package diff is `gold_buying_trend.py` and `render.py`.
- **The blast radius G1-G4,** as in addenda 1-5. Both branches are covered.

## Conditions

1. The act-start gates hold at the act: plan exactly 0/5/0, live base = G1's CodeSha256, the NEVER-2 entry
   `etfs-rivalfunds-fast-a1-r7` committed before the apply, and nothing in flight.
2. **ONE rule, shown to be one:** the post-act read names the function and threshold that decide "Sectors not shown" on the
   ranking panels and on the trend panels, and shows they are the same, as G6-1 recommends. A second, parallel threshold is a
   finding for CRO~RV.
3. **The post-act read comes from the SERVED objects:** `sector_source` is present on the trend rows (own / other_fund counts
   printed); the four funds' trend sector tables are replaced by "Sectors not shown"; every value is equal to its pre-act value.
   HTTP status is never the grade.

**CTO HALF: SIGNED** for plan 0/5/0 at CLOUD 93227704b7, blast radius G1-G4, both branches.
