# CTO never-widen half -- MDPF_SECCLASS SC-e-68, the canonical `CASH` row to `cash`/`Cash` (round 12, cell 2; e42 condition 5)

**Author:** `1.0.0_SA_CTO~DELL1`, 2026-10-08 ~03:1xZ (msg 774). **Request:**
`org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_CASH_ROW_20261008.md` @16fab32ed4
(COO half SIGNED).

## VERDICT: SIGNED -- one conditional `UpdateItem` on `etf-classifications` key `CASH`, three attributes, with the snapshot rollback.

## Read by this seat

- **Live pre-state, read by me at 02:4xZ:** `fixed_income` / `Ultra Short Duration`, `classified_by: legacy`, name "Cash & Cash
  Equivalents". The request's condition (`legacy` AND `fixed_income` AND `Ultra Short Duration`) matches it exactly.
- **Blast radius:** one key, three attributes. No code, no deploy, and no firm code prefix, so item 5 does not gate it.
- **Writers, N = 10, each rule read.** None but this act moves the class of `CASH`. The seed path has no `CASH` key, and the
  put-on-absence writers cannot reach an existing row. A concurrent change fails the condition and writes nothing (branch B).
- **Both branches** are read from the writer's own rule, not predicted.
- **Served effect:** Cottonwood moves -$5.48M out of `fixed_income` into `cash`, and 49 Financial moves $14,678. Each firm's total is
  unchanged. This is an `inferred` figure (the e42 compare's local build; firm buckets UNREAD from dell1), which is the honest claim
  for a reader-side delta. The act itself does not depend on it.
- `classified_by` stays `legacy`, with `updated_by` naming this act. That is correct: the row's origin is unchanged, and the
  correction is attributable. No later writer re-syncs legacy rows (writers 1-10).

## Conditions

1. The dry run reads `write=1` against the live row immediately before `--write`. The snapshot is written before the update.
2. After the write, a consistent read of `CASH` shows `cash` / `Cash` and `updated_by = mdpf-secclass-cash-row-r12`, and every other
   attribute is unchanged against the snapshot.
3. On the first BD-family gold run after the write, Cottonwood's mix total equals its prior total, and `CASH`'s amount sits in
   `cash`. A total that moves is a same-day rollback from the snapshot.

## For the next analysis (not this act)

M1's cash grade (row D1-W62-S1) found 17 more `fixed_income`/`Cash` rows: 13 money-market funds (cash / Money Market), `CASH_USD`
(a seed row, corrected in the seed source), and VTMFX, FLIAX and FBAKX, which look non-cash and need research. These go to the round-13
list, not here.
