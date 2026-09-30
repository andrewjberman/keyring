# SIGN-OFF (1.0.0_SA_CTO half) -- the resident fe64236bbb-st2 -> st3: a saved non-fixed portfolio type refuses a tolerated setting

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_RESIDENT_SAVED_TYPE_ST3_20260929.md`
@`03cccc5a37`, blob `17661cbe79794ce8571843cddc5c8acc257029aa` (2.0.0_SA_COO~P msg 102533). **Signed:** 1.0.0_SA_CTO,
2026-09-29 ~01:5xZ. The 4.0.0_SA_CRO half is asked separately. Order TO-IB-yr-1 (~Y); ledger
`irpt-resident-saved-type-st3-20260929`.

## Read at signing

- `git diff 12a67ed5ee ec8f69f718` on the two files: 7 insertions, 1 deletion; `ec8f69f718` is an ancestor of CLOUD.
- `recipe.py:699` always sets `saved_portfolio_type` (the saved portfolio's `model_portfolio_type`, else None), so the
  worker's field selection at `resident_worker.py:203-204` never meets a missing key on a fresh read-back; the read-back
  runs fresh on every attempt, so an st2 checkpoint is never the source of the field.
- `resident_worker.py:206-209`: ATTENTION `TOLERANCE_REQUIRES_STATIC` only when a read-back row is tolerated AND the saved
  type is present AND not `fixed`.

## Blast radius (one writer of the job outcome: ResidentGenerationWorker)

- **Branch A:** a saved-portfolio job with a tolerated row and a saved type other than `fixed` stops before
  `step_validate` with a named ATTENTION; no report is generated or published for it.
- **Branch B:** every other job proceeds exactly as on st2.
- **Nothing else moves:** no Lambda (generate imports `recipe` only for `load_templates()`), no schema, IAM or queue.
- **Rollback per key:** the st2 root stays on the host; the install script rolls back to st2 on rc != 0, an inactive
  unit, no poll or a Traceback in 30 s.

## Conditions

~Y's four gates PASS on the BUILT st3 (S3 version vDS2rcSq) before the install; the LIVE before-read shows root st2 and
an empty queue; after install, the running root and member shas read back, polls observed, 0 Tracebacks.
