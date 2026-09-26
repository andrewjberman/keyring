# ANDREW-DIRECT 2026-09-26 ~21:2xZ -- securities already tagged in the ETF Classifier keep that classification

**Channel:** the 1.0.0_SA_CTO terminal, during the UI review landing. **Recorded by:** 1.0.0_SA_CTO, the same turn.

## Verbatim

"yes another thing is that securities which were already listed/tagged in the ETF CLassifier table should retain the
same classification. For example, VXX is tagged to "Structured" and GLD or PHYS are tagged to "Commodities". The
classification table shows both as "Alternatives", which is incorrect."

## What it binds

1. **Precedence rule:** for any security the ETF Classifier table lists, its tag there IS the security's
   classification. Every other source (the bd-securities class writes, the model classifier, the Holdings
   classification) yields to it.
2. **Named defects:**
   - VXX is shown as "Alternatives"; it must be "Structured".
   - GLD and PHYS are shown as "Alternatives"; they must be "Commodities".
3. **Routing:**
   - 2.0.0_SA_COO~M, who owns the classification table and Holdings, measures and fixes.
   - 4.0.0_SA_CRO adds the finding to the UI review register as UIR-50, so it is covered like the other 49.
   - The CTO lands UIR-50 in the DSGN_IRPTV1 PRD.
4. **Law:** a change to served classifications is a served move, so it goes under a never-widen half with its
   per-firm delta.
