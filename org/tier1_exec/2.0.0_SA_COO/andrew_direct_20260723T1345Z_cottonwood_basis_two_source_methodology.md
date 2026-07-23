# ANDREW-DIRECT — Cottonwood basis is a TWO-SOURCE overlay; reference it properly + record the methodology

**Channel:** Andrew-direct to COO terminal, 2026-07-23 ~13:45Z.
**VERBATIM (Andrew):** "Yes keep in mind here that the Cottonwood basis is a little more complex, i need
you to make sure you reference it properly. We're pulling the models from their 'rebalance' domain, and
overlaying 'datamining' holdings for values. Check in with DS to confirm the structure and make sure our
methodology is recorded and referenced properly."

## The methodology (Andrew's statement — to be confirmed grounded with DS)
Cottonwood's basis is a **two-source overlay**, unlike 49F/INF single-source:
- **MODELS** (which accounts are in which models — the model membership/assignment) come from the BD
  **REBALANCE** domain (the daily Rebalancer pull).
- **VALUES** (the AUM dollar amounts) are **overlaid from BD DATAMINING holdings**.
So: model membership from Rebalancer, dollar values from DataMining, overlaid. (fee_scope = model, per the
fee-basis: Opal takes fees from cottonwood MODELS only — [[andrew_direct on the fee-basis business logic]].)

## The DEFECT this catches (live at directive time)
The served artifacts label cottonwood `partners_basis = "bd-datamining-holdings"` and
`fee_basis_components.cottonwood.basis = "bd-datamining-holdings"` — that names ONLY the VALUES source
(datamining), NOT the model source (rebalance). **The basis reference UNDER-STATES the methodology.**

## The directive (3 parts)
1. **Reference it properly** — the basis must name BOTH sources (rebalance-models + datamining-values),
   not just datamining.
2. **Check in with DS** to confirm the structure as implemented (grounded, Rule 22: file:line @ commit —
   is model-membership really from Rebalancer and values from DataMining?).
3. **Record the methodology** — the two-source overlay documented + referenced from the artifact.

## COO actions (2026-07-23 ~13:45Z)
- [x] DS check-in dispatched (@134545Z): confirm structure grounded + fix the basis label to name both
  sources + create/reference the methodology record.
- [x] CTO co-sign condition added (@134553Z): cottonwood BASIS-REFERENCE gates the cottonwood-inclusive
  Global serve; DECOUPLED from P1 (renderer fix) + the fresh-49F/INF publish (those proceed).
- [x] Andrew acknowledged: HOLDING the cottonwood-inclusive Global serve until referenced properly.
- **HOLD:** a correct number under a wrong-basis label is still mis-referenced — the cottonwood serve
  waits until DS confirms structure (grounded) + the label names both sources + the methodology is recorded.
- My counter-sign now carries "cottonwood basis names both sources" alongside the fee-basis reconciliation.

**Delete/close when: DS confirms structure grounded + the corrected basis label serves + the methodology
record is referenced. Until then this is a live serve-gate.**

-- `2.0.0_SA_COO`, ~13:45Z
