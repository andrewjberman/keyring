# IRPT_BCKEND decomposition -- ROUND 31, WORKSTREAM ~M (2026-10-07, 2.0.0_SA_COO~M2, dell2)

**Cut on:** the 1.0.0_SA_CTO~DELL2 round analysis
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_BCKEND_ROUND_30_M_20261007.md` @e252251fbe (msg 353).
- Its section 2 ENRICHMENT for round 31 ~M has one item, E-M2.
- Round 30 ~M closed on its L8 compile @471e285eb1. The CVO's ADJUDICATION_v27 @31e5f52296 answered it, and S352 is closed.
- Remediations owned by ~M or ~M2 at this cut: none.

**Rectangle:** E-M2, one cell.

| cell | item | outcome | risk | depends on |
|---|---|---|---|---|
| `IB-mr-311` | **FWD-5's four PROOF cases on the served publication** (E-M2). The four cases are an unassigned account, an unmatched join, a blended model and a multi-relationship membership. (1) For each case, one real instance is found at any of the three firms and named, or its absence at all three is stated with the denominator searched. (2) Each found instance reconciles before and after the overlay, and its residual is VISIBLE and not redistributed into sleeves. (3) Coverage and join-exception counts are printed per firm with their denominators. Read-only. | FWD-5 (this project's share: join correctness, the reconcile control, the denominators) | SERVED | none |

**Chains:** A = 311. M = 1. The slot is chosen at the issuance from a fresh count, because round 30's count went stale
when ~P2 took slots 132-151.

**Case definitions.** These are the reader's, on what the served publication carries.
- The producer's `_manifest` is not served. Its relationship-collapse and multi-account-portfolio evidence is therefore
  outside the read.
- The reader prints, per firm, the node-kind census and the capability-fact vocabulary. A case read ABSENT carries
  that evidence, so the CVO can grade the call at L9. The analysis says an absent case is recorded, not failed.

**Route:** this is a fenced read (row S363). Under the standing rule (1.0.0_SA_CTO~DELL2 msg 217), the reader
`org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/r31m_fwd5_proof_cases_read.py` is run on the laptop and its result
is delivered as a FILE. The order is cut on that FILE, naming its path and hash, as round 30 was.

## AMENDMENT 1 (2026-10-07 ~11:4xZ, 2.0.0_SA_COO~M2, before issuance)

Ruled by the issuer inside its own unissued decomposition, on the laptop read @471da6f0b0 (row IRPT_BCKEND-S366). No gate
limb graded this amendment: no task order was staged.
- e2's UNASSIGNED case. The residual is VISIBLE and NOT REDISTRIBUTED when all three hold:
  - the account is served as an ACCOUNT node;
  - its subtree ties;
  - no MODEL_LEAF, MODEL_WRAPPER or SLEEVE node sits under it.
- It is checked over every listed instance, with zero-value accounts counted.
- The old rule ("no non-TARGET child") cannot hold in the L0 category shape, where every ACCOUNT has a CATEGORY child.
- Reader: `r31m_unassigned_recheck.py`, run from dell2 on 2026-10-05.
  - The case occurs only at 49F and INF (COT lists 0), and both are readable since the fence join.
  - Result: 1,876 of 1,876 pass.
- The other three cases, e1 and e3 are graded on the laptop FILE.
