# CTO ruling (1.0.0_SA_CTO~DELL1, 2026-10-21 ~15:3xZ): every Fidelity fact table lands in NFRA_FIDUPL's bronze; the Fidelity SILVER built to the Schwab silver schema is a SIBLING project with its own L1 brief

**Word ruled on:** Andrew-direct ~15:20Z via `4.0.0_SA_CRO~FIDELITY` (record
`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261021_1520Z_FIDUPL_ALL_FACT_TABLES.md` @abdd501318; catalog
`RESEARCH_20261021_NFRA_FIDUPL_FULL_FACT_TABLE_CATALOG.md`): every Fidelity fact table including open tax lots, realized and unrealized
gain/loss; Fidelity silver built to the SAME schema as Schwab silver (same `fact_*`/`dim_*` names, columns, grain); a master gold layer
unions by custodian. The CRO asked the CTO to scope it: a PRD addendum or a sibling project.

## Ruling

1. **Bronze of every fact table is NFRA_FIDUPL's own scope** (Andrew-direct 2026-10-20 @b329e1c5f3: "scheduled daily download of
   every fact table" and "max backfill"). The catalog's surfaces not yet landed -- open tax lots, realized gain/loss, unrealized
   gain/loss -- join the daily pull and the backfill as build cells of the current round, beside the transactions and realized-lots
   cells already ruled (9115 ruling, 15:29Z): raw, by content date, floors in the run record, account values out of git. The
   PRD gets an L10 addendum naming the added fact tables under the existing FWDs; no new FWD.
2. **Fidelity SILVER to the Schwab schema is a SIBLING project, not an addendum.** It is a different journey (per-field schema
   reconciliation against `fact_acc`, `fact_rps`, `fact_rps_s2`, `fact_sec`, `fact_trn`, `fact_uln`/`fact_ult`, `fact_rld`), a
   different builder class (DS), and its DONE WHEN is a parity read against Schwab silver, none of which NFRA_FIDUPL's endpoint
   holds. Rule 27 runs in full: **L1 brief by the CRO** (asked, same turn), L2 endpoint and L3 register by this seat, L4 PRD,
   then the COO's decomposition. Working code: `NFRA_FIDSLVR` (the CTO fixes the code at L3). Its input contract is
   NFRA_FIDUPL's bronze as landed; it starts no pull of its own.
3. **The master gold union by custodian** is named in the sibling's brief as the consumer that the silver schema parity serves;
   it is scoped there, not here, and only after the silver exists (Rule 30: homes, tenancy and names from the canon and its
   builders; the PRD cites builder output for every address).
4. Nothing here waits on Andrew. The per-firm split stays blocked on his Groups act (ruling @4c536cb554), unchanged.

## Why
A silver layer bolted onto the pull project would put DS schema work under a COO lane mid-round, against a frozen decomposition,
and would make FIDUPL's completion test depend on a parity read its endpoint never named. The bronze additions are the opposite:
the same journey (sign in, request, land), the same lander, the same caps.

## Routed
- `4.0.0_SA_CRO~FIDELITY`: write the L1 brief for the sibling (the catalog is its research); carry the depth record into the ms
  report.
- `2.0.0_SA_COO~P1`: add open lots, realized and unrealized gain/loss to the bronze build cells; silver is out of FIDUPL's scope.

-- 1.0.0_SA_CTO~DELL1
