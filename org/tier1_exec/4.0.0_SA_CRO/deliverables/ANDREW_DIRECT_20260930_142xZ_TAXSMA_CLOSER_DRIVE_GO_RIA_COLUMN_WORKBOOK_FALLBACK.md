# ANDREW-DIRECT 2026-09-30 ~14:2xZ (10:2x ET) at the 4.0.0_SA_CRO terminal -- MDPF_TAXSMA: close it under a FAST lease; RIA column routes the firm; workbook value is the fallback

**Author:** 4.0.0_SA_CRO (Chief Research Officer)
**Home:** org/tier1_exec/4.0.0_SA_CRO/
**Channel:** Andrew typed at this seat's terminal, three messages, on the deep-dive record @8cdcc2aba9
(`MDPF_TAXSMA_STATUS_DEEP_DIVE_20260930.md`, section 6 named the seat departure and the surfaces).

## Verbatim

Message 1:

> "Yeah let's do it. There's a couple comments I want to make. Yang just updated the sharepoint file with an RIA column
> which we should use for matching to firm. Also some of these accounts may not appear in their designated master
> account. If that is the case, we just refer to the AUM (Mn) Column."

Message 2:

> "In essence, there should be a fallback where if we dont see a 49 account in 0833 schwab, or a cottonwood account in
> black diamond, then just use the excel value."

## What the word does

1. **Seats `4.0.0_SA_CRO` on MDPF_TAXSMA under a FAST lease (`/closer-drive`)**, the departure named in the deep dive:
   the skill reads "the project's COO lane only" and the CRO charter §3 leaves applies to the CTO. Both were put to
   Andrew in section 6 of @8cdcc2aba9 ("What this seat needs from Andrew to start: one line seating 4.0.0_SA_CRO ...
   plus his word that the CRO runs the applies under ledger + safe-apply for this project") and "Yeah let's do it" is
   the answer. Everything FAST never relaxes still binds: safe-commit, own worktree, never-widen sign-off on served
   output, deploy ledger, safe-apply, no PROD promotion, secrets.
2. **The workbook's new `RIA` column is the firm axis.** `49 Financial` rows reconcile against Schwab master 0833;
   `Cottonwood` rows reconcile against Black Diamond (the cottonwood custody basis the estate already uses). The
   contract's 49financial-only membership widens to per-firm membership keyed on RIA.
3. **Fallback basis.** A traded workbook row absent from its RIA's custodian source is valued at the workbook
   `AUM (Mn)` column (x 1,000,000), carried with its own basis token so the served figure says which rows are custodian
   -measured and which are workbook-stated. This amends PRD v0.5 §3.5 / A04 ("sales estimates ... cannot replace it")
   for exactly that case; FWD-5 still holds because the basis travels with the value.

## Measured at the word (workbook item 01L6LHKFXVVTRR73M6KZGIHM4FY2ATNK4U, read 14:1xZ)

15 columns now (RIA inserted at D). 16 rows; RIA = 49 Financial on 13 rows, Cottonwood on 2 (rows 12, 13), blank on
row 16. Rows 12-15 now carry Inception/Last Trade 9/28/2026 with Traded = No.

## Not authorized by this word

PROD portal promotion; any vendor egress beyond the Gateway's own M365 read under the named identity; the never-widen
sign-off itself (still CTO + COO halves); moving or deleting any served key.
