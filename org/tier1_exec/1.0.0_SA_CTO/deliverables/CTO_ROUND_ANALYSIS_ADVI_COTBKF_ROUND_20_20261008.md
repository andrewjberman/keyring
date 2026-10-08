# ADVI_COTBKF -- ROUND ANALYSIS, round 20

Author `1.0.0_SA_CTO~DELL2`, 2026-10-08 ~18:4xZ, under NFRA_CTLPLN ADDENDUM v0.12 C-ROLES.

**Input:** `3.0.0_SA_CVO`'s slug (msg 1411), the L9 grade @ea6b96a66a (CB20t2-AC3 MET), and REMEDIATION_v13. MAY-CLOSE, ARMED 0.
D2-W41-S1 is OPEN to this seat.

## 1. State

- **Rule (b) did not land 316067107.**
  - No custodian designation is readable from the data the chain reads: `Position_Type` reads CASH on 1,408,059 of 1,416,497
    transaction rows, for every security.
  - The CVO scanned the cached extracts and found no core or sweep column.
  - sweeps-v2 = v1 (FDIC66606, FDIC66853). This is correct under the round-19 ruling.
- **The CRO's research** (`RESEARCH_20261008_COMMONWEALTH_FILES_VS_SCHWAB_FACT_TABLES.md` @bb9db7b2e3) explains why. These files are
  Commonwealth's accounting-system extract, not a custodian feed, and no column names a custodian.
- **E1's classing of the 163 MATCH -> DIFF months:**
  - 16 sit in accounts holding 316067107;
  - 147 sit in accounts holding neither 316067107 nor another unlisted money-market fund.
  - So rule (b) can move at most 16 of the 163 months.

## 2. Ruling -- D2-W41-S1, and where round 21 goes

**The 147 come first.**
- The designation search for 316067107 is PARKED, owned by this seat. The condition that un-parks it: a custodian statement or account
  agreement naming the core position reaches the project. The laptop's restricted statements around 2023-03-17 are the first place to
  look, through the fenced path, and no vendor contact is made for this.
- Until then the 16 stay DIFF and are labeled as such in every grade. A one-entry re-run closes them if the source arrives.

**Why.** 147 of 163 movers have a cause we have not named, against a bound of 16 for the parked item. A month that went MATCH -> DIFF
when the sweep turned INTERNAL may also have matched before only because two errors offset. If so, DIFF is the truer state, and the fix
lies elsewhere in the chain.

## 3. ENRICHMENT -- round 21, ONE issuance by `2.0.0_SA_COO~C2`

| # | item | criteria (at most three) | risk |
|---|---|---|---|
| E1 | **Name the cause of the 147 "neither" movers** | (1) each of the 147 months is assigned exactly one cause class, with counts summing to 147. The classes include at least: (i) the sweep balance entering the daily value; (ii) a prior MATCH by offsetting errors, shown by the before-state's two components; (iii) other, named. (2) One month per class is traced end to end, with the day values printed from the persisted month grades. (3) A control: E1's 16 core-holding months are reported separately and are not mixed into the 147. | LOCAL |

The real run of cells B-D stays bound by the price load (unchanged).

-- 1.0.0_SA_CTO~DELL2
