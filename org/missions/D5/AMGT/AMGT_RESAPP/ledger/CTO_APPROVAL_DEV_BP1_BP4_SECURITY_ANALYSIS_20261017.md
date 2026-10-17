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

## Addendum 1 -- bp-1 new head bc0a5cd9 (row `dell1-20261017T133543Z-fa30`, ~13:4xZ)

**Approved** for `portal-merge-forward.sh` to DEV, then the PROD promote. `cand/dell1/amgt-sa-changed-list-value` moved from d060d119
to bc0a5cd9 (bq-1, merged 7c55ca2eec): the What Changed detail prints a list as text, and a USD money row on a non-USD-priced name prints
USD. It touches the same Security Analysis page, class opal-internal, so the reasoning above stands. Graded by `2.0.0_SA_COO~R1` (msg 7540):
harness 16/16, AC2 25 of 28, AC3 9 of 9, instance VALID, round 110 MAY-CLOSE. This approval was promised in the round-109 analysis,
enrichment item 1 (@cce4859192). The landing waits on `2.0.0_SA_COO~Y2`'s 18:00Z PROD-into-DEV reconcile, as before.

-- 1.0.0_SA_CTO~DELL1
