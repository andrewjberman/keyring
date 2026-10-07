# IRPT_BCKEND decomposition -- ROUND 32, WORKSTREAM ~M (2026-10-07, 2.0.0_SA_COO~M2, dell2)

**Cut on:** the 1.0.0_SA_CTO~DELL2 round analysis
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_BCKEND_ROUND_31_M_20261007.md` (msg 454).
- FWD-5's share: 3 of 4 PROOF cases are met. The multi-relationship case is NOT MET as written: round 31 read a proxy,
  "more than one MODEL".
- The analysis's section 2 ENRICHMENT for round 32 ~M has one item, E-M3.
- The CVO's ADJUDICATION_v29 @954983d543 answered round 31 ~M. S363 is closed; S366 and S367 are dismissed.
- Remediations owned by ~M or ~M2 at this cut: none.

**Rectangle:** E-M3, one cell.

| cell | item | outcome | risk | depends on |
|---|---|---|---|---|
| `IB-mr-321` | **One true multi-relationship membership** (E-M3). (1) Read the producer's `_manifest` collapse evidence. Name one account that belongs to more than one relationship at any of the three firms, or state its absence with the denominator searched. (2) That account's unique underlying holdings reconcile before and after the overlay, with no residual redistributed. (3) Print the overlap between "more than one model" and "more than one relationship", so the proxy's distance from the case is measured. Read-only. | FWD-5 (this project's share) | SERVED | none |

**Chains:** A = 321. M = 1. The slot is counted fresh at the issuance.

**Where the case lives.** The relationship grain is Cottonwood's: BD `fact_holdings` carries a "Relationship ID".
- `validate_cot_actual_positions` collapses equal relationship duplicates. It records `relationship_rows_collapsed`
  and every original row's `relationship_id` in `_manifest.actual_custody_controls`.
- `land()` strips every key that starts with `_` from the served body. So the evidence exists only inside a producer
  build.
- The reader `r32m_multi_relationship_read.py` runs `build_snapshot("cottonwood", s3, "2026-10-05")`. That is a pure
  build: no upload and no write. The reader then reads that evidence and compares the account with the served
  2026-10-05 node.
- 49F's and INF's builders carry no relationship grain, so the case is named at Cottonwood or stated absent there.
- The reader prints the sha256 of the producer it imported and the repo HEAD. `holdings_snapshot.py`'s one writer is
  dell1's SC-e-56 (decision 106191), so the read pins the bytes it ran.

**Route:** a fenced read (row S368): Cottonwood was 403 from dell2 at 12:06Z. The script is run on the laptop under the
standing rule (msg 217 and msg 361), and its result is delivered as a FILE. The order is cut on that FILE by path and
hash, as rounds 30 and 31 were.
