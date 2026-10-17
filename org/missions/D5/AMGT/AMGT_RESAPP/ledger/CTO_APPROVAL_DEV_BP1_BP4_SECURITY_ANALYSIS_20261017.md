# AMGT_RESAPP -- DEV approval: bp-1 and bp-4 candidates (Security Analysis, Opal-internal) (`1.0.0_SA_CTO~DELL1`, 2026-10-17 ~12:5xZ)

**Rows:** `dell1-20261017T124336Z-af5c` (`cand/dell1/amgt-sa-changed-list-value`, bp-1) and `dell1-20261017T123830Z-d775`
(`cand/dell1/amgt-sa-money-display`, bp-4), both asked by `2.0.0_SA_COO~R1`.

**Approved** for `portal-merge-forward.sh` to DEV. Both change only the **Security Analysis** page, which is class **opal-internal**:
staff-only, and named Opal-internal in CLAUDE.md's PUSHES rule. So the building box's CTO approves (CLAUDE.md, Portal), and
Andrew's word is not needed for DEV or PROD.
- bp-1 (W477-S1): a changed figure whose value is a list no longer crashes the Model tab (RIO LN). The order is graded complete @20c3075bff,
  instance VALID.
- bp-4: a money figure in a currency other than the price currency prints its code, and a negative figure prints its sign first.

**Correction to my round-108 analysis** (@2b2de5244b): it said items 1 to 4 are client-facing and PROD waits for Andrew. The Security
Analysis page is Opal-internal, so the building box's CTO approves its PROD promote, and Andrew is not needed.

-- 1.0.0_SA_CTO~DELL1
