# ANDREW-DIRECT 2026-09-24 ~18:4xZ -- the $10K rounding is removed for Investor Reporting only

**Channel:** the 1.0.0_SA_CTO terminal. It is his answer to the scope question 2.0.0_SA_COO~M's record raised,
`org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260924_184xZ_IRPT_FIRM_TAB_FILTER_AND_10K_ROUNDING.md`
@af2dd7335d. **Recorded by:** 1.0.0_SA_CTO, same turn.

## The question, verbatim

"The $10K rounding lives in the shared CategoryViewTree component, which both Model Portfolios (your 09-15 ask) and
the IRPT Holdings tab use. Where should it go?"

The options offered:
- "Remove everywhere (Recommended)";
- "Remove for IRPT only" -- "Investor Reporting shows exact amounts; Model Portfolios keeps the $10K grain from your
  09-15 word. The component gains a switch that Holdings turns off."

## The answer, verbatim

"Remove for IRPT only"

## What it binds

- **Investor Reporting shows exact amounts.**
  - `portal/src/components/CategoryViewTree.tsx` gains a switch whose default keeps today's $10K grain.
  - The IRPT Holdings drill (`pages/InvestorReporting/tabs/holdings/DrillTree.tsx`) turns it off.
- **Model Portfolios keeps its $10K grain** from the 09-15 word
  (`org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260915_025xZ_DSGN_REBRND_ROUND_TO_10K_AND_49FINANCIAL_TAX_SMA.md`).
- **Who builds it:** 2.0.0_SA_COO~D, the IRPT portal frontend integrator.
- **The shared file:** it is also in `MDPF_TAXSMA` `TO-TX-c-2`'s write grant (pending), so the change is additive only.
