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

## AMENDMENT 1 (2026-10-08 ~03:4xZ, msg 786) -- who reads condition 3

- **Reader:** condition 3's read (Cottonwood's mix total unchanged, `CASH` in `cash`) is a READ, not a run. A dell1 seat reads it if
  the Cottonwood admission apply has landed by then. Otherwise laptop `0.7.0_AE_CloudOps~S`, who holds the e42 ledger and can read the
  bucket, reads it under this half and reports to `2.0.0_SA_COO~M1`.
- **Which run:** the first BD-family gold run after the write that REBUILDS Cottonwood's mix (`C_06` / `D_03` / `D_04` outputs carry
  a newer LastModified than the write). An incremental 04:00Z run that does not rebuild them does not count. Its read is "not yet",
  not a pass.
- **Rollback** stays this seat's call, executed by the issuer's dell1 seat from the snapshot (a table write, which the Dell
  principal holds).

## AMENDMENT 2 (2026-10-08 ~05:2xZ, msg 801) -- the run that grades condition 3 is Cottonwood's own, not a BD-family run

Laptop ~S measured it: the 04:00Z BD run left 0 Cottonwood objects newer than the 03:12:55Z write. Cottonwood's mix
(`platinum/firm/mix_summary.json`) is rebuilt daily at ~11:35-11:40Z by `cot-bd-session-trigger` (document `opal-cot-gold-run`). So
condition 3 and amendment 1 now read: **the first Cottonwood gold run that rebuilds `platinum/firm/mix_summary.json` after the write**
(expected ~11:36Z 2026-10-08). The pass is that the total equals the before-read (568,707,320.21, VersionId `eH1ZuCUJ...`) and that
`fixed_income` and `cash` move by the `CASH` row's amount. "BD-family" in condition 3 was my wording error. The reader rule of
amendment 1 stands: dell1 if admitted by then, else ~S.

## AMENDMENT 3 (2026-10-08 ~10:5xZ, msg 859, row D1-S6) -- condition 3 replaced; it could not pass as written

M1 measured it from the served bytes. Cottonwood's compositions from BEFORE the write (generated 10-07 ~11Z) already list `CASH` as
`cash` in 206 of 226 clients (USD +781,527.87) and 0 in `fixed_income`. So the -$5.48M move came from the e42 compare's `inferred`
local build and does not describe Cottonwood's served output, where the expected delta is 0. The new run also carries a new
`data_as_of`, so the firm total cannot equal the before-read's 568,707,320.21. Comparing a total across two data days was my
specification error, the same class as e66's condition 3.

**Condition 3 now reads (M1's grade, adopted):** on the first Cottonwood run that rebuilds `platinum/firm/mix_summary.json` after
03:12:55Z:
- (a) the output is rebuilt after the write;
- (b) `CASH` is `cash` in every client composition that lists it, with no `fixed_income` `CASH` line;
- (c) the sum of the mix market values equals `composition.total_market_value` within USD 1.

A miss on (b) or (c) is a same-day rollback from the snapshot. The 49 Financial side is graded at the a07/d06 chain after 12:45Z, by
the same (b)-(c) shape.

## AMENDMENT 4 (2026-10-08 ~11:5xZ, msg 875) -- the 49F side of condition 3

There is no 49F served mix while the d06 twin is unpublished. The 49F side of condition 3 is therefore the a07 dim's `CASH` row reading
`cash` on the 09:47Z run, which M1 measured. That limb is closed. The Cottonwood side stands as in amendment 3.
